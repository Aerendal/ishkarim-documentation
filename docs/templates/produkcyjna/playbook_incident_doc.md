# Playbook „Co‑jeśli” — <Scenariusz>

> Procedura reakcji na określone zdarzenia/warunki. Używaj w sytuacjach zgodnych z triggerami.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: RUNBOOK
    type: operational_procedures
    from_sections:
      - operational_steps
      - system_commands
    to_sections:
      - incident_procedures
      - remediation_actions
    influence: "Runbook dostarcza procedur operacyjnych"
    when:
      condition: playbook.type == "incident"
      applies: always

  - id: MONITORING-PLAN
    type: detection_triggers
    from_sections:
      - alert_definitions
      - metric_thresholds
    to_sections:
      - incident_triggers
      - detection_criteria
    influence: "Monitoring definiuje kiedy uruchomić playbook"
    when:
      condition: monitoring.configured == true
      applies: always

  - id: BCP
    type: continuity_requirements
    from_sections:
      - rto_rpo_targets
      - recovery_priorities
    to_sections:
      - response_timeframes
      - escalation_criteria
    influence: "BCP określa wymagania czasowe i priorytety"
    when:
      condition: incident.is_critical == true
      applies: conditionally
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: INCIDENT-LOG
    type: execution_record
    from_sections:
      - playbook_execution
      - actions_taken
    to_sections:
      - incident_timeline
      - resolution_documentation
    influence: "Wykonanie playbooku jest dokumentowane w logu incydentu"
    when:
      condition: playbook.executed == true
      applies: always

  - id: POST-MORTEM
    type: lessons_learned
    from_sections:
      - incident_response
      - effectiveness_assessment
    to_sections:
      - improvement_actions
      - playbook_updates
    influence: "Incydenty prowadzą do ulepszeń playbooków"
    when:
      condition: incident.resolved == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: ESCALATION-MATRIX
    relationship: communication_protocol
    sections_mapping:
      - from: escalation_paths
        to: stakeholder_notification
    usage: "Matryca eskalacji określa ścieżki komunikacji"
```

### Satellite Documents

```yaml
satellites:
  - name: INCIDENT-CHECKLIST
    purpose: "Checklista kroków podczas incydentu"
    trigger: per_incident
    lifecycle: incident_duration
    retention: permanent
```

---
## 0. Metadane
- **Wersja**: `<vX.Y>`
- **Właściciel (On-call / Duty)**: `<rola/osoba>`
- **Zespół**: `<...>`
- **Dotyczy systemów**: `<usługi/komponenty>`
- **SEV mapa**: `SEV0 (krytyczny) … SEV3 (niski)`

## 1. Sygnały i triggery
- **Warunki wejścia**: `<progi alertów, zdarzenia logów, symptomy>`
- **Wykluczenia / false-positive**: `<...>`

## 2. Triage — pierwsze 5 minut
- [ ] Potwierdź alert i przypisz Ownera (czas: `<X min>`)
- [ ] Zbierz podstawowe metryki/telemetrię
- [ ] Określ SEV i wpływ (klienci, zakres)
- [ ] Komunikat w `<kanał>` z szablonu (poniżej)

## 3. Drzewo decyzyjne (reguły „If‑Then‑Because”)
| If (warunek) | Then (akcja) | Because (uzasadnienie) | Owner | Limit czasu |
|---|---|---|---|---|
| `<np. błąd 5xx > 3% przez 5 min>` | `<włącz FF: degrade_mode>` | `<ochrona SLO>` | `<on-call>` | `<5 min>` |
| `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

## 4. Procedury
### 4.1 Kontenerzacja/Izolacja (Containment)
- `<kroki>`
### 4.2 Diagnoza
- `<checklisty, zapytania, grafana/kibana linki>`
### 4.3 Remediacja
- `<komendy, playbooki zależne>`
### 4.4 Rollback/Failover
- `<jak przełączyć, kryteria powrotu>`

## 5. Komunikacja
- **Kanał incydentu**: `<#kanał>`
- **Szablon komunikatu**:  
  `SEV<k> | <system> | <objawy> | start <HH:MMZ> | Owner <imię> | ETA <…>`
- **Stakeholderzy (RACI)**: R `<...>` / A `<...>` / C `<...>` / I `<...>`

## 6. Kryteria zamknięcia
- [ ] Wskaźniki w normie przez `<T>`
- [ ] Przywrócono normalny poziom usług
- [ ] Zapis w dzienniku incydentu + linki do logów/metryk

## 7. Post‑mortem / Lessons Learned
- **Data**: `<...>`
- **Root cause**: `<...>`
- **Akcje korekcyjne (SMART)**:  
  - [ ] `<akcja>` Owner: `<>` Do: `<YYYY-MM-DD>`

## 8. Załączniki
- **Runbooki powiązane**: `<linki>`
- **Dashboardy/alerty**: `<linki>`
