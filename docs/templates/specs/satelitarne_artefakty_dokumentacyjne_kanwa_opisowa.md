# Satelitarne artefakty dokumentacyjne — kanwa opisowa

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Doc Types Spec]** `specs_doc_types.md`
  - Type: `informs`
  - Reason: Satellite types (TODO, DOR, DOD, etc.) must align with doc types
  - Sections used: satellites_required field in doc_types.yaml

- **[Gates Spec]** `specs_gates.md`
  - Type: `informs`
  - Reason: Satellites (Approval, Evidence) required for gate checkpoints

### Impacts (Downstream Documents)
- **ALL Templates** `../*.md` + `../examples/*.md`
  - Type: `informs`
  - Reason: Defines satellite document patterns used by all templates
  - Cascade: `false` (informative only)

### Related Documents
- **[Doc Types Spec]** `specs_doc_types.md` - Defines doctypes that require satellites
- **[Error Codes Spec]** `specs_error_codes.md` - Defines errors for missing satellites (E160)
- **[Gates Spec]** `specs_gates.md` - Defines gate requirements that trigger satellite creation

### Satellite Documents
- **[Changelog]** `satellites/CHANGELOG-SAT-SPEC-001.md` - Version history of this spec

### Conditional Cross-References
```yaml
# Universal spec - no domain conditions
# Applies to ALL document types across ALL domains
```

### Validation Rules
- [ ] All satellite kinds (TODO_SECTION, DOR, DOD, etc.) defined
- [ ] Each satellite kind has description and purpose
- [ ] Front-matter schema specified (YAML format)
- [ ] Storage convention documented (docs/project/satellites/)

---

Dokument podsumowuje koncepcję **satelitów dokumentu** — lekkich, atomowych artefaktów towarzyszących głównym dokumentom projektowym (PRD, TDD, Business Case, Feasibility itp.). Zawiera definicje, zasady użycia, rekomendowaną strukturę przechowywania oraz gotowe szablony front‑matter dla najczęściej stosowanych artefaktów.

---

## 1. Cel kanwy
- Ujednolicić sposób tworzenia i przechowywania artefaktów satelitarnych.  
- Zapewnić ślad audytowy i śledzenie zależności między dokumentami.  
- Umożliwić automatyczne generowanie issue/PR skeletonów na podstawie front‑matter.

---

## 2. Co to są „satelity dokumentu”?
Satelity to krótkie, jednozadaniowe lub kilkusekcyjne pliki o niskim koszcie utrzymania, które towarzyszą dużym dokumentom i umożliwiają:  
- rozbijanie pracy (TODO per sekcja),  
- formalizację wejścia (DoR) i wyjścia (DoD),  
- zachowanie dowodów (evidence items),  
- rejestr decyzji (ADR/Decision Log),  
- kontrolę zmian (Change Requests, Changelog),  
- formalne zatwierdzenia (Approval records).

---

## 3. Zestawy satelitów — zasada proporcjonalności
- **Minimalny (one‑pager):** TODO, Changelog, Approval.  
- **Standard (dokumenty średniej ważności — PRD, Business Case):** front‑matter dokumentu, TODO per sekcja, DoR (sekcja lub dokument), DoD (document‑level), Review checklist, Approval record, Evidence folder, ADR links, Changelog.  
- **Pełny (dokumenty krytyczne/regulatory/release):** wszystkie powyższe + DPIA fragments, QA test cases, runbook references, audit trail, monitoring plan, legal sign‑off.

---

## 4. Najważniejsze typy satelitów (lista szybkiego dostępu)
- TODO / Action Item  
- DoR (Definition of Ready)  
- DoD (Definition of Done)  
- ADR / Decision Record  
- RFC / Proposal  
- Change Request (CR)  
- Evidence Item (dowód/załącznik)  
- Approval / Sign‑off record  
- Review Checklist  
- RTM fragment (traceability)  
- Test Case / QA Script  
- Runbook entry / Deployment Playbook  
- Postmortem / Incident report  

---

## 5. Gdzie przechowywać (konwencja katalogów)
Rekomendowana struktura w repozytorium projektu:

```
docs/<project>/
  ├─ <document>.md                # główny dokument z front‑matter
  ├─ todos/                        # TODO per section (*.md)
  ├─ approvals/                    # approval records
  ├─ evidence/                     # załączniki (xlsx/pdf/csv)
  ├─ adr/                          # ADR entries
  ├─ qa/                           # test cases, scripts
  └─ changelog.md

templates/atomic/
  ├─ TODO_template.md
  ├─ DoR_template.md
  ├─ DoD_template.md
  └─ Approval_template.md
```

---

## 6. Uniwersalny front‑matter (zalecany dla wszystkich atomów)
Używaj YAML front‑matter, aby umożliwić automatyzację i parsowanie.

```yaml
---
id: "ATOM-<TYPE>-000"
type: "todo|adr|rfc|cr|decision|meeting|issue|spike|test|checklist|release|incident|risk|approval"
title: "Krótki tytuł"
owner: "Imię Nazwisko / Zespół"
status: "todo|in-progress|review|blocked|done|approved"
priority: "P0|P1|P2|P3"
created: "YYYY-MM-DD"
due: "YYYY-MM-DD"         # opcjonalne
related: []                 # lista powiązanych plików / id
approver: ""              # jeśli dotyczy
tags: []
---
```

---

## 7. Typowe szablony (skrót)
**TODO (per section)** — front‑matter + checklista kroków do zamknięcia.  
**DoR (Definition of Ready)** — lista kryteriów wejścia; weryfikacja przed startem (owner: PO).  
**DoD (Definition of Done)** — lista kryteriów wyjścia; musi być spełniona przed zamknięciem i przed release (owner: Team/QA).  
**Approval record** — krótki zapis: kto zatwierdził, data, notatka.

> W kanwie `templates/atomic/` znajdują się pełne wersje tych szablonów gotowe do kopiowania i wypełniania.

---

## 8. Zasady operacyjne / dobre praktyki
1. **Proporcjonalność**: rozbijaj artefakty tylko tam, gdzie wartość przewyższa koszt zarządzania.  
2. **1 problem = 1 atom**: każdy atom powinien rozwiązywać jedną sprawę/kwestię.  
3. **Powiązania**: każde satelitarne id powinno mieć `related` wskazujący dokument główny.  
4. **Automatyzacja**: generuj TODO → issue/PR skeletony automatycznie (skrypt/Jinja2).  
5. **Wersjonowanie i audit**: każda akceptacja (Approval) i decyzja (ADR) musi być commitowana z odwołaniem do PR.  
6. **Checkpoints**: łącz DoR i DoD z checkpointami (go/no‑go, requirements freeze, release readiness, ops handover, closure).

---

## 9. Workflow — przykład szybkiego cyklu dla PRD (praktycznie)
1. Utwórz `DOC-PRD-001.md` (front‑matter + outline).  
2. Wygeneruj `TODO` per sekcja w `docs/<project>/todos/`.  
3. Wypełnij sekcje → PO/AUTHORS uzupełniają treść.  
4. Tech Lead / QA sprawdzają DoR (sekcja/dokument).  
5. Gdy DoR OK → development / review → DoD checklist w PR.  
6. Po spełnieniu DoD → Approval record → publish + changelog update + archiwum evidence.

---

## 10. Automatyzacja (opcje do wdrożenia)
- Generator szablonów Jinja2 (`scripts/render_templates.py`).  
- Action: tworzenie Issue z front‑matter TODO (GitHub Action / CLI).  
- Linter front‑matter (CI check) — walidacja pól `id`, `type`, `owner`, `status`.  
- Raport traceability: CSV/JSON generowany z `related` powiązań.

---

## 11. Kolejne kroki (co mogę wygenerować teraz)
- pełny zestaw plików `templates/atomic/` (DoR, DoD, TODO, Approval, ADR, Spike, Evidence),  
- manifest CSV/JSON z metadanymi (id, nazwa, kategoria, effort_days),  
- przykładowe wypełnienia (demo) dla 3 dokumentów: Executive Summary, PRD, TDD,  
- skrypt Jinja2 do renderowania i GitHub Action do tworzenia issue skeleton.

---

> Jeśli potwierdzisz, wygeneruję wskazane pliki w `templates/` i manifest — lub od razu zainicjuję Issue skeletony w Twoim systemie (jeśli chcesz).

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Doc Types Spec]** `specs_doc_types.md`
  - Type: `informs`
  - Reason: Satellite types (TODO, DOR, DOD, etc.) must align with doc types
  - Sections used: satellites_required field in doc_types.yaml

- **[Gates Spec]** `specs_gates.md`
  - Type: `informs`
  - Reason: Satellites (Approval, Evidence) required for gate checkpoints

### Impacts (Downstream Documents)
- **ALL Templates** `../*.md` + `../examples/*.md`
  - Type: `informs`
  - Reason: Defines satellite document patterns used by all templates
  - Cascade: `false` (informative only)

### Related Documents
- **[Doc Types Spec]** `specs_doc_types.md` - Defines doctypes that require satellites
- **[Error Codes Spec]** `specs_error_codes.md` - Defines errors for missing satellites (E160)
- **[Gates Spec]** `specs_gates.md` - Defines gate requirements that trigger satellite creation

### Satellite Documents
- **[Changelog]** `satellites/CHANGELOG-SAT-SPEC-001.md` - Version history of this spec

### Conditional Cross-References
```yaml
# Universal spec - no domain conditions
# Applies to ALL document types across ALL domains
```

### Validation Rules
- [ ] All satellite kinds (TODO_SECTION, DOR, DOD, etc.) defined
- [ ] Each satellite kind has description and purpose
- [ ] Front-matter schema specified (YAML format)
- [ ] Storage convention documented (docs/project/satellites/)
