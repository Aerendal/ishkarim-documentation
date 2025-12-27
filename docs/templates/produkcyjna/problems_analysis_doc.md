# Katalog Problemów i Błędów

> **Framework:** arc42 (Rozdział 11: Risks & Technical Debt)  
> **Data analizy:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół]  
> **Status:** [Draft/Review/Approved]  
> **Powiązane:** ← `01_AS_IS`, → `04_PROCES_REFAKTORYZACJI`, → `02_TO_BE`

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: AS-IS-ARCHITECTURE
    type: problem_source
    from_sections:
      - technical_debt_inventory
      - quality_metrics
      - performance_issues
    to_sections:
      - problem_catalog
      - severity_assessment
    influence: "AS-IS identyfikuje obszary wymagające analizy problemów"
    when:
      condition: analysis.type == "problems"
      applies: always

  - id: CODE-REVIEW
    type: quality_evidence
    from_sections:
      - code_smells
      - violation_patterns
    to_sections:
      - code_quality_problems
      - anti_patterns_list
    influence: "Code review dostarcza przykładów problemów w kodzie"
    when:
      condition: review.has_findings == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: REFACTORING-PROCESS
    type: work_definition
    from_sections:
      - prioritized_problems
      - root_causes
    to_sections:
      - refactoring_backlog
      - phase_planning
    influence: "Katalog problemów definiuje zakres refaktoringu"
    when:
      condition: document.complete == true
      applies: always

  - id: TO-BE-ARCHITECTURE
    type: requirements_input
    from_sections:
      - anti_patterns
      - quality_issues
    to_sections:
      - quality_attributes
      - architecture_requirements
    influence: "Problemy informują o wymaganiach dla TO-BE"
    when:
      condition: problems.analyzed == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: ANTI-PATTERNS-DOC
    relationship: detailed_catalog
    sections_mapping:
      - from: anti_pattern_definitions
        to: identified_anti_patterns
    usage: "Katalog anty-wzorców klasyfikuje znalezione problemy"
```

### Satellite Documents

```yaml
satellites:
  - name: PROBLEM-TICKETS
    purpose: "Issue tickets dla każdego zidentyfikowanego problemu"
    trigger: during_analysis
    lifecycle: until_resolved
    retention: permanent

  - name: ROOT-CAUSE-ANALYSIS
    purpose: "Szczegółowa analiza przyczyn głównych problemów"
    trigger: for_critical_issues
    lifecycle: per_problem
    retention: permanent
```

---

## EXECUTIVE SUMMARY

### Cel Dokumentu
[Dlaczego katalogujemy problemy - 2-3 zdania]

### Status Dashboard Problemów

| Kategoria | Total | Critical | High | Medium | Low | Trend |
|-----------|-------|----------|------|--------|-----|-------|
| **Architektura** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **Techniczne** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **Bezpieczeństwo** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **Jakość kodu** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **LSP Diagnostics** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **Performance** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **DevOps/CI** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **Dokumentacja** | [N] | [X] | [X] | [X] | [X] | ↑/→/↓ |
| **TOTAL** | [N] | [X] | [X] | [X] | [X] | - |

### Top 10 Problemów (Priorytet)

| Rank | ID | Problem | Severity | Impact | Effort | Moduły |
|------|----|---------| ---------|--------|--------|--------|
| 1 | [A-001] | [Problem] | P0 Critical | [Business/Technical] | XL | [Moduły] |
| 2 | [S-001] | [CVE] | P0 Critical | Security | M | [Moduły] |
| 3 | [A-002] | [Problem] | P1 High | [Impact] | L | [Moduły] |
| ... | ... | ... | ... | ... | ... | ... |
| 10 | [T-010] | [Problem] | P2 Medium | [Impact] | S | [Moduły] |

### Metryki Ogólne

- **Całkowita liczba problemów:** [N]
- **Krytyczne (P0):** [X] - wymaga natychmiastowej akcji
- **Wysokie (P1):** [Y] - naprawić w ciągu 1-2 tygodni
- **Średnie (P2):** [Z] - naprawić w ciągu miesiąca
- **Niskie (P3):** [W] - backlog

---

## 1. SYSTEM KLASYFIKACJI PROBLEMÓW

### 1.1. Kategorie

| Prefix | Kategoria | Opis | Przykład |
|--------|-----------|------|----------|
| **A-** | Architektura | Problemy strukturalne, coupling, boundaries | A-001: Monolit Security_Analysis |
| **T-** | Techniczne | Performance, bugs, implementation issues | T-001: Symbol graph > 30s |
| **S-** | Security | CVE, vulnerabilities, compliance gaps | S-001: CVE-2024-XXXXX |
| **Q-** | Jakość kodu | Code smells, complexity, duplikacje | Q-001: God Object 1842 LOC |
| **L-** | LSP Diagnostics | Type errors, undefined symbols, import issues | L-001: Missing type annotation |
| **P-** | Performance | Latency, memory, CPU bottlenecks | P-001: Canvas p95 > SLA |
| **D-** | DevOps/CI | Build failures, flaky tests, deployment | D-001: 22% CI failure rate |
| **DOC-** | Dokumentacja | Missing docs, outdated, incomplete | DOC-001: 8/14 bez README |

### 1.2. Severity Levels

| Level | Label | Kryteria | SLA Response | Przykład |
|-------|-------|----------|--------------|----------|
| **P0** | Critical | System broken, security risk, data loss | < 4h | Critical CVE, complete module failure |
| **P1** | High | Major functionality broken, poor UX | < 1 week | Coupling issues, performance degradation |
| **P2** | Medium | Moderate impact, workaround exists | < 1 month | Code smells, minor bugs |
| **P3** | Low | Nice to have, cosmetic | Backlog | Documentation gaps, refactoring opportunities |

### 1.3. Impact Areas

| Impact | Opis | Metryka |
|--------|------|---------|
| **Reliability** | System crashes, errors | MTBF, error rate |
| **Performance** | Slow response, high resource usage | Latency, throughput |
| **Security** | Vulnerabilities, data exposure | CVE count, CVSS score |
| **Maintainability** | Hard to change, understand | Technical debt, complexity |
| **Scalability** | Cannot handle growth | Max users, max data |
| **Usability** | Poor UX, confusing | User satisfaction, time to complete task |
| **Compliance** | Regulatory, standards | OWASP, CWE coverage |

### 1.4. Effort Estimation

| Size | Person-Days | Przykład |
|------|-------------|----------|
| **XS** | 0.5-1 | Zmiana konfiguracji, drobna poprawka |
| **S** | 1-3 | Bug fix, minor refactoring |
| **M** | 3-10 | Module extraction, interface definition |
| **L** | 10-20 | Major refactoring, new subsystem |
| **XL** | 20-40 | Architecture overhaul, split monolith |
| **XXL** | 40+ | Complete rewrite |

---

## 2. PROBLEMY ARCHITEKTONICZNE (A-XXX)

### Format Opisu Problemu:

**ID:** A-XXX  
**Tytuł:** [Krótki opis problemu]  
**Severity:** P0 | P1 | P2 | P3  
**Impact:** [Area + metryka]  
**Affected Modules:** [Lista modułów]  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open | In Progress | Resolved | Won't Fix

**Opis:**
[Szczegółowy opis problemu - co jest nie tak]

**Przykłady:**
[Konkretne przykłady z kodu/architektury]

**Root Cause:**
[Głębsza przyczyna - dlaczego problem powstał]

**Impact Analysis:**
- **Reliability:** [Wpływ na niezawodność]
- **Maintainability:** [Wpływ na łatwość zmian]
- **Performance:** [Wpływ na wydajność]
- **[Inne]:** [...]

**Proposed Solution:**
[Krótki opis rozwiązania - szczegóły w → `04_PROCES_REFAKTORYZACJI`]

**Effort:** XS | S | M | L | XL | XXL  
**Priority:** P0 | P1 | P2 | P3  
**Owner:** [Team/Osoba]

**Dependencies:**
- **Blokuje:** [Inne problemy, które nie mogą być naprawione póki ten jest otwarty]
- **Zablokowane przez:** [Problemy, które muszą być naprawione najpierw]

**References:**
- → `01_AS_IS.md#X.Y` (gdzie opisany stan obecny)
- → `02_TO_BE.md#X.Y` (jak ma być naprawione)
- → Issue #123 (jeśli istnieje)

---

### 2.1. A-001: Security_Analysis to Monolit

**Severity:** P0 Critical  
**Impact:** Maintainability (Technical Debt: 25 dni), Scalability  
**Affected Modules:** Security_Analysis  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open → **Zaplanowane do naprawy w TO-BE**

**Opis:**
Security_Analysis (48 MB, 60% całości projektu) łączy 4 różne funkcjonalności bez wyraźnych granic:
1. SAST (Static Application Security Testing)
2. SCA (Software Composition Analysis)
3. Secrets Scanning
4. Fix Proposals + Reachability Analysis

To narusza Single Responsibility Principle. Moduł zmienia się z wielu powodów (nowe reguły SAST, nowe źródła CVE, nowa logika fix generation).

**Przykłady:**
```
Security_Analysis/
├── sast/           # 15 MB - SAST engine
├── sca/            # 18 MB - SCA engine
├── secrets/        # 8 MB - Secrets scanner
├── fixes/          # 5 MB - Fix proposals
├── reachability/   # 2 MB - Reachability analysis
└── L1_FAZA0/       # ⚠️ 8 MB duplikacji metadata!
```

**Root Cause:**
- Historyczny wzrost: Moduł zaczynał jako SAST, potem dodano SCA, potem Secrets, etc.
- Brak refactoringu przy dodawaniu nowych features
- Presja czasu: "Dodajmy to tutaj, bo już mamy security"

**Impact Analysis:**
- **Maintainability:** 
  - Zmiana w jednej części może zepsuć inną
  - 1,842 LOC God Object (`unified_pipeline.py`)
  - Test coverage tylko 68% (trudno testować monolit)
  - Technical debt: 25 person-days
  
- **Scalability:**
  - Scan 1000 plików = 45s (blisko SLA 60s)
  - Przy większych projektach (2000+ files) timeout!
  
- **Reusability:**
  - Nie możemy użyć SCA bez ciągnięcia całego SAST
  - Inne moduły muszą zależeć od 48 MB tylko dla 1 funkcji

**Proposed Solution:**
Split na 4 moduły (→ `02_TO_BE.md#3.1-3.4`):
1. **SAST_Engine** (~12 MB) - tylko SAST
2. **SCA_Engine** (~15 MB) - tylko SCA + CVE lookup
3. **Secrets_Scanner** (~8 MB) - tylko secrets detection
4. **FixOps** (~8 MB) - fix proposals, ranking, reachability

**Effort:** XL (8-12 tygodni)  
**Priority:** P0  
**Owner:** Security Team + Architecture Team

**Dependencies:**
- **Blokuje:** A-004 (tight coupling Security ↔ IR_SBOM)
- **Zablokowane przez:** Brak (może zacząć natychmiast)

**References:**
- → `01_AS_IS.md#3.1` (szczegóły Security_Analysis)
- → `02_TO_BE.md#3.1-3.4` (docelowa struktura 4 modułów)
- → `04_PROCES.md#Phase1` (plan podziału)

---

### 2.2. A-002: Duplikacja Metadata w Security_Analysis

**Severity:** P1 High  
**Impact:** Disk Space (8 MB waste), Maintainability  
**Affected Modules:** Security_Analysis  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open

**Opis:**
Katalog `Security_Analysis/L1_FAZA0/metadata/normalized/` (~8 MB) zawiera duplikaty danych już obecnych w innych częściach projektu lub jest przestarzały.

**Przykłady:**
```bash
$ du -sh Security_Analysis/L1_FAZA0/
8.0M    Security_Analysis/L1_FAZA0/

$ find Security_Analysis/L1_FAZA0/ -name "*.json" | wc -l
342 plików JSON
```

**Root Cause:**
- Snapshot mechanizm: L1_FAZA0, L1_FAZA1 jako "checkpoints"
- Metadata kopiowana zamiast linkowana/referencowana
- Brak garbage collection dla starych snapshots

**Impact Analysis:**
- **Disk Space:** 8 MB z 48 MB (17% modułu!)
- **Maintainability:** Konfuzja - która kopia jest źródłem prawdy?
- **Performance:** Dłuższe scany (więcej plików do przejrzenia)

**Proposed Solution:**
1. Utworzenie **SHARED_RESOURCES/metadata/** (→ `02_TO_BE.md#5`)
2. Migration danych do shared location
3. Usunięcie duplikatów z Security_Analysis
4. References zamiast copies

**Effort:** M (2-3 tygodnie)  
**Priority:** P1  
**Owner:** Architecture Team

**Dependencies:**
- **Blokuje:** Brak
- **Zablokowane przez:** Utworzenie SHARED_RESOURCES (→ Phase 0 w `04_PROCES.md`)

**References:**
- → `01_AS_IS.md#3.1` (obecna struktura)
- → `02_TO_BE.md#5` (SHARED_RESOURCES plan)

---

### 2.3. A-003: Code_Refactoring ma 106 Katalogów - Chaos

**Severity:** P1 High  
**Impact:** Maintainability (navigation nightmare), Onboarding (confusion)  
**Affected Modules:** Code_Refactoring  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open

**Opis:**
Moduł Code_Refactoring (4.6 MB, 995 plików) ma 106 katalogów. Średnia głębokość: 5 poziomów. Brak jasnej struktury.

**Przykłady:**
```bash
$ find Moduły/Code_Refactoring -type d | wc -l
106

$ find Moduły/Code_Refactoring -type d | head -10
Moduły/Code_Refactoring/adapters/python/transformers/...
Moduły/Code_Refactoring/adapters/typescript/parsers/...
Moduły/Code_Refactoring/core/engines/impact/...
Moduły/Code_Refactoring/core/engines/planner/...
Moduły/Code_Refactoring/utils/helpers/language_detection/...
...
```

**Root Cause:**
- Over-engineering: Zbyt wiele warstw abstrakcji
- Brak refactoringu przy dodawaniu języków
- Feature sprawl: "Dodajmy nowy katalog dla każdej rzeczy"

**Impact Analysis:**
- **Onboarding:** Nowi devs gubią się (3 tygodnie onboarding!)
- **Maintainability:** "Gdzie jest kod dla X?" = 15 min szukania
- **IDE Performance:** Niektóre IDE wolne przy 100+ katalogach

**Proposed Solution:**
Restrukturyzacja na 3 moduły z płaską hierarchią (→ `02_TO_BE.md#3.9-3.10`):
1. **Core_Engine** - refactoring logic (max 3 poziomy katalogów)
2. **Language_Adapters** - adaptery per język (flat structure)
3. **Impact_Planner** - impact analysis

**Effort:** L (4-6 tygodni)  
**Priority:** P1  
**Owner:** Dev Tools Team

**Dependencies:**
- **Blokuje:** Onboarding nowych devs, performance IDE
- **Zablokowane przez:** Brak

**References:**
- → `01_AS_IS.md#3.3` (obecna struktura Code_Refactoring)
- → `02_TO_BE.md#3.9-3.10` (docelowe 3 moduły)

---

[Powtórzyć format dla wszystkich problemów architektonicznych]

**Pozostałe problemy architektoniczne:**
- A-004: Tight coupling Security_Analysis ↔ IR_SBOM_Impact
- A-005: Brak wyraźnych interfejsów między modułami (95% importuje implementacje bezpośrednio)
- A-006: Provenance_Secrets łączy 2 niezależne funkcjonalności
- A-007: IR_SBOM_Impact - 3 engines bez separacji
- A-008: Brak wersjonowania modułów (compatibility nightmare)
- A-009: God Objects w 3 modułach (> 1000 LOC)
- A-010: Circular dependency risk (nie egzekwowany w CI)

---

## 3. PROBLEMY TECHNICZNE (T-XXX)

### 3.1. T-001: Symbol Graph Build > 30s dla Dużych Projektów

**Severity:** P2 Medium  
**Impact:** Performance (granica SLA 30s), UX (developer frustration)  
**Affected Modules:** IR_SBOM_Impact (SymbolGraph_Builder)  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open

**Opis:**
Budowa grafu symboli dla projektów > 2000 plików trwa 22s (avg), 35s (p95). SLA: 30s. Jesteśmy na granicy, przy wzroście projektu przekroczymy SLA.

**Przykłady:**
```python
# Benchmark results:
Project Size    | Avg Time | p95 Time | SLA | Status
500 files       | 5s       | 8s       | ✓   | OK
1000 files      | 12s      | 18s      | ✓   | OK
2000 files      | 22s      | 35s      | ⚠️  | Granica
5000 files      | 58s      | 90s      | ✗   | FAIL
```

**Root Cause:**
- Single-threaded parsing AST
- Brak cache (każdy build od zera)
- Inefficient graph construction (O(n²) w niektórych przypadkach)

**Impact Analysis:**
- **Performance:** Blisko SLA breach
- **Scalability:** Nie zadziała dla enterprise projects (10k+ files)
- **UX:** Developers czekają, frustration

**Proposed Solution:**
1. **Parallelization:** ProcessPoolExecutor dla parsowania plików
2. **Caching:** Cache parsed ASTs (invalidate on file change)
3. **Incremental:** Rebuild tylko zmienione części grafu
4. **Algorithmic:** O(n log n) graph construction

**Effort:** M (3-4 tygodnie)  
**Priority:** P2 (P1 jeśli mamy enterprise clients)  
**Owner:** Platform Team

**Dependencies:**
- **Blokuje:** Scalability dla > 5k files
- **Zablokowane przez:** Brak

**References:**
- → `01_AS_IS.md#10.1` (performance benchmarks)
- → `02_TO_BE.md#8.2` (optimization strategies)

---

[Powtórzyć dla pozostałych problemów technicznych]

**Pozostałe problemy techniczne:**
- T-002: Canvas p95 latency > SLA przy 40+ users (120ms vs 100ms)
- T-003: God Object unified_pipeline.py (1,842 LOC, complexity 42!)
- T-004: Brak cache - każdy SAST scan od zera (45s avg)
- T-005: Flaky tests - 22% CI failure rate (intermittent failures)
- T-006: Memory leak w Collaborative_Canvas (WebSocket connections)
- T-007: SBOM generation nie obsługuje monorepos (single package.json assumption)
- T-008: Race condition w Secrets_Broker lease expiration
- T-009: Hard-coded paths (nie działa poza Linux)
- T-010: No graceful degradation przy API failures (crash vs fallback)

---

## 4. PROBLEMY BEZPIECZEŃSTWA (S-XXX)

### 4.1. S-001: CVE-2024-XXXXX w semgrep < 1.50

**Severity:** P0 Critical  
**Impact:** Security (CVSS 9.8 - Remote Code Execution)  
**Affected Modules:** Security_Analysis (SAST engine)  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open

**Opis:**
Zależność `semgrep 1.45.0` ma krytyczną lukę CVE-2024-XXXXX: RCE via malicious rule file.

**CVE Details:**
- **CVE ID:** CVE-2024-XXXXX
- **CVSS Score:** 9.8 (Critical)
- **Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **CWE:** CWE-94: Improper Control of Generation of Code
- **Affected Versions:** semgrep < 1.50.0
- **Fixed in:** semgrep >= 1.50.0

**Attack Scenario:**
1. Attacker crafts malicious semgrep rule file
2. User runs SAST scan with attacker's rules (e.g., from public registry)
3. semgrep executes arbitrary code on user's machine
4. RCE achieved

**Reachability Analysis:**
✅ **REACHABLE** - Używamy semgrep do SAST, akceptujemy custom rules.

**Impact Analysis:**
- **Confidentiality:** HIGH - Attacker może czytać pliki
- **Integrity:** HIGH - Attacker może modyfikować kod
- **Availability:** HIGH - Attacker może usunąć dane/shutdown

**Proposed Solution:**
1. **Immediate:** Upgrade semgrep 1.45.0 → 1.50.0+ (patch)
2. **Short-term:** Rule validation - tylko trusted sources
3. **Long-term:** Sandboxing semgrep execution (containers)

**Effort:** S (1 dzień patch, 1 tydzień testing)  
**Priority:** P0 Critical - **FIX ASAP (< 24h)**  
**Owner:** Security Team

**Dependencies:**
- **Blokuje:** Compliance, production deployment
- **Zablokowane przez:** Brak

**References:**
- → CVE Details: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-XXXXX
- → semgrep Release Notes: https://github.com/returntocorp/semgrep/releases/tag/v1.50.0
- → `01_AS_IS.md#11.2` (CVE list)
- → `02_TO_BE.md#7.5` (CVE management process)

---

[Powtórzyć dla pozostałych CVE i problemów security]

**Pozostałe problemy bezpieczeństwa:**
- S-002: CVE-2024-YYYYY w node-sass < 9.0 (CVSS 7.5 High)
- S-003: Brak RBAC/Autoryzacji (Critical gap)
- S-004: Logs zawierają PII (GDPR violation risk)
- S-005: Brak rate limiting (DoS risk)
- S-006: Secrets w environment variables (nie rotated)
- S-007: Brak input size limits (memory exhaustion attack)
- S-008: CSRF protection nie wszędzie (Canvas mutations)
- S-009: Hardcoded admin credentials w testach (committed to git!)
- S-010: Brak Content Security Policy (XSS risk)

---

## 5. PROBLEMY JAKOŚCI KODU (Q-XXX)

### 5.1. Q-001: God Object unified_pipeline.py (1,842 LOC)

**Severity:** P2 Medium  
**Impact:** Maintainability (Complexity 42), Testability (tylko 60% coverage)  
**Affected Modules:** Security_Analysis  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open

**Opis:**
Plik `Security_Analysis/L1_FAZA1/tools/unified_pipeline.py` ma 1,842 linii kodu w jednym pliku. Funkcja `process_all()` ma cyclomatic complexity 42 (target: < 15).

**Metrics:**
```
File: unified_pipeline.py
- LOC: 1,842
- Functions: 23
- Classes: 3
- Avg Complexity: 18.5
- Max Complexity: 42 (process_all)
- Test Coverage: 60%
- Duplicate Code: 12% (wewnątrz pliku!)
```

**Root Cause:**
- "One file to rule them all" anti-pattern
- Incremental additions bez refactoringu
- Brak code review enforcement (jak to przeszło?!)

**Impact Analysis:**
- **Maintainability:** Zmiana zajmuje 3× dłużej (understanding overhead)
- **Testability:** 60% coverage, trudno mock dependencies
- **Bug Risk:** Complexity 42 = wysoka szansa na bugs

**Proposed Solution:**
Refactoring do modułów (→ `04_PROCES.md`):
1. Extract classes per responsibility (SRP)
2. Split process_all() na 5-10 mniejszych funkcji
3. Dependency Injection dla testability
4. Target: < 300 LOC per file, complexity < 15

**Effort:** M (2-3 tygodnie)  
**Priority:** P2  
**Owner:** Security Team

**Dependencies:**
- **Blokuje:** Zwiększenie test coverage
- **Zablokowane przez:** Brak (może być równolegle z A-001)

---

[Powtórzyć dla pozostałych code quality issues]

**Pozostałe problemy jakości:**
- Q-002: 15% duplikacji kodu (target: < 5%)
- Q-003: Brak type hints w 40% Python code
- Q-004: Inconsistent naming (camelCase vs snake_case w tym samym module)
- Q-005: Magic numbers w kodzie (brak const defines)
- Q-006: Dead code (12 funkcji nigdy nie wywołanych)
- Q-007: Commented-out code (500+ linii zakomentowanych)
- Q-008: No docstrings w 60% funkcji publicznych
- Q-009: Global variables w 3 modułach
- Q-010: 200+ TODO/FIXME comments (tech debt indicators)

---

## 6. PROBLEMY LSP DIAGNOSTICS (L-XXX)

### 6.1. L-001: Missing Type Annotations (Python)

**Severity:** P3 Low  
**Impact:** Developer Experience (IDE hints), Maintainability  
**Affected Modules:** Wszystkie Python modules (40% funkcji)  
**Discovered:** [YYYY-MM-DD via LSP scan]  
**Status:** Open

**Opis:**
40% funkcji Python nie ma type hints. Pyright/mypy zgłaszają 847 warnings.

**Przykłady:**
```python
# ✗ Źle (brak type hints):
def scan_code(path, rules):
    return process(path, rules)

# ✓ Dobrze:
def scan_code(path: Path, rules: list[str]) -> ScanResult:
    return process(path, rules)
```

**Impact Analysis:**
- **Developer Experience:** Brak autocomplete, hints
- **Bug Prevention:** Type checker nie wykryje błędów
- **Documentation:** Code self-documenting gdy ma types

**Proposed Solution:**
1. Automated: `pytype` / `monkeytype` generowanie hints
2. Manual: Review i fix generated hints
3. CI Enforcement: mypy/pyright strict mode

**Effort:** M (1-2 tygodnie distributed across team)  
**Priority:** P3  
**Owner:** All Python developers

---

[Powtórzyć dla innych LSP diagnostics]

**Pozostałe LSP diagnostics:**
- L-002: Undefined imports w TypeScript (15 plików)
- L-003: Unused variables (234 instances)
- L-004: Unreachable code (45 instances)
- L-005: Type mismatches TypeScript (89 errors)

---

## 7. PROBLEMY PERFORMANCE (P-XXX)

[Lista już opisana w T-XXX, ale można wydzielić osobną kategorię jeśli preferowana]

---

## 8. PROBLEMY DEVOPS/CI (D-XXX)

### 8.1. D-001: Flaky Tests - 22% CI Failure Rate

**Severity:** P1 High  
**Impact:** Developer Productivity (re-runs cost time), CI/CD Reliability  
**Affected Modules:** Wszystkie (głównie Integration tests)  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open

**Opis:**
22% build failures w CI pipeline. Po re-run: 85% succeeds (= flaky tests, nie real failures).

**Metrics:**
```
Last 100 builds:
- Total: 100
- Failed first run: 22
- Passed on re-run: 19
- Actual failures: 3
- Flaky rate: 19/100 = 19%
```

**Root Causes:**
1. **Race conditions** w async tests (timing-dependent)
2. **Shared state** między testami (nie isolated)
3. **External dependencies** (network, API calls w testach)
4. **Timeouts** zbyt krótkie (marginal timings)

**Impact Analysis:**
- **Developer Time:** 2h/dev/week na debugowanie flaky tests
- **CI Cost:** 2× więcej builds (re-runs)
- **Confidence:** Devs ignorują failures ("to pewnie flaky")

**Proposed Solution:**
1. **Quarantine flaky tests** - osobny pipeline
2. **Fix root causes:**
   - Proper async test patterns (await all)
   - Isolated test data (fixtures per test)
   - Mock external deps
   - Increase timeouts to reasonable values
3. **Monitoring:** Track flakiness per test

**Effort:** M (2-3 tygodnie - distributed)  
**Priority:** P1  
**Owner:** QA Team + Dev Team (divided by ownership)

---

[Powtórzyć dla innych DevOps issues]

**Pozostałe problemy DevOps:**
- D-002: Build time 20 min (target: < 15 min)
- D-003: Brak dependency caching w CI (rebuild from scratch każdy raz)
- D-004: No parallel test execution (sequential = slow)
- D-005: Deployment rollback takes 15 min (target: < 5 min)

---

## 9. PROBLEMY DOKUMENTACJI (DOC-XXX)

### 9.1. DOC-001: 8/14 Modułów bez README

**Severity:** P2 Medium  
**Impact:** Onboarding (3 tygodnie!), Knowledge Transfer  
**Affected Modules:** 8 modułów bez README  
**Discovered:** [YYYY-MM-DD]  
**Status:** Open

**Opis:**
57% modułów (8/14) nie ma README.md. Nowi devs nie wiedzą jak zacząć.

**Missing READMEs:**
1. Advanced_Testing
2. Attack_Surface
3. Arch_Fitness
4. Multirepo_Orchestrator
5. Runtime_Feedback
6. LLM_Auth_Providers
7. Diff_Viewer
8. CICD_Tooling

**Impact Analysis:**
- **Onboarding:** Nowi devs 3 tygodnie zamiast 1 tydzień
- **Knowledge Transfer:** Tribal knowledge (tylko w głowach)
- **Adoption:** Nikt nie używa modułów bo nie wie jak

**Proposed Solution:**
Template-based documentation (→ `08_SZABLON_MODUŁ.md`):
- README per moduł (quick start)
- ARCHITECTURE per moduł (design)
- API_REFERENCE per moduł

**Effort:** S (1-2 dni per moduł = 2 tygodnie total)  
**Priority:** P2  
**Owner:** Module owners (distributed)

---

[Powtórzyć dla innych doc issues]

**Pozostałe problemy dokumentacji:**
- DOC-002: Brak Architecture docs (14/14 modułów!)
- DOC-003: API documentation outdated (60% endpoints changed)
- DOC-004: No examples/tutorials
- DOC-005: Diagrams missing (tylko text descriptions)

---

## 10. MACIERZ PROBLEMÓW vs MODUŁY

| Problem ID | Severity | Sec_Analysis | Collab_Canvas | Code_Refact | Prov_Secrets | IR_SBOM | ... |
|------------|----------|--------------|---------------|-------------|--------------|---------|-----|
| A-001 | P0 | ●●● | - | - | - | - | ... |
| A-002 | P1 | ●● | - | - | - | - | ... |
| A-003 | P1 | - | - | ●●● | - | - | ... |
| S-001 | P0 | ●●● | - | - | - | - | ... |
| S-003 | P0 | ●● | ●● | ● | ● | ● | ... |
| T-001 | P2 | - | - | - | - | ●● | ... |
| Q-001 | P2 | ●●● | - | - | - | - | ... |
| D-001 | P1 | ● | ● | ● | ● | ● | ... |

**Legenda:** ●●● = Primary impact, ●● = Secondary, ● = Minor

**Hotspot Modules (najwięcej problemów):**
1. **Security_Analysis:** 8 problemów (A-001, A-002, S-001, Q-001, ...)
2. **Code_Refactoring:** 5 problemów (A-003, T-001, ...)
3. **IR_SBOM_Impact:** 4 problemy (A-007, T-001, ...)

---

## 11. MACIERZ RYZYKA

**Prawdopodobieństwo × Wpływ:**

```
        │ Low Impact │ Medium Impact │ High Impact │ Critical Impact
────────┼─────────────┼───────────────┼─────────────┼─────────────────
High    │             │ A-003, D-001  │ A-002       │ S-003
Prob    │             │               │             │
────────┼─────────────┼───────────────┼─────────────┼─────────────────
Medium  │ Q-002-Q-010 │ T-001, P-001  │ A-004, A-005│ A-001
Prob    │ DOC-001-005 │               │             │
────────┼─────────────┼───────────────┼─────────────┼─────────────────
Low     │ L-001-L-005 │ Q-001, T-003  │             │ S-001, S-002
Prob    │             │               │             │
────────┴─────────────┴───────────────┴─────────────┴─────────────────
```

**Focus Area:** Prawy górny kwadrant (High Prob × High/Critical Impact)
- A-001, A-002, S-003, D-001

---

## 12. PLAN NAPRAWY - PRIORYTETYZACJA

### 12.1. Phase 0: Emergency Fixes (Week 1)

**P0 Critical - Fix ASAP (<24h-48h):**
- [ ] S-001: Patch CVE-2024-XXXXX (upgrade semgrep)
- [ ] S-002: Patch CVE-2024-YYYYY (upgrade node-sass)

**Effort:** 2-3 dni  
**Owner:** Security Team

### 12.2. Phase 1: Foundation (Week 1-2)

**P0 + P1 High Priority:**
- [ ] S-003: Implementacja RBAC (2 tygodnie)
- [ ] S-004: Sanityzacja PII w logach (1 tydzień)
- [ ] D-001: Fix top 10 flaky tests (1 tydzień)

**Effort:** 2 tygodnie  
**Owner:** Security + QA Teams

### 12.3. Phase 2: Architecture Overhaul (Week 3-14)

**P0 Architectural:**
- [ ] A-001: Split Security_Analysis (8 tygodni) ← **BIGGEST IMPACT**
- [ ] A-003: Restrukturyzacja Code_Refactoring (6 tygodni)
- [ ] A-002: SHARED_RESOURCES + cleanup duplikacji (2 tygodnie)

[Details → `04_PROCES_REFAKTORYZACJI.md`]

### 12.4. Phase 3: Quality & Performance (Week 15-20)

**P2 Medium:**
- [ ] T-001: Performance optimization SymbolGraph (3 tygodnie)
- [ ] Q-001: Refactor God Objects (3 tygodnie)
- [ ] DOC-001: Complete documentation (2 tygodnie)

### 12.5. Phase 4: Polish (Week 21-24)

**P3 Low + remaining P2:**
- [ ] L-001: Type hints (2 tygodnie distributed)
- [ ] Q-002-Q-010: Code quality improvements
- [ ] Remaining tech debt

---

## 13. METRYKI POSTĘPU

### 13.1. KPI Tracking

| Kategoria | Baseline | Target | Current | % Done |
|-----------|----------|--------|---------|--------|
| **Critical (P0)** | 12 | 0 | [X] | [Y%] |
| **High (P1)** | 18 | < 5 | [X] | [Y%] |
| **Medium (P2)** | 25 | < 10 | [X] | [Y%] |
| **Low (P3)** | 30 | < 15 | [X] | [Y%] |
| **Total** | 85 | < 30 | [X] | [Y%] |

**Target:** Redukcja 65% problemów (85 → 30)

### 13.2. Burn-down Chart

```
Problems
│
85 ●
│   ╲
│     ╲
│       ●
50│         ╲
│           ╲
│             ●
30│               ─────●
│                      
0 └─────────────────────────────▶ Time
   W0  W4  W8  W12 W16 W20 W24
```

---

## ZAŁĄCZNIKI

### A. Szczegółowe Logi LSP Diagnostics

[Eksport z LSP scanner - pełna lista warnings/errors]

### B. CVE Database Snapshot

[Lista wszystkich znanych CVE z datami discovery]

### C. Technical Debt Metrics

**SonarQube Report:**
- Debt Ratio: 18.5%
- Code Smells: 342
- Bugs: 23
- Vulnerabilities: 12

---

## CHECKLIST KOMPLETNOŚCI

- [x] Executive Summary (dashboard, top 10, metryki)
- [x] System klasyfikacji (kategorie, severity, impact, effort)
- [x] Problemy architektoniczne (A-XXX) - format standardowy
- [x] Problemy techniczne (T-XXX)
- [x] Problemy bezpieczeństwa (S-XXX) - CVE details
- [x] Problemy jakości kodu (Q-XXX)
- [x] LSP Diagnostics (L-XXX)
- [x] DevOps/CI (D-XXX)
- [x] Dokumentacja (DOC-XXX)
- [x] Macierz problemów vs moduły
- [x] Macierz ryzyka (probability × impact)
- [x] Plan naprawy - priorytetyzacja (phases)
- [x] Metryki postępu (KPI, burn-down)
- [x] Cross-references (links do AS-IS, TO-BE, PROCES)

**Wypełnienie:** Każdy problem używa standardowego formatu z ID, severity, impact, root cause, solution, effort, dependencies, references.
