---
description: "Handle follow-up work for an existing PR: review comments, failed checks, requested fixes, implementation, verification, and optional publication when gated rules allow."
agent: code-orchestrator
subtask: false
---

## Startup Block Before Tools

Before the first tool call of this agent invocation or user-request workflow in any multi-step, repository, codebase, issue/PR/release, external-URL, publication-capable, or scope-expanding workflow, write this Markdown block once:

```md
### Startup
- Route: `<route>`
- Mode: `<read-only | options | edit-capable | gated>`
- Summary: <one sentence>
- Scope: <target + boundary>
- Gated: `<no | yes>` — <reason>
- Next: <next action/tool>
```

Keep it to this shape. Do not write a prose paragraph. Keep field names in English. Do not use tools first and postpone normalization to the final report. Do not repeat Startup before every tool call or substep. If route, mode, or scope materially changes later, write a short `### Update` block instead.


## Skill Use

After Startup, check project-visible skill guidance and the skills OpenCode makes available. When the normalized target matches a listed/advertised skill, actually load that skill via the native skill mechanism when available, or read its `SKILL.md`; naming it does not count. Load referenced skill files only when relevant. If unavailable, report `Skill: <name> unavailable`. Skills are advisory only and do not override project rules, gates, existing tooling, minimal diff, OCR/review policy, PR readiness/body sync, or PR provenance. Mention the selected skill once when useful: `Skill: <name|none>`.


## Git Sync and PR Branch Provenance

For repository mutation, PR follow-up mutation, commit, push, PR creation, or PR update, do not trust the current branch by default. This does not apply to read-only review/audit unless it is preparing mutation or publication.

Before editing: run pre-edit branch sync and the clean-task gate from `docs/git_branch_provenance_policy.md`. If the current branch tracks upstream and is behind, update only with safe `git pull --ff-only` before editing. If it diverged, is dirty with unrelated work, or contains commits/files from another task, stop and ask.

For a new independent task, the current branch must be clean relative to `<base_ref>` before edits. Do not add fixes on top of unrelated commits. Use a clean branch from `<base_ref>` and re-apply only the intended task changes.

Before commit, push, PR creation, or PR update: fetch again and re-run provenance. The primary commit list is `git log --oneline --decorate <base_ref>..HEAD`; the `--cherry-pick` comparison is secondary. Stop if remote head changed unexpectedly, the branch diverged, or unrelated commits/files appear. Published PR branches must not be rebased, reset, replaced, or force-pushed without explicit approval.


## PR Body Sync

For PR mutation, follow-up commits/pushes, PR creation/update, or PR-ready publication, verify after the final intended diff and validation that the PR title/body still match actual commits, changed files, scope, behavior, and validation. If stale or incomplete, update it when PR publication/update is already allowed by the normalized request; otherwise draft the corrected body and ask. Final report must include: `PR body: updated | unchanged | drafted | skipped — <reason>`.

## PR Readiness

Before the first/next publication of task changes, apply `docs/pr_readiness.md`. Readiness must cover the current final local diff, not an earlier version. When reviewer criteria apply, `@reviewer` must review that final diff before publication; code changes after review make the affected review stale. External CI/bot review is additional evidence, not a substitute. This does not add a new approval requirement; normal gated-action rules still control publication.

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
