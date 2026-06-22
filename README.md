<div align="center">

# OpenCode Agent Pack v28.7

### Model-agnostic agents · Startup checkpoints · Behavioral contracts · Persistent planning · Readable public output

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Persistent Planning](https://img.shields.io/badge/Persistent--Planning-On-16a34a?style=for-the-badge)](#)
[![Readable Output](https://img.shields.io/badge/Readable--Markdown-On-7c3aed?style=for-the-badge)](#)
[![Workflow Safety](https://img.shields.io/badge/Gated--Actions-On-f97316?style=for-the-badge)](#)

</div>

---

## ✨ What is this?

This is an opinionated **OpenCode / OpenChamber agent configuration pack** for real project work: bugfixing, UI work, PR follow-up, release prep, project audits, long investigations, and multi-agent workflows.

It is built around four rules:

> **Understand the request by meaning, preserve user/project contracts, keep long work in files, and write human-readable output.**

Version **v28.7** is based on `opencode_model_agnostic_persistent_v28_6.zip` and adds a mandatory **startup checkpoint before the first tool call** for multi-step, repository, issue/PR/release, external-URL, codebase, mutation-capable, publication-capable, or scope-expanding workflows.

---

## 🚀 Highlights

| Area | What this pack enforces |
|---|---|
| ✅ Model agnostic | Agents do not contain provider-specific `model:` overrides. Use the active OpenCode/OpenChamber model. |
| ✅ Semantic routing | Route by normalized intent, scope, target, action level, confidence, and evidence — not magic trigger phrases. |
| ✅ Startup checkpoint | Before tools, summarize route/mode, outcome, target, action level, confidence, gated yes/no, and scope boundary. |
| ✅ Behavioral Contract Check | Before user-facing changes, preserve the natural user action/value source instead of exposing raw internals. |
| ✅ Right-level fixes | Do not patch only the first call site when the bug belongs in a shared helper/service/composable/API wrapper. |
| ✅ Gated actions | Commits, PRs, releases, deps, secrets, destructive commands, runtime config, and broad product/architecture choices require explicit approval. |
| ✅ Persistent planning | Long-running/multi-agent work uses durable `plans/<plan>/` artifacts so another agent can resume without starting over. |
| ✅ Readable public output | User replies, PR comments, issues, releases, changelogs, reviews, and handovers must be clean, skimmable, target-aware Markdown/plain text. |
| ✅ UI/MCP/UUPM policy | External UI sources and component registries are constrained by project patterns and approval gates. |

---

## 🧭 Startup checkpoint before tools

Every multi-step, repository, issue/PR/release, external-URL, codebase, mutation-capable, publication-capable, or scope-expanding workflow must start with a compact visible checkpoint **before the first tool call**:

```text
Startup completed. Route: <route>. Mode: <read-only/options/edit-capable/gated>.

Normalization:
- outcome: ...
- target: ...
- action level: ...
- confidence: ...
- gated: yes/no — why
- scope boundary: ...
```

This is required even for read-only work. If the work is read-only, the agent says `gated: no — read-only`. The checkpoint prevents silent scope drift, broad discovery, and accidental mutation before the agent has summarized the user's request.

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

## 📝 Startup checkpoints + output formatting rules

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

- ✅ no missing files from the v28.5 base;
- ✅ YAML frontmatter parses for all agents and commands;
- ✅ JSONC snippets parse;
- ✅ install scripts pass `bash -n`;
- ✅ no provider-specific `model:` overrides in agents;
- ✅ no stale provider-specific model IDs;
- ✅ no stale model route references;
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

**OpenCode Agent Pack v28.7**  
Semantic routing · Durable plans · Contract-preserving fixes · Readable output

</div>
