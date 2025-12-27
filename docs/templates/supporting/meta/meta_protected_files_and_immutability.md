# Pliki chronione (System-of-Record) + ochrona przed usunięciem

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Poniższe pliki są „punktami odniesienia” (system-of-record). Bez nich spójność projektu i walidacja przestają być wiarygodne.

## 1) Lista plików chronionych (PROTECTED_FILES)
**Rekomendacja:** trzymaj tę listę również jako `specs/protected_files.yaml`.

- `specs/doc_types.yaml`
- `specs/gates.yaml`
- `specs/error_codes.yaml`
- `docs/_meta/facts.yaml`
- `docs/_meta/waivers.yaml`
- `docs/_meta/glossary.md`

Opcjonalnie (gdy wdrażasz automatyzację):
- `specs/todo_generation_policy.yaml`
- `scripts/validate_docs.py`
- `scripts/build_reports.py`

---

## 2) Ochrona systemowa (Linux) — tylko „sudo” może odblokować

### Ustawienie flagi immutable (blokada edycji/usunięcia)
```bash
sudo chattr +i specs/doc_types.yaml specs/gates.yaml specs/error_codes.yaml \
  docs/_meta/facts.yaml docs/_meta/waivers.yaml docs/_meta/glossary.md
```

### Tymczasowe odblokowanie (na czas edycji)
```bash
sudo chattr -i specs/doc_types.yaml
# edycja...
sudo chattr +i specs/doc_types.yaml
```

### Sprawdzenie flag
```bash
lsattr specs/doc_types.yaml
```

---

## 3) Ochrona repo (zalecane) — polityka PR
Nawet jeśli pliki są immutable lokalnie, w repo warto dodać zasadę:
- zmiana plików chronionych wymaga PR + review,
- commit musi zawierać wpis w `CHANGELOG` (np. `docs/_meta/change_log.md`),
- w CI uruchamia się testy walidatora na fixtures.

---

## 4) Szkielety plików meta (do wklejenia)

### `docs/_meta/facts.yaml`
```yaml
version: 1
project_id: "CLIENT_X"
project_name: "Nazwa projektu"
currency: "EUR"

# Single Source of Truth (przykładowe fakty)
baseline_budget_eur: 0
baseline_timeline:
  target_release: "YYYY-MM-DD"
  target_go_no_go: "YYYY-MM-DD"

kpi_targets:
  kpi_1: ""
  kpi_2: ""

# Pola opcjonalne
compliance_profile: "base"   # base|healthcare|fintech|public|defense
stakeholders:
  sponsor: ""
  cfo: ""
  dpo: ""
  tech_lead: ""
```

### `docs/_meta/waivers.yaml`
```yaml
version: 1
waivers: []

# Przykład wpisu:
# - id: WAIVER-001
#   rule_id: RULE-PRD-FUNC-MIN10
#   reason: "Projekt MVP ma 6 user stories; zakres uzgodniony."
#   approved_by: "Product Owner"
#   approved_at: "YYYY-MM-DD"
#   expires_at: "YYYY-MM-DD"
#   scope: ["DOC-PRD-001"]
```

### `docs/_meta/glossary.md`
```markdown
---
id: "GLOSSARY-001"
owner: "Documentation Owner"
status: "live"
version: "0.1"
---

# Glossary

## Terminy
- **KPI** — ...
- **Gate** — ...
- **Evidence** — ...
- **DoR / DoD** — ...
```

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: DOC-TYPES-SPEC-*
    type: requires
    reason: "Protected files require specification of document types to protect"
    conditions:
      - when: "project.has_validation === true"
        applies: true
    sections:
      - from: "Doc Types Spec §1 Type definitions"
        to: "§1 Lista plików chronionych"
        influence: "Specification defines which files are system-of-record"

  - id: GATES-SPEC-*
    type: requires
    reason: "Protected files include gate specifications that control checkpoints"
    sections:
      - from: "Gates Spec §1 Gate definitions"
        to: "§1 Lista plików chronionych"
        influence: "Gate definitions are protected as critical project controls"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: VALIDATION-*
    type: blocks
    reason: "Validation scripts cannot run without protected specification files"
    conditions:
      - when: "project.has_automation === true"
        applies: true
    sections:
      - from: "§1 Lista plików chronionych"
        to: "Validation Script §1 Load specs"
        influence: "Protected specs define validation rules and behavior"

  - id: CI-PIPELINE-*
    type: blocks
    reason: "CI pipelines require protected files for consistent validation"
    sections:
      - from: "§1 Lista plików chronionych"
        to: "CI Pipeline §1 Validation step"
        influence: "Protected files ensure validation rules are immutable"

  - id: FACTS-*
    type: informs
    reason: "Facts file provides single source of truth for project data"
    sections:
      - from: "§4 facts.yaml"
        to: "All Documents §0 Meta"
        influence: "Facts provide baseline budget, timeline, KPIs for all docs"

  - id: WAIVERS-*
    type: informs
    reason: "Waivers file allows controlled exceptions to validation rules"
    sections:
      - from: "§4 waivers.yaml"
        to: "Validation Results §1 Exceptions"
        influence: "Waivers suppress specific rule violations with justification"
```

### Related Documents

```yaml
related:
  - id: ERROR-CODES-SPEC-*
    type: informs
    reason: "Error codes specification is also a protected file"

  - id: TODO-GENERATION-POLICY-*
    type: informs
    reason: "TODO generation policy may be protected when implemented"

  - id: GLOSSARY-*
    type: informs
    reason: "Glossary provides consistent terminology across project"
```

### Satellite Documents

```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-PROTECTED-*.md"
    required: false
    purpose: "Audit trail of changes to protected files"

  - type: TODO
    path: "satellites/todos/TODO-PROTECTED-*.md"
    required: false
    purpose: "Track updates to protected specifications"
```
