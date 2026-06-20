---
description: Prepare or verify release notes from actual repository history; treat tags/releases/publication as gated actions.
agent: code-workflow-orchestrator
subtask: true
---

## Behavioral Contract Check

For any user-facing UI/config/API/workflow behavior change, do not implement only the data plumbing. Before planning or editing, summarize:

- user-facing action
- value source
- valid-value domain
- existing project pattern to inspect
- whether raw/internal/manual values would be exposed to normal users

Do not derive behavior directly from schema/storage/API type. Preserve the existing affordance class unless the normalized request explicitly asks for a raw/manual/editor workflow.

## Persistent Planning Mode

For long-running, multi-session, or multi-agent work, use `plans/<plan>/` as durable state. Read existing plan artifacts before continuing. Do not create arbitrary markdown reports. Use compact digests and update canonical plan/docs artifacts when the command is responsible for planning state.

Run the release-prep workflow for: $ARGUMENTS

Check previous release/tag and current history/diff when repository history or release metadata is accessible; otherwise report the missing source. Build release notes only from actual commits, merged PRs, linked issues, and final code changes. Do not invent features, fixes, impact, or breaking changes.

Do not create tags or releases unless the gated-action rule allows that exact action. Return one consolidated markdown report with green/yellow/red stage status and release notes draft or verification result.
