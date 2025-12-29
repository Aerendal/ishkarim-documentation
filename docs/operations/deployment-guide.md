---
id: DEPLOYMENT-001
title: "Przewodnik Wdrożenia - System Dokumentacji Semantycznej"
type: deployment-guide
status: draft
created: 2025-12-26

dependencies:
  - id: TDD-001-V2
    type: requires
    reason: "Wdrożenie oparte na designie architektury"
  - id: TEST-PLAN-001
    type: requires
    status_constraint: [all-tests-passed]
    reason: "Nie można wdrożyć bez zaliczonych testów"

evidence_ids:
  - E-165
---

# Przewodnik Wdrożenia

## Wymagania Wstępne

### Wymagania Systemowe
- **OS**: Linux, macOS, lub Windows 10+
- **Python**: 3.11 lub wyższy
- **RAM**: 4GB minimum, 8GB zalecane
- **Dysk**: 500MB dla aplikacji, 10GB+ dla workspace dokumentacji

### Zależności
```bash
# Instalacja z PyPI
pip install semantic-docs

# Lub ze źródeł
git clone https://github.com/org/semantic-docs.git
cd semantic-docs
pip install -e .
```

## Kroki Instalacji

### Krok 1: Instalacja Zależności Python
```bash
pip install -r requirements.txt
```

**Kluczowe pakiety**:
- PySide6 >= 6.5.0
- networkx >= 3.2.0
- pydantic >= 2.5.0
- python-frontmatter >= 1.0.0
- markdown-it-py >= 3.0.0
- watchdog >= 3.0.0

### Krok 2: Inicjalizacja Workspace
```bash
semantic-docs init /path/to/docs

# Tworzy strukturę:
# /path/to/docs/
#   ├── pre-production/
#   ├── engineering/
#   ├── implementation/
#   ├── operations/
#   ├── satellites/
#   └── .semantic/
#       ├── config.yaml
#       └── index.db (SQLite)
```

### Krok 3: Konfiguracja
Edytuj `.semantic/config.yaml`:
```yaml
workspace:
  root: /path/to/docs
  watch_enabled: true

parser:
  markdown_extensions:
    - tables
    - fenced_code
    - yaml_frontmatter

validator:
  schemas_path: ./schemas/document_types.yaml
  strict_mode: true

graph:
  layout: cola  # cola, dagre, cose
  max_nodes: 1000

storage:
  sqlite_path: .semantic/index.db
  fts5_enabled: true
  rebuild_on_startup: false

gui:
  theme: dark  # dark, light
  font_size: 12
```

### Krok 4: Budowanie Indeksu
```bash
semantic-docs index --rebuild

# Output:
# Indeksowanie 43 dokumentów...
# [████████████████████] 43/43 (100%)
# Zaindeksowane w 2.3s
# Zbudowany graf: 43 nodes, 87 edges
# Wykryte luki: 14 (7 critical)
```

### Krok 5: Uruchomienie GUI
```bash
semantic-docs gui

# Lub tryb CLI:
semantic-docs analyze /path/to/docs
```

## Weryfikacja

### Sprawdzenia Post-Deployment
```bash
# Test parsera
semantic-docs parse /path/to/docs/engineering/prd-v2.md

# Test validatora
semantic-docs validate /path/to/docs/engineering/prd-v2.md

# Test grafu
semantic-docs graph --show-cycles

# Test luk
semantic-docs gaps --severity critical
```

**Oczekiwany output**:
- ✅ Wszystkie docs sparsowane (0 błędów)
- ✅ Walidacja: 43/43 zaliczone
- ✅ Graf: 0 cykli wykrytych
- ✅ Luki: 14 znalezionych, 7 critical

## Rollback

Jeśli deployment się nie powiedzie:
```bash
# Przywróć poprzednią wersję
pip install semantic-docs==<previous-version>

# Przebuduj indeks
semantic-docs index --rebuild

# Weryfikuj
semantic-docs --version
```

## Troubleshooting

**Problem**: GUI nie uruchamia się
**Rozwiązanie**: Sprawdź instalację PySide6
```bash
python -c "import PySide6; print(PySide6.__version__)"
```

**Problem**: Indeks SQLite uszkodzony
**Rozwiązanie**: Przebuduj
```bash
rm .semantic/index.db
semantic-docs index --rebuild
```

**Problem**: Degradacja wydajności
**Rozwiązanie**: Sprawdź liczbę docs, przebuduj FTS5
```bash
semantic-docs index --rebuild --optimize
```

## Powiązane Dokumenty
- [TDD-001-V2](../engineering/tdd-v2.md)
- [TEST-PLAN-001](../implementation/test-plan.md)
- [RUNBOOK-001](#) (procedury operacyjne)
