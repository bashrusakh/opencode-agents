---
description: Author and verify implementation plans for one or more persistent plan phases.
agent: plan
subtask: true
---

## Purpose

Create `plans/<plan>/implementation/phase-N-impl.md` grounded against the actual codebase.

## Required behavior

- Read the plan, active phase, todo, relevant code, and existing patterns.
- Identify files, symbols, data flow, tests, risks, and stop points.
- Verify that referenced files/symbols exist.
- Keep implementation plan above code level; do not edit source code.
- If authoring multiple phase plans, process sequentially and run a consistency check for shared interfaces, naming, and assumptions.
