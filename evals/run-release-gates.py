#!/usr/bin/env python3
"""Run release-gate checks without converting unresolved findings into PASS.

Structural/static checks and contract/protocol checks are separate evidence classes.
Promotion requires both. Behavioral semantic replay remains a separate mandatory claim
when a release says those scenarios passed.
"""
from __future__ import annotations
import subprocess, sys, argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description='Run candidate gates; --release also requires prior-package preservation evidence')
parser.add_argument('--release', action='store_true', help='assert this is a promotable release, not just a candidate self-check')
parser.add_argument('--previous', type=Path, help='prior released ZIP or extracted package')
parser.add_argument('--preservation-review', type=Path, help='completed evidence-bearing prior-release review ledger')
args=parser.parse_args()
if args.release and (args.previous is None or args.preservation_review is None):
    parser.error('--release requires --previous and --preservation-review')
if not args.release and (args.previous is not None or args.preservation_review is not None):
    parser.error('--previous/--preservation-review require --release')
checks=[
    ("contract audit selftest", [sys.executable, str(ROOT/'evals/contract-protocol-selftest.py')]),
    ("skill control selftest", [sys.executable, str(ROOT/'evals/skill-control-selftest.py')]),
    ("skill control audit", [sys.executable, str(ROOT/'evals/skill-control-audit.py')]),
    ("semantic ownership selftest", [sys.executable, str(ROOT/'evals/semantic-ownership-selftest.py')]),
    ("semantic ownership audit", [sys.executable, str(ROOT/'evals/semantic-ownership-audit.py')]),
    ("semantic domain selftest", [sys.executable, str(ROOT/'evals/semantic-domain-selftest.py')]),
    ("semantic domain audit", [sys.executable, str(ROOT/'evals/semantic-domain-audit.py')]),
    ("section ownership selftest", [sys.executable, str(ROOT/'evals/section-ownership-selftest.py')]),
    ("section ownership audit", [sys.executable, str(ROOT/'evals/section-ownership-audit.py')]),
    ("runtime residency selftest", [sys.executable, str(ROOT/'evals/runtime-residency-selftest.py')]),
    ("runtime residency audit", [sys.executable, str(ROOT/'evals/runtime-residency-audit.py')]),
    ("workflow path selftest", [sys.executable, str(ROOT/'evals/workflow-path-selftest.py')]),
    ("workflow path audit", [sys.executable, str(ROOT/'evals/workflow-path-audit.py')]),
    ("reference integrity selftest", [sys.executable, str(ROOT/'evals/reference-integrity-selftest.py')]),
    ("reference integrity audit", [sys.executable, str(ROOT/'evals/reference-integrity-audit.py')]),
    ("static policy regressions", [sys.executable, str(ROOT/'evals/static-policy-regressions.py')]),
    ("prior-release preservation selftest", [sys.executable, str(ROOT/'evals/prior-release-preservation-selftest.py')]),
    ("installer safety selftest", [sys.executable, str(ROOT/'evals/installer-safety-selftest.py')]),
    ("contract/protocol audit", [sys.executable, str(ROOT/'evals/contract-protocol-audit.py')]),
    ("role-handoff selftest", [sys.executable, str(ROOT/'evals/role-handoff-selftest.py')]),
    ("role-handoff edge audit", [sys.executable, str(ROOT/'evals/role-handoff-audit.py')]),
]
if args.release:
    checks.append(('prior-release semantic preservation', [sys.executable,
        str(ROOT/'evals/prior-release-preservation.py'), '--previous', str(args.previous.resolve()),
        '--candidate', str(ROOT), '--review', str(args.preservation_review.resolve())]))
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
if args.release:
    print("RELEASE GATES: PASS — cross-version preservation reviewed; behavioral replay still requires real execution")
else:
    print("CANDIDATE GATES: PASS — NOT promotion evidence without --release/--previous/--preservation-review")
