---
name: persistent-planning
description: Use when a task genuinely requires durable coordination across long duration, broad scope, multiple sessions, multiple agents, or more state than one reliable session can preserve. Do not load for short, self-contained, or read-only work that can be completed without durable task artifacts.
---

# Persistent planning

Persistent planning preserves one authoritative task state across work boundaries. It does not create new product authority, widen scope, or authorize repository mutation.

## Prefer the nearest existing owner

If the project already defines a canonical plan, roadmap, tracker, or handover convention, use it. Do not create a parallel planning system merely because this pack has a default representation.

When repository planning artifacts are authorized and no project convention exists, the pack default is:

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

## Durable state contract

The authoritative plan state must let another session reconstruct:

- the established outcome and active scope;
- the current phase/work package;
- material decisions and their authority/evidence status;
- completed and remaining work;
- blockers and unresolved choices;
- state-bound verification/review evidence;
- the next safe action.

On resume, read the canonical current state before changing it and continue from that state instead of reconstructing progress from chat summaries.

## Work-package cycle

For broad implementation, use the minimal cycle needed to keep state coherent:

1. define the bounded work package;
2. check it against current authority/scope/gates;
3. execute only that package;
4. reflect durable conclusions, blockers, and next action back into the canonical state.

This cycle is a coordination aid, not a mandatory ceremony. Collapse steps when the state is obvious and no information would be lost.

Read-only/audit work does not create repository plan files merely for continuity. Repository planning artifacts are mutations and remain subject to the root authorization policy.
