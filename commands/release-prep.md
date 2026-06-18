---
description: Prepare or verify release notes from actual repository history; never publish releases unless explicitly requested.
agent: code-workflow-orchestrator
subtask: false
---

Run the release-prep workflow for: $ARGUMENTS

Check previous release/tag and current history/diff when available. Build release notes only from actual commits, merged PRs, linked issues, and final code changes. Do not invent features, fixes, impact, or breaking changes.

Do not create tags or releases unless the user explicitly asked for that action. Return one consolidated markdown report with green/yellow/red stage status and release notes draft or verification result.
