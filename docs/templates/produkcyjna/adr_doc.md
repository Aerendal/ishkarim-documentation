# 📄 Architecture Decision Records (ADR)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: requires
    reason: "High-Level Architecture defines architectural context and constraints for decisions"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "High-Level Architecture §2 Architecture Overview"
        to: "§3 Context"
        influence: "Current architecture provides context for architectural decisions"
      - from: "High-Level Architecture §4 Integration Points"
        to: "§8 Dependencies & Impacts"
        influence: "Integration architecture affects architectural decision impacts"

  - id: TDD-*
    type: influences
    reason: "TDD may contain technical constraints that inform architectural decisions"
    conditions:
      - when: "tdd.exists === true"
        applies: true
    sections:
      - from: "TDD §8 Technical Constraints"
        to: "§3 Context"
        influence: "Technical constraints frame the decision context"

  - id: PRD-*
    type: influences
    reason: "PRD defines requirements that drive architectural decisions"
    conditions:
      - when: "decision.driven_by === 'requirements'"
        applies: true
    sections:
      - from: "PRD §6 Non-Functional Requirements"
        to: "§3 Context"
        influence: "NFRs (performance, scalability, security) drive architectural choices"

  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter defines budget and timeline constraints affecting architectural decisions"
    conditions:
      - when: "decision.has_budget_impact === true"
        applies: true
    sections:
      - from: "Project Charter §14 Budget Allocation"
        to: "§6 Pros & Cons"
        influence: "Budget constraints affect technology selection and architecture choices"
```

### Impacts
```yaml
impacts:
  - id: TDD-*
    type: blocks
    reason: "ADR decisions must be incorporated into Technical Design Document"
    conditions:
      - when: "adr.status === 'accepted'"
        applies: true
      - when: "adr.status === 'proposed'"
        applies: false
    sections:
      - from: "§4 Decision"
        to: "TDD §3 System Architecture"
        influence: "Accepted architectural decisions define system architecture"
      - from: "§7 Consequences"
        to: "TDD §8 Technical Constraints"
        influence: "Decision consequences become technical constraints"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "ADRs refine and evolve the high-level architecture"
    conditions:
      - when: "adr.status === 'accepted'"
        applies: true
    sections:
      - from: "§4 Decision"
        to: "High-Level Architecture §2 Architecture Overview"
        influence: "Architectural decisions update the high-level architecture diagrams"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Infrastructure and deployment decisions affect deployment procedures"
    conditions:
      - when: "adr.category === 'infrastructure' || 'deployment'"
        applies: true
    sections:
      - from: "§4 Decision"
        to: "Deployment Guide §2 Installation Steps"
        influence: "Architectural decisions determine deployment requirements and procedures"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: informs
    reason: "Architectural decisions introduce new operational risks"
    conditions:
      - when: "adr.has_operational_impact === true"
        applies: true
    sections:
      - from: "§7 Consequences"
        to: "Operational Risk Assessment §3 Risk Inventory"
        influence: "Negative consequences and trade-offs become operational risks"
```

### Related
```yaml
related:
  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Feasibility studies inform technology selection decisions"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Technical risks identified may drive architectural decisions"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor technology selections documented as ADRs"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ADR-*.md"
    required: false
    purpose: "Track implementation tasks resulting from architectural decisions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ADR-*.md"
    required: true
    purpose: "Store benchmarks, proof-of-concepts, research findings supporting decisions"

  - type: DoR
    path: "satellites/dor/DOR-ADR-*.md"
    required: false
    purpose: "Define prerequisites before making architectural decision (research, POCs, stakeholder input)"

  - type: DoD
    path: "satellites/dod/DOD-ADR-*.md"
    required: true
    purpose: "Define completion criteria: decision documented, reviewed, approved, communicated to team"
```

## Cel biznesowy / techniczny
Architecture Decision Records (ADR) dokumentują kluczowe decyzje architektoniczne podejmowane w projekcie wraz z ich uzasadnieniem. Pozwalają na przejrzystość i śledzenie ewolucji architektury systemu.

## Zawartość

### Title
Zwięzły tytuł decyzji (np. "ADR-001: Wybór bazy danych NoSQL dla user sessions").

### Status
Status decyzji: Proposed / Accepted / Deprecated / Superseded (z linkiem do ADR który zastąpił).

### Context
Kontekst biznesowy i techniczny, który doprowadził do potrzeby podjęcia decyzji. Jakie wymagania/problemy musimy rozwiązać?

### Decision
Jasny opis podjętej decyzji architektonicznej i wybranego rozwiązania.

### Alternatives Considered
Lista rozważanych alternatyw z opisem każdej opcji i powodów odrzucenia.

### Pros & Cons
Argumenty za i przeciw wybranego rozwiązania w kontekście:
- Performance
- Scalability
- Maintainability
- Cost
- Team expertise
- Time to market

### Consequences
Konsekwencje decyzji:
- Pozytywne (korzyści, możliwości)
- Negatywne (trade-offs, ryzyka, długi techniczny)
- Neutralne (zmiany wymagające adaptacji)

### Technical Implications
Wpływ na architekturę systemu, integracje, performance, security.

### Dependencies & Impacts
Zależności od innych systemów/decyzji i wpływ na inne komponenty architektury.

### Implementation Notes
Kluczowe uwagi implementacyjne, wzorce do zastosowania, best practices.

### Decision Makers
Lista osób zaangażowanych w podjęcie decyzji z przypisanymi rolami.

### Date & Version
Data podjęcia decyzji, wersja dokumentu, historia zmian.

### References
Linki do powiązanych dokumentów (TDD, PRD, RFC), artykułów technicznych, benchmarków.

## Czego nie zawiera
- Pełnych kodów źródłowych
- Szczegółowych implementacji
- Raportów finansowych

## Objętość
- Dokumenty ciągłe (2–4 strony na decyzję)

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Architekci systemów
- Developerzy
- Project managerowie
