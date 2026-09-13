# Changelog

This changelog summarizes user-visible workflow changes. Detailed rationale and before/after behavior for major releases lives under `docs/releases/`.

## v28.34

v28.34 keeps the v28.33 workflow and strengthens right-level fix selection without adding a new stage or case-specific exception.

- Fix selection now starts from the end-to-end acceptance condition for the requested outcome, not from the nearest editable component.
- Before implementation, the chosen ownership/fix boundary must be capable of guaranteeing that condition across materially relevant paths, states, callers, partitions/instances, and lifecycle transitions.
- Local or per-partition guarantees do not count as proof of a system-level invariant unless their composition/aggregate behavior is established.
- If the proposed boundary cannot guarantee the required outcome, the workflow moves the fix level outward or escalates before coding instead of accumulating local patches.
- Planner, orchestrator, debugger, build, and reviewer role guidance now applies the same canonical fix-boundary principle.
- v28.31-v28.33 current-upstream freshness, repository state identity, and PR base-drift handling are retained unchanged.

See [`docs/releases/v28.34.md`](docs/releases/v28.34.md) for the detailed before/after explanation.

## v28.33

v28.33 adds base-drift handling to PR state identity.

- Final validation/review is bound to `Base SHA + Candidate HEAD`.
- Base is refreshed before final review, before PR publication, and before Ready.
- A moved base makes affected evidence stale by default; reuse requires proof that effective diff/integration context is unchanged.
- Reviewer/provenance output records the reviewed Base SHA.

See [`docs/releases/v28.33.md`](docs/releases/v28.33.md) and [`docs/pr_readiness.md`](docs/pr_readiness.md).

## v28.32

v28.32 extends current-upstream freshness into end-to-end repository state identity.

- Directly invoked roles own applicable freshness when no parent/orchestrator exists; delegated leaves still consume caller-supplied fresh target context instead of fetching redundantly.
- Authoritative target ref/SHA and intended mutation state survive nested delegation until explicitly changed.
- Static inspection, executable workspace, mutation baseline, verification/review, and publication are distinct state-identity steps that must not be silently mixed.
- Issue/report-derived work resolves its applicability target from issue/project metadata instead of assuming local checkout; publishing a current-state issue rechecks moved target evidence before publication.
- Tester validates executing state for target-bound evidence; mismatched-worktree results are workspace-only/target-unverified.
- Debugger/build/UI implementation refuse to edit a stale or unrelated worktree when the assignment is bound to a current authoritative target.
- `/ui-options` now follows the existing materially-distinct-options policy instead of forcing 2–3 alternatives.

See [`docs/releases/v28.32.md`](docs/releases/v28.32.md) and [`docs/git_branch_provenance_policy.md`](docs/git_branch_provenance_policy.md).

## v28.31

v28.31 fixes stale-code analysis when a workflow must decide whether an issue/behavior still exists in the current upstream/default/base state.

- Current-upstream claims now require a freshly resolved authoritative remote ref + SHA before code is treated as current.
- The primary/orchestrator performs the freshness fetch once and passes the target ref/SHA to specialists; leaf roles do not independently fetch by default.
- A stale local checkout may be used only as comparison/history evidence when it differs from the authoritative target; it cannot silently stand in for current upstream.
- Read-only `git fetch` is explicitly separated from `pull`/rebase/reset/checkout, so freshness checks do not mutate the working tree.
- `/bug-issue` and issue-originated bugfix diagnosis now resolve the report target first and verify current-upstream applicability against the fetched authoritative ref; explicitly local-workspace reports remain local.

See [`docs/releases/v28.31.md`](docs/releases/v28.31.md) and [`docs/git_branch_provenance_policy.md`](docs/git_branch_provenance_policy.md).

## v28.30

v28.30 keeps the v28.29 role/verification cadence and adds four targeted workflow-hygiene rules without adding a new skill or mandatory stage.

- A failed root-cause fix that leaves the same material failure now resets hypothesis confidence before another similar mutation is authorized.
- Orchestrators resolve safe non-gated uncertainty from evidence and batch compatible blocking user decisions; existing approval gates are unchanged.
- User-facing output now leads by state: result first when complete, blocker/action first when blocked, first executable step first for user-run procedures.
- Numbered steps are reserved for ordered human procedures rather than findings, options, status, or internal workflow diagrams.
- README Candidate/verification diagrams now explicitly show the optional/required Candidate-level `@tester` checkpoint before the final reviewer.

See [`docs/releases/v28.30.md`](docs/releases/v28.30.md) for the detailed before/after explanation.

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
