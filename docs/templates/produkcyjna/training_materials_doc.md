# 📄 Training Materials

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: USER-GUIDE-*
    type: requires
    reason: "User Guide provides foundational content for training materials"
    conditions:
      - when: "training.audience === 'end_users'"
        applies: true
    sections:
      - from: "User Guide §3 Step-by-Step Instructions"
        to: "§2 Tutorials"
        influence: "User guide instructions become training tutorials"
      - from: "User Guide §6 FAQ"
        to: "§4 Common Questions"
        influence: "FAQ becomes training reference material"

  - id: ADMINISTRATOR-GUIDE-*
    type: requires
    reason: "Admin Guide provides content for administrator training"
    conditions:
      - when: "training.audience === 'administrators'"
        applies: true
    sections:
      - from: "Administrator Guide §2 Configuration"
        to: "§3 Hands-on Exercises"
        influence: "Admin procedures become hands-on training exercises"

  - id: OPERATIONAL-MANUAL-*
    type: requires
    reason: "Operational Manual provides content for operations training"
    conditions:
      - when: "training.audience === 'operations_team'"
        applies: true
    sections:
      - from: "Operational Manual §3 Daily Operations"
        to: "§3 Operations Training"
        influence: "Operational procedures become training curriculum"

  - id: RUNBOOK-*
    type: influences
    reason: "Runbook procedures require operations training"
    conditions:
      - when: "training.includes_ops_procedures === true"
        applies: true
    sections:
      - from: "Runbook §2 System Start/Stop"
        to: "§3 Operations Training"
        influence: "Runbook procedures become operational training content"

  - id: SECURITY-PLAN-*
    type: influences
    reason: "Security policies require security awareness training"
    conditions:
      - when: "training.includes_security === true"
        applies: true
    sections:
      - from: "Security Plan §2 Security Policies"
        to: "§3 Security Training"
        influence: "Security policies define security awareness training content"

  - id: COMPLIANCE-REPORT-*
    type: influences
    reason: "Compliance requirements may mandate training"
    conditions:
      - when: "compliance.requires_training === true"
        applies: true
    sections:
      - from: "Compliance Report §1 Regulations"
        to: "§3 Compliance Training"
        influence: "Regulatory requirements define compliance training needs"

  - id: DATA-GOVERNANCE-POLICY-*
    type: influences
    reason: "Data governance policies require staff training"
    conditions:
      - when: "training.includes_data_governance === true"
        applies: true
    sections:
      - from: "Data Governance Policy §3 Roles"
        to: "§3 Data Governance Training"
        influence: "Data governance roles and policies define training curriculum"

  - id: KNOWLEDGE-TRANSFER-PLAN-*
    type: influences
    reason: "Knowledge transfer methods inform training delivery"
    conditions:
      - when: "project.has_knowledge_transfer === true"
        applies: true
    sections:
      - from: "Knowledge Transfer Plan §4 Transfer Methods"
        to: "§3 Training Delivery"
        influence: "Knowledge transfer methods become training approaches"
```

### Impacts
```yaml
impacts:
  - id: ONBOARDING-GUIDE-*
    type: influences
    reason: "Training materials are part of onboarding process"
    conditions:
      - when: "project.has_onboarding === true"
        applies: true
    sections:
      - from: "§2 Tutorials"
        to: "Onboarding Guide §4 Training Schedule"
        influence: "Training modules become onboarding curriculum"

  - id: UAT-PLAN-*
    type: informs
    reason: "UAT participants may need training before testing"
    conditions:
      - when: "uat.requires_participant_training === true"
        applies: true
    sections:
      - from: "§2 Tutorials"
        to: "UAT Plan §3 Participant Preparation"
        influence: "Training materials prepare UAT participants"
```

### Related
```yaml
related:
  - id: BCP-*
    type: informs
    reason: "BCP may require crisis response training"

  - id: DRP-*
    type: informs
    reason: "DRP procedures require disaster recovery training"

  - id: INCIDENT-REPORT-*
    type: informs
    reason: "Incident learnings may reveal training gaps"

  - id: ACCESSIBILITY-REPORT-*
    type: informs
    reason: "Accessibility training for assistive technology usage"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TRAINING-*.md"
    required: false
    purpose: "Track training material development and delivery schedule"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TRAINING-*.md"
    required: true
    purpose: "Store training recordings, participant feedback, completion certificates, assessment results"

  - type: DoD
    path: "satellites/dod/DOD-TRAINING-*.md"
    required: true
    purpose: "Define completion criteria: all materials created, delivery tested, participant feedback collected"
```

## Cel biznesowy / techniczny
Training Materials służą do edukacji użytkowników końcowych oraz zespołów operacyjnych. Mają na celu ułatwienie korzystania z systemu i zwiększenie adopcji produktu.

## Zawartość
- Instrukcje krok po kroku
- Tutoriale (tekstowe i graficzne)
- Zrzuty ekranu / wideo
- Najczęstsze problemy i rozwiązania
- Ćwiczenia praktyczne
- Dokumentacja dla administratorów

## Czego nie zawiera
- Szczegółowych kodów źródłowych
- Strategii marketingowych
- Analiz finansowych

## Objętość
- 5–15 stron
- 10–20 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Użytkownicy końcowi
- Administratorzy
- Zespół wsparcia technicznego
