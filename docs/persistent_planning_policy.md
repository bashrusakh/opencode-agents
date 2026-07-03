# Persistent Planning Policy

This policy adapts the file-based planning model from `opencode-processing-skills` into this OpenCode agent pack. Use it when semantic normalization shows the task is long-running, broad-scope, multi-session, multi-agent, or likely to lose useful context if kept only in chat. Phrases like full-project inspection, broad bug hunt, large refactor, large UI redesign, or project-wide audit are examples, not triggers.

## Core principle

The file structure is the interface. For long-running work, durable state lives in files, not in chat history, private reasoning, or ad-hoc markdown reports. A new agent must be able to resume from canonical files alone.

Route by normalized scope, not by exact wording. Use Persistent Planning Mode when the work needs durable coordination, resumability, phased execution, or handoff between agents/sessions. Do not use it for a narrow single-session fix merely because the user used a phrase that resembles an example.

Subagents should return compact digests. Durable findings, decisions, todos, implementation plans, reviews, and handovers belong in `docs/` and `plans/` artifacts.

## Canonical target layout

Use this layout in the target project:

```text
plans/<plan>/
  plan.md
  phases/
    phase-N.md
  implementation/
    phase-N-impl.md
  reviews/
    plan-review.md
    impl-plan-review-phase-N.md
    impl-review-phase-N.md
  todo.md
  handovers/
    session-YYYY-MM-DD.md

docs/
  overview.md
  modules/
  features/
  handovers/
    session-YYYY-MM-DD.md
```

Do not invent parallel workflow directories such as `.opencode/workflows/` for this mode. Do not create random files like `audit-notes.md`, `deepseek-report.md`, `final-final.md`, or agent-specific reports unless the user explicitly asks for that artifact.

## Planning entities

| Entity | File | Purpose |
|---|---|---|
| Plan | `plans/<plan>/plan.md` | Objective, requirements, Definition of Done, phases overview |
| Phase | `plans/<plan>/phases/phase-N.md` | What this phase delivers and why |
| Implementation Plan | `plans/<plan>/implementation/phase-N-impl.md` | How to implement the phase; grounded file/symbol steps |
| Review | `plans/<plan>/reviews/*.md` | Independent quality gate for plan, implementation plan, or implementation |
| Todo | `plans/<plan>/todo.md` | Trackable items, status, changelog, current next action |
| Handover | `plans/<plan>/handovers/session-*.md` | Session continuity: progress, decisions, blockers, next step |

Phases define what and why. Implementation plans define how. This separation allows a technical approach to change without silently changing the accepted scope.

## Typical flow

1. Discuss: clarify requirements and scope.
2. Create Plan: create `plan.md`, phase files, and `todo.md`.
3. Review Plan: optional quality gate for scope, DoD, risks, and phase boundaries.
4. Author Implementation Plan: create `implementation/phase-N-impl.md`, grounded against actual files/symbols.
5. Review Implementation Plan: optional quality gate for actionability and feasibility.
6. Execute Work Package: gated execution using Blueprint -> Gate -> Execute -> Digest.
7. Review Implementation: optional code/result review against acceptance criteria.
8. Update Plan: update `todo.md`, changelog, phase status, decisions, and next step.
9. Generate Handover: write session context for the next agent/session.

## Execution protocol

For broad implementation work use:

```text
Blueprint -> Gate -> Execute -> Digest
```

- Blueprint: propose concrete step list, touched files, checks, risks, and rollback/stop points.
- Gate: primary agent/user reviews and approves before source edits when the action is broad or otherwise gated.
- Execute: implementation agent changes code and verifies.
- Digest: compact result summary; durable state is reflected in plan artifacts by the planning/maintainer workflow.

Git operations stay gated and must not be performed by implementation subagents unless the exact publication action is allowed by the root rules.

## Resume protocol

Before resuming a long-running plan, read:

1. `plans/<plan>/plan.md`
2. `plans/<plan>/todo.md`
3. relevant `phases/phase-N.md`
4. relevant `implementation/phase-N-impl.md` when implementation is next
5. latest `reviews/*.md` related to the active phase
6. latest `handovers/session-*.md`
7. project `AGENTS.md` / `agents.md` and `CONTRIBUTING.md` when present

Then report the current phase, current todo item, known blockers, and the next safe action. Do not restart from zero unless the canonical files are missing or stale.

## Multi-agent rules

- One canonical plan directory per long-running task.
- All agents read the canonical plan artifacts before continuing.
- No arbitrary markdown files or private side reports.
- Do not duplicate another agent's work; update the existing plan/todo/review artifact instead.
- Subagents return digests, not giant dumps.
- The primary/orchestrator owns user interaction, planning decisions, and git/publication gates.
- Implementation agents execute only the approved work package and return digest.
- Review agents write review artifacts or return review digest according to the command.

## Status vocabulary

Use a small stable status set in `todo.md` and reviews:

```text
new
active
blocked
needs-review
approved
in-progress
done
deferred
rejected
```

Each status change should include a short dated changelog entry with evidence or command output when relevant.
