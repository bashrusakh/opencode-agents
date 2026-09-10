# Changelog

This changelog summarizes user-visible workflow changes. Detailed rationale and before/after behavior for major releases lives under `docs/releases/`.

## v28.29

v28.29 keeps the v28.28 orchestration/PR lifecycle and corrects verification cadence across implementation, testing, review, UI, and audit roles.

- Implementation-capable roles now return **implementation-local evidence** as the default post-edit check layer.
- `@tester` is no longer a mechanical stage after every fix/work package/commit; it is an independent checkpoint used when the request, risk, integration boundary, evidence quality, or project policy justifies it.
- One tester invocation now covers the complete already-applicable verification boundary instead of splitting predictable focused/preserved/suite checks across repeated calls; an individual FAIL does not end the batch when independent remaining checks can still add useful evidence.
- Complexity work packages are mutation/scope boundaries first; independent tester checkpoints are placed at meaningful integration boundaries rather than after every package.
- UI orchestration no longer invokes tester merely because runnable frontend checks exist; `ui-implementer` returns local evidence first.
- Reviewer cadence is now explicit: final owned-PR Candidate review remains required; ordinary review runs at stable high-risk boundaries, consumes fresh implementation/tester/CI evidence, and uses only narrow spot-checks instead of repeating broad verification.
- Auditor batches related executable verification questions instead of invoking tester/reviewer once per finding, and its own checks are limited to narrow finding-specific spot-checks rather than duplicating broad tester/CI coverage.
- Added a general stage-economy rule: reuse fresh evidence and re-invoke specialists only when the target/evidence boundary materially changed, prior coverage was incomplete/blocked, or independence itself is required.
- Separate `@explore` is no longer triggered just because the exact bug/UI file is unknown; debugger/implementer may trace within a bounded assignment, while explore is reserved for materially broad/ambiguous mapping. Debugger also reuses fresh caller/tester/CI reproduction evidence instead of mechanically rerunning the same pre-fix failure.
- Accessibility review is also stage-economized: a UI-file/cosmetic edit alone does not trigger `@a11y-reviewer`; use it for materially accessibility-sensitive semantic/interaction changes or explicit policy. When both tester and a11y apply after implementation, functional/integration verification runs first so avoidable fixes do not immediately stale a11y evidence. An explicitly needed pre-implementation a11y consultation is advisory and is not mislabeled as a final implemented-state verdict.
- UI options/plan/audit modes are no longer collapsed into a forced “2–3 options” output; each mode now returns its actual deliverable and options are created only when materially distinct choices exist.
- UI orchestration now states the final reviewer handoff explicitly when root review cadence applies; owned-PR UI Candidates cannot skip the whole-change pre-push review.
- The v28.28 review-before-push Candidate HEAD lifecycle remains unchanged.

See [`docs/releases/v28.29.md`](docs/releases/v28.29.md) and [`docs/verification_strategy.md`](docs/verification_strategy.md).

## v28.28

v28.28 keeps the v28.27 routing/role model and makes long-running multi-agent and PR workflows more deterministic.

- Orchestrators now explicitly own scope, stage order, escalation, findings, and publication; specialists own execution details only inside delegated boundaries.
- Related state/lifecycle/protocol/concurrency/persistence findings escalate to one shared invariant model instead of repeated one-comment/one-patch loops.
- Reviewer findings are grouped by underlying invariant and final owned-PR readiness requires a whole-change base-to-local-Candidate-HEAD verdict.
- Owned PRs use a Draft → local Candidate HEAD → review → push exact reviewed SHA → remote checks → Ready lifecycle. Intermediate Draft repair pushes still do not require final review after every batch, and the final full review is not repeated merely because the unchanged reviewed SHA was pushed.
- Failing/blocked required verification may coexist with authorized Draft repair work but still blocks Ready/merge/release/completion.
- Nested orchestrators may choose child stages only when that authority was explicitly delegated.
- PR reports include the canonical PR URL; owned-PR readiness reports also include state and Candidate HEAD.
- OCR remains reviewer-selected unless user/project policy explicitly requires it.
- Agent modes/permissions and bundled UUPM content were not broadened/changed by this policy release.

See [`docs/releases/v28.28.md`](docs/releases/v28.28.md) for the detailed before/after explanation.

## v28.27

v28.27 consolidated the model-agnostic behavioral contract around semantic routing, hard role boundaries, evidence freshness, correct Git base semantics, safer test/review behavior, and command/docs consistency.

Earlier release history is not reconstructed here; use the repository/package history where available.
