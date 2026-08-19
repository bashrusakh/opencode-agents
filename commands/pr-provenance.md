---
description: "Verify branch provenance before commit, push, PR creation, or PR update."
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


## PR Body Sync

For PR mutation, follow-up commits/pushes, PR creation/update, or PR-ready publication, verify after the final intended diff and validation that the PR title/body still match actual commits, changed files, scope, behavior, and validation. If stale or incomplete, update it when PR publication/update is already allowed by the normalized request; otherwise draft the corrected body and ask. Final report must include: `PR body: updated | unchanged | drafted | skipped — <reason>`.

## PR Branch Provenance

Run a read-only branch provenance check against the project/PR base. Default to `<base_ref>=origin/main` only when no other base is known.

```bash
git status -sb
git branch -vv
git remote -v
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git status -sb
git log --oneline --decorate <base_ref>..HEAD
git log --oneline --decorate --left-right --cherry-pick <base_ref>...HEAD
git diff --name-status <base_ref>...HEAD
git diff --stat <base_ref>...HEAD
```

For a new independent task, `<base_ref>..HEAD` and `<base_ref>...HEAD` must be empty before edits. For an existing PR follow-up, ahead commits/files are allowed only when they belong to the same PR/task.

If the branch tracks upstream and is behind, report whether a safe `git pull --ff-only` is possible. If it diverged, remote head changed unexpectedly, or unrelated work appears, report unsafe and stop. Do not edit, commit, push, rebase, reset, or force-push in this command unless the user separately approves that gated action.

Report:

- base ref and current branch
- upstream tracking branch and branch state
- task branch status: new clean / existing PR / user-approved / unsafe
- commits ahead of base
- changed files
- unrelated commits/files: yes/no
- whether edit/commit/push/PR is safe
- required cleanup if unsafe

Check this branch/PR provenance: $ARGUMENTS
