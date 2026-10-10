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
check(len(agents) == 17, f"expected 17 agents, found {len(agents)}")
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
semantic_runtime = "\n".join([root_sem, checkpoint_sem, evaluator_sem])
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


# Temporary transition-eval structure guards. These prove only that the replay
# contract is explicit enough to run consistently; they do not prove behavior.
traces = text("evals/semantic-transition-traces.md")
check(traces.count("### ST-") == 18, "semantic-transition suite must contain 18 cases")
for field in [
    "**Initial user/spec fixture:**",
    "**Runtime/repository fixture:**",
    "**Injected intermediate output:**",
    "**Expected earliest observable stop/preservation point:**",
]:
    check(traces.count(field) == 18, f"semantic-transition suite missing per-case field: {field}")
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

if failures:
    print("STATIC POLICY REGRESSIONS: FAIL")
    for item in failures:
        print(f"- {item}")
    sys.exit(1)
print(f"STATIC POLICY REGRESSIONS: PASS ({len(agents)} agents; schema/dependency/blocker/product/PR/resource/UI/eval guards)")
