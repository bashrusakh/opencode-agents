# Contract / protocol audit — v30.78 beta

## Scope

v30.78 changes the standing runtime contract of `code-orchestrator` only. Other runtime roles keep their v30.77 behavior. The change addresses user-visible orchestration state and user-decision context; it does not alter role topology, permissions, mutation ownership, PR lifecycle, or Librarian ownership.

## Role executability

`contract-protocol-audit.py` reports **18 PASS / 0 REVIEW / 0 FAIL**.

To keep the fix narrow, `code-orchestrator` now uses a dedicated `code_orchestrator` audit profile. `ui-orchestrator` retains the generic `orchestrator` profile and is not required to inherit the new communication semantics merely because both roles coordinate specialists.

The dedicated profile adds two material capabilities:

- `workflow_state_visibility` — long multi-stage workflows synthesize meaningful current workflow state and next stage/owner without narrating the tool stream;
- `decision_context` — evidence-resolvable uncertainty is handled before user escalation, and a genuine user-owned choice is self-contained even when its evidence came from hidden child/tool context.

Synthetic selftests verify that a complete orchestrator passes while removal of either capability produces REVIEW rather than a false PASS.

## Handoff topology

No topology change: **57 discovered / 57 classified** pack-owned role relations. Existing high-risk handoff profiles and generic delegation contracts remain satisfied.

## Transition regressions

The suite now contains **ST-01…ST-74**.

New scenarios:

- ST-71 — multi-stage orchestration milestone visibility;
- ST-72 — preservation against tool-by-tool status narration;
- ST-73 — self-contained decision brief for hidden specialist context;
- ST-74 — evidence-resolvable technical ambiguity is not promoted into a user product choice.

These scenarios are release contracts only until replayed in isolated OpenCode sessions.

## Evidence limits

Static/contract/selftest/package PASS proves retention and executability of the known guards, not live behavioral compliance. Fresh isolated replay of ST-01…ST-74 remains pending.
