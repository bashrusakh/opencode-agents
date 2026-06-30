<div align="center">

> v28.15 cleans permissions, command names, duplicate review/plan commands, and stale snippets.

# OpenCode Agent Pack v28.15

### Model-agnostic agents · Startup blocks · OCR review · Clean PR branches · Persistent planning · Readable output

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Startup Block](https://img.shields.io/badge/Startup--Block-On-7c3aed?style=for-the-badge)](#)
[![OCR Review](https://img.shields.io/badge/OCR--Review-Preferred-0f766e?style=for-the-badge)](#)
[![Clean PR Branches](https://img.shields.io/badge/Clean--PR--Branches-On-f97316?style=for-the-badge)](#)

</div>

---

## What's new in v28.15

- Permissions now follow default-allow style with only role-incompatible tools disabled.
- Commands stay minimal: `description`, `agent`, and `subtask: false`; no command-level permission sandbox.
- Built-in/base agents `build`, `explore`, `general`, and `plan` are preserved unchanged by name.
- Duplicate plan/review commands were folded into `/plan` and `/review`.
- Custom agent/command names were shortened and made consistent.
- The stale command JSONC snippet was removed; `commands/*.md` is the single command source of truth.

---

## What this is

This is an opinionated **OpenCode / OpenChamber agent configuration pack** for real project work: bugfixing, UI work, PR follow-up, code review, release prep, project audits, long investigations, and multi-agent workflows.

Core rule:

> Understand the request by meaning, preserve user/project contracts, keep long work in files, prove branch safety before publication, and write human-readable output.

---

## Highlights

| Area | What this pack enforces |
|---|---|
| Model agnostic | Agents do not contain provider-specific `model:` overrides. They use the active OpenCode/OpenChamber model. |
| Semantic routing | Route by normalized intent, scope, target, action level, confidence, and evidence — not magic trigger phrases. |
| Startup block | Before tools, emit a compact Markdown block with route, mode, summary, scope, gated status, and next action. |
| Behavioral contracts | Before user-facing changes, preserve the natural user action/value source instead of exposing raw internals. |
| Right-level fixes | Fix the shared helper/service/composable/API wrapper when the bug belongs there, not only the first call site. |
| Gated actions | Commits, pushes, PRs, releases, deps, secrets, destructive commands, runtime config, and broad product/architecture choices require approval. |
| Git sync before mutation | The active primary/orchestrator handles base-branch sync before mutation/publication work; leaf subagents are not forced to fetch before inspection. |
| PR branch provenance | Before commit/push/PR/update, agents prove the branch contains only intended commits/files. |
| OCR review | Alibaba `open-code-review` is the preferred backend for code/diff/PR review when installed and allowed. |
| Persistent planning | Long-running/multi-agent work uses durable `plans/<plan>/` artifacts. |
| Readable output | User replies, PR comments, issues, releases, changelogs, reviews, and handovers must be concise, skimmable Markdown/plain text. |

---

## Startup block before tools

Every multi-step, repository, issue/PR/release, external-URL, codebase, mutation-capable, publication-capable, or scope-expanding workflow must start with this visible Markdown block **before the first tool call**:

```md
### Startup
- Route: `<route>`
- Mode: `<read-only | options | edit-capable | gated>`
- Summary: <one sentence>
- Scope: <target + boundary>
- Gated: `<no | yes>` — <reason>
- Next: <next action/tool>
```

Rules:

- Use Markdown, not a prose paragraph.
- Keep field names in English.
- Keep it short: heading + six bullets.
- For read-only work: `Gated: no — read-only`.
- Put the scope boundary in `Scope` before broad discovery.
- Do not use tools before this block except for a trivial single-step answer that needs no tools.

---

## Git and PR safety

### Pre-edit sync gate

Before changing code/config/docs in a repository, the active primary/orchestrator must check the branch and fetch the base branch.

Required intent:

```text
Know the current branch, base branch, working tree state, and whether the branch is stale before editing.
```

If the branch is stale, agents must update/rebase before edits when safe. If the update would rewrite a published branch, pull unrelated commits, create conflicts, or violate project rules, they must stop and ask.

### PR branch provenance gate

A PR is the entire base-to-head comparison, not the last commit.

Before commit, push, PR creation, or PR update, agents must prove that the branch contains only intended commits/files.

Typical checks:

```bash
git status --short
git branch --show-current
git fetch origin <base>
git log --oneline --decorate --left-right --cherry-pick origin/<base>...HEAD
git diff --name-status origin/<base>...HEAD
git diff --stat origin/<base>...HEAD
```

If unrelated commits or files appear, agents must stop. Recovery is a clean branch from `origin/<base>` plus cherry-pick/re-apply only intended work.

Useful file:

```text
docs/GIT_BRANCH_PROVENANCE_POLICY.md
```

Command:

```text
/pr-provenance
```

---

## OCR / Open Code Review integration

Alibaba `open-code-review` is the **preferred backend for code/diff/PR review** when installed and allowed.

Policy:

```text
OCR is the review engine. @reviewer is the policy and judgment layer.
```

The reviewer must:

- emit the Startup block before tools;
- normalize review target and scope;
- check privacy/gated status because OCR may send code/diffs/context to the configured LLM provider;
- run OCR with `--audience agent` and useful `--background` context when allowed;
- filter false positives and low-value nits;
- add right-level, behavioral-contract, tests, and risky API/schema/config judgment;
- never auto-apply fixes for review-only requests.

Useful files:

```text
docs/OCR_REVIEW_POLICY.md
commands/review.md
agents/reviewer.md
snippet/open-code-review-usage.md
```

---

## Core philosophy

### Route by meaning, not words

Persistent Planning Mode activates when the normalized task is long-running, broad-scope, multi-agent, multi-session, likely to lose useful context, or likely to require phased execution, reviews, handoffs, or resumable state.

Phrases like `full-project inspection`, `broad bug hunt`, `large refactor`, or `project-wide audit` are examples/signals, not trigger phrases.

### Preserve behavioral contracts

A schema type does not define the user experience.

Before changing user-facing behavior, agents must identify:

- what action the user naturally performs;
- who or what provides the value;
- what values are valid and where that domain comes from;
- which existing project pattern handles the same kind of action;
- whether the naive fix exposes raw/internal/manual values.

### Files are memory for long work

For long-running tasks:

> Chat history is not memory. Private reasoning is not memory. Canonical files are memory.

Use `plans/<plan>/` so another model/provider/session can resume from durable artifacts.

### Public output should be readable

No AI wall of text.

Default to target-aware Markdown/plain text:

- short summary first;
- headings only when useful;
- bullets for multiple reasons, risks, files, or checks;
- fenced code blocks for commands, logs, paths, config, or exact proposed text;
- compact tables only when the target renders them well;
- clear conclusion/next action.

For OpenCode CLI, Telegram, Hermes, terminals, and chat relays, prefer compact Markdown/plain text and avoid raw HTML, oversized tables, deeply nested lists, and GitHub-only formatting.

---

## Directory layout

```text
AGENTS.md
agents/
commands/
docs/
install/
snippet/
```

Persistent planning layout inside a target project:

```text
plans/<plan>/
  plan.md
  phases/
    phase-N.md
  implementation/
    phase-N-impl.md
  reviews/
    plan-review.md
    impl-plan-review-phase-N.md
    impl-review-phase-N.md
  todo.md
  handovers/
    session-YYYY-MM-DD.md

docs/
  overview.md
  modules/
  features/
  handovers/
    session-YYYY-MM-DD.md
```

---

## Workflow modes

| Mode | Flow |
|---|---|
| Small/focused work | `normalize -> inspect -> implement if allowed -> verify -> report` |
| User-facing work | `normalize -> inspect -> Behavioral Contract Check -> implement -> verify -> review/report` |
| Long-running work | `Discuss -> /plan -> /review when needed -> /execute-plan -> /review when needed -> /plan update/handover` |

Broad implementation uses:

```text
Blueprint -> Gate -> Execute -> Digest
```

---

## Commands included

| Command | Purpose |
|---|---|
| `/bugfix` | Full bugfix workflow with investigation, fix, verification, and review. |
| `/bug-issue` | Verify a bug report and draft/open a factual issue when requested. |
| `/code-explore` | Explore code and return facts, paths, call paths, and patterns. |
| `/debug` | Reproduce/root-cause/fix a concrete failure or runtime error. |
| `/devops-check` | Inspect Docker/systemd/CI/runtime/deployment state. |
| `/verify` | Run tests, linters, builds, and smoke checks without editing. |
| `/review` | Unified review command for code, PRs, plans, implementation plans, results, and fix-level checks; prefers OCR when installed and allowed. |
| `/pr-followup` | Follow-up work on an existing PR with branch provenance checks. |
| `/pr-provenance` | Read-only proof that the current branch/PR contains only intended commits/files. |
| `/audit` | Broad repository/project audit with persistent planning when scope requires it. |
| `/release-prep` | Release notes and release checks from verified facts only. |
| `/plan` | Create/resume/update/handover persistent plan state and author implementation plans. |
| `/execute-plan` | Execute an approved plan/work package using Blueprint → Gate → Execute → Digest. |
| `/ui-audit` | UI/layout/UX audit. |
| `/ui-options` | UI redesign options without editing. |
| `/ui-plan` | Concrete UI redesign/theme plan. |
| `/ui-redesign` | Full UI redesign workflow. |
| `/ui-implement` | Implement an approved UI plan. |
| `/ui-a11y-check` | Accessibility/keyboard/focus/contrast/responsive check. |
| `/ui-mcp-setup` | UI MCP setup. |
| `/ui-uupm-setup` | UI UX Pro Max / UUPM setup. |


---

## Install

### Global install

```bash
./install/install-global.sh
```

Installs to:

```text
~/.config/opencode/AGENTS.md
~/.config/opencode/agents/
~/.config/opencode/commands/
~/.config/opencode/docs/
~/.config/opencode/snippet/
```

### Project-local install

Run from the repository root:

```bash
/path/to/opencode_model_agnostic_persistent_v28_15/install/install-project.sh
```

Installs to:

```text
./AGENTS.md
./.opencode/agents/
./.opencode/commands/
./.opencode/docs/
./.opencode/snippet/
```

---

## Validation checklist

This pack is expected to validate with:

- expected v28.15 renames/deletions only;
- YAML frontmatter parses for all agents and commands;
- no command has `subtask: true`;
- no command has a `permission:` block;
- no stale deleted command or renamed agent references remain;
- install scripts pass `bash -n`;
- no provider-specific `model:` overrides in agents;
- no stale provider-specific model IDs;
- no plural snippet-directory path references;
- root rules include semantic routing, startup blocks, behavioral contracts, OCR review, branch provenance, persistent planning, and readable public output.

---

## Recommended use

Use this pack when you want agents that can:

- inspect a project for a long time without losing context;
- hand off work between models/providers;
- avoid duplicate fixes across multiple agents;
- preserve UI/product behavior instead of only satisfying schema plumbing;
- use OCR for stronger code/diff/PR review when available;
- keep GitHub/PR/release work safe and evidence-based;
- format GitHub/Telegram/Hermes/OpenCode CLI output cleanly.

---

<div align="center">

**OpenCode Agent Pack v28.15**  
Semantic routing · Top-level commands · Primary orchestrators · OCR review · Clean PR branches · Durable plans

</div>
