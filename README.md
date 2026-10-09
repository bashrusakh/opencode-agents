<div align="center">

# OpenCode Agent Pack v30.43 beta

### Model-agnostic routing · strict role boundaries · bounded multi-agent workflows · evidence-grounded verification

[![OpenCode](https://img.shields.io/badge/OpenCode-Agents-111827?style=for-the-badge)](#)
[![Model Agnostic](https://img.shields.io/badge/Model--Agnostic-Yes-2563eb?style=for-the-badge)](#)
[![Semantic Routing](https://img.shields.io/badge/Semantic--Routing-On-7c3aed?style=for-the-badge)](#)
[![Regression Guard](https://img.shields.io/badge/Regression--Guard-On-f97316?style=for-the-badge)](#)

</div>

---

## What changed in v30.43 beta

- Restores outcome-first/plain-language wording to the canonical root communication contract while keeping Markdown and brevity globally owned there.
- Removes duplicate generic Markdown/verbosity rules from `output-formatting` and duplicate material-decision wording from `code-orchestrator`; those layers now keep only their destination/role-specific consequences.
- Converts repeated authority/evidence statements in gates, delegation, and regression guidance into explicit references to the canonical claim-authority section while preserving their local gate/delegation/test semantics.

See [`docs/releases/v30.43-beta.md`](docs/releases/v30.43-beta.md).

---

## Core model

`AGENTS.md` is the canonical workflow policy. Agent files add role-specific behavior; skills add conditional procedural guidance. README is an overview, not a second policy source.

### Semantic routing

Routing follows the requested outcome, target, action level, current repository state, and authoritative project guidance — not magic keywords.

| Request | Typical route |
|---|---|
| “Where is this implemented?” | `explore` |
| “Fix this runtime bug” | `debugger` |
| “Implement this bounded code/config outcome” | `build` |
| “Review this PR” | `reviewer` |
| “Audit the project” | `auditor` |
| “Plan a broad implementation” | `project-planner` |
| “Redesign these settings” | `ui-orchestrator` |
| “Why is this service failing?” | `devops` |

The table shows the semantic owner. Actual primary/subagent execution still follows OpenCode agent mode and the pack's delegation rules.

### Role and authority boundaries

Roles are capability contracts:

```text
orchestrator
  owns WHAT / SCOPE / NEXT / escalation / publication

specialist
  owns HOW inside the assigned boundary
```

A specialist may choose implementation details needed inside its assignment. It may not silently widen the task, strengthen acceptance, take another role's protected stage, change PR/publication state, or turn its own finding into new authority.

A failed or unavailable specialist does not transfer its prohibited capabilities to the caller unless the policy defines an explicit authority-preserving fallback.

### Claims, scope, and fix level

The pack treats material decisions about framing, required behavior, scope, ownership, invariants, and fix level as claims that require evidence. Derived reasoning, review findings, tests, and prior-agent decisions do not become authority merely because later work depends on them.

Implementation may cross files or layers when that is a necessary technical consequence of an already-established outcome. Complexity by itself is not permission to strengthen the required behavior or widen what the task authorizes.

### Evidence belongs to the state it checked

Tests and review verdicts apply to the actual state they inspected. Later changes invalidate only the evidence they can affect.

A narrow test proves only its covered behavior. A fresh remote `ref@SHA` must not silently become stale-worktree evidence. Review and verification should identify the exact candidate state they support.

### Gated actions stay explicit

Public/external, destructive, publication, scope-authority, and other gated actions follow `AGENTS.md`. Already-authorized actions do not need repeated confirmation; a materially changed target, scope, destination, or risk does.

---

## PR workflow

For confirmed **owned PRs**, implementation and readiness are separate states:

```text
Draft
  ↓ implementation / repair / intermediate CI
local Candidate HEAD
  ↓ final applicable local checks
  ↓ @tester when independent verification adds value or is required
  ↓ whole-PR @reviewer
push exact reviewed SHA
  ↓ reconcile remote head + applicable checks/dependencies
Ready transition when authorized and its real preconditions hold
```

Key invariants:

- active owned PR implementation stays Draft;
- the final reviewer covers the complete base-to-Candidate-HEAD change, not only the latest patch;
- the reviewed SHA is pushed unchanged before Ready;
- unchanged SHA does not require another full review solely because it was pushed;
- unresolved required evidence blocks Ready; lifecycle-dependent evidence is checked when it can actually exist;
- repository discussions/issues/RFCs are gates only when repository policy makes their state a prerequisite;
- unowned or ambiguous PRs are not automatically moved between Draft and Ready.

Detailed rules live in `AGENTS.md` and the `pr-readiness`, `git-provenance`, and review skills.

---

## Review and verification

### Right-level implementation

Choose the narrowest existing ownership boundary that can guarantee the established outcome across affected paths and states. Do not patch the first visible caller when the behavior belongs to a shared owner, and do not invent a broader invariant merely to justify a larger fix.

### Regression guard

For bugfixes and shared/existing behavior changes, verify both:

- the behavior intentionally changed;
- the closest applicable behavior or invariant that must remain unchanged.

Shared/stateful changes receive proportionally broader checks. Tests, snapshots, lint/type rules, and coverage are not weakened merely to create a PASS.

### Verification cadence

Verification is proportional rather than a mandatory fixed chain:

```text
implementation role -> focused local evidence
meaningful boundary -> @tester when independent verification adds value
stable candidate -> final applicable validation + @reviewer
published candidate -> remote CI/status
```

A work package ending does not automatically require `@tester`, and reviewer should not mechanically repeat a fresh broad test pass.

### Open Code Review integration

Alibaba `open-code-review` is optional review support:

```text
OCR delegate = deterministic local scope/rule preflight
@reviewer    = host-model semantic review and verdict
OCR managed  = optional/required independent second-model escalation
```

Managed OCR is not a universal Ready gate and review-only workflows do not auto-apply its suggestions.

---

## Persistent planning

Persistent planning is for work that genuinely needs durable coordination across broad scope, phases, agents, or sessions. Root keeps only the trigger and durable-state contract; when persistent planning applies, load `persistent-planning` and prefer the project's existing planning convention before the pack default.

`project-planner` is intentionally separate from OpenCode's built-in `plan` agent so repository planning writes do not depend on the built-in plan agent's restricted edit policy. Read-only audits do not create repository plan files merely to maintain agent state.

---

## Experimental semantic evaluation

The pack currently uses two separate semantic roles because they answer different lifecycle questions.

`semantic-checkpoint` is a **pre-mutation gate**. After relevant read-only discovery, `code-orchestrator` invokes it only when the candidate direction materially establishes or changes required behavior, acceptance, scope, ownership, invariant, fix level, or product/domain policy. `proceed` authorizes only the checked semantic boundary: the orchestrator still hands ordinary technical mechanics to the implementation role and does not turn optional mechanisms named by the checkpoint into acceptance. `hold` and `unverified` block mutation until their material blockers are addressed; an unchanged blocked candidate is not re-run merely to seek a different verdict. Routine technical mechanics under already-established acceptance do not trigger the checkpoint.

Each checkpoint evaluation runs in a **fresh child session**. A re-check after new evidence or a materially revised candidate does not continue the previous checkpoint conversation; the new child reconstructs the current decision from authoritative task/session evidence. More generally, the pack reuses a child session only for deliberate continuation of the same specialist-owned assignment, not merely because the same role is called again.

`session-evaluator` remains a **post-hoc diagnostic** and, while the temporary semantic-eval experiment is active, runs once only when `code-orchestrator` reaches a terminal successful outcome about to be reported: the normalized session goal is satisfied or an owned PR candidate reaches final readiness. It classifies confirmed findings as:

- `instruction-violation`
- `instruction-ambiguity`
- `instruction-gap`
- `execution-error`
- `justified`

`unverified` is an evidence status, not a finding class, and does not require a failure classification. The evaluator proposes prompt changes only for confirmed reusable instruction ambiguities or gaps.

Both roles reconstruct relevant OpenChamber session history with read-only `session.list` / `session.messages`, use exact parent/participating session IDs supplied by `code-orchestrator` before any discovery, and fall back to `session.list` only for missing identities or relationships needed by the material evidence boundary. They prefer child-session history over parent summaries and do not turn diagnostic output into task authority. `session-evaluator` ignores prior evaluator diagnoses as workflow evidence and uses `semantic-checkpoint` only as gate-control evidence (for example, whether a `hold` was obeyed), not as proof of the underlying requirement.

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

Startup is the only routine pre-tool narration. A material finding, blocker, or route/mode/scope change may use a compact `### Update`; ordinary tool use and completed substeps are not narrated. Final reports lead with the result and include only material evidence needed by the recipient.

### GrayMatter memory

GrayMatter is an optional external MCP integration and is not bundled. When present, it can restore unfinished work and durable project context; repository code/docs/history/tool output remain authoritative over recalled memory.

---

## UI workflow and component intelligence

Existing project components, tokens, and design patterns come first. When relevant and available, UI work can use existing project components, official shadcn sources, compatible registries, optional secondary MCP references, and manual implementation when no source fits.

UI UX Pro Max (UUPM) is optional design intelligence, not a component source and not permission to introduce a new design system.

Human-facing setup references:

- [`docs/ui_mcp_setup.md`](docs/ui_mcp_setup.md)
- [`docs/uupm_setup.md`](docs/uupm_setup.md)

These setup docs are not runtime policy and installers do not copy them into OpenCode configuration.

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
| `project-planner` | Architecture/persistent planning; may write authorized plan artifacts, never source implementation |
| `semantic-checkpoint` | Experimental pre-mutation semantic gate for material candidate decisions after discovery |
| `session-evaluator` | Experimental post-hoc audit of completed orchestrator sessions and child-agent calls against governing instructions |
| `devops` | Runtime/CI/deploy diagnostics and authorized operational changes |
| `general` | Read-only bounded fallback research when no specialist fits |
| `ui-orchestrator` | UI workflow coordination; never implements itself |
| `ui-auditor` | Read-only UI/UX audit |
| `ui-planner` | Concrete UI implementation planning |
| `ui-implementer` | Focused UI implementation |
| `a11y-reviewer` | Independent accessibility/interaction review |

**Count:** 17 agents. No bundled agent has a provider-specific `model:` override.

The pack ships no custom slash commands. Natural-language routing is owned by `AGENTS.md`; use OpenCode's explicit agent selection when you intentionally want a specific role.

---

## Skills and integrations

### Bundled skills

```text
api-designer          cpp-pro                  git-provenance
golang-pro            graymatter-memory        open-code-review
open-code-review-delegate output-formatting     persistent-planning
playwright-expert      pr-readiness             python-pro
react-expert           resource-lifecycle       rust-engineer
secure-code-guardian   typescript-pro           ui-ux-pro-max
verification-strategy vue-expert
```

**Count:** 20 skills. Skills are conditional/procedural guidance and remain subordinate to root/project authority, role boundaries, and gates.

### External integrations

These external projects provide optional integrations or source material referenced by bundled skills/docs:

- GrayMatter memory: https://github.com/angelnicolasc/graymatter
- Alibaba `open-code-review`: https://github.com/alibaba/open-code-review
- Jeffallan `claude-skills` source material: https://github.com/Jeffallan/claude-skills
- UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

---

## Prompt and evaluation design references

The pack is model-agnostic. The links below are **design references**, not runtime dependencies or model-routing requirements. Vendor-specific advice is adopted only when it generalizes to the pack's goals and survives pack-specific regression checks.

### OpenAI

- Current prompt-engineering guidance: https://developers.openai.com/api/docs/guides/prompt-engineering
- Rethinking skills/`AGENTS.md`/prompt scaffolding for newer coding models: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- Evidence-based persistent goals and bounded completion contracts: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- Turn real traces and feedback into reusable evals and harness changes: https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop
- Separate review/repair/validation and let observed validation decide success: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex

### Anthropic

- Agent-evaluation design using transcripts, outcomes, graders, and real failure cases: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Harness design with separate evaluator roles, concrete grading criteria, and deliberate simplification as model capability improves: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Claude Opus 5 prompting guidance on scope, over-verification, self-correction, and subagent use: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Claude Sonnet 5.5 prompting guidance on initiative/scope and proportionate coding verification: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5

### DeepSeek

- DeepSeek Harness code-review guidance: verify live state, review semantic contracts, and verify review claims instead of accepting them performatively: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-code-review/SKILL.md
- DeepSeek Harness prose guidance: direct verbs, one main action per sentence when ambiguity matters, stable terminology, preserve exceptions: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-doc/SKILL.md
- DeepSeek Harness skill-system design: keep standing prompt context small and load task-specific instruction bodies on demand: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/notes/archived/feature/2026-07-05-skill-system.md

### Z.ai / GLM

- GLM-5.3 agent engineering/evaluation: executable and verifiable long-horizon environments, separate verifier/judge signals, realistic end-to-end task completion: https://z.ai/blog/glm-5.3
- GLM-5.3 engineering feedback loops: turn ambiguous observations into testable hypotheses and validate changes against correctness/stability/performance criteria: https://z.ai/blog/glm-built-its-inference-infrastructure

These references change as models and harnesses evolve. Re-evaluate inherited prompt scaffolding against current models rather than treating old vendor advice as permanent doctrine.

---

## Runtime references

These links document runtime surfaces used by the pack; they are separate from the prompt-design references above.

- OpenCode agent definitions, modes, permissions, and child-session behavior: https://opencode.ai/v2/docs/agents
- OpenChamber agent-tool control surface, including `session.list` and `session.messages`: https://github.com/openchamber/openchamber/blob/main/packages/web/server/lib/openchamber-control/actions.js
- OpenChamber control-service/runtime documentation: https://github.com/openchamber/openchamber/blob/main/packages/web/server/lib/openchamber-control/DOCUMENTATION.md

The experimental `semantic-checkpoint` and `session-evaluator` roles depend on those OpenChamber read-only session actions being exposed to the active agent environment.

---

## Install

### Global

```bash
./install/install-global.sh
```

Installs under `~/.config/opencode/`:

- `AGENTS.md`
- `agents/`
- `skills/`

The global installer backs up the existing root `AGENTS.md` and obsolete package-owned paths before removing them. It also backs up and removes the obsolete package-owned `tools/session_trace.js` when upgrading from v30.27-v30.29. Current agent/skill files are copied in place; use the project-local installer or your own config backup when you need a full pre-install snapshot. Package documentation is not copied into OpenCode runtime.

### Project-local

From the target repository root:

```bash
/path/to/opencode-agent-pack/install/install-project.sh
```

Installs:

- `./AGENTS.md`
- `.opencode/agents/`
- `.opencode/skills/`

The installer backs up existing runtime surfaces before copying the pack and removes only explicitly listed obsolete package-owned paths, including the old `.opencode/tools/session_trace.js` when present. It does not install custom commands, tools, snippets, or docs.

---

## Documentation map

| Document | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Canonical behavioral/workflow policy |
| [`CHANGELOG.md`](CHANGELOG.md) | Release history and links to retained release notes |
| [`docs/releases/v30.43-beta.md`](docs/releases/v30.43-beta.md) | Current release notes |
| [`docs/semantic-design-manual.md`](docs/semantic-design-manual.md) | Method for turning developer guidance and traces into durable semantic rules |
| [`docs/semantic-design-source-audit.md`](docs/semantic-design-source-audit.md) | Source → generalized rule → reverse-action preservation audit |
| [`docs/releases/v30.32-beta.md`](docs/releases/v30.32-beta.md) | Claim-authority clarification |
| [`docs/releases/v30.27-beta.md`](docs/releases/v30.27-beta.md) | `session-evaluator` introduction and compatibility notes |
| [`docs/ui_mcp_setup.md`](docs/ui_mcp_setup.md) | Human-facing UI component MCP setup |
| [`docs/uupm_setup.md`](docs/uupm_setup.md) | Human-facing UI UX Pro Max setup |

---

## Release validation

A release archive should verify at least:

- exactly **17 agents**, **20 skills**, zero package custom commands, and zero package custom tools;
- valid agent frontmatter and no provider-specific `model:` overrides;
- every current role reference resolves and obsolete package-owned `plan.md` does not remain active after upgrade;
- root stays below the pack's `<50 KiB` target;
- run a **fresh semantic prompt audit** over root `AGENTS.md` and every agent file as one corpus:
  - each standing instruction must still prevent a concrete failure mode or encode a current product/workflow requirement;
  - remove semantic duplicates, stale model-era scaffolding, unnecessary verification/subagent rituals, role↔root restatements, release-validation or “what did not change” narration in runtime prompts, and workaround rules whose cause no longer exists;
  - retain a local reminder only when salience at that decision point materially reduces a known failure mode;
  - after any prompt change, rerun semantic invariant checks that test the general rules rather than incident-specific wording;
- agent/skill/install surfaces match the release manifest and unexpected runtime files are not introduced;
- subagent session continuity follows assignment continuity: new specialist assignments/independent judgments use fresh child sessions, while continuation is explicit and limited to the same specialist-owned workstream;
- `semantic-checkpoint` remains read-only/non-implementing, gates only material pre-mutation semantic decisions, runs each verdict in a fresh child session, and does not classify instruction failures or require post-mutation proof before edits;
- `code-orchestrator` treats `proceed` as candidate-specific authorization, preserves optional mechanisms as implementation choices, keeps `hold`/`unverified` blocked until their stated blockers are materially addressed, does not re-run an unchanged blocked candidate for verdict-shopping, and never continues a prior checkpoint child for a new verdict;
- `session-evaluator` remains post-hoc/diagnostic, uses only OpenChamber `session.list`/`session.messages`, consumes supplied parent/participating session IDs before fallback discovery, keeps `unverified` separate from finding classes, treats checkpoint verdicts only as gate-control evidence, and audits the original decision path independently;
- session-aware delegated judgments do not enumerate the project merely to rediscover supplied session identities; `session.list` remains fallback only for missing identities/relationships, while OpenChamber pagination defects remain runtime defects rather than prompts for broader semantic crawling;
- Startup/update/final communication remains compact: no duplicate prose plan around Startup, no routine tool narration, and no empty/repeated report sections;
- the semantic design manual remains documentation rather than runtime policy, and its source-preservation audit still derives the tracked developer actions after abstraction;
- installer scripts pass `bash -n`, preserve unrelated user/project files, and match their documented backup/overwrite behavior;
- external/setup docs remain documentation only and are not required runtime policy;
- vendored/adapted skill content retains source/license attribution;
- archive extraction is safe and the roundtrip manifest matches the working tree.

---

<div align="center">

**OpenCode Agent Pack v30.43 beta**  
Semantic routing · bounded orchestration · evidence-grounded verification

</div>
