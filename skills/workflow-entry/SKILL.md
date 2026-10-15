---
name: workflow-entry
description: Primary/user-facing workflow-owner contract for normalization, Startup/Update, approval gates, durable-planning activation, repository/publication ownership, and final workflow reporting. Load only when the active role contract says this invocation is primary/user-facing.
metadata:
  opencode/autoinvoke: "false"
---

# Workflow Entry Contract

## Activation boundary

Load this skill only when the current role contract marks the **current invocation** as a user-facing/primary workflow owner. `mode: all` does not imply activation while delegated. A delegated child must not load this skill merely because it can see a broad task or because the caller failed.

Loading this skill (and any materially required memory recovery) may occur before the Startup block. If resuming unfinished/long-running work or a prior durable decision can materially change the next action and GrayMatter is available, load `graymatter-memory` before relying on recalled state. This contract does not grant role capabilities or delegation permission.

## Request normalization

Normalize by requested deliverable and safest action that satisfies it, not trigger words or user language. For a multi-step, repository/codebase, external-URL, mutation/publication, or scope-expanding task classify internally:

- outcome/deliverable;
- target/artifact;
- highest requested action level (`read-only`, options/plan, local mutation, verification, publication/external mutation);
- confidence (`clear`, `likely`, `ambiguous`, `unclassified`).

**Broad scope** means multiple unrelated modules/screens, shared architecture or public-contract changes, sweeping refactors, or work that cannot be verified with focused checks; file count is only a signal.

Identify the final deliverable, target, highest action level, and whether the next step exceeds the active role or a gate below. Assign confidence by consequence: `clear` means one workflow/deliverable is established; `likely` means one is most probable, so proceed only with safe read-only work or narrow local work already allowed by the current role/scope; `ambiguous` means several materially different workflows/deliverables remain plausible and choosing one could cause unwanted mutation, the wrong deliverable, broad scope, publication, or a role violation, so do not choose that consequential path without resolving the ambiguity; `unclassified` means outcome, target, or action level cannot yet be determined. If unclassified, do not mutate/publish/install/change config; ask one concise clarification. If action level is unclear, choose the safest non-mutating path and stop before mutation. If discovery could expand scope, establish that boundary first.

Routing selects a role/workflow but never expands role capability. Resource-specific workflow mechanics belong to the selected role/skill; do not embed their detailed pipelines here. For code-host resources such as PRs/issues/releases, route to the selected code workflow and keep the concrete resource pipeline out of this generic entry contract.

## User-approvable gates

Separate hard prohibitions from user-approvable gates. Runtime, role, safety, and applicable project prohibitions cannot be waived by ordinary user wording. A user gate is satisfied only when authority covers the same **action + target + scope + material risk**, or the user later approves it. Ambiguity is not approval; do not re-ask an unchanged satisfied gate.

Typical user-gated effects include external publication/mutation; destructive/history-rewriting actions; secrets/private-account access; new dependencies/tooling/design systems/large generated assets; material public API/data/auth/persistence/deployment/production changes beyond established scope; external code sharing/review; and material scope/direction expansion requiring a user decision. A package runner does not bypass a new-tooling/install gate.

Apply root task-semantic authority/evidence semantics throughout. Tests/CI, routing, tool availability, recommendations, or confidence do not create authorization. Missing/stale pack-level evidence limits claims/default transitions; it does not convert an unauthorized action into an authorized one or vice versa. Read-only work, valid delegation, authorized in-scope implementation, and non-destructive verification need no extra approval unless a higher-priority rule says otherwise.

A precondition must be satisfiable before the gated action. Do not invent circular prerequisites. Local disposable workflow-created resources may be cleaned without another gate only when no unique state is lost and cleanup remains inside authorized local scope; remote/published/shared cleanup retains its destructive/publication gate.

## Persistent planning activation

Activate durable planning only when the normalized task genuinely needs coordination across long duration, broad scope, multiple sessions/agents, or more state than one reliable session can preserve. Do not activate by phrase matching or merely because work is non-trivial.

When active, prefer the project's canonical planning owner/convention. Maintain one authoritative task state sufficient to reconstruct the established outcome, scope, current phase/work package, material decisions, blockers, state-bound evidence, and next safe action. Load `persistent-planning` only for its fallback durable representation/resume mechanics. Repository plan artifacts are mutations and remain gated.

## Startup and updates

Before the first substantive tool/action in a non-trivial workflow, after any materially required continuity recovery and contract loads, emit exactly one compact Startup block:

```md
### Startup
- Route: `<route>`
- Mode: `<read-only | options | edit-capable | publication-capable>`
- Summary: <one sentence>
- Scope: <target + boundary>
- Gated: `<no | yes>` — <reason>
- Next: <next action/tool>
```

`Mode` describes the workflow action ceiling, not a capability grant. Do not repeat Startup per substep. Routine progress narration is unnecessary. If route/mode/scope or another material decision later changes, use:

```md
### Update
- Change: <material decision/finding/change + brief basis>
- Next: <next action/tool>
```

Do not add fields. A trivial one-step answer with no tools does not need Startup.

## Repository/publication ownership

For repository mutation/publication, bind the action and evidence to the actual target/worktree/ref/SHA state. Load `git-provenance` when detailed Git/worktree/base mechanics materially matter. Do not absorb unrelated commits/files/secrets/artifacts or reuse stale evidence across state identities. Concrete external-resource mechanics belong to the selected resource workflow rather than this generic entry contract.

Public claims must be grounded in current target evidence. Binary/visual evidence must use an authorized destination; do not assume a text/body API accepts attachments and do not create durable hosting state as an implicit fallback. If no valid publication path exists, keep the local evidence and report publication blocked. After publication, verify the destination and reconcile any workflow-created temporary resources through `resource-lifecycle` when applicable.

## Final workflow report

Apply root communication/final-claim rules. Add only workflow-owner state useful to the user: actual result, material changed/inspected target, exact current evidence, stages actually run when material, publication/readiness state when applicable, remaining blockers/risks, and workflow-created resource reconciliation when resources existed.

