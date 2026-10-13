# Contract / protocol audit — v30.82 beta

## Scope

v30.82 changes one runtime role contract: `debugger`. No role permissions, delegation topology, root semantic owner, skill contract, installer control flow, UI-role contract, or publication/gate semantics change.

The change operationalizes an existing debugger obligation rather than adding a new one: root §2.2.1 still owns authority/evidence fidelity; root §§7.2–7.3 still own right-level correction and case-to-verification semantics; `debugger` now has a stronger role-local procedure for applying those owners while diagnosing and closing a bugfix.

## Debugger execution contract

The characteristic correction loop remains:

1. bind the exact symptom and candidate state;
2. separate defect evidence from caller/reviewer remediation advice;
3. trace root cause and owning boundary;
4. select the smallest right-level fix;
5. return focused and preserved-behavior evidence.

v30.82 strengthens steps 3–5 with a bounded falsification loop:

- for a non-trivial bug, concretize only the materially relevant established case classes before fix selection;
- choose semantically different representatives capable of falsifying the root-cause/fix hypothesis;
- preserve material target conditions for external grammar/API/tool/runtime/environment claims;
- when an assignment premise or explicit patch constraint conflicts with stronger behavior/evidence, distinguish a real authoritative implementation constraint from lower-authority diagnostic/remediation detail;
- reset the hypothesis when lower-authority detail is contradicted; stop/escalate if genuinely authoritative constraints conflict;
- before return, falsify the final mechanism again and refuse to count correlated self-authored tests as closure for an established class.

This is method specialization, not a second semantic policy owner.

## Handoff composition

No caller→debugger edge changes. Existing `code-orchestrator → debugger` and other reroute semantics already require the defect proposition, governing behavior/invariant, evidence, affected boundary, and exact state while keeping suggested remediation non-binding unless independently established. v30.82 makes debugger robust even when a handoff still contains an incorrect factual premise or over-specific mechanism.

A direct exact implementation constraint remains binding when its authority is genuine and it is consistent with higher-priority behavior. The new rule does not let debugger discard explicit requirements under the label of "hypothesis".

## Preservation boundary

The falsification requirement is proportional:

- it applies to materially relevant classes already established by the task/repository/root contract;
- it does not require arbitrary cross-products or invented edge classes;
- simple local bugs can remain simple when one focused reproduction and nearest preserved behavior adequately discriminate the hypothesis;
- environment/version probing is required only when that condition materially affects the proposition;
- inability to establish a material class produces an evidence gap, not automatic redesign or a ritual independent-review stage.

## Regression evidence

ST-80…ST-82 exercise the debugger-specific failure classes. ST-83 and ST-84 preserve existing reviewer/orchestrator semantics exposed by the same audit window without changing those runtime contracts. Static policy regressions require the debugger case-map/falsification, target-fidelity, contradictory-handoff, correlated-test, and reset language to remain present, and require all 84 transition cases to retain their fixture/stop-point structure.

Role topology/classification remains unchanged. The existing contract/protocol and role-handoff audits continue to test the closed-world relation set and role executability.

These are static/contract regression classes; they do not constitute fresh isolated behavioral replay of ST-01…ST-84.
