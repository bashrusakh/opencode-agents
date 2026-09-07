<div align="center">

> v28.27 cleans up the behavioral contract for stronger model-agnostic execution: semantic routing, hard role boundaries, evidence freshness, and command/docs consistency without rebuilding the package around per-agent permission mazes.

# OpenCode Agent Pack v28.27

### Semantic routing · Hard role boundaries · GrayMatter memory · OCR review · Clean PR provenance · Persistent planning

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Semantic Routing](https://img.shields.io/badge/Semantic--Routing-On-7c3aed?style=for-the-badge)](#)
[![OCR Review](https://img.shields.io/badge/OCR--Review-Preferred-0f766e?style=for-the-badge)](#)
[![Regression Guard](https://img.shields.io/badge/Regression--Guard-On-f97316?style=for-the-badge)](#)

</div>

---

## What changed in v28.27

- Reworked root `AGENTS.md` to remove accumulated contradictions and duplicated policy layers.
- Kept routing semantic: the requested outcome selects the appropriate role/workflow; users do not need magic trigger phrases or to know the internal agent graph.
- Strengthened hard role boundaries. An orchestrator/reviewer/auditor/planner does not become an implementer because a specialist failed, was rate-limited, was unavailable, or looked unnecessary.
- Explicitly blocks alternate-editor fallbacks such as `sed`, `python`, shell redirection, generators, or VCS restore/checkout when a role is not allowed to implement.
- Kept per-agent permissions as a coarse runtime ceiling rather than rebuilding semantic behavior as a large permission matrix.
- Added evidence freshness for all workflows: validation/review claims belong to the effective state/diff they actually checked.
- Prohibits weakening/skipping tests, assertions, snapshots, lint/type rules, or coverage merely to manufacture a passing result.
- Fixed Git base semantics: resolve the actual PR/project base; `origin/main` is only an example, never a universal default.
- Made persistent planning compatible with read-only workflows: audits do not create repository plan files merely to maintain agent state.
- Simplified all 21 commands into intent entry points instead of copies of the root policy.
- Aligned docs/snippets with the same root contract and refreshed UI MCP/UUPM setup guidance.

v28.26 GrayMatter memory integration and upstream skill refresh remain in place. UI UX Pro Max bundled skill content remains intentionally unchanged in this release.

---

## What this pack is

An opinionated OpenCode/OpenChamber agent configuration pack for project work: focused implementation, bugfixes, UI work, PR follow-up, review, release prep, audits, DevOps diagnostics, and resumable multi-agent workflows.

Core principle:

> Normalize the requested outcome, route it to a capable role, preserve the user/project contract, prove current evidence, and never silently escalate a role because delegation failed.

---

## Behavioral architecture

### 1. Semantic routing

Routing is based on the normalized deliverable, target, action level, repository evidence, and current scope — not literal keywords.

Examples:

- "where is this implemented?" -> discovery/explore
- "fix this failing test/runtime bug" -> bugfix/debug workflow
- "change this known config/code path" -> focused implementation
- "review this PR/diff" -> reviewer
- "audit the whole project" -> auditor
- "redesign these settings" -> UI workflow
- "why is the service failing?" -> DevOps diagnostics

The same meaning should route consistently even when phrased differently or in another language.

### 2. Role boundaries

Roles are capability contracts, not suggestions.

- `code-orchestrator` coordinates multi-step coding workflows and never implements repository changes itself.
- `ui-orchestrator` coordinates UI workflows and never implements repository changes itself.
- `reviewer`, `auditor`, `explore`, `tester`, `a11y-reviewer`, and `general` remain read-only for their assigned responsibilities.
- `plan` may maintain authorized planning artifacts but does not implement source/config/tests.
- `build`, `debugger`, `ui-implementer`, and authorized `devops` work are implementation-capable within their role/scope.

A failed/unavailable/rate-limited specialist does **not** transfer its capability to the caller. Substitute only another role that genuinely owns the required action; otherwise report that stage as blocked.

The pack intentionally does not use a large per-agent shell/command permission matrix as a substitute for this semantic contract.

### 3. Authorization gates

External/public/destructive/scope-expanding actions are gated in root `AGENTS.md`. If the user's normalized request already clearly authorizes the exact action, target, and scope, do not ask again.

Typical gated actions include branch/commit/PR/issue/release mutation, destructive history/data operations, new dependencies/design systems, secrets/private resources, production/runtime changes, materially different product/architecture direction, and publication with blocked required verification.

---

## Startup block

After any required GrayMatter bootstrap and before the first non-memory tool call in a workflow covered by the root `AGENTS.md` Startup rule (including repository/codebase, issue/PR/release, external-URL, publication-capable, scope-expanding, or other multi-step tool workflows), emit exactly one compact Startup block:

```md
### Startup
- Route: `<route>`
- Mode: `<read-only | options | edit-capable | publication-capable>`
- Summary: <one sentence>
- Scope: <target + boundary>
- Gated: `<no | yes>` — <reason>
- Next: <next action/tool>
```

`Mode` is the normalized workflow action ceiling; it never overrides the current agent's role boundary.

If route/mode/scope materially changes later, use a compact `### Update` instead of repeating Startup.

---

## GrayMatter memory

GrayMatter is an **optional external MCP integration**; it is not bundled in this archive. Install and wire it separately when persistent memory is wanted:

- Upstream: https://github.com/angelnicolasc/graymatter

When GrayMatter MCP tools are present, the pack uses persistent memory deliberately:

1. resume unfinished work with `checkpoint_resume` when applicable;
2. search the stable repository `agent_id` and `__shared__` before Startup;
3. store durable atomic conclusions/preferences/decisions/workarounds;
4. use checkpoints for transient unfinished-task state;
5. update/forget stale memories instead of leaving conflicting facts live.

If GrayMatter is not available in the current toolbelt, the memory-specific rules are skipped. Repository code/docs/history/tool output remain authoritative over recalled memory.

---

## Correctness and regression discipline

### Behavioral contract

For user-facing UI/config/API/workflow changes, identify the natural user action, value source/domain, existing project pattern, and whether a naive implementation would expose raw/internal controls that normal users should not need.

### Right-level fixes

Fix the behavior at the abstraction that owns it. Do not patch only the first caller when a shared helper/service/composable/API wrapper is the real fault boundary.

### Regression guard

For bugfixes and changes to existing/shared behavior:

- prove the intended changed behavior;
- prove the closest applicable preserved behavior/invariant;
- broaden verification proportionally for shared/multi-caller/stateful paths;
- prefer a regression test at the existing test layer when practical;
- do not introduce a new test framework just to satisfy the rule.

### Evidence freshness

Validation and review verdicts belong to the effective state/diff they checked. Later changes invalidate affected evidence. Re-run only what the later change can affect before claiming success.

A focused passing check proves only the behavior it exercises. Never claim project/module-wide verification unless the broader checks actually ran.

Do not make a failing check pass by deleting, skipping, weakening, or broadening assertions/snapshots/type/lint/coverage requirements unless the normalized task intentionally changes that expected behavior and project evidence supports it.

---

## Git / PR safety

Resolve the actual head remote, base remote, base branch, and `<base_ref>` from project guidance, tracking state, PR metadata, or repository metadata.

Example only:

```text
<base_remote>=origin
<base_branch>=main
<base_ref>=origin/main
```

Never use that example blindly.

A PR is the entire base-to-head comparison, not the last commit. Before publication, prove the intended commit range/files, current branch state, fresh validation/review evidence, and synchronized PR metadata.

Detailed references:

```text
docs/git_branch_provenance_policy.md
docs/pr_readiness.md
```

---

## OCR / Open Code Review

Alibaba `open-code-review` is the preferred backend for code/diff/commit/branch/workspace/PR review when installed and external code sharing is allowed.

```text
OCR = review engine
@reviewer = scope/privacy/judgment/verdict layer
```

The package vendors the upstream `open-code-review` skill unchanged from upstream policy. Follow the loaded skill/current CLI timeout + effort semantics; do not hardcode an old package timeout or kill reviews with a 120-second outer cap.

Review-only requests never auto-apply OCR suggestions.

See:

```text
docs/ocr_review_policy.md
snippet/open-code-review-usage.md
```

---

## Persistent planning

Use persistent planning only when work genuinely needs durable coordination/resumability across broad scope, phases, agents, or sessions.

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

For read-only/audit workflows, do not create repository plan files merely to persist agent state. Reuse existing plan state or use GrayMatter checkpoint/runtime state unless file mutation is separately authorized.

Broad execution uses:

```text
Blueprint -> Gate -> Execute -> Digest
```

`Gate` checks authorization; it is not a repeated confirmation ritual for already authorized scope.

---

## UI component / design intelligence stack

Existing project components and design system come first.

When appropriate and available:

1. existing project components/tokens/styles;
2. official shadcn MCP/default registry;
3. additional public/GitHub shadcn-compatible registries through the official shadcn mechanism;
4. optional Jpisnice `shadcn-ui-mcp-server` as secondary/reference source;
5. manual implementation when no suitable source fits.

UUPM/UI UX Pro Max is optional design intelligence, not the component MCP and not permission to create a new design system.

Setup references:

```text
docs/ui_component_policy.md
docs/ui_mcp_install_for_agent.md
docs/uupm_install_for_agent.md
```

---

## Bundled agents

| Agent | Role |
|---|---|
| `build` | Focused, clearly scoped implementation |
| `code-orchestrator` | Multi-step coding/PR/bug-issue/release coordination; never implements itself |
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

Commands are **intent entry points**, not duplicate policy documents. Root `AGENTS.md` and the selected agent contract provide shared behavior.

| Command | Purpose |
|---|---|
| `/audit` | Broad read-only project/repository audit |
| `/bug-issue` | Verify a reported bug and draft/open a factual non-duplicate issue |
| `/bugfix` | Multi-step bugfix coordination |
| `/code-explore` | Read-only codebase exploration |
| `/debug` | Root-cause and fix a confirmed failure |
| `/devops-check` | Runtime/CI/deploy/config diagnostics |
| `/execute-plan` | Execute the current persistent-plan work package |
| `/plan` | Create/resume/update persistent plan state |
| `/pr-followup` | Existing PR comments/checks/fixes/verification/publication follow-up |
| `/pr-provenance` | Read-only base-to-head branch provenance proof |
| `/release-prep` | Grounded release-note/release-state preparation or verification |
| `/review` | Independent review; OCR preferred for code when allowed |
| `/ui-a11y-check` | Accessibility/interaction review |
| `/ui-audit` | UI/UX audit |
| `/ui-implement` | Implement an understood UI change/accepted plan |
| `/ui-mcp-setup` | Configure supported UI MCP stack |
| `/ui-options` | Produce 2-3 grounded UI directions without implementation |
| `/ui-plan` | Concrete implementable UI plan |
| `/ui-redesign` | Coordinate complete UI redesign workflow by semantic need |
| `/ui-uupm-setup` | Configure UUPM for OpenCode |
| `/verify` | Independent tests/lint/build/smoke verification |

---

## Bundled skills

The package currently bundles:

```text
api-designer
cpp-pro
golang-pro
open-code-review
playwright-expert
python-pro
react-expert
rust-engineer
secure-code-guardian
typescript-pro
ui-ux-pro-max
vue-expert
```

Skills are advisory and selected semantically from actual project context. A matching skill must actually be loaded/read before claiming it was used.

Upstream sources / external integrations:

- GrayMatter persistent memory: https://github.com/angelnicolasc/graymatter
- Alibaba `open-code-review`: https://github.com/alibaba/open-code-review
- Jeffallan `claude-skills`: https://github.com/Jeffallan/claude-skills
- UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (bundled content intentionally retained unchanged in v28.27)

---

## Install

### Global

```bash
./install/install-global.sh
```

Installs under:

```text
~/.config/opencode/AGENTS.md
~/.config/opencode/agents/
~/.config/opencode/commands/
~/.config/opencode/docs/
~/.config/opencode/skills/
~/.config/opencode/snippet/
```

### Project-local

From the target repository root:

```bash
/path/to/opencode_model_agnostic_persistent_v28_27/install/install-project.sh
```

Installs to:

```text
./AGENTS.md
./.opencode/agents/
./.opencode/commands/
./.opencode/docs/
./.opencode/skills/
./.opencode/snippet/
```

---

## Validation expectations

A release archive should verify at least:

- 15 agents and 21 commands;
- YAML frontmatter parses for every agent/command;
- no provider-specific agent `model:` overrides;
- all bundled commands keep `subtask: false` and contain no command-level permission or model overrides;
- agent `mode`/permission frontmatter unchanged unless a release explicitly targets permissions;
- no stale `Mode: gated`, hardcoded universal `origin/main`, old OCR timeout contract, or obsolete version-path references;
- install scripts pass `bash -n` and copy complete skill directories;
- UI UX Pro Max bundled skill stays byte-identical when a release explicitly excludes its update;
- upstream-vendored skill files are not silently wrapped/replaced by package-authored copies;
- archive roundtrip manifest matches the working tree.

---

<div align="center">

**OpenCode Agent Pack v28.27**  
Semantic routing · Role boundaries · Fresh evidence · GrayMatter · OCR · Clean PRs

</div>
