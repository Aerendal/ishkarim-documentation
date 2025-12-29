---
id: PRD-001
title: "Product Requirements Document - System Zarządzania Dokumentacją"
type: prd
domain: requirements
status: draft
created: 2025-12-26
updated: 2025-12-26
owner: "Zespół Produktowy"
phase: requirements
priority: critical
dependencies:
  - EXEC-SUM-001
  - BIZ-CASE-001
  - VISION-001
  - CONCEPTS-001
related:
  - TDD-001
  - RTM-001
---

# Product Requirements Document - System Zarządzania Dokumentacją

## Spis Treści

### 1. Przegląd Dokumentu (Linie 60-120)
- 1.1 Cel i Zakres
- 1.2 Grupa Docelowa
- 1.3 Przewodnik po Strukturze Dokumentu
- 1.4 Dokumenty Powiązane

### 2. Przegląd Systemu (Linie 121-200)
- 2.1 Deklaracja Wizji
- 2.2 Kluczowe Możliwości
- 2.3 Propozycja Wartości dla Użytkowników
- 2.4 Metryki Sukcesu

### 3. Persony Użytkowników & Use Cases (Linie 201-280)
- 3.1 Persony Główne
  - 3.1.1 Programista Python
  - 3.1.2 Product Manager
  - 3.1.3 Inżynier QA
  - 3.1.4 Technical Writer
- 3.2 Persony Drugorzędne
- 3.3 Scenariusze Use Case

### 4. Wymagania Funkcjonalne (Linie 281-680)
- 4.1 Moduł Parser (FR-001 do FR-004)
- 4.2 Moduł Validator (FR-005 do FR-008)
- 4.3 Moduł Graph Builder (FR-009 do FR-013)
- 4.4 Gap Detection Engine (FR-014 do FR-020)
- 4.5 Moduł GUI (FR-021 do FR-025)
- 4.6 Moduł Storage (FR-026 do FR-028)
- 4.7 Moduł File Watcher (FR-029 do FR-030)
- 4.8 Moduł Proactive Assistant (FR-031 do FR-033)
- 4.9 Moduł Satellite Documents (FR-034 do FR-038)
- 4.10 Moduł Domain (FR-039 do FR-040)

### 5. Wymagania Niefunkcjonalne (Linie 681-800)
- 5.1 Wymagania Wydajnościowe (NFR-001 do NFR-003)
- 5.2 Wymagania Niezawodności (NFR-004 do NFR-005)
- 5.3 Wymagania Skalowalności (NFR-006 do NFR-007)
- 5.4 Wymagania Użyteczności (NFR-008 do NFR-009)
- 5.5 Wymagania Utrzymywalności (NFR-010 do NFR-011)
- 5.6 Wymagania Bezpieczeństwa (NFR-012)
- 5.7 Wymagania Kompatybilności (NFR-013 do NFR-014)
- 5.8 Wymagania Rozszerzalności (NFR-015)

### 6. User Stories (Linie 801-920)
- 6.1 Developer Stories (US-001 do US-003)
- 6.2 Product Manager Stories (US-004 do US-006)
- 6.3 QA Engineer Stories (US-007 do US-008)
- 6.4 Technical Writer Stories (US-009 do US-010)

### 7. Bramki Jakości & Kryteria Akceptacji (Linie 921-1020)
- 7.1 Definicje Bramek Jakości
- 7.2 Kryteria Akceptacji per FR
- 7.3 Przegląd Strategii Testowania

### 8. Ograniczenia Techniczne & Zależności (Linie 1021-1100)
- 8.1 Stos Technologiczny
- 8.2 Zależności Zewnętrzne
- 8.3 Wymagania Systemowe
- 8.4 Punkty Integracji

### 9. Macierz Mapowania Koncepcji (Linie 1101-1180)
- 9.1 Mapowanie Koncepcje → FR
- 9.2 Mapowanie FR → Moduł
- 9.3 Mapowanie FR → Test

### 10. Dodatki & Referencje (Linie 1181-1200)
- 10.1 Glosariusz
- 10.2 Referencje
- 10.3 Log Zmian

---

## 1. Przegląd Dokumentu

### 1.1 Cel i Zakres

[**Do wypełnienia**: Opisać cel PRD, co obejmuje, jakie problemy rozwiązuje]

### 1.2 Grupa Docelowa

[**Do wypełnienia**: Kto powinien czytać ten dokument - deweloperzy, PM, QA, stakeholderzy]

### 1.3 Przewodnik po Strukturze Dokumentu

[**Do wypełnienia**: Jak nawigować po dokumencie, co znajduje się w każdej sekcji]

### 1.4 Dokumenty Powiązane

| Dokument | ID | Relacja | Opis |
|----------|----|---------| -----|
| Executive Summary | EXEC-SUM-001 | Dependency | Strategiczne uzasadnienie projektu |
| Business Case | BIZ-CASE-001 | Dependency | ROI i analiza biznesowa |
| Vision Document | VISION-001 | Dependency | Długoterminowa wizja produktu |
| Concepts Document | CONCEPTS-001 | Dependency | Definicje koncepcji i funkcji |
| Technical Design Document | TDD-001 | Related | Projekt techniczny (do stworzenia) |
| Requirements Traceability Matrix | RTM-001 | Related | Mapowanie wymaga ń (do stworzenia) |

---

## 2. Przegląd Systemu

### 2.1 Deklaracja Wizji

[**Do wypełnienia**: Krótka deklaracja wizji z VISION-001 - czym jest system, dlaczego istnieje]

### 2.2 Kluczowe Możliwości

[**Do wypełnienia**: Lista 5-7 głównych możliwości systemu:
- Parsowanie dokumentów markdown z YAML frontmatter
- Automatyczna walidacja względem schematów
- Budowanie i wizualizacja grafu zależności
- Wykrywanie luk (E110-E160)
- Proaktywne sugestie następnych kroków
- Interaktywne GUI z grafem
- Real-time monitoring zmian w plikach]

### 2.3 Propozycja Wartości dla Użytkowników

[**Do wypełnienia**: Dla każdej persony - jaką wartość dostaje z systemu]

### 2.4 Metryki Sukcesu

[**Do wypełnienia**: Kluczowe metryki z VISION-001:
- 95%+ kompletność dokumentacji przy bramkach
- < 5s analiza 100 dokumentów
- 80%+ dokładność wykrywania luk
- 4.5/5 zadowolenie użytkowników]

---

## 3. Persony Użytkowników & Use Cases

### 3.1 Persony Główne

#### 3.1.1 Programista Python

**Kim jest**: [Opis persony]
**Cele**: [Co chce osiągnąć]
**Bóle**: [Jakie ma problemy]
**Zyski**: [Co zyskuje z systemu]

#### 3.1.2 Product Manager

[**Do wypełnienia**: Analogicznie jak powyżej]

#### 3.1.3 Inżynier QA

[**Do wypełnienia**: Analogicznie jak powyżej]

#### 3.1.4 Technical Writer

[**Do wypełnienia**: Analogicznie jak powyżej]

### 3.2 Persony Drugorzędne

[**Do wypełnienia**: DevOps/SRE, Audytorzy Compliance]

### 3.3 Scenariusze Use Case

**Scenariusz 1: Tworzenie Nowego Dokumentu PRD**
[**Do wypełnienia**: Krok po kroku jak użytkownik tworzy nowy dokument]

**Scenariusz 2: Analiza Luk w Projekcie**
[**Do wypełnienia**: Jak PM analizuje kompletność dokumentacji]

**Scenariusz 3: Śledzenie Wymagań do Testów**
[**Do wypełnienia**: Jak QA używa RTM do weryfikacji pokrycia]

---

## 4. Wymagania Funkcjonalne

### 4.1 Moduł Parser (FR-001 do FR-004)

**Cel modułu**: Parsowanie plików markdown z YAML frontmatter do strukturalnych obiektów

**Kluczowe Odpowiedzialności**:
- Ekstrakcja YAML frontmatter
- Parsowanie markdown do AST
- Identyfikacja sekcji
- Wykrywanie odniesień do innych dokumentów

#### FR-001: Parsowanie Plików Markdown

**Opis**: System musi być zdolny do parsowania plików markdown (.md) z YAML frontmatter i konwersji ich na strukturalne obiekty ParsedDocument. Parser powinien obsługiwać pełny proces: odczyt pliku, ekstrakcję frontmatter, parsowanie markdown do AST, identyfikację sekcji oraz wykrywanie odniesień do innych dokumentów.

**Cel Biznesowy**: Umożliwienie automatycznej analizy i walidacji dokumentacji bez manualnego wprowadzania danych. Parser jest fundamentem całego systemu - bez niego żadna inna funkcjonalność nie może działać.

**Acceptance Criteria**:
- [ ] AC-1: System parsuje 100% poprawnie sformatowanych plików .md bez błędów
- [ ] AC-2: Wydajność: parsowanie pojedynczego dokumentu < 50ms, 100 dokumentów < 5 sekund
- [ ] AC-3: Parser ekstrahuje wszystkie komponenty: frontmatter YAML, sekcje markdown (H1-H6), treść sekcji, numery linii
- [ ] AC-4: Parser obsługuje błędy gracefully: FileNotFoundError, YAMLParseError, MarkdownParseError z czytelnymi komunikatami
- [ ] AC-5: Parser zwraca obiekt ParsedDocument z polami: file_path, frontmatter (dict), sections (List[Section]), references (List[Reference]), ast (MarkdownAST)

**Constraints**:
- Musi używać biblioteki `python-frontmatter` do ekstrakcji YAML
- Musi używać `markdown-it-py` do parsowania markdown do AST
- Obsługa tylko plików .md (nie .mdx, .rst, etc.)
- Maksymalny rozmiar pliku: 10 MB

**Success Metric**:
- 100% dokumentów testowych sparsowanych poprawnie
- Zero crashy podczas parsowania w testach regression
- Pokrycie testami ≥ 90% dla modułu parser

**Mapuje Koncepcje**: C-007 (Parser), C-001 (Dokument)

---

#### FR-002: Ekstrakcja YAML Frontmatter

**Opis**: System musi ekstrahować YAML frontmatter z początku pliku markdown, parsować go do struktury dict oraz oddzielać od markdown body. Frontmatter zawiera kluczowe metadane dokumentu (id, type, status, dependencies, related) i musi być poprawnie wyciągnięty dla wszystkich dalszych operacji walidacji i budowania grafu.

**Cel Biznesowy**: Metadane frontmatter są sercem systemu zarządzania dokumentacją - definiują tożsamość dokumentu, jego typ, status w cyklu życia oraz relacje z innymi dokumentami. Bez poprawnej ekstrakcji frontmatter niemożliwa jest automatyczna walidacja i wykrywanie luk.

**Acceptance Criteria**:
- [ ] AC-1: System rozpoznaje frontmatter YAML otoczony znacznikami `---` na początku i końcu
- [ ] AC-2: Poprawna ekstrakcja wszystkich standardowych pól: id, title, type, domain, status, owner, dependencies, related
- [ ] AC-3: Zwrócona para (frontmatter_dict, markdown_body) gdzie frontmatter jest sparsowany do Python dict
- [ ] AC-4: Obsługa plików bez frontmatter - zwrócenie pustego dict i pełnej treści jako body
- [ ] AC-5: Walidacja składni YAML - wykrywanie błędów parsowania z czytelnymi komunikatami o lokalizacji błędu

**Constraints**:
- Frontmatter musi znajdować się na początku pliku (pierwsze znaki to `---`)
- Format YAML musi być zgodny ze specyfikacją YAML 1.2
- Wieloliniowe wartości YAML muszą być obsługiwane poprawnie
- Listy dependencies i related muszą być wyekstrahowane jako Python list

**Success Metric**:
- 100% dokumentów z poprawnym frontmatter ekstrahowanych bez błędów
- Wszystkie typy YAML (string, int, bool, list, dict) poprawnie konwertowane do Python
- < 10ms na ekstrakcję frontmatter z pojedynczego dokumentu

**Mapuje Koncepcje**: C-007 (Parser), C-008 (Metadata)

#### FR-003: Identyfikacja Sekcji

**Opis**: System musi identyfikować wszystkie sekcje markdown (nagłówki ## od poziomu H1 do H6) wraz z ich treścią, poziomem hierarchii oraz numerami linii. Sekcje są kluczowe dla walidacji kompletności dokumentu - każdy typ dokumentu definiuje wymagane sekcje które muszą istnieć.

**Cel Biznesowy**: Wykrywanie brakujących sekcji (gap E110) jest jedną z głównych funkcji systemu. Bez poprawnej identyfikacji sekcji niemożliwa jest walidacja czy dokument zawiera wszystkie wymagane komponenty (np. "## User Personas", "## Functional Requirements"). Identyfikacja sekcji umożliwia również generowanie spisu treści z zakresami linii.

**Acceptance Criteria**:
- [ ] AC-1: System identyfikuje wszystkie nagłówki markdown od poziomu H1 (#) do H6 (######)
- [ ] AC-2: Dla każdej sekcji system ekstrahuje: name (tekst nagłówka), level (1-6), content (treść między tym a następnym nagłówkiem), line_start, line_end
- [ ] AC-3: Sekcje zachowują hierarchię - sekcje niższego poziomu (np. H3) są poprawnie zagnieżdżone w sekcjach wyższego poziomu (H2)
- [ ] AC-4: System zwraca List[Section] gdzie Section jest obiektem dataclass z polami: name, level, content, line_start, line_end
- [ ] AC-5: Puste sekcje (bez treści) są wykrywane i reportowane

**Constraints**:
- Parsowanie musi używać AST z markdown-it-py (nie prostych regex)
- Nagłówki w blokach kodu (```) nie mogą być traktowane jako sekcje
- Nagłówki w cytatach (>) muszą być rozpoznawane jako normalne sekcje
- Numery linii muszą być dokładne (1-indexed)

**Success Metric**:
- 100% sekcji w dokumentach testowych poprawnie zidentyfikowanych
- 100% dokładność wykrywania poziomu sekcji (H1-H6)
- Dokładność numerów linii: ± 0 linii (zero margin of error)

**Mapuje Koncepcje**: C-007 (Parser)

#### FR-004: Detekcja Odniesień

**Opis**: System musi automatycznie wykrywać wszystkie odniesienia do innych dokumentów zarówno w frontmatter YAML (pola dependencies, related) jak i w treści markdown (inline references). Każde odniesienie musi być sklasyfikowane według typu połączenia (requires, implements, references, tested-by, informs) i zmapowane do konkretnego numeru linii dla ułatwienia debugowania.

**Cel Biznesowy**: Automatyczna detekcja odniesień jest fundamentem dla budowania grafu zależności. Zamiast manualnego definiowania wszystkich połączeń, system inteligentnie wykrywa je z samego contentu dokumentów. To redukuje błędy ludzkie i oszczędza czas - wystarczy napisać "dependencies: [BIZ-CASE-001]" a system automatycznie utworzy połączenie typu "requires" w grafie.

**Acceptance Criteria**:
- [ ] AC-1: System wykrywa odniesienia w polach frontmatter: dependencies (lista ID), related (lista ID)
- [ ] AC-2: System wykrywa inline references w markdown body używając wzorców: "[DOC-ID]", "See also: DOC-ID", "Implements: DOC-ID"
- [ ] AC-3: Każde odniesienie zwraca obiekt Reference z polami: target_id (str), type (str), line (int), context (str)
- [ ] AC-4: Typ połączenia jest automatycznie określany: dependencies→"requires", related→"references", implements→"implements", tested-by→"tested-by"
- [ ] AC-5: System raportuje invalid references (ID które nie matchują formatu np. brak myślnika, małe litery)

**Constraints**:
- Format ID dokumentu: uppercase letters, myślnik, cyfry (np. PRD-001, TDD-042, ADR-005)
- Regex pattern dla ID: `[A-Z]+(-[A-Z]+)*-[0-9]+`
- Odniesienia w blokach kodu (```) są ignorowane
- Duplikaty odniesień do tego samego dokumentu są filtrowane

**Success Metric**:
- 100% odniesień z frontmatter wykrytych poprawnie
- ≥ 95% dokładność wykrywania inline references (false positives < 5%)
- Każde odniesienie ma poprawny numer linii (± 0 linii)

**Mapuje Koncepcje**: C-007 (Parser), C-009 (Połączenie)

---

### 4.2 Moduł Validator (FR-005 do FR-008)

**Cel modułu**: Walidacja dokumentów względem schematów typów

**Kluczowe Odpowiedzialności**:
- Walidacja frontmatter YAML
- Sprawdzanie wymaganych sekcji
- Wykrywanie placeholderów
- Walidacja typów połączeń

#### FR-005: Walidacja Schematu Dokumentu

**Opis**: System musi przeprowadzać kompleksową walidację dokumentu względem schematu jego typu (DocumentType). Walidacja obejmuje sprawdzenie frontmatter, wymaganych sekcji, zawartości oraz zgodności z regułami domenowymi. Wynik walidacji to obiekt ValidationResult zawierający listę błędów, ostrzeżeń oraz flag valid (bool).

**Cel Biznesowy**: Automatyczna walidacja eliminuje manualne code review i zapewnia że każdy dokument spełnia standardy jakości przed postępem do kolejnej fazy. To jest kluczowy komponent quality gates - dokument nie może przejść bramki jeśli walidacja zwraca błędy critical severity.

**Acceptance Criteria**:
- [ ] AC-1: System waliduje dokument wywołując sekwencyjnie: validate_frontmatter_schema(), validate_required_sections(), check_placeholders()
- [ ] AC-2: Zwracany obiekt ValidationResult zawiera: valid (bool), document_id (str), errors (List[ValidationError]), warnings (List[ValidationWarning]), timestamp (datetime)
- [ ] AC-3: ValidationError zawiera: type (str), severity (critical|high|medium|low), message (str), location (str), remediation (str)
- [ ] AC-4: valid=True tylko gdy zero errors (warnings nie blokują)
- [ ] AC-5: Każdy błąd ma konkretną lokalizację (frontmatter, line X, section Y) i remediation steps

**Constraints**:
- Walidacja musi używać Pydantic dla type-safe validation
- Schemat DocumentType musi być załadowany z YAML przed walidacją
- Performance: walidacja pojedynczego dokumentu < 100ms
- Walidacja nie modyfikuje dokumentu (read-only operation)

**Success Metric**:
- 100% dokumentów testowych walidowanych poprawnie (zgodnie z oczekiwaniami)
- Zero false positives (dokumenty poprawne nie mogą być flagowane jako invalid)
- Wskaźnik false negatives < 2% (dokumenty z błędami muszą być wykryte)

**Mapuje Koncepcje**: C-006 (Walidator), C-002 (Typ Dokumentu)

#### FR-006: Walidacja Frontmatter

**Opis**: System musi walidować pola YAML frontmatter względem schematu DocumentType, sprawdzając obecność wymaganych pól, poprawność wartości enum, zgodność z wzorcami regex oraz ograniczenia specyficzne dla typu. Walidacja frontmatter jest pierwszym krokiem pełnej walidacji dokumentu.

**Cel Biznesowy**: Frontmatter definiuje metadane kluczowe dla funkcjonowania systemu (id, type, status, owner). Niepoprawny frontmatter uniemożliwia indeksowanie dokumentu, budowanie grafu i wykrywanie luk. Walidacja frontmatter zapewnia że każdy dokument ma kompletne i poprawne metadane.

**Acceptance Criteria**:
- [ ] AC-1: System sprawdza obecność wszystkich required_fields zdefiniowanych w schemacie DocumentType (np. id, title, type, status, owner)
- [ ] AC-2: System waliduje wartości enum - pole status musi być jednym z ["draft", "review", "completed", "archived"], pole priority z ["critical", "high", "medium", "low"]
- [ ] AC-3: System waliduje wzorce regex - pole id musi matchować pattern `[A-Z]+(-[A-Z]+)*-[0-9]+`
- [ ] AC-4: System zwraca List[ValidationError] z dokładną lokalizacją błędu (frontmatter, field name) i sugerowaną poprawką
- [ ] AC-5: System waliduje typy pól - string fields nie mogą być int, list fields nie mogą być string

**Constraints**:
- Pydantic BaseModel musi być użyty do definiowania schematów frontmatter
- Walidacja musi być przeprowadzana zgodnie z YAML 1.2 spec
- Custom validators Pydantic mogą być dodawane dla specyficznych reguł domenowych
- Walidacja nie powinna modyfikować oryginalnego frontmatter dict

**Success Metric**:
- 100% brakujących wymaganych pól wykrytych
- 100% niepoprawnych wartości enum wykrytych
- ≥ 95% niepoprawnych formatów ID wykrytych
- Każdy błąd zawiera sugerowaną poprawkę w polu remediation

**Mapuje Koncepcje**: C-006 (Walidator), C-008 (Metadata)

#### FR-007: Walidacja Wymaganych Sekcji

**Opis**: System musi sprawdzać czy dokument zawiera wszystkie sekcje markdown zdefiniowane jako mandatory w schemacie DocumentType. Każda wymagana sekcja ma pattern (regex) do matchowania nazwy sekcji oraz opcjonalnie min_items (minimalna liczba elementów w sekcji). Brak wymaganej sekcji generuje gap E110.

**Cel Biznesowy**: Kompletność struktury dokumentu jest kluczowa dla jakości dokumentacji. PRD bez sekcji "## Functional Requirements" jest niekompletny. TDD bez "## System Architecture" nie spełnia standardów. Walidacja wymaganych sekcji zapewnia że każdy dokument ma wszystkie niezbędne komponenty przed przejściem quality gate.

**Acceptance Criteria**:
- [ ] AC-1: System iteruje przez wszystkie required_sections ze schematu DocumentType i sprawdza obecność sekcji matchujących pattern
- [ ] AC-2: Dla sekcji z min_items system liczy elementy (np. list items w sekcji "## Functional Requirements") i waliduje czy count >= min_items
- [ ] AC-3: Brak mandatory sekcji generuje ValidationError typu E110 z severity="critical"
- [ ] AC-4: ValidationError zawiera: name wymaganej sekcji, pattern użyty do matchowania, sugerowaną lokalizację (np. "dodaj po sekcji X")
- [ ] AC-5: System raportuje zarówno całkowicie brakujące sekcje jak i sekcje z insufficient items

**Constraints**:
- Pattern matching musi używać regex, nie prostego string equality
- Sekcje muszą być matchowane case-insensitive (np. "## user personas" matchuje pattern "^## User Personas")
- Liczenie items musi obsługiwać markdown lists (- item, * item, 1. item)
- Puste sekcje (tylko nagłówek bez treści) są traktowane jako brakujące

**Success Metric**:
- 100% brakujących mandatory sections wykrytych
- 100% sekcji z insufficient items wykrytych
- Zero false positives (sekcje istniejące nie mogą być flagowane jako brakujące)
- Każdy błąd E110 zawiera konkretny remediation plan

**Mapuje Koncepcje**: C-006 (Walidator)

#### FR-008: Detekcja Placeholderów

**Opis**: System musi automatycznie wykrywać markery placeholderów (TODO, TBD, PLACEHOLDER, XXX, FIXME) w treści markdown i frontmatter, generując gap E120 dla każdego znalezienia. Placeholdery wskazują na niekompletną treść która musi być uzupełniona przed finalizacją dokumentu.

**Cel Biznesowy**: Placeholdery to sygnał że dokument jest w trakcie tworzenia i nie jest gotowy do review lub release. Automatyczna detekcja placeholderów zapobiega sytuacjom gdzie dokument przechodzi quality gate z niekompletną treścią. To jest szczególnie krytyczne dla bramki REQ-FREEZE - żaden PRD z placeholderami nie może być zatwierdzony.

**Acceptance Criteria**:
- [ ] AC-1: System wykrywa następujące wzorce placeholderów (case-insensitive): TODO, TBD, PLACEHOLDER, XXX, FIXME, [Do wypełnienia]
- [ ] AC-2: Dla każdego znalezienia system generuje ValidationError typu E120 z severity określonym kontekstem - placeholder w sekcji critical (np. "## Functional Requirements") ma severity="high", w sekcji informacyjnej (np. "## References") ma severity="medium"
- [ ] AC-3: ValidationError zawiera: exact text placeholdera, numer linii, nazwa sekcji w której znaleziono, kontekst (fragment tekstu wokół)
- [ ] AC-4: Placeholdery w blokach kodu (``` ```) i przykładach są ignorowane (nie generują errors)
- [ ] AC-5: System raportuje summary statistics - total count placeholderów, breakdown by severity

**Constraints**:
- Regex pattern musi matchować całe słowa, nie fragmenty (np. "TODO" ale nie "TODOIST")
- Detekcja musi działać zarówno w plain text jak i w markdown formatting (bold, italic, etc.)
- Placeholdery w komentarach HTML (<!-- TODO -->) muszą być wykrywane
- Performance: < 50ms na przeszukanie dokumentu 1000 linii

**Success Metric**:
- 100% placeholderów wykrytych w testach
- Zero false positives (normalne użycie słów typu "todo list" nie może być flagowane)
- Severity poprawnie przypisane w 100% przypadków (based on section importance)
- Placeholdery w code blocks: 0% false alarms

**Mapuje Koncepcje**: C-006 (Walidator), C-004 (Luka - E120)

---

### 4.3 Moduł Graph Builder (FR-009 do FR-013)

**Cel modułu**: Budowanie i zarządzanie grafem zależności dokumentów

**Kluczowe Odpowiedzialności**:
- Konstrukcja NetworkX DiGraph
- Zarządzanie węzłami i krawędziami
- Detekcja cykli
- Obliczanie emergentnej hierarchii

#### FR-009: Konstrukcja Grafu Zależności

**Opis**: System musi budować skierowany graf zależności (NetworkX DiGraph) z listy sparsowanych dokumentów, gdzie węzły reprezentują dokumenty a krawędzie typowane połączenia między nimi. Graf jest fundamentem dla analizy hierarchii, wykrywania cykli, identyfikacji ścieżek krytycznych oraz wizualizacji relacji w GUI.

**Cel Biznesowy**: Graf zależności jest kluczem do proaktywnego zarządzania projektem. Pozwala automatycznie odpowiedzieć na pytania: "Co blokuje release?", "Które dokumenty są na critical path?", "Czy istnieją cykliczne zależności?". Bez grafu system byłby tylko parserem - z grafem staje się inteligentnym asystentem projektowym.

**Acceptance Criteria**:
- [ ] AC-1: System tworzy NetworkX DiGraph i dodaje węzeł dla każdego dokumentu poprzez wywołanie add_node(graph, document)
- [ ] AC-2: System tworzy krawędzie dla wszystkich odniesień wykrytych przez parser poprzez wywołanie add_edge(graph, from_doc, to_doc, edge_type)
- [ ] AC-3: Po konstrukcji system wywołuje detect_cycles(graph) i loguje warning jeśli wykryto cykliczne zależności
- [ ] AC-4: System wywołuje calculate_hierarchy_levels(graph) aby przypisać emergentny poziom hierarchii każdemu węzłowi
- [ ] AC-5: Zwracany DependencyGraph zawiera: graph (DiGraph), nodes (Dict[str, Node]), edges (List[Connection]), cycles (List), hierarchy_levels (Dict[str, int])

**Constraints**:
- Musi używać biblioteki NetworkX (nie custom implementation)
- Graf musi być directed (DiGraph) nie undirected
- Węzły identyfikowane przez document ID (string) nie obiekty
- Maksymalna skala: 10,000 węzłów, 50,000 krawędzi
- Performance: budowanie grafu dla 100 dokumentów < 2 sekundy

**Success Metric**:
- 100% dokumentów dodanych jako węzły (zero dropped nodes)
- 100% odniesień utworzonych jako krawędzie (zero broken references ignored)
- Cykle wykrywane w 100% przypadków testowych
- Hierarchy levels poprawnie obliczone (walidacja manualnie)

**Mapuje Koncepcje**: C-003 (Graf Zależności)

#### FR-010: Zarządzanie Węzłami

**Opis**: System musi tworzyć i zarządzać węzłami grafu, gdzie każdy węzeł reprezentuje dokument wraz z metadanymi podstawowymi (z frontmatter) oraz obliczonymi (incoming/outgoing connections, hierarchy level, gaps, blockers). Węzły są podstawową jednostką grafu i muszą zawierać wszystkie informacje potrzebne do wizualizacji i analizy.

**Cel Biznesowy**: Węzeł to nie tylko ID dokumentu - to bogaty obiekt zawierający status, priorytet, luki, połączenia oraz pozycję w hierarchii projektu. Metadane obliczone (hierarchy_level, gaps, blockers) są kluczowe dla proaktywnych sugestii - system wie który dokument jest na critical path, który ma najwięcej luk, który blokuje inne dokumenty.

**Acceptance Criteria**:
- [ ] AC-1: Funkcja add_node(graph, document) tworzy węzeł z ID dokumentu i zapisuje wszystkie metadane frontmatter jako atrybuty węzła (type, status, owner, priority, etc.)
- [ ] AC-2: Funkcja create_node(document) zwraca obiekt Node z polami: document_id, document_type, status, metadata (dict), incoming_connections (List), outgoing_connections (List)
- [ ] AC-3: Funkcja calculate_node_properties(node, graph) oblicza właściwości pochodne: hierarchy_level (int), critical_path (bool), gaps (List[Gap]), blockers (List[str])
- [ ] AC-4: Funkcja get_incoming_connections(node, graph) zwraca listę węzłów które mają krawędzie do tego węzła (predecessors)
- [ ] AC-5: Funkcja get_outgoing_connections(node, graph) zwraca listę węzłów do których ten węzeł ma krawędzie (successors)

**Constraints**:
- Metadane węzła muszą być JSON-serializable (dla eksportu do GUI)
- Obliczone właściwości muszą być cache'owane - nie przeliczać przy każdym dostępie
- Węzły bez incoming connections to root nodes (level 0)
- Węzły orphan (bez incoming ani outgoing) muszą być flagowane

**Success Metric**:
- 100% metadanych frontmatter poprawnie zapisanych w węzłach
- Incoming/outgoing connections poprawnie obliczone dla 100% węzłów
- Hierarchy levels poprawnie przypisane (validacja: max(parent_levels) + 1)
- Performance: get_node_properties() < 10ms per node

**Mapuje Koncepcje**: C-010 (Węzeł), C-003 (Graf Zależności)

#### FR-011: Zarządzanie Krawędziami

[**Placeholder**]

#### FR-012: Detekcja Cykli

[**Placeholder**]

#### FR-013: Obliczanie Hierarchii

[**Placeholder**]

---

### 4.4 Gap Detection Engine (FR-014 do FR-020)

**Cel modułu**: Wykrywanie luk w dokumentacji (E110-E160) i generowanie remediacji

**Kluczowe Odpowiedzialności**:
- Detekcja 6 typów luk (E110-E160)
- Kategoryzacja po severity (critical, high, medium, low)
- Generowanie kroków remediacji
- Integracja z TODO satelitami

#### FR-014: E110 Detekcja Brakujących Sekcji

[**Placeholder**]

#### FR-015: E120 Detekcja Placeholderów

[**Placeholder**]

#### FR-016: E130 Detekcja Brakujących Dowodów

[**Placeholder**]

#### FR-017: E140 Detekcja Złamanych Zależności

[**Placeholder**]

#### FR-018: E150 Detekcja Blokerów Bramek

[**Placeholder**]

#### FR-019: E160 Detekcja Brakujących Zatwierdzeń

[**Placeholder**]

#### FR-020: Generowanie Remediacji Luk

[**Placeholder**]

---

### 4.5 Moduł GUI (FR-021 do FR-025)

**Cel modułu**: Interaktywny interfejs graficzny z wizualizacją grafu

[**Placeholders** dla FR-021 do FR-025]

---

### 4.6 Moduł Storage (FR-026 do FR-028)

**Cel modułu**: Persystencja i indeksowanie dokumentów w SQLite

[**Placeholders** dla FR-026 do FR-028]

---

### 4.7 Moduł File Watcher (FR-029 do FR-030)

**Cel modułu**: Monitorowanie zmian w plikach i automatyczna re-analiza

[**Placeholders** dla FR-029 do FR-030]

---

### 4.8 Moduł Proactive Assistant (FR-031 do FR-033)

**Cel modułu**: Proaktywne sugestie i wykrywanie brakujących dokumentów

[**Placeholders** dla FR-031 do FR-033]

---

### 4.9 Moduł Satellite Documents (FR-034 do FR-038)

**Cel modułu**: Automatyczne generowanie i zarządzanie dokumentami satelitarnymi

[**Placeholders** dla FR-034 do FR-038]

---

### 4.10 Moduł Domain (FR-039 do FR-040)

**Cel modułu**: Rejestracja domen i zastosowanie reguł walidacji specyficznych dla domeny

[**Placeholders** dla FR-039 do FR-040]

---

## 5. Wymagania Niefunkcjonalne

### 5.1 Wymagania Wydajnościowe (NFR-001 do NFR-003)

#### NFR-001: Wydajność Parsowania

**Requirement**: System musi parsować pojedynczy dokument w < 50ms, 100 dokumentów w < 5 sekund

**Pomiar**: [Do wypełnienia]

**Priorytet**: Critical

---

#### NFR-002: Wydajność Budowania Grafu

[**Placeholder**]

#### NFR-003: Responsywność GUI

[**Placeholder**]

---

### 5.2 Wymagania Niezawodności (NFR-004 do NFR-005)

[**Placeholders** dla NFR-004 do NFR-005]

### 5.3 Wymagania Skalowalności (NFR-006 do NFR-007)

[**Placeholders** dla NFR-006 do NFR-007]

### 5.4 Wymagania Użyteczności (NFR-008 do NFR-009)

[**Placeholders** dla NFR-008 do NFR-009]

### 5.5 Wymagania Utrzymywalności (NFR-010 do NFR-011)

[**Placeholders** dla NFR-010 do NFR-011]

### 5.6 Wymagania Bezpieczeństwa (NFR-012)

[**Placeholder** dla NFR-012]

### 5.7 Wymagania Kompatybilności (NFR-013 do NFR-014)

[**Placeholders** dla NFR-013 do NFR-014]

### 5.8 Wymagania Rozszerzalności (NFR-015)

[**Placeholder** dla NFR-015]

---

## 6. User Stories

### 6.1 Developer Stories (US-001 do US-003)

#### US-001: Parsuj i Waliduj Dokument

**Jako** Programista Python,
**Chcę** parsować i automatycznie walidować pliki markdown,
**Żeby** wykryć błędy wcześnie i zaoszczędzić czas.

**Acceptance Criteria**:
- [ ] [Do wypełnienia]

**Related FR**: FR-001, FR-002, FR-005

---

#### US-002: Śledź Zależności Wymagań

[**Placeholder**]

#### US-003: Wykryj Brakującą Dokumentację

[**Placeholder**]

---

### 6.2 Product Manager Stories (US-004 do US-006)

[**Placeholders** dla US-004 do US-006]

### 6.3 QA Engineer Stories (US-007 do US-008)

[**Placeholders** dla US-007 do US-008]

### 6.4 Technical Writer Stories (US-009 do US-010)

[**Placeholders** dla US-009 do US-010]

---

## 7. Bramki Jakości & Kryteria Akceptacji

### 7.1 Definicje Bramek Jakości

#### REQ-FREEZE Gate

**Cel**: Zamrożenie wymagań przed rozpoczęciem designu

**Warunki**:
- [ ] PRD status = "review" lub "approved"
- [ ] Wszystkie wymagane sekcje PRD obecne
- [ ] Zero placeholderów TODO/TBD w sekcjach krytycznych
- [ ] RTM-001 zainicjalizowane
- [ ] Zatwierdzenie stakeholderów uzyskane

**Blokery**: [Do wypełnienia przy analizie]

---

### 7.2 Kryteria Akceptacji per FR

[**Do wypełnienia**: Zbiorczy widok wszystkich AC z FR-001 do FR-040]

### 7.3 Przegląd Strategii Testowania

[**Do wypełnienia**: High-level opis jak będą testowane wymagania]

---

## 8. Ograniczenia Techniczne & Zależności

### 8.1 Stos Technologiczny

**Wymagane technologie**:
- Python 3.11+
- PySide6 (Qt dla Python)
- NetworkX (analiza grafów)
- SQLite (storage)
- Watchdog (file monitoring)
- python-frontmatter (YAML parsing)
- markdown-it-py (markdown parsing)
- Pydantic (walidacja)

### 8.2 Zależności Zewnętrzne

[**Do wypełnienia**: Biblioteki third-party, usługi]

### 8.3 Wymagania Systemowe

**Minimalne wymagania**:
- Python 3.11 lub nowszy
- 2 GB RAM
- 500 MB miejsca na dysku
- Linux, macOS, lub Windows 10+

### 8.4 Punkty Integracji

[**Do wypełnienia**: Zewnętrzne systemy z którymi integrujemy, API]

---

## 9. Macierz Mapowania Koncepcji

### 9.1 Mapowanie Koncepcje → FR

| Koncepcja ID | Nazwa Koncepcji | FR IDs | Moduł | Priorytet |
|--------------|----------------|--------|-------|-----------|
| C-001 | Dokument | FR-001, FR-002, FR-003, FR-004, FR-026 | Parser, Storage | Critical |
| C-002 | Typ Dokumentu | FR-005, FR-006, FR-027 | Validator, Storage | Critical |
| C-003 | Graf Zależności | FR-009, FR-010, FR-011, FR-012, FR-013, FR-028 | Graph Builder | Critical |
| C-004 | Luka | FR-014, FR-015, FR-016, FR-017, FR-018, FR-019, FR-020, FR-029 | Gap Engine | Critical |
| C-005 | Bramka Jakości | FR-030, FR-031 | Proactive Assistant | High |
| C-006 | Walidator | FR-005, FR-006, FR-007, FR-008, FR-032 | Validator | Critical |
| C-007 | Parser | FR-001, FR-002, FR-003, FR-004 | Parser | Critical |
| C-008 | Metadata (Frontmatter) | FR-002, FR-006, FR-033 | Parser, Validator | Critical |
| C-009 | Połączenie (Edge) | FR-011, FR-034 | Graph Builder | High |
| C-010 | Węzeł (Node) | FR-010, FR-035 | Graph Builder | High |
| C-011 | Satelita | FR-036, FR-037, FR-038 | Satellite Module | Medium |
| C-012 | Domena | FR-039, FR-040 | Domain Module | Medium |

**Pokrycie**: Wszystkie 12 koncepcji z CONCEPTS-001 zmapowane na 40 wymagań funkcjonalnych ✓

---

### 9.2 Mapowanie FR → Moduł

| FR ID | Requirement | Moduł Python | Ścieżka Pliku | Priorytet |
|-------|-------------|--------------|---------------|-----------|
| FR-001 | Parsowanie Plików Markdown | parser.py | src/core/parser.py | Critical |
| FR-002 | Ekstrakcja YAML Frontmatter | parser.py | src/core/parser.py | Critical |
| FR-003 | Identyfikacja Sekcji | parser.py | src/core/parser.py | Critical |
| FR-004 | Detekcja Odniesień | parser.py | src/core/parser.py | High |
| FR-005 | Walidacja Schematu Dokumentu | validator.py | src/core/validator.py | Critical |
| ... | [Do uzupełnienia] | ... | ... | ... |

---

### 9.3 Mapowanie FR → Test

[**Do wypełnienia**: Tabela FR ID → Test Type → Test File → Test Count]

---

## 10. Dodatki & Referencje

### 10.1 Glosariusz

**AST (Abstract Syntax Tree)**: Drzewo składniowe reprezentujące strukturę markdown

**Frontmatter**: Metadata YAML na początku pliku markdown

**Gap**: Wykryta luka lub niespójność w dokumentacji

**Quality Gate**: Punkt kontrolny wymagający spełnienia kryteriów przed postępem

**RTM (Requirements Traceability Matrix)**: Macierz śledząca mapowanie wymagań do designu/impl/testów

[**Do wypełnienia**: Dodatkowe terminy]

---

### 10.2 Referencje

- **EXEC-SUM-001**: `/docs/pre-production/executive-summary.md`
- **BIZ-CASE-001**: `/docs/pre-production/business-case.md`
- **VISION-001**: `/docs/pre-production/vision.md`
- **CONCEPTS-001**: `/docs/engineering/koncepcje.md`
- **Plan Implementacji**: `/home/jerzy/.claude/plans/lively-crunching-milner.md`

---

### 10.3 Log Zmian

| Data | Wersja | Autor | Zmiany |
|------|--------|-------|--------|
| 2025-12-26 | 0.1 | Zespół Produktowy | Utworzenie szkieletu PRD |
| 2025-12-26 | 0.2 | Zespół Produktowy | Wypełnienie 10 core FR: Parser (FR-001 do FR-004), Validator (FR-005 do FR-008), Graph Builder (FR-009 do FR-010) |

---

**Status**: Draft - 10 core FR ukończone (Parser, Validator, Graph Builder), pozostałe 30 FR oczekują na wypełnienie
**Ostatnia Aktualizacja**: 2025-12-26
**Ukończone Sekcje**:
- ✅ Moduł Parser (FR-001 do FR-004) - 100% szczegółów wypełnionych
- ✅ Moduł Validator (FR-005 do FR-008) - 100% szczegółów wypełnionych
- ✅ Moduł Graph Builder (FR-009 do FR-010) - Pierwsze 2 z 5 wymagań wypełnione

**Następne Kroki**:
1. Review pierwszych 10 FR z użytkownikiem
2. Po zatwierdzeniu - wypełnić pozostałe FR (FR-011 do FR-040)
3. Wypełnić sekcje NFR i US
4. Utworzyć satelity (TODO, DOR, DOD, RTM)
