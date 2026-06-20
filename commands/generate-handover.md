---
description: Generate a session handover for a persistent plan or standalone docs handover.
agent: plan
subtask: true
---

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

Create a handover so another agent/session can resume without chat history.

## Required behavior

For a plan, write `plans/<plan>/handovers/session-YYYY-MM-DD.md`. For standalone documentation work, write `docs/handovers/session-YYYY-MM-DD.md`.

Include current phase, completed work, changed files, decisions, blockers, open questions, commands/checks run, and exact next step.

Return only a compact digest and the handover path.
