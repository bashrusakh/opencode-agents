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


## Skill Use

After Startup, check project-visible skill guidance and the skills OpenCode makes available. When the normalized target matches a listed/advertised skill, actually load that skill via the native skill mechanism when available, or read its `SKILL.md`; naming it does not count. Load referenced skill files only when relevant. If unavailable, report `Skill: <name> unavailable`. Skills are advisory only and do not override project rules, gates, existing tooling, minimal diff, OCR/review policy, PR readiness/body sync, or PR provenance. Mention the selected skill once when useful: `Skill: <name|none>`.


## Git Sync and PR Branch Provenance

For repository mutation, PR follow-up mutation, commit, push, PR creation, or PR update, do not trust the current branch by default. This does not apply to read-only review/audit unless it is preparing mutation or publication.

Before editing: run pre-edit branch sync and the clean-task gate from `docs/git_branch_provenance_policy.md`. If the current branch tracks upstream and is behind, update only with safe `git pull --ff-only` before editing. If it diverged, is dirty with unrelated work, or contains commits/files from another task, stop and ask.

For a new independent task, the current branch must be clean relative to `<base_ref>` before edits. Do not add fixes on top of unrelated commits. Use a clean branch from `<base_ref>` and re-apply only the intended task changes.

Before commit, push, PR creation, or PR update: fetch again and re-run provenance. The primary commit list is `git log --oneline --decorate <base_ref>..HEAD`; the `--cherry-pick` comparison is secondary. Stop if remote head changed unexpectedly, the branch diverged, or unrelated commits/files appear. Published PR branches must not be rebased, reset, replaced, or force-pushed without explicit approval.


## PR Body Sync

For PR mutation, follow-up commits/pushes, PR creation/update, or PR-ready publication, verify after the final intended diff and validation that the PR title/body still match actual commits, changed files, scope, behavior, and validation. If stale or incomplete, update it when PR publication/update is already allowed by the normalized request; otherwise draft the corrected body and ask. Final report must include: `PR body: updated | unchanged | drafted | skipped — <reason>`.

## OCR Review Backend

For code, diff, commit, branch, workspace, or PR review, prefer OCR/open-code-review when installed and allowed. OCR is read-only locally but may send code/diffs/context to the configured OCR LLM provider, so privacy approval is required when not already covered by user/project policy.

If OCR is available and approved, use agent-friendly output:

```bash
ocr review --audience agent --timeout 10 --background "<project/request context>"
```

Use scoped OCR flags when the target is known: `--commit`, `--from`, `--to`, or `--preview`. Do not run OCR with a 120-second shell/tool timeout; set the surrounding shell/tool timeout to at least 10 minutes when supported. If OCR is unavailable, not configured, or not approved, fall back to native read-only review and say why.

Do not edit files, apply patches, run formatters, stage, commit, push, publish, or apply OCR suggestions unless the user separately asks for fixes and the gated-action rule allows the exact action.

## User-Facing Output Formatting

Use readable Markdown: short summary, severity sections, bullets for findings, code fences for commands/output, exact file/line references, and clear verdict/next action.

Review this code/diff/PR/commit/branch/workspace: $ARGUMENTS

If no target is specified, review the current git diff/workspace according to OCR/default reviewer behavior.
