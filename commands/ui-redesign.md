---
description: "Coordinate a complete UI/web redesign workflow in one request, selecting audit, planning, implementation, accessibility review, and verification stages by semantic need."
agent: ui-orchestrator
subtask: false
---

Run the UI/web redesign workflow for: $ARGUMENTS

Follow the active `AGENTS.md`, ui-orchestrator contract, and applicable UI policy. Do not make the user manually invoke every specialist.

Normalize whether the deliverable is options/audit/plan-only or actual implementation. For implementation requests, coordinate only the stages needed by the current state: discovery when targets are unknown, UI audit when existing UX needs assessment, planning when direction is not yet concrete, implementation by `@ui-implementer`, accessibility review when applicable, and focused verification.

Do not force a fixed stage sequence when evidence already supplies a stage's result. Conversely, a failed/unavailable specialist is not a reason for the orchestrator to perform that role's prohibited work.

Stop for genuinely unresolved materially different design/product direction or another root-gated action. Otherwise continue through authorized safe stages and return one consolidated result tied to the final effective UI diff/state.
