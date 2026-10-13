# Contract / protocol audit — v30.85 beta

## Scope

v30.85 changes four existing role contracts but no role topology or permissions:

- `code-orchestrator`;
- `semantic-checkpoint`;
- `trajectory-auditor`;
- `session-evaluator`.

No implementation/debug/review/test/UI role or skill gains or loses substantive ownership. Root authority/evidence semantics remain canonical.

## Ownership split

The control plane is now explicitly owner-first:

| Role | Lifecycle question | Ownership effect |
|---|---|---|
| `code-orchestrator` | What does the whole task currently mean, what evidence/model changed, and what must happen next? | accountable workflow owner |
| `semantic-checkpoint` | Does the residual authority-bearing semantic proposition have enough authority for mutation? | independent semantic second opinion/gate |
| `trajectory-auditor` | Does the owner's residual longitudinal concern justify the proposed next transition? | independent trajectory second opinion |
| `session-evaluator` | Did the completed workflow preserve instructions/authority and behave as accountable ownership rather than pass-through/controller dependence? | post-hoc diagnostic only |

## `code-orchestrator` executability

New required core capabilities:

1. `owner_synthesis` — ingest evidence/hypothesis/recommendation separately, reconcile against task/current state, update whole-task model, decide, then delegate;
2. `owner_control_plane` — self-reassess trajectory first, use semantic checkpoint only for residual semantic authority, and invoke trajectory audit only for a concrete residual longitudinal question.

The contract explicitly rejects both:

- specialist recommendation -> direct next workflow transition;
- cumulative concern -> prefer controller instead of parent reassessment.

A narrow read-only factual reconciliation is permitted when it avoids pointless delegation, but it does not grant implementation/review/debug/deep-discovery capability.

## Live controller composition

### `code-orchestrator -> semantic-checkpoint`

Now a dedicated high-risk profile. The handoff must bind:

- owner reconciliation performed;
- exact unresolved semantic proposition;
- strongest authority/evidence;
- mutation boundary;
- why the owner cannot safely settle the authority relation;
- fresh independent checkpoint semantics;
- anti-overreach: routine technical owner/fix-level/abstraction changes under settled behavior are not sufficient by themselves.

### `code-orchestrator -> trajectory-auditor`

The existing high-risk profile is strengthened. The handoff must bind:

- task anchor;
- owner reassessment performed;
- current owner model;
- exact unresolved trajectory question;
- why primary evidence could not safely resolve it;
- relevant material transitions and session identity;
- bounded five-verdict semantics;
- controller anti-overreach.

The auditor remains read-only and does not become first-line correction clustering or architecture selection.

## Post-hoc evaluator composition

`session-evaluator` gains workflow-owner quality checks without creating a new live gate. It inspects:

- owner synthesis;
- task-model continuity;
- specialist pass-through;
- controller dependence/overuse/underuse;
- existing authority, assignment, review, verification, and failure-classification dimensions.

Its result remains diagnostic evidence and cannot create new task authority.

## Eval inventory

- roles: 19;
- closed-world role relations: 59/59;
- high-risk handoff profiles: 16;
- generic delegation contracts: 3;
- semantic transition scenarios: 106 (ST-01…ST-106).

ST-97…ST-106 specifically cover the new owner/control-plane semantics. The contract selftest also contains malicious pass-through and controller-first orchestrator fixtures that must fail.

## Claim boundary

Contract/static/handoff PASS establishes structural executability and regression coverage only. It does not substitute for fresh isolated behavioral replay of the new owner/controller behavior.
