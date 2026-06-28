---
description: "Configure the UI MCP stack: official shadcn MCP with standard registry, official shadcn MCP with GitHub/public registries, and Jpisnice shadcn-ui-mcp-server with GitHub token."
agent: devops
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


## Git Sync and PR Branch Provenance

For repository mutation, PR follow-up, commit, push, or PR work, do not trust the current branch by default. Before edits or publication:

```bash
git status --short
git branch --show-current
git fetch origin <base>
git log --oneline --decorate --left-right --cherry-pick origin/<base>...HEAD
git diff --name-status origin/<base>...HEAD
git diff --stat origin/<base>...HEAD
```

Use the project/PR base, defaulting to `origin/main` only when no other base is known. Rebase/update before editing when safe and clean. If the branch contains unrelated commits/files, or rebase/update would rewrite public history or conflict, stop and ask. Do not open/push/update a PR with unrelated work.

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

Configure the local UI MCP stack for OpenCode: $ARGUMENTS

Use `docs/UI_MCP_INSTALL_FOR_AGENT.md` as the source of truth.

Do not overwrite existing config without backups. Configure official shadcn MCP as the primary MCP engine using the standard shadcn registry. Allow official shadcn MCP to use GitHub/public shadcn-compatible registries. Configure Jpisnice shadcn-ui-mcp-server as secondary/reference MCP with a GitHub token via local secret. UI UX Pro Max/UUPM is configured separately by `/uupm-setup` and is design intelligence only. Local/private/authenticated registry setup is a gated action.

Return one consolidated markdown report with green/yellow/red stage status and exact commands/results.
