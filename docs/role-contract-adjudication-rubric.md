# Role-contract semantic adjudication rubric

Use this rubric when the automated contract audit reports `REVIEW`, when a new routed role is added, or when a role changes materially. It exists to decide whether the standing contract is actually executable; it is not a waiver mechanism.

For the role under review, answer from the active root/orchestrator/role contracts and one realistic bounded assignment:

1. **Start condition** — Can the role determine what state/target/claim it is acting on and what it is not allowed to absorb from adjacent roles?
2. **First real action** — Does the role know what to inspect/derive/do first without the caller supplying the missing algorithm?
3. **Characteristic core loop** — Is the method that makes this capability distinct actually local to the role (not merely a root pointer or a list of topics)?
4. **Decision branches** — Are the important condition→action transitions explicit enough for a weaker conforming model: continue, broaden inside scope, stop, reroute, escalate, or mark unknown?
5. **False-success defense** — Does the role know what evidence would *not* be sufficient and how it can try to falsify its own working conclusion where appropriate?
6. **Evidence closure** — Is there a role-local threshold for what supports the returned claim, including unavailable/invalid/stale evidence?
7. **Stop/escalation** — Can the role identify when the task has become another role's responsibility or requires new authority/design/product decisions?
8. **Result semantics** — Can the parent distinguish complete vs partial/advisory/unverified results without reconstructing hidden assumptions?
9. **Protocol compatibility** — Does the producer→parent→role handoff preserve authority/evidence/hypothesis classes without turning recommendations into recipes or partial work into completion?
10. **Overreach preservation case** — Would a simple valid task still remain simple, or does the proposed strengthening force ritual planning/testing/review where the role does not need it?

A semantic adjudication may conclude that a compact contract is sufficient, but it must cite the concrete role-local clauses that answer the rubric and include the overreach/preservation case. “The model probably knows how” or “root already says good engineering” is not sufficient.

If the role cannot answer the rubric without inventing missing procedure, strengthen the role contract. Do not add a role-specific checker exception merely to recover PASS.
