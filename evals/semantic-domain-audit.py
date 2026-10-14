#!/usr/bin/env python3
"""Typed semantic-domain audit.

Semantic ownership and semantic vocabulary are different invariants. Ownership asks
who defines a contract. This gate asks whether a literal that belongs to one typed
state domain is silently reused as a peer value in another domain (for example an
evidence status becoming a workflow verdict).

The spec declares shared typed domains. Workflow-verdict enums are also discovered
from runtime agent prompts under Verdict/Verdict semantics headings so a new verdict
domain cannot appear without being inventoried.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

BACKTICK = re.compile(r"`([^`]+)`")
VERDICT_HEAD = re.compile(r"^##+\s+Verdict(?:\s+semantics)?\s*$", re.I)
HEADING = re.compile(r"^#{1,6}\s+")
BULLET_TOKEN = re.compile(r"^\s*-\s+`([^`]+)`\s+[—-]")


def read(root: Path, rel: str) -> str:
    p = root / rel
    if not p.is_file():
        raise FileNotFoundError(rel)
    return p.read_text(encoding="utf-8")


def signature_present(text: str, groups: list[list[str]]) -> bool:
    return bool(groups) and all(any(re.search(p, text, re.I | re.M) for p in g) for g in groups)


def _pack_skill_paths(root: Path, skill_spec_path: Path | None = None) -> list[Path]:
    spec_path = skill_spec_path or (root / "evals/skill-control-spec.json")
    if not spec_path.is_file():
        return []
    data = json.loads(spec_path.read_text(encoding="utf-8"))
    return [
        root / row["path"] for row in data.get("skills", [])
        if row.get("class") in {"pack-workflow", "pack-integration"}
    ]


def discover_verdict_domains(root: Path, skill_spec_path: Path | None = None) -> list[tuple[str, str, list[str]]]:
    found: list[tuple[str, str, list[str]]] = []
    paths = [*sorted((root / "agents").glob("*.md")), *_pack_skill_paths(root, skill_spec_path)]
    for path in sorted(set(paths)):

        lines = path.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            if not VERDICT_HEAD.match(lines[i]):
                i += 1
                continue
            heading = lines[i].strip()
            tokens: list[str] = []
            j = i + 1
            while j < len(lines):
                if j > i + 1 and HEADING.match(lines[j]):
                    break
                m = BULLET_TOKEN.match(lines[j])
                if m:
                    tokens.append(m.group(1))
                j += 1
            if tokens:
                found.append((str(path.relative_to(root)), heading, tokens))
            i = j
    return found


def audit(root: Path, spec_path: Path, skill_spec_path: Path | None = None) -> list[str]:
    failures: list[str] = []
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"semantic-domain spec unreadable: {exc}"]
    if spec.get("schema_version") != 1:
        failures.append("semantic-domain spec schema_version must be 1")
    domains = spec.get("domains")
    if not isinstance(domains, list) or not domains:
        return failures + ["semantic-domain spec domains must be a non-empty list"]

    token_owner: dict[str, str] = {}
    declared_verdicts: dict[tuple[str, str], set[str]] = {}
    for dom in domains:
        did = dom.get("id")
        dclass = dom.get("domain_class")
        owner = dom.get("owner")
        tokens = dom.get("tokens") or []
        if not isinstance(did, str) or not did:
            failures.append("semantic domain missing id")
            continue
        if not isinstance(owner, str) or not owner:
            failures.append(f"{did}: missing owner")
            continue
        try:
            owner_text = read(root, owner)
        except FileNotFoundError:
            failures.append(f"{did}: owner missing: {owner}")
            continue
        sig = dom.get("owner_signature")
        if sig and not signature_present(owner_text, sig):
            failures.append(f"{did}: owner signature missing from {owner}")
        if not isinstance(tokens, list) or len(tokens) < 2:
            failures.append(f"{did}: typed domain must declare at least two tokens")
            continue
        for token in tokens:
            if not isinstance(token, str) or not token:
                failures.append(f"{did}: invalid token {token!r}")
                continue
            previous = token_owner.get(token)
            if previous and previous != did:
                failures.append(f"typed literal `{token}` belongs to multiple semantic domains: {previous}, {did}")
            token_owner[token] = did
        if dclass == "workflow_verdict":
            heading = dom.get("owner_heading")
            if not isinstance(heading, str) or not heading:
                failures.append(f"{did}: workflow verdict domain missing owner_heading")
            else:
                declared_verdicts[(owner, heading)] = set(tokens)

    discovered = discover_verdict_domains(root, skill_spec_path)
    for path, heading, tokens in discovered:
        key = (path, heading)
        declared = declared_verdicts.get(key)
        if declared is None:
            failures.append(f"undeclared workflow-verdict domain discovered at {path} {heading}: {tokens}")
            continue
        actual = set(tokens)
        if actual != declared:
            failures.append(
                f"workflow-verdict domain drift at {path} {heading}: declared={sorted(declared)} actual={sorted(actual)}"
            )

    for key in declared_verdicts:
        if not any((p, h) == key for p, h, _ in discovered):
            failures.append(f"declared workflow-verdict domain not discovered at {key[0]} {key[1]}")

    # Negative guards: typed evidence/relation literals may be discussed near verdict
    # prose, but may not themselves be returned/declared as workflow verdicts.
    protected = {
        token
        for dom in domains
        if dom.get("domain_class") in {"evidence_status", "proposition_relation"}
        for token in dom.get("tokens", [])
    }
    runtime_paths = [root / "AGENTS.md", *sorted((root / "agents").glob("*.md")), *_pack_skill_paths(root, skill_spec_path)]
    verdict_use_patterns = [
        lambda t: re.compile(rf"return\s+`{re.escape(t)}`[^\n]*\bverdict\b", re.I),
        lambda t: re.compile(rf"\bworkflow verdict\b[^\n]*`{re.escape(t)}`", re.I),
        lambda t: re.compile(rf"`{re.escape(t)}`\s+[—-][^\n]*\bworkflow verdict\b", re.I),
        lambda t: re.compile(rf"\b(?:workflow\s+)?verdict\b[^\n]{{0,48}}(?:is|=|:)\s*`{re.escape(t)}`", re.I),
        lambda t: re.compile(rf"`{re.escape(t)}`[^\n]{{0,48}}\b(?:workflow\s+)?verdict\b", re.I),
    ]
    negative_guard = re.compile(r"not as .*workflow verdict|distinct from .*evidence status|rather than creating .*peer class|remain .* as evidence state|remains .* evidence state", re.I)
    for path in runtime_paths:
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            if negative_guard.search(line):
                continue
            for token in protected:
                if any(p(token).search(line) for p in verdict_use_patterns):
                    failures.append(
                        f"typed literal `{token}` is reused as workflow-verdict semantics in {path.relative_to(root)}:{lineno}: {line.strip()}"
                    )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    default_root = Path(__file__).resolve().parents[1]
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--spec", type=Path, default=None)
    parser.add_argument("--skill-spec", type=Path, default=None)
    args = parser.parse_args()
    root = args.root.resolve()
    spec_path = (args.spec or root / "evals/semantic-domain-spec.json").resolve()
    failures = audit(root, spec_path, args.skill_spec.resolve() if args.skill_spec else None)
    if failures:
        print("SEMANTIC DOMAIN AUDIT: FAIL")
        for f in failures:
            print(f"- {f}")
        return 1
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    print(f"SEMANTIC DOMAIN AUDIT: PASS ({len(spec['domains'])} typed domains)")
    for d in spec["domains"]:
        print(f"- {d['id']} [{d['domain_class']}]: {', '.join(d['tokens'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
