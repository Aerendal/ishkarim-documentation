> Powiązana propozycja: [PROPOZYCJA-4-Concept-Exploration-Workflows](../../proposals/PROPOZYCJA-4-Concept-Exploration-Workflows.md)
>
> System specs: [specs_gates.md](specs_gates.md) | [specs_doc_types.md](specs_doc_types.md)

```yaml
version: 1

# Concept Exploration Workflows
# Definiuje 4 end-to-end workflows dla eksploracji konceptów i decyzji

workflows:

  TECH_EXPLORATION:
    description: "End-to-end workflow for technical exploration"
    use_case: "Software development R&D - exploring new technologies, architectures, tools"
    flow: "Unknown/Risk → Hypothesis → Experiment/PoC → Decision → Implementation"
    duration_target: "<8 weeks"

    phases:
      - phase: discovery
        description: "Formulate and validate hypothesis"
        artifacts:
          - HYPOTHESIS-DOC (required)
          - SPIKE-SOLUTION (optional, if quick answer needed)
          - POC-DOC (optional, if detailed validation needed)
          - EXPERIMENT-LOG (required if PoC)
        checkpoint: GATE-HYPOTHESIS_REVIEW
        decision_point: "Hypothesis validated?"

      - phase: analysis
        description: "Aggregate research results and analyze options"
        artifacts:
          - RESEARCH-FINDINGS (required)
          - TRADE-OFF-ANALYSIS (required if 2+ options)
          - OPTION-COMPARISON-MATRIX (optional, qualitative comparison)
        checkpoint: GATE-VALIDATION_GATE
        decision_point: "Which option to choose?"

      - phase: decision
        description: "Make formal decision"
        artifacts:
          - ADR (required)
          - DECISION-LOG (alternative for lightweight decisions)
        checkpoint: GATE-DECISION_APPROVAL
        decision_point: "Proceed vs Pivot vs Stop"

      - phase: implementation
        description: "Design and implement solution"
        artifacts:
          - TDD (required)
          - SPRINT-CORE (required)
        checkpoint: GATE-REQ_FREEZE
        decision_point: "Ready for production?"

    gates:
      - GATE-HYPOTHESIS_REVIEW (after discovery)
      - GATE-VALIDATION_GATE (after analysis)
      - GATE-DECISION_APPROVAL (after decision)
      - GATE-REQ_FREEZE (before implementation)

    example_scenario: "Explore React Server Components for performance optimization"

  BUSINESS_INNOVATION:
    description: "End-to-end workflow for business innovation"
    use_case: "Product/startup validation - exploring new business ideas and validating market fit"
    flow: "Idea → Research → Validation → Business Case → PRD → Implementation"
    duration_target: "<12 weeks"

    phases:
      - phase: ideation
        description: "Formulate and validate business hypothesis"
        artifacts:
          - HYPOTHESIS-DOC (required)
          - MARKET-ANALYSIS (required)
          - EXPERIMENT-LOG (required, customer interviews/A/B tests)
        checkpoint: GATE-HYPOTHESIS_VALIDATION
        decision_point: "Customer problem validated?"

      - phase: validation
        description: "Validate market size and feasibility"
        artifacts:
          - RESEARCH-FINDINGS (required)
          - FEASIBILITY-STUDY (required, technical/economic/legal)
        checkpoint: GATE-MARKET_VALIDATION
        decision_point: "Market viable and feasible?"

      - phase: go_no_go
        description: "Make go/no-go decision"
        artifacts:
          - GO-NO-GO-DECISION (required)
        checkpoint: GATE-GO_NO_GO
        decision_point: "GO vs PIVOT vs NO-GO"
        decision_options:
          - GO: "Proceed to business case"
          - PIVOT: "Return to ideation with learnings"
          - NO-GO: "Archive idea"

      - phase: planning
        description: "Build business case and requirements"
        artifacts:
          - BUSINESS-CASE (required)
          - PRD (required)
        checkpoint: GATE-REQ_FREEZE
        decision_point: "Business case approved?"

      - phase: execution
        description: "Build and launch MVP"
        artifacts:
          - SPRINT-CORE (required)
          - TDD (required)
        checkpoint: GATE-RELEASE_READY
        decision_point: "Ready to launch?"

    gates:
      - GATE-HYPOTHESIS_VALIDATION (after ideation)
      - GATE-MARKET_VALIDATION (after validation)
      - GATE-GO_NO_GO (after go_no_go)
      - GATE-REQ_FREEZE (after planning)
      - GATE-RELEASE_READY (after execution)

    example_scenario: "Startup building AI-powered invoice processing for SMB"

  RISK_MITIGATION:
    description: "End-to-end workflow for risk mitigation exploration"
    use_case: "Enterprise risk management - exploring mitigation alternatives for identified risks"
    flow: "Risk Identified → Alternative Exploration → Trade-off Analysis → Decision → Mitigation Plan"
    duration_target: "<6 weeks"

    phases:
      - phase: exploration
        description: "Identify and validate mitigation options"
        artifacts:
          - ALTERNATIVE-EXPLORATION (required)
          - POC-DOC (optional, if validation needed)
        checkpoint: GATE-OPTIONS_IDENTIFIED
        decision_point: "Min 3 options identified?"

      - phase: analysis
        description: "Quantitative scoring of alternatives"
        artifacts:
          - TRADE-OFF-ANALYSIS (required)
        checkpoint: GATE-DECISION_REVIEW
        decision_point: "Clear winner identified?"

      - phase: decision
        description: "Select mitigation approach"
        artifacts:
          - ADR (required)
          - DECISION-LOG (alternative)
        checkpoint: GATE-APPROVAL
        decision_point: "Mitigation approved?"

      - phase: implementation
        description: "Implement and monitor mitigation"
        artifacts:
          - MITIGATION-PLAN (required)
          - MONITORING-PLAN (required)
        checkpoint: none
        decision_point: "Mitigation effective?"

    gates:
      - GATE-OPTIONS_IDENTIFIED (after exploration)
      - GATE-DECISION_REVIEW (after analysis)
      - GATE-APPROVAL (after decision)

    example_scenario: "Enterprise mitigating vendor lock-in risk (AWS-only → multi-cloud)"

  PARALLEL_BRANCHING:
    description: "Parallel concept exploration workflow"
    use_case: "R&D concurrent exploration - testing multiple approaches in parallel"
    flow: "Parent Concept → Branch 1 & 2 & 3 → Compare → Merge/Kill Decision"
    duration_target: "<6 weeks"

    phases:
      - phase: fork
        description: "Create parallel exploration branches"
        artifacts:
          - CONCEPT-BRANCH (multiple, one per branch)
        checkpoint: GATE-BRANCH_CREATION
        decision_point: "Branches properly isolated?"

      - phase: exploration
        description: "Parallel execution with mid-point review"
        artifacts:
          - EXPERIMENT-LOG (per branch)
        checkpoint: GATE-MID_POINT_REVIEW
        decision_point: "Continue all branches or kill underperforming?"

      - phase: comparison
        description: "Compare all branch results"
        artifacts:
          - RESEARCH-FINDINGS (aggregate)
        checkpoint: GATE-RESULTS_REVIEW
        decision_point: "All branches complete?"

      - phase: merge_kill
        description: "Decide which branches to merge/kill"
        artifacts:
          - ADR (required)
          - DECISION-LOG (alternative)
        checkpoint: GATE-MERGE_KILL_DECISION
        decision_point: "Merge best / Kill rest / Hybrid"
        decision_options:
          - MERGE: "Merge winning branch to parent"
          - KILL: "Archive failed branches"
          - HYBRID: "Combine insights from multiple branches"

    gates:
      - GATE-BRANCH_CREATION (after fork)
      - GATE-MID_POINT_REVIEW (after exploration, Week 2)
      - GATE-RESULTS_REVIEW (after comparison)
      - GATE-MERGE_KILL_DECISION (after merge_kill)

    example_scenario: "AI team exploring 3 model architectures for churn prediction"

# Success Metrics (per workflow)

metrics:
  M1_WORKFLOW_ADOPTION_RATE:
    description: "% projects using defined workflows (vs ad-hoc)"
    target: ">60% in 6 months"
    measurement: "Projects tagged with workflow_type in metadata"
    calculation: "(projects_with_workflow / total_projects) * 100"

  M2_CHECKPOINT_COMPLIANCE:
    description: "% projects that pass all checkpoints in workflow"
    target: ">80%"
    measurement: "Gate validation logs"
    calculation: "(projects_passing_all_gates / projects_started) * 100"

  M3_TIME_TO_DECISION:
    description: "Average time from workflow start → final decision"
    target:
      TECH_EXPLORATION: "<8 weeks"
      BUSINESS_INNOVATION: "<12 weeks"
      RISK_MITIGATION: "<6 weeks"
      PARALLEL_BRANCHING: "<6 weeks"
    measurement: "Timestamp tracking (workflow start → ADR approved)"
    calculation: "avg(decision_timestamp - workflow_start_timestamp)"

  M4_WORKFLOW_COMPLETION_RATE:
    description: "% workflows completed (vs abandoned mid-way)"
    target: ">70%"
    measurement: "Workflows started vs completed"
    calculation: "(workflows_completed / workflows_started) * 100"

  M5_DECISION_QUALITY:
    description: "% decisions not requiring reversal within 6 months"
    target: ">85%"
    measurement: "DECISION-REVERSAL count vs total decisions"
    calculation: "((total_decisions - reversals_within_6mo) / total_decisions) * 100"

# Workflow Dependencies (how workflows can compose)

workflow_composition:
  description: "Workflows can be nested and composed"
  examples:
    - parent: BUSINESS_INNOVATION
      nested: TECH_EXPLORATION
      scenario: "Startup validating business idea, needs tech exploration for feasibility"

    - parent: TECH_EXPLORATION
      nested: PARALLEL_BRANCHING
      scenario: "Tech exploration involves testing multiple architectures in parallel"

    - parent: RISK_MITIGATION
      nested: TECH_EXPLORATION
      scenario: "Mitigating technical risk requires tech exploration to validate alternatives"

# Validation Rules (referenced by gates)

validation_criteria:
  RULE-HYP-TESTABLE:
    description: "Hypothesis must be testable"
    validation: "Hypothesis has clear success criteria defined"
    error_message: "Hypothesis lacks testable success criteria"

  RULE-HYP-SUCCESS-CRITERIA:
    description: "Hypothesis has quantifiable success criteria"
    validation: "Success criteria are measurable (>70% threshold recommended)"
    error_message: "Success criteria not quantifiable or threshold too low"

  RULE-RF-VALIDATION-THRESHOLD:
    description: "Research findings validate hypothesis"
    validation: ">70% of success criteria met"
    error_message: "Research findings do not validate hypothesis (<70% criteria met)"

  RULE-ALT-MIN-3-OPTIONS:
    description: "Alternative exploration identifies minimum 3 options"
    validation: "At least 3 distinct alternatives documented"
    error_message: "Less than 3 alternatives identified (min 3 required for proper trade-off)"
```

---

## Document Cross-References

### Dependencies (Required Inputs)
```yaml
dependencies:
  - id: specs_doc_types.md
    type: requires
    reason: "Workflows reference doctypes (HYPOTHESIS-DOC, ADR, TDD, etc.)"
    sections:
      - from: "workflows.*.phases.*.artifacts"
        to: "specs_doc_types.doctypes"
        influence: "Workflow artifacts must be valid doctypes"

  - id: specs_gates.md
    type: requires
    reason: "Workflows reference gates as checkpoints"
    sections:
      - from: "workflows.*.gates"
        to: "specs_gates.gates"
        influence: "Workflow gates must be defined in gates spec"

  - id: PROPOZYCJA-4-Concept-Exploration-Workflows.md
    type: implements
    reason: "This spec implements the workflows defined in Propozycja 4"
```

### Impacts (Downstream Documents)
```yaml
impacts:
  - id: dependency_graph.md
    type: visualizes
    reason: "Dependency graph contains Mermaid diagrams for workflows"
    sections:
      - from: "workflows section"
        to: "Graf I, J, K, L (workflow graphs)"
        influence: "Workflow definitions drive graph visualization"

  - id: engineering/workflows/concept-exploration-workflows.md
    type: documents
    reason: "User guide explains how to use workflows defined here"
```

### Related Documents
```yaml
related:
  - id: specs_error_codes.md
    type: informs
    reason: "Validation rules reference error codes"

  - id: satelitarne_artefakty_dokumentacyjne_kanwa_opisowa.md
    type: uses
    reason: "Workflows use satellite artifacts (APPROVAL, EVIDENCE, CHANGELOG)"
```

### Satellite Documents
```yaml
satellites:
  - type: Changelog
    path: "satellites/CHANGELOG-SPECS-WORKFLOWS-001.md"
    required: false

  - type: Evidence
    path: "satellites/evidence/E-WORKFLOW-*.md"
    required: false
    purpose: "Evidence of workflow effectiveness (metrics, case studies)"
```

---

## Notatki implementacyjne

### Integracja z istniejącym systemem

**Gates Integration:**
- TECH_EXPLORATION używa: GATE-HYPOTHESIS_REVIEW, GATE-VALIDATION_GATE, GATE-DECISION_APPROVAL, GATE-REQ_FREEZE
- BUSINESS_INNOVATION używa: GATE-HYPOTHESIS_VALIDATION, GATE-MARKET_VALIDATION, GATE-GO_NO_GO, GATE-REQ_FREEZE, GATE-RELEASE_READY
- RISK_MITIGATION używa: GATE-OPTIONS_IDENTIFIED, GATE-DECISION_REVIEW, GATE-APPROVAL
- PARALLEL_BRANCHING używa: GATE-BRANCH_CREATION, GATE-MID_POINT_REVIEW, GATE-RESULTS_REVIEW, GATE-MERGE_KILL_DECISION

**Doctypes Integration:**
- Wszystkie workflows używają istniejących doctypes z specs_doc_types.md
- Nowe doctypes potrzebne: RESEARCH-FINDINGS, ALTERNATIVE-EXPLORATION, CONCEPT-BRANCH (do utworzenia)

**Sprint Integration:**
- TECH_EXPLORATION.implementation używa SPRINT-CORE
- BUSINESS_INNOVATION.execution używa SPRINT-CORE
- Workflows mogą być wykonywane w ramach Discovery Sprints (specs pokazują integrację)

### Workflow Composability

Workflows są komponowalne - można je zagnieżdżać:
- Business Innovation może zawierać Tech Exploration (dla feasibility)
- Tech Exploration może zawierać Parallel Branching (dla porównania opcji)
- Risk Mitigation może zawierać Tech Exploration (dla walidacji mitigation options)

### Metryki i monitoring

System metryk pozwala śledzić:
- Czy workflows są adoptowane (M1)
- Czy zespoły przechodzą przez gates (M2)
- Jak długo trwają decyzje (M3)
- Czy workflows są complete vs abandoned (M4)
- Czy decyzje są jakościowe (M5)

---

**Koniec specs_workflows.md**
