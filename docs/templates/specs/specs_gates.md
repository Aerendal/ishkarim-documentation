> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

```yaml
version: 1

# Bramki (checkpointy) — walidator raportuje blokady per gate.
# Gate jest „odblokowany” tylko jeśli wszystkie warunki są spełnione.

gates:

  GATE-GO_NO_GO:
    description: "Decyzja wejścia w realizację (go/no-go)"
    required_documents:
      - {doctype: EXEC_SUMMARY,    min_status: approved}
      - {doctype: BUSINESS_CASE,   min_status: approved}
      - {doctype: FINANCIAL_PLAN,  min_status: in-review}
      - {doctype: MARKET_ANALYSIS, min_status: in-review}
      - {doctype: FEASIBILITY,     min_status: approved}
    required_rules:
      - RULE-BC-SCENARIOS-MIN3
      - RULE-BC-EVID-REQUIRED
    required_satellites:
      # wymagamy formalnego sign-off dla kluczowych dokumentów
      - {kind: APPROVAL, for_doctypes: [BUSINESS_CASE, FEASIBILITY, EXEC_SUMMARY]}
      - {kind: EVIDENCE, for_doctypes: [BUSINESS_CASE, MARKET_ANALYSIS, FINANCIAL_PLAN]}
    approvers: ["Sponsor", "CFO"]

  GATE-REQ_FREEZE:
    description: "Zamrożenie wymagań — start implementacji na stabilnej bazie"
    required_documents:
      - {doctype: ROADMAP_PRODUCT, min_status: approved}
      - {doctype: PRD,            min_status: approved}
      - {doctype: HLA,            min_status: in-review}
      - {doctype: RTM,            min_status: draft}
    required_rules:
      - RULE-PRD-AC-MIN5
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [PRD, ROADMAP_PRODUCT]}
      - {kind: EVIDENCE, for_doctypes: [PRD]}
    conditional_requirements:
      # Jeśli projekt dotyczy danych osobowych — DPIA staje się obowiązkowe
      - when:
          profile_any_of: ["healthcare", "fintech", "public"]
        require_documents:
          - {doctype: DPIA, min_status: approved}
          - {doctype: SECURITY_PLAN, min_status: approved}
        require_satellites:
          - {kind: APPROVAL, for_doctypes: [DPIA, SECURITY_PLAN]}
    approvers: ["Product Owner", "Tech Lead", "Security/DPO (if applicable)"]

  GATE-RELEASE_READY:
    description: "Gotowość do wydania (release readiness)"
    required_documents:
      - {doctype: TEST_PLAN,       min_status: approved}
      - {doctype: TDD,             min_status: in-review}
      - {doctype: RUNBOOK,         min_status: in-review}
      - {doctype: SECURITY_PLAN,   min_status: in-review}
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [TEST_PLAN, RUNBOOK]}
      - {kind: CHANGELOG, for_doctypes: [RUNBOOK]}
    approvers: ["Release Manager", "QA Lead", "DevOps Lead", "Product Owner"]

  GATE-OPS_HANDOVER:
    description: "Formalne przekazanie do operacji (ops handover)"
    required_documents:
      - {doctype: RUNBOOK,          min_status: approved}
      - {doctype: MONITORING_PLAN,  min_status: approved}
      - {doctype: SIRP,             min_status: approved}
      - {doctype: DRP,              min_status: approved}
      - {doctype: BCP,              min_status: approved}
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [RUNBOOK, MONITORING_PLAN, SIRP, DRP, BCP]}
    approvers: ["Head of Operations", "DevOps Lead", "Security Lead"]

  GATE-PROJECT_CLOSURE:
    description: "Zamknięcie projektu (closure)"
    required_documents:
      # (opcjonalnie: zdefiniuj doctypes POSTMORTEM i CLOSURE_REPORT w doc_types.yaml,
      # jeśli chcesz pełne formalne zamknięcie)
      - {doctype: ROADMAP_PRODUCT, min_status: archived}
    approvers: ["Sponsor", "Project Manager"]

  # === Concept Exploration Workflow Gates (PROPOZYCJA-4) ===

  # Tech Exploration Workflow Gates
  GATE-HYPOTHESIS_REVIEW:
    description: "Hypothesis validation checkpoint (Tech Exploration)"
    workflow: WF-TECH-EXPLORATION
    phase: discovery
    required_documents:
      - {doctype: HYPOTHESIS-DOC, min_status: approved}
    required_rules:
      - RULE-HYP-TESTABLE
      - RULE-HYP-SUCCESS-CRITERIA
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [HYPOTHESIS-DOC]}
    approvers: ["Research Lead", "Product Owner"]
    decision_options: ["Proceed to Spike/PoC", "Reject hypothesis"]

  GATE-VALIDATION_GATE:
    description: "Research validation checkpoint (Tech Exploration)"
    workflow: WF-TECH-EXPLORATION
    phase: analysis
    required_documents:
      - {doctype: RESEARCH-FINDINGS, min_status: approved}
    required_rules:
      - RULE-RF-VALIDATION-THRESHOLD
    required_satellites:
      - {kind: EVIDENCE, for_doctypes: [RESEARCH-FINDINGS]}
      - {kind: APPROVAL, for_doctypes: [RESEARCH-FINDINGS]}
    approvers: ["Tech Lead", "Product Owner"]
    decision_options: ["Proceed to ADR", "More Research", "Pivot"]

  GATE-DECISION_APPROVAL:
    description: "Architecture decision approval (Tech Exploration)"
    workflow: WF-TECH-EXPLORATION
    phase: decision
    required_documents:
      - {doctype: ADR, min_status: approved}
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [ADR]}
      - {kind: EVIDENCE, for_doctypes: [ADR]}
    approvers: ["Tech Lead", "Architect", "Product Owner"]
    decision_options: ["Proceed to TDD", "Re-evaluate"]

  # Business Innovation Workflow Gates
  GATE-HYPOTHESIS_VALIDATION:
    description: "Business hypothesis validation (Business Innovation)"
    workflow: WF-BUSINESS-INNOVATION
    phase: ideation
    required_documents:
      - {doctype: HYPOTHESIS-DOC, min_status: approved}
    required_rules:
      - RULE-HYP-TESTABLE
      - RULE-HYP-SUCCESS-CRITERIA
      - RULE-HYP-CUSTOMER-VALIDATION
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [HYPOTHESIS-DOC]}
    approvers: ["Product Owner", "Business Lead"]
    decision_options: ["Proceed to Market Research", "Pivot"]

  GATE-MARKET_VALIDATION:
    description: "Market & customer validation (Business Innovation)"
    workflow: WF-BUSINESS-INNOVATION
    phase: validation
    required_documents:
      - {doctype: RESEARCH-FINDINGS, min_status: approved}
      - {doctype: MARKET-ANALYSIS, min_status: approved}
    required_rules:
      - RULE-MARKET-TAM-MIN
      - RULE-CUSTOMER-VALIDATION-THRESHOLD
    required_satellites:
      - {kind: EVIDENCE, for_doctypes: [RESEARCH-FINDINGS, MARKET-ANALYSIS]}
      - {kind: APPROVAL, for_doctypes: [RESEARCH-FINDINGS, MARKET-ANALYSIS]}
    approvers: ["Product Owner", "Business Lead", "Investor (if applicable)"]
    decision_options: ["Proceed to Feasibility", "Pivot to different segment"]

  GATE-FEASIBILITY_CHECK:
    description: "Feasibility assessment (Business Innovation)"
    workflow: WF-BUSINESS-INNOVATION
    phase: validation
    required_documents:
      - {doctype: FEASIBILITY, min_status: approved}
    required_rules:
      - RULE-FEASIBILITY-TECHNICAL
      - RULE-FEASIBILITY-ECONOMIC
      - RULE-FEASIBILITY-LEGAL
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [FEASIBILITY]}
      - {kind: EVIDENCE, for_doctypes: [FEASIBILITY]}
    approvers: ["CTO", "CFO", "Legal"]
    decision_options: ["Proceed to Go/No-Go", "Re-scope", "Terminate"]

  # Risk Mitigation Workflow Gates
  GATE-OPTIONS_IDENTIFIED:
    description: "Alternative options identified (Risk Mitigation)"
    workflow: WF-RISK-MITIGATION
    phase: exploration
    required_documents:
      - {doctype: ALTERNATIVE-EXPLORATION, min_status: approved}
    required_rules:
      - RULE-ALT-MIN-3-OPTIONS
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [ALTERNATIVE-EXPLORATION]}
    approvers: ["Risk Owner", "Decision Owner"]
    decision_options: ["Proceed to Analysis", "More Research"]

  GATE-DECISION_REVIEW:
    description: "Trade-off analysis review (Risk Mitigation)"
    workflow: WF-RISK-MITIGATION
    phase: analysis
    required_documents:
      - {doctype: TRADE-OFF-ANALYSIS, min_status: approved}
    required_rules:
      - RULE-TRADEOFF-CLEAR-WINNER
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [TRADE-OFF-ANALYSIS]}
    approvers: ["Risk Owner", "Tech Lead", "Business Owner"]
    decision_options: ["Proceed to Decision", "Re-evaluate weights"]

  GATE-APPROVAL:
    description: "Mitigation approach approval (Risk Mitigation)"
    workflow: WF-RISK-MITIGATION
    phase: decision
    required_documents:
      - {doctype: ADR, min_status: approved}
    optional_documents:
      - {doctype: DECISION-LOG, min_status: approved}
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [ADR]}
    approvers: ["CTO", "Risk Owner", "Compliance (if applicable)"]
    decision_options: ["Proceed to Implementation", "Reconsider"]

  # Parallel Branching Workflow Gates
  GATE-BRANCH_CREATION:
    description: "Concept branch creation (Parallel Branching)"
    workflow: WF-PARALLEL-BRANCHING
    phase: fork
    required_documents:
      - {doctype: HYPOTHESIS-DOC, min_status: approved}
      - {doctype: CONCEPT-BRANCH, min_status: approved, min_count: 2}
    required_rules:
      - RULE-BRANCH-CLEAR-DIVERGENCE
      - RULE-BRANCH-RESOURCES-ALLOCATED
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [CONCEPT-BRANCH]}
    approvers: ["Research Lead", "Resource Manager"]
    decision_options: ["Proceed with parallel exploration"]

  GATE-MID_POINT_REVIEW:
    description: "Mid-point progress check (Parallel Branching)"
    workflow: WF-PARALLEL-BRANCHING
    phase: exploration
    timing: "Week 2-3 (mid-point)"
    required_documents:
      - {doctype: EXPERIMENT-LOG, min_status: in-progress, per_branch: true}
    required_rules:
      - RULE-BRANCH-PROGRESS-CHECK
    approvers: ["Research Lead"]
    decision_options: ["Continue all branches", "Kill underperforming branch"]

  GATE-RESULTS_REVIEW:
    description: "Branch results review (Parallel Branching)"
    workflow: WF-PARALLEL-BRANCHING
    phase: comparison
    required_documents:
      - {doctype: RESEARCH-FINDINGS, min_status: approved}
      - {doctype: TRADE-OFF-ANALYSIS, min_status: approved}
    required_rules:
      - RULE-BRANCH-FAIR-COMPARISON
    required_satellites:
      - {kind: EVIDENCE, for_doctypes: [RESEARCH-FINDINGS]}
      - {kind: APPROVAL, for_doctypes: [RESEARCH-FINDINGS, TRADE-OFF-ANALYSIS]}
    approvers: ["Research Lead", "CTO"]
    decision_options: ["Proceed to Merge/Kill"]

  GATE-MERGE_KILL_DECISION:
    description: "Concept branch merge/kill decision (Parallel Branching)"
    workflow: WF-PARALLEL-BRANCHING
    phase: merge_kill
    required_documents:
      - {doctype: RESEARCH-FINDINGS, min_status: approved}
      - {doctype: ADR, min_status: approved}
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [RESEARCH-FINDINGS, ADR]}
    approvers: ["Research Lead", "CTO"]
    decision_options: ["Merge Branch X", "Kill Branch Y/Z", "Hybrid (X+Y)"]

# Uwaga: Gate-centric reporting
# Walidator powinien generować raport: które gate'y są zablokowane i przez jakie root-cause błędy.
```

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Doc Types Spec]** `specs_doc_types.md`
  - Type: `requires`
  - Reason: Gates require specific doctypes (required_documents field)

- **[Satellites Spec]** `satelitarne_artefakty_dokumentacyjne_kanwa_opisowa.md`
  - Type: `requires`
  - Reason: Gates require specific satellites (required_satellites field)

### Impacts (Downstream Documents)
- **ALL Templates** (indirectly)
  - Type: `validates`
  - Reason: Gates determine document progression and approval workflows
  - Cascade: `true`

### Related Documents
- **[Doc Types Spec]** `specs_doc_types.md` - Doctypes specify which gates they unlock
- **[Error Codes Spec]** `specs_error_codes.md` - E150 (Gate blocked) uses gate definitions

### Satellite Documents
- **[Changelog]** `satellites/CHANGELOG-GATES-SPEC-001.md`

### Conditional Requirements
```yaml
# Gates themselves contain conditional_requirements
# Example: GATE-REQ_FREEZE requires DPIA only when profile === 'healthcare'
```

### Validation Rules
- [ ] All gates have unique IDs (GATE-GO_NO_GO, GATE-REQ_FREEZE, etc.)
- [ ] All required_documents reference valid doctypes
- [ ] All required_satellites reference valid satellite kinds
- [ ] All approvers are valid roles
- [ ] Conditional_requirements use valid when clauses
