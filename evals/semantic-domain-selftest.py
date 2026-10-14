#!/usr/bin/env python3
"""Synthetic tests for semantic-domain-audit.py."""
from __future__ import annotations
import importlib.util
import json
import tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('domain_audit', HERE/'semantic-domain-audit.py')
mod=importlib.util.module_from_spec(spec); assert spec and spec.loader; spec.loader.exec_module(mod)


def make(root: Path, trajectory_token: str) -> Path:
    (root/'agents').mkdir(parents=True, exist_ok=True)
    (root/'AGENTS.md').write_text(
        'Preserve the evidence state. use `unverified` only for evidence/verification state, not as a relation or workflow verdict. '\
        'classify the candidate relation as `preserved` or `indeterminate`.\n', encoding='utf-8')
    (root/'agents/semantic-checkpoint.md').write_text(
        '## Verdict\n\nReturn exactly one:\n\n- `proceed` — go\n- `hold` — block\n- `insufficient-context` — context missing\n', encoding='utf-8')
    (root/'agents/trajectory-auditor.md').write_text(
        f'## Verdict semantics\n\nReturn exactly one workflow verdict:\n\n- `continue` — go\n- `reanchor` — anchor\n- `reassess` — reassess\n- `checkpoint-required` — checkpoint\n- `{trajectory_token}` — evidence missing\n', encoding='utf-8')
    data={"schema_version":1,"domains":[
        {"id":"evidence_status","domain_class":"evidence_status","owner":"AGENTS.md","owner_signature":[["use `unverified` only for evidence/verification state"],["Preserve the evidence state"]],"tokens":["established","unverified","contradicted"]},
        {"id":"proposition_relation","domain_class":"proposition_relation","owner":"AGENTS.md","owner_signature":[["classify the candidate relation"],["`preserved`"],["`indeterminate`"]],"tokens":["preserved","refined","indeterminate"]},
        {"id":"semantic_checkpoint_verdict","domain_class":"workflow_verdict","owner":"agents/semantic-checkpoint.md","owner_heading":"## Verdict","tokens":["proceed","hold","insufficient-context"]},
        {"id":"trajectory_verdict","domain_class":"workflow_verdict","owner":"agents/trajectory-auditor.md","owner_heading":"## Verdict semantics","tokens":["continue","reanchor","reassess","checkpoint-required",trajectory_token]}
    ]}
    p=root/'spec.json'; p.write_text(json.dumps(data), encoding='utf-8'); return p

with tempfile.TemporaryDirectory(prefix='semantic-domain-selftest-') as td:
    base=Path(td)
    good=base/'good'; good.mkdir(); sp=make(good,'insufficient-evidence')
    assert not mod.audit(good,sp), mod.audit(good,sp)
    bad=base/'bad'; bad.mkdir(); sp=make(bad,'unverified')
    findings=mod.audit(bad,sp)
    assert any('belongs to multiple semantic domains' in f for f in findings), findings

    skillbad=base/'skillbad'; skillbad.mkdir(); sp=make(skillbad,'insufficient-evidence')
    (skillbad/'skills/helper').mkdir(parents=True); (skillbad/'evals').mkdir(exist_ok=True)
    (skillbad/'skills/helper/SKILL.md').write_text('## Verdict semantics\n\n- `unverified` — workflow verdict\n- `continue` — continue\n', encoding='utf-8')
    (skillbad/'evals/skill-control-spec.json').write_text(json.dumps({'schema_version':1,'skills':[{'path':'skills/helper/SKILL.md','class':'pack-workflow'}]}), encoding='utf-8')
    findings=mod.audit(skillbad,sp)
    assert any('undeclared workflow-verdict domain' in f or 'reused as workflow-verdict semantics' in f for f in findings), findings

print('SEMANTIC DOMAIN SELFTEST: PASS')
