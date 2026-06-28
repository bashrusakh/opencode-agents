<div align="center">

> v28.11 keeps all package instruction text in English.

# OpenCode Agent Pack v28.11

### Model-agnostic agents · Startup blocks · Behavioral contracts · Persistent planning · Readable public output

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Persistent Planning](https://img.shields.io/badge/Persistent--Planning-On-16a34a?style=for-the-badge)](#)
[![Readable Output](https://img.shields.io/badge/Readable--Markdown-On-7c3aed?style=for-the-badge)](#)
[![Workflow Safety](https://img.shields.io/badge/Gated--Actions-On-f97316?style=for-the-badge)](#)
[![Clean PR Branches](https://img.shields.io/badge/Clean--PR--Branches-On-0f766e?style=for-the-badge)](#)

</div>

---


## ✨ What's new in v28.11

- 🚫 Added a hard banner in `AGENTS.md`: **rules cannot be ignored**.
- 🧱 Strengthened output formatting: **no AI wall of text**.
- ✍️ User/public output must be brief, clear, accessible, skimmable, and free of filler.
## ✨ What is this?

This is an opinionated **OpenCode / OpenChamber agent configuration pack** for real project work: bugfixing, UI work, PR follow-up, release prep, project audits, long investigations, and multi-agent workflows.

It is built around four rules:

> **Understand the request by meaning, preserve user/project contracts, keep long work in files, and write human-readable output.**

Version **v28.11** is based on `opencode_model_agnostic_persistent_v28_8.zip` and adds mandatory **Git sync + PR branch provenance** checks so agents do not edit stale branches or publish PRs that contain unrelated commits/files.

---

## 🚀 Highlights

| Area | What this pack enforces |
|---|---|
| ✅ Model agnostic | Agents do not contain provider-specific `model:` overrides. Use the active OpenCode/OpenChamber model. |
| ✅ Semantic routing | Route by normalized intent, scope, target, action level, confidence, and evidence — not magic trigger phrases. |
| ✅ Startup block | Before tools, summarize route/mode, outcome, target, action level, confidence, gated yes/no, and scope boundary. |
| ✅ Behavioral Contract Check | Before user-facing changes, preserve the natural user action/value source instead of exposing raw internals. |
| ✅ Right-level fixes | Do not patch only the first call site when the bug belongs in a shared helper/service/composable/API wrapper. |
| ✅ Gated actions | Commits, PRs, releases, deps, secrets, destructive commands, runtime config, and broad product/architecture choices require explicit approval. |
| ✅ Branch provenance | Before editing, committing, pushing, or opening/updating PRs, agents fetch the base and prove the branch contains only intended commits/files. |
| ✅ Persistent planning | Long-running/multi-agent work uses durable `plans/<plan>/` artifacts so another agent can resume without starting over. |
| ✅ Readable public output | User replies, PR comments, issues, releases, changelogs, reviews, and handovers must be clean, skimmable, target-aware Markdown/plain text. |
| ✅ UI/MCP/UUPM policy | External UI sources and component registries are constrained by project patterns and approval gates. |

---

## 🧭 Startup block before tools

Every multi-step, repository, issue/PR/release, external-URL, codebase, mutation-capable, publication-capable, or scope-expanding workflow must start with a compact visible Markdown block **before the first tool call**.

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
- Keep it short: heading + six bullets.
- Use Markdown, not a dense prose paragraph.
- Keep field names in English.
- For read-only work: `Gated: no — read-only`.
- Put the scope boundary in `Scope` before broad discovery.

This forces semantic normalization first, then tools. It prevents silent scope drift, broad discovery, and accidental mutation before the agent has summarized the user's request.

## 🧠 Core philosophy

### Route by meaning, not words

Persistent Planning Mode is activated when the **normalized task** is long-running, broad-scope, multi-agent, multi-session, likely to lose useful context, or likely to require phased execution, reviews, handoffs, or resumable state.

Phrases like `full-project inspection`, `broad bug hunt`, `large refactor`, or `project-wide audit` are **examples/signals**, not trigger phrases.

### Preserve behavioral contracts

A schema type does not define the user experience.

A value can be stored as a string while the user action is actually choosing from provider/model capabilities, selecting from project state, importing a file, approving a generated result, or confirming a system-derived value.

Before changing user-facing behavior, agents must identify:

- what action the user naturally performs;
- who or what provides the value;
- what values are valid and where that domain comes from;
- which existing project pattern handles the same kind of action;
- whether the naive fix exposes raw/internal/manual values.

### Files are memory for long work

For long-running tasks:

> **Chat history is not memory. Private reasoning is not memory. Canonical files are memory.**

Use `plans/<plan>/` so another model/provider/session can resume from durable artifacts.

### Public output should be readable

A correct answer can still be bad if it is a dense paragraph dumped into a PR comment, issue, release, Telegram message, or OpenCode CLI output.

Default to **target-aware portable Markdown**:

- short summary first;
- headings when there is context/reason/validation/conclusion;
- bullets for multiple reasons, risks, files, or checks;
- fenced code blocks for commands, logs, paths, config, or exact proposed text;
- compact tables only when the target renders them well;
- clear conclusion/next action when closing, deferring, superseding, or approving work.

For **OpenCode CLI, Telegram, Hermes, terminals, and chat relays**, prefer compact Markdown/plain text and avoid raw HTML, oversized tables, deeply nested lists, and GitHub-only formatting.

For **GitHub/GitLab**, use clean Markdown with sections and bullets.

---

## 📁 Directory layout

```text
AGENTS.md
agents/
commands/
docs/
install/
snippet/
```

### Persistent planning layout inside a target project

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

## 🧭 Workflow modes

### Small / focused work

```text
normalize -> inspect -> implement if allowed -> verify -> report
```

### User-facing work

```text
normalize -> inspect -> Behavioral Contract Check -> implement -> verify -> review/report
```

### Long-running work

```text
Discuss
-> Create Plan
-> Review Plan
-> Author Implementation Plan
-> Review Implementation Plan
-> Execute Work Package
-> Review Implementation
-> Update Plan
-> Generate Handover
```

Broad implementation uses:

```text
Blueprint -> Gate -> Execute -> Digest
```

---

## 🧩 Commands included

| Command | Purpose |
|---|---|
| `/create-plan` | Create canonical `plans/<plan>/` artifacts for long-running work. |
| `/resume-plan` | Resume from existing plan/todo/review/handover files. |
| `/update-plan` | Update todo, phase status, decisions, and next action. |
| `/generate-handover` | Produce a durable handoff for the next agent/session. |
| `/author-and-verify-implementation-plan` | Write implementation plan grounded in actual files/symbols. |
| `/review-plan` | Review plan quality before execution. |
| `/review-implementation-plan` | Review feasibility and safety of implementation plan. |
| `/execute-work-package` | Execute approved package using Blueprint → Gate → Execute → Digest. |
| `/review-implementation` | Review result against acceptance criteria. |
| `/project-audit` | Broad project audit with persistent planning when scope requires it. |
| `/bugfix` | Bugfix workflow with right-level and contract checks. |
| `/ui-*` | UI audit/options/plan/implementation/MCP/UUPM workflows. |
| `/verify` | Test/lint/build/smoke verification. |
| `/release-prep` | Release notes and release checks from verified facts only. |

---

## 📝 Startup blocks + output formatting rules

Use readable Markdown/plain text for anything a human will see.

| Target | Preferred format | Avoid |
|---|---|---|
| GitHub/GitLab PRs/issues/releases | Headings, bullets, code fences, compact tables when useful | Wall-of-text comments, vague conclusions |
| OpenCode CLI / terminals | Compact Markdown/plain text, short sections, code fences | Raw HTML, wide tables, deeply nested lists |
| Telegram / Hermes / chat relays | Short summary, bullets, simple Markdown/plain text | GitHub-only formatting, oversized tables |
| Markdown docs/handovers | Clear headings, stable sections, action-oriented bullets | Random ad-hoc report names and unstructured notes |

Minimum shape for public comments:

```md
Short summary.

### Why / Context
- ...
- ...

### Validation / Evidence
- ...

### Conclusion / Next action
...
```

---

## ⚙️ Install

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
/path/to/opencode_model_agnostic_persistent_v28_6/install/install-project.sh
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

## 🛡️ Validation checklist

This pack is expected to validate with:

- ✅ no missing files from the v28.8 base;
- ✅ YAML frontmatter parses for all agents and commands;
- ✅ JSONC snippets parse;
- ✅ install scripts pass `bash -n`;
- ✅ no provider-specific `model:` overrides in agents;
- ✅ no stale provider-specific model IDs;
- ✅ no stale provider-specific model IDs;
- ✅ no plural snippet-directory path references;
- ✅ root rules include semantic routing, behavioral contracts, persistent planning, and readable public output.

---

## ✅ Recommended use

Use this pack when you want agents that can:

- inspect a project for a long time without losing context;
- hand off work between models/providers;
- avoid duplicate fixes across multiple agents;
- preserve UI/product behavior instead of only satisfying schema plumbing;
- format GitHub/Telegram/Hermes/OpenCode CLI output cleanly;
- keep GitHub/PR/release work safe and evidence-based.

---

<div align="center">

**OpenCode Agent Pack v28.11**  
Semantic routing · Durable plans · Contract-preserving fixes · Readable output

</div>


## 🛡️ OCR / Open Code Review integration

This build integrates Alibaba `open-code-review` as the **preferred backend for code/diff/PR review** when it is installed and allowed.

**Policy:** OCR is the review engine; `@reviewer` is the policy and judgment layer.

The reviewer must:

- emit the startup block before tools;
- normalize review target/scope;
- check privacy/gated status before OCR, because OCR may send code/diffs/context to the configured LLM provider;
- run OCR with `--audience agent` and useful `--background` context when allowed;
- filter false positives and low-value nits;
- add right-level, behavioral-contract, tests, and risky API/schema/config judgment;
- never auto-apply fixes for review-only requests.

Useful files:

```text
docs/OCR_REVIEW_POLICY.md
commands/review.md
commands/pr-review.md
agents/reviewer.md
snippet/open-code-review-usage.md
```

## 🧰 Command added in v28.11

- `/pr-provenance-check` — read-only proof that the current branch/PR contains only intended commits/files.
