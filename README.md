<div align="center">

# OpenCode Agent Pack v28.5

### Model-agnostic agents · Behavioral-contract fixes · Persistent planning for long AI workflows

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Persistent Planning](https://img.shields.io/badge/Persistent--Planning-v28.5-16a34a?style=for-the-badge)](#)
[![Workflow Safety](https://img.shields.io/badge/Gated--Actions-On-f97316?style=for-the-badge)](#)

</div>

---

## What is this?

This is an opinionated **OpenCode / OpenChamber agent configuration pack** for real project work: bugfixing, UI work, PR follow-up, release prep, full-project audits, long-running investigations, and multi-agent workflows.

It is built around one rule:

> **The agent should understand the requested outcome and preserve project/user contracts — not blindly match phrases, schema fields, or provider-specific models.**

Version **v28.5** is based on `opencode_model_agnostic_persistent_v28_4.zip` and adds the final wording pass for semantic routing philosophy plus a GitHub-ready README.

---

## Highlights

| Area | What this pack enforces |
|---|---|
| ✅ Model agnostic | Agents do not contain provider-specific `model:` overrides. Use the active OpenCode/OpenChamber model. |
| ✅ Semantic routing | Route by normalized intent, scope, target, action level, confidence, and evidence — not magic trigger phrases. |
| ✅ Behavioral Contract Check | Before user-facing changes, preserve the natural user action/value source instead of exposing raw internals. |
| ✅ Right-level fixes | Do not patch only the first call site when the bug belongs in a shared helper/service/composable/API wrapper. |
| ✅ Gated actions | Commits, PRs, releases, deps, secrets, destructive commands, runtime config, and broad product/architecture choices require explicit approval. |
| ✅ Persistent planning | Long-running/multi-agent work uses durable `plans/<plan>/` artifacts so another agent can resume without starting over. |
| ✅ UI/MCP/UUPM policy | External UI sources and component registries are constrained by project patterns and gates. |
| ✅ GitHub/release discipline | No placeholder releases, no invented release notes, no hidden failing checks. |

---

## Why v28.5 exists

Earlier agent packs handled short tasks well, but long workflows had predictable failure modes:

- 🔌 connection drops and the agent forgets what it did;
- 🧠 a new model starts from zero;
- 🗂️ multiple agents create random Markdown reports with different names;
- 🧩 agents duplicate the same bugfix because they cannot see each other's state;
- 🧱 a technically valid fix changes the user-facing behavior.

v28.5 fixes this by combining:

1. **semantic request normalization**;
2. **behavioral contract preservation**;
3. **file-based persistent planning**;
4. **compact subagent digests instead of chat-only memory**.

---

## Core philosophy

### Route by meaning, not words

Persistent Planning Mode is activated when the normalized task is:

- long-running;
- broad-scope;
- multi-agent;
- multi-session;
- likely to lose useful context if kept only in chat;
- likely to require phased execution, reviews, handoffs, or resumable state.

Phrases like `full-project inspection`, `broad bug hunt`, `large refactor`, or `project-wide audit` are **examples**, not trigger phrases.

### Preserve behavioral contracts

A schema type does not define the user experience.

For example, a config value may be a string internally, but the user action might be choosing from provider/model capabilities, not typing raw internal strings. The agent must first identify:

- what action the user naturally performs;
- who or what provides the value;
- what values are valid;
- which existing project pattern handles the same kind of action;
- whether a naive implementation exposes raw/internal/manual values.

### Files are memory for long work

For long-running tasks:

> **Chat history is not memory. Private reasoning is not memory. Canonical files are memory.**

Use `plans/<plan>/` so any model can resume work from durable artifacts.

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

## Workflow modes

### Small / focused work

Use the normal fast path:

```text
normalize -> inspect -> implement if allowed -> verify -> report
```

### User-facing work

Add the behavioral layer:

```text
normalize -> inspect -> Behavioral Contract Check -> implement -> verify -> review/report
```

### Long-running work

Use persistent planning:

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

## Commands included

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
/path/to/opencode_model_agnostic_persistent_v28_5/install/install-project.sh
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

## Safety checklist

This pack is expected to validate with:

- ✅ no missing files from the v28.4 base;
- ✅ only intentional README/philosophy wording changes;
- ✅ YAML frontmatter parses for all agents and commands;
- ✅ JSONC snippets parse;
- ✅ install scripts pass `bash -n`;
- ✅ no provider-specific `model:` overrides in agents;
- ✅ no stale provider-specific model IDs;
- ✅ no stale model route references;
- ✅ no plural snippet-directory path references.

---

## Recommended use

Use this pack when you want agents that can:

- inspect a project for a long time without losing context;
- hand off work between models/providers;
- avoid duplicate fixes across multiple agents;
- preserve UI/product behavior instead of only satisfying schema plumbing;
- keep GitHub/PR/release work safe and evidence-based.

---

<div align="center">

**OpenCode Agent Pack v28.5**  
Semantic routing · Durable plans · Contract-preserving fixes

</div>
