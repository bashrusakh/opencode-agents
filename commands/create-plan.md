---
description: Create a persistent plan in plans/<plan>/ for long-running or multi-agent work.
agent: plan
subtask: true
---

## Startup Checkpoint Before Tools

Before the first tool call in any multi-step, repository, codebase, issue/PR/release, external-URL, publication-capable, or scope-expanding workflow, write:

```text
Startup completed. Route: <route>. Mode: <read-only/options/edit-capable/gated>.
```

Include outcome, target, action level, confidence, and `gated: yes/no`. If the next step is read-only, say `gated: no — read-only`. If discovery could expand scope, state the scope boundary before using tools. Do not use tools first and postpone normalization to the final report.

## User-Facing Output Formatting

For any user-visible answer or published text — final reply, PR/issue/release body, PR review/comment, changelog, handover, plan artifact, or Markdown doc — use readable target-aware Markdown by default.

- Start with a short summary.
- Use headings/sections when there is context, reasoning, validation, conclusion, or next action.
- Use bullets for multiple reasons, risks, checks, files, or decisions.
- Use fenced code blocks for commands, logs, paths, config, or exact proposed text.
- Avoid dense wall-of-text paragraphs.
- For OpenCode CLI, Hermes, Telegram, terminals, or chat relays, prefer compact portable Markdown/plain text; avoid raw HTML, oversized tables, deeply nested lists, and GitHub-only formatting.
- For GitHub/GitLab PRs, issues, releases, and review comments, use clean Markdown with a clear conclusion/next action.


## Purpose

Create canonical plan artifacts when normalized scope is long-running, broad, multi-agent, multi-session, or needs durable handoff/resume state. Broad audits, full-project bug hunts, large refactors, and large UI redesigns are examples, not trigger phrases.

## Required behavior

- Clarify scope until the plan name, objective, requirements, risks, and Definition of Done are clear.
- Create `plans/<plan>/plan.md`, `phases/phase-N.md`, and `todo.md`.
- Use the layout from `docs/PERSISTENT_PLANNING_POLICY.md`.
- Do not edit source code.
- Do not create arbitrary markdown reports.
- Return a compact digest with plan path, phases, current todo, risks, and next command.
