# PR readiness

The root `AGENTS.md` section on PR readiness is normative. Use this document as the compact publication-boundary procedure.

Run the gate before the first push/PR publication of task changes and again before a later push that changes an existing PR diff. It is not a per-edit/per-commit ritual and it is not a second approval gate.

## Ready state

The active primary/orchestrator may publish only when all applicable evidence matches the current effective diff:

- **Repository contract** — relevant root/scoped guidance and actually selected skills were loaded; current PR template/publication guidance was discovered when PR metadata is in scope.
- **Fix contract** — right-level/root-cause placement was checked; meaningful states/transitions/consumers/boundaries are mapped to verification when applicable.
- **Validation** — project-required and task-relevant checks are complete for the current diff. Existing/shared behavior changes include evidence for both changed behavior and the nearest preserved behavior/invariant. Shared primitives include the relevant existing suite or representative consumers when practical.
- **Review** — when root reviewer criteria apply, `@reviewer` reviewed the current final local diff. External CI/bot review is additional evidence, not a replacement for required pre-publication review.
- **Provenance** — `docs/git_branch_provenance_policy.md` is current after the latest branch/history changes.
- **PR metadata** — title/body describe the final scope, behavior/files, and actual validation.

A reviewer verdict of `changes required` blocks readiness unless the finding is resolved or the user explicitly authorizes publication with the known risk. Non-blocking notes do not force unrelated cleanup.

## Freshness

Readiness belongs to the state/diff that was checked. Re-run only evidence affected by later changes.

Typical invalidators:

- code/config/test/generated-output/dependency changes after validation or review;
- fixes made after reviewer findings;
- rebase, merge, cherry-pick, reset, or branch replacement;
- remote/head/base movement that changes the effective diff or integration state.

A fetch that changes no effective diff does not itself invalidate readiness. If reviewer criteria still apply after relevant edits, review the new final diff again.

## Normal ordering

1. pre-edit repository/branch checks;
2. understand root cause/right-level behavior and relevant cases;
3. implement and verify locally;
4. review the final diff when reviewer criteria apply;
5. resolve blocking review findings and re-run affected checks/review;
6. refresh provenance and PR metadata;
7. publish only when readiness is current and the root authorization gate permits the action;
8. treat CI/bot review as additional post-publication evidence.
