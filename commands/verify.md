---
description: Run relevant tests, linters, builds, and smoke checks without editing files.
agent: tester
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

Verify the current state for: $ARGUMENTS

Discover the relevant checks from project docs/configs, run the smallest checks that directly verify the requested scope first, and report exact commands/results.
