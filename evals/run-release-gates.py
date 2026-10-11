#!/usr/bin/env python3
"""Run release-gate checks without converting unresolved findings into PASS.

Structural/static checks and contract/protocol checks are separate evidence classes.
Promotion requires both. Behavioral semantic replay remains a separate mandatory claim
when a release says those scenarios passed.
"""
from __future__ import annotations
import subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
checks=[
    ("contract audit selftest", [sys.executable, str(ROOT/'evals/contract-protocol-selftest.py')]),
    ("static policy regressions", [sys.executable, str(ROOT/'evals/static-policy-regressions.py')]),
    ("contract/protocol audit", [sys.executable, str(ROOT/'evals/contract-protocol-audit.py')]),
    ("role-handoff selftest", [sys.executable, str(ROOT/'evals/role-handoff-selftest.py')]),
    ("role-handoff edge audit", [sys.executable, str(ROOT/'evals/role-handoff-audit.py')]),
]
failed=[]
for name,cmd in checks:
    print(f"\n=== {name} ===")
    proc=subprocess.run(cmd, cwd=ROOT)
    if proc.returncode:
        failed.append((name,proc.returncode))
print("\n=== release gate summary ===")
if failed:
    for name,code in failed:
        print(f"FAIL {name} (exit {code})")
    print("RELEASE GATES: FAIL — unresolved findings must not be waived merely to obtain PASS")
    raise SystemExit(1)
print("RELEASE GATES: PASS — behavioral replay claims still require actual isolated replay")
