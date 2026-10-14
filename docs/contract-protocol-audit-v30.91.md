# Contract / protocol audit — v30.91 beta

## Scope

v30.91 changes release methodology/evaluation ownership, not role topology or runtime capability boundaries. Runtime role count and caller→callee topology remain those of v30.90.

## Failure class addressed

Previous gates answered these questions well:

- is required semantic behavior present;
- is each substantive role executable;
- do caller→assignment→callee handoffs compose;
- did a known guard disappear.

They did not independently prove:

> is a material shared semantic contract defined **only by its canonical owner**?

A second consistent definition could therefore pass all behavioral and executability checks. Historical static guards could block known literal fragments, but not the general ownership class.

## New semantic-ownership contract

`evals/semantic-ownership-spec.json` declares material shared capabilities with:

- one canonical owner;
- one or more consumers;
- consumer mode: `reference`, `consume`, or `specialize`;
- owner and activation signatures;
- where applicable, a semantic-family redefinition signature evaluated inside a bounded line window.

The audit fails when:

- the declared owner disappears or no longer carries the owner contract;
- a consumer stops activating/referencing the owner;
- a reference/consume consumer locally reconstructs the shared semantic family;
- the manifest is structurally invalid or implausibly emptied.

The signatures are reviewable static evidence, not a claim that arbitrary natural-language semantic equivalence is solved. Material new shared contracts still require manifest review/update under the design manual.

## Role-executability interaction

The governing rule is now explicit:

`role executability = inherited shared contract + role-local method`.

Therefore a role audit must prove the consumer's own algorithm, decision logic, evidence threshold, false-success defense, stop/escalation, and result semantics without forcing a duplicate copy of generic owner policy.

## Anti-gaming evidence

`semantic-ownership-selftest.py` proves:

- clean owner reference → PASS;
- paraphrased second definition of a generic handoff schema → FAIL;
- missing owner activation → FAIL;
- owner signature drift → FAIL;
- legitimate role-local specialization without shared-policy redefinition → PASS.

ST-120 records the same failure class as a semantic transition scenario.

## Status

This document describes structural/contract evidence. Fresh isolated behavioral replay of ST-120 is not claimed here.
