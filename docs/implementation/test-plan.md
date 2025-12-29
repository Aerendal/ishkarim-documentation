---
id: TEST-PLAN-001
title: "Plan Testów - System Dokumentacji Semantycznej"
type: test-plan
status: draft
created: 2025-12-26

dependencies:
  - id: PRD-001-V2
    type: requires
    status_constraint: [req-freeze, approved]
    reason: "Plan testów testuje wymagania"
  - id: TDD-001-V2
    type: requires
    reason: "Plan testów waliduje design"

impacts: []
  # TEST-CASES-001 (planned - to be created during implementation)

evidence_ids:
  - E-160
---

# Plan Testów

## Poziomy Testowania

### 1. Testy Jednostkowe (cel: 80% coverage)
**Zakres**: Pojedyncze funkcje/klasy
**Narzędzia**: pytest, pytest-cov
**Odpowiedzialność**: Developerzy (inline z kodem)

**Kluczowe obszary**:
- Parser: ekstrakcja frontmatter, parsowanie sekcji
- Validator: walidacja schematu, detekcja placeholderów
- Graph: tworzenie node/edge, detekcja cykli
- Gap Engine: każdy typ luki (E110-E160)

**Cel coverage**: ≥ 80% line coverage

### 2. Testy Integracyjne
**Zakres**: Interakcje komponentów
**Narzędzia**: pytest z fixtures
**Odpowiedzialność**: QA Engineer

**Test suites**:
- Pipeline Parser → Validator
- Pipeline Parser → Graph Builder
- Gap Engine → Remediation Generator
- GUI → Backend (obsługa zdarzeń)

**Kryteria zaliczenia**: Wszystkie 95 FR zwalidowane end-to-end

### 3. Testy Wydajności
**Zakres**: Walidacja NFR
**Narzędzia**: pytest-benchmark, memory_profiler
**Odpowiedzialność**: Tech Lead + QA

**Benchmarki**:
| Metryka | Cel (NFR) | Metoda Testowa |
|---------|-----------|----------------|
| Parse 100 docs | < 5s | NFR-001 |
| Build graph (100 docs) | < 2s | NFR-002 |
| Search FTS5 (10k docs) | < 100ms | E-146 istniejący |
| Odpowiedź GUI | < 100ms | NFR-003 |

### 4. Testy Systemowe
**Zakres**: Scenariusze end-to-end
**Narzędzia**: pytest + automatyzacja GUI (pytest-qt)
**Odpowiedzialność**: QA Engineer

**Scenariusze**:
- US-001: Parsuj i waliduj dokument
- US-002: Śledź zależności wymagań
- US-003: Wykryj brakującą dokumentację
- US-004: Zobacz status dokumentacji projektu
- (Wszystkie 10 user stories z PRD-V2)

### 5. Testy Akceptacyjne
**Zakres**: Akceptacja użytkownika
**Narzędzia**: Testowanie manualne + formularze feedbacku
**Odpowiedzialność**: Product Owner + Beta Users

**Kryteria**:
- 5+ beta users kończy onboarding w < 30 min (NFR-008)
- Zadowolenie użytkowników ≥ 4.5/5 (NFR-009)
- 0 critical bugs zgłoszonych

## Środowisko Testowe

**Development**:
- Python 3.11 na Linux/macOS/Windows
- Virtual environment (venv)
- Sample docs: 100+ plików markdown

**CI/CD**:
- GitHub Actions (pytest przy push)
- Raporty coverage (codecov.io)
- Testy regresji wydajności

**Beta**:
- Prawdziwe workspace'y użytkowników (1000+ docs)
- Mieszane OS (Linux, macOS, Windows)

## Dane Testowe

**Przykładowe Dokumenty**:
- 20 PRD (różne statusy)
- 15 ADR (accepted, rejected, deprecated)
- 30 Specyfikacji komponentów
- 50 różnych dokumentów

**Edge Cases**:
- Zdeformowany YAML frontmatter
- Cykliczne zależności (A → B → C → A)
- Brakujące pliki (broken links)
- Bardzo duże docs (10,000+ linii)
- Znaki Unicode/specjalne

## Zarządzanie Defektami

**Poziomy Severity**:
- **Critical**: Crash, utrata danych, problem bezpieczeństwa → Fix natychmiast
- **High**: Feature zepsute, NFR wydajności naruszony → Fix w sprincie
- **Medium**: Drobny problem funkcjonalny → Backlog
- **Low**: Glitch UI, literówka → Nice to have

**Workflow**:
1. Zgłoś issue (GitHub Issues)
2. Triage (przypisz severity, sprint)
3. Fix + test
4. Weryfikuj + zamknij

## Harmonogram Testów

| Faza | Czas trwania | Aktywności |
|------|--------------|------------|
| Testy jednostkowe | Ongoing (każdy sprint) | Developerzy piszą testy inline |
| Testy integracyjne | Sprint 3-6 | QA buduje test suites |
| Testy wydajności | Sprint 3, 6 | Benchmark critical paths |
| Testy systemowe | Sprint 6 | Pełna walidacja US |
| Beta testing | Tydzień 13-14 | 5+ users, zbieranie feedbacku |

## Kryteria Sukcesu

- ✅ 80% code coverage osiągnięte
- ✅ Wszystkie 95 FR zwalidowane
- ✅ Wszystkie 15 NFR spełnione (benchmark)
- ✅ 0 critical bugs w beta
- ✅ Zadowolenie użytkowników ≥ 4.5/5

## Powiązane Dokumenty
- [PRD-001-V2](../engineering/prd-v2.md)
- [RTM-001](../engineering/rtm.md) (linkuje testy → wymagania)
<!-- TEST-CASES-001 (planned - to be created during implementation) -->
