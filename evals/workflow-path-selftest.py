#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,sys,tempfile,shutil,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent
sp=importlib.util.spec_from_file_location('wpa',HERE/'workflow-path-audit.py');m=importlib.util.module_from_spec(sp);sys.modules[sp.name]=m;sp.loader.exec_module(m)
fail=[]
def ck(x,msg):
 if not x:fail.append(msg)
# baseline must pass
ck(not m.audit(ROOT,HERE/'workflow-path-spec.json'),'baseline workflow-path spec rejected')
# synthetic mutations against copied package
def mutate(rel,old,new):
 td=Path(tempfile.mkdtemp(prefix='wfpath-'))
 try:
  shutil.copytree(ROOT,td/'p',dirs_exist_ok=True); p=td/'p'/rel; t=p.read_text();
  if old not in t: return False,'fixture drift'
  p.write_text(t.replace(old,new,1)); return bool(m.audit(td/'p',td/'p/evals/workflow-path-spec.json')),None
 finally: shutil.rmtree(td,ignore_errors=True)
cases=[
 ('agents/code-orchestrator.md','When the active code workflow reaches a material UI-domain routing decision, load `ui-routing-control`','When the active code workflow reaches a material UI-domain routing decision, skip `ui-routing-control`','UI route activation omission not rejected'),
 ('skills/ui-routing-control/SKILL.md','inherited target/state identity','current context','UI target identity omission not rejected'),
 ('skills/repository-workflow/SKILL.md','current review comments/checks','some PR metadata','PR preflight evidence omission not rejected'),
 ('agents/code-orchestrator.md','whole material task/acceptance surface','latest fix slice','whole-review acceptance model omission not rejected'),
 ('agents/code-orchestrator.md','complete affected boundary','some tests','tester boundary omission not rejected'),
 ('agents/code-orchestrator.md','For a debugger handoff, pass the exact symptom/reproduction or strongest current failure evidence, governing expected behavior/invariant, affected behavior boundary, and target/mutation identity','For a debugger handoff, pass only the current failure evidence and target identity','debugger governing-invariant handoff omission not rejected'),
 ('skills/ui-routing-control/SKILL.md','pass the leaf result plus exact updated target/state and material UI evidence back to `@ui-orchestrator`','let code-orchestrator choose the next UI stage','delegated UI reconciliation loop omission not rejected'),
 ('skills/session-evaluation-control/SKILL.md','does not gate final reporting','may gate final reporting','terminal non-gating drift not rejected'),
 ('skills/pr-readiness/SKILL.md','Do not invoke final whole-PR review merely because an individual correction batch ended','Run final whole-PR review whenever any correction batch ends','correction batch -> whole review churn not rejected'),
 ('skills/pr-readiness/SKILL.md','Do not infer a prerequisite waiver from an action sequence','Infer prerequisite waiver from the requested action sequence','Ready-without-review sequencing shortcut not rejected'),
 ('skills/delegation-control/SKILL.md','A material state transition outside those bounds is a separate mutation, not an implementation convenience.','A child may freely change task-relevant state when that is convenient for execution.','delegated task-state drift not rejected'),
 ('agents/code-orchestrator.md','Treat a specialist\'s returned **closure/completeness conclusion as a proposition-scoped claim, not workflow state**.','Treat a specialist\'s returned closure/completeness conclusion as workflow state once the specialist reports success.','producer completion -> parent closure laundering not rejected'),
 ('agents/code-orchestrator.md','Representative examples, local green checks, or evidence that shares one implementation assumption cannot establish broader domain/owner/invariant closure unless that evidence discriminates the broader proposition.','Representative examples or local green checks may establish broader domain/owner/invariant closure whenever the specialist reports complete.','representative evidence -> broad closure laundering not rejected'),
 ('skills/repository-workflow/SKILL.md','a stale local checkout cannot substitute merely because it offers a plausible explanation','a stale local checkout may substitute when refreshing the target state is unavailable','stale report diagnosis -> current-state claim laundering not rejected'),
 ('agents/session-evaluator.md','Do not reconstruct a missing governing contract from another rule, apparently equivalent workflow evidence, or a reasonable substitute.','A missing governing contract may be reconstructed from equivalent workflow evidence when the outcome appears safe.','missing governing contract -> compliant substitution not rejected'),
 ('agents/code-orchestrator.md','the workflow owner must not substitute a direct OCR call for the reviewer stage','the workflow owner may substitute a direct OCR call for the reviewer stage when OCR was explicitly requested','explicit OCR method -> reviewer ownership transfer not rejected'),
 ('agents/code-orchestrator.md','test whether the causal repair already removes its premise','accept every user-specified restriction as justified without checking any surrounding change','protective premise -> owner reconciliation bypass not rejected'),
 ('agents/reviewer.md','verify the **protection premise against the combined candidate**','assume the guard is justified whenever the tests pass','protective premise -> reviewer normal-path audit bypass not rejected'),
 ('agents/reviewer.md','not as permission to rewrite the specification or treat an expressly accepted tradeoff as a code defect','and unconditionally reject any restriction that inconveniences users, even if the exact cost is accepted','accepted protective tradeoff -> ritual reviewer veto not rejected'),
 ('agents/code-orchestrator.md','or create a planning/gate stage for ordinary adequately scoped fixes.','and force an extra product-impact review stage for every unrelated change.','unrelated PR -> ritual review stage not rejected')
]
for rel,old,new,msg in cases:
 ok,err=mutate(rel,old,new);ck(ok and not err,msg if not err else msg+': '+err)
if fail:
 print('WORKFLOW PATH SELFTEST: FAIL');[print('-',x) for x in fail];raise SystemExit(1)
print('WORKFLOW PATH SELFTEST: PASS')
