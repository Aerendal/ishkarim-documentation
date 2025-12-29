# HYPOTHESIS-DOC: Ishkarim - Migracja bazy dokumentów na MongoDB

---

## Document Metadata

```yaml
id: HYPOTHESIS-001
doctype: HYPOTHESIS-DOC
status: approved
version: 1.0
created: 2025-12-15
updated: 2025-12-20
owner: Jan Kowalski
project: Ishkarim Document Management System
hypothesis_type: technical
```

---

## Cross-References

```yaml
dependencies:
  - id: PRODUCT-BACKLOG-042
    type: research_input
    reason: "Story US-042 wymaga rozwiązania problemów z wydajnością wyszukiwania"
  - id: INNOVATION-ROADMAP-Q1-2026
    type: strategic_alignment
    reason: "Aligned z inicjatywą modernizacji stacku technicznego"

impacts:
  - id: EXPERIMENT-LOG-001
    type: blocks
    reason: "Eksperyment walidacyjny nie może się rozpocząć bez zatwierdzonej hipotezy"
  - id: ADR-042
    type: influences
    reason: "Wyniki walidacji hipotezy wpłyną na decyzję o wyborze bazy danych"
```

---

## SEC-HYP-CONTEXT: Kontekst i motywacja

### Problem do rozwiązania

Obecna implementacja Ishkarim wykorzystuje PostgreSQL jako główną bazę danych dla wszystkich typów dokumentów. W miarę wzrostu liczby dokumentów (obecnie ~15,000 dokumentów w typowym projekcie) obserwujemy problemy z wydajnością:

- Wyszukiwanie full-text po treści dokumentów Markdown: średni czas odpowiedzi 2.5s
- Zapytania o graf zależności między dokumentami: 1.8s dla grafu 1000+ połączeń
- Indeksowanie nowych dokumentów: ~500ms per document

Użytkownicy zgłaszają, że system staje się "powolny" przy większych projektach, co wpływa na produktywność zespołów dokumentacyjnych.

### Dlaczego teraz

1. **Wzrost adopcji**: 5 nowych klientów enterprise w Q4 2025, planują projekty 50,000+ dokumentów
2. **Konkurencja**: Notion i Confluence oferują search <100ms
3. **Roadmap Q1 2026**: Real-time collaboration wymaga szybkiego dostępu do dokumentów
4. **Techniczny dług**: Obecna struktura relacyjna dla dokumentów Markdown jest anty-wzorcem

### Background

- PostgreSQL 14.5, hosted na AWS RDS (db.t3.large)
- Dokumenty przechowywane jako TEXT w kolumnie `content`
- Full-text search używa `tsvector` i `GIN` index
- Graf zależności modelowany jako self-referencing many-to-many table
- Średni rozmiar dokumentu: 15KB Markdown

Wcześniejsze próby optymalizacji (dodanie indeksów, tuning PostgreSQL) przyniosły tylko 15% poprawę.

---

## SEC-HYP-STATEMENT: Stwierdzenie hipotezy (H0/H1)

### Hipoteza zerowa (H0)

Migracja z PostgreSQL na MongoDB nie poprawi wydajności operacji wyszukiwania i grafowych o więcej niż 20% przy jednoczesnym zachowaniu pełnej funkcjonalności systemu.

### Hipoteza alternatywna (H1)

Migracja z PostgreSQL na MongoDB poprawi:
- Wydajność full-text search o minimum 60% (z 2.5s do <1.0s)
- Wydajność zapytań grafowych o minimum 50% (z 1.8s do <0.9s)
- Czas indeksowania nowych dokumentów o 40% (z 500ms do <300ms)

przy zachowaniu 100% obecnej funkcjonalności i bez degradacji niezawodności systemu.

### Scope

**W zakresie:**
- Migracja storage warstwy dla dokumentów Markdown (.md, .canvas)
- Full-text search z wykorzystaniem MongoDB Atlas Search
- Graf zależności dokumentów (graph queries)
- Metadata i frontmatter dokumentów
- Wersjonowanie dokumentów (change history)

**Poza zakresem:**
- Migracja user authentication/authorization (pozostaje w PostgreSQL)
- Billing i subscription data (pozostaje w PostgreSQL)
- Audit logs (pozostają w PostgreSQL)
- Real-time collaboration infrastructure (odrębna hipoteza)

---

## SEC-HYP-ASSUMPTIONS: Założenia

### Założenia techniczne

- MongoDB Atlas z Search będzie dostępne w naszym AWS regionie (eu-central-1)
- Team ma podstawową wiedzę o NoSQL (3/5 developerów pracowało z MongoDB)
- Istniejące narzędzia do backup/restore będą kompatybilne lub zastępowalne
- Python driver (pymongo) jest stabilny i production-ready
- MongoDB 7.0+ wspiera wszystkie potrzebne features (transactions, aggregation pipeline)

### Założenia biznesowe

- Budget na infrastrukturę może wzrosnąć o max 30% (obecnie $800/mth PostgreSQL RDS)
- Czas migracji danych może wynieść max 2 tygodnie downtime (lub zero-downtime migration)
- Klienci akceptują potential breaking changes w API (z odpowiednim notice period)
- ROI osiągniemy w ciągu 6 miesięcy (poprzez reduced churn + nowi klienci)

### Założenia dotyczące zasobów

- 2 backend developers dostępni full-time przez 6 tygodni
- 1 DevOps engineer dostępny part-time (50%) przez 4 tygodnie
- Dostęp do staging environment identycznego jak production
- Budget na PoC/eksperyment: $2,000 (infrastructure + Atlas credits)

### Ograniczenia

- Nie możemy zmieniać API endpoints (zachowanie backward compatibility)
- Migracja musi być reversible (rollback plan obowiązkowy)
- Zero utraty danych podczas migracji
- GDPR compliance musi być zachowane (data residency w EU)

---

## SEC-HYP-SUCCESS-CRITERIA: Kryteria sukcesu/porażki

### Kryteria sukcesu (walidacja H1)

- [x] **Performance - Search**: Full-text search średnio <1.0s (baseline: 2.5s) ✅ Target: -60%
- [x] **Performance - Graph**: Graph queries średnio <0.9s (baseline: 1.8s) ✅ Target: -50%
- [x] **Performance - Indexing**: Document indexing <300ms (baseline: 500ms) ✅ Target: -40%
- [ ] **Functional**: 100% feature parity z obecnym systemem
- [ ] **Reliability**: Uptime ≥99.5% w 3-month pilot period
- [ ] **Cost**: Infrastructure cost ≤$1,040/mth (+30% vs baseline)
- [ ] **Migration**: Zero data loss during migration (verified checksums)

### Kryteria porażki (odrzucenie H1)

- [ ] Którakolwiek metryka performance NIE spełnia targetu
- [ ] Data loss >0 dokumentów podczas migracji
- [ ] Uptime <99% w pilot period
- [ ] Cost >$1,200/mth (+50% przekracza budżet)
- [ ] Brak możliwości implementacji critical features (np. transactions)

### Metryki

| Metryka | Baseline (obecny) | Target (oczekiwany) | Measurement method |
|---------|------------------|---------------------|-------------------|
| Full-text search latency (p95) | 2.5s | <1.0s | JMeter load test, 1000 concurrent queries |
| Graph query latency (p95) | 1.8s | <0.9s | Custom benchmark, dependency graph 1000 nodes |
| Document indexing time | 500ms | <300ms | Time measurement in ingestion pipeline |
| Monthly infrastructure cost | $800 | <$1,040 | AWS + Atlas billing |
| System uptime | 99.7% | ≥99.5% | Uptime monitoring (Datadog) |

---

## SEC-HYP-METHODOLOGY: Metodologia walidacji

### Podejście

Walidacja hipotezy będzie przeprowadzona w 3 fazach:

1. **PoC (Proof of Concept)** - 2 tygodnie
   - Minimal prototype z MongoDB
   - Import 10,000 sample documents
   - Benchmark queries vs PostgreSQL

2. **Pilot Deployment** - 4 tygodnie
   - Migracja 1 internal project (Ishkarim docs, ~5,000 docs)
   - Monitoring performance w production-like environment
   - User acceptance testing z internal team

3. **Validation** - 2 tygodnie
   - Analiza zebranych metryk
   - Stress testing i failure scenarios
   - Cost analysis (actual vs projected)

### Procedura

1. **Setup MongoDB Atlas cluster** (M30 tier, same as current RDS specs)
2. **Implement data migration script** (PostgreSQL → MongoDB)
3. **Adapt data access layer** (Repository pattern, swap implementations)
4. **Run benchmark suite** (JMeter scripts for search, graph queries)
5. **Deploy to staging** z real-world dataset
6. **Monitor for 4 weeks** (performance, errors, cost)
7. **Analyze results** vs success criteria
8. **Decision**: Proceed / Pivot / Stop

### Narzędzia i technologie

- **MongoDB Atlas**: M30 cluster (8GB RAM, 2 vCPU) - production-equivalent
- **MongoDB Atlas Search**: Lucene-based full-text search
- **pymongo**: Python driver dla MongoDB
- **JMeter**: Load testing i benchmarking
- **Datadog**: Monitoring, alerting, uptime tracking
- **Python scripts**: Data migration, validation, checksums

### Środowisko testowe

- **Staging environment**: AWS eu-central-1
- **MongoDB Atlas**: M30 dedicated cluster (same region)
- **Dataset**: 10,000 dokumentów (mix of .md, .canvas) - łącznie 150MB
- **Network**: Same VPC as production, private peering to Atlas
- **Load**: Simulate 50 concurrent users (average production load)

---

## SEC-HYP-RESOURCES: Wymagane zasoby

### Zespół

- **Backend Developer #1**: Lead developer - 100% przez 6 tygodni
  - Design data model
  - Implement migration scripts
  - Adapt data access layer

- **Backend Developer #2**: Developer - 100% przez 4 tygodnie (weeks 2-5)
  - Implement search functionality
  - Benchmarking i testing
  - Documentation

- **DevOps Engineer**: Infrastructure - 50% przez 4 tygodnie
  - Setup MongoDB Atlas
  - Configure monitoring
  - Migration automation

- **QA Engineer**: Testing - 25% przez 6 tygodni
  - Test plan execution
  - User acceptance testing
  - Performance validation

### Infrastruktura

- **MongoDB Atlas M30 cluster**: 2 months @ $350/month = $700
- **Additional staging resources**: AWS EC2, S3 = $200
- **Monitoring tools**: Datadog trial (free) lub existing subscription
- **Data transfer costs**: ~$100 (one-time)

### Budget

- Infrastructure (Atlas + AWS): $1,000
- Team time (fully loaded cost): ~$24,000 (240 hours @ $100/hr blended rate)
- Tools & licenses: $0 (using existing or trials)
- Contingency (10%): $2,500
- **Total:** $27,500

**Note**: Jeśli hipoteza potwierdzona → produkcyjna implementacja to kolejne ~$50,000 (pełna migracja, 12 tygodni)

---

## SEC-HYP-TIMELINE: Timeboxing

### Harmonogram

- **Start date:** 2026-01-06 (po świętach)
- **End date:** 2026-02-28 (8 tygodni total)
- **Duration:** 8 tygodni (6 tygodni aktywnej pracy + 2 tygodnie analiza/decyzja)

### Milestones

- [x] **2026-01-10**: PoC environment setup complete ✅
- [x] **2026-01-17**: Data migration script working ✅
- [ ] **2026-01-24**: Benchmark suite complete (week 3)
- [ ] **2026-01-31**: Pilot deployment to staging (week 4)
- [ ] **2026-02-14**: 2-week monitoring period complete (week 6)
- [ ] **2026-02-21**: Final validation & analysis (week 7)
- [ ] **2026-02-28**: Go/No-Go decision + ADR (week 8)

### Timebox constraint

8 tygodni to maksymalny czas na walidację hipotezy, ponieważ:
- Q1 2026 roadmap wymaga decyzji do końca lutego
- Nowi klienci enterprise onboarding w marcu (potrzebują performance commitments)
- Team availability (po marcu rozpoczynają inny project)
- Budget cycle - jeśli Proceed, potrzebujemy approval na Q2 spending

**Hard deadline**: 2026-02-28 - no extensions.

---

## TODO_SECTION: Zadania do wykonania

### Do zrobienia

- [ ] Zatwierdzenie budżetu przez CTO (Jan Kowalski → email do CTO)
- [ ] Setup MongoDB Atlas account i cluster (DevOps team)
- [ ] Prepare dataset dla PoC (10K docs z anonymized production data)
- [ ] Design MongoDB schema dla documents + dependencies
- [ ] Implement migration script v0.1

### W trakcie

- **W przygotowaniu**: JMeter benchmark scripts (Developer #2)
- **W przygotowaniu**: Data access layer abstraction (Developer #1)

### Zrealizowane

- [x] Draft hipotezy i success criteria (2025-12-15)
- [x] Stakeholder alignment meeting (2025-12-18)
- [x] Budget request submitted (2025-12-19)
- [x] Approval od Product Owner (2025-12-20)

---

## EVIDENCE: Dowody i dane wspierające

### Wstępne badania

- **MongoDB Case Studies**: [Uber](https://www.mongodb.com/blog/post/from-0-to-10-million-users-in-3-years) - similar use case, 70% latency improvement
- **Competitor analysis**: Notion uses MongoDB for document storage (confirmed via job postings)
- **Internal survey**: 12/15 developers prefer working with document DBs for unstructured content

### Poprzednie eksperymenty

- **2025-Q3**: PostgreSQL tuning (indexes, query optimization) → only 15% improvement
- **2025-Q2**: Elasticsearch spike dla search → good performance but adds complexity (separate system)

### Data sources

- Production metrics (last 6 months): Datadog dashboards
- User complaints: Support tickets #1234, #1456, #1789 (all mention "slow search")
- Customer feedback: NPS survey comments mention performance 23 times

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| 2025-12-15 | 0.1 | Jan Kowalski | Initial draft |
| 2025-12-18 | 0.5 | Jan Kowalski | Added success criteria po feedback od team |
| 2025-12-19 | 0.9 | Jan Kowalski | Budget i timeline refinement |
| 2025-12-20 | 1.0 | Jan Kowalski | Approved by Product Owner (Anna Nowak) |

---

## Notatki i uwagi

### Obawy zespołu (z meeting 2025-12-18)

- **Anna (PO)**: Czy MongoDB jest wystarczająco mature dla enterprise? → TAK, używa to m.in. eBay, Adobe, Cisco
- **Piotr (Backend)**: Jak zrobimy transactions (ACID)? → MongoDB 4.0+ wspiera multi-document transactions
- **Kasia (DevOps)**: Backup/restore strategy? → Atlas ma automated backups, point-in-time recovery

### Ryzyko mitygacji

Największe ryzyko: **Unknown unknowns w production**
- Mitigacja: Pilot deployment na internal project (low-risk environment)
- Rollback plan: Dual-write mode (PostgreSQL + MongoDB) przez 1 miesiąc

### Następne kroki po aprovaL

→ Create **EXPERIMENT-LOG-001** (tracking execution)
→ Create **POC-DOC-001** (PoC documentation)
→ Schedule **weekly sync** z stakeholderami

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** innovation
