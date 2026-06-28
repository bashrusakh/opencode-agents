---
description: Review completed implementation against the persistent plan, acceptance criteria, tests, and behavior contract.
agent: reviewer
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

## User-Facing Output Formatting

For any user-visible answer or published text — final reply, PR/issue/release body, PR review/comment, changelog, handover, plan artifact, or Markdown doc — use readable target-aware Markdown by default.

- Start with a short summary.
- Use headings/sections when there is context, reasoning, validation, conclusion, or next action.
- Use bullets for multiple reasons, risks, checks, files, or decisions.
- Use fenced code blocks for commands, logs, paths, config, or exact proposed text.
- Avoid dense wall-of-text paragraphs.
- For OpenCode CLI, Hermes, Telegram, terminals, or chat relays, prefer compact portable Markdown/plain text; avoid raw HTML, oversized tables, deeply nested lists, and GitHub-only formatting.
- For GitHub/GitLab PRs, issues, releases, and review comments, use clean Markdown with a clear conclusion/next action.



## OCR Review Backend

When reviewing code/diff produced by the implementation, prefer OCR/open-code-review if installed and allowed. Use OCR as the review engine, then add reviewer judgment for plan acceptance criteria, behavioral contract, right-level fix, and test coverage. Do not apply fixes during review.

## Purpose

Provide an independent quality gate after a work package implementation from `plans/<plan>/`.

## Required behavior

- Read the plan, phase, implementation plan, todo, and current diff.
- Review correctness, tests, security, behavior contract, right-level fix, and acceptance criteria.
- Write or return a review suitable for `plans/<plan>/reviews/impl-review-phase-N.md`.
- Do not edit source files.
