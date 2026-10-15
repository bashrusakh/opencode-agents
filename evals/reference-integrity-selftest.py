#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,tempfile,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('refaudit',HERE/'reference-integrity-audit.py')
m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)

def run_fixture(agent_line:str, pack_skill_line:str='')->list[str]:
    with tempfile.TemporaryDirectory(prefix='refint-') as td:
        r=Path(td); (r/'agents').mkdir(); (r/'skills/pack').mkdir(parents=True); (r/'skills/vendor').mkdir(parents=True); (r/'evals').mkdir()
        (r/'AGENTS.md').write_text('# x\n## 0. Universal\n## 2. Core\n### 2.2 Evidence\n## 5. Final\n')
        (r/'agents/a.md').write_text(agent_line+'\n')
        (r/'skills/pack/SKILL.md').write_text(pack_skill_line+'\n')
        (r/'skills/vendor/SKILL.md').write_text('Installing is a root section 99 gate.\n')
        (r/'evals/skill-control-spec.json').write_text(json.dumps({'skills':[
            {'path':'skills/pack/SKILL.md','class':'pack-workflow'},
            {'path':'skills/vendor/SKILL.md','class':'vendor-advisory'},
        ]}))
        old=m.ROOT; m.ROOT=r
        try: return m.audit()
        finally: m.ROOT=old

assert not run_fixture('Apply root section 2.2.'), 'valid current root reference failed'
assert run_fixture('Apply Root sections 2.2 and 7.'), 'dangling root section passed'
assert run_fixture('Use the root `### Update` form.'), 'stale Update owner passed'
assert run_fixture('Use the root review cadence.'), 'stale review cadence passed'
assert run_fixture('Use root section 2.2.','Stop at another root gate.'), 'stale pack-skill root gate passed'
print('REFERENCE INTEGRITY SELFTEST: PASS')
