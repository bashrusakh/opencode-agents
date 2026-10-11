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
good_code='''For every delegation pass objective and behavioral/target scope, allowed action level, expected deliverable/evidence, and stop or escalation conditions; omit upstream non-required mechanism proposals or label them explicitly non-binding. For devops pass the operational symptom and target environment, current evidence, action ceiling and authorized scope; do not assign a suspected config change as diagnosis, it remains a hypothesis. For librarian pass the bounded external research proposition, named external target, material version/range/environment or permission to establish it from direct metadata, allowed source/evidence scope and stop/applicability boundary; do not ask it to trace local usage or turn an upstream suspicion into the local diagnosis. For general pass one bounded research question with allowed evidence/source scope and stop when another specialist owns it. For UI implementation pass the established user-visible outcome, target/mutation state, material constraints and preserved behavior; do not preselect files or layout mechanics.'''
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
