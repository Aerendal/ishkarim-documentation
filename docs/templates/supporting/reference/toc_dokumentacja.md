# 📑 Spis treści (TOC) dokumentacji projektowej

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Hierarchiczna lista wszystkich typów dokumentów projektowych: przedprodukcyjnych, produkcyjnych i branżowych.

---

## 1. Dokumentacja przedprodukcyjna
- Executive Summary
- Business Case
- Pitch Deck (Inwestorski)
- Market Analysis
- Financial Plan / Projections
- Feasibility Study (Studium wykonalności)
- Stakeholder Map
- Go-To-Market Strategy
- Risk Overview (Inwestycyjny)
- Research Plan
- Project Charter
- Project Management Plan
- Communication Plan
- Procurement Plan
- Training Plan
- Cost-Benefit Analysis (CBA)
- Vision Document (Extended)
- Impact Assessment
- Innovation Roadmap
- Ethics & AI Guidelines
- Sustainability Report
- Data Privacy Impact Assessment (DPIA)
- Legal & Regulatory Register
- Innovation Log

---

## 2. Dokumentacja produkcyjna
- Product Requirements Document (PRD)
- Basic Requirements Document (BRD)
- High-Level Architecture
- Technical Design Document (TDD)
- Test Plan / QA Strategy
- Timeline & Milestones
- Risk Overview (Techniczny)
- Resource Requirements
- Operational Manual
- System Context Diagram
- Data Management Plan
- Security Plan
- Change Management Plan
- Configuration Management Plan
- Quality Assurance Plan
- Compliance Report
- Test Summary Report
- Requirements Traceability Matrix (RTM)
- Architecture Decision Records (ADR)
- Operations Runbook
- Incident Report
- Release Management Plan
- Migration Plan
- Integration Plan
- Monitoring & Observability Plan
- Performance Test Report
- API Documentation
- Data Governance Policy
- Vendor Management Plan
- Operational Risk Assessment
- Security Incident Response Plan (SIRP)
- Knowledge Base / Wiki
- Change Log / Release Notes
- Training Materials
- Maintenance & Support Guide
- Deployment Guide
- User Acceptance Test (UAT) Plan
- Postmortem / Retrospective Report
- Service Level Agreement (SLA)
- Disaster Recovery Plan (DRP)
- Knowledge Transfer Plan
- Closure Report
- Service Catalog
- User Guide
- Administrator Guide
- Onboarding Guide
- Accessibility Compliance Report

---

## 3. Dokumentacja branżowa

### Medycyna / Healthcare
- HIPAA Compliance Report
- Clinical Trial Documentation
- Medical Device File (MDR)

### Finanse / Banking
- PCI DSS Compliance Report
- SOX Compliance Report
- Basel III Risk Report

### Administracja publiczna
- GDPR Compliance Report
- eIDAS Compliance Documentation
- Public Sector Transparency Report

### Militaria / obronność
- Security Clearance Documentation
- NATO STANAG Compliance
- Cyber Defense Readiness Report

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: ALL-DOC-TYPES-*
    type: requires
    reason: "TOC requires complete list of all document types to provide navigation"
    conditions:
      - when: "project.has_documentation === true"
        applies: true
    sections:
      - from: "Document Type Catalog §All types"
        to: "§1-3 All TOC entries"
        influence: "Document catalog defines TOC structure and entries"

  - id: DOKUMENTACJA-TABELA-*
    type: requires
    reason: "TOC organization mirrors table categorization"
    sections:
      - from: "Dokumentacja Tabela §A-H Categories"
        to: "§1-3 Section structure"
        influence: "Table categories define TOC section groupings"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: NAVIGATION-*
    type: informs
    reason: "TOC provides primary navigation structure for documentation"
    conditions:
      - when: "project.has_multiple_docs === true"
        applies: true
    sections:
      - from: "§1-3 Hierarchical list"
        to: "Documentation Portal §1 Navigation menu"
        influence: "TOC structure defines navigation hierarchy"

  - id: PROJECT-PLANNING-*
    type: informs
    reason: "TOC helps teams understand full documentation scope"
    sections:
      - from: "§1 Dokumentacja przedprodukcyjna"
        to: "Project Plan §1 Pre-production deliverables"
        influence: "TOC pre-production section lists required early-stage docs"
      - from: "§2 Dokumentacja produkcyjna"
        to: "Project Plan §2 Production deliverables"
        influence: "TOC production section defines implementation-phase docs"

  - id: CHECKLIST-*
    type: informs
    reason: "TOC generates document completion checklists"
    sections:
      - from: "§1-3 All entries"
        to: "Checklist §1 Document status"
        influence: "Each TOC entry becomes a checklist item to track completion"
```

### Related Documents

```yaml
related:
  - id: DOKUMENTACJA-TABELA-*
    type: informs
    reason: "Comparison table provides detailed attributes for TOC entries"

  - id: DIAGRAM-ZALEZNOSCI-*
    type: informs
    reason: "Dependency diagram shows relationships between TOC entries"

  - id: TEMPLATES-README-*
    type: informs
    reason: "Template README provides usage guidance for TOC documents"
```

### Satellite Documents

```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TOC-*.md"
    required: false
    purpose: "Track TOC updates as new document types are added"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TOC-*.md"
    required: false
    purpose: "Examples of TOC usage in real projects"
```
