# L1 – Kanwa testów systemu

> Poziom L1 = **widok z góry** na całą strategię testowania systemu (architektura testów). Ten dokument nie zawiera jeszcze szczegółowych scenariuszy, tylko **co, po co i kiedy** jest testowane.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: SYSTEM-REQUIREMENTS
    type: test_requirements_source
    from_sections:
      - functional_requirements
      - non_functional_requirements
    to_sections:
      - test_coverage_matrix
      - test_scenarios
    influence: "Wymagania systemowe definiują zakres testów"
    when:
      condition: framework.type == "system_tests"
      applies: always

  - id: ARCHITECTURE-DOC
    type: system_understanding
    from_sections:
      - system_components
      - integration_points
    to_sections:
      - test_environment_setup
      - integration_test_scenarios
    influence: "Architektura określa co i jak testować"
    when:
      condition: tests.include_integration == true
      applies: always

  - id: QUALITY-ATTRIBUTES-SPEC
    type: nfr_testing_criteria
    from_sections:
      - performance_targets
      - security_requirements
      - reliability_targets
    to_sections:
      - performance_tests
      - security_tests
      - reliability_tests
    influence: "Atrybuty jakości definiują testy niefunkcjonalne"
    when:
      condition: tests.include_nfr == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: TEST-IMPLEMENTATION
    type: test_code
    from_sections:
      - test_framework_design
      - test_scenarios
    to_sections:
      - automated_test_suite
      - test_infrastructure
    influence: "Framework testów jest implementowany jako kod testów"
    when:
      condition: framework.approved == true
      applies: always

  - id: CI-CD-PIPELINE
    type: automation_integration
    from_sections:
      - test_execution_strategy
      - test_triggers
    to_sections:
      - pipeline_test_stages
      - quality_gates
    influence: "Testy są integrowane z pipeline CI/CD"
    when:
      condition: tests.automated == true
      applies: always

  - id: TEST-REPORTS
    type: quality_evidence
    from_sections:
      - test_execution_results
      - coverage_metrics
    to_sections:
      - quality_dashboards
      - release_readiness_criteria
    influence: "Wyniki testów dokumentują jakość systemu"
    when:
      condition: tests.executed == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: TEST-DATA-MANAGEMENT-STRATEGY
    relationship: data_provisioning
    sections_mapping:
      - from: test_data_requirements
        to: test_environment_setup
    usage: "Strategia zarządzania danymi testowymi wspiera framework"

  - id: DEFECT-MANAGEMENT-PROCESS
    relationship: issue_handling
    sections_mapping:
      - from: bug_reporting_workflow
        to: test_failure_handling
    usage: "Proces zarządzania defektami określa jak raportować błędy znalezione w testach"
```

### Satellite Documents

```yaml
satellites:
  - name: TEST-CASE-REPOSITORY
    purpose: "Repozytorium wszystkich przypadków testowych"
    trigger: per_test_case
    lifecycle: permanent
    retention: permanent

  - name: TEST-EXECUTION-LOGS
    purpose: "Logi z wykonania testów automatycznych"
    trigger: per_execution
    lifecycle: ephemeral
    retention: 3_months

  - name: COVERAGE-REPORTS
    purpose: "Raporty pokrycia kodu testami"
    trigger: per_build
    lifecycle: per_build
    retention: 6_months

  - name: PERFORMANCE-BENCHMARKS
    purpose: "Benchmarki wydajnościowe z testów"
    trigger: per_performance_test
    lifecycle: permanent
    retention: permanent
```

---

## 1. Cel i zakres L1

- Opis całej piramidy testów dla systemu.
- Wskazanie **które typy testów** są obowiązkowe, opcjonalne i kiedy są uruchamiane.
- Rozdzielenie odpowiedzialności: kto utrzymuje dany typ testów (dev / QA / DevOps / produkt / bezpieczeństwo).

---

## 2. Poziomy testów – mapa L1

### 2.1. Poziom UNIT

**Cel:** weryfikacja poprawności pojedynczych funkcji/klas.

**Kiedy wchodzą (triggery):**
- Każdy commit do feature brancha.
- Każdy merge request / pull request.
- Lokalnie przed commitem (zalecane).

**Założenia L1:**
- >80–90% krytycznej logiki biznesowej jest pokryte unit testami.
- Brak zewnętrznych zasobów (baza, sieć) – wszystko zamockowane.

---

### 2.2. Poziom INTEGRATION

**Cel:** sprawdzenie współpracy modułów (np. serwis + baza, serwis + kolejka, serwis + zewnętrzne API – mock lub sandbox).

**Kiedy wchodzą (triggery):**
- Każdy merge do głównej gałęzi (develop/main).
- Nocne buildy CI (pełny zestaw integracyjny).

**Założenia L1:**
- Scenariusze obejmują typowe przepływy między modułami.
- Dane testowe trzymane w osobnej bazie / kontenerze.

---

### 2.3. Poziom SYSTEM

**Cel:** testowanie systemu jako całości (pełna konfiguracja: backend + baza + kolejki + cache + UI/API).

**Kiedy wchodzą (triggery):**
- Każde przygotowanie wersji „release candidate”.
- Każdy większy refactor architektoniczny.

**Założenia L1:**
- Środowisko jak najbardziej zbliżone do produkcji.
- Obejmuje najważniejsze ścieżki biznesowe.

---

### 2.4. Poziom E2E (End-to-End)

**Cel:** symulacja zachowania realnego użytkownika (np. przez UI lub API) w typowych scenariuszach.

**Kiedy wchodzą (triggery):**
- Każdy release candidate.
- Nocne buildy (skrócona paczka „smoke E2E”).

**Założenia L1:**
- Minimalny zestaw krytycznych ścieżek: logowanie, rejestracja, główny flow biznesowy, raportowanie błędów.

---

### 2.5. Poziom ACCEPTANCE / UAT

**Cel:** potwierdzenie, że system spełnia wymagania biznesowe i można go zaakceptować.

**Kiedy wchodzą (triggery):**
- Przed wdrożeniem na produkcję (każda większa wersja).
- Po zakończeniu epiku / dużego pakietu funkcjonalności.

**Założenia L1:**
- Scenariusze przygotowane na bazie user stories / wymagań.
- Udział reprezentantów biznesu/klienta.

---

## 3. Typy testów wg celu – L1

Poniżej opisane są **główne typy testów**, które mogą występować na różnych poziomach (UNIT/INTEGRATION/SYSTEM/E2E). L1 definiuje **kiedy dany typ jest wymagany**.

### 3.1. Testy funkcjonalne

**Cel:** sprawdzenie, czy funkcje systemu działają zgodnie z wymaganiami.

**Wchodzą (obowiązkowe):**
- UNIT: krytyczna logika biznesowa.
- INTEGRATION: kluczowe przepływy między modułami.
- SYSTEM/E2E: główne scenariusze użytkownika.

### 3.2. Testy regresji

**Cel:** upewnienie się, że nowe zmiany nie psują istniejących funkcjonalności.

**Wchodzą (obowiązkowe):**
- Każdy merge do main/develop (zestaw automatycznych testów regresyjnych).
- Każdy release candidate (pełna/regresyjna paczka testów).

### 3.3. Testy smoke

**Cel:** szybka weryfikacja, czy system w ogóle działa po wdrożeniu lub buildzie.

**Wchodzą (obowiązkowe):**
- Po postawieniu środowiska testowego.
- Po wdrożeniu wersji na staging/pre-prod.

### 3.4. Testy sanity

**Cel:** szybkie sprawdzenie konkretnego obszaru po małej poprawce.

**Wchodzą (opcjonalne, zalecane):**
- Po naprawie buga w konkretnym module.

---

## 4. Testy niefunkcjonalne – L1

### 4.1. Testy wydajnościowe (Performance)

**Cel:** sprawdzić czas odpowiedzi i zachowanie systemu pod typowym obciążeniem.

**Wchodzą (obowiązkowe dla systemów krytycznych):**
- Przed pierwszym wdrożeniem na produkcję.
- Przed dużymi zmianami w architekturze (np. migracja bazy, zmiana cache).

### 4.2. Testy obciążeniowe (Load)

**Cel:** sprawdzić zachowanie systemu przy rosnącej liczbie użytkowników / żądań.

**Wchodzą (opcjonalne/obowiązkowe zależnie od projektu):**
- Systemy SaaS, systemy z dużym ruchem.

### 4.3. Testy przeciążeniowe (Stress)

**Cel:** sprawdzić granice wytrzymałości systemu i sposób degradacji.

**Wchodzą (opcjonalne):**
- Przy projektach z wysoką dostępnością (HA).

### 4.4. Testy stabilności / długotrwałe (Soak)

**Cel:** sprawdzić, czy system działa poprawnie przez długi czas (wycieki pamięci, degradacja wydajności).

**Wchodzą (opcjonalne/zalecane):**
- Systemy działające 24/7.

### 4.5. Testy bezpieczeństwa (Security)

**Cel:** analiza podatności, kontrola dostępu, poprawność autoryzacji, ochrona danych.

**Wchodzą (obowiązkowe):**
- Przed pierwszym wdrożeniem na produkcję.
- Po każdej większej zmianie w obszarze autoryzacji, uwierzytelniania, zarządzania danymi.

### 4.6. Testy odzyskiwania po awarii (Recovery)

**Cel:** weryfikacja backupów, procedur przywracania, integralności danych po awarii.

**Wchodzą (obowiązkowe dla systemów krytycznych):**
- Cyklowo (np. raz na kwartał).
- Po zmianach w mechanizmach backup/restore.

---

## 5. Sposób wykonania – L1

### 5.1. Testy automatyczne

**Wchodzą (default):**
- UNIT – zawsze.
- INTEGRATION – tam, gdzie tylko możliwe.
- E2E – minimalny zestaw krytycznych ścieżek.

### 5.2. Testy manualne

**Wchodzą (uzupełniająco):**
- UAT / Acceptance.
- Testy eksploracyjne UI.

### 5.3. Testy eksploracyjne

**Cel:** wykrycie nietypowych problemów, których nie przewidziano w scenariuszach.

**Wchodzą (zalecane):**
- Po większych zmianach UI/UX.
- Okresowo jako element przeglądu jakości.

---

## 6. Macierz „kiedy jakie testy wchodzą” – L1

Poniższa tabela jest szkicem do doprecyzowania na L2/L3.

| Wydarzenie                            | UNIT | INTEGRATION | SYSTEM | E2E  | PERFORMANCE | SECURITY | UAT  | SMOKE | REGRESSION |
|---------------------------------------|:----:|:-----------:|:------:|:----:|:-----------:|:--------:|:----:|:-----:|:----------:|
| Commit do feature brancha             |  X   |      -      |   -    |  -   |      -      |    -     |  -   |   -   |      -     |
| Pull/Merge Request                    |  X   |      X      |   -    |  -   |      -      |    -     |  -   |   -   |      X     |
| Merge do main/develop                 |  X   |      X      |   X    |  X   |   opcjonal  | opcjonal |  -   |   X   |      X     |
| Nocny build CI                        |  X   |      X      |   X    |  X   |   opcjonal  | opcjonal |  -   |   X   |      X     |
| Release candidate (RC)                |  X   |      X      |   X    |  X   |      X      |    X     |  X   |   X   |      X     |
| Wdrożenie na staging / pre‑prod       |  -   |      -      |   X    |  X   |   opcjonal  |    X     |  X   |   X   |      X     |
| Wdrożenie na produkcję               |  -   |      -      |   X    |  X   |   opcjonal  |    X     |  -   |   X   |      X     |
| Duży refactor architektury            |  X   |      X      |   X    |  X   |      X      |    X     |  -   |   X   |      X     |

Legenda: `X` – wymagane, `opcjonal` – zależy od krytyczności/typu systemu, `-` – zwykle nieuruchamiane na tym etapie.

---

## 7. Miejsca na doprecyzowanie (L2/L3)

Na poziomie L1 tylko zaznaczamy **co musi istnieć**. Szczegóły idą do L2/L3:

- **L2 – Specyfikacje testów**
  - Dokładne opisy przypadków testowych, scenariuszy, danych wejściowych/wyjściowych.
  - Definicja minimalnego pokrycia (coverage) dla UNIT/INTEGRATION.

- **L3 – Artefakty implementacyjne**
  - Struktura katalogów testów w repo.
  - Konfiguracja narzędzi (pytest, Jest, Playwright, Gatling, itp.).
  - Skrypty CI/CD uruchamiające odpowiednie pakiety testów w odpowiednich momentach.

---

> TODO (L1):
> - Zweryfikować, które testy niefunkcjonalne są **obowiązkowe** dla danego projektu.
> - Uzupełnić tabelę trigerów o konkretne nazwy pipeline’ów CI.
> - Powiązać typy testów z konkretnymi modułami systemu (L2: mapa domeny → mapa testów).

