---
description: Review a persistent plan for scope clarity, requirements, Definition of Done, risks, and phase boundaries.
agent: reviewer
subtask: true
---

## Startup Checkpoint Before Tools

Before the first tool call in any multi-step, repository, codebase, issue/PR/release, external-URL, publication-capable, or scope-expanding workflow, write:

```text
Startup completed. Route: <route>. Mode: <read-only/options/edit-capable/gated>.
```

Include outcome, target, action level, confidence, and `gated: yes/no`. If the next step is read-only, say `gated: no — read-only`. If discovery could expand scope, state the scope boundary before using tools. Do not use tools first and postpone normalization to the final report.

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

Provide an independent quality gate for `plans/<plan>/plan.md` and phase docs.

## Required behavior

- Do not edit source code.
- Check scope, requirements, DoD, phase boundaries, test strategy, missing risks, and ambiguity.
- Write or return a review suitable for `plans/<plan>/reviews/plan-review.md`.
- Classify result: approved / needs revision / blocked.
