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

## Preconditions

Check whether the CLI and delegation subcommands exist. Do not require `ocr llm test` for delegation mode.

```bash
which ocr
ocr delegate preview --help
ocr delegate rule --help
```

If `ocr` or the delegation subcommands are unavailable, report delegation as unavailable and use the active workflow's native review preflight. Do not install/upgrade OCR during ordinary review unless that action is separately authorized.

## Step 1 — Resolve the exact review target first

The caller/reviewer owns target identity. Resolve the authoritative workspace/range/commit and, when applicable, the current Base SHA + Candidate HEAD before treating delegation output as review evidence.

Use the matching preview mode:

```bash
# workspace
ocr delegate preview

# range / branch comparison
ocr delegate preview --from <from> --to <to>

# single commit
ocr delegate preview --commit <commit>
```

Useful shared flags include `--repo`, `--rule`, `--exclude`, `--background`, and `--background-file` when supported by the installed CLI.

### Structured-output compatibility

Probe `--help` before assuming `--format` support. When `--format` is listed, prefer JSON for agent parsing:

```bash
ocr delegate preview --format json ...
```

When the installed CLI does not expose `--format`, use the default text output instead. An `unknown flag: --format` result is a version-capability difference, not a reason to abandon an otherwise working delegate preflight.

Never silently truncate a too-large `--background-file`. If OCR rejects it for size, pass a faithful task-specific summary through `--background`; if a faithful summary would drop material requirements/constraints/acceptance criteria, omit OCR background and let the host reviewer read the source context directly.

## Step 2 — Build and reconcile the scope ledger

Preview should provide the review mode/ref metadata, reviewable file entries, and excluded entries/reasons.

Create a ledger for every previewed entry. Use `(path, status)` as the identity rather than path alone because workspace state can contain distinct entries for the same path (for example a staged deletion plus an untracked recreation).

Delegation output is deterministic scaffolding, not the authority for the requested target. Reconcile it with the reviewer's authoritative changed-file/effective-diff set:

- every authoritative changed entry must be explained by a reviewable or excluded delegate entry, or explicitly added to the host review when OCR filtering does not cover it;
- every delegate entry must belong to the requested target/state;
- excluded files must remain visible in the ledger with their reason; exclusion is not automatic permission to ignore behaviorally relevant config/generated/schema/metadata changes;
- an unexplained scope mismatch blocks a full-coverage claim until resolved.

## Step 3 — Resolve rules for reviewable files

Pass the reviewable paths to the rule subcommand:

```bash
ocr delegate rule <path1> <path2> ...
```

When supported, prefer structured output:

```bash
ocr delegate rule --format json <path1> <path2> ...
```

For large sets, resolve rules in bounded batches. OCR groups files that share the same rule content; preserve that grouping to avoid repeating the same checklist. If preview scope is already trustworthy but rule resolution fails, the host review may continue with higher-priority root/scoped project rules while recording `Delegate rules: partial/unavailable`; never invent missing OCR rules.

OCR-resolved rules are review guidance. They do not override higher-priority user requirements, root/scoped `AGENTS.md`, project guidance, reviewer policy, or explicit acceptance criteria.

## Step 4 — Read the actual diff/content

Use preview mode/ref metadata to obtain the exact changed content.

Range mode (use the previewed merge base when provided):

```bash
git diff <merge_base>..<to> -- <path>
```

Commit mode:

```bash
git show <commit> -- <path>
```

Workspace mode:

```bash
# tracked/staged/unstaged content relative to HEAD
git diff HEAD -- <path>

# untracked entry
cat <path>
```

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

## Managed OCR escalation

Do not call `ocr review` merely because delegation completed. Managed OCR is a separate independent-model escalation for cases where the active reviewer policy says it materially improves confidence or the user/project explicitly requires it.

If managed OCR is attempted and fails because of quota/rate/provider availability, keep the already-completed host review evidence. Treat managed OCR as unavailable for that escalation; it blocks the overall review only when managed OCR itself was explicitly required.

## Current command boundary

The documented delegation CLI used by this skill is:

```text
ocr delegate preview
ocr delegate rule <paths...>
```

Do not assume an aggregate `ocr delegate task` command exists unless the installed CLI's help explicitly exposes it.
