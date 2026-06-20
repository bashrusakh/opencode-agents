---
description: Propose UI/web redesign options without editing code. Use this for variants, ideas, layout alternatives, and choosing between quick/balanced/full redesign directions.
agent: ui-web-orchestrator
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

Propose UI/web redesign options for: $ARGUMENTS

This is options-only. Do not edit code and do not call @frontend-ui-implementer.

Use @explore and @ui-ux-auditor if the current UI needs to be understood.
Use @ui-redesign-planner to produce 2-3 concrete options:

1. Conservative / quick
2. Balanced / recommended
3. Full redesign

For each option include what changes, why it helps, affected screens/components, implementation risk, and estimated scope.

Stop after presenting the options and ask the user which direction to choose.


Read the detailed UI policy file defined in AGENTS.md when it exists.
