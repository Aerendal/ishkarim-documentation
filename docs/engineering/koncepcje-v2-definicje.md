---
id: CONCEPTS-001-V2-DEFINITIONS
title: "Definicje 18 Koncepcji Systemu"
type: concepts-definitions
parent: CONCEPTS-001-V2
domain: engineering
status: draft
created: 2025-12-26
---

# Część 1: Definicje Koncepcji (18 koncepcji)

← [Poprzednia: Filozofia](./koncepcje-v2-filozofia.md) | [Powrót do głównego dokumentu](./koncepcje-v2.md) | [Następna: Mapowanie →](./koncepcje-v2-mapowanie.md)

---

## Spis Treści

### Koncepcje NOWE (6)
- [C-013: Bramka Wejścia/Wyjścia](#c-013-bramka-wejściawyjścia-inputoutput-gate)
- [C-014: Graf Decyzyjny](#c-014-graf-decyzyjny-decision-graph)
- [C-015: Storytelling](#c-015-storytelling-narracja-obowiązkowa)
- [C-016: Nota Dowodowa](#c-016-nota-dowodowa-evidence-note)
- [C-017: Implementation Log](#c-017-implementation-log-dziennik-realizacji)
- [C-018: Post-mortem](#c-018-post-mortem-retrospektywa)

### Koncepcje ZMODYFIKOWANE (8)
- [C-001: Dokument](#c-001-dokument-zmodyfikowana)
- [C-002: Typ Dokumentu](#c-002-typ-dokumentu-zmodyfikowana)
- [C-003: Graf Zależności](#c-003-graf-zależności-zmodyfikowana)
- [C-004: Luka](#c-004-luka-zmodyfikowana)
- [C-005: Bramka Jakości](#c-005-bramka-jakości-zmodyfikowana)
- [C-008: Metadata](#c-008-metadata-zmodyfikowana)
- [C-011: Satelita](#c-011-satelita-zmodyfikowana)
- [C-012: Domena](#c-012-domena-zmodyfikowana)

### Koncepcje BEZ ZMIAN (4)
- [C-006: Walidator](#c-006-walidator-bez-zmian)
- [C-007: Parser](#c-007-parser-bez-zmian)
- [C-009: Połączenie (Edge)](#c-009-połączenie-edge-bez-zmian)
- [C-010: Węzeł (Node)](#c-010-węzeł-node-bez-zmian)

---

# Koncepcje NOWE

## C-013: Bramka Wejścia/Wyjścia (Input/Output Gate)

### Status: 🆕 NOWA

### Definicja
**Bramka** to aktywny mechanizm definiujący wpływ między artefaktami dokumentacyjnymi. Bramka nie jest statycznym linkiem — to mechanizm kaskadowy, który propaguje zmiany i wymusza weryfikację zależnych elementów.

### Rodzaje Bramek

#### 1. Bramki Globalne (między dokumentami)
```yaml
document: ADR-005
gates:
  input:  # Co wpływa NA ten dokument
    - id: RFC-2024-08
      type: requires
      status_constraint: [approved, completed]
      reason: "Definiuje wymagania techniczne"

    - id: ADR-003
      type: requires
      status_constraint: [approved]
      reason: "Wymaga zgodności z standardami"

  output:  # Na CO wpływa ten dokument
    - id: IMPL-CART-DB
      type: blocks
      until: "ADR-005.status == approved"
      reason: "Implementacja nie może ruszyć bez zatwierdzonej architektury"

    - id: OPS-RUNBOOK-07
      type: informs
      cascade: true
      reason: "Zmiana typu bazy wymaga aktualizacji runbooka"
```

**Mechanizm kaskadowy**:
- Zmiana statusu RFC-2024-08 → automatyczna weryfikacja ADR-005
- Zmiana treści ADR-005 → automatyczne TODO dla OPS-RUNBOOK-07
- ADR-005.status != "approved" → IMPL-CART-DB zablokowane (luka E150)

#### 2. Bramki Wewnętrzne (w obrębie dokumentu)
```yaml
document: PRD-001
internal_gates:
  - section: "Wymagania Niefunkcjonalne"
    impacts:
      - "Architektura" (sekcja musi spełnić NFR)
      - "Testy Wydajnościowe" (musi weryfikować metryki)
      - "Oszacowanie Kosztów" (musi uwzględnić infrastrukturę)

  - section: "Założenia Budżetowe"
    impacts:
      - "Wybór Technologii" (ograniczony budżetem)
      - "Strategia Skalowania" (zależna od budżetu)
```

**Mechanizm kaskadowy**:
- Zmiana NFR "latency < 100ms" → "latency < 50ms"
- System wykrywa 3 sekcje do weryfikacji
- Generuje luki E180 jeśli sekcje nie zostały zaktualizowane
- Tworzy TODO-PRD-XXX z konkretnymi krokami

### Właściwości Bramki

```python
class Gate:
    id: str
    gate_type: GateType  # input | output | internal
    source: DocumentRef | SectionRef
    target: DocumentRef | SectionRef
    connection_type: str  # requires | blocks | informs | impacts
    status_constraint: List[str] = []  # ['approved', 'completed']
    cascade: bool = False
    reason: str  # Uzasadnienie bramki
    evidence: List[str] = []  # [E-XXX] notes

class GateEvaluation:
    gate: Gate
    satisfied: bool
    blocking: bool = False
    message: str
    remediation: List[str]
```

### Funkcje Powiązane
- `F-081`: Definiowanie bramek wejścia/wyjścia
- `F-082`: Ewaluacja bramek (czy spełnione?)
- `F-083`: Propagacja zmian przez bramki
- `F-084`: Wykrywanie blokerów bramek
- `F-085`: Generowanie TODO z bramek

### Powiązania z Innymi Koncepcjami
- **C-001 (Dokument)**: Dokument posiada bramki globalne
- **C-002 (Typ Dokumentu)**: Typ definiuje dozwolone bramki
- **C-003 (Graf)**: Bramki tworzą krawędzie w grafie
- **C-004 (Luka)**: Niespełniona bramka = luka E150
- **C-005 (Bramka Jakości)**: Quality gate używa gate evaluation

---

## C-014: Graf Decyzyjny (Decision Graph)

### Status: 🆕 NOWA

### Definicja
**Graf decyzyjny** to struktura danych reprezentująca pełną historię procesu decyzyjnego, zawierająca kontekst w momencie decyzji, wszystkie rozważane opcje (również odrzucone) oraz uzasadnienie wyboru z evidence trail.

### Struktura Grafu Decyzyjnego

```yaml
decision_graph:
  decision_id: "DEC-ADR-005-001"
  decision_title: "Wybór bazy danych dla Cart Service"
  decision_date: 2024-08-15
  decision_maker: ["Tech Lead", "Backend Team"]

  context_T0:  # Stan wiedzy w momencie decyzji
    timestamp: "2024-08-15T10:00:00Z"
    global_context:
      available_resources:
        budget: "$5,000/month"
        team: "2 backend devs (SQL experience, no NoSQL)"
        timeline: "Launch by 2024-10-01"
      business_constraints:
        - "GDPR compliance (data in EU)"
        - "99.9% uptime SLA"
      tech_landscape:
        - "PostgreSQL 16 available"
        - "MySQL 8.0 available"
        - "MongoDB 7.0 available"
        - "DynamoDB available"

    internal_context:
      previous_decisions:
        - id: "ADR-003"
          title: "Standardy persystencji"
          constraint: "Wymaga ACID compliance"
      baseline_assumptions:
        - "Expected traffic: 10k req/s"
        - "Write-heavy workload (70% writes, 30% reads)"
        - "Data size: 2M products, 50k carts/day"

  options:
    - id: "OPTION-A"
      title: "MongoDB"
      status: rejected
      benchmark:
        throughput: "15k writes/s"
        latency_p99: "50ms"
        cost: "$3k/month (Atlas M40)"
      rejection_reason: "Brak ACID compliance (wymóg z ADR-003)"
      evidence: ["E-042"]

    - id: "OPTION-B"
      title: "MySQL 8.0"
      status: rejected
      benchmark:
        throughput: "8k writes/s"
        latency_p99: "80ms"
        cost: "$2k/month (RDS db.m5.large)"
      rejection_reason: "Słaba wydajność write (8k < 10k req/s target)"
      evidence: ["E-043"]

    - id: "OPTION-C"
      title: "PostgreSQL 16"
      status: selected
      benchmark:
        throughput: "12k writes/s"
        latency_p99: "60ms"
        cost: "$2.5k/month (RDS db.m5.large)"
      selection_reason: |
        Balance między ACID (wymóg), wydajnością (12k > 10k target),
        kosztem (within budget), i team expertise (SQL).
      evidence: ["E-044"]
      risks_accepted:
        - "Lower throughput niż DynamoDB (12k vs 25k)"
        - "Mitigation: Horizontal sharding jeśli > 10k req/s"

    - id: "OPTION-D"
      title: "DynamoDB"
      status: rejected
      benchmark:
        throughput: "25k writes/s"
        latency_p99: "30ms"
        cost: "$6k/month (provisioned)"
      rejection_reason: "Over budget ($6k > $5k) + vendor lock-in"
      evidence: ["E-045"]

  justification:
    why_C_not_A: "ACID compliance required by ADR-003"
    why_C_not_B: "Better write performance (12k vs 8k)"
    why_C_not_D: "Budget constraint ($2.5k vs $6k)"
    risks_accepted:
      - risk: "Lower throughput than DynamoDB"
        mitigation: "Horizontal sharding plan if traffic > 10k"
        trigger: "Traffic > 8k req/s sustained for 7 days"

  re_evaluation_triggers:
    - condition: "traffic > 8k req/s for 7 days"
      action: "Consider sharding or migration to DynamoDB"
    - condition: "cost > $4k/month for 3 months"
      action: "Re-evaluate cheaper alternatives"
```

### Funkcje Powiązane
- `F-086`: Tworzenie grafu decyzyjnego
- `F-087`: Rejestracja opcji (wszystkich, nie tylko wybranej)
- `F-088`: Capture context T₀
- `F-089`: Rejestracja uzasadnień porównawczych
- `F-090`: Wizualizacja grafu (Mermaid)
- `F-091`: Wykrywanie brakujących opcji (luka E190)
- `F-092`: Monitoring re-evaluation triggers

### Powiązania z Innymi Koncepcjami
- **C-003 (Graf Zależności)**: Graf decyzyjny to specjalizacja
- **C-016 (Nota Dowodowa)**: Każda opcja ma evidence
- **C-015 (Storytelling)**: Graf używany w narracji
- **C-018 (Post-mortem)**: Post-mortem weryfikuje decyzje

---

## C-015: Storytelling (Narracja Obowiązkowa)

### Status: 🆕 NOWA

### Definicja
**Storytelling** to wymagana forma dokumentacji, w której każda sekcja musi być napisana jako spójna narracja wyjaśniająca proces myślowy, kontekst i uzasadnienie, zamiast jako lista faktów.

### Dlaczego Storytelling?

#### 1. Narracja wymusza zrozumienie
Nie można spójnie opowiedzieć czegoś, czego się nie rozumie.

#### 2. Narracja ujawnia luki
Miejsca, gdzie "nie ma historii", to miejsca bez zrozumienia.

#### 3. Narracja jest testowalna
Można weryfikować czy osoba X rozumie system, prosząc ją o opowiedzienie jego ewolucji.

### Format Storytelling

```markdown
## Sekcja: [Nazwa]

### Historia decyzji

[Narracja opisująca:]
1. Stan wyjściowy (co było na początku?)
2. Problem/potrzeba (dlaczego coś trzeba było zmienić?)
3. Opcje rozważane (co mogliśmy zrobić?)
4. Proces eliminacji (dlaczego NIE opcja A, B, C?)
5. Wybór (dlaczego wybraliśmy opcję X?)
6. Konsekwencje wyboru (co zaakceptowaliśmy?)
7. Re-evaluation triggers (kiedy powrócić do decyzji?)

### Evidence Trail
- [E-XXX] Link do dowodu 1
- [E-YYY] Link do dowodu 2

### Re-evaluation Triggers
- Trigger 1: [warunek] → [akcja]
- Trigger 2: [warunek] → [akcja]
```

### Przykład: ❌ Fact List vs ✅ Storytelling

#### ❌ ŹLE (fact list):
```markdown
## Caching Strategy
System używa Redis jako cache. TTL ustawiony na 300s.
Port: 6379. Mode: standalone.
```

#### ✅ DOBRZE (storytelling):
```markdown
## Historia decyzji: Redis jako cache

Początkowo rozważaliśmy **cache in-memory** (Opcja A) używając Python dictionaries
z LRU eviction. Odrzuciliśmy to ze względu na brak współdzielenia między replikami
— każdy pod miałby własny cache, co przy 5 replikach oznaczało 5x więcej cache misses.

Następnie testowaliśmy **Memcached** (Opcja B). Benchmark pokazał dobrą wydajność
(20k ops/s) [E-050], ale zrezygnowaliśmy z powodu braku persystencji przy restarcie.
Incydent z 2024-07-10 [E-051] pokazał, że cold cache po restarcie powodował
15-minutowy spike latencji (p99: 50ms → 800ms), co łamało SLA.

Wybraliśmy **Redis** (Opcja C), akceptując koszt większej złożoności operacyjnej
(backup, clustering, monitoring). W kontekście naszego ruchu (10k req/s) i SLA (99.9%)
persystencja cache była krytyczna.

**TTL 300s** wynika z analizy częstotliwości zmian danych źródłowych [E-052].
Mediana updatów produktów = 4 min. TTL=5min oznacza ~80% requestów trafia w aktualny
cache, a ~20% może widzieć dane sprzed 1 update (akceptowalne dla product catalog).

### Evidence Trail
- [E-050] Memcached benchmark results
- [E-051] Incident report 2024-07-10 (cold cache spike)
- [E-052] Data update frequency analysis (PERF-2024-03)

### Re-evaluation Triggers
- Jeśli mediana częstotliwości updatów < 3 min przez 7 dni → rozważ TTL=180s
- Jeśli Redis cost > $2k/miesiąc → rozważ cache invalidation zamiast TTL
```

### Walidacja Storytelling

System automatycznie wykrywa brak storytellingu:

```python
class StorytellingValidator:
    def validate_section(self, section: Section) -> ValidationResult:
        indicators_of_fact_list = [
            "brak narracji (tylko bullet points)",
            "brak słów: 'początkowo', 'następnie', 'wybraliśmy'",
            "brak uzasadnienia porównawczego ('dlaczego X a nie Y')",
            "brak kontekstu decyzji",
            "brak evidence trail",
            "brak re-evaluation triggers"
        ]

        if any_indicator_present:
            return Gap(
                id="E180",
                type="missing-storytelling",
                severity="medium",
                message="Sekcja zawiera tylko fakty, brak narracji",
                remediation=[
                    "Opisz proces decyzyjny",
                    "Dodaj opcje rozważane",
                    "Uzasadnij wybór",
                    "Dodaj evidence trail"
                ]
            )
```

### Funkcje Powiązane
- `F-093`: Walidacja storytelling (detekcja fact list)
- `F-094`: Generowanie luki E180
- `F-095`: Storytelling templates per document type
- `F-096`: Extracting narrative structure

### Powiązania z Innymi Koncepcjami
- **C-014 (Graf Decyzyjny)**: Graf używany w narracji
- **C-016 (Nota Dowodowa)**: Evidence wplecione w narrację
- **C-004 (Luka)**: Brak storytelling = luka E180

---

## C-016: Nota Dowodowa (Evidence Note)

### Status: 🆕 NOWA

### Definicja
**Nota dowodowa** to clickable artefakt dokumentacyjny służący jako źródło prawdy dla twierdzeń i decyzji. Każde twierdzenie w dokumentacji musi mieć przypisaną notę dowodową w formacie `[E-XXX]`.

### Format Noty Dowodowej

```yaml
evidence_note:
  id: "E-042"
  type: benchmark
  title: "MongoDB performance benchmark for Cart Service"
  date: "2024-08-10"
  author: "Backend Team"

  content:
    summary: "Benchmark MongoDB write performance"
    methodology: "k6 load test, 1000 VU, 60s duration"
    results:
      throughput: "15k writes/s"
      latency_p50: "30ms"
      latency_p99: "50ms"
    environment:
      instance: "Atlas M40"
      region: "eu-central-1"

  artifacts:
    - type: file
      path: "/docs/satellites/evidence/E-042-benchmark-results.json"
    - type: file
      path: "/docs/satellites/evidence/E-042-k6-script.js"
    - type: url
      url: "https://grafana.company.com/dashboard/E-042"

  related_decisions:
    - "ADR-005" (Wybór bazy danych)

  validity:
    valid_from: "2024-08-10"
    valid_until: "2025-08-10"  # Benchmark ważny 1 rok
    re_validation_trigger: "MongoDB version upgrade"
```

### Typy Not Dowodowych

| Typ | Opis | Przykłady |
|-----|------|-----------|
| **benchmark** | Wyniki testów wydajnościowych | [E-042] MongoDB write perf |
| **incident** | Raport z incydentu | [E-051] Cache cold start spike |
| **analysis** | Analiza danych | [E-052] Data update frequency |
| **requirement** | Wymaganie biznesowe | [E-001] GDPR compliance requirement |
| **cost** | Kalkulacja kosztów | [E-045] DynamoDB cost estimation |
| **approval** | Formalne zatwierdzenie | [E-056] CFO email (budget approval) |
| **review** | Peer review | [E-060] Security review ADR-005 |
| **test** | Wyniki testów | [E-073] Integration test results |

### Użycie w Dokumentacji

```markdown
## Sekcja: Performance Requirements

System musi obsługiwać **10k req/s** [E-100] z latencją p99 < 100ms [E-101].

Wymaganie wynika z analizy ruchu produkcyjnego [E-102], która pokazała:
- Peak traffic: 8.5k req/s (Black Friday 2023)
- Projected growth: 15% YoY [E-103]
- Buffer: 20% (safety margin) [E-104]

### Evidence Trail
- [E-100] Business requirement: 10k req/s target
- [E-101] SLA definition: p99 < 100ms
- [E-102] Traffic analysis report (Q1-Q3 2024)
- [E-103] Growth projection (Finance team)
- [E-104] Engineering buffer policy
```

### Walidacja Not Dowodowych

```python
class EvidenceValidator:
    def validate_document(self, doc: Document) -> List[Gap]:
        gaps = []

        # Wykryj twierdzenia bez dowodów
        claims = extract_claims(doc.content)
        for claim in claims:
            if not has_evidence_note(claim):
                gaps.append(Gap(
                    id="E170",
                    type="missing-evidence",
                    severity="high",
                    location=claim.location,
                    message=f"Claim '{claim.text}' lacks evidence note",
                    remediation=[
                        f"Add evidence note [E-XXX] for claim",
                        f"Create evidence document if needed"
                    ]
                ))

        # Weryfikuj istnienie not
        evidence_refs = extract_evidence_refs(doc.content)
        for ref in evidence_refs:
            if not evidence_exists(ref):
                gaps.append(Gap(
                    id="E130",
                    type="broken-evidence",
                    severity="critical",
                    message=f"Evidence {ref} referenced but not found"
                ))

        return gaps
```

### Funkcje Powiązane
- `F-097`: Tworzenie noty dowodowej
- `F-098`: Linkowanie noty do decyzji/twierdzeń
- `F-099`: Walidacja istnienia not
- `F-100`: Wykrywanie twierdzeń bez dowodów (E170)
- `F-101`: Zarządzanie cyklem życia not (validity)

### Powiązania z Innymi Koncepcjami
- **C-014 (Graf Decyzyjny)**: Każda opcja ma evidence
- **C-015 (Storytelling)**: Evidence wplecione w narrację
- **C-011 (Satelita)**: Evidence note jako satelita
- **C-004 (Luka)**: Brak evidence = luka E170

---

## C-017: Implementation Log (Dziennik Realizacji)

### Status: 🆕 NOWA

### Definicja
**Implementation Log** to chronologiczny dziennik decyzji, odkryć i zmian podjętych podczas realizacji zadania. Log rejestruje wszystkie nieoczekiwane odkrycia, edge cases i odchylenia od pierwotnego planu.

### Format Implementation Log

```yaml
implementation_log:
  id: "IMPL-LOG-CART-DB-001"
  parent_document: "ADR-005"
  implementation_period:
    start: "2024-08-20"
    end: "2024-08-25"
  team: ["Backend Team", "DevOps"]

entries:
  - date: "2024-08-20"
    type: start
    content: |
      Rozpoczęcie implementacji PostgreSQL RDS.
      Status: Provisioning db.m5.large w eu-central-1.
    duration: "15 min"

  - date: "2024-08-21"
    type: unexpected_discovery
    severity: medium
    title: "Connection pooling limit exceeded"
    content: |
      **Problem**: Connection pooling domyślnie = 100 connections/replica.
      Przy 5 replikach = 500 connections, ale RDS limit = 400.

      **Impact**: Application crashes z "too many connections" error.

      **Root cause**: Load testing używał 3 replicas, prod ma 5.

      **Solution**: Obniżyliśmy pool size do 60/replica (300 total).

      **Trade-off**: Akceptujemy ryzyko connection starvation przy > 8k req/s.

      **Mitigation**: Monitoring alert jeśli wait_for_connection > 50ms p99.
    evidence: ["E-055"]
    decision_maker: "Tech Lead"
    approved: true

  - date: "2024-08-22"
    type: plan_deviation
    severity: high
    title: "Changed to Multi-AZ deployment"
    content: |
      **Original plan**: Single master, streaming replication.

      **Change**: Multi-AZ deployment (master + standby in separate AZ).

      **Reason**: Incident [E-051] z 2024-07-10 pokazał że single-AZ = SPOF.
      Downtime 45 min przy AZ failure.

      **Cost impact**: +$800/miesiąc (total: $3.3k vs budget $2.5k = OVER).

      **Approval**: CFO approved via email [E-056] 2024-08-22.

      **Documentation update**: Budget section w ADR-005 zaktualizowany.
    evidence: ["E-051", "E-056"]
    decision_maker: "Tech Lead + CFO"
    approved: true
    documents_updated: ["ADR-005"]

  - date: "2024-08-23"
    type: edge_case
    severity: low
    title: "Full-table scan on products query"
    content: |
      **Case**: Query `SELECT * FROM products WHERE attributes->>'color' = 'red'`
      timeout po 5000ms.

      **Cause**: Brak indeksu na jsonb column (product_attributes).

      **Solution**: Added GIN index: `CREATE INDEX ON products USING GIN (attributes)`

      **Performance**: Query time 5000ms → 50ms (100x improvement).

      **Learning**: Always index JSONB columns used in WHERE clauses.
    evidence: ["E-057"]

  - date: "2024-08-25"
    type: completion
    content: |
      Implementacja ukończona. System deployed do production.
      Zero downtime migration (blue-green deployment).
      All DoD criteria met.
```

### Typy Wpisów w Logu

| Typ | Opis | Severity |
|-----|------|----------|
| **start** | Rozpoczęcie implementacji | info |
| **unexpected_discovery** | Nieoczekiwane odkrycie | low-critical |
| **plan_deviation** | Odchylenie od planu | medium-critical |
| **edge_case** | Discovered edge case | low-medium |
| **performance_surprise** | Nieoczekiwana wydajność | info-medium |
| **blocker** | Bloker wymagający decyzji | high-critical |
| **completion** | Ukończenie zadania | info |

### Funkcje Powiązane
- `F-102`: Tworzenie implementation log
- `F-103`: Dodawanie wpisu do logu
- `F-104`: Linkowanie logu do decision/ADR
- `F-105`: Wykrywanie brakującego logu (E175)
- `F-106`: Generowanie post-mortem z logu

### Powiązania z Innymi Koncepcjami
- **C-018 (Post-mortem)**: Post-mortem bazuje na logu
- **C-011 (Satelita)**: Implementation log jako satelita
- **C-005 (Bramka Jakości)**: DoD wymaga kompletnego logu

---

## C-018: Post-mortem (Retrospektywa)

### Status: 🆕 NOWA

### Definicja
**Post-mortem** to retrospektywa przeprowadzana **zawsze** (nawet przy sukcesie) po ukończeniu zadania, analizująca co działało, co nie działało, jakie były niespodzianki i co zrobilibyśmy inaczej.

### Format Post-mortem

```yaml
post_mortem:
  id: "POST-MORTEM-CART-DB-001"
  parent_document: "ADR-005"
  implementation_log: "IMPL-LOG-CART-DB-001"

  metadata:
    project: "Cart Service Database Migration"
    completion_date: "2024-08-25"
    review_date: "2024-08-30"
    participants: ["Tech Lead", "Backend Team", "DevOps", "Product Manager"]
    outcome: success  # success | partial_success | failure

  timeline:
    planned_start: "2024-08-20"
    actual_start: "2024-08-20"
    planned_end: "2024-08-24"
    actual_end: "2024-08-25"
    delay: "1 day"
    delay_reason: "Multi-AZ setup (+1 day)"

  metrics:
    planned:
      throughput: "10k writes/s"
      latency_p99: "80ms"
      cost: "$2.5k/month"
      timeline: "5 days"

    actual:
      throughput: "12k writes/s"  # ✓ BETTER
      latency_p99: "60ms"          # ✓ BETTER
      cost: "$3.3k/month"          # ✗ OVER BUDGET
      timeline: "6 days"           # ✗ DELAYED

  what_worked_better:
    - item: "Migration speed"
      expected: "2M rows w 60 min"
      actual: "2M rows w 15 min (4x faster)"
      reason: "COPY command zamiast INSERT"
      learning: "Always use COPY for bulk migrations"
      evidence: ["E-058"]

    - item: "Zero downtime"
      expected: "5-10 min downtime"
      actual: "0 downtime"
      reason: "Blue-green deployment z 5-min validation"
      learning: "Blue-green essential for DB migrations"
      evidence: ["E-059"]

  what_worked_worse:
    - item: "Budget overrun"
      expected: "$2.5k/month"
      actual: "$3.3k/month (+$800)"
      reason: "Multi-AZ nie był w oryginalnym planie"
      impact: "Wymaga recurrent approval co 6 miesięcy"
      mitigation: "CFO approved [E-056]"

    - item: "Connection pooling issue"
      expected: "No connection issues"
      actual: "Connection limit exceeded, required fix"
      reason: "Load test z 3 replicas, prod ma 5"
      learning: "Always load test with production-like topology"
      evidence: ["E-055"]

  what_we_would_do_differently:
    - "Zaplanować Multi-AZ od początku (nie jako reaktywna zmiana)"
    - "Load test z prod topology (5 replicas, nie 3)"
    - "Buffer budget +20% dla nieprzewidzianych kosztów"
    - "Daily standups podczas migration (było: tylko async Slack)"

  re_evaluation_triggers:
    - condition: "Traffic > 8k req/s sustained for 7 days"
      action: "Consider horizontal sharding"
      monitoring: "Grafana alert: traffic_req_per_sec > 8000"

    - condition: "Connection wait time > 50ms p99"
      action: "Increase pool size OR add pgBouncer"
      monitoring: "Grafana alert: connection_wait_p99 > 50"

    - condition: "Cost > $4k/month for 3 months"
      action: "Re-evaluate cheaper alternatives (managed vs self-hosted)"
      monitoring: "Monthly cost review"

  success_metrics_90_days:
    review_date: "2024-11-25"
    criteria:
      - metric: "Latency p99 < 80ms"
        target: "60ms"
        status: pending

      - metric: "Uptime > 99.9%"
        target: "99.9%"
        status: pending

      - metric: "Zero data loss incidents"
        status: pending

      - metric: "Budget < $3.5k/month"
        target: "$3.3k"
        status: pending

  action_items:
    - id: "ACTION-001"
      title: "Update load testing guidelines"
      owner: "DevOps"
      due: "2024-09-15"
      status: pending

    - id: "ACTION-002"
      title: "Create migration runbook template"
      owner: "Tech Lead"
      due: "2024-09-30"
      status: pending
```

### Kiedy Przeprowadzać Post-mortem?

#### Obligatoryjnie:
1. **Po ukończeniu major feature** (> 5 dni pracy)
2. **Po incydencie** (downtime, data loss, security breach)
3. **Po przekroczeniu budżetu/czasu** (>20% overrun)
4. **90 dni po deployment** (long-term metrics review)

#### Opcjonalnie:
5. **Po eksperymencie** (A/B test, spike, PoC)
6. **Po zmianie procesu** (nowy workflow)

### Funkcje Powiązane
- `F-107`: Tworzenie post-mortem
- `F-108`: Generowanie post-mortem z impl log
- `F-109`: Tracking action items
- `F-110`: Monitoring re-evaluation triggers
- `F-111`: Wykrywanie brakującego post-mortem (E200)

### Powiązania z Innymi Koncepcjami
- **C-017 (Implementation Log)**: Post-mortem bazuje na logu
- **C-011 (Satelita)**: Post-mortem jako satelita
- **C-005 (Bramka Jakości)**: Post-mortem gate (required before closing)
- **C-004 (Luka)**: Brak post-mortem = luka E200

---

# Koncepcje ZMODYFIKOWANE

## C-001: Dokument (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Edycja** | Edit in place | Immutable + versioning |
| **Bramki** | Brak | Bramki wejścia/wyjścia |
| **Historia** | Git log | Graf decyzyjny |
| **Changelog** | Opcjonalny | Obowiązkowy |

### Definicja V2
**Dokument** to niemutowalny artefakt dokumentacyjny z YAML frontmatter i markdown content, posiadający dedykowane bramki wejścia/wyjścia, graf decyzyjny i pełną ścieżkę audytową.

### Właściwości Dokumentu V2

```yaml
document:
  id: "ADR-005"
  title: "Wybór bazy danych dla Cart Service"
  type: adr
  version: "2.0"  # Immutable versioning
  status: approved

  lifecycle:
    created: "2024-08-15"
    updated: "2024-08-22"  # Każda edycja = nowa wersja
    approved: "2024-08-23"
    deployed: "2024-08-25"

  gates:
    input: [...]   # C-013: Bramki wejścia
    output: [...]  # C-013: Bramki wyjścia

  decision_graph: "DEC-ADR-005-001"  # C-014: Graf decyzyjny

  satellites:
    - "TODO-ADR-005"
    - "IMPL-LOG-ADR-005"
    - "POST-MORTEM-ADR-005"
    - "E-042"  # Evidence notes
    - "E-043"
    - "E-044"

  changelog:  # Obowiązkowy
    - version: "2.0"
      date: "2024-08-22"
      author: "Tech Lead"
      changes: "Updated budget ($2.5k → $3.3k) due to Multi-AZ"
      reason: "Incident [E-051] showed single-AZ = SPOF"
      approved_by: "CFO"
      evidence: ["E-056"]
```

### Funkcje Powiązane
- `F-001`: Parsowanie dokumentu (bez zmian)
- `F-002`: Ekstrakcja frontmatter (bez zmian)
- `F-112`: **NOWA** - Immutable versioning
- `F-113`: **NOWA** - Changelog generation
- `F-114`: **NOWA** - Gate management

---

## C-002: Typ Dokumentu (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Szablon** | Statyczny plik | Aktywny artefakt z metadanymi |
| **Quality Gates** | Osobna koncepcja | **Fuzja** z typem dokumentu |
| **Validation** | Binarna (pass/fail) | Severity-based (critical/high/medium/low) |
| **Bramki** | Brak | Allowed gates per type |

### Definicja V2
**Typ Dokumentu** to schema definiujące strukturę, wymagania walidacyjne, lifecycle gates i dozwolone bramki dla kategorii dokumentów (ADR, RFC, PRD, etc.).

### Struktura Document Type V2

```yaml
document_type:
  id: "adr"
  name: "Architecture Decision Record"
  domain: "architecture"

  template:  # Template jako aktywny artefakt
    file: "templates/adr-template-proof-system.md"
    placeholders:
      - "{{DECISION_TITLE}}"
      - "{{DECISION_DATE}}"
      - "{{DECISION_MAKER}}"
    auto_populated_fields:
      - "id" (auto-generated: ADR-XXX)
      - "created" (timestamp)
      - "status" (default: draft)

  required_sections:
    - name: "Context"
      pattern: "^## Context"
      mandatory: true
      validation_severity: critical
      min_words: 100
      storytelling_required: true

    - name: "Decision"
      pattern: "^## Decision"
      mandatory: true
      validation_severity: critical
      min_words: 50

    - name: "Alternatives Considered"
      pattern: "^## Alternatives Considered"
      mandatory: true
      validation_severity: high
      min_items: 2  # Minimum 2 opcje alternatywne

    - name: "Consequences"
      pattern: "^## Consequences"
      mandatory: true
      validation_severity: high

    - name: "Evidence Trail"
      pattern: "^## Evidence Trail"
      mandatory: true
      validation_severity: medium
      min_evidence_notes: 2

  internal_gates:  # Bramki wewnętrzne (między sekcjami)
    - source: "Context"
      impacts: ["Decision", "Alternatives Considered"]
      reason: "Context defines constraints for options"

    - source: "Decision"
      impacts: ["Consequences"]
      reason: "Decision determines consequences"

  allowed_gates:  # Dozwolone bramki globalne
    input:
      - type: "requires"
        target_types: ["rfc", "prd", "adr"]

      - type: "informs"
        target_types: ["*"]  # Wszystkie typy

    output:
      - type: "blocks"
        target_types: ["implementation", "deployment"]
        until_status: ["approved"]

      - type: "informs"
        target_types: ["*"]

  lifecycle_gates:  # C-005: Bramki jakości per status
    - name: "DRAFT-COMPLETE"
      from_status: "draft"
      to_status: "review"
      conditions:
        - "All required sections present"
        - "No TODO/TBD placeholders"
        - "Minimum 2 alternatives documented"
        - "Decision graph created"

    - name: "REVIEW-PASS"
      from_status: "review"
      to_status: "approved"
      conditions:
        - "All critical gaps resolved"
        - "Peer review completed"
        - "Stakeholder sign-off obtained [E-XXX]"
        - "Evidence trail complete"

    - name: "DEPLOYED"
      from_status: "approved"
      to_status: "deployed"
      conditions:
        - "Implementation log created"
        - "DoD checklist completed"

    - name: "CLOSED"
      from_status: "deployed"
      to_status: "closed"
      conditions:
        - "Post-mortem completed (90 days after deploy)"
        - "All action items resolved"

  required_satellites:
    - type: "todo"
      auto_generate: true
      template: "templates/todo-template.md"

    - type: "dor"
      mandatory_for_status: ["review", "approved"]

    - type: "dod"
      mandatory_for_status: ["deployed"]

    - type: "implementation-log"
      mandatory_for_status: ["deployed"]

    - type: "post-mortem"
      mandatory_for_status: ["closed"]
      trigger: "90 days after deployed"

    - type: "evidence"
      min_count: 2
      types: ["benchmark", "analysis", "approval"]

  gap_detection:
    - id: "E110"
      condition: "missing required section"
      severity: "critical"

    - id: "E180"
      condition: "section lacks storytelling"
      severity: "medium"

    - id: "E190"
      condition: "alternatives < 2"
      severity: "high"
```

### Funkcje Powiązane
- `F-005`: Load document type schema (rozszerzona)
- `F-115`: **NOWA** - Validate lifecycle gate
- `F-116`: **NOWA** - Validate allowed gates
- `F-117`: **NOWA** - Generate satellites per type

---

## C-003: Graf Zależności (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA → Graf Decyzyjny

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Nazwa** | Graf Zależności | Graf Decyzyjny |
| **Zawartość** | Co zależy od czego | Kontekst + opcje + uzasadnienia |
| **Opcje** | Tylko wybrane | **Wszystkie** (również odrzucone) |
| **Kontekst** | Brak | Kontekst T₀ + constraints |
| **Evidence** | Brak | Evidence nodes per opcja |

### Definicja V2
**Graf Decyzyjny** to directed graph reprezentujący pełną historię decyzji, zawierający kontekst w momencie decyzji, wszystkie rozważane opcje (również odrzucone), uzasadnienia porównawcze i evidence trail.

### Struktura Grafu V2

```python
class DecisionGraph:
    # Nodes
    decision_nodes: List[DecisionNode]  # Decyzje
    option_nodes: List[OptionNode]      # Opcje (selected + rejected)
    context_nodes: List[ContextNode]    # Kontekst T₀
    evidence_nodes: List[EvidenceNode]  # Noty dowodowe

    # Edges
    context_influences: List[Edge]      # Kontekst → Decyzja
    option_belongs_to: List[Edge]       # Opcja → Decyzja
    option_rejected_by: List[Edge]      # Opcja → Reason
    option_selected: List[Edge]         # Opcja → Decyzja
    evidence_supports: List[Edge]       # Evidence → Opcja

    # Properties
    def get_rejected_options(self, decision_id: str) -> List[OptionNode]:
        """Zwraca opcje odrzucone dla decyzji"""

    def get_selection_rationale(self, decision_id: str) -> SelectionRationale:
        """Zwraca uzasadnienie wyboru (dlaczego X a nie Y)"""

    def get_context_at_time(self, decision_id: str) -> ContextSnapshot:
        """Zwraca kontekst w momencie decyzji"""
```

### Funkcje Powiązane
- `F-009`: Build decision graph (rozszerzona)
- `F-086`: **NOWA** - Create decision node
- `F-087`: **NOWA** - Register all options (not just selected)
- `F-088`: **NOWA** - Capture context T₀
- `F-089`: **NOWA** - Register comparative justifications
- `F-090`: **NOWA** - Visualize decision graph (Mermaid)

---

## C-004: Luka (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Typy** | E110-E160 (6 typów) | E110-E200 (10 typów) |
| **Evidence** | Nie wykrywa | **E170**: Brakująca nota dowodowa |
| **Storytelling** | Nie wykrywa | **E180**: Brak narracji |
| **Opcje** | Nie wykrywa | **E190**: Brak opcji alternatywnych |
| **Post-mortem** | Nie wykrywa | **E200**: Brak retrospektywy |

### Typy Luk V2

#### Typy ze V1 (bez zmian):
- **E110**: Brakująca wymagana sekcja
- **E120**: Placeholder detected (TODO/TBD)
- **E130**: Brakujący dokument satellite/evidence
- **E140**: Broken dependency (dokument nie istnieje)
- **E150**: Gate blocker (bramka jakości nie spełniona)
- **E160**: Brakujące zatwierdzenie (approval)

#### Typy NOWE w V2:
- **E170**: Brakująca nota dowodowa
  ```yaml
  gap:
    id: "E170"
    type: "missing-evidence"
    severity: high
    location: "prd.md:245"
    claim: "System must handle 10k req/s"
    message: "Claim lacks evidence note [E-XXX]"
    remediation:
      - "Add evidence note referencing traffic analysis"
      - "Create evidence document if not exists"
  ```

- **E180**: Brak storytelling (tylko lista faktów)
  ```yaml
  gap:
    id: "E180"
    type: "missing-storytelling"
    severity: medium
    location: "adr-005.md:150-160"
    section: "Decision"
    message: "Section contains facts only, lacks narrative"
    remediation:
      - "Describe decision process"
      - "Add alternatives considered"
      - "Justify choice comparatively"
  ```

- **E190**: Brak opcji alternatywnych w decyzji
  ```yaml
  gap:
    id: "E190"
    type: "missing-alternatives"
    severity: high
    location: "adr-005.md"
    decision: "DEC-ADR-005-001"
    alternatives_found: 1
    alternatives_required: 2
    message: "Decision has only 1 option, minimum 2 required"
    remediation:
      - "Document at least 1 alternative option"
      - "Explain why alternative was rejected"
  ```

- **E200**: Brak post-mortem (>30 dni po deploy)
  ```yaml
  gap:
    id: "E200"
    type: "missing-postmortem"
    severity: medium
    location: "adr-005.md"
    deployed_date: "2024-08-25"
    days_since_deploy: 95
    trigger: "Post-mortem required 90 days after deploy"
    message: "Post-mortem overdue by 5 days"
    remediation:
      - "Create post-mortem document"
      - "Review implementation log"
      - "Analyze success metrics"
  ```

### Funkcje Powiązane
- `F-014` - `F-019`: Detekcja E110-E160 (bez zmian)
- `F-100`: **NOWA** - Detect missing evidence (E170)
- `F-093`: **NOWA** - Detect missing storytelling (E180)
- `F-091`: **NOWA** - Detect missing alternatives (E190)
- `F-111`: **NOWA** - Detect missing post-mortem (E200)

---

## C-005: Bramka Jakości (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA → Lifecycle Gates

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Nazwa** | Bramka Jakości | Lifecycle Gates |
| **Zakres** | Per document | Per document type + per status transition |
| **Fazy** | Tylko DoD | **DoR + Implementation + DoD + Post-mortem** |
| **Integracja** | Osobna koncepcja | **Fuzja** z C-002 (Typ Dokumentu) |

### Definicja V2
**Lifecycle Gates** to zestaw warunków, które muszą być spełnione aby dokument mógł przejść z jednego statusu do drugiego, obejmujący cały cykl życia: DoR → Implementation → DoD → Post-mortem.

### Fazy Lifecycle Gates

#### Faza 1: Definition of Ready (DoR)
```yaml
gate:
  name: "DoR-ADR"
  from_status: null
  to_status: "draft"
  conditions:
    - "Problem statement defined"
    - "Stakeholders identified"
    - "Success criteria defined"
    - "Decision graph initialized"
```

#### Faza 2: Implementation Gate
```yaml
gate:
  name: "IMPL-GATE"
  from_status: "approved"
  to_status: "in-progress"
  conditions:
    - "Implementation log created"
    - "Resources allocated"
    - "Timeline agreed"
```

#### Faza 3: Definition of Done (DoD)
```yaml
gate:
  name: "DoD-ADR"
  from_status: "in-progress"
  to_status: "deployed"
  conditions:
    - "All acceptance criteria met"
    - "Implementation log complete"
    - "Metrics before/after measured"
    - "Tests passed"
    - "Documentation updated"
```

#### Faza 4: Post-mortem Gate
```yaml
gate:
  name: "POST-MORTEM-GATE"
  from_status: "deployed"
  to_status: "closed"
  trigger: "90 days after deploy"
  conditions:
    - "Post-mortem completed"
    - "Action items tracked"
    - "Re-evaluation triggers defined"
    - "Success metrics reviewed"
```

### Funkcje Powiązane
- `F-030`: **ROZSZERZONA** - Evaluate lifecycle gates
- `F-115`: **NOWA** - Validate status transition
- `F-118`: **NOWA** - Check DoR gate
- `F-119`: **NOWA** - Check DoD gate
- `F-120`: **NOWA** - Check post-mortem gate

---

## C-008: Metadata (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Pola** | Podstawowe (id, title, type, status) | +decision_date, +context_snapshot, +evidence_ids |
| **Decision tracking** | Brak | decision_date, decision_maker |
| **Context** | Brak | context_snapshot (T₀) |
| **Evidence** | Brak | evidence_ids (lista [E-XXX]) |

### Struktura Frontmatter V2

```yaml
---
# Podstawowe (bez zmian)
id: "ADR-005"
title: "Wybór bazy danych dla Cart Service"
type: adr
status: approved
created: "2024-08-15"
updated: "2024-08-22"
owner: "Tech Lead"

# NOWE pola w V2
decision_date: "2024-08-15"  # Kiedy podjęto decyzję
decision_maker: ["Tech Lead", "Backend Team"]

context_snapshot:  # Stan w momencie decyzji T₀
  budget: "$5k/month"
  team_size: 2
  timeline: "Launch by 2024-10-01"
  constraints:
    - "GDPR compliance"
    - "ACID required (ADR-003)"

evidence_ids:  # Wszystkie noty dowodowe
  - "E-042"  # MongoDB benchmark
  - "E-043"  # MySQL benchmark
  - "E-044"  # PostgreSQL benchmark
  - "E-045"  # DynamoDB cost
  - "E-051"  # Incident (cold cache)
  - "E-056"  # CFO approval

alternatives_considered:  # Opcje odrzucone
  - id: "OPTION-A"
    title: "MongoDB"
    status: rejected
    reason: "Brak ACID"
  - id: "OPTION-B"
    title: "MySQL"
    status: rejected
    reason: "Słaba wydajność write"
  - id: "OPTION-C"
    title: "PostgreSQL"
    status: selected
  - id: "OPTION-D"
    title: "DynamoDB"
    status: rejected
    reason: "Over budget"

# Bramki (C-013)
gates:
  input:
    - id: "RFC-2024-08"
      type: requires
    - id: "ADR-003"
      type: requires
  output:
    - id: "IMPL-CART-DB"
      type: blocks
    - id: "OPS-RUNBOOK-07"
      type: informs

# Satelity (bez zmian)
satellites:
  - "TODO-ADR-005"
  - "IMPL-LOG-ADR-005"
  - "POST-MORTEM-ADR-005"
---
```

### Funkcje Powiązane
- `F-002`: Extract frontmatter (rozszerzona)
- `F-033`: **ROZSZERZONA** - Manage metadata
- `F-121`: **NOWA** - Extract decision metadata
- `F-122`: **NOWA** - Extract context snapshot
- `F-123`: **NOWA** - Track alternatives

---

## C-011: Satelita (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Typy** | TODO, DOR, DOD, RTM | +IMPL-LOG, +POST-MORTEM, +EVIDENCE |
| **Auto-generation** | Tylko TODO | TODO + IMPL-LOG + POST-MORTEM |
| **Lifecycle** | Statyczne | Lifecycle-aware (tworzenie per status) |

### Typy Satelitów V2

#### Typy ze V1 (bez zmian):
- **TODO**: Lista zadań
- **DOR**: Definition of Ready
- **DOD**: Definition of Done
- **RTM**: Requirements Traceability Matrix

#### Typy NOWE w V2:
- **IMPL-LOG**: Implementation Log (C-017)
  ```yaml
  satellite:
    id: "IMPL-LOG-ADR-005"
    type: implementation-log
    parent: "ADR-005"
    auto_generate: true
    trigger: "status == in-progress"
    template: "templates/impl-log-template.md"
  ```

- **POST-MORTEM**: Retrospektywa (C-018)
  ```yaml
  satellite:
    id: "POST-MORTEM-ADR-005"
    type: post-mortem
    parent: "ADR-005"
    auto_generate: true
    trigger: "90 days after deployed"
    template: "templates/post-mortem-template.md"
  ```

- **EVIDENCE**: Noty dowodowe (C-016)
  ```yaml
  satellite:
    id: "E-042"
    type: evidence
    parent: "ADR-005"
    evidence_type: benchmark
    auto_generate: false  # Ręcznie tworzone
  ```

### Funkcje Powiązane
- `F-036` - `F-038`: Generowanie satelitów (rozszerzone)
- `F-124`: **NOWA** - Generate implementation log
- `F-125`: **NOWA** - Generate post-mortem
- `F-126`: **NOWA** - Link evidence notes

---

## C-012: Domena (ZMODYFIKOWANA)

### Status: 🔄 ZMODYFIKOWANA

### Zmiany względem V1

| Aspekt | V1 | V2 |
|--------|----|----|
| **Reguły** | Basic validation rules | +Policy Maps |
| **Priorities** | Brak | Domain-specific priorities |
| **Workflows** | Brak | Domain-specific workflows |

### Policy Maps (NOWE)

```yaml
domain:
  id: "architecture"
  name: "Architecture Domain"

  policy_map:
    - rule: "Load testing before approval"
      applies_to: ["adr"]
      condition: "type == adr AND impacts infrastructure"
      requirement:
        - "Load test results [E-XXX] required"
        - "Performance benchmarks documented"
      severity: critical

    - rule: "Cross-team review for major changes"
      applies_to: ["adr", "rfc"]
      condition: "impacts multiple services"
      requirement:
        - "Review by affected teams"
        - "Approval from service owners"
      severity: high

    - rule: "Monitoring FIRST, implementation SECOND"
      applies_to: ["implementation"]
      condition: "new feature OR infrastructure change"
      requirement:
        - "Monitoring dashboard created"
        - "Alerts configured"
        - "Runbook updated"
      before: "deployment"
      severity: critical
```

### Funkcje Powiązane
- `F-039`: Register domain (bez zmian)
- `F-040`: **ROZSZERZONA** - Domain-specific validation
- `F-127`: **NOWA** - Enforce policy maps
- `F-128`: **NOWA** - Domain-specific workflows

---

# Koncepcje BEZ ZMIAN

## C-006: Walidator (BEZ ZMIAN)

### Status: ✅ BEZ ZMIAN

### Definicja
System walidacji dokumentów względem schematów typów dokumentów, sprawdzający poprawność frontmatter, wymaganych sekcji i ograniczeń.

### Funkcje Powiązane
- `F-005`: Validate document schema
- `F-006`: Validate frontmatter
- `F-007`: Validate required sections
- `F-008`: Detect placeholders

---

## C-007: Parser (BEZ ZMIAN)

### Status: ✅ BEZ ZMIAN

### Definicja
Moduł parsujący pliki Markdown z YAML frontmatter, ekstrahujący metadane, sekcje i odniesienia do innych dokumentów.

### Funkcje Powiązane
- `F-001`: Parse markdown files
- `F-002`: Extract YAML frontmatter
- `F-003`: Identify sections
- `F-004`: Detect references

---

## C-009: Połączenie (Edge) (BEZ ZMIAN)

### Status: ✅ BEZ ZMIAN

### Definicja
Typowane połączenie między węzłami grafu (dokumentami), reprezentujące zależność semantyczną (requires, implements, references, tests, etc.).

### Funkcje Powiązane
- `F-011`: Manage edges
- `F-034`: Create and validate edges

---

## C-010: Węzeł (Node) (BEZ ZMIAN)

### Status: ✅ BEZ ZMIAN

### Definicja
Reprezentacja dokumentu w grafie zależności, zawierająca metadane dokumentu i obliczone właściwości (luki, blokery, poziom hierarchii).

### Funkcje Powiązane
- `F-010`: Manage nodes
- `F-035`: Calculate node properties

---

← [Poprzednia: Filozofia](./koncepcje-v2-filozofia.md) | [Powrót do głównego dokumentu](./koncepcje-v2.md) | [Następna: Mapowanie →](./koncepcje-v2-mapowanie.md)
