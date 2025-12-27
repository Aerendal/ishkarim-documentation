# 📄 Training Plan (dla zespołu)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: ETHICS-AI-GUIDELINES-*
    type: requires
    reason: "Ethics & AI Guidelines definiują AI ethics training requirements"
    conditions:
      - when: "team.works_with_ai === true"
        applies: true
    sections:
      - from: "Ethics AI Guidelines §12 Zasady etycznego rozwoju i wdrożenia AI"
        to: "§11 Cele szkoleniowe"
        influence: "Ethical principles wymagają team education jako training objective"
      - from: "Ethics AI Guidelines §16 Odpowiedzialności zespołu"
        to: "§12 Zakres szkoleń"
        influence: "Team responsibilities definiują role-based training needs"

  - id: LEGAL-REGISTER-*
    type: influences
    reason: "Legal Register compliance requirements mogą wymagać compliance training"
    conditions:
      - when: "project.requires_compliance_training === true"
        applies: true
    sections:
      - from: "Legal Register §14 Odpowiedzialnesoby/zespoły"
        to: "§12 Zakres szkoleń"
        influence: "Compliance responsibilities determine training topics"

  - id: PROJECT-MGMT-PLAN-*
    type: influences
    reason: "Project Management Plan może identify skill gaps wymagające training"
    sections:
      - from: "Project Mgmt Plan §13 Budżet i alokacja zasobów"
        to: "§15 Budżet na szkolenia"
        influence: "Resource plan może allocate training budget"

  - id: COMMUNICATION-PLAN-*
    type: influences
    reason: "Communication Plan new tools mogą wymagać tool training"
    conditions:
      - when: "communication.requires_new_tools === true"
        applies: true
    sections:
      - from: "Communication Plan §13 Kanały komunikacji"
        to: "§12 Zakres szkoleń"
        influence: "New communication tools wymagają user training"

  - id: ROADMAP-*
    type: influences
    reason: "Innovation Roadmap new technologies mogą wymagać technical training"
    sections:
      - from: "Innovation Roadmap §12 Technologie do zbadania"
        to: "§12 Zakres szkoleń"
        influence: "New technologies on roadmap require team upskilling"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts: []
# Training Plan typically doesn't block other documents, it supports execution
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: RESEARCH-PLAN-*
    type: informs
    reason: "Research tools mogą wymagać specialized training"

  - id: DPIA-*
    type: informs
    reason: "DPIA może identify privacy training needs"

  - id: IMPACT-ASSESSMENT-*
    type: informs
    reason: "Impact mitigation może wymagać training"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TRAINING-*.md"
    required: false
    purpose: "Tracking training scheduling, attendance, certification completion"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TRAINING-*.md"
    required: false
    purpose: "Training materials, attendance records, certificates, evaluation results"

  - type: DoR
    path: "satellites/dor/DOR-TRAINING-*.md"
    required: true
    purpose: "Definition of Ready: team composition known, skill gaps identified, training objectives defined before Training Plan"

  - type: DoD
    path: "satellites/dod/DOD-TRAINING-*.md"
    required: true
    purpose: "Definition of Done: training delivered, team certified, effectiveness evaluated, knowledge transfer verified"
```

---

## Cel biznesowy / techniczny
Training Plan definiuje strategię podnoszenia kompetencji zespołu projektowego. Dokument wspiera rozwój umiejętności potrzebnych do skutecznej realizacji projektu.

## Zawartość
- Cele szkoleniowe
- Zakres szkoleń
- Metody nauki (warsztaty, e-learning, mentoring)
- Harmonogram szkoleń
- Budżet na szkolenia
- Kryteria oceny skuteczności szkoleń

## Czego nie zawiera
- Kodów źródłowych
- Planów sprintowych
- Strategii marketingowych

## Objętość
- 2–4 strony
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Project managerowie
- HR / dział szkoleń
- Członkowie zespołu
