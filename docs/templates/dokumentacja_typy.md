# Katalog typów dokumentacji projektowej

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: ALL-TEMPLATES
    type: requires
    reason: "Katalog indeksuje wszystkie szablony dokumentacji - wymaga ich istnienia"
    conditions:
      - when: "project.requires_formal_documentation === true"
        applies: true
    sections:
      - from: "All template files (przedprodukcyjna, produkcyjna, branżowa)"
        to: "Katalog sections (wymagane, przydatne, nice-to-have)"
        influence: "Templates są organizowane i kategoryzowane w katalogu"

  - id: SPECS-DOC-TYPES
    type: influences
    reason: "Specs Doc Types definiuje typy dokumentów - katalog je indeksuje"
    sections:
      - from: "Specs Doc Types doctypes definitions"
        to: "Katalog categorization (wymagane, przydatne, nice-to-have)"
        influence: "Specification informs catalog organization"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: USER-NAVIGATION
    type: blocks
    reason: "Katalog jest głównym punktem nawigacji - użytkownicy nie mogą znaleźć szablonów bez niego"
    sections:
      - from: "Catalog index structure (categories, links)"
        to: "User template discovery and selection"
        influence: "Catalog organization guides users to appropriate templates"

  - id: PROJECT-DOCUMENTATION-PLANNING
    type: influences
    reason: "Katalog pokazuje pełny zakres dokumentacji - pomaga w planowaniu"
    conditions:
      - when: "project.phase === 'planning'"
        applies: true
    sections:
      - from: "Complete template listing with categories"
        to: "Project documentation strategy and scope definition"
        influence: "Catalog helps teams decide which documents to create"

  - id: TEMPLATE-MAINTENANCE
    type: informs
    reason: "Katalog ułatwia zarządzanie szablonami - identyfikuje luki i duplikaty"
    sections:
      - from: "Master index of all templates"
        to: "Template governance and quality assurance"
        influence: "Centralized index enables template lifecycle management"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: SPECS-DOC-TYPES
    type: informs
    reason: "Specs Doc Types provides formal definitions referenced by catalog"

  - id: SPECS-GATES
    type: informs
    reason: "Gates specifications reference required documents listed in catalog"

  - id: EXAMPLES-README
    type: informs
    reason: "Examples directory provides filled examples of templates in catalog"

  - id: SUPPORTING-DOCS
    type: informs
    reason: "Supporting documentation complements templates in catalog"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CATALOG-*.md"
    required: false
    purpose: "Tracking catalog updates, new template additions, reorganization tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CATALOG-*.md"
    required: false
    purpose: "Template usage analytics, user navigation patterns, gap analysis"

  - type: DoD
    path: "satellites/dod/DOD-CATALOG-*.md"
    required: false
    purpose: "Definition of Done: all templates indexed, categories validated, links verified"
```

---

Pełny katalog dokumentów projektowych – **przedprodukcyjnych, produkcyjnych i branżowych** – wraz z odnośnikami do osobnych plików.

## 📊 Wizualizacje

**📈 [Graf Zależności Dokumentów](../dependency_graph.md)** - Kompletna mapa zależności między dokumentami
- 3 grafy Mermaid: przedprodukcyjna, produkcyjna, pełny graf
- 957 połączeń między 116 dokumentami
- Statystyki najważniejszych dokumentów i typów relacji
- Analiza dependencies, impacts, i related documents

---

## Przedprodukcyjna

### Wymagane

- 📄 [Executive Summary](przedprodukcyjna/executive_summary_doc.md)
- 📄 [Business Case](przedprodukcyjna/business_case_doc.md)
- 📄 [Pitch Deck (Inwestorski)](przedprodukcyjna/pitch_deck_doc.md)
- 📄 [Market Analysis](przedprodukcyjna/market_analysis_doc.md)
- 📄 [Financial Plan / Projections](przedprodukcyjna/financial_plan_doc.md)

### Przydatne

- 📄 [Feasibility Study](przedprodukcyjna/feasibility_study_doc.md)
- 📄 [Stakeholder Map](przedprodukcyjna/stakeholder_map_doc.md)
- 📄 [Go-To-Market Strategy](przedprodukcyjna/go_to_market_doc.md)
- 📄 [Risk Overview (Inwestycyjny)](przedprodukcyjna/risk_overview_invest_doc.md)
- 📄 [Research Plan](przedprodukcyjna/research_plan_doc.md)
- 📄 [Project Charter](przedprodukcyjna/project_charter_doc.md)
- 📄 [Project Management Plan](przedprodukcyjna/project_management_plan_doc.md)
- 📄 [Communication Plan](przedprodukcyjna/communication_plan_doc.md)
- 📄 [Procurement Plan](przedprodukcyjna/procurement_plan_doc.md)
- 📄 [Training Plan](przedprodukcyjna/training_plan_doc.md)
- 📄 [Cost-Benefit Analysis (CBA)](przedprodukcyjna/cba_doc.md)

### Nice-to-have

- 📄 [Vision Document](przedprodukcyjna/vision_document_doc.md)
- 📄 [Impact Assessment](przedprodukcyjna/impact_assessment_doc.md)
- 📄 [Innovation Roadmap](przedprodukcyjna/innovation_roadmap_doc.md)
- 📄 [Innovation Log](przedprodukcyjna/innovation_log_doc.md)

### Prawne i compliance (przedprodukcyjne)

- 📄 [DPIA](przedprodukcyjna/dpia_doc.md)
- 📄 [Legal & Regulatory Register](przedprodukcyjna/legal_register_doc.md)
- 📄 [Ethics & AI Guidelines](przedprodukcyjna/ethics_ai_guidelines_doc.md)
- 📄 [Sustainability Report](przedprodukcyjna/sustainability_report_doc.md)

### Finansowanie i inwestycje

- **Funding Application Budget Justification** — szczegółowe uzasadnienie kosztów dla grantów
- **Letters of Support / Partner Commitment Letters** — załączniki do aplikacji o dofinansowanie
- **Cap Table Scenarios / Waterfall Model / Valuation Memo** — scenariusze rozwodnienia, wyjścia, wyceny
- **Term Sheet / Cap Table** — dokumenty dla inwestycji i rozłożenia udziałów
- **Investor Due Diligence Pack** — pakiet dokumentów dla procesu due diligence
- **Grant Narrative / Project Description** — rozbudowany opis projektu wymagany przez programy grantowe

### Zarządzanie i governance (przedprodukcyjne)

- **RAID log** — Risks, Assumptions, Issues, Dependencies
- **RACI / Responsibility Matrix** — macierz odpowiedzialności dla ról i zadań
- **OKR / KPI Plan** — cele i kluczowe wskaźniki mierzenia postępu
- **Pricing Strategy / Commercial Model** — model cenowy i warunki komercyjne

---

## Produkcyjna

### Wymagane - Requirements & Design

- 📄 [PRD](produkcyjna/prd_doc.md)
- 📄 [BRD](produkcyjna/brd_doc.md)
- 📄 [High-Level Architecture](produkcyjna/high_level_architecture_doc.md)
- 📄 [Technical Design Document (TDD)](produkcyjna/tdd_doc.md)
- 📄 [System Context Diagram](produkcyjna/system_context_diagram_doc.md)

### Wymagane - Testing & Quality

- 📄 [Test Plan / QA Strategy](produkcyjna/test_plan_doc.md)
- 📄 [Quality Assurance Plan](produkcyjna/qa_plan_doc.md)
- 📄 [UAT Plan](produkcyjna/uat_plan_doc.md)
- 📄 [Test Summary Report](produkcyjna/test_summary_report_doc.md)
- 📄 [RTM](produkcyjna/rtm_doc.md)

### Wymagane - Planning & Execution

- 📄 [Timeline & Milestones](produkcyjna/timeline_doc.md)
- 📄 [Resource Requirements](produkcyjna/resource_requirements_doc.md)

### Przydatne - Risk & Security

- 📄 [Risk Overview (Techniczny)](produkcyjna/risk_overview_tech_doc.md)
- 📄 [Security Plan](produkcyjna/security_plan_doc.md)
- 📄 [SIRP](produkcyjna/sirp_doc.md)
- 📄 [Operational Risk Assessment](produkcyjna/operational_risk_assessment_doc.md)

### Przydatne - Data & Governance

- 📄 [Data Management Plan](produkcyjna/data_management_plan_doc.md)
- 📄 [Data Governance Policy](produkcyjna/data_governance_policy_doc.md)
- 📄 [Compliance Report](produkcyjna/compliance_report_doc.md)

### Przydatne - Change & Configuration

- 📄 [Change Management Plan](produkcyjna/change_management_plan_doc.md)
- 📄 [Configuration Management Plan](produkcyjna/configuration_management_plan_doc.md)
- 📄 [ADR](produkcyjna/adr_doc.md)

### Przydatne - Integration & Migration

- 📄 [Migration Plan](produkcyjna/migration_plan_doc.md)
- 📄 [Integration Plan](produkcyjna/integration_plan_doc.md)
- 📄 [API Documentation](produkcyjna/api_documentation_doc.md)

### Przydatne - Operations & Monitoring

- 📄 [Operational Manual](produkcyjna/operational_manual_doc.md)
- 📄 [Runbook](produkcyjna/runbook_doc.md)
- 📄 [Monitoring & Observability Plan](produkcyjna/monitoring_plan_doc.md)
- 📄 [Performance Test Report](produkcyjna/performance_test_report_doc.md)

### Przydatne - Vendor & Procurement

- 📄 [Vendor Management Plan](produkcyjna/vendor_management_plan_doc.md)

### Nice-to-have - Documentation & Knowledge

- 📄 [Knowledge Base](produkcyjna/knowledge_base_doc.md)
- 📄 [Change Log / Release Notes](produkcyjna/change_log_doc.md)
- 📄 [Training Materials](produkcyjna/training_materials_doc.md)
- 📄 [User Guide](produkcyjna/user_guide_doc.md)
- 📄 [Administrator Guide](produkcyjna/administrator_guide_doc.md)
- 📄 [Onboarding Guide](produkcyjna/onboarding_guide_doc.md)

### Nice-to-have - Maintenance & Support

- 📄 [Maintenance & Support Guide](produkcyjna/maintenance_guide_doc.md)
- 📄 [Deployment Guide](produkcyjna/deployment_guide_doc.md)

### Nice-to-have - Release & Incidents

- 📄 [Release Management Plan](produkcyjna/release_management_plan_doc.md)
- 📄 [Incident Report](produkcyjna/incident_report_doc.md)
- 📄 [Postmortem / Retrospective Report](produkcyjna/postmortem_report_doc.md)

### Nice-to-have - Service Management

- 📄 [SLA](produkcyjna/sla_doc.md)
- 📄 [DRP](produkcyjna/drp_doc.md)
- 📄 [Service Catalog](produkcyjna/service_catalog_doc.md)
- 📄 [Knowledge Transfer Plan](produkcyjna/knowledge_transfer_plan_doc.md)
- 📄 [Closure Report](produkcyjna/closure_report_doc.md)

### Nice-to-have - Accessibility & Testing

- 📄 [Accessibility Compliance Report](produkcyjna/accessibility_report_doc.md)

---

## Branżowa

### Medycyna / Healthcare

- 📄 [HIPAA Compliance Report](branzowa/medycyna/hipaa_compliance_doc.md)
- 📄 [Clinical Trial Documentation](branzowa/medycyna/clinical_trial_doc.md)
- 📄 [Medical Device File (MDR)](branzowa/medycyna/medical_device_file_doc.md)
- **Regulatory Submission Dossier (FDA, MDR)** — komplet dokumentów do zgłoszeń regulatorowych
- **Pharmacovigilance Plan / SAE Handling Guide** — opieka nad zdarzeniami niepożądanymi
- **Statistical Analysis Plan (SAP)** — planowanie analiz statystycznych w badaniach klinicznych
- **Clinical Study Protocol Deviations Log** — rejestr odchyleń od protokołu
- **Institutional Review Board (IRB) submission pack** — pakiet dla komisji etycznej
- **Clinical SOPs / CRO agreements** — procedury badań i umowy z CRO

### Finanse / Banking

- 📄 [PCI DSS Compliance Report](branzowa/finanse/pci_dss_doc.md)
- 📄 [SOX Compliance Report](branzowa/finanse/sox_compliance_doc.md)
- 📄 [Basel III Risk Report](branzowa/finanse/basel3_doc.md)
- **KYC / AML procedures & Risk Assessment** — procedury Know Your Customer i Anti-Money Laundering

### Administracja publiczna

- 📄 [GDPR Compliance Report](branzowa/administracja/gdpr_doc.md)
- 📄 [eIDAS Compliance Documentation](branzowa/administracja/eidas_doc.md)
- 📄 [Public Sector Transparency Report](branzowa/administracja/public_sector_transparency_doc.md)

### Militaria / Obronność

- 📄 [Security Clearance Documentation](branzowa/militaria/security_clearance_doc.md)
- 📄 [NATO STANAG Compliance](branzowa/militaria/nato_stanag_doc.md)
- 📄 [Cyber Defense Readiness Report](branzowa/militaria/cyber_defense_doc.md)
- **Export Control / EAR / ITAR documentation** — dokumentacja kontroli eksportu

### Przemysł / Manufacturing

- **Bill of Materials (BOM) + Manufacturing Validation Report** — lista materiałów i walidacja produkcji
- **Supplier Qualification Report / Supplier Audit Pack** — dokumentacja audytów dostawców
- **Traceability Matrix** — kluczowe w produktach medycznych/produkcji

### Chemia / Środowisko

- **Safety Data Sheet / REACH compliance** — karty charakterystyki i zgodność REACH
- **Environmental Impact Assessment / Carbon Footprint Report** — ocena wpływu środowiskowego

### Telekomunikacja

- **Spectrum / Regulatory Filings** — dokumentacja regulacyjna dla telekomunikacji

---

## Rozszerzone kategorie specjalistyczne

### Governance, prawne i finansowe

#### Prawne i umowy

- **Data Processing Agreement (DPA)** — umowa przetwarzania danych (klauzule RODO)
- **Terms of Service / EULA / Privacy Policy** — regulaminy i polityki klienta
- **IP / Patent Filing Brief** — podsumowanie pomysłów do zgłoszenia patentowego
- **Contract Templates: MSA, SoW, NDA** — wzorce umów
- **Shareholders Agreement / Investment Agreement** — umowy inwestycyjne
- **Subscription Agreement / Term Sheet** — szczegółowe wzory
- **Employee Contracts / Contractor Agreement** — umowy pracownicze
- **Contributor License Agreement (CLA)** — dla open source
- **Vendor SLA Templates** — szczegółowe umowy usługowe

#### Governance korporacyjne

- **Board Papers / Steering Committee Reports** — raporty dla zarządu
- **Company Articles / Bylaws, Cap Table** — dokumenty korporacyjne
- **Records Retention Schedule / Retention Policy** — zasady retencji dokumentów
- **Data Transfer Impact Assessment (DTIA)** — ocena ryzyka przy transferze poza EEA

#### Finanse i audyt

- **Cashflow Forecast** — prognoza przepływów pieniężnych (dzienny/miesięczny)
- **Balance Sheet / P&L Detailed Template** — dla due diligence
- **Management Accounts Pack** — miesięczny pack dla inwestora
- **Internal Audit Plan & Audit Report** — plan i raport z audytu wewnętrznego

### Ryzyko, zgodność i bezpieczeństwo

#### Compliance i certyfikacje

- **SOC1 / SOC2 Readiness Checklist i Report Template**
- **ISO Certification Pack (ISO9001, ISO27001)** — wymagane artefakty
- **FedRAMP / FIPS / CMMC** — dla rynków USA
- **Data Retention Schedule** — harmonogram retencji danych
- **Data Transfer Agreement (DTA) / Standard Contractual Clauses (SCC)**
- **Breach Notification Procedure** — szczegółowy proces notyfikacji incydentu
- **Third-Party Risk Assessment / Supplier Security Questionnaire (SSQ)** — ocena dostawców

#### Security Operations

- **Threat Model / STRIDE / Attack Surface Document** — analiza zagrożeń
- **Penetration Test Report / Vulnerability Assessment** — wyniki pentestu i plan naprawczy
- **Secrets & Key Management Policy** — polityka zarządzania kluczami
- **Identity & Access Management (IAM) Plan** — polityka ról, provisioning i SSO
- **Cryptography Policy** — wymagania szyfrowania
- **Bug Bounty / Responsible Disclosure Policy** — zasady zgłaszania luk
- **Secrets Inventory & Key Rotation Plan** — rejestr sekretów, harmonogram rotacji
- **Incident Forensics Report** — szczegółowy raport forensics
- **Threat Intelligence Feed Integration Spec** — specyfikacja integracji threat intelligence
- **Security Architecture Review Report** — przegląd architektury bezpieczeństwa
- **Red Team / Purple Team Report** — wyniki i remediation
- **Secrets Rotation & Key Custody Procedure** — procedury rotacji kluczy

### Operacje, SRE i DevOps

#### Infrastruktura i architektura

- **Network Diagram / Infra Topology** — szczegółowe diagramy sieci
- **Capacity & Scalability Plan** — prognozy obciążenia, plany skalowania
- **Backup & Restore Plan** — procedury i RTO/RPO testów
- **Cost / Run-rate Forecast (ops)** — bieżące prognozy kosztów operacyjnych

#### Deployment i releases

- **Service Decommission / Sunsetting Plan** — procedura zamykania usług
- **Cutover / Go-Live Checklist** — szczegółowy plan przełączenia produkcji
- **Blue/Green / Canary Deployment Plan** — strategie wdrożeń
- **Healthcheck / Readiness Endpoints Spec** — standardy endpointów zdrowia
- **Cost Optimisation / Cloud Run-rate Plan** — optymalizacje kosztów

#### Operations Management

- **SRE Runbooks / On-call Rota** — playbooki operacyjne i harmonogramy dyżurów
- **Service Transition Plan** — change → ops handover
- **On-call Rota & Escalation Matrix** — operacyjne playbooki

### Data, ML i AI

#### Data Management

- **Data Catalog / Data Dictionary** — rejestr zbiorów danych i metadanych
- **Data Lineage & Provenance Diagrams** — skąd pochodzi dataset, transformacje
- **Dataset Datasheet / Model Card** — opis zbioru danych i modelu
- **Computational Environment Spec / Reproducibility Pack** — wersje środowiska, reprodukcja eksperymentu

#### ML/AI Governance

- **Model Risk Assessment / Model Governance Policy** — lifecycle, retraining policy
- **Model Evaluation Report / Bias & Fairness Assessment** — metryki modeli, testy uprzedzeń
- **ML Ops Playbook / Model Governance** — lifecycle modeli, retraining, wersjonowanie
- **Model Explainability Report / Explainability Artifacts** — wyjaśnialność modeli
- **Red-teaming ML / Adversarial Testing Report** — testy adversarial
- **Data Retention & Deletion Playbook** — dla ML pipelines
- **Synthetic Data Policy / Generation Controls** — polityka danych syntetycznych
- **Model Card + Datasheet + Reproducibility Pack** — kompletny pakiet dokumentacji modelu

### QA i testowanie

#### Plany i strategie testowe

- **Test Cases / Test Scripts** — szczegółowe przypadki testowe
- **Regression Test Suite / Automation Plan** — plan testów regresyjnych
- **Test Data Management Plan** — provisioning testów, anonimizacja danych
- **Automation Coverage Matrix** — mapowanie testów automatycznych do wymagań/RTM
- **PenTest Remediation Plan** — plan naprawczy po pentestach
- **Regression Release Checklist / Release Validation Script** — checklist walidacji

### UX, produkt i design

#### Design i użyteczność

- **Design System / Component Library Docs** — zasady UI, komponenty i tokeny
- **User Journey / Customer Journey Map** — przebieg doświadczeń użytkownika
- **Usability Test Report** — wyniki badań użyteczności i rekomendacje
- **Design Handoff Checklist** — dla devów

#### Lokalizacja i dostępność

- **Localization / Internationalization Plan** — tłumaczenia i obsługa lokalizacji
- **Localization Matrix / Translation Glossary** — zasady tłumaczeń
- **Accessibility Statement / VPAT** — kompletne oceny dostępności i deklaracje zgodności

#### Eksperymenty i feature management

- **Experimentation Plan / Feature Flagging Strategy** — jak testujemy zmiany, metryki sukcesu
- **Feature Toggle & Experimentation Plan** — plany A/B testów

### Marketing, sprzedaż i sukces klienta

#### Marketing i komunikacja

- **Marketing Plan / Campaign Briefs** — plany kampanii i KPI marketingowe
- **Press Kit / Brand Guidelines** — materiały PR i zasady brandingu

#### Sprzedaż

- **Sales Deck / Commercial Proposal Templates** — gotowe oferty i prezentacje
- **One-pager (investor-ready), Pitch metrics appendix** — materiały dla inwestorów
- **Case Study Template** — referencje do due diligence

#### Customer Success

- **Customer Success Plan / Onboarding Flow** — plan wdrożenia klienta i metryki sukcesu
- **Customer Onboarding Checklist / Success SLA** — checklist i SLA dla sukcesu klienta

### HR i organizacja

#### Rekrutacja i struktura

- **Hiring Plan / Org Chart** — plan rekrutacji i struktura organizacji
- **Role Profiles / Competency Matrix** — opisy ról i wymaganych kompetencji
- **Offer Letter / Compensation Matrix Template** — szablony ofert
- **Competency Assessment Template / Interview Scorecards** — oceny i scorecards

#### Rozwój i szkolenia

- **Training & Certification Plan** — roadmap szkoleń i certyfikacji
- **Competency Matrix + Training Roadmap** — mapowanie braków kompetencyjnych vs. plan szkoleń
- **Employee Handbook** — policy pack

#### Change Management

- **Organisational Change Management Plan** — przy dużych transformacjach

### Badania i nauka

#### Research & Development

- **State of the Art / Literature Review** — przegląd badań i rozwiązań
- **Prior Art / Freedom to Operate Report** — analiza patentów (przy IP)
- **Pre-registration / Preregistration documents** — dokumenty przedrejestracji badań

### Dokumenty pomocnicze i administracyjne

#### Operacyjne szablony

- **Change Request Form / CAB Minutes Template** — formularze CR i minutki CAB
- **Decision Log / Meeting Minutes** — rejestr decyzji i spotkań
- **Template: Meeting Minutes / Decision Log** — szablony operacyjne
- **Knowledge Transfer Checklist / Handover Form** — checklist przekazania wiedzy
- **Archive Index / Document Retention Policy** — zasady przechowywania i archiwizacji
- **Meeting Agendas + Action Item Tracker** — standaryzacja spotkań
- **Feature Decision Log / Change Impact Analysis** — dokumentacja decyzji i wpływu
- **API Catalogue / Endpoint Inventory** — ułatwia integracje i automatyzację

---

## TODO — szablony zadań

Dodano komplet szablonów TODO do powiązania z dokumentami.

**Lokalizacja szablonów:**

- `templates/todos/TODO_template.md` — wzór ogólny
- `templates/todos/TODO-EXSUM-001.md` — Executive Summary
- `templates/todos/TODO-PRD-001.md` — PRD
- `templates/todos/TODO-TDD-001.md` — TDD
- `templates/todos/TODO-FEAS-001.md` — Feasibility Study
- `templates/todos/TODO-BUSCASE-001.md` — Business Case
- `templates/todos/TODO-SEC-001.md` — Security Plan
- `templates/todos/TODO-DPIA-001.md` — DPIA
- `templates/todos/TODO-HIPAA-001.md` — HIPAA Compliance

**Zawartość szablonu TODO:**

- **Front-matter YAML**: id, title, document, owner, priority (P0-P3), effort_days, status (todo/in-progress/review/done/blocked), created, due, dependencies, related_docs, tags
- **Sekcje**: Opis, Cel / wartość biznesowa, Kryteria akceptacji, Kroki / checklist, Notatki

**Przykładowy workflow:**

1. Utwórz `docs/client_X/todos/` i skopiuj odpowiednie pliki TODO
2. Uzupełnij front-matter (owner, due, dependencies)
3. Przenieś zadania do Kanban (GitHub Projects / Jira) lub otwórz PR
4. Po ukończeniu zaktualizuj status na `done` i przypisz wersję dokumentu

---

## Uwagi

Każdy dokument z osobnym plikiem zawiera: **cel, zawartość, czego nie zawiera, objętość, kategoria, odbiorcy**.
