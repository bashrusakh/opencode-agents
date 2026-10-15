#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

def read(root,rel):
    p=root/rel
    if not p.is_file(): raise FileNotFoundError(rel)
    return p.read_text(encoding='utf-8')

def group(chunk,patterns): return any(re.search(p,chunk,re.I|re.M) for p in patterns)
def window(text,groups,width,min_groups=None):
    lines=text.splitlines()
    if not groups: return None
    required=len(groups) if min_groups is None else int(min_groups)
    if required < 1 or required > len(groups):
        raise ValueError(f'min_groups must be within 1..{len(groups)}, got {required}')
    for i in range(len(lines)):
        c='\n'.join(lines[i:i+max(1,width)])
        if sum(1 for g in groups if group(c,g)) >= required: return i+1,c
    return None

def frontmatter_mode(text):
    m=re.match(r'^---\n(.*?)\n---\n',text,re.S)
    if not m: return None
    mm=re.search(r'^mode:\s*(\S+)\s*$',m.group(1),re.M)
    return mm.group(1) if mm else None

def required_families(text, rows, label):
    out=[]
    for fam in rows or []:
        m=window(text,fam.get('groups') or [],fam.get('window_lines',12),fam.get('min_groups'))
        if not m: out.append(f"{label} missing required resident semantic family {fam.get('id')}")
    return out

def audit(root:Path,spec_path:Path):
    out=[]
    try: s=json.loads(spec_path.read_text())
    except Exception as e: return [f'residency spec unreadable: {e}']
    if s.get('schema_version')!=1: out.append('residency spec schema_version must be 1')
    r=s.get('root',{}); rp=r.get('path','AGENTS.md')
    try: rt=read(root,rp)
    except FileNotFoundError: return out+[f'root surface missing: {rp}']
    for fam in r.get('forbidden_families',[]):
        m=window(rt,fam.get('groups') or [],fam.get('window_lines',12),fam.get('min_groups'))
        if m: out.append(f"global root contains non-universal residency family {fam.get('id')} at {rp}:{m[0]}")
    out.extend(required_families(rt,r.get('required_families'),f'global root {rp}'))
    allowed_audiences={'primary-entry','delegation-caller','implementation/judgment','code-host-resource','terminal-diagnostic','code-to-ui-routing'}
    for c in s.get('contracts',[]):
        cid=c.get('id'); path=c.get('path'); audience=c.get('audience')
        if audience not in allowed_audiences: out.append(f'{cid}: invalid/missing residency audience {audience!r}')
        try: text=read(root,path)
        except FileNotFoundError: out.append(f'{cid}: contract missing: {path}'); continue
        if c.get('autoinvoke_false') and not re.search(r'opencode/autoinvoke:\s*["\']?false["\']?',text,re.I):
            out.append(f'{cid}: conditional contract must set opencode/autoinvoke false')
        out.extend(required_families(text,c.get('required_families'),f'{cid} {path}'))
        activators={a.get('path') for a in c.get('activators',[])}
        for a in c.get('activators',[]):
            ap=a.get('path'); sig=a.get('signature') or []
            try: at=read(root,ap)
            except FileNotFoundError: out.append(f'{cid}: activator missing: {ap}'); continue
            if not all(re.search(re.escape(x),at,re.I) for x in sig): out.append(f'{cid}: activation boundary missing/drifted in {ap}')
            mode=frontmatter_mode(at); need=a.get('mode')
            if need=='always-primary' and mode!='primary': out.append(f'{cid}: {ap} declared always-primary but frontmatter mode={mode!r}')
            if need=='primary-only' and mode!='all': out.append(f'{cid}: {ap} primary-only activation expects mode: all, got {mode!r}')
            for fam in c.get('forbidden_activator_families',[]):
                fm=window(at,fam.get('groups') or [],fam.get('window_lines',12),fam.get('min_groups'))
                if fm: out.append(f"{cid}: activator {ap} still contains conditional residency family {fam.get('id')} at line {fm[0]}")
        token=f'load `{cid}`'
        for fp in c.get('forbidden_role_paths',[]):
            try: ft=read(root,fp)
            except FileNotFoundError: out.append(f'{cid}: forbidden role missing: {fp}'); continue
            if token.lower() in ft.lower(): out.append(f'{cid}: forbidden residency activation present in {fp}')
    return out

def main():
    ap=argparse.ArgumentParser(); d=Path(__file__).resolve().parents[1]
    ap.add_argument('--root',type=Path,default=d); ap.add_argument('--spec',type=Path,default=None)
    a=ap.parse_args(); root=a.root.resolve(); sp=(a.spec or root/'evals/runtime-residency-spec.json').resolve()
    f=audit(root,sp)
    if f:
        print('RUNTIME RESIDENCY AUDIT: FAIL'); [print('-',x) for x in f]; return 1
    s=json.loads(sp.read_text()); print(f'RUNTIME RESIDENCY AUDIT: PASS ({len(s.get("contracts",[]))} conditional contracts; global root universal)'); return 0
if __name__=='__main__': raise SystemExit(main())
