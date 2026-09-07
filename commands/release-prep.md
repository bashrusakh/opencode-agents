---
description: "Prepare or verify release notes and release state from actual repository history; publish tags/releases only when explicitly in scope."
agent: code-orchestrator
subtask: false
---

Prepare or verify the release for: $ARGUMENTS

Follow the active `AGENTS.md` and code-orchestrator contract.

Ground release notes in actual repository/release evidence: previous release/tag, commits, merged PRs/issues, final diff, validation, and current release metadata when accessible. Do not invent features, fixes, impact, compatibility claims, or breaking changes.

If the deliverable is a draft/verification, stay non-publishing. If tag/release creation or update is clearly requested, apply the root authorization/readiness rules and verify the created/updated release before reporting completion.
