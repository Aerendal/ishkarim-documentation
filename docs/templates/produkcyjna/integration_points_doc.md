# Punkty Integracji Między Modułami

> **Framework:** arc42 (Rozdział 6: Runtime View + Interfaces) + API Design Best Practices  
> **Data opracowania:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół]  
> **Status:** [Draft/Review/Approved]  
> **Powiązane:** ← `02_TO_BE`, → `04_PROCES_REFAKTORYZACJI`, ← `03_PROBLEMY_I_BŁĘDY`

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: TO-BE-ARCHITECTURE
    type: interface_requirements
    from_sections:
      - module_boundaries
      - communication_patterns
    to_sections:
      - interface_definitions
      - contract_specifications
    influence: "TO-BE definiuje jak moduły się komunikują"
    when:
      condition: architecture.is_modular == true
      applies: always

  - id: AS-IS-ARCHITECTURE
    type: current_integration
    from_sections:
      - existing_interfaces
      - coupling_analysis
    to_sections:
      - integration_gaps
      - improvement_areas
    influence: "AS-IS pokazuje obecne punkty integracji"
    when:
      condition: analysis.includes_as_is == true
      applies: conditionally
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: API-DOCUMENTATION
    type: interface_specs
    from_sections:
      - interface_catalog
      - contract_definitions
    to_sections:
      - api_reference
      - usage_examples
    influence: "Punkty integracji generują dokumentację API"
    when:
      condition: interfaces.defined == true
      applies: always

  - id: CONTRACT-TESTS
    type: quality_assurance
    from_sections:
      - interface_contracts
      - data_schemas
    to_sections:
      - test_specifications
      - validation_rules
    influence: "Kontrakty wymagają testów kontraktowych"
    when:
      condition: contracts.require_testing == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: API-VERSIONING-POLICY
    relationship: compatibility_rules
    sections_mapping:
      - from: versioning_strategy
        to: interface_evolution
    usage: "Polityka wersjonowania określa ewolucję interfejsów"
```

### Satellite Documents

```yaml
satellites:
  - name: OPENAPI-SPECIFICATIONS
    purpose: "Specyfikacje OpenAPI dla REST API"
    trigger: per_interface
    lifecycle: continuous
    retention: permanent
```

---

## EXECUTIVE SUMMARY

### Cel Dokumentu
[Dlaczego dokumentujemy punkty integracji - zapewnienie loose coupling, contract-based collaboration, 2-3 zdania]

### Zakres

**Co dokumentujemy:**
- **Interfejsy** (APIs, Protocols) między modułami
- **Kontrakty danych** (schemas, formats)
- **Mechanizmy komunikacji** (sync, async, events)
- **SLA i Performance Guarantees**
- **Versioning i Backward Compatibility**

### Integration Dashboard

| Metryka | Wartość | Target | Status |
|---------|---------|--------|--------|
| **Liczba interfejsów** | [N] | [N docelowa] | 🔄 |
| **Interfejsy zdefiniowane** | [X] | 100% | 🔄 |
| **Contract tests** | [Y%] | 100% | 🔄 |
| **Breaking changes** | [Z] | 0 | 🔄 |
| **Documentation coverage** | [W%] | 100% | 🔄 |

### Kluczowe Integracje (Top 10)

| Rank | Consumer | Provider | Interface | Type | Criticality | Status |
|------|----------|----------|-----------|------|-------------|--------|
| 1 | FixOps | SAST_Engine | ISASTScanner | Sync | Critical | ✅ Defined |
| 2 | FixOps | SCA_Engine | ISCAScanner | Sync | Critical | ✅ Defined |
| 3 | SCA_Engine | SBOM_Generator | ISBOMProvider | Sync | High | ✅ Defined |
| 4 | Impact_Flow | SymbolGraph_Builder | IGraphBuilder | Sync | High | ✅ Defined |
| 5 | Platform_Tools | SAST_Engine | ISASTScanner | Sync | Medium | ✅ Defined |
| ... | ... | ... | ... | ... | ... | ... |

---

## 1. ZASADY INTEGRACJI

### 1.1. Fundamentalne Zasady

#### 1.1.1. Contract-First Design
**Principle:** Najpierw definicja kontraktu (interface), potem implementacja.

**Workflow:**
1. **Define Interface** (Protocol/Abstract Base Class)
2. **Document Contract** (inputs, outputs, errors, SLA)
3. **Implement Provider** (module providing functionality)
4. **Implement Consumer** (module using functionality)
5. **Contract Tests** (verify both sides honor contract)

**Example:**
```python
# Step 1: Define Interface
from typing import Protocol
from pathlib import Path

class ISASTScanner(Protocol):
    """Contract for SAST scanning services."""
    
    def scan(self, path: Path, config: ScanConfig) -> ScanResult:
        """Scan source code for security vulnerabilities.
        
        Args:
            path: Path to source code directory
            config: Scan configuration (rules, options)
        
        Returns:
            ScanResult containing findings
        
        Raises:
            ValueError: If path doesn't exist or is not a directory
            TimeoutError: If scan exceeds configured timeout
        
        Performance SLA:
            - < 30s average for 1000 files
            - < 512 MB memory usage
        """
        ...
    
    def get_supported_languages(self) -> list[str]:
        """Returns list of supported programming languages.
        
        Returns:
            List of language names (e.g., ["python", "javascript"])
        """
        ...
```

#### 1.1.2. Dependency Inversion
**Principle:** High-level modules zależą od abstrakcji, nie od konkretnych implementacji.

```python
# ✗ BAD - Direct dependency:
from sast_engine import SASTEngine  # concrete implementation

class FixOps:
    def __init__(self):
        self._sast = SASTEngine()  # tight coupling!

# ✓ GOOD - Dependency Inversion:
from interfaces import ISASTScanner  # abstraction

class FixOps:
    def __init__(self, sast_scanner: ISASTScanner):
        self._sast = sast_scanner  # DI - loose coupling!

# Usage (DI Container):
from sast_engine import create_scanner

scanner = create_scanner()  # concrete impl
fixops = FixOps(sast_scanner=scanner)  # injected
```

#### 1.1.3. Versioned Interfaces
**Principle:** Wszystkie publiczne API mają wersje (semantic versioning).

**Versioning Rules:**
- **MAJOR:** Breaking changes (remove methods, change signatures)
- **MINOR:** Backward-compatible additions (new methods, optional params)
- **PATCH:** Bug fixes (no API changes)

**Example:**
```python
# sast_engine v1.0.0
class ISASTScanner(Protocol):
    def scan(self, path: Path) -> ScanResult: ...

# sast_engine v1.1.0 (MINOR - backward compatible)
class ISASTScanner(Protocol):
    def scan(self, path: Path, config: ScanConfig = None) -> ScanResult: ...
    def scan_incremental(self, changes: ChangeSet) -> ScanResult: ...  # NEW

# sast_engine v2.0.0 (MAJOR - breaking change)
class ISASTScanner(Protocol):
    def scan(self, request: ScanRequest) -> ScanResult: ...  # CHANGED signature
```

**Compatibility Policy:**
- Minimum 2 MAJOR versions supported concurrently
- Deprecation warnings 1 version ahead
- Migration guide dla breaking changes

#### 1.1.4. Fail-Safe Integration
**Principle:** Failures w jednym module nie crashują innych.

**Patterns:**
- **Circuit Breaker:** Stop calling failing service
- **Timeouts:** Don't wait forever
- **Fallbacks:** Graceful degradation
- **Error Handling:** Clear error messages, no leaks

**Example:**
```python
from circuitbreaker import circuit

class ResilientSCAClient:
    @circuit(failure_threshold=5, recovery_timeout=60)
    def scan_dependencies(self, sbom):
        try:
            result = self._sca_engine.scan(sbom, timeout=30)
            return result
        except TimeoutError:
            logger.warning("SCA scan timed out, using cached results")
            return self._get_cached_results(sbom)
        except Exception as e:
            logger.error(f"SCA scan failed: {e}")
            # Return empty result instead of crashing
            return ScanResult(findings=[], status="error")
```

#### 1.1.5. Observable Integration
**Principle:** Wszystkie inter-module calls są monitorowane (metrics, tracing).

**Instrumentation:**
```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class SASTClient:
    def scan(self, path):
        with tracer.start_as_current_span(
            "sast.scan",
            attributes={"file_count": count_files(path)}
        ) as span:
            try:
                result = self._engine.scan(path)
                span.set_attribute("findings_count", len(result.findings))
                return result
            except Exception as e:
                span.record_exception(e)
                raise
```

### 1.2. Communication Patterns

#### Pattern 1: Synchronous Request-Response
**Use Case:** Immediate result needed

**Example:** SAST scan

```python
# Synchronous call:
scanner = create_scanner()
result = scanner.scan(path)  # Blocks until complete
process_results(result)
```

**Pros:** Simple, easy to reason about  
**Cons:** Caller blocked, doesn't scale for long operations

#### Pattern 2: Asynchronous (Callbacks/Promises)
**Use Case:** Non-blocking operations

**Example:** Long-running analysis

```python
# Async/await:
async def run_analysis():
    scanner = create_async_scanner()
    result = await scanner.scan(path)  # Non-blocking
    return result
```

**Pros:** Non-blocking, better resource utilization  
**Cons:** More complex error handling

#### Pattern 3: Event-Driven (Publish-Subscribe)
**Use Case:** One-to-many notifications, loose coupling

**Example:** Scan completed event

```python
# Publisher (SAST_Engine):
from events import EventBus

bus = EventBus()
result = scanner.scan(path)
bus.publish("sast.scan.completed", ScanCompletedEvent(result=result))

# Subscriber (FixOps):
bus.subscribe("sast.scan.completed", on_scan_completed)

def on_scan_completed(event):
    findings = event.result.findings
    # Generate fixes
```

**Pros:** Decoupled, extensible (add subscribers without changing publisher)  
**Cons:** Harder to trace, eventual consistency

#### Pattern 4: Shared Data (Files/Database)
**Use Case:** Large data transfer, audit trail

**Example:** SBOM shared via file

```python
# Producer (SBOM_Generator):
sbom = generate_sbom(path)
with open("artifacts/sbom.json", "w") as f:
    json.dump(sbom, f)

# Consumer (SCA_Engine):
with open("artifacts/sbom.json") as f:
    sbom = json.load(f)
result = scan_dependencies(sbom)
```

**Pros:** Simple, persistent, large data OK  
**Cons:** Coupling via file format, no real-time

---

## 2. KATALOG INTERFEJSÓW

### Format Opisu Interfejsu:

**ID:** INT-XXX  
**Nazwa:** [Nazwa interfejsu]  
**Provider:** [Moduł dostarczający]  
**Consumers:** [Lista modułów używających]  
**Type:** Sync | Async | Event | Data  
**Criticality:** Critical | High | Medium | Low  
**Version:** [X.Y.Z]  
**Status:** Defined | Implemented | Tested | Deprecated

**Opis:**
[Co robi ten interfejs - 2-3 zdania]

**Methods/Operations:**
[Lista metod z signatures]

**Data Contracts:**
[Input/output schemas]

**Error Handling:**
[Jakie błędy, jak obsługiwane]

**Performance SLA:**
[Latency, throughput, resource limits]

**Versioning:**
[Compatibility policy]

**Examples:**
[Przykłady użycia]

**Tests:**
[Contract tests location]

**References:**
- Code: `path/to/interface.py`
- Tests: `path/to/contract_tests.py`
- Docs: Link to API reference

---

### 2.1. INT-001: ISASTScanner

**Provider:** SAST_Engine  
**Consumers:** FixOps, Platform_Tools, CICD_Tooling  
**Type:** Synchronous Request-Response  
**Criticality:** Critical  
**Version:** 1.0.0  
**Status:** ✅ Defined

**Opis:**
Interfejs dla statycznej analizy bezpieczeństwa kodu (SAST). Pozwala na skanowanie kodu źródłowego pod kątem luk security (SQL injection, XSS, etc.).

**Methods:**

```python
from typing import Protocol, List
from pathlib import Path

class ISASTScanner(Protocol):
    """SAST scanning interface."""
    
    def scan(self, path: Path, config: ScanConfig) -> ScanResult:
        """Scan source code for security vulnerabilities.
        
        Args:
            path: Path to source code directory (must exist)
            config: Scan configuration
        
        Returns:
            ScanResult with findings
        
        Raises:
            ValueError: Invalid path or config
            TimeoutError: Scan exceeded timeout
            EngineError: Scanner engine failed
        
        SLA:
            - Latency: < 30s avg for 1000 files
            - Memory: < 512 MB
            - CPU: < 400% (multi-core)
        """
        ...
    
    def get_supported_languages(self) -> List[str]:
        """Returns list of supported languages.
        
        Returns:
            Language names: ["python", "javascript", "typescript", ...]
        """
        ...
    
    def validate_config(self, config: ScanConfig) -> bool:
        """Validate scan configuration.
        
        Args:
            config: Configuration to validate
        
        Returns:
            True if valid, False otherwise
        """
        ...
```

**Data Contracts:**

**ScanConfig:**
```json
{
  "type": "object",
  "properties": {
    "rules": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Rule IDs to run (e.g., ['sql-injection', 'xss'])"
    },
    "severity_threshold": {
      "type": "string",
      "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
      "default": "MEDIUM"
    },
    "timeout": {
      "type": "integer",
      "default": 60,
      "description": "Timeout in seconds"
    },
    "exclude_paths": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Glob patterns to exclude"
    }
  },
  "required": ["rules"]
}
```

**ScanResult:**
```json
{
  "type": "object",
  "properties": {
    "findings": {
      "type": "array",
      "items": {"$ref": "#/definitions/Finding"}
    },
    "stats": {
      "type": "object",
      "properties": {
        "files_scanned": {"type": "integer"},
        "duration_seconds": {"type": "number"},
        "rules_executed": {"type": "integer"}
      }
    },
    "metadata": {
      "type": "object",
      "properties": {
        "scanner_version": {"type": "string"},
        "scan_id": {"type": "string"}
      }
    }
  }
}
```

**Finding:**
```json
{
  "type": "object",
  "properties": {
    "id": {"type": "string", "format": "uuid"},
    "rule_id": {"type": "string"},
    "severity": {"enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"]},
    "message": {"type": "string"},
    "location": {
      "type": "object",
      "properties": {
        "file": {"type": "string"},
        "line": {"type": "integer"},
        "column": {"type": "integer"}
      }
    },
    "metadata": {"type": "object"}
  },
  "required": ["id", "rule_id", "severity", "message", "location"]
}
```

**Error Handling:**

| Error Type | When | HTTP Status (if REST) | Recovery |
|------------|------|----------------------|----------|
| `ValueError` | Invalid path/config | 400 Bad Request | Fix input |
| `TimeoutError` | Scan > timeout | 408 Timeout | Increase timeout or reduce scope |
| `EngineError` | Scanner failed | 500 Internal Error | Retry, check logs |
| `NotImplementedError` | Unsupported language | 501 Not Implemented | Use different scanner |

**Performance SLA:**

| Metric | Value | Percentile | Breach Action |
|--------|-------|------------|---------------|
| Latency | < 30s | p95 | Alert if > 40s |
| Latency | < 20s | p50 | - |
| Memory | < 512 MB | max | Kill if > 1 GB |
| CPU | < 400% | avg | - |
| Throughput | > 20 scans/min | - | Scale if needed |

**Versioning:**

**Current:** v1.0.0

**Roadmap:**
- v1.1.0: Add `scan_incremental(changes)` method (MINOR)
- v1.2.0: Add async variant `scan_async()` (MINOR)
- v2.0.0: Change `scan()` to accept `ScanRequest` object (MAJOR - breaking)

**Compatibility:**
- v1.x supported until 2026-01-01
- v2.0 migration guide available at `docs/migrations/v1-to-v2.md`

**Examples:**

**Basic scan:**
```python
from sast_engine import create_scanner, ScanConfig

scanner = create_scanner()
config = ScanConfig(rules=["sql-injection", "xss"])
result = scanner.scan(Path("./src"), config)

for finding in result.findings:
    print(f"{finding.severity}: {finding.message} at {finding.location.file}:{finding.location.line}")
```

**With error handling:**
```python
try:
    result = scanner.scan(path, config)
except ValueError as e:
    logger.error(f"Invalid input: {e}")
except TimeoutError:
    logger.warning("Scan timed out, partial results may be available")
except EngineError as e:
    logger.critical(f"Scanner failed: {e}")
    raise
```

**Tests:**

**Contract Test (Consumer side - FixOps):**
```python
# tests/integration/test_sast_contract.py
from fixops import FixOps
from sast_engine import create_scanner

def test_fixops_uses_sast_contract():
    """Verify FixOps correctly uses ISASTScanner contract."""
    scanner = create_scanner()
    fixops = FixOps(sast_scanner=scanner)
    
    result = fixops.generate_fixes(test_project)
    
    # Assert ISASTScanner was called correctly:
    assert scanner.scan.called
    assert isinstance(scanner.scan.call_args[0], Path)
    assert isinstance(scanner.scan.call_args[1], ScanConfig)
```

**Contract Test (Provider side - SAST_Engine):**
```python
# SAST_Engine/tests/contract/test_interface.py
from sast_engine import create_scanner

def test_sast_engine_implements_contract():
    """Verify SAST_Engine honors ISASTScanner contract."""
    scanner = create_scanner()
    
    # Test scan() returns ScanResult:
    result = scanner.scan(test_path, test_config)
    assert hasattr(result, 'findings')
    assert hasattr(result, 'stats')
    
    # Test get_supported_languages() returns list[str]:
    langs = scanner.get_supported_languages()
    assert isinstance(langs, list)
    assert all(isinstance(lang, str) for lang in langs)
```

**References:**
- **Interface Definition:** `shared_resources/interfaces/scanner_protocol.py`
- **Provider Implementation:** `SAST_Engine/src/api/__init__.py`
- **JSON Schema:** `shared_resources/schemas/scan_result.schema.json`
- **Contract Tests:** `tests/contracts/test_sast_scanner.py`
- **API Documentation:** `SAST_Engine/API_REFERENCE.md`

---

### 2.2. INT-002: ISCAScanner

**Provider:** SCA_Engine  
**Consumers:** FixOps, Platform_Tools  
**Type:** Synchronous  
**Criticality:** Critical  
**Version:** 1.0.0  
**Status:** ✅ Defined

**Opis:**
Interfejs dla Software Composition Analysis (SCA). Skanuje zależności projektu vs bazy CVE, wykrywa znane luki w bibliotekach.

**Methods:**

```python
class ISCAScanner(Protocol):
    """SCA scanning interface."""
    
    def scan_dependencies(
        self,
        sbom: dict,
        config: SCAConfig
    ) -> SCAResult:
        """Scan dependencies for known vulnerabilities.
        
        Args:
            sbom: Software Bill of Materials (CycloneDX or SPDX format)
            config: SCA configuration
        
        Returns:
            SCAResult with vulnerabilities found
        
        Raises:
            ValueError: Invalid SBOM format
            NetworkError: Cannot reach CVE databases
        
        SLA:
            - Latency: < 5s avg
            - Memory: < 128 MB
        """
        ...
    
    def get_cve_details(self, cve_id: str) -> CVEInfo:
        """Get detailed information about a CVE.
        
        Args:
            cve_id: CVE identifier (e.g., "CVE-2024-12345")
        
        Returns:
            CVEInfo with details
        
        Raises:
            NotFoundError: CVE not found
        """
        ...
```

[Analogiczny format jak INT-001: Data Contracts, Error Handling, Performance SLA, Examples, Tests, References]

---

### 2.3. INT-003: ISBOMProvider

**Provider:** SBOM_Generator  
**Consumers:** SCA_Engine, Platform_Tools  
**Type:** Synchronous  
**Criticality:** High  
**Version:** 1.0.0  
**Status:** ✅ Defined

**Opis:**
Interfejs dla generowania Software Bill of Materials (SBOM). Tworzy katalog wszystkich zależności projektu w standardowych formatach (CycloneDX, SPDX).

[Analogiczny format]

---

### 2.4. INT-004: ISymbolGraphBuilder

**Provider:** SymbolGraph_Builder  
**Consumers:** Impact_Flow, Reachability_Analyzer  
**Type:** Synchronous  
**Criticality:** High  
**Version:** 1.0.0  
**Status:** ✅ Defined

**Opis:**
Interfejs dla budowy grafu symboli (functions, classes, imports). Używany do reachability analysis i impact analysis.

[Analogiczny format]

---

### 2.5. INT-005: IRefactoringEngine

**Provider:** Core_Engine  
**Consumers:** IDE_Plugin, CLI_Tools  
**Type:** Synchronous  
**Criticality:** Medium  
**Version:** 1.0.0  
**Status:** ✅ Defined

**Opis:**
Interfejs dla silnika refaktoringu. Wykonuje transformacje kodu (rename, extract, inline, etc.).

[Analogiczny format]

---

[Powtórzyć dla wszystkich ~15-20 kluczowych interfejsów]

**Pozostałe interfejsy:**
- INT-006: ILanguageAdapter (Core_Engine ← Language_Adapters)
- INT-007: IFixGenerator (FixOps → SAST/SCA/Secrets)
- INT-008: ISecretsScanner (FixOps ← Secrets_Scanner)
- INT-009: IProvenanceService (Platform_Tools ← Provenance_Service)
- INT-010: ISecretsBroker (wszystkie ← Secrets_Broker)
- INT-011: IObligationsTracker (Platform_Tools)
- INT-012: IValidationService (Platform_Tools)
- INT-013: IPolicyGates (CICD_Tooling ← Platform_Tools)
- INT-014: ICollaborativeCanvas (Frontend ← Collaborative_Canvas)
- INT-015: IAuthProvider (wszystkie ← LLM_Auth_Providers)

---

## 3. DATA CONTRACTS (SCHEMAS)

### 3.1. Schema Repository

**Lokalizacja:** `shared_resources/schemas/`

**Format:** JSON Schema (Draft 2020-12)

**Struktura:**
```
shared_resources/schemas/
├── finding.schema.json           # Finding (SAST, SCA, Secrets)
├── scan_result.schema.json       # ScanResult
├── sbom.schema.json              # SBOM (CycloneDX, SPDX)
├── symbol_graph.schema.json      # Symbol Graph
├── impact_graph.schema.json      # Impact Analysis
├── refactoring_plan.schema.json  # Refactoring Plan
├── cve_info.schema.json          # CVE Details
└── ...
```

### 3.2. Schema Validation

**Enforcement:**
```python
from jsonschema import validate

# Producer validates output:
def scan(path, config):
    result = _do_scan(path, config)
    validate(instance=result, schema=SCAN_RESULT_SCHEMA)  # Validate!
    return result

# Consumer validates input:
def process_scan_result(result):
    validate(instance=result, schema=SCAN_RESULT_SCHEMA)  # Validate!
    # Process...
```

**CI Enforcement:**
```yaml
# CI check:
- name: Validate contract compliance
  run: |
    python scripts/validate_all_outputs.py
    # Fails jeśli output nie pasuje do schema
```

### 3.3. Schema Versioning

**Backward Compatibility:**
- **Adding optional field:** MINOR version bump (backward compatible)
- **Removing field:** MAJOR version bump (breaking)
- **Changing type:** MAJOR version bump (breaking)

**Example:**
```json
// v1.0.0
{
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "severity": {"enum": ["LOW", "MEDIUM", "HIGH"]}
  },
  "required": ["id", "severity"]
}

// v1.1.0 (MINOR - added optional field)
{
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "severity": {"enum": ["LOW", "MEDIUM", "HIGH"]},
    "cve_id": {"type": "string"}  // NEW, optional
  },
  "required": ["id", "severity"]
}

// v2.0.0 (MAJOR - changed enum)
{
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "severity": {"enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"]}  // CHANGED
  },
  "required": ["id", "severity"]
}
```

---

## 4. SLA I PERFORMANCE GUARANTEES

### 4.1. Performance SLA per Interface

| Interface | Operation | Latency (p50) | Latency (p95) | Throughput | Memory |
|-----------|-----------|---------------|---------------|------------|--------|
| ISASTScanner | scan() | < 20s | < 30s | 20 scans/min | < 512 MB |
| ISCAScanner | scan_dependencies() | < 3s | < 5s | 100 scans/min | < 128 MB |
| ISBOMProvider | generate_sbom() | < 2s | < 3s | 200 SBOMs/min | < 64 MB |
| ISymbolGraphBuilder | build() | < 10s | < 15s | 40 builds/min | < 256 MB |
| IRefactoringEngine | apply() | < 1s | < 2s | 300 ops/min | < 128 MB |

### 4.2. Monitoring i Alerting

**Metrics Collected:**
```python
# Per interface call:
interface_call_duration_seconds{interface="ISASTScanner", method="scan"}
interface_call_total{interface="ISASTScanner", method="scan", status="success|error"}
interface_memory_bytes{interface="ISASTScanner"}
```

**Alerts:**
```yaml
alerts:
  - name: SLABreach
    condition: interface_call_duration_seconds{quantile="0.95"} > SLA * 1.2
    action: PagerDuty
```

---

## 5. BACKWARD COMPATIBILITY I DEPRECATION

### 5.1. Compatibility Policy

**Support Window:**
- **Current MAJOR:** Full support
- **Previous MAJOR:** Maintenance mode (bug fixes only), min 6 months
- **Older MAJOR:** Deprecated, no support

**Example:**
```
Current: v2.x (full support)
Previous: v1.x (maintenance until 2026-06-01)
Deprecated: v0.x (no support, remove after v1.x EOL)
```

### 5.2. Deprecation Process

**Phase 1: Deprecation Notice (Version N)**
```python
import warnings

def old_method():
    warnings.warn(
        "old_method() is deprecated, use new_method() instead. "
        "Will be removed in version N+2.",
        DeprecationWarning,
        stacklevel=2
    )
    return new_method()
```

**Phase 2: Removal (Version N+2)**
```python
# old_method() removed entirely
```

**Migration Guide:**
```markdown
# Migration Guide: v1.x → v2.x

## Breaking Changes

### Change 1: scan() signature changed
**Old (v1.x):**
\`\`\`python
scanner.scan(path: Path, rules: list[str]) -> ScanResult
\`\`\`

**New (v2.x):**
\`\`\`python
scanner.scan(request: ScanRequest) -> ScanResult
\`\`\`

**Migration:**
\`\`\`python
# Old code:
result = scanner.scan(path, rules=["sql-injection"])

# New code:
request = ScanRequest(path=path, rules=["sql-injection"])
result = scanner.scan(request)
\`\`\`
```

---

## 6. TESTING STRATEGY

### 6.1. Contract Tests (Pact)

**Consumer-Driven Contracts:**

**Consumer test (FixOps):**
```python
from pact import Consumer, Provider

pact = (
    Consumer("FixOps")
    .has_pact_with(Provider("SAST_Engine"))
)

(pact
  .given("a valid source path")
  .upon_receiving("a request for SAST scan")
  .with_request(
      method="POST",
      path="/scan",
      body={"path": "/test/project", "rules": ["sql-injection"]}
  )
  .will_respond_with(
      status=200,
      body={
          "findings": Like([{
              "id": "uuid",
              "severity": "HIGH",
              "message": "SQL injection detected"
          }])
      }
  ))

# This generates a pact file: pacts/FixOps-SAST_Engine.json
```

**Provider verification (SAST_Engine):**
```python
from pact import Verifier

verifier = Verifier(
    provider="SAST_Engine",
    provider_base_url="http://localhost:8000"
)

verifier.verify_pacts(
    "pacts/FixOps-SAST_Engine.json",
    provider_states_setup_url="http://localhost:8000/setup"
)

# Verifies SAST_Engine honors the contract
```

### 6.2. Integration Tests

**End-to-End Integration:**
```python
def test_sast_to_fixops_integration():
    """Test full flow: SAST → FixOps."""
    
    # 1. SAST scan
    scanner = create_scanner()
    scan_result = scanner.scan(test_project, config)
    
    # 2. FixOps consumes SAST results
    fixops = FixOps(sast_scanner=scanner)
    fixes = fixops.generate_fixes(test_project)
    
    # 3. Verify
    assert len(fixes) > 0
    assert fixes[0].finding_id in [f.id for f in scan_result.findings]
```

### 6.3. Performance Tests

**Load Testing:**
```python
from locust import HttpUser, task

class InterfaceLoadTest(HttpUser):
    @task
    def test_sast_scan():
        response = self.client.post("/scan", json={
            "path": "/test/project",
            "config": {...}
        })
        assert response.elapsed.total_seconds() < 30  # SLA check
```

---

## 7. DOCUMENTATION

### 7.1. API Reference per Module

**Generated from code:**
```python
# SAST_Engine/src/api/__init__.py
"""SAST Engine Public API.

This module provides the ISASTScanner interface for static security analysis.

Example:
    >>> from sast_engine import create_scanner, ScanConfig
    >>> scanner = create_scanner()
    >>> result = scanner.scan(Path("./src"), ScanConfig(rules=["sql-injection"]))
    >>> print(f"Found {len(result.findings)} issues")
"""

# Generate docs:
# pdoc sast_engine --output-dir docs/api/
```

### 7.2. OpenAPI Spec (jeśli REST API)

```yaml
# openapi.yaml
openapi: 3.0.0
info:
  title: SAST Engine API
  version: 1.0.0
paths:
  /scan:
    post:
      summary: Scan source code
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScanRequest'
      responses:
        '200':
          description: Scan completed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScanResult'
```

---

## 8. INTEGRATION PATTERNS (RECIPES)

### 8.1. Pattern: Adapter Chaining

**Use Case:** Chain multiple adapters (SAST → SCA → Secrets → FixOps)

```python
class SecurityPipeline:
    """Orchestrates security scans."""
    
    def __init__(
        self,
        sast: ISASTScanner,
        sca: ISCAScanner,
        secrets: ISecretsScanner,
        fixops: IFixGenerator
    ):
        self._sast = sast
        self._sca = sca
        self._secrets = secrets
        self._fixops = fixops
    
    def run_full_scan(self, path):
        # Step 1: SAST
        sast_result = self._sast.scan(path, sast_config)
        
        # Step 2: SCA (needs SBOM)
        sbom = self._sbom_gen.generate_sbom(path)
        sca_result = self._sca.scan_dependencies(sbom)
        
        # Step 3: Secrets
        secrets_result = self._secrets.scan(path)
        
        # Step 4: Aggregate findings
        all_findings = (
            sast_result.findings +
            sca_result.vulnerabilities +
            secrets_result.findings
        )
        
        # Step 5: Generate fixes
        fixes = self._fixops.generate_fixes(all_findings)
        
        return PipelineResult(
            findings=all_findings,
            fixes=fixes
        )
```

### 8.2. Pattern: Parallel Execution

**Use Case:** Run SAST + SCA + Secrets in parallel

```python
import asyncio

async def run_parallel_scan(path):
    # Run all scans concurrently:
    sast_task = asyncio.create_task(sast.scan_async(path))
    sca_task = asyncio.create_task(sca.scan_async(path))
    secrets_task = asyncio.create_task(secrets.scan_async(path))
    
    # Wait for all:
    sast_result, sca_result, secrets_result = await asyncio.gather(
        sast_task, sca_task, secrets_task
    )
    
    return aggregate_results(sast_result, sca_result, secrets_result)
```

---

## ZAŁĄCZNIKI

### A. Interface Catalog (Quick Reference)

| ID | Interface | Provider | Consumers | Type | SLA Latency |
|----|-----------|----------|-----------|------|-------------|
| INT-001 | ISASTScanner | SAST_Engine | FixOps, Platform_Tools | Sync | < 30s p95 |
| INT-002 | ISCAScanner | SCA_Engine | FixOps, Platform_Tools | Sync | < 5s p95 |
| INT-003 | ISBOMProvider | SBOM_Generator | SCA_Engine | Sync | < 3s p95 |
| INT-004 | ISymbolGraphBuilder | SymbolGraph_Builder | Impact_Flow | Sync | < 15s p95 |
| ... | ... | ... | ... | ... | ... |

### B. Dependency Matrix

[Cross-reference table showing which modules depend on which interfaces]

### C. Migration Guides

[Links to all migration guides for breaking changes]

---

## CHECKLIST KOMPLETNOŚCI

- [x] Executive Summary (zakres, dashboard, kluczowe integracje)
- [x] Zasady integracji (contract-first, DI, versioning, fail-safe, observable)
- [x] Communication patterns (sync, async, events, shared data)
- [x] Katalog interfejsów (format standardowy, ~15-20 interfejsów)
- [x] Data contracts (schemas, validation, versioning)
- [x] SLA i performance guarantees (per interface, monitoring)
- [x] Backward compatibility (policy, deprecation process)
- [x] Testing strategy (contract tests, integration, performance)
- [x] Documentation (API reference, OpenAPI)
- [x] Integration patterns (recipes: chaining, parallel)
- [x] Załączniki (catalog, matrix, guides)
- [x] Cross-references (TO-BE, PROCES, PROBLEMY)

**Wypełnienie:** Każdy interfejs używa standardowego formatu z methods, data contracts, error handling, SLA, examples, tests, references.
