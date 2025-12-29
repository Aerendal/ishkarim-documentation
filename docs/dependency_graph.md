# Graf Zależności Dokumentów

Analiza zależności między dokumentami na podstawie sekcji Cross-References.

**158 dokumentów | 1367 połączeń | 8 grafów wizualizacyjnych**

## Spis treści grafów

- **Graf A**: Przedprodukcyjna - workflow dokumentów przedprodukcyjnych
- **Graf B**: Produkcyjna - workflow dokumentów produkcyjnych
- **Graf C**: Pełny Graf - top 30 najważniejszych dokumentów z połączeniami
- **Graf D**: Architecture Transformation Workflow - transformacja architektury
- **Graf E**: Sprint Types Workflow - różne typy sprintów
- **Graf F**: Sprint Workflow (Szczegółowy) - pełny cycle dokumentacji sprintowej ⭐ NOWY
- **Graf G**: Roadmap & Planning Workflow - strategiczne planowanie ⭐ NOWY
- **Graf H**: Atomic Satellites Network - satelitarne dokumenty atomowe ⭐ NOWY

## Graf A: Przedprodukcyjna

Workflow dokumentów przedprodukcyjnych (przed realizacją projektu).

```mermaid
graph TB
    VISION["Vision Document Extended"]
    BIZ_CASE["Business Case"]
    EXEC_SUM["Executive Summary"]
    CHARTER["Project Charter"]
    FEASIBILITY["Feasibility Study Studium wykonalności"]
    STAKEHOLDERS["Stakeholder Map"]
    MARKET["Market Analysis"]
    RISK_INV["Risk Overview Inwestycyjny"]
    CBA["Cost-Benefit Analysis CBA"]
    FINANCE["Financial Plan / Projections"]
    GTM["Go-To-Market Strategy"]
    PM_PLAN["Project Management Plan"]
    COMMUNICATION_PLAN["Communication Plan"]
    PROCUREMENT_PLAN["Procurement Plan"]
    DPIA["Data Privacy Impact Assessment DPIA"]

    VISION -->|blocks| BIZ_CASE
    VISION -->|blocks| EXEC_SUM
    VISION -->|blocks| CHARTER
    VISION -->|requires| BIZ_CASE
    MARKET -->|requires| BIZ_CASE
    FINANCE -->|requires| BIZ_CASE
    BIZ_CASE -->|blocks| EXEC_SUM
    BIZ_CASE -->|blocks| CHARTER
    BIZ_CASE -->|blocks| FEASIBILITY
    VISION -->|requires| EXEC_SUM
    BIZ_CASE -->|requires| EXEC_SUM
    MARKET -->|requires| EXEC_SUM
    EXEC_SUM -->|informs| CHARTER
    VISION -->|requires| CHARTER
    BIZ_CASE -->|requires| CHARTER
    EXEC_SUM -->|requires| CHARTER
    CHARTER -->|blocks| PM_PLAN
    CHARTER -->|blocks| STAKEHOLDERS
    BIZ_CASE -->|requires| FEASIBILITY
    MARKET -->|requires| FEASIBILITY
    FINANCE -->|requires| FEASIBILITY
    FEASIBILITY -->|blocks| CHARTER
    FEASIBILITY -->|informs| RISK_INV
    CHARTER -->|requires| STAKEHOLDERS
    VISION -->|influences| STAKEHOLDERS
    STAKEHOLDERS -->|blocks| COMMUNICATION_PLAN
    STAKEHOLDERS -->|blocks| PM_PLAN
    VISION -->|influences| MARKET
    MARKET -->|blocks| BIZ_CASE
    MARKET -->|blocks| FINANCE
    MARKET -->|blocks| GTM
    MARKET -->|informs| EXEC_SUM
    MARKET -->|influences| CBA
    BIZ_CASE -->|influences| RISK_INV
    MARKET -->|influences| RISK_INV
    DPIA -->|influences| RISK_INV
    CBA -->|influences| RISK_INV
    PROCUREMENT_PLAN -->|influences| RISK_INV
    RISK_INV -->|blocks| PM_PLAN
    RISK_INV -->|informs| EXEC_SUM
    BIZ_CASE -->|requires| CBA
    FINANCE -->|requires| CBA
    CBA -->|informs| EXEC_SUM
    CBA -->|influences| FINANCE
    BIZ_CASE -->|requires| FINANCE
    MARKET -->|requires| FINANCE
    CHARTER -->|influences| FINANCE
    FINANCE -->|blocks| CBA
    FINANCE -->|informs| EXEC_SUM
    FINANCE -->|influences| PROCUREMENT_PLAN
    MARKET -->|requires| GTM
    VISION -->|requires| GTM
    BIZ_CASE -->|influences| GTM
    FINANCE -->|influences| GTM
    GTM -->|informs| EXEC_SUM
    GTM -->|influences| COMMUNICATION_PLAN
    CHARTER -->|requires| PM_PLAN
    STAKEHOLDERS -->|requires| PM_PLAN
    FINANCE -->|influences| PM_PLAN
    COMMUNICATION_PLAN -->|influences| PM_PLAN
    PM_PLAN -->|influences| PROCUREMENT_PLAN
    CHARTER -->|requires| COMMUNICATION_PLAN
    STAKEHOLDERS -->|requires| COMMUNICATION_PLAN
    PM_PLAN -->|influences| COMMUNICATION_PLAN
    COMMUNICATION_PLAN -->|informs| PM_PLAN
    COMMUNICATION_PLAN -->|influences| STAKEHOLDERS
    CHARTER -->|requires| PROCUREMENT_PLAN
    FINANCE -->|requires| PROCUREMENT_PLAN
    FEASIBILITY -->|influences| PROCUREMENT_PLAN
    PROCUREMENT_PLAN -->|informs| PM_PLAN
    VISION -->|influences| DPIA
    FEASIBILITY -->|influences| DPIA

    classDef przedprodukcyjna fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    class VISION,BIZ_CASE,EXEC_SUM,CHARTER,FEASIBILITY,STAKEHOLDERS,MARKET,RISK_INV,CBA,FINANCE,GTM,PM_PLAN,COMMUNICATION_PLAN,PROCUREMENT_PLAN,DPIA przedprodukcyjna
```

## Graf B: Produkcyjna

Workflow dokumentów produkcyjnych (podczas realizacji projektu).

```mermaid
graph TB
    BRD["Basic Requirements Document BRD"]
    PRD["Product Requirements Document PRD"]
    TDD["Technical Design Document TDD"]
    HLA["High-Level Architecture"]
    TEST["Test Plan / QA Strategy"]
    UAT["User Acceptance Test UAT Plan"]
    QA["Quality Assurance Plan"]
    RTM["Requirements Traceability Matrix RTM"]
    DEPLOY["Deployment Guide"]
    SECURITY["Security Plan"]
    MONITOR["Monitoring & Observability Plan"]
    USER_DOC["User Guide"]
    ADMIN_DOC["Administrator Guide"]
    OPS_MANUAL["Operational Manual"]
    RUNBOOK["Operations Runbook"]
    MAINT["Maintenance & Support Guide"]
    CHANGE_MANAGEMENT_PLAN["Change Management Plan"]
    RELEASE_MANAGEMENT_PLAN["Release Management Plan"]
    API_DOC["API Documentation"]

    BRD -->|blocks| PRD
    BRD -->|influences| HLA
    BRD -->|influences| TEST
    BRD -->|requires| PRD
    PRD -->|blocks| TDD
    PRD -->|influences| HLA
    PRD -->|blocks| TEST
    PRD -->|influences| UAT
    PRD -->|influences| USER_DOC
    PRD -->|blocks| RTM
    HLA -->|requires| TDD
    PRD -->|requires| TDD
    SECURITY -->|requires| TDD
    TDD -->|blocks| API_DOC
    TDD -->|influences| DEPLOY
    TDD -->|influences| TEST
    TDD -->|informs| ADMIN_DOC
    PRD -->|requires| HLA
    HLA -->|blocks| TDD
    HLA -->|influences| DEPLOY
    HLA -->|influences| SECURITY
    PRD -->|requires| TEST
    TEST -->|influences| UAT
    TEST -->|influences| QA
    PRD -->|requires| UAT
    TEST -->|requires| UAT
    USER_DOC -->|influences| UAT
    PRD -->|requires| QA
    QA -->|blocks| TEST
    QA -->|influences| UAT
    PRD -->|requires| RTM
    BRD -->|influences| RTM
    TEST -->|requires| RTM
    TDD -->|requires| DEPLOY
    HLA -->|requires| DEPLOY
    SECURITY -->|requires| DEPLOY
    DEPLOY -->|influences| ADMIN_DOC
    DEPLOY -->|influences| RUNBOOK
    PRD -->|requires| SECURITY
    HLA -->|requires| SECURITY
    SECURITY -->|influences| TDD
    SECURITY -->|influences| DEPLOY
    SECURITY -->|influences| ADMIN_DOC
    TDD -->|requires| MONITOR
    HLA -->|requires| MONITOR
    PRD -->|influences| MONITOR
    MONITOR -->|influences| RUNBOOK
    MONITOR -->|influences| OPS_MANUAL
    PRD -->|requires| USER_DOC
    API_DOC -->|influences| USER_DOC
    USER_DOC -->|informs| UAT
    TDD -->|requires| ADMIN_DOC
    DEPLOY -->|requires| ADMIN_DOC
    SECURITY -->|requires| ADMIN_DOC
    RUNBOOK -->|requires| ADMIN_DOC
    ADMIN_DOC -->|informs| OPS_MANUAL
    ADMIN_DOC -->|influences| MAINT
    DEPLOY -->|requires| OPS_MANUAL
    ADMIN_DOC -->|requires| OPS_MANUAL
    RUNBOOK -->|requires| OPS_MANUAL
    MONITOR -->|requires| OPS_MANUAL
    DEPLOY -->|requires| RUNBOOK
    ADMIN_DOC -->|requires| RUNBOOK
    MONITOR -->|requires| RUNBOOK
    RUNBOOK -->|informs| OPS_MANUAL
    ADMIN_DOC -->|requires| MAINT
    DEPLOY -->|influences| MAINT
    BRD -->|requires| CHANGE_MANAGEMENT_PLAN
    DEPLOY -->|requires| RELEASE_MANAGEMENT_PLAN
    TDD -->|requires| API_DOC
    PRD -->|influences| API_DOC
    SECURITY -->|requires| API_DOC
    HLA -->|influences| API_DOC
    API_DOC -->|informs| USER_DOC
    API_DOC -->|influences| TEST

    classDef produkcyjna fill:#fff3e0,stroke:#e65100,stroke-width:2px
    class BRD,PRD,TDD,HLA,TEST,UAT,QA,RTM,DEPLOY,SECURITY,MONITOR,USER_DOC,ADMIN_DOC,OPS_MANUAL,RUNBOOK,MAINT,CHANGE_MANAGEMENT_PLAN,RELEASE_MANAGEMENT_PLAN,API_DOC produkcyjna
```

## Graf C: Pełny Graf Kluczowych Zależności

Top 30 najważniejszych dokumentów z połączeniami między fazami.

```mermaid
graph TB
    subgraph Przedprodukcyjna
        RISK_INV["Risk Overview Inwestycyjny"]
        IMPACT_ASSESSMENT["Impact Assessment"]
        MARKET["Market Analysis"]
        FINANCE["Financial Plan / Projections"]
        GTM["Go-To-Market Strategy"]
        LEGAL_REGISTER["Legal & Regulatory Register"]
        ROADMAP["Innovation Roadmap"]
    end

    subgraph Produkcyjna
        RISK_TECH["Risk Overview Techniczny"]
        PRD["Product Requirements Document PRD"]
        TIMELINE["Timeline & Milestones"]
        TRAINING_MATERIALS["Training Materials"]
        SIRP["Security Incident Response Plan ..."]
        TDD["Technical Design Document TDD"]
        RESOURCE_REQUIREMENTS["Resource Requirements"]
        VENDOR_MANAGEMENT_PLAN["Vendor Management Plan"]
        SECURITY["Security Plan"]
        TEST["Test Plan / QA Strategy"]
        OPS_MANUAL["Operational Manual"]
        ADR["Architecture Decision Records ADR"]
        API_DOC["API Documentation"]
        RUNBOOK["Operations Runbook"]
        SYSTEM_CONTEXT_DIAGRAM["System Context Diagram"]
        HLA["High-Level Architecture"]
        BCP["Business Continuity Plan BCP"]
        BRD["Basic Requirements Document BRD"]
        MONITOR["Monitoring & Observability Plan"]
    end

    subgraph Branżowa
        MEDICAL_DEVICE_FILE["Medical Device File MDR"]
        NATO_STANAG["NATO STANAG Compliance"]
        CLINICAL_TRIAL["Clinical Trial Documentation"]
        PCI_DSS["PCI DSS Compliance Report"]
    end

    HLA -->|requires| RISK_TECH
    TDD -->|influences| RISK_TECH
    PRD -->|influences| RISK_TECH
    RISK_TECH -->|influences| SECURITY
    RISK_TECH -->|influences| BCP
    RISK_TECH -->|influences| MONITOR
    RISK_TECH -->|influences| TEST
    RISK_TECH -->|informs| TIMELINE
    BRD -->|requires| PRD
    PRD -->|blocks| TDD
    PRD -->|influences| HLA
    PRD -->|blocks| TEST
    BRD -->|influences| TIMELINE
    RESOURCE_REQUIREMENTS -->|requires| TIMELINE
    TIMELINE -->|influences| TEST
    TIMELINE -->|informs| TRAINING_MATERIALS
    MARKET -->|influences| RISK_INV
    IMPACT_ASSESSMENT -->|influences| RISK_INV
    LEGAL_REGISTER -->|influences| RISK_INV
    OPS_MANUAL -->|requires| TRAINING_MATERIALS
    RUNBOOK -->|influences| TRAINING_MATERIALS
    SECURITY -->|influences| TRAINING_MATERIALS
    SECURITY -->|requires| SIRP
    MONITOR -->|requires| SIRP
    SIRP -->|influences| RUNBOOK
    SIRP -->|informs| TRAINING_MATERIALS
    SIRP -->|informs| BCP
    LEGAL_REGISTER -->|requires| IMPACT_ASSESSMENT
    IMPACT_ASSESSMENT -->|informs| RISK_TECH
    MARKET -->|blocks| FINANCE
    MARKET -->|blocks| GTM
    MARKET -->|informs| ROADMAP
    MARKET -->|influences| LEGAL_REGISTER
    HLA -->|requires| TDD
    PRD -->|requires| TDD
    ADR -->|requires| TDD
    SECURITY -->|requires| TDD
    TDD -->|blocks| API_DOC
    TDD -->|influences| TEST
    BRD -->|requires| RESOURCE_REQUIREMENTS
    HLA -->|influences| RESOURCE_REQUIREMENTS
    TDD -->|influences| RESOURCE_REQUIREMENTS
    RESOURCE_REQUIREMENTS -->|blocks| TIMELINE
    RESOURCE_REQUIREMENTS -->|influences| VENDOR_MANAGEMENT_PLAN
    RESOURCE_REQUIREMENTS -->|informs| TRAINING_MATERIALS
    RESOURCE_REQUIREMENTS -->|requires| VENDOR_MANAGEMENT_PLAN
    SECURITY -->|requires| VENDOR_MANAGEMENT_PLAN
    VENDOR_MANAGEMENT_PLAN -->|influences| RISK_TECH
    PRD -->|requires| SECURITY
    HLA -->|requires| SECURITY
    SECURITY -->|influences| TDD
    TEST -->|requires| NATO_STANAG
    MONITOR -->|requires| CLINICAL_TRIAL
    CLINICAL_TRIAL -->|informs| MEDICAL_DEVICE_FILE
    MARKET -->|requires| FINANCE
    ROADMAP -->|influences| FINANCE
    MARKET -->|requires| GTM
    FINANCE -->|influences| GTM
    GTM -->|influences| ROADMAP
    LEGAL_REGISTER -->|blocks| IMPACT_ASSESSMENT
    LEGAL_REGISTER -->|informs| RISK_TECH
    MARKET -->|requires| ROADMAP
    PRD -->|requires| TEST
    BRD -->|influences| TEST
    RUNBOOK -->|requires| OPS_MANUAL
    MONITOR -->|requires| OPS_MANUAL
    BCP -->|influences| OPS_MANUAL
    OPS_MANUAL -->|influences| TRAINING_MATERIALS
    HLA -->|requires| ADR
    TDD -->|influences| ADR
    PRD -->|influences| ADR
    ADR -->|blocks| TDD
    ADR -->|influences| HLA
    TDD -->|requires| API_DOC
    PRD -->|influences| API_DOC
    SECURITY -->|requires| API_DOC
    HLA -->|influences| API_DOC
    API_DOC -->|influences| TEST
    MONITOR -->|requires| RUNBOOK
    BCP -->|influences| RUNBOOK
    RUNBOOK -->|informs| OPS_MANUAL
    BRD -->|requires| SYSTEM_CONTEXT_DIAGRAM
    PRD -->|influences| SYSTEM_CONTEXT_DIAGRAM
    HLA -->|influences| SYSTEM_CONTEXT_DIAGRAM
    SYSTEM_CONTEXT_DIAGRAM -->|blocks| HLA
    SYSTEM_CONTEXT_DIAGRAM -->|informs| TDD
    SYSTEM_CONTEXT_DIAGRAM -->|informs| API_DOC
    PRD -->|requires| HLA
    BRD -->|influences| HLA
    HLA -->|blocks| TDD
    HLA -->|influences| SECURITY
    HLA -->|informs| ADR
    BCP -->|influences| TRAINING_MATERIALS
    BCP -->|informs| OPS_MANUAL
    BRD -->|blocks| PRD
    TDD -->|requires| MONITOR
    HLA -->|requires| MONITOR
    PRD -->|influences| MONITOR
    MONITOR -->|influences| RUNBOOK
    MONITOR -->|influences| OPS_MANUAL

    classDef przedprodukcyjna fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef produkcyjna fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef branzowa fill:#f3e5f5,stroke:#4a148c,stroke-width:2px

    class RISK_INV,IMPACT_ASSESSMENT,MARKET,FINANCE,GTM,LEGAL_REGISTER,ROADMAP przedprodukcyjna
    class RISK_TECH,PRD,TIMELINE,TRAINING_MATERIALS,SIRP,TDD,RESOURCE_REQUIREMENTS,VENDOR_MANAGEMENT_PLAN,SECURITY,TEST,OPS_MANUAL,ADR,API_DOC,RUNBOOK,SYSTEM_CONTEXT_DIAGRAM,HLA,BCP,BRD,MONITOR produkcyjna
    class MEDICAL_DEVICE_FILE,NATO_STANAG,CLINICAL_TRIAL,PCI_DSS branzowa
```

## Statystyki

- Total dokumentów: 158 (132 + 26 nowych)
- Total dependencies: 471 (+95)
- Total impacts: 509 (+104)
- Total related: 387 (+72)
- Total połączeń: 1367 (+271)
- Dokumenty bez dependencies: 18
- Dokumenty bez impacts: 18

### Najczęściej wymagane dokumenty (top 15):
  - **ROADMAP-PROD** (Product Roadmap): 28 razy (nowy lider!)
  - **SPRINT-PLAN** (Sprint Plan): 25 razy (nowy!)
  - **PRD** (Product Requirements Document PRD): 23 razy
  - **PROJECT-CHARTER** (Project Charter): 20 razy
  - **SPRINT-DOD** (Sprint Definition of Done): 18 razy (nowy!)
  - **RELEASE-CHECKLIST** (Release Checklist): 17 razy (nowy!)
  - **VISION-DOCUMENT** (Vision Document Extended): 16 razy
  - **TDD** (Technical Design Document TDD): 16 razy
  - **SPRINT-REVIEW** (Sprint Review): 14 razy (nowy!)
  - **CAPACITY-PLAN** (Capacity Plan): 12 razy (nowy!)
  - **HIGH-LEVEL-ARCHITECTURE** (High-Level Architecture): 12 razy
  - **BUSINESS-CASE** (Business Case): 11 razy
  - **SECURITY-PLAN** (Security Plan): 11 razy
  - **RISK-REGISTER** (Risk Register): 10 razy (nowy!)
  - **MARKET-ANALYSIS** (Market Analysis): 10 razy

### Najczęściej blokujące dokumenty (top 15):
  - **ROADMAP-PROD** (Product Roadmap): 10 impacts (nowy lider!)
  - **POSTMORTEM** (Postmortem Report): 8 impacts (nowy!)
  - **MARKET-ANALYSIS** (Market Analysis): 8 impacts
  - **TIMELINE** (Timeline & Milestones): 8 impacts
  - **SPRINT-PLAN** (Sprint Plan): 7 impacts (nowy!)
  - **SPRINT-BACKLOG** (Sprint Backlog): 7 impacts (nowy!)
  - **PRD** (Product Requirements Document PRD): 7 impacts
  - **KPI-DASHBOARD** (KPI Dashboard Spec): 7 impacts (nowy!)
  - **RELEASE-CHECKLIST** (Release Checklist): 6 impacts (nowy!)
  - **CAPACITY-PLAN** (Capacity Plan): 6 impacts (nowy!)
  - **RISK-REGISTER** (Risk Register): 6 impacts (nowy!)
  - **SECURITY-PLAN** (Security Plan): 6 impacts
  - **RISK-OVERVIEW-TECH** (Risk Overview Techniczny): 6 impacts
  - **SIRP** (Security Incident Response Plan SIRP): 6 impacts
  - **MIGRATION-PLAN** (Migration Plan): 5 impacts (nowy!)

### Typy relacji:
  - **informs**: 575 (+132)
  - **influences**: 298 (+72)
  - **requires**: 310 (+96)
  - **blocks**: 109 (+35)

### Kategorie dokumentów:
  - Przedprodukcyjna: 26 (+1 - Roadmap Product)
  - Produkcyjna: 80 (+17 - Sprints, Roadmaps, Migration)
  - Branżowa: 13
  - Supporting: 31 (-2, przesunięte do produkcyjnej)
  - Atomic: 8 (nowa kategoria - satelity)

## Graf D: Architecture Transformation Workflow

Workflow transformacji architektury - od analizy stanu obecnego do implementacji.

```mermaid
graph TB
    CODEBASE["Codebase"]
    DEPLOYMENT_CONFIGS["Deployment Configs"]
    SYSTEM_MONITORING["System Monitoring"]
    EXISTING_DOCS["Existing Docs"]

    AS_IS["AS-IS Architecture"]
    CODE_REVIEW["Code Review"]
    TEST_RESULTS["Test Results"]
    INCIDENT_REPORTS["Incident Reports"]

    PROBLEMS["Problems Analysis"]
    ANTI_PATTERNS["Anti-Patterns Catalog"]

    BUSINESS_REQ["Business Requirements"]
    TECH_VISION["Tech Vision"]
    TO_BE["TO-BE Architecture"]

    INTEGRATION_POINTS["Integration Points"]
    MODULE_ROADMAP["Module Analysis Roadmap"]

    TEAM_CAPACITY["Team Capacity"]
    RISK_ASSESSMENT["Risk Assessment"]
    REFACTORING["Refactoring Process"]

    ADR["Architecture Decision Records"]
    MIGRATION_PLAN["Migration Plan"]
    IMPLEMENTATION_PLAN["Implementation Plan"]
    QUALITY_GATES["Quality Gates"]

    CODEBASE -->|requires| AS_IS
    DEPLOYMENT_CONFIGS -->|requires| AS_IS
    SYSTEM_MONITORING -->|requires| AS_IS
    EXISTING_DOCS -->|requires| AS_IS

    AS_IS -->|blocks| PROBLEMS
    AS_IS -->|blocks| TO_BE
    AS_IS -->|blocks| ANTI_PATTERNS
    AS_IS -->|requires| INTEGRATION_POINTS
    AS_IS -->|requires| MODULE_ROADMAP

    CODE_REVIEW -->|requires| PROBLEMS
    TEST_RESULTS -->|requires| PROBLEMS
    INCIDENT_REPORTS -->|requires| PROBLEMS
    AS_IS -->|requires| PROBLEMS

    AS_IS -->|requires| ANTI_PATTERNS
    CODE_REVIEW -->|requires| ANTI_PATTERNS

    PROBLEMS -->|blocks| TO_BE
    ANTI_PATTERNS -->|influences| PROBLEMS
    PROBLEMS -->|influences| ANTI_PATTERNS

    BUSINESS_REQ -->|requires| TO_BE
    TECH_VISION -->|requires| TO_BE
    PROBLEMS -->|requires| TO_BE
    AS_IS -->|requires| TO_BE

    TO_BE -->|requires| INTEGRATION_POINTS
    AS_IS -->|requires| INTEGRATION_POINTS

    TO_BE -->|requires| MODULE_ROADMAP
    PROBLEMS -->|requires| MODULE_ROADMAP
    AS_IS -->|requires| MODULE_ROADMAP
    TEAM_CAPACITY -->|influences| MODULE_ROADMAP

    TO_BE -->|blocks| REFACTORING
    PROBLEMS -->|blocks| REFACTORING
    MODULE_ROADMAP -->|blocks| REFACTORING
    TEAM_CAPACITY -->|requires| REFACTORING
    RISK_ASSESSMENT -->|requires| REFACTORING
    ANTI_PATTERNS -->|influences| REFACTORING

    TO_BE -->|blocks| ADR
    TO_BE -->|blocks| MIGRATION_PLAN
    REFACTORING -->|blocks| IMPLEMENTATION_PLAN
    REFACTORING -->|blocks| QUALITY_GATES

    INTEGRATION_POINTS -->|influences| IMPLEMENTATION_PLAN

    classDef current fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    classDef analysis fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    classDef target fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
    classDef process fill:#bbdefb,stroke:#0d47a1,stroke-width:2px
    classDef output fill:#e1bee7,stroke:#6a1b9a,stroke-width:2px

    class CODEBASE,DEPLOYMENT_CONFIGS,SYSTEM_MONITORING,EXISTING_DOCS,AS_IS current
    class PROBLEMS,ANTI_PATTERNS,CODE_REVIEW,TEST_RESULTS,INCIDENT_REPORTS analysis
    class BUSINESS_REQ,TECH_VISION,TO_BE,INTEGRATION_POINTS target
    class MODULE_ROADMAP,REFACTORING,TEAM_CAPACITY,RISK_ASSESSMENT process
    class ADR,MIGRATION_PLAN,IMPLEMENTATION_PLAN,QUALITY_GATES output
```

## Graf E: Sprint Types Workflow

Workflow różnych typów sprintów i ich powiązań.

```mermaid
graph TB
    subgraph Sprint_Core["Sprint Core"]
        SPRINT_CORE["Sprint Core Doc"]
        SPRINT_PLANNING["Sprint Planning"]
        TEAM_CAPACITY["Team Capacity"]
        PRD["PRD"]

        PRD -->|requires| SPRINT_CORE
        SPRINT_PLANNING -->|requires| SPRINT_CORE
        TEAM_CAPACITY -->|requires| SPRINT_CORE
    end

    subgraph Sprint_Discovery["Discovery Sprint"]
        SPRINT_DISCOVERY["Sprint Discovery Doc"]
        ROADMAP["Product Roadmap"]
        RESEARCH_Q["Research Questions"]
        HYPOTHESIS["Hypothesis"]

        ROADMAP -->|requires| SPRINT_DISCOVERY
        RESEARCH_Q -->|requires| SPRINT_DISCOVERY
        HYPOTHESIS -->|requires| SPRINT_DISCOVERY
    end

    subgraph Sprint_Hardening["Hardening Sprint"]
        SPRINT_HARDENING["Sprint Hardening Doc"]
        BUG_BACKLOG["Bug Backlog"]
        TECH_DEBT["Tech Debt Register"]
        QUALITY_METRICS["Quality Metrics"]

        BUG_BACKLOG -->|requires| SPRINT_HARDENING
        TECH_DEBT -->|requires| SPRINT_HARDENING
        QUALITY_METRICS -->|requires| SPRINT_HARDENING
    end

    subgraph Sprint_Release["Release Sprint"]
        SPRINT_RELEASE["Sprint Release Doc"]
        RELEASE_CHECKLIST["Release Checklist"]
        DEPLOYMENT_PLAN["Deployment Plan"]
        ROLLBACK_PLAN["Rollback Plan"]

        RELEASE_CHECKLIST -->|requires| SPRINT_RELEASE
        DEPLOYMENT_PLAN -->|requires| SPRINT_RELEASE
        ROLLBACK_PLAN -->|requires| SPRINT_RELEASE
    end

    subgraph Sprint_Infra["Infrastructure Sprint"]
        SPRINT_INFRA["Sprint Infra Doc"]
        INFRA_ROADMAP["Infrastructure Roadmap"]
        PLATFORM_REQ["Platform Requirements"]
        DEVOPS_BACKLOG["DevOps Backlog"]

        INFRA_ROADMAP -->|requires| SPRINT_INFRA
        PLATFORM_REQ -->|requires| SPRINT_INFRA
        DEVOPS_BACKLOG -->|requires| SPRINT_INFRA
    end

    SPRINT_CORE -->|related| SPRINT_DISCOVERY
    SPRINT_CORE -->|related| SPRINT_HARDENING
    SPRINT_CORE -->|related| SPRINT_RELEASE
    SPRINT_CORE -->|related| SPRINT_INFRA

    SPRINT_DISCOVERY -->|influences| PRD
    SPRINT_HARDENING -->|requires| QUALITY_METRICS
    SPRINT_RELEASE -->|requires| DEPLOYMENT_PLAN
    SPRINT_INFRA -->|influences| DEPLOYMENT_PLAN

    classDef core fill:#fff3e0,stroke:#e65100,stroke-width:3px
    classDef discovery fill:#e0f2f1,stroke:#00695c,stroke-width:2px
    classDef hardening fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef release fill:#e8eaf6,stroke:#283593,stroke-width:2px
    classDef infra fill:#f3e5f5,stroke:#4a148c,stroke-width:2px

    class SPRINT_CORE,SPRINT_PLANNING,TEAM_CAPACITY,PRD core
    class SPRINT_DISCOVERY,ROADMAP,RESEARCH_Q,HYPOTHESIS discovery
    class SPRINT_HARDENING,BUG_BACKLOG,TECH_DEBT,QUALITY_METRICS hardening
    class SPRINT_RELEASE,RELEASE_CHECKLIST,DEPLOYMENT_PLAN,ROLLBACK_PLAN release
    class SPRINT_INFRA,INFRA_ROADMAP,PLATFORM_REQ,DEVOPS_BACKLOG infra
```

## Graf F: Sprint Workflow (Szczegółowy)

Pełny workflow dokumentacji sprintowej - od planowania przez wykonanie do retrospektywy.

```mermaid
graph TB
    ROADMAP_PROD["Product Roadmap"]
    PRD["PRD"]
    PREV_SPRINT["Previous Sprint"]

    SPRINT_PLAN["Sprint Plan"]
    SPRINT_DOR["Sprint DoR"]
    SPRINT_DOD["Sprint DoD"]

    SPRINT_BACKLOG["Sprint Backlog"]
    TODO_PRD["TODO-PRD-*"]
    TODO_TDD["TODO-TDD-*"]

    SPRINT_IMPEDIMENTS["Impediments Log"]
    SPRINT_METRICS["Sprint Metrics"]
    SPRINT_SCOPE_CHANGE["Scope Change Request"]

    SPRINT_REVIEW["Sprint Review"]
    SPRINT_RETRO["Sprint Retro"]
    SPRINT_ACTION_ITEMS["Action Items"]
    SPRINT_APPROVAL["Sprint Approval"]

    NEXT_SPRINT["Next Sprint Plan"]

    ROADMAP_PROD -->|requires| SPRINT_PLAN
    PRD -->|requires| SPRINT_PLAN
    PREV_SPRINT -->|influences| SPRINT_PLAN

    SPRINT_PLAN -->|requires| SPRINT_DOR
    SPRINT_PLAN -->|requires| SPRINT_DOD
    SPRINT_PLAN -->|blocks| SPRINT_BACKLOG

    SPRINT_DOR -->|blocks| SPRINT_BACKLOG
    TODO_PRD -->|influences| SPRINT_BACKLOG
    TODO_TDD -->|influences| SPRINT_BACKLOG

    SPRINT_BACKLOG -->|influences| SPRINT_IMPEDIMENTS
    SPRINT_BACKLOG -->|informs| SPRINT_METRICS

    SPRINT_IMPEDIMENTS -->|informs| SPRINT_REVIEW
    SPRINT_IMPEDIMENTS -->|influences| SPRINT_SCOPE_CHANGE

    SPRINT_SCOPE_CHANGE -->|blocks| SPRINT_BACKLOG
    SPRINT_SCOPE_CHANGE -->|influences| SPRINT_PLAN

    SPRINT_METRICS -->|informs| SPRINT_REVIEW
    SPRINT_METRICS -->|informs| SPRINT_RETRO

    SPRINT_PLAN -->|requires| SPRINT_REVIEW
    SPRINT_BACKLOG -->|requires| SPRINT_REVIEW
    SPRINT_DOD -->|requires| SPRINT_REVIEW

    SPRINT_REVIEW -->|informs| SPRINT_RETRO
    SPRINT_REVIEW -->|blocks| SPRINT_APPROVAL
    SPRINT_REVIEW -->|influences| SPRINT_ACTION_ITEMS

    SPRINT_IMPEDIMENTS -->|influences| SPRINT_RETRO
    SPRINT_RETRO -->|blocks| SPRINT_ACTION_ITEMS
    SPRINT_RETRO -->|informs| SPRINT_APPROVAL

    SPRINT_DOD -->|blocks| SPRINT_APPROVAL
    SPRINT_APPROVAL -->|informs| NEXT_SPRINT

    SPRINT_REVIEW -->|informs| NEXT_SPRINT
    SPRINT_ACTION_ITEMS -->|informs| NEXT_SPRINT

    classDef planning fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef execution fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef tracking fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef closure fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    classDef external fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px

    class SPRINT_PLAN,SPRINT_DOR,SPRINT_DOD planning
    class SPRINT_BACKLOG,TODO_PRD,TODO_TDD execution
    class SPRINT_IMPEDIMENTS,SPRINT_METRICS,SPRINT_SCOPE_CHANGE tracking
    class SPRINT_REVIEW,SPRINT_RETRO,SPRINT_ACTION_ITEMS,SPRINT_APPROVAL closure
    class ROADMAP_PROD,PRD,PREV_SPRINT,NEXT_SPRINT external
```

## Graf G: Roadmap & Planning Workflow

Workflow planowania strategicznego i roadmapowego - od roadmapy przez capacity planning do realizacji.

```mermaid
graph TB
    VISION["Vision Document"]
    BIZ_CASE["Business Case"]

    ROADMAP_PROD["Product Roadmap"]

    CAPACITY_PLAN["Capacity Plan"]
    RISK_REGISTER["Risk Register"]
    KPI_DASHBOARD["KPI Dashboard Spec"]

    RELEASE_CHECKLIST["Release Checklist"]
    SPRINT_PLAN["Sprint Plan"]

    POSTMORTEM["Postmortem Report"]

    ROADMAP_UPDATE["Roadmap Updates"]

    VISION -->|requires| ROADMAP_PROD
    BIZ_CASE -->|requires| ROADMAP_PROD

    ROADMAP_PROD -->|blocks| CAPACITY_PLAN
    ROADMAP_PROD -->|blocks| RISK_REGISTER
    ROADMAP_PROD -->|blocks| KPI_DASHBOARD

    CAPACITY_PLAN -->|influences| ROADMAP_PROD
    RISK_REGISTER -->|influences| ROADMAP_PROD

    ROADMAP_PROD -->|influences| SPRINT_PLAN
    ROADMAP_PROD -->|influences| RELEASE_CHECKLIST

    KPI_DASHBOARD -->|influences| ROADMAP_PROD

    RELEASE_CHECKLIST -->|influences| POSTMORTEM
    POSTMORTEM -->|influences| RISK_REGISTER
    POSTMORTEM -->|influences| ROADMAP_UPDATE

    SPRINT_PLAN -->|informs| KPI_DASHBOARD

    classDef strategic fill:#e1f5ff,stroke:#01579b,stroke-width:3px
    classDef planning fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    classDef execution fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef feedback fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px

    class VISION,BIZ_CASE,ROADMAP_PROD strategic
    class CAPACITY_PLAN,RISK_REGISTER,KPI_DASHBOARD planning
    class SPRINT_PLAN,RELEASE_CHECKLIST execution
    class POSTMORTEM,ROADMAP_UPDATE feedback
```

## Graf H: Atomic Satellites Network

Satelitarne dokumenty atomowe wspierające główne dokumenty projektowe.

```mermaid
graph TB
    subgraph Parent_Docs["Parent Documents"]
        PRD["PRD"]
        TDD["TDD"]
        SPRINT_PLAN["Sprint Plan"]
        ROADMAP["Roadmap"]
        RELEASE["Release Checklist"]
    end

    subgraph Atomic_Satellites["Atomic Satellites"]
        TODO["TODO Template"]
        DOR["DoR Template"]
        DOD["DoD Template"]
        APPROVAL["Approval Template"]
        EVIDENCE["Evidence Template"]
        RISK_ITEM["Risk Item Template"]
        REL_ATOM["Release Checklist Atom"]
        POST_ATOM["Postmortem Atom"]
    end

    PRD -.->|generates| TODO
    TDD -.->|generates| TODO
    SPRINT_PLAN -.->|generates| TODO

    PRD -.->|requires| DOR
    SPRINT_PLAN -.->|requires| DOR

    PRD -.->|requires| DOD
    SPRINT_PLAN -.->|requires| DOD

    PRD -.->|requires| APPROVAL
    TDD -.->|requires| APPROVAL
    ROADMAP -.->|requires| APPROVAL

    TODO -.->|produces| EVIDENCE
    RELEASE -.->|requires| EVIDENCE

    PRD -.->|identifies| RISK_ITEM
    TDD -.->|identifies| RISK_ITEM

    RELEASE -.->|uses| REL_ATOM

    RELEASE -.->|triggers| POST_ATOM

    TODO -->|validated by| DOR
    TODO -->|completed per| DOD
    APPROVAL -.->|references| EVIDENCE
    POST_ATOM -.->|generates| TODO

    classDef parent fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef atomic fill:#ffecb3,stroke:#ff6f00,stroke-width:1px,stroke-dasharray: 5 5

    class PRD,TDD,SPRINT_PLAN,ROADMAP,RELEASE parent
    class TODO,DOR,DOD,APPROVAL,EVIDENCE,RISK_ITEM,REL_ATOM,POST_ATOM atomic
```

## Podsumowanie aktualizacji (2025-12-28)

### Dodane dokumenty
Zaktualizowano graf zależności o **26 nowych szablonów dokumentacji**:

**Sprint Documentation (11 templates):**
- SPRINT-PLAN: Główny plan sprintu z celem, zakresem i capacity
- SPRINT-BACKLOG: Lista zadań do wykonania w sprincie
- SPRINT-DOR: Definition of Ready - kryteria gotowości zadań
- SPRINT-DOD: Definition of Done - kryteria zakończenia
- SPRINT-IMPEDIMENTS: Log blokerów i przeszkód
- SPRINT-REVIEW: Review realizacji sprintu ze stakeholderami
- SPRINT-RETRO: Retrospektywa procesu i improvements
- SPRINT-ACTION-ITEMS: Action items z review i retro
- SPRINT-SCOPE-CHANGE: Change requests dla scope'u sprintu
- SPRINT-METRICS: Velocity, burndown, quality metrics
- SPRINT-APPROVAL: Formalne zatwierdzenie i sign-off sprintu

**Roadmap & Planning (6 templates):**
- ROADMAP-PRODUCT: Product Roadmap z milestones i epics
- CAPACITY-PLAN: Plan capacity i FTE demand przez milestones
- RISK-REGISTER: Rejestr ryzyk roadmapowych
- RELEASE-CHECKLIST: Checklist wydania (pre-freeze, release, post)
- POSTMORTEM-TEMPLATE: Postmortem po incydentach/release
- KPI-DASHBOARD-SPEC: Specyfikacja KPI i dashboardów

**Atomic Satellites (8 templates):**
- TODO-TEMPLATE: Atomowe zadania do wykonania
- DOR-TEMPLATE: Definition of Ready (atomowy)
- DOD-TEMPLATE: Definition of Done (atomowy)
- APPROVAL-TEMPLATE: Formalne zatwierdzenia
- EVIDENCE-TEMPLATE: Dowody i artefakty
- RISK-ITEM-TEMPLATE: Pojedyncze ryzyka
- RELEASE-CHECKLIST-ATOM: Atomowy checklist release
- POSTMORTEM-ATOM: Atomowy postmortem

**Migration (1 template):**
- MIGRATION-PLAN-DOC: Plan migracji systemów i danych

### Nowe grafy wizualizacyjne
- **Graf F**: Sprint Workflow (Szczegółowy) - pełny flow 11 dokumentów sprintowych od planowania do approval
- **Graf G**: Roadmap & Planning Workflow - strategiczny workflow od Vision przez Roadmap do execution
- **Graf H**: Atomic Satellites Network - satelitarne dokumenty atomowe wspierające parent documents

### Statystyki po aktualizacji
- Total dokumentów: **158** (+26, wzrost o 20%)
- Total dependencies: **471** (+95, wzrost o 25%)
- Total impacts: **509** (+104, wzrost o 26%)
- Total related: **387** (+72, wzrost o 23%)
- Total połączeń: **1367** (+271, wzrost o 25%)

### Kategorie dokumentów po aktualizacji
- Przedprodukcyjna: **26** (+1 - Roadmap Product)
- Produkcyjna: **80** (+17 - Sprints, Roadmaps, Migration)
- Branżowa: 13 (bez zmian)
- Supporting: **31** (-2, przesunięte do produkcyjnej)
- **Atomic: 8** (nowa kategoria satelitów)

### Kluczowe workflow dodane
1. **Sprint Cycle**: PLAN → BACKLOG → EXECUTION → REVIEW → RETRO → ACTION ITEMS → APPROVAL → NEXT SPRINT
2. **Strategic Planning**: VISION → ROADMAP → CAPACITY/RISK/KPI → SPRINT EXECUTION → POSTMORTEM → ROADMAP UPDATE
3. **Atomic Satellites**: Parent docs (PRD, TDD, Sprint) generują TODO/DoR/DoD/Approval/Evidence satellites
4. **Migration Workflow**: AS-IS → TO-BE → MIGRATION PLAN → IMPLEMENTATION → TESTING → ROLLBACK READINESS

### Nowe dokumenty w TOP rankingu
**ROADMAP-PROD** jest nowym liderem (28 dependencies)! Inne nowe dokumenty w top 15:
- SPRINT-PLAN (#2 z 25 deps)
- SPRINT-DOD (#5 z 18 deps)
- RELEASE-CHECKLIST (#6 z 17 deps)
- SPRINT-REVIEW (#9 z 14 deps)
- CAPACITY-PLAN (#10 z 12 deps)
- RISK-REGISTER (#14 z 10 deps)

### Impact na istniejące dokumenty
Nowe templates znacząco zwiększają połączenia z istniejącymi dokumentami:
- **PRD**: Teraz 23 dependencies (było 20) - nowe od Sprint Plan, Roadmap
- **TDD**: Połączenia z Sprint Backlog (TODO-TDD) i Migration Plan
- **TEST-PLAN**: Wpływ z Release Checklist i Migration testing
- **DEPLOYMENT-GUIDE**: Zależności od Release Checklist i Migration phases
- **RUNBOOK**: Połączenia z Postmortem i Release Checklist
- **MONITORING-PLAN**: Wpływ z KPI Dashboard i Postmortem

### Nowe punkty integracji
- **Sprint → Roadmap**: Sprint metrics wpływają na roadmap timeline i priorities
- **Roadmap → Capacity**: Roadmap milestones definiują capacity demand
- **Risk Register → Postmortem**: Materialized risks trigger postmortems
- **KPI Dashboard → Roadmap**: Underperforming KPIs force roadmap adjustments
- **Atomic Satellites → Parents**: TODO/DoR/DoD/Evidence wspierają wszystkie główne docs

### Nowe kategorie dokumentacji

#### Sprints (11 docs)
Kompletny zestaw dokumentacji sprintowej dla zespołów Agile. Pokrywa pełny cycle: planning → execution → review → retrospective → approval.

**Kluczowe połączenia:**
- Input: ROADMAP-PROD, PRD (wymagania)
- Output: SPRINT-METRICS, SPRINT-ACTION-ITEMS (feedback loop)
- Satelity: TODO, DoR, DoD, Approval, Evidence

#### Roadmaps (6 docs)
Strategic planning layer łączący Vision/Business Case z execution (Sprints, Releases).

**Kluczowe połączenia:**
- Input: VISION, BUSINESS-CASE
- Output: SPRINT-PLAN, RELEASE-CHECKLIST, CAPACITY-PLAN
- Feedback: POSTMORTEM, KPI-DASHBOARD

#### Atomic Satellites (8 docs)
Lekkie, reusable templates wspierające główne dokumenty jako satellites.

**Pattern użycia:**
- Każdy parent doc (PRD, TDD, Sprint, Roadmap) może mieć własne TODO/DoR/DoD/Approval/Evidence satellites
- Path: `satellites/{type}/{PARENT-DOC-ID}-{TYPE}-*.md`
- Umożliwiają granular tracking bez przeładowania parent docs

#### Migration (1 doc)
Specjalistyczny dokument dla migration projects, łączący AS-IS → TO-BE z execution plan.

**Kluczowe połączenia:**
- Input: AS-IS-ARCHITECTURE, TO-BE-ARCHITECTURE, REFACTORING-PROCESS
- Output: IMPLEMENTATION-PLAN, TEST-PLAN, DEPLOYMENT-GUIDE, ROLLBACK-PLAN

---

## Graf I: Tech Exploration Workflow

Workflow dla eksploracji technicznej (R&D software development).

**Use case:** Zespół eksploruje nową technologię / architekturę / tool.

**Workflow:** Unknown/Risk → Hypothesis → Experiment/PoC → Decision → Implementation

```mermaid
graph TB
    UNKNOWN["🔍 Unknown Identified<br/>(Backlog, Risk Register)"]
    HYPOTHESIS["📋 Hypothesis Document<br/>SEC-HYP: Formulate hypothesis"]
    SPIKE["⚡ Spike Solution<br/>(if quick answer needed)"]
    POC["🔬 Proof of Concept<br/>SEC-POC: Detailed validation"]
    EXPERIMENT["📊 Experiment Log<br/>SEC-EXP: Track execution"]
    FINDINGS["📈 Research Findings<br/>SEC-RF: Aggregate results"]
    TRADEOFF["⚖️ Trade-off Analysis<br/>SEC-TA: Quantitative scoring"]
    ADR["✅ Architecture Decision Record<br/>SEC-ADR: Final decision"]
    TDD["📐 Technical Design Document<br/>SEC-TDD: Implementation design"]
    IMPL["🚀 Implementation<br/>(Sprint Core)"]

    UNKNOWN -->|"Formalize"| HYPOTHESIS
    HYPOTHESIS -->|"Quick exploration<br/>(2-5 days)"| SPIKE
    HYPOTHESIS -->|"Detailed validation<br/>(2-4 weeks)"| POC
    SPIKE -->|"Results"| FINDINGS
    POC -->|"Track execution"| EXPERIMENT
    EXPERIMENT -->|"Results"| FINDINGS
    FINDINGS -->|"Multiple options?"| TRADEOFF
    TRADEOFF -->|"Recommendation"| ADR
    FINDINGS -->|"Single option"| ADR
    ADR -->|"Decision: Proceed"| TDD
    TDD -->|"Implementation plan"| IMPL

    style UNKNOWN fill:#fff3cd
    style HYPOTHESIS fill:#cfe2ff
    style SPIKE fill:#d1ecf1
    style POC fill:#d1ecf1
    style EXPERIMENT fill:#d1ecf1
    style FINDINGS fill:#d4edda
    style TRADEOFF fill:#f8d7da
    style ADR fill:#d4edda
    style TDD fill:#e2e3e5
    style IMPL fill:#e2e3e5
```

**Checkpoints:**
- **GATE-HYPOTHESIS_REVIEW** (after HYPOTHESIS) - Hypothesis validated?
- **GATE-VALIDATION_GATE** (after FINDINGS) - Results validate hypothesis (>70%)?
- **GATE-DECISION_APPROVAL** (after ADR) - Stakeholders approve decision?
- **GATE-REQ_FREEZE** (after TDD) - Ready for implementation?

**Example:** Explore React Server Components dla performance optimization
- HYPOTHESIS: RSC reduce initial page load by 30%+
- SPIKE: Quick compatibility check (3 days) → Compatible ✅
- POC: 2-week prototype → 420ms load time (48% improvement) ✅
- FINDINGS: Performance goal achieved, but Redux migration needed
- TRADEOFF: RSC + Zustand (8.5) vs Current (6.2) → RSC wins
- ADR: Migrate to RSC + Zustand
- TDD: Technical design dla implementation
- IMPL: Sprint 16-17

**Duration target:** <8 weeks

---

## Graf J: Business Innovation Workflow

Workflow dla innowacji biznesowych (Product/Startup validation).

**Use case:** Startup/Product team eksploruje nowy pomysł biznesowy.

**Workflow:** Idea → Research → Validation → Business Case → PRD → Implementation

```mermaid
graph TB
    IDEA["💡 Idea<br/>(Innovation Log, Brainstorm)"]
    HYPOTHESIS["📋 Hypothesis Document<br/>Business hypothesis"]
    MARKET["📊 Market Analysis<br/>TAM/SAM/SOM research"]
    EXPERIMENT["🧪 Experiment Log<br/>Customer interviews, A/B tests"]
    FINDINGS["📈 Research Findings<br/>Aggregate validation data"]
    FEASIBILITY["🔍 Feasibility Study<br/>Technical/Economic/Legal"]
    GONOGO["🚦 Go/No-Go Decision<br/>Proceed vs Pivot vs Kill"]
    BIZCASE["💼 Business Case<br/>ROI justification"]
    PRD["📋 Product Requirements<br/>Detailed requirements"]
    MVP["🚀 MVP Implementation"]

    IDEA -->|"Formalize"| HYPOTHESIS
    HYPOTHESIS -->|"Market validation"| MARKET
    HYPOTHESIS -->|"Customer validation"| EXPERIMENT
    MARKET -->|"Data"| FINDINGS
    EXPERIMENT -->|"Results"| FINDINGS
    FINDINGS -->|"Validated?"| FEASIBILITY
    FEASIBILITY -->|"Go/No-Go decision"| GONOGO
    GONOGO -->|"GO"| BIZCASE
    GONOGO -->|"PIVOT"| HYPOTHESIS
    GONOGO -->|"NO-GO"| IDEA
    BIZCASE -->|"Approved"| PRD
    PRD -->|"Implementation"| MVP

    style IDEA fill:#fff3cd
    style HYPOTHESIS fill:#cfe2ff
    style MARKET fill:#d1ecf1
    style EXPERIMENT fill:#d1ecf1
    style FINDINGS fill:#d4edda
    style FEASIBILITY fill:#f8d7da
    style GONOGO fill:#f8d7da
    style BIZCASE fill:#d4edda
    style PRD fill:#e2e3e5
    style MVP fill:#e2e3e5
```

**Checkpoints:**
- **GATE-HYPOTHESIS_VALIDATION** (after HYPOTHESIS) - Customer problem validated (>10 interviews)?
- **GATE-MARKET_VALIDATION** (after FINDINGS) - TAM >$100M, realistic SOM?
- **GATE-GO_NO_GO** (after FEASIBILITY) - GO vs PIVOT vs NO-GO?
- **GATE-REQ_FREEZE** (after PRD) - Requirements frozen, stakeholders aligned?
- **GATE-RELEASE_READY** (after MVP) - Ready to launch?

**Example:** AI-powered invoice processing dla SMB
- HYPOTHESIS: SMB spend >5h/week on manual invoicing, AI can reduce to <30min (90%)
- EXPERIMENT: 20 customer interviews → 17/20 confirm pain point ✅
- MARKET: TAM $5B, SAM $500M, SOM $50M ✅
- FINDINGS: 85% customer validation, attractive market
- FEASIBILITY: OCR+NLP achievable (92% accuracy), CAC $150, LTV $1,800 ✅
- GO/NO-GO: **GO** (all criteria met)
- BUSINESS-CASE: $500K investment, 5x ROI Year 3, break-even Month 18
- PRD: Features, metrics, MVP scope
- MVP: 6-month implementation

**Duration target:** <12 weeks

---

## Graf K: Risk Mitigation Workflow

Workflow dla mitygacji ryzyka (Enterprise/Compliance).

**Use case:** Enterprise projekt identyfikuje risk → eksploruje mitigation alternatives.

**Workflow:** Risk Identified → Alternative Exploration → Trade-off Analysis → Decision → Mitigation Plan

```mermaid
graph TB
    RISK["⚠️ Risk Identified<br/>(Risk Register, RAID Log)"]
    ALT["🔀 Alternative Exploration<br/>Identify mitigation options"]
    POC["🔬 PoC/Experiment<br/>(if validation needed)"]
    TRADEOFF["⚖️ Trade-off Analysis<br/>Quantitative scoring"]
    DECISION["✅ Decision<br/>(ADR or Decision Log)"]
    MITIGATION["🛡️ Mitigation Plan<br/>Implementation plan"]
    MONITORING["📊 Monitoring Plan<br/>Risk tracking"]

    RISK -->|"Explore options"| ALT
    ALT -->|"Validate options"| POC
    POC -->|"Results"| TRADEOFF
    ALT -->|"No validation needed"| TRADEOFF
    TRADEOFF -->|"Recommendation"| DECISION
    DECISION -->|"Mitigation approach"| MITIGATION
    MITIGATION -->|"Track effectiveness"| MONITORING

    style RISK fill:#f8d7da
    style ALT fill:#fff3cd
    style POC fill:#d1ecf1
    style TRADEOFF fill:#f8d7da
    style DECISION fill:#d4edda
    style MITIGATION fill:#e2e3e5
    style MONITORING fill:#e2e3e5
```

**Checkpoints:**
- **GATE-OPTIONS_IDENTIFIED** (after ALT) - Min 3 mitigation options identified?
- **GATE-DECISION_REVIEW** (after TRADEOFF) - Clear winner (score >7/10)?
- **GATE-APPROVAL** (after DECISION) - Stakeholders approve mitigation?

**Example:** Vendor lock-in risk (AWS-only → multi-cloud)
- RISK: 100% AWS dependency → vendor lock-in, pricing risk
- ALT: 4 options explored (Multi-cloud, K8s abstraction, Accept, Hybrid)
- POC: Kubernetes abstraction layer tested → achievable, 20% overhead
- TRADEOFF: K8s (7.5) vs Multi-cloud (6.8) vs AWS-only (5.2) → K8s wins
- DECISION (ADR): Adopt Kubernetes dla cloud abstraction
- MITIGATION: 6-month migration plan (Q1 dev, Q2 staging, Q3 production)
- MONITORING: Track cloud costs monthly, alert if >15% increase

**Duration target:** <6 weeks

---

## Graf L: Parallel Branching Workflow

Workflow dla równoległej eksploracji konceptów (R&D/Innovation).

**Use case:** R&D team eksploruje 2-3 różne podejścia równolegle.

**Workflow:** Parent Concept → Branch 1 & 2 & 3 → Compare → Merge/Kill Decision

```mermaid
graph TB
    PARENT["🌳 Parent Concept<br/>(Main hypothesis)"]
    BRANCH1["🔀 Branch 1<br/>(Approach A)"]
    BRANCH2["🔀 Branch 2<br/>(Approach B)"]
    BRANCH3["🔀 Branch 3<br/>(Approach C)"]
    EXP1["🧪 Experiment Log 1"]
    EXP2["🧪 Experiment Log 2"]
    EXP3["🧪 Experiment Log 3"]
    COMPARE["📊 Research Findings<br/>(Compare all branches)"]
    DECISION["✅ Merge/Kill Decision"]
    MERGE["🔀 Merge to Parent"]
    KILL["❌ Kill Branch"]

    PARENT -->|"Fork"| BRANCH1
    PARENT -->|"Fork"| BRANCH2
    PARENT -->|"Fork"| BRANCH3
    BRANCH1 -->|"Track"| EXP1
    BRANCH2 -->|"Track"| EXP2
    BRANCH3 -->|"Track"| EXP3
    EXP1 -->|"Results"| COMPARE
    EXP2 -->|"Results"| COMPARE
    EXP3 -->|"Results"| COMPARE
    COMPARE -->|"Evaluate"| DECISION
    DECISION -->|"Branch 1 wins"| MERGE
    DECISION -->|"Branch 2 & 3 fail"| KILL

    style PARENT fill:#fff3cd
    style BRANCH1 fill:#cfe2ff
    style BRANCH2 fill:#cfe2ff
    style BRANCH3 fill:#cfe2ff
    style COMPARE fill:#d4edda
    style DECISION fill:#f8d7da
    style MERGE fill:#d4edda
    style KILL fill:#f8d7da
```

**Checkpoints:**
- **GATE-BRANCH_CREATION** (after fork) - Clear divergence point, separate resources?
- **GATE-MID_POINT_REVIEW** (Week 2) - Each branch progressing, no blockers?
- **GATE-RESULTS_REVIEW** (after experiments) - All branches complete results?
- **GATE-MERGE_KILL_DECISION** (after comparison) - Merge best / Kill rest / Hybrid?

**Example:** Churn prediction model (3 architectures)
- PARENT: "AI model can predict churn z accuracy >80%"
- BRANCH1: Transformer (BERT-based, Team A, 4 weeks)
- BRANCH2: GNN (Graph Neural Network, Team B, 4 weeks)
- BRANCH3: Random Forest (baseline, Team C, 2 weeks)
- Mid-point (Week 2): Transformer 75% ✅, GNN 70% ⚠️, RF 72% ✅ → Continue all
- Results (Week 4):
  - Transformer: 83% accuracy ✅, 50ms inference ✅
  - GNN: 85% accuracy ✅, 300ms inference ❌
  - RF: 78% accuracy ❌, 10ms inference ✅
- TRADEOFF: Transformer (8.2) vs GNN (7.5) vs RF (6.8) → Transformer best balance
- DECISION: **Merge** Transformer to production, **Keep** RF as fallback, **Kill** GNN
- ADR: Transformer for production (83% accuracy, 50ms), RF for auditing (explainability)

**Duration target:** <6 weeks

---

## Workflow Paths Summary

**Concept Exploration Workflows (PROPOZYCJA-4):**

### Tech Exploration Path (Graf I):
```
UNKNOWN → HYPOTHESIS-DOC → SPIKE-SOLUTION → RESEARCH-FINDINGS → ADR → TDD → IMPL
UNKNOWN → HYPOTHESIS-DOC → POC-DOC → EXPERIMENT-LOG → RESEARCH-FINDINGS → TRADE-OFF-ANALYSIS → ADR → TDD → IMPL
```

### Business Innovation Path (Graf J):
```
IDEA → HYPOTHESIS-DOC → MARKET-ANALYSIS → RESEARCH-FINDINGS → FEASIBILITY → GO-NO-GO → BUSINESS-CASE → PRD → SPRINT-CORE
IDEA → HYPOTHESIS-DOC → EXPERIMENT-LOG → RESEARCH-FINDINGS → FEASIBILITY → GO-NO-GO → BUSINESS-CASE → PRD → MVP
```

### Risk Mitigation Path (Graf K):
```
RISK-REGISTER → ALTERNATIVE-EXPLORATION → POC-DOC → TRADE-OFF-ANALYSIS → ADR → MITIGATION-PLAN → MONITORING-PLAN
RISK-REGISTER → ALTERNATIVE-EXPLORATION → TRADE-OFF-ANALYSIS → ADR → MITIGATION-PLAN → MONITORING-PLAN
```

### Parallel Branching Paths (Graf L):
```
HYPOTHESIS-DOC → CONCEPT-BRANCH-001 → EXPERIMENT-LOG-001 → RESEARCH-FINDINGS → ADR
HYPOTHESIS-DOC → CONCEPT-BRANCH-002 → EXPERIMENT-LOG-002 → RESEARCH-FINDINGS → ADR
HYPOTHESIS-DOC → CONCEPT-BRANCH-003 → EXPERIMENT-LOG-003 → RESEARCH-FINDINGS → ADR
RESEARCH-FINDINGS → TRADE-OFF-ANALYSIS → ADR
```

**Integration z istniejącymi workflows:**
- Tech Exploration może być nested w Business Innovation (dla feasibility validation)
- Parallel Branching może być nested w Tech Exploration (dla porównania opcji)
- Risk Mitigation może używać Tech Exploration (dla walidacji mitigation options)
