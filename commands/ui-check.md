---
description: Check UI/web changes for accessibility, keyboard flow, focus, contrast risks, responsive behavior, and form states.
agent: accessibility-reviewer
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

Check the UI/web changes for: $ARGUMENTS

Review current diff and relevant components. Do not edit files. Report actionable accessibility and interaction findings.

Read the detailed UI policy file defined in AGENTS.md when it exists.
