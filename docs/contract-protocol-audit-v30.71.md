# Contract / protocol audit — v30.71 beta

## Scope

v30.71 changes README/documentation topology and one layout-sensitive static release assertion. Runtime agent and skill contracts are unchanged from v30.70, and root semantic policy is unchanged apart from the pack-version marker.

## Results

- role executability: **17 PASS / 0 REVIEW / 0 FAIL**;
- discovered/classified pack-owned role relations: **54 / 54**;
- high-risk handoff profiles: PASS;
- generic delegation contracts: PASS;
- contract/protocol selftest v3: PASS;
- role-handoff selftest v2: PASS;
- aggregate release gates: PASS.

The static README current-release check was made layout-agnostic: it now verifies that README references the active version's release-note path rather than requiring the former documentation-table row format.

Fresh isolated semantic-transition replay remains a separate evidence class and is not claimed by this audit.
