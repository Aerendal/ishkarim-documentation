# Analiza i Roadmapa: [Nazwa Modułu]

> **Framework:** arc42 + Module-specific Analysis  
> **Data analizy:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół/Module Owner]  
> **Status:** [Draft / Review / Approved]  
> **Powiązane:** ← `01_AS_IS` (sekcja dla tego modułu), → `02_TO_BE` (docelowa architektura), → `04_PROCES` (plan transformacji)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: AS-IS-ARCHITECTURE
    type: module_inventory
    from_sections:
      - module_list
      - module_metrics
    to_sections:
      - analysis_scope
      - baseline_metrics
    influence: "AS-IS dostarcza listę modułów do analizy"
    when:
      condition: roadmap.type == "module_analysis"
      applies: always

  - id: TO-BE-ARCHITECTURE
    type: target_state
    from_sections:
      - target_modules
      - module_design
    to_sections:
      - transformation_goals
      - success_criteria
    influence: "TO-BE definiuje docelowy stan modułów"
    when:
      condition: architecture.has_target == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: REFACTORING-PROCESS
    type: detailed_planning
    from_sections:
      - module_roadmaps
      - dependencies_analysis
    to_sections:
      - implementation_sequence
      - phase_planning
    influence: "Roadmapy modułów informują o sekwencji refaktoringu"
    when:
      condition: roadmaps.complete == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: DEPENDENCY-GRAPH
    relationship: impact_analysis
    sections_mapping:
      - from: module_dependencies
        to: change_impact
    usage: "Graf zależności pokazuje wpływ zmian"
```

### Satellite Documents

```yaml
satellites:
  - name: PER-MODULE-ADR
    purpose: "ADR specyficzne dla każdego modułu"
    trigger: per_module
    lifecycle: permanent
    retention: permanent
```

---

## EXECUTIVE SUMMARY

### Moduł Overview

**ID:** [MXX]  
**Nazwa:** [Nazwa Modułu]  
**Kategoria:** [CORE_ENGINES / INTELLIGENCE_FEATURES / PLATFORM_SERVICES / etc.]  
**Status:** [Istniejący / Nowy (split z X) / Do Utworzenia]  
**Priorytet:** [P0 / P1 / P2]  
**Owner:** [Zespół]

### Kluczowe Charakterystyki

| Metryka | Wartość Obecna | Wartość Docelowa | Delta |
|---------|----------------|------------------|-------|
| **Rozmiar** | [X MB / plików] | [Y MB / plików] | [%] |
| **LOC** | [X linii] | [Y linii] | [%] |
| **Test Coverage** | [X%] | > 85% | +[Y]pp |
| **Technical Debt** | [X dni] | < [Y dni] | -[Z]% |
| **CVE Critical** | [N] | 0 | -100% |
| **Dependencies** | [N modułów] | [M modułów] | [change] |

### Status Transformation

**Obecny Stan (AS-IS):**
- [Krótki opis obecnego stanu - 2-3 zdania]
- [Główne problemy]

**Docelowy Stan (TO-BE):**
- [Krótki opis docelowego stanu - 2-3 zdania]
- [Kluczowe zmiany]

**Timeline:**
- **Start:** [YYYY-MM-DD]
- **Target Completion:** [YYYY-MM-DD]
- **Duration:** [N tygodni]

---

## 1. ODPOWIEDZIALNOŚĆ MODUŁU (SINGLE RESPONSIBILITY)

### 1.1. Główna Odpowiedzialność

**Jedno zdanie:** [Moduł X jest odpowiedzialny za Y]

**Szczegóły:**
[2-3 akapity opisujące dokładnie za co moduł odpowiada]

**Przykłady użycia:**
1. **Use Case 1:** [Opis - co użytkownik/system robi z tym modułem]
2. **Use Case 2:** [Opis]
3. **Use Case 3:** [Opis]

### 1.2. Granice Odpowiedzialności

**W zakresie (IN SCOPE):**
- ✅ [Funkcjonalność 1 - co JEST w zakresie]
- ✅ [Funkcjonalność 2]
- ✅ [Funkcjonalność 3]

**Poza zakresem (OUT OF SCOPE):**
- ❌ [Funkcjonalność 1 - co NIE jest w zakresie, kto za to odpowiada]
- ❌ [Funkcjonalność 2 - delegowane do modułu X]
- ❌ [Funkcjonalność 3 - delegowane do modułu Y]

### 1.3. Kryteria Przynależności

**Kod należy do tego modułu jeśli:**
1. [Kryterium 1 - np. "Dotyczy parsowania Python AST"]
2. [Kryterium 2 - np. "Nie wymaga external API calls"]
3. [Kryterium 3]

**Kod NIE należy tutaj jeśli:**
1. [Anti-kryterium 1 - np. "Wymaga dostępu do bazy danych" → to jest w innym module]
2. [Anti-kryterium 2]

---

## 2. ARCHITEKTURA MODUŁU

### 2.1. High-Level Structure

**Pattern:** [Clean Architecture / Hexagonal / Layered / etc.]

```
[Nazwa Modułu]/
├── README.md
├── ARCHITECTURE.md (ten dokument)
├── API_REFERENCE.md
├── CHANGELOG.md
│
├── src/
│   ├── core/          # Business logic (use cases)
│   ├── domain/        # Domain models (entities)
│   ├── interfaces/    # Abstractions (ports)
│   ├── adapters/      # External system adapters
│   ├── api/           # Public API
│   └── utils/         # Helpers
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── fixtures/
│
├── docs/
│   ├── decisions/     # ADRs
│   ├── diagrams/
│   └── guides/
│
├── examples/
│   └── example_usage.py
│
├── config/
│   └── default.yaml
│
└── schemas/
    └── data_schema.json
```

### 2.2. Component Diagram (C4 Level 3)

```
┌─────────────────────────────────────────┐
│         [Nazwa Modułu]                  │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────┐                       │
│  │   Public    │ ◄─── External Users   │
│  │     API     │                       │
│  └──────┬──────┘                       │
│         │                               │
│  ┌──────▼──────┐                       │
│  │    Core     │ ◄─── Business Logic   │
│  │  Use Cases  │                       │
│  └──────┬──────┘                       │
│         │                               │
│  ┌──────▼──────┐                       │
│  │   Domain    │ ◄─── Entities/Models  │
│  │   Models    │                       │
│  └──────┬──────┘                       │
│         │                               │
│  ┌──────▼──────┐                       │
│  │  Adapters   │ ◄─── External Systems │
│  └─────────────┘                       │
│                                         │
└─────────────────────────────────────────┘
```

### 2.3. Kluczowe Komponenty

#### 2.3.1. [Komponent 1: Nazwa]

**Odpowiedzialność:** [Co robi ten komponent]

**Lokalizacja:** `src/core/component1.py`

**Kluczowe klasy/funkcje:**
```python
class Component1:
    """[Docstring - co robi]."""
    
    def main_method(self, params):
        """[Opis metody]."""
        ...
```

**Dependencies:**
- **Upstream:** [Od czego zależy - inne komponenty/moduły]
- **Downstream:** [Co od niego zależy]

#### 2.3.2. [Komponent 2: Nazwa]

[Analogicznie jak 2.3.1]

[Powtórz dla wszystkich kluczowych komponentów - zwykle 3-7]

---

## 3. PUBLICZNE API

### 3.1. Interfejs Główny

**Nazwa:** [I<Nazwa>Protocol]

**Lokalizacja:** `shared_resources/interfaces/<nazwa>_protocol.py`

**Metody:**

```python
from typing import Protocol

class I<Nazwa>Protocol(Protocol):
    """[Opis interfejsu - kontrakt]."""
    
    def method1(self, param: Type) -> ReturnType:
        """[Opis metody 1].
        
        Args:
            param: [Opis parametru]
        
        Returns:
            [Opis zwracanej wartości]
        
        Raises:
            [Wyjątki]
        
        SLA:
            - Latency: [< X ms/s]
            - Memory: [< Y MB]
        """
        ...
    
    def method2(self, param: Type) -> ReturnType:
        """[Opis metody 2]."""
        ...
```

### 3.2. Modele Danych (Domain)

**[Model 1]:**
```python
from dataclasses import dataclass

@dataclass
class Model1:
    """[Opis modelu]."""
    field1: str
    field2: int
    field3: Optional[str] = None
```

**JSON Schema:**
```json
{
  "type": "object",
  "properties": {
    "field1": {"type": "string"},
    "field2": {"type": "integer"},
    "field3": {"type": "string"}
  },
  "required": ["field1", "field2"]
}
```

### 3.3. Przykłady Użycia

**Podstawowe użycie:**
```python
from <module> import create_<service>

service = create_<service>()
result = service.method1(param)
print(result)
```

**Zaawansowane (z konfiguracją):**
```python
from <module> import create_<service>, Config

config = Config(
    option1=value1,
    option2=value2
)
service = create_<service>(config)
result = service.method1(param)
```

**Error handling:**
```python
try:
    result = service.method1(param)
except ValueError as e:
    logger.error(f"Invalid input: {e}")
except TimeoutError:
    logger.warning("Operation timed out")
```

---

## 4. ZALEŻNOŚCI

### 4.1. Graf Zależności

```
[Nazwa Modułu]
    │
    ├─ depends on ──▶ [Module A]
    │                  (via IInterfaceA)
    │
    ├─ depends on ──▶ [Module B]
    │                  (via IInterfaceB)
    │
    └─ depends on ──▶ [External: Library X]
                       (version constraint)

[Module C] ──▶ depends on ──▶ [Nazwa Modułu]
                               (via IThisModuleInterface)
[Module D] ──▶ depends on ──▶ [Nazwa Modułu]
```

### 4.2. Dependencies Details

#### 4.2.1. Upstream (od czego zależy ten moduł)

| Dependency | Type | Interface | Version | Criticality | Justification |
|------------|------|-----------|---------|-------------|---------------|
| [Module A] | Internal | IInterfaceA | ^1.0 | High | [Dlaczego potrzebna ta zależność] |
| [Library X] | External | - | >= 2.0 | Medium | [Dlaczego] |

**Coupling Metrics:**
- **Efferent Coupling (Ce):** [N] - liczba modułów od których zależy
- **Instability (I):** [0.0-1.0] - I = Ce / (Ca + Ce)

**Target:** I < 0.5 dla foundation modules, I 0.5-0.8 dla higher-level modules

#### 4.2.2. Downstream (co zależy od tego modułu)

| Consumer | Via Interface | Use Case | Criticality |
|----------|---------------|----------|-------------|
| [Module C] | IThisModule | [Opis użycia] | High |
| [Module D] | IThisModule | [Opis] | Medium |

**Coupling Metrics:**
- **Afferent Coupling (Ca):** [N] - liczba modułów które od niego zależą
- **Stability:** [0.0-1.0] - Im wyższe Ca, tym bardziej stabilny (więcej od niego zależy)

### 4.3. External Dependencies (Libraries)

| Library | Version | Purpose | License | Size | Last Updated |
|---------|---------|---------|---------|------|--------------|
| [lib1] | ^2.0.0 | [Do czego używane] | MIT | 5 MB | 2024-10 |
| [lib2] | >= 1.5 | [Purpose] | Apache-2.0 | 2 MB | 2024-09 |

**Dependency Management:**
- **Python:** `requirements.txt` / `pyproject.toml`
- **JavaScript:** `package.json`
- **Automated updates:** Dependabot enabled

---

## 5. ANALIZA OBECNEGO STANU (AS-IS)

### 5.1. Statystyki

**Rozmiar:**
- **Total size:** [X MB]
- **Files:** [N plików]
- **LOC:** [X linii kodu]
- **Średnia LOC/plik:** [Y]

**Największe pliki:** (potencjalne God Objects)
1. `path/to/file1.py` - [X LOC]
2. `path/to/file2.py` - [Y LOC]

**Struktura katalogów:**
- **Liczba katalogów:** [N]
- **Średnia głębokość:** [M poziomów]

### 5.2. Jakość Kodu

**Test Coverage:**
- **Unit:** [X%]
- **Integration:** [Y%]
- **E2E:** [Z%]
- **Overall:** [W%]

**Target:** > 85%

**Complexity:**
- **Średnia McCabe:** [X]
- **Max McCabe:** [Y] w `[file:function]`
- **Target:** Średnia < 10, Max < 20

**Duplikacje:**
- **Całkowita duplikacja:** [X%]
- **Target:** < 3%

**Technical Debt:**
- **Debt (person-days):** [X dni]
- **Debt Ratio:** [Y%]
- **SQALE Rating:** [A-E]

**Maintainability Index:**
- **Średnia:** [X] (scale 0-100)
- **Target:** > 70

### 5.3. Problemy Zidentyfikowane

[Cross-reference do `03_PROBLEMY_I_BŁĘDY.md`]

**Top 5 problemów w tym module:**

| ID | Problem | Severity | Impact | Effort |
|----|---------|----------|--------|--------|
| [A-XXX] | [Opis] | P0 | [Area] | XL |
| [T-XXX] | [Opis] | P1 | [Area] | M |
| [Q-XXX] | [Opis] | P2 | [Area] | S |

**Szczegóły:** Zobacz `03_PROBLEMY_I_BŁĘDY.md` sekcje [X.Y]

### 5.4. Security

**CVE Count:**
- **Critical:** [N]
- **High:** [M]
- **Medium:** [K]
- **Low:** [L]

**Target:** 0 Critical, < 3 High

**Known Issues:**
- [CVE-ID]: [Opis - w jakiej dependency, jaki impact]

### 5.5. Performance

**Current Metrics:**

| Operation | Latency (avg) | Latency (p95) | Memory | SLA | Status |
|-----------|---------------|---------------|--------|-----|--------|
| [Op 1] | [X ms/s] | [Y ms/s] | [Z MB] | [SLA] | ✓/⚠️/✗ |
| [Op 2] | [X] | [Y] | [Z] | [SLA] | ✓/⚠️/✗ |

**Bottlenecks:**
1. [Bottleneck 1 - opis, lokalizacja, impact]
2. [Bottleneck 2]

---

## 6. DOCELOWA ARCHITEKTURA (TO-BE)

### 6.1. Zmiany Strukturalne

**Jeśli moduł istniejący - refactoring:**
- [Zmiana 1 - co i dlaczego zmieniamy]
- [Zmiana 2]

**Jeśli nowy moduł (split):**
- **Extracted from:** [Parent Module]
- **Reason for split:** [Dlaczego wydzielamy]
- **What moves:** [Co przenosimy do nowego modułu]

**Struktura docelowa:**
[Opis jak będzie wyglądała struktura po zmianach]

### 6.2. Nowe/Zmienione Komponenty

**[Komponent 1: Nowy/Zmieniony]:**
- **Status:** [New / Refactored / Deprecated]
- **Purpose:** [Co robi]
- **Changes:** [Jak się zmienia vs AS-IS]

### 6.3. Interfejsy i API

**Zmiany w publicznym API:**

**Breaking Changes (MAJOR version bump):**
- [Change 1 - old signature → new signature]
- [Migration guide link]

**Backward-Compatible Changes (MINOR):**
- [Change 1 - new method added]
- [Change 2 - new optional parameter]

**Bug Fixes (PATCH):**
- [Fix 1]

### 6.4. Docelowe Metryki

| Metryka | Current | Target | How to Achieve |
|---------|---------|--------|----------------|
| **Rozmiar** | [X MB] | [Y MB] | [Extract to separate module] |
| **Test Coverage** | [X%] | > 85% | [Add unit tests for...] |
| **Complexity** | [X avg] | < 10 avg | [Refactor God Objects] |
| **Tech Debt** | [X days] | < [Y days] | [Fix issues A-XXX, T-XXX] |
| **CVE Critical** | [N] | 0 | [Update dependencies] |
| **Performance** | [X ms] | < [Y ms] | [Optimize bottleneck Z] |

---

## 7. ROADMAP TRANSFORMACJI

### 7.1. Fazy

#### Phase 0: Przygotowanie (Week [N])

**Cel:** Groundwork dla transformacji

**Tasks:**
- [ ] [Task 1 - opis, owner]
- [ ] [Task 2]
- [ ] [Task 3]

**Deliverables:**
- [Deliverable 1]
- [Deliverable 2]

**Effort:** [X person-days]

#### Phase 1: [Nazwa Fazy] (Week [N-M])

**Cel:** [Główny cel tej fazy]

**Tasks:**
- [ ] [Task 1]
- [ ] [Task 2]

**Acceptance Criteria:**
- [ ] [Kryterium 1]
- [ ] [Kryterium 2]

**Deliverables:**
- [Deliverable 1]

**Effort:** [X person-days]

#### Phase 2: [Nazwa] (Week [M-K])

[Analogicznie jak Phase 1]

[Powtórz dla wszystkich faz - typowo 3-5 faz]

#### Phase N: Finalizacja i Weryfikacja

**Cel:** Validation i deployment

**Tasks:**
- [ ] Regression testing
- [ ] Performance benchmarks
- [ ] Documentation review
- [ ] Deployment

**Acceptance Criteria:**
- [ ] All tests pass
- [ ] Performance SLA met
- [ ] Documentation complete
- [ ] Approved by architect

### 7.2. Timeline

**Total Duration:** [N tygodni]

**Gantt Chart:**
```
Phase                | W1 | W2 | W3 | W4 | W5 | W6 |
---------------------|----|----|----|----|----|----|
Phase 0: Prep        |████|    |    |    |    |    |
Phase 1: [Name]      |    |████|████|    |    |    |
Phase 2: [Name]      |    |    |████|████|    |    |
Phase 3: Validation  |    |    |    |    |████|████|
```

**Milestones:**

| Milestone | Week | Deliverables | Status |
|-----------|------|--------------|--------|
| [M1] | [W1] | [Lista] | ⏳ Pending |
| [M2] | [W3] | [Lista] | ⏳ Pending |
| [M3] | [W6] | [Lista] | ⏳ Pending |

### 7.3. Resources

**Team:**
- **Owner:** [Osoba - primary responsible]
- **Developers:** [N osób]
- **QA:** [M osób]
- **Architect:** [Osoba - review i guidance]

**Tools:**
- [Tool 1 - do czego]
- [Tool 2]

**Budget:**
- **Effort:** [X person-days total]
- **Cost:** [Jeśli applicable]

---

## 8. MIGRATION PLAN

### 8.1. Migration Strategy

**Approach:** [Strangler Fig / Big Bang / Incremental / etc.]

**Rationale:** [Dlaczego wybraliśmy tę strategię]

### 8.2. Migration Steps

**Step 1: [Nazwa]**
- **Action:** [Co robimy]
- **Affected:** [Co/kto dotknięte]
- **Rollback:** [Jak wycofać jeśli problem]

**Step 2: [Nazwa]**
[Analogicznie]

[Powtórz dla wszystkich kroków]

### 8.3. Data Migration (jeśli applicable)

**Data to migrate:**
- [Dataset 1 - rozmiar, format, lokalizacja]
- [Dataset 2]

**Migration process:**
1. [Krok 1 - backup]
2. [Krok 2 - transform]
3. [Krok 3 - load]
4. [Krok 4 - verify]

**Rollback plan:**
[Jak przywrócić dane jeśli migration fails]

### 8.4. Consumer Migration

**Consumers to update:**

| Consumer Module | Current Dependency | New Dependency | Owner | Status |
|-----------------|-------------------|----------------|-------|--------|
| [Module C] | [Old API] | [New API] | [Team] | ⏳ Pending |
| [Module D] | [Old API] | [New API] | [Team] | ⏳ Pending |

**Migration Support:**
- **Wrapper:** [Czy zapewniamy wrapper dla old API przez transition period?]
- **Deprecation notice:** [When do we deprecate old API?]
- **Communication:** [How do we notify consumers?]

---

## 9. TESTING STRATEGY

### 9.1. Test Plan

**Levels:**

| Level | Coverage Target | Responsibility | Status |
|-------|-----------------|----------------|--------|
| Unit | > 85% | Developers | [X% current] |
| Integration | > 75% | Developers | [Y% current] |
| E2E | > 60% | QA | [Z% current] |
| Contract | 100% interfaces | Developers | [W% current] |
| Performance | No regression | QA | [Status] |

### 9.2. Test Cases

**Unit Tests:**
- [ ] [Test scenario 1]
- [ ] [Test scenario 2]

**Integration Tests:**
- [ ] [Integration scenario 1 - with Module A]
- [ ] [Integration scenario 2 - with Module B]

**E2E Tests:**
- [ ] [E2E scenario 1 - full flow]

**Regression Tests:**
- [ ] [Verify parity with old implementation]

**Performance Tests:**
- [ ] [Load test: X concurrent operations]
- [ ] [Stress test: Y operations/sec]

### 9.3. Acceptance Criteria

**Module-level:**
- [ ] All tests pass (unit, integration, E2E)
- [ ] Test coverage > 85%
- [ ] No Critical LSP errors
- [ ] No Critical CVE
- [ ] Performance SLA met
- [ ] Documentation complete

**Integration-level:**
- [ ] Contract tests pass (consumer & provider)
- [ ] All consumers migrated successfully
- [ ] No breaking changes introduced (or migration guide provided)

---

## 10. RISKS & MITIGATION

### 10.1. Risk Register

| ID | Risk | Probability | Impact | Score | Mitigation |
|----|------|-------------|--------|-------|------------|
| R-001 | [Opis ryzyka] | High/Med/Low | High/Med/Low | [P×I] | [Strategia] |
| R-002 | [Opis] | Med | High | 12 | [Strategia] |

### 10.2. Specific Risks dla tego modułu

**R-001: [Risk Name]**
- **Description:** [Co może pójść nie tak]
- **Impact:** [Jeśli się zmaterializuje, co się stanie]
- **Probability:** [High/Medium/Low]
- **Mitigation:** [Jak zapobiegamy / minimalizujemy]
- **Contingency:** [Plan B jeśli się zdarzy]

---

## 11. SUCCESS METRICS

### 11.1. KPI

| Metric | Baseline | Target | Current | % to Target |
|--------|----------|--------|---------|-------------|
| Test Coverage | [X%] | > 85% | [Y%] | [Z%] |
| Tech Debt | [X days] | < [Y days] | [Z days] | [W%] |
| Performance | [X ms] | < [Y ms] | [Z ms] | [W%] |
| CVE Count | [N] | 0 Critical | [M] | [Progress] |

### 11.2. Business Impact

**Quantifiable:**
- [Metric 1 - np. "Reduced scan time by 33%"]
- [Metric 2 - np. "Enabled 2× more scans/day"]

**Qualitative:**
- [Impact 1 - np. "Improved developer experience"]
- [Impact 2]

---

## ZAŁĄCZNIKI

### A. ADRs (Architecture Decision Records) dla tego modułu

**ADR-XXX: [Decision Title]**
- **Status:** Accepted
- **Context:** [Why was this decision needed?]
- **Decision:** [What did we decide?]
- **Consequences:** [What became easier/harder?]

[Lista wszystkich ADRs dla tego modułu]

### B. Referencje

**Code:**
- Interface: `shared_resources/interfaces/<module>_protocol.py`
- Implementation: `<Module>/src/api/__init__.py`
- Tests: `<Module>/tests/`

**Documentation:**
- README: `<Module>/README.md`
- API Reference: `<Module>/API_REFERENCE.md`
- Examples: `<Module>/examples/`

**Related Documents:**
- AS-IS Analysis: `01_AS_IS.md#[section]`
- TO-BE Architecture: `02_TO_BE.md#[section]`
- Problems Catalog: `03_PROBLEMY.md#[section]`
- Process: `04_PROCES.md#[phase]`

### C. Historia Zmian

| Wersja | Data | Autor | Zmiany |
|--------|------|-------|--------|
| 0.1 | [YYYY-MM-DD] | [Autor] | Draft początkowy |
| 1.0 | [YYYY-MM-DD] | [Autor] | Approved version |

---

## CHECKLIST KOMPLETNOŚCI

- [x] Executive Summary (overview, charakterystyki, status)
- [x] Odpowiedzialność modułu (SRP, granice, kryteria)
- [x] Architektura (struktura, komponenty, C4 diagram)
- [x] Publiczne API (interfejs, modele, przykłady)
- [x] Zależności (graf, upstream, downstream, metrics)
- [x] Analiza AS-IS (statystyki, jakość, problemy, security, performance)
- [x] Docelowa architektura TO-BE (zmiany, komponenty, API, metryki)
- [x] Roadmap (fazy, timeline, resources)
- [x] Migration plan (strategy, steps, data, consumers)
- [x] Testing strategy (plan, cases, acceptance)
- [x] Risks & Mitigation (register, specific risks)
- [x] Success metrics (KPI, business impact)
- [x] Załączniki (ADRs, referencje, historia)
- [x] Cross-references (AS-IS, TO-BE, PROBLEMY, PROCES)

**Wypełnienie:** Wszystkie `[placeholders]` zamienione na rzeczywiste wartości przed approval.
