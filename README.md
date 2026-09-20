<div align="center">

# OpenCode Agent Pack v30.00

### Model-agnostic routing · strict role boundaries · bounded multi-agent workflows · fresh evidence · clean PR lifecycle

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Semantic Routing](https://img.shields.io/badge/Semantic--Routing-On-7c3aed?style=for-the-badge)](#)
[![OCR Review](https://img.shields.io/badge/OCR--Review-Available-0f766e?style=for-the-badge)](#)
[![Regression Guard](https://img.shields.io/badge/Regression--Guard-On-f97316?style=for-the-badge)](#)

</div>

---

## What changed in v30.00

- Reduces the package to deterministic OpenCode runtime surfaces: `AGENTS.md`, `agents/`, and `skills/`.
- Removes package slash-command and snippet layers that duplicated semantic routing or had no runtime activation path.
- Consolidates cross-role policy in root while keeping execution details in their owning roles.
- Keeps `agents/code-orchestrator.md` exactly from v28.42 after testing showed that further role-local deduplication changed routing behavior.
- Preserves upgrade safety: installers prune only known package-owned legacy files and leave unrelated user/project files alone.

See [`docs/releases/v30.00.md`](docs/releases/v30.00.md).

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
| “Implement this already-specified UI change” | focused UI implementation / `ui-implementer` |
| “Review this PR” | `reviewer` |
| “Audit the project” | `auditor` |
| “Redesign these settings” | UI workflow / `ui-orchestrator` |
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

### OCR / Open Code Review

Alibaba `open-code-review` is integrated in two layers for code-like review:

```text
OCR delegate = deterministic local scope / exclusions / rule preflight (no OCR-side LLM)
@reviewer    = complete host-model review / coverage / judgment / final verdict
OCR managed  = optional or required independent second-model escalation
```

When compatible delegation is installed, reviewer uses it before reasoning and reconciles its output against the authoritative changed set. Managed `ocr review` is not the default first step; it runs only when explicitly required or when it materially improves confidence. Review-only requests never auto-apply OCR suggestions.

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

Manual environment setup is documented separately in [`docs/ui_mcp_setup.md`](docs/ui_mcp_setup.md) and [`docs/uupm_setup.md`](docs/uupm_setup.md). These are human-facing instructions only; normal UI roles do not load or depend on them.

---

## Bundled agents

| Agent | Role |
|---|---|
| `build` | Focused implementation; direct primary or delegated leaf |
| `code-orchestrator` | Multi-step coding/PR/bug/release coordination; never implements itself |
| `debugger` | Root-cause bugfix implementation |
| `explore` | Read-only codebase discovery/call-path tracing |
| `tester` | Independent verification; never fixes failures |
| `reviewer` | Independent code/diff/PR/plan review |
| `auditor` | Broad read-only project audit orchestrator |
| `plan` | Architecture/persistent planning; direct primary or delegated leaf; no source implementation |
| `devops` | Runtime/CI/deploy diagnostics and authorized operational changes |
| `general` | Read-only bounded fallback research when no specialist fits |
| `ui-orchestrator` | UI workflow owner when primary; delegated UI stage normalizer when called by another orchestrator; never implements itself |
| `ui-auditor` | Read-only UI/UX audit |
| `ui-planner` | Concrete UI implementation planning |
| `ui-implementer` | Focused UI implementation |
| `a11y-reviewer` | Independent accessibility/interaction review |

No agent file contains a provider-specific `model:` override.

---

## Custom commands

This pack ships **no custom slash commands**. Review, verification, debugging, planning, UI work, PR follow-up, release preparation, audits, code exploration, provenance inspection, and persistent-plan execution are routed from natural-language intent by `AGENTS.md` and the owning agent contracts.

If you intentionally want a specific agent rather than semantic routing, use OpenCode's explicit agent selection. UI MCP/UUPM environment setup is documented as ordinary manual instructions rather than coding commands.

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

Installs runtime configuration under `~/.config/opencode/` (`AGENTS.md`, `agents/`, and `skills/`). The package installs no custom commands or snippets. Documentation remains in the package and is not copied into OpenCode runtime.

### Project-local

From the target repository root:

```bash
/path/to/opencode_model_agnostic_persistent_v30_00/install/install-project.sh
```

Installs `AGENTS.md` plus `.opencode/{agents,skills}/` into the project. The package installs no custom commands, snippets, or docs into the project runtime.

---

## Documentation map

| Document | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Canonical behavioral/workflow policy |
| [`CHANGELOG.md`](CHANGELOG.md) | Release history index |
| [`docs/ui_mcp_setup.md`](docs/ui_mcp_setup.md) | Manual UI component MCP setup reference |
| [`docs/uupm_setup.md`](docs/uupm_setup.md) | Manual UI UX Pro Max setup reference |
| [`docs/releases/v30.00.md`](docs/releases/v30.00.md) | Current stable release notes |

The two setup documents are human-facing references, not runtime policy. No root/agent/skill behavior depends on them, and installers do not copy them into OpenCode configuration.

## Release validation

A release archive should verify at least:

- 15 agents and zero package custom commands;
- valid YAML frontmatter for every agent;
- no provider-specific agent model overrides;
- every historical command intent remains covered by resident natural-language routing plus an owning role contract;
- the two non-release setup docs are human-facing references only, are not copied into runtime, and are not required by root/agents/skills;
- every installed runtime file has a known OpenCode discovery/activation mechanism or deterministic resident consumer; no dead runtime surfaces are shipped;
- no package `snippet/` directory is installed or required; historical package-owned snippets are backed up/pruned on upgrade without touching unrelated files;
- no stale universal `origin/main`, outdated OCR timeout contract, or obsolete version-path references;
- install scripts pass `bash -n`, copy complete skill directories, and back up/prune exact obsolete package-owned command/doc filenames without touching unrelated entries;
- vendored/upstream skill content is not silently replaced by package-authored wrappers;
- archive roundtrip manifest matches the working tree.

---

<div align="center">

**OpenCode Agent Pack v30.00**  
Semantic routing · bounded orchestration · fresh evidence · clean PRs

</div>
