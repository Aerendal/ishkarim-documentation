---
id: CONCEPTS-001-MIGRATION-GUIDE
title: "Migration Guide: V1 → V2 Proof System"
type: migration-guide
parent: CONCEPTS-001-V2
domain: engineering
status: draft
created: 2025-12-26
---

# Migration Guide: CONCEPTS-001-V1 → CONCEPTS-001-V2

← [Powrót do CONCEPTS-V2](./koncepcje-v2.md) | [Zobacz też: DIFF Report](./CONCEPTS-001-DIFF-REPORT.md)

---

## Przegląd

Ten przewodnik pokazuje **krok po kroku** jak przepisać dokumenty z V1 (tradycyjne podejście) do V2 (proof system).

### Kogo to dotyczy?

- **Istniejące projekty** z dokumentacją V1 (ADR, RFC, PRD napisane przed 2025-12-26)
- **Zespoły migrujące** do proof system approach
- **Tech Writers** aktualizujący dokumentację

### Opcje Migracji

| Opcja | Zakres | Timeline | Effort | Zalecane dla |
|-------|--------|----------|--------|--------------|
| **A: Rewizja kompletna** | Wszystkie docs V1 → V2 | 2-4 tygodnie | Wysoki | Critical projects, regulated industries |
| **B: Przyrostowa** | Nowe docs = V2, stare = V1 (deprecated) | Ongoing | Niski | Non-critical projects, small teams |
| **C: Hybrydowa** | Critical docs → V2, reszta → V1 | 1-2 tygodnie | Średni | **ZALECANE** (balance effort/value) |

**Nasza rekomendacja**: **Opcja C (Hybrydowa)**

---

## Część 1: Strategie Migracji

### Strategia A: Rewizja Kompletna

**Kiedy użyć:**
- Projekt critical (finanse, medycyna, aerospace)
- Regulowany industry (wymaga pełnej audytowalności)
- Team > 10 osób (wysoka rotacja = knowledge loss risk)
- Dokumentacja > 2 lata (outdated, wiele deprecated docs)

**Proces:**
1. **Inwentaryzacja** (Dzień 1-2):
   - Lista wszystkich dokumentów V1 (ADR, RFC, PRD, etc.)
   - Priorytetyzacja (critical first)
   - Estymacja effort (per dokument)

2. **Migracja partiami** (Tydzień 1-4):
   - Batch 1: Critical ADRs (infra, architecture)
   - Batch 2: RFCs w użyciu
   - Batch 3: PRDs active projects
   - Batch 4: Reszta

3. **Walidacja** (Dzień ongoing):
   - Peer review per dokument
   - Gap detection (E110-E200)
   - Stakeholder approval

**Estimated Effort**:
- 20 dokumentów × 2-4h/doc = **40-80 godzin**
- Team 2 osoby = **2-4 tygodnie**

---

### Strategia B: Przyrostowa

**Kiedy użyć:**
- Projekt non-critical (internal tools)
- Team < 5 osób (niska rotacja)
- Budget/time limited

**Proces:**
1. **Freeze V1 docs** (Dzień 1):
   - Przenieś wszystkie V1 docs do `/docs-deprecated/`
   - Dodaj banner: "⚠️ This doc uses V1 format (deprecated). New docs use V2."

2. **New docs only V2** (Ongoing):
   - Nowe ADR/RFC/PRD = tylko V2
   - Stare docs = read-only (nie przepisujemy)

3. **On-demand migration** (As needed):
   - Jeśli V1 doc wymaga update → przepisz do V2 przy okazji
   - Jeśli V1 doc deprecated → leave as is

**Estimated Effort**:
- **Zero upfront cost** (migracja on-demand)
- **Per-document cost**: 2-4h (gdy potrzebne)

---

### Strategia C: Hybrydowa ✅ ZALECANE

**Kiedy użyć:**
- **Większość projektów** (best balance)

**Proces:**
1. **Identyfikuj critical docs** (Dzień 1):
   ```
   Critical doc = spełnia ≥2 kryteria:
   - Referenced przez ≥5 innych docs
   - Age > 1 rok (high staleness risk)
   - Impacts production (infra, architecture, security)
   - Compliance required (audit trail needed)
   ```

2. **Migruj critical docs** (Tydzień 1-2):
   - ~5-10 dokumentów (80/20 rule: 20% docs = 80% value)
   - Full V2 treatment (decision graph, storytelling, evidence)

3. **Deprecate non-critical docs** (Dzień 1):
   - Przenieś do `/docs-deprecated/`
   - Dodaj deprecation notice

4. **New docs V2** (Ongoing):
   - Wszystkie nowe docs = V2

**Estimated Effort**:
- 5-10 critical docs × 2-4h = **10-40 godzin**
- Team 1-2 osoby = **1-2 tygodnie**

---

## Część 2: Migracja ADR (Architecture Decision Record)

### Przykład PRZED (V1)

```markdown
---
id: ADR-005
title: "Database choice for Cart Service"
type: adr
status: approved
created: 2024-08-15
dependencies:
  - RFC-2024-08
  - ADR-003
---

# ADR-005: Database Choice

## Context
Cart Service needs a database. We need ACID and good write performance.

## Decision
We chose PostgreSQL 16.

## Consequences
- Good: ACID compliance, team knows SQL
- Bad: More complex than NoSQL

## Alternatives
MongoDB was considered but lacks ACID.
```

**Problemy**:
- ❌ Brak bramek (dependencies = static links)
- ❌ Brak decision graph (tylko 1 alternative, brak benchmarks)
- ❌ Brak storytelling (fact list "we chose X")
- ❌ Brak evidence (benchmarks gdzie?)
- ❌ Brak context T₀ (jaki był budget/timeline?)

---

### Przykład PO (V2)

```markdown
---
id: ADR-005-V2
title: "Database choice for Cart Service"
type: adr
status: approved
created: 2024-08-15
decision_date: 2024-08-15
decision_maker: ["Tech Lead", "Backend Team"]

# Bramki wejścia
dependencies:
  - id: RFC-2024-08
    type: requires
    status_constraint: [approved]
    cascade: true

  - id: ADR-003
    type: requires
    status_constraint: [approved]

# Bramki wyjścia
impacts:
  - id: IMPL-CART-DB
    type: blocks
    until: "ADR-005-V2.status == approved"
    cascade: true

  - id: OPS-RUNBOOK-07
    type: informs
    cascade: true

# Context T₀
context_snapshot:
  budget: "$5k/month"
  team_size: 2
  timeline: "Launch by 2024-10-01"
  constraints: ["GDPR", "ACID required (ADR-003)"]

# Evidence
evidence_ids: ["E-042", "E-043", "E-044", "E-045"]

# Alternatives
alternatives:
  - id: "OPTION-A"
    title: "MongoDB"
    status: rejected
    reason: "Brak ACID"
  - id: "OPTION-B"
    title: "MySQL"
    status: rejected
  - id: "OPTION-C"
    title: "PostgreSQL"
    status: selected
  - id: "OPTION-D"
    title: "DynamoDB"
    status: rejected

# Satellites
satellites:
  - IMPL-LOG-ADR-005-V2
  - POST-MORTEM-ADR-005-V2
---

# ADR-005-V2: Database Choice for Cart Service

## Historia decyzji: Dlaczego PostgreSQL?

Początkowo rozważaliśmy **in-memory cache** jako primary store (Opcja A)...
[STORYTELLING: Pełna narracja jak w Przykładzie 1 z koncepcje-v2-przyklady.md]

## Alternatives Considered (Full Details)

### Opcja A: MongoDB
**Benchmark** [E-042]: 15k writes/s, 50ms p99, $3k/m
**REJECTED**: Brak ACID w distributed setup...

### Opcja B: MySQL
**Benchmark** [E-043]: 8k writes/s, 80ms p99, $2k/m
**REJECTED**: Słaba wydajność write...

### Opcja C: PostgreSQL ✓
**Benchmark** [E-044]: 12k writes/s, 60ms p99, $2.5k/m
**SELECTED**: Balance ACID + performance + cost...

### Opcja D: DynamoDB
**Benchmark** [E-045]: 25k writes/s, 30ms p99, $6k/m
**REJECTED**: Over budget + vendor lock-in...

## Re-evaluation Triggers
1. Traffic > 8k req/s sustained 7 days → consider sharding
2. Cost > $4k/m for 3 months → re-evaluate
3. Multi-cloud requirement → check portability
```

---

### Migracja ADR: Checklist

#### Faza 1: Frontmatter (30 min)

- [ ] **Dodaj decision metadata**:
  ```yaml
  decision_date: "YYYY-MM-DD"
  decision_maker: ["Role 1", "Role 2"]
  ```

- [ ] **Przekształć dependencies → bramki**:
  ```yaml
  # V1
  dependencies: [RFC-001, ADR-003]

  # V2
  dependencies:
    - id: RFC-001
      type: requires
      status_constraint: [approved]
      cascade: true
  ```

- [ ] **Dodaj bramki wyjścia**:
  ```yaml
  impacts:
    - id: IMPL-XXX
      type: blocks
      until: "this.status == approved"
  ```

- [ ] **Dodaj context snapshot**:
  ```yaml
  context_snapshot:
    budget: "$Xk/month"
    team_size: N
    timeline: "YYYY-MM-DD"
    constraints: [...]
  ```

- [ ] **Dodaj evidence_ids**:
  ```yaml
  evidence_ids: ["E-XXX", "E-YYY"]
  ```

- [ ] **Dodaj alternatives**:
  ```yaml
  alternatives:
    - {id: "OPT-A", title: "X", status: rejected, reason: "..."}
    - {id: "OPT-B", title: "Y", status: selected}
  ```

#### Faza 2: Content (1-2 godziny)

- [ ] **Sekcja "Historia decyzji"** (storytelling):
  - Problem statement
  - Opcje rozważane (A, B, C, D...)
  - Proces eliminacji (dlaczego NIE A, NIE B...)
  - Wybór (dlaczego C)
  - Konsekwencje (risks accepted, benefits gained)

- [ ] **Sekcja "Alternatives Considered"** (szczegóły):
  - Per opcja:
    - Benchmark results [E-XXX]
    - Pros/cons
    - Rejection reason (jeśli rejected)
    - Selection reason (jeśli selected)

- [ ] **Sekcja "Re-evaluation Triggers"**:
  - Warunki triggering re-evaluation
  - Actions per trigger
  - Monitoring setup

#### Faza 3: Evidence Notes (30 min - 1h)

- [ ] **Stwórz evidence notes** (per alternative):
  ```markdown
  # /docs/satellites/evidence/E-042-mongodb-benchmark.md
  ---
  id: E-042
  type: benchmark
  date: "2024-08-10"
  ---
  # MongoDB Benchmark Results
  - Methodology: k6 load test, 1000 VU, 60s
  - Results: 15k writes/s, 50ms p99
  - Environment: Atlas M40, eu-central-1
  ```

#### Faza 4: Satellites (30 min)

- [ ] **Implementation Log** (jeśli deployed):
  - `/docs/satellites/impl-logs/IMPL-LOG-ADR-XXX.md`
  - Entries: discoveries, plan deviations, edge cases

- [ ] **Post-mortem** (jeśli 90+ dni po deploy):
  - `/docs/satellites/post-mortems/POST-MORTEM-ADR-XXX.md`
  - What worked better/worse, learnings

**Total Time**: **2.5 - 4.5 godziny** per ADR

---

## Część 3: Migracja RFC (Request for Comments)

### Różnice RFC vs ADR

| Aspekt | ADR | RFC |
|--------|-----|-----|
| **Focus** | Decyzja (już podjęta) | Propozycja (do dyskusji) |
| **Status** | draft → review → approved → deployed | draft → review → accepted/rejected |
| **Alternatives** | Wszystkie (+ rejected) | Preferowana + alternatives |
| **Decision graph** | Pełny (z context T₀) | Wstępny (kontekst może się zmienić) |

### Migracja RFC: Specyficzne Dodatki

Oprócz standardowych elementów (jak ADR):

- [ ] **Sekcja "Open Questions"**:
  ```markdown
  ## Open Questions
  1. **Q**: Czy budget $5k firm czy może wzrosnąć?
     **Status**: Pending CFO response
  2. **Q**: Czy team gotowy nauczyć się NoSQL?
     **Status**: Pending team survey
  ```

- [ ] **Sekcja "Feedback Received"**:
  ```markdown
  ## Feedback Received
  - **DevOps** (2024-08-12): "Prefer AWS-native services" → updated alternatives
  - **Security** (2024-08-13): "Ensure encryption at rest" → added to requirements
  ```

---

## Część 4: Migracja PRD (Product Requirements Document)

### PRD V1 → V2: Główne Zmiany

1. **Bramki wewnętrzne** (między sekcjami):
   ```yaml
   internal_gates:
     - source: "Wymagania Niefunkcjonalne"
       impacts: ["Architektura", "Testy", "Koszty"]
   ```

2. **Storytelling per FR** (Functional Requirement):
   ```markdown
   ## FR-001: Parsowanie Plików Markdown

   ### Historia wymagania
   Początkowo planowaliśmy tylko plain text (Opcja A), ale...
   [Storytelling: dlaczego markdown, nie plain text/rich text/WYSIWYG]

   ### Evidence
   - [E-010] User research: 80% devs prefer markdown
   - [E-011] Benchmark: markdown parsing < 50ms/doc
   ```

3. **Mapowanie FR → Koncepcje**:
   ```markdown
   **Mapuje Koncepcje**: C-007 (Parser), C-001 (Dokument)
   ```

### Migracja PRD: Checklist

- [ ] **Dodaj bramki wewnętrzne** (frontmatter)
- [ ] **Per FR: Dodaj storytelling** (dlaczego to wymaganie?)
- [ ] **Per FR: Dodaj evidence** ([E-XXX] user research/benchmarks)
- [ ] **Per FR: Mapuj do koncepcji** (C-XXX)
- [ ] **Dodaj re-evaluation triggers** (kiedy przeglądać wymagania?)

**Total Time**: **4-6 godzin** per PRD (zależnie od liczby FR)

---

## Część 5: Tworzenie Satelitów

### Implementation Log

**Kiedy tworzyć**: Gdy dokument przechodzi do statusu `in-progress`

**Template**:
```markdown
---
id: IMPL-LOG-XXX
type: implementation-log
parent: XXX
---

# Implementation Log: XXX

## Entry 1: YYYY-MM-DD - Start
Action: ...
Status: ...

## Entry 2: YYYY-MM-DD - Discovery
Type: unexpected_discovery
Severity: medium
Problem: ...
Solution: ...
Evidence: [E-XXX]
```

**Kiedy dodawać wpisy**:
- Rozpoczęcie pracy
- Każde unexpected discovery
- Każda zmiana w planie
- Każdy edge case
- Ukończenie

---

### Post-mortem

**Kiedy tworzyć**: 90 dni po deployment (automatyczny trigger)

**Template**:
```markdown
---
id: POST-MORTEM-XXX
type: post-mortem
parent: XXX
review_date: YYYY-MM-DD
outcome: success|partial|failure
---

# Post-mortem: XXX

## Metrics Review
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| ...    | ...    | ...    | ✅/❌   |

## What Worked Better
1. Item: ...
   Expected: ...
   Actual: ...
   Learning: ...

## What Worked Worse
1. Item: ...
   Reason: ...
   Mitigation: ...

## What We Would Do Differently
1. ...
2. ...

## Action Items
| ID | Title | Owner | Due | Status |
|----|-------|-------|-----|--------|
| ...| ...   | ...   | ... | ...    |
```

---

## Część 6: Automatyzacja Migracji

### Script: Bulk Frontmatter Update

```python
# migrate_frontmatter.py
import frontmatter
from pathlib import Path

def migrate_adr_frontmatter(file_path):
    """
    Migrate ADR V1 frontmatter → V2
    Adds: decision_date, context_snapshot, evidence_ids, alternatives
    """
    post = frontmatter.load(file_path)

    # Add new fields
    post['decision_date'] = post.get('created', '')
    post['decision_maker'] = ["PLACEHOLDER - FILL MANUALLY"]
    post['context_snapshot'] = {
        "budget": "PLACEHOLDER",
        "team_size": "PLACEHOLDER",
        "constraints": []
    }
    post['evidence_ids'] = []
    post['alternatives'] = []

    # Transform dependencies → gates
    if 'dependencies' in post:
        old_deps = post['dependencies']
        post['dependencies'] = [
            {
                'id': dep,
                'type': 'requires',
                'status_constraint': ['approved'],
                'cascade': False  # User must review
            }
            for dep in (old_deps if isinstance(old_deps, list) else [old_deps])
        ]

    # Save
    with open(file_path, 'wb') as f:
        frontmatter.dump(post, f)

# Usage:
# python migrate_frontmatter.py /docs/engineering/*.md
```

**Note**: Script adds PLACEHOLDERS → manual review required.

---

### Script: Evidence Note Generator

```python
# generate_evidence_stubs.py

def generate_evidence_stub(evidence_id, title, doc_type='benchmark'):
    """
    Generate stub evidence note for user to fill
    """
    template = f"""---
id: {evidence_id}
type: {doc_type}
title: "{title}"
date: "YYYY-MM-DD"  # FILL ME
author: "TEAM/PERSON"  # FILL ME
---

# {evidence_id}: {title}

## Summary
**PLACEHOLDER**: Brief description of evidence

## Methodology
**PLACEHOLDER**: How was this evidence obtained?

## Results
**PLACEHOLDER**: Key findings

## Artifacts
- [ ] Add link to raw data/report
- [ ] Add link to dashboard/visualization

## Related Decisions
- PLACEHOLDER: Which decisions does this support?
"""
    return template

# Usage:
# generate_evidence_stub("E-042", "MongoDB Benchmark", "benchmark")
```

---

## Część 7: Validation Checklist

### Per Dokument (Po Migracji)

- [ ] **Frontmatter complete**:
  - [ ] decision_date, decision_maker (ADR/RFC)
  - [ ] context_snapshot (T₀)
  - [ ] evidence_ids (≥1 evidence note)
  - [ ] alternatives (≥2 opcje dla decision docs)
  - [ ] dependencies as gates (z type/cascade)
  - [ ] impacts defined (bramki wyjścia)

- [ ] **Content storytelling**:
  - [ ] Sekcja "Historia decyzji" (narracja, nie fact list)
  - [ ] Sekcja "Alternatives Considered" (szczegóły per opcja)
  - [ ] Sekcja "Re-evaluation Triggers"

- [ ] **Evidence notes exist**:
  - [ ] Per alternative: ≥1 evidence note ([E-XXX])
  - [ ] Evidence note files created w `/docs/satellites/evidence/`

- [ ] **Satellites created** (jeśli applicable):
  - [ ] Implementation log (jeśli deployed)
  - [ ] Post-mortem (jeśli ≥90 dni po deploy)

- [ ] **Gap detection pass**:
  - [ ] Zero E170 (missing evidence)
  - [ ] Zero E180 (missing storytelling)
  - [ ] Zero E190 (missing alternatives)

---

## Część 8: Timeline Estimaty

### Per Document Type

| Type | V1 → V2 Time | Evidence Notes | Satellites | Total |
|------|--------------|----------------|------------|-------|
| **ADR** | 2-3h | +30m | +1h (impl log + post-mortem) | **3.5-4.5h** |
| **RFC** | 2-3h | +30m | - | **2.5-3.5h** |
| **PRD** | 4-6h | +1h | +30m (RTM update) | **5.5-7.5h** |

### Team Capacity

**1 person, full-time**:
- Week 1: 5 ADRs (20h)
- Week 2: 3 RFCs + 1 PRD (20h)
- **Total**: 5 ADRs + 3 RFCs + 1 PRD w 2 tygodnie

**2 people, part-time (50%)**:
- Week 1-2: 8 ADRs (40h / 2 people = 20h each)
- **Total**: 8 ADRs w 2 tygodnie

---

## Część 9: Prioritization Framework

### Kryteria Critical Docs

Dokument jest "critical" jeśli spełnia ≥2:

1. **High References** (≥5 innych docs linkuje do tego)
2. **Age > 1 rok** (high staleness risk)
3. **Impacts Production** (infrastructure, security, data)
4. **Compliance Required** (audit trail mandatory)
5. **Team Size > 5** (high rotation = knowledge loss risk)

### Scoring Model

```python
def calculate_priority_score(doc):
    score = 0
    score += min(doc.reference_count, 10)  # Max 10 points
    score += min(doc.age_years * 2, 10)    # Max 10 points (5 years)
    score += 10 if doc.impacts_production else 0
    score += 10 if doc.compliance_required else 0
    score += min(doc.team_size, 10)        # Max 10 points
    return score  # Max: 50 points

# Priority:
# 40-50: CRITICAL (migrate first)
# 25-39: HIGH (migrate if time)
# 10-24: MEDIUM (migrate on-demand)
# 0-9: LOW (leave as V1)
```

---

## Część 10: Common Pitfalls

### 1. ❌ Kopiowanie V1 content bez storytelling

**Błąd**:
```markdown
# V2 (źle)
## Decision
We chose PostgreSQL.
```

**Poprawnie**:
```markdown
# V2 (dobrze)
## Historia decyzji: Dlaczego PostgreSQL?
Początkowo rozważaliśmy MongoDB (15k writes/s), ale...
```

---

### 2. ❌ Evidence notes bez actual evidence

**Błąd**:
```markdown
# E-042 (źle)
MongoDB jest szybki.
```

**Poprawnie**:
```markdown
# E-042 (dobrze)
## Benchmark Results
- Methodology: k6, 1000 VU, 60s
- Throughput: 15k writes/s
- Latency p99: 50ms
- Environment: Atlas M40
- Raw data: /artifacts/E-042-results.json
```

---

### 3. ❌ Bramki bez cascade flag review

**Błąd**: Ustawienie `cascade: true` dla wszystkich bramek (notification overload).

**Poprawnie**: Review każdą bramkę:
- `requires` / `blocks` → `cascade: true` (critical)
- `informs` → `cascade: false` (jeśli minor), `true` (jeśli major)

---

### 4. ❌ Alternatives bez rejection reasons

**Błąd**:
```yaml
alternatives:
  - {id: "OPT-A", title: "MongoDB", status: rejected}
```

**Poprawnie**:
```yaml
alternatives:
  - id: "OPT-A"
    title: "MongoDB"
    status: rejected
    reason: "Brak ACID w distributed setup (required by ADR-003)"
    evidence: ["E-042"]
```

---

## Podsumowanie

### Quick Start (Hybrydowa Strategia)

1. **Dzień 1**: Identyfikuj 5-10 critical docs (scoring model)
2. **Tydzień 1**: Migruj critical ADRs (2-3 docs)
3. **Tydzień 2**: Migruj critical RFCs/PRDs (2-3 docs)
4. **Ongoing**: Nowe docs = tylko V2, stare = deprecated

### Success Metrics

Po migracji powinno być:
- ✅ Zero E170 gaps (wszystkie twierdzenia = evidence)
- ✅ Zero E180 gaps (wszystkie sekcje = storytelling)
- ✅ Zero E190 gaps (wszystkie decyzje = ≥2 alternatives)
- ✅ 100% critical docs w V2
- ✅ Team trained (wszyscy wiedzą jak pisać V2 docs)

### Next Steps

1. ✅ **Przeczytaj**: [DIFF-REPORT](./CONCEPTS-001-DIFF-REPORT.md) (zrozum co się zmieniło)
2. ✅ **Wybierz strategię**: A/B/C (hybrydowa zalecane)
3. ✅ **Rozpocznij migrację**: Pierwszy ADR (template available)
4. ✅ **Review & iterate**: Gap detection + peer review

---

← [Powrót do CONCEPTS-V2](./koncepcje-v2.md) | [Zobacz też: DIFF Report](./CONCEPTS-001-DIFF-REPORT.md)
