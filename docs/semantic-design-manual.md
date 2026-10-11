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

### 1.1 Task-semantic authority

Task-semantic authority answers: **what outcome, acceptance condition, constraint, or requested approach is established for the task/product?**

Typical sources:

- current user intent and explicit approvals;
- applicable project rules that govern the task/product contract;
- an artifact the user explicitly adopted as a specification, limited to its normative outcomes, acceptance criteria, and explicit constraints.

Safety/runtime/tool ceilings, hard role boundaries, gates, workflow policy, and instruction precedence answer a different question: **what may this actor/workflow do or claim?** They constrain execution and can block an otherwise valid requested action, but they do not thereby become product acceptance criteria or user-established task semantics.

Task-semantic authority is claim-level. A document, reviewer, test, or child agent is not globally authoritative merely because some statement inside it is valid.

Adopting a source does not transfer authority to every statement it contains. When the distinction matters, classify source propositions as normative outcome/acceptance/constraint, factual diagnosis/evidence, proposed mechanism, example/rationale, or optional recommendation/fallback. When a source is adopted as the task/specification, its normative task propositions inherit user authority; the other propositions keep their own semantic class unless separately adopted or required by another authority.

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

Evidence also has a state and provenance. Preserve the distinction between intended/planned action, reported completion, independently verified completion, reported failure/uncertainty, and independently verified failure/uncertainty. A completion report proves that completion was reported; without independent execution evidence it may remain unverified, but it is not equivalent to mere intent. Conversely, announcing a next step does not prove that it happened. When records disagree, preserve the disagreement instead of collapsing it into one stronger or weaker state.

### 1.3 Mechanism

Mechanism answers: **how will an established outcome be achieved?**

Examples:

- a selector shape;
- a synchronization primitive;
- an API route;
- a particular helper or callback;
- one implementation architecture among several compatible choices.

Do not promote mechanisms into acceptance criteria unless they are explicitly required or are a necessary consequence of the established outcome. A mechanism may still be selected by the role that owns the relevant implementation/design choice because it is adequate, necessary, or the strongest viable way to preserve the established outcome; upstream roles may propose alternatives, but that is reasoning/context rather than new authority or a downstream recipe.

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

### Proposition-preservation test

Authority bounds more than the maximum action level. Compare a candidate with the material proposition actually established and classify the relation when it matters:

- **preserved** — the established proposition is unchanged;
- **refined** — only implementation mechanics become more specific;
- **strengthened / weakened** — the force or result changes;
- **substituted** — a materially different approach, outcome, or constraint replaces the established one;
- **unverified** — available evidence cannot establish the relation.

A replacement is not merely a refinement because it is safer, narrower, technically better, lower-permission, or aimed at the same broad goal. Evidence may establish that the original proposition is blocked or non-viable, but that does not itself authorize a materially different replacement. Semantic substitution needs separate proposition-scoped authority unless the replacement was already established as a conditional alternative and evidence establishes that condition. Adequacy of the replacement does not create that authority.

### Evidence-fidelity test

Evidence is proposition-scoped too. A test, reproduction, benchmark, trace, or review finding proves only the proposition whose material preconditions, qualifiers, scope, and observable outcome its actual fixture/setup and oracle preserve. Translating an invariant into weaker, stronger, or ambiguous verification is semantic drift even when the artifact passes.

For a material proof obligation, ask: **what must be true for this evidence to distinguish the governing proposition from a counterexample, and does the actual artifact guarantee those conditions?** A failing artifact establishes a product defect only after that validity check; otherwise classify the result as a verification/test defect, environment-dependent evidence, or unresolved proof gap. Negative controls are useful when they materially increase discrimination, not as a ritual.

---

## 4. Put each rule at one owning layer

Instruction duplication is not robustness. It creates drift and conflicts.

Use this placement model.

### Root standing policy

Put a rule in root only when it must govern many unrelated workflows before role selection or delegation.

Examples:

- instruction/action precedence and task-semantic authority rules;
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

When auditing ownership, inspect the **cross-layer graph**, not only each file in isolation. A rule can have one apparent owner inside every file while still being duplicated across root, role, and skill. For every material state machine, lifecycle, or procedural integration, identify the canonical owner and verify that other layers only activate, constrain, consume, or report it.

A semantic role may reference a conditional integration, but provider/API/CLI invocation mechanics belong in the owning integration skill or runtime adapter unless the exact mechanic is itself part of that role's semantic responsibility.

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

### Assignment/role contract composition

A delegation prompt supplies instance-specific scope and context to the selected role; it does not replace that role's standing contract. Legitimate specialization can narrow the target, question, action ceiling, or requested evidence while preserving the role-owned obligations and result semantics that still apply. A deliberately partial diagnostic is valid when its boundary stays explicit, but its result cannot satisfy a broader stage.

Check both directions: could the assignment suppress or redefine a material role obligation, and could the caller later over-claim completion from a result that was intentionally partial?

### Role executability test

A routed substantive role needs more than a description plus a pointer back to root policy. Shared/root policy may own canonical semantics, but the role contract must still make the role-owned work executable. Proportional to the role, the contract should establish:

- what incoming assignment/context means and which parts are authority, evidence, constraints, or hypotheses;
- the role-owned procedure or decision sequence before it acts or returns a judgment;
- what evidence/self-check is sufficient for the role-local result and what is not;
- what the role must not absorb from adjacent roles;
- stop, blocker, escalation, or handoff behavior when the role cannot complete its obligation inside the boundary;
- result semantics: what the output proves, what remains partial/unknown, and what the caller may safely infer.

Do not count a generic statement such as “apply AGENTS.md” as the role-owned procedure when the root itself says detailed execution belongs to the role. A short contract is fine when the capability is simple, but substantive mutation, diagnosis, independent judgment, planning, orchestration, or verification needs enough local procedure that a weaker conforming model can derive the intended work without inventing the missing algorithm.

The audit question is not “is this prompt long enough?” It is:

> If the root/orchestrator routes a valid assignment here, can the role derive the required sequence, evidence threshold, stop conditions, and output semantics from its own standing contract plus shared policy?

If not, treat that as a role-contract gap even when another role later catches the mistake.

### Role contract semantic shape

Standardize substantive role contracts by **semantic function**, not by mandatory Markdown headings or prompt length. A reviewer should be able to point to one primary locus for each of these functions:

1. **Ownership** — what capability/stage the role owns, what it does not own, and which adjacent-role boundary matters.
2. **Invocation** — what a valid assignment means for this role: target/state/mode/action ceiling plus which incoming items are authority, constraints, evidence, or hypotheses when material.
3. **Method** — the characteristic role-owned action/decision loop, including the profile-specific false-success/adversarial defense needed to avoid the first plausible but wrong completion.
4. **Boundaries** — stop/blocker/escalation/reroute behavior, unavailable-evidence handling, and conditions under which the role must not absorb another stage.
5. **Result** — what the returned output proves, its target/evidence/coverage limits, what remains partial/unknown, and what the caller may safely infer.

The preferred reading order is roughly `Ownership → Invocation → Method → Boundaries → Result`, after the shared contract. This is a semantic shape, **not a five-heading template**:

- a simple role may combine Invocation or Boundaries with Role/Method when the primary locus remains obvious;
- an orchestrator may split Method across routing, workflow, evidence, and escalation sections;
- a verdict role may place target identity/evidence preconditions in a dedicated section instead of naming it `Invocation contract`;
- do not add a summary/restatement merely to make all five labels appear. Duplicate wording is justified only when decision-point salience prevents a concrete failure mode.

Standardization therefore asks two questions together: **is every semantic function present and easy to locate, and is each function expressed once at its strongest owner rather than copied for cosmetic uniformity?** A role can fail this shape despite having the expected headings, and can pass it without those headings when the functions are unambiguous.

When creating or materially revising a role, use this shape before polishing wording. When auditing an existing role, prefer moving/merging existing semantics only when the current placement obscures ownership or execution; do not churn an already clear role solely for heading consistency.

### Role lifecycle requalification

A prior PASS does not automatically survive a topology or ownership change. Re-run the role-executability and relevant handoff-interface tests whenever a change does any of the following:

- makes an existing role newly routable/delegable, broadens its `mode`/entry topology, or adds a new caller;
- moves a substantive responsibility, decision, proof obligation, or procedure from root/caller/skill into the role;
- removes or compacts role-local wording because the same semantic rule appears elsewhere;
- changes which role owns implementation, diagnosis, planning, verification, independent judgment, or publication work;
- converts an advisory/reference relationship into a mutation, verdict, or workflow-owning handoff.

For owner moves and compaction, run a **method-preservation test** before deleting the old wording: after the move, can the receiving role still derive the complete role-local action/decision sequence, evidence threshold, false-success defense, stop/escalation behavior, and result semantics without relying on the removed text? Canonical-owner deduplication is not successful if it leaves the owner with policy but no executable method.

Treat role topology as runtime semantics. A role promoted from primary-only to delegated/all use is a newly exposed interface even if the file contents did not change; it must be requalified against the weaker-conforming-model test and every new caller edge before release.

### Handoff interface composition test

Audit every material producer → parent/transformation → consumer edge as a protocol interface, not only as three individually valid documents. Record:

- what the producer output actually means and explicitly does not mean;
- what semantic classes the parent may preserve, omit, reframe, or add;
- what the consumer is allowed to infer from the resulting assignment;
- which role owns unresolved implementation/design/judgment choices;
- whether partial, advisory, diagnostic, or stale evidence can be laundered into full authority, proof, or completion.

A per-file PASS is insufficient when the composition is contradictory. For example, a producer that says a mechanism is technically adequate or may be forwarded unchanged conflicts with a consumer contract that says upstream mechanisms are only hypotheses. Fix the interface at the earliest owning stage rather than requiring the downstream model to resist contaminated context.

For release gating, maintain a **closed-world discovered handoff inventory** over pack-owned root/agent contracts. Every current `@role` relation must be classified (for example routing policy, direct delegation, reroute, return-to-parent, output-package, or boundary/reference), and the discovered set must exactly match the classified set. A newly discovered relation without classification and a stale classification with no remaining runtime relation both fail release. Classification is only topology evidence: material delegation edges still need caller→callee protocol checks.

Adding a new caller→callee relation therefore requires two proofs before promotion: the callee still passes role executability under the new context, and the edge satisfies the callee invocation contract without laundering caller hypotheses/partial evidence into authority or completion.

### New role test

Add a role only if at least one of these materially improves:

- capability isolation;
- permission/policy isolation;
- prompt clarity;
- independent judgment;
- trace legibility.

Do not add a role merely to create another check.

### Preserve decision space in exploratory delegation

An exploratory, planning, architectural, or diagnostic handoff should preserve the decision space established by the user. Pass the outcome, constraints, evidence, exclusions, and unresolved questions. Parent-originated candidate solutions, examples, preferences, or implementation ideas remain non-exhaustive hypotheses unless authority actually constrains the task to those alternatives.

When the purpose is an independent recommendation, avoid preselecting the solution architecture. A downstream choice among a parent-supplied list does not prove that the list was complete or user-authorized. A useful check before the handoff is: if the delegate returned an approach outside the parent's current candidates, would the original request allow it to be considered? If yes, the assignment must not make the parent candidates the closed choice set.

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

Separate coverage dimensions when they matter:

- **structural coverage** — which files/diff entries were inspected;
- **behavioral coverage** — which material claims/invariants were exercised;
- **evidentiary coverage** — which claims have evidence that actually discriminates the governing proposition from relevant counterexamples.

Full structural coverage does not imply full behavioral or evidentiary coverage.

### Derive review depth from the actual candidate

Acceptance/task scope and review surface are different objects. Acceptance scope establishes what change is requested; the actual candidate establishes which changed behaviors must be judged for correctness. If a nominally local patch materially alters a destructive boundary, authorization, ownership/reservation, lifecycle, concurrency/locking, persistence/migration, or another high-risk behavior, reviewing that boundary is not scope expansion. It increases review depth inside the candidate without creating implementation authority for unrelated fixes.

An explicitly selected implementation mechanism remains a proposition-scoped constraint, not proof that the candidate is adequate. Review still judges correctness, preserved behavior, fix level, maintainability, security, performance/resource effects, and regressions. A user may explicitly accept a specific tradeoff or temporary workaround; that bounds the review proposition to the exact accepted envelope but does not authorize additional collateral degradation or turn the workaround into production-grade design.

For changed guards/classifiers, preserve both material sides of the governing invariant when both matter. Review whether a prohibited state can be accepted and whether an established permitted state can be rejected. Use the nearest meaningful counterexample rather than assuming conservative rejection is inherently safe.

When a candidate materially changes the amount, placement, frequency, or scaling of work on a performance-sensitive path, compare it with Base behavior or an established expectation at representative scale. Trace meaningful fan-out/asymptotic changes, repeated I/O/network/process/retry/cache work, allocation or memory growth, and other resource costs. Do not invent a budget or require a benchmark by ritual; establish material impact or keep the claim as an evidence gap.

For changed work executed under a contended/global lock, transaction, scheduler/state guard, or similar critical shared resource, trace reachable changed calls far enough to expose blocking or materially expensive work and qualitative fan-out/cardinality. Filesystem, network, process, retry, recursive traversal, and comparable latency-bearing operations deserve explicit attention when their placement can change contention or liveness. Do not infer a defect from cost alone; establish the material impact or keep the claim as an evidence gap.

When a candidate reconstructs or reconciles shared state, review the relevant operations that mutate the same semantic state as a composition rather than validating the new mechanism only in isolation. Create/update/delete/restore/reconstruct paths can each be locally valid while their sequence violates the governing invariant. Use discriminating round trips when correctness depends on distinguishing intentional state from accidental absence.

Treat fallback/recovery reachability as part of the behavioral claim. A branch that exists syntactically does not establish that representative supported inputs can reach it through earlier guards, transformations, and failure points. If reachability is not established, the supported-behavior claim remains an evidence gap.

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

### Keep release gates adversarial to the candidate

A release check exists to falsify the candidate, not to confirm that expected wording is present. Separate at least three evidence classes:

1. **structural/retention checks** — schema, dependencies, known owner/consumer invariants, and whether a known guard disappeared;
2. **contract/protocol checks** — split into (a) role executability and (b) caller→assignment→callee edge compatibility. Every routed substantive role must be executable, and every real handoff must satisfy the callee invocation contract without laundering authority, proof, recipes, or completion; an individually correct caller and callee do not prove their edge;
3. **behavioral replay** — whether representative traces actually produce the required behavior under the evaluated model/runtime.

Mutation tests show that a known guard is load-bearing; they do not prove that the guard set is complete. Keyword/presence checks show structural evidence; they do not prove semantic adequacy. Do not add a role-specific exception merely because a new generic audit makes the current candidate fail. First decide whether the audit criterion itself is wrong using a nearby preservation/overreach case. If the criterion remains valid, keep the release red until the contract is fixed.

For routed-role executability, do not reduce the contract check to prompt size or vocabulary. Audit two layers independently:

- **generic execution skeleton** — role-local action sequence/decision rules, evidence threshold, stop/escalation and result semantics;
- **profile-specific core loop** — the characteristic method that makes that capability distinct (for example symptom→cause→fix→rerun for debugging, current-state→fault-layer isolation→authorized reversible action→postcondition for operations, or target→reference/call-flow trace→corroboration→bounded handoff for discovery).

A role that merely mentions the right nouns can still be non-executable. Conversely a compact role can be sufficient. Prompt length is diagnostic only and must never create PASS, REVIEW, or FAIL. Severity follows semantics: **FAIL** means the role lacks a foundational boundary or essential characteristic core-loop capability needed to execute safely; **REVIEW** means the core loop is executable but a material correctness/coverage branch remains under-specified. PASS additionally requires a characteristic false-success/adversarial defense, not just generic vocabulary. REVIEW is resolved only by strengthening the generic criterion/role contract or by a documented semantic adjudication with an overreach/preservation case; it is not a candidate-specific waiver.

The checker itself needs synthetic anti-gaming fixtures: keyword-stuffed thin roles must fail, profile-specific method gaps must fail even when generic dimensions are present, and a compact executable role must not hard-fail solely for size.

A gate may report **FAIL with useful findings** and still be a successful evaluation artifact. Do not redefine success as “all checks say PASS.” The goal is early error discovery and calibrated confidence.

### Trace semantic transitions end to end

Static ownership and cross-layer composition checks are necessary but insufficient. A material proposition can remain valid in each file while changing incorrectly at a handoff, retry, skill activation, verification step, or final summary.

For representative release scenarios, trace the proposition across the complete applicable workflow rather than grading documents independently. At each material transition record:

- incoming and outgoing proposition/state;
- qualifiers, preconditions, exclusions, unresolved conditions, and proof obligations that must survive;
- **what changed**;
- **why it changed** and the source of that cause;
- whether that source is task-semantic authority, evidence, implementation discretion, runtime fact, or another established class;
- what authorizes the resulting transition when authority is required;
- proposition relation separately from the evidence-state transition.

The central test is not merely whether a delta exists. It is whether the **cause is sufficient for that exact delta**. Evidence may establish that an earlier path is blocked without authorizing a materially different replacement. A downstream agent, loaded skill, repeated recommendation, or successful local artifact does not create provenance merely by producing a new state.

Treat a material semantic delta without identifiable and sufficient provenance as drift. Also test preservation cases so this rule does not freeze legitimate implementation refinement, user-authorized closed choices, project-local constraints, or evidence that merely resolves uncertainty.

For a negative replay, state explicitly whether the harness **injects** a faulty intermediate artifact at a named stage or expects the active upstream workflow to avoid producing that fault. Record the earliest observable stage that must preserve state or stop. Do not attribute an injected fault to the upstream role, and do not mix evidence-state changes such as uncertainty resolution into the proposition-relation taxonomy.

When a material authority-bearing interaction cannot be retrieved by a downstream semantic role, preserve provenance before dependent handoff rather than asking downstream roles to trust a later summary. A contemporaneous receipt can preserve the exact proposition, response, qualifiers, and source of the interaction; it is evidence of the interaction, not a new source of authority. Prefer the primary interaction whenever it remains retrievable.

For reproducible behavioral evals, attach the evaluated policy/runtime identity to the trace as metadata rather than user-visible prompt scaffolding. Version/package/root hashes, scenario identity, and model/runtime identity help determine which governing instruction set actually produced the trace without changing scenario semantics.

Convert observed failures into incident-independent synthetic regression scenarios. Preserve the semantic structure of the failure, not its repository names, UI labels, provider terms, or accidental implementation details. Run these scenarios in an isolated/fresh evaluation context; authoring-context agreement is not evidence that the candidate pack passes the replay.

For review-oriented regressions, distinguish isolated-path correctness from **composition correctness**. If independently valid projections/refinements can coexist, include a combined-state case; if a fallback depends on a prior stage failing, distinguish control-flow reachability from the prior stage's semantic success postcondition. When one layer owns an accepted or supported behavior domain, cross-layer tests must preserve that owner's domain rather than inheriting a narrower convenience representation or non-authoritative operational surface as an unstated precondition. Packaging/build/release matrices and similar operational subsets are evidence about their own surface unless authoritative policy makes them the governing domain.

---

## 14. Write semantic rules so an action can be derived from them

A good semantic rule contains enough information to determine behavior, not merely a principle slogan.

Name semantic states by their meaning, not by incidental presentation. Portable policy should not depend on UI colors, icons, badge names, local CI labels, repository-specific status vocabulary, or other origin-specific literal state values unless that representation is itself part of the governing contract. Translate presentation labels into the underlying semantic state before turning them into a reusable rule.

Treat a literal state/value in canonical policy as justified only when the pack explicitly defines it as a canonical semantic class/enum, or the exact external literal is itself part of the governing contract. Otherwise express the rule through the state's underlying meaning. Use a rename counterfactual: if the originating system renamed every local status/value while preserving their meanings, the reusable rule should remain complete and unambiguous. If it would not, the abstraction is too concrete.

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

For an independent judgment, fresh session identity is necessary but not sufficient. Keep prior verdicts, expected outcomes, parent conclusions, claimed-clean areas, and fix-history framing out of the initial judgment context; reconcile them after the independent result. A targeted re-review is different: known findings may be supplied, but the result must remain partial/incremental rather than masquerading as a fresh whole-scope judgment.

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
- selected/adequate mechanism vs required mechanism;
- intended action vs reported completion vs independently verified completion;
- temporary workaround vs desired outcome;
- conditional alternative vs active choice;
- non-exhaustive hypothesis vs exhaustive choice set;
- preserved/refined proposition vs semantic substitution.

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
- [ ] The rule has one canonical owner **across the full root → role → skill/runtime graph**, not merely within each file; consumers activate/reference the owner instead of restating its state machine or procedure.
- [ ] Every real caller→callee edge satisfies the callee invocation contract: required target/state/mode/action/evidence inputs are supplied, caller-originated solutions remain hypotheses unless authoritative, and deleting an edge-specific handoff guard makes an edge-level regression test fail even if both roles still pass individually.
- [ ] Every routed substantive role passes the role-executability test: shared/root policy may own common semantics, but the role itself contains enough role-owned procedure, profile-specific core loop, conditional decision logic, evidence/self-check, stop/escalation behavior, and result semantics to perform the delegated stage. Generic keywords alone are insufficient; prompt size is diagnostic only. `FAIL` and `REVIEW` follow semantic executability/severity, and PASS requires a characteristic false-success/adversarial defense in addition to the core loop.
- [ ] Every substantive role is readable through the semantic shape `Ownership → Invocation → Method → Boundaries → Result`: each function has one clear primary locus, merged/specialized sections are allowed, and no duplicate summary is added merely to satisfy a heading/template.
- [ ] Any role-topology/ownership change (new caller, `mode`/delegability expansion, responsibility/proof transfer, advisory→mutation/verdict transition) re-runs role qualification; an earlier PASS is not inherited merely because the role file itself was unchanged.
- [ ] Any deduplication/compaction or canonical-owner move that removes procedural wording passes the method-preservation test: the receiving role still has an executable role-local algorithm, false-success defense, evidence threshold, stop/escalation, and result semantics after the deletion.
- [ ] Every material producer → parent/transformation → consumer handoff is audited as one interface; individually valid files do not count as composition proof.
- [ ] The discovered pack-owned `@role` relation set exactly matches the classified handoff inventory. New/unclassified and stale classified edges both block promotion; topology classification alone does not waive material edge protocol checks.
- [ ] New routed roles/edges are discovered automatically or explicitly classified before promotion; an unclassified role/edge is a release finding rather than an implicit default.
- [ ] Release gates are adversarial to the candidate: unresolved generic contract/protocol findings keep promotion red unless the audit criterion is independently shown wrong by a preservation/overreach case. Do not add candidate-specific exceptions merely to recover PASS.
- [ ] Structural/static PASS and mutation PASS are treated only as evidence for known invariants/retention; they do not prove semantic completeness, role executability, handoff compatibility, or behavioral replay.
- [ ] Every stage/instrumentation hook has one explicit gating class. A diagnostic/non-gating hook must not inherit generic required-stage failure semantics that would change terminal outcome when the hook is unavailable.
- [ ] Semantic role prompts contain only role-owned semantics/integration points; provider/API/CLI retrieval or invocation mechanics live in a conditional skill/runtime adapter unless that mechanic is itself the governing contract.
- [ ] Audit findings are triaged by ownership/provenance before mutation: pack-owned canonical policy, pack-owned integration procedure, external/vendor skill content, project-local policy, and historical documentation are not interchangeable owners. Do not rewrite external/vendor semantics merely to make the pack look internally uniform; verify that root precedence/containment remains correct and change the external surface only when this pack intentionally owns that contract.
- [ ] Representative end-to-end semantic traces were replayed across the complete applicable workflow, not inferred from per-file inspection alone.
- [ ] For every material transition in those traces, the eval records what changed, why it changed, the cause/source, and whether sufficient authority/evidence exists for that exact resulting state; a blocker to an old path is not treated as automatic authority for a replacement.
- [ ] The replay set contains adversarial and preservation cases plus incident-independent regressions derived from established real failure classes, and was run in an isolated/fresh evaluation context.
- [ ] Standing prompt growth is justified; otherwise use conditional disclosure.
- [ ] Delegation/checking is conditional rather than ritual unless policy requires it.
- [ ] Fresh independent judgments isolate their initial context from prior verdict/expected-outcome framing; targeted re-review history is allowed only with explicitly partial/incremental verdict semantics.
- [ ] Important state identity is preserved.
- [ ] A negative/counterexample case prevents overreach.
- [ ] Reviewer depth follows actual candidate effects rather than issue wording alone: materially changed high-risk boundaries become review surfaces without becoming new implementation authority.
- [ ] When a changed guard/classifier has material allowed and prohibited sides, review checks both with meaningful counterexamples; when changed work runs under a contended critical resource, review traces reachable blocking/expensive work and qualitative fan-out without turning benchmarking into a ritual.
- [ ] Reviewer composition checks cover independently coexisting projections/refinements where isolated-path success would not prove the combined state; cross-layer accepted-domain checks keep the owning contract authoritative rather than inheriting a narrower local representation.
- [ ] Fallback/recovery review proves both control-flow reachability and any fallback-suppressing stage's semantic success postcondition; a successful return is not substituted for the required usable outcome.
- [ ] A preservation case protects a valid existing workflow.
- [ ] The synthesized rule passes the round-trip action test.
- [ ] Runtime/API assumptions were checked against the actual implementation when they are material.
- [ ] The pack declares one target host configuration generation for pack-owned runtime definitions; every agent frontmatter conforms to that generation, and legacy compatibility syntax is absent unless an explicit compatibility requirement justifies it.
- [ ] A host-schema migration is checked separately from permission-policy changes: action/resource/effect intent remains equivalent unless the release explicitly authorizes a policy delta.
- [ ] Every mandatory runtime dependency named by a role (required skill/tool/integration owner) is reachable under that role's **effective** host permissions; existence of the dependency and correctness of its ownership do not prove reachability.
- [ ] A static assertion about an active runtime invariant is checked against its canonical active owner/consumer surface directly; documentation/manual parity is tested separately and cannot satisfy a runtime-owner assertion.
- [ ] Static ownership/schema regression checks pass, but are not counted as evidence that end-to-end semantic replay passed.
- [ ] Every literal semantic state/value in canonical wording is either a pack-defined semantic class/enum or an exact external literal whose representation is contractual; otherwise the rule names the underlying meaning and survives renaming of incidental local values.
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
