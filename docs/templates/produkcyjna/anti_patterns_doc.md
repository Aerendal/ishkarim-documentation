# Anty-wzorce i Złe Praktyki

> **Framework:** Software Anti-Patterns + Clean Code Principles  
> **Data opracowania:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół]  
> **Status:** [Draft/Review/Approved]  
> **Powiązane:** ← `03_PROBLEMY_I_BŁĘDY`, → `04_PROCES_REFAKTORYZACJI`, → `02_TO_BE`

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: AS-IS-ARCHITECTURE
    type: evidence_source
    from_sections:
      - code_structure
      - architecture_patterns
    to_sections:
      - anti_pattern_instances
      - code_examples
    influence: "AS-IS dostarcza przykładów anty-wzorców w kodzie"
    when:
      condition: analysis.type == "anti_patterns"
      applies: always

  - id: CODE-REVIEW
    type: quality_findings
    from_sections:
      - code_smells
      - bad_practices
      - violation_patterns
    to_sections:
      - anti_pattern_catalog
      - severity_classification
    influence: "Code review identyfikuje konkretne wystąpienia anty-wzorców"
    when:
      condition: review.has_findings == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: PROBLEMS-ANALYSIS
    type: problem_classification
    from_sections:
      - anti_pattern_catalog
      - mitigation_strategies
    to_sections:
      - problem_types
      - solution_patterns
    influence: "Katalog anty-wzorców klasyfikuje i kategoryzuje problemy"
    when:
      condition: catalog.complete == true
      applies: always

  - id: REFACTORING-PROCESS
    type: refactoring_targets
    from_sections:
      - high_severity_patterns
      - mitigation_strategies
    to_sections:
      - refactoring_priorities
      - technical_debt_reduction
    influence: "Anty-wzorce definiują cele i priorytety refaktoringu"
    when:
      condition: patterns.prioritized == true
      applies: always

  - id: CODE-QUALITY-GATES
    type: prevention_rules
    from_sections:
      - detection_methods
      - automated_checks
    to_sections:
      - ci_cd_quality_gates
      - static_analysis_rules
    influence: "Wykryte anty-wzorce są zapobiegane przez quality gates"
    when:
      condition: prevention.automated == true
      applies: conditionally
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: DESIGN-PATTERNS-CATALOG
    relationship: correct_alternatives
    sections_mapping:
      - from: recommended_patterns
        to: mitigation_strategies
    usage: "Dobre wzorce projektowe są alternatywą dla anty-wzorców"

  - id: CLEAN-CODE-GUIDELINES
    relationship: best_practices
    sections_mapping:
      - from: coding_standards
        to: prevention_guidelines
    usage: "Wytyczne clean code zapobiegają powstawaniu anty-wzorców"
```

### Satellite Documents

```yaml
satellites:
  - name: ANTI-PATTERN-EXAMPLES
    purpose: "Przykłady kodu ilustrujące konkretne anty-wzorce"
    trigger: during_documentation
    lifecycle: permanent
    retention: permanent

  - name: REFACTORING-EXAMPLES
    purpose: "Przykłady przed/po pokazujące eliminację anty-wzorców"
    trigger: during_mitigation
    lifecycle: permanent
    retention: permanent

  - name: AUTOMATED-DETECTION-RULES
    purpose: "Reguły dla narzędzi statycznej analizy wykrywające anty-wzorce"
    trigger: after_pattern_identification
    lifecycle: continuous
    retention: permanent
```

---

## EXECUTIVE SUMMARY

### Cel Dokumentu
[Dlaczego katalogujemy anty-wzorce - uczenie się z błędów, przewodnik "czego NIE robić", 2-3 zdania]

### Definicja Anty-wzorca
**Anti-pattern:** Pozornie dobre rozwiązanie, które w rzeczywistości prowadzi do większych problemów niż te, które miało rozwiązać.

**Kluczowe cechy:**
- **Wydaje się dobrym pomysłem** na początku
- **Prowadzi do technical debt** w długim terminie
- **Ma znaną alternatywę** (lepszy wzorzec)

### Top 10 Anty-wzorców w Projekcie

| Rank | Anty-wzorzec | Where Found | Severity | Impact |
|------|--------------|-------------|----------|--------|
| 1 | God Object | Security_Analysis | Critical | Maintainability |
| 2 | Monolithic Module | Security_Analysis | Critical | Coupling, Scalability |
| 3 | Copy-Paste Programming | Metadata duplikacja | High | Consistency, Size |
| 4 | Spaghetti Code | unified_pipeline.py | High | Complexity |
| 5 | Tight Coupling | Security ↔ IR_SBOM | High | Testability, Reusability |
| 6 | Magic Numbers | Timeouts, limits | Medium | Maintainability |
| 7 | Yo-Yo Problem | Deep directory nesting | Medium | Navigation |
| 8 | Golden Hammer | "Dodaj do Security_Analysis" | Medium | Design |
| 9 | Lava Flow | Dead code, commented | Low | Confusion |
| 10 | Boat Anchor | Unused dependencies | Low | Build Time, Size |

### Metrykaanty-wzorców

**Całkowita liczba wystąpień:** [N]  
**Critical:** [X] - wymaga natychmiastowej naprawy  
**High:** [Y] - naprawić w ciągu miesiąca  
**Medium:** [Z] - backlog  
**Low:** [W] - nice to have

---

## 1. SYSTEM KLASYFIKACJI

### 1.1. Kategorie Anty-wzorców

| Kategoria | Opis | Przykłady |
|-----------|------|-----------|
| **Architectural** | Problemy strukturalne | Monolith, Tight Coupling, God Object |
| **Design** | Złe decyzje projektowe | Golden Hammer, Swiss Army Knife |
| **Code-level** | Problemy w kodzie | Spaghetti Code, Copy-Paste, Magic Numbers |
| **Process** | Złe procesy | Continuous Obsolescence, Analysis Paralysis |
| **Organizational** | Problemy zespołowe/procesu | Vendor Lock-in, Committee Design |

### 1.2. Severity Levels

| Level | Kryteria | Przykład |
|-------|----------|----------|
| **Critical** | Blokuje development, major architectural flaw | God Object, Monolith |
| **High** | Significant technical debt | Tight Coupling, Spaghetti |
| **Medium** | Moderate impact, workaround exists | Magic Numbers, Yo-Yo |
| **Low** | Cosmetic, minor annoyance | Lava Flow, Dead Code |

---

## 2. ARCHITECTURAL ANTI-PATTERNS

### 2.1. God Object (Big Ball of Mud)

**Aliases:** Blob, The One Class

**Definicja:**
Jedna klasa/moduł robi zbyt wiele rzeczy (narusza Single Responsibility Principle).

**Symptomy:**
- Plik > 1000 LOC
- Klasa z 20+ metodami
- Nazwa "Manager", "Utils", "Helper", "Service"
- Wszystko inne od niego zależy

**Gdzie Znaleziono:**
- `Security_Analysis/L1_FAZA1/tools/unified_pipeline.py` - **1,842 LOC!**
  - Klasa `UnifiedPipeline` ma 23 metody
  - Odpowiada za: SAST, SCA, Secrets, FixOps, Reporting, Configuration
  
**Przykład:**
```python
# ✗ God Object (BAD):
class UnifiedPipeline:
    """Does EVERYTHING."""
    
    def scan_sast(self): ...
    def scan_sca(self): ...
    def scan_secrets(self): ...
    def generate_fixes(self): ...
    def rank_fixes(self): ...
    def create_report(self): ...
    def send_notifications(self): ...
    def update_database(self): ...
    def generate_metrics(self): ...
    # ... 14 more methods
```

**Dlaczego To Złe:**
- **Maintainability:** Każda zmiana ryzykowna (może zepsuć coś innego)
- **Testability:** Trudno mock dependencies
- **Reusability:** Nie możesz użyć tylko jednej części
- **Team Collaboration:** Merge conflicts przy pracy wielu osób

**Prawidłowy Wzorzec: Single Responsibility**
```python
# ✓ GOOD - Separate responsibilities:
class SASTScanner:
    """Only SAST scanning."""
    def scan(self, path): ...

class SCAScanner:
    """Only SCA scanning."""
    def scan_dependencies(self, sbom): ...

class SecretsScanner:
    """Only secrets detection."""
    def scan(self, path): ...

class FixGenerator:
    """Only fix proposal generation."""
    def generate_fixes(self, findings): ...

# Composition:
class SecurityPipeline:
    """Orchestrates the pipeline (but delegates work)."""
    def __init__(self, sast, sca, secrets, fix_gen):
        self._sast = sast
        self._sca = sca
        self._secrets = secrets
        self._fix_gen = fix_gen
    
    def run(self, path):
        sast_findings = self._sast.scan(path)
        sca_findings = self._sca.scan_dependencies(...)
        # ... coordinate, but don't implement details
```

**Jak Wykrywać:**
```bash
# Find large files:
find . -name "*.py" -exec wc -l {} \; | sort -rn | head -10

# Find classes with many methods:
grep -r "def " Security_Analysis/ | grep -v test | wc -l
```

**Mitigacja:**
→ Zobacz `04_PROCES.md#Phase1.1` - Extract to separate modules

---

### 2.2. Monolithic Module

**Definicja:**
Jeden moduł zawiera wiele niezależnych funkcjonalności bez wyraźnych granic.

**Symptomy:**
- Moduł > 30 MB
- 4+ różne odpowiedzialności
- Zmiana w jednej części może zepsuć inną
- Trudno wyodrębnić tylko jedną funkcjonalność

**Gdzie Znaleziono:**
- **Security_Analysis** (48 MB!)
  - SAST (15 MB)
  - SCA (18 MB)
  - Secrets (8 MB)
  - FixOps (5 MB)
  - Duplikacja metadata (2 MB)

**Dlaczego To Złe:**
- **Coupling:** Wszystko ze sobą powiązane
- **Scalability:** Nie możesz skalować tylko jednej części
- **Deployment:** Mała zmiana = deploy całego modułu (48 MB!)
- **Team Ownership:** Konflikt ownership

**Prawidłowy Wzorzec: Microservices/Modular Monolith**
```
# ✗ BAD - All in one:
Security_Analysis (48 MB)
    ├── sast/
    ├── sca/
    ├── secrets/
    └── fixes/

# ✓ GOOD - Separate modules:
SAST_Engine (12 MB)
SCA_Engine (15 MB)
Secrets_Scanner (8 MB)
FixOps (8 MB)
```

**Mitigacja:**
→ Zobacz `04_PROCES.md#Phase1` - Split Security_Analysis into 4 modules

---

### 2.3. Tight Coupling (No Dependency Inversion)

**Definicja:**
Moduły bezpośrednio zależą od konkretnych implementacji (nie od abstrakcji).

**Symptomy:**
- Direct imports z innych modułów: `from other_module.internal import Thing`
- Brak interfaces/protocols
- Trudno zamockować w testach
- Zmiana w module B wymusza zmianę w module A

**Gdzie Znaleziono:**
- Security_Analysis → IR_SBOM_Impact
  ```python
  # ✗ Tight coupling:
  from ir_sbom_impact.symbol_graph.builder import SymbolGraphBuilder
  from ir_sbom_impact.sbom.generator import SBOMGenerator
  
  class Reachability:
      def __init__(self):
          self._graph_builder = SymbolGraphBuilder()  # konkretna impl!
  ```

**Dlaczego To Złe:**
- **Testability:** Trudno unit testować (trzeba ciągnąć cały IR_SBOM)
- **Reusability:** Nie możesz użyć Reachability bez IR_SBOM
- **Flexibility:** Nie możesz podmienić implementacji SymbolGraph

**Prawidłowy Wzorzec: Dependency Inversion**
```python
# ✓ GOOD - Depend on abstraction:
from interfaces import ISymbolGraphProvider  # abstraction

class Reachability:
    def __init__(self, graph_provider: ISymbolGraphProvider):
        self._graph_provider = graph_provider  # DI
    
    def analyze(self, cve):
        graph = self._graph_provider.get_graph()
        # ... analyze

# Usage (DI container):
from symbolgraph_builder import SymbolGraphBuilder

provider = SymbolGraphBuilder()  # concrete implementation
reachability = Reachability(graph_provider=provider)
```

**Mitigacja:**
1. Define interfaces (→ `02_TO_BE.md#4.4`)
2. Refactor to use DI
3. Architectural tests enforce

---

### 2.4. Swiss Army Knife

**Definicja:**
Moduł próbuje być "wszystkim dla wszystkich" - zbyt wiele features.

**Symptomy:**
- Moduł ma 10+ różnych use cases
- Readme wyjaśnia 5 różnych sposobów użycia
- API ma 50+ metod
- "Można użyć tego do X, Y, Z, ..."

**Gdzie Znaleziono:**
- Platform_Tools (996 KB, ale 15 różnych narzędzi!)
  - Validation
  - Gates policy
  - Obligations tracking
  - Utilities
  - Helpers
  - [etc.]

**Dlaczego To Złe:**
- **Confusion:** Użytkownicy nie wiedzą od czego zacząć
- **Bloat:** 90% features nieużywanych przez większość
- **Maintenance:** Trudno utrzymać tak wiele funkcji

**Prawidłowy Wzorzec: Focused Modules**
```
# ✗ BAD - Swiss Army Knife:
Platform_Tools
    ├── validation/
    ├── gates/
    ├── obligations/
    ├── utils/
    ├── helpers/
    └── [10 more...]

# ✓ GOOD - Focused:
Validation_Service (tylko validation)
Policy_Gates (tylko gates)
Obligations_Tracker (tylko obligations)
```

**Mitigacja:**
- Split na focused modules (jeśli warranted)
- Lub: Wyraźna dokumentacja per use case

---

### 2.5. Circular Dependencies

**Definicja:**
Moduł A zależy od B, B zależy od A (bezpośrednio lub pośrednio).

**Symptomy:**
- Import errors
- Difficult to understand dependencies
- Cannot load modules independently

**Gdzie Znaleziono:**
⚠️ **Potencjalnie w projekcie** (nie egzekwowane w CI!)

**Przykład:**
```python
# module_a.py
from module_b import B

class A:
    def method(self):
        return B().do_something()

# module_b.py
from module_a import A

class B:
    def do_something(self):
        return A().other_method()  # Circular!
```

**Dlaczego To Złe:**
- **Import Errors:** Python może się pogubić
- **Coupling:** Nie możesz użyć A bez B i na odwrót
- **Testing:** Nightmare

**Prawidłowy Wzorzec: Layered Architecture**
```
# ✓ GOOD - One-way dependencies:
High-Level Module A
    ↓ (depends on)
Mid-Level Module B
    ↓ (depends on)
Low-Level Module C

# C nie zależy od A ani B
# B nie zależy od A
```

**Jak Wykrywać:**
```python
# CI enforcement:
import networkx as nx

def test_no_circular_dependencies():
    graph = build_dependency_graph()
    assert nx.is_directed_acyclic_graph(graph), "Circular dependency detected!"
```

**Mitigacja:**
- Refactor to break cycle (introduce interface/abstraction)
- Architectural tests (fail CI if cycle detected)

---

## 3. DESIGN ANTI-PATTERNS

### 3.1. Golden Hammer

**Definicja:**
"Mam młotek (narzędzie/rozwiązanie), więc każdy problem wygląda jak gwóźdź."

**Symptomy:**
- "Dodajmy to do Security_Analysis" (bez względu na to, czy to security feature)
- Używanie tego samego narzędzia/frameworka do wszystkiego
- Opór przed nowymi rozwiązaniami

**Gdzie Znaleziono:**
- Każda nowa security-related feature trafia do Security_Analysis
  - SAST? → Security_Analysis
  - SCA? → Security_Analysis
  - Secrets? → Security_Analysis
  - FixOps? → Security_Analysis (ale to nie tylko security!)

**Dlaczego To Złe:**
- **Bloat:** Moduł rośnie bez kontroli
- **Misfit:** Nowe features force-fitted (nie naturalne)

**Prawidłowy Wzorzec: Right Tool for the Job**
- Evaluate każdy problem independently
- Create new module jeśli różna odpowiedzialność
- Don't default to "add to existing"

**Mitigacja:**
- Architecture review dla nowych features
- Checklist: "Czy to naprawdę pasuje do istniejącego modułu?"

---

### 3.2. Analysis Paralysis

**Definicja:**
Over-engineering, zbyt wiele warstw abstrakcji, zbyt wcześnie.

**Symptomy:**
- 106 katalogów dla 4.6 MB kodu (Code_Refactoring!)
- Interfaces dla wszystkiego (nawet małych internal things)
- "Może kiedyś będziemy potrzebować..."

**Gdzie Znaleziono:**
- **Code_Refactoring** (106 katalogów!)
  - Średnia głębokość: 5 poziomów
  - Niektóre ścieżki: `adapters/python/transformers/advanced/specialized/...`

**Dlaczego To Złe:**
- **Complexity:** Trudno znaleźć kod
- **Overhead:** 5 poziomów abstrakcji dla prostej rzeczy
- **YAGNI violation:** "You Aren't Gonna Need It"

**Prawidłowy Wzorzec: YAGNI + Refactor When Needed**
```
# ✗ Over-engineered (5 levels):
adapters/
    python/
        transformers/
            advanced/
                specialized/
                    my_function.py

# ✓ Simpler (2-3 levels):
adapters/
    python/
        my_function.py

# Refactor later jeśli rośnie:
adapters/
    python/
        basic/
            my_function.py
        advanced/
            other_function.py
```

**Mitigacja:**
- Start simple
- Refactor when you have 3+ examples (Rule of Three)
- YAGNI principle

---

### 3.3. Vendor Lock-in

**Definicja:**
Ścisła zależność od konkretnego vendora/narzędzia (trudno zmienić).

**Symptomy:**
- Semgrep-specific logic rozrzucona po kodzie
- Brak abstrakcji dla external tools
- "Jesteśmy związani z Semgrep forever"

**Where Found:**
- SAST engine bezpośrednio wywołuje semgrep (brak adapter pattern)

**Dlaczego To Złe:**
- **Flexibility:** Co jeśli Semgrep podniesie ceny 10×?
- **Evolution:** Co jeśli lepsze narzędzie się pojawi?

**Prawidłowy Wzorzec: Adapter Pattern**
```python
# ✗ BAD - Vendor lock-in:
import semgrep

def scan(path):
    return semgrep.run(path)  # tied to semgrep!

# ✓ GOOD - Adapter pattern:
class ISASTEngine(Protocol):
    def scan(self, path): ...

class SemgrepAdapter(ISASTEngine):
    def scan(self, path):
        import semgrep
        return semgrep.run(path)

class CodeQLAdapter(ISASTEngine):
    def scan(self, path):
        import codeql
        return codeql.analyze(path)

# Usage (DI):
def run_scan(path, engine: ISASTEngine):
    return engine.scan(path)

# Easy to switch:
engine = SemgrepAdapter()  # or CodeQLAdapter()
result = run_scan(test_path, engine)
```

**Mitigacja:**
→ Zobacz `02_TO_BE.md#3.1` - Adapter pattern dla SAST engines

---

## 4. CODE-LEVEL ANTI-PATTERNS

### 4.1. Spaghetti Code

**Definicja:**
Kod bez struktury, flow control chaotyczny, trudny do śledzenia.

**Symptomy:**
- Cyclomatic complexity > 20
- Nested if-else 5+ poziomów
- Goto (w językach które to mają)
- Brak funkcji helper (wszystko w jednej funkcji)

**Gdzie Znaleziono:**
- `unified_pipeline.py:process_all()` - complexity 42!

**Przykład:**
```python
# ✗ Spaghetti Code:
def process_all(path, config):
    if path.exists():
        if config.sast_enabled:
            if config.ruleset:
                results = []
                for file in path.glob("**/*.py"):
                    if file.stat().st_size < 1000000:
                        try:
                            ast = parse(file)
                            for rule in config.ruleset:
                                if rule.applies_to(ast):
                                    finding = check_rule(ast, rule)
                                    if finding:
                                        if finding.severity == "high":
                                            results.append(finding)
                                        elif finding.severity == "critical":
                                            # ... nested logic
                        except Exception as e:
                            log.error(e)
                            if config.fail_on_error:
                                raise
                            else:
                                continue
    # ... 200 more lines
```

**Dlaczego To Złe:**
- **Readability:** Nie wiesz co robi kod
- **Bugs:** Łatwo popełnić błąd w zagnieżdżeniu
- **Testing:** Nie możesz testować części

**Prawidłowy Wzorzec: Extract Method, Guard Clauses**
```python
# ✓ GOOD - Structured:
def process_all(path, config):
    # Guard clauses (early return):
    if not path.exists():
        raise ValueError(f"Path not found: {path}")
    if not config.sast_enabled:
        return []
    
    # Extract to methods:
    files = self._collect_files(path, config)
    results = self._scan_files(files, config)
    return self._filter_results(results, config)

def _collect_files(self, path, config):
    """Collect files to scan."""
    return [
        f for f in path.glob("**/*.py")
        if f.stat().st_size < config.max_file_size
    ]

def _scan_files(self, files, config):
    """Scan each file."""
    results = []
    for file in files:
        try:
            results.extend(self._scan_file(file, config))
        except Exception as e:
            self._handle_error(e, config)
    return results
```

**Metry:**
- **Cyclomatic Complexity:** Target < 15 (obecnie 42!)
- **Nesting Depth:** Target < 4 (obecnie 7)

**Mitigacja:**
- Refactor to smaller functions
- Guard clauses (early returns)
- Extract complex conditions to named functions

---

### 4.2. Copy-Paste Programming (Code Clones)

**Definicja:**
Kopiowanie kodu zamiast DRY (Don't Repeat Yourself).

**Symptomy:**
- Duplikacje > 5%
- Similar code in multiple places
- Bug fix w jednym miejscu, ale bug pozostaje w innych

**Gdzie Znaleziono:**
- **Security_Analysis metadata duplikacja** (~8 MB, 15% całego modułu!)
- Test setup code (każdy test ma identyczny setup)

**Przykład:**
```python
# ✗ Copy-Paste (BAD):
# File A:
def process_python_file(file):
    with open(file) as f:
        content = f.read()
    ast = parse(content)
    return analyze(ast)

# File B:
def process_typescript_file(file):
    with open(file) as f:
        content = f.read()
    ast = parse_ts(content)
    return analyze_ts(ast)

# File C:
def process_go_file(file):
    with open(file) as f:
        content = f.read()
    ast = parse_go(content)
    return analyze_go(ast)

# ✓ GOOD - Extract common:
def read_file(file):
    with open(file) as f:
        return f.read()

def process_file(file, parser, analyzer):
    content = read_file(file)
    ast = parser(content)
    return analyzer(ast)

# Usage:
process_file(py_file, parse_python, analyze_python)
process_file(ts_file, parse_typescript, analyze_typescript)
```

**Dlaczego To Złe:**
- **Maintenance:** Bug fix w 1 miejscu, ale 10 kopii pozostaje
- **Size:** 15% duplikacji = 15% marnowanej przestrzeni
- **Consistency:** Kopie rozsynchronizują się

**Prawidłowy Wzorzec: DRY**
- Extract to function/class
- Use inheritance/composition
- SHARED_RESOURCES dla wspólnych danych

**Mitigacja:**
→ Zobacz `04_PROCES.md#Phase0.4` - SHARED_RESOURCES extraction

---

### 4.3. Magic Numbers

**Definicja:**
Hard-coded values bez wyjaśnienia.

**Symptomy:**
- `timeout = 60` (60 czego? dlaczego 60?)
- `if size > 1048576:` (co to za liczba?)

**Gdzie Znaleziono:**
- Rozrzucone przez cały projekt:
  ```python
  if file_size > 10485760:  # ???
  time.sleep(3)  # why 3?
  max_retries = 5  # magic!
  ```

**Dlaczego To Złe:**
- **Readability:** Co oznacza ta liczba?
- **Maintainability:** Zmiana wymaga find-all

**Prawidłowy Wzorzec: Named Constants**
```python
# ✗ BAD - Magic numbers:
if file_size > 10485760:
    raise ValueError("File too large")

time.sleep(3)

# ✓ GOOD - Named constants:
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB
RETRY_DELAY_SECONDS = 3

if file_size > MAX_FILE_SIZE_BYTES:
    raise ValueError(f"File exceeds {MAX_FILE_SIZE_BYTES} bytes")

time.sleep(RETRY_DELAY_SECONDS)
```

**Mitigacja:**
- Define constants at module top
- Config file dla wartości które mogą się zmieniać

---

### 4.4. Yo-Yo Problem

**Definicja:**
Deep directory nesting - trzeba "jeździć" w górę i dół by zrozumieć kod.

**Symptomy:**
- Średnia głębokość katalogów > 5
- Import paths: `from a.b.c.d.e.f import Thing`

**Gdzie Znaleziono:**
- **Code_Refactoring** (106 katalogów, głębokość 5-7!)

**Dlaczego To Złe:**
- **Navigation:** 5 minut żeby znaleźć plik
- **Imports:** Long, fragile import paths
- **IDE Performance:** Niektóre IDE wolne

**Prawidłowy Wzorzec: Flat is Better Than Nested**
```
# ✗ BAD - Deep nesting:
adapters/
    python/
        transformers/
            advanced/
                specialized/
                    ast/
                        visitors/
                            my_visitor.py (7 levels!)

# ✓ GOOD - Flatter (max 3-4 levels):
adapters/
    python/
        my_visitor.py

# Or if needed:
adapters/
    python/
        ast_visitors/
            my_visitor.py (3 levels)
```

**Mitigacja:**
→ Zobacz `04_PROCES.md#Phase2` - Restrukturyzacja Code_Refactoring

---

### 4.5. Lava Flow

**Definicja:**
Dead code, commented-out code - nikt nie wie czy można usunąć.

**Symptomy:**
- 500+ linii zakomentowanych
- Funkcje nigdy nie wywołane
- Imports unused

**Gdzie Znaleziono:**
```python
# Przykłady:
# def old_method():
#     # This was used before, might need later
#     return legacy_logic()

import unused_module  # TODO: remove?

def never_called_function():
    """Nobody uses this."""
    pass
```

**Dlaczego To Złe:**
- **Confusion:** "Czy to jest używane?"
- **Clutter:** Harder to navigate
- **False signals:** "Ten kod musi być ważny skoro jest"

**Prawidłowy Wzorzec: Delete It!**
- Git history keeps old code jeśli potrzebujesz
- Delete commented code
- Delete unused functions/imports

**Jak Wykrywać:**
```bash
# Find commented code:
grep -r "# def " --include="*.py"

# Find unused imports (Python):
pip install vulture
vulture .

# Find unused functions:
vulture . --min-confidence 80
```

**Mitigacja:**
- Delete ruthlessly
- CI enforcement (fail jeśli unused imports)

---

## 5. PROCESS ANTI-PATTERNS

### 5.1. Continuous Obsolescence

**Definicja:**
Dependency versions przestarzałe, nie updatowane.

**Symptomy:**
- Dependencies 2+ lat stare
- CVE w dependencies
- "Nie updatujemy bo może się zepsuć"

**Gdzie Znaleziono:**
- 12 CVE (2 Critical!)
- semgrep 1.45.0 (current: 1.50.0+)

**Dlaczego To Złe:**
- **Security:** Known vulnerabilities
- **Performance:** Brak bugfixes, optimizations
- **Debt accumulation:** Im dłużej czekasz, tym trudniej update

**Prawidłowy Wzorzec: Continuous Updates**
```yaml
# Dependabot/Renovate:
updates:
  - package-ecosystem: "pip"
    schedule:
      interval: "weekly"
    auto-merge:
      - dependency-type: "patch"  # Auto-merge patches

  - package-ecosystem: "npm"
    schedule:
      interval: "weekly"
```

**Mitigacja:**
- Automated dependency updates (Dependabot)
- Weekly review of updates
- Auto-merge patches (minor versions after testing)

---

### 5.2. Testing Only Through UI

**Definicja:**
Brak unit/integration tests, tylko manual UI testing.

**Symptoms:**
- Test coverage < 50%
- "Działa u mnie" syndrome
- Bugs discovered in production

**Where Found:**
- Test coverage 69% (not horrible, but below 85% target)
- Some modules < 60%

**Dlaczego To Złe:**
- **Slow feedback:** Manual testing takes days
- **Incomplete coverage:** Human can't test all paths
- **Regression risk:** No automated check

**Prawidłowy Wzorzec: Test Pyramid**
```
        /\
       /E2E\       (10%) - Few, slow, expensive
      /------\
     /  Integ \    (30%) - Medium
    /----------\
   / Unit Tests \  (60%) - Many, fast, cheap
  /--------------\
```

**Mitigacja:**
→ Zobacz `04_PROCES.md` - Test strategy, coverage > 85%

---

## 6. DETEKCJA I ZAPOBIEGANIE

### 6.1. Automated Detection

**CI/CD Checks:**
```yaml
# .github/workflows/anti-patterns.yml
name: Anti-Pattern Detection

on: [pull_request]

jobs:
  detect:
    runs-on: ubuntu-latest
    steps:
      - name: Check file size
        run: |
          # Detect God Objects (> 500 LOC)
          find . -name "*.py" -exec wc -l {} \; | awk '$1 > 500'
          if [ $? -eq 0 ]; then exit 1; fi
      
      - name: Check complexity
        run: |
          pip install radon
          radon cc . -a -nb
          # Fail jeśli avg complexity > 10
      
      - name: Check duplicates
        run: |
          pip install pylint
          pylint --disable=all --enable=duplicate-code .
      
      - name: Check circular deps
        run: |
          python scripts/check_circular_deps.py
      
      - name: Check dead code
        run: |
          pip install vulture
          vulture . --min-confidence 80
```

### 6.2. Code Review Checklist

**Per PR, reviewer checks:**
- [ ] No files > 500 LOC
- [ ] No functions > 50 LOC
- [ ] Complexity < 15
- [ ] No magic numbers
- [ ] No copy-paste (DRY)
- [ ] No commented code
- [ ] Dependencies fresh (< 6 months old)
- [ ] Tests added/updated
- [ ] Documentation updated

### 6.3. Architectural Tests

```python
# tests/architecture/test_anti_patterns.py
import pytest

def test_no_god_objects():
    """No file > 500 LOC."""
    large_files = find_files_larger_than(500)
    assert len(large_files) == 0, f"God Objects: {large_files}"

def test_no_circular_dependencies():
    """No circular deps between modules."""
    graph = build_module_graph()
    assert nx.is_directed_acyclic_graph(graph)

def test_no_tight_coupling():
    """All inter-module deps via interfaces."""
    violations = find_direct_imports()
    assert len(violations) == 0, f"Tight coupling: {violations}"

def test_max_directory_depth():
    """Max 4 levels of directories."""
    deep_dirs = find_directories_deeper_than(4)
    assert len(deep_dirs) == 0, f"Yo-Yo: {deep_dirs}"
```

---

## 7. EDUCATION & AWARENESS

### 7.1. Team Training

**Workshops:**
- **"Anti-Patterns 101"** - Wprowadzenie (2h)
- **"Refactoring Workshop"** - Hands-on (4h)
- **"Clean Architecture"** - Design principles (3h)

**Resources:**
- "Refactoring" by Martin Fowler
- "Clean Code" by Robert C. Martin
- "AntiPatterns" by Brown et al.

### 7.2. Documentation

- **This document** - Katalog anty-wzorców
- **ADRs** - Architecture decisions (why we chose X)
- **Runbooks** - "How to avoid X"

---

## ZAŁĄCZNIKI

### A. Quick Reference

| Anty-wzorzec | Wykrycie | Mitigacja |
|--------------|----------|-----------|
| God Object | File > 500 LOC | Extract classes/modules |
| Monolith | Module > 30 MB | Split to focused modules |
| Tight Coupling | Direct imports | Use interfaces, DI |
| Spaghetti | Complexity > 15 | Extract methods, guard clauses |
| Copy-Paste | Duplicates > 5% | DRY, extract functions |
| Magic Numbers | Hard-coded values | Named constants |
| Yo-Yo | Depth > 4 | Flatten structure |
| Lava Flow | Commented code | Delete it! |

### B. Tools

**Static Analysis:**
- **radon** - Complexity metrics
- **pylint** - Linting + duplicates
- **vulture** - Dead code detection
- **SonarQube** - Comprehensive analysis

**CI Integration:**
- **pre-commit hooks** - Catch before commit
- **GitHub Actions** - Automated checks

---

## CHECKLIST KOMPLETNOŚCI

- [x] Executive Summary (top 10, metryki)
- [x] System klasyfikacji (kategorie, severity)
- [x] Architectural anti-patterns (5 głównych)
- [x] Design anti-patterns (3 główne)
- [x] Code-level anti-patterns (5 głównych)
- [x] Process anti-patterns (2 główne)
- [x] Detekcja i zapobieganie (automated, checklist, tests)
- [x] Education & awareness (training, resources)
- [x] Załączniki (quick reference, tools)
- [x] Cross-references (PROBLEMY, PROCES, TO-BE)

**Format:** Każdy anti-pattern ma: definicję, symptomy, where found, dlaczego złe, prawidłowy wzorzec, przykłady, mitigację.
