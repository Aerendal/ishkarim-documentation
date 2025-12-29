---
id: PRD-001-V2
title: "Product Requirements Document - System Zarządzania Dokumentacją (Proof System)"
type: prd
domain: requirements
status: req-freeze
created: 2025-12-26
updated: 2025-12-26
owner: "Zespół Produktowy"
phase: requirements
priority: critical
requirements_frozen_date: 2025-12-26
frozen_by: ["Product Owner", "Tech Lead"]

gate_history:
  - gate: REQ-FREEZE
    date: 2025-12-26
    conditions_met:
      all_FR_complete: true
      all_NFR_complete: true
      stakeholder_approval: true
      no_critical_placeholders: true

# Bramki wejścia (co wpływa na ten dokument)
dependencies:
  - id: "EXEC-SUM-001"
    title: "Podsumowanie Wykonawcze"
    type: requires
    status_constraint: [approved]
    reason: "Wyrównanie strategiczne - system musi spełniać cele strategiczne"
    evidence: []

  - id: "BIZ-CASE-001-V2"
    title: "Uzasadnienie Biznesowe V2"
    type: requires
    status_constraint: [approved]
    reason: "Uzasadnienie biznesowe - wymagania muszą dawać ROI"
    evidence: []

  - id: "VISION-001-V2"
    title: "Dokument Wizji - Proof System V2"
    type: informs
    status_constraint: [approved]
    reason: "Kierunek długoterminowy - wymagania wyrównane z wizją 12-24m"
    evidence: []

  - id: "CONCEPTS-001-V2"
    title: "System Koncepcji - Proof System"
    type: requires
    status_constraint: [completed]
    reason: "Conceptual foundation - wszystkie FR mapują do 18 koncepcji"
    evidence: []

# Bramki wyjścia (na co ten dokument wpływa)
impacts:
  - id: "TDD-001-V2"
    title: "Technical Design Document - System Zarządzania Dokumentacją (Proof System)"
    type: blocks
    until: "PRD-001-V2.status == req-freeze"
    reason: "Nie możemy projektować architektury bez zamrożonych wymagań"
    cascade: true

  - id: "TEST-PLAN-001"
    title: "Plan Testów"
    type: blocks
    until: "PRD-001-V2.status == req-freeze"
    reason: "Plan testów wymaga stabilnych AC i NFR"
    cascade: true

  - id: "RTM-001"
    title: "Macierz Identyfikowalności Wymagań"
    type: informs
    until: "PRD-001-V2.status == draft"
    reason: "RTM inicjalizowane z FR/NFR, aktualizowane przy zmianach"
    cascade: true

# Bramki wewnętrzne (między sekcjami tego dokumentu)
internal_gates:
  - source: "Wymagania Funkcjonalne"
    impacts: ["Wymagania Niefunkcjonalne", "Architektura", "Strategia Testowania"]
    reason: "FR determinują NFR (np. FR-009 graf → NFR-002 wydajność grafu)"

  - source: "Wymagania Niefunkcjonalne"
    impacts: ["Stos Technologiczny", "Szacunki Kosztów", "Plan Implementacji"]
    reason: "NFR wpływają na wybór technologii i harmonogram"

  - source: "Persony Użytkowników"
    impacts: ["User Stories", "Wymagania Funkcjonalne", "Wymagania UI/UX"]
    reason: "Persony determinują historie i AC"

# Context snapshot (T₀ - stan w momencie decyzji)
context_snapshot:
  budget: "TBD (w BIZ-CASE-001-V2)"
  team_size: 2
  team_skills: ["Python", "TypeScript", "NetworkX", "PySide6", "Markdown"]
  timeline: "MVP by 2025-Q2, V1.0 by 2025-Q3"
  constraints:
    - "Standalone Python app (nie Obsidian plugin extension)"
    - "Local-first (pliki .md, nie cloud)"
    - "Cross-platform (Linux, macOS, Windows)"
    - "Proof system compatible (bramki, evidence, storytelling)"
    - "NetworkX dla graph analysis"
    - "SQLite dla persistence"

# Evidence trail
evidence_ids:
  - "E-001"  # User research - 80% devs prefer markdown over proprietary
  - "E-002"  # Benchmark - markdown parsing < 50ms/doc
  - "E-003"  # Survey - gap detection #1 pain point in documentation
  - "E-004"  # Analysis - broken dependencies cost 15% dev time
  - "E-005"  # Prototype - NetworkX handles 10k nodes < 2s

# Alternatives considered (dlaczego te wymagania, nie inne)
alternatives:
  - id: "OPTION-A"
    title: "Obsidian Plugin (TypeScript extension)"
    status: rejected
    reason: "Locked do Obsidian ecosystem, brak standalone flexibility"
    evidence: ["E-006"]

  - id: "OPTION-B"
    title: "Web App (React + Backend API)"
    status: rejected
    reason: "Cloud dependency, latency w large repos, data privacy concerns"
    evidence: ["E-007"]

  - id: "OPTION-C"
    title: "Standalone Python App (PySide6 GUI)"
    status: selected
    reason: "Local-first, cross-platform, mature ecosystem (NetworkX, Pydantic)"
    evidence: ["E-005", "E-008"]

  - id: "OPTION-D"
    title: "CLI-only (no GUI)"
    status: rejected
    reason: "Graph visualization critical - user research: 90% prefer GUI"
    evidence: ["E-009"]

# Satellites (auto-generated lub manual)
satellites:
  - "TODO-PRD-001-V2"
  - "DOR-PRD-001-V2"
  - "DOD-PRD-001-V2"
  - "RTM-001"
  - "IMPL-LOG-PRD-001-V2"

# Changelog (obowiązkowy)
changelog:
  - version: "2.0"
    date: "2025-12-26"
    author: "Zespół Produktowy"
    changes: "Migracja V1 → V2: dodano bramki, storytelling, evidence notes, decision graph"
    reason: "Adopcja proof system approach z CONCEPTS-001-V2"
    approved_by: "N/A (draft)"
    evidence: ["CONCEPTS-001-MIGRATION-GUIDE"]

  - version: "1.0"
    date: "2025-12-24"
    author: "Zespół Produktowy"
    changes: "Initial version (deprecated)"
    reason: "Traditional documentation approach"
---

# PRD-001-V2: System Zarządzania Dokumentacją (Proof System)

← [Poprzednia: CONCEPTS-001-V2](./koncepcje-v2.md) | [Satellite: TODO →](../satellites/todos/TODO-PRD-001-V2.md)

---

## Spis Treści

### 1. Przegląd Dokumentu (Linie 150-230)
- 1.1 Cel i Zakres
- 1.2 Grupa Docelowa
- 1.3 Historia Wymagań
- 1.4 Dokumenty Powiązane

### 2. Przegląd Systemu (Linie 231-340)
- 2.1 Deklaracja Wizji
- 2.2 Kluczowe Możliwości
- 2.3 Propozycja Wartości
- 2.4 Metryki Sukcesu

### 3. Persony & Use Cases (Linie 341-480)
- 3.1 Persony Główne (4 persony)
- 3.2 Scenariusze Use Case

### 4. Wymagania Funkcjonalne (Linie 481-1450)
- 4.1 Parser (FR-001 do FR-004)
- 4.2 Validator (FR-005 do FR-008)
- 4.3 Graph Builder (FR-009 do FR-013)
- 4.4 Gap Detection (FR-014 do FR-020, FR-100, FR-091, FR-093, FR-111)
- 4.5 Gate Management (FR-081 do FR-085)
- 4.6 Storytelling Engine (FR-092 do FR-099)
- 4.7 Evidence Management (FR-101 do FR-106)
- 4.8 Implementation Log (FR-112 do FR-114)
- 4.9 GUI (FR-021 do FR-025)
- 4.10 Storage (FR-026 do FR-028)

### 5. Wymagania Niefunkcjonalne (Linie 1451-1650)
- 5.1 Wydajność (NFR-001 do NFR-003)
- 5.2 Niezawodność (NFR-004 do NFR-005)
- 5.3 Skalowalność (NFR-006 do NFR-007)
- 5.4 Użyteczność (NFR-008 do NFR-009)
- 5.5 Utrzymywalność (NFR-010 do NFR-011)

### 6. User Stories (Linie 1651-1850)
- 6.1 Developer Stories (US-001 do US-003)
- 6.2 Product Manager Stories (US-004 do US-006)
- 6.3 QA Stories (US-007 do US-008)
- 6.4 Writer Stories (US-009 do US-010)

### 7. Quality Gates & AC (Linie 1851-2000)
- 7.1 REQ-FREEZE Gate
- 7.2 DoR/DoD Definitions
- 7.3 Acceptance Criteria Matrix

### 8. Constraints & Dependencies (Linie 2001-2150)
- 8.1 Stos Technologiczny
- 8.2 Ograniczenia Systemowe
- 8.3 Punkty Integracji

### 9. Mapowanie Koncepcje → FR (Linie 2151-2300)

### 10. Re-evaluation Triggers (Linie 2301-2400)

### 11. Appendices (Linie 2401-2500)

---

## 1. Przegląd Dokumentu

### 1.1 Cel i Zakres

**Cel**: Ten dokument definiuje **kompletne wymagania funkcjonalne i niefunkcjonalne** dla Systemu Zarządzania Dokumentacją w podejściu **proof system** z pełną audytowalnością.

**Zakres**:
- ✅ **IN SCOPE**:
  - 95 wymagań funkcjonalnych (FR-001 do FR-114+)
  - 15 wymagań niefunkcjonalnych (NFR-001 do NFR-015)
  - 10 user stories (US-001 do US-010)
  - Pełne mapowanie do 18 koncepcji z CONCEPTS-001-V2
  - Evidence notes per requirement
  - Decision context dla major features

- ❌ **OUT OF SCOPE**:
  - Szczegóły implementacji (to jest w TDD-001-V2)
  - Architektura komponentów (to jest w TDD-001-V2)
  - Test cases (to jest w TEST-PLAN-001)
  - Deployment procedures (to jest w DEPLOY-001)

### 1.2 Grupa Docelowa

Ten dokument jest dla:
- **Product Owners** - zatwierdzają wymagania biznesowe
- **Zespołu Inżynieryjnego** - implementują FR/NFR
- **QA Engineers** - piszą testy z AC
- **Technical Writers** - tworzą dokumentację użytkownika
- **Stakeholders** - rozumieją co system robi (i dlaczego)

### 1.3 Historia Wymagań: Dlaczego Proof System?

**Punkt startowy (T₀: 2025-12-20)**: Mieliśmy działający prototyp Obsidian plugin (TypeScript) z podstawową funkcjonalnością gap detection. Obserwowaliśmy 3 główne problemy:

**Problem 1 - Brak Auditability** [E-003]:
> 15% czasu developerów szło na debugging "dlaczego ta decyzja została podjęta". Dokumenty były edytowane in-place bez historii decyzji.

Rozważaliśmy rozwiązania:
- **Opcja A**: Git history - ODRZUCONA (techniczny log, nie semantyczny)
- **Opcja B**: Comment threads (GitHub-style) - ODRZUCONA (rozproszone, trudne do track)
- **Opcja C**: Graf decyzyjny + evidence notes - ✓ WYBRANA

**Problem 2 - Broken Dependencies Cascade** [E-004]:
> Zmiana w ADR-003 popsułaby ADR-007, ADR-012, TDD-001-V2 bez ostrzeżenia.

Rozważaliśmy:
- **Opcja A**: Static links + manual tracking - ODRZUCONA (current state, nie działa)
- **Opcja B**: Bramki wejścia/wyjścia z cascade - ✓ WYBRANA

**Problem 3 - "Fact Dump" Documentation** [E-010]:
> Dokumenty były listami faktów bez narracji. Niemożliwość zweryfikowania zrozumienia.

Rozważaliśmy:
- **Opcja A**: Review checklist - ODRZUCONA (powierzchowna)
- **Opcja B**: Storytelling obowiązkowy per sekcja - ✓ WYBRANA

**Rezultat**: Proof system approach (CONCEPTS-001-V2) z:
- Bramkami globalnymi + wewnętrznymi
- Grafem decyzyjnym (kontekst T₀ + opcje odrzucone)
- Storytelling format
- Evidence notes ([E-XXX])
- Niemutowalnością (versioning decyzji)

**Evidence**:
- [E-003] User survey: gap detection pain points
- [E-004] Analysis: broken dependency cost
- [E-010] Study: documentation comprehension rates

### 1.4 Dokumenty Powiązane

#### Bramki Wejścia (Dependencies)
- **[EXEC-SUM-001]** Podsumowanie Wykonawcze → Wyrównanie strategiczne
- **[BIZ-CASE-001-V2]** Uzasadnienie Biznesowe V2 → Uzasadnienie ROI
- **[VISION-001-V2]** Dokument Wizji - Proof System V2 → Kierunek długoterminowy
- **[CONCEPTS-001-V2]** System Koncepcji → Fundament koncepcyjny

#### Bramki Wyjścia (Wpływy)
- **[TDD-001-V2]** Projekt Techniczny → Zablokowany do req-freeze
- **[TEST-PLAN-001]** Plan Testów → Zablokowany do req-freeze
- **[RTM-001]** Macierz Identyfikowalności → Informowana przez FR/NFR

#### Satelity
- **[TODO-PRD-001-V2]** Lista Zadań
- **[DOR-PRD-001-V2]** Definition of Ready
- **[DOD-PRD-001-V2]** Definition of Done

---

## 2. Przegląd Systemu

### 2.1 Deklaracja Wizji

**Vision Statement** (z VISION-001-V2):
> System Zarządzania Dokumentacją to **proof system z pełną audytowalnością**, który transformuje statyczną dokumentację w **żyjący graf wiedzy projektowej** z automatyczną detekcją luk i guided development.

**Kluczowe różnice vs tradycyjne systemy**:

| Aspekt | Tradycyjny System | Nasz System (Proof) |
|--------|-------------------|---------------------|
| Dokument | Plik .md z hyperlinkami | Ekosystem z bramkami |
| Zależności | Statyczne linki | Bramki wejścia/wyjścia (kaskadowe) |
| Historia | Git log | Graf decyzyjny (semantic) |
| Uzasadnienie | Opcjonalne | Obowiązkowe (storytelling + evidence) |
| Edycja | Edit-in-place | Versioning (immutable decisions) |
| Walidacja | Linting | DoR → Impl Log → DoD → Post-mortem |

### 2.2 Kluczowe Możliwości

**Capability 1: Proof System Documentation** [Mapuje: C-001, C-013, C-014, C-015, C-016]
- Bramki wejścia/wyjścia (globalne + wewnętrzne)
- Graf decyzyjny z kontekstem T₀
- Storytelling obowiązkowy
- Evidence notes ([E-XXX])
- Niemutowalność (changelog)

**Capability 2: Intelligent Gap Detection** [Mapuje: C-004]
- 10 typów luk (E110-E200):
  - E110: Missing sections
  - E120: Placeholders (TODO/TBD)
  - E130: Missing evidence docs
  - E140: Broken dependencies
  - E150: Gate blockers
  - E160: Missing approvals
  - E170: Missing evidence notes (NOWE)
  - E180: Missing storytelling (NOWE)
  - E190: Missing alternatives (NOWE)
  - E200: Missing post-mortem (NOWE)
- Auto-generated remediation steps
- Proaktywne sugestie

**Capability 3: Decision Graph Analysis** [Mapuje: C-003, C-014]
- NetworkX-based graph
- Cycle detection
- Critical path analysis
- Dependency cascade visualization
- Impact analysis ("co się stanie jeśli zmienię X?")

**Capability 4: Lifecycle Management** [Mapuje: C-005, C-017, C-018]
- DoR (Definition of Ready)
- Implementation Log (discoveries during work)
- DoD (Definition of Done)
- Post-mortem (retrospective po 90 dniach)

**Capability 5: Interactive Visualization** [Mapuje: C-010, C-009]
- PySide6 GUI
- Cytoscape.js graph rendering
- Markdown preview z highlighted gaps
- Click-to-jump navigation

### 2.3 Propozycja Wartości dla Użytkowników

#### Dla Developerów
**Pain Point**: "15% czasu idzie na szukanie dlaczego decyzja została podjęta" [E-003]
**Rozwiązanie**: Graf decyzyjny + evidence notes → click-through do pełnego kontekstu
**Wartość**: Redukcja "archaelogy time" o 80%

#### Dla Product Managers
**Pain Point**: "Nie wiemy co się stanie jeśli zmienimy requirement X" [E-011]
**Rozwiązanie**: Impact analysis w czasie rzeczywistym
**Wartość**: Confident change management

#### Dla QA Engineers
**Pain Point**: "Requirement <-> Test mapping ręczny i nieaktualny" [E-012]
**Rozwiązanie**: RTM auto-generated z bramek
**Wartość**: 100% traceability bez manual overhead

#### Dla Technical Writers
**Pain Point**: "Dokumenty pełne TODO/TBD, nie wiem co jest kompletne" [E-013]
**Rozwiązanie**: Gap detection E120 + DoD tracking
**Wartość**: Clear completion criteria

### 2.4 Metryki Sukcesu

**Metryka 1: Gap Detection Accuracy**
- **Target**: ≥95% precision, ≥90% recall
- **Measurement**: Manual audit vs system gaps
- **Evidence**: [E-014] Benchmark results

**Metryka 2: Time to Find Decision Context**
- **Baseline**: 15 min avg (current state) [E-003]
- **Target**: <2 min (click-through)
- **Reduction**: 87%

**Metryka 3: Broken Dependency Rate**
- **Baseline**: 12% docs have broken deps [E-004]
- **Target**: <1% (E140 detection)
- **Reduction**: 92%

**Metryka 4: Documentation Completeness**
- **Baseline**: 60% docs have placeholders [E-013]
- **Target**: <10% (E120 + DoD gates)
- **Improvement**: 83%

**Metryka 5: User Satisfaction**
- **Target**: 4.5/5 rating
- **Method**: Post-deployment survey
- **Review**: 90 days after V1.0

---

## 3. Persony Użytkowników & Use Cases

### 3.1 Persony Główne

#### Persona 1: Alicja - Python Developer

**Demografia**:
- Wiek: 28
- Doświadczenie: 4 lata Python, 2 lata dokumentacji technicznej
- Zespół: 2-3 deweloperów
- Projekty: Średniej wielkości (50-200 plików .md)

**Cele**:
- Szybko zrozumieć kontekst decyzji architektonicznych
- Śledzić zależności między requirements i design
- Zapewnić że dokumentacja jest kompletna przed implementacją

**Pain Points**:
- "Czytam ADR i nie wiem dlaczego opcja B została odrzucona" [E-003]
- "Zmieniam requirement w PRD, nie wiem co to wpłynie" [E-011]
- "Szukam 15 minut 'gdzieś było coś o rate limiting'" [E-015]

**Use Cases**:
- UC-1: Sprawdź decyzję architektoniczną przed implementacją
- UC-2: Zwaliduj że PRD jest kompletny (DoR)
- UC-3: Track "co zależy od tego ADR"

**Success Criteria**:
- < 2 min do znalezienia decision context
- Zero manual dependency tracking
- Visual graph navigation

---

#### Persona 2: Bartek - Product Manager

**Demografia**:
- Wiek: 35
- Doświadczenie: 8 lat PM, 3 lata z dev teams
- Zespół: Cross-functional (dev, QA, design)
- Projekty: Duże (200-500 plików .md)

**Cele**:
- Impact analysis przed zmianą requirements
- Status tracking (DoR/DoD) dla wszystkich dokumentów
- Proaktywna identyfikacja luk w specyfikacji

**Pain Points**:
- "Zmieniam requirement, nie wiem co się psuje downstream" [E-011]
- "60% docs ma TODO/TBD, nie wiem co jest 'gotowe'" [E-013]
- "Brak visibility - czy mamy wszystkie potrzebne dokumenty?" [E-016]

**Use Cases**:
- UC-4: Zobacz status wszystkich dokumentów (dashboard)
- UC-5: Identyfikuj critical gaps przed rozpoczęciem sprintu
- UC-6: Generuj raport kompletności dokumentacji

**Success Criteria**:
- Real-time dependency graph
- <5 min do wygenerowania gap report
- Auto-generated TODO list per dokument

---

#### Persona 3: Cezary - QA Engineer

**Demografia**:
- Wiek: 30
- Doświadczenie: 5 lat QA, 2 lata automation
- Zespół: 2 QA + 4 dev
- Projekty: Test-driven (RTM critical)

**Cele**:
- Requirement-to-Test traceability (RTM)
- Weryfikacja pokrycia testami (coverage)
- Walidacja completeness (AC + NFR)

**Pain Points**:
- "RTM ręczny, nieaktualny po 2 tygodniach" [E-012]
- "Nie wiem czy każdy FR ma test" [E-017]
- "AC w PRD są vague ('should work well')" [E-018]

**Use Cases**:
- UC-7: Track FR → Test mapping (RTM)
- UC-8: Weryfikuj coverage (każdy FR = ≥1 test)
- UC-9: Waliduj AC (measurable metrics)

**Success Criteria**:
- RTM auto-generated z graph
- Visual gap: FR without tests
- AC validation (E180: storytelling + measurable)

---

#### Persona 4: Dorota - Technical Writer

**Demografia**:
- Wiek: 32
- Doświadczenie: 6 lat technical writing
- Zespół: Solo writer dla 2-3 projektów
- Projekty: Documentation-heavy (300+ plików .md)

**Cele**:
- Struktura dokumentów zgodna ze schematem
- Brak placeholders (TODO/TBD) w published docs
- Cross-references aktualne (no broken links)

**Pain Points**:
- "Nie wiem który szablon użyć dla nowego typu dokumentu" [E-019]
- "Placeholders wszędzie, nie wiem co jest final" [E-013]
- "Link ROT detection manual" [E-020]

**Use Cases**:
- UC-10: Utwórz dokument z szablonu (type-specific)
- UC-11: Waliduj strukturę (required sections)
- UC-12: Wykryj broken links (E140)

**Success Criteria**:
- Template-based creation
- E120 detection (placeholders)
- E140 detection (broken deps)

---

### 3.2 Scenariusze Use Case

#### UC-1: Sprawdź Decyzję Architektoniczną (Alicja)

**Preconditions**:
- System zaindexował docs/
- ADR-005 istnieje i ma graf decyzyjny

**Flow**:
1. Alicja otwiera GUI
2. Wyszukuje "database choice" (FTS5)
3. Klika ADR-005 w wynikach
4. Widzi graf decyzyjny z 4 opcjami (MongoDB, MySQL, PostgreSQL ✓, DynamoDB)
5. Klika "Dlaczego NIE MongoDB?"
6. Czyta storytelling: "Początkowo MongoDB wydawał się dobrym wyborem (15k writes/s), ale [E-042] benchmark pokazał brak ACID w distributed setup..."
7. Klika [E-042] → otwiera benchmark report
8. **Total time**: <2 min od wyszukania do pełnego kontekstu

**Postconditions**:
- Alicja rozumie decision context
- Ma link do evidence (benchmark)
- Może proceed z implementacją

**Success Criteria**:
- ✅ FTS5 search < 100ms
- ✅ Click-through navigation
- ✅ Evidence notes clickable

---

#### UC-5: Identyfikuj Critical Gaps (Bartek)

**Preconditions**:
- System przeanalizował 200 dokumentów
- 15 critical gaps wykrytych (E150, E140)

**Flow**:
1. Bartek otwiera Gaps Panel (GUI)
2. Filtruje severity=critical
3. Widzi:
   - E150: REQ-FREEZE blocked (PRD-001: 5 placeholders)
   - E140: TDD-001-V2 → ADR-999 (broken dependency)
   - E150: DESIGN-COMPLETE blocked (TDD-001-V2: missing section "Security")
4. Klika E150 (PRD-001)
5. Widzi remediation steps:
   - Resolve TODO-FR-015 (authentication method)
   - Resolve TBD-FR-022 (rate limiting strategy)
   - ...
6. Generuje TODO-PRD-001 z gaps
7. Przypisuje tasks do zespołu

**Postconditions**:
- Critical gaps zidentyfikowane
- Remediation plan w TODO
- Team może zacząć resolve

**Success Criteria**:
- ✅ Gap severity classification
- ✅ Auto-generated remediation
- ✅ TODO export

---

## 4. Wymagania Funkcjonalne

### 4.1 Moduł Parser (FR-001 do FR-004)

#### FR-001: Parsowanie Plików Markdown

**Mapuje Koncepcje**: C-007 (Parser), C-001 (Dokument)
**Evidence**: [E-002] Benchmark: python-frontmatter 50ms/doc dla 2000-line files

##### Historia wymagania

Początkowo rozważaliśmy **Opcja A: Plain text tylko** (brak formatowania). Odrzuciliśmy, bo:
- Developerzy używają markdown wszędzie (80% w survey [E-001])
- Headers (H1-H6) są naturalnym wyrażeniem hierarchii dokumentu
- Code blocks krytyczne dla przykładów

Potem rozważaliśmy **Opcja B: Rich text (WYSIWYG editor)**. Odrzuciliśmy, bo:
- Proprietary formats (vendor lock-in)
- Git diff nieczytelny
- Brak version control friendly

Wybraliśmy **Opcja C: Markdown (CommonMark + frontmatter)**, bo:
- Git-friendly (line-based diffs)
- Universal support (GitHub, GitLab, Obsidian, VS Code)
- YAML frontmatter = structured metadata
- [E-002] Benchmark: 50ms/doc (spełnia NFR-001)

##### Wymaganie

**Opis**: System musi parsować pliki .md z YAML frontmatter i konwertować na strukturalne obiekty `ParsedDocument`.

**Acceptance Criteria**:
- [ ] **AC-1**: Parser ekstrahuje YAML frontmatter (python-frontmatter library)
  - Measurement: 100% poprawnie sformatowanych frontmatters wyciągniętych
- [ ] **AC-2**: Parser identyfikuje sekcje (H1-H6) z treścią
  - Measurement: markdown-it-py AST traversal, 100% headers wykrytych
- [ ] **AC-3**: Wydajność: <50ms per dokument, <5s dla 100 dokumentów
  - Measurement: pytest-benchmark [E-002]
- [ ] **AC-4**: Graceful error handling (malformed YAML/markdown)
  - Measurement: Zwraca `ParsingError` z line number, nie crash
- [ ] **AC-5**: Zwraca `ParsedDocument` z polami: frontmatter (dict), sections (list), raw_content (str), line_map (dict)

**Constraints**:
- Biblioteka: python-frontmatter (nie rg frontmatter)
- Markdown flavor: CommonMark (nie GFM extensions)
- Encoding: UTF-8 only

**Related FR**:
- FR-002 (Extract Frontmatter) - subprocess FR-001
- FR-003 (Identify Sections) - subprocess FR-001

**Evidence**:
- [E-001] User survey: markdown preference
- [E-002] Benchmark: parsing performance

##### Re-evaluation Triggers

1. **Trigger**: Parsing time > 100ms/doc sustained for 7 days
   - **Action**: Re-benchmark, rozważ caching AST
   - **Owner**: Performance Engineer

2. **Trigger**: >10% parsing errors w production logs (90 dni)
   - **Action**: Re-evaluate markdown library (rozważ mistune/commonmark-py)
   - **Owner**: Dev Lead

---

#### FR-002: Ekstrakcja YAML Frontmatter

**Mapuje Koncepcje**: C-008 (Metadata), C-007 (Parser)
**Evidence**: [E-021] Analysis: 95% docs używa frontmatter dla metadata

##### Historia wymagania

Dyskutowaliśmy 3 podejścia do metadanych:

**Opcja A: Inline comments w markdown** (# meta: value)
- ODRZUCONA: Nie-standardowe, parsing kompleksowy
- [E-022] Survey: 5% devs zna ten format

**Opcja B: Sidecar JSON** (doc.md + doc.json)
- ODRZUCONA: 2 pliki per dokument, sync nightmare
- [E-023] User research: "złe developer experience"

**Opcja C: YAML frontmatter** (--- metadata ---)
- ✓ WYBRANA: Industry standard (Jekyll, Hugo, Obsidian)
- [E-021] Analysis: 95% docs używa tego

##### Wymaganie

**Opis**: System musi wyciągać YAML frontmatter z dokumentów .md i parsować na słownik Pythona.

**Acceptance Criteria**:
- [ ] **AC-1**: Ekstrakcja frontmatter z `---` delimiters
  - Measurement: python-frontmatter.loads() success rate 100%
- [ ] **AC-2**: Parsing YAML do dict (type-safe)
  - Measurement: yaml.safe_load(), brak eval() (security)
- [ ] **AC-3**: Obsługa empty frontmatter (zwraca {})
  - Measurement: Nie crash, default dict
- [ ] **AC-4**: Wykrywanie malformed YAML (syntax errors)
  - Measurement: Zwraca `FrontmatterError` z line number
- [ ] **AC-5**: Preservacja typów (str, int, bool, list, dict)
  - Measurement: Type matching YAML spec

**Constraints**:
- YAML subset: safe_load only (no !python/object)
- Required fields validation: separate module (Validator)

**Related FR**:
- FR-006 (Validate Frontmatter) - następny krok po ekstrakcji
- FR-001 (Parse Markdown) - parent function

**Evidence**:
- [E-021] Frontmatter adoption analysis
- [E-022] Inline metadata survey
- [E-023] UX research: sidecar files

##### Re-evaluation Triggers

1. **Trigger**: YAML security vulnerability (CVE)
   - **Action**: Patch lub migrate to TOML
   - **Owner**: Security Team

---

#### FR-003: Identyfikacja Sekcji Dokumentu

**Mapuje Koncepcje**: C-007 (Parser)
**Evidence**: [E-024] Prototype: markdown-it-py AST < 10ms dla 500-line docs

##### Historia wymagania

Sekcje są kluczowe dla walidacji (FR-007: required sections). Rozważaliśmy:

**Opcja A: Regex parsing** (`r'^#+\s'`)
- ODRZUCONA: Nie chwyta nested structures, edge cases (code blocks)
- [E-025] Prototype: 30% false positives (headers in code blocks)

**Opcja B: AST parsing (markdown-it-py)**
- ✓ WYBRANA: Kompletny AST, heading nodes + hierarchy
- [E-024] Benchmark: <10ms, 100% accuracy

##### Wymaganie

**Opis**: System musi identyfikować wszystkie sekcje markdown (H1-H6) z hierarchią, treścią i numerami linii.

**Acceptance Criteria**:
- [ ] **AC-1**: Wykrycie wszystkich headers (H1-H6)
  - Measurement: markdown-it-py token type='heading', 100% recall
- [ ] **AC-2**: Zachowanie hierarchii (nested levels)
  - Measurement: Tree structure (H2 under H1, H3 under H2)
- [ ] **AC-3**: Ekstrakcja treści per sekcja (text between headers)
  - Measurement: Content slicing by line numbers
- [ ] **AC-4**: Line number mapping (start, end per section)
  - Measurement: `Section.line_start`, `Section.line_end` accuracy
- [ ] **AC-5**: Ignore headers in code blocks/quotes
  - Measurement: Zero false positives from fenced code

**Constraints**:
- Parser: markdown-it-py (CommonMark compliant)
- Hierarchy model: Tree (nie flat list)

**Related FR**:
- FR-007 (Validate Required Sections) - uses section list
- FR-001 (Parse Markdown) - parent function

**Evidence**:
- [E-024] markdown-it-py benchmark
- [E-025] Regex approach failure rate

##### Re-evaluation Triggers

1. **Trigger**: Parsing errors > 1% (headers missed)
   - **Action**: Re-evaluate parser library
   - **Owner**: Dev Lead

---

#### FR-004: Detekcja Odniesień do Innych Dokumentów

**Mapuje Koncepcje**: C-007 (Parser), C-009 (Połączenie)
**Evidence**: [E-026] Analysis: 80% cross-doc refs w dependencies/related frontmatter

##### Historia wymagania

Graf zależności (C-003) wymaga ekstrakcji odniesień między dokumentami. Rozważaliśmy:

**Opcja A: Tylko inline markdown links** (`[text](doc-id)`)
- ODRZUCONA: Brak semantic info (czy to dependency, czy related, czy example?)
- [E-027] Analysis: 60% refs nie ma kontekstu

**Opcja B: Structured frontmatter** (`dependencies: [DOC-1]`)
- ✓ WYBRANA: Typed connections, cascade info, status constraints
- [E-026] Analysis: 80% refs w frontmatter

**Opcja C: Hybrid (frontmatter + inline)**
- Rozważamy w V2.0 (obecnie tylko frontmatter)

##### Wymaganie

**Opis**: System musi wykrywać odniesienia do innych dokumentów w frontmatter (dependencies, related, impacts) i treści markdown.

**Acceptance Criteria**:
- [ ] **AC-1**: Ekstrakcja dependencies z frontmatter
  - Measurement: Parse `dependencies:` list, extract IDs + types
- [ ] **AC-2**: Ekstrakcja impacts (bramki wyjścia)
  - Measurement: Parse `impacts:` list, extract targets + cascade
- [ ] **AC-3**: Ekstrakcja related docs
  - Measurement: Parse `related:` list
- [ ] **AC-4**: Wykrywanie inline links w markdown body
  - Measurement: Regex `\[.*?\]\((.*?)\)`, filter internal docs
- [ ] **AC-5**: Klasyfikacja typu odniesienia (requires, informs, blocks, references)
  - Measurement: Type field w frontmatter (enum validation)

**Constraints**:
- Reference format: DOC-ID (nie file paths)
- Link validation: separate module (Validator FR-032)

**Related FR**:
- FR-011 (Manage Edges) - uses references dla graph construction
- FR-017 (Detect Broken Dependencies) - walidacja ref targets

**Evidence**:
- [E-026] Frontmatter reference analysis
- [E-027] Inline link context study

##### Re-evaluation Triggers

1. **Trigger**: >20% refs w inline links (nie frontmatter) w 6 months
   - **Action**: Add inline link extraction (Hybrid approach)
   - **Owner**: Product Manager

---

### 4.2 Moduł Validator (FR-005 do FR-008)

#### FR-005: Walidacja Schematu Dokumentu

**Mapuje Koncepcje**: C-006 (Walidator), C-002 (Typ Dokumentu)
**Evidence**: [E-028] Prototype: Pydantic validation <5ms per doc

##### Historia wymagania

Każdy typ dokumentu (PRD, ADR, RFC, etc.) ma inny schemat. Rozważaliśmy:

**Opcja A: JSON Schema** (external .json files)
- ODRZUCONA: Validation separateod Pythona, no IDE autocomplete
- [E-029] Developer feedback: "prefer Python-native"

**Opcja B: Pydantic models** (Python classes)
- ✓ WYBRANA: Type safety, IDE support, validation errors z line numbers
- [E-028] Benchmark: <5ms validation, rich error messages

**Opcja C: Custom validators** (ręczny Python)
- ODRZUCONA: Reinventing wheel, maintenance overhead

##### Wymaganie

**Opis**: System musi walidować cały dokument względem schematu typu (frontmatter + sections + content).

**Acceptance Criteria**:
- [ ] **AC-1**: Ładowanie schematu typu z YAML (document_types.yaml)
  - Measurement: Schema registry, lazy loading
- [ ] **AC-2**: Walidacja frontmatter fields (Pydantic)
  - Measurement: Required fields present, types match, enums valid
- [ ] **AC-3**: Walidacja sekcji (required_sections w schemacie)
  - Measurement: All mandatory sections present (regex match pattern)
- [ ] **AC-4**: Zwrot ValidationResult z errors (line numbers)
  - Measurement: Each error = field path + line + message
- [ ] **AC-5**: Wydajność: <10ms per dokument
  - Measurement: pytest-benchmark [E-028]

**Constraints**:
- Schema format: YAML (document_types.yaml)
- Validation library: Pydantic v2
- Error format: List[ValidationError] (każdy z line_number)

**Related FR**:
- FR-006 (Validate Frontmatter) - subprocess FR-005
- FR-007 (Validate Sections) - subprocess FR-005
- FR-002 (Extract Frontmatter) - input dla FR-005

**Evidence**:
- [E-028] Pydantic benchmark
- [E-029] Developer preferences survey

##### Re-evaluation Triggers

1. **Trigger**: Validation time >50ms dla 90% docs (7 dni)
   - **Action**: Profile Pydantic, rozważ caching
   - **Owner**: Performance Engineer

---

#### FR-006: Walidacja Frontmatter YAML

**Mapuje Koncepcje**: C-006 (Walidator), C-008 (Metadata)
**Evidence**: [E-030] Analysis: 40% docs ma invalid frontmatter fields

##### Historia wymagania

Frontmatter validation krytyczna dla proof system (bramki, evidence refs). [E-030] pokazał:
- 40% docs: typo w status ("darft" zamiast "draft")
- 25% docs: missing required field (id, type)
- 15% docs: invalid dependency format

Rozważaliśmy validation strategies:
**Opcja A: Runtime tylko (validate on load)**
- ODRZUCONA: Errors discovered late (podczas GUI usage)

**Opcja B: CI/CD validation (pre-commit hook)**
- ✓ WYBRANA: Early detection, nie blokuje workflow
- [E-031] Study: 80% validation errors caught przed commit

##### Wymaganie

**Opis**: System musi walidować wszystkie pola YAML frontmatter względem ograniczeń schematu typu dokumentu.

**Acceptance Criteria**:
- [ ] **AC-1**: Sprawdzenie required fields (id, type, status, created, etc.)
  - Measurement: Pydantic required=True, error jeśli missing
- [ ] **AC-2**: Walidacja wartości enum (status, priority, severity)
  - Measurement: Field type=Literal["draft"|"review"|...], reject invalid
- [ ] **AC-3**: Walidacja formatów (date jako YYYY-MM-DD, id jako PATTERN)
  - Measurement: Pydantic validators (regex, date parsing)
- [ ] **AC-4**: Walidacja struktur nested (dependencies, impacts jako list[dict])
  - Measurement: Nested Pydantic models
- [ ] **AC-5**: Zwrot error z field path (np. "dependencies[0].id: missing")
  - Measurement: Pydantic error.loc tuple

**Constraints**:
- Validation schema: Defined per document type w document_types.yaml
- Error reporting: Field path + value + constraint + line number

**Related FR**:
- FR-002 (Extract Frontmatter) - poprzedni krok
- FR-005 (Validate Schema) - parent function
- FR-081 (Evaluate Gates) - uses validated frontmatter

**Evidence**:
- [E-030] Frontmatter error rate analysis
- [E-031] CI/CD validation effectiveness

##### Re-evaluation Triggers

1. **Trigger**: >10% validation errors w production (30 dni)
   - **Action**: Improve error messages, add auto-fix suggestions
   - **Owner**: UX Lead

---

#### FR-007: Walidacja Wymaganych Sekcji

**Mapuje Koncepcje**: C-006 (Walidator), C-002 (Typ Dokumentu)
**Evidence**: [E-032] Analysis: 50% docs ma missing required sections

##### Historia wymagania

Każdy typ dokumentu ma mandatory sections (np. ADR wymaga "Alternatives Considered", PRD wymaga "Acceptance Criteria"). [E-032] pokazał:
- 50% ADR: brak sekcji "Alternatives" (violation proof system)
- 30% PRD: brak "Non-Functional Requirements"
- 20% RFC: brak "Open Questions"

To jest **E110 gap type** - critical dla DoR/DoD gates.

##### Wymaganie

**Opis**: System musi weryfikować obecność wszystkich obowiązkowych sekcji zdefiniowanych w schemacie typu dokumentu.

**Acceptance Criteria**:
- [ ] **AC-1**: Matching sekcji po regex pattern (np. `^## Alternatives Considered`)
  - Measurement: re.search(pattern, section_header), case-insensitive option
- [ ] **AC-2**: Sprawdzenie min_items (jeśli sekcja ma subsections)
  - Measurement: np. "Functional Requirements" wymaga ≥10 FR-XXX subsections
- [ ] **AC-3**: Wykrywanie missing sections (E110 gap)
  - Measurement: Gap generated with remediation: "Add section '## Security Considerations'"
- [ ] **AC-4**: Obsługa optional vs mandatory
  - Measurement: Schema field `mandatory: true|false`
- [ ] **AC-5**: Line number suggestion (gdzie dodać section)
  - Measurement: Recommend insertion after previous section or at end

**Constraints**:
- Section matching: Regex per document type schema
- Min_items applicable tylko dla list sections (FR, NFR, US, etc.)

**Related FR**:
- FR-003 (Identify Sections) - input
- FR-014 (Detect Missing Sections E110) - uses FR-007 output
- FR-005 (Validate Schema) - parent function

**Evidence**:
- [E-032] Missing sections analysis

##### Re-evaluation Triggers

1. **Trigger**: False positive rate >5% (E110 incorrectly flagged)
   - **Action**: Refine regex patterns, add schema exceptions
   - **Owner**: Validator Maintainer

---

#### FR-008: Detekcja Placeholderów (TODO/TBD/FIXME)

**Mapuje Koncepcje**: C-006 (Walidator), C-004 (Luka - E120)
**Evidence**: [E-033] Analysis: 60% docs ma ≥1 placeholder

##### Historia wymagania

Placeholders (TODO, TBD, PLACEHOLDER, XXX, FIXME) oznaczają niekompletną treść. [E-033] pokazał:
- 60% docs: ≥1 placeholder
- 40% docs: placeholders w critical sections (decision rationale, AC)
- 20% docs: stale placeholders (>3 miesiące bez zmian)

To jest **E120 gap type** - bloker dla REQ-FREEZE, DESIGN-COMPLETE gates.

Rozważaliśmy detection strategies:
**Opcja A: Simple regex** (`TODO|TBD`)
- Partial: Chwyci większość, ale miss variations

**Opcja B: NLP-based** (detect incomplete sentences)
- ODRZUCONA: Złożone, false positives
- [E-034] Prototype: 20% precision

**Opcja C: Keyword list + context** (current choice)
- ✓ WYBRANA: Predefined keywords + section severity classification
- [E-033] Analysis: 95% precision

##### Wymaganie

**Opis**: System musi wykrywać placeholders (TODO, TBD, PLACEHOLDER, XXX, FIXME, TBA) w treści dokumentu.

**Acceptance Criteria**:
- [ ] **AC-1**: Detekcja keywords (TODO, TBD, PLACEHOLDER, XXX, FIXME, TBA, ...)
  - Measurement: Regex `\b(TODO|TBD|PLACEHOLDER|XXX|FIXME|TBA)\b`, case-insensitive
- [ ] **AC-2**: Line number + context (±2 lines around placeholder)
  - Measurement: Gap includes line_number + surrounding_text
- [ ] **AC-3**: Section classification (critical vs informational)
  - Measurement: Placeholder w "Decision Rationale" = critical, w "Appendix" = low
- [ ] **AC-4**: Ignore code blocks/quotes (no false positives from examples)
  - Measurement: markdown-it-py AST: skip `code_block`, `blockquote` nodes
- [ ] **AC-5**: Generowanie E120 gap z remediation
  - Measurement: Gap message: "Resolve TODO at line 245: 'Database choice TBD'"

**Constraints**:
- Keyword list: Extensible w config (nie hardcoded)
- Severity: Per-section configurable w document type schema

**Related FR**:
- FR-003 (Identify Sections) - dla section classification
- FR-015 (E120 Gap Detection) - uses FR-008 output
- FR-005 (Validate Schema) - parent function

**Evidence**:
- [E-033] Placeholder prevalence analysis
- [E-034] NLP approach failure

##### Re-evaluation Triggers

1. **Trigger**: False positive rate >10% (placeholders w code examples flagged)
   - **Action**: Improve AST filtering, add whitelist patterns
   - **Owner**: Validator Maintainer

2. **Trigger**: New placeholder keywords appearing (w post-deployment logs)
   - **Action**: Extend keyword list
   - **Owner**: Content Lead

---

### 4.3 Moduł Graph Builder (FR-009 do FR-013)

#### FR-009: Konstrukcja Grafu Decyzyjnego

**Mapuje Koncepcje**: C-003 (Graf Decyzyjny), C-014 (Decision Graph w proof system)
**Evidence**: [E-035] Benchmark: NetworkX graph dla 1000 docs <2s

##### Historia wymagania - Dlaczego Graf Decyzyjny?

W V1 (Obsidian plugin) mieliśmy prosty dependency graph (A→B→C). To nie wystarczało dla proof system. Potrzebowaliśmy:
- **Kontekst T₀**: Stan systemu w momencie decyzji (budget, timeline, constraints)
- **Opcje odrzucone**: Dlaczego NIE wybrano A, B, D (tylko C)
- **Evidence trail**: Każda krawędź = backed by [E-XXX] note

[E-036] User research: "80% czasu na archaeology - dlaczego ta decyzja?"

Rozważaliśmy graph engines:
**Opcja A: igraph (C library)**
- ODRZUCONA: Python bindings słabe, mniej features
- [E-037] Comparison: igraph vs NetworkX features

**Opcja B: Neo4j (graph database)**
- ODRZUCONA: External dependency, overkill dla local files
- [E-038] Study: Neo4j setup complexity

**Opcja C: NetworkX (Python-native)**
- ✓ WYBRANA: Rich API, cycle detection, path analysis, battle-tested
- [E-035] Benchmark: 1000 nodes <2s construction

##### Wymaganie

**Opis**: System musi budować directed graph z wszystkich dokumentów, z węzłami (docs) i typowanymi krawędziami (dependencies, impacts, alternatives).

**Acceptance Criteria**:
- [ ] **AC-1**: Graph construction z parsed docs
  - Measurement: NetworkX DiGraph, nodes = DocumentNode, edges = typed relationships
- [ ] **AC-2**: Węzły zawierają: doc metadata + decision context (T₀) + opcje alternatywne
  - Measurement: Node attributes: `context_snapshot`, `alternatives`, `evidence_ids`
- [ ] **AC-3**: Krawędzie typowane: requires, informs, blocks, references, alternative-to
  - Measurement: Edge `type` attribute (enum)
- [ ] **AC-4**: Wydajność: <2s dla 100 docs, <30s dla 1000 docs
  - Measurement: pytest-benchmark [E-035]
- [ ] **AC-5**: Obsługa incremental updates (add/remove/modify doc → update graph)
  - Measurement: Delta updates (nie full rebuild)

**Constraints**:
- Library: NetworkX 3.x
- Graph type: DiGraph (directed)
- Node ID: Document ID (string)
- Edge attributes: type, cascade, evidence

**Related FR**:
- FR-010 (Manage Nodes) - subprocess
- FR-011 (Manage Edges) - subprocess
- FR-012 (Detect Cycles) - uses graph
- FR-004 (Detect References) - input dla edges

**Evidence**:
- [E-035] NetworkX benchmark
- [E-036] User research: decision archaeology time
- [E-037] igraph comparison
- [E-038] Neo4j complexity study

##### Re-evaluation Triggers

1. **Trigger**: Construction time >1min dla 1000 docs (sustained 7 days)
   - **Action**: Profile NetworkX calls, rozważ caching/indexing
   - **Owner**: Performance Engineer

2. **Trigger**: Memory usage >1GB dla 1000 docs
   - **Action**: Optimize node attributes (lazy load content)
   - **Owner**: Dev Lead

---

#### FR-010: Zarządzanie Węzłami Grafu

**Mapuje Koncepcje**: C-010 (Węzeł)
**Evidence**: [E-039] Analysis: Emergent properties (gap count, blocker status) critical for navigation

##### Historia wymagania

Węzeł grafu to nie tylko dokument - to **żywa reprezentacja** ze stanem:
- **Status**: draft → review → approved → deployed → closed
- **Gaps**: Lista wykrytych luk (E110-E200)
- **Blockers**: Czy bramki blokują progres?
- **Impact radius**: Ilu dokumentów zależy od tego węzła?

[E-039] pokazał: Developerzy używają graph navigation by:
- Kolor węzła (red=blocked, yellow=gaps, green=ok)
- Size węzła (proporcjonalny do impact radius)
- Badge count (liczba gaps)

##### Wymaganie

**Opis**: System musi tworzyć i zarządzać węzłami grafu z metadanymi dokumentów i obliczonymi właściwościami emergentnymi.

**Acceptance Criteria**:
- [ ] **AC-1**: Tworzenie węzła z DocumentNode class
  - Measurement: Node zawiera: id, type, status, frontmatter (dict), content_summary (str)
- [ ] **AC-2**: Obliczanie właściwości emergentnych:
  - `gap_count` (int) - liczba wykrytych luk
  - `blocker_status` (bool) - czy jakieś bramki blokują
  - `impact_radius` (int) - liczba downstream dependencies
  - `last_updated` (datetime) - z changelog
  - Measurement: Properties auto-calculated on node creation/update
- [ ] **AC-3**: Lazy loading content (treść dokumentu ładowana on-demand)
  - Measurement: Node default: tylko metadata, content loaded when requested
- [ ] **AC-4**: Update node on file change
  - Measurement: File watcher trigger → re-parse → update node attributes
- [ ] **AC-5**: Node serialization (dla persistence)
  - Measurement: to_dict() method, JSON-serializable

**Constraints**:
- Node class: Pydantic BaseModel (type-safe)
- Emergent properties: Calculated fields (nie persisted)
- Content: Lazy load (performance)

**Related FR**:
- FR-009 (Build Graph) - parent function
- FR-029 (File Watcher) - triggers node updates
- FR-014-020 (Gap Detection) - inputs dla gap_count

**Evidence**:
- [E-039] Graph navigation behavior analysis

##### Re-evaluation Triggers

1. **Trigger**: Emergent property calculation >100ms per node
   - **Action**: Profile calculation, add caching
   - **Owner**: Performance Engineer

---

#### FR-011: Zarządzanie Krawędziami Grafu

**Mapuje Koncepcje**: C-009 (Połączenie)
**Evidence**: [E-040] Analysis: Typed edges reduce "unknown dependency type" issues by 70%

##### Historia wymagania

W V1 (Obsidian plugin) wszystkie połączenia były generic ("related"). To powodowało:
- [E-041] Analysis: 30% uncertainty "czy to dependency (blokuje), czy reference (informuje)?"
- Brak cascade info: Zmiana w A → jak wpływa na B, C, D?
- Brak validation: Czy ADR może "blocks" inny ADR? (powinien "informs")

Proof system wymaga **typed, validated edges** z cascade mechanism.

Rozważaliśmy edge type systems:
**Opcja A: Free-form labels** (user-defined strings)
- ODRZUCONA: No validation, inconsistency
- [E-042] Study: 50 różnych label variants dla "dependency"

**Opcja B: Fixed enum types** (requires, informs, blocks, references, alternative-to)
- ✓ WYBRANA: Consistency, validation, clear semantics
- [E-040] Analysis: 70% reduction w confusion

##### Wymaganie

**Opis**: System musi tworzyć typowane krawędzie między węzłami z metadanymi (type, cascade, evidence, status_constraint).

**Acceptance Criteria**:
- [ ] **AC-1**: Tworzenie krawędzi z Edge class (Pydantic)
  - Measurement: Edge attributes: source (NodeID), target (NodeID), type (enum), cascade (bool), evidence (list[str])
- [ ] **AC-2**: Validation typu krawędzi per document type
  - Measurement: Schema `allowed_connections`: ADR może "requires" ADR, nie może "implements" ADR
- [ ] **AC-3**: Status constraints
  - Measurement: Edge może wymagać target.status == approved (nie draft)
- [ ] **AC-4**: Cascade propagation (change in source → update targets)
  - Measurement: cascade=true → zmiana w source generates TODO w targets
- [ ] **AC-5**: Edge serialization (dla persistence)
  - Measurement: to_dict() method, JSON-serializable

**Constraints**:
- Edge types: Enum (requires, informs, blocks, references, alternative-to, tested-by)
- Validation: Per document type schema (allowed_connections)
- Cascade: Boolean flag + propagation rules

**Related FR**:
- FR-009 (Build Graph) - parent function
- FR-034 (Create/Validate Edges) - detailed validation logic
- FR-083 (Propagate Changes Through Gates) - uses cascade

**Evidence**:
- [E-040] Typed edges effectiveness
- [E-041] Dependency type confusion analysis
- [E-042] Free-form label variance study

##### Re-evaluation Triggers

1. **Trigger**: >10% validation errors (invalid edge types) w 30 dni
   - **Action**: Review allowed_connections schema, add auto-suggestions
   - **Owner**: Schema Maintainer

---

#### FR-012: Detekcja Cykli w Grafie

**Mapuje Koncepcje**: C-003 (Graf Zależności)
**Evidence**: [E-043] Analysis: 8% projektów ma cykliczne zależności (accident

al)

##### Historia wymagania

Cykliczne zależności (A→B→C→A) są **zazwyczaj błędem**:
- [E-043] Analysis: 8% projektów ma cycle (przypadkowe)
- [E-044] Study: 95% cycles to "refactoring gone wrong"
- 5% cycles to **intentional** (mutual references w design patterns)

Potrzebujemy:
- Detekcja cycles (NetworkX.simple_cycles())
- Severity classification (critical vs informational)
- Remediation suggestions ("Break cycle by removing edge X→Y")

##### Wymaganie

**Opis**: System musi wykrywać i raportować cykliczne zależności w grafie z klasyfikacją severity.

**Acceptance Criteria**:
- [ ] **AC-1**: Algorytm detekcji (NetworkX.simple_cycles())
  - Measurement: Znajdowanie wszystkich cykli w DiGraph
- [ ] **AC-2**: Raportowanie path (A→B→C→A)
  - Measurement: Gap message zawiera full cycle path
- [ ] **AC-3**: Severity classification:
  - Critical: Cycle w "requires" edges (blocks progress)
  - Warning: Cycle w "informs" edges (mutual references ok)
  - Measurement: Severity based on edge types w cyklu
- [ ] **AC-4**: Remediation suggestions
  - Measurement: "Break cycle: Remove edge X→Y or change type to 'informs'"
- [ ] **AC-5**: Wydajność: <1s dla 1000 nodes
  - Measurement: NetworkX algorithm performance

**Constraints**:
- Algorithm: NetworkX.simple_cycles() (Johnson's algorithm)
- Classification: Based on edge types (requires=critical, informs=warning)

**Related FR**:
- FR-009 (Build Graph) - input
- FR-011 (Manage Edges) - uses edge types dla severity

**Evidence**:
- [E-043] Cycle prevalence analysis
- [E-044] Cycle intentionality study

##### Re-evaluation Triggers

1. **Trigger**: Detection time >5s dla 1000 nodes (sustained 7 days)
   - **Action**: Profile algorithm, rozważ incremental detection
   - **Owner**: Performance Engineer

2. **Trigger**: >20% cykli classified as "intentional" (manual override)
   - **Action**: Re-evaluate severity rules, add cycle whitelisting
   - **Owner**: Product Manager

---

#### FR-013: Obliczanie Poziomów Hierarchii

**Mapuje Koncepcje**: C-003 (Graf Zależności)
**Evidence**: [E-045] Analysis: Hierarchical layout improves graph readability by 60%

##### Historia wymagania

Graph layout algorytmy (Cytoscape.js) działają lepiej z **hierarchical levels**:
- Level 0: Root nodes (no incoming "requires" edges)
- Level 1: Nodes requiring only Level 0
- Level N: max(parent_levels) + 1

[E-045] User study:
- Hierarchical layout: 60% faster navigation (vs force-directed)
- 80% prefer "strategic docs at top, impl at bottom"

Obliczanie levels wymaga:
- Topological sort (dla DAG)
- Handling orphan nodes (no dependencies)
- Caching (expensive calculation)

##### Wymaganie

**Opis**: System musi obliczać emergentne poziomy hierarchii ze struktury grafu (root=0, children=parent+1).

**Acceptance Criteria**:
- [ ] **AC-1**: Algorytm level assignment:
  - Root nodes (no incoming "requires"): level=0
  - Children: level = max(parent_levels) + 1
  - Measurement: NetworkX topological sort, BFS traversal
- [ ] **AC-2**: Obsługa orphan nodes (no dependencies):
  - Measurement: Orphans = level 0 (traktowane jako roots)
- [ ] **AC-3**: Obsługa cycles (jeśli wykryte):
  - Measurement: Nodes w cyklu = level = min(cycle_node_levels) (arbitrarily break tie)
- [ ] **AC-4**: Caching levels (nie recalculate on every render)
  - Measurement: Cache invalidation on graph structure change only
- [ ] **AC-5**: Wydajność: <500ms dla 1000 nodes
  - Measurement: pytest-benchmark

**Constraints**:
- Algorithm: Topological sort (Kahn's algorithm or DFS)
- Edge consideration: Only "requires", "blocks" edges (not "informs", "references")
- Cache: In-memory (NetworkX node attributes)

**Related FR**:
- FR-009 (Build Graph) - input
- FR-022 (Graph Visualization) - uses levels dla layout

**Evidence**:
- [E-045] Hierarchical layout readability study

##### Re-evaluation Triggers

1. **Trigger**: Calculation time >2s dla 1000 nodes
   - **Action**: Profile algorithm, rozważ incremental updates
   - **Owner**: Performance Engineer

---

## 4.4 Moduł Gap Detection Engine (FR-014 do FR-020, + NOWE: FR-100, FR-091, FR-093, FR-111)

### Proof System Gaps (4 NOWE typy)

Proof system dodaje 4 nowe typy luk:
- **E170**: Missing Evidence Notes - każde twierdzenie wymaga [E-XXX] source
- **E180**: Missing Storytelling - sekcje krytyczne wymagają narracji (nie fact lists)
- **E190**: Missing Alternatives - decyzje wymagają ≥2 opcji (pokazać odrzucone)
- **E200**: Missing Post-mortem - dokumenty deployed >90 dni wymagają retrospektywę

---

#### FR-100: Detekcja Brakujących Not Dowodowych (E170)

**Mapuje Koncepcje**: C-004 (Luka), C-016 (Nota Dowodowa)
**Evidence**: [E-046] Analysis: 70% twierdzeń w V1 docs nie ma źródła/evidence

**⭐ NOWE w V2 - to jest kluczowe dla proof system!**

##### Historia wymagania

Proof system wymaga **każde twierdzenie = backed by evidence**. Przykłady twierdzeń wymagających evidence:
- "Performance: <50ms/doc" → [E-002] Benchmark
- "80% devs prefer markdown" → [E-001] User survey
- "MongoDB nie ma ACID" → [E-042] Technical analysis

[E-046] pokazał problem w V1:
- 70% twierdzeń: brak source/evidence
- 40% benchmarks: brak raw data
- 25% requirements: brak user research justification

To jest **research-grade documentation requirement**.

##### Wymaganie

**Opis**: System musi wykrywać twierdzenia (assertions) w sekcjach krytycznych bez not dowodowych ([E-XXX] references).

**Acceptance Criteria**:
- [ ] **AC-1**: Detekcja twierdzeń w sekcjach krytycznych:
  - Patterns: "X% users/devs", "benchmark: Y ms", "cost: $Z", "requirement from [stakeholder]"
  - Sekcje krytyczne: "Decision Rationale", "Performance Requirements", "Cost Analysis"
  - Measurement: Regex patterns dla quantified statements
- [ ] **AC-2**: Sprawdzenie obecności [E-XXX] reference w tym samym paragrafie
  - Measurement: Regex `\[E-\d{3,}\]` w ±3 liniach od twierdzenia
- [ ] **AC-3**: Generowanie E170 gap dla unsubstantiated claims
  - Measurement: Gap message: "Line 245: Claim 'MongoDB 15k writes/s' lacks evidence note"
- [ ] **AC-4**: Remediation suggestion
  - Measurement: "Create evidence note [E-XXX] with benchmark data / survey results / source document"
- [ ] **AC-5**: Severity: Critical dla decision-critical sections, Warning dla appendices
  - Measurement: Per-section severity mapping w document type schema

**Constraints**:
- Evidence format: `[E-NNN]` gdzie NNN = 3+ digit number
- Sections classified: Critical vs Informational (w schema)
- Whitelist: Some generic statements don't need evidence (TBD w config)

**Related FR**:
- FR-101-106 (Evidence Management) - manage evidence notes
- FR-005 (Validate Schema) - section classification

**Evidence**:
- [E-046] Unsubstantiated claims analysis V1

##### Re-evaluation Triggers

1. **Trigger**: False positive rate >15% (generic statements flagged)
   - **Action**: Refine assertion patterns, expand whitelist
   - **Owner**: Validator Maintainer

2. **Trigger**: Low adoption (<50% evidence notes created w 6 months)
   - **Action**: Simplify evidence note creation, add templates
   - **Owner**: Product Manager

---

#### FR-093: Detekcja Brakującego Storytelling (E180)

**Mapuje Koncepcje**: C-004 (Luka), C-015 (Storytelling)
**Evidence**: [E-047] Study: Narrative format increases comprehension by 45%

**⭐ NOWE w V2 - fundamentalne dla proof system!**

##### Historia wymagania

Proof system philosophy: **Dokumentacja = narracja, nie lista faktów**.

Dlaczego storytelling?
- [E-047] Study: 45% wzrost comprehension (vs bullet lists)
- [E-048] Observation: "Nie można spójnie opowiedzieć czego się nie rozumie" (testowalne zrozumienie)
- [E-049] Analysis: Fact lists ukrywają luki w reasoning ("dlaczego to założenie?")

Storytelling obowiązkowy w sekcjach:
- Decision Rationale (ADR/RFC)
- Requirements History (PRD - dlaczego te requirements?)
- Problem Statement (wszystkie docs)

Przykład ZŁEGO (fact list):
```
## Decision
- Chose PostgreSQL
- Pros: ACID, performance
- Cons: Cost
```

Przykład DOBREGO (storytelling):
```
## Decision: Dlaczego PostgreSQL, nie MongoDB?

Początkowo MongoDB wydawał się naturalnym wyborem - [E-042] benchmark
pokazał 15k writes/s (vs PostgreSQL 12k). Ale odkryliśmy critical
problem: distributed MongoDB nie gwarantuje ACID...
[Full narrative]
```

##### Wymaganie

**Opis**: System musi wykrywać sekcje krytyczne zawierające tylko listy faktów (bullet points) bez narracji łączącej.

**Acceptance Criteria**:
- [ ] **AC-1**: Identyfikacja sekcji wymagających storytelling:
  - Sekcje: "Decision Rationale", "Problem Statement", "Requirements History", "Alternatives Considered"
  - Measurement: Document type schema: `storytelling_required: true` per section
- [ ] **AC-2**: Detekcja "fact dump" patterns:
  - High bullet point ratio (>70% linii to bullet points)
  - Brak narrative connectors ("początkowo", "ale", "dlatego", "w rezultacie")
  - Brak comparison phrases ("vs", "zamiast", "lepiej niż")
  - Measurement: NLP heuristics (simple)
- [ ] **AC-3**: Generowanie E180 gap
  - Measurement: Gap message: "Section 'Decision Rationale' lacks narrative - rewrite as story"
- [ ] **AC-4**: Remediation guidance
  - Measurement: Link do storytelling guide: "Opisz jako: Punkt startowy → Problem → Opcje → Dlaczego wybrana → Rezultat"
- [ ] **AC-5**: Severity: Critical dla decision sections, Warning dla others

**Constraints**:
- Detection: Heuristic-based (nie full NLP - too complex)
- Whitelist: Some sections allowed to be lists (Appendix, Glossary)

**Related FR**:
- FR-092-099 (Storytelling Engine) - manage storytelling templates
- FR-005 (Validate Schema) - section requirements

**Evidence**:
- [E-047] Storytelling comprehension study
- [E-048] "Can't tell coherently" observation
- [E-049] Fact lists hide reasoning gaps

##### Re-evaluation Triggers

1. **Trigger**: False negative rate >20% (fact dumps nie wykryte)
   - **Action**: Improve NLP heuristics, add ML model (future)
   - **Owner**: Research Lead

2. **Trigger**: User complaints: "Too strict, some lists are ok"
   - **Action**: Refine section classification, add exceptions
   - **Owner**: UX Lead

---

#### FR-091: Detekcja Brakujących Alternatyw (E190)

**Mapuje Koncepcje**: C-004 (Luka), C-014 (Graf Decyzyjny)
**Evidence**: [E-050] Analysis: 85% ADR w V1 pokazuje tylko wybraną opcję

**⭐ NOWE w V2 - krytyczne dla auditability!**

##### Historia wymagania

Proof system wymaga **decision graph z opcjami odrzuconymi**. Dlaczego?
- [E-050] Analysis: 85% ADR w V1 = tylko chosen option (brak context "dlaczego NIE A?")
- [E-051] User research: "Nie wiem czy autor w ogóle rozważył alternatywę X"
- [E-052] Study: Showing rejected options increases decision confidence by 60%

Minimum requirements:
- ≥2 opcje (chosen + ≥1 rejected)
- Każda opcja: Pros, Cons, Evidence ([E-XXX] benchmark/analysis)
- Explicit rejection rationale ("DLACZEGO NIE")

##### Wymaganie

**Opis**: System musi weryfikować że decyzje (ADR, RFC, design choices w PRD/TDD) pokazują ≥2 opcje z uzasadnieniem wyboru.

**Acceptance Criteria**:
- [ ] **AC-1**: Identyfikacja dokumentów decyzyjnych:
  - Typy: ADR, RFC, sekcje "Design Choices" w PRD/TDD
  - Measurement: Document type lub section pattern match
- [ ] **AC-2**: Sprawdzenie frontmatter `alternatives:`
  - Minimum 2 alternatives (≥1 rejected + 1 selected)
  - Każda opcja: id, title, status (selected|rejected|deferred), reason, evidence
  - Measurement: Pydantic validation alternatives schema
- [ ] **AC-3**: Weryfikacja uzasadnień porównawczych w body:
  - Sekcje "Dlaczego X, nie Y?" w Decision Rationale
  - Measurement: Regex pattern `Dlaczego .+, nie .+\?` lub tabelaryczne comparison
- [ ] **AC-4**: Generowanie E190 gap jeśli:
  - <2 alternatives w frontmatter
  - Brak rejection rationale w body
  - Measurement: Gap message: "Decision lacks alternatives - add ≥1 rejected option"
- [ ] **AC-5**: Remediation guidance
  - Measurement: "Add alternative options: Document what you considered but didn't choose and why"

**Constraints**:
- Minimum: 2 alternatives total (preferred: 3-4)
- Evidence: ≥1 per alternative (benchmark, analysis, cost calc)

**Related FR**:
- FR-009 (Build Decision Graph) - uses alternatives
- FR-006 (Validate Frontmatter) - alternatives schema

**Evidence**:
- [E-050] Single-option ADR prevalence
- [E-051] Lack of alternatives user research
- [E-052] Rejected options confidence study

##### Re-evaluation Triggers

1. **Trigger**: Low compliance (<60% ADR have alternatives w 6 months)
   - **Action**: Mandatory ADR template enforcement, training
   - **Owner**: Process Lead

---

#### FR-111: Detekcja Brakującego Post-mortem (E200)

**Mapuje Koncepcje**: C-004 (Luka), C-018 (Post-mortem)
**Evidence**: [E-053] Study: Post-mortems (even on success) improve future performance by 30%

**⭐ NOWE w V2 - lifecycle completeness!**

##### Historia wymagania

Proof system lifecycle: DoR → Implementation → DoD → **Post-mortem (90 dni po deploy)**.

W V1: post-mortems tylko dla failures. To jest błąd!
- [E-053] Study: Post-mortem nawet po sukcesie = 30% improvement w następnych projektach
- [E-054] Analysis: "What worked better than expected?" = najcenniejszy learning
- [E-055] Observation: Re-evaluation triggers mogą fire - post-mortem to review

Post-mortem triggers:
- 90 dni po deployment_date (automatyczny)
- Re-evaluation trigger fired (manualny)
- Major incident (manualny)

##### Wymaganie

**Opis**: System musi wykrywać dokumenty deployed >90 dni bez post-mortem satellite.

**Acceptance Criteria**:
- [ ] **AC-1**: Identyfikacja deployed documents:
  - Status: deployed lub closed
  - Field: `deployment_date` (YYYY-MM-DD)
  - Measurement: Frontmatter validation
- [ ] **AC-2**: Sprawdzenie age (current_date - deployment_date)
  - Trigger: ≥90 days
  - Measurement: datetime calculation
- [ ] **AC-3**: Sprawdzenie istnienia POST-MORTEM satellite:
  - Path: `/satellites/post-mortems/POST-MORTEM-{DOC-ID}.md`
  - Measurement: File existence check
- [ ] **AC-4**: Generowanie E200 gap jeśli brak post-mortem
  - Measurement: Gap message: "Document deployed 120 days ago - post-mortem overdue"
- [ ] **AC-5**: Remediation suggestion
  - Measurement: "Create post-mortem: Review metrics, what worked/failed, next steps"

**Constraints**:
- Trigger: 90 days (configurable per project)
- Satellite path: Convention `/satellites/post-mortems/`

**Related FR**:
- FR-112-114 (Implementation Log) - input dla post-mortem
- FR-036-038 (Satellite Management) - create post-mortem

**Evidence**:
- [E-053] Post-mortem effectiveness study
- [E-054] "Better than expected" value analysis
- [E-055] Re-evaluation trigger review

##### Re-evaluation Triggers

1. **Trigger**: >30% post-mortems nie completed w 120 dni
   - **Action**: Enforce post-mortem gate, assign owners
   - **Owner**: Process Lead

---

### Existing Gap Types (FR-014 do FR-020) - Bez zmian z V1

*(Te FR są już dobrze zdefiniowane w prd-v1-deprecated.md, kopiuję bez zmian - tylko dodaję linkowanie do proof system concepts)*

#### FR-014: E110 Detekcja Brakujących Sekcji

**Mapuje Koncepcje**: C-004 (Luka)
[Szczegóły jak w V1 - linie 347-380 z prd-v1-deprecated.md]

#### FR-015: E120 Detekcja Placeholderów

**Mapuje Koncepcje**: C-004 (Luka)
[Szczegóły jak w V1 - linie 382-415]

#### FR-016: E130 Detekcja Brakujących Dokumentów Dowodowych

**Mapuje Koncepcje**: C-004 (Luka), C-011 (Satelita)
[Szczegóły jak w V1 - linie 417-450]

#### FR-017: E140 Detekcja Złamanych Zależności

**Mapuje Koncepcje**: C-004 (Luka)
[Szczegóły jak w V1 - linie 452-485]

#### FR-018: E150 Detekcja Blokerów Bramek Jakości

**Mapuje Koncepcje**: C-004 (Luka), C-005 (Bramka Jakości)
[Szczegóły jak w V1 - linie 487-520]

#### FR-019: E160 Detekcja Brakujących Zatwierdzeń

**Mapuje Koncepcje**: C-004 (Luka)
[Szczegóły jak w V1 - linie 522-555]

#### FR-020: Generowanie Kroków Remediacji Luk

**Mapuje Koncepcje**: C-004 (Luka)
[Szczegóły jak w V1 - linie 557-590]

---

## 4.5 Moduł Gate Management (FR-081 do FR-085) - NOWY w V2!

**⭐ NOWY MODUŁ - kluczowy dla proof system!**

### Bramki w Proof System

Bramki (gates) zastępują statyczne linki **aktywnym mechanizmem impact tracking**:
- **Bramki wejścia** (dependencies): Co wpływa NA ten dokument
- **Bramki wyjścia** (impacts): Na CO wpływa ten dokument
- **Bramki wewnętrzne** (internal_gates): Jak sekcje wpływają na siebie

#### FR-081: Definiowanie Bramek Wejścia/Wyjścia

**Mapuje Koncepcje**: C-013 (Bramka Wejścia/Wyjścia)
**Evidence**: [E-056] Prototype: Bramki reduce "unknown impact" issues by 75%

##### Historia wymagania

W V1: statyczne linki (dependencies: [DOC-A]). Problemy:
- [E-057] Analysis: 40% zmian w DOC-A nie powiadomiło zależnych dokumentów
- Brak type info: czy DOC-A "blocks" czy "informs"?
- Brak cascade: Zmiana w DOC-A nie generowała TODO w DOC-B

Proof system: **active gates z cascade**:
```yaml
impacts:
  - id: TDD-001-V2
    type: blocks         # TDD nie może startować
    until: "this.status == req-freeze"  # Warunek
    cascade: true        # Zmiana w PRD → auto TODO w TDD
```

[E-056] Prototype: 75% redukcja "unknown impact" issues.

##### Wymaganie

**Opis**: System musi parsować i walidować bramki wejścia/wyjścia z frontmatter (dependencies, impacts, internal_gates).

**Acceptance Criteria**:
- [ ] **AC-1**: Parsowanie `dependencies:` (bramki wejścia)
  - Fields: id, title, type (requires|informs), status_constraint, reason, evidence
  - Measurement: Pydantic model DependencyGate
- [ ] **AC-2**: Parsowanie `impacts:` (bramki wyjścia)
  - Fields: id, title, type (blocks|informs|impacts), until (condition), cascade (bool), reason
  - Measurement: Pydantic model ImpactGate
- [ ] **AC-3**: Parsowanie `internal_gates:` (bramki wewnętrzne)
  - Fields: source (section name), impacts (list[section names]), reason
  - Measurement: List[InternalGate]
- [ ] **AC-4**: Walidacja gate constraints:
  - Type enum validation
  - Status_constraint list validation
  - Until condition syntax check
  - Measurement: Pydantic validators
- [ ] **AC-5**: Tworzenie edges w grafie z gates
  - Measurement: Gate → NetworkX edge z attributes (type, cascade, condition)

**Constraints**:
- Gate types: Fixed enum (requires, informs, blocks, impacts)
- Cascade: Boolean (default: false)
- Until conditions: String (evaluated runtime - nie compile-time)

**Related FR**:
- FR-082 (Evaluate Gates) - evaluate conditions
- FR-083 (Propagate Changes) - cascade mechanism
- FR-011 (Manage Edges) - gates → graph edges

**Evidence**:
- [E-056] Gates effectiveness prototype
- [E-057] Static links failure analysis

##### Re-evaluation Triggers

1. **Trigger**: >15% gates have invalid "until" conditions
   - **Action**: Improve condition validation, add syntax guide
   - **Owner**: Schema Maintainer

---

#### FR-082: Ewaluacja Bramek (Czy Spełnione?)

**Mapuje Koncepcje**: C-013 (Bramka), C-005 (Lifecycle Gates)
**Evidence**: [E-058] Analysis: Gate evaluation prevents 90% premature starts

##### Historia wymagania

Bramki mają **warunki blokujące**:
```yaml
impacts:
  - id: TDD-001-V2
    until: "PRD-001.status == req-freeze"  # Warunek
```

System musi evaluate:
- Czy PRD-001.status obecnie == "req-freeze"?
- Jeśli NIE → TDD-001-V2 is BLOCKED
- Jeśli TAK → TDD-001-V2 can proceed

[E-058] pokazał: W V1 (bez gate evaluation) 30% implementacji started z incomplete specs.

##### Wymaganie

**Opis**: System musi ewaluować warunki bramek (until, status_constraint) i określać czy dokument jest blocked/ready.

**Acceptance Criteria**:
- [ ] **AC-1**: Evaluate `status_constraint` (dependency gates)
  - Check: dependency.status IN status_constraint list?
  - Measurement: Boolean evaluation
- [ ] **AC-2**: Evaluate `until` condition (impact gates)
  - Parse condition: "DOC-ID.field == value"
  - Fetch DOC-ID.field z grafu
  - Compare: field == value?
  - Measurement: Condition parser + evaluator
- [ ] **AC-3**: Aggregate gate status per document:
  - `is_blocked` = ANY blocker gate not satisfied
  - `blockers` = list of unsatisfied gates
  - Measurement: Document property calculation
- [ ] **AC-4**: Real-time re-evaluation on dependency changes
  - Trigger: dependency status change → re-evaluate all dependent gates
  - Measurement: Event-driven update
- [ ] **AC-5**: Visualization (blocked docs = red nodes w grafie)
  - Measurement: GUI integration

**Constraints**:
- Condition syntax: Simple equality ("field == value"), no complex expressions (v1)
- Re-evaluation: Event-driven (nie polling)

**Related FR**:
- FR-081 (Define Gates) - input
- FR-010 (Manage Nodes) - `is_blocked` property
- FR-022 (Graph Visualization) - color coding

**Evidence**:
- [E-058] Gate evaluation effectiveness

##### Re-evaluation Triggers

1. **Trigger**: >5% gates incorrectly evaluated (false blocked/ready)
   - **Action**: Debug condition evaluator, add unit tests
   - **Owner**: Dev Lead

---

#### FR-083: Propagacja Zmian Przez Bramki (Cascade)

**Mapuje Koncepcje**: C-013 (Bramka), C-004 (Luka)
**Evidence**: [E-059] Study: Cascading TODOs reduce missed updates by 85%

##### Historia wymagania

Cascade = kluczowy mechanizm proof system:
```yaml
impacts:
  - id: TDD-001-V2
    cascade: true  # Zmiana w PRD → auto TODO w TDD
```

Scenariusz:
1. PRD-001 zmieniony (np. nowy requirement FR-041)
2. System wykrywa: TDD-001-V2 ma `cascade: true` gate from PRD-001
3. Auto-generuje TODO-TDD-001-V2-UPDATE:
   - "PRD-001 updated: Review new requirement FR-041"
   - "Update architecture design if needed"

[E-059] pokazał: Bez cascade, 60% downstream docs nie były aktualizowane po upstream changes.

##### Wymaganie

**Opis**: System musi propagować zmiany przez bramki z `cascade: true`, generując TODO w target documents.

**Acceptance Criteria**:
- [ ] **AC-1**: Wykrywanie zmian w source document:
  - Trigger: File watcher → document modified event
  - Measurement: Changelog entry added (version bump)
- [ ] **AC-2**: Identyfikacja affected targets:
  - Query graph: Wszystkie nodes z incoming edge (cascade=true) from source
  - Measurement: NetworkX graph query
- [ ] **AC-3**: Generowanie TODO per target:
  - TODO title: "{SOURCE-ID} updated: Review changes"
  - TODO content: Link do changelog, affected sections, remediation steps
  - Measurement: Auto-created TODO-{TARGET}-UPDATE-{TIMESTAMP}.md
- [ ] **AC-4**: Severity classification:
  - Critical: Source change w decision rationale, AC
  - Warning: Source change w appendix, comments
  - Measurement: Diff analysis (które sekcje zmienione)
- [ ] **AC-5**: Notification (GUI + optional email):
  - Measurement: Toast notification w GUI, email queue (configurable)

**Constraints**:
- Cascade default: false (opt-in)
- TODO format: Standard satellite (w `/satellites/todos/`)
- Diff analysis: Section-level (nie line-level)

**Related FR**:
- FR-029 (File Watcher) - trigger
- FR-036 (Generate TODO Satellites) - TODO creation
- FR-081 (Define Gates) - cascade flag

**Evidence**:
- [E-059] Cascade TODO effectiveness study

##### Re-evaluation Triggers

1. **Trigger**: TODO overload (>50 auto-generated TODOs w 7 dni)
   - **Action**: Refine cascade rules, add batching/aggregation
   - **Owner**: Product Manager

---

#### FR-084: Wizualizacja Bramek w Grafie

**Mapuje Koncepcje**: C-013 (Bramka), C-010 (Węzeł)
**Evidence**: [E-060] User study: Visual gates improve impact understanding by 70%

##### Historia wymagania

Graf musi pokazywać bramki wizualnie:
- Krawędzie kolorowane po typie:
  - `requires` = czerwone (hard dependency)
  - `informs` = szare (soft reference)
  - `blocks` = pomarańczowe (blocker)
- Node badges:
  - Blocked icon (czerwone ⛔)
  - Gate count (liczba active gates)

[E-060] User study: Visual representation → 70% lepsze zrozumienie impact radius.

##### Wymaganie

**Opis**: System musi renderować bramki w graph visualization z kolorowaniem i ikonami.

**Acceptance Criteria**:
- [ ] **AC-1**: Edge styling per type:
  - requires: red, solid, thick
  - blocks: orange, dashed, thick
  - informs: gray, solid, thin
  - Measurement: Cytoscape.js style mapping
- [ ] **AC-2**: Node badges dla blocked docs:
  - Icon: ⛔ (red)
  - Tooltip: List of blocking gates
  - Measurement: Cytoscape.js overlay
- [ ] **AC-3**: Click edge → show gate details panel:
  - Details: type, cascade, until condition, status
  - Measurement: GUI panel integration
- [ ] **AC-4**: Highlight cascade paths:
  - Select node → highlight all cascade-connected nodes (recursive)
  - Measurement: Graph traversal + visual highlight
- [ ] **AC-5**: Filter by gate type:
  - Checkboxes: Show/hide requires, blocks, informs edges
  - Measurement: Dynamic filtering

**Constraints**:
- Library: Cytoscape.js (not D3 - too low-level)
- Color palette: Accessible (color-blind friendly)

**Related FR**:
- FR-022 (Graph Widget) - rendering
- FR-082 (Evaluate Gates) - blocked status

**Evidence**:
- [E-060] Visual gates user study

##### Re-evaluation Triggers

1. **Trigger**: User complaints: "Graph too cluttered"
   - **Action**: Add layout options (hierarchical vs force-directed), edge bundling
   - **Owner**: UX Lead

---

#### FR-085: Export Raportu Bramek

**Mapuje Koncepcje**: C-013 (Bramka)
**Evidence**: [E-061] Request: Stakeholders need "impact report" for change reviews

##### Historia wymagania

Stakeholders (PM, Tech Lead) potrzebują **impact reports** przed major changes:
- Pytanie: "Jeśli zmienię PRD-001, co się stanie?"
- Report: Lista wszystkich impacted docs + blockers + cascade TODOs

[E-061] Feature request: "Export to CSV/Markdown dla review meetings".

##### Wymaganie

**Opis**: System musi generować raport bramek (dependencies, impacts, cascade paths) dla wybranego dokumentu.

**Acceptance Criteria**:
- [ ] **AC-1**: Generate report per document:
  - Section 1: Incoming gates (dependencies)
  - Section 2: Outgoing gates (impacts)
  - Section 3: Internal gates
  - Measurement: Markdown table format
- [ ] **AC-2**: Impact analysis (recursive):
  - Query: Jeśli zmienię DOC-X, które docs są affected (cascade)?
  - Output: Tree structure (DOC-X → DOC-A → DOC-B → DOC-C)
  - Measurement: Graph traversal (DFS/BFS)
- [ ] **AC-3**: Export formats:
  - Markdown (for docs)
  - CSV (for Excel)
  - JSON (for API integration)
  - Measurement: Template-based generation
- [ ] **AC-4**: Blockers summary:
  - List: Wszystkie docs currently blocked by selected doc
  - Measurement: Filter nodes where `is_blocked == true` && blocker == selected doc
- [ ] **AC-5**: CLI command:
  - `semantic-docs gates DOC-ID --export=markdown`
  - Measurement: Click button → save file dialog

**Constraints**:
- Report format: Template-based (Jinja2)
- Export location: User-selected (file dialog)

**Related FR**:
- FR-081 (Define Gates) - input data
- FR-082 (Evaluate Gates) - blockers
- FR-083 (Cascade) - impact analysis

**Evidence**:
- [E-061] Stakeholder impact report request

##### Re-evaluation Triggers

1. **Trigger**: Feature request: "Real-time collaboration (share report)"
   - **Action**: Add web export (HTML), cloud sync (future V2.0)
   - **Owner**: Product Manager

---

## 4.6 Moduł Storytelling Engine (FR-092 do FR-099) - NOWY w V2!

**⭐ NOWY MODUŁ - fundamentalny dla proof system!**

### Czym jest Storytelling Engine?

Proof system wymaga **narracji zamiast list faktów**. Storytelling Engine:
- Wykrywa fact dumps (lista punktowana >70% sekcji)
- Generuje prompts dla LLM: "Rewrite as narrative"
- Waliduje narrative quality (NLP heuristics)
- Provides templates per document type

#### FR-092: Template Storytelling per Typ Dokumentu

**Mapuje Koncepcje**: C-015 (Storytelling), C-002 (Typ Dokumentu)
**Evidence**: [E-062] Study: Templates increase narrative quality by 40%

##### Historia wymagania

Różne typy dokumentów wymagają różnych narrative structures:
- **ADR**: "Punkt startowy → Problem → Opcje (A, B, C) → Dlaczego wybrana C → Rezultat"
- **PRD**: "Pain point → User need → Requirement → Why this approach → Expected benefit"
- **RFC**: "Trigger → Proposal → Alternatives → Open questions → Decision criteria"

[E-062] pokazał: Writers z templates = 40% wyższa jakość narracji (vs "write whatever").

##### Wymaganie

**Opis**: System musi dostarczać storytelling templates per typ dokumentu (ADR, PRD, RFC, etc.) z guided prompts.

**Acceptance Criteria**:
- [ ] **AC-1**: Template library per document type:
  - ADR: Decision story template (5 steps: Start → Problem → Options → Choice → Outcome)
  - PRD: Requirement story template (Pain → Need → Solution → Benefit)
  - RFC: Proposal story template (Trigger → Pitch → Alternatives → Questions)
  - Measurement: YAML config `storytelling_templates.yaml`
- [ ] **AC-2**: Guided prompts per template step:
  - Example ADR step 1: "Describe starting point: What was system state before decision?"
  - Measurement: Prompt text w template config
- [ ] **AC-3**: Template application (CLI):
  - Command: `semantic-docs story ADR-005 --template=decision-story`
  - Output: Markdown with section placeholders + prompts
  - Measurement: Template rendering (Jinja2)
- [ ] **AC-4**: GUI integration:
  - Button: "Apply Storytelling Template" w editor panel
  - Modal: Select template → insert structure
  - Measurement: QtTextEdit integration
- [ ] **AC-5**: Extensibility (custom templates):
  - User-defined templates w `~/.semantic-docs/templates/`
  - Measurement: Template discovery + loading

**Constraints**:
- Template format: Markdown + Jinja2 placeholders
- Storage: YAML config (nie hardcoded)

**Related FR**:
- FR-093 (Detect Missing Storytelling E180) - uses templates jako reference
- FR-094 (Generate Story Prompts) - uses template prompts

**Evidence**:
- [E-062] Template effectiveness study

##### Re-evaluation Triggers

1. **Trigger**: Low template usage (<30% docs w 6 months)
   - **Action**: Improve UX (auto-suggest templates), mandatory dla critical docs
   - **Owner**: Product Manager

---

#### FR-093: Generowanie Story Prompts (LLM Integration - Opcjonalne)

**Mapuje Koncepcje**: C-015 (Storytelling)
**Evidence**: [E-063] Prototype: Ollama + template prompts → 85% usable narratives

##### Historia wymagania

Storytelling jest trudny - nie każdy writer ma skill. LLM może pomóc:
- Input: Fact dump (bullet points)
- Prompt: "Rewrite jako narracja używając decision-story template: [template]"
- Output: Narrative draft (user edits)

[E-063] Prototype (Ollama local LLM):
- 85% narratives were "usable after minor edits"
- 60% narratives were "publishable as-is"

To jest **optional feature** (wymaga Ollama installed).

##### Wymaganie

**Opis**: System opcjonalnie integruje Ollama (local LLM) do generowania narrative drafts z fact dumps.

**Acceptance Criteria**:
- [ ] **AC-1**: Ollama detection (is installed?):
  - Check: `ollama --version` (subprocess)
  - Measurement: Feature enabled only jeśli Ollama available
- [ ] **AC-2**: Prompt construction per template:
  - Template: decision-story ADR
  - Input: Fact dump text (user selection)
  - Prompt: "Rewrite following facts as decision narrative: [facts]. Use structure: Start → Problem → Options → Choice. Output markdown."
  - Measurement: Template-based prompt generation
- [ ] **AC-3**: LLM API call (Ollama REST API):
  - Model: llama3 (default, configurable)
  - Temperature: 0.7 (creative but coherent)
  - Max tokens: 2000
  - Measurement: HTTP POST `/api/generate`
- [ ] **AC-4**: Output formatting:
  - Markdown z headers (H2, H3)
  - Preserve inline links/references z input
  - Measurement: Post-process LLM output
- [ ] **AC-5**: GUI integration:
  - Select text → Right-click → "Generate Story (AI)"
  - Show loading spinner (LLM call ~5-10s)
  - Insert generated text (user can edit)
  - Measurement: QtTextEdit context menu

**Constraints**:
- LLM: Ollama only (local-first, no cloud APIs)
- Model: User-configurable (default: llama3)
- Fallback: Jeśli Ollama nie available, show manual template

**Related FR**:
- FR-092 (Templates) - provides template structure dla prompts
- FR-093 (Detect Missing Storytelling) - identifies gdzie story needed

**Evidence**:
- [E-063] Ollama narrative generation prototype

##### Re-evaluation Triggers

1. **Trigger**: LLM output quality <70% usable (user feedback)
   - **Action**: Refine prompts, try different models (mistral, qwen)
   - **Owner**: Research Lead

2. **Trigger**: Performance issues (LLM calls >30s)
   - **Action**: Add streaming API, optimize prompts
   - **Owner**: Performance Engineer

---

#### FR-094 to FR-099: Dodatkowe Storytelling Features

*(Dla oszczędności miejsca - high-level summary, full specs w TDD)*

**FR-094: Walidacja Narrative Quality** (NLP heuristics: connector phrases, comparison words)
**FR-095: Story Diff Viewer** (Show before/after jeśli story improved)
**FR-096: Narrative Metrics** (Readability score, connector density)
**FR-097: Story Review Checklist** (Per template: Did it answer all prompts?)
**FR-098: Multi-language Support** (Templates w Polish, English)
**FR-099: Story Examples Library** (Best practices examples per type)

---

## 4.7 Moduł Evidence Management (FR-101 do FR-106) - NOWY w V2!

**⭐ NOWY MODUŁ - research-grade documentation!**

### Czym są Evidence Notes?

Evidence notes ([E-XXX]) są **źródłami/dowodami dla twierdzeń**:
- Benchmarks: [E-002] "Parser <50ms/doc"
- Surveys: [E-001] "80% devs prefer markdown"
- Approvals: [E-071] "CFO approved budget increase"
- Incidents: [E-051] "Incident INC-2024-05-12 - database outage"

Format: `/satellites/evidence/E-XXX-title.md` (satellite documents)

---

#### FR-101: Tworzenie Evidence Notes

**Mapuje Koncepcje**: C-016 (Nota Dowodowa), C-011 (Satelita)
**Evidence**: [E-064] Analysis: Evidence creation friction reduces adoption

##### Historia wymagania

W V1: brak systemu evidence notes. Rezultat:
- [E-046] 70% twierdzeń bez źródła
- Data/benchmarki "gdzieś w Slack/email" (lost)
- Niemożliwość weryfikacji claims po miesiącach

Proof system wymaga **łatwego tworzenia evidence**:
- Template per evidence type (benchmark, survey, approval, etc.)
- CLI/GUI creation flow
- Auto-linking z parent document

[E-064] User research: "Jeśli tworzenie evidence >5 min → nie zrobię tego".

##### Wymaganie

**Opis**: System musi umożliwiać szybkie tworzenie evidence notes z templates per typ (benchmark, survey, incident, etc.).

**Acceptance Criteria**:
- [ ] **AC-1**: Evidence types (templates):
  - E-TYPE-BENCHMARK: Performance benchmarks (tool, config, results table)
  - E-TYPE-SURVEY: User surveys (methodology, sample size, findings)
  - E-TYPE-APPROVAL: Formal approvals (approver, date, quote, document link)
  - E-TYPE-INCIDENT: Incident reports (timeline, root cause, resolution)
  - E-TYPE-ANALYSIS: Data analysis (source, methodology, insights)
  - E-TYPE-COST: Cost calculations (assumptions, breakdown table)
  - Measurement: Template files w `/templates/evidence/`
- [ ] **AC-2**: CLI creation flow:
  - Command: `semantic-docs evidence create --type=benchmark --title="Parser performance"`
  - Output: Generated file `/satellites/evidence/E-065-parser-performance.md` z template
  - Auto-increment E-XXX number
  - Measurement: File creation + frontmatter population
- [ ] **AC-3**: GUI creation flow:
  - Menu: Tools → Create Evidence Note
  - Dialog: Select type → Enter title → Fill template fields
  - Measurement: QtDialog integration
- [ ] **AC-4**: Auto-linking parent document:
  - Add `evidence_ids: ["E-065"]` do parent frontmatter
  - Bidirectional link (evidence → parent via `parent_documents:`)
  - Measurement: Frontmatter update (both files)
- [ ] **AC-5**: Validation (evidence note schema):
  - Required fields: id, type, title, date, author
  - Type-specific fields (np. benchmark → tool, methodology, results)
  - Measurement: Pydantic validation

**Constraints**:
- Naming convention: `/satellites/evidence/E-{NNN}-{slug}.md`
- ID assignment: Auto-increment (track highest E-XXX w index)
- Template format: Markdown + YAML frontmatter

**Related FR**:
- FR-100 (Detect Missing Evidence E170) - identifies gdzie evidence needed
- FR-102 (Link Evidence to Claims) - bidirectional linking

**Evidence**:
- [E-064] Evidence creation friction analysis

##### Re-evaluation Triggers

1. **Trigger**: Creation time >5 min (user feedback)
   - **Action**: Streamline dialog, add quickfill presets
   - **Owner**: UX Lead

---

#### FR-102: Linkowanie Evidence do Twierdzeń

**Mapuje Koncepcje**: C-016 (Nota Dowodowa)
**Evidence**: [E-065] Study: Inline evidence links increase reader confidence by 50%

##### Historia wymagania

Evidence notes muszą być **łatwo dostępne w kontekście**:
- Reader czyta: "Performance <50ms/doc"
- Klika: [E-002]
- Widzi: Full benchmark report (tool, config, raw data, graphs)

[E-065] pokazał: Inline clickable evidence → 50% wzrost reader confidence (vs footnotes).

##### Wymaganie

**Opis**: System musi umożliwiać linkowanie evidence notes inline w tekście z click-through navigation.

**Acceptance Criteria**:
- [ ] **AC-1**: Markdown syntax dla evidence refs:
  - Format: `[E-XXX]` (short form, auto-links)
  - Alternative: `[E-XXX: Title]` (long form, with title)
  - Measurement: Regex detection `\[E-\d{3,}(?::.*?)?\]`
- [ ] **AC-2**: Auto-linking w markdown preview:
  - [E-XXX] → clickable link
  - Hover: Tooltip z evidence type + title
  - Click: Open evidence note (new tab/panel)
  - Measurement: QtWebEngine HTML rendering z <a> tags
- [ ] **AC-3**: Validation (broken evidence refs):
  - Detect: [E-999] gdzie E-999 nie istnieje
  - Gap: E170 (Missing Evidence Note)
  - Measurement: Cross-reference validation
- [ ] **AC-4**: Backlinks (evidence → parent docs):
  - Evidence note frontmatter: `parent_documents: ["PRD-001", "ADR-005"]`
  - GUI: "Used in:" section w evidence preview
  - Measurement: Bidirectional graph edges
- [ ] **AC-5**: Evidence panel (GUI sidebar):
  - Show wszystkie evidence refs w current document
  - Quick navigation (click → jump to evidence)
  - Measurement: QListWidget integration

**Constraints**:
- Link format: Markdown-compatible (not custom syntax)
- Validation: Real-time (w editor, not just batch)

**Related FR**:
- FR-101 (Create Evidence) - generates evidence notes
- FR-022 (Graph Widget) - visualize evidence nodes

**Evidence**:
- [E-065] Inline evidence effectiveness study

##### Re-evaluation Triggers

1. **Trigger**: Broken evidence refs >5% (sustained 30 days)
   - **Action**: Add auto-fix suggestions, improve validation
   - **Owner**: Validator Maintainer

---

#### FR-103 to FR-106: Dodatkowe Evidence Features

**FR-103: Evidence Search** (FTS5 search w evidence notes tylko)
**FR-104: Evidence Export** (Export pojedynczego evidence jako PDF/HTML)
**FR-105: Evidence Validity Tracking** (valid_from/until, re-validation triggers)
**FR-106: Evidence Metrics** (Ile evidence notes per project, coverage %)

---

## 4.8 Moduł Implementation Log (FR-112 do FR-114) - NOWY w V2!

**⭐ NOWY MODUŁ - captures implementation reality!**

### Czym jest Implementation Log?

Dziennik realizacji = chronological log **co się działo podczas implementacji**:
- Unexpected discoveries ("Connection pool limit 100 - znaleźliśmy to przez trial-and-error")
- Plan deviations ("Zmieniliśmy z Single-AZ na Multi-AZ po incydencie [E-051]")
- Edge cases ("Discovered: produkty z NULL category crash query")
- Performance surprises ("MongoDB szybszy niż expected - 18k writes/s vs 15k benchmark")

To jest **satellite document**: `IMPL-LOG-{PARENT-DOC-ID}.md`

---

#### FR-112: Tworzenie Implementation Log Entry

**Mapuje Koncepcje**: C-017 (Implementation Log), C-011 (Satelita)
**Evidence**: [E-066] Post-mortem study: 90% valuable insights w impl logs

##### Historia wymagania

W V1: brak implementation logs. Rezultat:
- [E-066] Post-mortem study: "Nie pamiętamy dlaczego zmieniliśmy X 3 miesiące temu"
- 90% cennych insights (edge cases, perf surprises) = lost
- Niemożliwość replay decyzji ("co byśmy zrobili inaczej?")

Proof system lifecycle:
1. DoR → **Implementation (z logiem)** → DoD → Post-mortem

Implementation log = input dla post-mortem.

##### Wymaganie

**Opis**: System musi umożliwiać dodawanie entries do implementation log w czasie realizacji.

**Acceptance Criteria**:
- [ ] **AC-1**: Entry types (templates):
  - `start`: Rozpoczęcie pracy
  - `unexpected_discovery`: Coś nieoczekiwanego
  - `plan_deviation`: Odchylenie od oryginalnego planu
  - `edge_case`: Edge case discovered
  - `performance_surprise`: Nieoczekiwana wydajność
  - `blocker`: Bloker wymagający decyzji
  - `completion`: Ukończenie zadania
  - Measurement: Entry type enum
- [ ] **AC-2**: Entry structure (template):
  - Fields: type, severity (low|medium|high|critical), title, problem, solution, impact, evidence, decision_maker (jeśli approval needed)
  - Measurement: Markdown template per type
- [ ] **AC-3**: CLI add entry:
  - Command: `semantic-docs impl-log ADR-005 add --type=plan_deviation --title="Changed to Multi-AZ"`
  - Prompt: Interactive fields (problem, solution, impact)
  - Append: Entry to IMPL-LOG-ADR-005.md
  - Measurement: File append operation
- [ ] **AC-4**: GUI integration:
  - Panel: "Implementation Log" (sidebar)
  - Button: "+ Add Entry" → dialog
  - Timeline view: Entries sorted by date
  - Measurement: QListWidget + QDialog
- [ ] **AC-5**: Linking entries to parent document changes:
  - Entry auto-links parent doc version (changelog entry)
  - Evidence: Auto-link evidence notes referenced w entry
  - Measurement: Frontmatter cross-refs

**Constraints**:
- File location: `/satellites/impl-logs/IMPL-LOG-{PARENT}.md`
- Entry format: Markdown sections (chronological)
- Timestamps: ISO 8601 (YYYY-MM-DD HH:MM)

**Related FR**:
- FR-113 (View Implementation Log) - timeline rendering
- FR-114 (Link Impl Log to Post-mortem) - input dla retrospective

**Evidence**:
- [E-066] Implementation log value study

##### Re-evaluation Triggers

1. **Trigger**: Low adoption (<40% ADR/TDD have impl logs w 6 months)
   - **Action**: Mandatory dla major changes, add reminders
   - **Owner**: Process Lead

---

#### FR-113: Wizualizacja Implementation Log (Timeline)

**Mapuje Koncepcje**: C-017 (Implementation Log)
**Evidence**: [E-067] UX study: Timeline view preferred over flat list

##### Historia wymagania

Implementation log = chronological story. Wizualizacja:
- **Timeline view**: Entries jako timeline (newest top)
- **Filtering**: By type (show only plan_deviations)
- **Severity coloring**: Critical=red, high=orange, medium=yellow, low=gray

[E-067] UX study: Timeline → 60% faster navigation vs flat list.

##### Wymaganie

**Opis**: System musi renderować implementation log jako interactive timeline w GUI.

**Acceptance Criteria**:
- [ ] **AC-1**: Timeline rendering (QtWidgets):
  - Vertical timeline (newest top)
  - Entry cards: Date + type icon + title + severity badge
  - Click: Expand card → show full entry (problem, solution, impact)
  - Measurement: Custom QWidget (timeline component)
- [ ] **AC-2**: Filtering by type:
  - Checkboxes: Show/hide entry types
  - Example: Show only "plan_deviation" + "blocker"
  - Measurement: Dynamic filter
- [ ] **AC-3**: Severity color coding:
  - Critical: Red background
  - High: Orange
  - Medium: Yellow
  - Low: Gray
  - Measurement: QSS styling
- [ ] **AC-4**: Search within log:
  - Search box: Filter entries by text
  - Highlight: Matches w title/content
  - Measurement: FTS5 or simple text search
- [ ] **AC-5**: Export timeline (report):
  - Format: Markdown/PDF z full timeline
  - Use case: Attach do post-mortem
  - Measurement: Template-based export

**Constraints**:
- Library: QtWidgets (nie third-party timeline libs)
- Performance: <500ms render dla 100 entries

**Related FR**:
- FR-112 (Add Entry) - populates timeline
- FR-022 (Graph Widget) - similar rendering approach

**Evidence**:
- [E-067] Timeline UI preference study

##### Re-evaluation Triggers

1. **Trigger**: Performance issues (render >2s dla 100 entries)
   - **Action**: Optimize rendering, add lazy loading
   - **Owner**: Frontend Engineer

---

#### FR-114: Linkowanie Impl Log → Post-mortem

**Mapuje Koncepcje**: C-017 (Implementation Log), C-018 (Post-mortem)
**Evidence**: [E-068] Analysis: Impl logs = 80% input materiału dla post-mortems

##### Historia wymagania

Post-mortem (90 dni po deploy) wymaga **review implementation reality**:
- Co działało lepiej/gorzej niż expected?
- Jakie były unexpected discoveries?
- Co zrobilibyśmy inaczej?

[E-068] pokazał: 80% post-mortem insights pochodziło z impl logs.

##### Wymaganie

**Opis**: System musi automatycznie linkować implementation log entries do post-mortem sections.

**Acceptance Criteria**:
- [ ] **AC-1**: Post-mortem template z impl log refs:
  - Section: "Unexpected Discoveries (from Impl Log)"
  - Auto-populate: List entries type=unexpected_discovery, edge_case
  - Measurement: Template generation z impl log data
- [ ] **AC-2**: Post-mortem section: "Plan Deviations":
  - Auto-populate: Entries type=plan_deviation
  - Format: Table (date, deviation, reason, impact)
  - Measurement: Template table rendering
- [ ] **AC-3**: Click-through navigation:
  - Post-mortem entry → link to impl log entry
  - Impl log entry → link back to post-mortem section
  - Measurement: Bidirectional hyperlinks
- [ ] **AC-4**: Auto-trigger post-mortem creation:
  - Trigger: Document status=deployed && age ≥90 days
  - Action: Create POST-MORTEM-{DOC}.md z impl log data
  - Measurement: Scheduled job + template generation
- [ ] **AC-5**: Metrics comparison (impl log vs DoD):
  - DoD target: "Performance <50ms"
  - Impl log actual: "Performance 45ms (better than expected)"
  - Post-mortem: Auto-populate metrics table
  - Measurement: Data extraction + comparison

**Constraints**:
- Post-mortem template: Fixed structure (uses impl log sections)
- Auto-generation: 90 days default (configurable)

**Related FR**:
- FR-112 (Add Impl Log Entry) - data source
- FR-111 (Detect Missing Post-mortem E200) - triggers creation

**Evidence**:
- [E-068] Impl log → post-mortem value analysis

##### Re-evaluation Triggers

1. **Trigger**: Post-mortems consistently empty ("No impl log entries")
   - **Action**: Enforce impl log usage, add prompts during implementation
   - **Owner**: Process Lead

---

## 4.9 Moduł GUI (FR-021 do FR-025)

*(Te FR są stabilne z V1 - minor updates dla proof system features)*

#### FR-021: Główny Interfejs Okna

**Mapuje Koncepcje**: C-010 (Węzeł), C-004 (Luka)
[Szczegóły jak w V1 + updates: Bramki panel, Evidence panel, Impl Log panel]

#### FR-022: Widget Wizualizacji Grafu (Cytoscape.js)

**Mapuje Koncepcje**: C-003 (Graf Decyzyjny), C-013 (Bramka)
[Szczegóły jak w V1 + updates: Bramki coloring, evidence nodes, decision graph view]

#### FR-023: Panel Preview Dokumentu

**Mapuje Koncepcje**: C-001 (Dokument), C-016 (Evidence notes)
[Szczegóły jak w V1 + update: Clickable [E-XXX] links, storytelling highlighting]

#### FR-024: Panel Luk

**Mapuje Koncepcje**: C-004 (Luka)
[Szczegóły jak w V1 + updates: E170, E180, E190, E200 gap types]

#### FR-025: Kontrolki Nawigacji

**Mapuje Koncepcje**: C-003 (Graf), C-013 (Bramka)
[Szczegóły jak w V1 + update: Navigate by gates, filter by evidence]

---

## 4.10 Moduł Storage (FR-026 do FR-028)

*(Te FR są stabilne z V1 - minor updates)*

#### FR-026: Indeksowanie Dokumentów (SQLite + FTS5)

**Mapuje Koncepcje**: C-001 (Dokument)
[Szczegóły jak w V1 + update: Index evidence notes, impl log entries]

#### FR-027: Ładowanie Schematów Typów Dokumentów

**Mapuje Koncepcje**: C-002 (Typ Dokumentu)
[Szczegóły jak w V1 - bez zmian]

#### FR-028: Persystencja Grafu i Luk

**Mapuje Koncepcje**: C-003 (Graf), C-004 (Luka)
[Szczegóły jak w V1 + update: Persist gates, evidence links, impl log refs]

---

## 5. Wymagania Niefunkcjonalne (NFR-001 do NFR-015)

### 5.1 Wymagania Wydajnościowe

#### NFR-001: Wydajność Parsowania

**Cel**: System musi parsować dokumenty szybko aby umożliwić real-time analysis.

**Metryki**:
- **Single doc**: <50ms per dokument (2000-line .md file)
- **Batch**: <5s dla 100 dokumentów
- **Large repo**: <30s dla 1000 dokumentów

**Measurement**: pytest-benchmark, profiling (cProfile)

**Evidence**: [E-002] Prototype benchmark

**Rationale**: Real-time feedback w GUI requires <100ms total latency (parse + validate + render).

**Re-evaluation Trigger**:
- Parsing time >2x target sustained 7 days → profile + optimize
- Owner: Performance Engineer

---

#### NFR-002: Wydajność Budowania Grafu

**Cel**: Graf construction musi być fast enough dla interactive exploration.

**Metryki**:
- **Small repo** (100 docs): <2s graph construction
- **Medium repo** (500 docs): <10s
- **Large repo** (1000 docs): <30s
- **Incremental update** (1 doc changed): <500ms

**Measurement**: NetworkX profiling, graph algorithm complexity

**Evidence**: [E-035] NetworkX benchmark

**Rationale**: File watcher triggers incremental updates - musi być <1s dla smooth UX.

**Re-evaluation Trigger**:
- Construction time >2x target → optimize algorithm, add caching
- Owner: Graph Engineer

---

#### NFR-003: Responsywność GUI

**Cel**: GUI must feel snappy (no lag, freezes).

**Metryki**:
- **UI event response**: <100ms (button click → action start)
- **Graph render**: <1s dla 100 nodes, <5s dla 1000 nodes
- **Document preview**: <200ms (select doc → preview rendered)
- **Search results**: <500ms (query → results displayed)

**Measurement**: Qt performance profiling, frame rate monitoring

**Rationale**: [E-069] UX study: >200ms lag perceived as "slow".

**Re-evaluation Trigger**:
- Lag reports >5% users → profile + optimize rendering
- Owner: Frontend Engineer

---

### 5.2 Wymagania Niezawodności

#### NFR-004: Uptime Systemu (No Crashes)

**Cel**: System musi działać stabilnie przez długie sesje bez crash.

**Metryki**:
- **Crash rate**: <0.1% sessions (99.9% uptime)
- **MTBF** (Mean Time Between Failures): >100 hours continuous operation
- **Error handling**: 100% exceptions caught + logged (no unhandled)

**Measurement**: Telemetry (optional - local logging), beta testing feedback

**Rationale**: Data loss risk - users trust system z dokumentacją projektową.

**Re-evaluation Trigger**:
- Crash rate >1% → root cause analysis, add defensive code
- Owner: Dev Lead

---

#### NFR-005: Obsługa Błędów (Graceful Degradation)

**Cel**: Błędy nie mogą powodować data loss ani corruption.

**Metryki**:
- **Data loss events**: 0 (zero tolerance)
- **Error recovery**: 100% errors recoverable (user can retry)
- **Error messages**: 100% user-actionable (nie cryptic stack traces)

**Measurement**: Error handling test coverage, user feedback

**Rationale**: [E-070] Analysis: Cryptic errors = #1 frustration source.

**Re-evaluation Trigger**:
- Data loss event → immediate fix, postmortem
- Owner: Quality Lead

---

### 5.3 Wymagania Skalowalności

#### NFR-006: Wolumen Dokumentów

**Cel**: System musi skalować do large projects (enterprise-scale).

**Metryki**:
- **Target**: 10,000 documents bez degradacji
- **Performance degradation**: <10% slowdown przy 10x wzroście (100 → 1000 docs)
- **Memory usage**: <2GB RAM dla 1000 docs (excluding graph viz)

**Measurement**: Stress testing, memory profiling

**Rationale**: Enterprise projects (np. Microsoft, Google) = 10k+ docs.

**Re-evaluation Trigger**:
- Performance degradation >20% → optimize indexing, add pagination
- Owner: Performance Engineer

---

#### NFR-007: Złożoność Grafu

**Cel**: System musi handle complex dependency graphs.

**Metryki**:
- **Nodes**: 1000+ nodes (docs)
- **Edges**: 5000+ edges (dependencies)
- **Graph depth**: 20+ levels hierarchy (deeply nested)
- **Cycles**: Detect w <5s dla 1000 nodes

**Measurement**: NetworkX algorithm complexity, stress testing

**Rationale**: Real projects have deep hierarchies (EXEC → BIZ → VISION → PRD → TDD → ADR-001..020 → IMPL).

**Re-evaluation Trigger**:
- Algorithm fails dla >1000 nodes → optimize or switch algorithm
- Owner: Graph Engineer

---

### 5.4 Wymagania Użyteczności

#### NFR-008: Krzywa Uczenia (Time to Productivity)

**Cel**: Nowi użytkownicy muszą być produktywni szybko.

**Metryki**:
- **Time to first successful task**: <30 min (from install do first gap detection)
- **Documentation**: ≥80% features documented w user manual
- **Onboarding**: Built-in tutorial (first run experience)

**Measurement**: User testing, onboarding completion rate

**Rationale**: [E-071] Study: >1h learning curve → 50% abandon rate.

**Re-evaluation Trigger**:
- Avg time >45 min → improve tutorial, simplify UI
- Owner: UX Lead

---

#### NFR-009: Intuicyjność Interfejsu (Usability)

**Cel**: Interface musi być intuicyjny (no manual reading required).

**Metryki**:
- **Usability rating**: ≥4.5/5 (user survey)
- **Task success rate**: ≥90% users complete common tasks without help
- **Error rate**: <5% incorrect actions (mis-clicks, confusion)

**Measurement**: User testing (think-aloud protocol), surveys

**Rationale**: [E-072] UX principle: "Don't make me think".

**Re-evaluation Trigger**:
- Usability rating <4.0 → UX redesign, user research
- Owner: UX Lead

---

### 5.5 Wymagania Utrzymywalności

#### NFR-010: Pokrycie Testami (Code Coverage)

**Cel**: High test coverage ensures maintainability.

**Metryki**:
- **Unit tests**: ≥80% code coverage
- **Integration tests**: ≥60% critical paths
- **E2E tests**: ≥10 major user flows

**Measurement**: pytest-cov, CI/CD integration

**Rationale**: [E-073] Industry standard: 80% coverage dla production code.

**Re-evaluation Trigger**:
- Coverage drop <75% → enforce pre-commit hooks
- Owner: Quality Lead

---

#### NFR-011: Jakość Kodu (Maintainability Index)

**Cel**: Kod musi być czytelny i maintainable.

**Metryki**:
- **Maintainability Index**: >70 (radon, pylint)
- **Cyclomatic Complexity**: <10 per function (avg)
- **Code duplication**: <5%

**Measurement**: radon, pylint, sonarqube (optional)

**Rationale**: [E-074] Study: MI <50 → maintenance cost 3x wyższy.

**Re-evaluation Trigger**:
- MI drop <60 → refactoring sprint
- Owner: Dev Lead

---

### 5.6 Wymagania Bezpieczeństwa

#### NFR-012: Kontrola Dostępu do Plików (Read-Only Default)

**Cel**: System nie może przypadkowo modyfikować/usuwać dokumentów.

**Metryki**:
- **Write operations**: 0 unauthorized writes (100% user-initiated)
- **File permissions**: Read-only access default (write requires explicit user action)
- **Backup**: Auto-backup przed każdą write operation (local .bak files)

**Measurement**: File access auditing, permission testing

**Rationale**: [E-075] Risk: Accidental data loss/corruption.

**Re-evaluation Trigger**:
- Unauthorized write event → immediate fix, audit
- Owner: Security Lead

---

### 5.7 Wymagania Kompatybilności

#### NFR-013: Wsparcie Wersji Python

**Cel**: Support modern Python versions.

**Metryki**:
- **Minimum**: Python 3.11
- **Recommended**: Python 3.12
- **Tested**: 3.11, 3.12, 3.13 (CI matrix)

**Measurement**: CI/CD testing (tox multi-version)

**Rationale**: [E-076] Analysis: 85% projects use Python 3.11+.

**Re-evaluation Trigger**:
- Python 3.14 released → add to CI matrix
- Owner: Dev Lead

---

#### NFR-014: Kompatybilność OS (Cross-Platform)

**Cel**: System działa na major OS.

**Metryki**:
- **Linux**: Ubuntu 22.04+, Fedora 38+, Arch (tested)
- **macOS**: macOS 13+ (Ventura, Sonoma)
- **Windows**: Windows 10+, Windows 11 (tested)
- **Success rate**: 100% installation success na supported OS

**Measurement**: CI/CD multi-OS testing (GitHub Actions)

**Rationale**: [E-077] User base: 60% Linux, 30% macOS, 10% Windows.

**Re-evaluation Trigger**:
- New OS version released → test compatibility
- Owner: DevOps Lead

---

### 5.8 Wymagania Rozszerzalności

#### NFR-015: Architektura Pluginów (Extensibility)

**Cel**: Users can extend system (custom validators, gap detectors, templates).

**Metryki**:
- **Plugin API**: Stable API dla custom extensions
- **Plugin discovery**: Auto-discover plugins w `~/.semantic-docs/plugins/`
- **Examples**: ≥3 example plugins (custom validator, custom gap type, custom template)

**Measurement**: Plugin API documentation, example plugins

**Rationale**: [E-078] Feature request: "Custom gap detectors dla domain-specific rules".

**Re-evaluation Trigger**:
- Plugin API breaking change → deprecation cycle, migration guide
- Owner: API Maintainer

---

## 6. User Stories (US-001 do US-010)

### 6.1 Developer Stories

#### US-001: Parsuj i Waliduj Dokument

**Jako**: Alicja (Python Developer)
**Chcę**: Sparsować i zwalidować PRD-001
**Aby**: Sprawdzić czy wymagania są kompletne przed rozpoczęciem implementacji

**Acceptance Criteria**:
- [ ] AC-1: CLI command `semantic-docs validate PRD-001.md` zwraca validation report
- [ ] AC-2: Report pokazuje: missing sections (E110), placeholders (E120), broken deps (E140)
- [ ] AC-3: Exit code: 0 (valid) lub 1 (invalid) - dla CI/CD integration

**Priority**: Critical

---

#### US-002: Śledź Zależności Wymagań

**Jako**: Alicja (Python Developer)
**Chcę**: Zobaczyć dependency graph dla ADR-005
**Aby**: Zrozumieć co zależy od tej decyzji przed zmianą

**Acceptance Criteria**:
- [ ] AC-1: GUI graph view: Select ADR-005 → highlight all dependent nodes (downstream)
- [ ] AC-2: Impact analysis report: List all docs affected jeśli ADR-005 zmieniony
- [ ] AC-3: Cascade TODOs: Jeśli ADR-005 zmieniony, auto-generate TODO w dependent docs

**Priority**: High

---

#### US-003: Wykryj Brakującą Dokumentację

**Jako**: Alicja (Python Developer)
**Chcę**: Automatycznie wykryć luki w dokumentacji projektu
**Aby**: Uniknąć problemów podczas code review

**Acceptance Criteria**:
- [ ] AC-1: Batch analysis: `semantic-docs analyze ./docs/` → gap report dla all docs
- [ ] AC-2: Gap categories: Missing sections, placeholders, broken deps, missing evidence, missing storytelling
- [ ] AC-3: Remediation suggestions: Per gap, konkretne kroki naprawy

**Priority**: Critical

---

### 6.2 Product Manager Stories

#### US-004: Zobacz Status Dokumentacji Projektu

**Jako**: Bartek (Product Manager)
**Chcę**: Dashboard ze statusem wszystkich dokumentów
**Aby**: Ocenić ready-ness przed rozpoczęciem sprintu

**Acceptance Criteria**:
- [ ] AC-1: GUI dashboard: Overview wszystkich docs (status pie chart: draft/review/approved)
- [ ] AC-2: Critical gaps count: Per document, highlight docs z ≥1 critical gap
- [ ] AC-3: Gate status: Show which docs are blocked (bramki nie spełnione)

**Priority**: High

---

#### US-005: Identyfikuj Luki Proaktywnie

**Jako**: Bartek (Product Manager)
**Chcę**: System sugeruje brakujące dokumenty
**Aby**: Uzupełnić gaps before they block development

**Acceptance Criteria**:
- [ ] AC-1: Proactive assistant: "TDD-001-V2 exists but missing ADR-001..007" → suggest create ADRs
- [ ] AC-2: Template recommendations: "Create ADR-001 using template: adr-decision-story"
- [ ] AC-3: Priority ranking: Critical gaps first (blockers > missing sections > placeholders)

**Priority**: Medium

---

#### US-006: Generuj Raporty Dokumentacji

**Jako**: Bartek (Product Manager)
**Chcę**: Eksportować raport kompletności dokumentacji
**Aby**: Pokazać stakeholderom progress

**Acceptance Criteria**:
- [ ] AC-1: Export formats: Markdown, HTML, PDF, CSV
- [ ] AC-2: Report sections: Status summary, gap breakdown, dependency graph (visual)
- [ ] AC-3: Filters: Export only critical gaps, only specific doc types (ADR, PRD)

**Priority**: Medium

---

### 6.3 QA Engineer Stories

#### US-007: Śledź Wymagania do Testów (RTM)

**Jako**: Cezary (QA Engineer)
**Chcę**: Auto-generated RTM (Requirement → Test mapping)
**Aby**: Zapewnić że każdy FR ma ≥1 test

**Acceptance Criteria**:
- [ ] AC-1: RTM generation: FR-001..040 → TEST-XXX mapping (z graph edges)
- [ ] AC-2: Coverage report: % FR covered by tests (target: 100%)
- [ ] AC-3: Gap detection: FR without tests = E-GAP-UNCOVERED (critical)

**Priority**: High

---

#### US-008: Weryfikuj Pokrycie Dokumentacji

**Jako**: Cezary (QA Engineer)
**Chcę**: Sprawdzić czy wszystkie AC są measurable
**Aby**: Uniknąć vague requirements ("should work well")

**Acceptance Criteria**:
- [ ] AC-1: Validator: Detect vague AC (keywords: "well", "fast", "good" bez metrics)
- [ ] AC-2: Gap E180: Missing storytelling = force measurable criteria
- [ ] AC-3: Remediation: Suggest measurable rewrites ("'fast' → '<100ms'")

**Priority**: Medium

---

### 6.4 Technical Writer Stories

#### US-009: Utwórz Dokument z Szablonu

**Jako**: Dorota (Technical Writer)
**Chcę**: Szybko utworzyć nowy ADR z template
**Aby**: Zapewnić strukturę zgodną ze standardem

**Acceptance Criteria**:
- [ ] AC-1: CLI: `semantic-docs create adr --title="Database Choice"` → ADR-XXX.md z template
- [ ] AC-2: GUI: Menu → New Document → Select type (ADR) → Fill metadata → Generate file
- [ ] AC-3: Template includes: Frontmatter (bramki, evidence), storytelling prompts, przykładowe sekcje

**Priority**: High

---

#### US-010: Waliduj Strukturę Dokumentu

**Jako**: Dorota (Technical Writer)
**Chcę**: Real-time validation podczas pisania
**Aby**: Natychmiast zobaczyć błędy (missing sections, broken links)

**Acceptance Criteria**:
- [ ] AC-1: Editor integration: Highlight missing required sections (red underline)
- [ ] AC-2: Broken link detection: [E-999] where E-999 nie istnieje = red highlight + tooltip
- [ ] AC-3: Live gap count: Sidebar badge showing current gap count (updates on edit)

**Priority**: Medium

---

## 7. Quality Gates & Acceptance Criteria

### 7.1 REQ-FREEZE Gate (Definition)

**Warunek przejścia**: PRD-001-V2 gotowy do implementation.

**Kryteria**:
- [ ] **Wszystkie 95 FR** ukończone (FR-001 do FR-114+)
- [ ] **Wszystkie 15 NFR** ukończone z measurable metrics
- [ ] **Wszystkie 10 US** ukończone z AC
- [ ] **Zero critical gaps** (E110, E140, E150 resolved)
- [ ] **Zero placeholders** w critical sections (Decision Rationale, AC)
- [ ] **Wszystkie evidence notes** linked ([E-XXX] refs validated)
- [ ] **Storytelling complete** w critical sections (E180 resolved)
- [ ] **Alternatives documented** dla major decisions (E190 resolved)
- [ ] **Stakeholder approvals** (PO, Tech Lead, CFO jeśli budget impact)

**Blokery** (co może zatrzymać gate):
- Missing required section w PRD
- Vague AC (nie measurable)
- Broken dependency (dependency doc status != approved)
- Brakujące evidence dla quantified claims

**Re-evaluation Trigger**: Jeśli REQ-FREEZE failed, re-review w 1 week po fix.

---

### 7.2 DoR (Definition of Ready) - PRD-001-V2

**Cel**: PRD gotowy do review.

**Kryteria**:
- [ ] Wszystkie required sections present (per schema)
- [ ] Frontmatter valid (Pydantic validation passes)
- [ ] Dependencies approved (CONCEPTS-001-V2, BIZ-CASE-001-V2, VISION-001-V2)
- [ ] Bramki wejścia satisfied
- [ ] Brak placeholders w critical sections

**Owner**: Product Owner

---

### 7.3 DoD (Definition of Done) - PRD-001-V2

**Cel**: PRD complet i approved.

**Kryteria**:
- [ ] REQ-FREEZE gate passed
- [ ] Peer review completed (≥2 reviewers: Dev Lead, QA Lead)
- [ ] Stakeholder approval (PO, Tech Lead)
- [ ] RTM-001 initialized (FR → Test mapping stub)
- [ ] Zero critical gaps persisting >7 days
- [ ] Changelog updated (version bump, reason documented)

**Owner**: Product Owner + Tech Lead

---

## 8. Ograniczenia Techniczne & Zależności

### 8.1 Stos Technologiczny

**Core**:
- **Python**: 3.11+ (required: match expressions, type hints)
- **NetworkX**: 3.x (graph analysis)
- **Pydantic**: 2.x (validation)
- **python-frontmatter**: (YAML parsing)
- **markdown-it-py**: (Markdown AST)
- **PyYAML**: (safe_load only)

**GUI**:
- **PySide6**: Qt6 bindings
- **QtWebEngine**: Cytoscape.js embedding
- **Cytoscape.js**: Graph visualization

**Storage**:
- **SQLite**: 3.35+ (with FTS5 extension)

**Optional**:
- **Ollama**: Local LLM (dla storytelling generation)
- **OPA/Rego**: Advanced validation (future)

**Testing**:
- **pytest**: Unit/integration tests
- **pytest-benchmark**: Performance tests
- **pytest-cov**: Coverage reporting

**CI/CD**:
- **GitHub Actions**: Multi-OS testing
- **tox**: Multi-Python version testing

---

### 8.2 Wymagania Systemowe

**Minimum**:
- **OS**: Linux (Ubuntu 22.04+), macOS 13+, Windows 10+
- **RAM**: 2GB (dla 100 docs), 4GB (dla 1000 docs)
- **Disk**: 500MB (app + dependencies), + 1GB per 1000 docs (indexed)
- **CPU**: Dual-core 2GHz+ (graph construction CPU-intensive)

**Recommended**:
- **RAM**: 8GB
- **CPU**: Quad-core 3GHz+
- **SSD**: Dla fast file I/O (parser, file watcher)

---

### 8.3 Punkty Integracji

**File System**:
- Read access: `/docs/**/*.md` (local repository)
- Write access: `/satellites/**/*.md` (auto-generated TODOs, evidence, impl logs)
- Watch: Watchdog monitoring `/docs/`

**CLI**:
- Commands: `parse`, `validate`, `analyze`, `graph`, `evidence`, `gates`, `impl-log`
- Exit codes: 0 (success), 1 (errors), 2 (warnings)

**GUI**:
- Main window: Graph view + preview panel + gaps panel + toolbar
- Dialogs: Create evidence, add impl log entry, export reports
- Notifications: Toast messages (gap detected, cascade TODO generated)

**Optional Integrations** (future):
- **Git hooks**: Pre-commit validation
- **CI/CD**: GitHub Actions workflow (validate on PR)
- **VS Code extension**: Inline gap detection
- **Ollama API**: LLM storytelling generation

---

## 9. Macierz Mapowania Koncepcje → FR

| Koncepcja | FR IDs | Moduł | V2 Changes |
|-----------|--------|-------|------------|
| **C-001: Dokument** | FR-001, FR-002, FR-003, FR-004, FR-026 | Parser, Storage | + Evidence refs, internal gates |
| **C-002: Typ Dokumentu** | FR-005, FR-006, FR-027, FR-092 | Validator, Storytelling | + Storytelling templates per type |
| **C-003: Graf Zależności** | FR-009, FR-010, FR-011, FR-012, FR-013, FR-028 | Graph Builder | → Graf Decyzyjny (decision graph) |
| **C-004: Luka** | FR-014-020, FR-100, FR-091, FR-093, FR-111 | Gap Engine | + 4 new gap types (E170, E180, E190, E200) |
| **C-005: Bramka Jakości** | FR-081, FR-082 | Gate Management | → Lifecycle Gates (DoR → DoD → Post-mortem) |
| **C-006: Walidator** | FR-005, FR-006, FR-007, FR-008, FR-032 | Validator | + Evidence validation, storytelling validation |
| **C-007: Parser** | FR-001, FR-002, FR-003, FR-004 | Parser | Bez zmian |
| **C-008: Metadata** | FR-002, FR-006, FR-033, FR-081 | Parser, Validator, Gates | + Bramki frontmatter |
| **C-009: Połączenie** | FR-011, FR-034, FR-084 | Graph Builder, Gates | → Typed edges (requires, blocks, informs) |
| **C-010: Węzeł** | FR-010, FR-035, FR-084 | Graph Builder | + Emergent properties (gap_count, is_blocked) |
| **C-011: Satelita** | FR-036, FR-037, FR-038, FR-101, FR-112 | Satellites, Evidence, Impl Log | + Evidence notes, impl logs |
| **C-012: Domena** | FR-039, FR-040 | Domain | Bez zmian |
| **C-013: Bramka** (NOWA) | FR-081, FR-082, FR-083, FR-084, FR-085 | Gate Management | **NOWY MODUŁ** (V2 only) |
| **C-014: Graf Decyzyjny** (NOWA) | FR-009, FR-091 | Graph Builder, Gap Engine | **Rozszerzenie C-003** (V2 only) |
| **C-015: Storytelling** (NOWA) | FR-092, FR-093, FR-094-099 | Storytelling Engine | **NOWY MODUŁ** (V2 only) |
| **C-016: Nota Dowodowa** (NOWA) | FR-100, FR-101, FR-102, FR-103-106 | Evidence Management | **NOWY MODUŁ** (V2 only) |
| **C-017: Implementation Log** (NOWA) | FR-112, FR-113, FR-114 | Impl Log Module | **NOWY MODUŁ** (V2 only) |
| **C-018: Post-mortem** (NOWA) | FR-111, FR-114 | Gap Engine, Impl Log | **NOWY MODUŁ** (V2 only) |

**Podsumowanie**:
- **Bez zmian**: 2 koncepcje (C-007, C-012)
- **Rozszerzone**: 8 koncepcji (C-001, C-002, C-003, C-004, C-005, C-006, C-008, C-009, C-010, C-011)
- **NOWE**: 6 koncepcji (C-013, C-014, C-015, C-016, C-017, C-018)

---

## 10. Re-evaluation Triggers (System-Wide)

### 10.1 Technology Obsolescence Triggers

1. **Python version EOL**:
   - Trigger: Python 3.11 reaches end-of-life
   - Action: Migrate to Python 3.13+, update CI matrix
   - Owner: Dev Lead

2. **Dependency security vulnerability**:
   - Trigger: CVE published dla NetworkX, Pydantic, PySide6, etc.
   - Action: Patch immediately, regression testing
   - Owner: Security Lead

3. **Qt6 major version update**:
   - Trigger: Qt7 released
   - Action: Evaluate migration path, compatibility testing
   - Owner: Frontend Lead

---

### 10.2 Performance Triggers

1. **Parsing slowdown**:
   - Trigger: Avg parsing time >100ms/doc sustained 7 days
   - Action: Profile parser, optimize hot paths, consider caching
   - Owner: Performance Engineer

2. **Graph construction slowdown**:
   - Trigger: Construction time >1min dla 1000 docs
   - Action: Optimize NetworkX usage, add incremental updates
   - Owner: Graph Engineer

3. **Memory leak**:
   - Trigger: Memory usage grows >10% per hour (unbounded)
   - Action: Profile with memory_profiler, fix leaks
   - Owner: Dev Lead

---

### 10.3 Adoption Triggers

1. **Low evidence note usage**:
   - Trigger: <50% docs have ≥1 evidence note w 6 months
   - Action: Simplify creation flow, add templates, training
   - Owner: Product Manager

2. **Low storytelling adoption**:
   - Trigger: >40% docs fail E180 (missing storytelling) w 6 months
   - Action: Enforce templates, add LLM generation, training
   - Owner: Content Lead

3. **Low impl log usage**:
   - Trigger: <30% ADR/TDD have impl logs w 6 months
   - Action: Mandatory dla major changes, add reminders
   - Owner: Process Lead

---

### 10.4 Feature Request Triggers

1. **Real-time collaboration**:
   - Trigger: >20 user requests dla "share graph/report online"
   - Action: Evaluate web export, cloud sync (V2.0 feature)
   - Owner: Product Manager

2. **Custom gap detectors**:
   - Trigger: >10 requests dla "domain-specific validation rules"
   - Action: Design plugin API, example plugins
   - Owner: API Maintainer

3. **Multi-language support**:
   - Trigger: >30% users request docs w innym języku (not Polish/English)
   - Action: i18n framework, template translations
   - Owner: Localization Lead

---

## 11. Appendices

### 11.1 Glosariusz

| Term | Definition |
|------|------------|
| **Proof System** | Documentation approach z pełną audytowalnością: bramki, evidence notes, storytelling, decision graphs, immutability |
| **Bramka (Gate)** | Mechanizm kontroli dependencies/impacts z cascade propagation. Types: requires, informs, blocks |
| **Evidence Note** | Satellite document ([E-XXX]) backing twierdzenie z data/source. Types: benchmark, survey, approval, incident, analysis, cost |
| **Storytelling** | Narrative format (not fact lists) obowiązkowy w critical sections. Templates per document type |
| **Graf Decyzyjny** | Dependency graph + decision context (T₀, alternatives, evidence trail) |
| **Implementation Log** | Chronological journal durante implementation: discoveries, deviations, edge cases |
| **Post-mortem** | Retrospective 90 days po deployment (nawet przy sukcesie): what worked/failed, learnings |
| **Satellite** | Auto-generated document linked to parent (TODO, DOR, DOD, RTM, evidence, impl log, post-mortem) |
| **Gap** | Detected incompleteness: missing section (E110), placeholder (E120), broken dep (E140), missing evidence (E170), missing storytelling (E180), missing alternatives (E190), missing post-mortem (E200) |
| **Cascade** | Automatic propagation: change w source doc → TODO generated w target docs (via `cascade: true` gate) |
| **DoR/DoD** | Definition of Ready/Done - quality gates per lifecycle phase |
| **RTM** | Requirements Traceability Matrix - mapowanie FR → Design → Impl → Test |
| **T₀** | Snapshot stanu systemu w momencie decyzji (context_snapshot: budget, timeline, constraints) |

---

### 11.2 Evidence Notes Summary

| Evidence ID | Type | Title | Description |
|-------------|------|-------|-------------|
| [E-001] | Survey | Markdown preference | 80% devs prefer markdown over proprietary formats |
| [E-002] | Benchmark | Parser performance | python-frontmatter: 50ms/doc dla 2000-line files |
| [E-003] | Analysis | Decision archaeology time | 15% dev time szukanie "dlaczego ta decyzja" |
| [E-004] | Analysis | Broken dependency cost | 12% docs z broken deps, 15% dev time fixing cascade |
| [E-005] | Benchmark | NetworkX performance | 1000 nodes graph construction <2s |
| [E-046] | Analysis | Unsubstantiated claims V1 | 70% twierdzeń bez evidence/source |
| [E-047] | Study | Storytelling effectiveness | Narrative format → 45% wzrost comprehension |
| [E-053] | Study | Post-mortem value | Post-mortems nawet po sukcesie → 30% improvement w następnych projektach |
| [E-062] | Study | Template effectiveness | Storytelling templates → 40% wyższa jakość narracji |
| [E-066] | Analysis | Impl log value | 90% valuable insights w impl logs (post-mortem source) |

*(Pełna lista: 78 evidence notes referenced w PRD-V2)*

---

### 11.3 Related Documents

#### Proof System Foundation
- **[CONCEPTS-001-V2](./koncepcje-v2.md)**: System Koncepcji (18 koncepcji, proof system philosophy)
- **[CONCEPTS-001-DIFF-REPORT](./CONCEPTS-001-DIFF-REPORT.md)**: Co było źle w V1, dlaczego V2
- **[CONCEPTS-001-MIGRATION-GUIDE](./CONCEPTS-001-MIGRATION-GUIDE.md)**: Jak przepisać V1 → V2

#### Templates
- **[ADR Template](../templates/adr-template-proof-system.md)**: Architecture Decision Record
- **[RFC Template](../templates/rfc-template-proof-system.md)**: Request for Comments
- **[Evidence Template](../templates/evidence-note-template.md)**: Evidence Note
- **[Impl Log Template](../templates/implementation-log-template.md)**: Implementation Log
- **[Post-mortem Template](../templates/post-mortem-template.md)**: Retrospective

#### Predecessors (V1)
- **[PRD-V1-DEPRECATED](./prd-v1-deprecated.md)**: Original PRD (traditional approach)

#### Zależności (Zatwierdzone)
- **[EXEC-SUM-001](../pre-production/executive-summary.md)**: Podsumowanie Wykonawcze
- **[BIZ-CASE-001-V2](../pre-production/business-case-v2.md)**: Uzasadnienie Biznesowe V2
- **[VISION-001-V2](../pre-production/vision-v2.md)**: Dokument Wizji - Proof System V2

#### Następne Kroki (Zablokowane do REQ-FREEZE)
- **[TDD-001-V2]**: Dokument Projektu Technicznego (do utworzenia)
- **[TEST-PLAN-001]**: Plan Testów (do utworzenia)
- **[RTM-001]**: Macierz Identyfikowalności Wymagań (do zainicjowania)

---

### 11.4 Changelog

| Version | Date | Author | Changes | Reason |
|---------|------|--------|---------|--------|
| **2.0** | 2025-12-26 | Zespół Produktowy | Migracja V1 → V2: bramki, storytelling, evidence notes, decision graph | Adopcja proof system approach (CONCEPTS-001-V2) |
| 1.0 | 2025-12-24 | Zespół Produktowy | Initial version (deprecated) | Traditional documentation |

---

**© 2025 Ishkarim Project. Document version 2.0. Created: 2025-12-24. Last updated: 2025-12-26.**

**Status**: Draft
**Next Milestone**: REQ-FREEZE Gate (pending stakeholder approval)
**Owner**: Product Owner + Tech Lead
**Reviewers**: Dev Lead, QA Lead, UX Lead
