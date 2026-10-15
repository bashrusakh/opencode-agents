# Contract / protocol audit — v30.96 beta

## Scope

v30.96 checks resource-specific residency inside `code-orchestrator`: code-host mechanics are conditional, while generic orchestration remains resident and narrower lifecycle/provenance contracts retain their canonical ownership.

Permissions/frontmatter semantics and vendor skill content are out of scope and unchanged.

## Resource ownership graph

`workflow-entry` route/gate -> `code-orchestrator` conditional activation -> `code-host-workflow` host mechanics -> `pr-readiness` Owned-PR lifecycle / `git-provenance` ref-SHA identity / `output-formatting` destination formatting / `resource-lifecycle` temporary-resource reconciliation.

The old v30.95 resource sections map as follows:

- `Existing PR follow-up` -> `code-host-workflow` Existing PR follow-up;
- `Issue / ticket / report` -> `code-host-workflow` Issue / ticket / report;
- `Release prep` -> `code-host-workflow` Release / host publication;
- PR template host-metadata fallback and PR-specific result fields -> `code-host-workflow`;
- Owned-PR identity/Draft-Candidate-Ready remains `pr-readiness`;
- ref/SHA/worktree identity remains `git-provenance`;
- generic user publication authorization remains `workflow-entry`;
- generic owner synthesis/findings/implementation routing remains `code-orchestrator`.

## Release-gate composition

The aggregate runner retains role/skill/ownership/domain/placement/residency/static/installer/handoff gates. Runtime-residency selftest now also proves that a resource procedure copied into an always-resident activator is rejected. Destructive resource mutations are expected to fail before release promotion.
