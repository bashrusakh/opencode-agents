#!/usr/bin/env python3
"""Synthetic self-tests for contract/protocol audit v3.

The fixtures deliberately avoid current-pack wording. They test properties:
- keyword stuffing cannot satisfy role executability;
- a compact but genuinely executable role can pass (no size quota);
- a mutation role without its characteristic diagnostic core loop fails;
- an executable audit-orchestrator with missing reconciliation is REVIEW, not FAIL;
- producer-side recipe contamination is rejected;
- semantic role-contract shape is enforced by function, not by five matching headings.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
MOD_PATH = HERE / "contract-protocol-audit.py"
spec = importlib.util.spec_from_file_location("contract_protocol_audit", MOD_PATH)
mod = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)

failures=[]
def check(cond, msg):
    if not cond:
        failures.append(msg)

def audit(role, profile, text):
    return mod.audit_role(role, profile, text)

keyword_stuff = """
## Role
Scope evidence ownership preserved regression unknown verification stop escalation result.
## Rules
- Check scope.
- Verify evidence.
- Report result.
## Result
Return evidence, unknowns, and verification.
"""
a = audit("fake-build", "implementation", keyword_stuff)
check(a.status == "FAIL", "keyword-stuffed implementation role was not rejected")
check(any("core-loop" in f or "operational" in f or "decision" in f for f in a.findings),
      "keyword-stuffed role did not fail for executable-method reasons")

thin_ops = """
## Role
Diagnose and operate the assigned service safely.
## Rules
- Inspect current configuration.
- Apply authorized changes only.
- Verify the result.
- Provide rollback.
## Result
Return diagnosis, commands, verification and rollback.
"""
a = audit("fake-devops", "ops_mutation", thin_ops)
check(a.status == "FAIL", "thin ops role without diagnostic isolation was not rejected")
check(any("isolate_before_mutation" in f for f in a.findings),
      "ops role did not fail on missing diagnostic isolation core loop")


# Heading-perfect shell: the preferred semantic shape is not a five-heading template.
# Matching labels cannot compensate for a missing executable method/core loop.
heading_shell = """
## Role
Own implementation work.
## Invocation contract
Receive scope and evidence.
## Method
Implement the change.
## Boundaries
Stop when blocked.
## Result
Return the result.
"""
a = audit("fake-heading-shell", "implementation", heading_shell)
check(a.status == "FAIL", "five-heading shell without executable implementation method was not rejected")

# Compact discovery role: intentionally short, but it contains an actual search/trace
# method, decision rules, evidence discipline, bounded stop/handoff and result contract.
compact_discovery = """
## Role
Answer the bounded repository-discovery question without editing anything.
## Exploration method
- Start from the assigned target/ref and locate the named files, symbols or entry points.
- Search references and trace callers/callees plus relevant data/state flow; inspect adjacent tests/docs or a similar implementation when they can corroborate the claim.
- For material negative claims such as not found/unused/no caller, check naming or alias variants, references/callers and applicable generated/config surfaces; report not found within the searched scope and never turn not searched into does not exist.
- Corroborate call/data/state flow through an actual caller/reference/consumer/transition edge rather than similar names or nearby files.
- If a ref/SHA governs the question, bind claims to that exact state before reporting them.
- If evidence does not establish a detail, mark it unknown and do not guess a root cause.
- When the answer is supported, stop; if the task becomes implementation/review/verification, return the evidence and hand off to the owning role.
## Result
Return exact paths/symbols, supported findings, relevant call/data-flow links, unknowns, and the next role when needed.
"""
a = audit("fake-explore", "discovery", compact_discovery)
check(a.status == "PASS", f"compact executable discovery role should PASS without five standardized headings: {a.status} {a.findings} {a.review_reasons}")
check(not a.findings and not a.review_reasons, f"compact discovery role has unexpected findings: {a.findings} {a.review_reasons}")

thin_discovery = """
## Role
Search the requested symbol and report what you find.
## Method
Use grep on the named source directory. If there is no exact match, report that it is unused. Infer data flow from nearby similarly named files.
## Result
Return paths and findings.
"""
a = audit("fake-thin-explore", "discovery", thin_discovery)
check(a.status == "FAIL", "discovery role with absolute negative claims and adjacency-only flow inference was not rejected")

complete_ops = """
## Role
Operate only the delegated runtime target and authorized action scope.
## Diagnostic workflow
1. Start from the observed symptom and inspect the current service status, logs, runtime configuration, ports and permissions before changing anything.
2. If multiple layers can explain the symptom, isolate whether the failure is service, configuration, network, permission or application-owned and return a handoff when application code owns it.
3. Before a state-changing action, confirm authorization for the exact target, action and scope; otherwise stop and report the blocker.
4. Apply the smallest reversible operational change and record rollback/restore steps.
5. After the change, verify the intended postcondition with concrete status/health commands and roll back or report the unresolved failure if verification does not support success.
## Result
Return target, observed evidence, diagnosis, authorized change, exact commands/results, verification, rollback, blockers and handoff when needed.
"""
a = audit("fake-devops-good", "ops_mutation", complete_ops)
check(not a.findings, f"complete synthetic ops contract falsely hard-failed: {a.findings}")


# External technical research is not generic lookup: it must bind applicability,
# challenge a plausible-but-wrong version/source, reconcile conflict, and return
# provenance without converting external evidence into project authority.
complete_external = """
## Role
Own a bounded external library/API proposition and remain read-only; do not decide the project implementation or local root cause.
## Invocation contract
Receive the external target and question. Bind the product/library/API plus material version/range, branch/tag, platform or environment; if applicability cannot be established, report the gap instead of answering for latest.
## Research method
1. Establish the exact target/version and split the question into checkable claims.
2. Search official version-specific documentation, tagged upstream source/tests, release or migration notes, maintainer issues/PRs, then community evidence as needed.
3. Choose sources by authority, exact-version applicability and directness, preserving source provenance/links.
4. If the first answer is from latest docs, another major/minor version or another platform, challenge its applicability before using it.
5. When sources conflict, reconcile by authority, version applicability and directness; do not vote. If they cannot be resolved, preserve an unresolved evidence gap.
6. Distinguish direct evidence, inference and community workaround. External best practice is not project authority and an upstream issue is not the local root cause.
7. Stop when the bounded proposition is supported, disproved or unresolved; return repository tracing/planning/review needs to the caller.
## Result
Answer the proposition first, cite the strongest applicable source/provenance, report only material version/freshness/conflict limitations, and do not claim a project requirement, local root cause, implementation choice or candidate correctness.
"""
a = audit("fake-librarian-good", "external_research", complete_external)
check(a.status == "PASS", f"complete external-research contract should PASS: {a.status} {a.findings} {a.review_reasons}")

thin_external = """
## Role
Research external library documentation and provide evidence.
## Method
- Search official documentation.
- Return the best answer and source.
## Result
Return the result with evidence.
"""
a = audit("fake-librarian-thin", "external_research", thin_external)
check(a.status == "FAIL", "thin external research role without version/conflict applicability loop was not rejected")
check(any("core-loop" in f or "external" in f for f in a.findings),
      "thin external research role did not fail for its characteristic core loop")

# Orchestrator communication is semantic, not a verbosity quota: long workflows expose
# meaningful workflow state, while user decisions are self-contained and evidence-first.
complete_orchestrator = """
## Role
Act as the accountable workflow owner for a bounded multi-stage coding outcome: own scope, routing, whole-task state and user-visible workflow state without implementing repository changes.
## Workflow-owner synthesis loop
1. Normalize the requested outcome/scope and choose the next specialist/stage.
2. If a required owner cannot run, stop blocked and return the next safe handoff instead of substituting yourself.
3. Construct each assignment from the established outcome, constraints, evidence, exact target/state, and stop boundary; omit non-binding mechanism proposals.
4. After a material specialist result, perform one bounded owner pass: ingest facts/evidence, hypotheses, recommendations and unresolved questions; reconcile them with the task anchor/current state/other evidence; update the whole-task model; decide the exact next question/action; then delegate. A specialist's recommended next role, stage, mechanism or remediation is input, not a workflow transition. Do not invoke an independent controller merely to avoid an ordinary workflow-owner decision.
5. When repeated corrections or same-policy counterexamples materially challenge the model, perform bounded owner trajectory reassessment yourself. If one evidence-backed model remains, continue normally. Invoke trajectory-auditor only when an exact longitudinal question remains unresolved after the owner reassessment; pass owner reassessment performed, current owner model, why available primary evidence could not safely resolve it, and the residual question.
6. For semantic authority, perform owner reconciliation first. Invoke semantic-checkpoint only when an exact semantic proposition remains unresolved or policy requires independence; do not invoke it merely because technical owner/fix level/abstraction/scope changes under settled behavior. Pass owner reconciliation performed and why the owner cannot safely settle the authority relation.
7. On a multi-stage workflow, when a meaningful stage establishes new current workflow state, report to the user what is established/unresolved and which next stage or owner comes next and why; batch tool calls and specialist invocations instead of narrating the tool stream.
8. Reconcile every returned result with current state before consuming it; if a verdict is partial or stale, preserve that boundary and do not over-claim completion.
9. Before asking the user to resolve a material choice, resolve factual/technical uncertainty with read-only evidence and keep implementation discretion with its owner.
10. If a user-owned choice remains, ask a self-contained question for someone who has not seen child sessions or tool output: explain the affected surface, viable alternatives and consequences/tradeoffs, and give a recommendation when evidence supports one before the exact question.
## Result
Return the consolidated workflow result, current target/state, material specialist evidence, blockers/unresolved choices, and next safe action only when one remains.
"""
a = audit("fake-orchestrator-good", "code_orchestrator", complete_orchestrator)
check(a.status == "PASS", f"complete orchestrator communication contract should PASS: {a.status} {a.findings} {a.review_reasons}")

quiet_orchestrator = complete_orchestrator.replace(
    "7. On a multi-stage workflow, when a meaningful stage establishes new current workflow state, report to the user what is established/unresolved and which next stage or owner comes next and why; batch tool calls and specialist invocations instead of narrating the tool stream.\n",
    "7. Continue to the next stage after each specialist returns.\n",
)
a = audit("fake-orchestrator-quiet", "code_orchestrator", quiet_orchestrator)
check(a.status == "REVIEW", f"orchestrator lacking workflow-state visibility should REVIEW: {a.status} {a.findings} {a.review_reasons}")
check(any("workflow_state_visibility" in r for r in a.review_reasons), "quiet orchestrator did not surface workflow-state visibility gap")

opaque_question_orchestrator = complete_orchestrator.replace(
    "9. Before asking the user to resolve a material choice, resolve factual/technical uncertainty with read-only evidence and keep implementation discretion with its owner.\n10. If a user-owned choice remains, ask a self-contained question for someone who has not seen child sessions or tool output: explain the affected surface, viable alternatives and consequences/tradeoffs, and give a recommendation when evidence supports one before the exact question.\n",
    "9. If a specialist reports a material choice, ask the user which option they want.\n",
)
a = audit("fake-orchestrator-opaque-question", "code_orchestrator", opaque_question_orchestrator)
check(a.status == "REVIEW", f"orchestrator with hidden-context user question should REVIEW: {a.status} {a.findings} {a.review_reasons}")
check(any("decision_context" in r for r in a.review_reasons), "opaque-question orchestrator did not surface decision-context gap")

pass_through_orchestrator = complete_orchestrator.replace(
    "A specialist's recommended next role, stage, mechanism or remediation is input, not a workflow transition.",
    "A specialist's recommended next stage may be accepted as the workflow transition without separate parent synthesis when the specialist is credible.",
)
a = audit("fake-orchestrator-pass-through", "code_orchestrator", pass_through_orchestrator)
check(a.status == "FAIL", f"orchestrator allowing specialist pass-through should FAIL: {a.status} {a.findings} {a.review_reasons}")
check(any("owner_synthesis" in f for f in a.findings), "pass-through orchestrator did not fail owner_synthesis")

controller_first_orchestrator = complete_orchestrator.replace(
    "When repeated corrections or same-policy counterexamples materially challenge the model, perform bounded owner trajectory reassessment yourself. If one evidence-backed model remains, continue normally. Invoke trajectory-auditor only when an exact longitudinal question remains unresolved after the owner reassessment; pass owner reassessment performed, current owner model, why available primary evidence could not safely resolve it, and the residual question.",
    "When cumulative history raises a material question, prefer trajectory-auditor over performing your own reassessment.",
)
a = audit("fake-orchestrator-controller-first", "code_orchestrator", controller_first_orchestrator)
check(a.status == "FAIL", f"controller-first orchestrator should FAIL: {a.status} {a.findings} {a.review_reasons}")
check(any("owner_control_plane" in f for f in a.findings), "controller-first orchestrator did not fail owner_control_plane")

# Executable audit orchestrator with good scope/risk/evidence/result semantics but no
# explicit conflict reconciliation is usable yet materially incomplete: REVIEW, not FAIL.
partial_auditor = """
## Role
Audit the assigned target by delegating evidence collection to appropriate specialists.
## Audit method
1. Bind the target ref/SHA and audit scope before delegating.
2. Choose @explore, @tester or @reviewer based on the highest-risk dimensions and gather evidence from each.
3. Classify each supported finding by confidence and severity; do not invent missing coverage.
4. If evidence is insufficient for a dimension, mark that coverage missing and stop short of a stronger claim.
## Result
Return overall status, findings with evidence/severity/confidence, specialist coverage, and uncovered areas.
"""
a = audit("fake-auditor", "audit_orchestrator", partial_auditor)
check(a.status == "REVIEW", f"audit orchestrator missing only reconciliation should REVIEW, not FAIL: {a.status} {a.findings} {a.review_reasons}")
check(any("reconcile_specialists" in r for r in a.review_reasons),
      "audit orchestrator did not surface missing reconciliation as REVIEW")


# Role topology/profile inventory is closed-world: adding a new routed/pack-owned role
# without requalification/profile is a release failure, and stale profiles also fail.
inv = mod.profile_inventory_findings({"alpha", "beta"}, {"alpha": "discovery"})
check(any("UNCLASSIFIED roles" in f and "beta" in f for f in inv),
      "new role without executable-contract audit profile did not block release")
inv = mod.profile_inventory_findings({"alpha"}, {"alpha": "discovery", "retired": "planning"})
check(any("STALE role-profile" in f and "retired" in f for f in inv),
      "stale role profile did not block release")

role_texts = {
    "semantic-checkpoint": "## Result\nImplementation mechanism H is adequate and may be passed unchanged.",
    "build": "It is not an implementation recipe. A non-required mechanism remains a hypothesis. Do not start from the requested patch shape and work backward.",
    "debugger": "Treat proposed remediation or patch shape as a hypothesis and diagnose the root cause.",
    "ui-implementer": "A supplied audit/plan is context, not blanket authority; non-required recommendations remain hypotheses.",
    "devops": "Default to read-only diagnostics before state-changing work. Require authorization for the exact action.",
    "code-orchestrator": "Construct the handoff from outcome and evidence; omit non-binding mechanisms.",
    "ui-orchestrator": "Construct the implementation handoff; do not forward plan recommendations as blanket authority.",
    "reviewer": "Use a fresh independent review bound to the exact Candidate target state; omit prior verdict framing."
}
findings = mod.protocol_findings(role_texts, {"code-orchestrator":{"build","debugger","devops"}})
check(any("semantic-checkpoint" in f for f in findings),
      "protocol audit failed to reject producer-side implementation certification")

clean = dict(role_texts)
clean["semantic-checkpoint"] = "## Result\nAuthorize only the semantic mutation boundary; a proposed mechanism remains non-binding and is not certified as implementation adequacy."
clean_findings = mod.protocol_findings(clean, {"code-orchestrator":{"build","debugger","devops"}})
check(not any("semantic-checkpoint" in f for f in clean_findings),
      "protocol audit falsely rejected clean semantic-boundary handoff")

reviewer_good = """
Use a fresh independent review bound to the exact Candidate target state; omit prior verdict framing.
Managed OCR is independent evidence, not a substitute for host-review coverage. Maintain a host-owned ledger across the authoritative changed/effective-diff set; an OCR-selected entry does not become host-reviewed. Absence of OCR comments is not evidence of correctness. In the result, never add OCR-selected entries to host coverage.
"""
reviewer_bad = """
Use a fresh independent review bound to the exact Candidate target state; omit prior verdict framing.
Run managed OCR. Review only files OCR excludes, then combine OCR-selected files with those host-inspected files and report full PR coverage. Validate any OCR comments before returning the verdict.
"""
findings = mod.protocol_findings({"reviewer": reviewer_good}, {})
check(not any("managed-review evidence" in f for f in findings),
      "protocol audit falsely rejected independent host/OCR coverage separation")
findings = mod.protocol_findings({"reviewer": reviewer_bad}, {})
check(any("managed-review evidence" in f for f in findings),
      "protocol audit failed to reject OCR+host complement coverage laundering")

if failures:
    print("CONTRACT / PROTOCOL SELFTEST v3: FAIL")
    for f in failures:
        print(" -", f)
    raise SystemExit(1)
print("CONTRACT / PROTOCOL SELFTEST v3: PASS")
