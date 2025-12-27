# Proces Refaktoryzacji i Transformacji

> **Framework:** arc42 (Rozdział 9: Architecture Decisions) + Clean Architecture Principles  
> **Data opracowania:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół]  
> **Status:** [Draft/Review/Approved]  
> **Powiązane:** ← `03_PROBLEMY_I_BŁĘDY`, → `02_TO_BE`, ← `01_AS_IS`

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: PROBLEMS-ANALYSIS
    type: work_input
    from_sections:
      - prioritized_problems
      - root_causes
    to_sections:
      - refactoring_scope
      - phase_planning
    influence: "Katalog problemów definiuje co refaktorować"
    when:
      condition: process.type == "refactoring"
      applies: always

  - id: TO-BE-ARCHITECTURE
    type: target_definition
    from_sections:
      - target_architecture
      - design_patterns
    to_sections:
      - refactoring_goals
      - acceptance_criteria
    influence: "TO-BE określa docelowy stan refaktoringu"
    when:
      condition: architecture.defined == true
      applies: always

  - id: AS-IS-ARCHITECTURE
    type: baseline
    from_sections:
      - current_modules
      - dependencies
    to_sections:
      - migration_starting_point
      - impact_analysis
    influence: "AS-IS jest punktem wyjścia dla transformacji"
    when:
      condition: migration.requires_baseline == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: SPRINT-BACKLOG
    type: work_items
    from_sections:
      - refactoring_tasks
      - phase_breakdown
    to_sections:
      - sprint_planning
      - task_assignments
    influence: "Proces refaktoringu generuje zadania do sprintów"
    when:
      condition: process.started == true
      applies: always

  - id: TDD-STRATEGY
    type: quality_assurance
    from_sections:
      - testing_requirements
      - quality_gates
    to_sections:
      - test_coverage_goals
      - testing_approach
    influence: "Refaktoring wymaga strategii testowania"
    when:
      condition: quality.testing_required == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: MIGRATION-PLAYBOOK
    relationship: execution_guide
    sections_mapping:
      - from: migration_procedures
        to: execution_steps
    usage: "Playbook szczegółowo opisuje kroki migracji"
```

### Satellite Documents

```yaml
satellites:
  - name: REFACTORING-PROGRESS-TRACKER
    purpose: "Tracking postępu refaktoringu"
    trigger: continuous
    lifecycle: process_duration
    retention: permanent

  - name: PHASE-COMPLETION-REPORTS
    purpose: "Raporty zakończenia każdej fazy"
    trigger: per_phase
    lifecycle: per_phase
    retention: permanent
```

---

## EXECUTIVE SUMMARY

### Cel Procesu
[Dlaczego robimy refaktoryzację - business + technical reasons, 2-3 zdania]

### Zakres Transformacji

**Co transformujemy:**
- **Strukturę:** 14 modułów → 26 modułów (podział monolitów)
- **Architekturę:** Tight coupling → Loose coupling (interfaces)
- **Jakość:** Tech debt 147 dni → < 75 dni (-49%)
- **Bezpieczeństwo:** 12 CVE → 0 Critical CVE
- **Performance:** SAST 45s → < 30s (-33%)

### Timeline i Resources

| Faza | Duration | Team Size | Deliverables |
|------|----------|-----------|--------------|
| **Phase 0: Preparation** | 2 tygodnie | 3 devs | CVE patches, interfaces, SHARED_RESOURCES skeleton |
| **Phase 1: Security Split** | 3 tygodnie | 4 devs | 4 nowe moduły z Security_Analysis |
| **Phase 2: Code_Refact Split** | 2 tygodnie | 3 devs | 3 nowe moduły z Code_Refactoring |
| **Phase 3: Provenance Split** | 1 tydzień | 2 devs | 2 nowe moduły z Provenance_Secrets |
| **Phase 4: IR_SBOM Split** | 2 tygodnie | 3 devs | 3 nowe moduły z IR_SBOM_Impact |
| **Phase 5: Integration** | 2 tygodnie | 5 devs | E2E testing, performance validation |
| **Phase 6: Rollout** | 2 tygodnie | 6 devs | Production deployment, monitoring |
| **TOTAL** | **14 tygodni** | **Peak: 6** | **26 modułów + full observability** |

### Success Dashboard

| Metryka | Start | Target | Status |
|---------|-------|--------|--------|
| Critical CVE | 2 | 0 | 🔄 In Progress |
| Modules | 14 | 26 | 🔄 In Progress |
| Largest Module | 48 MB | < 15 MB | 🔄 In Progress |
| Test Coverage | 69% | > 85% | 🔄 In Progress |
| Tech Debt | 147 days | < 75 days | 🔄 In Progress |
| Documentation | 43% | 100% | 🔄 In Progress |

---

## 1. ZASADY PROCESU REFAKTORYZACJI

### 1.1. Fundamentalne Zasady

#### 1.1.1. Nie Psuj Działającego Systemu
**Principle:** Make it work, make it right, make it fast (in that order).

**Praktyczne implikacje:**
- Każda zmiana musi mieć regresję tests
- Feature flags dla smooth rollout
- Rollback plan dla każdej fazy
- Production nie może się złamać!

**Enforcement:**
```yaml
# CI/CD gate:
before_merge:
  - regression_tests: PASS
  - integration_tests: PASS
  - performance_benchmarks: < baseline + 10%
```

#### 1.1.2. Incremental Transformation
**Principle:** Mały krok, validate, next step. Nie big bang!

**Praktyczne implikacje:**
- Split 1 moduł at a time
- Parallel run old + new (compare results)
- Gradual migration (10% → 50% → 100%)

**Timeline:**
```
Week 1-2:  Phase 0 (prep)
Week 3-5:  Phase 1 (Security_Analysis split)
Week 6-7:  Phase 2 (Code_Refactoring split)
Week 8:    Phase 3 (Provenance_Secrets split)
Week 9-10: Phase 4 (IR_SBOM_Impact split)
Week 11-12: Phase 5 (Integration)
Week 13-14: Phase 6 (Rollout)
```

#### 1.1.3. Test-Driven Refactoring
**Principle:** Tests first, then refactor.

**Workflow:**
1. **Characterization tests:** Capture current behavior
2. **Refactor:** Change structure, not behavior
3. **Validation:** Compare new vs old results
4. **Enhancement:** Improve behavior (if needed)

**Example:**
```python
# 1. Characterization test (before refactoring):
def test_sast_scan_characterization():
    """Capture current behavior - regression baseline."""
    result_old = SecurityAnalysis().scan(test_project)
    save_baseline(result_old, "baseline_v1.json")

# 2. After refactoring:
def test_sast_scan_regression():
    """Ensure new implementation matches old."""
    baseline = load_baseline("baseline_v1.json")
    result_new = SASTEngine().scan(test_project)
    assert_results_equivalent(result_new, baseline)
```

#### 1.1.4. Documentation-Driven Development
**Principle:** Document architecture decisions (ADR), then implement.

**ADR Template:**
```markdown
# ADR-XXX: [Decision Title]

**Status:** Proposed | Accepted | Deprecated | Superseded

**Context:** [What is the issue we're facing?]

**Decision:** [What did we decide?]

**Consequences:** [What becomes easier/harder after this decision?]

**Alternatives Considered:** [What else did we evaluate?]
```

#### 1.1.5. Continuous Integration & Deployment
**Principle:** Każdy commit → automated validation.

**CI Pipeline:**
```
[Commit] → [Lint] → [Unit Tests] → [Integration Tests] 
       → [Security Scan] → [Performance Benchmark]
       → [Build Artifacts] → [Deploy Staging]
       → [Smoke Tests] → [Ready for Prod]
```

### 1.2. Refactoring Patterns

#### Pattern 1: Strangler Fig (dla monolitów)

**Opis:** Stopniowe zastępowanie starego systemu nowym, wrapping old functionality.

**Zastosowanie:** Security_Analysis split

**Steps:**
1. **Create new module** (np. SAST_Engine)
2. **Implement interface** (ISASTScanner)
3. **Wrapper in old module** - forwarding calls
4. **Feature flag** - switch between old/new
5. **Gradual migration** - consumers move to new API
6. **Deprecate old** - after 100% migration
7. **Remove old** - cleanup

**Code Example:**
```python
# Step 3: Wrapper w Security_Analysis (old):
from sast_engine import SASTEngine  # new module

class SecurityAnalysis:
    def scan_sast(self, path):
        if FEATURE_FLAG_NEW_SAST:
            # Nowy sposób:
            engine = SASTEngine()
            return engine.scan(path)
        else:
            # Stary sposób (deprecated):
            return self._legacy_sast_scan(path)
```

#### Pattern 2: Branch by Abstraction

**Opis:** Interface-first, then switch implementations.

**Zastosowanie:** Wszystkie inter-module dependencies

**Steps:**
1. **Define interface** (Protocol)
2. **Old implementation** implements interface
3. **New implementation** implements interface
4. **Consumers** use interface (not implementation)
5. **Switch** implementation via DI

**Code Example:**
```python
# Step 1: Interface
from typing import Protocol

class ISBOMProvider(Protocol):
    def generate_sbom(self, path: Path) -> dict: ...

# Step 2: Old impl
class LegacySBOMGenerator:
    def generate_sbom(self, path): ...  # old way

# Step 3: New impl
class SBOMGenerator:
    def generate_sbom(self, path): ...  # new way

# Step 4: Consumer
class SCAEngine:
    def __init__(self, sbom_provider: ISBOMProvider):
        self._sbom = sbom_provider  # DI - don't care which impl
    
    def scan(self, path):
        sbom = self._sbom.generate_sbom(path)
        ...

# Step 5: Switch (via config/DI container)
if USE_NEW_SBOM:
    provider = SBOMGenerator()
else:
    provider = LegacySBOMGenerator()

scanner = SCAEngine(sbom_provider=provider)
```

#### Pattern 3: Extract Module

**Opis:** Wydzielanie funkcjonalności do nowego modułu.

**Steps:**
1. **Identify cohesive subset** of code
2. **Create new module skeleton**
3. **Copy code** (don't move yet!)
4. **Adapt to new structure** (Clean Architecture)
5. **Tests** - parity with old
6. **Parallel run** - validate
7. **Switch consumers** to new module
8. **Delete old code**

---

## 2. GOVERNANCE I ROLE

### 2.1. Role i Odpowiedzialności

| Rola | Osoba/Zespół | Odpowiedzialność | Czas |
|------|--------------|------------------|------|
| **Transformation Lead** | [Osoba] | Overall coordination, decisions | 100% |
| **Architect** | [Osoba] | Architecture design, ADRs, reviews | 75% |
| **Module Owners** | [Zespoły] | Implementation, testing, docs | 100% |
| **QA Lead** | [Osoba] | Test strategy, validation | 50% |
| **Security Lead** | [Osoba] | CVE patches, security reviews | 50% |
| **DevOps Lead** | [Osoba] | CI/CD, deployment, monitoring | 75% |
| **Tech Writer** | [Osoba] | Documentation, templates | 50% |

### 2.2. Decision-Making Process

**Types of Decisions:**

1. **Architectural (ADR required):**
   - Approval: Architect + Transformation Lead
   - Process: Proposal → Review → Decision → Document ADR
   - Example: "Split Security_Analysis into 4 modules"

2. **Implementation:**
   - Approval: Module Owner + Architect review
   - Process: Design doc → Review → Implement
   - Example: "Use libcst for Python AST parsing"

3. **Operational:**
   - Approval: DevOps Lead
   - Process: RFC → Review → Approve
   - Example: "Use Prometheus for metrics"

**Escalation:**
- Module Owner → Architect → Transformation Lead → Stakeholders

### 2.3. Communication Channels

| Channel | Frequency | Attendees | Purpose |
|---------|-----------|-----------|---------|
| **Daily Standup** | Daily, 15 min | All devs | Blockers, progress |
| **Architecture Review** | 2×/week, 1h | Architect, leads | Design decisions |
| **Demo** | Weekly, 30 min | All + stakeholders | Show progress |
| **Retrospective** | Bi-weekly, 1h | All devs | Process improvement |
| **Slack #refactoring** | Async | All | Quick questions |

---

## 3. PROCES KROK PO KROKU

### 3.1. PHASE 0: Przygotowanie (Week 1-2)

**Cele:**
- ✅ Patch critical CVE
- ✅ Setup infrastructure (observability, CI/CD)
- ✅ Define wszystkie interfaces
- ✅ Create SHARED_RESOURCES skeleton

#### Task 0.1: Emergency CVE Patches

**Owner:** Security Team  
**Duration:** 2 dni  
**Priority:** P0 Critical

**Steps:**
1. **Audit dependencies:**
   ```bash
   npm audit
   pip-audit
   ```

2. **Patch Critical CVE:**
   - S-001: `semgrep 1.45.0 → 1.50.0+`
   - S-002: `node-sass 8.0 → 9.0+`

3. **Test regression:**
   ```bash
   pytest tests/security/
   npm test
   ```

4. **Deploy patch:**
   - Staging → Smoke tests → Production

**Acceptance Criteria:**
- [ ] 0 Critical CVE
- [ ] All tests pass
- [ ] No performance degradation

#### Task 0.2: Observability Stack Setup

**Owner:** DevOps Team  
**Duration:** 1 tydzień  
**Priority:** P0

**Steps:**
1. **Prometheus + Grafana:**
   ```yaml
   # docker-compose.yml
   services:
     prometheus:
       image: prom/prometheus
       volumes:
         - ./prometheus.yml:/etc/prometheus/prometheus.yml
     grafana:
       image: grafana/grafana
   ```

2. **OpenTelemetry instrumentation:**
   ```python
   from opentelemetry import trace
   from opentelemetry.sdk.trace import TracerProvider
   
   trace.set_tracer_provider(TracerProvider())
   tracer = trace.get_tracer(__name__)
   ```

3. **Dashboards:**
   - Overview dashboard (all modules)
   - Per-module dashboards
   - SLO tracking

**Acceptance Criteria:**
- [ ] Metrics flowing to Prometheus
- [ ] Traces visible in Jaeger
- [ ] Dashboards operational
- [ ] Alerts configured

#### Task 0.3: Interfaces Definition

**Owner:** Architect + Module Owners  
**Duration:** 1 tydzień  
**Priority:** P0

**Steps:**
1. **Create `shared_resources/interfaces/`:**
   ```python
   # shared_resources/interfaces/scanner_protocol.py
   from typing import Protocol, List
   from pathlib import Path
   
   class ISASTScanner(Protocol):
       def scan(self, path: Path, config: dict) -> ScanResult: ...
       def get_supported_languages(self) -> List[str]: ...
   
   class ISCAScanner(Protocol):
       def scan_dependencies(self, sbom: dict) -> List[Vulnerability]: ...
   
   class ISBOMProvider(Protocol):
       def generate_sbom(self, path: Path, format: str) -> dict: ...
   
   # etc. for all inter-module dependencies
   ```

2. **Document contracts:**
   - Input/output schemas
   - Error handling
   - Performance guarantees (SLA)

**Acceptance Criteria:**
- [ ] All interfaces defined (minimum 10)
- [ ] JSON schemas for data types
- [ ] Contract documentation complete

#### Task 0.4: SHARED_RESOURCES Creation

**Owner:** Architect Team  
**Duration:** 3 dni  
**Priority:** P1

**Steps:**
1. **Create structure:**
   ```bash
   mkdir -p SHARED_RESOURCES/{metadata,schemas,examples,interfaces,utils}
   ```

2. **Extract metadata** from Security_Analysis:
   ```bash
   mv Security_Analysis/L1_FAZA0/metadata/normalized/* \
      SHARED_RESOURCES/metadata/
   ```

3. **Version control:**
   ```toml
   # SHARED_RESOURCES/pyproject.toml
   [project]
   name = "shared-resources"
   version = "0.1.0"
   ```

**Acceptance Criteria:**
- [ ] Structure created
- [ ] Metadata extracted (8 MB)
- [ ] README.md z usage guidelines
- [ ] Versioned (semver)

#### Task 0.5: CI/CD Per-Module Pipelines

**Owner:** DevOps Team  
**Duration:** 1 tydzień  
**Priority:** P1

**Steps:**
1. **Monorepo detection:**
   ```yaml
   # .github/workflows/ci.yml
   on:
     pull_request:
       paths:
         - 'SAST_Engine/**'
         - 'SCA_Engine/**'
   
   jobs:
     detect-changes:
       outputs:
         modules: ${{ steps.changes.outputs.modules }}
     
     test-module:
       needs: detect-changes
       strategy:
         matrix:
           module: ${{ fromJson(needs.detect-changes.outputs.modules) }}
       steps:
         - run: pytest ${{ matrix.module }}/tests/
   ```

2. **Per-module versioning:**
   - Semantic versioning
   - Automated changelog generation

**Acceptance Criteria:**
- [ ] CI runs only for changed modules
- [ ] Per-module test isolation
- [ ] Versioning automated

---

### 3.2. PHASE 1: Security_Analysis Split (Week 3-5)

**Cel:** 1 moduł (48 MB) → 4 moduły (SAST_Engine, SCA_Engine, Secrets_Scanner, FixOps)

**Owner:** Security Team (4 devs)  
**Duration:** 3 tygodnie  
**Priority:** P0

#### Task 1.1: SAST_Engine Extraction

**Substeps:**

**1.1.1. Create Module Skeleton (Day 1)**
```bash
mkdir -p SAST_Engine/{src,tests,docs,config,schemas}
cd SAST_Engine

# Structure per standard (→ TO-BE section 1.4)
mkdir -p src/{core,domain,interfaces,adapters,api,utils}
mkdir -p tests/{unit,integration,e2e,fixtures}
mkdir -p docs/{decisions,diagrams,guides}
```

**1.1.2. Copy SAST Code (Day 1-2)**
```bash
# Copy existing code
cp -r ../Security_Analysis/sast/* src/

# Organize per Clean Architecture:
# - Domain models → src/domain/
# - Use cases → src/core/
# - Semgrep/CodeQL adapters → src/adapters/
# - Public API → src/api/
```

**1.1.3. Refactor to Clean Architecture (Day 3-5)**

**Domain layer:**
```python
# src/domain/models.py
from dataclasses import dataclass
from enum import Enum

class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

@dataclass
class Finding:
    id: str
    rule_id: str
    severity: Severity
    message: str
    location: Location
    metadata: dict

@dataclass
class ScanResult:
    findings: list[Finding]
    stats: ScanStats
    metadata: dict
```

**Core (use cases):**
```python
# src/core/scanner.py
from ..domain.models import ScanResult
from ..interfaces.scanner_protocol import ISASTScanner

class SASTScanner:
    """Core SAST scanning logic."""
    
    def __init__(self, engine_adapter):
        self._engine = engine_adapter
    
    def scan(self, path: Path, config: ScanConfig) -> ScanResult:
        # 1. Validate input
        self._validate_path(path)
        
        # 2. Scan via adapter
        raw_results = self._engine.execute_scan(path, config)
        
        # 3. Transform to domain model
        findings = self._transform_results(raw_results)
        
        # 4. Return
        return ScanResult(findings=findings, ...)
```

**Adapters:**
```python
# src/adapters/semgrep.py
class SemgrepAdapter:
    """Adapter for Semgrep engine."""
    
    def execute_scan(self, path, config):
        # Call semgrep CLI
        result = subprocess.run([
            "semgrep",
            "--config", config.ruleset,
            "--json",
            str(path)
        ], capture_output=True)
        return json.loads(result.stdout)
```

**Public API:**
```python
# src/api/__init__.py
from ..core.scanner import SASTScanner
from ..domain.models import ScanResult, Finding
from ..adapters.semgrep import SemgrepAdapter

# Factory function
def create_scanner(engine="semgrep"):
    if engine == "semgrep":
        adapter = SemgrepAdapter()
    else:
        raise ValueError(f"Unknown engine: {engine}")
    
    return SASTScanner(engine_adapter=adapter)

__all__ = ["create_scanner", "ScanResult", "Finding"]
```

**1.1.4. Tests (Day 6-8)**

**Unit tests:**
```python
# tests/unit/test_scanner.py
def test_scan_validates_path():
    scanner = SASTScanner(mock_adapter)
    with pytest.raises(ValueError):
        scanner.scan(Path("/nonexistent"), config)

def test_scan_transforms_results():
    scanner = SASTScanner(mock_adapter)
    result = scanner.scan(test_project, config)
    assert isinstance(result, ScanResult)
    assert len(result.findings) > 0
```

**Integration tests:**
```python
# tests/integration/test_semgrep_adapter.py
def test_semgrep_adapter_real_scan():
    adapter = SemgrepAdapter()
    result = adapter.execute_scan(fixture_project, test_config)
    assert "results" in result
```

**Regression tests:**
```python
# tests/e2e/test_regression.py
def test_parity_with_old_security_analysis():
    """Ensure new SAST_Engine produces same results as old."""
    # Old way:
    old_result = SecurityAnalysis().scan_sast(test_project)
    
    # New way:
    new_scanner = create_scanner()
    new_result = new_scanner.scan(test_project, default_config)
    
    # Compare:
    assert_findings_equivalent(old_result, new_result)
```

**1.1.5. Documentation (Day 9)**

```markdown
# SAST_Engine/README.md

## Overview
SAST_Engine provides static application security testing.

## Quick Start
\`\`\`python
from sast_engine import create_scanner

scanner = create_scanner(engine="semgrep")
result = scanner.scan(Path("./src"), config)

for finding in result.findings:
    print(f"{finding.severity}: {finding.message}")
\`\`\`

## API Reference
See API_REFERENCE.md

## Architecture
See ARCHITECTURE.md
```

**1.1.6. Wrapper in Old Module (Day 10)**

```python
# Security_Analysis/sast_wrapper.py
from sast_engine import create_scanner

class SecurityAnalysis:
    def scan_sast(self, path):
        if FEATURE_FLAG_NEW_SAST:
            # Route to new module:
            scanner = create_scanner()
            return scanner.scan(path, self._get_config())
        else:
            # Old implementation (deprecated):
            return self._legacy_sast_scan(path)
```

**1.1.7. Validation & Rollout (Day 11-15)**

**Parallel run (Week 3):**
```python
# CI: Run both old and new, compare results
old_result = legacy_scan()
new_result = new_scan()

if not results_match(old_result, new_result):
    alert_team()
    investigate_difference()
```

**Gradual rollout (Week 4-5):**
- Week 4: 10% traffic → new module
- Week 5: 50% traffic → new module
- End Week 5: 100% → new module

**Acceptance Criteria:**
- [ ] SAST_Engine module created (~12 MB)
- [ ] Clean Architecture structure
- [ ] Test coverage > 85%
- [ ] Regression tests pass (100% parity)
- [ ] Documentation complete
- [ ] Parallel run successful (1 week)
- [ ] 100% traffic routed to new module
- [ ] Performance: < 30s avg (vs 45s old)

#### Task 1.2: SCA_Engine Extraction

[Analogiczny proces jak 1.1, duration: 3 tygodnie]

**Key differences:**
- Dependencies: `ISBOMProvider` interface (DI)
- External APIs: OSV, NVD, npm audit
- Output: Vulnerability list + CVSS scores

#### Task 1.3: Secrets_Scanner Extraction

[Analogiczny proces, duration: 2 tygodnie]

**Key differences:**
- Pattern-based detection
- Entropy analysis
- Git history scanning

#### Task 1.4: FixOps Extraction

[Analogiczny proces, duration: 3 tygodnie]

**Key differences:**
- Aggregates findings from SAST + SCA + Secrets
- Ranking algorithm
- Fix proposal generation

#### Task 1.5: Deprecate Security_Analysis

**Steps:**
1. **Deprecation notice:**
   ```python
   # Security_Analysis/__init__.py
   import warnings
   
   warnings.warn(
       "Security_Analysis is deprecated. "
       "Use SAST_Engine, SCA_Engine, Secrets_Scanner, FixOps instead.",
       DeprecationWarning
   )
   ```

2. **Update consumers:**
   ```python
   # Platform_Tools migration:
   # Old:
   from security_analysis import SecurityAnalysis
   scanner = SecurityAnalysis()
   
   # New:
   from sast_engine import create_scanner
   scanner = create_scanner()
   ```

3. **Remove old code (after 1 release cycle):**
   ```bash
   git rm -r Moduły/Security_Analysis/sast/
   git rm -r Moduły/Security_Analysis/sca/
   # Keep wrapper for 2 releases, then remove completely
   ```

**Acceptance Criteria:**
- [ ] All consumers migrated
- [ ] Deprecation warnings logged
- [ ] Old code removed (or scheduled for removal)

---

### 3.3. PHASE 2: Code_Refactoring Split (Week 6-7)

[Analogiczny proces jak Phase 1]

**Modules created:**
- Core_Engine
- Language_Adapters
- Impact_Planner

**Duration:** 2 tygodnie (mniejszy moduł: 4.6 MB vs 48 MB)

---

### 3.4. PHASE 3: Provenance_Secrets Split (Week 8)

[Analogiczny proces]

**Modules created:**
- Provenance_Service
- Secrets_Broker

**Duration:** 1 tydzień

---

### 3.5. PHASE 4: IR_SBOM_Impact Split (Week 9-10)

[Analogiczny proces]

**Modules created:**
- SymbolGraph_Builder
- SBOM_Generator
- Impact_Flow

**Duration:** 2 tygodnie

---

### 3.6. PHASE 5: Integration & Validation (Week 11-12)

**Cel:** End-to-end testing nowej architektury (wszystkie 26 modułów razem)

**Owner:** QA Team + All Module Owners  
**Duration:** 2 tygodnie  
**Priority:** P0

#### Task 5.1: End-to-End Test Suite

**Scenarios:**

**E2E-001: Full Security Scan Pipeline**
```python
def test_e2e_security_pipeline():
    """Test pełnej ścieżki: SAST + SCA + Secrets + FixOps."""
    
    # 1. SAST Scan
    sast = create_scanner("semgrep")
    sast_findings = sast.scan(test_project, sast_config)
    
    # 2. SCA Scan
    sbom_gen = SBOMGenerator()
    sbom = sbom_gen.generate_sbom(test_project)
    
    sca = SCAEngine(sbom_provider=sbom_gen)
    sca_findings = sca.scan_dependencies(sbom)
    
    # 3. Secrets Scan
    secrets = SecretsScanner()
    secret_findings = secrets.scan(test_project)
    
    # 4. Aggregate & Fix
    fixops = FixOps()
    all_findings = sast_findings + sca_findings + secret_findings
    fixes = fixops.propose_fixes(all_findings)
    
    # Assertions:
    assert len(all_findings) > 0
    assert len(fixes) > 0
    assert fixes[0].priority == "HIGH"
```

**E2E-002: Refactoring Pipeline**
```python
def test_e2e_refactoring():
    """Test ścieżki refaktoringu: Symbol Graph → Impact → Refactor."""
    
    # 1. Build symbol graph
    sg_builder = SymbolGraphBuilder()
    graph = sg_builder.build(test_project)
    
    # 2. Propose refactoring
    planner = ImpactPlanner()
    plan = planner.plan_refactoring(graph, "rename_function", params)
    
    # 3. Execute refactoring
    core = CoreEngine()
    result = core.apply_refactoring(test_project, plan)
    
    # Assertions:
    assert result.success
    assert result.files_modified == expected_count
```

#### Task 5.2: Performance Benchmarks

**Baseline vs New:**

| Operation | Baseline (AS-IS) | New (TO-BE) | Target | Status |
|-----------|------------------|-------------|--------|--------|
| SAST scan (1000 files) | 45s avg | [X]s avg | < 30s | 🔄 Measure |
| SCA scan | 8s | [X]s | < 5s | 🔄 Measure |
| Symbol graph | 22s | [X]s | < 15s | 🔄 Measure |
| Canvas sync (50u) | 120ms p95 | [X]ms | < 80ms | 🔄 Measure |

**Acceptance:**
- [ ] All operations meet or exceed targets
- [ ] No regression > 10% from baseline

#### Task 5.3: Load Testing

**Scenarios:**
- Concurrent scans: 10 simultaneous SAST scans
- Canvas users: 100 concurrent users
- API throughput: 1000 req/s

**Tools:**
- Locust for load generation
- Prometheus for metrics collection

#### Task 5.4: Security Audit

**Checklist:**
- [ ] All CVE Critical patched
- [ ] RBAC implemented and tested
- [ ] PII sanitization verified (no leaks in logs)
- [ ] Secrets rotation working
- [ ] Rate limiting configured
- [ ] Input validation comprehensive

**Penetration Testing:**
- External firm (if budget allows)
- Internal security team review

#### Task 5.5: Documentation Review

**Completeness Check:**
- [ ] All 26 modules have README.md
- [ ] All 26 modules have ARCHITECTURE.md
- [ ] API_REFERENCE.md for public APIs
- [ ] Migration guides for breaking changes
- [ ] Cross-references validated

---

### 3.7. PHASE 6: Production Rollout (Week 13-14)

**Cel:** Deploy nowej architektury do production z zero downtime

**Owner:** DevOps Team + All  
**Duration:** 2 tygodnie  
**Priority:** P0

#### Task 6.1: Deployment Preparation

**Pre-deployment Checklist:**
- [ ] All E2E tests pass
- [ ] Performance benchmarks met
- [ ] Security audit complete
- [ ] Documentation complete
- [ ] Rollback plan tested
- [ ] On-call team trained
- [ ] Stakeholders notified

**Deployment Strategy:** Blue-Green

```
┌─────────────┐         ┌─────────────┐
│   Blue      │         │   Green     │
│   (Old)     │         │   (New)     │
│             │         │             │
│ 14 modules  │         │ 26 modules  │
└─────────────┘         └─────────────┘
       │                       │
       └───────────┬───────────┘
                   │
            ┌──────▼──────┐
            │  Load Bal.  │
            └─────────────┘
```

#### Task 6.2: Gradual Rollout

**Week 13:**
- **Day 1-2:** Deploy to staging → Smoke tests
- **Day 3:** Deploy to production (Green environment)
- **Day 4-5:** Route 10% traffic to Green
  - Monitor: error rate, latency, metrics
  - Compare: Blue vs Green dashboards
  
**Week 14:**
- **Day 1-2:** Route 50% traffic to Green
  - Continue monitoring
  - Incident response on standby
- **Day 3-4:** Route 100% traffic to Green
  - Blue kept running (hot standby)
- **Day 5:** Decommission Blue (if all stable)

#### Task 6.3: Monitoring & Alerting

**Critical Alerts:**
```yaml
alerts:
  - name: HighErrorRate
    condition: error_rate > 5%
    action: PagerDuty + auto-rollback
  
  - name: LatencySpike
    condition: p95_latency > SLA * 1.5
    action: PagerDuty
  
  - name: CVE Detected
    condition: critical_cve_count > 0
    action: Email + Slack
```

**Dashboards:**
- Real-time traffic split (Blue vs Green)
- Error rates per module
- Latency percentiles (p50, p95, p99)
- Resource utilization (CPU, memory)

#### Task 6.4: Rollback Procedure

**Trigger Conditions:**
- Error rate > 5% sustained for 5 min
- Critical bug discovered
- Performance degradation > 25%

**Rollback Steps:**
1. **Immediate:** Switch load balancer back to Blue (< 2 min)
2. **Verify:** Check metrics stabilize
3. **Communicate:** Notify team + stakeholders
4. **Investigate:** Root cause analysis
5. **Fix Forward:** Patch issue, re-deploy to Green
6. **Retry Rollout:** After validation

**Rollback SLA:** < 5 min (manual), < 2 min (auto)

---

## 4. RISK MANAGEMENT

### 4.1. Risk Register

| ID | Risk | Probability | Impact | Score | Mitigation |
|----|------|-------------|--------|-------|------------|
| R-001 | Regression bugs in split modules | High | High | 16 | Extensive testing, parallel run |
| R-002 | Performance degradation | Medium | High | 12 | Benchmarking, optimization budget |
| R-003 | Team overload | High | Medium | 12 | Prioritization, external help if needed |
| R-004 | Timeline slip | Medium | Medium | 9 | Buffer weeks, re-scope if needed |
| R-005 | Production incident | Low | Critical | 12 | Rollback plan, monitoring, on-call |
| R-006 | Stakeholder pushback | Low | Medium | 6 | Regular demos, early communication |
| R-007 | Incomplete migration | Medium | High | 12 | Migration tracking, forced deprecation |

### 4.2. Contingency Plans

**If timeline slips by > 2 weeks:**
- **Option A:** Reduce scope (delay non-P0 modules)
- **Option B:** Add resources (contractors)
- **Option C:** Accept delay, re-communicate timeline

**If critical bug found in production:**
- **Immediate:** Rollback to old (Blue)
- **Short-term:** Hot-fix in new (Green)
- **Long-term:** Root cause analysis + prevention

**If team capacity drops (illness, etc.):**
- **Cross-training:** Each module has 2+ knowledgeable people
- **Documentation:** Onboarding docs for rapid ramp-up
- **External:** Contractors on standby

---

## 5. QUALITY GATES

### 5.1. Per-Phase Quality Gates

**Phase 0: Preparation**
- [ ] 0 Critical CVE
- [ ] Observability stack operational
- [ ] All interfaces defined
- [ ] SHARED_RESOURCES created

**Phase 1-4: Module Splits**
- [ ] Test coverage > 85%
- [ ] Regression tests pass (100%)
- [ ] Documentation complete (README, ARCH, API)
- [ ] No performance regression > 10%
- [ ] Parallel run successful (1 week)

**Phase 5: Integration**
- [ ] All E2E tests pass
- [ ] Performance targets met
- [ ] Security audit complete
- [ ] 0 Critical issues

**Phase 6: Rollout**
- [ ] Smoke tests pass
- [ ] Canary 10% successful (stable for 24h)
- [ ] Rollback tested
- [ ] Monitoring operational

### 5.2. Definition of Done

**For each module split:**
- [x] Code refactored to Clean Architecture
- [x] Public API defined (via interface)
- [x] Unit tests (> 85% coverage)
- [x] Integration tests (> 75%)
- [x] Regression tests (parity with old)
- [x] Documentation (README, ARCHITECTURE, API_REFERENCE, CHANGELOG)
- [x] ADR if architectural decision
- [x] Peer review (2+ approvers)
- [x] Security review (if touches auth/secrets/data)
- [x] Performance benchmark (no regression)
- [x] Deployment to staging successful
- [x] Smoke tests pass

---

## 6. COMMUNICATION & REPORTING

### 6.1. Status Reporting

**Weekly Report Template:**
```markdown
# Refactoring Status - Week [N]

## Progress
- Completed: [List of tasks]
- In Progress: [Current work]
- Blocked: [Issues]

## Metrics
| Metric | Last Week | This Week | Target | Status |
|--------|-----------|-----------|--------|--------|
| Modules Completed | X | Y | 26 | [%] |
| Test Coverage | X% | Y% | >85% | [status] |
| CVE Critical | X | Y | 0 | [status] |

## Risks
- [New/updated risks]

## Next Week
- [Planned work]
```

**Recipients:**
- Stakeholders (exec summary)
- All team (full report)
- Archive (for retrospective)

### 6.2. Demo Schedule

**Bi-weekly Demos:**
- **Audience:** Stakeholders, team, interested parties
- **Duration:** 30 min
- **Content:**
  - What we built (demo)
  - Metrics progress
  - Challenges & solutions
  - Next steps

---

## 7. POST-REFACTORING

### 7.1. Retrospective

**After Phase 6 completion:**

**Agenda:**
1. **What went well?** (celebrate successes)
2. **What didn't go well?** (learn from failures)
3. **What should we do differently next time?**

**Output:** Lessons Learned document

### 7.2. Technical Debt Tracking

**After refactoring, track new debt:**
- Monthly SonarQube scans
- Quarterly architecture reviews
- Continuous dependency updates

**Goal:** Prevent debt from accumulating again!

### 7.3. Continuous Improvement

**Ongoing:**
- Performance monitoring (catch regressions early)
- Security scans (new CVE)
- User feedback (is new architecture better for devs?)

---

## ZAŁĄCZNIKI

### A. ADR Index

Lista wszystkich Architecture Decision Records:
- ADR-001: Split Security_Analysis into 4 modules
- ADR-002: Use Dependency Inversion for all inter-module deps
- ADR-003: Adopt Clean Architecture pattern
- [etc.]

### B. Migration Scripts

Przykładowe skrypty do migracji:
```python
# migrate_consumers.py
"""Auto-update import statements from old to new modules."""

import re
from pathlib import Path

def migrate_file(file_path):
    content = file_path.read_text()
    
    # Old → New mapping
    replacements = {
        "from security_analysis import SecurityAnalysis":
            "from sast_engine import create_scanner",
        "SecurityAnalysis().scan_sast":
            "create_scanner().scan",
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    file_path.write_text(content)

# Run on all Python files
for file in Path("./").rglob("*.py"):
    migrate_file(file)
```

### C. Rollback Runbook

**Emergency Rollback Procedure:**

1. **Assess situation** (< 1 min)
   - Check error rate dashboard
   - Check alerts
   - Decision: rollback? or investigate?

2. **Execute rollback** (< 2 min)
   ```bash
   # Switch load balancer to Blue
   kubectl patch service api-gateway -p '{"spec":{"selector":{"version":"blue"}}}'
   
   # Verify traffic routed
   curl http://api-gateway/health
   ```

3. **Verify stability** (5 min)
   - Check error rate drops
   - Check metrics stabilize

4. **Communicate** (< 5 min)
   - Slack: "#incidents - Rolled back to Blue due to [reason]"
   - PagerDuty: Update incident

5. **Investigate** (async)
   - Logs analysis
   - Root cause
   - Fix

---

## CHECKLIST KOMPLETNOŚCI

- [x] Executive Summary (goals, timeline, dashboard)
- [x] Zasady procesu (principles, patterns)
- [x] Governance (roles, decision-making, communication)
- [x] Proces krok po kroku (Phase 0-6, detailed steps)
- [x] Risk management (register, contingencies)
- [x] Quality gates (per-phase, definition of done)
- [x] Communication & Reporting (status, demos)
- [x] Post-refactoring (retrospective, debt tracking)
- [x] Załączniki (ADRs, scripts, runbooks)
- [x] Cross-references (TO-BE, PROBLEMY, AS-IS)
