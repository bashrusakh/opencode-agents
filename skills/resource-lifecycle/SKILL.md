---
name: resource-lifecycle
description: Use when the workflow deliberately creates temporary worktrees, branches, files, processes, evidence workspaces, or hosted resources that require cleanup reconciliation. Root AGENTS.md remains authoritative.
---

# Resource lifecycle

## What enters the lifecycle

Track resources deliberately created or repurposed by the current workflow for temporary execution, isolation, verification, or evidence: temporary worktrees/checkouts, local branches, temp files/directories, local servers/processes, generated evidence files, and temporary hosted/publication resources. Ordinary project/tool-managed caches and incidental build outputs are not automatically workflow-owned.

## Ownership

Creation creates a cleanup obligation. The creator owns cleanup by default; explicit handoff transfers it. A delegated specialist cleans safe local temporary resources before returning or reports each remaining resource/status. If the specialist fails before reporting cleanup, status is `unknown`; the workflow owner reconciles known/discoverable resources before claiming completion. Pre-existing resources are never implicitly owned because they look temporary.

## Reconciliation

Track related resources independently: a worktree, local branch, remote ref, process, local evidence file, and hosted artifact are separate identities. Before completion, every known workflow-created temporary resource is exactly one of:

```text
cleaned
intentionally retained
cleanup blocked
ownership transferred
```

Prefer cleanup after the last consumer. Auto-clean a local resource only when workflow ownership is established, it is no longer needed, it contains no unique/unpreserved state, and removal stays within authorized local scope. Never force cleanup across uncertain ownership or unique state. Remote/published/shared teardown retains its destructive/publication gate; creation/publication authorization does not automatically authorize later deletion.

For visual evidence, preserve the durable screenshot/result first, stop temporary processes, verify worktree/branch state is disposable, clean safe local resources, and reconcile any remote/hosted resource separately. Durable evidence and its temporary execution environment are different resources.
