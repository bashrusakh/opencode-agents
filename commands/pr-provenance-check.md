---
description: Verify branch provenance before commit, push, PR creation, or PR update.
agent: code-workflow-orchestrator
subtask: true
---

## Startup Checkpoint Before Tools

Before the first tool call in any multi-step, repository, codebase, issue/PR/release, external-URL, publication-capable, or scope-expanding workflow, write:

```text
Startup completed. Route: <route>. Mode: <read-only/options/edit-capable/gated>.
```

Include outcome, target, action level, confidence, and `gated: yes/no`. If the next step is read-only, say `gated: no — read-only`. If discovery could expand scope, state the scope boundary before using tools. Do not use tools first and postpone normalization to the final report.

## Git Sync and PR Branch Provenance

Run a read-only branch provenance check against the project/PR base. Default to `origin/main` only when no other base is known.

```bash
git status --short
git branch --show-current
git fetch origin <base>
git log --oneline --decorate --left-right --cherry-pick origin/<base>...HEAD
git diff --name-status origin/<base>...HEAD
git diff --stat origin/<base>...HEAD
```

Report:

- base branch and current branch
- commits ahead of base
- changed files
- unrelated commits/files: yes/no
- whether commit/push/PR is safe
- required cleanup if unsafe

Do not edit, commit, push, rebase, reset, or force-push in this command unless the user separately approves that gated action.

Check this branch/PR provenance: $ARGUMENTS
