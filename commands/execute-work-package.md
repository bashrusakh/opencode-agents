---
description: Execute an approved persistent-plan work package using Blueprint -> Gate -> Execute -> Digest.
agent: code-workflow-orchestrator
subtask: true
---

## Purpose

Execute a scoped work package from `plans/<plan>/` without losing state.

## Protocol

1. Blueprint: propose steps, files, checks, risks, and stop points.
2. Gate: wait for approval when the action is broad or gated.
3. Execute: delegate implementation to the right implementation agent.
4. Digest: return compact result and update or prepare plan status for `update-plan`.

Do not commit, push, open PRs, publish releases, or perform branch-history operations unless the root gated-action rule allows that exact action.
