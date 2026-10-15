---
name: code-host-workflow
description: Conditional code-host resource workflow for existing PR follow-up, issue/ticket/report handling, release/publication mechanics, host metadata/template discovery, and resource-specific reporting. Load only when code-orchestrator has normalized the active workflow to one of these code-host resources.
metadata:
  opencode/autoinvoke: "false"
---

# Code-host Resource Workflow

## Activation boundary

Load this skill only when the active `code-orchestrator` workflow targets an **existing PR**, **issue/ticket/report**, **release/tag**, or another public code-host resource as a requested deliverable. Do not load it for an ordinary bugfix, tests/docs-only task, local implementation, or generic review merely because the repository is hosted remotely.

This skill owns host-resource discovery and lifecycle-adjacent mechanics only. It does not grant repository-edit or publication authority. `workflow-entry` owns the user authorization/publication gate; `git-provenance` owns ref/SHA/worktree identity; `pr-readiness` owns the canonical **Owned PR** definition and Draft/Candidate/Ready lifecycle; `output-formatting` owns destination formatting; `resource-lifecycle` owns workflow-created temporary-resource reconciliation.

## Existing PR follow-up

Stay on the existing PR branch by default. At entry, resolve the canonical PR URL/resource identity, ownership, Draft/Ready state, head/base, effective diff, current review comments/checks, and known todo. Load `pr-readiness` for its canonical **Owned PR** definition before any ownership-dependent PR-state decision, and load `git-provenance` when detailed target/base/ref identity matters.

For a confirmed **Owned PR**, consume the `pr-readiness` lifecycle/state-transition contract; do not restate its Draft/Candidate/publication/Ready sequence here. Read-only review/planning does not itself mutate PR state, and an unowned or ambiguously owned PR is never auto-transitioned.

For “review this PR and fix what is wrong,” combine current host findings with any needed independent review, then return confirmed findings to the workflow owner in bounded groups rather than one-comment/one-patch cycles. A shared design/invariant gap is an escalation signal, not another host-specific patch ritual.

## Issue / ticket / report

Resolve the state the report targets before verification. For current upstream/default/base claims, use `git-provenance` to refresh and bind the authoritative ref/SHA when needed. For an explicitly local-workspace claim, use that workspace rather than fetching only for formality. Distinguish confirmed facts from suspected root cause.

Search existing issues when repository access makes that relevant before creating a duplicate. Draft/open an issue only when issue creation is in scope and authorized by the active `workflow-entry` gate. Treat repository implementation as a separate deliverable: request an implementation stage only when changed code/config/UI/tests/docs is separately established as requested scope.

## Release / host publication

Build release notes/check inputs from actual repository history, relevant PR/issues, current code state, and current verification evidence. Repository changelog/docs/config edits remain a separate implementation stage. Tag/release/public publication stays under the active `workflow-entry` gate.

Discover applicable repository publication/template guidance before drafting a public PR/issue/release artifact when the resource requires it. For PR metadata, do not infer that no template/guidance exists merely because it is absent from the current worktree; consult available repository-host metadata when needed. Public claims must remain grounded in current target evidence.

For substantial PR/issue/release/review artifacts, load `output-formatting` when destination-specific formatting materially helps. After creation/update, verify the published resource identity plus material metadata/body before reporting publication complete. Reconcile workflow-created temporary resources through `resource-lifecycle` when applicable.

## Resource result contract

Return the canonical resource URL/identity when available, current host state, material comments/checks/todo or duplicate-search result, publication result, and any blocker that remains outside the resource workflow. Feed host findings back to the `code-orchestrator` findings model; this skill does not own code mutation.

For an owned final PR candidate/readiness result, report the exact Base/Candidate/remote-head/readiness identity required by `pr-readiness` without duplicating its state machine. An owned PR reaching its final readiness boundary is a terminal resource success for any active terminal workflow-evaluation hook.
