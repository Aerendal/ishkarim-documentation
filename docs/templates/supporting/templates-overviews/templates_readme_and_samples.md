# 📂 Szablony dokumentów — README (Markdown)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Preferujesz format **Markdown (.md)** — zgoda. Przygotuję pełen pakiet szablonów w prostym, edytowalnym formacie Markdown z blokiem YAML (front-matter) na początku każdego pliku. Poniżej znajdziesz:

1. Zasugerowaną **strukturę katalogów** dla szablonów.
2. Standardowy **front-matter (YAML)** dla każdego dokumentu.
3. Dwa **przykładowe szablony** w Markdown: *Executive Summary* i *PRD* — możesz je skopiować bezpośrednio do plików `templates/...`.
4. Krótkie **instrukcje** jak używać szablonów i propozycję prostego skryptu do generowania dokumentów.

---

## 1. Proponowana struktura katalogów

```
templates/
  przedprodukcyjne/
    Executive_Summary.md
    Business_Case.md
    Pitch_Deck.md
    Feasibility_Study.md
    Financial_Plan.md
    ...
  produkcyjne/
    PRD.md
    BRD.md
    TDD.md
    Test_Plan.md
    Runbook.md
    ...
  branżowe/
    medycyna/
      HIPAA_Compliance_Report.md
      Clinical_Trial_Documentation.md
    fintech/
      PCI_DSS_Compliance_Report.md
      SOX_Compliance_Report.md
    administracja/
      GDPR_Compliance_Report.md
    obronnosc/
      Security_Clearance.md
  docs/
    README.md   # (ten plik)
    schema.json
  scripts/
    render_template.py
  examples/
    example_startup/
    example_medical/
```

---

## 2. Standardowy front-matter (YAML)

Wszędzie stosujemy prosty blok YAML na początku pliku — ułatwia to automatyzację i walidację.

```yaml
---
title: "{{ title | default('Tytuł dokumentu') }}"
project: "{{ project | default('NAZWA_PROJEKTU') }}"
client: "{{ client | default('NAZWA_KLIENTA') }}"
author: "{{ author | default('Imię Nazwisko') }}"
reviewers: []
version: "0.1.0"
status: "draft"   # draft | review | approved
date_created: "YYYY-MM-DD"
last_modified: "YYYY-MM-DD"
tags: []
related_docs: []
compliance: []  # np. ["RODO","HIPAA","PCI-DSS"]
---
```

**Uwagi:** pola front-matter można dostosować (dorzucę JSON Schema jeśli chcesz walidację w CI).

---

## 3. Przykładowe szablony (.md)

Skopiuj poniższe pliki do katalogu `templates/przedprodukcyjne/` i `templates/produkcyjne/`.

### `templates/przedprodukcyjne/Executive_Summary.md`

```markdown
---
title: "Executive Summary"
project: "NAZWA_PROJEKTU"
client: ""
author: ""
reviewers: []
version: "0.1.0"
status: "draft"
date_created: "YYYY-MM-DD"
tags: ["executive","pitch"]
related_docs: []
compliance: []
---

# Executive Summary

## 1. Cel projektu (1-2 zdania)
> Szybkie streszczenie, dlaczego projekt jest ważny.

## 2. Problem / Opportunity
- Krótkie stwierdzenie problemu lub szansy rynkowej.

## 3. Rozwiązanie i unikalna wartość
- Co proponujemy, dlaczego to działa, przewaga konkurencyjna.

## 4. Rynek i model biznesowy
- Wielkość rynku, segmenty, model przychodów (krótkie liczby).

## 5. Harmonogram i milestones (wysokopoziomowo)
- Milestone 1 — data
- Milestone 2 — data

## 6. Zespół
- Kluczowe role i krótkie bio.

## 7. Co oczekujemy (wezwanie do działania)
- Wysokość finansowania / typ wsparcia / decyzja.

---
*Suggested length: 1–2 pages.*
```

### `templates/produkcyjne/PRD.md`

```markdown
---
title: "Product Requirements Document"
project: "NAZWA_PROJEKTU"
client: ""
author: "Product Owner"
reviewers: []
version: "0.1.0"
status: "draft"
date_created: "YYYY-MM-DD"
tags: ["prd","requirements"]
related_docs: []
compliance: []
---

# Product Requirements Document (PRD)

## 0. Meta
- **Project:** NAZWA_PROJEKTU
- **Author:** Product Owner
- **Version:** 0.1.0
- **Status:** draft

## 1. Cel produktu
*Opis celu biznesowego i problemu, który rozwiązujemy.*

## 2. Zakres (In scope / Out of scope)
- **In scope:**
  - ...
- **Out of scope:**
  - ...

## 3. Personas / Użytkownicy
- Persona A — krótki opis
- Persona B — krótki opis

## 4. Wymagania funkcjonalne (User Stories)
1. **ID:** PRD-F-001
   **As a** [rola] **I want** [co] **so that** [korzyść]
   **Acceptance criteria:**
   - AC1
   - AC2

2. PRD-F-002 ...

## 5. Wymagania niefunkcjonalne
- Wydajność: ...
- Dostępność: ...
- Bezpieczeństwo: ...

## 6. Integracje / zależności
- API X — sposób integracji
- System Y — zależność

## 7. Kryteria akceptacji
- Lista warunków do spełnienia aby uznać rozwój za zakończony.

## 8. Harmonogram (wysokopoziomowo)
- Milestone 1 — data
- Milestone 2 — data

## 9. Ryzyka i mitigacje
- Ryzyko A — plan mitigacji

## 10. Powiązane dokumenty
- link do TDD, Test Plan, RTM

---
*Suggested length: 8–15 pages depending on scope.*
```

---

## 4. Krótkie instrukcje użycia i prosty skrypt (opcjonalnie)

### Ręcznie

1. Skopiuj potrzebne pliki `.md` do `templates/<faza>/`.
2. Utwórz plik `data/<client>/meta.yaml` z wypełnionym front-matter (możesz użyć tego samego YAML).
3. Skopiuj `templates/...` -> `docs/<client>/` i wypełnij treść.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: TEMPLATE-SPEC-*
    type: requires
    reason: "Template README requires template specifications and structure definitions"
    conditions:
      - when: "project.has_templates === true"
        applies: true
    sections:
      - from: "Template Specification §1 Front-matter schema"
        to: "§2 Standardowy front-matter"
        influence: "Specification defines YAML structure for all templates"
      - from: "Template Specification §2 Directory structure"
        to: "§1 Proponowana struktura katalogów"
        influence: "Specification guides template organization"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: EXEC-SUMMARY-*
    type: informs
    reason: "README provides template guidance for creating Executive Summary"
    conditions:
      - when: "document.type === 'przedprodukcyjne'"
        applies: true
    sections:
      - from: "§3 Przykładowe szablony"
        to: "Executive Summary §All"
        influence: "Template example guides document creation"

  - id: PRD-*
    type: informs
    reason: "README provides template guidance for creating PRD"
    conditions:
      - when: "document.type === 'produkcyjne'"
        applies: true
    sections:
      - from: "§3 Przykładowe szablony"
        to: "PRD §All"
        influence: "Template example guides PRD structure"

  - id: ALL-DOC-*
    type: informs
    reason: "README informs all documentation creation via templates"
    sections:
      - from: "§2 Standardowy front-matter"
        to: "All Documents §0 Meta"
        influence: "Front-matter standard applies to all documents"
```

### Related Documents

```yaml
related:
  - id: RENDER-SCRIPT-*
    type: informs
    reason: "Optional rendering scripts automate template instantiation"

  - id: SCHEMA-JSON-*
    type: informs
    reason: "JSON Schema validates template front-matter structure"

  - id: EXAMPLES-*
    type: informs
    reason: "Example projects demonstrate template usage"
```

### Satellite Documents

```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TEMPLATES-*.md"
    required: false
    purpose: "Track template creation and maintenance tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TEMPLATES-*.md"
    required: false
    purpose: "Example filled templates from real projects"
```

###
