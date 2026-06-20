---
description: Execute an approved persistent-plan work package using Blueprint -> Gate -> Execute -> Digest.
agent: code-workflow-orchestrator
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

Execute a scoped work package from `plans/<plan>/` without losing state.

## Protocol

1. Blueprint: propose steps, files, checks, risks, and stop points.
2. Gate: wait for approval when the action is broad or gated.
3. Execute: delegate implementation to the right implementation agent.
4. Digest: return compact result and update or prepare plan status for `update-plan`.

Do not commit, push, open PRs, publish releases, or perform branch-history operations unless the root gated-action rule allows that exact action.
