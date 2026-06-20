---
description: Create a persistent plan in plans/<plan>/ for long-running or multi-agent work.
agent: plan
subtask: true
---

## Purpose

Create canonical plan artifacts when normalized scope is long-running, broad, multi-agent, multi-session, or needs durable handoff/resume state. Broad audits, full-project bug hunts, large refactors, and large UI redesigns are examples, not trigger phrases.

## Required behavior

- Clarify scope until the plan name, objective, requirements, risks, and Definition of Done are clear.
- Create `plans/<plan>/plan.md`, `phases/phase-N.md`, and `todo.md`.
- Use the layout from `docs/PERSISTENT_PLANNING_POLICY.md`.
- Do not edit source code.
- Do not create arbitrary markdown reports.
- Return a compact digest with plan path, phases, current todo, risks, and next command.
