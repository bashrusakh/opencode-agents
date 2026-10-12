# Contract / protocol audit — v30.79 beta

## Scope

v30.79 changes the standing runtime contract of `reviewer` only. It clarifies the composition boundary between host review judgment and managed `open-code-review` / `ocr review` evidence. Role topology, permissions, deterministic delegation procedure, managed-OCR invocation mechanics, PR lifecycle, and all other runtime role contracts remain unchanged.

## Reviewer protocol

The authoritative changed/effective-diff set now feeds two non-substitutable ledgers when managed OCR is used:

1. **host reviewer ledger** — independently inspected/accounted entries and host gaps/skips;
2. **managed OCR ledger** — selected/completed/failed/waived entries plus comments.

`Coverage: full PR` is a host claim. OCR selection/completion cannot mark a host ledger entry reviewed. OCR findings remain useful independent evidence and must be validated/reconciled; no-finding OCR output cannot supply a host pass.

Parallel execution remains valid. The change is about semantic ownership of coverage/judgment, not about serializing the review.

## Contract/eval evidence

`contract-protocol-audit.py` adds a reviewer-specific protocol check for:

- managed OCR as independent evidence rather than host substitute;
- host-owned changed/effective-diff ledger;
- no conversion of OCR-selected entries into host-reviewed entries;
- no correctness inference from zero OCR findings.

`contract-protocol-selftest.py` exercises both the valid separate-ledger contract and the invalid complement-union contract. The static reviewer guard checks the same runtime semantics without treating keyword presence as behavioral proof.

## Transition regression

The suite now contains **ST-01…ST-75**.

ST-75 fails the specific reusable class where a 14-entry review gets 10 managed-OCR selections, the host directly inspects only the four excluded entries, and the reviewer reports full coverage from the union. It passes only when host coverage is independently complete/accounted and managed OCR is reported separately.

## Evidence limits

Static/contract/selftest/package PASS proves that the candidate preserves these explicit contracts. It does not prove live behavioral compliance. Fresh isolated replay of ST-01…ST-75 remains pending.
