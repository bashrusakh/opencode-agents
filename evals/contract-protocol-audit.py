#!/usr/bin/env python3
"""Adversarial cross-role protocol and role-executability audit (v3).

The release gate is designed to falsify the pack, not to reward keyword presence.
A routed role passes only when its *role-local* contract contains an executable core
loop for that role, enough conditional/sequence structure for a weaker conforming
model to act without inventing the missing algorithm, explicit evidence/stop/result
semantics, and compatible producer -> parent transformation -> consumer semantics.

Prompt length is diagnostic only. No byte/line threshold may change a role status.
FAIL means the characteristic execution loop is not safely executable; REVIEW means
the loop is executable but a material correctness/coverage branch remains under-specified.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "evals/contract-protocol-spec.json").read_text(encoding="utf-8"))
AGENT_DIR = ROOT / "agents"

ACTION = re.compile(
    r"\b(?:ask|bind|capture|check|choose|classify|compare|confirm|construct|continue|derive|"
    r"diagnose|discover|establish|evaluate|find|identify|inspect|isolate|load|map|measure|"
    r"preserve|read|reconcile|record|report|reproduce|rerun|return|route|run|search|stop|"
    r"trace|validate|verify|write|apply|implement|review|test)\b",
    re.I,
)
CONDITIONAL = re.compile(r"\b(?:if|when|unless|only when|otherwise|except when|until)\b", re.I)
SEQUENCE = re.compile(r"\b(?:at the start|start from|before|first|then|after|next|finally|before returning|before return)\b", re.I)
NUMBERED = re.compile(r"(?m)^\s*\d+[.)]\s+\S")
BULLET = re.compile(r"(?m)^\s*[-*]\s+\S")

# Generic dimension evidence. Unlike v1, method-oriented dimensions are evaluated
# outside the Result section so a role cannot pass merely by promising to report a word.
DIM = {
    "scope_input": [r"\b(assign(?:ment|ed)|delegat(?:ed|ion)|scope|boundary|bounded|outcome|contract|target)\b"],
    "pre_action_model": [r"\b(before (?:the )?(?:first )?(?:edit|mutation)|pre[- ]?(?:edit|mutation)|implementation proof|establish .* before|derive .* before)\b"],
    "ownership": [r"\b(owner|owning|ownership|primitive|shared abstraction|right level|fix level)\b"],
    "preserved_behavior": [r"\b(preserv(?:e|ed|ation)|negative case|regression|sibling|unaffected|case map|falsif)\b"],
    "self_review": [r"\b(self[- ]review|pre[- ]return|final diff|effective diff|final state|inspect .*diff)\b"],
    "verification": [r"\b(verify|verification|validation|rerun|check(?:s|ed)?|test(?:s|ed)?)\b"],
    "reproduction": [r"\b(reproduce|reproduction|failing check|observed failure|exact symptom)\b"],
    "root_cause": [r"\b(root cause|root-cause|hypothesis|diagnos)\b"],
    "hypothesis_reset": [r"\b(reset|reassess|discard .*hypothesis|failed .*hypothesis|if .* still fails|if .* rejected|contradicts? .*hypothesis)\b"],
    "diagnose_before_change": [r"\b(default to read-only diagnostics|diagnos|inspect .* before|before .*chang)\b"],
    "authorization": [r"\b(authoriz|permission|gate|explicitly authorized|state-changing|production|remote action)\b"],
    "rollback": [r"\b(rollback|reversible|restore)\b"],
    "state_binding": [r"\b(state identity|target ref|candidate|base sha|head sha|exact .*state|fresh ref|freshly resolved|workspace-only|ref/sha)\b"],
    "independence": [r"\b(independent|fresh child|fresh .*review|prior verdict|expected verdict|read-only)\b"],
    "coverage_derivation": [r"\b(derive .*checks|coverage|affected behavior boundary|representative consumers|applicable verification set)\b"],
    "evidence": [r"\b(evidence|proof|proves?|actual output|command|artifact|confidence|supported by)\b"],
    "adversarial_preservation": [r"\b(counterexample|adversarial|both sides|preserv(?:e|ed|ation)|negative|regression|falsif|nearest)\b"],
    "bounded_verdict": [r"\b(verdict|pass with notes|changes required|approve|request changes|confidence limited|advisory|partial|incremental)\b"],
    "unknowns": [r"\b(unknown|gap|uncertain|not covered|do not guess|cannot establish|unresolved|insufficient evidence)\b"],
    "external_target": [r"\b(external target|product|library|framework|api|protocol|upstream|version|version/range|branch/tag|platform|environment|applicability|latest)\b"],
    "decision_space": [r"\b(alternative|tradeoff|decision|unresolved|do not choose|hypothes|direction)\b"],
    "verification_plan": [r"\b(validation|verification|regression|test|checklist|checkpoint)\b"],
    "coverage_limits": [r"\b(not covered|coverage|scope|unknown|limit|too large|highest-risk|confidence|uncovered)\b"],
    "routing": [r"\b(route|routing|choose .*role|specialists?|delegate|delegation|stage)\b"],
    "handoff_construction": [r"\b(handoff|assignment).*(?:outcome|constraint|evidence|target|state|reconstruct|omit|non-binding)\b", r"\b(reconstruct|construct).*(?:handoff|assignment)\b"],
    "result_interpretation": [r"\b(reconcile|synthesi[sz]e|partial|full .*verdict|over[- ]claim|result semantics|do not .*claim|consume .*evidence|conflict(?:ing)? .*result)\b"],
    "authority_boundary": [r"\b(authority|authoritative|not .*authority|does not certify|non-binding|hypothesis|evidence .*not)\b"],
    "finding_classification": [r"\b(instruction-violation|instruction-ambiguity|instruction-gap|execution-error|finding class|classif)\b"],
    "stop_escalation": [r"\b(blocked|blocker|stop|return .*caller|return .*parent|handoff|escalat|out[- ]of[- ]scope|cannot .*claim|do not .*represent|if .*requires?)\b"],
}

PROCEDURE_HEADINGS = re.compile(
    r"(?mi)^##+\s+(workflow|method|rules|check|implementation|planning|exploration|audit|verification|diagnostic|review focus|adversarial review depth|audit method|checkpoint method|specialist use|choose the .*stage|findings and escalation|review and verification|planning evidence|implementation workflow|invocation contract)\b"
)

RESULT_HEADING = re.compile(r"(?mi)^##\s+(?:Result|Final report)\s*$")

# Profile-specific core-loop capabilities. Each capability contains groups; every group
# must match somewhere in the role-local contract. These are profile semantics, not
# current-role phrases, so adding a new role cannot inherit a silent PASS.
CORE = {
    "implementation": {
        "derive_before_edit": [[r"before .*edit|before .*mutation|implementation proof"], [r"owner|primitive|owning|right level"], [r"preserv|negative|regression|case map|falsif"]],
        "final_self_check": [[r"final diff|final state|self[- ]review|pre[- ]return"], [r"verify|validation|test|check"]],
        "bounded_escalation": [[r"stop|return .*caller|escalat|out[- ]of[- ]scope"], [r"new .*decision|new .*protocol|cross[- ]layer|outside .*scope|boundary"]],
    },
    "debug_mutation": {
        "symptom_to_cause": [[r"exact symptom|failing .*test|traceback|reproduc|concrete evidence"], [r"trace .*code path|root operation|primitive|root cause"], [r"hypothesis|root cause"]],
        "cause_to_fix": [[r"owner|owning|shared owner|fix boundary|fix level"], [r"smallest .*fix|minimal .*fix|right[- ]level fix"], [r"rerun|re-run|focused failing case"]],
        "failed_hypothesis_reset": [[r"same .*failure|still fails|evidence contradict|rejected"], [r"reset|reassess|hypothesis"]],
    },
    "ops_mutation": {
        "observe_before_action": [[r"inspect .*current|current .*configuration|current .*state|read-only diagnostics"], [r"diagnos|symptom|logs?|status|runtime"]],
        "isolate_before_mutation": [[r"isolate|distinguish|determine .*cause|identify .*cause|failure .*layer|which .*layer|whether .*failure"], [r"before .*chang|before .*propos|diagnos|symptom|evidence"]],
        "authorized_reversible_action": [[r"authoriz|permission|gate"], [r"exact action|target|scope"], [r"reversible|rollback|restore"]],
        "postchange_proof": [[r"verify|verification"], [r"concrete commands?|exact commands?|actual .*result|post[- ]change|health"]],
    },
    "independent_review": {
        "bind_exact_target": [[r"exact .*state|candidate head|base sha|target .*state|ref/sha|stable implemented result"], [r"fresh|independent|read-only"]],
        "derive_attack_surface": [[r"review surface|affected .*boundary|changed .*behavior|proportionally to .*change|inspect"], [r"counterexample|adversarial|negative|preserv|regression|both sides"]],
        "bounded_judgment": [[r"evidence|checks? .*used|actual .*output"], [r"verdict|approve|request changes|changes required|pass with notes|advisory"], [r"blocked|insufficient|limit|cannot .*claim|not verified|stop|return"]],
    },
    "verification": {
        "bind_and_plan": [[r"state .*executed|head|candidate|workspace-only|target-unverified"], [r"derive .*checks|applicable verification set|whole assignment|affected behavior boundary"]],
        "discriminating_evidence": [[r"changed behavior"], [r"preserved|unaffected|regression"], [r"preconditions|qualifiers|negative control|could .*claim .*false|valid evidence"]],
        "classify_and_bound": [[r"code .*environment|environment.*code|setup|tooling"], [r"not run|skipped|unavailable|coverage|confidence"], [r"do not .*fix|never .*verified|never say .*verified"]],
    },
    "discovery": {
        "question_to_trace": [[r"find|identify|locate|search|trace|inspect"], [r"files?|symbols?|call paths?|callers?|references?|data flow|state flow|similar implementations?|patterns?"], [r"adjacent|related|nearby|tests?/docs?|boundar"]],
        "corroborate_not_infer": [[r"support|evidence|current code|tool output|exact file paths?|symbols?"], [r"do not guess|unknown|gap|not .*root cause|cannot establish"]],
        "negative_claim_scope": [[r"not found|unused|no caller|no implementation|negative .*claim"], [r"naming|alias|variant|references?|callers?|generated|config"], [r"searched scope|does not exist|not searched"]],
        "flow_edge_corroboration": [[r"call/data/state flow|call.*flow|data.*flow|state.*flow"], [r"actual edge|caller|reference|consumer|transition"], [r"similar names|nearby files|adjacency|infer"]],
        "bounded_handoff": [[r"bounded|scope|depth|quick|medium|thorough"], [r"handoff|right role|appropriate role|do not .*implement|do not .*verify"]],
    },
    "analysis_fallback": {
        "question_to_evidence": [[r"question|objective|scope|assignment"], [r"inspect|research|gather|read|search"], [r"evidence|source|support"]],
        "separate_known_unknown": [[r"fact|evidence|hypothesis|inference"], [r"unknown|gap|uncertain|cannot establish|do not guess"]],
        "bounded_handoff": [[r"scope|bounded|out[- ]of[- ]scope"], [r"handoff|return .*caller|specialist|route|stop"]],
    },
    "external_research": {
        "bind_external_target": [[r"external target|product|library|framework|api|protocol|upstream"], [r"version|range|branch|tag|platform|environment|applicability"], [r"bind|establish|identify"]],
        "source_and_applicability": [[r"official|normative|tagged upstream|upstream source|release|migration|maintainer|community"], [r"authority"], [r"version applicability|exact-version applicability|directness"]],
        "reconcile_conflicts": [[r"when sources conflict|if .*sources .*conflict|conflicting sources"], [r"reconcile .*authority.*applicability.*directness|compare .*authority.*applicability.*directness"], [r"do not vote"]],
        "bounded_external_result": [[r"answer .*first|answer the .* proposition first"], [r"provenance|source|link|ref"], [r"not .*project requirement|does not .*local root cause|does not .*implementation choice|does not .*candidate correctness"]],
    },
    "planning": {
        "inspect_before_plan": [[r"inspect|read"], [r"existing patterns?|shared abstractions?|current .*code|project .*constraints"]],
        "ownership_and_choices": [[r"owner|owning|fix level|smallest existing"], [r"alternative|tradeoff|decision|do not choose|authority"]],
        "execution_and_verification_plan": [[r"batch|package|sequence|ordered|dependencies?"], [r"validation|verification|regression|test"], [r"risk|unknown|decision|blocker"]],
    },
    "audit": {
        "scope_and_risk": [[r"scope|target|current .*state"], [r"highest-risk|risk|priority|primary user job|changed .*ui|audit"]],
        "evidence_and_counterexample": [[r"evidence|file paths?|symbols?|actual .*output"], [r"counterexample|negative|preserv|regression|confirm|reject"]],
        "coverage_and_stop": [[r"not covered|uncovered|coverage|limit|confidence"], [r"stop|blocked|insufficient|return .*caller|escalat|cannot .*claim"]],
    },
    "audit_orchestrator": {
        "scope_and_specialists": [[r"scope|target ref|target .*sha|fresh"], [r"specialist|@explore|@tester|@reviewer|delegate"]],
        "risk_and_evidence": [[r"highest-risk|high-risk|risk"], [r"evidence|confirmed|likely|hypothesis|confidence"]],
        "reconcile_specialists": [[r"reconcile|synthesi[sz]e"], [r"conflict|partial|missing .*coverage|cannot .*flatten|do not .*invent|coverage missing"]],
        "bounded_audit_result": [[r"not covered|coverage|uncovered"], [r"severity|critical|high|medium|low"], [r"overall status|result|report"]],
    },
    "orchestrator": {
        "normalize_and_route": [[r"normalize|intent|outcome|scope"], [r"route|choose .*role|specialist|stage"]],
        "clean_handoff": [[r"construct|reconstruct"], [r"handoff|assignment"], [r"outcome|constraint|evidence|target|state"], [r"omit|non-binding|do not forward|not blanket authority"]],
        "consume_without_overclaim": [[r"reconcile|consume|result"], [r"partial|full .*verdict|do not .*claim|over[- ]claim|stale|fresh"]],
    },
    "code_orchestrator": {
        "normalize_and_route": [[r"normalize|intent|outcome|scope"], [r"route|choose .*role|specialist|stage"]],
        "clean_handoff": [[r"construct|reconstruct"], [r"handoff|assignment"], [r"outcome|constraint|evidence|target|state"], [r"omit|non-binding|do not forward|not blanket authority"]],
        "consume_without_overclaim": [[r"reconcile|consume|result"], [r"partial|full .*verdict|do not .*claim|over[- ]claim|stale|fresh"]],
        "owner_synthesis": [[r"workflow-owner synthesis loop|bounded owner pass"], [r"ingest.*facts/evidence.*hypotheses.*recommendations|facts/evidence.*hypotheses.*recommendations"], [r"update the whole-task model"], [r"recommended next role.*not a workflow transition|recommended next role, stage, mechanism.*not a workflow transition"], [r"independent controller.*ordinary workflow-owner decision|ordinary workflow-owner decision.*independent controller"]],
        "owner_control_plane": [[r"bounded owner trajectory reassessment yourself"], [r"exact longitudinal question remains unresolved after the owner reassessment"], [r"owner reconciliation (?:performed|first)|perform owner reconciliation"], [r"do not .*semantic-checkpoint.*technical owner|technical owner.*fix level.*semantic-checkpoint|do .*not.*invoke the checkpoint merely because"]],
        "workflow_state_visibility": [[r"multi[- ]stage workflow|multi[- ]step workflow|longer multi[- ]stage workflow"], [r"workflow state rather than the tool stream|workflow state[^.\n]{0,180}(?:established|unresolved)"], [r"(?:meaningful stage|batched evidence result)[^.\n]{0,240}(?:establish|current state)"], [r"(?:stage/owner|next stage|next owner)[^.\n]{0,180}(?:comes next|why)|comes next and why"], [r"do not announce every tool call|batch nearby work|tool stream"]],
        "decision_context": [[r"factual/technical uncertainty|factual[^.\n]{0,80}technical uncertainty"], [r"implementation discretion"], [r"self-contained[^.\n]{0,200}(?:child sessions?|tool output)|has not seen child sessions"], [r"viable alternatives[^.\n]{0,180}(?:consequences|tradeoffs)|alternatives[^.\n]{0,120}consequences/tradeoffs"], [r"recommendation[^.\n]{0,140}evidence supports|evidence[^.\n]{0,120}support[^.\n]{0,80}recommend"]],
    },
    "semantic_gate": {
        "bind_and_classify": [[r"claim|proposition|candidate|target .*state"], [r"authority|evidence|authoritative"], [r"preserv|refin|strengthen|weaken|contradict|classif"]],
        "residual_authority_boundary": [[r"owner reconciliation performed"], [r"exact unresolved semantic proposition|exact semantic proposition whose authority remains unresolved"], [r"ordinary technical owner/fix-level/abstraction decisions are not a reason|technical ownership.*fix-level.*not by itself a semantic choice"], [r"why the workflow owner could not safely settle|why the owner cannot safely settle"]],
        "typed_state_axes": [[r"proceed.*hold.*insufficient-context|insufficient-context.*workflow verdict"], [r"evidence status|`unverified`.*evidence"], [r"proposition relation|`indeterminate`.*relation"], [r"workflow verdict[^.\n]{0,180}distinct from[^.\n]{0,180}`unverified` evidence status[^.\n]{0,180}`indeterminate` proposition relation"]],
        "boundary_not_recipe": [[r"mutation boundary|semantic boundary|proceed"], [r"non-binding|not .*recipe|does not certify|not .*implementation .*adequacy|mechanism .*hypothesis"]],
        "bounded_result": [[r"evidence|proof|confidence"], [r"stop|blocked|cannot .*proceed|return .*parent|escalat"], [r"result|verdict|handoff"]],
    },
    "trajectory_audit": {
        "recover_task_anchor": [[r"task anchor|user-authorized outcome|end-to-end acceptance"], [r"actual user|primary session|session history|primary evidence"], [r"parent.*report|packet.*not.*proof|summary.*not.*proof"]],
        "second_opinion_boundary": [[r"second opinion"], [r"owner reassessment performed"], [r"exact unresolved trajectory question"], [r"why available primary evidence could not safely resolve|could not safely resolve that question"], [r"does not .*serve as the first-line|workflow owner must first synthesize"]],
        "material_transition_chain": [[r"evidence.*interpretation|interpretation.*action|hypothesis.*action"], [r"scoped result|acceptance effect|end-to-end acceptance"], [r"material trajectory|material transitions"]],
        "progress_without_false_stall": [[r"acceptance progress"], [r"enabling progress"], [r"diagnostic progress"], [r"planned staged work|later milestone.*not expected|not global non-progress"], [r"independent defects?.*external outage|external outage.*independent defects?"]],
        "drift_and_cluster_test": [[r"hypothesis laundering|acceptance erosion|scoped evidence"], [r"independent.*clustered.*unverified|clustered.*independent"], [r"does not mean.*architecture|do not infer.*multiple fixes|not .*bad design"]],
        "bounded_next_transition": [[r"return exactly one workflow verdict"], [r"continue.*proposed next transition|proposed next transition.*continue"], [r"reanchor.*workflow framing|workflow framing.*reanchor"], [r"reassess.*cumulative evidence|cumulative evidence.*reassess"], [r"checkpoint-required.*semantic-checkpoint|semantic-checkpoint.*checkpoint-required"], [r"insufficient-evidence.*primary session evidence|primary session evidence.*insufficient-evidence"], [r"do not choose.*replacement|does not.*choose.*architecture|never chooses.*fix"]],
    },
    "evaluation": {
        "trace_contract": [[r"trace|session|assignment|handoff"], [r"standing .*contract|role .*contract|authority|scope"]],
        "workflow_owner_quality": [[r"workflow-owner synthesis|owner synthesis"], [r"specialist pass-through"], [r"controller dependence"], [r"independently determined the next required question/action|next required question/action before delegating"]],
        "classify_failure": [[r"instruction-violation|instruction-ambiguity|instruction-gap|execution-error|classif"], [r"evidence|exact .*message|tool .*output|trace"]],
        "bound_conclusion": [[r"coverage|not covered|limit|unknown"], [r"result|finding|report"], [r"stop|escalat|cannot .*claim|partial"]],
    },
}


# Capability severity distinguishes an inoperable role from an executable role with a
# material contract weakness. Missing essential capabilities block as FAIL. Missing
# material capabilities block promotion as REVIEW, but do not claim the role is unusable.
CORE_SEVERITY = {
    "implementation": {"derive_before_edit": "FAIL", "final_self_check": "FAIL", "bounded_escalation": "FAIL"},
    "debug_mutation": {"symptom_to_cause": "FAIL", "cause_to_fix": "FAIL", "failed_hypothesis_reset": "FAIL"},
    "ops_mutation": {"observe_before_action": "FAIL", "isolate_before_mutation": "FAIL", "authorized_reversible_action": "FAIL", "postchange_proof": "FAIL"},
    "independent_review": {"bind_exact_target": "FAIL", "derive_attack_surface": "FAIL", "bounded_judgment": "FAIL"},
    "verification": {"bind_and_plan": "FAIL", "discriminating_evidence": "FAIL", "classify_and_bound": "FAIL"},
    "discovery": {"question_to_trace": "FAIL", "corroborate_not_infer": "FAIL", "negative_claim_scope": "FAIL", "flow_edge_corroboration": "FAIL", "bounded_handoff": "FAIL"},
    "analysis_fallback": {"question_to_evidence": "FAIL", "separate_known_unknown": "FAIL", "bounded_handoff": "FAIL"},
    "external_research": {"bind_external_target": "FAIL", "source_and_applicability": "FAIL", "reconcile_conflicts": "FAIL", "bounded_external_result": "FAIL"},
    "planning": {"inspect_before_plan": "FAIL", "ownership_and_choices": "FAIL", "execution_and_verification_plan": "FAIL"},
    "audit": {"scope_and_risk": "FAIL", "evidence_and_counterexample": "FAIL", "coverage_and_stop": "FAIL"},
    "audit_orchestrator": {"scope_and_specialists": "FAIL", "risk_and_evidence": "FAIL", "reconcile_specialists": "REVIEW", "bounded_audit_result": "FAIL"},
    "orchestrator": {"normalize_and_route": "FAIL", "clean_handoff": "FAIL", "consume_without_overclaim": "FAIL"},
    "code_orchestrator": {"normalize_and_route": "FAIL", "clean_handoff": "FAIL", "consume_without_overclaim": "FAIL", "owner_synthesis": "FAIL", "owner_control_plane": "FAIL", "workflow_state_visibility": "REVIEW", "decision_context": "REVIEW"},
    "semantic_gate": {"bind_and_classify": "FAIL", "residual_authority_boundary": "FAIL", "typed_state_axes": "FAIL", "boundary_not_recipe": "FAIL", "bounded_result": "FAIL"},
    "trajectory_audit": {"recover_task_anchor": "FAIL", "second_opinion_boundary": "FAIL", "material_transition_chain": "FAIL", "progress_without_false_stall": "FAIL", "drift_and_cluster_test": "FAIL", "bounded_next_transition": "FAIL"},
    "evaluation": {"trace_contract": "FAIL", "workflow_owner_quality": "FAIL", "classify_failure": "FAIL", "bound_conclusion": "FAIL"},
}

# Characteristic false-success challenges. These are deliberately semantic rather than
# size/keyword quotas: a role must explain what it does when the first plausible path,
# apparent success, or upstream framing is misleading.
CHALLENGE = {
    "implementation": [[r"mechanism .*hypothesis|not .*recipe|do not .*work backward|requested patch shape"], [r"falsif|negative|preserv|regression|case map"]],
    "debug_mutation": [[r"first failing call site|root cause|hypothesis"], [r"reset|reassess|contradict|still fails|same failure"]],
    "ops_mutation": [[r"isolate|distinguish|which .*layer|whether .*failure|identify .*cause"], [r"before .*chang|before .*propos|read-only diagnos|evidence"]],
    "independent_review": [[r"counterexample|adversarial|negative|preserv|regression"], [r"not .*correctness|constraint .*not|prior .*verdict|fresh|independent"]],
    "verification": [[r"preserv|negative control|precondition|qualifier|could .*false"], [r"environment|setup|tooling|not .*verified|valid evidence"]],
    "discovery": [[r"references?|callers?|adjacent|similar implementation|data flow|state flow|searched scope"], [r"do not guess|unknown|cannot establish|not .*root cause|not searched"]],
    "analysis_fallback": [[r"fact|evidence|hypothesis|inference"], [r"unknown|gap|cannot establish|do not guess"]],
    "external_research": [[r"latest|another .*version|major/minor version|platform|fix released after|wrong .*version|applicability"], [r"conflict|do not vote|unresolved evidence gap|cannot be resolved"]],
    "planning": [[r"existing .*owner|ownership|alternative|tradeoff|decision"], [r"authority|do not choose|unresolved|hypothesis"]],
    "audit": [[r"evidence|confirm|reject|counterexample|negative|preserv|regression"], [r"coverage|not covered|confidence|cannot .*claim|insufficient"]],
    "audit_orchestrator": [[r"conflict|partial|missing .*coverage|reconcile|synthesi"], [r"do not .*invent|cannot .*flatten|coverage|confidence"]],
    "orchestrator": [[r"omit|non-binding|do not forward|not blanket authority|do not replace .*specialist|do not skip .*stage"], [r"partial|full .*verdict|stale|fresh|over[- ]claim|required .*cannot run|implementation is blocked|return .*parent|unresolved .*direction"]],
    "code_orchestrator": [[r"omit|non-binding|do not forward|not blanket authority|do not replace .*specialist|do not skip .*stage"], [r"partial|full .*verdict|stale|fresh|over[- ]claim|required .*cannot run|implementation is blocked|return .*parent|unresolved .*direction"], [r"recommended next role.*not a workflow transition|ordinary workflow-owner decision|owner trajectory reassessment"]],
    "semantic_gate": [[r"non-binding|not .*recipe|does not certify|not .*adequacy|hypothesis"], [r"authority|evidence|proposition|claim"], [r"owner reconciliation performed|ordinary technical .* not a reason|technical ownership.*not by itself"]],
    "trajectory_audit": [[r"local.*success|locally successful|correction epoch|global non-progress|end-to-end"], [r"planned staged|independent|different owners|not .*turn count|not .*multiple fixes|does not mean.*architecture"], [r"packet.*not.*proof|parent.*report.*not.*proof|primary session"], [r"second opinion|owner reassessment performed|exact unresolved trajectory question"]],
    "evaluation": [[r"instruction-violation|instruction-ambiguity|instruction-gap|execution-error|classif"], [r"evidence|trace|exact .*message|tool .*output"], [r"workflow-owner synthesis|specialist pass-through|controller dependence"]],
}

# Only foundational generic dimensions are hard on their own. Other missing dimensions
# are material REVIEW findings unless an essential profile core capability already makes
# them a FAIL. This prevents a useful role from being called non-executable because one
# secondary semantic is under-specified.
FOUNDATIONAL_DIMENSIONS = {"scope_input", "procedure", "result_semantics"}

PROFILE_MIN = {
    "implementation": (5, 2),
    "debug_mutation": (5, 2),
    "ops_mutation": (5, 3),
    "independent_review": (5, 2),
    "verification": (6, 2),
    "discovery": (4, 2),
    "analysis_fallback": (4, 2),
    "external_research": (6, 2),
    "planning": (5, 2),
    "audit": (5, 2),
    "audit_orchestrator": (6, 2),
    "orchestrator": (6, 3),
    "code_orchestrator": (6, 3),
    "semantic_gate": (6, 2),
    "trajectory_audit": (8, 3),
    "evaluation": (6, 2),
}

@dataclass
class RoleAudit:
    role: str
    profile: str
    status: str
    findings: list[str]
    review_reasons: list[str]
    dimensions_ok: list[str]
    core_ok: list[str]
    action_lines: int
    decision_lines: int
    sequence_signals: int
    nonblank_body: int
    body_chars: int


def split_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def section_map(text: str) -> dict[str, str]:
    out: dict[str, list[str]] = {"__preamble__": []}
    current = "__preamble__"
    for line in text.splitlines():
        m = re.match(r"^##+\s+(.+?)\s*$", line)
        if m:
            current = m.group(1).strip().lower()
            out.setdefault(current, [])
        else:
            out.setdefault(current, []).append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def body_without_frontmatter_and_shared(text: str) -> str:
    text = split_frontmatter(text)
    text = re.sub(r"(?ms)^## Shared contract\s+.*?(?=^## |\Z)", "", text)
    return text.strip()


def method_text(text: str) -> str:
    sections = section_map(text)
    parts = []
    for name, body in sections.items():
        if name in {"result", "final report", "shared contract"}:
            continue
        parts.append(("## " + name + "\n" if name != "__preamble__" else "") + body)
    return "\n".join(parts)


def result_text(text: str) -> str:
    sections = section_map(text)
    return sections.get("result", "") or sections.get("final report", "")


def count_operational_lines(method: str) -> int:
    count = 0
    for line in method.splitlines():
        s = re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", line).strip()
        if s and ACTION.search(s):
            count += 1
    return count


def count_decisions(method: str) -> int:
    count = 0
    for line in method.splitlines():
        s = line.strip()
        if s and CONDITIONAL.search(s) and ACTION.search(s):
            count += 1
    return count


def count_sequence_signals(method: str) -> int:
    return len(SEQUENCE.findall(method)) + len(NUMBERED.findall(method))


def dimension_present(method: str, result: str, name: str) -> bool:
    if name == "procedure":
        return bool(PROCEDURE_HEADINGS.search(method))
    if name == "result_semantics":
        return bool(result) and bool(re.search(r"\b(report|return|verdict|result|include|provide)\b", result, re.I))
    hay = result if name in {"bounded_verdict"} else method
    pats = DIM.get(name, [])
    return any(re.search(p, hay, re.I | re.M | re.S) for p in pats)


def capability_present(text: str, groups: list[list[str]]) -> bool:
    return all(any(re.search(p, text, re.I | re.M | re.S) for p in group) for group in groups)


def discover_routed_roles(agent_names: set[str]) -> dict[str, set[str]]:
    callers = [ROOT / "AGENTS.md", AGENT_DIR / "code-orchestrator.md", AGENT_DIR / "ui-orchestrator.md", AGENT_DIR / "auditor.md"]
    edges: dict[str, set[str]] = {}
    for path in callers:
        caller = "root" if path.name == "AGENTS.md" else path.stem
        text = path.read_text(encoding="utf-8")
        for role in sorted(set(re.findall(r"@([a-zA-Z0-9_-]+)", text))):
            if role in agent_names and role != caller:
                edges.setdefault(caller, set()).add(role)
    return edges


def audit_role(role: str, profile: str, text: str) -> RoleAudit:
    body = body_without_frontmatter_and_shared(text)
    method = method_text(body)
    result = result_text(body)
    reqs = SPEC["profiles"][profile]["critical"]
    missing_dims = [d for d in reqs if not dimension_present(method, result, d)]

    core_defs = CORE.get(profile, {})
    missing_core = [name for name, groups in core_defs.items() if not capability_present(body, groups)]
    core_ok = [name for name in core_defs if name not in missing_core]

    actions = count_operational_lines(method)
    decisions = count_decisions(method)
    seq = count_sequence_signals(method)
    min_actions, min_decisions = PROFILE_MIN.get(profile, (4, 2))

    findings: list[str] = []
    review: list[str] = []

    hard_dims = [d for d in missing_dims if d in FOUNDATIONAL_DIMENSIONS]
    soft_dims = [d for d in missing_dims if d not in FOUNDATIONAL_DIMENSIONS]
    if hard_dims:
        findings.append("missing foundational role-local dimensions: " + ", ".join(hard_dims))
    if soft_dims:
        review.append("material role-local dimensions need strengthening: " + ", ".join(soft_dims))

    sev = CORE_SEVERITY.get(profile, {})
    hard_core = [c for c in missing_core if sev.get(c, "FAIL") == "FAIL"]
    soft_core = [c for c in missing_core if sev.get(c, "FAIL") == "REVIEW"]
    if hard_core:
        findings.append("missing essential profile core-loop capabilities: " + ", ".join(hard_core))
    if soft_core:
        review.append("material profile capability under-specified: " + ", ".join(soft_core))

    if actions < min_actions:
        review.append(f"thin role-local operational procedure ({actions} action-bearing lines; profile reference >= {min_actions}); confirm the core loop is still executable")
    if decisions < min_decisions:
        review.append(f"thin conditional decision logic ({decisions} condition->action lines; profile reference >= {min_decisions}); confirm decisions are not implicit/underspecified")

    # Sequence is not a universal requirement; if core/action/decision evidence is strong,
    # a compact declarative decision procedure may still be executable. Missing sequencing
    # therefore asks for REVIEW only when the role is otherwise structurally adequate.
    if seq == 0 and not findings and profile not in {"audit", "discovery"}:
        review.append("no explicit sequence cue/numbered workflow; manually confirm that the decision procedure is executable rather than a descriptive checklist")

    # Adversarial/preservation challenge: what prevents the role from accepting the first
    # plausible path or apparent success? Missing this does not always make the basic role
    # unusable, but it blocks promotion because false-success handling is under-specified.
    challenge = CHALLENGE.get(profile)
    challenge_ok = True
    if challenge:
        challenge_ok = capability_present(body, challenge)
        if not challenge_ok:
            review.append("characteristic false-success/adversarial challenge is not explicit enough")

    nonblank = sum(bool(x.strip()) for x in body.splitlines())
    chars = len(body)
    status = "FAIL" if findings else ("REVIEW" if review else "PASS")
    return RoleAudit(
        role=role,
        profile=profile,
        status=status,
        findings=findings,
        review_reasons=review,
        dimensions_ok=[d for d in reqs if d not in missing_dims],
        core_ok=core_ok,
        action_lines=actions,
        decision_lines=decisions,
        sequence_signals=seq,
        nonblank_body=nonblank,
        body_chars=chars,
    )


def protocol_findings(role_texts: dict[str, str], edges: dict[str, set[str]]) -> list[str]:
    findings: list[str] = []
    mutation_roles = ["build", "debugger", "ui-implementer", "devops"]
    mutation_guard_patterns = {
        "build": [r"not .*implementation recipe", r"requested patch shape|mechanism .*hypothesis|non-required mechanism"],
        "debugger": [r"proposed remediation|patch shape", r"hypothesis"],
        "ui-implementer": [r"plan .*context|audit/plan .*context", r"non-required .*hypoth"],
        "devops": [r"diagnos.*before|default to read-only diagnostics", r"authoriz|permission|gate"],
    }
    for role in mutation_roles:
        if role not in role_texts or not any(role in targets for targets in edges.values()):
            continue
        text = role_texts[role]
        if not all(re.search(p, text, re.I | re.S) for p in mutation_guard_patterns[role]):
            findings.append(f"PROTOCOL {role}: mutation consumer lacks a complete upstream-recommendation / authorization guard")

    for orch in ["code-orchestrator", "ui-orchestrator"]:
        text = role_texts.get(orch, "")
        if not (re.search(r"construct|reconstruct", text, re.I) and re.search(r"handoff|assignment", text, re.I) and re.search(r"omit|non-binding|do not forward|not blanket authority", text, re.I)):
            findings.append(f"PROTOCOL {orch}: no clear mutation-handoff reconstruction/filter contract")

    for producer in ["semantic-checkpoint", "project-planner", "ui-planner", "ui-auditor"]:
        text = role_texts.get(producer, "")
        if text and re.search(r"pass(?:ed)? unchanged|implementation (?:is )?adequate|correct implementation mechanism", text, re.I):
            findings.append(f"PROTOCOL {producer}: producer language can certify/forward an implementation mechanism instead of preserving decision ownership")

    reviewer = role_texts.get("reviewer", "")
    if reviewer and not (re.search(r"exact .*candidate|candidate head|target state", reviewer, re.I) and re.search(r"prior .*verdict|expected .*verdict|fresh", reviewer, re.I)):
        findings.append("PROTOCOL reviewer: fresh independent review context/state isolation is not explicit enough")
    if reviewer and not (
        re.search(r"parent-derived(?: or prior-task)? investigative direction|investigative path", reviewer, re.I)
        and re.search(r"actually present in .*model-visible context|model-visible context", reviewer, re.I)
        and re.search(r"does .*not.*by itself contaminate|not .*contaminate.*merely.*available", reviewer, re.I | re.S)
        and re.search(r"automatic context injection|intentional retrieval", reviewer, re.I)
        and re.search(r"contaminated|contamination", reviewer, re.I)
        and re.search(r"clean assignment|clean .*invocation boundary", reviewer, re.I)
        and re.search(r"locator, not proof", reviewer, re.I)
    ):
        findings.append("PROTOCOL reviewer: fresh whole-change isolation does not distinguish available capability from actually exposed investigative steering or does not preserve authority provenance")
    if reviewer and not (
        re.search(r"managed ocr .*independent evidence.*not a substitute for host-review coverage|managed ocr .*not .*substitute .*host", reviewer, re.I | re.S)
        and re.search(r"host-owned ledger|host .*ledger", reviewer, re.I)
        and re.search(r"does not become host-reviewed|never add .*ocr-selected .*host coverage", reviewer, re.I)
        and re.search(r"absence of ocr comments .*not evidence of correctness|zero[- ]finding .*not", reviewer, re.I)
    ):
        findings.append("PROTOCOL reviewer: managed-review evidence can substitute for independent host coverage/judgment")

    return findings


def profile_inventory_findings(agent_names: set[str], role_profiles: dict[str, str]) -> list[str]:
    findings: list[str] = []
    missing_profiles = sorted(agent_names - set(role_profiles))
    stale_profiles = sorted(set(role_profiles) - agent_names)
    if missing_profiles:
        findings.append("UNCLASSIFIED roles without audit profile: " + ", ".join(missing_profiles))
    if stale_profiles:
        findings.append("STALE role-profile entries: " + ", ".join(stale_profiles))
    return findings


def main() -> int:
    agent_names = {p.stem for p in AGENT_DIR.glob("*.md")}
    role_profiles = SPEC["role_profiles"]
    hard_findings: list[str] = []

    hard_findings.extend(profile_inventory_findings(agent_names, role_profiles))

    edges = discover_routed_roles(agent_names)
    routed = set().union(*edges.values()) if edges else set()
    for role in sorted(routed):
        if role not in role_profiles:
            hard_findings.append(f"ROUTING {role}: routed substantive role has no role-contract profile")

    role_texts: dict[str, str] = {}
    audits: list[RoleAudit] = []
    for role in sorted(agent_names):
        raw = (AGENT_DIR / f"{role}.md").read_text(encoding="utf-8")
        role_texts[role] = body_without_frontmatter_and_shared(raw)
        profile = role_profiles.get(role)
        if profile:
            audits.append(audit_role(role, profile, raw))

    proto = protocol_findings(role_texts, edges)
    hard_findings.extend(proto)

    print("CONTRACT / PROTOCOL AUDIT v3")
    print("Discovered delegation edges:")
    for caller in sorted(edges):
        print(f"  {caller} -> {', '.join(sorted(edges[caller]))}")
    print("\nRole executability matrix:")
    for a in audits:
        print(
            f"  {a.status:6} {a.role:20} [{a.profile}] "
            f"body={a.nonblank_body}nl/{a.body_chars}c actions={a.action_lines} decisions={a.decision_lines} seq={a.sequence_signals}"
        )
        for f in a.findings:
            print(f"         FAIL: {f}")
        for r in a.review_reasons:
            print(f"       REVIEW: {r}")
        if a.status == "PASS":
            print(f"         core: {', '.join(a.core_ok) if a.core_ok else 'n/a'}")

    failed_roles = [a for a in audits if a.status == "FAIL"]
    review_roles = [a for a in audits if a.status == "REVIEW"]
    print()
    if hard_findings:
        print("Protocol/classification findings:")
        for item in hard_findings:
            print("  -", item)
    print(
        f"SUMMARY: roles FAIL={len(failed_roles)} REVIEW={len(review_roles)} PASS={len(audits)-len(failed_roles)-len(review_roles)}; "
        f"protocol/classification findings={len(hard_findings)}"
    )

    if failed_roles or review_roles or hard_findings:
        print("\nFAIL: promotion blocked. REVIEW is intentionally release-blocking until semantic adjudication documents why the compact contract is executable or the role is strengthened.")
        print("Prompt length is diagnostic only; no byte/line threshold can independently create FAIL or PASS.")
        return 1
    print("\nPASS: no unresolved role-executability or protocol-composition findings.")
    print("This PASS remains only a prerequisite; isolated behavioral replay is still required.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
