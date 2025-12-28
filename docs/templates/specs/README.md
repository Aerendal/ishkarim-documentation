# Specs — Specyfikacje Systemu Dokumentacji

## 📋 Przeznaczenie

Folder zawiera **specyfikacje systemu dokumentacji Ishkarim** — meta-dokumenty definiujące jak działa cały system szablonów, jakie są typy dokumentów, kody błędów, gates i satelity.

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Definiowania typów dokumentów** (doc types - wymagane sekcje, satelity)
- **Walidacji dokumentów** (error codes - co może pójść nie tak)
- **Kontroli jakości** (gates - checkpoints go/no-go)
- **Zarządzania satelitami** (satellite artifacts - TODO, DoR, DoD, etc.)

## 👥 Kto używa?

- **System Architects** — projektują i utrzymują system dokumentacji
- **Validators** — walidują dokumenty według specs
- **Tool Developers** — budują narzędzia oparte na specs (parsery, linters)
- **Contributors** — dodają nowe typy dokumentów według specs
- **Automation Engineers** — implementują automated checks

## ⏱️ Kiedy używać?

**Timing:**
- **System design:** Gdy projektujesz system dokumentacji
- **Extension:** Gdy dodajesz nowy typ dokumentu
- **Validation:** Gdy walidуjesz dokument
- **Automation:** Gdy budujesz tooling (linters, validators)

## 📂 Specyfikacje (4 pliki)

### specs_doc_types.md
**Rejestr typów dokumentów**

Definiuje wszystkie typy dokumentów w systemie:
- `EXEC_SUMMARY`, `BUSINESS_CASE`, `PRD`, `HLA`, `TDD`, etc.
- Dla każdego typu:
  - `required_meta` — wymagane pola front-matter
  - `required_sections` — wymagane sekcje H2
  - `satellites_required` — wymagane satelity (TODO, DoR, DoD, etc.)
  - `dependencies` — wymagane dokumenty (np. PRD requires BUSINESS_CASE)
  - `outputs` — jakie gates odblokowuje
  - `sufficiency_rules` — reguły wystarczalności (min items, etc.)

**Przykład:**
```yaml
PRD:
  required_meta: [id, doctype, status, version, owner]
  required_sections:
    - {id: SEC-PRD-GOAL, title: "Cel produktu"}
    - {id: SEC-PRD-FUNC, title: "Wymagania funkcjonalne"}
  satellites_required: [TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL]
  dependencies:
    - {doctype: BUSINESS_CASE, min_status: approved}
  outputs:
    unlock_gates: [GATE-REQ_FREEZE]
```

### specs_error_codes.md
**Kody błędów i walidacja**

Definiuje wszystkie error codes dla walidacji dokumentów:
- `E100` — Missing file
- `E110` — Missing required section
- `E120` — Placeholder present
- `E130` — Missing evidence
- `E140` — Missing dependency link
- `E150` — Gate blocked (aggregate)
- `E160` — Missing approval
- `E200` — Contradiction / conflicting facts
- `E210` — ID collision
- `W310` — Recommended section missing
- `S900` — Secret/PII detected

Dla każdego kodu:
- `severity_default` — BLOCKER / ERROR / WARN
- `todo_action` — TODO / BATCH_TODO / RFC / NONE / SECURITY_INCIDENT
- `message_template` — Template wiadomości błędu
- `remediation_template` — Jak naprawić

### specs_gates.md
**Gates i checkpoints**

Definiuje gates (go/no-go decision points):
- `GATE-GO_NO_GO` — Initial project approval
- `GATE-REQ_FREEZE` — Requirements freeze
- `GATE-RELEASE_READY` — Release readiness
- `GATE-OPS_HANDOVER` — Operations handover
- `GATE-CLOSURE` — Project closure

Dla każdego gate:
- `required_documents` — dokumenty wymagane do odblokowania
- `required_approvals` — kto musi zatwierdzić
- `validation_rules` — jakie error codes muszą być rozwiązane

### satelitarne_artefakty_dokumentacyjne_kanwa_opisowa.md
**Satellite artifacts framework**

Definiuje system satelitów (lightweight artifacts):
- `TODO_SECTION` — TODO per sekcja dokumentu
- `DOR_DOC` — Definition of Ready dla dokumentu
- `DOD_DOC` — Definition of Done dla dokumentu
- `APPROVAL` — Approval / sign-off record
- `EVIDENCE` — Evidence items + evidence-index
- `CHANGELOG` — Historia zmian dokumentu
- `CR` — Change Request
- `ADR` — Architecture Decision Record

Dla każdego satelity:
- `description` — co to jest
- `purpose` — do czego służy
- `front_matter_schema` — YAML schema
- `storage_convention` — gdzie przechowywać

## 🔗 Powiązania

**Dependencies:**
- (brak — specs są foundation, nie zależą od innych docs)

**Impacts:**
- ➡️ **ALL Templates** → wszystkie szablony comply ze specs
- ➡️ **Validators** → validation tools używają specs
- ➡️ **Automation** → automated workflows bazują na specs
- ➡️ **Extensions** → nowe typy dokumentów muszą follow specs

## 📊 Statystyki

- **Liczba specs:** 4 core specifications
- **Pokrycie:** 100% systemu (wszystkie docs muszą comply)
- **Doc types defined:** ~25 typów dokumentów
- **Error codes defined:** 11 kodów (E100-S900)
- **Gates defined:** 5 checkpoints
- **Satellites defined:** 8 typów satelitów

## 🚀 Quick Start

**Scenario 1: Chcesz dodać nowy typ dokumentu**
1. Czytaj: `specs_doc_types.md` (zrozum strukturę doctype)
2. Definiuj: Nowy doctype w YAML (required_sections, satellites, etc.)
3. Testuj: Stwórz przykład i zwaliduj

**Scenario 2: Budujesz validator**
1. Parse: `specs_doc_types.md` → lista wymagań per doctype
2. Parse: `specs_error_codes.md` → lista error codes
3. Implementuj: Walidację według specs
4. Raportuj: Błędy w formacie error codes

**Scenario 3: Rozumiesz system**
1. Start: `satelitarne_artefakty_*.md` (koncepcja satelitów)
2. Potem: `specs_doc_types.md` (typy dokumentów)
3. Następnie: `specs_error_codes.md` (walidacja)
4. Na koniec: `specs_gates.md` (checkpoints)

## ⚠️ Uwagi

- **Foundation layer:** Specs są podstawą całego systemu — zmiany tu = impact wszędzie
- **YAML format:** Wszystkie specs używają YAML dla machine-readability
- **Versioning:** Specs mają `version: 1` — breaking changes = version bump
- **Backward compatibility:** Zmiany muszą być backward compatible lub z migration plan

## 🛠️ Tooling oparty na specs

**Obecnie możliwe:**
- ✅ Document validators (check required sections)
- ✅ Gate enforcers (block if deps not met)
- ✅ Satellite generators (auto-create TODO when doc created)
- ✅ Error reporters (format validation errors)

**Przyszłość (z propozycji):**
- 🔮 Auto-propagation (update deps when doc changes)
- 🔮 Living documentation engine (track freshness)
- 🔮 AI-assisted filling (suggest content based on specs)

## 📖 Zobacz też

- [../supporting/](../supporting/) — Meta-documentation, overviews
- [../examples/](../examples/) — Przykłady wypełnionych szablonów
- [../../dependency_graph.md](../../dependency_graph.md) — Graf zależności
- [../../proposals/](../../proposals/) — Propozycje ulepszeń systemu

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Specs (System Specifications / Foundation Layer)
**Rola:** Definiuje całą mechanikę systemu dokumentacji Ishkarim
