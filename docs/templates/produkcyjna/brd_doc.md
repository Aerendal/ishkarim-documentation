# 📄 Basic Requirements Document (BRD)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter provides foundational project scope and objectives for BRD"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
      - when: "project.type === 'informal' || 'spike'"
        applies: false
    sections:
      - from: "Project Charter §12 Project Objectives"
        to: "§2 Business Objectives"
        influence: "Project objectives define business objectives in BRD"
      - from: "Project Charter §13 Project Scope"
        to: "§4 Scope & Boundaries"
        influence: "Project scope defines BRD boundaries"

  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case provides business justification and problem definition"
    conditions:
      - when: "project.requires_business_justification === true"
        applies: true
    sections:
      - from: "Business Case §5 Problem Statement"
        to: "§3 Problem Statement"
        influence: "Business problem definition drives BRD problem statement"
      - from: "Business Case §15 Success Metrics"
        to: "§8 Success Criteria & KPIs"
        influence: "Business metrics define BRD success criteria"

  - id: VISION-*
    type: influences
    reason: "Vision Document provides strategic context for requirements"
    conditions:
      - when: "project.has_strategic_vision === true"
        applies: true
    sections:
      - from: "Vision §13 Strategic Business Goals"
        to: "§2 Business Objectives"
        influence: "Strategic goals inform business objectives"

  - id: FEASIBILITY-STUDY-*
    type: influences
    reason: "Feasibility Study validates that requirements are achievable"
    conditions:
      - when: "feasibility_study.exists === true"
        applies: true
    sections:
      - from: "Feasibility Study §4 Technical Feasibility"
        to: "§9 Assumptions & Constraints"
        influence: "Feasibility findings define technical constraints"
```

### Impacts
```yaml
impacts:
  - id: PRD-*
    type: blocks
    reason: "PRD expands BRD requirements into detailed product specifications"
    conditions:
      - when: "project.requires_detailed_specs === true"
        applies: true
      - when: "project.type === 'simple' && brd.sufficient === true"
        applies: false
    sections:
      - from: "§5 Core Functional Requirements"
        to: "PRD §5 Functional Requirements"
        influence: "Core requirements become detailed functional requirements in PRD"
      - from: "§6 Core Non-Functional Requirements"
        to: "PRD §6 Non-Functional Requirements"
        influence: "Core NFRs expand into detailed NFR specifications"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "BRD requirements inform initial architecture decisions"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§6 Core Non-Functional Requirements"
        to: "High-Level Architecture §2 Architecture Overview"
        influence: "NFRs (scalability, performance) drive architecture choices"

  - id: TEST-PLAN-*
    type: influences
    reason: "BRD requirements define what needs testing"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§5 Core Functional Requirements"
        to: "Test Plan §3 Test Scenarios"
        influence: "Functional requirements define test scenarios"
      - from: "§8 Success Criteria & KPIs"
        to: "Test Plan §5 Acceptance Criteria"
        influence: "Success criteria define acceptance testing criteria"

  - id: TIMELINE-*
    type: influences
    reason: "BRD timeline provides foundation for detailed project timeline"
    conditions:
      - when: "project.requires_detailed_timeline === true"
        applies: true
    sections:
      - from: "§10 High-Level Timeline"
        to: "Timeline §2 Project Milestones"
        influence: "High-level timeline defines major project milestones"
```

### Related
```yaml
related:
  - id: RESOURCE-REQUIREMENTS-*
    type: informs
    reason: "BRD requirements inform resource planning"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "BRD identifies initial risks that need assessment"

  - id: RTM-*
    type: informs
    reason: "Requirements Traceability Matrix tracks BRD requirements through implementation"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-BRD-*.md"
    required: false
    purpose: "Track requirements clarification and stakeholder approval tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-BRD-*.md"
    required: false
    purpose: "Store stakeholder interviews, requirements workshops, market research"

  - type: DoR
    path: "satellites/dor/DOR-BRD-*.md"
    required: true
    purpose: "Define prerequisites: stakeholder interviews complete, problem validated, scope agreed"

  - type: DoD
    path: "satellites/dod/DOD-BRD-*.md"
    required: true
    purpose: "Define completion criteria: requirements reviewed, stakeholders approved, feasibility confirmed"
```

## Cel biznesowy / techniczny
BRD określa minimalny zestaw wymagań niezbędnych do rozpoczęcia prac produkcyjnych. Służy jako dokument bazowy, który zapewnia wspólne zrozumienie podstawowych potrzeb projektu.

## Zawartość

### Executive Summary
Wysokopoziomowe streszczenie projektu i jego celów biznesowych.

### Business Objectives
Kluczowe cele biznesowe, które projekt ma osiągnąć (zwiększenie przychodów, redukcja kosztów, poprawa UX).

### Problem Statement
Jaki problem biznesowy rozwiązujemy i dlaczego teraz?

### Scope & Boundaries
Co jest w zakresie projektu, a co NIE jest (boundary definition).

### Core Functional Requirements
Minimalne wymagania funkcjonalne niezbędne do uruchomienia produktu (MVP approach).

### Core Non-Functional Requirements
Minimalne wymagania niefunkcjonalne (performance, security, compliance).

### Key Stakeholders
Lista kluczowych interesariuszy i ich oczekiwań.

### Success Criteria & KPIs
Kryteria sukcesu i metryki biznesowe do pomiaru rezultatów.

### Assumptions & Constraints
Założenia projektowe i ograniczenia (budżet, czas, zasoby, technologia).

### High-Level Timeline
Wysokopoziomowy harmonogram z kluczowymi milestone'ami.

### Dependencies
Zależności od innych projektów, systemów lub zespołów.

### Risks
Kluczowe ryzyka biznesowe i techniczne (bez szczegółowej mitygacji).

### Approval Requirements
Kto musi zaaprobować dokument przed rozpoczęciem prac.

## Czego nie zawiera
- Nadmiarowych szczegółów technicznych
- Szczegółowych planów sprintowych
- Kodów źródłowych

## Objętość
- 8–12 stron
- 15–20 punktów kluczowych

## Kategoria
- **Wymagane** (produkcyjne)

## Odbiorcy
- Zespół developerski
- Product owner
- Project manager
