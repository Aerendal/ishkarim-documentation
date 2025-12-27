# 📄 Risk Overview (Inwestycyjny)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: BIZ-CASE-*
    type: influences
    reason: "Business Case business assumptions mogą reveal business risks"
    conditions:
      - when: "project.has_business_model === true"
        applies: true
    sections:
      - from: "Business Case §16 Prognozy finansowe"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Financial projections assumptions are assessed jako financial risks"

  - id: MARKET-ANALYSIS-*
    type: influences
    reason: "Market Analysis competitive landscape reveals market risks"
    sections:
      - from: "Market Analysis §13 Kluczowi gracze i analiza konkurencji"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Competitive threats są identified jako market risks"
      - from: "Market Analysis §16 Potencjalne bariery wejścia"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Market entry barriers są assessed jako strategic risks"

  - id: DPIA-*
    type: influences
    reason: "DPIA privacy risks są escalated do Risk Overview"
    conditions:
      - when: "dpia.identifies_high_risks === true"
        applies: true
    sections:
      - from: "DPIA §14 Identyfikacja ryzyk dla prywatności"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Privacy risks są included jako compliance/reputational risks"

  - id: IMPACT-ASSESSMENT-*
    type: influences
    reason: "Impact Assessment ethical/environmental risks informują Risk Overview"
    sections:
      - from: "Impact Assessment §14 Ryzyka etyczne"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Ethical risks są escalated jako reputational risks"

  - id: LEGAL-REGISTER-*
    type: influences
    reason: "Legal Register compliance gaps reveal legal risks"
    conditions:
      - when: "legal.has_compliance_gaps === true"
        applies: true
    sections:
      - from: "Legal Register §15 Status zgodności"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Non-compliance issues są assessed jako legal/financial risks"

  - id: CBA-*
    type: influences
    reason: "CBA pessimistic scenarios reveal financial risks"
    sections:
      - from: "CBA §14 Analiza scenariuszowa"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Pessimistic scenarios identify downside financial risks"

  - id: PROCUREMENT-PLAN-*
    type: influences
    reason: "Procurement Plan vendor dependencies reveal supply chain risks"
    conditions:
      - when: "procurement.has_critical_vendors === true"
        applies: true
    sections:
      - from: "Procurement Plan §14 Kryteria wyboru dostawców"
        to: "§11 Lista kluczowych ryzyk biznesowych"
        influence: "Vendor dependencies są assessed jako supply chain risks"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROJECT-MGMT-PLAN-*
    type: blocks
    reason: "Project Management Plan requires Risk Overview dla risk management planning"
    sections:
      - from: "§11 Lista kluczowych ryzyk biznesowych"
        to: "Project Mgmt Plan §15 Plan ryzyka"
        influence: "Identified risks definiują risk management strategies"
      - from: "§14 Strategia mitigacji (plan awaryjny)"
        to: "Project Mgmt Plan §15 Plan ryzyka"
        influence: "Mitigation strategies są incorporated w project risk plan"

  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary musi communicate key risks do decision makers"
    sections:
      - from: "§11 Lista kluczowych ryzyk biznesowych"
        to: "Executive Summary §17 Ryzyka"
        influence: "Top risks są highlighted dla executive awareness"

  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck may address key risks dla investor transparency"
    conditions:
      - when: "pitch.includes_risks === true"
        applies: true
    sections:
      - from: "§14 Strategia mitigacji (plan awaryjny)"
        to: "Pitch Deck §19 Risk Mitigation"
        influence: "Risk mitigation demonstrates risk management capability"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: COMMUNICATION-PLAN-*
    type: informs
    reason: "Risk communication może be part of Communication Plan"

  - id: STAKEHOLDER-MAP-*
    type: informs
    reason: "Risk assessment może identify stakeholder concerns"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RISK-*.md"
    required: false
    purpose: "Tracking risk monitoring tasks, mitigation action items"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RISK-*.md"
    required: true
    purpose: "Risk assessments, mitigation plans, risk monitoring reports"

  - type: DoR
    path: "satellites/dor/DOR-RISK-*.md"
    required: true
    purpose: "Definition of Ready: project scope defined, key dependencies identified, business case analyzed before Risk Overview"

  - type: DoD
    path: "satellites/dod/DOD-RISK-*.md"
    required: true
    purpose: "Definition of Done: all major risks identified, impact/probability assessed, mitigation strategies defined, monitoring plan established"
```

---

## Cel biznesowy / techniczny
Risk Overview (inwestycyjny) przedstawia główne zagrożenia związane z realizacją projektu z perspektywy inwestora. Pomaga ocenić ryzyko i zaplanować sposoby jego minimalizacji.

## Zawartość
- Lista kluczowych ryzyk biznesowych
- Potencjalny wpływ na projekt
- Prawdopodobieństwo wystąpienia
- Strategia mitigacji (plan awaryjny)
- Wskaźniki wczesnego ostrzegania

## Czego nie zawiera
- Niskopoziomowych błędów implementacyjnych
- Kodów źródłowych
- Szczegółowych analiz technicznych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy
- Zarząd
- Komitety ryzyka
