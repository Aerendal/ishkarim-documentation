# 📄 Performance Test Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines performance requirements to test against"
    conditions:
      - when: "project.has_performance_requirements === true"
        applies: true
    sections:
      - from: "PRD §6 Non-Functional Requirements (Performance)"
        to: "§3 Performance Baselines"
        influence: "Performance NFRs define target performance metrics"

  - id: TDD-*
    type: influences
    reason: "TDD defines system architecture affecting performance"
    conditions:
      - when: "project.has_technical_design === true"
        applies: true
    sections:
      - from: "TDD §3 System Architecture"
        to: "§2 Test Scope"
        influence: "System architecture defines performance test scope"

  - id: MONITORING-PLAN-*
    type: influences
    reason: "Monitoring thresholds inform performance test baselines"
    conditions:
      - when: "project.has_monitoring === true"
        applies: true
    sections:
      - from: "Monitoring Plan §3 Alert Thresholds"
        to: "§3 Performance Baselines"
        influence: "Monitoring thresholds provide baseline performance metrics"
```

### Impacts
```yaml
impacts:
  - id: TEST-SUMMARY-REPORT-*
    type: influences
    reason: "Performance test results are part of overall test summary"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 Test Results"
        to: "Test Summary Report §3 Performance Results"
        influence: "Performance test outcomes included in test summary"

  - id: TDD-*
    type: informs
    reason: "Performance bottlenecks may require architecture changes"
    conditions:
      - when: "performance_issues.severity === 'critical'"
        applies: true
    sections:
      - from: "§5 Bottleneck Analysis"
        to: "TDD §3 System Architecture"
        influence: "Performance bottlenecks drive architecture optimizations"

  - id: MONITORING-PLAN-*
    type: informs
    reason: "Performance test results validate monitoring thresholds"
    conditions:
      - when: "project.has_monitoring === true"
        applies: true
    sections:
      - from: "§3 Test Results"
        to: "Monitoring Plan §3 Alert Thresholds"
        influence: "Actual performance data validates or updates monitoring thresholds"
```

### Related
```yaml
related:
  - id: SLA-*
    type: informs
    reason: "Performance test results validate SLA commitments"

  - id: CAPACITY-PLANNING-*
    type: informs
    reason: "Performance results inform capacity planning"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-PERF-TEST-*.md"
    required: false
    purpose: "Track performance optimization tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-PERF-TEST-*.md"
    required: true
    purpose: "Store load test results, performance graphs, profiling data, benchmark reports"

  - type: DoD
    path: "satellites/dod/DOD-PERF-TEST-*.md"
    required: true
    purpose: "Define completion criteria: all scenarios tested, baselines met, bottlenecks identified"
```

## Cel biznesowy / techniczny
Performance Test Report dokumentuje wyniki testów wydajnościowych systemu. Pomaga ocenić, czy system spełnia wymagania dotyczące szybkości, stabilności i skalowalności.

## Zawartość
- Zakres przeprowadzonych testów wydajnościowych
- Konfiguracja środowiska testowego
- Wyniki (czasy odpowiedzi, przepustowość, obciążenie)
- Identyfikacja wąskich gardeł
- Rekomendacje optymalizacyjne

## Czego nie zawiera
- Strategii marketingowych
- Raportów finansowych
- Niezweryfikowanych hipotez

## Objętość
- 2–4 strony
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- QA / testerzy
- Developerzy
- Project managerowie
