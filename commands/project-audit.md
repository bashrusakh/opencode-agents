---
description: Run a broad read-only project audit for logic bugs, dead code, wrong fix levels, duplicate logic, test gaps, UI/API mismatches, and optimization opportunities.
agent: project-auditor
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

Run a full project audit for: $ARGUMENTS

Do not edit files, apply patches, commit, push, open PRs, or open issues. Orchestrate specialist subagents for audit areas that need an independent pass, continue automatically through safe read-only/review/verification stages, and return one consolidated markdown report with green/yellow/red stage status.

Focus on:
- project structure and core flows
- logic bugs and incorrect assumptions
- dead/stale/unreachable code
- wrong-level fixes and duplicated local patches
- UI/API drift and frontend/backend mismatch
- auth/permission/data-safety risks
- test gaps and verification results
- practical optimization opportunities
