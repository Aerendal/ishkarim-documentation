# 📄 Product Requirements Document (PRD)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: BRD-*
    type: requires
    reason: "BRD provides baseline requirements that PRD expands into detailed specifications"
    conditions:
      - when: "project.has_brd === true"
        applies: true
      - when: "project.starts_with_prd === true"
        applies: false
    sections:
      - from: "BRD §5 Core Functional Requirements"
        to: "§5 Functional Requirements"
        influence: "BRD core requirements expand into detailed PRD functional requirements"
      - from: "BRD §6 Core Non-Functional Requirements"
        to: "§6 Non-Functional Requirements"
        influence: "BRD NFRs expand into detailed PRD NFR specifications"

  - id: VISION-*
    type: influences
    reason: "Vision Document provides strategic context and product vision"
    conditions:
      - when: "project.has_vision_doc === true"
        applies: true
    sections:
      - from: "Vision §13 Strategic Business Goals"
        to: "§3 Product Vision & Objectives"
        influence: "Strategic goals inform product vision and objectives"

  - id: BIZ-CASE-*
    type: influences
    reason: "Business Case provides business justification and problem definition"
    conditions:
      - when: "project.has_business_case === true"
        applies: true
    sections:
      - from: "Business Case §5 Problem Statement"
        to: "§2 Problem Statement"
        influence: "Business problem drives product requirements"
      - from: "Business Case §15 Success Metrics"
        to: "§11 Success Metrics"
        influence: "Business metrics become product success metrics"

  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter defines scope, objectives, and constraints"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
    sections:
      - from: "Project Charter §13 Project Scope"
        to: "§15 Out of Scope"
        influence: "Project scope defines what is explicitly excluded from PRD"
      - from: "Project Charter §14 Budget Allocation"
        to: "§8 Technical Constraints"
        influence: "Budget constraints affect technical requirements feasibility"
```

### Impacts
```yaml
impacts:
  - id: TDD-*
    type: blocks
    reason: "TDD cannot be created without detailed requirements from PRD"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§5 Functional Requirements"
        to: "TDD §2 Functional Design"
        influence: "Functional requirements define what technical design must deliver"
      - from: "§6 Non-Functional Requirements"
        to: "TDD §3 System Architecture"
        influence: "NFRs (performance, scalability, security) drive architecture decisions"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "PRD requirements inform architecture decisions"
    conditions:
      - when: "project.requires_architecture === true"
        applies: true
    sections:
      - from: "§6 Non-Functional Requirements"
        to: "High-Level Architecture §2 Architecture Overview"
        influence: "NFRs drive architectural patterns and component selection"

  - id: TEST-PLAN-*
    type: blocks
    reason: "Test Plan requires PRD requirements as test basis"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§5 Functional Requirements"
        to: "Test Plan §3 Test Scenarios"
        influence: "Functional requirements define what must be tested"
      - from: "§7 Use Cases & User Flows"
        to: "Test Plan §3 Test Scenarios"
        influence: "Use cases become test scenarios"

  - id: UAT-PLAN-*
    type: influences
    reason: "UAT validates PRD requirements with users"
    conditions:
      - when: "project.has_uat === true"
        applies: true
    sections:
      - from: "§4 User Stories & Personas"
        to: "UAT Plan §3 UAT Scenarios"
        influence: "User stories become UAT acceptance scenarios"
      - from: "§11 Success Metrics"
        to: "UAT Plan §5 Acceptance Criteria"
        influence: "Success metrics define UAT acceptance criteria"

  - id: USER-GUIDE-*
    type: influences
    reason: "User Guide documents features defined in PRD"
    conditions:
      - when: "project.has_end_users === true"
        applies: true
    sections:
      - from: "§5 Functional Requirements"
        to: "User Guide §3 Feature Documentation"
        influence: "Functional requirements define features to document"
      - from: "§4 User Stories & Personas"
        to: "User Guide §2 User Personas"
        influence: "User personas inform user guide audience and tone"

  - id: RTM-*
    type: blocks
    reason: "Requirements Traceability Matrix tracks PRD requirements through implementation"
    conditions:
      - when: "project.requires_traceability === true"
        applies: true
    sections:
      - from: "§5 Functional Requirements"
        to: "RTM §2 Requirements Traceability"
        influence: "PRD requirements become traceability matrix entries"

  - id: COMPLIANCE-REPORT-*
    type: influences
    reason: "PRD compliance requirements need verification"
    conditions:
      - when: "prd.has_compliance_requirements === true"
        applies: true
    sections:
      - from: "§6 Non-Functional Requirements (Compliance)"
        to: "Compliance Report §2 Compliance Status"
        influence: "Compliance requirements define what needs compliance verification"
```

### Related
```yaml
related:
  - id: RESOURCE-REQUIREMENTS-*
    type: informs
    reason: "PRD requirements inform resource planning"

  - id: TIMELINE-*
    type: informs
    reason: "PRD milestones inform detailed project timeline"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "PRD identifies risks requiring assessment"

  - id: API-DOCUMENTATION-*
    type: informs
    reason: "PRD functional requirements may define API needs"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-PRD-*.md"
    required: false
    purpose: "Track requirements clarification and stakeholder approval tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-PRD-*.md"
    required: true
    purpose: "Store user research, requirements workshops, stakeholder approvals, prototypes"

  - type: DoR
    path: "satellites/dor/DOR-PRD-*.md"
    required: true
    purpose: "Define prerequisites: user research complete, stakeholders identified, problem validated"

  - type: DoD
    path: "satellites/dod/DOD-PRD-*.md"
    required: true
    purpose: "Define completion criteria: all requirements documented, acceptance criteria defined, stakeholders approved"
```

## Cel biznesowy / techniczny
PRD definiuje pełny zestaw wymagań produktowych, zarówno funkcjonalnych, jak i niefunkcjonalnych. Jest podstawowym punktem odniesienia dla zespołów developerskich, testerów i menedżerów produktu.

## Zawartość

### Executive Summary
Zwięzłe streszczenie kontekstu, celów biznesowych, kluczowych decyzji produktowych i oczekiwanych rezultatów.

### Problem Statement
Jaki konkretny problem rozwiązujemy? Opis pain points użytkowników, skali problemu i wpływu na biznes.

### Product Vision & Objectives
Wizja produktu, cele strategiczne i metryki sukcesu (OKRs, KPIs).

### User Stories & Personas
Kto korzysta z produktu i dlaczego? Szczegółowe user stories w formacie "Jako [persona], chcę [akcja], aby [cel]" wraz z opisem kluczowych person.

### Functional Requirements (FR)
Szczegółowe wymagania funkcjonalne z priorytetami (MoSCoW) i acceptance criteria dla każdego wymagania.

### Non-Functional Requirements (NFR)
- Performance (czas odpowiedzi, przepustowość, skalowanie)
- Security (uwierzytelnianie, autoryzacja, szyfrowanie)
- Scalability (limity użytkowników, wzrost danych)
- Reliability & Availability (uptime, fault tolerance)
- Usability (dostępność, UX, responsywność)
- Maintainability (architektura, dokumentacja kodu)
- Compliance (RODO, ISO, regulacje branżowe)

### Use Cases & User Flows
Scenariusze użycia z diagramami przepływów, happy paths i edge cases.

### Technical Constraints
Ograniczenia techniczne (istniejące systemy, legacy code, infrastruktura, budżet techniczny).

### Dependencies
Lista zależności od innych projektów, systemów zewnętrznych, zespołów lub zasobów.

### Impacts & Stakeholder Analysis
Kogo ten dokument wpływa? Analiza interesariuszy i potencjalnego wpływu na inne systemy/zespoły.

### Success Metrics
Jak mierzymy sukces? Metryki biznesowe i techniczne (user adoption, performance, revenue impact).

### Risks & Mitigations
Zidentyfikowane zagrożenia dla projektu z oceną prawdopodobieństwa, wpływu i planami mitygacji.

### Timeline & Milestones
Kluczowe kamienie milowe, fazy projektu i szacowany harmonogram (high-level roadmap).

### Out of Scope
Co explicite NIE jest częścią tego dokumentu/projektu (zarządzanie oczekiwaniami).

### Approval & Sign-off
Kto musi zaaprobować dokument? Lista decydentów, daty przeglądów i status zatwierdzenia.

## Czego nie zawiera
- Luźnych pomysłów i niezweryfikowanych koncepcji
- Kodów źródłowych
- Szczegółowych planów sprintowych

## Objętość
- 15–25 stron
- 30–50 punktów kluczowych

## Kategoria
- **Wymagane** (produkcyjne)

## Odbiorcy
- Zespół developerski
- QA / testerzy
- Product owner / project manager
