---
id: CONCEPTS-001-DIFF-REPORT
title: "DIFF Report: Co Było Źle w CONCEPTS-001-V1"
type: diff-report
parent: CONCEPTS-001-V2
domain: engineering
status: draft
created: 2025-12-26
---

# DIFF Report: CONCEPTS-001-V1 → CONCEPTS-001-V2

← [Powrót do CONCEPTS-V2](./koncepcje-v2.md)

---

## Streszczenie Wykonawcze

**Data rewizji**: 2025-12-26
**Wersja stara**: CONCEPTS-001-V1 (deprecated → koncepcje-v1-deprecated.md)
**Wersja nowa**: CONCEPTS-001-V2 (koncepcje-v2.md + 5 plików modułowych)

### Fundamentalna Zmiana

**V1**: Tradycyjne podejście do dokumentacji (dokument = tekst do edycji)
**V2**: **Proof System** (dokument = ekosystem artefaktów z pełną audytowalnością)

### Statystyki Zmian

| Metryka | V1 | V2 | Zmiana |
|---------|----|----|--------|
| **Koncepcje** | 12 | 18 | +6 (+50%) |
| **Funkcje** | ~60 | ~95 | +35 (+58%) |
| **Typy luk** | 6 (E110-E160) | 10 (E110-E200) | +4 (+67%) |
| **Rozmiar** | 1546 linii | ~3050 linii | +1504 (+97%) |
| **Plików** | 1 | 6 | +5 (modularyzacja) |

---

## Część 1: Filozoficzna Rewolucja

### 1.1 Problem z V1: Pasywna Dokumentacja

#### Co Było Źle

**V1 traktowało dokumentację jako statyczny tekst:**
```yaml
# V1 approach
document:
  id: ADR-005
  title: "Database choice"
  dependencies: [RFC-2024-08, ADR-003]  # Statyczne linki
  content: "Wybraliśmy PostgreSQL."  # Wynik bez procesu
```

**Problemy**:
1. **Brak kontekstu decyzji**: Nie wiemy DLACZEGO PostgreSQL (jakie były alternatywy?)
2. **Pasywne zależności**: Link do RFC-2024-08, ale co jeśli RFC się zmieni? System nie propaguje zmian
3. **Brak audytowalności**: Nie wiemy co było rozważane i odrzucone
4. **Brak evidence**: Decyzja oparta na czym? Benchmark? Guesswork?

#### Incident Demonstrujący Problem

**Data**: 2024-06-20
**Problem**: Nowy developer zaproponował MongoDB (lepszaperformance).
**Response**: Senior powiedział "potrzebowaliśmy ACID" ale nie pamiętał szczegółów.
**Root cause**: V1 nie zapisało:
- Że rozważaliśmy MongoDB
- Benchmarki MongoDB (15k writes/s vs PostgreSQL 12k)
- Dlaczego odrzuciliśmy (brak ACID w distributed setup)

**Skutek**: 30 min debata, re-benchmarking MongoDB (już to robiliśmy 2 lata temu).

### 1.2 Rozwiązanie w V2: Proof System

**V2 traktuje dokumentację jako proof system:**
```yaml
# V2 approach
document:
  id: ADR-005

  gates:  # Aktywne bramki zamiast statycznych linków
    input:
      - id: RFC-2024-08
        type: requires
        status_constraint: [approved]
        cascade: true  # Zmiana w RFC → auto TODO dla ADR

  decision_graph: DEC-ADR-005-001  # Pełny graf decyzyjny

  alternatives:  # WSZYSTKIE opcje (nie tylko wybrana)
    - MongoDB (rejected: no ACID)
    - MySQL (rejected: slow writes)
    - PostgreSQL (selected)
    - DynamoDB (rejected: over budget)

  evidence_ids: [E-042, E-043, E-044, E-045]  # Benchmarks
```

**Korzyści**:
1. **Kontekst zachowany**: Widzimy wszystkie opcje + uzasadnienia
2. **Aktywne propagacja**: RFC zmienia się → system tworzy TODO dla ADR
3. **Pełna audytowalność**: Graf decyzyjny z evidence trail
4. **避免 repetition**: "Już sprawdzaliśmy MongoDB, oto dlaczego NIE"

---

## Część 2: Zmiany w Koncepcjach

### 2.1 Koncepcje NOWE (6)

#### C-013: Bramka Wejścia/Wyjścia

**Dlaczego nie było w V1?**
V1 miało tylko statyczne linki (`dependencies: [doc-A, doc-B]`).

**Problem z V1**:
- Link nie ma semantyki (co to znaczy "dependency"?)
- Link jest pasywny (zmiana w doc-A nie wpływa na doc-B)
- Brak typów (requires vs informs vs blocks)

**Dlaczego dodano w V2?**
**Incident 2024-07-15**: ADR-003 zmienił wymaganie ACID → eventual consistency. ADR-005 (Database choice) nadal wymagał ACID (outdated). Zespół wybrał PostgreSQL zamiast Cassandra. Overpaid $9k przez 6 miesięcy.

**V2 Solution**: Bramki z typami + cascade + propagacja zmian.

**Przykład V2**:
```yaml
gate:
  source: ADR-003
  target: ADR-005
  type: impacts
  cascade: true
  # Zmiana w ADR-003 → auto TODO dla ADR-005
```

---

#### C-014: Graf Decyzyjny

**Dlaczego nie było w V1?**
V1 zapisywało tylko wynik decyzji ("Wybraliśmy X"), nie proces.

**Problem z V1**:
- Brak opcji alternatywnych (co jeszcze rozważaliśmy?)
- Brak kontekstu T₀ (jaki był stan wiedzy w momencie decyzji?)
- Brak uzasadnień porównawczych (dlaczego X a nie Y?)

**Dlaczego dodano w V2?**
**Potrzeba re-evaluation**: Warunki zmieniają się (budget rośnie, nowe technologie), musimy wiedzieć czy wrócić do odrzuconej opcji.

**V2 Solution**: Decision Graph z:
- Context T₀ (budget, timeline, constraints)
- Wszystkie opcje (selected + rejected + deferred)
- Uzasadnienia (dlaczego C, a nie A/B/D?)
- Evidence nodes (benchmarks per opcja)

---

#### C-015: Storytelling

**Dlaczego nie było w V1?**
V1 nie wymuszało formy dokumentacji (mogła być lista faktów).

**Problem z V1**:
```markdown
## V1 (fact list)
System używa Redis. TTL=300s.
```

**Problemy**:
- Brak kontekstu (dlaczego Redis, nie Memcached?)
- Brak uzasadnienia (dlaczego TTL=300s?)
- Brak opcji alternatywnych

**Dlaczego dodano w V2?**
**Narracja wymusza zrozumienie**: Nie można spójnie opowiedzieć czegoś czego się nie rozumie. Jeśli developer nie potrafi napisać storytelling → nie rozumie decyzji → prawdopodobnie źle zaimplementuje.

**V2 Solution**: Wymagana forma storytelling z:
- Historia decyzji (problem → opcje → wybór → konsekwencje)
- Evidence trail
- Re-evaluation triggers

**Walidacja**: Luka E180 jeśli sekcja = fact list.

---

#### C-016: Nota Dowodowa

**Dlaczego nie było w V1?**
V1 nie miało systemu dla dowodów (mogły być linki ad-hoc).

**Problem z V1**:
```markdown
## V1
Wybraliśmy PostgreSQL bo jest szybszy.
(Szybszy od czego? Gdzie benchmark?)
```

**Problemy**:
- Twierdzenia bez dowodów
- Brak clickable links do benchmarków/testów
- Brak validity period (benchmark z 2020 nieaktualny w 2024)

**Dlaczego dodano w V2?**
**Research-grade documentation**: Każde twierdzenie = evidence note [E-XXX] z:
- Source (skąd wiemy?)
- Proof (benchmark/test results)
- Context (kiedy było prawdą?)
- Validity (do kiedy ważne?)

**V2 Solution**:
```markdown
Wybraliśmy PostgreSQL (12k writes/s [E-044]) zamiast MySQL (8k writes/s [E-043]).
```

**Walidacja**: Luka E170 jeśli twierdzenie bez evidence note.

---

#### C-017: Implementation Log

**Dlaczego nie było w V1?**
V1 zakładało że implementacja = straightforward (plan → execute → done).

**Problem z V1**:
- Nieoczekiwane odkrycia nie są zapisywane (tracone przy rotacji ludzi)
- Edge cases discovered in prod = lost knowledge
- Zmiany w planie nie są justyfikowane

**Dlaczego dodano w V2?**
**Incident 2024-08-21**: Connection pool issue discovered (500 connections > 400 RDS limit). Fix applied, ale nie zapisany. 6 miesięcy później: Inny projekt, ten sam problem, 2h debugging (już rozwiązaliśmy!).

**V2 Solution**: Implementation Log z typami wpisów:
- `unexpected_discovery` (connection pool limit)
- `plan_deviation` (Multi-AZ dodany reaktywnie)
- `edge_case` (full-table scan on JSONB)

**Korzyść**: Knowledge retention + input dla post-mortem.

---

#### C-018: Post-mortem

**Dlaczego nie było w V1?**
V1: Post-mortem tylko przy failures, nie przy successes.

**Problem z V1**:
- Success = no retrospective → lost learnings
- "Co działało lepiej niż oczekiwano?" = niezapisane
- "Co zrobilibyśmy inaczej?" = niezapisane

**Dlaczego dodano w V2?**
**Continuous improvement**: Success też ma learnings. Przykład: Migration 4× szybsza (15 min vs 60 min expected) bo COPY command. Learning: Always use COPY. Ale jeśli nie zapiszemy → następna migracja użyje INSERT (slower).

**V2 Solution**: Post-mortem obligatoryjny nawet przy success:
- What worked better?
- What worked worse?
- What would we do differently?
- Re-evaluation triggers

**Trigger**: 90 dni po deploy (automatyczny).

**Walidacja**: Luka E200 jeśli post-mortem missing > 30 dni po trigger.

---

### 2.2 Koncepcje ZMODYFIKOWANE (8)

#### C-001: Dokument

**V1 → V2 Zmiany**:

| Aspekt | V1 | V2 | Dlaczego zmiana |
|--------|----|----|-----------------|
| **Edycja** | Edit in place | Immutable + versioning | Audit trail (każda zmiana = nowa wersja) |
| **Bramki** | Brak | Input/output gates | Aktywna propagacja zmian |
| **Changelog** | Opcjonalny | Obowiązkowy | Każda zmiana musi mieć reason + evidence |

**Problem z V1**:
Edit in place = historia zmian w Git, ale:
- Git log = techniczny (commit hash, diff)
- Brak semantic history (DLACZEGO zmiana?)

**V2 Solution**:
```yaml
changelog:
  - version: "2.0"
    date: "2024-08-22"
    changes: "Budget $2.5k → $3.3k (Multi-AZ)"
    reason: "Incident [E-051] = single-AZ SPOF"
    evidence: ["E-056"]  # CFO approval
```

---

#### C-002: Typ Dokumentu

**V1 → V2 Zmiany**:

| Aspekt | V1 | V2 | Dlaczego zmiana |
|--------|----|----|-----------------|
| **Template** | Statyczny plik | Aktywny artefakt | Template z auto-populated fields + placeholders |
| **Quality Gates** | Osobna koncepcja | **Fuzja** z document type | Gates per type (ADR ≠ RFC) |
| **Validation** | Binary (pass/fail) | Severity-based (critical/high/medium/low) | Nie wszystkie gaps = show-stoppers |

**Problem z V1**:
Document type + quality gates = separate concepts → duplicacja (każdy typ definiuje gates osobno).

**V2 Solution (Organic Fusion)**:
```yaml
document_type:
  id: adr

  lifecycle_gates:  # Fuzja: Gates per document type
    - name: "DRAFT-COMPLETE"
      from: draft
      to: review
      conditions: [...]

  required_sections:
    - name: "Context"
      validation_severity: critical  # Nie binary!
```

**Korzyść**: DRY (Don't Repeat Yourself) + severity-based validation.

---

#### C-003: Graf Zależności → Graf Decyzyjny

**V1 → V2 Zmiany**:

| Aspekt | V1 | V2 | Dlaczego zmiana |
|--------|----|----|-----------------|
| **Nazwa** | Graf Zależności | Graf Decyzyjny | Semantyczna zmiana (nie tylko "kto zależy od kogo") |
| **Zawartość** | Tylko selected options | **Wszystkie opcje** (+ rejected) | Re-evaluation + learning |
| **Kontekst** | Brak | Context T₀ | Time-travel (zrozumienie decyzji w kontekście) |
| **Evidence** | Brak | Evidence nodes | Każda opcja = benchmark/test |

**Problem z V1**:
Graf pokazywał "ADR-005 depends on RFC-2024-08", ale:
- Nie pokazywał DLACZEGO (jaki był reasoning?)
- Nie pokazywał opcji alternatywnych

**V2 Solution**: Graf decyzyjny = decision tree z:
- Decision node (ADR-005)
- Option nodes (MongoDB, MySQL, PostgreSQL, DynamoDB)
- Context nodes (budget, timeline, constraints)
- Evidence nodes (benchmarks)
- Edges (option → decision, evidence → option)

---

#### C-004: Luka

**V1 → V2 Zmiany**:

| Aspekt | V1 | V2 | Dlaczego zmiana |
|--------|----|----|-----------------|
| **Typy** | E110-E160 (6) | E110-E200 (10) | +4 nowe typy dla proof system |

**Nowe Typy w V2**:
- **E170**: Brakująca nota dowodowa (twierdzenie bez evidence)
- **E180**: Brak storytelling (sekcja = fact list)
- **E190**: Brak opcji alternatywnych (decyzja bez alternatives)
- **E200**: Brak post-mortem (>30 dni po deploy)

**Dlaczego dodano?**
V1 wykrywało techniczne luki (missing section, broken link). V2 dodaje **semantic gaps** (brak storytelling, brak evidence).

---

#### C-005: Bramka Jakości → Lifecycle Gates

**V1 → V2 Zmiany**:

| Aspekt | V1 | V2 | Dlaczego zmiana |
|--------|----|----|-----------------|
| **Nazwa** | Bramka Jakości | Lifecycle Gates | Semantyczna zmiana (cały lifecycle, nie tylko DoD) |
| **Fazy** | Tylko DoD | **DoR + Impl + DoD + Post-mortem** | Pełny cykl życia |

**Problem z V1**:
V1 miało tylko DoD (Definition of Done). Ale:
- Brak DoR → prace zaczynają się bez clear requirements
- Brak Implementation tracking → discoveries lost
- Brak Post-mortem → learnings lost

**V2 Solution**: 4 fazy lifecycle:
1. **DoR**: Czy gotowi do rozpoczęcia? (requirements clear, evidence plan created)
2. **Implementation**: Tracking discoveries (impl log entries)
3. **DoD**: Czy ukończone? (metrics met, tests passed)
4. **Post-mortem**: Retrospektywa (even on success)

---

#### C-008: Metadata

**V1 → V2 Zmiany**:

**Nowe Pola w V2**:
```yaml
# V1
id, title, type, status, created, updated, owner

# V2 (additional fields)
decision_date: "2024-08-15"
decision_maker: ["Tech Lead", "Backend Team"]
context_snapshot: {...}  # Stan w T₀
evidence_ids: [E-042, E-043, E-044]
alternatives_considered: [...]
```

**Dlaczego dodano?**
V1 metadata = identyfikacja dokumentu. V2 metadata = **context capture** dla decision graph.

---

#### C-011: Satelita

**V1 → V2 Zmiany**:

**Nowe Typy Satelitów w V2**:
- **IMPL-LOG**: Implementation Log (C-017)
- **POST-MORTEM**: Retrospektywa (C-018)
- **EVIDENCE**: Noty dowodowe (C-016)

**Dlaczego dodano?**
V1 satelity = TODO, DOR, DOD, RTM (task tracking). V2 dodaje **knowledge artifacts** (impl log, post-mortem, evidence).

---

#### C-012: Domena

**V1 → V2 Zmiany**:

**Nowe: Policy Maps**
```yaml
domain:
  id: architecture
  policy_map:
    - rule: "Load testing before approval"
      applies_to: [adr]
      requirement: "Load test results [E-XXX]"
```

**Dlaczego dodano?**
V1: Domain = logical grouping. V2: Domain = **policy enforcement** (reguły specyficzne dla domeny).

**Przykład**: Architecture domain wymaga load testing przed approval ADR. Compliance domain wymaga security review przed deployment.

---

### 2.3 Koncepcje BEZ ZMIAN (4)

| ID | Koncepcja | Status V1 → V2 |
|----|-----------|----------------|
| C-006 | Walidator | ✅ Bez zmian (core validation logic OK) |
| C-007 | Parser | ✅ Bez zmian (parsing markdown + YAML OK) |
| C-009 | Połączenie (Edge) | ✅ Bez zmian (graph edges OK, ale używane inaczej w V2) |
| C-010 | Węzeł (Node) | ✅ Bez zmian (graph nodes OK) |

**Dlaczego bez zmian?**
Te koncepcje są "low-level" (implementacja), nie "high-level" (filozofia). Filozofia zmienia się (V1 → V2), ale implementacja parsing/validation pozostaje.

---

## Część 3: Implikacje Zmian

### 3.1 Dla Istniejących Dokumentów

**Status**: Wszystkie dokumenty napisane w V1 są **deprecated** ale zachowane jako evidence.

**Migracja**:
- CONCEPTS-001-V1 → `koncepcje-v1-deprecated.md`
- PRD-001-V1 → `prd-v1-deprecated.md`

**Nowe wersje**:
- CONCEPTS-001-V2 (modularny, 6 plików)
- PRD-V2 (z bramkami, storytelling, evidence)

**Migration Guide**: [CONCEPTS-001-MIGRATION-GUIDE.md](./CONCEPTS-001-MIGRATION-GUIDE.md)

---

### 3.2 Dla Zespołu

**Learning Curve**:
- **V1**: Markdown + YAML frontmatter (familiar)
- **V2**: + Decision graphs + Storytelling + Evidence notes (new skills)

**Estimated Time to Proficiency**:
- Reading V2 docs: 2-4 godziny (zrozumienie filozofii)
- Writing V2 docs: 2-3 dni (pierwsze ADR/RFC z storytelling)
- Mastery: 2-4 tygodnie (comfortable z decision graphs)

---

### 3.3 Dla Narzędzi

**Nowe Funkcje w Systemie** (Python app):
- Gate evaluator (F-081 to F-085)
- Decision graph builder (F-086 to F-092)
- Storytelling validator (F-093 to F-096)
- Evidence tracker (F-097 to F-101)
- Implementation log manager (F-102 to F-106)
- Post-mortem generator (F-107 to F-111)

**Total**: +35 nowych funkcji (było 60 → będzie 95)

---

## Część 4: Kluczowe Learnings z V1

### Co Działało w V1 (zachowujemy)

1. **Modularność typów dokumentów** ✓
   - ADR, RFC, PRD jako osobne typy
   - Szablony per typ

2. **Gap detection** ✓
   - E110-E160 gaps działały dobrze
   - V2: Rozszerzamy o E170-E200

3. **Satelity** ✓
   - TODO, DOR, DOD, RTM były użyteczne
   - V2: Dodajemy IMPL-LOG, POST-MORTEM, EVIDENCE

### Co Nie Działało w V1 (naprawiamy)

1. **Pasywne zależności** ❌
   - Linki statyczne nie propagowały zmian
   - V2: Aktywne bramki z cascade

2. **Brak decision context** ❌
   - Tylko wynik, nie proces
   - V2: Decision graph z alternatives + context T₀

3. **Brak storytelling** ❌
   - Fact lists bez uzasadnień
   - V2: Storytelling obligatoryjny + validator

4. **Brak evidence system** ❌
   - Twierdzenia bez dowodów
   - V2: Evidence notes [E-XXX] obowiązkowe

5. **Brak post-mortems** ❌
   - Success = no retrospective
   - V2: Post-mortem nawet przy success

---

## Część 5: Rekomendacje

### Dla Nowych Projektów
✅ **Użyj CONCEPTS-V2 od początku**
- Pełny proof system
- Wszystkie 18 koncepcji
- Wszystkie 95 funkcji

### Dla Istniejących Projektów (z V1 docs)

**Opcja A: Rewizja kompletna** (zalecane dla critical projects)
- Przepisz wszystkie ADR/RFC z V1 → V2
- Dodaj decision graphs, evidence notes, storytelling
- Timeline: 2-4 tygodnie (dla ~20 dokumentów)

**Opcja B: Rewizja przyrostowa** (dla non-critical projects)
- Zachowaj V1 docs "as is" (deprecated)
- Nowe dokumenty piszemy w V2
- Starych NIE przepisujemy (unless re-evaluated)
- Timeline: ongoing

**Opcja C: Hybrydowa**
- Critical docs (> 5 dependencies, > 1 year old) → przepisz do V2
- Non-critical docs → leave as V1
- Timeline: 1-2 tygodnie (dla ~5-10 critical docs)

**Nasza rekomendacja**: **Opcja C (Hybrydowa)**

---

## Podsumowanie

### Co Było Źle w V1?

1. **Pasywna dokumentacja** (edit in place, statyczne linki)
2. **Brak decision context** (tylko wyniki, nie proces)
3. **Brak audytowalności** (opcje odrzucone = lost)
4. **Brak evidence system** (twierdzenia bez dowodów)
5. **Brak storytelling** (fact lists bez uzasadnień)
6. **Incomplete lifecycle** (tylko DoD, nie DoR/Impl/Post-mortem)

### Jak V2 to Naprawia?

1. **Aktywna dokumentacja** (bramki, propagacja zmian)
2. **Decision graph** (context T₀ + wszystkie opcje + uzasadnienia)
3. **Pełna audytowalność** (git log dla decyzji)
4. **Evidence notes** ([E-XXX] obowiązkowe)
5. **Storytelling** (narracja obowiązkowa + validator)
6. **Complete lifecycle** (DoR → Impl Log → DoD → Post-mortem)

### Cena Zmian

**Upfront Cost**: +50% effort (trzeba pisać więcej)
**Long-term Benefit**: -80% time wasted on "dlaczego to zrobiliśmy?"

**ROI**: Zwrot po 6-12 miesiącach (knowledge retention + avoid repetition).

---

← [Powrót do CONCEPTS-V2](./koncepcje-v2.md) | [Następny: Migration Guide →](./CONCEPTS-001-MIGRATION-GUIDE.md)
