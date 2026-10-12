#!/usr/bin/env python3
"""Static release guards for known cross-layer policy regressions.

These checks verify package structure/ownership/schema properties only. They do not
establish semantic correctness and do not replace fresh isolated transition replay.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
failures = []

def check(cond, msg):
    if not cond:
        failures.append(msg)

def text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

# OpenCode V2 frontmatter generation: one schema across all pack-owned agents.
agents = sorted((ROOT / "agents").glob("*.md"))
check(len(agents) == 18, f"expected 18 agents, found {len(agents)}")
for path in agents:
    raw = path.read_text(encoding="utf-8")
    end = raw.find("\n---\n", 4)
    fm = raw[4:end] if raw.startswith("---\n") and end != -1 else ""
    check(bool(re.search(r"(?m)^permissions:\s*$", fm)), f"{path.name}: missing V2 permissions")
    check(not bool(re.search(r"(?m)^permission:\s*$", fm)), f"{path.name}: legacy V1 permission field")
    check(not bool(re.search(r"(?m)^\s*-\s*action:\s*(task|bash)\s*$", fm)), f"{path.name}: legacy V1 action name")
    for effect in re.findall(r"(?m)^\s*effect:\s*(\S+)\s*$", fm):
        check(effect in {"allow", "deny", "ask"}, f"{path.name}: invalid permission effect {effect}")

# Blocker evidence must not become replacement authority.
# Check each active owner/consumer independently: documentation parity must never
# satisfy an assertion about an active runtime surface.
root_sem = text("AGENTS.md")
manual_sem = text("docs/semantic-design-manual.md")
checkpoint_sem = text("agents/semantic-checkpoint.md")
evaluator_sem = text("agents/session-evaluator.md")
code_orchestrator_sem = text("agents/code-orchestrator.md")
semantic_runtime = "\n".join([root_sem, checkpoint_sem, evaluator_sem])

# Release identity must stay consistent across canonical/root and overview surfaces.
version_match = re.search(r"\*\*Pack version: ([^*]+)\*\*", root_sem)
check(version_match is not None, "AGENTS.md: pack version marker missing")
if version_match:
    pack_version = version_match.group(1).strip()
    readme_sem = text("README.md")
    changelog_sem = text("CHANGELOG.md")
    check(
        f"# OpenCode Agent Pack {pack_version}" in readme_sem
        and f"**OpenCode Agent Pack {pack_version}**" in readme_sem,
        "README.md: header/footer version drift from AGENTS.md",
    )
    check(
        changelog_sem.startswith(f"# Changelog\n\n## {pack_version}"),
        "CHANGELOG.md: current release heading drift from AGENTS.md",
    )
    release_slug = pack_version.replace(" beta", "-beta").replace(".", ".")
    current_release_link = f"docs/releases/{release_slug}.md"
    check(
        current_release_link in readme_sem,
        "README.md: current release-notes link drift from AGENTS.md",
    )
    check(
        (ROOT / f"docs/releases/{release_slug}.md").is_file(),
        "docs/releases: current release-notes file missing",
    )

# README delegated-specialist inventory must reflect the actual closed-world topology,
# not just agent mode. Any role that is the target of a direct or conditional delegation
# edge belongs in the inventory, including mode: all roles that can also be top-level.
edge_inventory_sem = text("evals/role-handoff-audit.py")
delegated_targets = {
    target
    for _, target, kind in re.findall(
        r"\('([^']+)'\s*,\s*'([^']+)'\)\s*:\s*'(delegation|conditional_delegate)'",
        edge_inventory_sem,
    )
}
delegated_section = re.search(
    r"(?ms)^## Delegated specialists\s*(.*?)(?=^---\s*$|^## )",
    readme_sem,
)
check(delegated_section is not None, "README.md: Delegated specialists section missing")
if delegated_section:
    documented_targets = set(re.findall(r"(?m)^\|\s*`([^`]+)`\s*\|", delegated_section.group(1)))
    check(
        documented_targets == delegated_targets,
        "README.md: delegated-specialist inventory drift from classified delegation topology "
        f"(missing={sorted(delegated_targets - documented_targets)}, stale={sorted(documented_targets - delegated_targets)})",
    )
# The workflow owner must expose semantic progress without becoming a tool logger,
# and must translate hidden specialist context into a decision-complete user question.
check(
    "workflow state rather than the tool stream" in code_orchestrator_sem
    and "what is now established or still unresolved" in code_orchestrator_sem
    and "which stage/owner comes next and why" in code_orchestrator_sem
    and "short single-stage workflow may go directly from Startup to Final" in code_orchestrator_sem,
    "code-orchestrator: workflow-milestone communication guard missing",
)
check(
    "factual/technical uncertainty" in code_orchestrator_sem
    and "self-contained for someone who has not seen child sessions or tool output" in code_orchestrator_sem
    and "viable alternatives and their material consequences/tradeoffs" in code_orchestrator_sem
    and "recommendation when the evidence supports one" in code_orchestrator_sem,
    "code-orchestrator: decision-context completeness guard missing",
)

for bad in [
    "requires separate authority or evidence of an established blocker",
    "require separate authority for the substitution or evidence of an established blocker",
    "without an established blocker or separate authority accepting the reduction",
]:
    check(bad.lower() not in semantic_runtime.lower(), f"blocker-as-authority wording returned in active runtime: {bad}")
check(
    "does not itself authorize a materially different replacement" in root_sem,
    "AGENTS.md: canonical blocker/replacement guard missing",
)
check(
    "does not itself authorize a materially different replacement" in manual_sem,
    "semantic-design-manual: blocker/replacement parity missing",
)
check(
    "a blocker may invalidate the original path but does not itself establish the replacement" in checkpoint_sem,
    "semantic-checkpoint: blocker/replacement enforcement missing",
)
check(
    "a blocker may establish non-viability of the original path but does not itself authorize the replacement" in evaluator_sem,
    "session-evaluator: blocker/replacement diagnostic guard missing",
)



# Delegated task text specializes the selected role; it must not rewrite role-owned
# obligations or allow a partial diagnostic to masquerade as a complete stage verdict.
check(
    "An assignment specializes the selected role contract; it does not replace it" in root_sem
    and "must remain explicitly partial" in root_sem
    and "cannot satisfy a broader stage" in root_sem,
    "AGENTS.md: assignment/role-contract composition guard missing",
)
check(
    "selected role's standing contract" in evaluator_sem
    and "partial result was not later consumed as completion of a broader stage" in evaluator_sem,
    "session-evaluator: assignment/role-contract diagnostic guard missing",
)
check(
    "it is an implementation constraint, not evidence of candidate adequacy/correctness" in root_sem
    and "collateral degradation/tradeoffs that were not separately established" in root_sem,
    "AGENTS.md: implementation-constraint/correctness boundary missing",
)
check(
    "selected only by the role/authority that owns that implementation/design choice" in root_sem
    and "other roles may propose mechanisms only as non-binding hypotheses" in root_sem,
    "AGENTS.md: implementation-mechanism ownership boundary missing",
)
check(
    "freshness also requires **judgment-context isolation**" in root_sem
    and "task-contract propositions with provenance/qualifiers" in root_sem
    and "material implementation constraints" in root_sem
    and "Do not frame a candidate mechanism as accepted/correct design" in root_sem
    and "Do not seed the child with prior verdicts" in root_sem
    and "targeted re-review" in root_sem
    and "partial/incremental" in root_sem,
    "AGENTS.md: independent-judgment context-isolation guard missing",
)
check(
    "check judgment-context isolation" in evaluator_sem
    and "must not pre-anchor the fresh child with prior verdicts" in evaluator_sem
    and "targeted re-review" in evaluator_sem
    and "fresh whole-scope judgment" in evaluator_sem,
    "session-evaluator: independent-judgment contamination diagnostic guard missing",
)

# Required skill dependencies must be reachable through the effective V2 permission rules.
def frontmatter(rel):
    raw = text(rel)
    end = raw.find("\n---\n", 4)
    return raw[4:end] if raw.startswith("---\n") and end != -1 else ""

def permission_rules(rel):
    rules = []
    current = None
    for line in frontmatter(rel).splitlines():
        m = re.match(r"\s*-\s*action:\s*(.+?)\s*$", line)
        if m:
            if current and {"action", "resource", "effect"} <= current.keys():
                rules.append(current)
            current = {"action": m.group(1).strip().strip('"\'')}
            continue
        if current is None:
            continue
        m = re.match(r"\s*resource:\s*(.+?)\s*$", line)
        if m:
            current["resource"] = m.group(1).strip().strip('"\'')
            continue
        m = re.match(r"\s*effect:\s*(.+?)\s*$", line)
        if m:
            current["effect"] = m.group(1).strip().strip('"\'')
    if current and {"action", "resource", "effect"} <= current.keys():
        rules.append(current)
    return rules

def glob_match(pattern, value):
    # V2 permission resources here use only '*' wildcards; keep the regression
    # oracle intentionally narrow instead of pretending to emulate the host.
    rx = "^" + re.escape(pattern).replace(r"\*", ".*") + "$"
    return re.match(rx, value) is not None

def effective_permission(rel, action, resource):
    effect = None
    for rule in permission_rules(rel):
        if glob_match(rule["action"], action) and glob_match(rule["resource"], resource):
            effect = rule["effect"]
    return effect

# Generic reachability: any pack-owned skill that an agent prompt explicitly says to
# load must not be denied by that agent's effective skill permission.
skill_ids = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
for agent_path in agents:
    rel = f"agents/{agent_path.name}"
    body = agent_path.read_text(encoding="utf-8")
    for line in body.splitlines():
        if "load" not in line.lower():
            continue
        for skill_id in skill_ids:
            if f"`{skill_id}`" in line:
                effect = effective_permission(rel, "skill", skill_id)
                check(effect != "deny", f"{rel}: referenced skill {skill_id} is effectively denied")

# Incident-independent regression for the two semantic roles whose active contract
# requires the canonical session-evidence owner.
for rel in ["agents/semantic-checkpoint.md", "agents/session-evaluator.md"]:
    check(
        effective_permission(rel, "skill", "session-evidence") == "allow",
        f"{rel}: required skill session-evidence is not effectively allowed",
    )

# Evidence must not establish a new material product/design choice by itself.
planner_ui = text("agents/project-planner.md") + "\n" + text("agents/ui-orchestrator.md")
for bad in [
    "user intent/evidence does not establish the governing choice",
    "unless current user intent or evidence establishes it",
]:
    check(bad not in planner_ui, f"evidence/product-authority shortcut returned: {bad}")
check(planner_ui.count("does not by itself") >= 2, "product/design evidence boundary missing")

# pr-readiness is the reusable Draft/Candidate/Ready state-machine owner.
pr = text("skills/pr-readiness/SKILL.md")
check("During active work on an owned PR, intermediate Draft publication" in pr, "pr-readiness Draft owner missing")
check("When implementation is complete, establish the final intended local state as **Candidate HEAD**" in pr, "pr-readiness Candidate owner missing")
check("Ready evidence contract" in pr, "pr-readiness Ready owner missing")
check("Owned PRs are created as Draft by default." not in text("skills/git-provenance/SKILL.md"), "git-provenance still owns Draft creation")
check("not a second Draft/Candidate/Ready sequence" in text("AGENTS.md"), "root single-owner declaration missing")
check("do not define a separate UI lifecycle order" in text("agents/ui-orchestrator.md"), "UI role still owns lifecycle order")

# resource-lifecycle owns resource state machine; root owns trigger/gate only.
root_text = text("AGENTS.md")
resource = text("skills/resource-lifecycle/SKILL.md")
for state in ["`cleaned`", "`intentionally retained`", "`cleanup blocked`", "`ownership transferred`", "status as `unknown`"]:
    check(state not in root_text, f"root duplicates resource lifecycle state {state}")
for state in ["cleaned", "intentionally retained", "cleanup blocked", "ownership transferred", "status is `unknown`"]:
    check(state in resource, f"resource-lifecycle missing state {state}")

# Named UI provider/source ordering exists in one integration owner, not generic UI roles.
ui_skill = text("skills/ui-component-sources/SKILL.md")
source_order = [
    "existing project components/tokens/styles/layout primitives",
    "official shadcn MCP/standard registry",
    "official shadcn MCP with public GitHub-compatible registries",
    "Jpisnice shadcn-ui MCP as a secondary/reference source",
    "manual implementation",
]
try:
    positions = [ui_skill.index(item) for item in source_order]
    check(positions == sorted(positions), "UI source order changed")
except ValueError as exc:
    failures.append(f"UI source owner missing expected source: {exc}")
ui_roles = [
    "agents/ui-orchestrator.md",
    "agents/ui-planner.md",
    "agents/ui-implementer.md",
    "agents/ui-auditor.md",
    "agents/a11y-reviewer.md",
]
for rel in ui_roles:
    lower = text(rel).lower()
    for token in ["shadcn", "jpisnice", "uupm", "registry/mcp", "mcp/registry"]:
        check(token not in lower, f"{rel}: provider/integration literal leaked into generic role: {token}")
for rel in ui_roles[:4]:
    check("ui-component-sources" in text(rel), f"{rel}: does not consume canonical UI integration owner")

# Reviewer-owned adversarial depth: structural presence only, not behavioral proof.
reviewer = text("agents/reviewer.md")
check(
    "whether a prohibited state can be accepted" in reviewer
    and "whether an established permitted state can be rejected" in reviewer,
    "reviewer: bidirectional guard/classifier counterexample contract missing",
)
check(
    "Derive the **review surface** from the actual candidate" in reviewer
    and "This expands review depth, not implementation authority" in reviewer,
    "reviewer: acceptance-scope/review-surface boundary missing",
)
check(
    "contended/global lock" in reviewer
    and "N × M × work" in reviewer
    and "latency-bearing operations" in reviewer,
    "reviewer: critical-resource call-chain cost contract missing",
)
check(
    "reconstruction/reconciliation of shared state" in reviewer
    and "create, update, delete, restore, or reinterpret" in reviewer
    and "intentional state from accidental absence" in reviewer,
    "reviewer: shared-state mutator composition contract missing",
)
check(
    "establish reachability as part of the behavior claim" in reviewer
    and "can actually reach the fallback" in reviewer
    and "existence of a branch" in reviewer,
    "reviewer: fallback/recovery reachability contract missing",
)
check(
    "projections, annotations, classifications, or refinements" in reviewer
    and "combined states" in reviewer
    and "must not silently erase, skip, or bypass" in reviewer,
    "reviewer: independent projection/refinement composition contract missing",
)
check(
    "candidate behavior or accepted values are bounded by a domain owned by another layer" in reviewer
    and "packaging/build/release matrix" in reviewer
    and "other non-authoritative operational surface" in reviewer
    and "must not silently narrow the accepted or supported behavior domain" in reviewer
    and "evidence about their own coverage" in reviewer,
    "reviewer: generalized authoritative-domain preservation contract missing",
)
check(
    "semantic success postcondition" in reviewer
    and "reported success suppresses fallback" in reviewer
    and "successful return is not evidence" in reviewer,
    "reviewer: fallback semantic-success contract missing",
)
check(
    "Review the candidate independently against the authoritative task contract" in reviewer
    and "implementation mechanism constrains the solution only to that exact established proposition" in reviewer
    and "does not waive collateral effects that were not separately accepted" in reviewer
    and "contract/design incompatibility" in reviewer
    and "exact accepted envelope" in reviewer,
    "reviewer: implementation-constraint independence/tradeoff boundary missing",
)
check(
    "materially changes the amount, placement, frequency, or scaling of work" in reviewer
    and "compare the candidate with Base behavior or an established performance/resource expectation" in reviewer
    and "allocations/memory growth" in reviewer
    and "performance/resource regression" in reviewer
    and "report the specific evidence gap" in reviewer,
    "reviewer: general performance/resource regression contract missing",
)
check(
    "Do not waive wrong fix level because the requested case passes" in reviewer
    and "test-specific branches, duplicated policy, compatibility tricks" in reviewer
    and "temporary workarounds" in reviewer
    and "never silently normalize it into production-grade design" in reviewer,
    "reviewer: wrong-fix-level/workaround reporting contract missing",
)
check(
    "For every code/diff/commit/branch/workspace/PR review" in reviewer
    and "load `open-code-review-delegate`" in reviewer
    and "before substantive host review reasoning" in reviewer
    and "delegate preflight is mandatory" in reviewer
    and "not a risk/usefulness heuristic" in reviewer
    and "if delegation is unavailable" in reviewer
    and "continue with the native review preflight" in reviewer
    and "Managed `open-code-review` / `ocr review` is separate from mandatory delegation" in reviewer,
    "reviewer: mandatory deterministic OCR delegate preflight contract missing",
)
check(
    "Managed OCR is independent evidence, not a substitute for host-review coverage or reasoning" in reviewer
    and "host-owned ledger" in reviewer
    and "does not become host-reviewed merely because OCR covered it" in reviewer
    and "absence of OCR comments is not evidence of correctness" in reviewer
    and "never add OCR-selected entries to host coverage" in reviewer,
    "reviewer: managed OCR independence/host coverage contract missing",
)

# Material user decisions that are not retrievable downstream need provenance
# preservation, but the receipt itself must not become a new authority source.
orch = text("agents/code-orchestrator.md")
session_evidence = text("skills/session-evidence/SKILL.md")
check(
    "For a fresh whole-change/final reviewer judgment" in orch
    and "authoritative task-contract propositions needed for judgment" in orch
    and "label only that exact proposition as an `implementation constraint`" in orch
    and "do not present the mechanism as an accepted design, adequate/correct fix" in orch
    and "Do not seed the fresh reviewer with prior reviewer/OCR verdicts or findings" in orch
    and "claimed-clean areas" in orch
    and "reconcile it only after the reviewer returns" in orch
    and "targeted re-review" in orch
    and "partial/incremental" in orch,
    "code-orchestrator: fresh reviewer context-isolation/mechanism-framing contract missing",
)
check(
    "preserve a contemporaneous provenance receipt" in orch
    and "exact material proposition presented" in orch
    and "does not create or broaden authority" in orch,
    "code-orchestrator: opaque-interaction provenance receipt contract missing",
)
check(
    "contemporaneous provenance receipt created before the dependent handoff" in session_evidence
    and "A later paraphrase such as `user decided X` is not an equivalent receipt" in session_evidence
    and "does not itself create, broaden, or reinterpret authority" in session_evidence,
    "session-evidence: receipt consumption/provenance boundary missing",
)


# Cross-role mutation handoffs must preserve role ownership instead of laundering
# upstream planning/checkpoint/review recommendations into implementation recipes.
checkpoint_sem = text("agents/semantic-checkpoint.md")
debugger_sem = text("agents/debugger.md")
ui_orch_sem = text("agents/ui-orchestrator.md")
ui_impl_sem = text("agents/ui-implementer.md")
check(
    "do not certify a concrete implementation mechanism, patch shape, or technical design as correct" in checkpoint_sem
    and "does not certify design/implementation adequacy" in checkpoint_sem
    and "Remaining implementation uncertainty belongs to the implementation role" in checkpoint_sem
    and "## Result" in checkpoint_sem
    and "**Mutation boundary**" in checkpoint_sem
    and "Do not recommend forwarding the candidate or checkpoint report unchanged as an implementation recipe" in checkpoint_sem
    and "Candidate handoff" not in checkpoint_sem,
    "semantic-checkpoint: semantic authorization still leaks into implementation certification/recipe",
)
check(
    "omit upstream non-required mechanism/remediation proposals by default" in orch
    and "do not forward the candidate/checkpoint report verbatim" in orch
    and "does not certify a proposed implementation mechanism" in orch
    and "do not turn a reviewer/tester remediation suggestion or patch shape into the assigned fix" in orch,
    "code-orchestrator: mutation handoff still permits upstream recipe laundering",
)
check(
    "Treat any caller/reviewer/tester proposed remediation or patch shape as a hypothesis" in debugger_sem
    and "diagnose the root cause from the governing behavior and evidence" in debugger_sem,
    "debugger: caller/remediation recipe anchoring guard missing",
)
check(
    "upstream plan/checkpoint/review recommendations were not laundered into a binding implementation recipe" in evaluator_sem
    and "debugger received the defect/invariant/evidence rather than an unestablished remediation shape" in evaluator_sem,
    "session-evaluator: cross-role mutation-handoff contamination diagnostic missing",
)
check(
    "do not forward the whole artifact as binding implementation authority" in ui_orch_sem
    and "omit non-required layout/mechanism recommendations by default" in ui_orch_sem
    and "A supplied audit/plan is context, not blanket authority or correctness proof" in ui_impl_sem
    and "non-required mechanism/layout recommendations remain hypotheses" in ui_impl_sem,
    "UI mutation handoff: plan/audit recipe-laundering guard missing",
)


# A returned build package that independent evidence proves defective must not
# re-enter ordinary build iteration merely because build authored the code.
build_sem = text("agents/build.md")
check(
    "returned implementation package is later rejected by valid independent evidence" in orch
    and "route the corrective mutation by the **current action**, not by the original implementer" in orch
    and "belongs to `@debugger`" in orch
    and "Do not send the defect back to `@build` as ordinary implementation" in orch
    and "own local verification before returning its current package" in orch
    and "root reset/escalation rules before another patch" in orch,
    "code-orchestrator: independently rejected build package can still loop back as ordinary build work",
)
check(
    "do not accept a follow-up assignment whose primary purpose is to repair a concrete confirmed product-code defect" in build_sem
    and "bugfix/root-cause work owned by `@debugger`" in build_sem
    and "own local checks discover before you return the current package" in build_sem
    and "purely mechanical non-bug/tests/docs corrections" in build_sem,
    "build: post-return confirmed-defect reroute boundary missing",
)
check(
    "It is not proof that a proposed mechanism is correct and is not an implementation recipe" in build_sem
    and "implementation proof" in build_sem
    and "narrowest existing owner/primitive" in build_sem
    and "nearest preserved behavior/invariant" in build_sem
    and "Do not start from the requested patch shape and work backward" in build_sem,
    "build: pre-edit implementation-proof/owner reasoning gate missing",
)
check(
    "## Pre-return self-review and verification" in build_sem
    and "inspect the effective diff/state against the implementation proof" in build_sem
    and "actually wired into the required behavior" in build_sem
    and "preserves the nearest required sibling/negative behavior" in build_sem
    and "mandatory implementation self-review, not independent `@reviewer` evidence" in build_sem
    and "A green focused test does not by itself complete the package" in build_sem,
    "build: pre-return self-review/preserved-behavior gate missing",
)
check(
    "for every materially relevant input, state/transition, representation, lifecycle, boundary/environment, or consumer class" in build_sem
    and "at least one materially different representative capable of falsifying the chosen mechanism" in build_sem
    and "actively try to falsify the final mechanism against the established case map" in build_sem
    and "Derive those probes from the behavioral contract and owning abstraction, not from the patch shape" in build_sem
    and "multiple self-authored tests that share the same implementation assumption do not establish closure" in build_sem
    and "unclosed established class" in build_sem,
    "build: cross-class falsification/self-test blind-spot gate missing",
)

# External technical evidence has a distinct owner from repository discovery, generic fallback, and planning.
librarian_sem = text("agents/librarian.md")
explore_sem = text("agents/explore.md")
general_sem = text("agents/general.md")
planner_sem = text("agents/project-planner.md")
check(
    "read-only external technical evidence specialist" in librarian_sem.lower()
    and "authority + exact-version applicability + directness" in librarian_sem
    and "Do not vote by number of sources" in librarian_sem
    and "do not emit empty report sections" in librarian_sem
    and "does not by itself establish local repository usage" in librarian_sem,
    "librarian: external-evidence ownership/boundary contract missing",
)
check(
    "Repository-local descriptive evidence is this role's domain" in explore_sem
    and "not repository exploration" in explore_sem,
    "explore: local-repository boundary against external research missing",
)
check(
    "no dedicated external-technical-evidence owner applies" in general_sem
    and "external library/API/upstream/version evidence research" in general_sem,
    "general: fallback still overlaps external technical evidence owner",
)
check(
    "do not absorb authoritative external technical research into planning" in planner_sem
    and "return the evidence need to the caller" in planner_sem,
    "project-planner: external-evidence boundary missing",
)
check(
    "@librarian" not in explore_sem and "@librarian" not in general_sem and "@librarian" not in planner_sem,
    "leaf roles gained direct librarian routing instead of returning the adjacent evidence need to the caller",
)
check(
    "@librarian" in root_sem
    and "@librarian" in text("agents/code-orchestrator.md")
    and "@librarian" in text("agents/auditor.md"),
    "librarian: intended root/orchestrator/auditor routing surfaces missing",
)

# Release-gate audit surfaces are separate from the legacy static presence harness.
contract_audit = text("evals/contract-protocol-audit.py")
contract_spec = text("evals/contract-protocol-spec.json")
contract_selftest = text("evals/contract-protocol-selftest.py")
release_gates = text("evals/run-release-gates.py")
check("role-local executable method" in contract_spec and "Ownership -> Invocation -> Method -> Boundaries -> Result" in contract_spec and "producer output, parent transformation, consumer input" in contract_spec and "Keyword presence" in contract_spec, "contract/protocol spec missing semantic-shape/adversarial audit principles")
check("CONTRACT / PROTOCOL AUDIT v3" in contract_audit and "missing essential profile core-loop capabilities" in contract_audit and "REVIEW is intentionally release-blocking" in contract_audit and "Prompt length is diagnostic only" in contract_audit, "contract audit v3 severity/core-loop/review gate missing")
check("keyword-stuffed implementation role was not rejected" in contract_selftest and "thin ops role without diagnostic isolation" in contract_selftest and "five-heading shell without executable implementation method was not rejected" in contract_selftest and "compact executable discovery role" in contract_selftest and "without five standardized headings" in contract_selftest and "audit orchestrator missing only reconciliation" in contract_selftest and "producer-side implementation certification" in contract_selftest and "new role without executable-contract audit profile did not block release" in contract_selftest and "stale role profile did not block release" in contract_selftest and "thin external research role without version/conflict applicability loop was not rejected" in contract_selftest and "complete external-research contract should PASS" in contract_selftest, "contract audit v3 synthetic anti-gaming/severity/lifecycle/semantic-shape/external-research selftests missing")
edge_audit = text("evals/role-handoff-audit.py")
edge_selftest = text("evals/role-handoff-selftest.py")
release_gates = text("evals/run-release-gates.py")
check("Closed-world static audit" in edge_audit and "EDGE_CLASSIFICATION" in edge_audit and "UNCLASSIFIED EDGE" in edge_audit and "STALE EDGE" in edge_audit and "ui-orchestrator','a11y-reviewer" in edge_audit and "code-orchestrator','devops" in edge_audit and "auditor','specialists" in edge_audit and "code-orchestrator','librarian" in edge_audit and "auditor','librarian" in edge_audit, "role-handoff closed-world inventory/profiles missing")
check("recipe-shaped devops handoff not rejected" in edge_selftest and "unbound a11y handoff not rejected" in edge_selftest and "preselected UI planning handoff not rejected" in edge_selftest and "unbounded auditor specialist handoff not rejected" in edge_selftest and "new unclassified handoff edge did not block release" in edge_selftest and "stale handoff classification did not block release" in edge_selftest and "unbound librarian handoff not rejected" in edge_selftest and "auditor librarian authority/applicability omission not rejected" in edge_selftest, "role-handoff synthetic anti-gaming/inventory/external-research selftests missing")
check("role-handoff selftest" in release_gates and "role-handoff edge audit" in release_gates, "release gate runner missing role-handoff checks")
check("unresolved findings must not be waived merely to obtain PASS" in release_gates, "release gate aggregator may waive unresolved contract findings")
check("Role lifecycle requalification" in text("docs/semantic-design-manual.md") and "method-preservation test" in text("docs/semantic-design-manual.md") and "closed-world discovered handoff inventory" in text("docs/semantic-design-manual.md"), "semantic-design manual missing role lifecycle/method-preservation/closed-world edge audit")
check("Role contract semantic shape" in text("docs/semantic-design-manual.md") and "Ownership → Invocation → Method → Boundaries → Result" in text("docs/semantic-design-manual.md") and "not a five-heading template" in text("docs/semantic-design-manual.md"), "semantic-design manual missing semantic role-contract shape / anti-template rule")

# Temporary transition-eval structure guards. These prove only that the replay
# contract is explicit enough to run consistently; they do not prove behavior.
traces = text("evals/semantic-transition-traces.md")
check(traces.count("### ST-") == 75, "semantic-transition suite must contain 75 cases")
for field in [
    "**Initial user/spec fixture:**",
    "**Runtime/repository fixture:**",
    "**Injected intermediate output:**",
    "**Expected earliest observable stop/preservation point:**",
]:
    check(traces.count(field) == 75, f"semantic-transition suite missing per-case field: {field}")
for case in [
    "ST-19 — A changed guard must preserve both material classification sides",
    "ST-20 — Critical-section review must propagate cost through the reachable call chain",
    "ST-21 — Issue framing must not artificially close the actual review surface",
    "ST-22 — Shared-state reconstruction must compose with existing mutators",
    "ST-23 — A fallback capability claim requires reachable supported inputs",
    "ST-24 — A narrower non-authoritative surface must not redefine an authoritative behavior domain",
    "ST-25 — Repeated counterexamples to one invariant must converge on the owning rule",
    "ST-26 — Independent projection/refinement paths must compose without silent erasure",
    "ST-27 — Fallback must not be suppressed by false semantic success",
    "ST-28 — Delegated assignment must specialize rather than redefine the selected role contract",
    "ST-29 — Review evidence must remain bound to the exact candidate state",
    "ST-30 — Mutation receipt must not substitute for authoritative state read-back",
    "ST-31 — Deterministic code-review delegation must not become discretionary",
    "ST-32 — Fresh independent judgment must not be pre-anchored by prior verdict framing",
    "ST-33 — An implementation constraint must not become a correctness waiver",
    "ST-34 — Functional success must not hide a material performance or resource regression",
    "ST-35 — Independently rejected implementation must not loop back as ordinary build work",
    "ST-36 — Implementation handoff/checkpoint approval must not become a code recipe or correctness proof",
    "ST-37 — Build must self-review the final diff against changed and preserved behavior before returning",
    "ST-38 — Build must not narrow an authoritative domain through a convenient local surface",
    "ST-39 — Incomplete or unknown evidence must not be collapsed into a positive classification",
    "ST-40 — Local movement must not be mistaken for durable monotonic progress",
    "ST-41 — Identity equality must not silently stand in for identity lifetime",
    "ST-42 — Failure of the chosen implementation path must not prove capability fallback is unavailable",
    "ST-43 — Local worker termination must not be mistaken for whole-operation termination",
    "ST-44 — Semantic checkpoint authorization must not certify or forward an implementation recipe",
    "ST-45 — A confirmed finding must become a debugger defect contract, not a reviewer patch recipe",
    "ST-46 — A plan or audit must not become blanket mutation authority",
    "ST-47 — A routed substantive role must have an executable role-local contract",
    "ST-48 — Per-file correctness must not substitute for producer→transformer→consumer protocol compatibility",
    "ST-49 — Role-contract keyword stuffing must not satisfy executability",
    "ST-50 — Compact role contracts must be judged by executability, not byte count",
    "ST-51 — Generic contract dimensions must not replace the role-specific core loop",
]:
    check(case in traces, f"semantic-transition suite missing reviewer regression: {case}")
check(
    "non-authoritative operational or convenience surface" in traces
    and "packaging/build/release matrix" in traces
    and "authority to redefine the governing domain" in traces,
    "ST-24 no longer exercises generalized authoritative-domain narrowing",
)
check(
    "review evidence remains state-identity-bound" in traces
    and "Green tests/CI on the newer state are separate evidence layers" in traces,
    "ST-29 exact-candidate evidence-freshness regression missing",
)
check(
    "mutation acknowledgment is evidence that the request/report occurred" in traces
    and "authoritative post-mutation" in traces,
    "ST-30 mutation-read-back regression missing",
)
check(
    "compatible deterministic delegation is available" in traces
    and "required preflight for the applicable target class" in traces
    and "pass fallback only when delegation is unavailable" in traces,
    "ST-31 mandatory deterministic delegate-preflight regression missing",
)
check(
    "judgment-context isolation, not merely a new child-session identity" in traces
    and "prior verdicts, claimed-clean areas, expected outcome" in traces
    and "targeted fix re-review" in traces
    and "partial/incremental" in traces
    and "reconcile that independent result with prior findings" in traces,
    "ST-32 independent-judgment context-contamination regression missing",
)
check(
    "implementation constraint" in traces
    and "blanket authority for collateral regressions/tradeoffs" in traces
    and "exact accepted envelope" in traces
    and "contract/design incompatibility" in traces,
    "ST-33 implementation-constraint/correctness-waiver regression missing",
)
check(
    "material performance or resource regression" in traces
    and "relative to Base or an established performance/resource expectation" in traces
    and "no explicit performance benchmark/threshold was supplied" in traces
    and "must not invent a performance budget" in traces,
    "ST-34 material performance/resource-regression review missing",
)
check(
    "`@build` returns its package with local evidence" in traces
    and "valid independent reviewer/tester/CI/reproduction result establishes a concrete product-code defect" in traces
    and "routes to `@debugger`" in traces
    and "merely because build authored the code" in traces
    and "local pre-return self-correction stays with build" in traces,
    "ST-35 independently-rejected-build reroute/convergence regression missing",
)
check(
    "checkpoint approval must not become a code recipe or correctness proof" in traces.lower()
    and "narrowest owner that can guarantee the outcome" in traces
    and "non-required H remains a hypothesis/option" in traces
    and "does not work backward from the requested patch shape" in traces,
    "ST-36 build handoff/checkpoint recipe-regression missing",
)
check(
    "self-review the final diff against changed and preserved behavior" in traces.lower()
    and "before package return" in traces
    and "green focused case" in traces
    and "implementation-local preserved/representative check" in traces
    and "does not label this self-review independent review" in traces,
    "ST-37 build pre-return self-review regression missing",
)
check(
    "narrow an authoritative domain through a convenient local surface" in traces.lower()
    and "incomplete or unknown evidence" in traces.lower()
    and "durable monotonic progress" in traces.lower()
    and "identity lifetime" in traces.lower()
    and "capability fallback is unavailable" in traces.lower()
    and "whole-operation termination" in traces.lower()
    and "self-authored tests" in traces,
    "ST-38..ST-43 trace-derived build falsification suite missing",
)
check(
    "checkpoint authorization must not certify or forward an implementation recipe" in traces.lower()
    and "must not certify design/implementation adequacy" in traces
    and "orchestrator must reconstruct the mutation handoff" in traces,
    "ST-44 checkpoint-to-mutation recipe-laundering regression missing",
)
check(
    "debugger defect contract, not a reviewer patch recipe" in traces.lower()
    and "separate the defect proposition/evidence from remediation advice" in traces
    and "caller/reviewer remediation suggestion as a hypothesis" in traces,
    "ST-45 finding-to-debugger recipe-laundering regression missing",
)
check(
    "plan or audit must not become blanket mutation authority" in traces.lower()
    and "actually adopted plan propositions/constraints" in traces
    and "whole artifact as correctness proof" in traces,
    "ST-46 plan/audit mutation-authority regression missing",
)
check(
    "routed substantive role must have an executable role-local contract" in traces.lower()
    and "role-owned procedure/decision sequence" in traces
    and "role-specific exception solely to preserve PASS" in traces,
    "ST-47 role-executability regression missing",
)
check(
    "producer→transformer→consumer protocol compatibility" in traces.lower()
    and "producer output semantics, parent transformation, consumer input semantics" in traces
    and "per-file/static PASS hides an incompatible handoff" in traces,
    "ST-48 cross-role protocol-composition regression missing",
)
check(
    "role-contract keyword stuffing must not satisfy executability" in traces.lower()
    and "matched vocabulary is not an executable method" in traces
    and "profile-specific core-loop capabilities" in traces,
    "ST-49 keyword-stuffing role-contract regression missing",
)
check(
    "compact role contracts must be judged by executability, not byte count" in traces.lower()
    and "byte/line count is reported only as diagnostic context" in traces
    and "never changes status" in traces
    and "fixed size/sparsity quota alone creates `FAIL` or `REVIEW`" in traces,
    "ST-50 compact-role preservation/no-size-status regression missing",
)
check(
    "generic contract dimensions must not replace the role-specific core loop" in traces.lower()
    and "diagnostic isolation" in traces
    and "generic dimensions are insufficient" in traces,
    "ST-51 profile-specific core-loop regression missing",
)
check(
    "contract-audit severity must distinguish non-executable roles from executable roles with a material gap" in traces.lower()
    and "essential profile core-loop capability produces `FAIL`" in traces
    and "material secondary branch gap produces release-blocking `REVIEW`" in traces
    and "Prompt size never changes either status" in traces,
    "ST-52 contract-audit severity calibration regression missing",
)
check(
    "devops must isolate the failing layer before operational mutation" in traces.lower()
    and "treat the suspicious setting as a hypothesis rather than root cause" in traces.lower()
    and "authorization is treated as correctness evidence" in traces.lower(),
    "ST-53 devops diagnose-before-mutation regression missing",
)
check(
    "general fallback must research a bounded question without impersonating a specialist" in traces.lower()
    and "fact/evidence" in traces.lower() and "inference/hypothesis" in traces.lower(),
    "ST-54 general fallback research-discipline regression missing",
)
check(
    "ui audit must diagnose the current user-job/state before recommending redesign" in traces.lower()
    and "generic preference becomes a finding" in traces.lower(),
    "ST-55 UI audit current-state/counterexample regression missing",
)
check(
    "ui planning must derive from current ownership and preserve unresolved product decisions" in traces.lower()
    and "unresolved product choices" in traces.lower(),
    "ST-56 UI planning authority/ownership regression missing",
)
check(
    "ui implementation must self-review the final state" in traces.lower()
    and "representative changed and preserved/negative states" in traces.lower(),
    "ST-57 UI implementation final-state self-review regression missing",
)
check(
    "accessibility verdict must bind the exact target and affected interaction boundary" in traces.lower()
    and "advisory vs stable-result mode" in traces.lower(),
    "ST-58 a11y target/interaction-boundary regression missing",
)
check(
    "broad auditor must reconcile conflicting/partial specialist evidence without voting" in traces.lower()
    and "compares evidence validity/directness" in traces.lower(),
    "ST-59 audit reconciliation regression missing",
)
check(
    "caller handoff must satisfy the callee invocation contract" in traces.lower()
    and "individual-role pass hides an under-specified or recipe-shaped edge" in traces.lower(),
    "ST-60 caller-callee invocation-contract regression missing",
)
check(
    "role topology promotion requires executable-contract requalification" in traces.lower()
    and "prior pass is not inherited" in traces.lower(),
    "ST-61 topology requalification regression missing",
)
check(
    "canonical-owner deduplication must preserve an executable method" in traces.lower()
    and "method-preservation audit" in traces.lower(),
    "ST-62 owner-move/compaction preservation regression missing",
)
check(
    "new pack-owned role relation must enter the closed-world handoff inventory" in traces.lower()
    and "unknown relation fails" in traces.lower()
    and "stale classification fails" in traces.lower(),
    "ST-63 closed-world edge inventory regression missing",
)
check(
    "role-contract standardization must preserve semantic function rather than enforce heading uniformity" in traces.lower()
    and "five semantic functions" in traces.lower()
    and "heading/template conformity substitutes for semantic executability" in traces.lower(),
    "ST-64 semantic-shape/anti-template regression missing",
)
check(
    "external technical evidence must bind the target version instead of answering from `latest`" in traces.lower()
    and "challenge `latest` applicability" in traces.lower(),
    "ST-65 external target/version applicability regression missing",
)
check(
    "external source conflicts must be reconciled by authority, applicability, and directness rather than voting" in traces.lower()
    and "never treat source count as proof" in traces.lower(),
    "ST-66 external source-conflict reconciliation regression missing",
)
check(
    "external best practice or upstream advice must not become project authority" in traces.lower()
    and "recommendation rather than project acceptance" in traces.lower(),
    "ST-67 external-advice authority regression missing",
)
check(
    "external research must not absorb repository discovery or implementation planning" in traces.lower()
    and "explore = local present" in traces.lower()
    and "librarian = external truth" in traces.lower()
    and "project-planner = implementation future" in traces.lower(),
    "ST-68 librarian/explore/planner ownership-boundary regression missing",
)
check(
    "caller handoff to external research must carry proposition, target, applicability, and source boundary" in traces.lower()
    and "bounded external research proposition" in traces.lower(),
    "ST-69 librarian caller-handoff regression missing",
)
check(
    "external-research result formatting must preserve evidence semantics without mandatory report boilerplate" in traces.lower()
    and "omit empty sections" in traces.lower()
    and "lightest presentation" in traces.lower(),
    "ST-70 librarian result-format semantics regression missing",
)
check(
    "multi-stage orchestration must synthesize workflow milestones without narrating the tool stream" in traces.lower()
    and "opaque tool stream" in traces.lower()
    and "what is established/unresolved" in traces.lower(),
    "ST-71 orchestrator milestone-visibility regression missing",
)
check(
    "milestone visibility must not regress into tool-by-tool status narration" in traces.lower()
    and "no time/tool-count quota forces updates" in traces.lower()
    and "startup → tools → final" in traces.lower(),
    "ST-72 anti-status-spam preservation regression missing",
)
check(
    "user decision raised from hidden specialist context must be self-contained" in traces.lower()
    and "viable alternatives and consequences/tradeoffs" in traces.lower()
    and "recommendation when evidence supports one" in traces.lower(),
    "ST-73 hidden-context decision-brief regression missing",
)
check(
    "evidence-resolvable technical ambiguity must not be promoted into a user product choice" in traces.lower()
    and "resolve factual/technical part" in traces.lower()
    and "continue without user choice" in traces.lower(),
    "ST-74 evidence-before-user-choice regression missing",
)
check(
    "managed review coverage must not substitute for host reviewer coverage" in traces.lower()
    and "ocr-selected entries do not become host-reviewed" in traces.lower()
    and "host coverage: 14/14" in traces.lower()
    and "managed ocr coverage: 10 selected / 10 completed" in traces.lower(),
    "ST-75 host/OCR coverage-independence regression missing",
)
check(
    "proposition relation: `preserved | refined | strengthened | weakened | substituted | unverified`" in traces,
    "semantic-transition suite proposition-relation axis missing",
)
check(
    "transition class: `preserved | refined | strengthened | weakened | substituted | uncertainty-resolved | unverified`" not in traces,
    "semantic-transition suite still mixes evidence resolution into proposition relation",
)
check(
    "classify the transition as `uncertainty-resolved`" not in traces,
    "ST-09 still classifies uncertainty resolution as a proposition relation",
)
check(
    all(key in traces for key in ["`pack_version`", "`package_sha256`", "`active_root_sha256`", "`scenario_id`"])
    and "user-visible startup contract" in traces,
    "semantic-transition suite trace metadata contract missing",
)

if failures:
    print("STATIC POLICY REGRESSIONS: FAIL")
    for item in failures:
        print(f"- {item}")
    sys.exit(1)
print(f"STATIC POLICY REGRESSIONS: PASS ({len(agents)} agents; schema/dependency/blocker/product/PR/resource/UI/reviewer/eval guards)")
