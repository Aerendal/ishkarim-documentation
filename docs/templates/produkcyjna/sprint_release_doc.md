# Szablon Sprintu — RELEASE

> Przygotowanie i dowiezienie wydania produkcyjnego z kontrolą ryzyka.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: SPRINT-HARDENING
    type: quality_gate_predecessor
    from_sections:
      - slo_confirmation
      - defect_resolution
      - stability_verification
    to_sections:
      - release_readiness_criteria
      - go_nogo_assessment
    influence: "Hardening musi potwierdzić stabilność przed release"
    when:
      condition: sprint.type == "release"
      applies: always

  - id: ROADMAP
    type: feature_scope
    from_sections:
      - planned_features
      - release_milestones
    to_sections:
      - release_scope
      - feature_list
    influence: "Roadmapa określa co wchodzi do wydania"
    when:
      condition: sprint.planning_phase == true
      applies: always

  - id: CHANGELOG
    type: release_content
    from_sections:
      - completed_features
      - bug_fixes
      - breaking_changes
    to_sections:
      - release_notes_content
      - migration_guide_needs
    influence: "Changelog dostarcza treści do komunikacji o wydaniu"
    when:
      condition: sprint.documentation_phase == true
      applies: always

  - id: COMPLIANCE-CHECKLIST
    type: regulatory_requirement
    from_sections:
      - license_compliance
      - data_privacy_requirements
      - security_standards
    to_sections:
      - release_gate_checklist
      - approval_requirements
    influence: "Wymagania compliance determinują checklistę wydania"
    when:
      condition: project.has_compliance_requirements == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: RELEASE-NOTES
    type: user_documentation
    from_sections:
      - new_features
      - improvements
      - bug_fixes
      - breaking_changes
    to_sections:
      - user_facing_documentation
      - migration_guide
    influence: "Sprint release generuje oficjalną dokumentację wydania"
    when:
      condition: sprint.completed == true
      applies: always

  - id: DEPLOYMENT-LOG
    type: audit_trail
    from_sections:
      - deployment_execution
      - rollback_events
      - verification_results
    to_sections:
      - production_history
      - incident_reference
    influence: "Release tworzy audytowalny ślad wdrożenia produkcyjnego"
    when:
      condition: deployment.completed == true
      applies: always

  - id: CUSTOMER-COMMUNICATION
    type: stakeholder_notification
    from_sections:
      - release_announcement
      - known_issues
      - support_readiness
    to_sections:
      - email_campaigns
      - support_tickets_prep
    influence: "Release wymaga komunikacji z klientami i supportem"
    when:
      condition: release.affects_users == true
      applies: always

  - id: POST-RELEASE-MONITORING
    type: observability_activation
    from_sections:
      - feature_flags_status
      - monitoring_dashboards
      - alert_rules
    to_sections:
      - active_monitoring_plan
      - incident_watch_period
    influence: "Release aktywuje wzmożony monitoring przez okres stabilizacji"
    when:
      condition: deployment.completed == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: DEPLOYMENT-RUNBOOK
    relationship: execution_procedure
    sections_mapping:
      - from: deployment_steps
        to: release_execution_plan
    usage: "Runbook definiuje szczegółowe kroki wdrożenia"

  - id: ROLLBACK-PLAN
    relationship: contingency
    sections_mapping:
      - from: rollback_procedures
        to: nogo_actions
    usage: "Plan rollback określa jak wycofać wydanie w przypadku problemów"

  - id: FEATURE-FLAGS-CONFIG
    relationship: risk_mitigation
    sections_mapping:
      - from: flag_definitions
        to: gradual_rollout_strategy
    usage: "Feature flags umożliwiają stopniowe udostępnianie funkcji"

  - id: GO-NOGO-CHECKLIST
    relationship: decision_framework
    sections_mapping:
      - from: criteria_definitions
        to: release_decision
    usage: "Checklist strukturyzuje decyzję o wydaniu produkcyjnym"
```

### Satellite Documents

```yaml
satellites:
  - name: RELEASE-CANDIDATE-TAG
    purpose: "Tag w repozytorium oznaczający kandydata do wydania"
    trigger: code_freeze
    lifecycle: permanent
    retention: permanent

  - name: UAT-SIGN-OFF
    purpose: "Formalne zatwierdzenie przez biznes/QA"
    trigger: before_release
    lifecycle: single_event
    retention: permanent

  - name: DEPLOYMENT-CHECKLIST-EXECUTED
    purpose: "Wypełniona checklista z podpisami odpowiedzialnych"
    trigger: during_deployment
    lifecycle: single_event
    retention: permanent

  - name: POST-RELEASE-METRICS
    purpose: "Metryki z pierwszych 24-48h po wydaniu"
    trigger: after_deployment
    lifecycle: monitoring_period
    retention: 6_months
```

---
## 0. Metryki nagłówka
- **Sprint ID**: `<YYYY‑MM‑DD / Release‑N>`
- **Zespół / Obszar**: `<...>`
- **Czas trwania**: `<start → koniec>`
- **Okno wydania (freeze → prod)**: `<daty>`
- **Tryb sprintu**: `release`

## 1. Cel sprintu
- `<wydanie wersji X.Y z funkcjami A/B/C>`
- **Kryteria sukcesu**: `<deployment bez rollbacku, NPS, brak P0>`

## 2. Zakres
- **Zmiany wchodzące**: `<lista epików/feature'ów>`
- **Poza zakresem**: `<...>`

## 3. Bramka jakości wydania
- [ ] Code freeze od `<data>`
- [ ] Smoke/UAT na prod‑like zaliczone
- [ ] Checklisty zgodności/licencji podpisane
- [ ] Plan komunikacji do klientów/Supportu gotowy
- [ ] Runbook wdrożenia + rollback przetestowany

## 4. CI/CD i wersjonowanie
- **Strategia release**: `<tagi, gałęzie, artefakty>`
- **Migracje danych/DB**: `<plan>`
- **Feature flags**: `<lista, stany startowe>`

## 5. Kryteria „Go/No‑Go”
- **Go**: `<metryki, testy, ryzyko>`
- **No‑Go**: `<progi, scenariusze>`
- **Komitet decyzyjny**: `<RACI>`

## 6. Noty wydania i komunikacja
- **RELEASE_NOTES**: `<link>`
- **CHANGELOG**: `<link>`
- **Komunikaty**: `<kanały, harmonogram>`

---
## Bramka „START”
- [ ] Freeze + zakres potwierdzone
- [ ] UAT/Smoke plan i środowiska gotowe
- [ ] Plan komunikacji uzgodniony
## Bramka „CLOSE”
- [ ] Wydanie na PROD zakończone sukcesem
- [ ] Telemetria i SLO w normie po `<T>`
- [ ] Noty wydania/CHANGELOG opublikowane
