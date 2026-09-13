<div align="center">

# OpenCode Agent Pack v28.34

### Model-agnostic routing · strict role boundaries · bounded multi-agent workflows · fresh evidence · clean PR lifecycle

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Semantic Routing](https://img.shields.io/badge/Semantic--Routing-On-7c3aed?style=for-the-badge)](#)
[![OCR Review](https://img.shields.io/badge/OCR--Review-Available-0f766e?style=for-the-badge)](#)
[![Regression Guard](https://img.shields.io/badge/Regression--Guard-On-f97316?style=for-the-badge)](#)

</div>

---

## What changed in v28.34

v28.34 keeps the v28.33 freshness/state-identity/PR-base rules and adds one general right-level-fix safeguard: choose the fix boundary from the required end-to-end outcome, not from the nearest editable component.

- **Outcome-owned fix boundary** — before implementation, define the end-to-end acceptance condition and choose the smallest ownership boundary that can actually guarantee it across materially relevant paths, states, callers, partitions/instances, and lifecycle transitions.
- **Composition check** — a local or per-partition guarantee is not treated as proof of a system-level invariant unless its aggregate/composed behavior is established.
- **Escalate before coding** — if the proposed boundary cannot guarantee the required outcome, move the fix level outward or escalate before mutation rather than accumulating partial local patches.
- **Existing resets and state identity retained** — the v28.30 failed-fix reset plus v28.31-v28.33 freshness, state-identity, and base-drift rules remain unchanged.

**Details:** [CHANGELOG.md](CHANGELOG.md) · [v28.34 release notes](docs/releases/v28.34.md)

---

## What this pack is

An opinionated OpenCode/OpenChamber agent configuration for real project work: focused implementation, bugfixes, UI changes, PR follow-up, review, release preparation, audits, DevOps diagnostics, and resumable multi-agent workflows.

The pack is intentionally **model-agnostic**. It describes behavior, roles, evidence, and workflow boundaries instead of binding agents to a provider-specific model.

> Normalize the requested outcome → route it to the right role → keep work inside the agreed scope → verify the actual result → report only what current evidence proves.

The canonical behavioral contract is [`AGENTS.md`](AGENTS.md). README explains the system; it does not replace that policy.

---

## How the workflow works

### Semantic routing

Routing follows the requested outcome, target, action level, and repository evidence — not magic keywords.

| Request | Typical route |
|---|---|
| “Where is this implemented?” | discovery / `explore` |
| “Fix this runtime bug” | bugfix workflow / `debugger` |
| “Change this known code/config path” | focused implementation / `build` |
| “Review this PR” | `reviewer` |
| “Audit the project” | `auditor` |
| “Redesign these settings” | UI workflow |
| “Why is this service failing?” | `devops` diagnostics |

The same intent should route consistently even when phrased differently or in another language.

### Role boundaries

Roles are capability contracts, not suggestions.

```text
orchestrator
  owns WHAT / SCOPE / NEXT / escalation / publication

specialist
  owns HOW inside the assigned boundary
```

A specialist may choose the commands, files, tests, and implementation details needed inside its assignment. It may not silently widen scope, fix unrelated findings, start the next workflow stage, change PR state, or negotiate a new gate unless that authority was explicitly delegated.

If a specialist is unavailable or fails, its capabilities do **not** transfer to the caller. The workflow either routes to another genuinely capable role or reports the stage as blocked.

### Complexity escalation

Small/local fixes stay small. When repeated findings expose one shared state machine, lifecycle, protocol, concurrency, persistence, ownership, or similar invariant, the workflow stops treating every symptom as a separate patch.

```text
related findings
→ shared invariant/state model
→ bounded work packages
→ targeted verification
→ stable candidate
→ final review
```

File count alone does not trigger this escalation.

### Evidence stays tied to the state it checked

Tests and review verdicts apply to the actual diff/state they inspected. Later changes invalidate only the evidence they can affect.

A narrow passing test proves only that narrow behavior. Server checks do not prove a changed UI boundary; UI checks do not prove persistence or migration behavior.

State identity follows the work: a fresh remote `ref@SHA` must not silently turn into stale-worktree inspection, execution, mutation, testing, or review. Runtime evidence belongs to the workspace state that actually executed it.

### Authorization stays explicit

Public/external, destructive, scope-expanding, and other gated actions still follow the canonical rules in `AGENTS.md`. Already-authorized actions do not require a duplicate confirmation; a materially changed target, scope, destination, or risk does.

---

## PR workflow

For confirmed **owned PRs**, active implementation and final readiness are separate states:

```text
Draft
  ↓ implementation / repair / intermediate CI
local Candidate HEAD
  ↓ final local checks
  ↓ @tester if independent verification is useful/required
  ↓ whole-PR reviewer
push exact reviewed SHA
  ↓ remote SHA identity + CI/status
Ready
```

Key points:

- active owned PR work stays **Draft**;
- intermediate Draft repair pushes do not require the expensive final review after every commit;
- once implementation is complete, the exact **local** final commit becomes the Candidate HEAD;
- final applicable local validation — including one batched `@tester` checkpoint when independent verification is useful/required — and whole-PR `@reviewer` run against that Candidate HEAD **before its final push**;
- the exact reviewed SHA is then pushed unchanged and the remote PR head must match it;
- push alone does not trigger another full review when the SHA is unchanged;
- final `@reviewer` coverage is the complete base-to-local-Candidate-HEAD change, not only the latest patch or current older remote head;
- required failing/blocked checks may coexist with repair work in Draft, but still block Ready/merge/release/completion;
- OCR may assist the reviewer when useful or explicitly required; it is not a universal Ready gate;
- unowned or ambiguous PRs are never automatically switched between Draft and Ready.

Detailed policy: [`docs/pr_readiness.md`](docs/pr_readiness.md) · [`docs/git_branch_provenance_policy.md`](docs/git_branch_provenance_policy.md)

---

## Startup and resumability

For workflows covered by the root Startup rule, the active agent emits one compact context block before normal tool work:

```md
### Startup
- Route: `<route>`
- Mode: `<read-only | options | edit-capable | publication-capable>`
- Summary: <one sentence>
- Scope: <target + boundary>
- Gated: `<no | yes>` — <reason>
- Next: <next action/tool>
```

A later material route/mode/scope change uses a compact `### Update`; Startup is not repeated before every tool call.

### GrayMatter memory

GrayMatter is an **optional external MCP integration** and is not bundled in the archive. When present, it can restore unfinished work and durable project context; repository code/docs/history/tool output remain authoritative over recalled memory.

Upstream: https://github.com/angelnicolasc/graymatter

---

## Review and correctness

### Right-level fixes

Fix behavior at the abstraction that owns it. Do not patch only the first caller when the real fault belongs to a shared helper, service, composable, parser, API wrapper, or stateful primitive.

### Regression guard

For bugfixes and existing/shared behavior changes, verify both:

- the behavior intentionally changed;
- the closest applicable behavior/invariant that must remain unchanged.

Shared or stateful changes should receive proportionally broader verification. Do not weaken tests, snapshots, lint/type rules, or coverage merely to manufacture a PASS.

### Verification cadence

Verification is layered rather than a fixed agent chain:

```text
implementation role -> focused local evidence
meaningful boundary -> @tester when independent verification adds value
stable candidate -> applicable final local validation
                 -> @tester if independent verification is useful/required
                 -> @reviewer
published candidate -> remote CI/status
```

A work package ending does not automatically trigger `@tester`, and reviewer should not repeat a fresh broad test pass. When tester is used, one assignment should cover the complete already-applicable affected boundary.

Policy: [`docs/verification_strategy.md`](docs/verification_strategy.md)

### OCR / Open Code Review

Alibaba `open-code-review` is available as a review backend when installed/configured and external code sharing is allowed.

```text
OCR       = optional review engine
@reviewer = scope / privacy / judgment / final verdict
```

The reviewer decides whether OCR materially helps unless the user/project explicitly requires it. Review-only requests never auto-apply OCR suggestions.

Policy: [`docs/ocr_review_policy.md`](docs/ocr_review_policy.md)

---

## Persistent planning

Persistent planning is for work that genuinely needs durable coordination across broad scope, phases, agents, or sessions — not for every small task.

When repository plan artifacts are authorized:

```text
plans/<plan>/
  plan.md
  phases/phase-N.md
  implementation/phase-N-impl.md
  reviews/*.md
  todo.md
  handovers/session-YYYY-MM-DD.md
```

Read-only audits do not create repository plan files merely to maintain agent state.

Policy: [`docs/persistent_planning_policy.md`](docs/persistent_planning_policy.md)

---

## UI workflow and component intelligence

Existing project components, tokens, and design patterns come first.

When relevant and available, the stack can use:

1. existing project components/styles;
2. official shadcn MCP/default registry;
3. additional shadcn-compatible registries through the official mechanism;
4. optional Jpisnice `shadcn-ui-mcp-server` as a secondary/reference source;
5. manual implementation when no suitable source fits.

UI UX Pro Max (UUPM) is optional design intelligence, **not** a component source and not permission to introduce a new design system.

References: [`docs/ui_component_policy.md`](docs/ui_component_policy.md) · [`docs/ui_mcp_install_for_agent.md`](docs/ui_mcp_install_for_agent.md) · [`docs/uupm_install_for_agent.md`](docs/uupm_install_for_agent.md)

---

## Bundled agents

| Agent | Role |
|---|---|
| `build` | Focused, clearly scoped implementation |
| `code-orchestrator` | Multi-step coding/PR/bug/release coordination; never implements itself |
| `debugger` | Root-cause bugfix implementation |
| `explore` | Read-only codebase discovery/call-path tracing |
| `tester` | Independent verification; never fixes failures |
| `reviewer` | Independent code/diff/PR/plan review |
| `auditor` | Broad read-only project audit orchestrator |
| `plan` | Architecture/persistent planning artifacts; no source implementation |
| `devops` | Runtime/CI/deploy diagnostics and authorized operational changes |
| `general` | Read-only bounded fallback research when no specialist fits |
| `ui-orchestrator` | Coordinated UI workflow; never implements itself |
| `ui-auditor` | Read-only UI/UX audit |
| `ui-planner` | Concrete UI implementation planning |
| `ui-implementer` | Focused UI implementation |
| `a11y-reviewer` | Independent accessibility/interaction review |

No agent file contains a provider-specific `model:` override.

---

## Commands included

Commands are **intent entry points**, not copies of the root policy.

| Command | Purpose |
|---|---|
| `/audit` | Broad read-only project/repository audit |
| `/bug-issue` | Verify a bug and draft/open a factual non-duplicate issue |
| `/bugfix` | Multi-step bugfix coordination |
| `/code-explore` | Read-only codebase exploration |
| `/debug` | Root-cause and fix a confirmed failure |
| `/devops-check` | Runtime/CI/deploy/config diagnostics |
| `/execute-plan` | Execute the current persistent-plan work package |
| `/plan` | Create/resume/update persistent plan state |
| `/pr-followup` | Existing PR comments/checks/fixes/verification/publication follow-up |
| `/pr-provenance` | Read-only base-to-head branch provenance proof |
| `/release-prep` | Grounded release-note/release-state preparation or verification |
| `/review` | Independent review; OCR available when useful/allowed |
| `/ui-a11y-check` | Accessibility/interaction review |
| `/ui-audit` | UI/UX audit |
| `/ui-implement` | Implement an understood UI change/accepted plan |
| `/ui-mcp-setup` | Configure supported UI MCP stack |
| `/ui-options` | Produce grounded UI directions without implementation |
| `/ui-plan` | Concrete implementable UI plan |
| `/ui-redesign` | Coordinate a complete UI redesign workflow by semantic need |
| `/ui-uupm-setup` | Configure UUPM for OpenCode |
| `/verify` | Independent tests/lint/build/smoke verification |

---

## Bundled skills and external integrations

Bundled skills:

```text
api-designer        cpp-pro              golang-pro
open-code-review    playwright-expert    python-pro
react-expert        rust-engineer        secure-code-guardian
typescript-pro      ui-ux-pro-max        vue-expert
```

Skills are advisory and selected from actual project context. A matching skill must be loaded/read before claiming it was used.

Upstream / external sources:

- GrayMatter persistent memory: https://github.com/angelnicolasc/graymatter
- Alibaba `open-code-review`: https://github.com/alibaba/open-code-review
- Jeffallan `claude-skills`: https://github.com/Jeffallan/claude-skills
- UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

---

## Install

### Global

```bash
./install/install-global.sh
```

Installs under `~/.config/opencode/` (`AGENTS.md`, agents, commands, docs, skills, snippets).

### Project-local

From the target repository root:

```bash
/path/to/opencode_model_agnostic_persistent_v28_34/install/install-project.sh
```

Installs `AGENTS.md` plus `.opencode/{agents,commands,docs,skills,snippet}/` into the project.

---

## Documentation map

| Document | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Canonical behavioral/workflow policy |
| [`CHANGELOG.md`](CHANGELOG.md) | Release-by-release summary |
| [`docs/releases/v28.34.md`](docs/releases/v28.34.md) | v28.34 outcome-owned fix-boundary safeguard |
| [`docs/releases/v28.33.md`](docs/releases/v28.33.md) | v28.33 PR base-drift / `Base SHA + Candidate HEAD` handling |
| [`docs/releases/v28.32.md`](docs/releases/v28.32.md) | v28.32 state-identity chain and direct-entry freshness |
| [`docs/releases/v28.31.md`](docs/releases/v28.31.md) | v28.31 current-state freshness changes |
| [`docs/releases/v28.30.md`](docs/releases/v28.30.md) | v28.30 workflow-hygiene changes |
| [`docs/releases/v28.29.md`](docs/releases/v28.29.md) | v28.29 verification-cadence changes |
| [`docs/releases/v28.28.md`](docs/releases/v28.28.md) | v28.28 orchestration / PR lifecycle changes |
| [`docs/verification_strategy.md`](docs/verification_strategy.md) | Verification layers, tester cadence, and batching |
| [`docs/pr_readiness.md`](docs/pr_readiness.md) | Draft / Candidate HEAD / Ready lifecycle |
| [`docs/git_branch_provenance_policy.md`](docs/git_branch_provenance_policy.md) | Branch/base/head provenance and current-upstream freshness |
| [`docs/ocr_review_policy.md`](docs/ocr_review_policy.md) | Reviewer/OCR policy |
| [`docs/persistent_planning_policy.md`](docs/persistent_planning_policy.md) | Durable planning lifecycle |
| [`docs/ui_component_policy.md`](docs/ui_component_policy.md) | UI component/source policy |
| [`docs/output_formatting_policy.md`](docs/output_formatting_policy.md) | User-facing output formatting |

---

## Release validation

A release archive should verify at least:

- 15 agents and 21 commands;
- valid YAML frontmatter for every agent/command;
- no provider-specific agent or command model overrides;
- all commands keep `subtask: false` and no command-level permission overrides;
- no stale universal `origin/main`, outdated OCR timeout contract, or obsolete version-path references;
- install scripts pass `bash -n` and copy complete skill directories;
- vendored/upstream skill content is not silently replaced by package-authored wrappers;
- archive roundtrip manifest matches the working tree.

---

<div align="center">

**OpenCode Agent Pack v28.34**  
Semantic routing · bounded orchestration · fresh evidence · clean PRs

</div>
