---
description: "Coordinate a complete UI/web redesign workflow in one request, selecting audit, planning, implementation, accessibility review, and verification stages by semantic need."
agent: ui-orchestrator
subtask: false
---

Run the UI/web redesign workflow for: $ARGUMENTS

Follow the active `AGENTS.md`, ui-orchestrator contract, and applicable UI policy. Do not make the user manually invoke every specialist.

Normalize whether the deliverable is options/audit/plan-only or actual implementation. For implementation requests, coordinate only the stages needed by the current state: separate discovery only when the target/ownership is materially broad or ambiguous, UI audit when existing UX needs assessment, planning when direction is not yet concrete, implementation by `@ui-implementer`, independent tester verification only at a meaningful affected/integration boundary when it materially adds confidence or policy/request requires it, and accessibility review only when the change touches an accessibility-sensitive interaction/semantic boundary or policy requires it, on the resulting stable UI state. A cosmetic UI-file edit alone is not an accessibility-review trigger. If both tester and accessibility review are post-implementation checks, run functional/integration verification first. Apply the root reviewer cadence to the stable final diff; an owned-PR Candidate requires the whole-change reviewer pass before its final push.

Do not force a fixed stage sequence when evidence already supplies a stage's result. Conversely, a failed/unavailable specialist is not a reason for the orchestrator to perform that role's prohibited work.

Stop for genuinely unresolved materially different design/product direction or another root-gated action. Otherwise continue through authorized safe stages and return one consolidated result tied to the final effective UI diff/state.
