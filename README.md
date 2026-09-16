<div align="center">

# OpenCode Agent Pack v28.38

### Model-agnostic routing · strict role boundaries · bounded multi-agent workflows · fresh evidence · clean PR lifecycle

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Semantic Routing](https://img.shields.io/badge/Semantic--Routing-On-7c3aed?style=for-the-badge)](#)
[![OCR Review](https://img.shields.io/badge/OCR--Review-Available-0f766e?style=for-the-badge)](#)
[![Regression Guard](https://img.shields.io/badge/Regression--Guard-On-f97316?style=for-the-badge)](#)

</div>

---

## What changed in v28.38

v28.38 hardens **claim authority** before semantic correspondence. Referenced issues, PRs, plans, comments, tests, docs, and task assignments can contain real requirements, evidence, and hypotheses side by side; the container no longer grants every statement the same authority.

- **Per-claim authority** — material requirements are normalized from current user intent and project-local authoritative rules, not inferred from the artifact or heading that contains them.
- **Explicit elevation stays possible** — a current instruction or authoritative project rule may make an entire referenced artifact, or selected parts of it, normative.
- **Authority is not truth** — system evidence can support or refute a claim, but cannot by itself make that claim a requirement; reviewer checks these questions separately.
- **Issue/report safety** — issue-derived bugfixes use the report as context/evidence while independently establishing which claims actually define the desired outcome.
- **Semantic correspondence remains downstream** — only after the contract is normalized does review ask whether implementation evidence justifies the semantic conclusion.

**Details:** [CHANGELOG.md](CHANGELOG.md) · [v28.38 release notes](docs/releases/v28.38.md)

---

## What changed in v28.37

v28.37 refines the v28.36 premise-validation work into one more general rule: **semantic correspondence**. The pack no longer enumerates classes of risky mechanisms; it asks whether the technical evidence being used actually represents the semantic property the workflow claims to prove.

- **Semantic property first** — acceptance and review claims are stated as outcomes/invariants before implementation details are used as evidence.
- **Evidence correspondence** — implementation facts and test evidence count only when their correspondence to the claimed semantics is established.
- **Inference check** — reviewers prove the direction of inference actually being used and look for ordinary valid behavior where the same technical evidence would not justify the claimed semantic conclusion.
- **Generic verification fidelity** — a test result proves only the production conclusion that its setup and observation actually support; no case taxonomy is required.
- **Cleaner handoffs** — orchestrator/planner keep implementation proxies as hypotheses rather than silently promoting them into acceptance criteria.

**Details:** [CHANGELOG.md](CHANGELOG.md) · [v28.37 release notes](docs/releases/v28.37.md)

---

## What changed in v28.36

v28.36 closes a semantic-review gap where one unproven implementation premise could be repeated by an assignment, implementation, comments, tests, and reviewer and thereby look independently validated.

- **Contract provenance** — authoritative outcome/invariant evidence is separated from caller-derived implementation hypotheses.
- **Premise tracing** — materially correctness-critical guards/state transitions must be traced into production producers/consumers and challenged by reasoning through an ordinary valid transition that could falsify the assumption.
- **Semantic-proof coverage** — full changed-file coverage no longer substitutes for reading unchanged adjacent code when correctness depends on it.
- **Harness fidelity** — lifecycle/identity/order/ownership/timing-sensitive tests prove production behavior only when their fixtures/mocks preserve the governing production semantic.
- **Cleaner handoffs** — orchestrator/planner do not promote speculative mechanisms into acceptance criteria merely because an earlier stage proposed them.

**Details:** [CHANGELOG.md](CHANGELOG.md) · [v28.36 release notes](docs/releases/v28.36.md)

---

## What changed in v28.35

v28.35 keeps v28.34 right-level fix-boundary safeguards and changes code-review execution so deterministic OCR delegation runs before reviewer reasoning when available, while expensive managed `ocr review` becomes an explicit confidence escalation rather than the default first backend.

- **Delegate-first review preflight** — `ocr delegate preview` + `ocr delegate rule` provide file selection/exclusions/ref metadata and per-file review rules without an OCR-side LLM.
- **Authoritative scope reconciliation** — delegate output is checked against the actual workspace/range or Base SHA + Candidate HEAD changed set; excluded files cannot disappear silently.
- **Host reviewer owns the full pass** — `@reviewer` reviews every accounted changed entry with its own model and reports explicit coverage.
- **Managed OCR is second opinion** — `ocr review` runs only when explicitly required or when an independent model pass materially improves confidence; quota/provider failure no longer destroys a complete host review unless managed OCR was mandatory.
- **Current OCR skills** — the bundled normal OCR skill is updated from the supplied current CLI contract, and a separate `open-code-review-delegate` skill is added.

**Details:** [CHANGELOG.md](CHANGELOG.md) · [v28.35 release notes](docs/releases/v28.35.md) · [OCR policy](docs/ocr_review_policy.md)

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
- OCR delegate preflight prepares deterministic scope/rules when available; managed OCR may add a second-model pass when useful/required and is not a universal Ready gate;
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

Alibaba `open-code-review` is integrated in two layers for code-like review:

```text
OCR delegate = deterministic local scope / exclusions / rule preflight (no OCR-side LLM)
@reviewer    = complete host-model review / coverage / judgment / final verdict
OCR managed  = optional or required independent second-model escalation
```

When compatible delegation is installed, reviewer uses it before reasoning and reconciles its output against the authoritative changed set. Managed `ocr review` is not the default first step; it runs only when explicitly required or when it materially improves confidence. Review-only requests never auto-apply OCR suggestions.

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
| `/review` | Independent review; delegate preflight when available, managed OCR when useful/required |
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
open-code-review    open-code-review-delegate
playwright-expert    python-pro
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
/path/to/opencode_model_agnostic_persistent_v28_38/install/install-project.sh
```

Installs `AGENTS.md` plus `.opencode/{agents,commands,docs,skills,snippet}/` into the project.

---

## Documentation map

| Document | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Canonical behavioral/workflow policy |
| [`CHANGELOG.md`](CHANGELOG.md) | Release-by-release summary |
| [`docs/releases/v28.38.md`](docs/releases/v28.38.md) | v28.38 per-claim authority/provenance normalization |
| [`docs/releases/v28.37.md`](docs/releases/v28.37.md) | v28.37 semantic-correspondence refinement |
| [`docs/releases/v28.36.md`](docs/releases/v28.36.md) | v28.36 contract provenance / premise-validation hardening |
| [`docs/releases/v28.35.md`](docs/releases/v28.35.md) | v28.35 delegate-first reviewer/OCR execution |
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

**OpenCode Agent Pack v28.38**  
Semantic routing · bounded orchestration · fresh evidence · clean PRs

</div>
