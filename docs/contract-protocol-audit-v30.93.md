# Contract / protocol audit — v30.93 beta

## Scope

v30.93 extends semantic ownership/type/control coverage into pack-owned skills and strengthens external-skill containment. Agent permission/frontmatter policy is deliberately out of scope and unchanged. Third-party skill bodies/references/scripts are not edited.

## Skill provenance/control graph

All 22 bundled skill entrypoints are classified in `evals/skill-control-spec.json`:

- 9 pack-controlled workflow/integration skills;
- 13 vendor-advisory skills.

Pack-controlled skills declare material section inventory, owned/consumed semantic capabilities, typed domains, and side-effect class. Vendor directories are SHA-256 guarded and may not become pack semantic/domain owners merely because they are bundled.

## Canonical ownership splits

- Root memory policy -> `graymatter-memory` provider mechanics.
- Root persistent-planning activation/canonical state -> `persistent-planning` fallback representation/resume mechanics.
- Root evidence validity/freshness -> `verification-strategy` layering/cadence/tester activation -> `tester` execution/reporting.
- Root provenance-receipt interface -> `code-orchestrator` producer trigger -> `session-evidence` retrieval/consumer mechanics.
- Reviewer contract -> deterministic OCR preflight evidence from vendor skill; substantive review method/coverage/verdict remain reviewer-owned.
- `ui-component-sources` -> vendor UUPM remains advisory and cannot self-authorize install/persist/default-stack/source-of-truth changes.

## Typed domains

Six declared domains are checked, including pack-skill lifecycle states for `resource-lifecycle` and `pr-readiness`. Verdict discovery and protected-token negative checks cover roles plus declared pack-controlled skill entrypoints.

## Gate composition

The aggregate release runner includes:

- contract/protocol selftest;
- skill-control selftest + closed-world/provenance audit;
- semantic-ownership selftest + audit;
- semantic-domain selftest + audit;
- root/orchestrator section ownership selftest + audit;
- static policy regressions;
- installer safety;
- contract/protocol role executability;
- role-handoff selftest + closed-world edge audit.

Behavioral replay remains separate and is not inferred from structural PASS.
