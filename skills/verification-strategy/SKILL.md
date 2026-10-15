---
name: verification-strategy
description: Use when an active role or implementation-contract activates nontrivial verification planning, evidence freshness, blocked-check handling, or broad verification/readiness claims. Owns verification layering, batching/cadence, and independent-tester activation; root owns authority/evidence semantics and implementation-contract owns shared engineering freshness/regression rules.
---

# Verification strategy

Apply root section 2.2 plus `implementation-contract` when active for evidence validity, preservation, freshness, and regression rules. This skill adds only verification-layer selection, batching/cadence, and the independent-tester checkpoint decision.

Verification has separate layers; do not turn them into a ceremonial agent chain:

1. **Implementation-local evidence** — `@debugger`, `@build`, `@ui-implementer`, or another mutation role runs the applicable checks after its affected edit/package and reports exactly what they prove.
2. **Independent verification checkpoint** — invoke `@tester` only when the request explicitly asks for independent verification/reproduction, the change crosses a meaningful integration/shared/stateful boundary, implementation-local evidence is insufficient/uncertain, or user/project policy requires an independent pass. Package completion alone is not a trigger.
3. **Remote/host evidence** — CI/status checks validate the published candidate in its remote environment and do not automatically require another local `@tester` run when the candidate is unchanged.

A work-package boundary is primarily a mutation/scope boundary, not automatically a verification-agent boundary. Several related packages may accumulate implementation-local evidence and then receive one independent `@tester` checkpoint when they form a coherent behavioral/integration state. Conversely, a risky package may deserve an earlier checkpoint when later work depends on that result.

When `@tester` is invoked, give it the **complete affected verification boundary** plus available changed/preserved/invariant and target-state context. The tester owns command selection, execution, and reporting under its role contract; do not fragment one known boundary into ceremonial repeated invocations.

Use root evidence freshness to decide what must be re-run after state changes; this skill decides only the affected verification layer/batch. For owned-PR readiness, preserve the reviewed Base SHA + Candidate HEAD identity supplied by `pr-readiness`/`git-provenance` and do not substitute workspace-only evidence for target-bound proof.

If an affected required check cannot run, report the blocker and keep that verification boundary unresolved. Implementation may continue only inside an already-established safe work package when later work does not depend on the blocked result; do not expand the design merely to route around unavailable evidence. Lifecycle-dependent handling remains governed by `pr-readiness` and the active workflow-entry/user gate.
