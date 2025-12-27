# Analiza Stanu Obecnego (AS-IS)

> **Framework:** arc42 + C4 Model + IEEE 42010  
> **Data analizy:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół]  
> **Status:** [Draft/Review/Approved]  
> **Powiązane dokumenty:** → `02_TO_BE`, → `03_PROBLEMY_I_BŁĘDY`

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: CODEBASE-SCAN
    type: data_source
    from_sections:
      - file_structure
      - dependency_graph
    to_sections:
      - architecture_inventory
      - technical_metrics
    influence: "Skan kodu dostarcza surowe dane o aktualnej strukturze"
    when:
      condition: analysis.type == "as_is"
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: TO-BE-ARCHITECTURE
    type: vision_input
    from_sections:
      - current_architecture
      - identified_problems
    to_sections:
      - improvement_opportunities
      - target_state_design
    influence: "Stan obecny definiuje punkt wyjścia dla docelowej architektury"
    when:
      condition: document.complete == true
      applies: always

  - id: PROBLEMS-ANALYSIS
    type: problem_identification
    from_sections:
      - technical_debt_areas
      - anti_patterns
    to_sections:
      - problem_catalog
      - root_cause_analysis
    influence: "AS-IS ujawnia problemy wymagające analizy"
    when:
      condition: analysis.has_issues == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: CODE-REVIEW-FINDINGS
    relationship: quality_input
    sections_mapping:
      - from: review_comments
        to: code_quality_issues
    usage: "Findings z code review wzbogacają analizę"
```

### Satellite Documents

```yaml
satellites:
  - name: ARCHITECTURE-DIAGRAMS
    purpose: "Wizualizacje obecnej architektury"
    trigger: during_analysis
    lifecycle: continuous
    retention: permanent
```

---

## EXECUTIVE SUMMARY

### Cel Dokumentu
[Zwięzły opis - dlaczego analizujemy obecny stan, dla kogo ten dokument]

### Kluczowe Wnioski
- **Wniosek 1:** [najważniejsze odkrycie]
- **Wniosek 2:** [drugi najważniejszy]
- **Wniosek 3:** [trzeci]

### Zakres Analizy
- **Moduły objęte:** [14 modułów]
- **Wyłączone:** [co pominięto i dlaczego]
- **Okres:** [od kiedy do kiedy dane]

### Status Dashboard
| Metryka | Wartość | Trend | Target |
|---------|---------|-------|--------|
| Liczba modułów | [14] | → | [26] |
| Całkowity rozmiar | [~79 MB] | ↑ | [stabilny] |
| Technical debt | [X dni] | ↑ | [< Y dni] |
| Test coverage | [Z%] | → | [> 80%] |
| CVE Critical | [N] | ↓ | [0] |

---

## 1. KONTEKST BIZNESOWY I INTERESARIUSZE

### 1.1. Cel Systemu
**Problem biznesowy:**
[Jaki problem rozwiązuje system - 2-3 zdania]

**Wartość dla biznesu:**
- [Wartość 1]
- [Wartość 2]

### 1.2. Interesariusze (IEEE 42010)

| Rola | Osoba/Zespół | Concerns | Wpływ | Zaangażowanie |
|------|--------------|----------|-------|---------------|
| Product Owner | [Nazwa] | [Business value, ROI] | Wysoki | Tygodniowy |
| Tech Lead | [Nazwa] | [Architecture, quality] | Wysoki | Dzienny |
| DevOps | [Nazwa] | [Deployment, stability] | Średni | Dzienny |
| Security | [Nazwa] | [Vulnerabilities, compliance] | Wysoki | Tygodniowy |
| End Users | [Grupa] | [Features, performance] | Niski | - |

### 1.3. Historia Projektu
- **Data rozpoczęcia:** [YYYY-MM-DD]
- **Milestones:**
  - [YYYY-MM]: [Milestone 1]
  - [YYYY-MM]: [Milestone 2]
- **Ewolucja architektury:** [Jak system się zmieniał]

---

## 2. ARCHITEKTURA OBECNA

### 2.1. Context Diagram (C4 Level 1)
```
┌─────────────────────────────────────────────┐
│         AIUnifiedDesktop System             │
│                                             │
│  [14 modułów bezpieczeństwa i analizy]     │
└─────────────────────────────────────────────┘
         ↑              ↑              ↑
         │              │              │
    [User/Dev]    [CI/CD System]  [External APIs]
```

### 2.2. Container Diagram (C4 Level 2)
```
[Diagram pokazujący główne kontenery/moduły]

┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CORE      │────▶│ INTELLIGENCE│────▶│  PLATFORM   │
│  ENGINES    │     │  FEATURES   │     │  SERVICES   │
└─────────────┘     └─────────────┘     └─────────────┘
```

### 2.3. Przegląd Modułów (arc42 5.1 Building Blocks)

| ID | Nazwa Modułu | Rozmiar | Pliki | Języki | Status | Owner | Tech Debt |
|----|--------------|---------|-------|--------|--------|-------|-----------|
| M01 | Security_Analysis | 48 MB | 4,329 | Py | Prod | [Zespół] | Wysoki |
| M02 | Collaborative_Canvas | 9.8 MB | 329 | TS/JS | Prod | [Zespół] | Średni |
| M03 | Code_Refactoring | 4.6 MB | 995 | Py/TS | Beta | [Zespół] | Wysoki |
| M04 | Provenance_Secrets | 4.2 MB | 445 | Py | Prod | [Zespół] | Średni |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Całkowite statystyki:**
- **Liczba modułów:** 14
- **Całkowity rozmiar:** ~79 MB
- **Całkowita liczba plików:** ~8,000+
- **Języki:** Python (45%), TypeScript (30%), JavaScript (15%), Go (5%), Inne (5%)

---

## 3. SZCZEGÓŁOWA ANALIZA MODUŁÓW

### 3.1. [Moduł: Security_Analysis]

**Podstawowe Informacje:**
- **ID:** M01
- **Ścieżka:** `Moduły/Security_Analysis/`
- **Rozmiar:** 48 MB (60% całości!)
- **Liczba plików:** 4,329
- **Liczba katalogów:** 80 podkatalogów
- **Języki:** Python 85%, YAML 10%, JSON 5%
- **Status:** Produkcja
- **Właściciel:** [Zespół Security]

**Odpowiedzialność (arc42 1.2):**
Moduł odpowiada za:
1. Statyczną analizę bezpieczeństwa kodu (SAST)
2. Analizę komponentów i CVE (SCA)
3. Wykrywanie hardcoded secrets
4. Generowanie propozycji napraw
5. Analizę osiągalności luk (reachability)

**Komponenty Wewnętrzne (arc42 5.2):**
```
Security_Analysis/
├── sast/           # SAST Engine - Semgrep, CodeQL
├── sca/            # SCA Engine - OSV, NVD
├── secrets/        # Secrets Scanner
├── fixes/          # Fix Proposals
├── reachability/   # Reachability Analysis
├── L1_FAZA0/       # ⚠️ Metadata (duplikacje!)
└── L1_FAZA1/       # ⚠️ Reports
```

**Problem: Monolit**
⚠️ Ten moduł łączy 4-5 różnych funkcjonalności bez wyraźnych granic!

**Interfaces Publiczne (arc42 6.1):**

**API:**
```python
# SAST
def scan_code(source_path, rules) -> ScanResult
def get_sast_findings() -> list[Finding]

# SCA  
def scan_dependencies(sbom_path) -> list[Vulnerability]
def get_cve_details(cve_id) -> CVEInfo

# Secrets
def scan_secrets(path) -> list[Secret]

# Fixes
def generate_fixes(findings) -> list[FixProposal]
```

**CLI:**
```bash
security-analysis scan --path ./src --output findings.json
security-analysis sca --sbom sbom.json
security-analysis secrets --scan ./
```

**Konfiguracja (arc42 10.1):**
```yaml
# configs/sast_rulesets.yaml
rulesets:
  - semgrep: p/security-audit
  - codeql: security-extended

# configs/severity_overrides.yaml  
overrides:
  - rule_id: "hardcoded-secret"
    severity: "CRITICAL"
```

**Zależności (arc42 3.1 + 3.2):**
- **Upstream (od czego zależy):**
  - `SymbolGraph_Builder` (z IR_SBOM_Impact) - dla reachability
  - `SBOM_Generator` (z IR_SBOM_Impact) - dla SCA
- **Downstream (co od niego zależy):**
  - `Platform_Tools` - gates policy
  - `CICD_Tooling` - CI/CD pipelines
- **External:**
  - semgrep >= 1.45.0
  - npm audit API
  - OSV API
  - NVD API

**Metryki Wydajności (arc42 11.2):**
| Operacja | Czas (avg) | Pamięć | SLA |
|----------|------------|--------|-----|
| SAST scan (1000 files) | 45s | 512 MB | < 60s |
| SCA scan | 8s | 128 MB | < 15s |
| Secrets scan | 12s | 256 MB | < 20s |

**Metryki Jakości:**
- **Test coverage:** 75% (unit), 60% (integration)
- **Cyclomatic complexity:** Średnio 8.5 (max 42!)
- **Duplikacje:** 15% kodu
- **Technical debt:** 25 dni

**Problemy Zidentyfikowane:** → Zobacz `03_PROBLEMY_I_BŁĘDY.md`
- A-001: Brak wyraźnych granic między SAST/SCA/Secrets
- A-002: Duplikacje metadata w L1_FAZA0/
- T-005: Wolny SAST scan (> 60s dla dużych projektów)
- S-003: CVE-2024-XXXXX w semgrep < 1.50

[Powtórzyć dla każdego z 14 modułów]

---

## 4. STOS TECHNOLOGICZNY (arc42 8.1)

### 4.1. Języki Programowania

| Język | Wersja | Użycie | LOC | % Kodu | Trendy |
|-------|--------|--------|-----|--------|--------|
| Python | 3.11+ | Backend, analiza, narzędzia | 45,000 | 45% | Stabilny |
| TypeScript | 5.0+ | Frontend, Canvas | 30,000 | 30% | Rosnący |
| JavaScript | ES2022 | Frontend legacy | 15,000 | 15% | Spadający |
| Go | 1.21+ | Performance-critical | 5,000 | 5% | Rosnący |
| Shell | Bash 5.0 | Automation, CI/CD | 3,000 | 3% | Stabilny |
| YAML | - | Config, workflows | 2,000 | 2% | Stabilny |

### 4.2. Frameworki i Biblioteki

**Backend (Python):**
- **FastAPI** 0.104+ - API servers (LLM_Auth_Providers)
- **libcst** 1.1+ - Python CST refactoring (Code_Refactoring)
- **semgrep** 1.45+ - SAST engine (Security_Analysis)
- **pydantic** 2.4+ - Data validation
- **pytest** 7.4+ - Testing framework

**Frontend (TypeScript/JavaScript):**
- **TipTap** 2.0+ - Rich text editor (Collaborative_Canvas)
- **Yjs** 13.6+ - CRDT for collaboration (Collaborative_Canvas)
- **ts-morph** 20.0+ - TypeScript AST (Code_Refactoring)
- **React** 18+ - UI framework (gdzie używany)
- **Vite** 5.0+ - Build tool

**Tools & CLI:**
- **Typer** 0.9+ - Python CLI
- **Rich** 13.0+ - Terminal formatting

### 4.3. Infrastruktura i Operacje

**System Operacyjny:**
- Development: Linux (Ubuntu 22.04), macOS 13+
- Production: Linux containers

**Bazy Danych:**
- **SQLite** - Local development, obligations storage
- **PostgreSQL** 15+ - Production database (planowane)
- **JSON files** - Configuration, examples

**Message Queue / Events:**
- **WebSocket** - Real-time collaboration (Collaborative_Canvas)

**Storage:**
- File system - SBOM, reports, cache
- Git - Provenance, versioning

---

## 5. ZALEŻNOŚCI MIĘDZY MODUŁAMI (arc42 3.2)

### 5.1. Graf Zależności

```
Legend: A ──▶ B  (A depends on B)

SymbolGraph_Builder (IR_SBOM_Impact)
    │
    ├──▶ SBOM_Generator
    │        │
    │        └──▶ SCA_Engine (Security_Analysis)
    │                 │
    │                 └──▶ FixOps
    │
    └──▶ Impact_Analyzer
             │
             └──▶ Code_Refactoring ──▶ Language_Adapters
                                            │
                                            └──▶ Core_Engine

Platform_Tools ◀── (używane przez wszystkie)
CICD_Tooling ◀── (integruje wszystkie)
```

### 5.2. Macierz Zależności

|     | M01 | M02 | M03 | M04 | M05 | M06 | M07 | M08 | M09 | M10 | M11 | M12 | M13 | M14 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **M01 Security_Analysis** | - | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| **M02 Collaborative_Canvas** | ✗ | - | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| **M03 Code_Refactoring** | ✗ | ✗ | - | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| **M09 IR_SBOM_Impact** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | - | ✗ | ✗ | ✗ | ✗ | ✗ |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Legenda:** ✓ = zależy od, ✗ = nie zależy

### 5.3. Szczegółowe Zależności

#### Security_Analysis → IR_SBOM_Impact

**Typ:** Direct dependency  
**Powód:** Reachability analysis wymaga symbol graph  
**Interfejs używany:**
```python
from ir_sbom_impact.symbol_graph import SymbolGraphBuilder
from ir_sbom_impact.sbom import SBOMGenerator

builder = SymbolGraphBuilder()
graph = builder.build(source_path)
```

**Stopień sprzężenia:** Wysoki (⚠️ Problem!)  
**Problem:** Bezpośrednie użycie wewnętrznych struktur zamiast publicznego API

**Metryki coupling:**
- **Afferent coupling (Ca):** 3 (3 moduły zależą od Security_Analysis)
- **Efferent coupling (Ce):** 2 (Security_Analysis zależy od 2 modułów)
- **Instability (I = Ce/(Ca+Ce)):** 0.4 (umiarkowanie stabilny)

[Powtórzyć dla każdej ważnej zależności]

---

## 6. DANE I PRZECHOWYWANIE (arc42 5.3)

### 6.1. Modele Danych

#### Model: Finding (Security_Analysis)
```yaml
Finding:
  id: string (UUID)
  type: enum[SAST, SCA, SECRET]
  severity: enum[CRITICAL, HIGH, MEDIUM, LOW]
  rule_id: string
  message: string
  location:
    file: string
    line: integer
    column: integer
  metadata:
    cve_id: string? (jeśli SCA)
    cvss_score: float?
    reachability: enum[REACHABLE, UNREACHABLE, UNKNOWN]
  fix_proposals: list[FixProposal]
  created_at: datetime
```

#### Model: SymbolGraph (IR_SBOM_Impact)
```yaml
SymbolGraph:
  nodes: list[Symbol]
  edges: list[Dependency]
  
Symbol:
  id: string
  name: string
  type: enum[function, class, module]
  location: Location
  exports: list[string]
  
Dependency:
  source: string (symbol_id)
  target: string (symbol_id)
  type: enum[import, call, inheritance]
```

### 6.2. Bazy Danych i Storage

| Typ Danych | Format | Lokalizacja | Rozmiar | Backup | Owner Module |
|------------|--------|-------------|---------|--------|--------------|
| Findings | NDJSON | `security/findings.ndjson` | ~5 MB | Git | Security_Analysis |
| SBOM | CycloneDX/SPDX JSON | `sbom/*.json` | ~2 MB | Git | IR_SBOM_Impact |
| Symbol Graph | JSON | `graphs/*.json` | ~10 MB | Git | IR_SBOM_Impact |
| Config | YAML | `configs/*.yaml` | ~500 KB | Git | Wszystkie |
| Obligations | SQLite | `obligations.db` | ~1 MB | Backup | Platform_Tools |
| Attestations | JSON | `provenance/*.json` | ~3 MB | Git + Backup | Provenance_Secrets |
| Secrets Leases | Encrypted JSON | `secrets/leases/*.enc` | ~100 KB | Secure Storage | Provenance_Secrets |

**Całkowity storage:** ~21.6 MB (dane), ~79 MB (kod + dane)

### 6.3. Formaty Plików

**SARIF (Static Analysis Results Interchange Format):**
```json
{
  "version": "2.1.0",
  "runs": [{
    "tool": {"driver": {"name": "semgrep"}},
    "results": [...]
  }]
}
```

**CycloneDX SBOM:**
```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.4",
  "components": [...]
}
```

---

## 7. PRZEPŁYWY DANYCH (arc42 6.2)

### 7.1. Główny Przepływ: Security Scan

```
┌─────────┐                ┌──────────────────┐                ┌─────────┐
│  User   │───[trigger]───▶│ Security_Analysis│────[results]──▶│ Reports │
│   CLI   │                │      Module      │                │  JSON   │
└─────────┘                └──────────────────┘                └─────────┘
                                    │
                                    ├─[1]─▶ SAST Engine ──▶ Semgrep API
                                    │                      └─▶ CodeQL
                                    │
                                    ├─[2]─▶ SCA Engine ───▶ SBOM_Generator
                                    │                      └─▶ OSV API
                                    │                      └─▶ NVD API
                                    │
                                    ├─[3]─▶ Secrets Scanner
                                    │
                                    ├─[4]─▶ Reachability ──▶ SymbolGraph
                                    │
                                    └─[5]─▶ FixOps ───────▶ Ranked fixes
```

**Opis kroków:**
1. **SAST:** Skanowanie kodu źródłowego z regułami security
2. **SCA:** Analiza zależności vs CVE databases  
3. **Secrets:** Wykrywanie hardcoded secrets
4. **Reachability:** Sprawdzenie czy CVE jest w użyciu
5. **FixOps:** Generowanie propozycji napraw

**Dane wejściowe:**
- Source code path: `string`
- SBOM (optional): `CycloneDX JSON`
- Configuration: `YAML`

**Dane wyjściowe:**
- Findings: `NDJSON` (line-delimited JSON)
- Unified report: `SARIF`
- Dashboard: `HTML`

**SLA:** < 60s dla 1000 plików

### 7.2. Przepływ: SBOM Generation

[Analogiczny format dla innych głównych przepływów]

---

## 8. INTERFEJSY I API (arc42 6.1)

### 8.1. REST API (gdzie używane)

**LLM_Auth_Providers:**

| Endpoint | Metoda | Opis | Request | Response | Auth |
|----------|--------|------|---------|----------|------|
| `/auth/login` | POST | OAuth login | `{provider, redirect_uri}` | `{auth_url}` | None |
| `/auth/callback` | GET | OAuth callback | `?code=...&state=...` | `{access_token}` | None |
| `/providers` | GET | Lista providerów | - | `[{id, name, status}]` | Token |
| `/api/proxy` | POST | Proxy do LLM API | `{prompt, model}` | `{response}` | Token |

### 8.2. CLI Interfaces

**Security_Analysis:**
```bash
# Scan
security-analysis scan --path ./src --output findings.json

# SCA only
security-analysis sca --sbom sbom.json --format sarif

# Secrets
security-analysis secrets --scan ./ --allowlist .secrets-allow

# Generate fixes
security-analysis fix --findings findings.json --output fixes.json
```

**IR_SBOM_Impact:**
```bash
# Symbol graph
symbolgraph build --source ./src --output graph.json

# SBOM
sbom generate --source ./src --format cyclonedx --output sbom.json

# Impact analysis
impact analyze --changes changes.json --graph graph.json
```

### 8.3. Events / WebSocket (gdzie używane)

**Collaborative_Canvas:**

| Event | Direction | Payload | Opis |
|-------|-----------|---------|------|
| `diff.preview` | Server→Client | `{diff, metadata}` | Preview zmian |
| `canvas.update` | Bidirectional | `{ops, clientId}` | CRDT operations (Yjs) |
| `cursor.move` | Client→Server | `{position, user}` | Pozycja kursora |
| `selection.change` | Client→Server | `{range, user}` | Zaznaczenie |

---

## 9. METRYKI I STATYSTYKI (arc42 11.1)

### 9.1. Rozmiar Kodu

**Całościowe:**
- **Całkowita liczba plików:** 8,247
- **Łączna liczba linii kodu:** 103,000 LOC
- **Kod bez komentarzy:** 87,500 LOC (85%)
- **Komentarze:** 10,300 linii (10%)
- **Puste linie:** 5,200 (5%)

**Podział według języka:**
| Język | LOC | Pliki | % Kodu | Średnia LOC/plik |
|-------|-----|-------|--------|------------------|
| Python | 46,350 | 420 | 45% | 110 |
| TypeScript | 30,900 | 280 | 30% | 110 |
| JavaScript | 15,450 | 190 | 15% | 81 |
| Go | 5,150 | 45 | 5% | 114 |
| Shell | 3,090 | 85 | 3% | 36 |
| YAML | 2,060 | 1,250 | 2% | 1.6 |

**Największe pliki:** (potencjalne God Objects)
1. `Security_Analysis/L1_FAZA1/tools/unified_pipeline.py` - 1,842 LOC ⚠️
2. `Code_Refactoring/refactoring_engine.py` - 1,456 LOC ⚠️
3. `Collaborative_Canvas/canvas_server.ts` - 1,234 LOC ⚠️

### 9.2. Pokrycie Testami

| Moduł | Unit | Integration | E2E | Overall |
|-------|------|-------------|-----|---------|
| Security_Analysis | 75% | 60% | 40% | 68% |
| IR_SBOM_Impact | 85% | 70% | 50% | 76% |
| Code_Refactoring | 70% | 55% | 30% | 62% |
| Collaborative_Canvas | 80% | 65% | 55% | 72% |
| **Średnia** | **77%** | **62%** | **44%** | **69%** |

**Target:** > 80% (unit), > 70% (integration), > 50% (E2E)  
**Status:** ⚠️ Poniżej targetu

### 9.3. Metryki Jakości Kodu

**Complexity (McCabe Cyclomatic Complexity):**
- **Średnia:** 8.5
- **Mediana:** 5.0
- **Max:** 42 (⚠️ `unified_pipeline.py:process_all()`)
- **Funkcje > 15:** 23 funkcje (2.3%)

**Target:** Średnia < 10, Max < 20

**Duplikacje:**
- **Całkowita duplikacja:** 15,450 LOC (15%)
- **Największe duplikacje:**
  - `L1_FAZA0/metadata/normalized/*` w Security_Analysis (⚠️ 8,000 LOC)
  - Similarity w testach: 2,500 LOC

**Target:** < 5% duplikacji

**Technical Debt:**
- **Całkowity dług:** 147 person-days
- **Debt ratio:** 18.5% (wysoki!)
- **SQALE Rating:** C
- **Top contributors:**
  - Security_Analysis: 25 dni
  - Code_Refactoring: 18 dni
  - Collaborative_Canvas: 15 dni

**Maintainability Index:**
- **Średnia:** 62 (moderate)
- **Target:** > 70

### 9.4. Metryki Coupling/Cohesion

| Moduł | Afferent (Ca) | Efferent (Ce) | Instability (I) | Abstractions (A) |
|-------|---------------|---------------|-----------------|------------------|
| Security_Analysis | 3 | 2 | 0.40 | 0.15 |
| IR_SBOM_Impact | 5 | 0 | 0.00 | 0.30 |
| Code_Refactoring | 2 | 2 | 0.50 | 0.20 |
| Platform_Tools | 8 | 1 | 0.11 | 0.40 |

**I (Instability) = Ce / (Ca + Ce)**
- 0.0 = maksymalnie stabilny
- 1.0 = maksymalnie niestabilny

---

## 10. WYDAJNOŚĆ (arc42 11.2)

### 10.1. Benchmarki Obecne

| Operacja | Moduł | Czas (avg) | Czas (p95) | Pamięć | CPU | SLA | Status |
|----------|-------|------------|------------|--------|-----|-----|--------|
| SAST scan (1000 files) | Security_Analysis | 45s | 58s | 512 MB | 280% | < 60s | ✓ OK |
| SCA scan | Security_Analysis | 8s | 12s | 128 MB | 80% | < 15s | ✓ OK |
| Symbol graph build | IR_SBOM_Impact | 22s | 35s | 256 MB | 200% | < 30s | ⚠️ Granica |
| SBOM generation | IR_SBOM_Impact | 5s | 8s | 64 MB | 50% | < 10s | ✓ OK |
| Refactoring (rename) | Code_Refactoring | 3s | 5s | 128 MB | 100% | < 5s | ⚠️ Granica |
| Canvas sync (50 users) | Collaborative_Canvas | 50ms | 120ms | 1 GB | 150% | < 100ms | ⚠️ p95 przekroczone |

**Wąskie Gardła:**
1. **Symbol graph build** - parsowanie AST dla dużych projektów
2. **Canvas sync p95** - spike przy > 40 użytkownikach
3. **SAST scan** - Semgrep dla > 2000 plików

### 10.2. Resource Usage (Production-like)

**Pamięć:**
- **Baseline:** 450 MB (idle)
- **Peak:** 2.1 GB (podczas full scan)
- **Average:** 850 MB

**CPU:**
- **Average:** 35%
- **Peak:** 420% (multi-core, podczas SAST)

**Disk I/O:**
- **Read:** 45 MB/s (average podczas scan)
- **Write:** 8 MB/s (reports, cache)

### 10.3. Scalability Analysis

**Current Limits:**
- **Max files per scan:** ~5,000 (potem timeout)
- **Max concurrent users (Canvas):** ~50 (potem degradacja)
- **Max SBOM size:** ~10 MB JSON (potem memory issues)

**Bottlenecks:**
- Single-threaded parsery w niektórych modułach
- Brak cache dla powtarzających się operacji
- Synchroniczne I/O

---

## 11. BEZPIECZEŃSTWO (arc42 11.3)

### 11.1. Obecne Kontrole Bezpieczeństwa

| Kontrola | Implementacja | Moduły | Status | Gap |
|----------|---------------|--------|--------|-----|
| **Autentykacja** | OAuth 2.0 + PKCE | LLM_Auth_Providers | ✓ Działa | - |
| **Autoryzacja** | ⚠️ Brak RBAC | - | ✗ Brak | Krytyczne |
| **Walidacja wejścia** | Pydantic schemas | Python modules | ✓ Częściowo | Niekompletne |
| **Sanityzacja output** | ⚠️ Logs zawierają PII | Security_Analysis | ✗ Problem | Wysoki |
| **Encryption at rest** | AES-256 dla secrets | Provenance_Secrets | ✓ Działa | - |
| **Encryption in transit** | TLS 1.3 | API/WebSocket | ✓ Działa | - |
| **Secrets management** | Leases + rotation | Provenance_Secrets | ✓ Działa | - |
| **Audit logging** | NDJSON events | Platform_Tools | ✓ Działa | - |
| **Rate limiting** | ⚠️ Brak | API | ✗ Brak | Średni |
| **Input size limits** | ⚠️ Niespójne | Różne | ✗ Problem | Średni |

### 11.2. Znane Luki (CVE)

| CVE ID | Severity | CVSS | Component | Version | Fix Available | Status |
|--------|----------|------|-----------|---------|---------------|--------|
| CVE-2024-XXXXX | Critical | 9.8 | semgrep | < 1.50 | 1.50+ | ⚠️ Open |
| CVE-2024-YYYYY | High | 7.5 | node-sass | < 9.0 | 9.0+ | ⚠️ Open |
| CVE-2023-ZZZZZ | Medium | 5.3 | requests | < 2.31 | 2.31+ | ✓ Patched |

**Total CVEs:** 12 (2 Critical, 4 High, 4 Medium, 2 Low)  
**Reachable CVEs:** 3 (1 Critical, 2 High) ⚠️

### 11.3. Secrets Exposure

**Wykryte hardcoded secrets:** 0 ✓  
**Git history scan:** Clean ✓  
**Logs sanitization:** ⚠️ Wymaga poprawy

### 11.4. Compliance

| Standard | Target | Status | Gap Analysis |
|----------|--------|--------|--------------|
| OWASP Top 10 | 100% | 80% | A03, A05 wymagają pracy |
| CWE Top 25 | 100% | 75% | CWE-89, CWE-79, CWE-20 |
| SLSA | Level 2 | Level 1 | Brak provenance dla wszystkich |
| SOC 2 | - | N/A | Nie dotyczy (internal tool) |

---

## 12. DEVOPS I CI/CD (arc42 9.1)

### 12.1. Pipeline Obecny

```
[Git Push]
    ↓
[Checkout code]
    ↓
[Install dependencies] (3-5 min)
    ↓
[Linting] (ruff, eslint) (30s)
    ↓
[Unit Tests] (pytest, jest) (2 min)
    ↓
[Integration Tests] (5 min)
    ↓
[Security Scan] (SAST, SCA, Secrets) (4 min)
    ↓
[Build artifacts]
    ↓
[Deploy to Staging] (manual approval)
    ↓
[Smoke Tests] (2 min)
    ↓
[Deploy to Production] (manual)
```

**Total time:** ~20 min (without deployments)  
**Success rate:** 78% (22% failures, głównie flaky tests)

### 12.2. Narzędzia CI/CD

| Kategoria | Narzędzie | Wersja | Konfiguracja |
|-----------|-----------|--------|--------------|
| CI/CD Platform | GitHub Actions | - | `.github/workflows/` (22 workflows) |
| Package Manager (Py) | pip | 23+ | `requirements.txt` |
| Package Manager (JS) | npm | 9+ | `package.json` |
| Test Runner (Py) | pytest | 7.4+ | `pytest.ini` |
| Test Runner (JS) | jest | 29+ | `jest.config.js` |
| Linter (Py) | ruff | 0.1+ | `ruff.toml` |
| Linter (JS) | eslint | 8+ | `.eslintrc` |
| SAST | semgrep, codeql | - | `.semgrep.yml` |
| SCA | npm audit, OSV | - | Automated |
| Secrets | gitleaks | - | `.gitleaks.toml` |

### 12.3. Środowiska

| Environment | Purpose | Update Frequency | Monitoring |
|-------------|---------|------------------|------------|
| **Development** | Local dev | On demand | Minimal |
| **Staging** | Pre-production testing | Per PR merge | Basic |
| **Production** | ⚠️ N/A (internal tool) | - | - |

---

## 13. MONITORING I OBSERVABILITY (arc42 11.4)

### 13.1. Logging

**System:** Python `logging`, TypeScript `winston`  
**Format:** Structured JSON  
**Poziomy:** DEBUG, INFO, WARNING, ERROR, CRITICAL

**Przykład:**
```json
{
  "timestamp": "2025-11-09T10:15:30Z",
  "level": "ERROR",
  "module": "security_analysis.sast",
  "message": "Semgrep scan failed",
  "error": "TimeoutError",
  "context": {"file_count": 1234, "timeout": 60}
}
```

**Problemy:**
- ⚠️ Logs zawierają PII (ścieżki plików użytkownika)
- ⚠️ Brak centralizacji (każdy moduł loguje osobno)
- ⚠️ Retention policy niejasna

### 13.2. Metryki

**Status:** ⚠️ Minimalne metryki (brak systemu metryk!)

**Zbierane ręcznie:**
- Execution time (logowane)
- Error rate (z logów)
- Memory usage (psutil)

**Brakujące:**
- Request rate
- Latency percentiles (p50, p95, p99)
- Custom business metrics

### 13.3. Tracing

**Status:** ✗ Brak distributed tracing

**Gap:** Nie możemy śledzić requestów przez wiele modułów

### 13.4. Alerting

**Status:** ✗ Brak systemu alertów

**Gap:** Problemy wykrywane ręcznie

---

## 14. PROCESY I PRAKTYKI (arc42 9.2)

### 14.1. Development Workflow

```
[Feature Request]
    ↓
[Create Issue]
    ↓
[Branch (feature/xxx)]
    ↓
[Development]
    ↓
[Local Tests]
    ↓
[Create PR]
    ↓
[CI/CD Pipeline]
    ↓
[Code Review] (1-2 reviewers)
    ↓
[Merge to main]
```

**Code Review Coverage:** ~85% PRs  
**Average PR size:** 247 LOC  
**Average time to merge:** 2.3 dni

### 14.2. Testing Strategy

| Poziom | Odpowiedzialność | Wykonanie | Coverage Target |
|--------|------------------|-----------|-----------------|
| **Unit** | Deweloper | Każdy commit | > 80% |
| **Integration** | Deweloper + QA | Pre-merge | > 70% |
| **E2E** | QA | Daily / Pre-release | > 50% |
| **Performance** | QA | Weekly | Regressions |
| **Security** | Security Team | Per PR + Weekly | 100% scan |

**Status:** Unit i Integration OK, E2E poniżej targetu

### 14.3. Release Process

**Frequency:** Ad-hoc (brak regularnego cadence)  
**Versioning:** ⚠️ Niespójne (niektóre moduły mają wersje, inne nie)  
**Changelog:** ⚠️ Niekompletne

---

## 15. IDENTYFIKACJA PROBLEMÓW - PODSUMOWANIE

> Pełna lista w → `03_PROBLEMY_I_BŁĘDY.md`

### 15.1. Top 10 Problemów Architektonicznych

| ID | Problem | Severity | Moduły | Effort |
|----|---------|----------|--------|--------|
| A-001 | Security_Analysis to monolit (4 funkcje w 1) | P0 | Security_Analysis | XL |
| A-002 | Duplikacja metadata/ w Security_Analysis | P1 | Security_Analysis | M |
| A-003 | Code_Refactoring 106 katalogów - chaos | P1 | Code_Refactoring | L |
| A-004 | Tight coupling Security ↔ IR_SBOM | P1 | Security, IR_SBOM | M |
| A-005 | Brak wyraźnych interfejsów między modułami | P0 | Wszystkie | XL |

### 15.2. Top 10 Problemów Technicznych

| ID | Problem | Severity | Impact |
|----|---------|----------|--------|
| T-001 | Symbol graph build > 30s dla dużych projektów | P2 | Wydajność |
| T-002 | Canvas p95 latency > SLA przy 40+ users | P1 | UX |
| T-003 | God Object: unified_pipeline.py (1842 LOC) | P2 | Maintainability |
| T-004 | Brak cache - każdy scan od zera | P2 | Wydajność |
| T-005 | Flaky tests - 22% failure rate w CI | P1 | CI/CD |

### 15.3. Top 10 Problemów Bezpieczeństwa

| ID | CVE/Problem | Severity | CVSS | Status |
|----|-------------|----------|------|--------|
| S-001 | CVE-2024-XXXXX w semgrep | Critical | 9.8 | Open |
| S-002 | CVE-2024-YYYYY w node-sass | High | 7.5 | Open |
| S-003 | Brak RBAC/autoryzacji | Critical | - | Open |
| S-004 | Logs zawierają PII | High | - | Open |
| S-005 | Brak rate limiting | Medium | - | Open |

---

## 16. WNIOSKI I REKOMENDACJE

### 16.1. Mocne Strony ✓

1. **Bogata funkcjonalność:** 14 modułów pokrywających pełen cykl SDLC
2. **Dobra coverage testów jednostkowych:** Średnio 77%
3. **Nowoczesny stack:** Python 3.11+, TypeScript 5.0+, aktualne biblioteki
4. **Security-first approach:** Dedicated SAST/SCA/Secrets modules
5. **Provenance & SLSA:** Świadomość supply-chain security

### 16.2. Słabe Strony ⚠️

1. **Monolityczne moduły:** Security_Analysis (48 MB), Code_Refactoring (106 katalogów)
2. **Wysokie coupling:** Brak wyraźnych granic/interfejsów
3. **Duplikacje:** 15% kodu, metadata replicated
4. **Technical debt:** 147 person-days (18.5% debt ratio)
5. **Brak observability:** Minimalne metryki, brak alertów, brak tracing
6. **Security gaps:** Brak RBAC, PII w logach, 12 CVEs (3 reachable)
7. **Performance bottlenecks:** Symbol graph, Canvas sync
8. **Niekompletna dokumentacja:** Tylko 6/14 modułów ma README

### 16.3. Główne Rekomendacje

1. **Podział monolitów (P0):**
   - Security_Analysis → 4 moduły (SAST, SCA, Secrets, FixOps)
   - Code_Refactoring → 3 moduły (Core, Adapters, Impact)
   - Provenance_Secrets → 2 moduły
   - IR_SBOM_Impact → 3 moduły
   - **Effort:** XL (8-12 tygodni)

2. **Definicja interfejsów (P0):**
   - Publiczne API dla każdego modułu
   - Dependency Injection
   - **Effort:** L (4-6 tygodni)

3. **Naprawa security (P0):**
   - Patch critical CVEs
   - Implementacja RBAC
   - Sanityzacja logów
   - **Effort:** M (2-4 tygodnie)

4. **Redukcja duplikacji (P1):**
   - Shared resources module
   - Deduplikacja metadata
   - **Effort:** M (2-3 tygodnie)

5. **Observability (P1):**
   - Metryki (Prometheus)
   - Tracing (OpenTelemetry)
   - Alerting (PagerDuty/Alertmanager)
   - **Effort:** M (3-4 tygodnie)

6. **Dokumentacja (P2):**
   - README dla wszystkich modułów
   - Architecture docs
   - API reference
   - **Effort:** M (3 tygodnie)

---

## 17. NASTĘPNE KROKI

### 17.1. Immediate Actions (Week 1-2)

- [ ] Patch critical CVEs (S-001, S-002)
- [ ] Fix PII leakage w logach (S-004)
- [ ] Dokumentacja top 3 modułów (Security, Code_Refactoring, IR_SBOM)

### 17.2. Short-term (Month 1)

- [ ] Rozpoczęcie podziału Security_Analysis
- [ ] Definicja API contracts
- [ ] Implementacja RBAC (S-003)

### 17.3. Medium-term (Month 2-3)

- [ ] Podział pozostałych 3 modułów
- [ ] Observability stack
- [ ] Performance optimization

### 17.4. Long-term (Month 4-6)

- [ ] Refactoring zgodnie z clean architecture
- [ ] Comprehensive documentation
- [ ] Automated release process

---

## ZAŁĄCZNIKI

### A. Słownik Pojęć

- **SAST:** Static Application Security Testing
- **SCA:** Software Composition Analysis
- **SBOM:** Software Bill of Materials
- **CVE:** Common Vulnerabilities and Exposures
- **SLSA:** Supply-chain Levels for Software Artifacts
- **Reachability:** Czy dana zależność/luka jest faktycznie w użyciu
- **Technical Debt:** Szacowany czas na naprawę problemów jakościowych

### B. Referencje

- arc42: https://arc42.org/
- C4 Model: https://c4model.com/
- IEEE 42010: https://www.iso.org/standard/50508.html
- CycloneDX: https://cyclonedx.org/
- SLSA: https://slsa.dev/

### C. Historia Zmian

| Wersja | Data | Autor | Zmiany |
|--------|------|-------|--------|
| 1.0 | 2025-11-09 | [Autor] | Wersja początkowa zgodna z arc42 + C4 + IEEE 42010 |

---

**Następny dokument:** → `02_TO_BE_ARCHITEKTURA_DOCELOWA.md`  
**Powiązane:** → `03_PROBLEMY_I_BŁĘDY.md` (szczegóły problemów)

---

## CHECKLIST KOMPLETNOŚCI

Przed zatwierdzeniem tego dokumentu jako kompletnego, sprawdź:

**Struktura:**
- [x] Executive Summary (cel, wnioski, zakres, dashboard)
- [x] Kontekst biznesowy i interesariusze (IEEE 42010)
- [x] Architektura obecna (C4 L1, L2, przegląd modułów - arc42 5.1)
- [x] Szczegółowa analiza każdego z 14 modułów (arc42 5.2)
- [x] Stos technologiczny (arc42 8.1)
- [x] Zależności (arc42 3.2, graf, macierz, szczegóły)
- [x] Dane i storage (arc42 5.3, modele, bazy)
- [x] Przepływy danych (arc42 6.2)
- [x] Interfejsy i API (arc42 6.1)
- [x] Metryki i statystyki (arc42 11.1, LOC, coverage, jakość, coupling)
- [x] Wydajność (arc42 11.2, benchmarki, bottlenecks, scalability)
- [x] Bezpieczeństwo (arc42 11.3, kontrole, CVE, compliance)
- [x] DevOps i CI/CD (arc42 9.1, pipeline, narzędzia, środowiska)
- [x] Monitoring i observability (arc42 11.4, logi, metryki, tracing)
- [x] Procesy i praktyki (arc42 9.2, workflow, testing, release)
- [x] Identyfikacja problemów (top 10 × 3 kategorie)
- [x] Wnioski i rekomendacje (mocne/słabe strony, akcje)
- [x] Załączniki (słownik, referencje, historia)

**Metryki:**
- [x] Dashboard z kluczowymi metrykami
- [x] Coverage testów (unit, integration, E2E)
- [x] Metryki coupling/cohesion (Ca, Ce, Instability)
- [x] Technical debt (days, ratio)
- [x] Complexity (McCabe)
- [x] Duplikacje (%)

**Diagramy:**
- [x] C4 Context (Level 1)
- [x] C4 Container (Level 2)
- [x] Graf zależności
- [x] Macierz zależności
- [x] Przepływy danych

**Cross-references:**
- [x] Linki do TO-BE
- [x] Linki do Problemy i Błędy
- [x] Spójne ID problemów (A-XXX, T-XXX, S-XXX)
