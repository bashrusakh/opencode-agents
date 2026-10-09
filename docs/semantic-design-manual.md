# Semantic Design Manual for Agent Instructions

## Purpose

This manual explains how to turn developer guidance, real agent traces, and project requirements into durable model-agnostic agent semantics without accumulating brittle prompt rituals.

It is a **design manual**, not runtime policy. `AGENTS.md` remains the canonical runtime policy for this pack.

The goal is not to copy vendor prompts. The goal is to preserve the reusable behavior behind them:

- who owns a decision;
- what authorizes a requirement;
- what evidence can prove a claim;
- when delegation adds value;
- where an instruction should live;
- what observable action must follow from the rule;
- how to verify that the rule still produces the intended behavior on current models and runtime surfaces.

## 1. Separate four kinds of truth

Do not put every useful statement into one prompt layer. First classify it.

### 1.1 Authority

Authority answers: **what is required or allowed?**

Typical sources:

- current user intent and explicit approvals;
- applicable project rules;
- safety/runtime/tool ceilings;
- an artifact the user explicitly adopted as a specification, limited to its normative outcomes, acceptance criteria, and explicit constraints.

Authority is claim-level. A document, reviewer, test, or child agent is not globally authoritative merely because some statement inside it is valid.

### 1.2 Evidence

Evidence answers: **what do we know about the current system or candidate?**

Examples:

- code and configuration facts;
- current repository state;
- tool output;
- tests and benchmarks;
- runtime traces;
- independent review findings;
- reproducible failure cases.

Evidence can support a requirement or implementation claim. It does not create product authority by repetition.

### 1.3 Mechanism

Mechanism answers: **how will an established outcome be achieved?**

Examples:

- a selector shape;
- a synchronization primitive;
- an API route;
- a particular helper or callback;
- one implementation architecture among several compatible choices.

Do not promote mechanisms into acceptance criteria unless they are explicitly required or are a necessary consequence of the established outcome.

### 1.4 Runtime fact

Runtime facts answer: **what can the actual harness/tool/API do?**

Examples:

- OpenCode agent modes and permissions;
- child-session context behavior;
- tool parameter constraints;
- OpenChamber session-read behavior.

A semantic rule cannot override runtime reality. When the observed runtime contradicts the documented contract, fix or bound the runtime assumption instead of adding prompt mythology around it.

---

## 2. Build semantics from outcomes, not procedures

A durable rule starts with an observable outcome.

Bad starting point:

> Always run reviewer, then tester, then verifier.

Better starting point:

> Do not claim completion until the material behavior changed by the task has evidence appropriate to its risk and state.

The second form leaves room for the current model and project to choose the cheapest valid mechanism.

A useful semantic contract normally defines:

1. **Outcome** — what must be true.
2. **Verification surface** — what evidence can establish it.
3. **Preserved constraints** — what must not regress.
4. **Boundary** — scope, tools, files, systems, or authority limits.
5. **Iteration policy** — how the next action is chosen when evidence says the outcome is not yet met.
6. **Blocked condition** — when the agent must stop and report instead of inventing a path.

This is the model-agnostic abstraction behind goal-oriented agent instructions.

---

## 3. Convert every material inference into a claim

A material decision about any of these is a claim:

- framing;
- required behavior;
- scope;
- ownership;
- invariant;
- fix level;
- product/domain policy;
- publication or destructive authority.

For each material claim, ask:

1. What authorizes it?
2. What evidence supports it?
3. What conclusion is that evidence supposed to prove?
4. Can the same evidence exist while the conclusion is false?
5. Does the reverse direction also need proof?

If the evidence-to-conclusion link is incomplete, keep the statement as a hypothesis or unresolved choice.

### Counterexample test

A compact way to catch semantic overreach is:

> Construct one plausible state where the evidence is still true but the proposed requirement or conclusion is false.

If such a state exists, the evidence is insufficient to establish that semantic claim.

---

## 4. Put each rule at one owning layer

Instruction duplication is not robustness. It creates drift and conflicts.

Use this placement model.

### Root standing policy

Put a rule in root only when it must govern many unrelated workflows before role selection or delegation.

Examples:

- authority hierarchy;
- gated actions;
- shared evidence rules;
- general delegation ownership;
- user-facing communication cadence.

### Role prompt

Put a rule in the owning role when it governs only that role's responsibility.

Examples:

- reviewer report contract;
- tester refusal to fix failures;
- orchestrator consumption of a semantic gate verdict.

### Skill

Use a skill for conditional procedural knowledge that should load only when relevant.

The skill description should be short and precise enough to answer **when this applies**. Put the full procedure in the skill body and supporting references.

### Project documentation

Keep project-specific commands, architecture, constraints, and conventions in their project-owned documents. Global agent policy should point to them conditionally rather than copying them.

### Runtime adapter/tool

Put behavior in runtime code when it is actually a tool/API contract, not a reasoning preference.

Do not compensate for a broken pagination API, permission boundary, or session topology with semantic prose if the runtime can be corrected.

---

## 5. Use progressive disclosure

Standing context should contain only rules needed often enough to justify permanent prompt cost.

A good structure is:

```text
root policy
  -> short routing/activation rule
  -> role or skill selected by task
  -> detailed reference only when needed
```

Do not preload the full corpus “just in case.”

Progressive disclosure is especially important because:

- unused instructions consume context;
- overlapping instructions can contradict each other;
- a broad skill description causes false activation;
- model capability changes can make old scaffolding actively harmful.

### Maintenance test

For every standing rule, periodically ask:

> What measured failure happens if this instruction is removed?

If the answer is unknown, the rule is a candidate for removal, relocation, or an eval experiment.

---

## 6. Define role ownership before delegation

Before adding a specialist, decide who owns the user-facing workflow.

### Manager-owned bounded specialist

Use this pattern when:

- the parent must synthesize the final result;
- the specialist performs a bounded capability;
- the parent owns scope, next action, escalation, and publication.

The specialist owns **HOW inside the assignment**, not the surrounding workflow.

### Ownership handoff

Use a handoff only when the specialist should actually own the next conversational branch or workflow responsibility.

Do not simulate a handoff merely because a specialist has useful expertise.

### New role test

Add a role only if at least one of these materially improves:

- capability isolation;
- permission/policy isolation;
- prompt clarity;
- independent judgment;
- trace legibility.

Do not add a role merely to create another check.

---

## 7. Delegate conditionally, not ritually

Delegation is useful when the task benefits from:

- isolated context;
- parallel independent workstreams;
- a genuinely independent judgment;
- a specialist capability that should not pollute the parent context.

Work directly when the task is:

- simple;
- sequential;
- tightly stateful across steps;
- cheaper to resolve with a few direct tool calls;
- not improved by independent context.

### Session continuity

Continuity follows the assignment, not the role name.

- New independent assignment or judgment -> fresh child context.
- Deliberate continuation of the same specialist-owned workstream -> continuation may preserve useful state.
- Same agent type invoked again -> does **not** by itself justify reuse.

This keeps independent judgments independent without destroying useful stateful work.

---

## 8. Chain only where the intermediate state matters

Do not decompose every multistep task into explicit orchestration.

Use an explicit chain when the intermediate output must be:

- inspected;
- graded;
- approved;
- branched on;
- persisted for another session;
- used as a hard workflow boundary.

Otherwise let a capable model handle ordinary multi-step reasoning internally.

A semantic checkpoint is justified only when a material candidate is about to turn uncertain semantics into mutation. It is not a universal pre-edit ceremony.

---

## 9. Verification must be proportional and state-bound

Verification is not a fixed stage count.

### Evidence belongs to the state it checked

Bind important evidence to the exact candidate state:

- ref/SHA;
- dirty state where relevant;
- base/head pair for a diff or PR;
- runtime/config state when it changes behavior.

### Match evidence to the claim

Examples:

- syntax check -> syntax claim;
- focused regression -> covered behavior;
- integration test -> integration contract;
- end-to-end environment check -> end-to-end outcome;
- review -> judgment about the inspected candidate, not proof that runtime behavior succeeded.

### Avoid over-verification

Do not require independent reviewer/tester/reverification after every small unit of work.

Invoke an independent stage when:

- policy requires it;
- risk/non-obviousness makes independence valuable;
- state changed enough to stale the relevant evidence;
- the task sits beyond what the current implementation role reliably validates alone.

When a model already performs a behavior reliably, legacy scaffolding that forces the same behavior can waste context and tokens or produce duplicated work.

---

## 10. Separate judgment, mutation, and proof when the separation adds value

A strong repair loop can use three distinct responsibilities:

```text
review / diagnose
    -> identify candidate defect or delta
repair
    -> make bounded changes
validation
    -> execute the artifact and determine what remains
```

The important semantic property is not “three agents.” It is that:

- review findings are not automatically proof;
- the repair step does not define success;
- validation observes the changed system;
- validation failure becomes evidence for the next iteration.

These responsibilities may be performed by separate roles, separate calls, or a simpler workflow depending on task risk and current model capability.

---

## 11. Build feedback that can drive the next action

Useful feedback has three properties.

### Local

Tie the signal to a specific path, state, input, transition, or hypothesis whenever possible.

“Tests failed” is weaker than “this input takes this branch and produces this wrong state.”

### Timely and cheap enough

Use the smallest validation surface that can answer the current question. Do not deploy the entire system when a focused test can falsify the hypothesis.

### Objectively verifiable

Logs and correlations can suggest a cause. A controlled experiment or appropriate reference check establishes whether the proposed cause/change actually explains the behavior.

### Layered feedback

Local checks and end-to-end checks have different jobs:

- local checks eliminate wrong hypotheses quickly;
- end-to-end checks establish that the local improvement survives the real workload and introduces no material regression.

---

## 12. Improve the harness from traces, not anecdotes

When a real workflow fails:

1. Capture the trace or reconstruct the observable workflow.
2. Identify the earliest material divergence.
3. Classify the cause before changing prompts.
4. Separate:
   - missing evidence;
   - runtime/tool defect;
   - ordinary execution error;
   - clear instruction violation;
   - true instruction ambiguity;
   - true reusable instruction gap.
5. Convert the reusable expected behavior into an eval/regression case.
6. Change the narrowest owning harness layer.
7. Rerun the same eval plus nearby preservation checks.
8. Keep the change only if it improves the measured behavior without unacceptable regressions.

### Do not patch prompts for every failure

A failure does **not** imply an instruction gap.

If the existing instruction clearly covered the behavior, the correct response may be:

- execution fix;
- better tool implementation;
- stronger evidence retrieval;
- improved test fixture;
- runtime bug fix;
- no prompt change at all.

This is one of the most important protections against prompt accretion.

---

## 13. Evaluate both the transcript and the outcome

A polished final answer can coexist with a failed real-world result.

Agent evaluation therefore needs two views.

### Transcript / trace

Use it to inspect:

- tool choices;
- intermediate decisions;
- scope changes;
- retries;
- delegation behavior;
- evidence handling;
- token/turn/tool-call cost.

### Outcome / environment state

Use it to determine whether the requested real condition actually became true.

For important behavior, combine the grader that best fits the property:

- deterministic/code-based checks;
- model-based judgment for nuanced criteria;
- human judgment where preference or policy cannot be reduced safely.

Do not use one grader type for everything.

---

## 14. Write semantic rules so an action can be derived from them

A good semantic rule contains enough information to determine behavior, not merely a principle slogan.

Use this template:

```text
WHEN <trigger/state>
ACTOR <role/owner>
MUST / MAY / MUST NOT <observable action>
BECAUSE / EVIDENCE <what establishes the need>
BOUNDARY <what this does not authorize or imply>
IF BLOCKED <stop/escalation behavior>
```

You do not need to render those labels literally in runtime prompts. They are a design checklist.

### Example

Weak:

> Be careful with subagents.

Derivable rule:

> Start a new specialist assignment or independent judgment in fresh child context. Continue an existing child only when deliberately continuing the same specialist-owned workstream; role identity alone does not justify reuse.

The second form predicts an action in a concrete case.

---

## 15. Preserve qualifiers, exceptions, and modality

Semantic loss often happens during summarization and delegation.

Preserve distinctions such as:

- must vs may;
- default vs fallback;
- supported vs currently wired;
- absence vs unknown;
- evidence vs authority;
- recommendation vs adopted requirement;
- temporary workaround vs desired outcome;
- conditional alternative vs active choice.

Use stable terminology and direct verbs. Split stacked instructions when ambiguity can change behavior. A shorter sentence is not better if it destroys a condition or exception.

---

## 16. Communication is part of the harness contract

User-facing narration should be informative without becoming another execution log.

### Before tools

Use one compact startup statement/block that says what the agent is about to do and the relevant boundary. Do not add a second prose plan around it.

### During work

Update the user only when there is:

- a material finding;
- a blocker;
- a meaningful change of direction;
- a decision where steering would materially help.

State the finding/change and the next action. Do not narrate routine tool use or completed substeps.

### Final response

Lead with the outcome. Include only material evidence, verification, blockers, risks, and publication/cleanup state that actually applies.

### Delegated reports

Optimize for the recipient agent, not for ceremony. Return the decision/finding, material evidence, unresolved blocker, and state identity needed by the caller. Omit empty sections and repeated context.

---

## 17. Long-running work needs durable state only when the task needs it

For genuinely long-running or multi-session work:

- decompose into tractable work packages;
- persist the authoritative task state in structured artifacts;
- make handoffs reconstructable;
- bind completed evidence to the state it checked.

Do not create persistent plans, sprint machinery, journals, or handoff documents for short work merely because the harness supports them.

Every persistence mechanism encodes an assumption that the model cannot carry the task without it. Test that assumption periodically.

---

## 18. Human authority remains at objectives, boundaries, and risk

Even highly autonomous engineering agents still need externally established:

- objectives;
- acceptance constraints;
- destructive/publication boundaries;
- risk policy;
- unsupported-domain choices.

The agent may propose hypotheses, mechanisms, and experiments. It may not silently convert those proposals into product authority.

---

## 19. The semantic-design workflow

Use this process when adding or changing agent semantics.

### Step 1 — Observe

Start from one of:

- an explicit new requirement;
- a real trace failure;
- a measured recurring failure pattern;
- a runtime capability change;
- a vendor/model behavior change that may invalidate old scaffolding.

### Step 2 — Classify before prescribing

Ask which layer failed:

```text
authority?
evidence?
execution?
runtime/tool contract?
role/capability boundary?
instruction ambiguity?
instruction gap?
```

Do not write a new prompt rule until the failure is actually semantic/instructional.

### Step 3 — State the expected observable behavior

Write what the agent should do in the failing scenario without naming the incident, repository, or implementation trick.

### Step 4 — Find the owner

Choose exactly one canonical owner:

- root policy;
- role;
- skill;
- project rule;
- runtime/tool;
- test/eval only.

### Step 5 — Bound it

Record what the rule does **not** imply.

This prevents a local fix from becoming a new general policy.

### Step 6 — Write the smallest actionable rule

Prefer trigger + actor + action + boundary over explanatory prose.

### Step 7 — Build a semantic regression matrix

Include at least:

- the motivating failure in generalized form;
- a nearby case that should **not** trigger the rule;
- a case where the rule would overreach if phrased too broadly;
- a preservation case for an existing valid workflow.

### Step 8 — Run the round-trip test

Hide the original source/manual from the reviewer and ask:

> Given only this synthesized rule/manual and scenario X, what should the agent do?

Compare that action to the source guidance.

A summary is semantically complete only if the important action and important exception can be reconstructed.

### Step 9 — Check prompt cost and duplication

Ask:

- Can an existing rule already produce the behavior?
- Can this live in a conditional skill instead of root?
- Did we copy the same semantic rule into multiple roles?
- Did the change create a mandatory stage where only a conditional judgment was intended?

### Step 10 — Re-evaluate after model/runtime upgrades

Delete or weaken scaffolding when current models reliably handle the behavior without it. Keep only load-bearing instructions demonstrated by evals, policy boundaries, or hard runtime needs.

---

## 20. Anti-patterns

### Incident-to-policy overfitting

Bad:

> When PR discussion label X exists, always wait.

Better:

> When an applicable project policy makes an external discussion/state a prerequisite, treat that state as a gate; otherwise it is evidence/context, not an automatic blocker.

### Mechanism canonization

Bad:

> Use callback Y because the checkpoint mentioned it.

Better:

> Preserve the established behavior and checked bounds; ordinary implementation mechanics remain implementation-owned unless independently required.

### Ritual verification

Bad:

> Every change must use tester + reviewer + final verifier.

Better:

> Reuse fresh evidence and invoke independent judgment only when policy, risk, state change, or measured model weakness makes it valuable.

### Prompt patching a runtime bug

Bad:

> Add more instructions telling the model to try harder to retrieve complete history.

Better:

> Verify the tool/runtime contract; fix the runtime or expose a reliable completion signal/pagination mechanism.

### Derived authority laundering

Bad:

> Reviewer says policy X is required -> assignment says policy X is required -> test expects policy X -> therefore user required X.

Better:

> Preserve the chain as evidence. Establish product authority independently before treating X as acceptance.

### Full-context preload

Bad:

> Read every architecture/testing/deployment document before every edit.

Better:

> Load the document whose domain applies to the current task.

---

## 21. Release checklist for semantic changes

Before shipping a prompt/harness semantic change, verify:

- [ ] The motivating failure is established, not inferred from a summary alone.
- [ ] The failure is not better classified as execution, evidence, test-fixture, or runtime/tool error.
- [ ] The expected behavior is stated independently of the incident.
- [ ] Authority and evidence are not conflated.
- [ ] Optional mechanisms remain optional.
- [ ] The rule has one canonical owner.
- [ ] Standing prompt growth is justified; otherwise use conditional disclosure.
- [ ] Delegation/checking is conditional rather than ritual unless policy requires it.
- [ ] Important state identity is preserved.
- [ ] A negative/counterexample case prevents overreach.
- [ ] A preservation case protects a valid existing workflow.
- [ ] The synthesized rule passes the round-trip action test.
- [ ] Runtime/API assumptions were checked against the actual implementation when they are material.
- [ ] The final prompt is written with stable terms, direct actions, preserved conditions, and no unnecessary narration.

---

## Source families

This manual synthesizes the reference set already tracked by the OpenCode Agent Pack.

### OpenAI

- Prompt engineering: https://developers.openai.com/api/docs/guides/prompt-engineering
- Rethinking skills and prompts for GPT-6 Astra: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- Using Goals in Codex: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- Agent improvement loop with traces/evals: https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop
- Iterative repair loops: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex
- Orchestration and handoffs: https://developers.openai.com/api/docs/guides/agents/orchestration

### Anthropic

- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Prompting Claude Opus 5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Prompting Claude Sonnet 5.5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
- Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Harness design for long-running application development: https://www.anthropic.com/engineering/harness-design-long-running-apps

### DeepSeek Harness

- Code-review skill: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-code-review/SKILL.md
- Documentation/prose skill: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-doc/SKILL.md
- Skill-system design note: https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/notes/archived/feature/2026-07-05-skill-system.md

### Z.ai / GLM

- GLM-5.3 agent engineering/evaluation: https://z.ai/blog/glm-5.3
- GLM inference engineering feedback loop: https://z.ai/blog/glm-built-its-inference-infrastructure

### Runtime references kept separate from methodology

- OpenCode agents/modes/permissions: https://opencode.ai/v2/docs/agents
- OpenChamber control actions: https://github.com/openchamber/openchamber/blob/main/packages/web/server/lib/openchamber-control/actions.js
- OpenChamber control runtime documentation: https://github.com/openchamber/openchamber/blob/main/packages/web/server/lib/openchamber-control/DOCUMENTATION.md

See `docs/semantic-design-source-audit.md` for the source-to-action preservation check.
