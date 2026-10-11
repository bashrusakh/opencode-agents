# Contract / protocol audit — v30.77 beta

## Role executability

Runtime agent contracts are unchanged from v30.76. `contract-protocol-audit.py` reports **18 PASS / 0 REVIEW / 0 FAIL**.

## Handoff topology

Runtime topology is unchanged from v30.76. `role-handoff-audit.py` reports **57 discovered / 57 classified** pack-owned relations.

## README delegation inventory

The release adds a documentation-consistency invariant: `README.md`'s `## Delegated specialists` inventory must equal the set of role targets classified as `delegation` or `conditional_delegate` in the closed-world topology. This catches both omissions (such as a newly delegated `mode: all` role missing from README) and stale entries.

The check is derived from topology rather than from a candidate-specific list, so a future delegation-edge change changes the expected README inventory automatically.

## Evidence limits

This release does not alter behavioral contracts or claim new behavioral replay evidence. ST-01…ST-70 remains the current transition suite; fresh isolated replay remains pending.
