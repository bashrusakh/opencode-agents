---
description: Review code/diff/PR/commit/branch/workspace using @reviewer; prefer OCR/open-code-review when available and approved.
agent: reviewer
subtask: true
---

## Startup Checkpoint Before Tools

Before the first tool call in any multi-step, repository, codebase, issue/PR/release, external-URL, publication-capable, or scope-expanding workflow, write:

```text
Startup completed. Route: <route>. Mode: <read-only/options/edit-capable/gated>.
```

Include outcome, target, action level, confidence, and `gated: yes/no`. If the next step is read-only, say `gated: no — read-only`. If discovery could expand scope, state the scope boundary before using tools. Do not use tools first and postpone normalization to the final report.

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
