---
description: Check whether a bugfix/security/audit/PR fix is implemented at the correct abstraction level.
agent: fix-level-reviewer
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

Review only the fix level for: $ARGUMENTS

Check duplicated local patches, missed shared abstractions, unsafe primitive coverage, and similar call sites. Do not edit files.
