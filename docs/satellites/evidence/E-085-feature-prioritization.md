---
id: E-085
title: "Macierz Priorytetyzacji Feature'ów"
type: evidence
evidence_type: analysis
date: 2025-12-26

related_documents:
  - PRD-001-V2
  - ROADMAP-001

source:
  type: internal_analysis
  date_collected: 2025-12-26
---

# Macierz Priorytetyzacji Feature'ów

## Kontekst
W celu określenia zakresu MVP oraz roadmapy na Q1-Q2 2026, przeprowadzono systematyczną priorytetyzację 20 potencjalnych features Ishkarim. Wykorzystano framework RICE (Reach, Impact, Confidence, Effort) popularny w product management.

## Metodologia

### RICE Framework
**Formuła**: `RICE Score = (Reach × Impact × Confidence) / Effort`

**Definicje**:
- **Reach**: Ilu użytkowników dotknie feature w ciągu 3 miesięcy? (liczba)
- **Impact**: Jak duży wpływ na użytkownika? (0.25=minimal, 0.5=low, 1=medium, 2=high, 3=massive)
- **Confidence**: Jak pewni jesteśmy danych? (50%=low, 80%=medium, 100%=high)
- **Effort**: Ile person-months pracy? (liczba)

### Źródła Danych
- **Reach**: User interviews (E-081, E-082, E-083) + market research (E-080)
- **Impact**: User pain points z wywiadów (ranked 1-10 severity)
- **Confidence**: Data quality (interviews=100%, assumptions=50%)
- **Effort**: Engineering estimates (Tech Lead review)

### Założenia
- **Target users (MVP)**: 50 beta users w Q1 2026
- **Timeline**: 6 miesięcy development (2 devs)
- **Scope**: Features dla MVP (Top 10) vs Post-MVP (11-20)

## Wyniki

### Top 20 Features - RICE Scores

| Rank | Feature ID | Feature Name | Reach | Impact | Confidence | Effort | **RICE Score** | **Priority** |
|------|------------|--------------|-------|--------|------------|--------|----------------|--------------|
| 1 | FR-010 | Parser YAML + relacje | 50 | 3 | 100% | 2 | **75** | MVP |
| 2 | FR-020 | Gap detection engine | 50 | 3 | 100% | 3 | **50** | MVP |
| 3 | FR-030 | Proof system (validate evidence) | 40 | 2 | 80% | 2 | **32** | MVP |
| 4 | FR-011 | Graf wizualizacja (NetworkX) | 50 | 2 | 100% | 2 | **50** | MVP |
| 5 | FR-040 | Quality gates (block publish) | 30 | 3 | 80% | 1.5 | **48** | MVP |
| 6 | FR-012 | GUI Qt (PySide6) | 50 | 1 | 100% | 3 | **17** | MVP |
| 7 | FR-050 | File watcher (auto-reload) | 50 | 1 | 100% | 1 | **50** | MVP |
| 8 | FR-060 | Search FTS5 (SQLite) | 50 | 1 | 100% | 1.5 | **33** | MVP |
| 9 | FR-070 | Export HTML/PDF reports | 25 | 2 | 80% | 2 | **20** | MVP |
| 10 | FR-080 | Completeness tracking (%) | 40 | 2 | 80% | 1 | **64** | MVP |
| 11 | FR-090 | CI/CD integration (GitHub Actions) | 20 | 2 | 50% | 2 | **10** | Post-MVP |
| 12 | FR-100 | CLI tools (ishkarim check) | 20 | 1 | 80% | 1 | **16** | Post-MVP |
| 13 | FR-110 | Markdown import/export | 30 | 1 | 100% | 1.5 | **20** | Post-MVP |
| 14 | FR-120 | Version control (Git integration) | 25 | 2 | 50% | 3 | **8** | Post-MVP |
| 15 | FR-130 | Collaboration (comments) | 15 | 2 | 50% | 4 | **4** | Post-MVP |
| 16 | FR-140 | Real-time sync (multi-user) | 10 | 3 | 50% | 6 | **2.5** | Post-MVP |
| 17 | FR-150 | Templates (compliance/FDA/HIPAA) | 10 | 2 | 80% | 1 | **16** | Post-MVP |
| 18 | FR-160 | Audit mode (export proof trails) | 10 | 3 | 80% | 2 | **12** | Post-MVP |
| 19 | FR-170 | Code parser (Python/JS → docs) | 15 | 2 | 50% | 4 | **4** | Post-MVP |
| 20 | FR-180 | IDE plugins (VS Code) | 10 | 1 | 50% | 3 | **2** | Post-MVP |

**MVP threshold**: RICE > 15 (Top 10 features)

---

### MVP Features (Top 10) - Detailed Breakdown

#### 1. **FR-010: Parser YAML + Relacje** (RICE: 75)
**Dlaczego #1**: Foundation całego systemu. Bez parsera nie ma produktu.
- **Reach**: 50/50 users (100%)
- **Impact**: 3/3 (massive - enables wszystko inne)
- **Effort**: 2 person-months (Parser + YAML validator)

#### 2. **FR-020: Gap Detection Engine** (RICE: 50)
**Dlaczego #2**: Top pain point z wywiadów (E-081, E-082). Unikalna wartość Ishkarim.
- **Reach**: 50/50 users (technical writers + PMs)
- **Impact**: 3/3 (massive - oszczędza 10h/tydzień per user)
- **Effort**: 3 person-months (Graph traversal + semantic logic)

#### 3. **FR-011: Graf Wizualizacja** (RICE: 50)
**Dlaczego #3**: Tie z FR-020. Essential dla UX - users muszą WIDZIEĆ dependencies.
- **Reach**: 50/50 users
- **Impact**: 2/3 (high - nie critical, ale highly desired)
- **Effort**: 2 person-months (NetworkX + Qt integration)

#### 4. **FR-040: Quality Gates** (RICE: 48)
**Dlaczego #4**: Enforcement mechanism. Bez tego gap detection jest tylko "nice to know".
- **Reach**: 30/50 users (PMs + tech writers w regulated industries)
- **Impact**: 3/3 (massive dla compliance use case)
- **Effort**: 1.5 person-months (Validator + UI alerts)

#### 5. **FR-080: Completeness Tracking** (RICE: 64)
**Dlaczego #5**: Wysokie RICE, ale zależy od FR-020 (gap detection). Nice visual indicator.
- **Reach**: 40/50 users
- **Impact**: 2/3 (high - dashboard view, management visibility)
- **Effort**: 1 person-month (Aggregacja z gap detector)

#### 6. **FR-050: File Watcher** (RICE: 50)
**Dlaczego #6**: UX critical - auto-reload przy zmianie plików. Standard w modern tools.
- **Reach**: 50/50 users
- **Impact**: 1/3 (medium - quality of life)
- **Effort**: 1 person-month (Watchdog integration)

#### 7. **FR-060: Search FTS5** (RICE: 33)
**Dlaczego #7**: Basic functionality - search is expected w każdym docs tool.
- **Reach**: 50/50 users
- **Impact**: 1/3 (medium - not differentiator, but necessary)
- **Effort**: 1.5 person-months (SQLite FTS5 + UI)

#### 8. **FR-030: Proof System** (RICE: 32)
**Dlaczego #8**: Unique value prop, ale niszowy (compliance users). Lower reach.
- **Reach**: 40/50 users (nie wszyscy potrzebują proof enforcement)
- **Impact**: 2/3 (high dla compliance, low dla others)
- **Effort**: 2 person-months (Validator + proof types)

#### 9. **FR-070: Export HTML/PDF** (RICE: 20)
**Dlaczego #9**: Compliance requirement (audit exports). Lower reach (tylko PM/compliance).
- **Reach**: 25/50 users
- **Impact**: 2/3 (high dla audits)
- **Effort**: 2 person-months (Templating + export engine)

#### 10. **FR-012: GUI Qt** (RICE: 17)
**Dlaczego #10**: Foundation dla visualization/interaction. Low impact (funkcjonalny, not beautiful).
- **Reach**: 50/50 users
- **Impact**: 1/3 (medium - MVP GUI = basic, not polished)
- **Effort**: 3 person-months (PySide6 + layout)

**Total MVP Effort**: 19.5 person-months ≈ **5 miesięcy dla 2 devs** (realistic dla Q1-Q2 2026)

---

### Post-MVP Features (11-20) - Defer to Q3-Q4 2026

#### Why Deferred?
- **Lower reach**: CI/CD, CLI tools, IDE plugins = niszowe (developers only)
- **Higher effort**: Real-time sync (6 person-months), collaboration (4 person-months)
- **Lower confidence**: Assumptions-based (no strong user validation yet)
- **Not differentiators**: Markdown import/export, version control = "nice to have"

#### Top Post-MVP Candidates (Q3 2026)
1. **FR-110: Markdown import/export** (RICE: 20) - Interop z Obsidian/Confluence
2. **FR-100: CLI tools** (RICE: 16) - Developer experience
3. **FR-150: Templates** (RICE: 16) - Onboarding velocity dla compliance users

---

## Implikacje

### MVP Scope Definition (PRD-001-V2)
**Must-Have** (Top 10 features):
- Parser + relacje (FR-010)
- Gap detection (FR-020)
- Graf wizualizacja (FR-011)
- Quality gates (FR-040)
- Completeness tracking (FR-080)
- File watcher (FR-050)
- Search FTS5 (FR-060)
- Proof system (FR-030)
- Export HTML/PDF (FR-070)
- GUI Qt (FR-012)

**Total effort**: 19.5 person-months → **5-6 miesięcy dla 2 devs**

### Roadmap (ROADMAP-001)
- **Q1 2026**: Foundation (FR-010, FR-012, FR-050, FR-060) - 7.5 person-months
- **Q2 2026**: Core value (FR-020, FR-011, FR-040, FR-030, FR-080, FR-070) - 12 person-months
- **Q3 2026**: Developer features (FR-100, FR-110, FR-090) - 4.5 person-months
- **Q4 2026**: Collaboration (FR-150, FR-160, FR-120) - 6 person-months

### Success Metrics (E-098)
MVP success = Delivery Top 10 features by end Q2 2026:
- ✅ Parser handles 100+ docs in <5s
- ✅ Gap detection finds 90%+ real gaps
- ✅ Graf visualizes 500+ nodes smoothly
- ✅ Quality gates block incomplete docs
- ✅ 5+ beta users using daily

## Dane Raw

### RICE Calculation Spreadsheet

```
Feature ID | Reach | Impact | Confidence | Effort | RICE Score | Notes
-----------|-------|--------|------------|--------|------------|-------
FR-010     | 50    | 3      | 100%       | 2      | 75         | Foundation
FR-020     | 50    | 3      | 100%       | 3      | 50         | Top pain point
FR-011     | 50    | 2      | 100%       | 2      | 50         | Visualization essential
FR-040     | 30    | 3      | 80%        | 1.5    | 48         | Compliance enforcement
FR-080     | 40    | 2      | 80%        | 1      | 64         | Dashboard visibility
FR-050     | 50    | 1      | 100%       | 1      | 50         | Auto-reload UX
FR-060     | 50    | 1      | 100%       | 1.5    | 33         | Search expected
FR-030     | 40    | 2      | 80%        | 2      | 32         | Proof validation
FR-070     | 25    | 2      | 80%        | 2      | 20         | Audit exports
FR-012     | 50    | 1      | 100%       | 3      | 17         | GUI foundation
-----------|-------|--------|------------|--------|------------|-------
TOTAL MVP  | -     | -      | -          | 19.5   | -          | 10 features
```

### Effort Breakdown (Engineering Estimates)

| Feature | Task Breakdown | Estimated Hours | Person-Months |
|---------|----------------|-----------------|---------------|
| FR-010 Parser | YAML parser (100h) + Validator (60h) + Relations parser (80h) + Tests (80h) | 320h | 2 |
| FR-020 Gap detection | Graph traversal (120h) + Semantic rules (100h) + UI integration (60h) + Tests (80h) | 360h | 2.25 |
| FR-011 Graf viz | NetworkX setup (40h) + Qt integration (80h) + Layout algorithms (60h) + Tests (40h) | 220h | 1.4 |
| FR-040 Quality gates | Validator logic (60h) + UI alerts (40h) + Config (20h) + Tests (40h) | 160h | 1 |
| FR-080 Completeness | Aggregator (40h) + Dashboard widget (60h) + Tests (20h) | 120h | 0.75 |
| FR-050 File watcher | Watchdog integration (60h) + Reload logic (40h) + Tests (40h) | 140h | 0.9 |
| FR-060 Search FTS5 | SQLite FTS5 setup (60h) + Indexer (80h) + UI search bar (40h) + Tests (40h) | 220h | 1.4 |
| FR-030 Proof system | Proof validator (100h) + Types (60h) + UI (40h) + Tests (60h) | 260h | 1.6 |
| FR-070 Export | HTML template (80h) + PDF engine (100h) + UI export dialog (40h) + Tests (40h) | 260h | 1.6 |
| FR-012 GUI Qt | PySide6 setup (60h) + Main window (100h) + Layouts (120h) + Widgets (100h) + Tests (80h) | 460h | 2.9 |

**Assumption**: 1 person-month = 160 hours (20 days × 8h)

### User Feedback - Feature Wishlist Frequency

Z wywiadów E-081, E-082, E-083, zbiorcze wishlist features:
- **Gap detection**: Mentioned by 3/3 users (100%)
- **Dependency graph**: Mentioned by 3/3 users (100%)
- **Quality gates**: Mentioned by 2/3 users (67% - PM, tech writer)
- **Proof system**: Mentioned by 1/3 users (33% - PM w compliance)
- **Completeness tracking**: Mentioned by 2/3 users (67% - PM, tech writer)
- **CI/CD integration**: Mentioned by 1/3 users (33% - developer)
- **Markdown support**: Mentioned by 1/3 users (33% - developer)
- **Real-time collaboration**: Mentioned by 0/3 users (0% - not a priority)

**Validation**: Top 10 MVP features align z user wishlist (gap detection, graph, gates = most wanted)
