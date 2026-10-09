# Semantic Design Source Preservation Audit

## Purpose

This audit checks whether `docs/semantic-design-manual.md` preserves the **actionable consequence** of the developer references used by the pack, rather than merely repeating their themes.

Method:

1. Extract a material action/recommendation from each source family.
2. Identify the synthesized manual rule that is supposed to preserve it.
3. Ask whether a reader who has only the manual could derive the same action in the representative scenario.
4. Mark `PASS`, `PARTIAL`, or `FAIL`.

A source does not need to be copied verbatim. It passes when the behavior and material exception survive abstraction.

## Preservation matrix

| Source | Original actionable guidance | Manual derivation | Result |
|---|---|---|:---:|
| OpenAI — Prompt engineering | Separate durable developer rules from task input; use clear instructions/examples/context; test/evaluate prompt behavior. | §§1, 4, 13, 14, 19 separate authority/context, choose one owner, use actionable rules and regression checks. | PASS |
| OpenAI — Rethinking skills/prompts | Shorten skill descriptions, use progressive disclosure, make doc loading contextual, remove stale scaffolding and unnecessary test rituals as model capability improves. | §§4–5, 9, 19 require short activation metadata, conditional loading, measured removal of scaffolding, and no ritual verification. | PASS |
| OpenAI — Goals in Codex | Define outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop condition. | §2 reproduces those six semantic fields as the default outcome contract. | PASS |
| OpenAI — Agent improvement loop | Start from real traces/feedback, turn recurring expectations into evals, change the harness, rerun the gate; do not reduce improvement to prompt tuning. | §12 explicitly defines trace → classification → eval → narrow harness change → rerun. | PASS |
| OpenAI — Iterative repair loops | Separate review, repair, and validation; let validation determine remaining delta and next repair. | §10 preserves judgment/mutation/proof separation and makes observed validation the next-iteration input. | PASS |
| OpenAI — Orchestration and handoffs | Use handoff when specialist owns the branch; use manager-owned specialists as bounded capabilities when the manager keeps final ownership; split only for real instruction/tool/policy differences. | §§6–7 make workflow ownership explicit and condition role/delegation creation on isolation/independence value. | PASS |
| Anthropic — Opus 5 | Explicitly limit response verbosity; one short pre-tool status; update only on important findings/direction changes; outcome first; remove blanket verification/subagent instructions that cause over-verification. | §§9 and 16 plus the root communication invariant preserve cadence, concise reporting, and proportional verification. | PASS |
| Anthropic — Prompting best practices | Use subagents for parallel/isolated/independent work; direct execution for simple/sequential/stateful work; explicit chaining only when intermediate inspection/branching is needed; damp overengineering. | §§7–8 and §20 derive the same delegation/chaining decision and minimality boundary. | PASS |
| Anthropic — Sonnet 5.5 | Steer initiative so work completes without premature check-ins but stops at requested scope; add stronger real checks when observed behavior shows completion claims without execution evidence. | §§2, 9, 19 preserve completion/blocked boundaries and treat model-specific verification scaffolding as symptom/eval-driven rather than universal. | PASS |
| Anthropic — Demystifying evals | Evaluate both transcript and environment outcome; use appropriate code/model/human graders; run multiple trials when variability matters. | §13 explicitly separates transcript and outcome and chooses graders by property. Trial-count policy is intentionally not universalized, but variability remains an eval-design concern rather than a runtime ritual. | PASS |
| Anthropic — Harness design | Decompose long tasks and persist structured handoff state when needed; simplify harness components empirically as models improve; evaluator is valuable only beyond reliable solo capability. | §§9, 17, 19 require conditional persistence/evaluation and measured removal of non-load-bearing harness components. | PASS |
| DeepSeek — code review | Verify live base/head; review semantic contracts and real consumers; challenge speculative generality; use negative controls; verify reviewer claims rather than agreeing performatively. | §§1, 3, 9, 12, 19 bind evidence to state, require counterexamples, reject speculative scope, and classify findings before accepting them. | PASS |
| DeepSeek — documentation/prose | One owner per durable fact; execute claimed operations; remove unreproduced claims; stable terms, direct verbs, explicit actor/action, preserve modality/exceptions. | §§4, 14–15 and release checklist preserve fact ownership, action-derivable prose, stable terminology and exceptions. | PASS |
| DeepSeek — skill system | Keep catalog metadata small, disclose full instruction bodies on demand, keep deterministic skill resolution, avoid injecting every skill body into every request. | §§4–5 derive conditional skill loading and minimal activation metadata. Provider-specific registry mechanics are correctly left runtime-specific. | PASS |
| GLM-5.3 | Train/evaluate in executable, verifiable, realistic long-horizon environments; use independent verification/judging and both end-to-end completion and fine-grained criteria. | §§9, 13, 17 require realistic state-bound outcomes plus focused criteria; independent judgment is conditional on value/risk rather than mandatory everywhere. | PASS |
| GLM inference engineering | Turn ambiguous failures into local, timely, objective feedback; test hypotheses with controlled experiments; use local checks for diagnosis and end-to-end checks for final acceptance; humans own objectives/bounds/risk. | §§11 and 18 reproduce those responsibilities and the layered validation loop. | PASS |
| OpenCode runtime docs | `mode`, permissions, and child-session topology are runtime facts; subagents use fresh child context and permissions are hard ceilings. | §§1.4, 6–7 explicitly separate runtime capability from semantic authority and use fresh context for new independent assignments. | PASS |

**Result: 17/17 PASS.**

## Reverse derivation spot checks

These checks start only from the manual, then ask for the action expected by the original source.

### Case A — a database skill has a broad description and is loaded for every DB-related task

From manual §§4–5:

- narrow the activation description to the actual workflow;
- keep full instructions in the skill body;
- load them only when the workflow applies.

This reproduces the OpenAI/DeepSeek progressive-disclosure action.

**PASS**

### Case B — a coding task is simple, but the harness forces explorer → reviewer → tester → verifier

From manual §§7–9 and §19:

- direct execution is preferred for simple/stateful work;
- independent stages require policy/risk/measured value;
- remove stale scaffolding if evals show no loss.

This reproduces Anthropic/OpenAI guidance against ritual delegation and over-verification.

**PASS**

### Case C — a reviewer says an implementation mechanism is required and the next agent implements it as acceptance

From manual §§1–3:

- reviewer statement is evidence, not authority;
- mechanism remains implementation-owned unless explicitly required or necessary for the established outcome;
- unresolved product semantics return to the workflow owner.

This reproduces the pack's generalized claim-authority rule without needing the original incident.

**PASS**

### Case D — an agent gives a polished “done” answer but the environment was not changed successfully

From manual §13:

- transcript quality is not outcome proof;
- inspect environment state with an appropriate deterministic/outcome grader.

This reproduces Anthropic's outcome-vs-transcript distinction.

**PASS**

### Case E — performance drops after a change and logs correlate one subsystem with the slowdown

From manual §11:

- use the correlation to form a hypothesis;
- choose a local controlled experiment that can falsify it;
- retain the change only after objective validation;
- use end-to-end checks for final workload acceptance.

This reproduces the GLM dense-feedback guidance.

**PASS**

### Case F — a long task spans sessions

From manual §17:

- decompose only as needed;
- persist structured authoritative task state and handoff context;
- do not impose the same artifacts on short work;
- periodically test whether the scaffold remains load-bearing.

This preserves Anthropic long-running harness guidance while retaining the simplification lesson.

**PASS**

### Case G — agentic work has noisy narration

From manual §16:

- one compact pre-tool status;
- updates only for material findings/blockers/direction changes;
- final begins with outcome;
- no routine tool narration.

This reproduces the Claude Opus 5 action directly.

**PASS**

## Abstraction choices that were intentionally not copied

The manual does not universalize:

- vendor-specific model names or effort settings;
- fixed trial counts;
- XML as a mandatory prompt syntax;
- provider-specific skill registry internals;
- a fixed planner/generator/evaluator topology;
- a fixed reviewer/tester sequence;
- model-specific verification prompts that are recommended only when a measured behavior needs them.

Those details either belong to a specific runtime/model or are examples of a broader semantic rule already preserved above.

## Audit verdict

**PASS.** The manual retains the important observable actions and exceptions of the tracked developer references while removing provider-specific implementation detail and fixed rituals.

The strongest unifying rule is:

> Start from an authoritative outcome and observable evidence; put the smallest actionable rule in the layer that owns it; delegate and verify only where they add measured value; use real traces and outcome evals to decide whether the harness needs another rule or less scaffolding.
