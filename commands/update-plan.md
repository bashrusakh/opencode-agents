---
description: Update persistent plan status, todo items, changelog, phase transition, and next action.
agent: plan
subtask: true
---

## Purpose

Keep the canonical plan artifacts current after exploration, implementation, review, verification, or handover.

## Required behavior

- Update `plans/<plan>/todo.md` with stable statuses and changelog entries.
- Update phase status when a phase starts, blocks, finishes, or is deferred.
- Record decisions and evidence in the existing plan artifacts.
- Do not create random reports.
- Return a compact digest with changed plan files and next action.
