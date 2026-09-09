---
description: "Verify branch provenance and base-to-head scope before commit, push, PR creation, or PR update."
agent: code-orchestrator
subtask: false
---

Verify PR/branch provenance for: $ARGUMENTS

Follow the active `AGENTS.md` and the applicable installed/project `git_branch_provenance_policy.md`.

Resolve the actual head remote, base remote, base branch/ref, tracking state, and existing PR context from repository evidence. Do not assume `origin/main` when the base is unknown.

Prove the task's complete base-to-head commit range and changed-file set, identify unrelated/pre-existing commits or files, and distinguish a clean task branch from a polluted/diverged branch.

This command is provenance verification, not implementation. Do not rewrite history or repair a polluted branch unless a separate authorized workflow requests that action.

When a specific PR is part of the provenance target, include its canonical PR URL and current Draft/Ready state in the report.
