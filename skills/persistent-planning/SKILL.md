---
name: persistent-planning
description: Use only after the active workflow owner activates durable planning. Owns fallback durable representation, resume, and work-package persistence mechanics; workflow-control/caller owns activation and canonical task-state policy.
---

# Persistent planning

The active workflow owner (normally via `workflow-control`) owns activation, canonical task-state semantics, preference for an existing project planning owner, and any repository-mutation gate. This skill begins after that boundary is established and does not redefine it.

## Fallback durable representation

When the active workflow owner establishes that durable repository planning is authorized and no existing project convention can serve as the canonical representation, the pack fallback is:

```text
plans/<plan>/
  plan.md
  phases/phase-N.md
  implementation/phase-N-impl.md
  reviews/*.md
  todo.md
  handovers/session-YYYY-MM-DD.md
```

Use only the files needed by the actual task. Do not create empty artifact categories for symmetry.

## Resume and update procedure

On resume, read the root-established canonical current state before changing it. Continue from that state instead of reconstructing progress from chat summaries. If the fallback representation is the canonical owner for this task, update only the smallest artifact set needed to preserve current work-package state, durable decisions/blockers, state-bound evidence, and the next safe action already required by the active workflow-owner state.

## Work-package cycle

For broad implementation, use the minimal cycle needed to keep the canonical state coherent:

1. define the bounded work package from current canonical state;
2. execute only that package within the already-established authority/scope/gates;
3. reflect durable conclusions, blockers, evidence changes, and next action back into the canonical representation.

This cycle is a coordination aid, not a mandatory ceremony. Collapse steps when no durable state would be lost. Repository planning artifacts remain mutations governed by the root authorization policy.
