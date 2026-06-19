---
description: Propose UI/web redesign options without editing code. Use this for variants, ideas, layout alternatives, and choosing between quick/balanced/full redesign directions.
agent: ui-web-orchestrator
subtask: true
---

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
