---
description: Implement an already planned UI/web redesign using the existing frontend architecture.
agent: frontend-ui-implementer
subtask: true
---

## Startup Checkpoint Before Tools

Before the first tool call in any multi-step, repository, codebase, issue/PR/release, external-URL, publication-capable, or scope-expanding workflow, write:

```text
Startup completed. Route: <route>. Mode: <read-only/options/edit-capable/gated>.
```

Include outcome, target, action level, confidence, and `gated: yes/no`. If the next step is read-only, say `gated: no — read-only`. If discovery could expand scope, state the scope boundary before using tools. Do not use tools first and postpone normalization to the final report.

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

Implement the planned UI/web redesign for: $ARGUMENTS

Before editing, read project rules and inspect existing components/styles. Reuse current architecture. Keep the diff focused. New dependencies and new design systems are gated actions.


Read the detailed UI policy file defined in AGENTS.md when it exists.
