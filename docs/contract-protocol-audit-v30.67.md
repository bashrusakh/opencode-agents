# Contract / protocol audit — v30.67 beta

v30.67 tightens the release-blocking role/protocol audit after v30.66 proved too permissive. The goal remains falsification: a role does not pass because it contains expected nouns, points to root policy, or is long enough.

## What was wrong with v30.66

The v1 checker treated many dimensions as keyword-presence predicates. `procedure` could pass from a matching heading plus a few bullets, and terms such as `evidence`, `unknown`, `ownership`, or `verification` could satisfy a dimension even when they appeared only descriptively or only in the final result section. That made false PASS plausible for thin routed roles.

## v2 contract model

For every routed role the v2 audit checks four independent surfaces:

1. **generic execution skeleton** — role-local method, action-bearing steps, conditional decision rules, evidence/verification, stop/escalation, and result semantics;
2. **profile-specific core loop** — the characteristic method of the capability, such as symptom→cause→fix→rerun for debugging or current-state→fault-layer isolation→authorized reversible action→postcondition for operations;
3. **sparse-evidence review** — prompt length is diagnostic only, but unusually sparse role-local evidence cannot silently become PASS; it becomes release-blocking `REVIEW` until semantically adjudicated or strengthened;
4. **cross-role protocol composition** — producer output, parent transformation, consumer input, and consumer standing contract remain one interface.

The checker evaluates method-oriented evidence outside the final Result section so a role cannot satisfy its working method merely by promising to report a word.

## Anti-gaming self-tests

Synthetic fixtures now prove that:

- keyword-stuffed implementation text fails;
- an operational role with authorization/verification/rollback but no diagnostic isolation fails its profile-specific core loop;
- a compact discovery role with a real target→trace→corroborate→handoff method is not hard-failed solely for size;
- producer-side implementation certification is rejected at a handoff boundary.

## Current v30.67 audit result

`python evals/contract-protocol-audit.py` blocks promotion with:

- **FAIL: 7 roles**
- **REVIEW: 2 roles**
- **PASS: 8 roles**

| Role | Status | Main reason |
|---|---|---|
| `a11y-reviewer` | FAIL | weak exact-target/evidence/adversarial/stop semantics |
| `auditor` | FAIL | no explicit reconciliation contract for conflicting/partial specialist results |
| `build` | PASS | explicit pre-edit proof, ownership, falsification, final self-review and escalation |
| `code-orchestrator` | PASS | explicit routing, clean-handoff construction and bounded result consumption |
| `debugger` | REVIEW | strong core loop, but compact role-local evidence is too sparse for automatic structural PASS |
| `devops` | FAIL | authorization/rollback/verification exist, but fault-layer/root-cause isolation before mutation is not operationalized |
| `explore` | REVIEW | useful bounded discovery rules exist, but the role-local contract is compact enough that semantic adjudication is required instead of silent keyword PASS |
| `general` | FAIL | no executable research/analysis method or unknown/evidence discipline |
| `project-planner` | PASS | current-state/pattern inspection, ownership/choice discipline, sequencing and verification/risk plan are explicit |
| `reviewer` | PASS | full independent judgment contract |
| `semantic-checkpoint` | PASS | explicit semantic authority/classification/boundary contract |
| `session-evaluator` | PASS | explicit trace/evidence/failure-classification contract |
| `tester` | PASS | exact-state binding, derived verification set, discriminating evidence and bounded result semantics |
| `ui-auditor` | FAIL | mostly inspection topics; weak method, coverage and stop semantics |
| `ui-implementer` | FAIL | no mandatory final-state/final-diff self-review gate |
| `ui-orchestrator` | PASS | explicit routing, handoff construction, stage selection and result reconciliation |
| `ui-planner` | FAIL | weak ownership/fix-level and escalation semantics |

`plan` is not a current package-owned routed role. The old package-owned `agents/plan.md` was renamed to `project-planner.md` in v30.25; historical references to `@plan` are not active v30.67 routing edges. The active package role audited here is `project-planner`.

## Interpretation

A PASS is not behavioral proof. A REVIEW is not a cosmetic warning: promotion remains red until the role is strengthened or the generic criterion is semantically disproved with an overreach/preservation case. A FAIL is a contract finding. None may be converted to PASS by adding candidate-specific exceptions.

## Promotion status

**NOT PROMOTION-READY.**

Static retention and audit self-tests can pass while this contract/protocol gate remains red. Fresh isolated behavioral replay of the semantic-transition suite is still a separate evidence class.
