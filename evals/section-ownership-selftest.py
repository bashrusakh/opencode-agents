#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('sec',HERE/'section-ownership-audit.py')
m=importlib.util.module_from_spec(sp); assert sp and sp.loader; sp.loader.exec_module(m)
with tempfile.TemporaryDirectory(prefix='section-owner-selftest-') as td:
    r=Path(td); (r/'agents').mkdir()
    (r/'AGENTS.md').write_text('## Root\n\n### Routing\n',encoding='utf-8')
    (r/'agents/code-orchestrator.md').write_text('## Role\n\n### Flow\n',encoding='utf-8')
    spec={"schema_version":1,"surfaces":{
      "AGENTS.md":[{"heading":"## Root","placement":"shared_owner","purpose":"shared root policy owner"},{"heading":"### Routing","placement":"shared_owner","purpose":"shared routing owner"}],
      "agents/code-orchestrator.md":[{"heading":"## Role","placement":"role_owner","purpose":"role-owned workflow purpose"},{"heading":"### Flow","placement":"role_owner","purpose":"role-owned workflow mechanics"}]}}
    p=r/'map.json'; p.write_text(json.dumps(spec),encoding='utf-8')
    assert not m.audit(r,p), m.audit(r,p)
    (r/'agents/code-orchestrator.md').write_text('## Role\n\n### New hidden pipeline\n\n### Flow\n',encoding='utf-8')
    findings=m.audit(r,p)
    assert any('unmapped runtime sections' in x for x in findings), findings
print('SECTION OWNERSHIP SELFTEST: PASS')
