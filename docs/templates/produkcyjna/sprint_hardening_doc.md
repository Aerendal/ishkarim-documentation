# Szablon Sprintu — HARDENING / Stabilization

> Fokus na defektach krytycznych, wydajności, bezpieczeństwie i dokumentacji.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: BUG-TRACKER
    type: defect_input
    from_sections:
      - p0_p1_bugs
      - regression_issues
      - customer_escalations
    to_sections:
      - defect_backlog
      - priority_list
    influence: "Krytyczne defekty determinują zakres hardening sprintu"
    when:
      condition: sprint.type == "hardening"
      applies: always

  - id: PERFORMANCE-BASELINE
    type: quality_standard
    from_sections:
      - slo_targets
      - performance_benchmarks
    to_sections:
      - nfr_goals
      - acceptance_criteria
    influence: "Baseline określa cele wydajnościowe sprintu"
    when:
      condition: sprint.has_performance_goals == true
      applies: always

  - id: SECURITY-SCAN-RESULTS
    type: vulnerability_input
    from_sections:
      - critical_high_vulns
      - sast_dast_findings
    to_sections:
      - security_tasks
      - remediation_plan
    influence: "Wyniki skanów definiują zadania security"
    when:
      condition: scan.has_critical_findings == true
      applies: always

  - id: SPRINT-CORE
    type: predecessor
    from_sections:
      - incomplete_nfr
      - discovered_issues
    to_sections:
      - technical_debt_items
      - stability_tasks
    influence: "Niedokończone NFR z core sprintu trafiają do hardening"
    when:
      condition: core_sprint.has_carryover_nfr == true
      applies: conditionally
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: SPRINT-RELEASE
    type: release_readiness
    from_sections:
      - stabilization_results
      - slo_confirmation
      - defect_resolution
    to_sections:
      - release_quality_gate
      - go_nogo_criteria
    influence: "Hardening potwierdza gotowość do wydania produkcyjnego"
    when:
      condition: sprint.completed == true AND results.meets_slo == true
      applies: always

  - id: RUNBOOK
    type: operational_documentation
    from_sections:
      - incident_scenarios
      - recovery_procedures
    to_sections:
      - troubleshooting_guide
      - escalation_paths
    influence: "Hardening aktualizuje procedury operacyjne"
    when:
      condition: sprint.has_operational_updates == true
      applies: always

  - id: PERFORMANCE-REPORT
    type: measurement
    from_sections:
      - load_test_results
      - stress_test_results
      - soak_test_results
    to_sections:
      - capacity_planning
      - scaling_recommendations
    influence: "Testy wydajnościowe dostarczają danych do planowania capacity"
    when:
      condition: sprint.has_performance_tests == true
      applies: always

  - id: TECH-DEBT-REGISTER
    type: quality_improvement
    from_sections:
      - code_quality_improvements
      - refactoring_completed
    to_sections:
      - resolved_debt_items
      - quality_metrics_update
    influence: "Hardening redukuje dług techniczny"
    when:
      condition: sprint.has_debt_reduction == true
      applies: conditionally
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: SLO-DEFINITION-DOC
    relationship: quality_contract
    sections_mapping:
      - from: service_level_objectives
        to: acceptance_thresholds
    usage: "SLO definiują cele jakościowe hardening sprintu"

  - id: MONITORING-PLAN
    relationship: observability
    sections_mapping:
      - from: metrics_definitions
        to: verification_criteria
    usage: "Plan monitoringu weryfikuje osiągnięcie SLO"

  - id: INCIDENT-PLAYBOOK
    relationship: operational_readiness
    sections_mapping:
      - from: incident_procedures
        to: stability_requirements
    usage: "Playbooki informują o wymaganiach stabilnościowych"
```

### Satellite Documents

```yaml
satellites:
  - name: PERFORMANCE-TEST-RESULTS
    purpose: "Szczegółowe wyniki testów wydajnościowych"
    trigger: after_performance_tests
    lifecycle: sprint_duration
    retention: 6_months

  - name: SECURITY-REMEDIATION-LOG
    purpose: "Śledzenie napraw luk bezpieczeństwa"
    trigger: during_security_fixes
    lifecycle: sprint_duration
    retention: permanent

  - name: DEFECT-RESOLUTION-REPORT
    purpose: "Raport rozwiązanych defektów P0/P1"
    trigger: at_closure
    lifecycle: single_event
    retention: permanent

  - name: SLO-VERIFICATION-EVIDENCE
    purpose: "Dowody potwierdzenia SLO na prod-like env"
    trigger: after_verification
    lifecycle: sprint_duration
    retention: 1_year
```

---
## 0. Metryki nagłówka
- **Sprint ID**: `<YYYY‑MM‑DD / Hardening‑N>`
- **Zespół / Obszar**: `<...>`
- **Czas trwania**: `<start → koniec>`
- **Capacity (osobodni)**: `<...>`
- **Tryb sprintu**: `hardening`

## 1. Cel sprintu
- `<stabilizacja pod wydanie / redukcja defektów / spełnienie SLO>`
- **KPI**: `<defect leakage ↓, TTR ↓, SLO potwierdzone>`

## 2. Zakres i priorytety
- **Defekty (P0/P1)**: `<lista>`
- **Wydajność**: `<cele P95/P99, throughput>`
- **Bezpieczeństwo**: `<minimum poziomu, np. brak High/Critical>`
- **Dokumentacja**: `<playbooki, runbooki, README>`

## 3. DoD rozszerzone
- [ ] Testy niefunkcjonalne: performance/load/stress
- [ ] Wyniki skanów SAST/DAST/Dependency: `0 High/Critical`
- [ ] Testy regresji automatyczne przechodzą
- [ ] Runbook/Playbook uzupełnione
- [ ] SLO/SLI potwierdzone na środowisku prod‑like
- [ ] Plan rollback zweryfikowany

## 4. Obserwowalność i jakość
- **Dashboards**: `<linki>`
- **Alerty**: `<progi i test alertingu>`
- **Budżet błędu**: `<bieżący stan>`

## 5. Ryzyka i zależności
- `<...>`

---
## Bramka „START”
- [ ] Zestaw defektów i NFR uzgodniony
- [ ] Środowisko prod‑like dostępne
- [ ] Narzędzia do pomiarów gotowe
## Bramka „CLOSE”
- [ ] Wszystkie P0/P1 zamknięte lub zdeeskalowane
- [ ] SLO osiągnięte/potwierdzone
- [ ] Wyniki testów i skanów załączone
