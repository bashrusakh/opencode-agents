---
description: Prepare or verify release notes from actual repository history; treat tags/releases/publication as gated actions.
agent: code-workflow-orchestrator
subtask: true
---

Run the release-prep workflow for: $ARGUMENTS

Check previous release/tag and current history/diff when repository history or release metadata is accessible; otherwise report the missing source. Build release notes only from actual commits, merged PRs, linked issues, and final code changes. Do not invent features, fixes, impact, or breaking changes.

Do not create tags or releases unless the gated-action rule allows that exact action. Return one consolidated markdown report with green/yellow/red stage status and release notes draft or verification result.
