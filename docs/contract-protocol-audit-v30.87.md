# Contract / protocol audit — v30.87 beta

## Scope

v30.87 changes two runtime role contracts:

- `code-orchestrator` — fresh reviewer handoff composition and authority provenance handling;
- `reviewer` — fresh investigative-context isolation and provenance self-defense.

No role permissions, topology edges, implementation/debug/test/UI ownership, publication lifecycle, or controller semantics change.

## Ownership split

`code-orchestrator` owns the task contract and exact target identity. It may pass binding outcome/acceptance propositions and exact authority-backed review constraints, but it does not own the reviewer's investigation strategy.

`reviewer` owns independent derivation of affected surfaces, risks, investigation order, probes and coverage from the authoritative contract plus the actual candidate.

Fresh context is judged semantically by the information exposed, not by labels or formatting. Parent-derived investigative direction contaminates fresh judgment even when it contains no explicit prior verdict and even when embedded as methodology.

A provenance label from the parent is a locator, not authority proof. Material review authority must remain recoverable from the underlying user/task/project source or remain unresolved.

## Targeted review preservation

A targeted/partial re-review may receive a known finding and its discriminating reproduction because that finding is the requested scope. The returned verdict remains partial/incremental and cannot substitute for fresh whole-change coverage.

## Eval inventory

- roles: 19;
- role relations: unchanged from v30.86;
- high-risk handoff profiles: unchanged from v30.86;
- semantic transition scenarios: 110 (ST-01…ST-110).

ST-107 generalizes fresh-context contamination to parent-derived investigative direction. ST-108 preserves independently authoritative extra review requirements. ST-109 blocks parent-authored methodology seeding regardless of presentation. ST-110 blocks provenance laundering.

## Claim boundary

Structural/contract/static/handoff validation does not constitute fresh behavioral replay. Any isolated model replay is reported separately and is not implied by this audit.
