#!/usr/bin/env python3
"""Manifest-driven cross-layer semantic ownership audit.

This gate checks declared material shared contracts as an ownership graph:
canonical owner -> reference/consume/specialize consumer. It is intentionally
architectural, not behavioral: it can reject a second consistent definition even
when both role executability and runtime behavior would otherwise remain green.

The manifest is the reviewable semantic inventory. Regex signatures are semantic
family evidence, not a claim that arbitrary paraphrase detection is solved.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MODES = {"reference", "consume", "specialize"}


def _read(root: Path, rel: str) -> str:
    path = root / rel
    if not path.is_file():
        raise FileNotFoundError(rel)
    return path.read_text(encoding="utf-8")


def _group_present(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.I | re.M) for pattern in patterns)


def _signature_present(text: str, groups: list[list[str]]) -> bool:
    return bool(groups) and all(_group_present(text, group) for group in groups)


def _window_match(
    text: str,
    groups: list[list[str]],
    window_lines: int,
    min_groups: int | None = None,
) -> tuple[int, str] | None:
    lines = text.splitlines()
    if not groups:
        return None
    required = len(groups) if min_groups is None else int(min_groups)
    if required < 1 or required > len(groups):
        raise ValueError(f"min_groups must be within 1..{len(groups)}, got {required}")
    width = max(1, int(window_lines))
    for start in range(len(lines)):
        chunk = "\n".join(lines[start:start + width])
        matched = sum(1 for group in groups if _group_present(chunk, group))
        if matched >= required:
            excerpt = "\n".join(lines[start:start + min(width, 8)])
            return start + 1, excerpt
    return None


def audit(root: Path, spec_path: Path, skill_spec_path: Path | None = None) -> list[str]:
    failures: list[str] = []
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"manifest unreadable: {exc}"]

    if spec.get("schema_version") != 1:
        failures.append("manifest schema_version must be 1")
    capabilities = spec.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        return failures + ["manifest capabilities must be a non-empty list"]

    seen_ids: set[str] = set()
    declared_paths: set[str] = set()
    pack_skill_paths: set[str] = set()
    skill_spec = skill_spec_path or (root / "evals/skill-control-spec.json")
    if skill_spec.is_file():
        try:
            skill_data = json.loads(skill_spec.read_text(encoding="utf-8"))
            pack_skill_paths = {
                row["path"] for row in skill_data.get("skills", [])
                if row.get("class") in {"pack-workflow", "pack-integration"}
            }
        except Exception as exc:
            failures.append(f"skill-control manifest unreadable for ownership scan: {exc}")
    for cap in capabilities:
        cid = cap.get("id")
        owner = cap.get("owner")
        if not isinstance(cid, str) or not cid:
            failures.append("capability missing non-empty id")
            continue
        if cid in seen_ids:
            failures.append(f"{cid}: duplicate capability id")
        seen_ids.add(cid)
        if not isinstance(owner, str) or not owner:
            failures.append(f"{cid}: missing canonical owner")
            continue
        declared_paths.add(owner)
        try:
            owner_text = _read(root, owner)
        except FileNotFoundError:
            failures.append(f"{cid}: owner path missing: {owner}")
            continue
        owner_sig = cap.get("owner_signature") or []
        if not _signature_present(owner_text, owner_sig):
            failures.append(f"{cid}: canonical owner no longer carries declared owner signature: {owner}")

        consumers = cap.get("consumers")
        if not isinstance(consumers, list) or not consumers:
            failures.append(f"{cid}: material shared capability has no declared consumers")
            continue
        seen_consumers: set[str] = set()
        for consumer in consumers:
            path = consumer.get("path")
            mode = consumer.get("mode")
            if not isinstance(path, str) or not path:
                failures.append(f"{cid}: consumer missing path")
                continue
            if path == owner:
                failures.append(f"{cid}: canonical owner cannot also be listed as its own consumer")
            if path in seen_consumers:
                failures.append(f"{cid}: duplicate consumer path: {path}")
            seen_consumers.add(path)
            declared_paths.add(path)
            if mode not in MODES:
                failures.append(f"{cid}: consumer {path} has invalid mode {mode!r}")
            try:
                consumer_text = _read(root, path)
            except FileNotFoundError:
                failures.append(f"{cid}: consumer path missing: {path}")
                continue
            activation = consumer.get("activation_signature") or []
            if not _signature_present(consumer_text, activation):
                failures.append(f"{cid}: consumer does not activate/reference declared owner: {path}")

            forbidden = consumer.get("forbidden_redefinition")
            if mode in {"reference", "consume"} and not forbidden:
                failures.append(f"{cid}: {mode} consumer {path} lacks a redefinition signature; the manifest could not distinguish reference/consumption from a second owner")
            if forbidden:
                groups = forbidden.get("groups") or []
                window_lines = forbidden.get("window_lines", 12)
                match = _window_match(consumer_text, groups, window_lines, forbidden.get("min_groups"))
                if match:
                    line, excerpt = match
                    failures.append(
                        f"{cid}: consumer redefines owner semantic family in {path}:{line} "
                        f"instead of remaining only a {mode} consumer; excerpt={excerpt!r}"
                    )

        guard = cap.get("pack_skill_guard")
        if guard and pack_skill_paths:
            groups = guard.get("groups") or []
            width = guard.get("window_lines", 12)
            allow = {owner, *seen_consumers, *(guard.get("allow_paths") or [])}
            for skill_path in sorted(pack_skill_paths - allow):
                try:
                    skill_text = _read(root, skill_path)
                except FileNotFoundError:
                    failures.append(f"{cid}: pack skill path missing during global ownership scan: {skill_path}")
                    continue
                match = _window_match(skill_text, groups, width, guard.get("min_groups"))
                if match:
                    line, excerpt = match
                    failures.append(
                        f"{cid}: undeclared pack-skill second owner in {skill_path}:{line}; excerpt={excerpt!r}"
                    )

    # The manifest is intentionally about cross-layer contracts. A path typo or empty
    # inventory should fail loudly rather than silently turning this into a no-op gate.
    if len(seen_ids) < 5:
        failures.append("semantic ownership manifest is implausibly small for the current shared-contract surface")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    default_root = Path(__file__).resolve().parents[1]
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--spec", type=Path, default=None)
    parser.add_argument("--skill-spec", type=Path, default=None)
    args = parser.parse_args()
    root = args.root.resolve()
    spec_path = (args.spec or (root / "evals/semantic-ownership-spec.json")).resolve()
    failures = audit(root, spec_path, args.skill_spec.resolve() if args.skill_spec else None)
    if failures:
        print("SEMANTIC OWNERSHIP AUDIT: FAIL")
        for finding in failures:
            print(f"- {finding}")
        return 1
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    print(f"SEMANTIC OWNERSHIP AUDIT: PASS ({len(spec['capabilities'])} shared capabilities)")
    for cap in spec["capabilities"]:
        consumers = ", ".join(f"{c['path']}[{c['mode']}]" for c in cap["consumers"])
        print(f"- {cap['id']}: {cap['owner']} -> {consumers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
