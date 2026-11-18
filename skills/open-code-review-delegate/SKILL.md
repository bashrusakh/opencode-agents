---
name: open-code-review-delegate
description: >
  Deterministic preflight for code review using Alibaba Open Code Review delegation mode.
  OCR selects/filter files and resolves per-file review rules without calling an OCR-side
  LLM; the host reviewer performs the actual review with its own model and tools.
license: Apache-2.0
compatibility: >
  Requires the `ocr` CLI. Delegation mode does not require an OCR LLM provider or API key.
metadata:
  author: alibaba / package integration
  homepage: https://github.com/alibaba/open-code-review
  version: "1.0.0"
---

# Open Code Review — Delegation Preflight

Use delegation mode to make code-review scope and rule resolution deterministic while leaving review reasoning to the host agent. This skill does not grant mutation authority and does not replace the active `AGENTS.md`, reviewer role, project rules, target-identity rules, or publication gates.

Do not require `ocr llm test` or any OCR-side provider credentials for delegation mode.

## Step 1 — Resolve the exact review target and run preview

The caller/reviewer owns target identity. Resolve the authoritative workspace/range/commit and, when applicable, the current Base SHA + Candidate HEAD before treating delegation output as review evidence.

Invoke the appropriate preview command directly; do not spend a separate tool call on `which ocr`, `command -v ocr`, or `--help` probes. The preview invocation itself establishes whether the CLI/subcommand is available and returns the actual target scope. If it fails because the command or delegate subcommand is unavailable, record that exact failure and follow the active reviewer contract's unavailable-delegate handling. Do not claim that delegate preflight completed, and do not install/upgrade OCR unless separately authorized under the active workflow's user-approval gate for new tooling.

Use the matching preview mode:

```bash
# workspace
ocr delegate preview --format json

# range / branch comparison; --to is optional and defaults to HEAD
ocr delegate preview --from <from> --format json
ocr delegate preview --from <from> --to <to> --format json

# single commit
ocr delegate preview --commit <commit> --format json
```

With `--from` and no `--to`, the target defaults to `HEAD`. Range mode compares the merge-base to the target commit and excludes staged, unstaged, and untracked workspace changes. Range and commit modes are mutually exclusive; omit range/commit flags for workspace mode.

Useful shared flags include `--repo`, `--rule`, `--exclude`, `--background`, and `--background-file` when supported by the installed CLI.

### Structured-output compatibility

The `--format` flag is available in OCR v1.9.0 and later. Prefer `--format json` for agent parsing. If a `preview` or `rule` command fails specifically with `unknown flag: --format`, retry that same command without `--format` and use text output for the remainder of the affected delegation run. Preserve explicit mode, refs, file paths/statuses, and rule information from the text output; do not parse text as JSON or invent schema fields. Do not retry without the flag for any other error: report it and stop the affected operation.

The host reviewer can consume equivalent text output. Programmatic integrations that require `schema_version` or other JSON fields must require a JSON-capable CLI instead; check `ocr --version` and request an authorized upgrade when needed.

### Background-context limits and safe argument handling

`--background-file` has two independent limits: the raw file must not exceed 1 MiB, and the sanitized content must not exceed 8000 characters. Either limit aborts the command. Never silently truncate the original context. If it is oversized:

1. Create a faithful task-specific summary that preserves requirements, constraints, acceptance criteria, and other review-critical details.
2. Ensure any replacement background file is within both limits, or pass the summary through `--background` as one correctly escaped shell argument. Prefer argument-array APIs when available; otherwise use the shell's proper argument-quoting mechanism. Do not interpolate untrusted summary text directly into a double-quoted shell template: `$()`, backticks, quotes, and variable references can still be evaluated.
3. Omit the original oversized `--background-file` so OCR does not reload it and fail again.
4. If a faithful summary is impossible, omit OCR background and let the host reviewer read the original context directly.

## Step 2 — Build and reconcile the scope ledger

Preview should provide the review mode/ref metadata, reviewable file entries, and excluded entries/reasons.

Create a ledger for every previewed entry. Use `(path, status)` as the identity rather than path alone because workspace state can contain distinct entries for the same path (for example a staged deletion plus an untracked recreation).

Delegation output is deterministic scaffolding, not the authority for the requested target. Reconcile it with the reviewer's authoritative changed-file/effective-diff set:

- every authoritative changed entry must be explained by a reviewable or excluded delegate entry, or explicitly added to the host review when OCR filtering does not cover it;
- every delegate entry must belong to the requested target/state;
- excluded files must remain visible in the ledger with their reason; exclusion is not automatic permission to ignore behaviorally relevant config/generated/schema/metadata changes;
- an unexplained scope mismatch blocks a full-coverage claim until resolved.

## Step 3 — Resolve rules for reviewable files

Pass the reviewable paths to the rule subcommand. It must use the same target-selection flags as the preview so rules are resolved against the same target/state:

```bash
# Workspace mode
ocr delegate rule --format json <path1> <path2> ...

# Range mode: repeat the exact --from/--to selection from preview
ocr delegate rule --from <from> --format json <path1> <path2> ...
ocr delegate rule --from <from> --to <to> --format json <path1> <path2> ...

# Commit mode: repeat the exact commit selection from preview
ocr delegate rule --commit <commit> --format json <path1> <path2> ...
```

When `--from` was supplied without `--to` in preview, pass the same `--from` without `--to` to `rule`; both subcommands default the target to `HEAD`. Repeat an explicit `--repo` as well, so rule resolution uses the same repository as preview. Apply the exact `--format` compatibility fallback from Step 1 if the installed CLI rejects that flag.

For large sets, resolve rules in bounded batches. OCR groups files that share the same rule content; preserve that grouping to avoid repeating the same checklist. If preview scope is already trustworthy but rule resolution fails, the host review may continue with higher-priority root/scoped project rules while recording `Delegate rules: partial/unavailable`; never invent missing OCR rules.

OCR-resolved rules are review guidance. They do not override higher-priority user requirements, root/scoped `AGENTS.md`, project guidance, reviewer policy, or explicit acceptance criteria.

## Step 4 — Read the actual diff/content

Use preview mode/ref metadata to obtain the exact changed content.

Use `git --no-pager` for every Git invocation in this review. Disable external diff programs, text conversion, and color so the inspected patch is deterministic. Put paths after `--` and quote every dynamic ref/path as one shell argument; use argument-array APIs where available rather than constructing shell commands by string concatenation.

**Range mode** (use the previewed merge base when provided):

```bash
git --no-pager diff --no-ext-diff --no-textconv --no-color \
  "$merge_base..$to" -- "$path"
```

**Commit mode**:

```bash
git --no-pager show --no-ext-diff --no-textconv --no-color \
  "$commit" -- "$path"
```

**Workspace mode**:

```bash
# tracked/staged/unstaged content relative to HEAD
git --no-pager diff --no-ext-diff --no-textconv --no-color \
  HEAD -- "$path"

# untracked entry (read the complete file directly)
cat -- "$path"
```

For context, use similarly bounded and quoted commands:

```bash
git --no-pager log --no-color --oneline -- "$path"
git --no-pager blame --no-textconv -- "$path"
git --no-pager show --no-ext-diff --no-textconv --no-color "$ref:$path"
```

For large diffs, write output to a unique absolute temporary file outside the repository. Create its parent directory first and ensure the chosen path does not overwrite an existing file. Add `--output="$diff_file"` to the selected mode's Git command, for example:

```bash
git --no-pager diff --no-ext-diff --no-textconv --no-color \
  --output="$diff_file" "$merge_base..$to" -- "$path"
```

After Git exits successfully, read the entire file in bounded chunks; do not inspect only its beginning or end. Remove the temporary file after review. If Git fails or times out, retry where safe or mark that ledger entry `skipped` with the concrete error. If the output is unexpectedly empty, run a fresh delegate preview and reconcile the result before treating the file as having no diff.

For workspace-untracked entries, read the complete file directly with `cat -- "$path"`; do not use `git diff` for content that Git has not tracked.

Read surrounding code/tests/config/history only as needed to judge the change and its affected invariant. Do not substitute a different checkout/state for a target-bound review.

## Step 5 — Host reviewer performs the review

For every reviewable ledger entry:

- inspect the exact diff/content;
- apply its resolved rule group plus higher-priority project/user/reviewer constraints;
- inspect the nearest meaningful context needed for correctness, security, regression, right-level ownership, and affected state/lifecycle/protocol invariants;
- mark it `reviewed`, or `skipped` with a concrete defensible reason.

For large changes, process bounded batches while preserving one complete ledger. Do not stop after the first severe finding.

This delegation preflight does **not** call an OCR-side LLM. A later managed `ocr review` is a separate optional/required independent-review step governed by the active reviewer policy.

## Step 6 — Coverage and report

Before a complete verdict, reconcile the ledger against the authoritative target and report at least:

- `total_entries`;
- `reviewed_entries`;
- `skipped_entries` with reasons;
- `coverage_rate`;
- any delegate/authoritative-scope mismatch;
- delegate mode/ref/merge-base identity when relevant.

A full-coverage verdict requires every authoritative changed entry to be accounted for, not merely every item that OCR chose as reviewable.

Findings should prioritize material correctness/security/data-loss/regression issues. Report medium findings when useful; suppress low-value style/nit findings and likely false positives.

## Current command boundary

The documented delegation CLI used by this skill is:

```text
ocr delegate preview [--from <ref> [--to <ref>] | --commit <hash>]
ocr delegate rule [--from <ref> [--to <ref>] | --commit <hash>] <paths...>
```

Do not assume an aggregate `ocr delegate task` command exists unless the installed CLI's help explicitly exposes it. The `--to` default and target flags must be kept identical between preview and rule.
