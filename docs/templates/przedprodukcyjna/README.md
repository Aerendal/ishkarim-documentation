# Przedprodukcyjna — Dokumenty Fazy Przedprodukcyjnej

## 📋 Przeznaczenie

Folder zawiera **szablony dokumentów dla fazy przedprodukcyjnej** — etapu, w którym projekt jest planowany, analizowany i przygotowywany do wdrożenia, ale jeszcze **nie trafił do produkcji**.

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Planowania projektu** (charter, scope, feasibility)
- **Analizy wymagań** (PRD, use cases, user stories)
- **Projektowania architektury** (HLA, TDD, C4 model)
- **Zarządzania wymaganiami** (RTM, BRD, stakeholder analysis)
- **Przygotowania do wdrożenia** (test plans, deployment guides)

## 👥 Kto używa?

- **Product Owners** — PRD, user stories, stakeholder communication
- **Architects** — HLA, TDD, C4 diagrams
- **Tech Leads** — technical design, API specs
- **Project Managers** — project charter, timeline, risk register
- **QA Teams** — test plans, RTM

## ⏱️ Kiedy używać?

**Faza:** Przedprodukcyjna (Pre-Production)
**Timing:** Od kick-off do pierwszego deployment
**Lifecycle:** `draft → in-review → approved` (przed produkcją)

## 📂 Kategorie dokumentów (30 szablonów)

### Planowanie Projektu
- `project_charter.md` — Project Charter (cel, zakres, stakeholders)
- `project_scope_statement.md` — Scope Statement
- `feasibility_study.md` — Studium wykonalności
- `project_management_plan.md` — Plan zarządzania projektem

### Wymagania
- `prd_product_requirements_document.md` — PRD (wymagania produktowe)
- `brd_business_requirements_document.md` — BRD (wymagania biznesowe)
- `user_stories.md` — User Stories
- `use_cases.md` — Use Cases
- `rtm_requirements_traceability_matrix.md` — RTM (śledzenie wymagań)

### Architektura & Design
- `hla_high_level_architecture.md` — HLA (architektura wysokopoziomowa)
- `tdd_technical_design_document.md` — TDD (projekt techniczny)
- `c4_model_architecture_diagram.md` — C4 Model (diagramy architektury)
- `api_specification.md` — API Specification
- `database_schema_design.md` — Database Schema Design

### Testowanie
- `test_plan.md` — Test Plan (strategia testów)
- `test_cases.md` — Test Cases
- `uat_user_acceptance_testing_plan.md` — UAT Plan

### Deployment & Operations
- `deployment_guide.md` — Deployment Guide
- `runbook_operations_guide.md` — Runbook (operacje)
- `monitoring_plan.md` — Monitoring Plan

### Stakeholders & Communication
- `stakeholder_analysis.md` — Stakeholder Analysis
- `stakeholder_communication_plan.md` — Communication Plan
- `raci_matrix.md` — RACI Matrix (odpowiedzialności)

### Risk & Compliance
- `risk_register.md` — Risk Register
- `assumptions_log.md` — Assumptions Log
- `compliance_checklist.md` — Compliance Checklist

### Inne
- `glossary.md` — Glossary (słownik terminów)
- `project_timeline.md` — Project Timeline
- `decision_log.md` — Decision Log

## 🔗 Powiązania

**Dependencies:**
- ⬅️ **Business Case** (z fazy investor) → uzasadnia projekt
- ⬅️ **Market Analysis** → definiuje kontekst rynkowy

**Impacts:**
- ➡️ **Produkcyjna** → dokumenty przedprodukcyjne są podstawą dla produkcyjnych
- ➡️ **Sprints** → wymagania z PRD trafiają do sprintów
- ➡️ **Tests** → test plans bazują na wymaganiach

## 📊 Statystyki

- **Liczba szablonów:** 30
- **Pokrycie Cross-References:** 100%
- **Połączenia w grafie:** ~400+ dependencies/impacts
- **Średnia wielkość:** 150-300 linii per szablon

## 🚀 Quick Start

1. **Rozpocznij od:** `project_charter.md` (cel i zakres projektu)
2. **Następnie:** `prd_product_requirements_document.md` (wymagania)
3. **Potem:** `hla_high_level_architecture.md` (architektura)
4. **Na koniec:** `test_plan.md` + `deployment_guide.md` (przygotowanie do wdrożenia)

## 📖 Zobacz też

- [../produkcyjna/README.md](../produkcyjna/README.md) — Dokumenty produkcyjne
- [../sprints/README.md](../sprints/README.md) — Zarządzanie sprintami
- [../specs/](../specs/) — Specyfikacje systemu dokumentacji
- [../../dependency_graph.md](../../dependency_graph.md) — Graf zależności

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Przedprodukcyjna (Pre-Production Phase)
