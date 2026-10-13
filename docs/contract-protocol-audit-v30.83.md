# Contract / protocol audit — v30.83 beta

## Scope

v30.83 adds one delegated read-only role, `trajectory-auditor`, and one new delegation edge from `code-orchestrator`. The role is intentionally separate from both existing semantic lifecycle roles:

- `semantic-checkpoint` — pre-mutation, candidate-local semantic readiness;
- `trajectory-auditor` — mid-workflow, cumulative trajectory / next-transition justification;
- `session-evaluator` — post-hoc causal/compliance diagnosis after completed workflow.

No existing implementation/review/test/debug/UI role loses or gains its substantive ownership.

## Role executability contract

The new characteristic loop is:

1. recover the current task anchor from primary session evidence rather than trusting the parent packet;
2. reconstruct only material evidence -> interpretation -> action -> result -> acceptance-effect transitions;
3. distinguish acceptance/enabling/diagnostic/no-material progress so intermediate staged work is not falsely treated as failure;
4. test proposition lineage and repeated correction shape for drift, laundering, erosion, and clustered boundaries while preserving independent-defect counterexamples;
5. judge only the proposed next transition with bounded verdict semantics.

The role cannot mutate, shell, delegate, repair, publish, review code as a substitute for `reviewer`, diagnose/fix as `debugger`, select architecture as `project-planner`, or classify pack defects as `session-evaluator`.

## Handoff composition

The `code-orchestrator -> trajectory-auditor` packet binds:

- current task anchor;
- trigger;
- parent/material child session identity;
- material transitions and their end-to-end acceptance effects;
- current strategy/hypothesis;
- proposed next transition;
- workflow-owner rationale.

The packet is explicitly a report/index, not proof. The auditor uses the existing `session-evidence` owner to check material claims against primary history.

`code-orchestrator` consumes the result without transferring workflow ownership. `continue` authorizes only the audited next transition; `reanchor` restores lost framing; `reassess` blocks another mutation on the current strategy pending bounded read-only reassessment; `checkpoint-required` uses the existing semantic gate; `unverified` is not a pass.

## Anti-overreach boundary

The integration does not create a fixed stage after every correction. It is not triggered solely by turn/session/commit/review counts. Isolated ordinary defects, explicit staged work before its final milestone, and evidence-backed independent blockers remain direct-flow counterexamples.

The repeated-correction trigger is evidence-shaped: cumulative local success plus another same-path material blocker that is not already demonstrably independent. The auditor may still return `continue` when the accumulated evidence supports the current strategy.

## Static audit result

The candidate contract/protocol audit reports all 19 roles executable with no REVIEW/FAIL findings. Closed-world role topology is 59 discovered / 59 classified, with 15 high-risk handoff profiles and 3 generic delegation contracts. The new role uses the canonical `session-evidence` skill and introduces no mutation/publication capability.

## Regression boundary

ST-85…ST-94 are the new trajectory-specific behavioral specifications. Static guards verify that all 94 cases retain the standard fixture/stop-point shape, and targeted mutation probes are used to show the gate fails when task-anchor recovery, anti-overreach controls, or bounded verdict semantics are removed.

These checks are prerequisites, not a substitute for fresh isolated model replay.
