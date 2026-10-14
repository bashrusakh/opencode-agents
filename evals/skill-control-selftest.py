#!/usr/bin/env python3
"""Synthetic anti-gaming fixtures for skill-control-audit.py."""
from __future__ import annotations
import hashlib, importlib.util, json, tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('skill_control_audit', HERE/'skill-control-audit.py')
mod=importlib.util.module_from_spec(sp); assert sp and sp.loader; sp.loader.exec_module(mod)

def dh(path:Path)->str:
    h=hashlib.sha256()
    for f in sorted(x for x in path.rglob('*') if x.is_file()):
        h.update(str(f.relative_to(path)).encode()+b'\0'+f.read_bytes()+b'\0')
    return h.hexdigest()

def fixture(root:Path):
    (root/'skills/owned').mkdir(parents=True); (root/'skills/vendor').mkdir(parents=True); (root/'evals').mkdir()
    (root/'skills/owned/SKILL.md').write_text('# Owned\n\n## Mechanics\n\nOwned mechanism.\n')
    (root/'skills/vendor/SKILL.md').write_text('# Vendor\n\nUpstream bytes.\n')
    owner={"schema_version":1,"capabilities":[{"id":"owned_mechanics","owner":"skills/owned/SKILL.md","owner_signature":[["Owned mechanism"]],"consumers":[{"path":"ROOT.md","mode":"reference","activation_signature":[["owned skill"]],"forbidden_redefinition":{"groups":[["never-match-a"],["never-match-b"]],"window_lines":4}}]}]}
    (root/'ROOT.md').write_text('Use owned skill.\n')
    (root/'evals/semantic-ownership-spec.json').write_text(json.dumps(owner))
    (root/'evals/semantic-domain-spec.json').write_text(json.dumps({"schema_version":1,"domains":[]}))
    spec={"schema_version":1,"skills":[
        {"path":"skills/owned/SKILL.md","class":"pack-workflow","entry_sections":["Mechanics"],"owned_capabilities":["owned_mechanics"],"consumed_capabilities":[],"typed_domains":[],"side_effect_class":"test"},
        {"path":"skills/vendor/SKILL.md","class":"vendor-advisory","directory_sha256":dh(root/'skills/vendor'),"owned_capabilities":[],"consumed_capabilities":[],"typed_domains":[],"side_effect_class":"vendor"}
    ]}
    p=root/'evals/skill-control-spec.json'; p.write_text(json.dumps(spec)); return p

with tempfile.TemporaryDirectory(prefix='skill-control-selftest-') as td:
    b=Path(td)
    clean=b/'clean'; clean.mkdir(); spec=fixture(clean); assert not mod.audit(clean,spec), mod.audit(clean,spec)

    unclassified=b/'unclassified'; unclassified.mkdir(); spec=fixture(unclassified)
    (unclassified/'skills/new').mkdir(); (unclassified/'skills/new/SKILL.md').write_text('# New\n')
    f=mod.audit(unclassified,spec); assert any('unclassified skill entrypoints' in x for x in f), f

    heading=b/'heading'; heading.mkdir(); spec=fixture(heading)
    with (heading/'skills/owned/SKILL.md').open('a') as out: out.write('\n## New shared policy\n')
    f=mod.audit(heading,spec); assert any('entry section inventory drift' in x for x in f), f

    vendor=b/'vendor'; vendor.mkdir(); spec=fixture(vendor)
    with (vendor/'skills/vendor/SKILL.md').open('a') as out: out.write('\nchanged upstream bytes\n')
    f=mod.audit(vendor,spec); assert any('vendor skill bytes changed' in x for x in f), f

print('SKILL CONTROL SELFTEST: PASS')
