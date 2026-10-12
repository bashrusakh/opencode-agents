#!/usr/bin/env python3
"""Behavioral smoke tests for installer ownership/preservation semantics.

These tests use isolated temporary HOME/project directories and invoke the real shell
installers. They prove only installer filesystem behavior, not OpenCode runtime loading.
"""
from __future__ import annotations
import os, subprocess, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GLOBAL=ROOT/'install/install-global.sh'
PROJECT=ROOT/'install/install-project.sh'

def run(script: Path, cwd: Path, home: Path, extra=None):
    env=os.environ.copy(); env['HOME']=str(home)
    if extra: env.update(extra)
    return subprocess.run(['bash', str(script)], cwd=cwd, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def check(cond, msg):
    if not cond: raise AssertionError(msg)

with tempfile.TemporaryDirectory(prefix='opencode-installer-selftest-') as td:
    t=Path(td)

    # Project-owned AGENTS.md without a global pack root: fail before mutation.
    home=t/'home-no-global'; home.mkdir()
    proj=t/'project-blocked'; proj.mkdir()
    original='# Project rules\nkeep me\n'; (proj/'AGENTS.md').write_text(original)
    p=run(PROJECT, proj, home)
    check(p.returncode==2, f'project installer should block without global root: {p.returncode} {p.stderr}')
    check((proj/'AGENTS.md').read_text()==original, 'project-owned AGENTS.md changed on blocked install')
    check(not (proj/'.opencode').exists(), 'blocked project install mutated .opencode')

    # Project-owned AGENTS.md with a recognizable global pack root: preserve project file,
    # install agents/skills, and preserve ambiguous legacy commands.
    home=t/'home-global'; gbase=home/'.config/opencode'; gbase.mkdir(parents=True)
    (gbase/'AGENTS.md').write_text('# OpenCode Agent Rules\n\n**Pack version: v30.79 beta**\n')
    proj=t/'project-preserve'; (proj/'.opencode/commands').mkdir(parents=True)
    (proj/'AGENTS.md').write_text(original)
    legacy='my custom review command\n'; (proj/'.opencode/commands/review.md').write_text(legacy)
    p=run(PROJECT, proj, home)
    check(p.returncode==0, f'project installer failed with global root: {p.returncode} {p.stderr}')
    check((proj/'AGENTS.md').read_text()==original, 'project-owned AGENTS.md was overwritten')
    check((proj/'.opencode/commands/review.md').read_text()==legacy, 'ambiguous project legacy command was deactivated')
    check((proj/'.opencode/agents/reviewer.md').is_file(), 'project agents not installed')
    check((proj/'.opencode/.agent-pack/managed-files.sha256').is_file(), 'project ownership receipt missing')

    # No project AGENTS.md: the pack root may be installed project-locally.
    home=t/'home-empty'; home.mkdir()
    proj=t/'project-new'; proj.mkdir()
    p=run(PROJECT, proj, home)
    check(p.returncode==0, f'new project install failed: {p.returncode} {p.stderr}')
    check('# OpenCode Agent Rules' in (proj/'AGENTS.md').read_text(), 'pack root not installed into project without AGENTS.md')

    # Unknown global AGENTS.md: refuse before mutating runtime surfaces.
    home=t/'home-custom'; base=home/'.config/opencode'; base.mkdir(parents=True)
    custom='# My global rules\ndo not replace\n'; (base/'AGENTS.md').write_text(custom)
    p=run(GLOBAL, t, home)
    check(p.returncode==2, f'global installer should refuse unknown AGENTS.md: {p.returncode} {p.stderr}')
    check((base/'AGENTS.md').read_text()==custom, 'unknown global AGENTS.md changed on blocked install')
    check(not (base/'agents').exists(), 'blocked global install mutated agents directory')

    # Recognized prior pack root: update, back up collisions, preserve ambiguous legacy names.
    home=t/'home-upgrade'; base=home/'.config/opencode'; (base/'agents').mkdir(parents=True); (base/'commands').mkdir(parents=True)
    old_root='# OpenCode Agent Rules\n\n**Pack version: v30.79 beta**\nold pack root\n'; (base/'AGENTS.md').write_text(old_root)
    old_reviewer='customized previous reviewer\n'; (base/'agents/reviewer.md').write_text(old_reviewer)
    legacy='personal review command\n'; (base/'commands/review.md').write_text(legacy)
    p=run(GLOBAL, t, home)
    check(p.returncode==0, f'global upgrade failed: {p.returncode} {p.stderr}')
    check('**Pack version: v30.80 beta**' in (base/'AGENTS.md').read_text(), 'global pack root not updated')
    check((base/'commands/review.md').read_text()==legacy, 'ambiguous global command was deactivated')
    receipt=base/'.agent-pack/managed-files.sha256'; check(receipt.is_file(), 'global ownership receipt missing')
    backups=list((base/'.agent-pack/backups').glob('*/agents/reviewer.md'))
    check(backups and backups[-1].read_text()==old_reviewer, 'colliding global reviewer was not backed up')
    root_backups=list((base/'.agent-pack/backups').glob('*/AGENTS.md'))
    check(root_backups and root_backups[-1].read_text()==old_root, 'prior global pack root was not backed up')

print('INSTALLER SAFETY SELFTEST: PASS')
