---
description: Resume an existing persistent plan from canonical plans/<plan>/ artifacts.
agent: plan
subtask: true
---

## Purpose

Bootstrap a new session or agent from durable plan state.

## Required behavior

Read, in order:

1. `plans/<plan>/plan.md`
2. `plans/<plan>/todo.md`
3. active `phases/phase-N.md`
4. active `implementation/phase-N-impl.md` when present
5. relevant `reviews/*.md`
6. latest `handovers/session-*.md`
7. project-local `AGENTS.md` / `agents.md` and `CONTRIBUTING.md` when present

Then report current phase, current todo item, blockers, known decisions, and next safe action. Do not restart from zero unless canonical files are missing or stale.
