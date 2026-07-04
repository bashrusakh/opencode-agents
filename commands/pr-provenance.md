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

Report:

- base ref and current branch
- upstream tracking branch and branch state
- commits ahead of base
- changed files
- unrelated commits/files: yes/no
- whether edit/commit/push/PR is safe
- required cleanup if unsafe

Do not edit, commit, push, rebase, reset, or force-push in this command unless the user separately approves that gated action.

Check this branch/PR provenance: $ARGUMENTS
