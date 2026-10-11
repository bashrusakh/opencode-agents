# Contract / protocol audit — v30.74 beta

## Semantic-shape audit

The audit lens is `Ownership → Invocation → Method → Boundaries → Result`. Section names are evidence locators, not required template names.

| Role | Ownership | Invocation | Method | Boundaries | Result |
|---|---|---|---|---|---|
| `a11y-reviewer` | `Role` | `Invocation contract` | `Review method` + applicable checks | `Role` + review stop/evidence rules | `Result` |
| `auditor` | `Role` | specialist handoffs + `Target identity` | specialist use + audit/evidence/reconciliation | `Role` + specialist/reconciliation limits | `Result` |
| `build` | `Role` | `Role` + opening `Implementation` semantics | `Implementation` + pre-return falsification | `Role` + publication/escalation rules | `Final report` |
| `code-orchestrator` | `Role` + `Hard boundary` | `Delegation` + target/edit-baseline rules | role selection + workflow/review/evidence sections | hard boundary + findings/escalation/publication | `Final report` |
| `debugger` | `Role` | `Role` + workflow target/symptom entry | `Workflow` | complexity + `Guardrails` | `Result` |
| `devops` | `Role` | `Invocation contract` | `Diagnostic workflow` | role/action-ceiling + workflow stop/rollback | `Result` |
| `explore` | `Role` | `Role` + exploration-depth target rules | `Exploration depth` | read-only/bounded-discovery rules | `Result` |
| `general` | `Role` | `Role` + method objective/source boundary | `Method` | protected-capability/unknown stop rules | `Result` |
| `project-planner` | `Role` | `When to use this role` + delegated boundary | planning evidence + durable-plan semantics | role/use/authority limits | `Result` |
| `reviewer` | `Role` | `Target identity` + `Review integration` | review focus/full-rule/adversarial/fix-level sections | read-only role + evidence/coverage limits | `Result` |
| `semantic-checkpoint` | `Role` | role boundary + `Evidence to inspect` | `Checkpoint method` + evidence status | role boundary + verdict constraints | `Result` |
| `session-evaluator` | `Role` | role boundary + `Evidence to inspect` | audit method + finding classes/diagnosis | post-hoc/read-only + evidence/classification limits | `Result` |
| `tester` | `Role` | `Invocation contract` | `Verification workflow` | independent/read-only + invalid-evidence limits | `Result` |
| `ui-auditor` | `Role` | `Invocation contract` | `Audit method` | read-only/current-state/coverage limits | `Result` |
| `ui-implementer` | `Role` | `Invocation contract` | `Implementation workflow` | workflow escalation/evidence limits | `Result` |
| `ui-orchestrator` | `Role` + `Hard boundary` | delegated bounds + leaf handoff contracts | UI-stage selection + implementation workflow | hard boundary + cross-layer/parent return | `Final report` |
| `ui-planner` | `Role` | `Invocation contract` | `Planning method` | authority/unknown/escalation rules | `Result` |

**Verdict: 17/17 structurally clear; no runtime-role rewrite required for standardization.**

## Automated prerequisites

- contract/protocol audit: 17 PASS / 0 REVIEW / 0 FAIL;
- closed-world handoff inventory: 54 discovered / 54 classified;
- ST-64 protects semantic-function standardization from degrading into heading/template enforcement.

## Deferred capability

`librarian` remains a design TODO only. It is not part of the current role inventory and therefore does not alter the 17-role/54-edge runtime topology.
