---
name: delegation-control
description: Caller-side delegation contract for handoffs, child-session freshness, routing/fallback, evidence reuse/review cadence, and temporary-resource reconciliation. Load only when the active invocation is expected and allowed to dispatch/reconcile subagents.
metadata:
  opencode/autoinvoke: "false"
---

# Delegation Control

## Activation boundary

Load only when the active role/invocation both **may** and **should** dispatch/reconcile subagents. A `mode: all` role invoked as a delegated child does not inherit caller ownership unless its role contract explicitly says so. This skill grants no delegation capability.

The active caller remains accountable for scope, stage order, authorized actions, current findings, state identity, evidence consumption, and final claims.

## Handoff contract

Delegate when another role owns the next action or independent work materially improves correctness/context management. Do not delegate merely to enact a fixed stage list, and do not absorb prohibited work when delegation fails.

Each assignment defines objective, target/behavior scope, allowed action level, expected deliverable/evidence, stop/escalation boundary, and relevant state identity. Make the packet **minimally sufficient and reconstructable, not exhaustive**. Separate identity, authoritative outcome/constraints, unresolved question/action, evidence needed, and stop conditions. Omit settled chronology, superseded alternatives, duplicate evidence, parent internal reasoning, and accumulated session dumps unless the callee actually needs them. Compression that collapses semantic distinctions is a handoff defect.

Resolve workflow-level ambiguity needed to set those bounds; leave execution-local mechanics to the specialist. The assignment specializes but never replaces the selected role contract. It may narrow scope/question/action/evidence, but cannot waive role obligations, independence requirements, stop conditions, or verdict semantics. A narrow/targeted result remains partial and cannot impersonate a broader stage.

New material scope/direction/user decision/role/gated action returns to the caller. Apply root authority/evidence semantics to specialist output: returned evidence does not itself authorize new scope, acceptance, or a gated action.

## Delegated state boundary

The assignment's action ceiling applies to task-relevant state as well as content. A child may create incidental disposable execution artifacts only when they are intrinsic to the already-authorized action and do not rebind the authoritative target, change task-resource ownership/topology, or relocate/transfer pre-existing workflow state. A material state transition outside those bounds is a separate mutation, not an implementation convenience.

If the child discovers that completing the assignment requires such a transition, stop and return the required state/scope expansion to the caller before performing it. Correct output does not retroactively authorize an out-of-bound state transition. Resources validly created inside the delegated boundary still follow `resource-lifecycle`; that lifecycle contract reconciles resources but does not create mutation authority.

## Decision-space preservation

For exploratory/planning/architectural/diagnostic delegation, pass the established outcome, constraints, evidence, exclusions, and unresolved questions. Do not turn parent-generated candidate solutions/examples/preferences into an exhaustive choice set unless authority actually constrains the task that way. If useful, label candidate approaches as non-exhaustive hypotheses. Independent recommendation should receive the problem and authoritative constraints rather than a preselected architecture.

## Child-session freshness and independent judgment

Session continuity follows assignment continuity, not agent identity. Start a fresh child for a new specialist assignment or independent judgment; continue a child only when deliberately continuing the same specialist-owned workstream.

For independent judgment, pass target/state, authoritative task propositions with provenance/qualifiers, material implementation constraints, and inspectable evidence. Do not seed prior verdicts, expected answers, parent conclusions, claimed-clean areas, or fix-history framing. The fresh child does not resume parent task memory/checkpoints merely because the parent workflow is long-running. Do not disable, hide, or reconfigure an optional integration merely to manufacture freshness or independence; consider isolation reconfiguration only when actual task-specific contaminating content is observed, no clean invocation boundary is otherwise available, and the configuration change is authorized.

A requested whole-scope judgment receives the whole authoritative acceptance surface, not only the latest fix/risk slice. Structural inspection of the whole diff does not compensate for a partial semantic acceptance model. Targeted re-review may receive the finding it must re-check, but remains partial/incremental.

If a judgment will feed a gated downstream decision, state the exact **decision boundary**. A review/verdict establishes only the claim it evaluated; it does not itself satisfy or authorize a later Ready/merge/release/other transition with additional prerequisites.

## Routing, topology, and fallback

Execution topology comes from agent frontmatter: `primary` = top-level only, `subagent` = child only, `all` = either subject to role-local rules. Entry routing chooses a top-level owner; delegation routing chooses an invokable bounded executor. An entry target is not automatically a delegation target.

Generic entry defaults when role selection/transfer is actually needed:

- coordinated code/repository work -> `@code-orchestrator`;
- broad repository audit -> `@auditor`;
- focused non-UI implementation -> `@build`;
- architecture/sequencing -> `@project-planner`;
- external technical evidence -> `@librarian`;
- coordinated UI work -> `@ui-orchestrator`.

Generic leaf routing:

- discovery/tracing -> `@explore`; confirmed root-cause bugfix -> `@debugger`;
- verification/reproduction -> `@tester`; review -> `@reviewer`;
- CI/deploy/runtime -> `@devops`; external technical evidence -> `@librarian`; unmatched bounded research -> `@general`;
- UI implementation/audit/plan/a11y -> corresponding UI specialist.

The active role/role-specific workflow may add tighter discriminators. Preserve the active workflow owner unless policy explicitly transfers ownership. A failed/unavailable/rate-limited/hidden/skipped child does not transfer its capabilities to the caller or make a required stage pass. Retry only genuinely transient failures. Use a fallback only when the standing route explicitly permits it and it preserves scope, mutation/gate/delegation authority, independence, and workflow semantics.

A delegated orchestrator may choose leaf stages only inside its delegated domain and returns bounded assignments to the workflow owner when its role contract forbids another generation. Prefer serialized mutation; parallel mutation requires proven disjoint files/state/contracts.

## Evidence reuse and review cadence

A multi-agent workflow is not a fixed pipeline. Reuse fresh evidence. Re-invoke a specialist only when state change makes evidence stale, the prior assignment was incomplete/blocked, a new material boundary appears, or independent judgment is actually required. If a claimed root-cause fix fails materially, reassess the hypothesis before issuing a similar patch.

Explicit review-only work uses reviewer ownership. Otherwise use independent review when risk/non-obviousness materially benefits from it, not ritualistically after every package/test/commit. Resource-specific lifecycle rules (for example owned-PR final-candidate review) belong to their dedicated skill.

For **final whole-change review**, by default complete applicable implementation-local and independent verification that could invalidate or change the candidate **before** invoking the reviewer. Reconcile findings, perform needed corrections and affected re-verification, and establish the intended stable candidate first. Do not run a costly final whole-change review concurrently with unfinished candidate-invalidating verification merely to shorten elapsed time; honor the user's cost/latency priorities. Independent verification activities may run concurrently when their execution and evidence do not interfere.

Do not wait for checks unavailable at the current lifecycle stage (such as remote checks that require publication); identify them as pending, unavailable, or deferred, **never passed**. Early **targeted** review is appropriate for a bounded material question when it can avoid wasted implementation or verification effort; it remains partial and cannot replace final whole-change review. The workflow owner may choose a different ordering when there is a concrete, evidence-backed reason, making the tradeoff visible rather than silently consuming costly review on a mutable candidate.

## Workflow-created resources

Temporary resources created by the workflow must be reconciled before completion. When such resources exist, load `resource-lifecycle`; it owns resource identity, cleanup ownership/transfer, failure handling, terminal states, and reconciliation. Cleanup authorization remains with the active workflow-control/user gate or delegated action ceiling.
