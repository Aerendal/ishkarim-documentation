# Rules‑Spec — Specyfikacja Reguł

> Szablon definicji reguł dla silnika reguł/automatyzacji lub polityk biznesowych.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: BRD
    type: business_requirements
    from_sections:
      - business_rules
      - decision_logic
      - constraints
    to_sections:
      - rule_definitions
      - rule_conditions
      - rule_actions
    influence: "Wymagania biznesowe definiują reguły do implementacji"
    when:
      condition: spec.type == "rules"
      applies: always

  - id: PRD
    type: product_requirements
    from_sections:
      - feature_specifications
      - user_workflows
    to_sections:
      - trigger_definitions
      - action_specifications
    influence: "PRD określa triggery i akcje dla reguł"
    when:
      condition: product.has_rules_based_features == true
      applies: always

  - id: DATA-MODEL
    type: data_context
    from_sections:
      - entity_definitions
      - attribute_specifications
    to_sections:
      - rule_scope
      - condition_expressions
    influence: "Model danych definiuje encje i atrybuty używane w regułach"
    when:
      condition: rules.use_data_model == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: RULES-ENGINE-IMPLEMENTATION
    type: technical_implementation
    from_sections:
      - rule_specifications
      - rule_format
    to_sections:
      - engine_configuration
      - rule_deployment
    influence: "Specyfikacja reguł jest implementowana w silniku reguł"
    when:
      condition: spec.approved == true
      applies: always

  - id: RULE-TESTS
    type: quality_assurance
    from_sections:
      - rule_definitions
      - expected_outcomes
    to_sections:
      - test_scenarios
      - validation_cases
    influence: "Reguły wymagają testów weryfikujących poprawność"
    when:
      condition: rules.require_testing == true
      applies: always

  - id: AUDIT-LOG
    type: compliance_trail
    from_sections:
      - rule_executions
      - decision_rationale
    to_sections:
      - audit_entries
      - compliance_reports
    influence: "Wykonanie reguł jest audytowane dla compliance"
    when:
      condition: rules.require_audit == true
      applies: conditionally
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: DECISION-TABLES
    relationship: rule_representation
    sections_mapping:
      - from: decision_matrix
        to: rule_conditions
    usage: "Tabele decyzyjne wizualizują logikę reguł"

  - id: BUSINESS-GLOSSARY
    relationship: terminology
    sections_mapping:
      - from: term_definitions
        to: rule_vocabulary
    usage: "Glosariusz definiuje terminy używane w regułach"
```

### Satellite Documents

```yaml
satellites:
  - name: RULE-REGISTRY
    purpose: "Rejestr wszystkich aktywnych reguł w systemie"
    trigger: continuous
    lifecycle: permanent
    retention: permanent

  - name: RULE-TEST-SUITE
    purpose: "Zestaw testów GIVEN-WHEN-THEN dla reguł"
    trigger: per_rule
    lifecycle: permanent
    retention: permanent

  - name: RULE-CONFLICT-ANALYSIS
    purpose: "Analiza potencjalnych konfliktów między regułami"
    trigger: before_deployment
    lifecycle: per_release
    retention: permanent
```

---
## 0. Metadane
- **Wersja**: `<vX.Y>`
- **Obszar/Domena**: `<np. billing, risk>`
- **Właściciel**: `<rola/osoba>`

## 1. Model danych i słownik
- **Encje**: `<User, Order, Payment, …>`
- **Atrybuty kluczowe**: `<...>`
- **Źródła danych**: `<stream/batch/API>`

## 2. Format reguły (YAML)
```yaml
rule:
  id: "<RULE-001>"
  name: "<Czytelna nazwa>"
  description: "<Cel reguły>"
  scope: "<gdzie obowiązuje>"
  trigger: "<zdarzenie/kwerenda/cykl>"
  condition: "<wyrażenie logiczne>"
  guard: "<warunek ochronny opcjonalny>"
  action:
    - type: "<akcja>"
      params: { key: value }
  priority: <0-100>        # większe = ważniejsze
  enabled: true
  cooldown: "<np. 5m>"     # zapobieganie pętli
  throttle: "<np. 100/min>"
  schedule: "<cron opcjonalny>"
  owner: "<rola>"
  audit:
    log: true
    pii_masking: "auto|on|off"
  metrics:
    - name: "<metric_name>"
      increment: 1
  conflicts:
    strategy: "first-win|priority|all"
  version: "<semver>"
  tags: ["<...>"]
```

## 3. Semantyka wyrażeń (EBNF – mini)
```
expr    := or_expr
or_expr := and_expr { "OR" and_expr }
and_expr:= not_expr { "AND" not_expr }
not_expr:= [ "NOT" ] atom
atom    := predicate | "(" expr ")"
predicate:= ident comparator value
comparator:= "==" | "!=" | ">" | ">=" | "<" | "<=" | "IN" | "MATCHES"
```
**Przykład warunku**: `user.country == "PL" AND order.value >= 500`

## 4. Rozwiązywanie konfliktów
- **Strategia**: `<first-win/priority/all>`
- **Deterministyczność**: `<zasady porządku>`

## 5. Testy reguł (GIVEN‑WHEN‑THEN)
- **GIVEN**: `<wejście>`
- **WHEN**: `<zdarzenie/warunek>`
- **THEN**: `<oczekiwane akcje/skutki>`

## 6. Ograniczenia i bezpieczeństwo
- **Idempotencja**: `<tak/nie + jak>`
- **Ochrona przed reentrancy**: `<cooldown/throttle>`
- **Dane wrażliwe**: `<maskowanie, minimalizacja>`

## 7. Monitorowanie i audyt
- **Log formatu audytu**: `<schemat>`
- **Metryki**: `<trygery/hity/błędy/opóźnienia>`

## 8. Wersjonowanie i lifecycle
- **Workflow**: `draft → review → approved → deployed → retired`
- **Migracje**: `<jak zmieniać bez przerw>`

## 9. Rejestr reguł (tabela)
| ID | Nazwa | Status | Priorytet | Właściciel | Ostatnia zmiana |
|---|---|---|---:|---|---|
| `<RULE-001>` | `<...>` | `approved` | `90` | `<...>` | `<YYYY-MM-DD>` |
