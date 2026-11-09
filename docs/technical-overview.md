[← Short README](../README.md)

<div align="center">

# OpenCode Agent Pack v31.22 — Technical overview

### A semantic agent instruction pack for OpenCode

**Understand the task first · Establish the intended outcome · Execute with accountable agents**

</div>

---

## What is a semantic agent pack?

**The defining purpose is to turn a user's request into an actionable, evidence-grounded task before agents start implementing it.** The user should not have to write a detailed technical specification (ТЗ) just to get a useful result. They can describe a problem, an objective, or an observed failure in ordinary language; the pack directs the workflow owner to **determine what needs to be achieved**, using the request, repository, existing behavior, documentation, and other applicable evidence.

Here, *semantic* refers to **understanding and establishing the task's meaning**, not semantic search, embeddings, or automatic model selection. Preserving that meaning later is essential, but it is **a consequence of having established the task**, not the definition of semantic orchestration.

The workflow therefore begins with task interpretation:

1. **Understand the request.** Identify the user's intended result, relevant target, and observed problem. Distinguish what the user actually established from assumptions and proposed implementation mechanisms.
2. **Establish the task.** Inspect relevant project context and actual behavior to determine scope, constraints, preserved invariants, and how the required result could be recognized. Develop a task model proportionate to the request rather than inventing a full specification.
3. **Resolve consequential uncertainty.** If multiple materially different outcomes remain plausible, investigate safely or ask a focused question before making an unauthorized or hard-to-reverse choice. Ambiguity is not permission to invent requirements.
4. **Execute against that task model.** Choose the appropriate owner and specialists, implement within role boundaries, verify the actual expected behavior, and reconcile findings before claiming completion.

**A formal specification is optional, not ignored.** If the user supplies explicit requirements or acceptance criteria, they remain authoritative within the applicable rules. The pack does not promise to infer unknowable preferences or authorize consequential actions merely because an agent found one interpretation plausible.

## Why this matters

A generic instruction file might say *"act as a senior developer"*, *"write tests"* or *"review the patch"*. Those instructions can guide execution but do not, on their own, establish **what the user is asking to achieve**. In an underspecified request, agents can otherwise jump to a plausible fix, choose the wrong success criterion, and execute that mistaken interpretation very efficiently.

For example, a user says: **"CPU percentages in the panel look wrong — fix them."** They need not supply a design document specifying whether CPU should be normalized to machine cores or a container quota. The workflow owner first examines the existing UI contract, calculations and relevant behavior to establish the intended meaning of the numbers. If the evidence still supports incompatible interpretations, the owner resolves that decision before directing an implementation. A patch that makes one chart look reasonable but contradicts the rest of the UI is not automatically the right task outcome.

The semantic layer makes task definition explicit while keeping execution flexible. After the task is established, the package helps prevent that meaning being lost or silently rewritten during delegation, implementation, review, verification and publication.

## How it differs from a prompt collection

This is **not only a library of agent personalities or role prompts**. It combines task interpretation with workflow ownership and explicit authority/evidence contracts:

- **Task-first normalization.** [`workflow-control`](../skills/workflow-control/SKILL.md) classifies the requested result, target, permissible action level and uncertainty *before* selecting a consequential path. The [`code-orchestrator`](../agents/code-orchestrator.md) maintains the task anchor as the work evolves.
- **Requirements are not guesses or implementation choices.** [`AGENTS.md`](../AGENTS.md) distinguishes authorized requirements, source-backed evidence, hypotheses and local mechanisms. A developer's proposal, a passing test or a review comment does not silently become a user requirement.
- **One accountable workflow owner, bounded specialists.** Implementation, testing, review and diagnostics have different responsibilities and capability limits. Delegation transfers a bounded assignment, not ownership of the user's actual objective.
- **Conditional workflow rules instead of one giant prompt.** Approval gates, Git provenance, PR lifecycle, UI routing and session diagnostics load when relevant, limiting unnecessary standing context.
- **Tests for the instructions.** Semantic ownership maps and regression scenarios in [`evals/`](../evals/) check for contract drift and contradictory handoffs. They do not replace tests of the application being built.

These are architectural differences from a *simple* prompt collection, not a claim that no other framework offers similar features. This package is a set of OpenCode instructions and associated checks, **not** a new runtime or an automatic model router.

## What you gain — and the limits

The intended practical gain is that you can **delegate an engineering objective without drafting a full ТЗ first**. Agents are instructed to establish what success means from the available evidence, choose an appropriate workflow, and expose material decisions or uncertainties rather than silently assuming them.

For larger tasks, the same contracts aim to reduce wrong-scope fixes, unauthorized operations, unsupported completion claims and information loss between specialists. For a small, already-defined edit, a single bounded agent can be more efficient than a multi-agent workflow.

**No numerical improvement is claimed:** success rate, speed, token cost, or real-model compliance have not been established by controlled comparisons against alternative packs. Interpretation can still fail, and genuinely missing intent may require a user decision.

## From request to result

```text
User describes a goal, problem, or request — a detailed ТЗ is not required
    ↓
Workflow owner interprets request + relevant project evidence
    ↓
Establishes task: intended result, target, constraints, acceptance evidence
    ├─ material ambiguity? → investigate safely or ask the user
    └─ sufficiently established? → choose role and permitted workflow
    ↓
Bounded specialists implement / test / review as needed
    ↓
Owner reconciles evidence against the established task
    ↓
Qualified outcome, limitations and relevant decisions returned to user
```

This is an **adaptive process**, not a mandatory sequence of agent calls. The user can select a narrower top-level role for an already well-scoped task.

**[Start with the right role](#start-here)** · **[Installation](#install)** · **[Architecture](#where-the-rules-live)** · **[Release evidence](#release-and-design-references)**

## At a glance

- **19 agent roles** in [`agents/`](../agents/), including primary workflow owners and bounded specialists.
- **28 bundled skills** in [`skills/`](../skills/), including conditional workflow controls, technical guidance, and optional integrations.
- **Semantic instruction and protocol checks** in [`evals/`](../evals/), with methodology and release notes in [`docs/`](../docs/).
- **Model-agnostic policies:** the pack does not pin or change a model/provider. Role-specific model suitability still needs testing on real workloads.

---

## Start here

For most multi-step coding work, start with **`code-orchestrator`**.

It is the main coordination role for work that may need several stages such as discovery, implementation, debugging, verification, review, PR follow-up, CI repair, or release preparation. It coordinates specialists; it does not edit repository files itself.

Choose a different top-level workflow owner when the task is intentionally narrower:

| You want to… | Start with | Mode |
|---|---|---|
| Carry a coding issue/bug/PR/release task through multiple specialist stages | **`code-orchestrator`** | `primary` |
| Make one already-bounded code/config/tests/docs change | `build` | `all` |
| Run a broad read-only repository audit | `auditor` | `primary` |
| Produce an architecture/multi-file/deployment implementation plan | `project-planner` | `all` |
| Establish a bounded external technical docs/upstream/version fact | `librarian` | `all` |
| Coordinate UI/UX analysis, planning, and implementation | `ui-orchestrator` | `all` |

`mode: all` means a role may be top-level or delegated subject to its own contract; it does not make every role interchangeable.

### Typical topology

```text
user
  ↓
code-orchestrator (one primary workflow owner for a multi-stage code task)
  ├─ build / debugger / UI specialist  → bounded implementation
  ├─ tester                           → behavior and test evidence
  ├─ reviewer                         → independent judgment
  └─ other specialists, when needed  → bounded findings
  ↓
reconcile results, remaining risks and required gates
  ↓
one consolidated user-facing outcome
```

For a narrower top-level task, the user can instead select `build`, `auditor`, `project-planner`, `librarian`, or `ui-orchestrator` as the **primary owner**. They are alternatives at entry, **not** children that must all run under `code-orchestrator`. The actual handoffs depend on the task; this is not a fixed pipeline or a runtime-enforced DAG.

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

Every colliding managed destination is backed up before replacement and the installer writes an ownership receipt under `~/.config/opencode/.agent-pack/`. An existing global `AGENTS.md` that is not recognizable as a prior pack root is **not** replaced by default; the installer stops before mutation. Explicit replacement is available with `OPENCODE_AGENT_PACK_REPLACE_GLOBAL_AGENTS=1` and still keeps a backup. Ambiguous legacy command/doc/tool names are preserved unless a prior receipt proves package ownership.

### Project-local

From the target repository root:

```bash
/path/to/opencode-agent-pack/install/install-project.sh
```

Installs `.opencode/agents/` and `.opencode/skills/`. For the root policy:

- if the project has no `./AGENTS.md`, the installer may install the pack root there;
- if `./AGENTS.md` is a recognizable prior pack root, it is backed up and upgraded;
- if the repository already owns `./AGENTS.md`, it is preserved. A recognizable global pack root must already be installed; otherwise the project installer stops before mutation rather than replacing project rules or creating a parallel policy owner.

Project-local collisions are backed up under `.opencode/.agent-pack/backups/`, an ownership receipt is recorded, and ambiguous legacy names are preserved unless ownership is proven.

---

## Model selection notes (October 2026 snapshot; advisory)

The pack remains model-agnostic: this is a **dated maintainer advisory**, not an automatically maintained leaderboard, runtime requirement, or hard compatibility gate. Re-check the live results before choosing a model in a later month; compare the **same benchmark version and reasoning-effort setting**, and prioritize your own orchestration traces over aggregate scores.

| Role / decision responsibility | Suggested capability tier | Approximate screening floor |
|---|---|---|
| **`code-orchestrator`** (scope, architectural tradeoffs, multi-agent control) | Strong reasoning/agentic model | **Terminal-Bench 4.0 ≥45%** and **AA-Briefcase v1.1 ≥1500 Elo** |
| `project-planner`, independent `reviewer` | Similar reasoning tier; reviewer should retain independent judgment | Use the same two indicators as a starting point, not a pass/fail gate |
| `debugger`, `build`, `tester` (bounded technical stages) | Efficient capable coding/agentic model | Terminal-Bench 4.0 roughly **25–30%+** as an optional rough filter; verify per task |

**Examples meeting both orchestrator indicators at a tested high-effort configuration:** Claude Sonnet 5.5 Max, Claude Opus 5.5 Max, GPT-6 Astra High/Xhigh, GPT-6.1 Sol **Max**, Claude Fable 5.1 High/Max. **Conditional candidates:** Gemini 4 Argon High (strong terminal result; Briefcase just below the suggested floor), GLM-5.3 Max (strong Briefcase; terminal result below it). Lower-effort variants of the same model may **not** meet both floors; in particular, GPT-6.1 Sol High does not meet the stated Briefcase cutoff on the published comparison.

**Maintainer-tested orchestrator exclusions (October 2026):** **DeepSeek V4.1 Flash, GLM-5.3 Flash, and MiniMax M3.1 Flash are not suitable for the `code-orchestrator` role in this pack.** This is the pack maintainer's direct hands-on assessment of their reliability at orchestration (workflow ownership, handoffs, scope judgment, and mandatory checkpoints), **not** a claim about their general coding ability or a benchmark result. The observation does not exclude these models from bounded specialist roles when independently validated, and must not be generalized to different variants such as **GLM-5.3 Max**. Do not use aggregate coding benchmarks to override role-specific observed failures.

These benchmarks measure broad technical autonomy and knowledge-work performance, **not direct compliance with this pack's handoff/authority/reassessment rules**. A strong implementation score cannot substitute for demonstrated scope judgment or independent review. Recheck current results before configuring a model: [Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase), [model comparison](https://artificialanalysis.ai/models/comparisons).

---

## Delegated specialists

These roles can own bounded delegated stages inside a larger workflow. A `mode: all` role may also be selected directly for the narrower top-level task described above; delegation does not change its role contract.

| Role | What it is for | Mode |
|---|---|---|
| `build` | Bounded implementation of an already-established non-UI code/config/tests/docs outcome | `all` |
| `project-planner` | Architecture, sequencing, state/invariant modeling, and implementation planning | `all` |
| `librarian` | Read-only authoritative external technical docs/upstream/version evidence | `all` |
| `ui-orchestrator` | Bounded coordination of a delegated UI/UX subworkflow | `all` |
| `explore` | Read-only codebase discovery, symbol/call-path tracing, existing-pattern lookup | `subagent` |
| `debugger` | Confirmed failures requiring root-cause diagnosis and a right-level bug fix | `subagent` |
| `tester` | Independent reproduction, tests/builds/smoke checks, preserved-behavior evidence | `subagent` |
| `reviewer` | Independent code/diff/PR/plan review; never applies fixes | `subagent` |
| `devops` | Runtime/service/CI/deployment diagnostics and explicitly authorized operational changes | `subagent` |
| `general` | Read-only bounded research when no more specific specialist owns the question | `subagent` |
| `semantic-checkpoint` | Pre-mutation semantic gate used by `code-orchestrator` | `subagent` |
| `session-evaluator` | Post-hoc semantic compliance diagnostic for completed orchestrated work | `subagent` |
| `trajectory-auditor` | Mid-workflow longitudinal audit of task-anchor preservation and cumulative progress | `subagent` |
| `ui-auditor` | Read-only UI/UX analysis of an existing screen or flow | `subagent` |
| `ui-planner` | Concrete implementable UI design/layout/theme plan | `subagent` |
| `ui-implementer` | Bounded implementation of an accepted UI/web outcome | `subagent` |
| `a11y-reviewer` | Independent accessibility/interaction verification | `subagent` |

The exact invocation contract for each role is in its file under [`agents/`](../agents/). A role description is not the policy for when the role must be called.

---

## Where the rules live

| Surface | Canonical responsibility |
|---|---|
| [`AGENTS.md`](../AGENTS.md) | Universal semantic kernel: precedence, authority/evidence, continuity, capability/skill boundaries, communication and evidence-bound final claims |
| [`agents/`](../agents/) | Role-local execution methods, decision loops, evidence/self-checks, stop/escalation, result semantics |
| [`skills/`](../skills/) | Conditional shared/runtime procedure: workflow control, delegation control, change contract, repository workflow, terminal diagnostics and other specialized integrations |
| [`docs/semantic-design-manual.md`](../docs/semantic-design-manual.md) | Method for designing, auditing, and releasing semantic prompt/role changes |
| [`evals/`](../evals/) | Structural, role-contract, handoff-protocol, and semantic-transition regression machinery |
| [`docs/releases/`](../docs/releases/) | Current release explanation (historical notes are retained separately in the release bundle) |

---

## Notable integrations

### Open Code Review

`reviewer` owns the Open Code Review integration. The pack includes:

- `open-code-review-delegate` for deterministic local review preflight;
- `open-code-review` for managed second-model review when applicable.

These are reviewer-owned specialist skills, not general workflow skills. See [`agents/reviewer.md`](../agents/reviewer.md) and the corresponding skill files for their executable contracts.

### Persistent planning

`project-planner` can use the bundled `persistent-planning` skill when durable planning is actually needed. See the role and skill contracts for its trigger and persistence procedure.

### UI component intelligence

UI roles can use bundled component/source and framework-specific skills. Human setup notes are in:

- [`docs/ui_mcp_setup.md`](../docs/ui_mcp_setup.md)
- [`docs/uupm_setup.md`](../docs/uupm_setup.md)

---

## External integrations

These external projects provide optional integrations or source material referenced by bundled skills and documentation:

- GrayMatter memory: https://github.com/angelnicolasc/graymatter
- Alibaba `open-code-review`: https://github.com/alibaba/open-code-review
- Jeffallan `claude-skills` source material: https://github.com/Jeffallan/claude-skills
- UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

These links document provenance and optional integration surfaces.

---

## Prompt and evaluation design references

The pack is model-agnostic. These are design references rather than runtime dependencies or model-routing requirements. Vendor-specific guidance is adopted only when it generalizes to the pack's goals and survives pack-specific review/regression checks.

### OpenAI

- Current prompt-engineering guidance: https://developers.openai.com/api/docs/guides/prompt-engineering
- Rethinking skills/`AGENTS.md`/prompt scaffolding for newer coding models: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- Evidence-based persistent goals and bounded completion contracts: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- Turn real traces and feedback into reusable evals and harness changes: https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop
- Separate review/repair/validation and let observed validation decide success: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex
- GPT-6 agentic eagerness / clarification: do already-authorized read-only or reversible work needed to make a remaining choice concrete before asking: https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra

### Anthropic

- Agent-evaluation design using transcripts, outcomes, graders, and real failure cases: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Harness design with separate evaluator roles, concrete grading criteria, and deliberate simplification as model capability improves: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Claude Opus 5 prompting guidance on scope, over-verification, self-correction, and subagent use: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Claude Opus 5.5 guidance on user-facing progress visibility in long agentic/tool workflows: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- Claude Sonnet 5.5 prompting guidance on initiative/scope and proportionate coding verification: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5

### DeepSeek

- DeepSeek Harness code-review guidance: verify live state, review semantic contracts, and verify review claims instead of accepting them performatively: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-code-review/SKILL.md
- DeepSeek Harness prose guidance: direct verbs, one main action per sentence when ambiguity matters, stable terminology, preserve exceptions: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-doc/SKILL.md
- DeepSeek Harness skill-system design: keep standing prompt context small and load task-specific instruction bodies on demand: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/notes/archived/feature/2026-07-05-skill-system.md

### Z.ai / GLM

- GLM-5.3 agent engineering/evaluation: executable and verifiable long-horizon environments, separate verifier/judge signals, realistic end-to-end task completion: https://z.ai/blog/glm-5.3
- GLM-5.3 engineering feedback loops: turn ambiguous observations into testable hypotheses and validate changes against correctness/stability/performance criteria: https://z.ai/blog/glm-built-its-inference-infrastructure

These references may evolve with models and harnesses; inherited scaffolding should be re-evaluated rather than treated as permanent doctrine.

---

## Package contents

### Agents

The pack contains 19 agents:

`a11y-reviewer`, `auditor`, `build`, `code-orchestrator`, `debugger`, `devops`, `explore`, `general`, `librarian`, `project-planner`, `reviewer`, `semantic-checkpoint`, `session-evaluator`, `tester`, `trajectory-auditor`, `ui-auditor`, `ui-implementer`, `ui-orchestrator`, `ui-planner`.

### Skills

The pack contains 28 bundled skills:

`api-designer`, `repository-workflow`, `cpp-pro`, `delegation-control`, `git-provenance`, `golang-pro`, `graymatter-memory`, `change-contract`, `open-code-review`, `open-code-review-delegate`, `output-formatting`, `persistent-planning`, `playwright-expert`, `pr-readiness`, `python-pro`, `react-expert`, `resource-lifecycle`, `rust-engineer`, `secure-code-guardian`, `session-evaluation-control`, `session-evidence`, `typescript-pro`, `ui-component-sources`, `ui-routing-control`, `ui-ux-pro-max`, `verification-strategy`, `vue-expert`, `workflow-control`.

Pack-owned shared control skills are loaded explicitly by role/invocation boundary and do not autoinvoke. Specialist/advisory skills are discovered through the runtime/project-visible skill surface and loaded by the role that owns their integration.

---

## License

Pack-authored material is licensed under the **MIT License**. The copyright notice intentionally includes the project author's GitHub profile and must be retained with the license notice in copies or substantial portions:

`Copyright (c) 2026 bashrusakh (https://github.com/bashrusakh)`

Bundled third-party material keeps its upstream license. See [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) and [`LICENSES/`](../LICENSES/).

---

## Release and design references

| If you need… | Read… |
|---|---|
| Release notes | [`docs/releases/v31.22.md`](../docs/releases/v31.22.md) |
| Release history | [`CHANGELOG.md`](../CHANGELOG.md) |
| Historical role/protocol audit evidence | Separately delivered with the v31.16 bundle (not installed in the base pack); v31.22 validation accompanies its release bundle |
| Skill control / provenance manifest | [`evals/skill-control-spec.json`](../evals/skill-control-spec.json) |
| Shared semantic owner→consumer manifest | [`evals/semantic-ownership-spec.json`](../evals/semantic-ownership-spec.json) |
| Typed semantic-domain manifest | [`evals/semantic-domain-spec.json`](../evals/semantic-domain-spec.json) |
| Root/orchestrator section-placement map | [`evals/root-orchestrator-section-map.json`](../evals/root-orchestrator-section-map.json) |
| Runtime residency / audience map | [`evals/runtime-residency-spec.json`](../evals/runtime-residency-spec.json) |
| Semantic transition scenarios | [`evals/semantic-transition-traces.md`](../evals/semantic-transition-traces.md) |
| Source-to-generalized-rule preservation method | [`docs/semantic-design-source-audit.md`](../docs/semantic-design-source-audit.md) |

Release validation is defined in **§21 of [`docs/semantic-design-manual.md`](../docs/semantic-design-manual.md)**. A distributable release must pass the **previous-release preservation review** using the prior published ZIP and final candidate, in addition to standalone gates.

---

<div align="center">

**OpenCode Agent Pack v31.22**  
Semantic contracts · bounded delegation · evidence-grounded outcomes

</div>
