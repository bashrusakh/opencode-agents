# PR readiness

Use this only at the publication boundary for task changes: before the first push/PR publication and before a later push that changes an existing PR diff. It is not a per-edit/per-commit checklist and it does not replace the normal gated-action approval rules.

## Ready state

The active primary/orchestrator may publish only when the current effective diff has all applicable evidence:

- **Repository contract** — relevant root/scoped guidance was read; selected/required `SKILL.md` was actually read; current PR template/publication guidance was discovered when PR metadata is in scope.
- **Fix contract** — root/right-level placement was checked. When behavior spans multiple meaningful states, transitions, consumers, boundaries, or input shapes, the relevant cases were identified and mapped to verification.
- **Validation** — project-required and task-relevant checks are complete for the current diff. For bugfixes or changes to existing/shared behavior, evidence covers both the intended changed behavior and applicable preserved behavior; shared-primitive changes include the relevant existing suite or representative consumers when practical. A newly added focused test alone is not sufficient regression evidence. Report only real command/tool results; never guess test counts, lint status, or validation claims.
- **Review** — when `AGENTS.md` reviewer applicability criteria match, `@reviewer` reviewed the current final local diff. External CI/bot review is post-publication/additional evidence, not a replacement for local pre-publication review.
- **Provenance** — the existing `docs/git_branch_provenance_policy.md` gate is current after the latest branch/history changes.
- **PR metadata** — when a PR exists or will be created/updated, title/body describe the final scope, changed behavior/files, and actual validation.

A reviewer result of `changes required` blocks readiness unless the finding is fixed or the user explicitly approves publication with the known risk. Non-blocking notes do not force unrelated cleanup.

## Freshness

Readiness belongs to the effective diff that was checked. Re-check only the evidence made stale by later changes.

These normally invalidate affected evidence:

- code/config/test changes after validation or review;
- fixes made in response to reviewer findings;
- rebase, merge, cherry-pick, reset, or branch replacement;
- remote/head/base movement that changes the effective diff or integration state.

A fetch that changes no effective diff does not by itself invalidate readiness. If reviewer criteria still apply after code changes, review the new final local diff again before publication.

## Ordering

For a normal implementation/fix workflow:

1. pre-edit repository/branch checks;
2. understand root/right-level behavior and relevant cases;
3. implement and verify locally;
4. review the final local diff when reviewer criteria apply;
5. fix blocking review findings and re-run affected validation/review;
6. refresh provenance and PR metadata;
7. publish only when both PR readiness and the existing gated-action rule allow it;
8. treat CI/bot review as additional post-publication evidence and follow up only when needed.
