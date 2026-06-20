---
description: Reproduce and fix a failing test, traceback, build failure, runtime error, or reproducible bug.
agent: debugger
subtask: true
---

## Behavioral Contract Check

For any user-facing UI/config/API/workflow behavior change, do not implement only the data plumbing. Before planning or editing, summarize:

- user-facing action
- value source
- valid-value domain
- existing project pattern to inspect
- whether raw/internal/manual values would be exposed to normal users

Do not derive behavior directly from schema/storage/API type. Preserve the existing affordance class unless the normalized request explicitly asks for a raw/manual/editor workflow.

Debug this failure: $ARGUMENTS

Start from evidence, reproduce when the provided evidence or project commands allow a non-destructive reproduction, find root cause, apply the smallest right-level fix, and run the focused verification.
