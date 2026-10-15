CONTRACT / PROTOCOL AUDIT v3
Discovered delegation edges:
  auditor -> a11y-reviewer, devops, explore, general, librarian, reviewer, tester, ui-auditor
  code-orchestrator -> build, debugger, devops, explore, general, librarian, project-planner, reviewer, semantic-checkpoint, session-evaluator, tester, trajectory-auditor, ui-implementer, ui-orchestrator
  ui-orchestrator -> a11y-reviewer, code-orchestrator, explore, reviewer, tester, ui-auditor, ui-implementer, ui-planner

Role executability matrix:
  PASS   a11y-reviewer        [independent_review] body=28nl/4419c actions=12 decisions=4 seq=7
         core: bind_exact_target, derive_attack_surface, bounded_judgment
  PASS   auditor              [audit_orchestrator] body=50nl/6636c actions=15 decisions=5 seq=8
         core: scope_and_specialists, risk_and_evidence, reconcile_specialists, bounded_audit_result
  PASS   build                [implementation] body=25nl/8073c actions=15 decisions=13 seq=14
         core: derive_before_edit, final_self_check, bounded_escalation
  PASS   code-orchestrator    [code_orchestrator] body=144nl/37444c actions=72 decisions=44 seq=86
         core: normalize_and_route, clean_handoff, consume_without_overclaim, owner_synthesis, owner_control_plane, workflow_state_visibility, decision_context
  PASS   debugger             [debug_mutation] body=19nl/6114c actions=13 decisions=9 seq=16
         core: symptom_to_cause, cause_to_fix, failed_hypothesis_reset
  PASS   devops               [ops_mutation] body=15nl/3609c actions=10 decisions=7 seq=11
         core: observe_before_action, isolate_before_mutation, authorized_reversible_action, postchange_proof
  PASS   explore              [discovery] body=20nl/2782c actions=9 decisions=5 seq=1
         core: question_to_trace, corroborate_not_infer, negative_claim_scope, flow_edge_corroboration, bounded_handoff
  PASS   general              [analysis_fallback] body=12nl/2363c actions=7 decisions=5 seq=7
         core: question_to_evidence, separate_known_unknown, bounded_handoff
  PASS   librarian            [external_research] body=24nl/5691c actions=15 decisions=9 seq=11
         core: bind_external_target, source_and_applicability, reconcile_conflicts, bounded_external_result
  PASS   project-planner      [planning] body=26nl/5432c actions=15 decisions=8 seq=1
         core: inspect_before_plan, ownership_and_choices, execution_and_verification_plan
  PASS   reviewer             [independent_review] body=62nl/21905c actions=40 decisions=27 seq=16
         core: bind_exact_target, derive_attack_surface, bounded_judgment
  PASS   semantic-checkpoint  [semantic_gate] body=81nl/11975c actions=32 decisions=8 seq=7
         core: bind_and_classify, residual_authority_boundary, typed_state_axes, boundary_not_recipe, bounded_result
  PASS   session-evaluator    [evaluation] body=89nl/18774c actions=45 decisions=17 seq=14
         core: trace_contract, workflow_owner_quality, classify_failure, bound_conclusion
  PASS   tester               [verification] body=31nl/4606c actions=14 decisions=8 seq=4
         core: bind_and_plan, discriminating_evidence, classify_and_bound
  PASS   trajectory-auditor   [trajectory_audit] body=51nl/11678c actions=22 decisions=9 seq=25
         core: recover_task_anchor, second_opinion_boundary, material_transition_chain, progress_without_false_stall, drift_and_cluster_test, bounded_next_transition
  PASS   ui-auditor           [audit] body=14nl/3130c actions=8 decisions=3 seq=9
         core: scope_and_risk, evidence_and_counterexample, coverage_and_stop
  PASS   ui-implementer       [implementation] body=17nl/4392c actions=11 decisions=7 seq=11
         core: derive_before_edit, final_self_check, bounded_escalation
  PASS   ui-orchestrator      [orchestrator] body=42nl/8129c actions=19 decisions=13 seq=7
         core: normalize_and_route, clean_handoff, consume_without_overclaim
  PASS   ui-planner           [planning] body=16nl/3435c actions=7 decisions=3 seq=9
         core: inspect_before_plan, ownership_and_choices, execution_and_verification_plan

SUMMARY: roles FAIL=0 REVIEW=0 PASS=19; protocol/classification findings=0

PASS: no unresolved role-executability or protocol-composition findings.
This PASS remains only a prerequisite; isolated behavioral replay is still required.
