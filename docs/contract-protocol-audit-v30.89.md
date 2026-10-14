# Contract / protocol audit — v30.89 beta

## Scope

v30.89 changes the generic delegation/continuity contract plus `code-orchestrator`, `reviewer`, `session-evaluator`, `graymatter-memory`, and `pr-readiness`. It does not add/remove roles or delegation edges.

## Runtime semantic deltas

1. **Fresh-child continuity boundary** — long-running parent continuity stays with the workflow owner. A fresh independent reviewer does not run the parent's GrayMatter/checkpoint recovery; enabled recall capability alone remains non-contaminating, while actually injected/retrieved prior-task steering still contaminates freshness.
2. **Whole-scope acceptance model** — a whole-PR/whole-change target requires an authoritative acceptance model spanning the material PR/task surface. Structural `Coverage: full PR` remains distinct from semantic acceptance-model coverage.
3. **Qualifier preservation** — slice-limited/qualified reviewer evidence cannot be strengthened into whole readiness. Executable/live proof may remain explicitly deferred only after the whole semantic model was judged.
4. **Parent hypothesis boundary** — one-layer observations/parent technical inferences do not become `preserve`, `required`, or test oracles without governing authority or discriminating system evidence.
5. **Readiness reversal** — a related material blocker after readiness/publication triggers bounded owner reassessment before another local fix/review/Ready cycle; repeated reopenings widen the reassessment.
6. **Handoff ergonomics** — specialist packets are minimally sufficient/reconstructable; dense serialized session dumps and compression that blurs identity/scope/authority/evidence state are contract defects.

## Role / handoff audit

- role contracts: **19/19 PASS**;
- pack-owned role relations: **59/59 classified**;
- high-risk handoff profiles: **17**;
- generic delegation contracts: **3**;
- role/topology inventory: unchanged from v30.88.

## Prompt growth

`agents/code-orchestrator.md`: **42,794 → 43,361 bytes (+567, +1.3%)** after deduplicating the initial implementation of these guards. The new semantics are concentrated in handoff construction, whole-review consumption, and readiness reassessment rather than duplicated throughout the prompt.

## Evaluation

Semantic-transition inventory extends through **ST-118**:

- ST-113 fresh reviewer must not recover parent-task memory;
- ST-114 whole target requires whole acceptance model;
- ST-115 qualified slice verdict cannot become whole readiness;
- ST-116 parent technical inference cannot become preserved requirement/test oracle;
- ST-117 handoff must be minimally sufficient and reconstructable;
- ST-118 related blocker after readiness reopens the owner model.

Targeted destructive probes cover seven harmful mutations: latest-slice whole-review contract, qualifier laundering, parent-hypothesis laundering, serialized handoff dump, reviewer parent-memory recovery, GrayMatter parent-resume leakage, and Ready-reset without owner reassessment. All seven are blocked by promotion gates.

Static/contract/handoff gates are prerequisites only. Fresh isolated behavioral model replay of ST-113…ST-118 is **not** implied by PASS and is not claimed unless separately executed.
