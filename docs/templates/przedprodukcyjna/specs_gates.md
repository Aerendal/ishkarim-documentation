> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: SPECS-DOC-TYPES-*
    type: requires
    reason: "Gates specifications reference Doc Types dla required_documents criteria"
    sections:
      - from: "Specs Doc Types doctypes list"
        to: "Gates required_documents sections"
        influence: "Doc Types definiują which documents can be required at gates"

  - id: SPECS-ERROR-CODES-*
    type: requires
    reason: "Gates use Error Codes dla validation rules i blocking conditions"
    sections:
      - from: "Specs Error Codes validation rules"
        to: "Gates required_rules sections"
        influence: "Error codes (RULE-BC-SCENARIOS-MIN3, etc.) definiują gate passing criteria"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROJECT-GOVERNANCE-*
    type: blocks
    reason: "Gates definiują decision checkpoints dla all projects"
    sections:
      - from: "Gates (GO_NO_GO, REQ_FREEZE, RELEASE_READY, OPS_HANDOVER)"
        to: "Project lifecycle decision points"
        influence: "Gates structure project progression i approval workflows"

  - id: ALL-REQUIRED-DOCS-*
    type: blocks
    reason: "Gates determine which documents muszą być completed dla project progression"
    sections:
      - from: "required_documents per gate"
        to: "Document creation priorities"
        influence: "Gate requirements drive documentation planning i priorities"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: PROJECT-CHARTER-*
    type: informs
    reason: "Project Charter approvals są often gate prerequisites"

  - id: PROJECT-MGMT-PLAN-*
    type: informs
    reason: "Project Management Plan incorporates gate timing w project schedule"

  - id: SATELITARNE-ARTEFAKTY-*
    type: informs
    reason: "Gates require satellite artifacts (APPROVAL, EVIDENCE, etc.)"
```

### Satellite Documents
```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SPECS-GATES-*.md"
    required: false
    purpose: "Gate review records, approval workflows, gate passing history"

  - type: TODO
    path: "satellites/todos/TODO-SPECS-GATES-*.md"
    required: false
    purpose: "Tracking gate criteria refinements, new gates addition, conditional requirements updates"
```

---

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

# Uwaga: Gate-centric reporting
# Walidator powinien generować raport: które gate’y są zablokowane i przez jakie root-cause błędy.
```
