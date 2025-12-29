---
id: CONCEPTS-001
title: "Dokument Koncepcje - System Zarządzania Dokumentacją w Pythonie"
type: concepts
domain: documentation
status: deprecated
created: 2025-12-26
updated: 2025-12-26
owner: Zespół Architektoniczny
phase: design
priority: critical
dependencies:
  - EXEC-SUM-001
  - BIZ-CASE-001
  - VISION-001
related:
  - PRD-001
  - TDD-001
deprecation_date: 2025-12-20
superseded_by: "CONCEPTS-V2"
migration_guide: "Zobacz CONCEPTS-V2 dla podejścia proof system"
---

# Dokument Koncepcje: System Zarządzania Dokumentacją w Pythonie

## Cel Dokumentu

Ten dokument definiuje wszystkie kluczowe koncepcje systemu, mapuje je na konkretne funkcje implementacyjne, oraz opisuje jak każda funkcja powinna działać. Jest to pomost między wizją strategiczną a implementacją techniczną.

---

## Część 1: Definicje Koncepcji

### 1.1 Dokument (Document)

**Definicja**: Podstawowa jednostka wiedzy w systemie. Plik markdown (.md) z metadanymi w formacie YAML frontmatter oraz strukturalnym contentem.

**Właściwości**:
- **ID**: Unikalny identyfikator (np. PRD-001, TDD-042)
- **Typ**: Kategoria dokumentu określająca schemat (np. PRD, TDD, ADR)
- **Status**: Stan w cyklu życia (draft, review, completed, archived)
- **Frontmatter**: Metadata YAML na początku pliku
- **Sekcje**: Strukturalne części contentu (## headings)
- **Zależności**: Odniesienia do innych dokumentów
- **Połączenia**: Typowane relacje z innymi dokumentami

**Przykład frontmatter**:
```yaml
---
id: PRD-001
title: "Product Requirements Document - Parser Module"
type: prd
domain: engineering
status: draft
created: 2025-12-26
owner: Team Lead
priority: critical
dependencies:
  - BIZ-CASE-001
related:
  - TDD-001
---
```

### 1.2 Typ Dokumentu (Document Type)

**Definicja**: Szablon określający strukturę, wymagane sekcje, dozwolone połączenia oraz reguły walidacji dla danej kategorii dokumentów.

**Właściwości**:
- **ID typu**: Unikalny identyfikator typu (np. "prd", "tdd", "adr")
- **Nazwa**: Czytelna nazwa (np. "Product Requirements Document")
- **Domena**: Logiczna grupa (requirements, architecture, testing, operations)
- **Schemat frontmatter**: Wymagane i opcjonalne pola YAML
- **Wymagane sekcje**: Lista obowiązkowych sekcji markdown
- **Dozwolone połączenia**: Typy wychodzących i przychodzących relacji
- **Reguły walidacji**: Constraints dla pól i sekcji

**Przykład definicji typu**:
```yaml
document_types:
  - id: "prd"
    name: "Product Requirements Document"
    domain: "requirements"
    frontmatter_schema:
      required_fields: [id, title, type, status, owner]
      optional_fields: [priority, dependencies, related]
      field_constraints:
        status:
          enum: ["draft", "review", "req-freeze", "approved"]
    required_sections:
      - name: "User Personas"
        pattern: "^## User Personas"
        mandatory: true
      - name: "Functional Requirements"
        pattern: "^## Functional Requirements"
        mandatory: true
        min_items: 10
    allowed_connections:
      outbound:
        - type: "requires"
          target_types: ["business-case", "vision"]
        - type: "informs"
          target_types: ["tdd", "test-plan"]
```

### 1.3 Graf Zależności (Dependency Graph)

**Definicja**: Skierowany graf reprezentujący relacje między dokumentami. Węzły to dokumenty, krawędzie to typowane połączenia.

**Właściwości**:
- **Węzły (Nodes)**: Dokumenty z metadanymi
- **Krawędzie (Edges)**: Typowane połączenia między dokumentami
- **Kierunkowość**: Graf skierowany (dependency flow)
- **Cykle**: System wykrywa i raportuje cykliczne zależności
- **Ścieżki krytyczne**: Identyfikacja łańcuchów blokujących
- **Poziomy hierarchii**: Wyliczane automatycznie z grafu

**Typy połączeń**:
1. **requires** (wymaga): Twarda zależność - dokument A nie może być ukończony bez dokumentu B
2. **implements** (implementuje): Dokument realizuje wymagania z innego dokumentu
3. **references** (odnosi się): Miękka zależność - kontekst, nie bloker
4. **tested-by** (testowany przez): Połączenie wymaganie → test case
5. **informs** (informuje): Dokument dostarcza kontekst dla innego

**Przykład grafu**:
```
BIZ-CASE-001 --[requires]--> EXEC-SUM-001
BIZ-CASE-001 --[informs]--> PRD-001
PRD-001 --[requires]--> BIZ-CASE-001
PRD-001 --[informs]--> TDD-001
TDD-001 --[requires]--> PRD-001 (status: req-freeze)
TDD-001 --[implements]--> PRD-001
TEST-PLAN-001 --[requires]--> PRD-001
<!-- TEST-PLAN-001 --[tested-by]--> TEST-CASES-001 (planned) -->
```

### 1.4 Luka (Gap)

**Definicja**: Wykryta niespójność, brak lub niekompletność w dokumentacji, która blokuje jakość lub postęp projektu.

**Typy luk**:
- **E110 - Brakująca Sekcja**: Wymagana sekcja nie istnieje w dokumencie
- **E120 - Placeholder**: Wykryto marker TODO, TBD, PLACEHOLDER
- **E130 - Brakujący Dowód**: Dokument wymaga satelity (evidence) której brakuje
- **E140 - Złamana Zależność**: Odniesienie do nieistniejącego lub niepoprawnego dokumentu
- **E150 - Bloker Bramki**: Dokument nie spełnia wymagań quality gate
- **E160 - Brakujące Zatwierdzenie**: Brak approval dla krytycznego dokumentu

**Właściwości**:
- **ID**: Unikalny identyfikator luki
- **Typ**: Kategoria (E110-E160)
- **Severity**: critical, high, medium, low
- **Dokument źródłowy**: Gdzie wykryto lukę
- **Opis**: Co dokładnie brakuje
- **Remediacja**: Kroki do naprawy
- **Status**: open, in-progress, resolved, false-positive

**Przykład luki**:
```json
{
  "id": "GAP-PRD-001-E110-001",
  "type": "E110",
  "severity": "critical",
  "source_document": "PRD-001",
  "description": "Brakująca wymagana sekcja: 'Acceptance Criteria'",
  "remediation": [
    "Dodać sekcję '## Acceptance Criteria' do PRD-001",
    "Zdefiniować AC dla każdego user story",
    "Uzyskać akceptację od stakeholderów"
  ],
  "status": "open",
  "detected_at": "2025-12-26T10:30:00Z"
}
```

### 1.5 Bramka Jakości (Quality Gate)

**Definicja**: Punkt kontrolny w procesie projektowym, który wymaga spełnienia określonych kryteriów przed postępem do kolejnej fazy.

**Główne bramki**:
1. **STRATEGIC-APPROVAL**: Po Executive Summary, Business Case, Vision
2. **REQ-FREEZE**: Po PRD - zamrożenie wymagań przed designem
3. **DESIGN-COMPLETE**: Po TDD, ADRs - design zatwierdzony przed implementacją
4. **IMPL-READY**: Przed rozpoczęciem sprintu - wszystkie zależności gotowe
5. **RELEASE-READY**: Przed wdrożeniem - testy, dokumentacja ops kompletna
6. **OPS-HANDOVER**: Przekazanie do ops - runbooki, monitoring gotowe

**Właściwości bramki**:
- **ID**: Identyfikator bramki
- **Nazwa**: Czytelna nazwa
- **Warunki**: Lista kryteriów do spełnienia
- **Blokery**: Dokumenty lub luki blokujące przejście
- **Status**: blocked, ready, passed
- **Wymagane zatwierdzenia**: Role które muszą zaaprobować

**Przykład bramki**:
```yaml
quality_gates:
  - id: "REQ-FREEZE"
    name: "Requirements Freeze"
    phase: "requirements → design"
    conditions:
      - PRD status == "review" OR "approved"
      - All required PRD sections present
      - No TODO/TBD placeholders in PRD
      - RTM initialized
      - Stakeholder approval obtained
    blockers:
      - type: "document"
        id: "PRD-001"
        reason: "Status still 'draft', missing sections"
      - type: "gap"
        id: "GAP-PRD-001-E120-003"
        reason: "Placeholder detected in Functional Requirements"
    status: "blocked"
```

### 1.6 Walidator (Validator)

**Definicja**: Komponent odpowiedzialny za weryfikację dokumentu względem schematu typu dokumentu oraz reguł domenowych.

**Typy walidacji**:
1. **Walidacja frontmatter**: Sprawdzenie wymaganych pól YAML
2. **Walidacja sekcji**: Sprawdzenie obecności wymaganych sekcji markdown
3. **Walidacja zawartości**: Wykrywanie placeholderów, pustych sekcji
4. **Walidacja połączeń**: Sprawdzenie czy połączenia są zgodne z allowed_connections
5. **Walidacja zależności**: Czy dokumenty dependency istnieją i mają poprawny status
6. **Walidacja bramek**: Czy dokument spełnia kryteria quality gate

**Wyjście walidacji**:
```python
ValidationResult(
    valid=False,
    document_id="PRD-001",
    errors=[
        ValidationError(
            type="MISSING_SECTION",
            severity="critical",
            message="Brakuje wymaganej sekcji: 'Acceptance Criteria'",
            location="document_body",
            remediation="Dodaj sekcję ## Acceptance Criteria"
        ),
        ValidationError(
            type="PLACEHOLDER_DETECTED",
            severity="high",
            message="Znaleziono placeholder 'TODO' w sekcji Functional Requirements",
            location="line 45",
            remediation="Uzupełnij treść lub usuń placeholder"
        )
    ],
    warnings=[
        ValidationWarning(
            message="Opcjonalna sekcja 'Risk Analysis' nie została dodana"
        )
    ]
)
```

### 1.7 Parser

**Definicja**: Komponent ekstrahujący strukturalne informacje z plików markdown, w tym frontmatter YAML, sekcje, oraz zawartość.

**Fazy parsowania**:
1. **Ekstrakcja frontmatter**: Odczyt YAML z początku pliku
2. **Parsowanie markdown**: Konwersja markdown do AST (Abstract Syntax Tree)
3. **Identyfikacja sekcji**: Wykrycie nagłówków (## Heading)
4. **Ekstrakcja metadanych**: Pobranie ID, typu, statusu, zależności
5. **Analiza połączeń**: Identyfikacja odniesień do innych dokumentów

**Wyjście parsera**:
```python
ParsedDocument(
    file_path="/docs/engineering/prd.md",
    frontmatter={
        "id": "PRD-001",
        "type": "prd",
        "status": "draft",
        "dependencies": ["BIZ-CASE-001"]
    },
    sections=[
        Section(name="User Personas", level=2, content="...", line_start=15),
        Section(name="Functional Requirements", level=2, content="...", line_start=45)
    ],
    references=[
        Reference(target_id="BIZ-CASE-001", type="requires", line=8),
        Reference(target_id="TDD-001", type="informs", line=120)
    ],
    ast=MarkdownAST(...)
)
```

### 1.8 Metadata (Frontmatter)

**Definicja**: Strukturalne metadane w formacie YAML na początku każdego dokumentu markdown, określające właściwości dokumentu.

**Standardowe pola**:
- **id** (wymagane): Unikalny identyfikator dokumentu
- **title** (wymagane): Tytuł dokumentu
- **type** (wymagane): Typ dokumentu (prd, tdd, adr, itp.)
- **domain** (opcjonalne): Domena (requirements, architecture, testing, operations)
- **status** (wymagane): Stan dokumentu (draft, review, completed, archived)
- **created** (opcjonalne): Data utworzenia
- **updated** (opcjonalne): Data ostatniej modyfikacji
- **owner** (wymagane): Osoba/zespół odpowiedzialny
- **phase** (opcjonalne): Faza projektu (discovery, design, development, operations)
- **priority** (opcjonalne): Priorytet (critical, high, medium, low)
- **dependencies** (opcjonalne): Lista ID dokumentów które są wymagane
- **related** (opcjonalne): Lista ID dokumentów powiązanych

**Rozszerzenia domenowe**:
Różne typy dokumentów mogą mieć dodatkowe pola specyficzne dla domeny.

### 1.9 Połączenie (Connection/Edge)

**Definicja**: Typowana relacja między dwoma dokumentami w grafie zależności.

**Struktura połączenia**:
```python
Connection(
    from_document="PRD-001",
    to_document="BIZ-CASE-001",
    connection_type="requires",
    metadata={
        "mandatory": True,
        "status_constraint": "completed",  # BIZ-CASE-001 musi być completed
        "gate": "REQ-FREEZE"
    }
)
```

**Reguły połączeń**:
- **Typowanie**: Każdy typ dokumentu definiuje allowed_connections
- **Walidacja kierunku**: Outbound vs inbound connections
- **Constraints statusu**: Niektóre połączenia wymagają określonego statusu dokumentu docelowego
- **Wykrywanie cykli**: System raportuje cykliczne zależności jako błąd

### 1.10 Węzeł (Node)

**Definicja**: Reprezentacja dokumentu w grafie zależności wraz z metadanymi obliczonymi.

**Właściwości węzła**:
```python
Node(
    document_id="PRD-001",
    document_type="prd",
    status="draft",
    metadata={...},

    # Obliczone
    incoming_connections=["BIZ-CASE-001 --requires--> PRD-001"],
    outgoing_connections=["PRD-001 --informs--> TDD-001"],
    hierarchy_level=2,  # Wyliczone z grafu
    critical_path=True,
    gaps=[GAP-PRD-001-E110-001, GAP-PRD-001-E120-003],
    blockers=[],
    next_steps=["Uzupełnij sekcję Acceptance Criteria"]
)
```

### 1.11 Satelita (Satellite Document)

**Definicja**: Pomocniczy dokument wspierający dokument główny - TODOs, Evidence, Approvals, Definition of Ready/Done.

**Typy satelitów**:
1. **TODO**: Konkretne zadania do wykonania dla dokumentu głównego
2. **EVIDENCE**: Dowody, badania, benchmarki wspierające decyzje
3. **APPROVAL**: Formalne zatwierdzenia od stakeholderów
4. **DOR**: Definition of Ready - kryteria gotowości
5. **DOD**: Definition of Done - kryteria kompletności
6. **RTM**: Requirements Traceability Matrix

**Przykład TODO satelity**:
```yaml
---
id: TODO-PRD-001-TASK-001
title: "Uzupełnij sekcję Acceptance Criteria"
type: todo
parent_document: PRD-001
status: open
priority: high
assigned_to: Product Owner
due_date: 2025-12-28
---

## Zadanie

Dodać sekcję "## Acceptance Criteria" do PRD-001 z AC dla każdego user story.

## Acceptance Criteria

- [ ] Sekcja utworzona w PRD-001
- [ ] AC zdefiniowane dla wszystkich 15 user stories
- [ ] Każde AC jest testowalne (Given/When/Then)
- [ ] Stakeholderzy zaaprobowali AC
```

### 1.12 Domena (Domain)

**Definicja**: Logiczna grupa typów dokumentów oraz reguł walidacji specyficznych dla danej kategorii.

**Główne domeny**:
1. **Requirements**: PRD, User Stories, Use Cases
2. **Architecture**: TDD, ADR, System Architecture, Data Model
3. **Implementation**: Sprint Plans, DoR/DoD, Implementation Guides
4. **Testing**: Test Plans, Test Cases, Test Reports
5. **Operations**: Deployment Guides, Runbooks, Monitoring Plans

**Struktura domeny**:
```python
Domain(
    id="requirements",
    name="Requirements Domain",
    document_types=["prd", "user-story", "use-case"],
    validation_rules=[
        Rule("Requirements must have acceptance criteria"),
        Rule("Requirements must be traceable to business case")
    ],
    quality_gates=["REQ-FREEZE"],
    gap_detectors=[MissingACDetector, PlaceholderDetector]
)
```

---

## Część 2: Mapowanie Koncepcje → Funkcje

### 2.1 Dokument

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `parse_document(file_path)` | Parsowanie pliku markdown + frontmatter |
| `validate_document(document, schema)` | Walidacja względem schematu typu |
| `get_metadata(document)` | Ekstrakcja metadanych z frontmatter |
| `extract_sections(document)` | Identyfikacja sekcji markdown |
| `get_document_status(document)` | Pobranie statusu dokumentu |
| `update_document_status(document, new_status)` | Aktualizacja statusu |
| `get_dependencies(document)` | Lista dokumentów dependency |
| `save_document(document, file_path)` | Zapis dokumentu do pliku |

### 2.2 Typ Dokumentu

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `load_document_type(type_id)` | Ładowanie definicji typu z YAML |
| `get_required_sections(doc_type)` | Lista wymaganych sekcji |
| `get_allowed_connections(doc_type)` | Dozwolone typy połączeń |
| `validate_frontmatter(frontmatter, doc_type)` | Walidacja YAML względem schematu |
| `get_validation_rules(doc_type)` | Reguły walidacji dla typu |
| `instantiate_document(doc_type, params)` | Utworzenie nowego dokumentu z szablonu |

### 2.3 Graf Zależności

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `build_graph(documents)` | Budowanie grafu z listy dokumentów |
| `add_node(graph, document)` | Dodanie węzła do grafu |
| `add_edge(graph, from_doc, to_doc, edge_type)` | Dodanie połączenia |
| `detect_cycles(graph)` | Wykrywanie cyklicznych zależności |
| `find_dependencies(graph, node_id)` | Znalezienie zależności węzła |
| `calculate_hierarchy_levels(graph)` | Wyliczenie poziomów hierarchii |
| `find_critical_path(graph)` | Identyfikacja ścieżki krytycznej |
| `get_descendants(graph, node_id)` | Wszystkie potomkowie węzła |
| `get_ancestors(graph, node_id)` | Wszystkie przodkowie węzła |
| `visualize_graph(graph)` | Eksport grafu do Cytoscape.js |

### 2.4 Luka

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `detect_gaps(document, doc_type, graph)` | Wykrycie wszystkich luk w dokumencie |
| `detect_missing_sections(document, doc_type)` | Wykrycie E110 |
| `detect_placeholders(document)` | Wykrycie E120 (TODO, TBD) |
| `detect_missing_evidence(document)` | Wykrycie E130 |
| `detect_broken_dependencies(document, graph)` | Wykrycie E140 |
| `detect_gate_blockers(document, gate)` | Wykrycie E150 |
| `detect_missing_approvals(document)` | Wykrycie E160 |
| `generate_remediation(gap)` | Wygenerowanie kroków naprawy |
| `categorize_gap(gap)` | Przypisanie severity |
| `get_gap_stats()` | Statystyki luk (total, open, resolved) |

### 2.5 Bramka Jakości

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `evaluate_gate(gate_id, documents, gaps)` | Sprawdzenie statusu bramki |
| `get_gate_conditions(gate_id)` | Lista warunków bramki |
| `get_gate_blockers(gate_id)` | Dokumenty/luki blokujące |
| `check_gate_ready(gate_id)` | Czy bramka gotowa do przejścia |
| `approve_gate(gate_id, approver)` | Zatwierdzenie bramki |
| `get_required_approvals(gate_id)` | Wymagane zatwierdzenia |

### 2.6 Walidator

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `validate(document, doc_type)` | Pełna walidacja dokumentu |
| `validate_frontmatter_schema(frontmatter, schema)` | Walidacja YAML |
| `validate_required_sections(document, doc_type)` | Walidacja sekcji |
| `validate_connections(document, doc_type, graph)` | Walidacja połączeń |
| `validate_dependencies(document, graph)` | Walidacja zależności |
| `check_placeholders(content)` | Wykrywanie TODO/TBD |
| `validate_status_constraints(document, graph)` | Walidacja constraints statusu |

### 2.7 Parser

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `parse(file_path)` | Pełne parsowanie pliku |
| `extract_frontmatter(content)` | Ekstrakcja YAML frontmatter |
| `parse_yaml(yaml_str)` | Parsowanie YAML do dict |
| `parse_markdown_to_ast(content)` | Markdown → AST |
| `extract_sections_from_ast(ast)` | Identyfikacja sekcji |
| `find_references(content)` | Znalezienie odniesień do innych dokumentów |
| `extract_metadata_from_frontmatter(frontmatter)` | Pobranie metadanych |

### 2.8 Metadata (Frontmatter)

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `get_field(frontmatter, field_name)` | Pobranie wartości pola |
| `set_field(frontmatter, field_name, value)` | Ustawienie wartości pola |
| `validate_required_fields(frontmatter, required)` | Sprawdzenie wymaganych pól |
| `get_document_id(frontmatter)` | Pobranie ID dokumentu |
| `get_document_type(frontmatter)` | Pobranie typu dokumentu |
| `get_dependencies_list(frontmatter)` | Lista zależności |

### 2.9 Połączenie (Connection/Edge)

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `create_connection(from_doc, to_doc, conn_type)` | Utworzenie połączenia |
| `validate_connection(connection, doc_types)` | Walidacja dozwolonego połączenia |
| `get_connection_metadata(connection)` | Pobranie metadata połączenia |
| `check_status_constraint(connection, graph)` | Sprawdzenie constraints statusu |

### 2.10 Węzeł (Node)

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `create_node(document)` | Utworzenie węzła z dokumentu |
| `get_incoming_connections(node, graph)` | Połączenia przychodzące |
| `get_outgoing_connections(node, graph)` | Połączenia wychodzące |
| `calculate_hierarchy_level(node, graph)` | Wyliczenie poziomu w hierarchii |
| `is_on_critical_path(node, graph)` | Czy węzeł na ścieżce krytycznej |
| `get_node_gaps(node)` | Luki węzła |
| `get_next_steps(node, gaps)` | Sugerowane następne kroki |

### 2.11 Satelita (Satellite Document)

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `create_satellite(parent_doc, satellite_type)` | Utworzenie satelity |
| `link_satellite_to_parent(satellite, parent)` | Połączenie satelita → parent |
| `get_satellites(document)` | Lista satelitów dokumentu |
| `generate_todo_from_gap(gap)` | Wygenerowanie TODO z luki |

### 2.12 Domena (Domain)

**Funkcje implementujące koncepcję**:

| Funkcja | Odpowiedzialność |
|---------|------------------|
| `register_domain(domain)` | Rejestracja domeny w systemie |
| `get_domain_by_doc_type(doc_type)` | Znalezienie domeny dla typu |
| `get_domain_validation_rules(domain)` | Reguły walidacji domeny |
| `get_domain_gap_detectors(domain)` | Gap detectors domeny |

---

## Część 3: Specyfikacje Funkcji

### 3.1 Parser Module

#### `parse_document(file_path: str) -> ParsedDocument`

**Cel**: Parsowanie pliku markdown z frontmatter YAML do strukturalnego obiektu.

**Parametry wejściowe**:
- `file_path` (str): Absolutna ścieżka do pliku .md

**Wartość zwracana**:
- `ParsedDocument`: Obiekt zawierający frontmatter, sekcje, references, AST

**Algorytm**:
1. Odczytaj plik z dysku
2. Wywołaj `extract_frontmatter(content)` → (frontmatter_yaml, body)
3. Wywołaj `parse_yaml(frontmatter_yaml)` → frontmatter_dict
4. Wywołaj `parse_markdown_to_ast(body)` → ast
5. Wywołaj `extract_sections_from_ast(ast)` → sections[]
6. Wywołaj `find_references(body)` → references[]
7. Utwórz obiekt ParsedDocument z wszystkimi składowymi
8. Zwróć ParsedDocument

**Obsługa błędów**:
- `FileNotFoundError`: Plik nie istnieje
- `YAMLParseError`: Niepoprawny YAML w frontmatter
- `MarkdownParseError`: Niepoprawny markdown

**Przykład użycia**:
```python
parsed = parse_document("/docs/engineering/prd.md")
print(parsed.frontmatter["id"])  # "PRD-001"
print(len(parsed.sections))      # 8
```

---

#### `extract_frontmatter(content: str) -> Tuple[str, str]`

**Cel**: Ekstrakcja YAML frontmatter z początku pliku markdown.

**Parametry wejściowe**:
- `content` (str): Pełna zawartość pliku markdown

**Wartość zwracana**:
- `Tuple[str, str]`: (frontmatter_yaml, markdown_body)

**Algorytm**:
1. Sprawdź czy content zaczyna się od `---`
2. Jeśli nie - zwróć ("", content)
3. Znajdź drugi `---` (koniec frontmatter)
4. Wyodrębnij frontmatter (między dwoma `---`)
5. Wyodrębnij body (po drugim `---`)
6. Zwróć (frontmatter, body)

**Przykład**:
```python
content = """---
id: PRD-001
type: prd
---

## Section 1
Content here.
"""

frontmatter, body = extract_frontmatter(content)
# frontmatter = "id: PRD-001\ntype: prd"
# body = "\n## Section 1\nContent here."
```

---

#### `parse_markdown_to_ast(content: str) -> MarkdownAST`

**Cel**: Parsowanie markdown do Abstract Syntax Tree używając markdown-it-py.

**Parametry wejściowe**:
- `content` (str): Markdown body (bez frontmatter)

**Wartość zwracana**:
- `MarkdownAST`: Drzewo składniowe markdown

**Algorytm**:
1. Utwórz parser: `md = MarkdownIt()`
2. Parsuj: `tokens = md.parse(content)`
3. Utwórz AST z tokens
4. Zwróć AST

**Biblioteka**: `markdown-it-py`

---

#### `extract_sections_from_ast(ast: MarkdownAST) -> List[Section]`

**Cel**: Identyfikacja sekcji (## headings) z AST markdown.

**Parametry wejściowe**:
- `ast` (MarkdownAST): Drzewo składniowe markdown

**Wartość zwracana**:
- `List[Section]`: Lista sekcji z nazwą, poziomem, contentem

**Algorytm**:
1. Iteruj przez tokeny AST
2. Dla każdego tokenu typu "heading":
   - Wyciągnij poziom (level: 1-6)
   - Wyciągnij tekst nagłówka (name)
   - Wyciągnij numer linii (line_start)
3. Dla każdej sekcji:
   - Znajdź content (tekst między tym heading a następnym)
4. Utwórz listę Section obiektów
5. Zwróć sections

**Struktura Section**:
```python
@dataclass
class Section:
    name: str           # "User Personas"
    level: int          # 2 (dla ##)
    content: str        # Pełna treść sekcji
    line_start: int     # 15
    line_end: int       # 44
```

---

#### `find_references(content: str) -> List[Reference]`

**Cel**: Znalezienie wszystkich odniesień do innych dokumentów w treści.

**Parametry wejściowe**:
- `content` (str): Treść markdown

**Wartość zwracana**:
- `List[Reference]`: Lista odniesień z target_id, type, line

**Algorytm**:
1. Przeszukaj content używając regex dla wzorców:
   - `requires: [DOC-ID]` w frontmatter
   - `dependencies: [DOC-ID, ...]` w frontmatter
   - `related: [DOC-ID, ...]` w frontmatter
   - `See also: [DOC-ID]` w body
2. Dla każdego znalezienia:
   - Wyciągnij target_id (np. "PRD-001")
   - Określ type połączenia (requires, references, informs)
   - Zapisz numer linii
3. Utwórz listę Reference
4. Zwróć references

**Struktura Reference**:
```python
@dataclass
class Reference:
    target_id: str      # "BIZ-CASE-001"
    type: str           # "requires"
    line: int           # 8
    context: str        # Fragment tekstu wokół odniesienia
```

---

### 3.2 Validator Module

#### `validate_document(document: ParsedDocument, doc_type: DocumentType) -> ValidationResult`

**Cel**: Pełna walidacja dokumentu względem schematu typu.

**Parametry wejściowe**:
- `document` (ParsedDocument): Sparsowany dokument
- `doc_type` (DocumentType): Definicja typu dokumentu

**Wartość zwracana**:
- `ValidationResult`: Obiekt z valid, errors, warnings

**Algorytm**:
1. Wywołaj `validate_frontmatter_schema(document.frontmatter, doc_type.frontmatter_schema)`
2. Wywołaj `validate_required_sections(document, doc_type.required_sections)`
3. Wywołaj `check_placeholders(document.content)` → wykryj TODO/TBD
4. Jeśli wszystkie walidacje OK → valid=True
5. Jeśli jakieś błędy → valid=False, zbierz errors
6. Zwróć ValidationResult

**Struktura ValidationResult**:
```python
@dataclass
class ValidationResult:
    valid: bool
    document_id: str
    errors: List[ValidationError]
    warnings: List[ValidationWarning]
    timestamp: datetime
```

---

#### `validate_frontmatter_schema(frontmatter: dict, schema: dict) -> List[ValidationError]`

**Cel**: Walidacja YAML frontmatter względem schematu.

**Parametry wejściowe**:
- `frontmatter` (dict): Sparsowany frontmatter YAML
- `schema` (dict): Schemat z required_fields, optional_fields, constraints

**Wartość zwracana**:
- `List[ValidationError]`: Lista błędów walidacji

**Algorytm**:
1. Sprawdź `required_fields`:
   - Dla każdego wymaganego pola:
     - Jeśli brakuje → dodaj ValidationError
2. Sprawdź `field_constraints`:
   - Dla każdego pola z constraints:
     - Jeśli enum: sprawdź czy wartość w dozwolonych
     - Jeśli pattern: sprawdź regex
     - Jeśli brak zgodności → dodaj ValidationError
3. Zwróć listę ValidationError

**Przykład błędu**:
```python
ValidationError(
    type="MISSING_REQUIRED_FIELD",
    severity="critical",
    message="Brakuje wymaganego pola frontmatter: 'owner'",
    location="frontmatter",
    remediation="Dodaj pole 'owner: Team Lead' do frontmatter"
)
```

---

#### `validate_required_sections(document: ParsedDocument, required_sections: List[dict]) -> List[ValidationError]`

**Cel**: Sprawdzenie czy dokument zawiera wszystkie wymagane sekcje.

**Parametry wejściowe**:
- `document` (ParsedDocument): Sparsowany dokument
- `required_sections` (List[dict]): Lista wymaganych sekcji z schematu

**Wartość zwracana**:
- `List[ValidationError]`: Lista błędów brakujących sekcji

**Algorytm**:
1. Dla każdej wymaganej sekcji w required_sections:
   - Pobierz pattern (np. "^## User Personas")
   - Sprawdź czy istnieje sekcja w document.sections matchująca pattern
   - Jeśli mandatory=True i brakuje → dodaj ValidationError (E110)
   - Jeśli min_items określone:
     - Policz items w sekcji (np. liczba list items)
     - Jeśli < min_items → dodaj ValidationError
2. Zwróć listę ValidationError

---

#### `check_placeholders(content: str) -> List[ValidationError]`

**Cel**: Wykrycie placeholderów (TODO, TBD, PLACEHOLDER) w treści.

**Parametry wejściowe**:
- `content` (str): Treść markdown

**Wartość zwracana**:
- `List[ValidationError]`: Lista znalezionych placeholderów (E120)

**Algorytm**:
1. Zdefiniuj wzorce regex: `TODO`, `TBD`, `PLACEHOLDER`, `XXX`, `FIXME`
2. Przeszukaj content używając regex
3. Dla każdego znalezienia:
   - Wyciągnij numer linii
   - Wyciągnij kontekst (fragment tekstu wokół)
   - Utwórz ValidationError typu E120
4. Zwróć listę ValidationError

**Przykład**:
```python
ValidationError(
    type="PLACEHOLDER_DETECTED",
    severity="high",
    message="Znaleziono placeholder 'TODO' w sekcji Functional Requirements",
    location="line 45",
    remediation="Uzupełnij treść lub usuń placeholder"
)
```

---

### 3.3 Graph Builder Module

#### `build_graph(documents: List[ParsedDocument]) -> DependencyGraph`

**Cel**: Budowanie grafu zależności z listy dokumentów.

**Parametry wejściowe**:
- `documents` (List[ParsedDocument]): Lista sparsowanych dokumentów

**Wartość zwracana**:
- `DependencyGraph`: Graf zależności (NetworkX DiGraph)

**Algorytm**:
1. Utwórz pusty graf: `graph = networkx.DiGraph()`
2. Dla każdego dokumentu:
   - Wywołaj `add_node(graph, document)`
3. Dla każdego dokumentu:
   - Dla każdej referencji w document.references:
     - Wywołaj `add_edge(graph, document.id, reference.target_id, reference.type)`
4. Wywołaj `detect_cycles(graph)` → jeśli cykle → loguj warning
5. Wywołaj `calculate_hierarchy_levels(graph)` → przypisz level każdemu node
6. Zwróć graph

**Struktura DependencyGraph**:
```python
class DependencyGraph:
    graph: networkx.DiGraph
    nodes: Dict[str, Node]
    edges: List[Connection]
    cycles: List[List[str]]
    hierarchy_levels: Dict[str, int]
```

---

#### `add_node(graph: networkx.DiGraph, document: ParsedDocument)`

**Cel**: Dodanie węzła dokumentu do grafu.

**Parametry wejściowe**:
- `graph` (DiGraph): Graf NetworkX
- `document` (ParsedDocument): Dokument do dodania

**Algorytm**:
1. Utwórz node_id z document.frontmatter["id"]
2. Utwórz metadata dict z frontmatter
3. Dodaj węzeł do grafu:
   ```python
   graph.add_node(node_id, **metadata)
   ```

---

#### `add_edge(graph: networkx.DiGraph, from_doc: str, to_doc: str, edge_type: str)`

**Cel**: Dodanie połączenia między dokumentami.

**Parametry wejściowe**:
- `graph` (DiGraph): Graf NetworkX
- `from_doc` (str): ID dokumentu źródłowego
- `to_doc` (str): ID dokumentu docelowego
- `edge_type` (str): Typ połączenia (requires, implements, references, etc.)

**Algorytm**:
1. Sprawdź czy oba węzły istnieją w grafie
   - Jeśli nie → loguj warning (broken dependency)
2. Dodaj krawędź:
   ```python
   graph.add_edge(from_doc, to_doc, type=edge_type)
   ```

---

#### `detect_cycles(graph: networkx.DiGraph) -> List[List[str]]`

**Cel**: Wykrycie cyklicznych zależności w grafie.

**Parametry wejściowe**:
- `graph` (DiGraph): Graf zależności

**Wartość zwracana**:
- `List[List[str]]`: Lista cykli (każdy cykl = lista node IDs)

**Algorytm**:
1. Użyj algorytmu NetworkX:
   ```python
   cycles = list(networkx.simple_cycles(graph))
   ```
2. Zwróć cycles

**Przykład cyklu**:
```python
cycles = [
    ["PRD-001", "TDD-001", "PRD-001"],  # PRD → TDD → PRD
]
```

---

#### `calculate_hierarchy_levels(graph: networkx.DiGraph) -> Dict[str, int]`

**Cel**: Wyliczenie poziomów hierarchii dla każdego węzła (emergent hierarchy).

**Parametry wejściowe**:
- `graph` (DiGraph): Graf zależności

**Wartość zwracana**:
- `Dict[str, int]`: Mapowanie node_id → level

**Algorytm**:
1. Znajdź węzły bez incoming edges (root nodes) → level 0
2. Dla każdego poziomu począwszy od 0:
   - Znajdź wszystkie węzły z incoming tylko z poprzednich poziomów
   - Przypisz level = max(parent_levels) + 1
3. Zwróć mapowanie

**Przykład**:
```python
{
    "EXEC-SUM-001": 0,      # Root
    "BIZ-CASE-001": 1,      # Wymaga EXEC-SUM
    "VISION-001": 1,        # Wymaga EXEC-SUM
    "PRD-001": 2,           # Wymaga BIZ-CASE, VISION
    "TDD-001": 3,           # Wymaga PRD
}
```

---

#### `find_dependencies(graph: networkx.DiGraph, node_id: str) -> List[str]`

**Cel**: Znalezienie wszystkich bezpośrednich zależności węzła.

**Parametry wejściowe**:
- `graph` (DiGraph): Graf zależności
- `node_id` (str): ID węzła

**Wartość zwracana**:
- `List[str]`: Lista IDs węzłów od których zależy node_id

**Algorytm**:
1. Użyj NetworkX:
   ```python
   predecessors = list(graph.predecessors(node_id))
   ```
2. Zwróć predecessors

---

#### `visualize_graph(graph: DependencyGraph) -> dict`

**Cel**: Eksport grafu do formatu Cytoscape.js do wizualizacji w GUI.

**Parametry wejściowe**:
- `graph` (DependencyGraph): Graf zależności

**Wartość zwracana**:
- `dict`: JSON-serializable struktura dla Cytoscape.js

**Algorytm**:
1. Utwórz listę `elements = []`
2. Dla każdego węzła w graph:
   - Dodaj obiekt node:
     ```python
     {
       "data": {
         "id": node_id,
         "label": node_metadata["title"],
         "type": node_metadata["type"],
         "status": node_metadata["status"],
         "level": hierarchy_levels[node_id]
       },
       "classes": node_metadata["status"]  # dla CSS styling
     }
     ```
3. Dla każdej krawędzi w graph:
   - Dodaj obiekt edge:
     ```python
     {
       "data": {
         "source": from_node,
         "target": to_node,
         "label": edge_type,
         "type": edge_type
       },
       "classes": edge_type  # dla CSS styling
     }
     ```
4. Zwróć `{"elements": elements}`

---

### 3.4 Gap Engine Module

#### `detect_gaps(document: ParsedDocument, doc_type: DocumentType, graph: DependencyGraph) -> List[Gap]`

**Cel**: Wykrycie wszystkich typów luk w dokumencie.

**Parametry wejściowe**:
- `document` (ParsedDocument): Dokument do analizy
- `doc_type` (DocumentType): Definicja typu
- `graph` (DependencyGraph): Graf zależności

**Wartość zwracana**:
- `List[Gap]`: Lista wykrytych luk

**Algorytm**:
1. Utwórz pustą listę gaps = []
2. Wywołaj `detect_missing_sections(document, doc_type)` → gaps_E110
3. Wywołaj `detect_placeholders(document)` → gaps_E120
4. Wywołaj `detect_missing_evidence(document)` → gaps_E130
5. Wywołaj `detect_broken_dependencies(document, graph)` → gaps_E140
6. Wywołaj `detect_gate_blockers(document, gate)` → gaps_E150
7. Wywołaj `detect_missing_approvals(document)` → gaps_E160
8. Połącz wszystkie gaps → gaps
9. Dla każdego gap:
   - Wywołaj `categorize_gap(gap)` → przypisz severity
   - Wywołaj `generate_remediation(gap)` → wygeneruj kroki naprawy
10. Zwróć gaps

---

#### `detect_missing_sections(document: ParsedDocument, doc_type: DocumentType) -> List[Gap]`

**Cel**: Wykrycie brakujących wymaganych sekcji (E110).

**Parametry wejściowe**:
- `document` (ParsedDocument): Dokument
- `doc_type` (DocumentType): Typ dokumentu z required_sections

**Wartość zwracana**:
- `List[Gap]`: Lista luk E110

**Algorytm**:
1. Dla każdej wymaganej sekcji w doc_type.required_sections:
   - Sprawdź czy section istnieje w document.sections
   - Jeśli mandatory=True i brakuje:
     - Utwórz Gap:
       ```python
       Gap(
         id=f"GAP-{document.id}-E110-{counter}",
         type="E110",
         severity="critical",
         source_document=document.id,
         description=f"Brakująca wymagana sekcja: '{section.name}'",
         remediation=[
           f"Dodać sekcję '## {section.name}' do {document.id}",
           "Uzupełnić treść zgodnie z szablonem"
         ],
         status="open",
         detected_at=datetime.now()
       )
       ```
2. Zwróć listę gaps

---

#### `detect_placeholders(document: ParsedDocument) -> List[Gap]`

**Cel**: Wykrycie placeholderów TODO/TBD (E120).

**Parametry wejściowe**:
- `document` (ParsedDocument): Dokument

**Wartość zwracana**:
- `List[Gap]`: Lista luk E120

**Algorytm**:
1. Przeszukaj document.content używając regex dla: TODO, TBD, PLACEHOLDER, XXX, FIXME
2. Dla każdego znalezienia:
   - Utwórz Gap typu E120
   - Severity = "high" (jeśli w critical section) lub "medium"
   - Dodaj do listy
3. Zwróć gaps

---

#### `detect_broken_dependencies(document: ParsedDocument, graph: DependencyGraph) -> List[Gap]`

**Cel**: Wykrycie złamanych zależności - odniesienia do nieistniejących dokumentów (E140).

**Parametry wejściowe**:
- `document` (ParsedDocument): Dokument
- `graph` (DependencyGraph): Graf zależności

**Wartość zwracana**:
- `List[Gap]`: Lista luk E140

**Algorytm**:
1. Dla każdej referencji w document.references:
   - Sprawdź czy target_id istnieje w graph.nodes
   - Jeśli NIE istnieje:
     - Utwórz Gap E140:
       ```python
       Gap(
         type="E140",
         severity="critical",
         description=f"Złamana zależność: dokument '{reference.target_id}' nie istnieje",
         remediation=[
           f"Utworzyć dokument {reference.target_id}",
           f"Lub usunąć odniesienie z {document.id}"
         ]
       )
       ```
   - Jeśli istnieje ale ma niepoprawny status (np. wymaga "completed" a jest "draft"):
     - Utwórz Gap E140 z severity="high"
2. Zwróć gaps

---

#### `detect_gate_blockers(document: ParsedDocument, gate: QualityGate) -> List[Gap]`

**Cel**: Wykrycie blokerów bramki jakości (E150).

**Parametry wejściowe**:
- `document` (ParsedDocument): Dokument próbujący przejść bramkę
- `gate` (QualityGate): Definicja bramki

**Wartość zwracana**:
- `List[Gap]`: Lista luk E150

**Algorytm**:
1. Dla każdego warunku w gate.conditions:
   - Sprawdź czy dokument spełnia warunek
   - Przykłady warunków:
     - `status == "review" OR "approved"`
     - `all_required_sections_present == True`
     - `no_placeholders == True`
   - Jeśli warunek NIE spełniony:
     - Utwórz Gap E150
2. Zwróć gaps

---

#### `generate_remediation(gap: Gap) -> List[str]`

**Cel**: Wygenerowanie konkretnych kroków naprawy dla luki.

**Parametry wejściowe**:
- `gap` (Gap): Luka

**Wartość zwracana**:
- `List[str]`: Lista kroków remediacji

**Algorytm**:
1. Na podstawie gap.type:
   - E110: `["Dodać sekcję '## {section_name}' do {doc_id}", "Uzupełnić treść"]`
   - E120: `["Usunąć placeholder '{placeholder}' z linii {line}", "Uzupełnić faktyczną treścią"]`
   - E140: `["Utworzyć dokument {target_id}", "Lub usunąć odniesienie"]`
   - E150: `["Spełnić warunki bramki: {conditions}", "Uzyskać wymagane zatwierdzenia"]`
2. Zwróć listę kroków

---

#### `categorize_gap(gap: Gap) -> str`

**Cel**: Przypisanie severity do luki na podstawie typu i kontekstu.

**Parametry wejściowe**:
- `gap` (Gap): Luka

**Wartość zwracana**:
- `str`: Severity (critical, high, medium, low)

**Algorytm**:
1. Reguły severity:
   - E110 (missing section):
     - Jeśli mandatory=True → critical
     - Jeśli optional → medium
   - E120 (placeholder):
     - Jeśli w critical section (np. Requirements) → high
     - Jeśli w optional section → medium
   - E140 (broken dependency):
     - Jeśli dependency type="requires" → critical
     - Jeśli type="references" → medium
   - E150 (gate blocker):
     - Zawsze critical (blokuje postęp)
2. Zwróć severity

---

### 3.5 Proactive Assistant Module

#### `suggest_next_steps(graph: DependencyGraph, gaps: List[Gap]) -> List[str]`

**Cel**: Proaktywne sugerowanie co należy zrobić jako następne.

**Parametry wejściowe**:
- `graph` (DependencyGraph): Graf zależności
- `gaps` (List[Gap]): Lista wszystkich luk

**Wartość zwracana**:
- `List[str]`: Lista sugerowanych kroków

**Algorytm**:
1. Priorytetyzuj luki według severity (critical > high > medium > low)
2. Dla top 5 critical gaps:
   - Dodaj remediację do sugestii
3. Identyfikuj dokumenty blokujące (maja status "in-progress" ale dependencies nie są spełnione):
   - Sugeruj ukończenie dependencies
4. Znajdź następne dokumenty w łańcuchu (np. jeśli PRD jest "completed", sugeruj utworzenie TDD)
5. Zwróć listę sugestii

---

#### `infer_missing_documents(graph: DependencyGraph, doc_types: List[DocumentType]) -> List[str]`

**Cel**: Wnioskowanie brakujących dokumentów na podstawie typowych łańcuchów.

**Parametry wejściowe**:
- `graph` (DependencyGraph): Graf zależności
- `doc_types` (List[DocumentType]): Wszystkie dostępne typy dokumentów

**Wartość zwracana**:
- `List[str]`: Lista sugerowanych brakujących typów dokumentów

**Algorytm**:
1. Zdefiniuj typowe łańcuchy:
   ```python
   chains = [
     ["exec-summary", "business-case", "prd", "tdd", "impl-plan"],
     ["prd", "test-plan", "test-cases"],
     ["tdd", "deployment-guide", "runbook"]
   ]
   ```
2. Dla każdego łańcucha:
   - Sprawdź które dokumenty istnieją
   - Jeśli istnieje doc[i] ale brakuje doc[i+1]:
     - Sugeruj utworzenie doc[i+1]
3. Zwróć listę sugestii

---

#### `generate_todo_from_gap(gap: Gap, parent_doc: str) -> SatelliteDocument`

**Cel**: Automatyczne wygenerowanie satelity TODO z luki.

**Parametry wejściowe**:
- `gap` (Gap): Luka do konwersji
- `parent_doc` (str): ID dokumentu rodzica

**Wartość zwracana**:
- `SatelliteDocument`: Satelita TODO

**Algorytm**:
1. Utwórz ID: `TODO-{parent_doc}-TASK-{counter}`
2. Utwórz title z gap.description
3. Utwórz content markdown:
   ```markdown
   ---
   id: TODO-PRD-001-TASK-001
   type: todo
   parent_document: PRD-001
   status: open
   priority: {gap.severity}
   ---

   ## Zadanie

   {gap.description}

   ## Kroki Remediacji

   {gap.remediation as checklist}
   ```
4. Zwróć SatelliteDocument

---

### 3.6 Storage Module

#### `index_document(document: ParsedDocument, db: sqlite3.Connection)`

**Cel**: Indeksowanie dokumentu w SQLite dla szybkiego wyszukiwania.

**Parametry wejściowe**:
- `document` (ParsedDocument): Dokument do zaindeksowania
- `db` (Connection): Połączenie SQLite

**Algorytm**:
1. Utwórz record w tabeli `documents`:
   ```sql
   INSERT INTO documents (id, type, status, title, file_path, metadata, indexed_at)
   VALUES (?, ?, ?, ?, ?, ?, ?)
   ```
2. Dla każdej sekcji:
   - Wstaw do tabeli `sections` z FTS5 index dla full-text search
3. Dla każdej referencji:
   - Wstaw do tabeli `connections`

---

#### `save_gaps(gaps: List[Gap], store_path: str)`

**Cel**: Persystencja luk do pliku JSON.

**Parametry wejściowe**:
- `gaps` (List[Gap]): Lista luk
- `store_path` (str): Ścieżka do pliku JSON

**Algorytm**:
1. Serializuj gaps do JSON
2. Zapisz do pliku store_path
3. Handle errors (permission, disk full)

---

### 3.7 File Watcher Module

#### `watch_directory(directory: str, callback: Callable)`

**Cel**: Monitorowanie katalogu dla zmian w plikach i automatyczna analiza.

**Parametry wejściowe**:
- `directory` (str): Katalog do watchowania
- `callback` (Callable): Funkcja wywoływana przy zmianie

**Algorytm**:
1. Użyj biblioteki Watchdog:
   ```python
   observer = Observer()
   handler = FileSystemEventHandler()
   handler.on_modified = callback
   observer.schedule(handler, directory, recursive=True)
   observer.start()
   ```
2. Callback otrzymuje event z file_path
3. Callback wywołuje re-analysis dokumentu

---

## Część 4: Przepływy Danych i Interakcje

### 4.1 Przepływ: Parsowanie i Walidacja Dokumentu

```
1. User tworzy/edytuje plik .md
2. File Watcher wykrywa zmianę
3. Parser.parse_document(file_path) → ParsedDocument
4. DocumentType.load_document_type(type_id) → DocumentType
5. Validator.validate_document(document, doc_type) → ValidationResult
6. Jeśli errors → zwróć użytkownikowi
7. Jeśli valid → index_document(document, db)
```

### 4.2 Przepływ: Budowanie Grafu i Wykrywanie Luk

```
1. Parser parsuje wszystkie dokumenty → List[ParsedDocument]
2. GraphBuilder.build_graph(documents) → DependencyGraph
3. GraphBuilder.detect_cycles(graph) → raportuj cykle
4. GraphBuilder.calculate_hierarchy_levels(graph) → przypisz levels
5. Dla każdego dokumentu:
   - GapEngine.detect_gaps(document, doc_type, graph) → List[Gap]
6. GapStore.save_gaps(all_gaps, store_path)
7. ProactiveAssistant.suggest_next_steps(graph, gaps) → sugestie
```

### 4.3 Przepływ: Wizualizacja w GUI

```
1. User otwiera GUI
2. GraphBuilder.visualize_graph(graph) → cytoscape_json
3. GUI.GraphWidget renderuje graf używając Cytoscape.js
4. User klika na węzeł
5. GUI.PreviewWidget ładuje dokument i wyświetla preview
6. GUI.GapsPanel wyświetla luki dla wybranego dokumentu
7. User klika "Fix Gap"
8. GUI otwiera dokument w edytorze z podświetleniem brakującej sekcji
```

### 4.4 Przepływ: Automatyczne Generowanie TODO

```
1. GapEngine wykrywa critical gap
2. ProactiveAssistant.generate_todo_from_gap(gap, parent_doc) → SatelliteDocument
3. System zapisuje satelitę TODO do `/satellites/todos/`
4. GraphBuilder dodaje edge: parent_doc --supports--> TODO
5. User widzi TODO w GUI jako task do wykonania
```

---

## Część 5: Następne Kroki Implementacji

### 5.1 Priorytetyzacja Funkcji

**Faza 1 (Foundation) - Tydzień 1-2**:
1. `parse_document()` ✅ CRITICAL
2. `extract_frontmatter()` ✅ CRITICAL
3. `parse_markdown_to_ast()` ✅ CRITICAL
4. `validate_frontmatter_schema()` ✅ CRITICAL
5. `load_document_type()` ✅ CRITICAL

**Faza 2 (Graph) - Tydzień 3-4**:
6. `build_graph()` ✅ CRITICAL
7. `add_node()`, `add_edge()` ✅ CRITICAL
8. `detect_cycles()` ✅ HIGH
9. `calculate_hierarchy_levels()` ✅ HIGH
10. `index_document()` ✅ MEDIUM

**Faza 3 (Gap Detection) - Tydzień 5-6**:
11. `detect_gaps()` ✅ CRITICAL
12. `detect_missing_sections()` ✅ CRITICAL
13. `detect_placeholders()` ✅ HIGH
14. `detect_broken_dependencies()` ✅ CRITICAL
15. `generate_remediation()` ✅ HIGH

**Faza 4 (GUI) - Tydzień 7-9**:
16. `visualize_graph()` ✅ HIGH
17. GUI.MainWindow (PySide6) ✅ HIGH
18. GUI.GraphWidget (Cytoscape.js) ✅ HIGH
19. GUI.GapsPanel ✅ MEDIUM

**Faza 5 (File Watching) - Tydzień 10**:
20. `watch_directory()` ✅ MEDIUM
21. Incremental analysis ✅ MEDIUM

**Faza 6 (Advanced) - Tydzień 11-12**:
22. `suggest_next_steps()` ✅ MEDIUM
23. `infer_missing_documents()` ✅ LOW
24. `generate_todo_from_gap()` ✅ MEDIUM
25. Export reports (HTML, PDF) ✅ LOW

### 5.2 Mapowanie Funkcje → Moduły Python

| Funkcja | Moduł Python | Ścieżka |
|---------|--------------|---------|
| `parse_document()` | `parser.py` | `src/core/parser.py` |
| `validate_document()` | `validator.py` | `src/core/validator.py` |
| `build_graph()` | `graph_builder.py` | `src/core/graph_builder.py` |
| `detect_gaps()` | `gap_engine.py` | `src/core/gap_engine.py` |
| `load_document_type()` | `document_type.py` | `src/models/document_type.py` |
| `index_document()` | `document_store.py` | `src/storage/document_store.py` |
| `visualize_graph()` | `graph_builder.py` | `src/core/graph_builder.py` |
| `watch_directory()` | `file_watcher.py` | `src/core/file_watcher.py` |
| `suggest_next_steps()` | `proactive_assistant.py` | `src/core/proactive_assistant.py` |

---

## Podsumowanie

Ten dokument Koncepcje definiuje:

1. **12 kluczowych koncepcji** systemu zarządzania dokumentacją
2. **Mapowanie każdej koncepcji na konkretne funkcje** (~60 funkcji)
3. **Pełne specyfikacje 30+ funkcji** z algorytmami, parametrami, wartościami zwracanymi
4. **Przepływy danych** między komponentami
5. **Priorytetyzację implementacji** (6 faz, 12 tygodni)

System będzie działał na zasadzie:
- **Parser** → ekstrakcja struktury z markdown
- **Validator** → weryfikacja względem schematów
- **Graph Builder** → budowanie grafu zależności
- **Gap Engine** → wykrywanie luk i generowanie remediacji
- **Proactive Assistant** → sugestie następnych kroków
- **GUI** → wizualizacja i interakcja

Wszystko razem tworzy **proaktywny, self-organizing system dokumentacji** który:
- Automatycznie wykrywa luki
- Sugeruje co zrobić jako następne
- Wymusza bramki jakości
- Wizualizuje hierarchię emergentną
- Śledzi wszystkie zależności

---

**Status**: Draft - Oczekuje na zatwierdzenie przed przejściem do PRD
**Ostatnia Aktualizacja**: 2025-12-26
**Następne Kroki**: Stworzyć PRD z mapowaniem koncepcje → wymagania funkcjonalne
