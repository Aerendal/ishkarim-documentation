# Living Documentation Framework - Automation

Automatyczne narzędzia dla Living Documentation Framework (Phase 2).

## 🎯 Funkcjonalność

### 1. Health Check (`health_check.py`)

Automatyczne sprawdzanie zdrowia dokumentów - 7 kontroli:

1. **Freshness Check** - czy dokument był ostatnio modyfikowany
2. **Dependency Validity** - czy zależności istnieją i są aktualne
3. **Cross-Reference Consistency** - czy referencje są poprawne
4. **Owner Assignment** - czy dokument ma przypisanego właściciela
5. **Required Sections Completeness** - czy wymagane sekcje są kompletne
6. **Upstream Changes Pending** - czy są nie obsłużone zmiany upstream
7. **Satellite Completeness** - czy dokumenty satelitarne są kompletne

### 2. Document Parser (`document_parser.py`)

Parser dokumentów markdown z YAML front-matter i Living Documentation metadata.

---

## 📦 Instalacja

### Wymagania

- Python 3.11+
- Git

### Setup

```bash
# 1. Przejdź do katalogu automation
cd docs/automation

# 2. Zainstaluj zależności
pip install -r requirements.txt

# 3. Gotowe!
```

---

## 🚀 Użycie

### Health Check

**Format terminalowy (pretty output):**
```bash
cd docs
python automation/scripts/health_check.py --format terminal
```

**Format Markdown (do raportu):**
```bash
python automation/scripts/health_check.py --format markdown > health-report.md
```

**Format JSON (do CI/CD):**
```bash
python automation/scripts/health_check.py --format json > health-report.json
```

**Tylko dokumenty z critical issues:**
```bash
python automation/scripts/health_check.py --critical-only
```

### Document Parser

**Z linii poleceń:**
```bash
python automation/scripts/document_parser.py engineering/requirements/prd.md
```

**Z kodu Python:**
```python
from document_parser import DocumentParser

parser = DocumentParser()

# Parse pojedynczego dokumentu
doc = parser.parse("engineering/requirements/prd.md")
print(doc.id, doc.version, doc.status)

# Parse wszystkich dokumentów w katalogu
documents = parser.parse_directory(".", skip_templates=True)

# Znajdź dokument po ID
doc = parser.find_document_by_id("PRD-001-V2")
```

---

## 📋 Przykłady

### Przykład 1: Daily Health Check

```bash
#!/bin/bash
# daily-health-check.sh

cd /path/to/docs
python automation/scripts/health_check.py --format markdown > /tmp/health-report.md

# Jeśli są problemy (exit code 1), wyślij powiadomienie
if [ $? -ne 0 ]; then
    echo "Health check failed! Check /tmp/health-report.md"
    # Wyślij email lub Slack notification
fi
```

### Przykład 2: CI/CD Integration (GitHub Actions)

```yaml
name: Living Documentation Health Check

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC
  push:
    paths:
      - 'engineering/**/*.md'
      - 'pre-production/**/*.md'

jobs:
  health-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          cd docs/automation
          pip install -r requirements.txt

      - name: Run health check
        run: |
          cd docs
          python automation/scripts/health_check.py --format markdown > health-report.md

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: health-report
          path: docs/health-report.md

      - name: Create issue if critical
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: '🔴 Living Documentation Health Check Failed',
              body: 'Critical health issues detected. Check workflow artifacts.',
              labels: ['living-documentation', 'health-check']
            })
```

### Przykład 3: Parse dokumentów programatycznie

```python
from document_parser import DocumentParser

parser = DocumentParser()

# Parse wszystkich dokumentów
documents = parser.parse_directory(".", skip_templates=True)

# Filtruj dokumenty z Living Doc metadata
living_docs = [doc for doc in documents if doc.has_living_doc_metadata]

print(f"Found {len(living_docs)} Living Documentation documents")

# Analiza statusów
status_counts = {}
for doc in living_docs:
    status_counts[doc.status] = status_counts.get(doc.status, 0) + 1

print("Status distribution:", status_counts)

# Znajdź dokumenty z warnings
for doc in living_docs:
    if doc.health_status == "warning":
        print(f"{doc.id}: {doc.health_status}")
```

---

## ⚙️ Konfiguracja

Konfiguracja w pliku `config/automation-config.yaml`:

```yaml
health_check:
  freshness_thresholds:
    prd: 90          # PRD powinien być aktualizowany co 90 dni
    tdd: 90
    adr: 365         # ADRy są długożyciowe
    vision: 180      # Vision co pół roku
    default: 90
```

---

## 📊 Health Check Output

### Terminal Format

```
┌─────────────────────────────────────────┐
│ Living Documentation Health Summary     │
├─────────┬───────────────────────────────┤
│ Status  │                Count          │
├─────────┼───────────────────────────────┤
│ 🟢 Healthy │                    4       │
│ 🟡 Warning │                    2       │
│ 🔴 Critical│                    0       │
│ Total      │                    6       │
└─────────┴───────────────────────────────┘

┌────────┬──────────────┬────────┬─────────────────────────┐
│ Status │ Document ID  │ Checks │ Issues                  │
├────────┼──────────────┼────────┼─────────────────────────┤
│   🟢   │ PRD-001-V2   │  7/7   │ -                       │
│   🟢   │ VISION-001   │  7/7   │ -                       │
│   🟡   │ TDD-001-V2   │  5/7   │ Required Sections, ...  │
└────────┴──────────────┴────────┴─────────────────────────┘
```

### Markdown Format

```markdown
# Living Documentation Health Report

**Generated:** 2025-12-29T...

## Summary

- **Total Documents:** 6
- 🟢 **Healthy:** 4
- 🟡 **Warning:** 2
- 🔴 **Critical:** 0

## Document Health

### 🟢 PRD-001-V2 - Product Requirements Document

**File:** `engineering/requirements/prd.md`
**Status:** HEALTHY
**Checks:** 7/7 healthy, 0 warnings, 0 critical

### 🟡 TDD-001-V2 - Technical Design Document

**File:** `engineering/requirements/tdd.md`
**Status:** WARNING
**Checks:** 5/7 healthy, 2 warnings, 0 critical

**Issues:**
- 🟡 **Required Sections Completeness:** Missing 2 sections (85%)
- 🟡 **Upstream Changes Pending:** 1 high severity upstream changes pending
```

---

## 🔧 Troubleshooting

### Problem: ModuleNotFoundError: No module named 'frontmatter'

**Rozwiązanie:**
```bash
pip install -r requirements.txt
```

### Problem: FileNotFoundError: Document not found

**Rozwiązanie:**
Upewnij się, że uruchamiasz skrypt z katalogu `docs/`:
```bash
cd docs/
python automation/scripts/health_check.py
```

### Problem: Health check shows "No Living Documentation documents found"

**Rozwiązanie:**
Sprawdź czy dokumenty mają rozszerzone metadane Living Documentation (version_metadata, lifecycle, document_health).

---

## 📈 Roadmap

- [x] Phase 2.1: Core scripts (parser, health check)
- [ ] Phase 2.2: Impact propagation script
- [ ] Phase 2.3: GitHub Action workflow
- [ ] Phase 2.4: Email/Slack notifications
- [ ] Phase 2.5: Web dashboard

---

## 📝 License

Part of Ishkarim Documentation Management System.
