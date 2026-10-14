#!/usr/bin/env python3
"""Ensure root/code-orchestrator section placement is explicitly reviewed.

This is not a semantic-equivalence detector. It closes a different blind spot: a new
or moved material section cannot silently enter either always-loaded surface without
being classified as shared owner/boundary, role owner, specialization, or reference
consumer in the reviewed section map.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

VALID={"shared_owner","shared_boundary","role_owner","specialization","reference_consumer"}
HEAD=re.compile(r"^(##|###)\s+.+$")


def headings(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding='utf-8').splitlines() if HEAD.match(line)]


def audit(root: Path, spec_path: Path) -> list[str]:
    failures=[]
    try:
        spec=json.loads(spec_path.read_text(encoding='utf-8'))
    except Exception as exc:
        return [f"section map unreadable: {exc}"]
    if spec.get('schema_version') != 1:
        failures.append('section map schema_version must be 1')
    surfaces=spec.get('surfaces')
    if not isinstance(surfaces,dict) or not surfaces:
        return failures+['section map surfaces must be a non-empty object']
    for rel, entries in surfaces.items():
        path=root/rel
        if not path.is_file():
            failures.append(f"mapped surface missing: {rel}"); continue
        actual=headings(path)
        mapped=[]
        if not isinstance(entries,list):
            failures.append(f"{rel}: map entries must be a list"); continue
        for e in entries:
            h=e.get('heading'); placement=e.get('placement'); purpose=e.get('purpose')
            if not isinstance(h,str) or not h:
                failures.append(f"{rel}: entry missing heading"); continue
            mapped.append(h)
            if placement not in VALID:
                failures.append(f"{rel} {h}: invalid placement {placement!r}")
            if not isinstance(purpose,str) or len(purpose.strip()) < 12:
                failures.append(f"{rel} {h}: purpose is missing/too weak")
        if actual != mapped:
            missing=[h for h in actual if h not in mapped]
            stale=[h for h in mapped if h not in actual]
            order=(not missing and not stale and actual != mapped)
            if missing: failures.append(f"{rel}: unmapped runtime sections: {missing}")
            if stale: failures.append(f"{rel}: stale mapped sections: {stale}")
            if order: failures.append(f"{rel}: section-map order differs from runtime order")
    return failures


def main()->int:
    parser=argparse.ArgumentParser(); default=Path(__file__).resolve().parents[1]
    parser.add_argument('--root',type=Path,default=default); parser.add_argument('--spec',type=Path,default=None)
    a=parser.parse_args(); root=a.root.resolve(); sp=(a.spec or root/'evals/root-orchestrator-section-map.json').resolve()
    f=audit(root,sp)
    if f:
        print('SECTION OWNERSHIP AUDIT: FAIL'); [print('-',x) for x in f]; return 1
    spec=json.loads(sp.read_text(encoding='utf-8'))
    n=sum(len(v) for v in spec['surfaces'].values())
    print(f'SECTION OWNERSHIP AUDIT: PASS ({n} mapped sections across {len(spec["surfaces"])} surfaces)')
    return 0
if __name__=='__main__': raise SystemExit(main())
