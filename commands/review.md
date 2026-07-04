---
description: "Review code, diff, PR, branch, plan, implementation plan, completed implementation, or fix level using @reviewer; prefer OCR/open-code-review when available and approved."
agent: reviewer
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

Before edits or publication:

```bash
git status -sb
git branch -vv
git remote -v
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git status -sb
git log --oneline --decorate <base_ref>..HEAD
git diff --name-status <base_ref>...HEAD
git diff --stat <base_ref>...HEAD
```

Use explicit refs such as `<base_remote>=origin`, `<base_branch>=main`, `<base_ref>=origin/main`. If the branch tracks upstream and is behind, fast-forward/update before editing only when clean and safe. If it diverged, contains unrelated work, or update/rebase would rewrite published history or conflict, stop and ask.

## OCR Review Backend

For code, diff, commit, branch, workspace, or PR review, prefer OCR/open-code-review when installed and allowed. OCR is read-only locally but may send code/diffs/context to the configured OCR LLM provider, so privacy approval is required when not already covered by user/project policy.

If OCR is available and approved, use agent-friendly output:

```bash
ocr review --audience agent --background "<project/request context>"
```

Use scoped OCR flags when the target is known: `--commit`, `--from`, `--to`, or `--preview`. If OCR is unavailable, not configured, or not approved, fall back to native read-only review and say why.

Do not edit files, apply patches, run formatters, stage, commit, push, publish, or apply OCR suggestions unless the user separately asks for fixes and the gated-action rule allows the exact action.

## User-Facing Output Formatting

Use readable Markdown: short summary, severity sections, bullets for findings, code fences for commands/output, exact file/line references, and clear verdict/next action.

Review this code/diff/PR/commit/branch/workspace: $ARGUMENTS

If no target is specified, review the current git diff/workspace according to OCR/default reviewer behavior.
