> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: ALL-DOC-TEMPLATES-*
    type: requires
    reason: "Specs Doc Types definiuje strukturę i wymagania dla wszystkich typów dokumentów w systemie"
    conditions:
      - when: "project.requires_formal_documentation === true"
        applies: true
    sections:
      - from: "N/A (meta-document)"
        to: "All document templates"
        influence: "Doc types specification definiuje structure, required sections, satellites, dependencies dla każdego document type"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: ALL-TEMPLATES-*
    type: blocks
    reason: "Wszystkie szablony dokumentów muszą comply ze specs defined w Doc Types"
    sections:
      - from: "doctypes section"
        to: "All template documents"
        influence: "Specification definiuje required_meta, required_sections, satellites_required dla każdego typu dokumentu"

  - id: SPECS-GATES-*
    type: influences
    reason: "Doc Types specifications są used by Gates specifications"
    sections:
      - from: "doctypes section"
        to: "Specs Gates gates section"
        influence: "Gates reference doctypes dla required_documents criteria"

  - id: SPECS-ERROR-CODES-*
    type: influences
    reason: "Error codes validate compliance with Doc Types specifications"
    sections:
      - from: "required_sections, satellites_required"
        to: "Specs Error Codes validation rules"
        influence: "Doc Types requirements definiują what error codes validate against"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: SPECS-ERROR-CODES-*
    type: informs
    reason: "Error codes enforce Doc Types specifications"

  - id: SPECS-GATES-*
    type: informs
    reason: "Gates use Doc Types specifications dla document requirements"

  - id: SATELITARNE-ARTEFAKTY-*
    type: informs
    reason: "Satellite artifacts specifications reference Doc Types satellite requirements"
```

### Satellite Documents
```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SPECS-DOC-TYPES-*.md"
    required: false
    purpose: "Documentation standards references, template validation results"

  - type: TODO
    path: "satellites/todos/TODO-SPECS-DOC-TYPES-*.md"
    required: false
    purpose: "Tracking specifications updates, new document types addition"
```

---

```yaml
version: 2

# Kolejność statusów (używane do porównań min_status)
# Extended for Living Documentation Framework (PROPOZYCJA-2)
status_order:
  # Initial states
  - draft              # Initial creation, work in progress
  - in-review          # Under review by stakeholders

  # Active states
  - approved           # Formally approved, active
  - evolving           # Approved but actively evolving (iterative refinement)
  - validating         # Under validation (testing assumptions)
  - refining           # Minor refinements (approved but being polished)

  # Transition states
  - superseded         # Replaced by newer version (still accessible)
  - deprecated         # Marked for sunset (still usable, but discouraged)
  - sunset             # End-of-life announced (sunset date set)

  # Terminal states
  - archived           # No longer active, historical reference only
  - migrated           # Migrated to new document (with migration link)

# Wykrywanie pustych treści / placeholderów
placeholders:
  tokens: ["TBD", "TODO", "...", "<fill>", "<wstaw>", "do uzupełnienia"]
  # Sekcje, w których placeholder może wystąpić bez błędu (np. Appendix)
  allow_in_section_ids: ["SEC-APPENDIX", "SEC-NOTES"]

# Wspólne definicje „satelitów” (artefaktów pomocniczych)
satellites:
  kinds:
    TODO_SECTION: {description: "TODO per sekcja dokumentu"}
    DOR_DOC:      {description: "Definition of Ready dla dokumentu"}
    DOD_DOC:      {description: "Definition of Done dla dokumentu"}
    APPROVAL:     {description: "Approval / sign-off record"}
    EVIDENCE:     {description: "Evidence items + evidence-index"}
    CHANGELOG:    {description: "Historia zmian dokumentu"}
    CR:           {description: "Change Request (zmiana zakresu / dat / budżetu)"}
    ADR:          {description: "Architecture Decision Record"}

# Rejestr typów dokumentów + wymagane sekcje + reguły „wystarczalności”
doctypes:

  EXEC_SUMMARY:
    group: investor
    domain: business
    description: "Executive Summary dla inwestora/grantu"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-EXSUM-GOAL, title: "Cel projektu"}
      - {id: SEC-EXSUM-PROBLEM, title: "Problem / Opportunity"}
      - {id: SEC-EXSUM-SOLUTION, title: "Rozwiązanie"}
      - {id: SEC-EXSUM-MARKET, title: "Rynek"}
      - {id: SEC-EXSUM-MODEL, title: "Model biznesowy"}
      - {id: SEC-EXSUM-ASK, title: "Czego oczekujemy (Ask)"}
      - {id: SEC-EXSUM-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, APPROVAL, EVIDENCE, CHANGELOG]
    dependencies: []
    outputs:
      unlock_gates: [GATE-GO_NO_GO]

  BUSINESS_CASE:
    group: investor
    domain: business
    description: "Business Case (uzasadnienie inwestycji)"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-BC-CONTEXT, title: "Kontekst i cel"}
      - {id: SEC-BC-ALTS, title: "Alternatywy"}
      - {id: SEC-BC-FIN, title: "Finanse i scenariusze"}
      - {id: SEC-BC-ROI, title: "ROI / NPV / założenia"}
      - {id: SEC-BC-RISKS, title: "Ryzyka i mitigacje"}
      - {id: SEC-BC-REC, title: "Rekomendacja"}
      - {id: SEC-BC-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL, EVIDENCE, CHANGELOG]
    dependencies:
      - {doctype: FINANCIAL_PLAN, min_status: in-review}
      - {doctype: MARKET_ANALYSIS, min_status: in-review}
    outputs:
      unlock_gates: [GATE-GO_NO_GO]
    sufficiency_rules:
      - id: RULE-BC-SCENARIOS-MIN3
        severity: BLOCKER
        section_id: SEC-BC-FIN
        check: {kind: min_list_items, min: 3}
        remediation: "Dodaj min. 3 scenariusze (pesymistyczny/realistyczny/optymistyczny) + kluczowe założenia."
      - id: RULE-BC-EVID-REQUIRED
        severity: BLOCKER
        section_id: SEC-BC-EVID
        check: {kind: require_non_placeholder}
        remediation: "Uzupełnij evidence: linki/załączniki (arkusz finansowy, źródła rynku) i opisz ich użycie."
    # Living Documentation Framework (PROPOZYCJA-2)
    lifecycle_config:
      allowed_statuses: [draft, in-review, approved, evolving, validating, refining, deprecated, sunset, archived, migrated]
      default_status: draft
      freshness_threshold_days: 180
      auto_health_check: true
      auto_deprecation_notice: true
    version_config:
      semantic_versioning: true
      major_change_triggers:
        - business_model_changed
        - target_market_pivoted
        - budget_changed_over_20_percent
        - recommendation_flipped
      minor_change_triggers:
        - scenario_added
        - risk_added
        - budget_adjusted_under_20_percent
        - alternative_added
      patch_change_triggers:
        - typo_fix
        - formatting_change
        - clarification
        - roi_calculation_refined
    deprecation_config:
      deprecation_notice_days: 90
      requires_migration_guide: true
      auto_notify_references: true

  FINANCIAL_PLAN:
    group: investor
    domain: finance
    description: "Plan finansowy i projekcje"
    file_extensions: [".md", ".xlsx", ".csv"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-FIN-BUDGET, title: "Budżet"}
      - {id: SEC-FIN-PROJ, title: "Projekcje"}
      - {id: SEC-FIN-ASSUM, title: "Założenia"}
      - {id: SEC-FIN-SCEN, title: "Scenariusze"}
      - {id: SEC-FIN-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, APPROVAL, EVIDENCE, CHANGELOG]
    dependencies: []
    outputs:
      unlock_gates: [GATE-GO_NO_GO]

  MARKET_ANALYSIS:
    group: investor
    domain: business
    description: "Analiza rynku (TAM/SAM/SOM, konkurencja)"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-MKT-SIZE, title: "Wielkość rynku (TAM/SAM/SOM)"}
      - {id: SEC-MKT-TRENDS, title: "Trendy"}
      - {id: SEC-MKT-COMP, title: "Konkurencja"}
      - {id: SEC-MKT-SEG, title: "Segmentacja"}
      - {id: SEC-MKT-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, APPROVAL, EVIDENCE, CHANGELOG]
    dependencies: []
    outputs:
      unlock_gates: [GATE-GO_NO_GO]

  FEASIBILITY:
    group: investor
    domain: engineering
    description: "Studium wykonalności (techniczne/ekonomiczne/prawne)"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-FEAS-TECH, title: "Wykonalność techniczna"}
      - {id: SEC-FEAS-ECO, title: "Wykonalność ekonomiczna"}
      - {id: SEC-FEAS-REG, title: "Wykonalność prawna/regulacyjna"}
      - {id: SEC-FEAS-RISK, title: "Ryzyka i mitigacje"}
      - {id: SEC-FEAS-REC, title: "Rekomendacja (go/pilot/no-go)"}
      - {id: SEC-FEAS-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL, EVIDENCE, CHANGELOG]
    dependencies: []
    outputs:
      unlock_gates: [GATE-GO_NO_GO]

  ROADMAP_PRODUCT:
    group: planning
    domain: product
    description: "Roadmap produktowa (12m)"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-RM-CONTEXT, title: "Kontekst i cele"}
      - {id: SEC-RM-MILESTONES, title: "Milestones / Releases"}
      - {id: SEC-RM-EPICS, title: "Epiki / Feature sets"}
      - {id: SEC-RM-DEPS, title: "Zależności i blokery"}
      - {id: SEC-RM-RISKS, title: "Ryzyka"}
      - {id: SEC-RM-CAP, title: "Capacity / Budżet"}
      - {id: SEC-RM-KPI, title: "KPI i metryki sukcesu"}
      - {id: SEC-RM-GATES, title: "Checkpoints / Gates"}
      - {id: SEC-RM-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, APPROVAL, EVIDENCE, CHANGELOG]
    dependencies:
      - {doctype: BUSINESS_CASE, min_status: in-review}
    outputs:
      unlock_gates: [GATE-REQ_FREEZE]

  PRD:
    group: requirements
    domain: product
    description: "Product Requirements Document"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-PRD-GOAL, title: "Cel produktu"}
      - {id: SEC-PRD-SCOPE, title: "Zakres (In/Out)"}
      - {id: SEC-PRD-PERSONAS, title: "Personas / Użytkownicy"}
      - {id: SEC-PRD-FUNC, title: "Wymagania funkcjonalne"}
      - {id: SEC-PRD-NFR, title: "Wymagania niefunkcjonalne"}
      - {id: SEC-PRD-AC, title: "Kryteria akceptacji"}
      - {id: SEC-PRD-DEPS, title: "Integracje / zależności"}
      - {id: SEC-PRD-RISK, title: "Ryzyka i mitigacje"}
      - {id: SEC-PRD-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL, EVIDENCE, CHANGELOG]
    dependencies:
      - {doctype: BUSINESS_CASE, min_status: approved}
      - {doctype: ROADMAP_PRODUCT, min_status: approved}
    outputs:
      unlock_gates: [GATE-REQ_FREEZE]
    sufficiency_rules:
      - id: RULE-PRD-AC-MIN5
        severity: BLOCKER
        section_id: SEC-PRD-AC
        check: {kind: min_list_items, min: 5}
        remediation: "Dodaj min. 5 kryteriów akceptacji (AC) w sekcji 'Kryteria akceptacji'."
      - id: RULE-PRD-FUNC-MIN10
        severity: ERROR
        section_id: SEC-PRD-FUNC
        check: {kind: min_list_items, min: 10}
        remediation: "Uzupełnij wymagania funkcjonalne: min. 10 user stories (lub uzasadnij mniejszy zakres w BRD)."
    # Living Documentation Framework (PROPOZYCJA-2)
    lifecycle_config:
      allowed_statuses: [draft, in-review, approved, evolving, validating, refining, deprecated, sunset, archived, migrated]
      default_status: draft
      freshness_threshold_days: 90
      auto_health_check: true
      auto_deprecation_notice: true
    version_config:
      semantic_versioning: true
      major_change_triggers:
        - section_removed
        - scope_pivoted
        - breaking_dependency_change
        - target_users_changed
      minor_change_triggers:
        - section_added
        - dependency_added
        - scope_expanded
        - new_functional_requirement
      patch_change_triggers:
        - typo_fix
        - formatting_change
        - clarification
        - acceptance_criteria_clarified
    deprecation_config:
      deprecation_notice_days: 90
      requires_migration_guide: true
      auto_notify_references: true

  HLA:
    group: design
    domain: engineering
    description: "High-Level Architecture"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-HLA-CONTEXT, title: "Kontekst systemu"}
      - {id: SEC-HLA-COMP, title: "Komponenty i odpowiedzialności"}
      - {id: SEC-HLA-FLOWS, title: "Przepływy danych"}
      - {id: SEC-HLA-INTEG, title: "Integracje"}
      - {id: SEC-HLA-RISK, title: "Ryzyka"}
      - {id: SEC-HLA-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, APPROVAL, CHANGELOG]
    dependencies:
      - {doctype: PRD, min_status: in-review}
    outputs:
      unlock_gates: [GATE-REQ_FREEZE]

  TDD:
    group: design
    domain: engineering
    description: "Technical Design Document"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-TDD-OVERVIEW, title: "Overview"}
      - {id: SEC-TDD-MODULES, title: "Moduły / komponenty"}
      - {id: SEC-TDD-API, title: "API"}
      - {id: SEC-TDD-DB, title: "Baza danych / schemat"}
      - {id: SEC-TDD-SEC, title: "Bezpieczeństwo"}
      - {id: SEC-TDD-PERF, title: "Wydajność"}
      - {id: SEC-TDD-OBS, title: "Observability"}
      - {id: SEC-TDD-DEPLOY, title: "Wdrożenie"}
      - {id: SEC-TDD-TEST, title: "Testowanie"}
      - {id: SEC-TDD-ADR, title: "Decyzje (ADR links)"}
      - {id: SEC-TDD-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL, ADR, CHANGELOG]
    dependencies:
      - {doctype: HLA, min_status: approved}
      - {doctype: PRD, min_status: approved}
    outputs:
      unlock_gates: [GATE-RELEASE_READY]
    # Living Documentation Framework (PROPOZYCJA-2)
    lifecycle_config:
      allowed_statuses: [draft, in-review, approved, evolving, validating, refining, deprecated, sunset, archived, migrated]
      default_status: draft
      freshness_threshold_days: 120
      auto_health_check: true
      auto_deprecation_notice: true
    version_config:
      semantic_versioning: true
      major_change_triggers:
        - architecture_pattern_changed
        - technology_stack_changed
        - breaking_api_change
        - database_schema_breaking_change
      minor_change_triggers:
        - new_module_added
        - api_endpoint_added
        - database_table_added
        - new_integration_added
      patch_change_triggers:
        - typo_fix
        - diagram_update
        - clarification
        - performance_tuning_details
    deprecation_config:
      deprecation_notice_days: 60
      requires_migration_guide: true
      auto_notify_references: true

  ADR:
    group: decisions
    domain: engineering
    description: "Architecture Decision Record (wpis)"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-ADR-CONTEXT, title: "Kontekst"}
      - {id: SEC-ADR-OPTIONS, title: "Opcje"}
      - {id: SEC-ADR-DECISION, title: "Decyzja"}
      - {id: SEC-ADR-CONSEQ, title: "Konsekwencje"}
    satellites_required: [APPROVAL]
    dependencies: []
    outputs: {unlock_gates: []}

  TEST_PLAN:
    group: qa
    domain: quality
    description: "Test Plan / QA Strategy"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-TP-SCOPE, title: "Zakres testów"}
      - {id: SEC-TP-TYPES, title: "Typy testów"}
      - {id: SEC-TP-ENV, title: "Środowiska"}
      - {id: SEC-TP-DATA, title: "Test data"}
      - {id: SEC-TP-CRIT, title: "Kryteria pass/fail"}
      - {id: SEC-TP-SCHED, title: "Harmonogram"}
      - {id: SEC-TP-EVID, title: "Źródła / Evidence"}
    satellites_required: [TODO_SECTION, APPROVAL, CHANGELOG]
    dependencies:
      - {doctype: PRD, min_status: approved}
      - {doctype: TDD, min_status: in-review}
    outputs:
      unlock_gates: [GATE-RELEASE_READY]

  RTM:
    group: qa
    domain: quality
    description: "Requirements Traceability Matrix"
    file_extensions: [".csv", ".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections: []
    satellites_required: [CHANGELOG]
    dependencies:
      - {doctype: PRD, min_status: approved}
      - {doctype: TEST_PLAN, min_status: in-review}
    outputs:
      unlock_gates: [GATE-REQ_FREEZE]

  RUNBOOK:
    group: ops
    domain: operations
    description: "Operations Runbook"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-RB-STARTSTOP, title: "Start/Stop"}
      - {id: SEC-RB-MON, title: "Monitoring"}
      - {id: SEC-RB-INC, title: "Incydenty"}
      - {id: SEC-RB-ROLL, title: "Rollback"}
      - {id: SEC-RB-CONTACT, title: "Kontakty / Eskalacje"}
    satellites_required: [APPROVAL, CHANGELOG]
    dependencies:
      - {doctype: TDD, min_status: in-review}
    outputs:
      unlock_gates: [GATE-OPS_HANDOVER, GATE-RELEASE_READY]

  MONITORING_PLAN:
    group: ops
    domain: operations
    description: "Monitoring & Observability Plan"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-MON-METRICS, title: "Metryki"}
      - {id: SEC-MON-ALERTS, title: "Alerty"}
      - {id: SEC-MON-DASH, title: "Dashboardy"}
      - {id: SEC-MON-SLO, title: "SLO/SLI"}
    satellites_required: [APPROVAL, CHANGELOG]
    dependencies:
      - {doctype: RUNBOOK, min_status: in-review}
    outputs:
      unlock_gates: [GATE-OPS_HANDOVER]

  SECURITY_PLAN:
    group: compliance
    domain: security
    description: "Security Plan"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-SEC-CTRL, title: "Kontrole bezpieczeństwa"}
      - {id: SEC-SEC-ACCESS, title: "Dostęp i uprawnienia"}
      - {id: SEC-SEC-CRYPTO, title: "Szyfrowanie"}
      - {id: SEC-SEC-IR, title: "Incident Response (link do SIRP)"}
      - {id: SEC-SEC-COMP, title: "Zgodność"}
    satellites_required: [APPROVAL, EVIDENCE, CHANGELOG]
    dependencies: []
    outputs:
      unlock_gates: [GATE-REQ_FREEZE, GATE-RELEASE_READY]

  DPIA:
    group: compliance
    domain: legal
    description: "Data Privacy Impact Assessment"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-DPIA-FLOWS, title: "Przepływy danych"}
      - {id: SEC-DPIA-DATA, title: "Kategorie danych"}
      - {id: SEC-DPIA-RISK, title: "Ocena ryzyka"}
      - {id: SEC-DPIA-MIT, title: "Mitigacje"}
      - {id: SEC-DPIA-APP, title: "Zatwierdzenia"}
    satellites_required: [APPROVAL, EVIDENCE, CHANGELOG]
    dependencies:
      - {doctype: SECURITY_PLAN, min_status: in-review}
    outputs:
      unlock_gates: [GATE-REQ_FREEZE]

  SIRP:
    group: ops
    domain: security
    description: "Security Incident Response Plan"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-SIRP-ROLES, title: "Role"}
      - {id: SEC-SIRP-STEPS, title: "Procedury"}
      - {id: SEC-SIRP-COMMS, title: "Komunikacja"}
      - {id: SEC-SIRP-POST, title: "Postmortem"}
    satellites_required: [APPROVAL, CHANGELOG]
    dependencies:
      - {doctype: SECURITY_PLAN, min_status: in-review}
    outputs:
      unlock_gates: [GATE-OPS_HANDOVER]

  DRP:
    group: ops
    domain: operations
    description: "Disaster Recovery Plan"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-DRP-SCEN, title: "Scenariusze awarii"}
      - {id: SEC-DRP-RTO, title: "RTO/RPO"}
      - {id: SEC-DRP-REST, title: "Odtwarzanie"}
      - {id: SEC-DRP-TEST, title: "Testy DRP"}
    satellites_required: [APPROVAL, CHANGELOG]
    dependencies: []
    outputs:
      unlock_gates: [GATE-OPS_HANDOVER]

  BCP:
    group: ops
    domain: operations
    description: "Business Continuity Plan"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-BCP-PROCS, title: "Procesy krytyczne"}
      - {id: SEC-BCP-PLAN, title: "Plan ciągłości"}
      - {id: SEC-BCP-COMMS, title: "Komunikacja kryzysowa"}
      - {id: SEC-BCP-TEST, title: "Ćwiczenia"}
    satellites_required: [APPROVAL, CHANGELOG]
    dependencies: []
    outputs:
      unlock_gates: [GATE-OPS_HANDOVER]

  SPRINT_OUTPUT_CONTRACT:
    group: sprint
    domain: delivery
    description: "Sprint Output Contract"
    file_extensions: [".md"]
    required_meta: [id, doctype, status, version, owner, project]
    required_sections:
      - {id: SEC-SPR-GOAL, title: "Sprint Goal"}
      - {id: SEC-SPR-BACKLOG, title: "Backlog z deklaracją output"}
      - {id: SEC-SPR-EVID, title: "Evidence"}
      - {id: SEC-SPR-APP, title: "Akceptacja"}
    satellites_required: [APPROVAL]
    dependencies: []
    outputs:
      unlock_gates: []
```
