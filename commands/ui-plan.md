---
description: Create a concrete UI/web redesign or theme plan from an audit, screenshot, issue, or requested screen.
agent: ui-redesign-planner
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

Create a concrete UI/web redesign plan for: $ARGUMENTS

Use current project structure and components. Before using UUPM/UI UX Pro Max, perform the UUPM availability check from the detailed UI policy file defined in AGENTS.md. If unavailable or not checked, continue without it and say so. Do not edit files.

Include element priority, layout plan, component strategy, tokens if relevant, responsive behavior, accessibility notes, and implementation steps.


Read the detailed UI policy file defined in AGENTS.md when it exists.
