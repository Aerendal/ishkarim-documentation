---
# === Standardowe pola (istniejące) ===
id: DOC-PRD-015
doctype: PRD
status: evolving
version: "1.2.0"
owner: "Anna Kowalska"
project: "Ishkarim"
created: "2025-11-15"

# === NOWE: Status Metadata (Living Documentation) ===
status_metadata:
  previous_status: approved
  status_changed_date: "2025-12-20"
  status_reason: "Iteracyjne dopracowywanie na podstawie feedbacku z Sprint 5 - dodanie funkcji interaktywnego filtrowania grafu"
  next_review_date: "2026-01-15"

# === NOWE: Lifecycle Tracking ===
lifecycle:
  created: "2025-11-15"
  first_approved: "2025-12-01"
  last_modified: "2025-12-29"
  last_reviewed: "2025-12-29"
  sunset_date: null
  migration_target: null

# === NOWE: Version Metadata (Semantic Versioning) ===
version_metadata:
  major: 1       # Initial approved version
  minor: 2       # Non-breaking additions (interactive filters)
  patch: 0       # No patches yet
  breaking_changes: false
  backward_compatible_with: ["1.1.x", "1.0.x"]
  forward_compatible_with: []

version_history:
  - version: "1.2.0"
    date: "2025-12-20"
    author: "Anna Kowalska"
    type: "minor"
    summary: "Dodano interaktywne filtrowanie grafu zależności (FR-28, FR-29, FR-30)"
    breaking: false
    impacts:
      - id: DOC-TDD-015
        action: "Wymaga aktualizacji architektury - dodanie filtru w warstwie prezentacji"
      - id: DOC-TEST-PLAN-015
        action: "Wymaga nowych test cases dla funkcji filtrowania"

  - version: "1.1.0"
    date: "2025-12-10"
    author: "Anna Kowalska"
    type: "minor"
    summary: "Rozszerzono NFR - dodano wymagania performance dla grafów >500 węzłów"
    breaking: false
    impacts:
      - id: DOC-TDD-015
        action: "Review strategii renderowania dla dużych grafów"

  - version: "1.0.0"
    date: "2025-12-01"
    author: "Anna Kowalska"
    type: "major"
    summary: "Pierwsza zatwierdzona wersja PRD - wizualizacja grafu zależności dokumentów"
    breaking: false
    impacts:
      - id: DOC-TDD-015
        action: "Rozpoczęcie projektowania technicznego"
      - id: DOC-TEST-PLAN-015
        action: "Utworzenie test plan"

# === NOWE: Cross-Reference Status (Impact Propagation) ===
cross_reference_status:
  upstream_changes_pending:
    - id: DOC-BUSINESS-CASE-001
      changed_version: "2.3.0"
      changed_date: "2025-12-28"
      change_type: "minor"
      impact_severity: "low"
      action_required: "Review budżetu - zwiększono alokację na UI/UX o 15%"
      acknowledged: true
      acknowledged_by: "Anna Kowalska"
      acknowledged_date: "2025-12-29"
      acknowledgment_notes: "Przeanalizowano - bez wpływu na zakres PRD, budżet wystarczający"

  downstream_impacts_pending:
    - id: DOC-TDD-015
      notified_date: "2025-12-20"
      acknowledged: true
      acknowledged_by: "Piotr Wiśniewski (Tech Lead)"
      acknowledged_date: "2025-12-21"
    - id: DOC-TEST-PLAN-015
      notified_date: "2025-12-20"
      acknowledged: false

# === NOWE: Document Health ===
document_health:
  status: "healthy"
  last_health_check: "2025-12-29T08:30:00Z"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified_days_ago: 0
      threshold_days: 90
      message: "Dokument aktualny - ostatnia modyfikacja dzisiaj"

    - name: "Dependency Validity"
      status: "healthy"
      all_dependencies_valid: true
      total_dependencies: 3
      valid_dependencies: 3
      message: "Wszystkie zależności aktywne (BUSINESS_CASE, ROADMAP, MARKET_ANALYSIS)"

    - name: "Cross-Reference Consistency"
      status: "healthy"
      all_references_valid: true
      message: "Wszystkie cross-references spójne (TDD, TEST_PLAN mają backlinki)"

    - name: "Owner Assignment"
      status: "healthy"
      owner_active: true
      message: "Owner aktywny (Anna Kowalska)"

    - name: "Required Sections Completeness"
      status: "healthy"
      all_sections_present: true
      missing_sections: []
      message: "Wszystkie wymagane sekcje PRD kompletne"

    - name: "Upstream Changes Pending"
      status: "healthy"
      pending_changes: 0
      message: "Brak oczekujących zmian upstream (BUSINESS_CASE acknowledged)"

    - name: "Satellite Completeness"
      status: "healthy"
      missing_satellites: []
      message: "Wszystkie satelity obecne (TODO, DOR, DOD, APPROVAL, EVIDENCE, CHANGELOG)"

  overall_score: 98
  risk_level: "low"

# === NOWE: Deprecation (jeśli dotyczy) ===
deprecation: null

---

# PRD: Interaktywna Wizualizacja Grafu Zależności Dokumentów

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: DOC-BUSINESS-CASE-001
    type: requires
    reason: "PRD bazuje na business case - wizualizacja grafu zależności zwiększa produktywność użytkowników o 30%"
    min_status: approved
    current_version: "2.3.0"
    sections:
      - from: "§5 Wymagania funkcjonalne"
        to: "BUSINESS_CASE §3 ROI Analysis"
        influence: "ROI zakłada 30% redukcję czasu nawigacji po dokumentach dzięki grafowi"

  - id: DOC-ROADMAP-001
    type: requires
    reason: "Graf zależności jest kluczową funkcją w Roadmap Q1 2026"
    min_status: approved
    current_version: "1.5.0"
    sections:
      - from: "§1 Cel produktu"
        to: "ROADMAP §4 Q1 2026 Milestones"
        influence: "Graf jest milestone M3 w Q1 2026"

  - id: DOC-MARKET-ANALYSIS-001
    type: informs
    reason: "Market analysis pokazuje, że konkurencja ma podobną funkcję - musimy dorównać"
    current_version: "1.2.0"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: DOC-TDD-015
    type: blocks
    reason: "TDD wymaga zatwierdzonego PRD przed rozpoczęciem detailed design"
    sections:
      - from: "§5 Wymagania funkcjonalne"
        to: "TDD §3 Moduły / komponenty"
        influence: "Functional requirements definiują komponenty UI: GraphCanvas, NodeRenderer, EdgeRenderer"

  - id: DOC-TEST-PLAN-015
    type: blocks
    reason: "Test Plan wymaga acceptance criteria z PRD"
    sections:
      - from: "§6 Kryteria akceptacji"
        to: "TEST-PLAN §3 Test Cases"
        influence: "AC definiują test scenarios: graf renderuje <2s, obsługuje 1000+ węzłów, zoom działa płynnie"

  - id: DOC-USER-GUIDE-015
    type: influences
    reason: "User Guide dokumentuje funkcje opisane w PRD"
    sections:
      - from: "§5 Wymagania funkcjonalne"
        to: "USER-GUIDE §2 Graf Zależności"
        influence: "PRD definiuje user-facing features dla dokumentacji"
```

### Related Documents

```yaml
related:
  - id: DOC-ADR-045
    type: informs
    reason: "ADR-045 wybrał Cytoscape.js jako bibliotekę do wizualizacji grafu"

  - id: DOC-EVIDENCE-143
    type: informs
    reason: "E-143: Cytoscape performance benchmark - validacja, że Cytoscape obsługuje nasze wymagania"
```

### Satellite Documents

```yaml
satellites:
  - type: TODO_SECTION
    path: "satellites/todos/TODO-PRD-015.md"
    status: "in_progress"
    purpose: "Tracking outstanding tasks (§8 Interactive Filters - design finalization)"

  - type: DOR_DOC
    path: "satellites/dor/DOR-PRD-015.md"
    status: "done"
    purpose: "Definition of Ready - PRD spełnia kryteria gotowości do review"

  - type: DOD_DOC
    path: "satellites/dod/DOD-PRD-015.md"
    status: "done"
    purpose: "Definition of Done - PRD spełnia kryteria kompletności"

  - type: APPROVAL
    path: "satellites/approvals/APPROVAL-PRD-015.md"
    status: "approved"
    purpose: "Approval record - zatwierdzenie przez Product Owner, Tech Lead, Stakeholders"

  - type: EVIDENCE
    path: "satellites/evidence/EVIDENCE-PRD-015-INDEX.md"
    status: "done"
    purpose: "Evidence index linking to: E-143 (Cytoscape benchmark), E-144 (User interviews - graph needs)"

  - type: CHANGELOG
    path: "satellites/changelog/CHANGELOG-PRD-015.md"
    status: "active"
    purpose: "Version history with semantic versioning (currently v1.2.0)"
```

---

# 1. Cel Produktu

## 1.1. Problem / Opportunity

**Problem:**

Użytkownicy Ishkarim (tech writers, PMs, developers) tracą czas na **manualną nawigację po zależnościach dokumentów**:

- **Pain Point 1:** Trudno zrozumieć, które dokumenty są od siebie zależne
  - Przykład: "PRD wymaga zatwierdzonego BUSINESS_CASE" — ale która wersja? Jakie sekcje?
  - Efekt: Użytkownicy czytają nieprawidłowe wersje dokumentów, outdated dependencies

- **Pain Point 2:** Brak wizualizacji impact propagation
  - Przykład: "Zmienił się BUSINESS_CASE — które dokumenty muszę zaktualizować?"
  - Efekt: Missed updates, inconsistent documentation

- **Pain Point 3:** Dependency graph istnieje (w Mermaid), ale jest statyczny
  - Nie można filtrować (np. "pokaż tylko PRD i TDD")
  - Nie można zoomować (graf 148 dokumentów jest nieczytelny)
  - Nie można kliknąć węzła → przejść do dokumentu

**Dane (z Evidence E-144: User Interviews):**
- 78% użytkowników zgłosiło: "Trudno mi znaleźć powiązane dokumenty"
- Średni czas nawigacji: **12 minut/dzień** spędzone na szukaniu dependencies
- 45% użytkowników: "Nie wiedziałem, że dokument X zależy od Y — dowiedziałem się dopiero gdy coś się zepsuło"

**Opportunity:**

Interaktywna wizualizacja grafu zależności może **zredukować czas nawigacji o 70%** (12 min → 3.6 min/dzień) = **30% wzrost produktywności** w zarządzaniu dokumentacją.

**ROI (z BUSINESS_CASE-001):**
- Oszczędność czasu: 8.4 min/user/day × 20 users × 250 days = **700 godzin/rok**
- Cost savings: 700h × $50/h (średnia stawka) = **$35,000/rok**

---

## 1.2. Vision Statement

**Dla:** Tech writers, Product Managers, Developers pracujących z Ishkarim

**Którzy:** Potrzebują szybko zrozumieć zależności między dokumentami i śledzić impact propagation

**Ishkarim Graph Visualization jest:** Interaktywną wizualizacją grafu zależności dokumentów

**Która:** Umożliwia filtrowanie, zoom, klikanie węzłów, i real-time highlighting zmian upstream/downstream

**W przeciwieństwie do:** Statycznego grafu Mermaid w markdown files

**Nasz produkt:** Jest interaktywny, konfigurowalny, i zintegrowany z systemem Living Documentation (auto-update gdy dokumenty się zmieniają)

---

## 1.3. Success Metrics (KPIs)

| Metryka | Baseline (Teraz) | Target (Q2 2026) | Measurement |
|---------|------------------|------------------|-------------|
| **Czas nawigacji do powiązanego dokumentu** | 90 sec (manual search) | 20 sec (click node) | User analytics |
| **% użytkowników używających grafu** | 0% (brak funkcji) | >70% | Feature usage analytics |
| **Dokładność identyfikacji dependencies** | 60% (manual) | >95% (auto) | Survey + validation |
| **User satisfaction (NPS)** | 6.5 (obecny NPS Ishkarim) | >8.0 | Quarterly survey |
| **Redukcja czasu nawigacji** | Baseline | -70% | Time tracking |

---

# 2. Zakres (In/Out of Scope)

## 2.1. In Scope (MVP)

**Must Have (P0):**

✅ **Graf podstawowy:**
- Renderowanie grafu zależności dokumentów (wszystkie 148+ docs)
- Węzły: Dokumenty (DOC-ID jako label)
- Krawędzie: Dependencies (requires, influences, informs, blocks)
- Layout: Hierarchiczny (dependencies → documents → impacts)

✅ **Interakcje podstawowe:**
- Zoom (scroll wheel)
- Pan (drag canvas)
- Kliknięcie węzła → otwórz dokument (nowa karta)
- Hover węzła → tooltip (DOC-ID, title, status, version)

✅ **Performance:**
- Render time <2s dla grafów do 500 węzłów
- Smooth zoom/pan (60 FPS)

**Should Have (P1):**

✅ **Filtrowanie:**
- Filtr po doctype (np. "pokaż tylko PRD, TDD")
- Filtr po status (np. "pokaż tylko approved documents")
- Filtr po project (np. "pokaż tylko Project Alpha docs")

✅ **Highlighting:**
- Highlight upstream dependencies (czerwony) gdy wybrany węzeł
- Highlight downstream impacts (zielony) gdy wybrany węzeł

---

## 2.2. Out of Scope (MVP)

**Defer to V2 (Post-MVP):**

❌ **Edycja grafu:**
- Dodawanie nowych zależności przez drag&drop
- Usuwanie zależności
- **Rationale:** V1 = read-only visualization. V2 = edycja.

❌ **Real-time collaboration:**
- Multi-user cursors (jak Figma)
- **Rationale:** Nice-to-have, not critical for MVP

❌ **Advanced analytics:**
- Centrality analysis (które dokumenty są najbardziej critical)
- Cluster detection (grupy silnie powiązanych dokumentów)
- **Rationale:** Advanced use case, defer to V2

❌ **Export do formatu graficznego:**
- Export do PNG, SVG, PDF
- **Rationale:** Can screenshot for now, export in V2

---

## 2.3. Out of Scope (Forever)

**Never Planned:**

❌ **3D visualization:**
- Graf w 3D (WebGL)
- **Rationale:** Over-engineering, 2D wystarczy

❌ **Automatyczne layoutowanie custom:**
- User-defined layout positions (manual positioning węzłów)
- **Rationale:** Hierarchical layout działa dobrze, manual positioning = maintenance hell

---

# 3. Personas / Użytkownicy

## Persona 1: Tech Writer (Primary User)

**Imię:** Maria, 32 lata
**Rola:** Technical Writer w firmie software'owej (50+ employees)
**Doświadczenie:** 5 lat w tech writing, zna Markdown, Git, podstawy HTML/CSS

**Goals:**
- Szybko znaleźć powiązane dokumenty (TDD dla danego PRD)
- Zrozumieć, które dokumenty muszę zaktualizować gdy PRD się zmienia
- Uniknąć outdated references (linking do deprecated docs)

**Pain Points (Current):**
- "Spędzam 15 minut dziennie na szukaniu dependencies w Markdown files"
- "Nie wiem, które dokumenty są impacted gdy aktualizuję PRD"
- "Graf Mermaid jest nieczytelny (148 dokumentów = chaos)"

**How they'll use Graph Visualization:**
- **Use Case 1:** Klikam węzeł PRD-015 → widzę, że zależy od BUSINESS_CASE-001
- **Use Case 2:** Klikam węzeł PRD-015 → widzę downstream impacts (TDD-015, TEST-PLAN-015) highlighted green
- **Use Case 3:** Filtruję graf: "pokaż tylko PRD + TDD" → redukuję noise

**Frequency:** Daily (every time updating/reading docs)

---

## Persona 2: Product Manager (Secondary User)

**Imię:** Jan, 38 lat
**Rola:** Product Manager
**Doświadczenie:** 10 lat w PM, używa JIRA, Confluence, Notion

**Goals:**
- High-level overview dependencies (które projekty są od siebie zależne)
- Szybko zidentyfikować bottlenecks (critical documents blokujące wiele innych)
- Validate roadmap dependencies (czy ROADMAP-001 ma wszystkie required docs approved)

**Pain Points (Current):**
- "Nie widzę big picture — które dokumenty są critical path"
- "Trudno zwalidować readiness for gate (np. czy wszystkie deps dla GATE-REQ_FREEZE są approved)"

**How they'll use Graph Visualization:**
- **Use Case 1:** Zoom out → widzę cały graf projektu → identificuję bottlenecks (docs z wieloma incoming edges)
- **Use Case 2:** Filtruję po status "approved" → widzę, które docs są ready
- **Use Case 3:** Klikam węzeł ROADMAP → widzę czy wszystkie dependencies są approved (zielone) czy draft (czerwone)

**Frequency:** Weekly (during planning/review meetings)

---

## Persona 3: Developer (Tertiary User)

**Imię:** Piotr, 28 lat
**Rola:** Backend Developer
**Doświadczenie:** 4 lata w software development

**Goals:**
- Znaleźć TDD dla danej feature (aby zrozumieć implementation details)
- Sprawdzić, czy TDD jest up-to-date z PRD
- Zidentyfikować related ADRs (architecture decisions)

**Pain Points (Current):**
- "Nie wiem, które TDD odpowiada któremu PRD"
- "Czytam outdated TDD bo nie wiedziałem, że PRD się zmienił"

**How they'll use Graph Visualization:**
- **Use Case 1:** Klikam węzeł PRD-015 → widzę TDD-015 highlighted → klikam → otwieram TDD
- **Use Case 2:** Widzę, że TDD-015 ma status "evolving" (żółty węzeł) → wiem, że design się zmienia
- **Use Case 3:** Filtruję graf: "pokaż tylko TDD + ADR" → widzę architecture decisions dla danego TDD

**Frequency:** 2-3x per week (when starting new feature)

---

# 4. Wymagania Funkcjonalne

## FR-01: Renderowanie Grafu Zależności

**Priority:** P0 (Must Have)

**Opis:**
System renderuje interaktywny graf zależności dokumentów, gdzie:
- **Węzły** = Dokumenty (DOC-ID jako label, np. "PRD-015")
- **Krawędzie** = Zależności (requires, influences, informs, blocks)

**Acceptance Criteria:**
- AC-01: Graf renderuje wszystkie dokumenty z front-matter `id: DOC-*`
- AC-02: Krawędzie renderują zależności z `dependencies` section w front-matter
- AC-03: Layout jest hierarchiczny (dependencies → document → impacts, left-to-right lub top-to-bottom)
- AC-04: Węzły mają kolory według statusu:
  - 🟢 Green: approved
  - 🔵 Blue: in-review
  - 🟡 Yellow: evolving, validating, refining
  - 🔴 Red: deprecated, sunset
  - ⚪ Gray: draft, archived
- AC-05: Render time <2 sekundy dla grafów do 500 węzłów

**Input:** Front-matter YAML z `id`, `dependencies`, `status`
**Output:** Interaktywny graf w canvas (Cytoscape.js)

**Related:** ADR-045 (Cytoscape.js selection), E-143 (Cytoscape benchmark)

---

## FR-02: Zoom Grafu

**Priority:** P0 (Must Have)

**Opis:**
Użytkownik może zoomować graf używając scroll wheel lub pinch gesture (mobile/tablet).

**Acceptance Criteria:**
- AC-06: Scroll wheel up → zoom in (max 300%)
- AC-07: Scroll wheel down → zoom out (min 25%)
- AC-08: Zoom jest smooth (60 FPS, no stuttering)
- AC-09: Zoom centruje się na pozycji kursora (zoom "towards cursor")
- AC-10: Pinch gesture (touch devices) działa (zoom in/out)

**Input:** Scroll wheel event, pinch gesture event
**Output:** Graf zoomowany

---

## FR-03: Pan (Przesuwanie) Grafu

**Priority:** P0 (Must Have)

**Opis:**
Użytkownik może przesuwać graf (panning) używając drag gesture.

**Acceptance Criteria:**
- AC-11: Click + drag (mouse) → przesuwa graf
- AC-12: Touch + drag (mobile) → przesuwa graf
- AC-13: Panning jest smooth (60 FPS)
- AC-14: Cursor zmienia się na "grab" podczas drag

**Input:** Mouse drag event, touch drag event
**Output:** Graf przesunięty

---

## FR-04: Kliknięcie Węzła → Otwórz Dokument

**Priority:** P0 (Must Have)

**Opis:**
Użytkownik może kliknąć węzeł grafu → system otwiera dokument w nowej karcie.

**Acceptance Criteria:**
- AC-15: Click węzła → otwiera dokument (file path z front-matter)
- AC-16: Dokument otwiera się w nowej karcie (target="_blank")
- AC-17: Jeśli dokument nie istnieje (broken link) → pokazuje error message: "Dokument nie znaleziony: DOC-ID"

**Input:** Click event na węźle
**Output:** Nowa karta z dokumentem otwartym

---

## FR-05: Hover Węzła → Tooltip

**Priority:** P0 (Must Have)

**Opis:**
Gdy użytkownik najedzie kursorem na węzeł, system pokazuje tooltip z metadata.

**Acceptance Criteria:**
- AC-18: Hover węzła → pokazuje tooltip
- AC-19: Tooltip zawiera:
  - `id` (np. "DOC-PRD-015")
  - `title` (np. "Interaktywna Wizualizacja Grafu")
  - `doctype` (np. "PRD")
  - `status` (np. "evolving")
  - `version` (np. "1.2.0")
  - `owner` (np. "Anna Kowalska")
- AC-20: Tooltip pojawia się po 300ms delay (not instant)
- AC-21: Tooltip znika gdy cursor opuszcza węzeł

**Input:** Hover event na węźle
**Output:** Tooltip z metadata

---

## FR-06: Filtrowanie po Doctype

**Priority:** P1 (Should Have)

**Opis:**
Użytkownik może filtrować graf po typie dokumentu (doctype).

**Acceptance Criteria:**
- AC-22: UI ma multi-select dropdown "Filtruj po Doctype"
- AC-23: Opcje: PRD, TDD, BUSINESS_CASE, ADR, TEST_PLAN, ROADMAP, etc. (all doctypes)
- AC-24: Domyślnie: wszystkie zaznaczone (pokazuje wszystkie docs)
- AC-25: User odznacza "PRD" → węzły PRD znikają (fade out animation)
- AC-26: Krawędzie do ukrytych węzłów też znikają
- AC-27: Filtrowanie jest instant (<100ms response time)

**Input:** User selection w dropdown
**Output:** Graf z filtered nodes

---

## FR-07: Filtrowanie po Status

**Priority:** P1 (Should Have)

**Opis:**
Użytkownik może filtrować graf po statusie dokumentu.

**Acceptance Criteria:**
- AC-28: UI ma multi-select dropdown "Filtruj po Status"
- AC-29: Opcje: draft, in-review, approved, evolving, validating, refining, deprecated, sunset, archived, migrated
- AC-30: Domyślnie: approved, evolving, validating, refining zaznaczone (hide draft/archived by default)
- AC-31: User zaznacza tylko "approved" → pokazuje tylko approved docs
- AC-32: Filtrowanie działa z FR-06 (doctype filter) → można kombinować (np. "approved PRD only")

**Input:** User selection w dropdown
**Output:** Graf z filtered nodes

---

## FR-08: Filtrowanie po Project

**Priority:** P1 (Should Have)

**Opis:**
Użytkownik może filtrować graf po projekcie (project field w front-matter).

**Acceptance Criteria:**
- AC-33: UI ma multi-select dropdown "Filtruj po Project"
- AC-34: Opcje: dynamicznie loaded z front-matter `project` field (np. "Ishkarim", "Project Alpha", "Project Beta")
- AC-35: Domyślnie: wszystkie zaznaczone
- AC-36: User wybiera tylko "Ishkarim" → pokazuje tylko Ishkarim docs

**Input:** User selection w dropdown
**Output:** Graf z filtered nodes

---

## FR-09: Highlight Upstream Dependencies

**Priority:** P1 (Should Have)

**Opis:**
Gdy użytkownik kliknie węzeł, system highlightuje upstream dependencies (dokumenty, od których wybrany dokument zależy).

**Acceptance Criteria:**
- AC-37: Click węzła → upstream dependencies highlighted czerwonym
- AC-38: Upstream = dokumenty w `dependencies` section front-matter
- AC-39: Krawędzie do upstream też highlighted (thicker, red)
- AC-40: Pozostałe węzły dimmed (opacity 0.3)
- AC-41: Click background → unhighlight (powrót do normal view)

**Input:** Click event na węźle
**Output:** Graf z highlighted upstream

---

## FR-10: Highlight Downstream Impacts

**Priority:** P1 (Should Have)

**Opis:**
Gdy użytkownik kliknie węzeł, system highlightuje downstream impacts (dokumenty, które zależą od wybranego dokumentu).

**Acceptance Criteria:**
- AC-42: Click węzła → downstream impacts highlighted zielonym
- AC-43: Downstream = dokumenty które mają wybrany węzeł w `dependencies` section
- AC-44: Krawędzie od downstream też highlighted (thicker, green)
- AC-45: Upstream (FR-09) i downstream (FR-10) mogą być highlighted jednocześnie (czerwony + zielony)
- AC-46: Click background → unhighlight

**Input:** Click event na węźle
**Output:** Graf z highlighted downstream

---

# 5. Wymagania Niefunkcjonalne (NFRs)

## NFR-01: Performance — Render Time

**Priority:** P0 (Must Have)

**Requirement:**
Graf renderuje w <2 sekundy dla grafów do 500 węzłów.

**Rationale:**
User tolerance: 2s = acceptable, 5s+ = frustrating (per UX research)

**Measurement:**
- Load time = czas od kliknięcia "Show Graph" do fully rendered graph
- Measure w Chrome DevTools Performance tab

**Test Cases:**
- TC-01: 100 węzłów → render time <500ms
- TC-02: 250 węzłów → render time <1s
- TC-03: 500 węzłów → render time <2s

**Acceptance:**
- 95th percentile load time <2s (per Google Analytics)

---

## NFR-02: Performance — Zoom/Pan Smoothness

**Priority:** P0 (Must Have)

**Requirement:**
Zoom i pan działają przy 60 FPS (no stuttering, no lag).

**Rationale:**
60 FPS = płynna animacja (16.67ms per frame). <30 FPS = janky, poor UX.

**Measurement:**
- FPS counter w Chrome DevTools
- User testing (subjective smoothness rating)

**Test Cases:**
- TC-04: Zoom in/out (scroll wheel) → 60 FPS
- TC-05: Pan (drag) → 60 FPS

**Acceptance:**
- FPS ≥ 60 during zoom/pan (99% of time)

---

## NFR-03: Usability — Learnability

**Priority:** P1 (Should Have)

**Requirement:**
Nowi użytkownicy (first time) potrafią wykonać podstawowe operacje (zoom, pan, kliknięcie węzła) w <2 minuty bez instrukcji.

**Rationale:**
Graph visualization powinna być intuicyjna (convention: scroll = zoom, drag = pan, click = action)

**Measurement:**
- User testing: 5 nowych użytkowników (nie znają Ishkarim Graph)
- Czas do wykonania 3 tasków: zoom in, pan, kliknij węzeł

**Test Cases:**
- TC-06: User zoomuje graf (bez instrukcji) → average time <30s
- TC-07: User przesuwa graf (bez instrukcji) → average time <20s
- TC-08: User klika węzeł → otwiera dokument → average time <30s

**Acceptance:**
- 80% użytkowników wykonuje wszystkie 3 taski w <2 min total

---

## NFR-04: Accessibility — Keyboard Navigation

**Priority:** P2 (Could Have)

**Requirement:**
Graf jest dostępny via keyboard navigation (dla screen readers, accessibility).

**Rationale:**
WCAG 2.1 Level AA compliance — keyboard navigation required

**Features:**
- Tab → focus na węzłach (sequential)
- Enter → otwórz dokument (jak click)
- Arrow keys → pan canvas
- +/- keys → zoom in/out

**Measurement:**
- WCAG audit (automated tool: axe DevTools)
- Manual testing with screen reader (NVDA, JAWS)

**Acceptance:**
- All interactive elements keyboard accessible
- Screen reader announces node metadata (DOC-ID, title, status)

---

## NFR-05: Browser Compatibility

**Priority:** P0 (Must Have)

**Requirement:**
Graf działa na 95% przeglądarek (per usage stats).

**Supported Browsers:**
- ✅ Chrome 90+ (desktop + mobile)
- ✅ Firefox 88+ (desktop)
- ✅ Safari 14+ (desktop + iOS)
- ✅ Edge 90+ (desktop)

**Not Supported:**
- ❌ IE11 (deprecated, <1% usage)

**Measurement:**
- Cross-browser testing (BrowserStack)

**Acceptance:**
- Graf renderuje i działa (zoom, pan, click) na wszystkich supported browsers

---

## NFR-06: Responsive Design — Mobile Support

**Priority:** P1 (Should Have)

**Requirement:**
Graf jest responsive — działa na mobile (tablets, phones).

**Features:**
- Touch gestures: pinch to zoom, drag to pan, tap to click node
- Layout adapts (vertical layout dla mobile)

**Test Cases:**
- TC-09: iPad (1024×768) → graf renderuje, touch działa
- TC-10: iPhone (375×667) → graf renderuje, pinch zoom działa

**Acceptance:**
- Graf usable na tablets (iPad, Android tablets)
- Graf readable (nie wymagamy pełnej funkcjonalności na phones <400px width)

---

# 6. Kryteria Akceptacji (Acceptance Criteria)

## AC Summary Table

| ID | Category | Description | Priority |
|----|----------|-------------|----------|
| AC-01 | Rendering | Graf renderuje wszystkie dokumenty | P0 |
| AC-02 | Rendering | Krawędzie pokazują dependencies | P0 |
| AC-03 | Rendering | Layout hierarchiczny | P0 |
| AC-04 | Rendering | Węzły kolorowane według statusu | P0 |
| AC-05 | Performance | Render time <2s (500 nodes) | P0 |
| AC-06 | Zoom | Scroll up → zoom in (max 300%) | P0 |
| AC-07 | Zoom | Scroll down → zoom out (min 25%) | P0 |
| AC-08 | Zoom | Zoom smooth (60 FPS) | P0 |
| AC-09 | Zoom | Zoom towards cursor | P0 |
| AC-10 | Zoom | Pinch gesture (touch) | P0 |
| AC-11 | Pan | Click+drag → pan (mouse) | P0 |
| AC-12 | Pan | Touch+drag → pan (mobile) | P0 |
| AC-13 | Pan | Pan smooth (60 FPS) | P0 |
| AC-14 | Pan | Cursor changes to "grab" | P0 |
| AC-15 | Click Node | Click → open document | P0 |
| AC-16 | Click Node | Open in new tab | P0 |
| AC-17 | Click Node | Error if broken link | P0 |
| AC-18 | Tooltip | Hover → show tooltip | P0 |
| AC-19 | Tooltip | Tooltip shows metadata | P0 |
| AC-20 | Tooltip | 300ms delay | P0 |
| AC-21 | Tooltip | Disappears on mouse out | P0 |
| AC-22 | Filter | Multi-select dropdown "Doctype" | P1 |
| AC-23 | Filter | All doctypes listed | P1 |
| AC-24 | Filter | Default: all selected | P1 |
| AC-25 | Filter | Uncheck → nodes fade out | P1 |
| AC-26 | Filter | Edges to hidden nodes disappear | P1 |
| AC-27 | Filter | Instant filtering (<100ms) | P1 |
| AC-28 | Filter | Multi-select dropdown "Status" | P1 |
| AC-29 | Filter | All statuses listed | P1 |
| AC-30 | Filter | Default: hide draft/archived | P1 |
| AC-31 | Filter | Combine with doctype filter | P1 |
| AC-32 | Filter | Multi-select dropdown "Project" | P1 |
| AC-33 | Filter | Dynamic project list | P1 |
| AC-34 | Filter | Default: all projects | P1 |
| AC-35 | Highlight | Click → upstream red | P1 |
| AC-36 | Highlight | Upstream = dependencies | P1 |
| AC-37 | Highlight | Edges thicker, red | P1 |
| AC-38 | Highlight | Other nodes dimmed | P1 |
| AC-39 | Highlight | Click background → unhighlight | P1 |
| AC-40 | Highlight | Click → downstream green | P1 |
| AC-41 | Highlight | Downstream = impacts | P1 |
| AC-42 | Highlight | Edges thicker, green | P1 |
| AC-43 | Highlight | Upstream + downstream simultaneous | P1 |

**Total:** 43 Acceptance Criteria (23 P0, 20 P1)

---

# 7. Integracje / Zależności

## INT-01: Cytoscape.js Library

**Type:** External Dependency

**Description:**
System używa Cytoscape.js (open-source graph visualization library) do renderowania grafu.

**Rationale:**
- ADR-045: Wybrano Cytoscape.js po benchmarku (E-143)
- Performance: Cytoscape obsługuje 1000+ węzłów z smooth rendering
- Features: Built-in zoom, pan, layouts (hierarchical, force-directed)
- License: MIT (commercial-friendly)

**Version:** Cytoscape.js 3.26.0+

**Integration:**
- Import via npm: `npm install cytoscape`
- Usage: `const cy = cytoscape({ container: document.getElementById('graph'), ... })`

**Risk:**
- **Risk 1:** Cytoscape breaking change in future version
  - Mitigation: Lock version in package.json (`"cytoscape": "3.26.0"`)
- **Risk 2:** Cytoscape performance degradation dla >1000 węzłów
  - Mitigation: E-143 benchmark validated 1000+ nodes OK. If needed, implement virtualization (render only visible nodes)

---

## INT-02: Front-Matter Parser (YAML)

**Type:** Internal Dependency

**Description:**
System parsuje front-matter YAML z dokumentów Markdown aby zbudować graf.

**Required Fields:**
- `id` (DOC-ID)
- `doctype` (PRD, TDD, etc.)
- `status` (draft, approved, etc.)
- `version` (semantic version)
- `dependencies` (lista zależności)

**Integration:**
- Use library: `gray-matter` (npm package)
- Parse all `.md` files in docs/ directory
- Extract front-matter → build graph data structure

**Risk:**
- **Risk 1:** Malformed YAML (syntax errors)
  - Mitigation: Validation step (validate all YAML before rendering). Log errors, skip malformed docs.
- **Risk 2:** Missing required fields (id, doctype)
  - Mitigation: Default fallback (if no `id` → use filename, if no `doctype` → show as "Unknown")

---

## INT-03: Living Documentation Framework

**Type:** Internal Dependency

**Description:**
Graf integruje się z Living Documentation Framework — pokazuje extended metadata (lifecycle states, health status).

**Extended Features:**
- Node colors reflect extended lifecycle states (evolving, validating, refining → żółty)
- Tooltip pokazuje `document_health.status` (healthy/warning/critical)
- Highlight upstream changes pending (węzły z `cross_reference_status.upstream_changes_pending` → pulsing animation)

**Integration:**
- Read extended front-matter fields:
  - `status` (11 states vs 4)
  - `document_health.status`
  - `cross_reference_status`

**Risk:**
- **Risk 1:** Not all docs have extended front-matter (legacy docs)
  - Mitigation: Graceful degradation (if no extended fields → use basic metadata)

---

# 8. Ryzyka i Mitigacje

## RISK-01: Performance Degradation dla Dużych Grafów (>1000 węzłów)

**Likelihood:** Medium
**Impact:** High
**Severity:** HIGH

**Description:**
Jeśli projekt rozrasta się (200+ dokumentów), graf może renderować wolno (>5s) i zoom/pan może być laggy.

**Mitigation:**
1. **Benchmark:** E-143 validated Cytoscape handles 1000+ nodes OK (render <2s)
2. **Virtualization:** If needed, implement viewport culling (render only visible nodes)
3. **Lazy loading:** Load graph progressively (render 100 nodes at a time)
4. **Optimize layout:** Use faster layout algorithms (hierarchical vs force-directed)

**Contingency:**
- If performance <acceptable w user testing → implement virtualization before launch

---

## RISK-02: Browser Compatibility Issues (Safari, Firefox)

**Likelihood:** Low
**Impact:** Medium
**Severity:** MEDIUM

**Description:**
Cytoscape.js może mieć rendering issues na niektórych przeglądarkach (especially Safari).

**Mitigation:**
1. **Cross-browser testing:** Test na Chrome, Firefox, Safari, Edge (via BrowserStack)
2. **Polyfills:** Include polyfills dla starszych browsers (if needed)
3. **Fallback:** If Cytoscape fails → show static Mermaid graph (degraded experience)

**Contingency:**
- If critical issue found w Safari → fix before launch or add warning "Best viewed in Chrome"

---

## RISK-03: User Confusion — Graf Too Complex

**Likelihood:** Medium
**Impact:** Medium
**Severity:** MEDIUM

**Description:**
Graf 148 dokumentów może być overwhelming dla nowych użytkowników (zbyt wiele węzłów, trudno zrozumieć).

**Mitigation:**
1. **Default filters:** By default, hide draft/archived docs (reduce noise)
2. **Onboarding:** Show tutorial overlay (first time user) explaining zoom, pan, click, filters
3. **Preset views:** Add quick filters ("Show only PRDs", "Show only my project")

**Contingency:**
- If user testing shows confusion → improve onboarding (video tutorial, better tooltips)

---

## RISK-04: Outdated Graph Data (Stale Dependencies)

**Likelihood:** Medium
**Impact:** Medium
**Severity:** MEDIUM

**Description:**
Graf pokazuje dependencies z front-matter YAML. Jeśli YAML nie jest updated → graf jest outdated.

**Mitigation:**
1. **Living Documentation:** System trackuje upstream changes → notyfikuje owners → graf auto-refreshes
2. **Manual refresh:** Button "Refresh Graph" (re-parses all front-matter)
3. **Timestamp:** Show "Last updated: YYYY-MM-DD HH:MM" (users know if data is fresh)

**Contingency:**
- Phase 2 (automation): Auto-refresh grafu when documents change (file watcher)

---

# 9. Źródła / Evidence

## Evidence Index

| Evidence ID | Type | Description | Link |
|-------------|------|-------------|------|
| **E-143** | Benchmark | Cytoscape.js performance benchmark (1000+ nodes, <2s render) | `satellites/evidence/E-143-cytoscape-performance.md` |
| **E-144** | User Research | User interviews (5 tech writers, 3 PMs) - graph needs | `satellites/evidence/E-144-user-interviews-graph-needs.md` |
| **E-145** | Competitive Analysis | Competitor analysis (Notion, Confluence, Obsidian) - graph features | `satellites/evidence/E-145-competitive-graph-analysis.md` |
| **E-146** | Mockups | UI mockups (Figma) - graph canvas, filters, tooltips | `satellites/evidence/E-146-graph-ui-mockups.md` |

---

## Key Insights (z Evidence)

### E-143: Cytoscape Performance Benchmark

**Findings:**
- 100 nodes → render 420ms ✅
- 500 nodes → render 1.8s ✅
- 1000 nodes → render 3.2s ⚠️ (exceeds 2s target, but acceptable)
- 2000 nodes → render 8.5s ❌ (too slow)

**Conclusion:**
Cytoscape suitable dla Ishkarim (current: 148 docs, projected: <500 docs w 2026)

---

### E-144: User Interviews

**Pain Points:**
- 78% users: "Trudno znaleźć powiązane dokumenty"
- 62% users: "Nie wiem, które docs są impacted gdy coś się zmienia"
- 45% users: "Graf Mermaid nieczytelny"

**Feature Requests:**
- 100% users: "Chcę klikać węzeł → otwierać dokument"
- 85% users: "Chcę filtrować graf (np. tylko PRD)"
- 70% users: "Chcę widzieć upstream/downstream highlighted"

---

### E-145: Competitive Analysis

**Notion:**
- ✅ Ma graf zależności (pages)
- ❌ Nie ma filtrowania
- ❌ Nie pokazuje metadata (status, version)

**Confluence:**
- ✅ Ma "Page Tree" (hierarchical view)
- ❌ Nie jest interaktywny (no zoom/pan)

**Obsidian:**
- ✅ Ma "Graph View" (similar to ours)
- ✅ Filtrowanie po tags
- ❌ No status colors, no lifecycle

**Conclusion:**
Ishkarim może dorównać/przewyższyć konkurencję dzięki Living Documentation integration (status colors, health indicators)

---

# 10. Załączniki

## Appendix A: Technology Stack

| Component | Technology | Version | Rationale |
|-----------|-----------|---------|-----------|
| **Graph Library** | Cytoscape.js | 3.26.0+ | ADR-045, E-143 benchmark |
| **Front-End Framework** | React | 18.x | Existing Ishkarim stack |
| **YAML Parser** | gray-matter | 4.x | Standard library dla front-matter parsing |
| **Styling** | Tailwind CSS | 3.x | Existing Ishkarim UI framework |
| **Build Tool** | Vite | 5.x | Fast build, HMR |

---

## Appendix B: Changelog (Semantic Versioning)

Full changelog available at: `satellites/changelog/CHANGELOG-PRD-015.md`

**Summary:**

### [1.2.0] - 2025-12-20 (MINOR)
- **Added:** FR-28, FR-29, FR-30 (Interactive Filters)
- **Impact:** TDD-015 (architecture update), TEST-PLAN-015 (new test cases)

### [1.1.0] - 2025-12-10 (MINOR)
- **Changed:** NFR-01 extended (performance requirements dla >500 nodes)
- **Impact:** TDD-015 (review rendering strategy)

### [1.0.0] - 2025-12-01 (MAJOR)
- **Added:** Initial approved version (all sections complete)
- **Impact:** TDD-015 created, TEST-PLAN-015 created

---

## Appendix C: Glossary

| Term | Definition |
|------|------------|
| **Węzeł (Node)** | Reprezentacja dokumentu w grafie |
| **Krawędź (Edge)** | Reprezentacja zależności między dokumentami (dependency) |
| **Upstream** | Dokumenty, od których dany dokument zależy (dependencies) |
| **Downstream** | Dokumenty, które zależą od danego dokumentu (impacts) |
| **Layout** | Algorytm rozmieszczania węzłów (hierarchical, force-directed, circular) |
| **Cytoscape.js** | Open-source JavaScript library do wizualizacji grafów |
| **Front-matter** | YAML metadata na początku pliku Markdown |
| **Living Documentation** | Framework do dynamicznego zarządzania lifecycle dokumentów |

---

**Koniec PRD**

**Next Steps:**
1. ✅ PRD approved (2025-12-01) → STATUS: evolving (iterative refinement)
2. 🔄 TDD-015 in progress (Piotr Wiśniewski, Tech Lead)
3. ⏳ TEST-PLAN-015 pending (awaiting TDD-015 completion)
4. ⏳ Implementation target: Sprint 7-8 (Q1 2026)

**Stakeholders:**
- **Owner:** Anna Kowalska (Product Manager)
- **Tech Lead:** Piotr Wiśniewski (Backend/Frontend)
- **QA Lead:** Maria Nowak (Testing)
- **Approved by:** Jan Kowalski (CTO), Stakeholder Team

---

**Document Health:** 🟢 HEALTHY (score: 98/100, risk: low)
**Last Updated:** 2025-12-29
**Version:** 1.2.0 (MINOR - added interactive filters)
**Status:** evolving (iterative refinement based on Sprint 5 feedback)
