#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

STALE_PATTERNS={
    r'root\s+`###\s+(?:Startup|Update)`':'Startup/Update moved to workflow-control',
    r'root\s+map\b':'routing map moved to delegation-control',
    r'root\s+fallback\s+contract':'fallback contract moved to delegation-control',
    r'root\s+review\s+cadence':'review cadence moved to delegation-control',
    r'root\s+gate\b':'user-approvable gate procedure moved to workflow-control/caller boundary',
    r'root/project\s+routing':'routing/fallback moved to delegation-control/project policy',
    r'freshness\s+under\s+the\s+root\s+rule':'current-upstream/default/base freshness moved to git-provenance',
    r'judgment-context\s+isolation\s+under\s+the\s+root\s+contract':'independent-judgment isolation moved to delegation-control',
}

def root_sections(text:str)->set[str]:
    ids=set()
    for line in text.splitlines():
        m=re.match(r'^#{2,4}\s+([0-9]+(?:\.[0-9]+)*)\b',line)
        if m: ids.add(m.group(1))
    return ids

def pack_surfaces()->list[Path]:
    out=sorted((ROOT/'agents').glob('*.md'))
    spec=json.loads((ROOT/'evals/skill-control-spec.json').read_text())
    for row in spec.get('skills',[]):
        if row.get('class')!='vendor-advisory':
            out.append(ROOT/row['path'])
    return out

def audit()->list[str]:
    findings=[]
    root=(ROOT/'AGENTS.md').read_text()
    ids=root_sections(root)
    for p in pack_surfaces():
        text=p.read_text()
        rel=p.relative_to(ROOT)
        lines=text.splitlines()
        for i,line in enumerate(lines,1):
            # Explicit numeric root references must resolve in current AGENTS.md.
            if re.search(r'\broot\b',line,re.I):
                for m in re.finditer(r'root\s+(?:section|§)\s*([0-9]+(?:\.[0-9]+)*)',line,re.I):
                    if m.group(1) not in ids:
                        findings.append(f'{rel}:{i}: dangling root section {m.group(1)}')
                m=re.search(r'root\s+sections\s+(.+)',line,re.I)
                if m:
                    for sec in re.findall(r'\b([0-9]+(?:\.[0-9]+)*)\b',m.group(1)):
                        if sec not in ids:
                            findings.append(f'{rel}:{i}: dangling root section {sec}')
            for pat,why in STALE_PATTERNS.items():
                if re.search(pat,line,re.I):
                    findings.append(f'{rel}:{i}: stale semantic reference ({why})')
    return findings

def main()->int:
    f=audit()
    if f:
        print('REFERENCE INTEGRITY AUDIT: FAIL')
        for x in f: print('-',x)
        return 1
    print(f'REFERENCE INTEGRITY AUDIT: PASS ({len(root_sections((ROOT/"AGENTS.md").read_text()))} root sections; {len(pack_surfaces())} pack-controlled surfaces)')
    return 0

if __name__=='__main__': raise SystemExit(main())
