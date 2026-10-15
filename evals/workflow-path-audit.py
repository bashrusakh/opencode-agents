#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

def read(root,rel):
 p=root/rel
 if not p.is_file(): raise FileNotFoundError(rel)
 return p.read_text(encoding='utf-8')

def group_ok(text, pats): return any(re.search(p,text,re.I|re.M|re.S) for p in pats)
def first_line(text,pats):
 lines=text.splitlines()
 for i,line in enumerate(lines,1):
  if any(re.search(p,line,re.I) for p in pats): return i
 return None

def audit(root:Path,spec_path:Path):
 out=[]
 try:s=json.loads(spec_path.read_text())
 except Exception as e:return [f'workflow-path spec unreadable: {e}']
 if s.get('schema_version')!=1: out.append('workflow-path spec schema_version must be 1')
 rows=s.get('scenarios') or []
 if not rows:return out+['workflow-path spec scenarios must be non-empty']
 for sc in rows:
  sid=sc.get('id','?'); cache={}; positions=[]
  for i,node in enumerate(sc.get('nodes') or []):
   path=node.get('path'); groups=node.get('groups') or []
   try:text=cache.setdefault(path,read(root,path))
   except FileNotFoundError: out.append(f'{sid}: missing surface {path}'); continue
   anchor=node.get('anchor')
   scoped=text
   ln=None
   if anchor:
    ln=first_line(text,anchor)
    if ln is None:
     out.append(f'{sid}: {path} missing timing/order anchor {anchor}')
    else:
     positions.append((path,ln,node.get('label',str(i))))
     width=node.get('window_lines')
     if width:
      lines=text.splitlines(); scoped='\n'.join(lines[ln-1:ln-1+int(width)])
   for gi,g in enumerate(groups):
    if not group_ok(scoped,g): out.append(f'{sid}: {path} missing semantic group {gi+1}: {g}')
  # only compare explicit sequential nodes on same surface
  by={}
  for path,ln,label in positions: by.setdefault(path,[]).append((ln,label))
  for path,seq in by.items():
   nums=[x[0] for x in seq]
   if nums!=sorted(nums): out.append(f'{sid}: checkpoint order drift in {path}: {seq}')
  for h in sc.get('handoffs') or []:
   pp=h['producer']; cp=h['consumer']
   try:pt=cache.setdefault(pp,read(root,pp)); ct=cache.setdefault(cp,read(root,cp))
   except FileNotFoundError as e: out.append(f'{sid}: handoff surface missing: {e}'); continue
   for gi,g in enumerate(h.get('producer_groups') or []):
    if not group_ok(pt,g): out.append(f'{sid}: producer {pp} lacks required handoff info group {gi+1}: {g}')
   for gi,g in enumerate(h.get('consumer_groups') or []):
    if not group_ok(ct,g): out.append(f'{sid}: consumer {cp} does not bind/expect handoff info group {gi+1}: {g}')
  for f in sc.get('forbidden') or []:
   path=f['path']; text=cache.setdefault(path,read(root,path))
   if all(group_ok(text,g) for g in f.get('groups') or []): out.append(f"{sid}: forbidden shortcut/late activation present in {path}: {f.get('id','?')}")
 return out

def main():
 root0=Path(__file__).resolve().parents[1]
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=root0);ap.add_argument('--spec',type=Path,default=None)
 a=ap.parse_args();root=a.root.resolve();sp=(a.spec or root/'evals/workflow-path-spec.json').resolve();f=audit(root,sp)
 if f:
  print('WORKFLOW PATH AUDIT: FAIL');[print('-',x) for x in f];return 1
 n=len(json.loads(sp.read_text()).get('scenarios',[]));print(f'WORKFLOW PATH AUDIT: PASS ({n} end-to-end scenarios)');return 0
if __name__=='__main__':raise SystemExit(main())
