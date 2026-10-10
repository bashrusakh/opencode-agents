---
name: session-evidence
description: Retrieve complete, provenance-preserving OpenChamber session history for semantic checkpointing or retrospective evaluation without embedding provider mechanics in semantic role prompts.
---

# Session evidence retrieval

Use this skill only when a workflow role needs OpenChamber session history to establish material authority/evidence provenance or reconstruct a completed workflow.

The semantic role owns **what evidence it needs and how it interprets it**. This skill owns the current retrieval procedure.

## Read-only boundary

Use only the read-only OpenChamber actions `session.list` and `session.messages`. Do not mutate, fork, send, link, or otherwise change session state while using this skill.

## Prefer supplied identities

Use exact parent/participating session IDs supplied by the caller. Do not call `session.list` merely to rediscover an identity already provided.

If the caller states that the supplied participating-session set is complete for the evidence boundary, use those IDs directly and skip tree discovery.

If the parent ID, a materially participating child ID, or a required parent/child relationship is missing—or the supplied set is explicitly partial—use `session.list` only to resolve the missing identity/relationship. Request an explicit large result (`limit: 1000`, `all: true`, `withStatus: true`) and use `parentID` relationships rather than recency to distinguish participating descendants from unrelated sessions.

## Recover complete material history

For complete parent user-authority history, use `session.messages` with `role: user`, `all: true`, and no `limit`, `last`, or `lastAssistant`.

For a materially relevant parent or participating child history, use `session.messages` with `all: true` and no incompatible bounded selectors when complete chronology/provenance matters.

If a complete-history call fails because `all` was combined with `limit`, `last`, or `lastAssistant`, retry with `all: true` and without those selectors. Do not replace a failed complete-history request with a bounded window and then infer that older authority/evidence is absent.

If OpenCode materializes a large result into `~/.local/share/opencode/tool-output/`, read the managed output and continue from the complete result.

Prefer each participating child's own history over a parent's summary when the child's evidence is material. Follow an earlier participating branch only when a material claim depends on it; completeness does not require reading unrelated sessions.

## Completeness and provenance

Exclude diagnostic evaluator sessions when the consuming role's contract says they are not governing evidence. Treat a semantic-checkpoint verdict as workflow-control evidence, not as a substitute for primary task authority.

A later summary does not replace retrievable primary authority when provenance is material. If required history remains unavailable or incomplete after exhausting the relevant retrieval path, report that evidence boundary as partial/unverified rather than filling it from memory, hindsight, or a stronger restatement.

This skill defines retrieval mechanics only. It does not decide authority, adequacy, semantic substitution, failure classification, or checkpoint/evaluator verdicts.
