# Contract / protocol audit — v30.94 beta

## Scope

v30.94 audits **runtime residency** in addition to ownership, typed domains, role executability, skill provenance, and handoff composition. The target is the global-root over-residency failure class: caller/implementation procedure must not be injected into roles that neither own nor execute it.

Permission/frontmatter semantics and vendor skill bodies/references/scripts are intentionally out of scope and unchanged.

## Shared contract graph

The universal root now composes with three non-autoinvoked pack contracts:

- root universal kernel -> `workflow-entry` for primary/user-facing ownership;
- root universal kernel -> `delegation-control` for invocations that actually dispatch/reconcile subagents;
- root universal kernel -> `implementation-contract` for material implementation or implementation judgment.

Role executability is evaluated as universal inherited semantics + applicable conditional shared contract(s) + role-local method. A test may not require a role to duplicate a shared contract merely to remain executable.

## Audience boundaries

Primary roles (`code-orchestrator`, `auditor`) load entry/delegation contracts. `mode: all` roles activate owner contracts only when the current invocation is primary. Delegated invocations execute their bounded assignment without re-normalizing the user workflow or gaining another subagent generation. Implementation/judgment roles load the engineering contract only at the applicable stage.

## Release-gate composition

The aggregate runner now includes:

- contract/protocol selftest;
- skill-control selftest + audit;
- semantic-ownership selftest + audit;
- semantic-domain selftest + audit;
- root/orchestrator section-ownership selftest + audit;
- **runtime-residency selftest + audit**;
- static policy regressions;
- installer safety;
- contract/protocol role executability;
- role-handoff selftest + closed-world edge audit.

Residency mutations are release-blocking when they reinsert caller/implementation procedure into global root, make a conditional control skill auto-invokable, or make a forbidden leaf/delegated invocation load an owner-only contract. Behavioral replay remains a separate evidence class.
