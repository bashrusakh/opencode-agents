#!/usr/bin/env python3
"""Synthetic anti-gaming tests for closed-world caller -> specialist edge contracts."""
from __future__ import annotations
import importlib.util, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('edge',HERE/'role-handoff-audit.py')
m=importlib.util.module_from_spec(spec); sys.modules[spec.name]=m; spec.loader.exec_module(m)
fail=[]
def ck(x,msg):
    if not x: fail.append(msg)

def findings(c,o,u): return m.audit_texts({'code-orchestrator':c,'ui-orchestrator':u,'auditor':o})
# Start from semantic-good fixtures unrelated to current prose.
good_code='''For every delegation pass objective and behavioral/target scope, allowed action level, expected deliverable/evidence, and stop or escalation conditions; omit upstream non-required mechanism proposals or label them explicitly non-binding. After a material specialist result perform a bounded workflow-owner synthesis loop: ingest facts/evidence, hypotheses, recommendations and unresolved questions; reconcile them with the task anchor/current state/other evidence; update the whole-task model; decide the exact next question/action; only then delegate. A specialist's recommended next role, stage, mechanism or remediation is input, not a workflow transition, and an independent controller is not a substitute for an ordinary owner decision. For devops pass the operational symptom and target environment, current evidence, action ceiling and authorized scope; do not assign a suspected config change as diagnosis, it remains a hypothesis. For librarian pass the bounded external research proposition, named external target, material version/range/environment or permission to establish it from direct metadata, allowed source/evidence scope and stop/applicability boundary; do not ask it to trace local usage or turn an upstream suspicion into the local diagnosis. For general pass one bounded research question with allowed evidence/source scope and stop when another specialist owns it. For UI routing distinguish a settled user-visible outcome from unresolved presentation/interaction direction. If materially different layout, information-hierarchy, disclosure, interaction, or error-state treatments remain, or user feedback rejects the current treatment without adopting its replacement, delegate the bounded UI domain to @ui-orchestrator; do not invent the missing UI direction and pass it downstream as an established outcome. Direct @ui-implementer work is appropriate only when the material UI choice is established and focused mechanics remain. For UI implementation pass the established user-visible outcome, target/mutation state, material constraints and preserved behavior; do not preselect files or layout mechanics. Retain a task anchor and correction epoch model for end-to-end acceptance paths. When repeated corrections or same-policy counterexamples materially challenge the model, perform bounded owner trajectory reassessment first; if it yields one evidence-backed model, continue without a trajectory audit. Invoke a fresh @trajectory-auditor only when an exact longitudinal question remains unresolved after that owner reassessment or the user explicitly requests independent trajectory review. Pass owner reassessment performed, current owner model, exact unresolved trajectory question, why available primary evidence could not safely resolve it, current parent session ID, task anchor, material transitions and proposed next transition; the packet is a workflow-owner report, not proof. Consume exactly continue, reanchor, reassess, checkpoint-required, or unverified. For semantic checkpointing, first perform owner reconciliation and invoke fresh @semantic-checkpoint only for an exact semantic proposition whose authority remains unresolved or an explicit policy gate; pass owner reconciliation performed, strongest known authority/evidence, mutation boundary and why the owner cannot safely settle it. Do not invoke semantic checkpoint merely because technical owner, fix level, abstraction, invariant representation or necessary implementation scope changed under settled behavior. For a fresh whole-change/final reviewer judgment pass the exact requested target or Base/Candidate identity and authoritative task-contract propositions. Do not add a parent-authored Focus/Risks/Recent-fixes checklist from prior review/fix history and do not seed prior reviewer/OCR verdicts or findings; let the reviewer derive its risk model from the Candidate/effective diff. If user or project policy explicitly requests a review emphasis, pass it as additive and non-exhaustive. For a targeted re-review pass the known finding explicitly and keep the verdict partial/incremental.'''
good_ui='''Construct leaf assignments from the established UI outcome/problem, exact target/state when relevant, material constraints, evidence, and the leaf's question; do not solve the leaf's method upstream or forward the plan as authority. For ui audit pass the current screen/flow, primary user job, audit question/boundary and current-state evidence; do not preselect the redesign. For ui planning pass the established outcome/problem, current-state evidence, material constraints and unresolved design/layout/theme decision; parent options are non-exhaustive hypotheses. For ui implementation pass the established user-visible outcome, actually adopted plan propositions/constraints, target/mutation baseline and preserved behavior; omit non-required mechanism recommendations. For accessibility state advisory versus stable-result verification, exact stable target, changed interaction boundary, preserved behavior/constraints and available evidence; the verdict is stale after a later affecting edit.'''
good_audit='''Every specialist gets the audit question, exact target/state, bounded subsystem/behavior surface, allowed action level, expected evidence and stop/coverage boundary. Do not forward a suspected root cause or preferred fix as acceptance. Independent reviewer/a11y work preserves fresh judgment-context isolation. @devops has action ceiling read-only. @librarian receives the exact external technical proposition, named external target, material version/range/environment, allowed source/evidence scope and applicability/coverage boundary; its external evidence is not itself an audit finding, project requirement or local root cause. @general receives one bounded research question and does not replace a protected specialist stage.'''
ck(not findings(good_code,good_audit,good_ui),'good synthetic edge set rejected')

# Bad DevOps handoff: patch recipe instead of symptom/evidence/action boundary.
bad=good_code.replace('For devops pass the operational symptom and target environment, current evidence, action ceiling and authorized scope; do not assign a suspected config change as diagnosis, it remains a hypothesis.','For devops change nginx.conf to fix the issue.')
ck(any('code-orchestrator -> devops' in f for f in findings(bad,good_audit,good_ui)),'recipe-shaped devops handoff not rejected')
# Bad a11y handoff: no mode/state/interaction boundary.
badui=good_ui.replace('For accessibility state advisory versus stable-result verification, exact stable target, changed interaction boundary, preserved behavior/constraints and available evidence; the verdict is stale after a later affecting edit.','Ask accessibility reviewer if it looks okay.')
ck(any('ui-orchestrator -> a11y-reviewer' in f for f in findings(good_code,good_audit,badui)),'unbound a11y handoff not rejected')
# Bad planner handoff: chosen design laundered as requirement.
badui=good_ui.replace('For ui planning pass the established outcome/problem, current-state evidence, material constraints and unresolved design/layout/theme decision; parent options are non-exhaustive hypotheses.','Tell ui planner to produce the already chosen card layout.')
ck(any('ui-orchestrator -> ui-planner' in f for f in findings(good_code,good_audit,badui)),'preselected UI planning handoff not rejected')
# Bad audit specialist edge: no target/coverage/action semantics.
bado='''Delegate to @devops, @general and independent reviewer/a11y as useful. Let them inspect whatever they need.'''
fs=findings(good_code,bado,good_ui)
ck(any('auditor -> specialists' in f for f in fs),'unbounded auditor specialist handoff not rejected')
ck(any('auditor -> devops' in f for f in fs),'auditor devops read-only ceiling omission not rejected')

# Bad Librarian handoff: no external target/version/applicability boundary.
badlib=good_code.replace('For librarian pass the bounded external research proposition, named external target, material version/range/environment or permission to establish it from direct metadata, allowed source/evidence scope and stop/applicability boundary; do not ask it to trace local usage or turn an upstream suspicion into the local diagnosis.','For librarian research the docs and tell us what to use.')
ck(any('code-orchestrator -> librarian' in f for f in findings(badlib,good_audit,good_ui)),'unbound librarian handoff not rejected')
badauditlib=good_audit.replace('@librarian receives the exact external technical proposition, named external target, material version/range/environment, allowed source/evidence scope and applicability/coverage boundary; its external evidence is not itself an audit finding, project requirement or local root cause.','@librarian can research anything relevant and decide whether the finding is valid.')
ck(any('auditor -> librarian' in f for f in findings(good_code,badauditlib,good_ui)),'auditor librarian authority/applicability omission not rejected')

# Bad UI routing: the orchestrator knows the current treatment was rejected and a
# material UX/layout choice remains, but invents the replacement and sends it as
# settled direct implementation instead of delegating the bounded UI decision.
bad_ui_route=good_code.replace('For UI routing distinguish a settled user-visible outcome from unresolved presentation/interaction direction. If materially different layout, information-hierarchy, disclosure, interaction, or error-state treatments remain, or user feedback rejects the current treatment without adopting its replacement, delegate the bounded UI domain to @ui-orchestrator; do not invent the missing UI direction and pass it downstream as an established outcome. Direct @ui-implementer work is appropriate only when the material UI choice is established and focused mechanics remain.','When UI feedback says the current treatment is bad, choose a cleaner layout yourself and send the exact copy and placement directly to @ui-implementer.')
ck(any('code-orchestrator -> ui-orchestrator' in f for f in findings(bad_ui_route,good_audit,good_ui)),'unresolved UI direction was allowed to collapse into a direct implementation recipe')

# Bad trajectory handoff: the parent skips its own reassessment and asks the controller
# to decide what the workflow means merely because several corrections occurred.
bad_trajectory=good_code.replace('When repeated corrections or same-policy counterexamples materially challenge the model, perform bounded owner trajectory reassessment first; if it yields one evidence-backed model, continue without a trajectory audit. Invoke a fresh @trajectory-auditor only when an exact longitudinal question remains unresolved after that owner reassessment or the user explicitly requests independent trajectory review. Pass owner reassessment performed, current owner model, exact unresolved trajectory question, why available primary evidence could not safely resolve it, current parent session ID, task anchor, material transitions and proposed next transition; the packet is a workflow-owner report, not proof. Consume exactly continue, reanchor, reassess, checkpoint-required, or unverified.','If several corrections occurred, prefer asking @trajectory-auditor what the workflow means and follow its answer.')
ck(any('code-orchestrator -> trajectory-auditor' in f for f in findings(bad_trajectory,good_audit,good_ui)),'trajectory controller could replace first-line owner reassessment')

# Bad semantic-checkpoint handoff: ordinary technical ownership/fix-level decision is
# outsourced without a residual authority proposition or owner reconciliation.
bad_checkpoint=good_code.replace('For semantic checkpointing, first perform owner reconciliation and invoke fresh @semantic-checkpoint only for an exact semantic proposition whose authority remains unresolved or an explicit policy gate; pass owner reconciliation performed, strongest known authority/evidence, mutation boundary and why the owner cannot safely settle it. Do not invoke semantic checkpoint merely because technical owner, fix level, abstraction, invariant representation or necessary implementation scope changed under settled behavior.','Whenever technical ownership, fix level, abstraction or scope changes, ask @semantic-checkpoint whether to proceed.')
ck(any('code-orchestrator -> semantic-checkpoint' in f for f in findings(bad_checkpoint,good_audit,good_ui)),'semantic checkpoint could replace ordinary technical owner judgment')

# Bad fresh reviewer handoff: recent-fix history becomes the review plan.
bad_review=good_code.replace('Do not add a parent-authored Focus/Risks/Recent-fixes checklist from prior review/fix history and do not seed prior reviewer/OCR verdicts or findings; let the reviewer derive its risk model from the Candidate/effective diff. If user or project policy explicitly requests a review emphasis, pass it as additive and non-exhaustive.','Add a Focus section listing the last reviewer finding, the exact fix delta and the stress checks that should confirm it, then ask the whole-PR reviewer to confirm those areas.')
ck(any('code-orchestrator -> reviewer' in f for f in findings(bad_review,good_audit,good_ui)),'fresh whole-review recent-fix focus anchoring not rejected')

# Bad owner pass-through: a child recommendation may directly become the next workflow stage.
bad_owner=good_code.replace("A specialist's recommended next role, stage, mechanism or remediation is input, not a workflow transition, and an independent controller is not a substitute for an ordinary owner decision.","A specialist's recommended next role or mechanism may be accepted as the next workflow transition without separate parent synthesis when the specialist is credible.")
ck(not findings(bad_owner,good_audit,good_ui),'pass-through owner mutation unexpectedly caught by edge-only audit')

# Closed-world inventory: a newly discovered relation must fail until explicitly classified.
agent_names={'alpha','beta','gamma'}
discovered=m.discover_edges_from_texts({'alpha':'handoff to @beta then maybe @gamma','beta':'','gamma':''},agent_names)
inv=m.inventory_findings(discovered,{('alpha','beta'):'delegation'})
ck(any('UNCLASSIFIED EDGE alpha -> gamma' in f for f in inv),'new unclassified handoff edge did not block release')
# Stale classifications must also fail; otherwise inventory can drift away from runtime topology.
inv=m.inventory_findings({('alpha','beta')},{('alpha','beta'):'delegation',('beta','gamma'):'reroute'})
ck(any('STALE EDGE beta -> gamma' in f for f in inv),'stale handoff classification did not block release')
# Classification labels themselves are closed to known semantics.
inv=m.inventory_findings({('alpha','beta')},{('alpha','beta'):'magic'})
ck(any('INVALID EDGE CLASS alpha -> beta' in f for f in inv),'unknown edge classification kind did not block release')

if fail:
    print('ROLE HANDOFF SELFTEST v2: FAIL')
    for x in fail: print(' -',x)
    raise SystemExit(1)
print('ROLE HANDOFF SELFTEST v2: PASS')
