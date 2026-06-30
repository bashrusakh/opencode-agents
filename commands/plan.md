---
description: "Create, resume, update, hand over, or author implementation plans for persistent planning workflows."
agent: plan
subtask: false
---

## Startup Block Before Tools

Before the first tool call in any multi-step, repository, codebase, issue/PR/release, external-URL, publication-capable, or scope-expanding workflow, write Markdown only:

```md
### Startup
- Route: `<route>`
- Mode: `<read-only | options | edit-capable | gated>`
- Summary: <one sentence>
- Scope: <target + boundary>
- Gated: `<no | yes>` — <reason>
- Next: <next action/tool>
```

Keep it to this shape. Do not write a prose paragraph. Keep field names in English. Do not use tools first and postpone normalization to the final report.

## User-Facing Output Formatting

For any user-visible answer or published text — final reply, PR/issue/release body, PR review/comment, changelog, handover, plan artifact, or Markdown doc — use readable target-aware Markdown by default.

- Start with a short summary.
- Use headings/sections when there is context, reasoning, validation, conclusion, or next action.
- Use bullets for multiple reasons, risks, checks, files, or decisions.
- Use fenced code blocks for commands, logs, paths, config, or exact proposed text.
- Avoid dense wall-of-text paragraphs.

## Purpose

Handle persistent planning state through one command instead of exposing separate lifecycle commands.

Use `/plan` for:

- creating canonical `plans/<plan>/` artifacts;
- resuming an existing plan from `plan.md`, `todo.md`, phase docs, reviews, and handovers;
- updating todo/status/changelog/phase state after work;
- generating durable handover notes;
- authoring/verifying implementation plans grounded in actual files and symbols.

## Required behavior

- Read project `AGENTS.md` / `agents.md` and `CONTRIBUTING.md` when present.
- Use `docs/PERSISTENT_PLANNING_POLICY.md` as the durable planning source of truth.
- Keep plan state in canonical `plans/<plan>/` artifacts.
- Do not edit source code.
- Do not create random reports with new names.
- If the user asks for review of a plan/result, route that to `/review` semantics rather than inventing another plan command.
- Return a compact digest with changed plan files, blockers, and next safe action.
