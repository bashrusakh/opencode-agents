#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('res',HERE/'runtime-residency-audit.py')
m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)

with tempfile.TemporaryDirectory(prefix='residency-') as td:
    r=Path(td); (r/'agents').mkdir(); (r/'skills/workflow-entry').mkdir(parents=True); (r/'skills/code-host-workflow').mkdir(parents=True); (r/'skills/terminal-semantic-eval').mkdir(parents=True); (r/'skills/ui-routing-control').mkdir(parents=True)
    root_ok='# root\n## Universal\nUniversal invariant: authority evidence.\n'
    owner_ok='---\nmode: all\n---\nWhen this role is primary, load `workflow-entry`.\n'
    leaf_ok='---\nmode: subagent\n---\nleaf\n'
    skill_ok='---\nname: workflow-entry\ndescription: x\nmetadata:\n  opencode/autoinvoke: "false"\n---\n# x\nConditional procedure: bounded owner contract.\n'
    host_ok='---\nname: code-host-workflow\ndescription: x\nmetadata:\n  opencode/autoinvoke: "false"\n---\n# x\nHost resource procedure: canonical resource identity and state.\n'
    ui_ok='---\nname: ui-routing-control\ndescription: x\nmetadata:\n  opencode/autoinvoke: "false"\n---\n# x\nMaterial UI-domain routing decision. Settled user-visible outcome versus unresolved presentation/interaction direction. Delegate the bounded UI domain to `@ui-orchestrator` or route directly to `@ui-implementer`; pass inherited target/state identity and stage selection boundary.\n'
    term_ok='---\nname: terminal-semantic-eval\ndescription: x\nmetadata:\n  opencode/autoinvoke: "false"\n---\n# x\nTerminal successful outcome. Invoke `@session-evaluator` once with material participating child-session IDs; do not perform new session-history discovery. Treat result as diagnostic evidence only; it does not change an already-established terminal state and does not gate final reporting.\n'
    spec={
      'schema_version':1,
      'root':{'path':'AGENTS.md','audience':'universal','required_families':[{'id':'universal','window_lines':4,'groups':[['Universal invariant'],['authority'],['evidence']]}],'forbidden_families':[
        {'id':'startup','window_lines':8,'groups':[['Startup protocol'],['selected route'],['action ceiling'],['gate status'],['next action']]},
        {'id':'handoff','window_lines':8,'groups':[['bounded.*reconstructable'],['evidence expected'],['stop conditions'],['fresh child']]},
        {'id':'implementation','window_lines':8,'groups':[['pre[- ]mutation'],['fix boundary'],['preserved invariant'],['stale evidence']]},
        {'id':'codehost','window_lines':8,'groups':[['PR workflow'],['issue workflow'],['review comments'],['PR readiness']]},
      ]},
      'contracts':[{
        'id':'workflow-entry','path':'skills/workflow-entry/SKILL.md','audience':'primary-entry','autoinvoke_false':True,'required_families':[{'id':'conditional','window_lines':4,'groups':[['Conditional procedure'],['bounded owner contract']]}],
        'activators':[{'path':'agents/owner.md','mode':'primary-only','signature':['When this role is primary, load `workflow-entry`']}],
        'forbidden_role_paths':['agents/leaf.md'],
      },{
        'id':'code-host-workflow','path':'skills/code-host-workflow/SKILL.md','audience':'code-host-resource','autoinvoke_false':True,'required_families':[{'id':'host','window_lines':4,'groups':[['Host resource procedure'],['canonical resource identity']]}],
        'activators':[{'path':'agents/host-owner.md','mode':'always-primary','signature':['When code-host resource is selected, load `code-host-workflow`']}],
        'forbidden_role_paths':['agents/leaf.md'],
        'forbidden_activator_families':[{'id':'host-pipeline','window_lines':6,'groups':[['resolve PR state'],['search existing issues'],['release metadata']]}],
      },{
        'id':'ui-routing-control','path':'skills/ui-routing-control/SKILL.md','audience':'code-to-ui-routing','autoinvoke_false':True,'required_families':[{'id':'ui','window_lines':8,'groups':[['Material UI-domain routing decision'],['unresolved presentation/interaction direction'],['@ui-orchestrator'],['@ui-implementer']]}],
        'activators':[{'path':'agents/ui-owner.md','mode':'always-primary','signature':['When UI routing is material, load `ui-routing-control`']}],
        'forbidden_role_paths':['agents/leaf.md'],
        'forbidden_activator_families':[{'id':'ui-route','window_lines':8,'groups':[['settled user-visible outcome'],['unresolved presentation/interaction direction'],['@ui-orchestrator'],['@ui-implementer']]}],
      },{
        'id':'terminal-semantic-eval','path':'skills/terminal-semantic-eval/SKILL.md','audience':'terminal-diagnostic','autoinvoke_false':True,'required_families':[{'id':'terminal','window_lines':6,'groups':[['Terminal successful outcome'],['Invoke `@session-evaluator` once'],['diagnostic evidence only']]}],
        'activators':[{'path':'agents/terminal-owner.md','mode':'always-primary','signature':['At terminal success load `terminal-semantic-eval`']}],
        'forbidden_role_paths':['agents/leaf.md'],
        'forbidden_activator_families':[{'id':'terminal-procedure','window_lines':6,'groups':[['child-session IDs'],['session-history discovery'],['does not change an already-established terminal state']]}],
      }],
    }
    p=r/'spec.json'; p.write_text(json.dumps(spec))
    def reset():
        (r/'AGENTS.md').write_text(root_ok,encoding='utf-8')
        (r/'agents/owner.md').write_text(owner_ok,encoding='utf-8')
        (r/'agents/leaf.md').write_text(leaf_ok,encoding='utf-8')
        (r/'agents/host-owner.md').write_text('---\nmode: primary\n---\nWhen code-host resource is selected, load `code-host-workflow`.\n',encoding='utf-8')
        (r/'agents/terminal-owner.md').write_text('---\nmode: primary\n---\nAt terminal success load `terminal-semantic-eval`.\n',encoding='utf-8')
        (r/'agents/ui-owner.md').write_text('---\nmode: primary\n---\nWhen UI routing is material, load `ui-routing-control`.\n',encoding='utf-8')
        (r/'skills/workflow-entry/SKILL.md').write_text(skill_ok,encoding='utf-8')
        (r/'skills/code-host-workflow/SKILL.md').write_text(host_ok,encoding='utf-8')
        (r/'skills/ui-routing-control/SKILL.md').write_text(ui_ok,encoding='utf-8')
        (r/'skills/terminal-semantic-eval/SKILL.md').write_text(term_ok,encoding='utf-8')
    def must_fail(label:str):
        f=m.audit(r,p)
        assert f, f'{label}: mutation unexpectedly passed'
    reset(); assert not m.audit(r,p),m.audit(r,p)
    reset(); (r/'AGENTS.md').write_text('# root\n## Universal\n',encoding='utf-8'); must_fail('required universal semantic lost')
    reset(); (r/'skills/workflow-entry/SKILL.md').write_text(skill_ok.replace('Conditional procedure: bounded owner contract.\n',''),encoding='utf-8'); must_fail('required conditional semantic lost')
    reset(); (r/'AGENTS.md').write_text(root_ok+'Startup protocol: selected route, action ceiling, gate status, next action.\n'); must_fail('startup in root')
    reset(); (r/'AGENTS.md').write_text(root_ok+'Caller sends a bounded reconstructable packet with evidence expected, stop conditions, and a fresh child.\n'); must_fail('handoff in root')
    reset(); (r/'AGENTS.md').write_text(root_ok+'Implementation does pre-mutation inspection, selects the fix boundary and preserved invariant, then invalidates stale evidence.\n'); must_fail('implementation in root')
    reset(); (r/'AGENTS.md').write_text(root_ok+'PR workflow and issue workflow consume review comments before PR readiness.\n'); must_fail('resource pipeline in root')
    reset(); (r/'agents/leaf.md').write_text('---\nmode: subagent\n---\nload `workflow-entry`\n'); must_fail('leaf owner activation')
    reset(); (r/'skills/workflow-entry/SKILL.md').write_text(skill_ok.replace('"false"','"true"'),encoding='utf-8'); must_fail('autoinvoke enabled')
    reset(); (r/'agents/owner.md').write_text(owner_ok.replace('mode: all','mode: subagent'),encoding='utf-8'); must_fail('primary-only contract on subagent role')
    reset(); (r/'agents/owner.md').write_text('---\nmode: all\n---\nowner\n',encoding='utf-8'); must_fail('activation signature removed')
    reset(); (r/'agents/host-owner.md').write_text('---\nmode: primary\n---\nWhen code-host resource is selected, load `code-host-workflow`.\nresolve PR state; search existing issues; verify release metadata.\n',encoding='utf-8'); must_fail('conditional code-host pipeline remains in activator')
    reset(); (r/'agents/ui-owner.md').write_text('---\nmode: primary\n---\nWhen UI routing is material, load `ui-routing-control`.\nSettled user-visible outcome, unresolved presentation/interaction direction, @ui-orchestrator and @ui-implementer.\n',encoding='utf-8'); must_fail('conditional UI routing procedure remains in activator')
    reset(); (r/'skills/ui-routing-control/SKILL.md').write_text(ui_ok.replace('"false"','"true"'),encoding='utf-8'); must_fail('UI routing autoinvoke enabled')
    reset(); (r/'agents/terminal-owner.md').write_text('---\nmode: primary\n---\nAt terminal success load `terminal-semantic-eval`.\nPass child-session IDs, perform no session-history discovery, and diagnostic failure does not change an already-established terminal state.\n',encoding='utf-8'); must_fail('terminal evaluator handoff remains resident in activator')
    reset(); (r/'skills/terminal-semantic-eval/SKILL.md').write_text(term_ok.replace('"false"','"true"'),encoding='utf-8'); must_fail('terminal diagnostic autoinvoke enabled')
print('RUNTIME RESIDENCY SELFTEST: PASS')
