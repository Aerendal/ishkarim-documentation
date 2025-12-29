# Plan Pracy: Dokończenie Living Documentation Framework

**Data utworzenia**: 2025-12-29
**Status**: Aktywny plan pracy
**Cel**: Cleanup warnings, rozszerzenie pozostałych dokumentów, walidacja integralności

---

## Status Obecny (Checkpoint)

### Zakończone (23/23 dokumentów z metadata):
- ✅ 10 ADRs (ADR-001 do ADR-010) - all v1.0.0 approved
- ✅ 1 TDD (TDD-001-V2) - v0.9.0 evolving
- ✅ 1 Business Case (BIZ-CASE-001) - v0.5.0 draft
- ✅ 1 PRD (PRD-001-V2) - v2.0.0 approved
- ✅ 1 Vision (VISION-001) - v1.0.0 approved
- ✅ 6 Components (COMP-001 to COMP-006) - all v0.1.0 draft
- ✅ 1 API Spec (API-SPEC-001) - v1.0.0 approved
- ✅ 1 Data Models (DATA-MODEL-001) - v1.0.0 approved
- ✅ 1 Schemas (SCHEMA-001) - v1.0.0 approved **[HEALTHY - pierwszy bez warnings!]**

### Wykryte ostrzeżenia (do rozwiązania):
1. **CONCEPTS-001-V2** - referenced przez DATA-MODEL-001, ale nie istnieje (optional dependency)
2. **EXEC-SUM-001** - referenced przez BIZ-CASE-001 i VISION-001, ale nie istnieje
3. **Evidence validation** - sprawdzić które E-xxx dokumenty faktycznie istnieją

### Pozostałe dokumenty do rozszerzenia:
- Roadmap (pre-production/roadmap.md)
- Inne dokumenty w katalogach (jeśli istnieją)

---

## FAZA 1: Cleanup Warnings (Priorytet: KRYTYCZNY)

### Cel: Rozwiązać wszystkie invalid dependencies

### Task 1.1: Zbadaj CONCEPTS-001-V2 dependency

**Krok 1.1.1: Read DATA-MODEL-001 dependency section**
```bash
Akcja: Read engineering/data-models/DATA-MODEL-001.md (linie 8-16)
Cel: Sprawdzić dokładnie jak CONCEPTS-001-V2 jest referenced
Output: Zapisać w pamięci co dokładnie mówi dependency
```

**Krok 1.1.2: Search for CONCEPTS files**
```bash
Akcja: Glob pattern "**/*CONCEPT*.md" w całym repozytorium
Cel: Znaleźć wszystkie pliki z "CONCEPT" w nazwie
Output: Lista znalezionych plików
```

**Krok 1.1.3: Read znalezione CONCEPTS files (jeśli istnieją)**
```bash
Akcja: Read każdy znaleziony plik CONCEPTS
Cel: Sprawdzić czy któryś to CONCEPTS-001-V2 lub podobny
Output: ID i status każdego pliku
```

**Krok 1.1.4: Decyzja**
```
Opcja A: Jeśli CONCEPTS-001-V2 istnieje ale ma inną nazwę
  → Edit DATA-MODEL-001.md: Popraw dependency ID na prawidłowy
  → Commit: "fix: Popraw CONCEPTS dependency ID w DATA-MODEL-001"

Opcja B: Jeśli CONCEPTS-001-V2 nie istnieje wcale
  → Edit DATA-MODEL-001.md: Usuń całą dependency na CONCEPTS-001-V2
  → Read DATA-MODEL-001.md ponownie: Zweryfikuj że dependency usunięta
  → Update document_health.checks.Dependency Validity: status = "healthy"
  → Commit: "fix: Usuń optional CONCEPTS-001-V2 dependency z DATA-MODEL-001"

Opcja C: Jeśli CONCEPTS jest potrzebny
  → Utworzyć CONCEPTS-001-V2.md z Living Documentation metadata
  → (TO byłoby DUŻE zadanie - prawdopodobnie Opcja B jest lepsza)
```

---

### Task 1.2: Zbadaj EXEC-SUM-001 dependency

**Krok 1.2.1: Read BIZ-CASE-001 dependencies**
```bash
Akcja: Read pre-production/business-case.md (linie 12-14)
Cel: Sprawdzić jak EXEC-SUM-001 jest referenced w BIZ-CASE
Output: Dependency definition
```

**Krok 1.2.2: Read VISION-001 dependencies**
```bash
Akcja: Read pre-production/vision.md (sekcja dependencies)
Cel: Sprawdzić jak EXEC-SUM-001 jest referenced w VISION
Output: Dependency definition
```

**Krok 1.2.3: Search for EXEC-SUM files**
```bash
Akcja: Glob pattern "**/*EXEC*SUM*.md"
Cel: Znaleźć czy EXEC-SUM istnieje pod inną nazwą
Output: Lista znalezionych plików (jeśli istnieją)
```

**Krok 1.2.4: Decyzja**
```
Opcja A: Utworzyć EXEC-SUM-001 (jeśli executive summary jest potrzebny)
  → Krok 1: Write pre-production/executive-summary.md z podstawową strukturą
  → Krok 2: Read ADRs, PRD, Vision: Zebrać kluczowe punkty dla executive summary
  → Krok 3: Write EXEC-SUM-001 z Living Documentation metadata
  → Krok 4: Edit BIZ-CASE-001: Update dependency health check (valid)
  → Krok 5: Read BIZ-CASE-001 ponownie: Verify health updated
  → Krok 6: Edit VISION-001: Update dependency health check (valid)
  → Krok 7: Read VISION-001 ponownie: Verify health updated
  → Commit wszystko: "feat: Dodaj EXEC-SUM-001 Executive Summary"

Opcja B: Usunąć dependency (jeśli executive summary niepotrzebny)
  → Krok 1: Edit BIZ-CASE-001: Usuń EXEC-SUM-001 z dependencies
  → Krok 2: Read BIZ-CASE-001 ponownie: Verify usunięte
  → Krok 3: Edit BIZ-CASE-001: Update document_health (dependency valid)
  → Krok 4: Edit VISION-001: Usuń EXEC-SUM-001 z dependencies
  → Krok 5: Read VISION-001 ponownie: Verify usunięte
  → Krok 6: Edit VISION-001: Update document_health (dependency valid)
  → Commit: "fix: Usuń niepotrzebny EXEC-SUM-001 dependency"
```

**Rekomendacja**: Opcja B (usuń dependency) - Executive Summary może być sekcją w Vision lub BizCase, nie wymaga osobnego dokumentu.

---

## FAZA 2: Rozszerzenie Pozostałych Dokumentów (Priorytet: ŚREDNI)

### Task 2.1: Extend Roadmap

**Krok 2.1.1: Search for Roadmap**
```bash
Akcja: Glob pattern "**/*roadmap*.md" (case insensitive)
Cel: Znaleźć plik Roadmap
Output: Ścieżka do pliku lub info że nie istnieje
```

**Krok 2.1.2: Read Roadmap (jeśli istnieje)**
```bash
Akcja: Read {roadmap_path}
Cel: Zrozumieć strukturę i zawartość Roadmap
Output: Obecna struktura frontmatter, sections, brak metadata?
```

**Krok 2.1.3: Extend Roadmap z metadata (jeśli istnieje)**
```bash
Krok 1: Edit {roadmap_path}: Dodaj Living Documentation Framework metadata
  - status: approved lub draft (zależnie od zawartości)
  - version: 1.0.0 lub 0.1.0
  - dependencies: VISION-001 (roadmap wynika z vision)
  - review_frequency: quarterly (roadmap often updated)

Krok 2: Read {roadmap_path} ponownie: Verify metadata dodane

Krok 3: Commit: "docs: Rozszerz Roadmap o Living Documentation Framework metadata"
```

**Krok 2.1.4: Create Roadmap (jeśli nie istnieje)**
```bash
Jeśli Roadmap nie istnieje, zdecydować czy tworzyć:
  Opcja A: Utworzyć na podstawie Vision
  Opcja B: Pominąć (Roadmap może być sekcją w Vision)
```

---

### Task 2.2: Inventory All Remaining Documents

**Krok 2.2.1: List all markdown files**
```bash
Akcja: Glob pattern "**/*.md" w docs/
Cel: Pełna lista wszystkich plików .md
Output: Lista ścieżek (może być 100+ plików)
```

**Krok 2.2.2: Filter files bez Living Documentation metadata**
```bash
Akcja: Dla każdego pliku z listy:
  - Grep pattern "# === Living Documentation Framework"
  - Jeśli nie znaleziono → dodaj do listy "files without metadata"

Cel: Znaleźć wszystkie pliki które NIE mają metadata
Output: Lista plików do potencjalnego rozszerzenia
```

**Krok 2.2.3: Categorize remaining files**
```bash
Kategorie:
1. Templates (templates/**) - POMIŃ (templates nie potrzebują metadata)
2. Examples (examples/**) - POMIŃ (examples mogą nie mieć metadata)
3. Satellites (satellites/**) - EVALUATE (evidence/approvals/etc. mogą potrzebować)
4. Core docs (engineering/**, pre-production/**) - EXTEND (jeśli important)
5. Canvas files (*.canvas) - POMIŃ (Obsidian canvas, nie markdown docs)
```

**Krok 2.2.4: Priorytetyzacja**
```
HIGH priority:
- Engineering docs (architecture, decisions, requirements)
- Pre-production docs (business case, vision, roadmap)
- Evidence docs (E-xxx series) - jeśli są główne artifacts

MEDIUM priority:
- Implementation plans
- Test plans
- Deployment guides

LOW priority:
- Examples
- Templates
- Research notes
```

---

## FAZA 3: Evidence Validation (Priorytet: ŚREDNI)

### Cel: Sprawdzić które E-xxx evidence documents faktycznie istnieją

### Task 3.1: Extract all evidence IDs from documents

**Krok 3.1.1: Search all evidence_ids in metadata**
```bash
Akcja: Grep pattern "evidence_ids:" w całym docs/
Cel: Znaleźć wszystkie linie z evidence_ids arrays
Output: Lista wszystkich referenced E-xxx IDs
```

**Krok 3.1.2: Extract unique evidence IDs**
```bash
Akcja: Parse output z 3.1.1
  - Regex: E-\d{3} (E-001, E-145, etc.)
  - Unique sort

Cel: Lista wszystkich unikalnych E-xxx IDs referenced w dokumentach
Output: Sorted lista np. E-001, E-008, E-140, E-141, E-145, ...
```

**Krok 3.1.3: List actual evidence files**
```bash
Akcja: Glob pattern "satellites/evidence/E-*.md"
Cel: Znaleźć które E-xxx pliki faktycznie istnieją
Output: Lista istniejących plików
```

**Krok 3.1.4: Compare referenced vs actual**
```bash
Akcja: Porównaj listy z 3.1.2 i 3.1.3
Cel: Znaleźć:
  - Referenced ale missing (E-xxx w evidence_ids ale plik nie istnieje)
  - Existing ale unreferenced (plik istnieje ale nie ma references)

Output:
  MISSING: [E-001, E-042, ...] (referenced but file missing)
  ORPHANED: [E-999, ...] (file exists but no references)
```

**Krok 3.1.5: Decyzja per missing evidence**
```
Dla każdego MISSING evidence:

Opcja A: Evidence jest placeholder (nie krytyczne)
  → Update document: Usuń E-xxx z evidence_ids
  → Lub dodaj note: "E-xxx: Planned evidence, not yet created"

Opcja B: Evidence jest krytyczne
  → Utworzyć stub E-xxx.md z basic metadata
  → Lub odnaleźć evidence pod inną nazwą i poprawić reference

Opcja C: Evidence niepotrzebne
  → Usuń całkowicie z evidence_ids
```

---

## FAZA 4: Final Audit & Report (Priorytet: NISKI)

### Task 4.1: Generate Coverage Report

**Krok 4.1.1: Count documents by type**
```bash
Akcja: Grep all "type:" fields in frontmatter
Cel: Policzyć ile dokumentów każdego typu
Output:
  - adr: 10
  - tdd: 1
  - prd: 1
  - component: 6
  - api-spec: 1
  - data-model: 1
  - schema: 1
  - vision: 1
  - business-case: 1
  TOTAL: 23
```

**Krok 4.1.2: Count documents by status**
```bash
Akcja: Grep all "status:" fields
Cel: Breakdown by status
Output:
  - approved: X documents
  - draft: Y documents
  - evolving: Z documents
```

**Krok 4.1.3: Count health status**
```bash
Akcja: Grep "document_health:\n  status:"
Cel: How many healthy vs warning
Output:
  - healthy: 1 (SCHEMA-001)
  - warning: 22
```

**Krok 4.1.4: Write COVERAGE-REPORT.md**
```bash
Akcja: Write docs/COVERAGE-REPORT.md
Zawartość:
  - Document Count Summary
  - Status Breakdown
  - Health Status Summary
  - Remaining Warnings List
  - Coverage Percentage by Category
  - Recommendations for Next Steps
```

---

## STRATEGIA UTRZYMANIA KONTEKSTU

### Zasady podczas długich sesji edycji:

1. **Read Before Edit**
   - Zawsze przeczytaj plik PRZED edycją
   - Sprawdź obecną strukturę, ostatnie zmiany
   - Zidentyfikuj gdzie dokładnie dodać metadata

2. **Read After Edit**
   - Po każdej edycji przeczytaj zmieniony plik ponownie
   - Verify że zmiany są poprawne
   - Check że nie zepsuło się formatowanie YAML

3. **Checkpoint Every 3-5 Files**
   - Co 3-5 plików: git commit
   - Zapisz aktualny stan pracy
   - W commit message: podsumuj co zostało zrobione

4. **Re-read Context Files**
   - Jeśli edytujesz wiele dependencies:
     - Co 5-10 edycji przeczytaj główny context file ponownie
     - Przypomni sobie overall structure

5. **Track Progress Explicitly**
   - Użyj TodoWrite dla każdego major task
   - Mark completed po każdym checkpoint
   - To pomaga wrócić do pracy po przerwaniu

6. **Limit Scope per Session**
   - Nie próbuj zrobić wszystkiego naraz
   - 1 FAZA = 1 sesja pracy (max 10-15 plików)
   - Po każdej FAZIE: commit, push, podsumowanie

---

## EXECUTION ORDER (Rekomendowane)

### Sesja 1: Cleanup CONCEPTS (15-30 min)
```
1. Read DATA-MODEL-001 dependencies
2. Search for CONCEPTS files
3. Decide: usunąć dependency (prawdopodobnie)
4. Edit DATA-MODEL-001: usuń CONCEPTS-001-V2
5. Read DATA-MODEL-001: verify
6. Commit + push
```

### Sesja 2: Cleanup EXEC-SUM (15-30 min)
```
1. Read BIZ-CASE-001 dependencies
2. Read VISION-001 dependencies
3. Search for EXEC-SUM files
4. Decide: usunąć dependencies (prawdopodobnie)
5. Edit BIZ-CASE-001: usuń EXEC-SUM-001
6. Read BIZ-CASE-001: verify
7. Edit VISION-001: usuń EXEC-SUM-001
8. Read VISION-001: verify
9. Commit + push
```

### Sesja 3: Extend Roadmap (30-60 min)
```
1. Search for roadmap.md
2. Read roadmap.md (jeśli istnieje)
3. Edit roadmap.md: dodaj metadata
4. Read roadmap.md: verify
5. Commit + push
```

### Sesja 4: Evidence Validation (60-90 min)
```
1. Grep all evidence_ids
2. Extract unique E-xxx IDs
3. List actual E-*.md files
4. Compare lists
5. Decide per missing evidence
6. Edit documents: fix evidence references
7. Commit + push
```

### Sesja 5: Final Audit (30-60 min)
```
1. Count documents by type/status/health
2. Write COVERAGE-REPORT.md
3. Commit + push
4. Celebrate! 🎉
```

---

## QUICK REFERENCE: Read Patterns

### Przed edycją dependency:
```bash
Read {file} (linie dependencies section)
→ Understand current dependencies
→ Note which IDs are referenced
```

### Przed edycją health check:
```bash
Read {file} (linie document_health section)
→ Check current status
→ Note which checks are warning
```

### Po każdej edycji:
```bash
Read {file} (całość lub edited section)
→ Verify changes correct
→ Check YAML syntax valid
```

### Co 5 plików:
```bash
git status
git diff
→ Review accumulated changes
→ Commit if sensible checkpoint
```

---

## PRIORYTETYZACJA

### MUST DO (Sesja 1-2):
- ✅ Cleanup CONCEPTS-001-V2 dependency
- ✅ Cleanup EXEC-SUM-001 dependency
- Cel: Rozwiązać wszystkie invalid dependencies warnings

### SHOULD DO (Sesja 3):
- ✅ Extend Roadmap (jeśli istnieje)
- Cel: 100% coverage core documents

### NICE TO HAVE (Sesja 4-5):
- ✅ Evidence validation
- ✅ Final audit report
- Cel: Complete documentation system health

---

## NOTES

- **Zachowaj context**: Read before edit, read after edit, checkpoint frequently
- **Nie śpiesz się**: Lepiej 5 sesji po 30 min niż 1 sesja 2.5h bez checkpointów
- **Commit often**: Co 3-5 plików lub co 1 major task
- **Verify changes**: Zawsze re-read po edit żeby złapać błędy
- **Ask if unsure**: Jeśli decision unclear (create vs delete), ask user

---

**Ostatnia aktualizacja**: 2025-12-29
**Następny krok**: Rozpocznij Sesję 1 (Cleanup CONCEPTS)
