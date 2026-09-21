---
name: verification-strategy
description: Use for nontrivial verification planning, evidence freshness, blocked checks, or claims that require current validation evidence. Root AGENTS.md remains authoritative.
---

# Verification strategy

Verification has separate layers; do not turn them into a ceremonial agent chain:

1. **Implementation-local evidence** — `@debugger`, `@build`, `@ui-implementer`, or another mutation role runs the narrowest relevant checks after its affected edit/package and reports exactly what they prove.
2. **Independent verification checkpoint** — invoke `@tester` only when the request explicitly asks for independent verification/reproduction, the change crosses a meaningful integration/shared/stateful boundary, implementation-local evidence is insufficient/uncertain, or user/project policy requires an independent pass. Package completion alone is not a trigger.
3. **Remote/host evidence** — CI/status checks validate the published candidate in its remote environment and do not automatically require another local `@tester` run when the candidate is unchanged.

A work-package boundary is primarily a mutation/scope boundary, not automatically a verification-agent boundary. Several related packages may accumulate implementation-local evidence and then receive one independent `@tester` checkpoint when they form a coherent behavioral/integration state. Conversely, a risky package may deserve an earlier checkpoint when later work depends on that result.

When `@tester` is invoked, give it the **complete affected verification boundary** plus available changed/preserved/invariant and target-state context. The tester owns selection and execution of the applicable verification batch under its role contract; do not fragment one known boundary into ceremonial repeated invocations.

Run the narrowest relevant tests/checks from project docs/config that are non-destructive and do not require unapproved secrets or production services. Prefer focused checks before broader suites.

Validation evidence is tied to the effective diff, relevant environment/configuration, and—during owned-PR readiness—the reviewed Base SHA + Candidate HEAD. Any later code, config, test, dependency, generated-output, head, or base change invalidates every result that change could affect. Re-run only the affected checks before claiming success.

Executable evidence is also **state-identity-bound**. A test/build/smoke result proves a named remote target or Candidate only when the executing workspace is proven to represent that state; otherwise report it as workspace-only/target-unverified. For target-bound verification, record the executing HEAD and relevant dirty-worktree state so a stale checkout cannot be mistaken for the supplied ref/SHA.

A focused passing check proves only the behavior it exercises. Passing server/service tests do not prove a changed frontend/UI boundary; passing UI tests do not prove persistence/migration behavior; one layer's evidence never substitutes for another affected boundary. Do not claim module-, package-, repository-, or project-wide verification unless the corresponding broader checks actually ran.

If required verification for an affected behavioral boundary cannot run, report the exact blocker. Implementation may continue only inside an already-established invariant/work package when doing so is still safe; do not keep expanding the design while its affected verification boundary is unavailable. An owned PR cannot move to Ready while mandatory candidate evidence is blocked or stale.

Do not manufacture a pass by deleting, skipping, weakening, broadening, or disabling assertions, snapshots, type checks, lint rules, coverage requirements, tests, or validation steps unless the normalized task intentionally changes that expected behavior and current project evidence supports the change.

Review evidence is Base-SHA + Candidate-HEAD bound. If either changes, affected review evidence is stale by default; retain it only when the recomputed effective diff and affected integration context are proven unchanged.

If checks cannot run, report the exact command and exact error/blocker. Never claim success when required checks are unknown, skipped without explanation, stale, or failing.
