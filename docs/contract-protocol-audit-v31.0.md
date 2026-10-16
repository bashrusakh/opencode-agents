# v31.0 contract/protocol audit

Scope: behavioral orchestration hardening over v30.100 for owned-PR correction/review cadence and delegated task-state authority.

## Canonical ownership

- `pr-readiness` remains the sole owner of the Owned-PR lifecycle and now types it as **Draft -> Correction / stabilization -> Candidate HEAD -> Ready**.
- `code-orchestrator` consumes the correction/stabilization state; it does not redefine the lifecycle. Its role-local duty is to maintain the combined finding/model state and decide when the `pr-readiness` closure conditions are actually met.
- Root `AGENTS.md` owns the universal rule that an action ceiling covers **all task-relevant state**, not only content mutation.
- `delegation-control` specializes that universal rule for child assignments: a material state transition outside the assignment is a separate mutation and must return to the caller before execution.
- `resource-lifecycle` owns reconciliation only after resource mutation is authorized; it does not create resource-mutation authority.

## v31.0 regression boundaries

1. **Ready without whole-PR acceptance evidence** — publication/CI/Ready sequencing cannot implicitly waive a missing final whole-review prerequisite.
2. **Correction-package promotion churn** — a locally green/committed/targeted-reviewed bounded correction is evidence inside stabilization, not automatic Candidate promotion. Final whole-PR review is the exit gate from the stabilized combined state.
3. **Delegated task-state drift** — implementation/content authority does not imply authority to rebind target/resource state or relocate pre-existing workflow state. Concrete worktree-like behavior is only a regression fixture; the normative rule is provider/resource agnostic.

## Release-gate evidence

- 19/19 role contracts executable under the contract/protocol audit.
- 32 shared semantic ownership capabilities with one canonical owner each.
- 6 typed semantic domains; `owned_pr_lifecycle_state` now includes `Correction / stabilization`.
- 21 workflow-path scenarios, including the three v31.0 regression paths.
- Workflow-path mutation selftests reject: correction-batch -> whole-review churn, Ready prerequisite waiver inferred from action sequencing, and removal of the delegated task-state boundary.
- Reference-integrity, residency, skill-control, section ownership, installer safety, and handoff topology remain release-gated.

Permissions/frontmatter and vendor-advisory skill content are intentionally unchanged. Static/mutation release gates are prerequisites only; fresh isolated behavioral replay of ST-142..ST-144 is not claimed by this beta audit.
