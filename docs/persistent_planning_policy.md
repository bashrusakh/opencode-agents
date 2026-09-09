# Persistent Planning Policy

The root `AGENTS.md` Persistent Planning section is normative. This document defines the canonical repository-file interface when durable planning artifacts are actually in scope.

Use persistent planning when semantic normalization shows that work is broad, long-running, multi-session, multi-agent, phased, or likely to lose necessary coordination state. Example phrases are not triggers by themselves.

## Core principle

When repository planning artifacts are authorized, use one canonical `plans/<plan>/` directory as durable task/coordination state. Do not invent parallel workflow directories or agent-specific report files.

GrayMatter memory/checkpoints complement this interface:

- memory stores durable conclusions/preferences that are not already authoritative in project files;
- checkpoints store transient unfinished-task continuation state;
- existing canonical plan files remain the authority for the plan itself.

For read-only/audit workflows, do not create or modify repository plan files merely to preserve agent state. Reuse an existing plan when present; otherwise use checkpoint/runtime state unless plan-file mutation is separately authorized.

## Canonical layout

```text
plans/<plan>/
  plan.md
  phases/
    phase-N.md
  implementation/
    phase-N-impl.md
  reviews/
    plan-review.md
    impl-plan-review-phase-N.md
    impl-review-phase-N.md
  todo.md
  handovers/
    session-YYYY-MM-DD.md
```

Project documentation may live in the project's existing `docs/` structure when the task actually requires documentation. Do not create generic `audit-notes.md`, model-specific reports, or `final-final.md` files merely to persist chat output.

## Planning entities

| Entity | File | Purpose |
|---|---|---|
| Plan | `plan.md` | objective, requirements, Definition of Done, phase overview |
| Phase | `phases/phase-N.md` | what the phase delivers and why |
| Implementation plan | `implementation/phase-N-impl.md` | grounded file/symbol-level execution approach |
| Review | `reviews/*.md` | independent review artifact when such an artifact is in scope |
| Todo | `todo.md` | current items/status/changelog/next action |
| Handover | `handovers/session-*.md` | concise session continuity when durable handover is useful |

Phases define what/why; implementation plans define how. Do not silently change accepted scope while changing the technical approach.

## Typical lifecycle

Apply stages semantically rather than mechanically:

1. clarify objective/scope;
2. create/resume canonical plan state when needed and authorized;
3. review plan when independent plan review is materially useful;
4. author the active implementation plan grounded in actual files/symbols;
5. when complexity/design escalation is the reason for planning, establish the shared invariant/state/transition/interleaving model and bounded work packages before implementation;
6. review that plan when risk/complexity warrants it;
7. execute the current work package via `Blueprint -> Gate -> Execute -> Digest`;
8. review the stable implementation candidate when root reviewer/readiness criteria apply;
9. update canonical status/todo/decision state;
10. write a handover only when another session/agent genuinely needs durable continuation.

## Blueprint -> Gate -> Execute -> Digest

- **Blueprint** — bounded steps, target behavioral/surface boundary, files, checks, material risks, stop/escalation points, and—when complexity escalation applies—the invariant/interleaving cases this package must preserve.
- **Gate** — check the work package against current authorization; do not ask again for unchanged scope already authorized.
- **Execute** — route implementation to a capable role. Orchestrators/planners do not absorb implementation when delegation fails.
- **Digest** — reconcile current evidence, ensure any required canonical plan-file update is performed by a role allowed to maintain planning artifacts, and return a compact result.

Git/publication actions remain governed by the root gates and Git/PR policy.

## Resume protocol

Before resuming an existing plan, read the applicable current state:

1. `plan.md`;
2. `todo.md`;
3. active `phases/phase-N.md`;
4. active `implementation/phase-N-impl.md` when implementation is next;
5. relevant current reviews;
6. latest relevant handover;
7. current project-local rules.

Then state the current phase/item, blockers, and next safe action. Do not restart from zero unless the canonical state is missing/unusable.

## Multi-agent rules

- one canonical plan directory per long-running task;
- specialists read the state relevant to their assigned work;
- subagents return compact evidence/digests rather than giant dumps;
- the primary/orchestrator owns scope, stage order, current findings set, evidence reconciliation, user interaction, and Git/publication gates;
- every delegated work package is a hard behavioral/target boundary: specialists may choose execution details inside it but report required scope expansion back to the orchestrator before acting;
- implementation roles execute only the authorized work package and do not silently fix adjacent findings;
- a failed specialist does not transfer its prohibited capability to the caller;
- update existing canonical artifacts rather than creating competing side reports.

## Status vocabulary

Prefer a small stable set when `todo.md` needs status values:

```text
new
active
blocked
needs-review
approved
in-progress
done
deferred
rejected
```

Keep status changes concise and evidence-based. Do not add ceremony when a simpler existing project status convention already exists.
