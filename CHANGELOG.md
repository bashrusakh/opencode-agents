# Changelog

This changelog summarizes user-visible workflow changes. Detailed rationale and before/after behavior for major releases lives under `docs/releases/`.

## v28.28

v28.28 keeps the v28.27 routing/role model and makes long-running multi-agent and PR workflows more deterministic.

- Orchestrators now explicitly own scope, stage order, escalation, findings, and publication; specialists own execution details only inside delegated boundaries.
- Related state/lifecycle/protocol/concurrency/persistence findings escalate to one shared invariant model instead of repeated one-comment/one-patch loops.
- Reviewer findings are grouped by underlying invariant and final owned-PR readiness requires a whole-PR base-to-Candidate-HEAD verdict.
- Owned PRs use a Draft → Candidate HEAD → Ready lifecycle. Intermediate Draft repair pushes do not require final review after every batch.
- Failing/blocked required verification may coexist with authorized Draft repair work but still blocks Ready/merge/release/completion.
- Nested orchestrators may choose child stages only when that authority was explicitly delegated.
- PR reports include the canonical PR URL; owned-PR readiness reports also include state and Candidate HEAD.
- OCR remains reviewer-selected unless user/project policy explicitly requires it.
- Agent modes/permissions and bundled UUPM content were not broadened/changed by this policy release.

See [`docs/releases/v28.28.md`](docs/releases/v28.28.md) for the detailed before/after explanation.

## v28.27

v28.27 consolidated the model-agnostic behavioral contract around semantic routing, hard role boundaries, evidence freshness, correct Git base semantics, safer test/review behavior, and command/docs consistency.

Earlier release history is not reconstructed here; use the repository/package history where available.
