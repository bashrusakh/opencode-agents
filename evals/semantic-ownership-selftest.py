#!/usr/bin/env python3
"""Synthetic anti-gaming fixtures for semantic-ownership-audit.py."""
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
module_spec = importlib.util.spec_from_file_location("semantic_ownership_audit", HERE / "semantic-ownership-audit.py")
mod = importlib.util.module_from_spec(module_spec)
assert module_spec and module_spec.loader
module_spec.loader.exec_module(mod)


def write_fixture(root: Path, consumer: str, owner: str | None = None, mode: str = "reference") -> Path:
    (root / "roles").mkdir(parents=True, exist_ok=True)
    owner_text = owner or "Canonical owner defines a bounded shared delegation packet with a goal and stopping boundary.\n"
    (root / "ROOT.md").write_text(owner_text, encoding="utf-8")
    (root / "roles/consumer.md").write_text(consumer, encoding="utf-8")
    caps = []
    # Keep five minimal capabilities so manifest-size anti-no-op protection is exercised.
    for idx in range(5):
        caps.append({
            "id": f"cap_{idx}",
            "owner": "ROOT.md",
            "owner_signature": [["Canonical owner"]],
            "consumers": [{
                "path": "roles/consumer.md",
                "mode": mode,
                "activation_signature": [["inherits shared delegation contract"]],
                "forbidden_redefinition": {
                    "window_lines": 8,
                    "groups": [
                        ["goal", "objective"],
                        ["scope", "target"],
                        ["action ceiling", "allowed action"],
                        ["evidence", "deliverable"],
                        ["stop", "escalat"]
                    ]
                }
            }]
        })
    spec_path = root / "spec.json"
    spec_path.write_text(json.dumps({"schema_version": 1, "capabilities": caps}), encoding="utf-8")
    return spec_path


def expect(ok: bool, message: str):
    if not ok:
        raise AssertionError(message)


with tempfile.TemporaryDirectory(prefix="semantic-owner-selftest-") as td:
    base = Path(td)

    clean = base / "clean"; clean.mkdir()
    spec = write_fixture(clean, "This role inherits shared delegation contract. It adds only a role-local execution loop.\n")
    expect(not mod.audit(clean, spec), "clean owner->consumer reference should pass")

    dup = base / "duplicate"; dup.mkdir()
    # Deliberately paraphrased rather than copied from the owner. Behavior could be
    # perfectly consistent, but the consumer has become a second policy definition.
    spec = write_fixture(
        dup,
        "This role inherits shared delegation contract.\n"
        "Every handoff must state its objective, target scope, allowed action ceiling, expected evidence deliverable, and stop/escalation boundary.\n",
    )
    findings = mod.audit(dup, spec)
    expect(any("consumer redefines owner semantic family" in f for f in findings), "paraphrased duplicate was not rejected")

    missing_ref = base / "missing-ref"; missing_ref.mkdir()
    spec = write_fixture(missing_ref, "Role-local method only.\n")
    findings = mod.audit(missing_ref, spec)
    expect(any("does not activate/reference" in f for f in findings), "missing owner activation was not rejected")

    missing_owner = base / "missing-owner"; missing_owner.mkdir()
    spec = write_fixture(missing_owner, "This role inherits shared delegation contract.\n", owner="Owner text no longer defines the declared semantic family.\n")
    findings = mod.audit(missing_owner, spec)
    expect(any("owner no longer carries" in f for f in findings), "owner drift was not rejected")

    specialize = base / "specialize"; specialize.mkdir()
    spec = write_fixture(
        specialize,
        "This role inherits shared delegation contract. It specializes the domain with a local risk discriminator and evidence threshold.\n",
        mode="specialize",
    )
    expect(not mod.audit(specialize, spec), "role-local specialization without shared-policy redefinition should pass")

    skilldup = base / "skill-duplicate"; skilldup.mkdir()
    (skilldup / "roles").mkdir(); (skilldup / "skills/helper").mkdir(parents=True); (skilldup / "evals").mkdir()
    (skilldup / "ROOT.md").write_text("Canonical owner defines shared handoff policy.\n", encoding="utf-8")
    (skilldup / "roles/consumer.md").write_text("This role inherits shared delegation contract.\n", encoding="utf-8")
    (skilldup / "skills/helper/SKILL.md").write_text(
        "# Helper\n\nEvery handoff states its objective, target scope, allowed action ceiling, expected evidence deliverable, and stop/escalation boundary.\n", encoding="utf-8")
    caps=[]
    for idx in range(5):
        caps.append({
            "id": f"skill_cap_{idx}", "owner": "ROOT.md", "owner_signature": [["Canonical owner"]],
            "consumers": [{"path":"roles/consumer.md","mode":"reference","activation_signature":[["inherits shared delegation contract"]],
                "forbidden_redefinition":{"window_lines":8,"groups":[["goal","objective"],["scope","target"],["action ceiling","allowed action"],["evidence","deliverable"],["stop","escalat"]]}}],
            "pack_skill_guard":{"window_lines":8,"groups":[["goal","objective"],["scope","target"],["action ceiling","allowed action"],["evidence","deliverable"],["stop","escalat"]]}
        })
    skill_spec=skilldup / "evals/skill-control-spec.json"
    skill_spec.write_text(json.dumps({"schema_version":1,"skills":[{"path":"skills/helper/SKILL.md","class":"pack-workflow"}]}), encoding="utf-8")
    owner_spec=skilldup / "spec.json"; owner_spec.write_text(json.dumps({"schema_version":1,"capabilities":caps}), encoding="utf-8")
    findings=mod.audit(skilldup, owner_spec, skill_spec)
    expect(any("undeclared pack-skill second owner" in f for f in findings), "pack-skill paraphrased duplicate was not rejected")

print("SEMANTIC OWNERSHIP SELFTEST: PASS")
