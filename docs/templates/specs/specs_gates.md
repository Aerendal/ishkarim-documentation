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

  GATE-HYPOTHESIS_REVIEW:
    description: "Hypothesis validation checkpoint (Tech Exploration / Business Innovation)"
    required_documents:
      - {doctype: HYPOTHESIS-DOC, min_status: approved}
    required_rules:
      - RULE-HYP-TESTABLE
      - RULE-HYP-SUCCESS-CRITERIA
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [HYPOTHESIS-DOC]}
    approvers: ["Research Lead", "Product Owner"]

  GATE-VALIDATION_GATE:
    description: "Research validation checkpoint (Tech Exploration)"
    required_documents:
      - {doctype: RESEARCH-FINDINGS, min_status: approved}
    required_satellites:
      - {kind: EVIDENCE, for_doctypes: [RESEARCH-FINDINGS]}
      - {kind: APPROVAL, for_doctypes: [RESEARCH-FINDINGS]}
    approvers: ["Tech Lead", "Product Owner"]

  GATE-OPTIONS_IDENTIFIED:
    description: "Alternative options identified (Risk Mitigation)"
    required_documents:
      - {doctype: ALTERNATIVE-EXPLORATION, min_status: approved}
    required_rules:
      - RULE-ALT-MIN-3-OPTIONS
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [ALTERNATIVE-EXPLORATION]}
    approvers: ["Decision Owner"]

  GATE-MERGE_KILL_DECISION:
    description: "Concept branch merge/kill decision (Parallel Branching)"
    required_documents:
      - {doctype: RESEARCH-FINDINGS, min_status: approved}
      - {doctype: ADR, min_status: approved}
    required_satellites:
      - {kind: APPROVAL, for_doctypes: [RESEARCH-FINDINGS, ADR]}
    approvers: ["Research Lead", "CTO"]

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
