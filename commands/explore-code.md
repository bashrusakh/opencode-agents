---
description: Explore the codebase and return facts, file paths, call paths, and existing patterns.
agent: explore
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

Explore the codebase for: $ARGUMENTS

Use medium thoroughness by default unless the request says quick or very thorough. Return facts and paths only.
