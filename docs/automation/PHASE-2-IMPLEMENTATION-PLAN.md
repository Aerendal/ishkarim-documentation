# Phase 2 Automation - Implementation Plan

**Data:** 2025-12-29
**Status:** Implementation Started
**Based on:** PROPOZYCJA-2-Living-Documentation-Framework.md

---

## 1. Architektura

### 1.1. Komponenty

```
automation/
├── scripts/
│   ├── health_check.py          # Health check automation
│   ├── impact_propagation.py    # Impact propagation system
│   ├── document_parser.py       # YAML front-matter parser
│   └── utils.py                 # Common utilities
├── .github/
│   └── workflows/
│       └── living-docs-health.yml  # GitHub Action
├── config/
│   └── automation-config.yaml   # Configuration
└── README.md                    # Documentation
```

### 1.2. Technology Stack

- **Language:** Python 3.11+
- **Dependencies:**
  - `pyyaml` - YAML parsing
  - `python-frontmatter` - Markdown front-matter parsing
  - `gitpython` - Git operations
  - `rich` - Terminal output formatting
- **CI/CD:** GitHub Actions
- **Notifications:** GitHub Issues (MVP), Email/Slack (future)

---

## 2. Feature Breakdown

### 2.1. Health Check Script (`health_check.py`)

**Funkcjonalność:**
- Skanuje wszystkie dokumenty z Living Documentation metadata
- Wykonuje 7 health checks:
  1. **Freshness Check** - ostatnia modyfikacja vs threshold
  2. **Dependency Validity** - czy dependencies istnieją i są valid
  3. **Cross-Reference Consistency** - czy referencje są poprawne
  4. **Owner Assignment** - czy owner jest przypisany
  5. **Required Sections Completeness** - czy wymagane sekcje istnieją
  6. **Upstream Changes Pending** - czy są nieobsłużone zmiany upstream
  7. **Satellite Completeness** - czy satellites są kompletne
- Generuje raport (JSON, Markdown, Terminal)
- Exit code: 0 = wszystko OK, 1 = są warning/critical

**Usage:**
```bash
python automation/scripts/health_check.py --format markdown > health-report.md
python automation/scripts/health_check.py --format terminal  # Pretty output
python automation/scripts/health_check.py --format json > health-report.json
python automation/scripts/health_check.py --critical-only  # Only critical issues
```

### 2.2. Impact Propagation Script (`impact_propagation.py`)

**Funkcjonalność:**
- Wykrywa zmiany w dokumentach (git diff)
- Analizuje dependency graph
- Identyfikuje impacted downstream documents
- Aktualizuje `cross_reference_status.upstream_changes_pending`
- Tworzy GitHub Issues dla high severity changes (opcjonalne)
- Generuje raport zmian

**Usage:**
```bash
# Analyze changes since last commit
python automation/scripts/impact_propagation.py

# Analyze changes between commits
python automation/scripts/impact_propagation.py --from-commit abc123 --to-commit def456

# Dry run (don't modify files)
python automation/scripts/impact_propagation.py --dry-run

# Create GitHub issues for high severity
python automation/scripts/impact_propagation.py --create-issues
```

### 2.3. Document Parser (`document_parser.py`)

**Funkcjonalność:**
- Parser YAML front-matter z markdown files
- Ekstrakcja Living Documentation metadata
- Walidacja struktury metadata
- Helper functions dla innych skryptów

**API:**
```python
from document_parser import DocumentParser

parser = DocumentParser()
doc = parser.parse("engineering/requirements/prd.md")

print(doc.id)              # "PRD-001-V2"
print(doc.version)         # "2.0.0"
print(doc.status)          # "approved"
print(doc.health_status)   # "healthy"
print(doc.dependencies)    # List of dependency IDs
print(doc.impacts)         # List of impacted document IDs
```

### 2.4. GitHub Action (`living-docs-health.yml`)

**Trigger:**
- Schedule: Daily at 02:00 UTC
- On push to main (dla PRD, TDD, Vision, ADRs)
- Manual trigger (workflow_dispatch)

**Steps:**
1. Checkout repository
2. Setup Python 3.11
3. Install dependencies
4. Run health check script
5. Post results as PR comment (if triggered by PR)
6. Create GitHub Issue if critical issues found
7. Upload health report as artifact

---

## 3. Implementation Phases

### Phase 2.1: Core Scripts (Week 1)
- ✅ Document parser
- ✅ Health check script (7 checks)
- ✅ Impact propagation script (basic)
- ✅ Unit tests

### Phase 2.2: GitHub Integration (Week 2)
- ✅ GitHub Action workflow
- ✅ Issue creation for critical health issues
- ✅ PR comment integration

### Phase 2.3: Enhancement (Week 3 - Optional)
- 🔄 Email notifications
- 🔄 Slack webhook integration
- 🔄 Web dashboard (React + D3.js)

---

## 4. Configuration File

**`config/automation-config.yaml`:**

```yaml
# Living Documentation Automation Configuration

# Health Check Thresholds
health_check:
  freshness_thresholds:
    prd: 90          # days
    tdd: 90
    adr: 365
    vision: 180
    business_case: 90
    default: 90

  severity_levels:
    critical: ["required_sections_missing", "owner_unassigned", "broken_dependencies"]
    warning: ["stale_document", "missing_satellites", "pending_upstream_changes"]
    info: ["all_healthy"]

# Impact Propagation Rules
impact_propagation:
  version_bump_triggers:
    major:
      - "breaking_change"
      - "scope_pivoted"
      - "section_removed"
    minor:
      - "section_added"
      - "dependency_added"
      - "scope_expanded"
    patch:
      - "typo_fix"
      - "formatting_change"
      - "clarification"

  severity_mapping:
    major: "high"
    minor: "medium"
    patch: "low"

# GitHub Integration
github:
  create_issues: true
  issue_labels: ["living-documentation", "health-check"]
  assignees: []  # Empty = use document owner

# Notification Channels (Future)
notifications:
  email:
    enabled: false
    smtp_server: "smtp.example.com"
    from: "ishkarim-bot@example.com"

  slack:
    enabled: false
    webhook_url: ""
```

---

## 5. Success Criteria

**Phase 2 jest zakończone gdy:**
- ✅ Health check script działa dla wszystkich 6 dokumentów
- ✅ Impact propagation wykrywa zmiany i aktualizuje metadata
- ✅ GitHub Action wykonuje się codziennie
- ✅ Dokumentacja użycia jest kompletna
- ✅ Unit tests coverage > 80%
- ✅ Zero manual intervention dla daily health checks

---

## 6. Timeline

- **Day 1:** Core scripts (parser, health check, impact propagation) ✅ IN PROGRESS
- **Day 2:** GitHub Action integration
- **Day 3:** Testing & documentation
- **Day 4:** Deployment & monitoring

---

## 7. Metrics

**Metryki sukcesu (zgodnie z PROPOZYCJA-2):**
- M1: Document Freshness Rate > 80%
- M2: Stale Document Detection Rate > 95%
- M4: Cross-Reference Consistency Rate > 98%
- M5: Impact Propagation Acknowledgment Rate > 90%

---

**Next Steps:** Implementacja core scripts
