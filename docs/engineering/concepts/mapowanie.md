---
id: CONCEPTS-001-V2-MAPPING
title: "Mapowanie Koncepcje → Funkcje"
type: concepts-mapping
parent: CONCEPTS-001-V2
domain: engineering
status: draft
created: 2025-12-26
---

# Część 2: Mapowanie Koncepcje → Funkcje

← [Poprzednia: Definicje](./koncepcje-v2-definicje.md) | [Powrót do głównego dokumentu](./koncepcje-v2.md) | [Następna: Funkcje →](./koncepcje-v2-funkcje.md)

---

## Przegląd

Ten dokument mapuje **18 koncepcji** na **~95 funkcji** systemu, zorganizowanych w **12 modułów**.

### Statystyki

- **Koncepcje**: 18 (6 nowych + 8 zmodyfikowanych + 4 bez zmian)
- **Funkcje**: ~95 (było 60 w V1 → wzrost +58%)
- **Moduły**: 12
- **Nowe funkcje**: ~35 (dla proof system)

---

## Mapa Koncepcje → Moduły → Funkcje

### Moduł 1: Parser (F-001 do F-004)

**Koncepcje**: C-007 (Parser), C-001 (Dokument), C-008 (Metadata)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-001 | Parse Markdown Files | ✅ Bez zmian | C-007, C-001 |
| F-002 | Extract YAML Frontmatter | ✅ Bez zmian | C-007, C-008 |
| F-003 | Identify Sections | ✅ Bez zmian | C-007 |
| F-004 | Detect References | ✅ Bez zmian | C-007, C-009 |

---

### Moduł 2: Validator (F-005 do F-008)

**Koncepcje**: C-006 (Walidator), C-002 (Typ Dokumentu), C-008 (Metadata)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-005 | Validate Document Schema | ✅ Bez zmian | C-006, C-002 |
| F-006 | Validate Frontmatter | ✅ Bez zmian | C-006, C-008 |
| F-007 | Validate Required Sections | ✅ Bez zmian | C-006, C-002 |
| F-008 | Detect Placeholders (TODO/TBD) | ✅ Bez zmian | C-006, C-004 |

---

### Moduł 3: Graph Builder (F-009 do F-013)

**Koncepcje**: C-003 (Graf Decyzyjny), C-010 (Węzeł), C-009 (Połączenie)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-009 | Build Decision Graph | 🔄 Rozszerzona | C-003 |
| F-010 | Manage Graph Nodes | ✅ Bez zmian | C-010 |
| F-011 | Manage Graph Edges | ✅ Bez zmian | C-009 |
| F-012 | Detect Cycles | ✅ Bez zmian | C-003 |
| F-013 | Calculate Hierarchy Levels | ✅ Bez zmian | C-003 |

---

### Moduł 4: Gap Detection Engine (F-014 do F-020, F-091, F-093, F-100, F-111)

**Koncepcje**: C-004 (Luka), C-016 (Nota Dowodowa), C-015 (Storytelling), C-018 (Post-mortem)

| ID | Funkcja | Status | Typ Luki | Koncepcja |
|----|---------|--------|----------|-----------|
| F-014 | Detect Missing Sections | ✅ Bez zmian | E110 | C-004 |
| F-015 | Detect Placeholders | ✅ Bez zmian | E120 | C-004 |
| F-016 | Detect Missing Evidence Docs | ✅ Bez zmian | E130 | C-004, C-011 |
| F-017 | Detect Broken Dependencies | ✅ Bez zmian | E140 | C-004 |
| F-018 | Detect Gate Blockers | ✅ Bez zmian | E150 | C-004, C-005 |
| F-019 | Detect Missing Approvals | ✅ Bez zmian | E160 | C-004 |
| F-100 | Detect Missing Evidence Notes | 🆕 NOWA | E170 | C-004, C-016 |
| F-093 | Detect Missing Storytelling | 🆕 NOWA | E180 | C-004, C-015 |
| F-091 | Detect Missing Alternatives | 🆕 NOWA | E190 | C-004, C-014 |
| F-111 | Detect Missing Post-mortem | 🆕 NOWA | E200 | C-004, C-018 |
| F-020 | Generate Gap Remediation | ✅ Bez zmian | All | C-004 |

---

### Moduł 5: Gate Management (F-081 do F-085, F-115, F-118 do F-120)

**Koncepcje**: C-013 (Bramka Wejścia/Wyjścia), C-005 (Lifecycle Gates), C-002 (Typ Dokumentu)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-081 | Define Input/Output Gates | 🆕 NOWA | C-013 |
| F-082 | Evaluate Gates (są spełnione?) | 🆕 NOWA | C-013, C-005 |
| F-083 | Propagate Changes Through Gates | 🆕 NOWA | C-013 |
| F-084 | Detect Gate Blockers | 🆕 NOWA | C-013, C-004 |
| F-085 | Generate TODOs from Gates | 🆕 NOWA | C-013, C-011 |
| F-115 | Validate Lifecycle Gate | 🆕 NOWA | C-005, C-002 |
| F-118 | Check DoR Gate | 🆕 NOWA | C-005 |
| F-119 | Check DoD Gate | 🆕 NOWA | C-005 |
| F-120 | Check Post-mortem Gate | 🆕 NOWA | C-005, C-018 |

---

### Moduł 6: Decision Graph Manager (F-086 do F-092)

**Koncepcje**: C-014 (Graf Decyzyjny), C-016 (Nota Dowodowa), C-015 (Storytelling)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-086 | Create Decision Graph | 🆕 NOWA | C-014 |
| F-087 | Register All Options (not just selected) | 🆕 NOWA | C-014 |
| F-088 | Capture Context T₀ | 🆕 NOWA | C-014, C-008 |
| F-089 | Register Comparative Justifications | 🆕 NOWA | C-014, C-015 |
| F-090 | Visualize Decision Graph (Mermaid) | 🆕 NOWA | C-014 |
| F-091 | Detect Missing Alternatives | 🆕 NOWA | C-014, C-004 |
| F-092 | Monitor Re-evaluation Triggers | 🆕 NOWA | C-014, C-018 |

---

### Moduł 7: Storytelling Validator (F-093 do F-096)

**Koncepcje**: C-015 (Storytelling), C-004 (Luka)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-093 | Validate Storytelling (detect fact list) | 🆕 NOWA | C-015, C-004 |
| F-094 | Generate Gap E180 | 🆕 NOWA | C-015, C-004 |
| F-095 | Provide Storytelling Templates per Type | 🆕 NOWA | C-015, C-002 |
| F-096 | Extract Narrative Structure | 🆕 NOWA | C-015 |

---

### Moduł 8: Evidence Tracker (F-097 do F-101)

**Koncepcje**: C-016 (Nota Dowodowa), C-011 (Satelita), C-004 (Luka)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-097 | Create Evidence Note | 🆕 NOWA | C-016, C-011 |
| F-098 | Link Evidence to Decision/Claim | 🆕 NOWA | C-016, C-014 |
| F-099 | Validate Evidence Exists | 🆕 NOWA | C-016 |
| F-100 | Detect Missing Evidence Notes (E170) | 🆕 NOWA | C-016, C-004 |
| F-101 | Manage Evidence Lifecycle (validity) | 🆕 NOWA | C-016 |

---

### Moduł 9: Implementation Log Manager (F-102 do F-106)

**Koncepcje**: C-017 (Implementation Log), C-011 (Satelita), C-014 (Graf Decyzyjny)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-102 | Create Implementation Log | 🆕 NOWA | C-017, C-011 |
| F-103 | Add Entry to Log | 🆕 NOWA | C-017 |
| F-104 | Link Log to Decision/ADR | 🆕 NOWA | C-017, C-014 |
| F-105 | Detect Missing Implementation Log | 🆕 NOWA | C-017, C-004 |
| F-106 | Generate Post-mortem from Log | 🆕 NOWA | C-017, C-018 |

---

### Moduł 10: Post-mortem Generator (F-107 do F-111)

**Koncepcje**: C-018 (Post-mortem), C-011 (Satelita), C-017 (Implementation Log)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-107 | Create Post-mortem Document | 🆕 NOWA | C-018, C-011 |
| F-108 | Generate Post-mortem from Impl Log | 🆕 NOWA | C-018, C-017 |
| F-109 | Track Action Items | 🆕 NOWA | C-018 |
| F-110 | Monitor Re-evaluation Triggers | 🆕 NOWA | C-018, C-014 |
| F-111 | Detect Missing Post-mortem (E200) | 🆕 NOWA | C-018, C-004 |

---

### Moduł 11: Document Lifecycle (F-112 do F-114, F-121 do F-123)

**Koncepcje**: C-001 (Dokument), C-008 (Metadata), C-014 (Graf Decyzyjny)

| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-112 | Immutable Document Versioning | 🆕 NOWA | C-001 |
| F-113 | Generate Changelog | 🆕 NOWA | C-001, C-008 |
| F-114 | Manage Document Gates | 🆕 NOWA | C-001, C-013 |
| F-121 | Extract Decision Metadata | 🆕 NOWA | C-008, C-014 |
| F-122 | Extract Context Snapshot | 🆕 NOWA | C-008, C-014 |
| F-123 | Track Alternatives in Metadata | 🆕 NOWA | C-008, C-014 |

---

### Moduł 12: Satellite & Domain (F-021 do F-040, F-124 do F-128)

**Koncepcje**: C-011 (Satelita), C-012 (Domena), C-002 (Typ Dokumentu)

#### GUI Functions (F-021 do F-025) - Bez zmian
| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-021 | Main Window Interface | ✅ Bez zmian | - |
| F-022 | Graph Visualization Widget | ✅ Bez zmian | C-003 |
| F-023 | Document Preview Panel | ✅ Bez zmian | C-001 |
| F-024 | Gaps Panel | ✅ Bez zmian | C-004 |
| F-025 | Navigation Controls | ✅ Bez zmian | - |

#### Storage Functions (F-026 do F-028) - Bez zmian
| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-026 | Index Documents (SQLite + FTS5) | ✅ Bez zmian | C-001 |
| F-027 | Load Document Type Schemas | ✅ Bez zmian | C-002 |
| F-028 | Persist Gaps | ✅ Bez zmian | C-004 |

#### File Watcher (F-029) - Bez zmian
| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-029 | Monitor Directories (Watchdog) | ✅ Bez zmian | - |

#### Proactive Assistant (F-030 do F-033) - Rozszerzone
| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-030 | Evaluate Quality Gates | 🔄 Rozszerzona | C-005 |
| F-031 | Suggest Next Steps | ✅ Bez zmian | - |
| F-032 | Validate Connections | ✅ Bez zmian | C-009 |
| F-033 | Manage Metadata | 🔄 Rozszerzona | C-008 |

#### Satellite Management (F-034 do F-038, F-124 do F-126) - Rozszerzone + Nowe
| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-034 | Create and Validate Edges | ✅ Bez zmian | C-009, C-002 |
| F-035 | Calculate Node Properties | ✅ Bez zmian | C-010 |
| F-036 | Generate TODO Satellites | ✅ Bez zmian | C-011 |
| F-037 | Manage DOR/DOD | ✅ Bez zmian | C-011, C-005 |
| F-038 | Generate RTM | ✅ Bez zmian | C-011 |
| F-124 | Generate Implementation Log | 🆕 NOWA | C-011, C-017 |
| F-125 | Generate Post-mortem | 🆕 NOWA | C-011, C-018 |
| F-126 | Link Evidence Notes | 🆕 NOWA | C-011, C-016 |

#### Domain Management (F-039, F-040, F-127, F-128) - Rozszerzone + Nowe
| ID | Funkcja | Status | Koncepcja |
|----|---------|--------|-----------|
| F-039 | Register Domain | ✅ Bez zmian | C-012 |
| F-040 | Domain-Specific Validation | 🔄 Rozszerzona | C-012 |
| F-127 | Enforce Policy Maps | 🆕 NOWA | C-012 |
| F-128 | Domain-Specific Workflows | 🆕 NOWA | C-012 |

---

## Macierz Pełna: Koncepcje → Funkcje

### Koncepcje NOWE (6)

#### C-013: Bramka Wejścia/Wyjścia
**Funkcje**: F-081, F-082, F-083, F-084, F-085, F-114
**Moduły**: Gate Management (5), Document Lifecycle (1)

#### C-014: Graf Decyzyjny
**Funkcje**: F-086, F-087, F-088, F-089, F-090, F-091, F-092, F-098, F-104, F-110, F-121, F-122, F-123
**Moduły**: Decision Graph Manager (7), Evidence Tracker (1), Impl Log (1), Post-mortem (1), Document Lifecycle (3)

#### C-015: Storytelling
**Funkcje**: F-089, F-093, F-094, F-095, F-096
**Moduły**: Storytelling Validator (4), Decision Graph (1)

#### C-016: Nota Dowodowa
**Funkcje**: F-097, F-098, F-099, F-100, F-101, F-126
**Moduły**: Evidence Tracker (5), Satellite (1)

#### C-017: Implementation Log
**Funkcje**: F-102, F-103, F-104, F-105, F-106, F-124
**Moduły**: Impl Log Manager (5), Satellite (1)

#### C-018: Post-mortem
**Funkcje**: F-106, F-107, F-108, F-109, F-110, F-111, F-120, F-125
**Moduły**: Post-mortem Generator (6), Gate Management (1), Satellite (1)

### Koncepcje ZMODYFIKOWANE (8)

#### C-001: Dokument
**Funkcje**: F-001, F-002, F-023, F-026, F-112, F-113, F-114
**Moduły**: Parser (2), GUI (1), Storage (1), Document Lifecycle (3)

#### C-002: Typ Dokumentu
**Funkcje**: F-005, F-007, F-027, F-034, F-095, F-115, F-117
**Moduły**: Validator (2), Storage (1), Satellite (1), Storytelling (1), Gate Management (2)

#### C-003: Graf Zależności → Graf Decyzyjny
**Funkcje**: F-009, F-012, F-013, F-022
**Moduły**: Graph Builder (3), GUI (1)

#### C-004: Luka
**Funkcje**: F-008, F-014, F-015, F-016, F-017, F-018, F-019, F-020, F-024, F-028, F-084, F-091, F-093, F-094, F-100, F-105, F-111
**Moduły**: Gap Detection (11), GUI (1), Storage (1), Gate Management (1), Storytelling (2), Evidence (1), Impl Log (1), Post-mortem (1)

#### C-005: Bramka Jakości → Lifecycle Gates
**Funkcje**: F-018, F-030, F-037, F-082, F-115, F-118, F-119, F-120
**Moduły**: Gap Detection (1), Proactive (1), Satellite (1), Gate Management (5)

#### C-008: Metadata
**Funkcje**: F-002, F-006, F-033, F-088, F-113, F-121, F-122, F-123
**Moduły**: Parser (1), Validator (1), Proactive (1), Decision Graph (1), Document Lifecycle (4)

#### C-011: Satelita
**Funkcje**: F-016, F-036, F-037, F-038, F-097, F-102, F-107, F-124, F-125, F-126
**Moduły**: Gap Detection (1), Satellite Management (7), Evidence (1), Impl Log (1), Post-mortem (1)

#### C-012: Domena
**Funkcje**: F-039, F-040, F-127, F-128
**Moduły**: Domain Management (4)

### Koncepcje BEZ ZMIAN (4)

#### C-006: Walidator
**Funkcje**: F-005, F-006, F-007, F-008
**Moduły**: Validator (4)

#### C-007: Parser
**Funkcje**: F-001, F-002, F-003, F-004
**Moduły**: Parser (4)

#### C-009: Połączenie (Edge)
**Funkcje**: F-004, F-011, F-032, F-034
**Moduły**: Parser (1), Graph Builder (1), Proactive (1), Satellite (1)

#### C-010: Węzeł (Node)
**Funkcje**: F-010, F-035
**Moduły**: Graph Builder (1), Satellite (1)

---

## Podsumowanie Statystyczne

### Funkcje per Status

| Status | Liczba | % |
|--------|--------|---|
| 🆕 NOWA | 35 | 37% |
| 🔄 Rozszerzona | 6 | 6% |
| ✅ Bez zmian | 54 | 57% |
| **RAZEM** | **95** | **100%** |

### Funkcje per Moduł

| Moduł | Funkcje | Nowe | Rozszerzone | Bez zmian |
|-------|---------|------|-------------|-----------|
| 1. Parser | 4 | 0 | 0 | 4 |
| 2. Validator | 4 | 0 | 0 | 4 |
| 3. Graph Builder | 5 | 0 | 1 | 4 |
| 4. Gap Detection | 11 | 4 | 0 | 7 |
| 5. Gate Management | 9 | 9 | 0 | 0 |
| 6. Decision Graph | 7 | 7 | 0 | 0 |
| 7. Storytelling | 4 | 4 | 0 | 0 |
| 8. Evidence Tracker | 5 | 5 | 0 | 0 |
| 9. Impl Log Manager | 5 | 5 | 0 | 0 |
| 10. Post-mortem | 6 | 6 | 0 | 0 |
| 11. Document Lifecycle | 7 | 6 | 1 | 0 |
| 12. Satellite & Domain | 28 | 3 | 3 | 22 |
| **RAZEM** | **95** | **35** | **6** | **54** |

### Top Koncepcje per Liczba Funkcji

1. **C-004 (Luka)**: 17 funkcji
2. **C-014 (Graf Decyzyjny)**: 13 funkcji
3. **C-013 (Bramka Wejścia/Wyjścia)**: 9 funkcji
4. **C-011 (Satelita)**: 10 funkcji
5. **C-018 (Post-mortem)**: 8 funkcji
6. **C-008 (Metadata)**: 8 funkcji

---

← [Poprzednia: Definicje](./koncepcje-v2-definicje.md) | [Powrót do głównego dokumentu](./koncepcje-v2.md) | [Następna: Funkcje →](./koncepcje-v2-funkcje.md)
