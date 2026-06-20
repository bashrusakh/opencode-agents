---
description: "Run a full bugfix workflow in one request: investigate, fix, verify, and review according to normalized intent."
agent: code-workflow-orchestrator
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

## User-Facing Output Formatting

For any user-visible answer or published text — final reply, PR/issue/release body, PR review/comment, changelog, handover, plan artifact, or Markdown doc — use readable target-aware Markdown by default.

- Start with a short summary.
- Use headings/sections when there is context, reasoning, validation, conclusion, or next action.
- Use bullets for multiple reasons, risks, checks, files, or decisions.
- Use fenced code blocks for commands, logs, paths, config, or exact proposed text.
- Avoid dense wall-of-text paragraphs.
- For OpenCode CLI, Hermes, Telegram, terminals, or chat relays, prefer compact portable Markdown/plain text; avoid raw HTML, oversized tables, deeply nested lists, and GitHub-only formatting.
- For GitHub/GitLab PRs, issues, releases, and review comments, use clean Markdown with a clear conclusion/next action.

## Persistent Planning Mode

For long-running, multi-session, or multi-agent work, use `plans/<plan>/` as durable state. Read existing plan artifacts before continuing. Do not create arbitrary markdown reports. Use compact digests and update canonical plan/docs artifacts when the command is responsible for planning state.

Run the bugfix workflow for: $ARGUMENTS

Do not make the user manually run every agent. Orchestrate the needed subagents, continue automatically through safe stages, and return one consolidated markdown report with green/yellow/red stage status.

Use @explore when the code path is not identified. Use @tester when reproduction or verification is needed. Use @debugger for root cause and the smallest right-level fix. Use @fix-level-reviewer or @reviewer for diffs touching shared behavior, security, data handling, API contracts, concurrency, or logic with edge cases/state transitions not obvious from one local function.

Do not commit, push, open PRs, or publish anything unless the gated-action rule allows that exact action.
