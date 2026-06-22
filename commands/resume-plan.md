---
description: Resume an existing persistent plan from canonical plans/<plan>/ artifacts.
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

Bootstrap a new session or agent from durable plan state.

## Required behavior

Read, in order:

1. `plans/<plan>/plan.md`
2. `plans/<plan>/todo.md`
3. active `phases/phase-N.md`
4. active `implementation/phase-N-impl.md` when present
5. relevant `reviews/*.md`
6. latest `handovers/session-*.md`
7. project-local `AGENTS.md` / `agents.md` and `CONTRIBUTING.md` when present

Then report current phase, current todo item, blockers, known decisions, and next safe action. Do not restart from zero unless canonical files are missing or stale.
