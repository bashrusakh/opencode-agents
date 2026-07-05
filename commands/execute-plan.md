---
description: "Execute an approved persistent-plan work package using Blueprint -> Gate -> Execute -> Digest."
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


## Git Sync and PR Branch Provenance

For repository mutation, PR follow-up mutation, commit, push, PR creation, or PR update, do not trust the current branch by default. This does not apply to read-only review/audit unless it is preparing mutation or publication.

Before editing: run pre-edit branch sync and the clean-task gate from `docs/git_branch_provenance_policy.md`. If the current branch tracks upstream and is behind, update only with safe `git pull --ff-only` before editing. If it diverged, is dirty with unrelated work, or contains commits/files from another task, stop and ask.

For a new independent task, the current branch must be clean relative to `<base_ref>` before edits. Do not add fixes on top of unrelated commits. Use a clean branch from `<base_ref>` and re-apply only the intended task changes.

Before commit, push, PR creation, or PR update: fetch again and re-run provenance. The primary commit list is `git log --oneline --decorate <base_ref>..HEAD`; the `--cherry-pick` comparison is secondary. Stop if remote head changed unexpectedly, the branch diverged, or unrelated commits/files appear. Published PR branches must not be rebased, reset, replaced, or force-pushed without explicit approval.

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
4. Digest: return compact result and update or prepare plan status for `/plan`.

Do not commit, push, open PRs, publish releases, or perform branch-history operations unless the root gated-action rule allows that exact action.
