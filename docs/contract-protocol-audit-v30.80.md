# Contract / protocol audit — v30.80

## Scope

v30.80 changes semantic execution contracts in root plus `project-planner`, `semantic-checkpoint`, `session-evaluator`, `code-orchestrator`, and `explore`; it also tightens the `open-code-review` installation boundary. No delegation topology or role permission ceiling changes.

Installer behavior and package licensing are release/package surfaces rather than role topology, and are validated separately by installer behavioral selftests and static release guards.

## Planning ownership

The canonical split is now explicit:

- root §2.3 — trigger/activation and one-canonical-planning-state policy;
- `persistent-planning` — fallback representation and resume procedure;
- project-owned plan/roadmap/tracker — authoritative project convention when present;
- `project-planner` — consumes the canonical owner and writes only where its permission ceiling allows.

An unwritable project canonical owner produces a bounded update need for an authorized writer, not a parallel plan.

## Semantic-state typing

The previous overloaded `unverified` literal crossed three axes. v30.80 separates them:

- workflow gate verdict: `insufficient-context` when the checkpoint lacks enough trace/provenance/context;
- evidence state: `unverified` when evidence is insufficient;
- proposition relation: `indeterminate` when the relation cannot be classified.

`code-orchestrator` consumes `hold` and `insufficient-context` as separate blocking verdicts. The practical mutation outcome is the same while diagnostic semantics stay stable.

Root remains the canonical owner of `weakened`/`substituted` authority semantics. Checkpoint applies that rule prospectively; evaluator diagnoses historical transitions. Repeated explanatory state-machine prose was removed from the roles without removing their role-local method/result obligations.

## Explore contract

The discovery profile now requires two characteristic anti-false-success capabilities beyond generic evidence discipline:

1. material negative claims are scoped to the domain actually searched and test relevant aliases/references/generated/config surfaces;
2. material call/data/state-flow claims are supported by an actual relation edge, not naming/file adjacency.

The compact-role preservation fixture still passes, while a thin `grep exact symbol -> unused` / adjacency-flow fixture fails.

## Installer composition

Installer ownership no longer comes from basenames. The package records managed-file SHA-256 receipts; only receipt-proven unchanged stale files may be removed automatically. Unknown legacy names are preserved and warned.

Project/global root-policy conflicts are resolved before mutation. Real installer selftests prove the block-before-mutation, project-root preservation, collision backup, legacy-command preservation, and successful recognized-pack upgrade cases in isolated temporary trees.

## Licensing/provenance

The package now carries a root MIT license and third-party notices/license texts for bundled third-party material with established provenance. This is packaging provenance, not runtime authority.

## Evidence limits

Contract/static/installer selftests demonstrate that the explicit contracts are present and that the real shell installers satisfy the tested filesystem cases. They do not constitute isolated replay of semantic-transition scenarios. ST-01…ST-78 behavioral replay remains pending.
