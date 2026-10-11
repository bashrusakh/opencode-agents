#!/usr/bin/env python3
"""Closed-world static audit for pack-owned role handoff/routing interfaces.

This gate complements role executability. It has two independent jobs:
1. Inventory completeness: every pack-owned @role relation in root/agent contracts must be
   explicitly classified. A new unknown edge and a stale classification both fail release.
2. Interface semantics: material delegation callers and high-risk caller->callee edges must
   carry the target/state/authority/evidence boundaries needed by the downstream contract.

The inventory is intentionally closed-world. Adding an @role reference is a topology change,
not harmless prose: it requires conscious classification and, when material, an edge profile.
"""
from __future__ import annotations
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AG = ROOT / 'agents'


def text(name: str) -> str:
    return (AG / name).read_text(encoding='utf-8')


def groups_present(hay: str, groups: list[list[str]]) -> bool:
    return all(any(re.search(p, hay, re.I | re.M | re.S) for p in g) for g in groups)


# Closed-world classification of every current pack-owned @role relation discovered in
# AGENTS.md or an agents/*.md standing contract. Classification is semantic topology, not
# proof that the edge is safe; material edges are checked again below.
EDGE_CLASSIFICATION = {
    ('root','auditor'): 'routing_policy',
    ('root','build'): 'routing_policy',
    ('root','code-orchestrator'): 'routing_policy',
    ('root','debugger'): 'routing_policy',
    ('root','devops'): 'routing_policy',
    ('root','explore'): 'routing_policy',
    ('root','general'): 'routing_policy',
    ('root','project-planner'): 'routing_policy',
    ('root','reviewer'): 'routing_policy',
    ('root','session-evaluator'): 'routing_policy',
    ('root','tester'): 'routing_policy',
    ('root','ui-implementer'): 'routing_policy',
    ('root','ui-orchestrator'): 'routing_policy',

    ('auditor','a11y-reviewer'): 'delegation',
    ('auditor','devops'): 'delegation',
    ('auditor','explore'): 'delegation',
    ('auditor','general'): 'delegation',
    ('auditor','reviewer'): 'delegation',
    ('auditor','tester'): 'delegation',
    ('auditor','ui-auditor'): 'delegation',

    ('build','debugger'): 'reroute',
    ('build','reviewer'): 'conditional_delegate',
    ('build','tester'): 'conditional_delegate',

    ('code-orchestrator','build'): 'delegation',
    ('code-orchestrator','debugger'): 'delegation',
    ('code-orchestrator','devops'): 'delegation',
    ('code-orchestrator','explore'): 'delegation',
    ('code-orchestrator','general'): 'delegation',
    ('code-orchestrator','project-planner'): 'delegation',
    ('code-orchestrator','reviewer'): 'delegation',
    ('code-orchestrator','semantic-checkpoint'): 'delegation',
    ('code-orchestrator','session-evaluator'): 'delegation',
    ('code-orchestrator','tester'): 'delegation',
    ('code-orchestrator','ui-implementer'): 'delegation',
    ('code-orchestrator','ui-orchestrator'): 'delegation',

    ('debugger','tester'): 'boundary_reference',
    ('devops','debugger'): 'reroute',
    ('explore','tester'): 'boundary_reference',
    ('project-planner','tester'): 'boundary_reference',
    ('project-planner','ui-orchestrator'): 'specialist_boundary',
    ('project-planner','ui-planner'): 'specialist_boundary',
    ('reviewer','tester'): 'boundary_reference',
    ('ui-auditor','ui-planner'): 'escalation',
    ('ui-implementer','tester'): 'boundary_reference',

    ('ui-orchestrator','a11y-reviewer'): 'delegation',
    ('ui-orchestrator','code-orchestrator'): 'return_to_parent',
    ('ui-orchestrator','explore'): 'delegation',
    ('ui-orchestrator','reviewer'): 'delegation',
    ('ui-orchestrator','tester'): 'delegation',
    ('ui-orchestrator','ui-auditor'): 'delegation',
    ('ui-orchestrator','ui-implementer'): 'delegation',
    ('ui-orchestrator','ui-planner'): 'delegation',

    ('ui-planner','tester'): 'boundary_reference',
    ('ui-planner','ui-implementer'): 'output_package',
}

ALLOWED_KINDS = {
    'routing_policy', 'delegation', 'conditional_delegate', 'reroute',
    'boundary_reference', 'specialist_boundary', 'escalation',
    'return_to_parent', 'output_package',
}

# Generic delegation contracts shared by every direct leaf delegation from these callers.
# Specific high-risk edges below add stronger callee-specific requirements.
CALLER_DELEGATION = {
    'code-orchestrator': [
        [r'objective and behavioral/target scope'], [r'allowed action level'],
        [r'expected deliverable/evidence'], [r'stop or escalation conditions'],
        [r'omit upstream non-required mechanism|label it explicitly non-binding'],
    ],
    'auditor': [
        [r'audit question'], [r'exact target/state'], [r'bounded subsystem/behavior surface'],
        [r'allowed action level'], [r'expected evidence'], [r'stop/coverage boundary'],
        [r'do not forward .*suspected root cause|do not forward .*preferred fix|not acceptance'],
    ],
    'ui-orchestrator': [
        [r'established UI outcome/problem|established user-visible outcome'],
        [r'exact target/state when relevant|target/mutation baseline'],
        [r'material constraints'], [r'evidence'], [r"leaf's question|leaf assignments"],
        [r'do not solve the leaf.*method upstream|do not forward .*authority'],
    ],
}

# High-risk edge-specific semantic groups. These complement, not replace, the generic
# delegation contract above. All groups for an edge must hold.
EDGE = {
 ('code-orchestrator','devops'): [
   [r'operational symptom|symptom/target|symptom.*target'], [r'action ceiling'], [r'current evidence|evidence'],
   [r'do not assign .*config change|do not .*suspected .*change|hypoth'],
 ],
 ('code-orchestrator','general'): [
   [r'bounded .*research question|one bounded .*question'], [r'evidence/source scope|source scope|allowed evidence'], [r'specialist owns|another specialist|stop'],
 ],
 ('code-orchestrator','ui-implementer'): [
   [r'established user-visible outcome'], [r'target/mutation state|target.*state'], [r'material constraints'], [r'preserved behavior'],
   [r'do not preselect .*layout|do not preselect .*files|omit .*mechanism'],
 ],
 ('ui-orchestrator','ui-auditor'): [
   [r'current screen/flow'], [r'primary user job'], [r'audit question/boundary'], [r'current-state evidence'], [r'do not preselect .*redesign'],
 ],
 ('ui-orchestrator','ui-planner'): [
   [r'established outcome/problem'], [r'current-state evidence'], [r'material constraints'], [r'unresolved design/layout/theme decision'], [r'non-exhaustive hypotheses'],
 ],
 ('ui-orchestrator','ui-implementer'): [
   [r'established user-visible outcome'], [r'actually adopted plan propositions/constraints'], [r'target/mutation baseline'], [r'preserved behavior'], [r'omit non-required .*recommendations'],
 ],
 ('ui-orchestrator','a11y-reviewer'): [
   [r'advisory'], [r'stable-result verification|stable result'], [r'exact stable target'], [r'changed interaction boundary'], [r'preserved behavior/constraints|preserved behavior'], [r'available evidence'], [r'stale after .*edit'],
 ],
 ('auditor','specialists'): [
   [r'audit question'], [r'exact target/state'], [r'bounded subsystem/behavior surface'], [r'allowed action level'], [r'expected evidence'], [r'stop/coverage boundary'],
   [r'do not forward .*suspected root cause|do not forward .*preferred fix|not acceptance'],
 ],
 ('auditor','devops'): [[r'@devops'], [r'action ceiling read-only|set the action ceiling read-only']],
 ('auditor','general'): [[r'@general'], [r'one bounded research question'], [r'does not replace .*specialist stage']],
 ('auditor','independent-judgment'): [[r'independent reviewer/a11y'], [r'fresh judgment-context isolation|judgment-context isolation']],
}

CALLER_FILES = {'code-orchestrator':'code-orchestrator.md','ui-orchestrator':'ui-orchestrator.md','auditor':'auditor.md'}


def discover_edges_from_texts(texts: dict[str, str], agent_names: set[str]) -> set[tuple[str, str]]:
    out: set[tuple[str, str]] = set()
    for caller, hay in texts.items():
        for role in set(re.findall(r'@([a-zA-Z0-9_-]+)', hay)):
            if role in agent_names and role != caller:
                out.add((caller, role))
    return out


def inventory_findings(discovered: set[tuple[str,str]], classified: dict[tuple[str,str],str] | None = None) -> list[str]:
    classified = EDGE_CLASSIFICATION if classified is None else classified
    findings: list[str] = []
    unknown = sorted(discovered - set(classified))
    stale = sorted(set(classified) - discovered)
    invalid = sorted((edge, kind) for edge, kind in classified.items() if kind not in ALLOWED_KINDS)
    for caller, target in unknown:
        findings.append(f'UNCLASSIFIED EDGE {caller} -> {target}: discovered pack-owned @role relation has no topology/protocol classification')
    for caller, target in stale:
        findings.append(f'STALE EDGE {caller} -> {target}: classification exists but the relation is no longer present in pack-owned standing contracts')
    for (caller, target), kind in invalid:
        findings.append(f'INVALID EDGE CLASS {caller} -> {target}: {kind!r}')
    return findings


def audit_specific_edges(callers: dict[str,str]) -> list[str]:
    findings=[]
    for (caller,target), groups in EDGE.items():
        hay=callers.get(caller,'')
        if not groups_present(hay,groups):
            findings.append(f'{caller} -> {target}: handoff contract missing one or more required semantic groups')
    return findings


def audit_generic_delegators(callers: dict[str,str], classified: dict[tuple[str,str],str] | None = None) -> list[str]:
    classified = EDGE_CLASSIFICATION if classified is None else classified
    findings=[]
    material_callers={caller for (caller,_), kind in classified.items() if kind == 'delegation'}
    for caller in sorted(material_callers):
        groups=CALLER_DELEGATION.get(caller)
        if not groups:
            findings.append(f'{caller}: direct delegation edges exist but no generic caller assignment contract is audited')
            continue
        if not groups_present(callers.get(caller,''), groups):
            findings.append(f'{caller}: generic direct-delegation assignment contract missing one or more required semantic groups')
    return findings


def audit_texts(callers: dict[str,str]) -> list[str]:
    """Compatibility helper used by synthetic semantic fixtures."""
    return audit_generic_delegators(callers) + audit_specific_edges(callers)


def main() -> int:
    agent_names={p.stem for p in AG.glob('*.md')}
    all_texts={'root': (ROOT/'AGENTS.md').read_text(encoding='utf-8')}
    all_texts.update({p.stem:p.read_text(encoding='utf-8') for p in AG.glob('*.md')})
    discovered=discover_edges_from_texts(all_texts,agent_names)
    callers={k:text(v) for k,v in CALLER_FILES.items()}

    findings=[]
    findings.extend(inventory_findings(discovered))
    findings.extend(audit_generic_delegators(callers))
    findings.extend(audit_specific_edges(callers))

    print('ROLE HANDOFF EDGE AUDIT v2')
    print(f'Discovered/classified pack-owned role relations: {len(discovered)}/{len(EDGE_CLASSIFICATION)}')
    counts=Counter(EDGE_CLASSIFICATION.values())
    print('Classification inventory: ' + ', '.join(f'{k}={counts[k]}' for k in sorted(counts)))
    if findings:
        for f in findings: print(' - FAIL:',f)
        print(f'FAIL: {len(findings)} unresolved edge/inventory finding(s)')
        return 1
    print(f'PASS: closed-world inventory exact; {len(EDGE)} high-risk profiles and {len(CALLER_DELEGATION)} generic delegation contracts satisfied')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
