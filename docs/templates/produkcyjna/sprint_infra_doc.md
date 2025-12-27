# Szablon Sprintu — INFRA / Platform / Migration

> Outputem są zmiany w IaC, pipeline'ach, konfiguracjach i playbookach operacyjnych.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: INFRASTRUCTURE-ROADMAP
    type: strategic_planning
    from_sections:
      - platform_modernization_goals
      - cost_optimization_targets
      - scalability_requirements
    to_sections:
      - sprint_objectives
      - migration_scope
    influence: "Roadmapa infrastruktury określa priorytety modernizacji"
    when:
      condition: sprint.type == "infra"
      applies: always

  - id: CAPACITY-PLANNING-DOC
    type: sizing_input
    from_sections:
      - projected_load
      - growth_forecasts
    to_sections:
      - infrastructure_sizing
      - resource_allocation
    influence: "Planowanie capacity determinuje rozmiar infrastruktury"
    when:
      condition: sprint.involves_scaling == true
      applies: conditionally

  - id: SECURITY-ARCHITECTURE
    type: security_requirements
    from_sections:
      - network_policies
      - secrets_management
      - compliance_controls
    to_sections:
      - security_configuration
      - access_control_setup
    influence: "Architektura security definiuje wymagania bezpieczeństwa IaC"
    when:
      condition: sprint.has_security_implications == true
      applies: always

  - id: DISASTER-RECOVERY-PLAN
    type: resilience_requirements
    from_sections:
      - rto_rpo_targets
      - backup_requirements
      - ha_requirements
    to_sections:
      - dr_configuration
      - backup_automation
    influence: "Plan DR określa wymagania odtwarzalności infrastruktury"
    when:
      condition: sprint.affects_dr == true
      applies: conditionally
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: RUNBOOK
    type: operational_procedures
    from_sections:
      - infrastructure_changes
      - new_components
      - configuration_updates
    to_sections:
      - updated_procedures
      - troubleshooting_guides
    influence: "Zmiany infrastruktury wymagają aktualizacji runbooków"
    when:
      condition: sprint.completed == true
      applies: always

  - id: MONITORING-PLAN
    type: observability_update
    from_sections:
      - new_resources
      - configuration_changes
    to_sections:
      - monitoring_coverage
      - alert_rules
    influence: "Nowa infrastruktura wymaga nowego monitoringu"
    when:
      condition: sprint.adds_resources == true
      applies: always

  - id: COST-TRACKING
    type: financial_impact
    from_sections:
      - resource_allocation
      - license_costs
      - operational_costs
    to_sections:
      - budget_updates
      - cost_optimization_opportunities
    influence: "Zmiany infra wpływają na koszty operacyjne"
    when:
      condition: sprint.completed == true
      applies: always

  - id: COMPLIANCE-AUDIT-LOG
    type: regulatory_trail
    from_sections:
      - iac_changes
      - security_updates
      - access_control_changes
    to_sections:
      - audit_evidence
      - compliance_reporting
    influence: "Zmiany infrastruktury muszą być audytowalne"
    when:
      condition: project.has_compliance_requirements == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: IaC-STANDARDS-DOC
    relationship: coding_standards
    sections_mapping:
      - from: terraform_conventions
        to: code_quality_requirements
    usage: "Standardy IaC zapewniają spójność kodu infrastruktury"

  - id: NETWORK-ARCHITECTURE
    relationship: design_blueprint
    sections_mapping:
      - from: network_topology
        to: vpc_subnet_configuration
    usage: "Architektura sieci definiuje topologię infrastruktury"

  - id: SECRETS-MANAGEMENT-POLICY
    relationship: security_compliance
    sections_mapping:
      - from: rotation_policies
        to: secret_configuration
    usage: "Polityka sekretów określa zarządzanie kluczami i hasłami"

  - id: MIGRATION-PLAYBOOK
    relationship: execution_guide
    sections_mapping:
      - from: migration_steps
        to: sprint_execution_plan
    usage: "Playbook migracji strukturyzuje proces przejścia"
```

### Satellite Documents

```yaml
satellites:
  - name: IaC-CODE-REVIEW
    purpose: "Peer review zmian w kodzie infrastruktury"
    trigger: before_merge
    lifecycle: per_change
    retention: permanent

  - name: TERRAFORM-PLAN-OUTPUT
    purpose: "Output z terraform plan przed apply"
    trigger: before_deployment
    lifecycle: per_deployment
    retention: 3_months

  - name: INFRASTRUCTURE-TEST-RESULTS
    purpose: "Wyniki testów odtwarzalności (destroy/apply)"
    trigger: during_testing
    lifecycle: sprint_duration
    retention: 6_months

  - name: BACKUP-RESTORE-VERIFICATION
    purpose: "Dowody weryfikacji procedur backup/restore"
    trigger: after_dr_testing
    lifecycle: per_test
    retention: 1_year

  - name: NETWORK-DIAGRAM-UPDATES
    purpose: "Zaktualizowane diagramy topologii sieci"
    trigger: after_infrastructure_changes
    lifecycle: continuous
    retention: permanent
```

---
## 0. Metryki nagłówka
- **Sprint ID**: `<YYYY‑MM‑DD / Infra‑N>`
- **Zespół / Obszar**: `<Platform/DevOps/SRE>`
- **Czas trwania**: `<start → koniec>`
- **Capacity (osobodni)**: `<...>`
- **Tryb sprintu**: `infra/platform/migration`

## 1. Cel sprintu
- `<np. migracja do Kubernetes 1.xx / modernizacja CI>`
- **KPI**: `<czas deploy ↓, MTTR ↓, koszt infra ↓>`

## 2. Zakres i ryzyka
- **Zmiany IaC**: `<repo, moduły, wersje>`
- **Kompatybilność**: `<API, runtime, OS, sieć>`
- **Okna serwisowe**: `<daty/godziny>`
- **Licencje / koszty**: `<budżet, compliance>`

## 3. DoD (Infra)
- [ ] Review bezpieczeństwa (secrets, polityki)
- [ ] Testy odtwarzalności środowisk (destroy/apply)
- [ ] Backupy/restore przetestowane (jeśli dotyczy)
- [ ] Runbook/Playbook zaktualizowane
- [ ] Monitoring/alerting skonfigurowany
- [ ] DR/HA scenariusze zweryfikowane (jeśli dotyczy)

## 4. Plan i zależności
- **Etapy**: `<przygotowanie → migracja → weryfikacja → stabilizacja>`
- **Kontrakty i interfejsy**: `<API, protokoły, wersje>`
- **Zespoły zależne**: `<lista>`

## 5. Bezpieczeństwo i dane
- **Skan zależności i obrazy**: `<narzędzia, progi>`
- **Zasady kluczy i rotacja**: `<...>`
- **Dane (PII/RODO)**: `<klasyfikacja, maskowanie>`

---
## Bramka „START”
- [ ] Zatwierdzone zmiany IaC i okna serwisowe
- [ ] Plan rollback i backup gotowe
- [ ] Zgody compliance (jeśli wymagane)
## Bramka „CLOSE”
- [ ] Migracja zakończona, weryfikacja OK
- [ ] Runbooki/monitoring zaktualizowane
- [ ] Raport powdrożeniowy opublikowany
