# Contract / protocol audit — v30.75 beta

## Scope

v30.75 changes README/release documentation only. Runtime agent contracts and skill contracts are byte-identical to v30.74; root workflow policy is unchanged after normalizing the pack-version marker.

## Retained contract status

- role executability: **17 PASS / 0 REVIEW / 0 FAIL**;
- closed-world handoff inventory: **54 discovered / 54 classified**;
- semantic role shape remains `Ownership → Invocation → Method → Boundaries → Result` without mandatory heading/template conformity;
- `librarian` remains a deferred design TODO and is not part of runtime topology.

The detailed 17-role semantic-shape matrix remains in [`contract-protocol-audit-v30.74.md`](contract-protocol-audit-v30.74.md); v30.75 does not duplicate it because no role contract changed.

## README ownership check

README now has one architecture/navigation ownership table. Other `AGENTS.md` occurrences are limited to installation paths or literal external-reference naming, so README no longer maintains several prose copies of the same canonical-policy statement.
