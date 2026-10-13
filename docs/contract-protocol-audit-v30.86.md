# Contract / protocol audit — v30.86 beta

## Scope

v30.86 changes two runtime role contracts:

- `code-orchestrator` — fresh whole-change reviewer handoff composition only;
- `reviewer` — fresh-context contamination defense only.

No role permissions or topology edges change. Skills, implementation/debug/test/UI ownership, publication lifecycle, and the v30.85 owner/control-plane semantics remain unchanged.

## Fresh-review ownership split

`code-orchestrator` owns the task contract and exact target identity but must not provide its own review map for a fresh whole-change judgment. It retains prior findings/fix/test history for later reconciliation.

`reviewer` owns independent risk-surface derivation from the authoritative task contract and actual Candidate/effective diff. It cannot recreate independence after being seeded with prohibited judgmental history; contaminated fresh context blocks a fresh verdict and requires a clean assignment.

A user/project-policy emphasis is different from parent-generated focus: it carries independent authority/provenance and may be preserved, but only as additive/non-exhaustive emphasis.

Targeted re-review remains a separate partial lifecycle where a known finding and its discriminating reproduction may define the review scope.

## PR-readiness interaction

The readiness skill already requires a new corrected Candidate and repeated final whole-PR review after a `changes required` verdict. It does not require a targeted re-review after every fix. Thus a recent fix need not be exposed to the final reviewer as `Focus`; the corrected code is already present in the Candidate under review.

## Eval inventory

- roles: 19;
- role relations: 59/59 classified;
- high-risk handoff profiles: 17;
- generic delegation contracts: 3;
- semantic transition scenarios: 108 (ST-01…ST-108).

ST-32 is strengthened. ST-107 covers parent-authored recent-fix Focus/test-recipe contamination. ST-108 preserves explicit user/project emphasis without allowing it to narrow whole-change coverage.

## Claim boundary

Structural/contract/static/handoff validation is not fresh behavioral replay. Any isolated model replay is reported separately and is not implied by this audit.
