# Contract / protocol audit — v30.92 beta

## Scope

v30.92 changes semantic state typing, root/orchestrator ownership placement, and release-control coverage. Agent permission/frontmatter policy is deliberately out of scope and unchanged.

## Canonical ownership / placement

- **Root `AGENTS.md`** owns shared normalization, authority/evidence algebra, user-decision binding, authorization gates, generic delegation/independence, review activation/cadence, failed-fix reset, repository/provenance/publication discipline, and final-report policy.
- **`agents/code-orchestrator.md`** owns accountable workflow synthesis, code-specific routing discriminators, controller activation/consumption, findings/escalation, detailed bugfix/PR/issue/tests-docs/release-prep mechanics, and role-local evidence consumption.
- **`skills/pr-readiness/SKILL.md`** owns the reusable owned-PR Draft/Candidate/publication/Ready lifecycle state machine.
- **Specialist roles** retain their own role-local verdicts/methods; shared root contracts are inherited rather than copied for executability.

## Typed semantic domains

The release declares four current durable domains:

- evidence status: `established | unverified | contradicted`;
- proposition relation: `preserved | refined | strengthened | weakened | substituted | indeterminate`;
- semantic-checkpoint workflow verdict: `proceed | hold | insufficient-context`;
- trajectory-auditor workflow verdict: `continue | reanchor | reassess | checkpoint-required | insufficient-evidence`.

The audit discovers role `Verdict`/`Verdict semantics` enums and rejects typed literals assigned to more than one semantic domain.

## Root/orchestrator section map

All current `##` / `###` sections in root and code-orchestrator are explicitly mapped as shared owner/boundary, role owner, specialization, or reference consumer. Adding or moving a material section makes the section audit fail until placement is reviewed.

The map also confirms the repository-workflow split:

`root normalization/gates -> code-orchestrator detailed PR + issue mechanics -> pr-readiness owned-PR lifecycle`.

## Gate composition

The aggregate release runner now includes:

- contract/protocol selftest;
- semantic-ownership selftest + audit;
- semantic-domain selftest + audit;
- section-ownership selftest + audit;
- static policy regressions;
- installer safety;
- contract/protocol role executability;
- role-handoff selftest + closed-world edge audit.

Behavioral replay remains separate and is not inferred from structural PASS.
