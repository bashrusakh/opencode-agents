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
check(len(agents) == 19, f"expected 19 agents, found {len(agents)}")
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
trajectory_sem = text("agents/trajectory-auditor.md")
workflow_entry_sem = text("skills/workflow-control/SKILL.md")
code_host_sem = text("skills/repository-workflow/SKILL.md")
terminal_eval_sem = text("skills/session-evaluation-control/SKILL.md")
delegation_sem = text("skills/delegation-control/SKILL.md")
implementation_sem = text("skills/change-contract/SKILL.md")
pr_readiness_sem = text("skills/pr-readiness/SKILL.md")
semantic_runtime = "\n".join([root_sem, checkpoint_sem, evaluator_sem, workflow_entry_sem, delegation_sem, implementation_sem])

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
check(
    "### Workflow-owner synthesis loop" in code_orchestrator_sem
    and "**Ingest**" in code_orchestrator_sem
    and "**Reconcile**" in code_orchestrator_sem
    and "**Update the whole-task model**" in code_orchestrator_sem
    and "**Decide**" in code_orchestrator_sem
    and "**Delegate**" in code_orchestrator_sem
    and "not a workflow transition by itself" in code_orchestrator_sem
    and "Do not invoke an independent controller merely to avoid making an ordinary workflow-owner decision" in code_orchestrator_sem
    and "safe read-only primary evidence" in code_orchestrator_sem,
    "code-orchestrator: accountable-owner synthesis/reconciliation loop missing",
)
check(
    "bounded owner trajectory reassessment yourself" in code_orchestrator_sem
    and "If that bounded reassessment yields one evidence-backed model" in code_orchestrator_sem
    and "exact longitudinal question remains unresolved after the owner reassessment" in code_orchestrator_sem
    and "owner reassessment performed" in code_orchestrator_sem
    and "why available primary evidence could not safely resolve it" in code_orchestrator_sem
    and "not by themselves reasons to ask a controller" in code_orchestrator_sem,
    "code-orchestrator: owner-first trajectory reassessment/second-opinion boundary missing",
)
check(
    "independent authority-sensitive gate" in code_orchestrator_sem
    and "material semantic proposition remains unresolved after that owner reconciliation" in code_orchestrator_sem
    and "Do **not** invoke the checkpoint merely because strong repository evidence changes a technical owner" in code_orchestrator_sem
    and "owner reconciliation performed" in code_orchestrator_sem
    and "why the owner cannot safely settle the authority relation directly" in code_orchestrator_sem,
    "code-orchestrator: residual-authority semantic-checkpoint boundary missing",
)

check(
    "capability, not exposed task context" in root_sem
    and "do not retrieve parent investigative history merely because a recall integration exists" in root_sem
    and "fresh child does not resume parent task memory/checkpoints merely because the parent workflow is long-running" in delegation_sem
    and "Child-session freshness and independent judgment" in delegation_sem,
    "root/delegation-control: memory capability-versus-exposure freshness boundary missing",
)
check(
    "first plausible framing or solution level as a hypothesis" in root_sem
    and "materially different plausible framing" in root_sem,
    "AGENTS.md: non-trivial hypothesis/counter-framing invariant lost during residency split",
)
check(
    "If a required skill is unavailable" in root_sem
    and "Skill: <name> unavailable" in root_sem
    and "stage as blocked" in root_sem,
    "AGENTS.md: required-skill unavailable/blocking invariant lost",
)
check(
    "**Broad scope** means" in workflow_entry_sem
    and "file count is only a signal" in workflow_entry_sem
    and "`likely` means one is most probable" in workflow_entry_sem
    and "safe read-only work or narrow local work" in workflow_entry_sem
    and "`ambiguous` means several materially different workflows/deliverables remain plausible" in workflow_entry_sem,
    "workflow-control: broad-scope/confidence consequence semantics lost",
)
check(
    "absent from the current worktree" in code_host_sem
    and "repository-host metadata" in code_host_sem
    and "If no valid publication path exists, keep the local evidence and report publication blocked" in workflow_entry_sem
    and "verify the destination" in workflow_entry_sem,
    "repository-workflow/workflow-control: PR-template host lookup / visual-evidence publication fallback lost",
)
check(
    "Do not disable, hide, or reconfigure an optional integration merely to manufacture freshness or independence" in delegation_sem
    and "actual task-specific contaminating content" in delegation_sem
    and "configuration change is authorized" in delegation_sem,
    "delegation-control: anti-artificial-freshness reconfiguration guard missing",
)
check(
    "**Complexity/design escalation** means" in implementation_sem
    and "shared state, lifecycle, protocol, concurrency, persistence, or ownership rule" in implementation_sem
    and "invariant/state/transition/interleaving/ownership model" in implementation_sem,
    "change-contract: complexity/design escalation definition lost",
)
check(
    "**Owned PR** means" in pr_readiness_sem
    and "current authenticated/user account" in pr_readiness_sem
    and "branch name alone does not establish ownership" in pr_readiness_sem
    and "canonical **Owned PR** definition" in code_host_sem
    and "load `repository-workflow`" in code_orchestrator_sem,
    "pr-readiness/repository-workflow/code-orchestrator: canonical Owned PR identity chain missing",
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
    "A blocker to the prior path remains evidence, not replacement authority" in checkpoint_sem
    and "apply root section 2.2's relation/authority semantics" in checkpoint_sem,
    "semantic-checkpoint: blocker/replacement enforcement missing",
)
check(
    "a blocker may establish non-viability of the original path but does not itself authorize the replacement" in evaluator_sem,
    "session-evaluator: blocker/replacement diagnostic guard missing",
)



# Delegated task text specializes the selected role; it must not rewrite role-owned
# obligations or allow a partial diagnostic to masquerade as a complete stage verdict.
check(
    "An assignment specializes the selected role contract" in root_sem
    and "cannot waive role-owned obligations, independence, stop conditions, or verdict semantics" in root_sem
    and "A narrow/targeted result remains partial and cannot impersonate a broader stage" in delegation_sem,
    "root/delegation-control: assignment/role-contract composition guard missing",
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
    "Child-session freshness and independent judgment" in delegation_sem
    and "authoritative task propositions with provenance/qualifiers" in delegation_sem
    and "material implementation constraints" in delegation_sem
    and "Do not seed prior verdicts" in delegation_sem
    and "Targeted re-review" in delegation_sem
    and "partial/incremental" in delegation_sem,
    "delegation-control: independent-judgment context-isolation guard missing",
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

# Incident-independent regression for semantic roles whose active contract
# requires the canonical session-evidence owner.
for rel in ["agents/semantic-checkpoint.md", "agents/session-evaluator.md", "agents/trajectory-auditor.md"]:
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
check(
    "`pr-readiness` owns the canonical **Owned PR** definition and Draft/Candidate/Ready lifecycle" in code_host_sem
    and "Draft/Candidate/Ready" not in root_sem
    and "Draft/Candidate/Ready" not in workflow_entry_sem,
    "repository-workflow/workflow-control/root: PR lifecycle single-owner declaration missing",
)
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
    and "load `open-code-review-delegate` for its deterministic preflight only" in reviewer
    and "before substantive host review reasoning" in reviewer
    and "delegate preflight is mandatory" in reviewer
    and "not a risk/usefulness heuristic" in reviewer
    and "continue with the native review preflight" in reviewer
    and "vendor-skill text that continues into host review method" in reviewer
    and "Managed `open-code-review` / `ocr review` is separate from mandatory delegation" in reviewer
    and "Do not load or run managed OCR solely because the vendor skill description" in reviewer,
    "reviewer: deterministic OCR preflight / vendor-boundary contract missing",
)
check(
    "Managed OCR is independent evidence, not a substitute for host-review coverage or reasoning" in reviewer
    and "host-owned ledger" in reviewer
    and "does not become host-reviewed merely because OCR covered it" in reviewer
    and "absence of OCR comments is not evidence of correctness" in reviewer
    and "never add OCR-selected entries to host coverage" in reviewer,
    "reviewer: managed OCR independence/host coverage contract missing",
)
check(
    "task-specific judgmental or investigative information actually present in the reviewer's model-visible context" in reviewer
    and "does **not** by itself contaminate a fresh review" in reviewer
    and "uncertainty about whether such a capability could reveal prior context is not evidence" in reviewer
    and "Do not proactively retrieve prior-task/session memory" in reviewer
    and "Do not run parent-task checkpoint/memory recovery" in reviewer
    and "whole-PR authoritative acceptance model" in reviewer
    and "Coverage: full PR` describes host diff coverage, not semantic acceptance-model completeness" in reviewer
    and "Do not block the review, request integration changes, or treat freshness as unproven merely because a recall capability is available" in reviewer
    and "parent-derived or prior-task investigative direction" in reviewer
    and "including assignment text, automatic context injection, or intentional retrieval" in reviewer
    and "Do not speculate that contamination exists when no such task-specific steering content is visible" in reviewer
    and "independently derive the affected surfaces, risk model, investigation strategy and order" in reviewer
    and "locator, not proof" in reviewer
    and "targeted/partial re-review" in reviewer,
    "reviewer: fresh whole-change capability/exposure isolation or provenance defense missing",
)

# Material user decisions that are not retrievable downstream need provenance
# preservation, but the receipt itself must not become a new authority source.
orch = text("agents/code-orchestrator.md")
session_evidence = text("skills/session-evidence/SKILL.md")
check(
    "For a fresh whole-change/final reviewer judgment" in orch
    and ("what must be true, why it is authoritative, and what exact state is being reviewed" in orch or "what must be true, why authoritative, and what state is reviewed" in orch)
    and "label only that exact proposition as an `implementation constraint`" in orch
    and "parent-derived investigative direction" in orch
    and "regardless of wording, placement, formatting, or label" in orch
    and ("reviewer independently derives where risk exists and how to investigate it" in orch or "reviewer derives where risk exists and how to investigate it" in orch)
    and "review method or emphasis explicitly required by the user or an adopted project policy" in orch
    and "without parent-added investigative elaboration" in orch
    and "provenance label supplied by the parent is a locator, not proof of authority" in orch
    and "Apply root continuity semantics plus the loaded `delegation-control` independent-judgment isolation contract" in orch
    and "without importing parent investigative history into the reviewer context" in orch
    and "whole material task/acceptance surface" in orch
    and "targeted re-review" in orch
    and "partial/incremental" in orch
    and "fresh child does not resume parent task memory/checkpoints merely because the parent workflow is long-running" in delegation_sem,
    "code-orchestrator: fresh reviewer inherited-isolation/provenance contract missing",
)
check(
    "canonical receipt interface records the exact material proposition presented" in root_sem
    and "exact selected/typed response" in root_sem
    and "source/channel identity" in root_sem
    and "does not create, broaden, or reinterpret authority" in root_sem,
    "root: canonical provenance receipt interface missing",
)
check(
    "root section 2.2 **contemporaneous provenance receipt**" in orch
    and "root-defined receipt" in orch
    and "authority evidence boundary unresolved" in orch,
    "code-orchestrator: root receipt producer/reference boundary missing",
)
check(
    "consume the root section 2.2 **contemporaneous provenance receipt**" in session_evidence
    and "does not redefine that receipt schema" in session_evidence
    and "A later paraphrase such as `user decided X` is not an equivalent receipt" in session_evidence
    and "does not itself create, broaden, or reinterpret authority" in session_evidence,
    "session-evidence: root receipt consumption/provenance boundary missing",
)

check(
    "objective, target/behavior scope, allowed action level, expected deliverable/evidence, stop/escalation boundary" in delegation_sem
    and "minimally sufficient and reconstructable, not exhaustive" in delegation_sem
    and "Compression that collapses semantic distinctions is a handoff defect" in delegation_sem
    and "fresh child does not resume parent task memory/checkpoints merely because the parent workflow is long-running" in delegation_sem
    and "whole authoritative acceptance surface" in delegation_sem,
    "delegation-control: canonical handoff / fresh-child continuity / whole-scope acceptance contract missing",
)
graymatter = text("skills/graymatter-memory/SKILL.md")
check(
    "Apply root source-of-truth/continuity semantics first" in graymatter
    and "does not redefine memory authority, activation, fresh-judgment isolation" in graymatter
    and "apply the active role/delegation isolation contract" in graymatter,
    "graymatter-memory: root/active-isolation boundary is not referenced cleanly",
)
pr_readiness = text("skills/pr-readiness/SKILL.md")
check(
    "authoritative acceptance model that spans the whole PR/task surface" in pr_readiness
    and "Structural full-diff coverage does not cure an omitted semantic acceptance area" in pr_readiness
    and "explicitly deferred/out-of-lifecycle evidence surface" in pr_readiness,
    "pr-readiness: whole-PR semantic acceptance model / deferred-proof distinction missing",
)
check(
    "loaded `delegation-control` handoff contract" in orch
    and "workflow-specific reconstruction state" in orch
    and "parent-generated technical inference" in orch
    and "preserved end-to-end behavior" in orch
    and "focused/slice-limited/qualified result" in orch
    and "structural change-set coverage" in orch
    and "authoritative acceptance-model coverage" in orch
    and "readiness/publication claim later invalidated by a related material blocker" in orch
    and "Reassess the affected acceptance/ownership model before another local fix/review/transition cycle" in orch
    and "when reopenings repeat, widen the reassessment" in orch,
    "code-orchestrator: root-handoff activation / hypothesis / whole-review / readiness-reversal guards missing",
)
check(
    "whole authoritative acceptance model" in evaluator_sem
    and "parent-generated technical hypotheses" in evaluator_sem
    and "handoff proportionality" in evaluator_sem
    and "decision boundary was explicit" in evaluator_sem
    and "Ready/merge/release authorization" in evaluator_sem,
    "session-evaluator: whole-review/hypothesis/handoff-quality/decision-boundary diagnostics missing",
)

reviewer_sem = text("agents/reviewer.md")
check(
    "exact **decision boundary**" in delegation_sem
    and "does not itself satisfy or authorize a later Ready/merge/release/other transition" in delegation_sem
    and "judgment purpose and downstream decision boundary separately from target identity" in orch
    and "not authorization for that transition" in orch
    and "narrowest decision claim actually established" in reviewer_sem
    and "do not infer satisfaction of a broader lifecycle gate" in reviewer_sem
    and "does **not** itself establish or authorize the Ready transition or any later lifecycle transition" in pr_readiness,
    "independent-judgment decision-boundary / lifecycle-authorization guard missing",
)

# Canonical-owner dedup regression guard. These are historical root-owned formulations
# that must not reappear in code-orchestrator after the v30.90 owner compaction.
for duplicated_root_fragment in [
    "objective and behavioral/target scope",
    "If the original request would allow a materially different approach",
    "Do not run mutation specialists concurrently",
    "Preserve root section 2.2 evidence-state classes",
    "completed / partially completed / blocked / blocked by gate",
    "Docker/systemd/CI/deploy/runtime work -> `@devops`",
]:
    check(
        duplicated_root_fragment not in orch,
        f"code-orchestrator: root-owned semantic duplicate reintroduced: {duplicated_root_fragment}",
    )
check(
    "material participating child-session IDs" not in root_sem,
    "AGENTS.md: conditional terminal evaluator procedure duplicated back into root",
)

check(
    "load `session-evaluation-control`" in orch
    and "Invoke `@session-evaluator` once" in terminal_eval_sem
    and "material participating child-session IDs" in terminal_eval_sem
    and "Do not perform new session-history discovery" in terminal_eval_sem
    and "does not change an already-established terminal state" in terminal_eval_sem
    and "material participating child-session IDs" not in orch,
    "terminal semantic-eval: activation/handoff residency split missing or duplicated",
)

# Semantic ownership is a first-class release gate, not only a historical-fragment blacklist.
skill_control_spec_path = ROOT / "evals/skill-control-spec.json"
skill_control_audit_path = ROOT / "evals/skill-control-audit.py"
skill_control_selftest_path = ROOT / "evals/skill-control-selftest.py"
semantic_owner_spec_path = ROOT / "evals/semantic-ownership-spec.json"
semantic_owner_audit_path = ROOT / "evals/semantic-ownership-audit.py"
semantic_owner_selftest_path = ROOT / "evals/semantic-ownership-selftest.py"
semantic_domain_spec_path = ROOT / "evals/semantic-domain-spec.json"
semantic_domain_audit_path = ROOT / "evals/semantic-domain-audit.py"
semantic_domain_selftest_path = ROOT / "evals/semantic-domain-selftest.py"
section_map_path = ROOT / "evals/root-orchestrator-section-map.json"
section_audit_path = ROOT / "evals/section-ownership-audit.py"
section_selftest_path = ROOT / "evals/section-ownership-selftest.py"
check(skill_control_spec_path.is_file(), "skill control manifest missing")
check(skill_control_audit_path.is_file(), "skill control audit missing")
check(skill_control_selftest_path.is_file(), "skill control selftest missing")
check(semantic_owner_spec_path.is_file(), "semantic ownership manifest missing")
check(semantic_owner_audit_path.is_file(), "semantic ownership audit missing")
check(semantic_owner_selftest_path.is_file(), "semantic ownership selftest missing")
check(semantic_domain_spec_path.is_file(), "semantic domain manifest missing")
check(semantic_domain_audit_path.is_file(), "semantic domain audit missing")
check(semantic_domain_selftest_path.is_file(), "semantic domain selftest missing")
check(section_map_path.is_file(), "root/orchestrator section map missing")
check(section_audit_path.is_file(), "section ownership audit missing")
check(section_selftest_path.is_file(), "section ownership selftest missing")
if semantic_owner_spec_path.is_file():
    import json
    owner_spec = json.loads(semantic_owner_spec_path.read_text(encoding="utf-8"))
    owner_ids = {cap.get("id") for cap in owner_spec.get("capabilities", [])}
    expected_owner_ids = {
        "generic_specialist_handoff_contract", "decision_space_preservation",
        "generic_mutation_parallelism", "proposition_evidence_algebra",
        "generic_routing_defaults", "common_final_report_contract",
        "owned_pr_lifecycle", "session_evaluation_handoff",
        "independent_judgment_decision_boundary",
        "fresh_independent_judgment_isolation", "review_activation_and_reuse",
        "user_decision_binding", "publication_authorization_gate",
        "failed_fix_reset", "repository_resource_workflow",
        "vendor_skill_containment", "memory_authority_and_activation",
        "graymatter_tool_mechanics", "persistent_planning_activation_canonical_state",
        "persistent_planning_fallback_representation", "provenance_receipt_interface",
        "git_provenance_mechanics", "session_evidence_retrieval",
        "verification_evidence_invariants", "verification_layering_and_tester_activation",
        "resource_lifecycle_mechanics", "ui_component_source_ordering_and_vendor_boundary",
        "output_formatting_destination_procedure",
    }
    check(expected_owner_ids <= owner_ids, "semantic ownership manifest lost a declared material shared capability")
check(
    "role executability as inherited shared contract + role-local method" in manual_sem.lower()
    and "second semantically equivalent definition" in manual_sem.lower()
    and "semantic-ownership manifest" in manual_sem.lower()
    and "skill-control-spec.json" in manual_sem.lower()
    and "vendor skill bytes are provenance-preserved" in manual_sem.lower()
    and "typed semantic vocabulary as a separate control plane" in manual_sem.lower()
    and "declared pack-owned/integration skills" in manual_sem.lower()
    and "section-placement map" in manual_sem.lower(),
    "semantic design manual: generic cross-layer ownership/executability method missing",
)
if semantic_domain_spec_path.is_file():
    domain_spec = json.loads(semantic_domain_spec_path.read_text(encoding="utf-8"))
    domain_ids = {d.get("id") for d in domain_spec.get("domains", [])}
    check({"evidence_status", "proposition_relation", "semantic_checkpoint_verdict", "trajectory_verdict",
           "resource_lifecycle_terminal_state", "owned_pr_lifecycle_state"} <= domain_ids,
          "semantic domain manifest lost a typed state/verdict/lifecycle domain")
check(
    "`insufficient-evidence` — available primary session evidence is insufficient" in trajectory_sem
    and "`unverified` — available primary session evidence is insufficient" not in trajectory_sem,
    "trajectory-auditor: evidence-state literal still reused as workflow verdict",
)
check(
    "resource-specific workflow mechanics belong to the selected role/skill" in workflow_entry_sem.lower()
    and "repository resources such as PRs/issues/releases" in workflow_entry_sem
    and "Issue/ticket/report outcome" not in root_sem
    and "search existing issues" not in root_sem.lower()
    and "### Code-host resource workflow" in code_orchestrator_sem
    and "load `repository-workflow`" in code_orchestrator_sem
    and "## Existing PR follow-up" in code_host_sem
    and "## Issue / ticket / report" in code_host_sem
    and "Search existing issues" in code_host_sem
    and "## Release / host publication" in code_host_sem,
    "root/workflow-control/code-orchestrator/repository-workflow: resource workflow mechanics are not correctly layered",
)
traces_owner_sem = text("evals/semantic-transition-traces.md")
check(
    "consistent consumer duplicate is still a semantic-ownership regression" in traces_owner_sem.lower()
    and "inherited shared contract + role-local method" in traces_owner_sem.lower(),
    "semantic transition traces: ST-120 semantic-owner duplicate regression missing",
)

# Longitudinal trajectory auditing is a separate second-opinion lifecycle:
# owner must first reassess its own model, while the auditor independently checks only
# the residual longitudinal question against primary session evidence.
check(
    "current user-authorized task anchor" in trajectory_sem
    and "workflow-owner report and index, not independent proof" in trajectory_sem
    and "acceptance progress" in trajectory_sem
    and "enabling progress" in trajectory_sem
    and "diagnostic progress" in trajectory_sem
    and "hypothesis laundering" in trajectory_sem
    and "classify the relevant blockers as `independent` or `clustered`" in trajectory_sem
    and "classification evidence `unverified`" in trajectory_sem
    and "`report-only`, `pre-existing`, or locally `out-of-scope`" in trajectory_sem
    and "Do not let local severity" in trajectory_sem
    and "existing files/functions/call sites as evidence" in trajectory_sem
    and "does **not** mean the architecture is wrong" in trajectory_sem,
    "trajectory-auditor: anchor/primary-evidence/progress/cluster method missing",
)
check(
    "longitudinal **second opinion**" in trajectory_sem
    and "owner reassessment performed" in trajectory_sem
    and "exact unresolved trajectory question" in trajectory_sem
    and "why available primary evidence could not safely resolve" in trajectory_sem
    and "does not create task authority" in trajectory_sem
    and "serve as the first-line mechanism" in trajectory_sem,
    "trajectory-auditor: second-opinion invocation boundary missing",
)
check(
    "Return exactly one workflow verdict" in trajectory_sem
    and "`continue` — the proposed next transition is consistent" in trajectory_sem
    and "`reanchor` — the current workflow framing has materially" in trajectory_sem
    and "`reassess` — cumulative evidence no longer justifies" in trajectory_sem
    and "`checkpoint-required` — the proposed next transition would treat" in trajectory_sem
    and "`insufficient-evidence` — available primary session evidence is insufficient" in trajectory_sem
    and "remain `unverified` as evidence state" in trajectory_sem
    and "Do not propose replacement implementation" in trajectory_sem
    and "Do not classify prompt/instruction defects" in trajectory_sem
    and "Audit the trajectory, not the repository" in trajectory_sem
    and "`proceed/hold/insufficient-context`" in trajectory_sem,
    "trajectory-auditor: bounded verdict/ownership/checkpoint-contract missing",
)
check(
    "retain a compact **task anchor** across stages" in code_orchestrator_sem
    and "correction epoch" in code_orchestrator_sem
    and "cumulative counterexamples to the same classifier, normalizer, policy, or semantic boundary" in code_orchestrator_sem
    and "`report-only`, `pre-existing`, or leaf-reported `out-of-scope`" in code_orchestrator_sem
    and "bounded owner trajectory reassessment yourself" in code_orchestrator_sem
    and "If that bounded reassessment yields one evidence-backed model" in code_orchestrator_sem
    and "fresh `@trajectory-auditor` only when" in code_orchestrator_sem
    and "exact longitudinal question remains unresolved after the owner reassessment" in code_orchestrator_sem
    and "packet is a workflow-owner report, not proof" in code_orchestrator_sem
    and "`checkpoint-required` routes the exact unresolved semantic-authority proposition" in code_orchestrator_sem,
    "code-orchestrator: owner-first longitudinal control/verdict-consumption contract missing",
)
check(
    "independent authority-sensitive pre-mutation semantic gate" in checkpoint_sem
    and "owner reconciliation performed" in checkpoint_sem
    and "exact semantic proposition whose authority remains unresolved" in checkpoint_sem
    and "Ordinary technical owner/fix-level/abstraction decisions are not a reason to invoke you" in checkpoint_sem
    and "technical ownership, fix-level, shared-abstraction, invariant-representation, or necessary implementation-scope change is not by itself a semantic choice" in checkpoint_sem,
    "semantic-checkpoint: residual-authority/anti-overreach invocation contract missing",
)
check(
    "workflow-owner synthesis" in evaluator_sem
    and "specialist pass-through" in evaluator_sem
    and "controller dependence" in evaluator_sem
    and "independently determined the next required question/action" in evaluator_sem
    and "Workflow-owner quality" in evaluator_sem,
    "session-evaluator: accountable-owner/controller-use audit missing",
)

# Cross-role mutation handoffs must preserve role ownership instead of laundering
# upstream planning/checkpoint/review recommendations into implementation recipes.
checkpoint_sem = text("agents/semantic-checkpoint.md")
debugger_sem = text("agents/debugger.md")
ui_orch_sem = text("agents/ui-orchestrator.md")
ui_impl_sem = text("agents/ui-implementer.md")
check(
    "do not certify a concrete implementation mechanism, patch shape, technical owner, or technical design as correct" in checkpoint_sem
    and "does not certify design/implementation adequacy" in checkpoint_sem
    and "Remaining implementation uncertainty belongs to the implementation role" in checkpoint_sem
    and "## Result" in checkpoint_sem
    and "**Mutation boundary**" in checkpoint_sem
    and "Do not recommend forwarding the candidate or checkpoint report unchanged as an implementation recipe" in checkpoint_sem
    and "Candidate handoff" not in checkpoint_sem,
    "semantic-checkpoint: semantic authorization still leaks into implementation certification/recipe",
)
check(
    ("Keep unresolved mechanisms non-binding in edit-capable handoffs" in orch or "omit non-required mechanisms unless they are materially necessary factual context" in orch)
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
    "case-to-verification map concrete **before selecting the fix**" in debugger_sem
    and "materially different representative capable of falsifying the current root-cause/fix hypothesis" in debugger_sem
    and "external grammar/API/tool/runtime or target environment" in debugger_sem
    and "do not implement it merely because the assignment says so" in debugger_sem
    and "multiple self-authored tests that share the same implementation assumption" in debugger_sem
    and "as closure" in debugger_sem
    and "target-condition evidence" in debugger_sem,
    "debugger: cross-class falsification/contradictory-handoff/target-fidelity gate missing",
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
ui_route = text("skills/ui-routing-control/SKILL.md")
check(
    "load `ui-routing-control`" in orch
    and "settled user-visible outcome" in ui_route
    and "unresolved presentation/interaction direction" in ui_route
    and "functional requirement alone does not make the ui outcome settled" in ui_route.lower()
    and "rejects the current treatment without adopting a replacement" in ui_route.lower()
    and "delegate the bounded UI domain to `@ui-orchestrator`" in ui_route
    and "Do not invent a missing UI/product direction" in ui_route
    and "route directly to `@ui-implementer`" in ui_route,
    "code-to-UI route: unresolved UI direction can still be fabricated into a direct implementation handoff",
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
    "@librarian" in delegation_sem
    and "@librarian" in text("agents/code-orchestrator.md")
    and "@librarian" in text("agents/auditor.md"),
    "librarian: intended delegation-control/orchestrator/auditor routing surfaces missing",
)

# Release-gate audit surfaces are separate from the legacy static presence harness.
contract_audit = text("evals/contract-protocol-audit.py")
contract_spec = text("evals/contract-protocol-spec.json")
contract_selftest = text("evals/contract-protocol-selftest.py")
release_gates = text("evals/run-release-gates.py")
check("inherited shared contract + role-local method" in contract_spec and "second consistent definition" in contract_spec and "Ownership -> Invocation -> Method -> Boundaries -> Result" in contract_spec and "producer output, parent transformation, consumer input" in contract_spec and "Keyword presence" in contract_spec, "contract/protocol spec missing semantic-owner/semantic-shape/adversarial audit principles")
check("CONTRACT / PROTOCOL AUDIT v3" in contract_audit and "missing essential profile core-loop capabilities" in contract_audit and "REVIEW is intentionally release-blocking" in contract_audit and "Prompt length is diagnostic only" in contract_audit, "contract audit v3 severity/core-loop/review gate missing")
check("keyword-stuffed implementation role was not rejected" in contract_selftest and "thin ops role without diagnostic isolation" in contract_selftest and "five-heading shell without executable implementation method was not rejected" in contract_selftest and "compact executable discovery role" in contract_selftest and "without five standardized headings" in contract_selftest and "audit orchestrator missing only reconciliation" in contract_selftest and "producer-side implementation certification" in contract_selftest and "new role without executable-contract audit profile did not block release" in contract_selftest and "stale role profile did not block release" in contract_selftest and "thin external research role without version/conflict applicability loop was not rejected" in contract_selftest and "complete external-research contract should PASS" in contract_selftest, "contract audit v3 synthetic anti-gaming/severity/lifecycle/semantic-shape/external-research selftests missing")
edge_audit = text("evals/role-handoff-audit.py")
edge_selftest = text("evals/role-handoff-selftest.py")
release_gates = text("evals/run-release-gates.py")
check("Closed-world static audit" in edge_audit and "EDGE_CLASSIFICATION" in edge_audit and "UNCLASSIFIED EDGE" in edge_audit and "STALE EDGE" in edge_audit and "ui-orchestrator','a11y-reviewer" in edge_audit and "code-orchestrator','devops" in edge_audit and "auditor','specialists" in edge_audit and "code-orchestrator','librarian" in edge_audit and "auditor','librarian" in edge_audit, "role-handoff closed-world inventory/profiles missing")
check("recipe-shaped devops handoff not rejected" in edge_selftest and "unbound a11y handoff not rejected" in edge_selftest and "preselected UI planning handoff not rejected" in edge_selftest and "unbounded auditor specialist handoff not rejected" in edge_selftest and "new unclassified handoff edge did not block release" in edge_selftest and "stale handoff classification did not block release" in edge_selftest and "unbound librarian handoff not rejected" in edge_selftest and "auditor librarian authority/applicability omission not rejected" in edge_selftest, "role-handoff synthetic anti-gaming/inventory/external-research selftests missing")
check("skill control selftest" in release_gates and "skill control audit" in release_gates, "release gate runner missing skill-control checks")
check("role-handoff selftest" in release_gates and "role-handoff edge audit" in release_gates, "release gate runner missing role-handoff checks")
check("workflow path selftest" in release_gates and "workflow path audit" in release_gates, "release gate runner missing workflow-path checks")

check("unresolved findings must not be waived merely to obtain PASS" in release_gates, "release gate aggregator may waive unresolved contract findings")
check("Role lifecycle requalification" in text("docs/semantic-design-manual.md") and "method-preservation test" in text("docs/semantic-design-manual.md") and "closed-world discovered handoff inventory" in text("docs/semantic-design-manual.md"), "semantic-design manual missing role lifecycle/method-preservation/closed-world edge audit")
check("Role contract semantic shape" in text("docs/semantic-design-manual.md") and "Ownership → Invocation → Method → Boundaries → Result" in text("docs/semantic-design-manual.md") and "not a five-heading template" in text("docs/semantic-design-manual.md"), "semantic-design manual missing semantic role-contract shape / anti-template rule")

# Current semantic literal axes must remain type-distinct.
check(
    "exactly `proceed`, `hold`, or `insufficient-context`" in checkpoint_sem
    and "`unverified` — available evidence is insufficient" in checkpoint_sem
    and "`indeterminate`" in checkpoint_sem
    and "distinct from `unverified` evidence status and `indeterminate` proposition relation" in checkpoint_sem
    and "`hold` or `insufficient-context` blocks mutation" in code_orchestrator_sem,
    "semantic-checkpoint/code-orchestrator: verdict, evidence status, and proposition relation are not type-stable",
)
check(
    "`preserved`, `refined`, `strengthened`, `weakened`, `substituted`, or `indeterminate`" in evaluator_sem
    and "mark only conclusions depending on that branch `unverified`" in evaluator_sem,
    "session-evaluator: proposition relation still conflates with evidence uncertainty",
)

# Project planning representation belongs to persistent-planning; an unwritable project canonical owner must not fork.
check(
    "When the caller or loaded `workflow-control` activates durable planning" in planner_sem
    and "load `persistent-planning` for fallback representation/resume mechanics" in planner_sem
    and "Read that artifact as authoritative state" in planner_sem
    and "instead of creating a parallel plan solely because the canonical owner is not writable here" in planner_sem
    and "Persistent planning activation" in workflow_entry_sem,
    "project-planner/workflow-control: persistent-planning ownership or unwritable canonical-owner composition missing",
)

# Explore must defend against false absence/flow claims rather than passing on size/keywords alone.
check(
    "not found within <searched scope>" in explore_sem
    and "never collapse `not searched` into `not found`" in explore_sem
    and "corroborate the actual edge" in explore_sem
    and "similar names, nearby files" in explore_sem,
    "explore: negative-claim/flow corroboration false-success defense missing",
)

# Installer ownership/preservation and licensing surfaces are release-critical package semantics.
global_installer = text("install/install-global.sh")
project_installer = text("install/install-project.sh")
release_runner = text("evals/run-release-gates.py")
license_text = text("LICENSE")
third_party = text("THIRD_PARTY_NOTICES.md")
check(
    "Copyright (c) 2026 bashrusakh (https://github.com/bashrusakh)" in license_text
    and "MIT License" in license_text
    and "Jeffallan" in third_party
    and "open-code-review" in third_party
    and "ui-ux-pro-max" in third_party,
    "package licensing/third-party attribution surfaces missing",
)
check(
    "OPENCODE_AGENT_PACK_REPLACE_GLOBAL_AGENTS" in global_installer
    and "Refusing to replace an existing global" in global_installer
    and "managed-files.sha256" in global_installer
    and "filename is not ownership proof" in global_installer,
    "global installer: ownership/backup/preserve semantics missing",
)
check(
    "project-owned ./AGENTS.md" in project_installer
    and "no recognizable global OpenCode Agent Pack root" in project_installer
    and "Preserved existing project-owned AGENTS.md" in project_installer
    and "managed-files.sha256" in project_installer
    and "filename is not ownership proof" in project_installer,
    "project installer: project-root preservation/ownership semantics missing",
)
check(
    "installer-safety-selftest.py" in release_runner,
    "release gates: installer safety selftest not wired into aggregate gates",
)
check(
    "package runner does not bypass a new-tooling/install gate" in workflow_entry_sem.lower()
    and "new dependencies/tooling/design systems/large generated assets" in workflow_entry_sem
    and "third-party/vendor skills are advisory provider/domain guidance" in root_sem.lower(),
    "workflow-control/root containment: package-runner or vendor skill can bypass new-tooling authorization",
)

# Temporary transition-eval structure guards. These prove only that the replay
# contract is explicit enough to run consistently; they do not prove behavior.
traces = text("evals/semantic-transition-traces.md")
check(traces.count("### ST-") == 141, "semantic-transition suite must contain 141 cases")
for field in [
    "**Initial user/spec fixture:**",
    "**Runtime/repository fixture:**",
    "**Injected intermediate output:**",
    "**Expected earliest observable stop/preservation point:**",
]:
    check(traces.count(field) == 141, f"semantic-transition suite missing per-case field: {field}")
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
    "gate verdict, evidence status, and proposition relation must remain type-distinct" in traces.lower()
    and "insufficient-context" in traces
    and "proposition relation is `indeterminate`" in traces,
    "ST-76 typed semantic-state regression missing",
)
check(
    "repository discovery must falsify material negative and flow claims" in traces.lower()
    and "not found within <searched scope>" in traces
    and "not searched" in traces
    and "actual caller/reference/consumer/transition edge" in traces,
    "ST-77 discovery negative/flow regression missing",
)
check(
    "canonical project planning state outside planner write paths must not fork into a parallel plan" in traces.lower()
    and "roadmap.md" in traces.lower()
    and "persistent-planning" in traces.lower(),
    "ST-78 persistent-planning composition regression missing",
)
check(
    "unresolved ui direction must not be fabricated into a settled direct-implementation handoff" in traces.lower()
    and "functional requirement alone" in traces.lower()
    and "delegate the bounded ui domain to `@ui-orchestrator`" in traces.lower()
    and "direct `@ui-implementer`" in traces.lower()
    and "existing project pattern" in traces.lower(),
    "ST-79 UI routing discriminator regression missing",
)
check(
    "debugger must not execute a contradictory lower-authority fix constraint merely because it is explicit" in traces.lower()
    and "reset the diagnosis/fix hypothesis" in traces.lower()
    and "preservation counterexample" in traces.lower(),
    "ST-80 debugger contradictory-handoff regression missing",
)
check(
    "debugger evidence must preserve a material target-environment condition" in traces.lower()
    and "green local surrogate" in traces.lower()
    and "target fidelity" in traces.lower(),
    "ST-81 debugger target-environment fidelity regression missing",
)
check(
    "non-reproducing diagnostic probe must not confirm the hypothesized root cause" in traces.lower()
    and "absence of falsification is not causal confirmation" in traces.lower()
    and "keep root cause unverified" in traces.lower(),
    "ST-82 debugger non-reproducing-diagnosis regression missing",
)
check(
    "reviewer must not accept correlated self-tests as proof of an external grammar or protocol claim" in traces.lower()
    and "independent oracle" in traces.lower()
    and "correlated self-tests alone" in traces.lower(),
    "ST-83 reviewer correlated-evidence regression missing",
)
check(
    "opaque external-provider failure must not become a confirmed fix recipe before discriminating evidence" in traces.lower()
    and "generic provider error establishes the symptom" in traces.lower()
    and "preserve uncertainty" in traces.lower(),
    "ST-84 orchestrator opaque-provider-failure regression missing",
)
check(
    "st-85 — local correction success must trigger owner reassessment before another same-level patch" in traces.lower()
    and "perform one bounded owner trajectory reassessment" in traces.lower()
    and "without `trajectory-auditor`" in traces.lower(),
    "ST-85 owner-first local-success/global-nonprogress regression missing",
)
check(
    "st-86 — repeated hypothesis handoffs must not launder a parent inference into root cause" in traces.lower()
    and "keep h as hypothesis" in traces.lower()
    and "semantic-checkpoint` is not used merely to decide a technical root cause" in traces.lower(),
    "ST-86 owner hypothesis-laundering regression missing",
)
check(
    "st-87 — terminal completion must preserve the original end-to-end acceptance" in traces.lower()
    and "restore the original completion boundary in the owner model" in traces.lower(),
    "ST-87 owner completion-erosion regression missing",
)
check(
    "st-88 — scoped review success must remain scoped evidence under parent synthesis" in traces.lower()
    and "end-to-end effect unverified" in traces.lower(),
    "ST-88 scoped-review/e2e evidence regression missing",
)
check(
    "st-89 — clustered correction failures require owner boundary-level reassessment" in traces.lower()
    and "owner reconstructs the material chain" in traces.lower()
    and "if materially plausible models remain unresolved" in traces.lower(),
    "ST-89 owner clustered-correction regression missing",
)
check(
    "st-90 — independent correction failures must remain a direct-flow counterexample" in traces.lower()
    and "no trajectory auditor" in traces.lower(),
    "ST-90 independent-defects anti-overreach regression missing",
)
check(
    "st-91 — explicit staged work must not be misclassified as global non-progress" in traces.lower()
    and "continue to the next established stage without a trajectory audit" in traces.lower(),
    "ST-91 staged-work anti-overreach regression missing",
)
check(
    "st-92 — a prior trajectory `continue` verdict must not become sticky authority" in traces.lower()
    and "perform fresh owner reassessment" in traces.lower()
    and "only if a material longitudinal question still remains unresolved" in traces.lower(),
    "ST-92 owner-freshness/conditional-auditor regression missing",
)
check(
    "st-93 — the parent trajectory packet is an index, not primary proof" in traces.lower()
    and "after owner reassessment leaves a real residual trajectory question" in traces.lower()
    and "primary session history" in traces.lower(),
    "ST-93 second-opinion parent-packet evidence regression missing",
)
check(
    "st-94 — an isolated ordinary correction must not trigger controller ceremony" in traces.lower()
    and "route directly to `@debugger`" in traces.lower(),
    "ST-94 controller anti-ritual routing regression missing",
)
check(
    "st-95 — same-policy report-only/pre-existing counterexamples require owner abstraction reassessment" in traces.lower()
    and "reassess canonical owner/representation/invariant" in traces.lower()
    and "if materially plausible models remain" in traces.lower(),
    "ST-95 same-policy owner-reassessment regression missing",
)
check(
    "st-96 — unrelated low/pre-existing notes must not force abstraction reassessment or audit" in traces.lower()
    and "independent/unrelated" in traces.lower()
    and "no invented helper/planner/controller stage" in traces.lower(),
    "ST-96 residual-note anti-overreach regression missing",
)
check(
    "st-97 — a specialist recommendation must not become the next workflow stage by pass-through" in traces.lower()
    and "independently owns the transition" in traces.lower(),
    "ST-97 specialist-pass-through regression missing",
)
check(
    "st-98 — fact, hypothesis, and remediation must remain distinct during owner ingestion" in traces.lower()
    and "record f as evidence, h/h2 as hypotheses, r as recommendation" in traces.lower(),
    "ST-98 owner-ingestion epistemic-class regression missing",
)
check(
    "st-99 — evidence-backed technical ownership/fix-level change must not require semantic checkpoint" in traces.lower()
    and "no semantic checkpoint merely because fix level" in traces.lower(),
    "ST-99 semantic-checkpoint technical-owner anti-overreach regression missing",
)
check(
    "st-100 — residual semantic authority conflict requires semantic checkpoint" in traces.lower()
    and "owner states reconciliation performed" in traces.lower()
    and "invoke fresh `@semantic-checkpoint`" in traces.lower(),
    "ST-100 residual-authority checkpoint regression missing",
)
check(
    "st-101 — two plausible trajectory models remaining after owner reassessment require second opinion" in traces.lower()
    and "exact unresolved trajectory question" in traces.lower()
    and "cannot safely resolve" in traces.lower(),
    "ST-101 residual-trajectory second-opinion regression missing",
)
check(
    "st-102 — explicit user request for independent trajectory review remains sufficient invocation authority" in traces.lower()
    and "explicit user-requested independence" in traces.lower(),
    "ST-102 user-requested trajectory-audit regression missing",
)
check(
    "st-103 — a locally excellent deliverable that violates the task anchor must be rejected by the owner" in traces.lower()
    and "reject completion/transition" in traces.lower(),
    "ST-103 whole-task owner-protection regression missing",
)
check(
    "st-104 — session evaluator must diagnose specialist pass-through and controller dependence" in traces.lower()
    and "workflow-owner quality" in traces.lower()
    and "controller dependence" in traces.lower(),
    "ST-104 post-hoc owner-quality regression missing",
)
check(
    "st-105 — narrow factual reconciliation should not create an unnecessary subagent chain" in traces.lower()
    and "inspect the narrow primary evidence" in traces.lower(),
    "ST-105 bounded direct-reconciliation regression missing",
)
check(
    "st-106 — owner synthesis must be bounded rather than recursive think-loop" in traces.lower()
    and "one bounded ingest/reconcile/update/decide pass" in traces.lower(),
    "ST-106 anti-think-loop owner regression missing",
)
check(
    "st-107 — parent-derived investigative direction must not steer a fresh whole-change review" in traces.lower()
    and "request a clean assignment" in traces.lower()
    and "targeted partial re-review" in traces.lower(),
    "ST-107 fresh whole-change investigative-context isolation regression missing",
)
check(
    "st-108 — authoritative review emphasis is additive, not a whole-review boundary" in traces.lower()
    and "additive and non-exhaustive" in traces.lower(),
    "ST-108 explicit-emphasis preservation regression missing",
)
check(
    "st-109 — fresh reviewer derives investigation method independently" in traces.lower()
    and "regardless of wording, placement, formatting, or label" in traces.lower(),
    "ST-109 method-seeding regression missing",
)
check(
    "st-110 — parent provenance label does not create review authority" in traces.lower()
    and "locator, not proof" in traces.lower(),
    "ST-110 provenance-laundering regression missing",
)
check(
    "st-111 — available recall capability does not contaminate a fresh review" in traces.lower()
    and "capability availability" in traces.lower()
    and "without prior-task recall" in traces.lower(),
    "ST-111 capability-not-exposure regression missing",
)
check(
    "st-112 — actually exposed prior-task steering still contaminates fresh review" in traces.lower()
    and "automatic context injection" in traces.lower()
    and "request a clean" in traces.lower(),
    "ST-112 actual-exposure contamination regression missing",
)
check(
    "st-113 — fresh independent reviewer must not recover parent-task memory" in traces.lower()
    and "continuity belongs to the workflow owner" in traces.lower(),
    "ST-113 fresh-review parent-memory-recovery regression missing",
)
check(
    "st-114 — whole-pr target requires a whole authoritative acceptance model" in traces.lower()
    and "whole structural diff coverage does not manufacture missing semantic acceptance authority" in traces.lower(),
    "ST-114 whole-target/partial-acceptance regression missing",
)
check(
    "st-115 — qualified slice verdict must not be promoted into whole readiness" in traces.lower()
    and "structural diff coverage from semantic acceptance-model coverage" in traces.lower(),
    "ST-115 qualifier-laundering regression missing",
)
check(
    "st-116 — parent technical inference must not become a preserved requirement or test oracle" in traces.lower()
    and "parent hypotheses are evidence/inferences, not task authority" in traces.lower(),
    "ST-116 parent-hypothesis laundering regression missing",
)
check(
    "st-117 — specialist handoff must be minimally sufficient and reconstructable" in traces.lower()
    and "concision is not permission to destroy semantic distinctions" in traces.lower(),
    "ST-117 handoff-ergonomics regression missing",
)
check(
    "st-118 — related blocker after readiness reopens the owner model before another local cycle" in traces.lower()
    and "readiness reversal is trajectory evidence" in traces.lower(),
    "ST-118 readiness-reversal owner-reassessment regression missing",
)
check(
    "st-119 — independent review verdict must stay bound to its downstream decision boundary" in traces.lower()
    and "review pass" in traces.lower()
    and "later lifecycle authorization" in traces.lower(),
    "ST-119 review-verdict/lifecycle-boundary regression missing",
)
check(
    "st-120 — a consistent consumer duplicate is still a semantic-ownership regression" in traces.lower()
    and "second shared definition" in traces.lower()
    and "inherited shared contract + role-local method" in traces.lower(),
    "ST-120 semantic-owner duplicate regression missing",
)
check(
    "st-121 — evidence-status literal must not become a workflow verdict" in traces.lower()
    and "typed semantic-domain audit" in traces.lower()
    and "insufficient-evidence" in traces.lower(),
    "ST-121 typed semantic-domain collision regression missing",
)
check(
    "st-122 — adjacent issue and pr workflow mechanics share one conditional resource owner" in traces.lower()
    and "`repository-workflow`" in traces.lower()
    and "`pr-readiness` remains the canonical owner" in traces.lower(),
    "ST-122 issue/PR workflow-placement regression missing",
)
check(
    "st-123 — pack-owned skill cannot become an undeclared second semantic owner" in traces.lower()
    and "conditional loading does not permit a skill to become a second owner" in traces.lower(),
    "ST-123 pack-skill ownership regression missing",
)
check(
    "st-124 — typed semantic collision inside a pack-owned skill is a release failure" in traces.lower()
    and "skill-side collisions bypass the domain gate" in traces.lower(),
    "ST-124 pack-skill typed-domain regression missing",
)
check(
    "st-125 — vendor skill content remains subordinate to the pack integration boundary" in traces.lower()
    and "vendor subtree remains unchanged" in traces.lower(),
    "ST-125 vendor containment regression missing",
)
check(
    "st-126 — root-owned canonical state and skill-owned procedure must not collapse into duplicate policy" in traces.lower()
    and "inherited shared contract + skill-local procedure" in traces.lower(),
    "ST-126 root/skill ownership split regression missing",
)
check(
    "st-127 — correct ownership does not justify universal residency" in traces.lower()
    and "canonical ownership and prompt residency are independent design decisions" in traces.lower(),
    "ST-127 residency/ownership separation regression missing",
)
check(
    "st-128 — `mode: all` delegated invocation must not inherit primary-owner contracts" in traces.lower()
    and "capability to be primary does not make every invocation primary" in traces.lower(),
    "ST-128 delegated mode:all residency regression missing",
)
check(
    "st-129 — implementation procedure must be conditional without disappearing from implement/judge roles" in traces.lower()
    and "progressive disclosure must reduce unused context without deleting load-bearing engineering invariants" in traces.lower(),
    "ST-129 conditional implementation residency regression missing",
)
check(
    "st-130 — residency relocation must preserve universal hypothesis and required-skill semantics" in traces.lower()
    and "first plausible framing" in traces.lower()
    and "required skill" in traces.lower(),
    "ST-130 relocation preservation regression missing",
)
check(
    "st-131 — workflow-control relocation must preserve broad-scope and confidence consequences" in traces.lower()
    and "broad scope" in traces.lower()
    and "likely" in traces.lower()
    and "ambiguous" in traces.lower(),
    "ST-131 workflow-control preservation regression missing",
)
check(
    "st-132 — fresh-judgment and complexity escalation semantics survive progressive disclosure" in traces.lower()
    and "manufacture freshness" in traces.lower()
    and "complexity/design escalation" in traces.lower(),
    "ST-132 delegated/implementation preservation regression missing",
)
check(
    "st-133 — owned-pr identity and publication evidence semantics survive resource relocation" in traces.lower()
    and "branch name alone" in traces.lower()
    and "repository-host metadata" in traces.lower()
    and "publication blocked" in traces.lower(),
    "ST-133 owned-PR/publication preservation regression missing",
)
check(
    "st-134 — repository resource procedure must not be resident in ordinary code-orchestrator sessions" in traces.lower()
    and "do not load `repository-workflow`" in traces.lower(),
    "ST-134 repository-resource residency regression missing",
)
check(
    "st-135 — repository workflow composes with pr readiness instead of absorbing its state machine" in traces.lower()
    and "`pr-readiness` owns owned pr identity plus draft/candidate/ready lifecycle" in traces.lower()
    and "no duplicate pr lifecycle" in traces.lower(),
    "ST-135 repository-workflow/pr-readiness composition regression missing",
)
check(
    "proposition relation: `preserved | refined | strengthened | weakened | substituted | indeterminate`" in traces,
    "semantic-transition suite proposition-relation axis missing or still conflated with evidence status",
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

check(
    "ST-136" in traces and "session-evaluation-control" in traces and "standing orchestrator context" in traces,
    "ST-136 terminal semantic-eval residency regression missing",
)
check(
    "ST-137" in traces and "completion/readiness gate" in traces and "preserve terminal task state" in traces and "without laundering it into product acceptance authority" in traces,
    "ST-137 terminal diagnostic non-gating regression missing",
)
check(
    "ST-138" in traces and "ui-routing-control" in traces and "conditionally disclosed" in traces,
    "ST-138 UI routing conditional-residency regression missing",
)
check(
    "ST-139" in traces and "leaf result + exact updated target/state" in traces and "return to `ui-orchestrator`" in traces,
    "ST-139 delegated UI reconciliation-loop regression missing",
)
check(
    "ST-140" in traces and "governing expected behavior/invariant" in traces and "suspected root cause/remediation remains non-binding" in traces,
    "ST-140 debugger failure-contract handoff regression missing",
)
check(
    "ST-141" in traces and "workflow-path release gate" in traces and "producer omits target/state/authority/evidence" in traces,
    "ST-141 end-to-end workflow composition regression missing",
)

if failures:
    print("STATIC POLICY REGRESSIONS: FAIL")
    for item in failures:
        print(f"- {item}")
    sys.exit(1)
print(f"STATIC POLICY REGRESSIONS: PASS ({len(agents)} agents; schema/dependency/blocker/product/PR/resource/UI/reviewer/eval guards)")
