---
description: Generate a session handover for a persistent plan or standalone docs handover.
agent: plan
subtask: true
---

## Purpose

Create a handover so another agent/session can resume without chat history.

## Required behavior

For a plan, write `plans/<plan>/handovers/session-YYYY-MM-DD.md`. For standalone documentation work, write `docs/handovers/session-YYYY-MM-DD.md`.

Include current phase, completed work, changed files, decisions, blockers, open questions, commands/checks run, and exact next step.

Return only a compact digest and the handover path.
