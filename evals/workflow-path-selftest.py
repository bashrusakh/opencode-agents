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
  shutil.copytree(ROOT,td/'p',dirs_exist_ok=True,ignore=shutil.ignore_patterns('.git','.opencode','.graymatter','__pycache__','node_modules')); p=td/'p'/rel; t=p.read_text();
  if old not in t: return False,'fixture drift'
  p.write_text(t.replace(old,new,1)); return bool(m.audit(td/'p',td/'p/evals/workflow-path-spec.json')),None
 finally: shutil.rmtree(td,ignore_errors=True)
cases=[
 ('agents/code-orchestrator.md','When the active code workflow reaches a material UI-domain routing decision, load `ui-routing-control`','When the active code workflow reaches a material UI-domain routing decision, skip `ui-routing-control`','UI route activation omission not rejected'),
 ('skills/ui-routing-control/SKILL.md','inherited target/state identity','current context','UI target identity omission not rejected'),
 ('skills/code-host-workflow/SKILL.md','current review comments/checks','some PR metadata','PR preflight evidence omission not rejected'),
 ('agents/code-orchestrator.md','whole material task/acceptance surface','latest fix slice','whole-review acceptance model omission not rejected'),
 ('agents/code-orchestrator.md','complete affected boundary','some tests','tester boundary omission not rejected'),
 ('agents/code-orchestrator.md','For a debugger handoff, pass the exact symptom/reproduction or strongest current failure evidence, governing expected behavior/invariant, affected behavior boundary, and target/mutation identity','For a debugger handoff, pass only the current failure evidence and target identity','debugger governing-invariant handoff omission not rejected'),
 ('skills/ui-routing-control/SKILL.md','pass the leaf result plus exact updated target/state and material UI evidence back to `@ui-orchestrator`','let code-orchestrator choose the next UI stage','delegated UI reconciliation loop omission not rejected'),
 ('skills/terminal-semantic-eval/SKILL.md','does not gate final reporting','may gate final reporting','terminal non-gating drift not rejected')
]
for rel,old,new,msg in cases:
 ok,err=mutate(rel,old,new);ck(ok and not err,msg if not err else msg+': '+err)
if fail:
 print('WORKFLOW PATH SELFTEST: FAIL');[print('-',x) for x in fail];raise SystemExit(1)
print('WORKFLOW PATH SELFTEST: PASS')
