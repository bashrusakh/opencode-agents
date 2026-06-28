---
description: "Handle follow-up work for an existing PR: review comments, failed checks, requested fixes, implementation, verification, and optional commit/push when the gated-action rule allows that exact action."
agent: code-workflow-orchestrator
subtask: true
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

Run the existing-PR follow-up workflow for: $ARGUMENTS

Treat this as follow-up work for the existing PR by default. Work on the same PR branch. Creating a separate PR is a gated action; proceed only when separate-PR creation is the clear normalized deliverable and the gated-action rule allows it.

Inspect current branch/status/diff and PR context. If PR metadata is unavailable, report the missing source instead of guessing. Orchestrate the needed subagents. Continue automatically through safe stages. Return one consolidated markdown report with green/yellow/red stage status.

Commit or push only when the gated-action rule allows that exact commit/push/update action.

## Existing PR branch rule

Before changing code on an existing PR branch, fetch the PR base, run the provenance gate, and confirm the branch contains only work for that PR. If the branch includes unrelated commits/files from another PR or issue, stop and report the polluted branch state. Do not add follow-up fixes on top of a polluted branch.
