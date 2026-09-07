---
description: "Create, resume, update, hand over, or verify persistent implementation plans and canonical plan state."
agent: plan
subtask: false
---

Handle planning for: $ARGUMENTS

Follow the active `AGENTS.md`, plan role contract, and the applicable installed/project `persistent_planning_policy.md`.

Use `/plan` semantics for:
- creating authorized canonical `plans/<plan>/` artifacts;
- resuming from existing plan/todo/phase/review/handover state;
- updating durable status/todo/handover state after work;
- authoring an implementation plan grounded in actual files, symbols, constraints, and verification needs.

Do not implement source/config/test changes. Do not invent parallel workflow directories or arbitrary report files. If a plan/result needs independent review, treat that as review work rather than silently changing the planner role.

Return a compact digest of plan state, changed planning artifacts, blockers, and next safe action.
