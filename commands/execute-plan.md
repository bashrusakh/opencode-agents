---
description: "Execute the current authorized work package from a persistent plan using Blueprint -> Gate -> Execute -> Digest."
agent: code-orchestrator
subtask: false
---

Execute the planned work for: $ARGUMENTS

Follow the active `AGENTS.md`, code-orchestrator contract, and the applicable installed/project `persistent_planning_policy.md`.

Read the canonical `plans/<plan>/` state that applies, identify the active work package and unresolved blockers, then:
1. **Blueprint** — restate the bounded steps, files/surfaces, checks, and material risks.
2. **Gate** — stop only for authorization that is genuinely missing under the root gate; do not re-ask for already authorized scope.
3. **Execute** — route each bounded work package to a capable role under the orchestrator delegation contract; specialists do not expand the package on their own and the orchestrator never implements repository changes itself.
4. **Digest** — reconcile the actual diff/evidence against the assigned package, classify new/out-of-scope findings before more mutation, route any required canonical plan-file update to the planning role, and report the next state succinctly.

Do not expand beyond the active plan/work package without normalization and authorization for the changed scope.
