# Contract / protocol audit — v30.70 beta

## Role executability

Frozen semantic role criteria report **17 PASS / 0 REVIEW / 0 FAIL**. Prompt length is diagnostic only; every role is evaluated on its profile-specific core loop, conditional decisions, evidence/self-check, false-success defense, stop/escalation and result semantics.

## Closed-world handoff topology

`role-handoff-audit.py` discovers every pack-owned `@role` relation in root and standing agent contracts. The v30.70 topology is **54 discovered / 54 classified**:

- routing_policy: 13
- delegation: 26
- conditional_delegate: 2
- reroute: 2
- boundary_reference: 6
- specialist_boundary: 2
- escalation: 1
- return_to_parent: 1
- output_package: 1

Unknown discovered edges and stale classifications both block release. Material delegation callers still pass generic assignment-contract checks and high-risk callee-specific profiles; classification itself is not treated as compatibility proof.

## Lifecycle preservation

The existing semantic-design manual now requires requalification after role-topology/mode/caller expansion, substantive owner/proof transfer, prompt compaction/deduplication, or advisory→mutation/verdict transitions. Canonical-owner moves require a method-preservation test before procedural wording is deleted.

## Anti-gaming probes

Five mutation probes independently turn the relevant gate red: new unclassified edge, stale edge, new agent without audit profile, removed lifecycle/manual rule, and removed closed-world inventory selftest.

## Limits

These are static/contractual release prerequisites. They do not prove model behavior. Fresh isolated replay of ST-01…ST-63 remains pending.
