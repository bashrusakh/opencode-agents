---
description: Run the full UI/web redesign workflow in one request. The orchestrator calls audit, planning, implementation, accessibility review, and verification subagents automatically unless an approval gate is hit.
agent: ui-web-orchestrator
subtask: false
---

Run the full UI/web redesign workflow for: $ARGUMENTS

Do not make the user manually run each stage.

Call subagents in sequence and continue automatically when safe:
1. @explore if relevant files/routes/components/styles are not already known.
2. @ui-ux-auditor for current UX/layout audit and element priority.
3. @ui-redesign-planner for concrete redesign/layout/theme plan.
4. @frontend-ui-implementer if no approval gate is hit.
5. @accessibility-reviewer for UI/a11y check.
6. @tester for the narrowest relevant frontend validation.

Ask the user only if an approval gate is hit: ambiguous visual direction, new dependency/design system, broad rewrite, product/API/data/deployment behavior change, destructive action, secrets/external account action, blocked verification, or explicit user approval requirement.

Keep all work on the current PR branch if this is follow-up work for an existing PR.
Return one consolidated final report.
