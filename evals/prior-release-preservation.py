#!/usr/bin/env python3
"""Cross-version preservation ledger, separate from candidate-only gates.

This tool locates material changed hunks across the prior released pack and a
candidate and requires an evidence-bearing disposition for each before promotion.
It does *not* claim to automate semantic equivalence. Records live outside the
release distribution and bind to exact input file bytes/hunks.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
import stat
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> dict[str, bytes]:
    if path.is_dir():
        return {p.relative_to(path).as_posix(): p.read_bytes()
                for p in path.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    if path.suffix.lower() == '.zip' and path.is_file():
        with ZipFile(path) as z:
            files = {x.filename: z.read(x) for x in z.infolist() if not x.is_dir()}
        roots = {k.split('/')[0] for k in files}
        if len(roots) == 1 and all('/' in k for k in files):
            return {k.split('/', 1)[1]: v for k, v in files.items()}
        return files
    raise ValueError(f'expected directory or ZIP, got {path}')


def modes(path: Path) -> dict[str, str]:
    if path.is_dir():
        return {p.relative_to(path).as_posix(): oct(stat.S_IMODE(p.stat().st_mode))
                for p in path.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    with ZipFile(path) as z:
        entries = [x for x in z.infolist() if not x.is_dir()]
        root = len({x.filename.split('/')[0] for x in entries}) == 1
        return {x.filename.split('/', 1)[1] if root else x.filename:
                oct((x.external_attr >> 16) & 0o777) for x in entries}


def controlled(path: str) -> bool:
    return (path == 'AGENTS.md' or path.startswith(('agents/', 'skills/', 'evals/', 'install/'))
            or path in {'docs/semantic-design-manual.md', 'docs/semantic-design-source-audit.md'})


def hunk_changes(old: bytes | None, new: bytes | None) -> list[dict]:
    if old is None or new is None:
        return [{'old_range': '-' if old is None else 'entire file',
                 'new_range': '-' if new is None else 'entire file',
                 'removed': [] if old is None else old.decode('utf-8', 'replace').splitlines(),
                 'added': [] if new is None else new.decode('utf-8', 'replace').splitlines()}]
    a = old.decode('utf-8', 'replace').splitlines()
    b = new.decode('utf-8', 'replace').splitlines()
    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    result = []
    for group in matcher.get_grouped_opcodes(n=2):
        removed, added = [], []
        old_begin, new_begin = group[0][1], group[0][3]
        old_end, new_end = group[-1][2], group[-1][4]
        for tag, i1, i2, j1, j2 in group:
            if tag in ('delete', 'replace'):
                removed.extend(a[i1:i2])
            if tag in ('insert', 'replace'):
                added.extend(b[j1:j2])
        result.append({'old_range': f'{old_begin + 1}-{old_end}',
                       'new_range': f'{new_begin + 1}-{new_end}',
                       'removed': removed, 'added': added})
    return result


def ledger(prior: dict[str, bytes], candidate: dict[str, bytes],
           prior_modes: dict[str, str] | None = None, candidate_modes: dict[str, str] | None = None) -> dict:
    changed = []
    for path in sorted(set(prior) | set(candidate)):
        if not controlled(path) or prior.get(path) == candidate.get(path):
            continue
        old, new = prior.get(path), candidate.get(path)
        for i, hunk in enumerate(hunk_changes(old, new), 1):
            hunk_sig = sha(json.dumps([path, hunk], ensure_ascii=False, sort_keys=True).encode())[:16]
            changed.append({'id': f'{path}#{i}:{hunk_sig}', 'path': path,
                            'change': ('added' if old is None else 'removed' if new is None else 'modified'),
                            **hunk, 'assessment': 'PENDING', 'reason': '',
                            'retained_location': '', 'evidence_quote': '', 'authority': ''})
    prior_modes, candidate_modes = prior_modes or {}, candidate_modes or {}
    for path in sorted(set(prior_modes) & set(candidate_modes)):
        if controlled(path) and prior_modes[path] != candidate_modes[path]:
            hunk = {'old_range': 'file mode', 'new_range': 'file mode',
                    'removed': ['file mode: ' + prior_modes[path]],
                    'added': ['file mode: ' + candidate_modes[path]]}
            hunk_sig = sha(json.dumps([path, hunk], sort_keys=True).encode())[:16]
            changed.append({'id': f'{path}#mode:{hunk_sig}', 'path': path, 'change': 'mode_modified',
                            **hunk, 'assessment': 'PENDING', 'reason': '',
                            'retained_location': '', 'evidence_quote': '', 'authority': ''})
    prior_fingerprint = sha(json.dumps({p: [sha(v), prior_modes.get(p)] for p, v in sorted(prior.items()) if controlled(p)}, sort_keys=True).encode())
    candidate_fingerprint = sha(json.dumps({p: [sha(v), candidate_modes.get(p)] for p, v in sorted(candidate.items()) if controlled(p)}, sort_keys=True).encode())
    return {'schema': 1, 'previous_controlled_sha256': prior_fingerprint,
            'candidate_controlled_sha256': candidate_fingerprint,
            'changes': changed}


def report(info: dict, validation: list[str] | None = None) -> str:
    lines = ['# Previous-release preservation review', '',
             f'- Previous controlled-files fingerprint: `{info["previous_controlled_sha256"]}`',
             f'- Candidate controlled-files fingerprint: `{info["candidate_controlled_sha256"]}`',
             f'- Changed material hunks: **{len(info["changes"])}**',
             '- A changed hunk is not automatically a regression; an unchanged hunk is not independently proven correct.',
             '- This ledger verifies coverage/provenance of a source-aware semantic comparison, **not** automated semantic equivalence.', '']
    for change in info['changes']:
        lines += [f'## `{change["id"]}`', '',
                  f'- Type: {change["change"]}; old {change["old_range"]}, candidate {change["new_range"]}',
                  f'- Assessment: **{change["assessment"]}**',
                  f'- Reason: {change.get("reason") or "NOT REVIEWED"}', '']
        for title, text_lines in [('Prior lines removed or rewritten', change['removed']),
                                  ('Candidate lines added or rewritten', change['added'])]:
            lines += [f'**{title}** ({len(text_lines)} lines):', '```text']
            lines.extend((s[:300] for s in text_lines[:24]))
            if len(text_lines) > 24:
                lines.append(f'... {len(text_lines)-24} further lines; inspect full source diff')
            lines += ['```', '']
    if validation is not None:
        lines += ['## Validation', ''] + [f'- {x}' for x in validation] + ['']
    return '\n'.join(lines)


def validate(expected: dict, reviewed: dict, candidate: dict[str, bytes]) -> list[str]:
    issues = []
    for key in ('schema', 'previous_controlled_sha256', 'candidate_controlled_sha256'):
        if reviewed.get(key) != expected[key]:
            issues.append(f'{key} mismatch (stale or wrong baseline/candidate)')
    indexed = {item.get('id'): item for item in reviewed.get('changes', [])}
    if len(indexed) != len(reviewed.get('changes', [])):
        issues.append('duplicated change IDs in review')
    expected_ids = {item['id'] for item in expected['changes']}
    if set(indexed) != expected_ids:
        issues.append('missing/extra changed hunks in review')
    for current in expected['changes']:
        item = indexed.get(current['id'])
        if not item:
            continue
        for name in ('path', 'change', 'old_range', 'new_range', 'removed', 'added'):
            if item.get(name) != current[name]:
                issues.append(f'{current["id"]}: candidate diff metadata changed')
                break
        decision = item.get('assessment')
        if decision not in ('preserved', 'relocated', 'authorized_change', 'non_semantic'):
            issues.append(f'{current["id"]}: unresolved assessment ({decision})')
            continue
        if len(item.get('reason', '').strip()) < 25:
            issues.append(f'{current["id"]}: missing concrete before/after reasoning')
        if decision in ('preserved', 'relocated'):
            location = item.get('retained_location', '')
            quote = item.get('evidence_quote', '')
            data = candidate.get(location)
            if not data or len(quote.strip()) < 15 or quote not in data.decode('utf-8', 'replace'):
                issues.append(f'{current["id"]}: retained semantic not located in candidate evidence')
        if decision == 'authorized_change' and len(item.get('authority', '').strip()) < 10:
            issues.append(f'{current["id"]}: missing change authority')
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--prepare-review', type=Path, help='generate initially unresolved per-hunk JSON ledger')
    parser.add_argument('--review', type=Path, help='validate semantically reviewed ledger')
    parser.add_argument('--report', type=Path, help='write evidence packet Markdown')
    args = parser.parse_args()
    if bool(args.prepare_review) == bool(args.review):
        parser.error('use exactly one of --prepare-review or --review')
    prior, candidate = load(args.previous), load(args.candidate)
    expected = ledger(prior, candidate, modes(args.previous), modes(args.candidate))
    if args.prepare_review:
        args.prepare_review.parent.mkdir(parents=True, exist_ok=True)
        args.prepare_review.write_text(json.dumps(expected, ensure_ascii=False, indent=2) + '\n')
        issues = ['REVIEW REQUIRED — per-hunk semantic preservation not yet established'] if expected['changes'] else []
        if args.report:
            args.report.write_text(report(expected, issues))
        print(f'PRIOR-RELEASE PRESERVATION: {len(expected["changes"])} material hunks; '
              + ('REVIEW REQUIRED' if issues else 'NO CONTROLLED DIFF'))
        return 0
    reviewed = json.loads(args.review.read_text())
    issues = validate(expected, reviewed, candidate)
    if args.report:
        args.report.write_text(report(reviewed, issues if issues else ['all changed hunks adjudicated (semantic correctness requires independent evidence)']))
    if issues:
        for issue in issues:
            print('REVIEW: ' + issue)
        print('PRIOR-RELEASE PRESERVATION: FAIL — unresolved/stale semantic comparison')
        return 1
    print(f'PRIOR-RELEASE PRESERVATION: PASS — {len(expected["changes"])} reviewed material hunks; documented semantic dispositions')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f'PRIOR-RELEASE PRESERVATION: FAIL — {exc}', file=sys.stderr)
        raise SystemExit(1)
