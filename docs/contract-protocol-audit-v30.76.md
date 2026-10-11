# Contract / protocol audit — v30.76 beta

## Role executability

`contract-protocol-audit.py` v3 reports **18 PASS / 0 REVIEW / 0 FAIL**.

`librarian` uses a new profile-specific `external_research` contract. PASS requires an executable role-local method for:

- exact external target/version/applicability binding;
- source choice by authority + exact-version applicability + directness;
- conflicting-source reconciliation without vote counting;
- false-success defense against plausible but wrong-version/platform/latest evidence;
- bounded provenance-first result semantics that do not create project authority, local root cause, implementation choice, or review verdict.

The synthetic selftest separately proves that a thin `search official docs -> return answer` shell fails while a complete external-research loop passes.

## Ownership boundary

The release keeps the three neighboring domains disjoint:

- `explore`: repository-local descriptive evidence;
- `librarian`: external technical descriptive evidence;
- `project-planner`: prospective implementation/planning propositions.

`general` explicitly yields when the dedicated external-technical-evidence owner applies. Librarian may inspect direct dependency/runtime metadata only to bind the external target/version; it does not trace local usages/call paths or produce implementation sequencing.

## Handoff topology

`role-handoff-audit.py` v2 reports **57 discovered / 57 classified** pack-owned relations.

New relations:

- `root -> librarian`: routing policy;
- `code-orchestrator -> librarian`: delegation;
- `auditor -> librarian`: delegation.

Both material caller edges have explicit proposition/target/version/source/applicability contracts and synthetic negative fixtures. No direct `explore/general/project-planner -> librarian` edge is introduced.

## Semantic regression coverage

ST-65…ST-70 add external-research regressions for target-version binding, conflict reconciliation, recommendation/authority separation, cross-role ownership, caller handoff composition, and lightweight-but-provenance-preserving output.

Static/contract/mutation/package evidence remains a prerequisite only. Fresh isolated behavioral replay of ST-01…ST-70 remains pending.
