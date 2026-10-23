#!/usr/bin/env python3
"""Regression checks for baseline comparison and stale/unreviewed loss detection."""
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('preservation', HERE/'prior-release-preservation.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

with TemporaryDirectory(prefix='preservation-test-') as folder:
    root = Path(folder)
    before, after = root/'prev', root/'next'
    for base in (before, after):
        (base/'skills/change-contract').mkdir(parents=True)
        (base/'AGENTS.md').write_text('Shared evidence and user authority must remain in scope.\n')
    rule = 'For bounded semantic edits, prefer native patch or edit tools when they are available and safe.\n'
    (before/'skills/change-contract/SKILL.md').write_text(rule+'Do not bypass precision for convenience.\n')
    (after/'skills/change-contract/SKILL.md').write_text('Choose the narrowest reliable mutation mechanism.\n')
    prior, candidate = mod.load(before), mod.load(after)
    entry = mod.ledger(prior, candidate)
    assert entry['changes'] and any('native patch' in ' '.join(x['removed']) for x in entry['changes']), 'lost native edit rule not detected'
    assert mod.validate(entry, entry, candidate), 'unreviewed lost rule accepted'
    broken = json.loads(json.dumps(entry))
    for item in broken['changes']:
        item.update(assessment='preserved', reason='The exact earlier instruction remains in the new canonical skill owner.',
                    retained_location='skills/change-contract/SKILL.md', evidence_quote=rule.strip())
    assert mod.validate(entry, broken, candidate), 'fake retained quote accepted'
    reviewed = json.loads(json.dumps(entry))
    for item in reviewed['changes']:
        item.update(assessment='authorized_change', authority='explicit user instruction in task receipt',
                    reason='Intentional change of editing behavior: previous native editor preference replaced by broader choice.')
    assert not mod.validate(entry, reviewed, candidate), 'assessed, provenance-bound comparison should be accepted mechanically'
    (after/'AGENTS.md').write_text('Shared evidence only.\n')
    fresh = mod.ledger(prior, mod.load(after))
    assert mod.validate(fresh, reviewed, mod.load(after)), 'stale comparison accepted after additional edit'
    # Verify semantic-preservation proof remains a *reviewer* obligation: authorized-change
    # metadata is mechanically valid, not evidence that the claimed authority is genuine.
print('PRIOR-RELEASE PRESERVATION SELFTEST: PASS (loss, stale review and fake relocation rejected)')
