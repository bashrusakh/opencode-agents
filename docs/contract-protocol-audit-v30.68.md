# Contract / protocol audit — v30.68 beta

v30.68 calibrates audit severity without changing any runtime agent contract from v30.67.

## Status semantics

- **PASS** — characteristic role core loop, decision/evidence discipline, stop/escalation, result semantics, and a profile-relevant false-success/adversarial defense are explicit enough to execute without inventing the missing method.
- **REVIEW** — the role is executable, but a material correctness/coverage branch remains under-specified. REVIEW blocks promotion.
- **FAIL** — a foundational boundary or essential characteristic capability is absent; the role cannot safely be treated as an executable owner for the routed stage.

Prompt byte/line count is reported only as diagnostic context and never changes status.

## Frozen pre-repair role matrix

| Role | Status | Main reason |
|---|---|---|
| `a11y-reviewer` | FAIL | weak target binding and no derived/adversarial affected-interaction review surface |
| `auditor` | REVIEW | executable audit orchestration, but conflicting/partial specialist evidence reconciliation is under-specified |
| `build` | PASS | pre-edit proof, owner/falsification, final self-review, bounded escalation |
| `code-orchestrator` | PASS | routing, clean handoff construction, bounded result consumption |
| `debugger` | PASS | symptom→cause→owner/fix→rerun plus failed-hypothesis reset |
| `devops` | FAIL | no explicit fault-layer/root-cause isolation before mutation |
| `explore` | PASS | bounded question→trace→corroborate→unknown/handoff loop despite compact size |
| `general` | FAIL | no executable research method or fact/inference/unknown discipline |
| `project-planner` | PASS | current-state/owner/choice/sequence/verification/risk plan |
| `reviewer` | PASS | independent exact-target judgment and adversarial review contract |
| `semantic-checkpoint` | PASS | authority/classification/boundary-not-recipe contract |
| `session-evaluator` | PASS | trace/evidence/failure-classification contract |
| `tester` | PASS | exact-state verification plan, discriminating evidence and bounded claims |
| `ui-auditor` | FAIL | checklist topics without complete scope→evidence→counterexample→coverage/stop method |
| `ui-implementer` | FAIL | no mandatory final-state/final-diff self-review/falsification gate |
| `ui-orchestrator` | PASS | stage routing, clean UI handoff construction and stage/result boundaries |
| `ui-planner` | FAIL | weak current-state ownership/alternatives/escalation method |

## Manual comparison

The independent manual audit produced the same `PASS=10 / REVIEW=1 / FAIL=6` matrix. This baseline is frozen before role repair so later green results cannot be obtained by changing the detector alongside the roles.

## Promotion status

**NOT PROMOTION-READY.** Runtime role repair begins only after this baseline.
