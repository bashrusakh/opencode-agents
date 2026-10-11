# Contract / protocol audit — v30.66 beta

This audit is intentionally release-blocking. Its purpose is to find missing role execution contracts and incompatible handoff semantics, not to make the current candidate green.

## Evidence classes

The pack now separates:

1. **static/retention evidence** — schema, known owner/consumer invariants, dependency reachability, known rule retention;
2. **contract/protocol evidence** — routed-role executability and producer → transformer → consumer compatibility;
3. **behavioral replay evidence** — actual isolated semantic-transition runs under a named model/runtime.

A PASS in one class does not substitute for another.

## Current audit result

`python evals/contract-protocol-audit.py` returns **FAIL** with six unresolved findings. These findings were manually reviewed after the generic detector ran; no role-specific waiver was added merely to recover PASS.

| Role | Detector finding | Manual semantic review |
|---|---|---|
| `a11y-reviewer` | weak/missing state binding, adversarial/preserved behavior, stop/escalation | **confirmed gap** — the role has a useful accessibility checklist but does not clearly bind a final verdict to an exact/stable target or define what happens when final-state evidence is unavailable; preserved interaction/regression reasoning is implicit rather than operationalized |
| `auditor` | weak result interpretation/reconciliation | **likely gap** — specialist use and evidence rules are strong, but the role does not explicitly define how conflicting/partial specialist results constrain the synthesized audit status instead of being silently flattened |
| `general` | missing role-local procedure and unknown/gap discipline | **confirmed gap** — it is a bounded fallback description plus result contract, not an executable research/analysis method |
| `ui-auditor` | weak scope/input boundary, procedure, coverage limits, stop/escalation | **confirmed gap** — it lists UI topics to inspect but has little evidence/coverage procedure and no clear blocked/insufficient-evidence result semantics |
| `ui-implementer` | missing final-diff/self-review gate | **confirmed gap** — it has implementation and verification rules but lacks the implementation-local adversarial final-state review now required of the generic code builder |
| `ui-planner` | weak ownership/fix-level and stop/escalation | **likely gap** — it protects product/design decision space, but cross-layer ownership and stop/escalation when the plan requires a new owner/protocol are not explicit enough |

No cross-role recipe-laundering finding remains in v30.65/v30.66 on the currently modeled mutation edges; the v30.65 handoff fixes are therefore retained by the new protocol audit.

## What this audit does not prove

- A structural match for a role dimension does not prove the role executes it correctly.
- Six findings are not guaranteed to be the complete set of behavioral weaknesses.
- The absence of a protocol finding is not a behavioral replay PASS.
- Prompt length is not a quality metric; the audit asks whether the role-owned procedure is derivable and bounded.

## Promotion status

**NOT PROMOTION-READY.**

The static policy harness and contract-audit selftests pass, but the contract/protocol audit intentionally fails until the unresolved role findings are fixed or a generic criterion is independently disproved with a preservation/overreach case.
