#!/usr/bin/env python3
"""Closed-world control audit for bundled skill entrypoints.

Pack-owned/integration skills are first-class semantic graph nodes. Vendor skills are
classified but not normalized into pack policy; their bundled bytes are hash-guarded
and any package-owned integration boundary must live outside the vendor content.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

H2=re.compile(r"^##\s+(.+?)\s*$", re.M)
PACK_CLASSES={"pack-workflow","pack-integration"}
ALL_CLASSES=PACK_CLASSES|{"vendor-advisory"}

def read_json(p:Path): return json.loads(p.read_text(encoding='utf-8'))
def sig(text, groups): return bool(groups) and all(any(re.search(x,text,re.I|re.M) for x in g) for g in groups)
def dir_hash(path:Path)->str:
    h=hashlib.sha256()
    for f in sorted(x for x in path.rglob('*') if x.is_file()):
        h.update(str(f.relative_to(path)).encode()+b'\0'+f.read_bytes()+b'\0')
    return h.hexdigest()

def audit(root:Path, spec_path:Path, owner_path:Path|None=None, domain_path:Path|None=None)->list[str]:
    out=[]
    try: spec=read_json(spec_path)
    except Exception as e: return [f"skill-control spec unreadable: {e}"]
    if spec.get('schema_version')!=1: out.append('skill-control spec schema_version must be 1')
    rows=spec.get('skills')
    if not isinstance(rows,list) or not rows: return out+['skill-control spec skills must be non-empty']
    actual={str(p.relative_to(root)) for p in (root/'skills').glob('*/SKILL.md')}
    declared=[]
    by_path={}
    for row in rows:
        p=row.get('path'); cls=row.get('class')
        if not isinstance(p,str) or not p: out.append('skill row missing path'); continue
        if p in by_path: out.append(f'duplicate skill-control path: {p}')
        by_path[p]=row; declared.append(p)
        if cls not in ALL_CLASSES: out.append(f'{p}: invalid class {cls!r}')
        fp=root/p
        if not fp.is_file(): out.append(f'{p}: skill entrypoint missing'); continue
        for field in ('owned_capabilities','consumed_capabilities','typed_domains'):
            if not isinstance(row.get(field),list): out.append(f'{p}: {field} must be a list')
        if not isinstance(row.get('side_effect_class'),str) or not row.get('side_effect_class'):
            out.append(f'{p}: side_effect_class missing')
        if cls in PACK_CLASSES:
            expected=row.get('entry_sections')
            if not isinstance(expected,list): out.append(f'{p}: pack skill entry_sections must be a list')
            else:
                got=H2.findall(fp.read_text(encoding='utf-8'))
                if got!=expected: out.append(f'{p}: entry section inventory drift: declared={expected!r} actual={got!r}')
            if not row.get('owned_capabilities'): out.append(f'{p}: pack skill must own at least one declared semantic capability')
        elif cls=='vendor-advisory':
            expected=row.get('directory_sha256')
            if not isinstance(expected,str) or len(expected)!=64: out.append(f'{p}: vendor directory_sha256 missing')
            else:
                got=dir_hash(fp.parent)
                if got!=expected: out.append(f'{p}: vendor skill bytes changed without explicit provenance update: declared={expected} actual={got}')
            if row.get('owned_capabilities') or row.get('typed_domains'):
                out.append(f'{p}: vendor-advisory skill may not own pack semantic capabilities/domains')
            io=row.get('integration_owner')
            if io:
                owner=root/io
                if not owner.is_file(): out.append(f'{p}: integration owner missing: {io}')
                elif not sig(owner.read_text(encoding='utf-8'), row.get('integration_signature') or []):
                    out.append(f'{p}: pack integration boundary missing from {io}')
    if actual!=set(declared):
        miss=sorted(actual-set(declared)); stale=sorted(set(declared)-actual)
        if miss: out.append(f'unclassified skill entrypoints: {miss}')
        if stale: out.append(f'stale skill-control entries: {stale}')

    owner_spec=read_json(owner_path or root/'evals/semantic-ownership-spec.json')
    caps={c.get('id'):c for c in owner_spec.get('capabilities',[])}
    domain_spec=read_json(domain_path or root/'evals/semantic-domain-spec.json')
    domains={d.get('id'):d for d in domain_spec.get('domains',[])}
    for p,row in by_path.items():
        if row.get('class') not in PACK_CLASSES: continue
        for cid in row.get('owned_capabilities',[]):
            c=caps.get(cid)
            if not c: out.append(f'{p}: owned capability not in semantic-ownership manifest: {cid}')
            elif c.get('owner')!=p: out.append(f'{p}: capability {cid} owner mismatch: {c.get("owner")}')
        for cid in row.get('consumed_capabilities',[]):
            c=caps.get(cid)
            if not c: out.append(f'{p}: consumed capability not in semantic-ownership manifest: {cid}'); continue
            if p!=c.get('owner') and p not in [x.get('path') for x in c.get('consumers',[])]:
                out.append(f'{p}: consumed capability {cid} does not declare this skill as consumer')
        for did in row.get('typed_domains',[]):
            d=domains.get(did)
            if not d: out.append(f'{p}: typed domain not in semantic-domain manifest: {did}')
            elif d.get('owner')!=p: out.append(f'{p}: typed domain {did} owner mismatch: {d.get("owner")}')
    for cid,c in caps.items():
        owner=c.get('owner')
        if isinstance(owner,str) and owner.startswith('skills/'):
            r=by_path.get(owner)
            if not r: out.append(f'{cid}: skill owner is not in skill-control inventory: {owner}')
            elif r.get('class') not in PACK_CLASSES: out.append(f'{cid}: vendor skill cannot be pack semantic owner: {owner}')
            elif cid not in r.get('owned_capabilities',[]): out.append(f'{cid}: skill-control inventory does not list owner capability for {owner}')
    for did,d in domains.items():
        owner=d.get('owner')
        if isinstance(owner,str) and owner.startswith('skills/'):
            r=by_path.get(owner)
            if not r or r.get('class') not in PACK_CLASSES: out.append(f'{did}: typed domain owner is not a pack-controlled skill: {owner}')
            elif did not in r.get('typed_domains',[]): out.append(f'{did}: skill-control inventory does not list typed domain for {owner}')
    return out

def main()->int:
    ap=argparse.ArgumentParser(); root0=Path(__file__).resolve().parents[1]
    ap.add_argument('--root',type=Path,default=root0); ap.add_argument('--spec',type=Path,default=None)
    a=ap.parse_args(); root=a.root.resolve(); sp=(a.spec or root/'evals/skill-control-spec.json').resolve()
    f=audit(root,sp)
    if f:
        print('SKILL CONTROL AUDIT: FAIL'); [print('-',x) for x in f]; return 1
    spec=read_json(sp); pack=sum(x['class']!='vendor-advisory' for x in spec['skills']); vendor=len(spec['skills'])-pack
    print(f'SKILL CONTROL AUDIT: PASS ({len(spec["skills"])} skills; {pack} pack-controlled, {vendor} vendor-advisory)'); return 0
if __name__=='__main__': raise SystemExit(main())
