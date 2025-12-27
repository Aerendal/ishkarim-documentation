# Architektura Docelowa (TO-BE)

> **Framework:** arc42 + C4 Model + Clean Architecture Principles  
> **Data opracowania:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół]  
> **Status:** [Draft/Review/Approved]  
> **Powiązane:** ← `01_AS_IS`, → `04_PROCES_REFAKTORYZACJI`, → `06_PUNKTY_INTEGRACJI`

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: AS-IS-ARCHITECTURE
    type: baseline
    from_sections:
      - current_problems
      - technical_constraints
    to_sections:
      - improvement_areas
      - migration_considerations
    influence: "Stan obecny określa co trzeba poprawić"
    when:
      condition: document.type == "to_be"
      applies: always

  - id: PROBLEMS-ANALYSIS
    type: requirements_source
    from_sections:
      - root_causes
      - anti_patterns
    to_sections:
      - architecture_decisions
      - design_patterns
    influence: "Problemy definiują wymagania dla nowej architektury"
    when:
      condition: analysis.has_problems == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: REFACTORING-PROCESS
    type: implementation_plan
    from_sections:
      - target_architecture
      - migration_path
    to_sections:
      - refactoring_phases
      - migration_steps
    influence: "TO-BE definiuje docelowy stan dla refaktoringu"
    when:
      condition: document.approved == true
      applies: always

  - id: INTEGRATION-POINTS
    type: interface_definition
    from_sections:
      - module_boundaries
      - api_contracts
    to_sections:
      - interface_catalog
      - contract_specifications
    influence: "Docelowa architektura określa komunikację modułów"
    when:
      condition: architecture.is_modular == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: ARCHITECTURE-PRINCIPLES
    relationship: guiding_constraints
    sections_mapping:
      - from: principles_catalog
        to: architecture_decisions
    usage: "Zasady architektury kierują decyzjami projektowymi"
```

### Satellite Documents

```yaml
satellites:
  - name: TARGET-ARCHITECTURE-DIAGRAMS
    purpose: "Wizualizacje docelowej architektury"
    trigger: during_design
    lifecycle: continuous
    retention: permanent

  - name: ARCHITECTURE-DECISION-RECORDS
    purpose: "ADR dla każdej decyzji architektonicznej"
    trigger: per_decision
    lifecycle: permanent
    retention: permanent
```

---

## EXECUTIVE SUMMARY

### Wizja
[Jaka jest docelowa wizja architektury - 2-3 zdania opisujące cel końcowy]

### Cele Transformacji

1. **[Cel 1]:** [np. Zwiększenie modularności poprzez podział monolitów]
   - **KPI:** [Liczba modułów: 14 → 26]
   - **Termin:** [YYYY-MM]

2. **[Cel 2]:** [np. Poprawa skalowalności]
   - **KPI:** [p95 latency < 100ms]
   - **Termin:** [YYYY-MM]

3. **[Cel 3]:** [np. Redukcja technical debt o 50%]
   - **KPI:** [Debt ratio: 18.5% → < 9%]
   - **Termin:** [YYYY-MM]

### Transformation Dashboard

| Metryka | Obecny (AS-IS) | Docelowy (TO-BE) | Delta | Status |
|---------|----------------|------------------|-------|--------|
| Liczba modułów | 14 | 26 | +12 | 📋 Planowane |
| Największy moduł | 48 MB | < 15 MB | -69% | 📋 Planowane |
| Test coverage | 69% | > 85% | +16pp | 📋 Planowane |
| Technical debt | 147 dni | < 75 dni | -49% | 📋 Planowane |
| CVE Critical | 2 | 0 | -100% | 📋 Planowane |
| Deployment time | N/A | < 15 min | - | 📋 Nowe |

### Kluczowe Zmiany

**Strukturalne:**
- Podział 4 największych modułów na 12 mniejszych
- Utworzenie SHARED_RESOURCES dla wspólnych zasobów
- Hierarchiczna organizacja (CORE / INTELLIGENCE / PLATFORM / etc.)

**Architektoniczne:**
- Definicja wyraźnych interfejsów między modułami
- Dependency Inversion Principle
- Contract-based integration

**Operacyjne:**
- Observability stack (metryki, tracing, alerting)
- Automated deployment pipeline
- Per-module versioning

---

## 1. ZASADY ARCHITEKTONICZNE (arc42 2)

### 1.1. Fundamentalne Zasady

#### 1.1.1. Separation of Concerns (SoC)
**Definicja:** Każdy moduł ma jedną, wyraźnie zdefiniowaną odpowiedzialność.

**Realizacja:**
- Moduł SAST_Engine tylko SAST (nie SCA, nie Secrets)
- Moduł SCA_Engine tylko analiza komponentów
- Etc.

**Weryfikacja:**
- [ ] Każdy moduł ma jasny opis odpowiedzialności (1-2 zdania)
- [ ] Nie ma modułów typu "Utils" / "Common" / "Helpers"
- [ ] Граnice są egzekwowane przez testy architektoniczne

#### 1.1.2. Single Responsibility Principle (SRP)
**Definicja:** Moduł zmienia się tylko z jednego powodu.

**Realizacja:**
- Jeśli zmieniamy reguły SAST → zmienia się tylko SAST_Engine
- Jeśli zmieniamy format SBOM → zmienia się tylko SBOM_Generator

#### 1.1.3. Dependency Inversion Principle (DIP)
**Definicja:** Wysokopoziomowe moduły nie zależą od niskopoziomowych. Oba zależą od abstrakcji.

**Realizacja:**
```python
# Źle (AS-IS):
from security_analysis.sca_engine import SCAEngine  # konkretna implementacja

# Dobrze (TO-BE):
from interfaces import VulnerabilityScanner  # abstrakcja

class SCAEngine(VulnerabilityScanner):
    ...
```

**Weryfikacja:**
- [ ] Wszystkie zależności między modułami przez interfejsy
- [ ] Brak importów konkretnych implementacji z innych modułów
- [ ] Dependency Injection w użyciu

#### 1.1.4. Open/Closed Principle (OCP)
**Definicja:** Moduły otwarte na rozszerzenia, zamknięte na modyfikacje.

**Realizacja:**
- Plugin system dla nowych języków w Language_Adapters
- Strategy pattern dla różnych formatów SBOM

#### 1.1.5. Don't Repeat Yourself (DRY)
**Realizacja:**
- SHARED_RESOURCES dla wspólnych metadanych
- Brak duplikacji kodu między modułami
- **Target:** < 3% duplikacji (obecnie 15%)

#### 1.1.6. Principle of Least Surprise
**Realizacja:**
- Spójne nazewnictwo we wszystkich modułach
- Przewidywalne zachowanie API
- Jasne komunikaty błędów

### 1.2. Architectural Constraints

| Constraint | Powód | Impact |
|------------|-------|--------|
| **Język Python 3.11+** | Typing, performance | Wszystkie nowe moduły |
| **No circular dependencies** | Maintainability | Enforce w CI |
| **Max module size: 20 MB** | Manageable chunks | Design constraint |
| **Public API przez abstrakcje** | Loose coupling | Wszystkie interfejsy |
| **Semantic versioning** | Compatibility | Wszystkie moduły |
| **Test coverage > 80%** | Quality gate | CI blocker |

### 1.3. Wzorce Architektoniczne

**Clean Architecture (Robert C. Martin):**
```
┌──────────────────────────────────┐
│     Entities (Domain Models)     │
│                                  │
├──────────────────────────────────┤
│    Use Cases (Business Logic)    │
│                                  │
├──────────────────────────────────┤
│ Interface Adapters (Controllers) │
│                                  │
├──────────────────────────────────┤
│  Frameworks & Drivers (I/O)      │
└──────────────────────────────────┘
```

**Gdzie używamy:**
- SAST_Engine: Core logic vs Semgrep/CodeQL adapters
- SBOM_Generator: SBOM model vs CycloneDX/SPDX serializers

**Hexagonal Architecture (Ports & Adapters):**
```
        ┌─────────────┐
  Port  │             │  Port
◄───────┤  Core Logic ├───────►
        │             │
        └─────────────┘
             │
          Adapter
             ▼
       [External System]
```

**Gdzie używamy:**
- SCA_Engine: Port (VulnerabilityScanner), Adapters (OSV, NVD, npm audit)

**Repository Pattern:**
- Abstrakcja dostępu do danych (SBOM, Findings, Obligations)

### 1.4. Reguły Projektowe

#### Nazewnictwo

| Element | Konwencja | Przykład |
|---------|-----------|----------|
| **Moduły** | PascalCase_Suffix | `SAST_Engine`, `SBOM_Generator` |
| **Pliki Python** | snake_case | `sast_engine.py` |
| **Klasy** | PascalCase | `ScanResult`, `Finding` |
| **Funkcje** | snake_case | `scan_code()`, `get_findings()` |
| **Stałe** | UPPER_CASE | `MAX_FILE_SIZE`, `DEFAULT_TIMEOUT` |
| **Prywatne** | _underscore prefix | `_internal_method()` |
| **Interfejsy (abstrakcje)** | I prefix lub Protocol | `IScanner`, `ScannerProtocol` |

#### Struktura Katalogów (Standard)

```
ModuleName/
├── README.md                   # Główny opis
├── ARCHITECTURE.md             # Architektura modułu
├── API_REFERENCE.md            # Dokumentacja API
├── CHANGELOG.md                # Historia zmian
│
├── src/                        # Kod źródłowy
│   ├── __init__.py
│   ├── core/                   # Logika biznesowa (use cases)
│   │   ├── __init__.py
│   │   └── [domain_logic].py
│   ├── domain/                 # Modele domenowe (entities)
│   │   ├── __init__.py
│   │   └── [models].py
│   ├── interfaces/             # Abstrakcje (ports)
│   │   ├── __init__.py
│   │   └── [protocols].py
│   ├── adapters/               # Adaptery (do external systems)
│   │   ├── __init__.py
│   │   └── [adapters].py
│   ├── api/                    # Publiczne API modułu
│   │   ├── __init__.py
│   │   └── [public_api].py
│   └── utils/                  # Narzędzia pomocnicze
│       ├── __init__.py
│       └── [helpers].py
│
├── tests/                      # Testy
│   ├── __init__.py
│   ├── unit/                   # Testy jednostkowe
│   ├── integration/            # Testy integracyjne
│   ├── e2e/                    # Testy end-to-end
│   ├── fixtures/               # Dane testowe
│   └── conftest.py             # Pytest config
│
├── docs/                       # Dokumentacja dodatkowa
│   ├── decisions/              # ADR (Architecture Decision Records)
│   ├── diagrams/               # Diagramy (Mermaid, PlantUML)
│   └── guides/                 # Przewodniki
│
├── examples/                   # Przykłady użycia
│   └── [example_scripts].py
│
├── schemas/                    # Schematy danych
│   └── [json_schemas].json
│
├── config/                     # Konfiguracja
│   ├── default.yaml            # Domyślna config
│   └── [env_specific].yaml
│
├── pyproject.toml              # Python project config
├── requirements.txt            # Dependencies (lub poetry.lock)
└── .gitignore
```

#### Granice Modułów

**Reguła:** Moduł jest jednostką deploymentu i wersjonowania.

**Kryteria przynależności do modułu:**
1. **Cohesion:** Czy X i Y są używane razem? Jeśli tak, mogą być w tym samym module.
2. **Rate of change:** Czy X i Y zmieniają się z tych samych powodów? Jeśli tak, powinny być razem.
3. **Reusability:** Czy X jest używane przez wiele innych modułów? Jeśli tak, powinno być osobnym modułem.

**Przykład (SAST vs SCA):**
- Rate of change: Różne (SAST: nowe reguły, SCA: nowe źródła CVE)
- Reusability: Oba używane niezależnie
- **Decyzja:** Osobne moduły ✓

---

## 2. ARCHITEKTURA DOCELOWA (arc42 5)

### 2.1. Context Diagram (C4 Level 1)

```
External Systems:
┌────────────┐  ┌─────────────┐  ┌──────────────┐
│   GitHub   │  │  NPM/PyPI   │  │  OSV / NVD   │
│    API     │  │  Registries │  │  CVE APIs    │
└─────┬──────┘  └──────┬──────┘  └──────┬───────┘
      │                │                 │
      └────────────────┼─────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   AIUnifiedDesktop System    │
        │                              │
        │  26 modułów (Security, SBOM, │
        │  Analysis, Refactoring, etc.)│
        └──────────────────────────────┘
                       │
                       ▼
        ┌──────────────┴───────────────┐
        │                              │
   ┌────▼────┐              ┌─────────▼───┐
   │  Users  │              │   CI/CD     │
   │  (CLI)  │              │  Pipelines  │
   └─────────┘              └─────────────┘
```

### 2.2. Container Diagram (C4 Level 2)

```
┌─────────────────────────────────────────────────────────────┐
│                  AIUnifiedDesktop System                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐      ┌──────────────────────┐        │
│  │  CORE_ENGINES   │─────▶│ INTELLIGENCE_FEATURES│        │
│  ├─────────────────┤      ├──────────────────────┤        │
│  │ • SAST_Engine   │      │ • Impact_Flow        │        │
│  │ • SCA_Engine    │      │ • Impact_Planner     │        │
│  │ • Secrets_...   │      │ • FixOps             │        │
│  │ • SymbolGraph   │      │ • Core_Engine (Ref.) │        │
│  │ • SBOM_Gen.     │      │ • Language_Adapters  │        │
│  └─────────────────┘      └──────────────────────┘        │
│          │                            │                    │
│          └──────────┬─────────────────┘                    │
│                     ▼                                      │
│  ┌─────────────────────────────────────────────┐          │
│  │        PLATFORM_SERVICES                    │          │
│  ├─────────────────────────────────────────────┤          │
│  │ • Platform_Tools (validation, gates)        │          │
│  │ • Provenance_Service                        │          │
│  │ • Secrets_Broker                            │          │
│  │ • Arch_Fitness, Multirepo, Runtime_Feedback │          │
│  └─────────────────────────────────────────────┘          │
│                     │                                      │
│                     ▼                                      │
│  ┌─────────────────────────────────────────────┐          │
│  │        SHARED_RESOURCES                     │          │
│  ├─────────────────────────────────────────────┤          │
│  │ • metadata/ (common snapshots)              │          │
│  │ • schemas/ (JSON schemas)                   │          │
│  │ • examples/ (shared examples)               │          │
│  └─────────────────────────────────────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.3. Hierarchia Modułów Docelowa

```
AIUnifiedDesktop/
│
├── CORE_ENGINES/                        [5 modułów - fundamenty]
│   ├── SAST_Engine/                     [Split z Security_Analysis]
│   ├── SCA_Engine/                      [Split z Security_Analysis]
│   ├── Secrets_Scanner/                 [Split z Security_Analysis]
│   ├── SymbolGraph_Builder/             [Split z IR_SBOM_Impact]
│   └── SBOM_Generator/                  [Split z IR_SBOM_Impact]
│
├── INTELLIGENCE_FEATURES/               [5 modułów - analiza i inteligencja]
│   ├── Impact_Flow/                     [Split z IR_SBOM_Impact]
│   ├── Impact_Planner/                  [Split z Code_Refactoring]
│   ├── FixOps/                          [Split z Security_Analysis]
│   ├── Core_Engine/                     [Split z Code_Refactoring]
│   └── Language_Adapters/               [Split z Code_Refactoring]
│
├── ADVANCED_FEATURES/                   [3 moduły - bez zmian]
│   ├── Advanced_Testing/
│   ├── Attack_Surface/
│   └── Collaborative_Canvas/
│
├── SUPPORT_FEATURES/                    [2 moduły - bez zmian]
│   ├── Platform_Tools/
│   └── Diff_Viewer/                     [wrapper]
│
├── PLATFORM_SERVICES/                   [6 modułów]
│   ├── Provenance_Service/              [Split z Provenance_Secrets]
│   ├── Secrets_Broker/                  [Split z Provenance_Secrets]
│   ├── Arch_Fitness/                    [bez zmian]
│   ├── Multirepo_Orchestrator/          [bez zmian]
│   ├── Runtime_Feedback/                [bez zmian]
│   └── LLM_Auth_Providers/              [bez zmian]
│
├── INTEGRATION/                         [1 moduł - bez zmian]
│   └── CICD_Tooling/
│
└── SHARED_RESOURCES/                    [Nowy moduł]
    ├── metadata/                        [Przeniesione z Security_Analysis]
    ├── schemas/                         [Wspólne schematy JSON]
    └── examples/                        [Wspólne przykłady]
```

**Podsumowanie:**
- **Przed (AS-IS):** 14 modułów
- **Po (TO-BE):** 26 modułów + 1 SHARED = 27 jednostek
- **Nowych:** 12 (powstałe z podziału)
- **Bez zmian:** 11
- **Usunięte:** 4 (podzielone)

### 2.4. Lista Modułów Docelowych

| ID | Nazwa Modułu | Kategoria | Status | Pochodzenie | Rozmiar Szac. | Priorytet | Owner |
|----|--------------|-----------|--------|-------------|---------------|-----------|-------|
| **CORE_ENGINES** |||||||
| M01 | SAST_Engine | CORE | 🆕 Nowy | Split: Security_Analysis | ~12 MB | P0 | Security Team |
| M02 | SCA_Engine | CORE | 🆕 Nowy | Split: Security_Analysis | ~15 MB | P0 | Security Team |
| M03 | Secrets_Scanner | CORE | 🆕 Nowy | Split: Security_Analysis | ~8 MB | P0 | Security Team |
| M04 | SymbolGraph_Builder | CORE | 🆕 Nowy | Split: IR_SBOM_Impact | ~400 KB | P0 | Platform Team |
| M05 | SBOM_Generator | CORE | 🆕 Nowy | Split: IR_SBOM_Impact | ~500 KB | P0 | Platform Team |
| **INTELLIGENCE_FEATURES** |||||||
| M06 | Impact_Flow | INTEL | 🆕 Nowy | Split: IR_SBOM_Impact | ~500 KB | P1 | Platform Team |
| M07 | Impact_Planner | INTEL | 🆕 Nowy | Split: Code_Refactoring | ~1.2 MB | P1 | Dev Tools Team |
| M08 | FixOps | INTEL | 🆕 Nowy | Split: Security_Analysis | ~8 MB | P1 | Security Team |
| M09 | Core_Engine | INTEL | 🆕 Nowy | Split: Code_Refactoring | ~1.5 MB | P1 | Dev Tools Team |
| M10 | Language_Adapters | INTEL | 🆕 Nowy | Split: Code_Refactoring | ~1.9 MB | P1 | Dev Tools Team |
| **ADVANCED_FEATURES** |||||||
| M11 | Advanced_Testing | ADVANCED | ✅ Bez zmian | Istniejący | 1.2 MB | P2 | QA Team |
| M12 | Attack_Surface | ADVANCED | ✅ Bez zmian | Istniejący | 1.2 MB | P2 | Security Team |
| M13 | Collaborative_Canvas | ADVANCED | ✅ Bez zmian | Istniejący | 9.8 MB | P2 | Frontend Team |
| **SUPPORT_FEATURES** |||||||
| M14 | Platform_Tools | SUPPORT | ✅ Bez zmian | Istniejący | 996 KB | P2 | Platform Team |
| M15 | Diff_Viewer | SUPPORT | ✅ Bez zmian | Wrapper | 8 KB | P3 | Platform Team |
| **PLATFORM_SERVICES** |||||||
| M16 | Provenance_Service | PLATFORM | 🆕 Nowy | Split: Provenance_Secrets | ~2.5 MB | P1 | Security Team |
| M17 | Secrets_Broker | PLATFORM | 🆕 Nowy | Split: Provenance_Secrets | ~1.7 MB | P1 | Security Team |
| M18 | Arch_Fitness | PLATFORM | ✅ Bez zmian | Istniejący | 864 KB | P2 | Arch Team |
| M19 | Multirepo_Orchestrator | PLATFORM | ✅ Bez zmian | Istniejący | 948 KB | P2 | DevOps Team |
| M20 | Runtime_Feedback | PLATFORM | ✅ Bez zmian | Istniejący | 848 KB | P2 | QA Team |
| M21 | LLM_Auth_Providers | PLATFORM | ✅ Bez zmian | Istniejący | 212 KB | P2 | Integration Team |
| **INTEGRATION** |||||||
| M22 | CICD_Tooling | INTEGRATION | ✅ Bez zmian | Istniejący | 288 KB | P2 | DevOps Team |
| **SHARED** |||||||
| M23 | SHARED_RESOURCES | SHARED | 🆕 Nowy | Extracted | ~5 MB | P0 | Arch Team |

---

## 3. SZCZEGÓŁY MODUŁÓW DOCELOWYCH (arc42 5.2)

> Pełny opis każdego z 26 modułów. Format dla każdego:

### 3.1. [SAST_Engine]

**Podstawowe Informacje:**
- **ID:** M01
- **Kategoria:** CORE_ENGINES
- **Status:** 🆕 Nowy (split z Security_Analysis)
- **Rozmiar szacunkowy:** ~12 MB
- **Języki:** Python 95%, YAML 5%
- **Właściciel:** Security Team
- **Priorytet:** P0

**Odpowiedzialność (Single Responsibility):**
Statyczna analiza bezpieczeństwa kodu źródłowego (SAST). Wykrywanie luk typu SQL injection, XSS, hardcoded secrets (via patterns), command injection, path traversal, insecure crypto.

**Granice (Scope):**

**W zakresie:**
- Parsowanie kodu źródłowego (AST/pattern matching)
- Wykonywanie reguł SAST (Semgrep, CodeQL, ESLint, Ruff)
- Generowanie findings (lokalizacja, severity, message)
- Mapowanie findings do SARIF format

**Poza zakresem:**
- ❌ Analiza zależności (SCA) → to robi SCA_Engine
- ❌ Runtime secrets scanning → to robi Secrets_Scanner
- ❌ Fix proposals → to robi FixOps
- ❌ Reachability analysis → używa SymbolGraph_Builder (dependency)

**Struktura Katalogów:**
```
SAST_Engine/
├── README.md
├── ARCHITECTURE.md
├── API_REFERENCE.md
├── CHANGELOG.md
│
├── src/
│   ├── core/
│   │   ├── scanner.py          # Core SAST logic
│   │   ├── rule_engine.py      # Rule execution
│   │   └── findings.py         # Finding models
│   ├── domain/
│   │   ├── models.py           # ScanResult, Finding, Rule
│   │   └── enums.py            # Severity, RuleType
│   ├── interfaces/
│   │   └── scanner_protocol.py # ISASTScanner Protocol
│   ├── adapters/
│   │   ├── semgrep.py          # Semgrep adapter
│   │   ├── codeql.py           # CodeQL adapter
│   │   ├── eslint.py           # ESLint adapter
│   │   └── ruff.py             # Ruff adapter
│   ├── api/
│   │   └── __init__.py         # Public API
│   └── utils/
│       ├── sarif.py            # SARIF serializer
│       └── ast_helpers.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
├── config/
│   ├── default_rules.yaml
│   └── semgrep_rulesets.yaml
│
├── schemas/
│   └── finding.schema.json
│
└── pyproject.toml
```

**Interfejsy Publiczne (API Contract):**

```python
# src/interfaces/scanner_protocol.py
from typing import Protocol, List
from pathlib import Path
from .models import ScanResult, ScanConfig

class ISASTScanner(Protocol):
    """Interfejs dla SAST scannerów."""
    
    def scan(self, source_path: Path, config: ScanConfig) -> ScanResult:
        """Wykonaj skan SAST."""
        ...
    
    def get_supported_languages(self) -> List[str]:
        """Zwróć listę wspieranych języków."""
        ...


# src/api/__init__.py (Public API)
from ..core.scanner import SASTScanner
from ..domain.models import ScanResult, Finding, ScanConfig
from ..domain.enums import Severity, RuleType

__all__ = [
    "SASTScanner",
    "ScanResult",
    "Finding",
    "ScanConfig",
    "Severity",
    "RuleType",
]

# Użycie:
from sast_engine import SASTScanner, ScanConfig

scanner = SASTScanner()
result = scanner.scan(Path("./src"), ScanConfig(rules=["sql-injection"]))
```

**Zależności:**

**Upstream (od czego zależy):**
- **Brak zależności od innych modułów** (moduł leaf w grafie)
- **External:**
  - `semgrep >= 1.50.0` (FIXED CVE-2024-XXXXX)
  - `tree-sitter` dla parsowania (jeśli custom rules)
  
**Downstream (co od niego zależy):**
- `FixOps` - używa findings do generowania napraw
- `Platform_Tools` (gates) - sprawdza findings vs policy
- `CICD_Tooling` - uruchamia scany w pipeline

**Konfiguracja:**
```yaml
# config/default_rules.yaml
rulesets:
  semgrep:
    - p/security-audit
    - p/owasp-top-10
  
  custom_rules:
    - rules/sql-injection.yaml
    - rules/xss.yaml

severity_overrides:
  - rule_id: "hardcoded-password"
    from: "HIGH"
    to: "CRITICAL"

timeout: 60  # seconds per scan
max_findings: 1000
```

**Performance SLA:**
- **Scan time:** < 60s dla 1000 plików
- **Memory:** < 512 MB
- **CPU:** < 400% (multi-core)

**Metryki Sukcesu:**
- [ ] Test coverage > 85%
- [ ] False positive rate < 5%
- [ ] Recall (wykrywalność) > 95% dla OWASP Top 10
- [ ] Zero critical CVE dependencies
- [ ] Documentation coverage 100%

**Migration Path (z Security_Analysis):**
1. Wydzielenie `sast/` → `SAST_Engine/src/`
2. Refactoring do Clean Architecture (core/adapters)
3. Definicja public API
4. Testy regresji (compare results AS-IS vs TO-BE)
5. Deprecation notice w Security_Analysis
6. Usunięcie starego kodu

[Powtórz format dla pozostałych 25 modułów]

---

## 4. ZALEŻNOŚCI MIĘDZY MODUŁAMI (arc42 3.2)

### 4.1. Graf Zależności Docelowy

```
Legend:
  A ──▶ B  : A depends on B (uses B's API)
  [P]      : Protocol/Interface based dependency

Layer 1 (Foundation - no dependencies):
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ SymbolGraph      │  │ SAST_Engine      │  │ Secrets_Scanner  │
│ _Builder         │  │                  │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘

Layer 2 (depends on Layer 1):
┌──────────────────┐  ┌──────────────────┐
│ SBOM_Generator   │  │ Language         │
│        │         │  │ _Adapters        │
│        ▼ [P]     │  │                  │
│  SymbolGraph     │  │                  │
└──────────────────┘  └──────────────────┘

┌──────────────────┐
│ Impact_Flow      │
│        │         │
│        ▼ [P]     │
│  SymbolGraph     │
└──────────────────┘

Layer 3 (intelligence):
┌──────────────────┐  ┌──────────────────┐
│ SCA_Engine       │  │ Core_Engine      │
│        │         │  │     (Refactor)   │
│        ▼ [P]     │  │        │         │
│  SBOM_Generator  │  │        ▼ [P]     │
└──────────────────┘  │  Language_Adapt. │
                      └──────────────────┘

┌──────────────────┐
│ Impact_Planner   │
│        │         │
│        ▼ [P]     │
│  Impact_Flow     │
└──────────────────┘

Layer 4 (operations):
┌──────────────────┐
│ FixOps           │
│        │         │
│        ├─ [P] ──▶ SAST_Engine
│        ├─ [P] ──▶ SCA_Engine
│        └─ [P] ──▶ Secrets_Scanner
└──────────────────┘

Platform Services (use everything):
┌──────────────────────────────────────┐
│ Platform_Tools, CICD_Tooling, etc.   │
│  (używają modułów powyżej via API)   │
└──────────────────────────────────────┘

SHARED_RESOURCES:
└──▶ All modules (read-only access)
```

### 4.2. Macierz Zależności

**Legenda:** 
- ✓ = Direct dependency (przez interface)
- ✗ = No dependency
- ⚠️ = Should not depend (architectural violation if present)

|ID| M01 | M02 | M03 | M04 | M05 | M06 | M07 | M08 | M09 | M10 | ... |
|--|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **M01 SAST_Engine** | - | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ⚠️ | ✗ | ✗ | ... |
| **M02 SCA_Engine** | ✗ | - | ✗ | ✗ | ✓ | ✗ | ✗ | ⚠️ | ✗ | ✗ | ... |
| **M03 Secrets_Scanner** | ✗ | ✗ | - | ✗ | ✗ | ✗ | ✗ | ⚠️ | ✗ | ✗ | ... |
| **M04 SymbolGraph_Builder** | ✗ | ✗ | ✗ | - | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ... |
| **M05 SBOM_Generator** | ✗ | ✗ | ✗ | ✓ | - | ✗ | ✗ | ✗ | ✗ | ✗ | ... |
| **M06 Impact_Flow** | ✗ | ✗ | ✗ | ✓ | ✗ | - | ✗ | ✗ | ✗ | ✗ | ... |
| **M07 Impact_Planner** | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | - | ✗ | ✗ | ✗ | ... |
| **M08 FixOps** | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | - | ✗ | ✗ | ... |
| **M09 Core_Engine** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | - | ✓ | ... |
| **M10 Language_Adapters** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ⚠️ | - | ... |

**Metry stability:**
| Moduł | Afferent (Ca) | Efferent (Ce) | Instability (I) | Target Zone |
|-------|---------------|---------------|-----------------|-------------|
| SymbolGraph_Builder | 3 | 0 | 0.00 | ✓ Stable foundation |
| SAST_Engine | 1 | 0 | 0.00 | ✓ Stable |
| SCA_Engine | 1 | 1 | 0.50 | ✓ Balanced |
| FixOps | 2 | 3 | 0.60 | ✓ Higher-level |
| Core_Engine | 1 | 2 | 0.67 | ✓ Higher-level |

**I = Ce / (Ca + Ce)**  
**Target:** Foundation modules (I < 0.3), Intelligence (I 0.3-0.7)

### 4.3. Reguły Zależności

**Architectural Rules (egzekwowane w CI):**

1. **Zakaz cyklicznych zależności**
   ```python
   # Test:
   def test_no_circular_dependencies():
       graph = build_dependency_graph()
       assert graph.is_acyclic()
   ```

2. **Dependency Inversion**
   - Wszystkie zależności między modułami przez `interfaces/`
   - Brak importów konkretnych implementacji

3. **Layered Architecture**
   ```
   Higher layers MAY depend on lower layers
   Lower layers MUST NOT depend on higher layers
   
   Layer 4 (Operations)    ──▶
   Layer 3 (Intelligence)  ──▶
   Layer 2 (Builders)      ──▶
   Layer 1 (Foundation)
   ```

4. **Maksymalna głębokość zależności:** 3 poziomy
   - Przykład OK: FixOps → SCA_Engine → SBOM_Generator → SymbolGraph
   - Przykład BAD: 5+ poziomów (code smell)

5. **Stabilność vs Abstrakcja (Martin's Main Sequence)**
   ```
   A (Abstractness) = abstract_classes / total_classes
   I (Instability) = Ce / (Ca + Ce)
   
   Distance from Main Sequence: D = |A + I - 1|
   Target: D < 0.2
   ```

### 4.4. Interfejsy Między Modułami

#### SCA_Engine → SBOM_Generator

**Contract (Interface):**
```python
# shared_resources/interfaces/sbom_provider.py
from typing import Protocol
from pathlib import Path

class ISBOMProvider(Protocol):
    """Interfejs dostarczyciela SBOM."""
    
    def generate_sbom(
        self,
        source_path: Path,
        format: str = "cyclonedx"
    ) -> dict:
        """Generate SBOM from source.
        
        Args:
            source_path: Path to source code
            format: "cyclonedx" or "spdx"
            
        Returns:
            SBOM as dict (per spec)
        """
        ...
```

**Implementacja (SBOM_Generator):**
```python
# SBOM_Generator/src/api/__init__.py
from ..core.generator import SBOMGenerator as _Generator

class SBOMGenerator:
    """Public API implementing ISBOMProvider."""
    
    def generate_sbom(self, source_path, format="cyclonedx"):
        # Implementation
        ...
```

**Użycie (SCA_Engine):**
```python
# SCA_Engine/src/core/scanner.py
from interfaces import ISBOMProvider  # from shared

class SCAScanner:
    def __init__(self, sbom_provider: ISBOMProvider):
        self._sbom = sbom_provider  # Dependency Injection
    
    def scan(self, source_path):
        sbom = self._sbom.generate_sbom(source_path)
        # Analyze SBOM for vulnerabilities
        ...
```

**Wersjonowanie:**
- **Semantic Versioning:** MAJOR.MINOR.PATCH
- **Breaking change:** MAJOR bump
  - Zmiana sygnatur metod
  - Usunięcie pól z response
- **Non-breaking:** MINOR bump
  - Dodanie nowych pól (z defaults)
  - Nowe opcjonalne parametry
- **Bug fixes:** PATCH bump

**Zgodność wsteczna:**
- Minimum 2 wersje MAJOR wspierane równolegle
- Deprecation warnings 1 wersja wcześniej

[Powtórzyć dla każdego kluczowego interfejsu]

---

## 5. WSPÓLNE ZASOBY (SHARED_RESOURCES)

### 5.1. Cel i Uzasadnienie

**Problem w AS-IS:**
- Security_Analysis ma duplikacje `metadata/normalized/*` (~8 MB!)
- Każdy moduł duplikuje przykłady, schematy
- Brak single source of truth

**Rozwiązanie TO-BE:**
- Dedykowany moduł SHARED_RESOURCES
- Read-only dla innych modułów
- Wersjonowany niezależnie

### 5.2. Zawartość

```
SHARED_RESOURCES/
├── README.md
├── CHANGELOG.md
│
├── metadata/                   # Wspólne metadane (Phase snapshots)
│   ├── phases/
│   │   ├── phase_01/          # IR + SBOM + Impact
│   │   ├── phase_02/          # Validation
│   │   └── ...
│   └── normalized/            # Normalized metadata (extracted)
│
├── schemas/                    # Wspólne JSON schemas
│   ├── finding.schema.json    # Finding (SAST, SCA, Secrets)
│   ├── sbom.schema.json       # SBOM schema
│   ├── symbol_graph.schema.json
│   ├── impact_graph.schema.json
│   └── sarif.schema.json      # SARIF 2.1.0
│
├── examples/                   # Wspólne przykłady
│   ├── findings/
│   │   ├── sast_example.json
│   │   ├── sca_example.ndjson
│   │   └── secrets_example.json
│   ├── sboms/
│   │   ├── cyclonedx_npm.json
│   │   ├── cyclonedx_pip.json
│   │   └── spdx_go.json
│   └── graphs/
│       ├── symbol_graph_example.json
│       └── impact_graph_example.json
│
├── interfaces/                 # Wspólne interfejsy (Protocols)
│   ├── __init__.py
│   ├── scanner_protocol.py    # ISASTScanner, ISCAScanner, etc.
│   ├── sbom_provider.py       # ISBOMProvider
│   └── graph_builder.py       # ISymbolGraphBuilder
│
└── utils/                      # Wspólne utilities (używane rzadko!)
    ├── __init__.py
    └── validation.py          # Schema validation helpers
```

### 5.3. Zasady Użycia

**Access Policy:**
1. **Read-only** dla wszystkich modułów
2. **Zmian dokonuje:** Dedykowany maintainer (Arch Team)
3. **Proces zmian:**
   - Pull Request
   - Review przez 2+ arch team members
   - Impact analysis (jakie moduły dotknięte)
   - Versioning: semantic versioning

**Import Guidelines:**
```python
# ✓ Poprawnie:
from shared_resources.schemas import load_schema
from shared_resources.interfaces import ISASTScanner

# ✗ Źle (bezpośredni import plików):
import shared_resources.metadata.phases.phase_01.data
```

**Versioning:**
- SHARED_RESOURCES ma własne wersje (v1.0.0, v1.1.0, etc.)
- Breaking changes w schemas → MAJOR bump
- Moduły specyfikują wymaganą wersję:
  ```toml
  [dependencies]
  shared-resources = "^1.0.0"  # Compatible with 1.x.x
  ```

---

## 6. DANE I PRZECHOWYWANIE (arc42 5.3)

### 6.1. Strategia Danych

#### Własność Danych (Data Ownership)

**Zasada:** Każdy moduł jest właścicielem swoich danych.

| Typ Danych | Właściciel | Format | Storage | Dostęp z innych modułów |
|------------|------------|--------|---------|------------------------|
| SAST Findings | SAST_Engine | NDJSON | `sast_findings.ndjson` | Via API only |
| SCA Findings | SCA_Engine | NDJSON | `sca_findings.ndjson` | Via API only |
| SBOM | SBOM_Generator | CycloneDX JSON | `sbom.json` | Via API only |
| Symbol Graph | SymbolGraph_Builder | JSON | `symbol_graph.json` | Via API only |
| Impact Graph | Impact_Flow | JSON | `impact_graph.json` | Via API only |
| Obligations | Platform_Tools | SQLite/Postgres | `obligations.db` | Via API only |
| Secrets Leases | Secrets_Broker | Encrypted JSON | `leases/*.enc.json` | Via API only |
| Attestations | Provenance_Service | JSON | `attestations/*.json` | Via API only |

**Zakaz:** Bezpośredni dostęp do plików/bazy danych innego modułu!

```python
# ✗ Źle:
import json
with open("../sca_engine/sca_findings.ndjson") as f:
    findings = [json.loads(line) for line in f]

# ✓ Dobrze:
from sca_engine import SCAEngine
scanner = SCAEngine()
findings = scanner.get_findings()
```

#### Współdzielenie Danych

**Mechanizm:** Publish-Subscribe (Event-driven)

```python
# Module A (publisher):
from events import EventBus

bus = EventBus()
bus.publish("sast.scan.completed", ScanCompletedEvent(findings=results))

# Module B (subscriber):
bus.subscribe("sast.scan.completed", on_sast_completed)

def on_sast_completed(event):
    findings = event.findings
    # Process findings
```

**Alternatywa:** Shared read-only artifacts

```python
# SAST_Engine zapisuje wyniki do standardowej lokalizacji:
# artifacts/sast/findings.ndjson

# FixOps czyta z tej lokalizacji (read-only):
findings = read_ndjson("artifacts/sast/findings.ndjson")
```

### 6.2. Database Strategy

**Development:** SQLite  
**Production:** PostgreSQL 15+

**Schema per module:**
```sql
-- Platform_Tools/obligations
CREATE TABLE obligations (
    id UUID PRIMARY KEY,
    type VARCHAR(50),
    description TEXT,
    source VARCHAR(100),
    status VARCHAR(20),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Secrets_Broker/leases
CREATE TABLE secret_leases (
    id UUID PRIMARY KEY,
    secret_id VARCHAR(100),
    expires_at TIMESTAMP,
    scope JSONB,
    status VARCHAR(20)
);
```

**Migration Strategy:**
- Alembic (Python) lub Flyway dla migracji
- Per-module migration scripts
- Coordinated deployment

---

## 7. BEZPIECZEŃSTWO (arc42 11.3)

### 7.1. Security by Design Principles

**Zasady:**
1. **Least Privilege:** Każdy moduł ma minimalne uprawnienia
2. **Defense in Depth:** Wiele warstw ochrony
3. **Fail Secure:** Błędy nie kompromitują bezpieczeństwa
4. **Privacy by Design:** PII nie trafia do logów/metrics
5. **Zero Trust:** Walidacja na każdej granicy modułu

### 7.2. Kontrole Bezpieczeństwa (Target)

| Kontrola | Implementacja | Moduły | Target Status |
|----------|---------------|--------|---------------|
| **Autentykacja** | OAuth 2.0 + PKCE (S256) | LLM_Auth_Providers | ✓ Już jest |
| **Autoryzacja** | RBAC (Role-Based Access Control) | Platform_Tools | 🆕 Do implementacji |
| **Walidacja wejścia** | Pydantic schemas + size limits | Wszystkie | ✓ Ustandaryzowane |
| **Sanityzacja output** | PII removal, secret redaction | Wszystkie | 🆕 Do implementacji |
| **Encryption at rest** | AES-256-GCM | Secrets_Broker | ✓ Już jest |
| **Encryption in transit** | TLS 1.3, cert pinning | API/WebSocket | ✓ Już jest |
| **Secrets management** | Leases, rotation, scopes | Secrets_Broker | ✓ Już jest |
| **Audit logging** | Structured logs (JSON), NDJSON events | Platform_Tools | ✓ Już jest |
| **Rate limiting** | Token bucket per endpoint | API Gateway | 🆕 Do implementacji |
| **Input size limits** | Standardized limits | Wszystkie | 🆕 Do implementacji |
| **CSRF protection** | CSRF tokens dla mutations | WebSocket/API | 🆕 Do implementacji |
| **Content Security Policy** | CSP headers | Collaborative_Canvas | 🆕 Do implementacji |

### 7.3. RBAC Model (Nowy)

**Roles:**
- `admin` - Full access
- `security_analyst` - SAST/SCA/Secrets + FixOps
- `developer` - Code_Refactoring, Impact_Planner
- `auditor` - Read-only access do findings, obligations
- `ci_bot` - Automated scans

**Permissions:**
```yaml
roles:
  security_analyst:
    permissions:
      - sast:scan
      - sast:read_findings
      - sca:scan
      - sca:read_findings
      - secrets:scan
      - fixops:propose
    deny:
      - obligations:waive  # Only admin
```

**Implementation:**
```python
from rbac import require_permission

@require_permission("sast:scan")
def scan_code(user, source_path):
    # Only users with sast:scan permission can call this
    ...
```

### 7.4. Secrets Management (Enhanced)

**Hierarchy:**
```
Secrets_Broker (master)
    │
    ├─ Leases (ephemeral, TTL)
    │  └─ Per-request tokens (15 min TTL)
    │
    ├─ Rotation (automatic)
    │  └─ Every 30 days (configurable)
    │
    └─ Audit Trail
       └─ Who accessed what, when
```

**API:**
```python
from secrets_broker import SecretsClient

client = SecretsClient()

# Request lease
lease = client.request_lease(
    secret_id="github_token",
    scope={"repo": "myorg/myrepo"},
    ttl=900  # 15 minutes
)

# Use secret
response = github_api.call(token=lease.secret_value)

# Auto-revoke after TTL or explicit:
client.revoke_lease(lease.id)
```

### 7.5. CVE Management (Target: 0 Critical)

**Proces:**
1. **Continuous Scanning:** Dependency check w CI (każdy PR)
2. **Alerting:** Critical CVE → PagerDuty → < 4h response
3. **Patching SLA:**
   - Critical: < 24h
   - High: < 7 dni
   - Medium: < 30 dni
4. **Reachability Analysis:** Priorytetyzacja po sprawdzeniu czy CVE jest w użyciu
5. **Automated PRs:** Dependabot/Renovate dla patch versions

---

## 8. WYDAJNOŚĆ I SKALOWALNOŚĆ (arc42 11.2)

### 8.1. Performance Targets (SLA)

| Operacja | Current | Target | Improvement |
|----------|---------|--------|-------------|
| SAST scan (1000 files) | 45s avg, 58s p95 | < 30s avg, < 40s p95 | -33% |
| SCA scan | 8s avg | < 5s avg | -37% |
| Symbol graph build | 22s avg, 35s p95 | < 15s avg, < 25s p95 | -32% |
| SBOM generation | 5s | < 3s | -40% |
| Refactoring (rename) | 3s | < 2s | -33% |
| Canvas sync (50 users) | 50ms avg, 120ms p95 | < 50ms avg, < 80ms p95 | p95 -33% |

### 8.2. Optimization Strategies

**1. Caching:**
```python
# SAST_Engine
from cachetools import TTLCache

# Cache parsed ASTs (1h TTL)
ast_cache = TTLCache(maxsize=1000, ttl=3600)

def scan_file(file_path):
    if file_path in ast_cache:
        ast = ast_cache[file_path]
    else:
        ast = parse_ast(file_path)
        ast_cache[file_path] = ast
    # Scan AST
    ...
```

**2. Parallelization:**
```python
# SymbolGraph_Builder
from concurrent.futures import ProcessPoolExecutor

def build_graph(source_paths):
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        symbol_graphs = executor.map(build_file_graph, source_paths)
    return merge_graphs(symbol_graphs)
```

**3. Incremental Processing:**
```python
# Impact_Flow - tylko zmienione pliki
def analyze_impact(changes: ChangeSet, prev_graph: SymbolGraph):
    affected_files = changes.modified_files
    # Re-analyze tylko affected files, nie cały projekt
    subgraph = rebuild_subgraph(affected_files)
    return merge_with_previous(prev_graph, subgraph)
```

**4. Lazy Loading:**
```python
# SBOM_Generator - load components on-demand
class SBOM:
    def __init__(self, path):
        self._path = path
        self._components = None  # Not loaded yet
    
    @property
    def components(self):
        if self._components is None:
            self._components = self._load_components()
        return self._components
```

### 8.3. Scalability Architecture

**Horizontal Scaling (gdzie możliwe):**
- SAST_Engine: Sharding po katalogach
- SCA_Engine: Parallel scans per package manager
- Canvas sync: Multiple WebSocket servers (load balanced)

**Resource Limits:**
```yaml
# per-module limits
limits:
  sast_engine:
    max_file_size: 10MB
    max_files_per_scan: 5000
    memory_limit: 1GB
    cpu_limit: 4 cores
  
  symbol_graph_builder:
    max_symbols: 100000
    memory_limit: 2GB
```

---

## 9. OBSERVABILITY (arc42 11.4)

### 9.1. Logging (Standard for All Modules)

**Format:** Structured JSON

**Levels:** DEBUG, INFO, WARN, ERROR, CRITICAL

**Standard fields:**
```json
{
  "timestamp": "2025-11-09T10:15:30.123Z",
  "level": "INFO",
  "module": "sast_engine",
  "component": "scanner",
  "message": "Scan completed successfully",
  "context": {
    "scan_id": "uuid",
    "file_count": 1234,
    "duration_ms": 42000
  },
  "trace_id": "uuid",  # For distributed tracing
  "user_id": "hashed"  # NO PII!
}
```

**Sanitization (automatic):**
- PII removal: paths, emails, names
- Secret redaction: API keys, tokens
- Size limits: messages < 1KB

**Implementation:**
```python
import structlog

logger = structlog.get_logger()

logger.info(
    "scan_completed",
    scan_id=scan_id,
    file_count=len(files),
    duration_ms=duration
)
```

### 9.2. Metrics (Prometheus)

**Per-module metrics:**
```
# Request rate
<module>_requests_total{method="scan", status="success"}

# Latency
<module>_request_duration_seconds{method="scan", quantile="0.5|0.95|0.99"}

# Errors
<module>_errors_total{type="timeout|validation|internal"}

# Resource usage
<module>_memory_bytes
<module>_cpu_seconds_total

# Business metrics
sast_findings_total{severity="critical|high|medium|low"}
sca_vulnerabilities_total{severity="critical|high"}
```

**Dashboards (Grafana):**
- Overview: All modules health
- Per-module: Deep dive into specific module
- SLO tracking: SLA compliance

### 9.3. Distributed Tracing (OpenTelemetry)

**Trace propagation:**
```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("sast_scan") as span:
    span.set_attribute("file_count", len(files))
    
    # Nested span
    with tracer.start_as_current_span("parse_ast"):
        ast = parse(files)
    
    # Propagate to downstream service
    result = sca_client.scan(sbom, trace_context=span.get_span_context())
```

**Visualization:** Jaeger / Zipkin

### 9.4. Alerting (Prometheus Alertmanager)

**Alert Rules:**
```yaml
groups:
  - name: sast_engine
    rules:
      - alert: HighErrorRate
        expr: rate(sast_engine_errors_total[5m]) > 0.05
        for: 5m
        annotations:
          summary: "SAST Engine error rate > 5%"
          
      - alert: SlowScans
        expr: histogram_quantile(0.95, sast_engine_request_duration_seconds) > 60
        for: 10m
        annotations:
          summary: "SAST p95 latency > 60s (SLA breach)"
```

**Notification:** PagerDuty, Slack, Email

---

## 10. DEVOPS I CI/CD (arc42 9.1)

### 10.1. Pipeline Docelowy

```
[Git Push]
    ↓
[Determine Changed Modules] (monorepo detection)
    ↓
[Per-Module Pipelines] (parallel)
    ├─ Module A: Build → Test → Security Scan
    ├─ Module B: Build → Test → Security Scan
    └─ Module C: Build → Test → Security Scan
    ↓
[Integration Tests] (cross-module)
    ↓
[Build Artifacts] (per module)
    ↓
[Deploy to Staging] (automatic)
    ↓
[Smoke Tests]
    ↓
[Manual Approval] (for production)
    ↓
[Deploy to Production] (Canary: 10% → 50% → 100%)
    ↓
[Monitor] (automatic rollback if errors > threshold)
```

**Total time target:** < 15 min (currently 20 min)

### 10.2. Per-Module Versioning

**Semantic Versioning:**
```
v1.2.3
│ │ └─ PATCH: Bug fixes, no API changes
│ └─── MINOR: New features, backward compatible
└───── MAJOR: Breaking changes
```

**Release Process:**
1. PR merged → auto-increment PATCH
2. Feature complete → MINOR bump (manual)
3. Breaking API change → MAJOR bump (manual + migration guide)

**Changelog automation:**
```bash
# Auto-generate from git commits (conventional commits)
git log --oneline --no-merges v1.2.0..HEAD
```

### 10.3. Deployment Strategy

**Per Module Type:**

| Module Type | Strategy | Reason |
|-------------|----------|--------|
| **Core Engines** | Blue-Green | Zero downtime, instant rollback |
| **Intelligence** | Rolling | Gradual, lower risk |
| **Platform Services** | Canary | Monitor impact on all users |
| **CICD Tooling** | Recreate | Low traffic, maintenance window OK |

**Canary Example:**
```yaml
deployment:
  strategy: canary
  steps:
    - weight: 10%    # 10% traffic
      pause: 10m     # Monitor for 10 min
    - weight: 50%
      pause: 10m
    - weight: 100%
  
  auto_rollback:
    enabled: true
    conditions:
      - error_rate > 5%
      - p95_latency > SLA * 1.2
```

---

## 11. TESTOWANIE (arc42 9.2)

### 11.1. Test Strategy (Target)

| Level | Coverage Target | Responsibility | Frequency |
|-------|-----------------|----------------|-----------|
| **Unit** | > 85% | Deweloper | Per commit |
| **Integration** | > 75% | Deweloper + QA | Per PR |
| **Contract** | 100% interfaces | Deweloper | Per PR |
| **E2E** | > 60% critical paths | QA | Daily + Pre-release |
| **Performance** | Regression < 10% | QA | Weekly |
| **Security** | 100% scan | Security + CI | Per commit |
| **Chaos** | N/A | SRE | Monthly |

### 11.2. Contract Testing (Nowy)

**Cel:** Zapewnić zgodność między consumer i provider.

**Example (Pact):**
```python
# Consumer (SCA_Engine) test:
from pact import Consumer, Provider

pact = Consumer("SCA_Engine").has_pact_with(Provider("SBOM_Generator"))

(pact
  .given("valid source path")
  .upon_receiving("a request for SBOM")
  .with_request(method="POST", path="/generate", body={...})
  .will_respond_with(status=200, body={...}))

# This generates a pact file

# Provider (SBOM_Generator) verifies:
pact_verifier.verify_pacts(
    "SCA_Engine",
    "SBOM_Generator",
    pact_files=["pacts/sca_engine-sbom_generator.json"]
)
```

### 11.3. Architectural Tests

**Przykłady (ArchUnit dla Python):**
```python
from archunit import assert_that, classes_that

# Test 1: No circular dependencies
assert_that(all_modules()).have_no_circular_dependencies()

# Test 2: Core modules don't depend on higher layers
assert_that(
    classes_that()
    .reside_in_a_package("core_engines..")
).should_only_depend_on_packages_matching(
    "core_engines..",
    "shared_resources..",
    "stdlib"
)

# Test 3: All API calls через interfaces
assert_that(
    classes_that().are_not_interfaces()
).should_only_depend_on_classes_that_are_interfaces()
.when_calling_other_modules()
```

---

## 12. DOKUMENTACJA (arc42 12)

### 12.1. Standardy Dokumentacji

**Poziomy:**
1. **System-level:** Ten dokument (TO-BE)
2. **Module-level:** README, ARCHITECTURE per module
3. **Code-level:** Docstrings, comments

**Required per module:**
- [x] README.md (quick start)
- [x] ARCHITECTURE.md (internal design)
- [x] API_REFERENCE.md (public API)
- [x] CHANGELOG.md (history)
- [x] MIGRATION.md (if breaking changes from AS-IS)

**Quality Gates:**
- [ ] 100% public API documented
- [ ] All modules have README
- [ ] Architecture diagrams present

---

## 13. MIGRATION PATH (Roadmap)

### 13.1. Fazy Transformacji

#### Faza 0: Przygotowanie (Week 1-2)
**Cel:** Groundwork dla transformacji

- [ ] Patch critical CVEs (S-001, S-002)
- [ ] Utworzenie SHARED_RESOURCES skeleton
- [ ] Definicja wszystkich interfejsów (ISASTScanner, ISBOMProvider, etc.)
- [ ] Setup observability stack (Prometheus, Jaeger)
- [ ] CI/CD adjustments (per-module pipelines)

**Deliverables:**
- Interfaces package
- SHARED_RESOURCES v0.1.0
- Updated CI/CD configs

#### Faza 1: Podział Security_Analysis (Week 3-5)
**Cel:** 1 moduł → 4 moduły

**Tasks:**
1. Extraction SAST_Engine
   - [ ] Copy `sast/` → `SAST_Engine/src/`
   - [ ] Refactor to Clean Architecture
   - [ ] Define public API (implements ISASTScanner)
   - [ ] Tests (regression: compare results)
   - [ ] Documentation
   
2. Extraction SCA_Engine
   - [ ] Copy `sca/` → `SCA_Engine/src/`
   - [ ] Implement ISCAScanner
   - [ ] Integration with SBOM_Generator (via interface)
   - [ ] Tests, docs
   
3. Extraction Secrets_Scanner
   - [ ] Copy `secrets/` → `Secrets_Scanner/src/`
   - [ ] Tests, docs
   
4. Extraction FixOps
   - [ ] Copy `fixes/`, `reachability/`, `ranked/` → `FixOps/src/`
   - [ ] Implement aggregation logic (combines SAST + SCA + Secrets)
   - [ ] Tests, docs

5. Deprecation Security_Analysis
   - [ ] Deprecation notice w README
   - [ ] Wrapper forwarding calls to new modules
   - [ ] Update consumers (Platform_Tools, CICD)

**Rollback Plan:**
- Keep old Security_Analysis for 1 release cycle
- Feature flag to switch between old/new

#### Faza 2: Podział Code_Refactoring (Week 6-7)
**Cel:** 1 moduł → 3 moduły

[Analogiczny proces]

#### Faza 3: Podział Provenance_Secrets (Week 8)
**Cel:** 1 moduł → 2 moduły

[Analogiczny proces]

#### Faza 4: Podział IR_SBOM_Impact (Week 9-10)
**Cel:** 1 moduł → 3 moduły

[Analogiczny proces]

#### Faza 5: Integracja i Weryfikacja (Week 11-12)
**Cel:** End-to-end testing nowej architektury

- [ ] Integration tests (wszystkie moduły razem)
- [ ] Performance benchmarks (vs AS-IS baseline)
- [ ] Security audit (penetration testing)
- [ ] Documentation review (completeness check)
- [ ] User Acceptance Testing

#### Faza 6: Production Rollout (Week 13-14)
**Cel:** Deployment do production

- [ ] Blue-green deployment preparation
- [ ] Gradual rollout (10% → 50% → 100%)
- [ ] Monitoring dashboards
- [ ] On-call runbooks
- [ ] Post-mortem retrospective

**Total Timeline:** 14 tygodni (~3.5 miesiące)

### 13.2. Rollback Plan

**Per Faza:**
- Feature flags: Switch back to old modules
- Database migrations: Reversible (down scripts)
- Artifacts: Keep old versions for 2 releases

**Emergency Rollback:**
1. Disable new module (feature flag)
2. Route traffic to old module
3. Verify functionality
4. Investigate root cause
5. Fix forward or stay on old

---

## 14. RYZYKA I MITIGACJE

| ID | Ryzyko | Prawdopodobieństwo | Wpływ | Score | Mitigacja |
|----|--------|-------------------|-------|-------|-----------|
| R-001 | Podział modułów wprowadza regresje | Medium | High | 15 | Extensive testing, parallel run old/new |
| R-002 | Interfaces nie pokrywają wszystkich use cases | Medium | High | 15 | Early prototyping, stakeholder review |
| R-003 | Performance degradacja po podziale | Low | Medium | 6 | Benchmarking, optimization budget |
| R-004 | Team overload (3.5 miesiąca) | High | Medium | 18 | Prioritization, external help |
| R-005 | Breaking changes w dependencies | Medium | Medium | 9 | Versioning, backward compat |
| R-006 | Documentation drift | High | Low | 9 | Automated checks, CI enforcement |
| R-007 | Observability gaps | Medium | Medium | 9 | Phased rollout, dashboards first |

**Mitigation Strategies:**
- **R-001, R-002:** Contract testing, integration tests, gradual rollout
- **R-003:** Performance budgets w CI, regression benchmarks
- **R-004:** Clear prioritization (P0 first), possible timeline extension
- **R-005:** Dependency Inversion, interfaces stable
- **R-006:** Docs as code, CI checks for missing docs
- **R-007:** Observability stack in Phase 0

---

## 15. METRYKI SUKCESU (KPIs)

### 15.1. KPI Techniczne

| Metryka | Baseline (AS-IS) | Target (TO-BE) | Measurement |
|---------|------------------|----------------|-------------|
| **Modularność** | 14 modułów, max 48 MB | 26 modułów, max < 15 MB | Module size distribution |
| **Coupling** | Instability avg 0.45 | < 0.40 | Dependency metrics |
| **Test Coverage** | 69% | > 85% | Coverage reports |
| **Technical Debt** | 147 dni (18.5%) | < 75 dni (< 10%) | SonarQube debt ratio |
| **Build Time** | 20 min | < 15 min | CI/CD pipeline time |
| **CVE Count** | 12 (2 Critical) | 0 Critical, < 5 Total | Security scan |
| **Documentation** | 6/14 modules with README | 26/26 (100%) | Automated check |
| **Performance (SAST)** | 45s avg | < 30s avg | Benchmark suite |
| **Performance (Canvas)** | 120ms p95 | < 80ms p95 | APM metrics |

### 15.2. KPI Biznesowe

| Metryka | Baseline | Target | Impact |
|---------|----------|--------|--------|
| **Time to Market (nowe features)** | 4 tygodnie | 2 tygodnie | Faster delivery |
| **Bug rate** | 15 bugs/release | < 8 bugs/release | Better quality |
| **Onboarding time (nowi devs)** | 3 tygodnie | 1 tydzień | Better docs, smaller modules |
| **Incident MTTR** | 4h | < 2h | Better observability |
| **Deployment frequency** | 1×/miesiąc | 2×/tydzień | Per-module deploys |
| **Change failure rate** | 15% | < 5% | Better testing |

### 15.3. Acceptance Criteria

**Przed uznaniem transformacji za ukończoną:**

**Must Have (P0):**
- [ ] Wszystkie 12 nowych modułów deployed i działające
- [ ] 0 Critical CVE
- [ ] Test coverage > 85% (overall)
- [ ] Wszystkie moduły mają complete docs (README, ARCH, API)
- [ ] Observability stack operational (metrics, tracing, alerting)
- [ ] Performance SLA met (< targets)

**Should Have (P1):**
- [ ] RBAC implemented i tested
- [ ] Contract tests dla wszystkich inter-module dependencies
- [ ] Architectural tests passing (no violations)
- [ ] Migration guides dla wszystkich breaking changes

**Nice to Have (P2):**
- [ ] Automated release process (CI/CD)
- [ ] Chaos engineering tests
- [ ] Developer portal (centralized docs)

---

## 16. PORÓWNANIE AS-IS vs TO-BE

| Aspekt | AS-IS | TO-BE | Poprawa |
|--------|-------|-------|---------|
| **Liczba modułów** | 14 | 26 | +86% (lepsza granularność) |
| **Największy moduł** | 48 MB (Security) | < 15 MB | -69% |
| **Moduły > 10 MB** | 2 | 0 | -100% |
| **Duplikacje kodu** | 15% | < 3% | -80% |
| **Test coverage** | 69% | > 85% | +16pp |
| **Technical debt** | 147 dni | < 75 dni | -49% |
| **CVE Critical** | 2 | 0 | -100% |
| **Interfejsy zdefiniowane** | 0% | 100% | +100% |
| **Observability** | Minimal | Full stack | N/A |
| **Documentation** | 43% (6/14) | 100% (26/26) | +57pp |
| **SAST scan time** | 45s | < 30s | -33% |
| **Build time** | 20 min | < 15 min | -25% |
| **Deployment frequency** | 1×/month | 2×/week | +800% |

**Kluczowe Zmiany:**
1. ✅ Modularność: +12 modułów (separation of concerns)
2. ✅ Coupling: Interfejsy 100%, dependency inversion
3. ✅ Quality: Technical debt -49%, coverage +16pp
4. ✅ Security: 0 Critical CVE, RBAC, sanitization
5. ✅ Performance: -33% scan time, -25% build time
6. ✅ Observability: Full stack (metrics, tracing, alerting)
7. ✅ DevOps: Per-module CI/CD, automated deployment

---

## ZAŁĄCZNIKI

### A. Architectural Decision Records (ADRs)

**ADR-001: Split Security_Analysis into 4 modules**
- **Status:** Accepted
- **Context:** Security_Analysis is 48 MB monolith with 4 distinct responsibilities
- **Decision:** Split into SAST_Engine, SCA_Engine, Secrets_Scanner, FixOps
- **Consequences:** Better SoC, but more integration complexity

**ADR-002: Use Dependency Inversion for all inter-module dependencies**
- **Status:** Accepted
- **Context:** Tight coupling w AS-IS (direct imports)
- **Decision:** All dependencies via interfaces (Protocols)
- **Consequences:** Loose coupling, testability, but more boilerplate

[Więcej ADRs w `docs/decisions/`]

### B. Referencje

- **Clean Architecture:** Robert C. Martin, "Clean Architecture: A Craftsman's Guide to Software Structure and Design"
- **arc42:** https://arc42.org/
- **C4 Model:** https://c4model.com/
- **Semantic Versioning:** https://semver.org/
- **OpenTelemetry:** https://opentelemetry.io/
- **Prometheus:** https://prometheus.io/

### C. Historia Zmian

| Wersja | Data | Autor | Zmiany |
|--------|------|-------|--------|
| 1.0 | 2025-11-09 | [Autor] | Wersja początkowa zgodna z arc42 + Clean Arch |

---

**Poprzedni dokument:** ← `01_AS_IS_STAN_OBECNY.md`  
**Następny dokument:** → `04_PROCES_REFAKTORYZACJI.md`  
**Powiązane:** → `06_PUNKTY_INTEGRACJI.md` (interfejsy), → `03_PROBLEMY_I_BŁĘDY.md` (co naprawiamy)

---

## CHECKLIST KOMPLETNOŚCI

- [x] Executive Summary (wizja, cele, dashboard)
- [x] Zasady architektoniczne (SOLID, wzorce, reguły)
- [x] Architektura docelowa (C4 L1, L2, hierarchia, lista modułów)
- [x] Szczegóły każdego z 26 modułów (odpowiedzialność, granice, struktura, API, zależności)
- [x] Zależności między modułami (graf, macierz, reguły, interfejsy, wersjonowanie)
- [x] Wspólne zasoby (SHARED_RESOURCES: cel, zawartość, zasady)
- [x] Dane i storage (ownership, współdzielenie, database strategy)
- [x] Bezpieczeństwo (principles, kontrole, RBAC, secrets, CVE management)
- [x] Wydajność i skalowalność (SLA, optimization, scaling, limits)
- [x] Observability (logging, metrics, tracing, alerting)
- [x] DevOps i CI/CD (pipeline, versioning, deployment strategies)
- [x] Testowanie (strategy, contract testing, architectural tests)
- [x] Dokumentacja (standardy, levels, quality gates)
- [x] Migration path (fazy, timeline, rollback plan)
- [x] Ryzyka i mitigacje (lista, scoring, strategie)
- [x] Metryki sukcesu (KPI technical, KPI business, acceptance criteria)
- [x] Porównanie AS-IS vs TO-BE (tabela zmian)
- [x] Załączniki (ADRs, referencje, historia)
- [x] Cross-references (linki do AS-IS, Process, Integration Points)
