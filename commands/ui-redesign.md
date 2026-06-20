---
description: Run the full UI/web redesign workflow in one request. The orchestrator calls audit, planning, implementation, accessibility review, and verification subagents automatically unless a gated action is hit.
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

Run the full UI/web redesign workflow for: $ARGUMENTS

Do not make the user manually run each stage.

Call subagents in sequence and continue automatically when the next stage does not hit a gated action:
1. @explore if relevant files/routes/components/styles are not already known.
2. @ui-ux-auditor for current UX/layout audit and element priority.
3. @ui-redesign-planner for concrete redesign/layout/theme plan. It must read the detailed UI policy file defined in AGENTS.md when it exists and perform the UUPM availability check before using UUPM/UI UX Pro Max.
4. @frontend-ui-implementer if no gated action is hit.
5. @accessibility-reviewer for UI/a11y check.
6. @tester for the narrowest relevant frontend validation.

Ask the user only if a gated action is hit: ambiguous visual direction, new dependency/design system, broad scope rewrite, product/API/data/deployment behavior change, destructive action, secrets/external account action, or blocked verification.

Keep all work on the current PR branch if this is follow-up work for an existing PR.
Read the detailed UI policy file defined in AGENTS.md when it exists.

Return one consolidated final report. Include whether UUPM was used, unavailable, not checked, or skipped, and which guidance was applied/rejected.


If the request is only asking for options, variants, ideas, critique, or a plan, do not implement. Return 2-3 options and stop. For pure options, prefer /ui-options.
