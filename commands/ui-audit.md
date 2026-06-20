---
description: Audit a UI/web screen for layout, hierarchy, density, settings/form UX, and primary action placement.
agent: ui-ux-auditor
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

Audit this UI/web screen or area: $ARGUMENTS

Focus on:
- primary user job
- element priority
- layout density and wasted space
- primary action placement
- secondary/advanced controls
- settings/form ergonomics
- existing components/routes/styles to inspect

Read the detailed UI policy file defined in AGENTS.md when it exists.

Return a concrete audit and recommend the next UI agent.
