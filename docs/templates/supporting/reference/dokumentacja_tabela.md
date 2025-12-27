# 📊 Tabela porównawcza dokumentacji projektowej (zaktualizowana)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Poniżej znajduje się uporządkowana tabela dokumentów projektowych — pogrupowana według faz i obszarów (przedprodukcyjne, produkcyjne, compliance/data, ML/R&D, ops, prawne/ granty, UX/marketing oraz inne). Każda tabela zawiera: **zawartość**, **czego nie zawiera**, **sugerowaną objętość** i **kategoryzację**.

---

## A. Dokumenty przedprodukcyjne

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Executive Summary | Skrót projektu, problem, rozwiązanie, wezwanie do działania | Detali technicznych, backlogów | 1–2 | 5–7 | Wymagane (przedprod.) |
| Business Case | ROI, korzyści, alternatywy, NPV/ROI, scenariusze | Szczegółowych planów kodowania | 3–6 | 8–12 | Wymagane (przedprod.) |
| Pitch Deck | Kluczowe slajdy: problem, rozwiązanie, model, zespół, finansy | Architektury systemu, kodu | 10–15 slajdów | ~1 slajd / punkt | Wymagane (przedprod.) |
| Market Analysis | Wielkość rynku, trendy, konkurencja, TAM/SAM/SOM | Kodu, surowych formuł | 5–8 | 6–10 | Wymagane (przedprod.) |
| Financial Plan / Projections | Budżet, projekcje przychodów/kosztów, scenariusze | Planów technicznych | 3–6 | 6–10 | Wymagane (przedprod.) |
| Feasibility Study | Ocena wykonalności technicznej i ekonomicznej, rekomendacje | Detali sprintów | 4–8 | 8–12 | Wymagane (przedprod.) |
| Stakeholder Map | Interesariusze, wpływ/zaangażowanie, matryca interesów | Szczegółowych ocen personalnych | 1–2 | 5–8 | Przydatne (przedprod.) |
| Go‑To‑Market Strategy | Kanały, pricing, partnerstwa, plan wejścia na rynek | Specyfikacji kodu | 4–6 | 8–10 | Przydatne (przedprod.) |
| Research Plan | Pytania badawcze, metodologia, harmonogram | Implementacji kodu, backlogów | 3–5 | 6–10 | Przydatne (przedprod.) |
| Vision Document (Extended) | Wizja 2–3 lata, kierunki rozwoju, scenariusze strategiczne | Szczegółowych planów sprintów | 4–6 | 7–10 | Nice‑to‑Have (przedprod.) |
| Impact Assessment | Wpływ społeczny, regulacyjny, środowiskowy | Detali finansowych | 2–4 | 5–7 | Nice‑to‑Have (przedprod.) |
| Innovation Roadmap | Kierunki R&D, eksperymenty, kamienie milowe | Kodów źródłowych | 2–4 | 5–8 | Nice‑to‑Have (przedprod.) |
| Funding Application Budget Justification | Szczegółowe rozbicie kosztów dla grantów | Szerszych analiz rynkowych | 2–6 | 6–10 | Wymagane (granty) |
| Letters of Support / Partner Commitments | Listy intencyjne, zobowiązania partnerów | Pełnych kontraktów | 1–3 | 3–6 | Wymagane (granty/inwestorzy) |
| Cap Table / Valuation Memo | Struktura udziałów, scenariusze rozwodnienia, założenia wyceny | Szczegółowych planów produktu | 1–4 | 4–8 | Przydatne (inwestorzy) |

---

## B. Dokumenty produkcyjne / inżynierskie

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Product Requirements Document (PRD) | Funkcje, user stories, acceptance criteria, priorytety, kontekst biznesowy | Luźnych pomysłów | 8–20 | 20–40 | Wymagane (prod.) |
| Basic Requirements Document (BRD) | Minimalne wymagania funkcjonalne i niefunkcjonalne, zakres MVP | Nadmiarowych detali | 5–8 | 10–18 | Wymagane (prod.) |
| High‑Level Architecture (HLA) | Schemat systemu, moduły, integracje, zależności | Kod źródłowy | 3–6 | 6–10 | Wymagane (prod.) |
| Technical Design Document (TDD) | Moduły, klasy, API, sekwencje, diagramy, migracje | Strategii sprzedaży | 10–30 | 25–50 | Wymagane (prod.) |
| Architecture Decision Records (ADR) | Decyzje architektoniczne, kontekst, trade‑offs, konsekwencje | Długie opisy implementacji (kod) | 1–3 / entry | 3–6 / entry | Ciągłe (prod.) |
| Test Plan / QA Strategy | Typy testów, scenariusze, środowiska, kryteria akceptacji | Raportów finansowych | 5–10 | 10–20 | Wymagane (prod.) |
| Requirements Traceability Matrix (RTM) | Mapowanie wymagań → testy → user stories → implementacja | Kodu implementacji | 1–3 | 10–20 | Przydatne (prod.) |
| Runbook / Operations Manual | Procedury uruchomienia, CI/CD, playbooks, runbooks dla SRE | Slajdów inwestorskich | 5–15 | 15–30 | Przydatne (prod./ops) |
| Release Management Plan | Kryteria release, rollback, cutover plan, harmonogram | Strategii biznesowych | 2–6 | 6–12 | Przydatne (prod.) |
| UAT Plan | Scenariusze akceptacyjne, testy end‑to‑end, kryteria sukcesu | Raportów technicznych niepowiązanych z akceptacją | 2–6 | 6–12 | Przydatne (prod.) |
| Migration Plan | Plan migracji danych/systemów, rollback, walidacja danych | Materiałów marketingowych | 2–6 | 6–10 | Przydatne (prod.) |
| Integration Plan | Schematy integracji, kontrakty API, SLA integracyjne | Treści marketingowe | 2–6 | 6–12 | Przydatne (prod.) |
| API Documentation (machine‑readable) | Endpoints, request/response, auth, przykłady, wersjonowanie | Strategii sprzedaży | 3–20 | 8–30 | Wymagane / Przydatne (prod.) |
| Performance Test Report | Wyniki obciążeniowe, bottlenecks, rekomendacje, wykresy | Raportów finansowych | 3–8 | 8–16 | Przydatne (prod.) |
| Monitoring & Observability Plan | Metryki, alerty, SLO/SLI, dashboardy, metryki business | Treści marketingowe | 2–6 | 6–12 | Przydatne (ops.) |
| SIRP / Security Incident Response Plan | Procedury reagowania, komunikacja, role, eskalacje | Surowych danych analitycznych (bez podsumowania) | 3–8 | 8–14 | Wymagane / Przydatne (ops./security) |
| DRP / BCP | Disaster recovery, RTO/RPO, procedury awaryjne, checklists | Planów rozwoju produktu | 3–8 | 8–16 | Wymagane (ops.) |
| SLA / Service Catalog | Oferta usług, poziomy usług, KPI, odpowiedzialności | Kodów źródłowych | 1–4 | 4–10 | Przydatne (ops./biz) |

---

## C. Compliance, bezpieczeństwo i zarządzanie danymi

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Data Management Plan | Schematy danych, retencja, lineage, polityki backupowe | Szczegółów implementacji kodu | 2–6 | 6–12 | Wymagane / Przydatne (data) |
| Data Governance Policy | Role, klasyfikacja danych, polityki dostępu, właściciele danych | Szczegółów kodu | 2–6 | 6–10 | Przydatne (governance) |
| DPIA (Data Privacy Impact Assessment) | Mapy przepływu danych, ocena ryzyka PII/PHI, rekomendacje | Materiałów marketingowych | 3–6 | 6–10 | Wymagane (compliance) |
| HIPAA Compliance Report | Polityki PHI, audyty, procedury breach, kontrola dostępu | Szczegółowych implementacji kodu | 3–8 | 6–12 | Wymagane (medycyna, US) |
| PCI DSS Compliance Report | Audyty płatności, szyfrowanie, testy penetracyjne, konfiguracje | Planów sprzedaży | 5–12 | 8–16 | Wymagane (fintech) |
| SOX Compliance Report | Kontrole wewnętrzne, raporty finansowe, procedury audytu | Kodu aplikacji | 3–8 | 6–12 | Wymagane (finanse/korpo) |
| Third‑Party Risk Assessment / SSQ | Ocena dostawców, kontrola bezpieczeństwa, wymagania SLA | Pełnych kontraktów | 2–6 | 6–12 | Wymagane (compliance) |
| Breach Notification Procedure | Kroki notyfikacji, timeline, komunikacja z regulatorami/klientami | Strategii marketingowych | 1–4 | 4–8 | Wymagane (security/compliance) |
| Secrets Inventory & Key Rotation Plan | Lista sekretów, harmonogram rotacji, właściciele | Kodów źródłowych (sekrety nie przechowywać w repo) | 1–3 | 4–6 | Przydatne (security) |
| Supplier Qualification Pack / Audit Report | Wyniki audytów dostawców, rekomendacje, oceny ryzyka | Planów produktowych | 3–8 | 6–12 | Wymagane (hardware/medical) |

---

## D. ML / Research / Reproducibility

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Computational Environment Spec / Repro Pack | Specyfikacja środowiska (Docker/Conda), seed data, instrukcje uruchomienia | Materiałów marketingowych | 1–4 | 4–8 | Wymagane (R&D) |
| Model Risk Assessment / Model Governance Policy | Polityki retrainingu, walidacja modelu, monitorowanie driftu | Szczegółów planów sprzedaży | 2–6 | 6–12 | Wymagane (AI‑critical) |
| Data Lineage & Provenance Diagrams | Źródła danych, transformacje, właściciele danych | Kodów implementacji | 1–4 | 4–8 | Przydatne (data/compliance) |
| Experimentation Plan / Feature Flag Strategy | Hipotezy, metryki sukcesu, rollback, flagi funkcji | Pełnej implementacji | 2–4 | 4–8 | Przydatne (product/ops) |
| Test Data Management Plan | Anonimizacja, provisioning, seedy testowe, polityki | Materiałów marketingowych | 2–4 | 4–8 | Wymagane (QA/integration) |

---

## E. Ops / DevOps / SRE

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Cutover / Go‑Live Checklist (detailed) | Krok po kroku cutover, testy rollback, checklists pre/post | Materiałów marketingowych | 1–3 | 6–12 | Wymagane (release) |
| Service Decommission / Sunsetting Plan | Plan zamknięcia usługi, migracje danych, komunikacja klientom | Strategii sprzedażowych | 1–4 | 4–8 | Przydatne (ops) |
| Healthcheck / Readiness Endpoints Spec | Specyfikacja endpointów health/readiness, formaty odpowiedzi, polityki | Materiałów marketingowych | 1–2 | 2–4 | Przydatne (dev/sre) |
| Cost Optimisation / Cloud Run‑rate Plan | Prognoza kosztów, optymalizacje, rekomendacje oszczędności | Planów produktowych | 2–4 | 4–8 | Przydatne (ops/fin) |
| Secrets Inventory (powtórzone) | Rejestr sekretów i powiązane procesy | - | 1–3 | 4–6 | Przydatne (security) |

---

## F. Legal / Regulatory / Grants

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Grant Narrative / Project Description (długi) | Rozbudowany opis projektu wymagany w aplikacjach grantowych | Krótkich streszczeń | 5–20 | 10–30 | Wymagane (granty) |
| Funding Application Budget Justification | Szczegółowe uzasadnienie kosztów dla grantów | Ogólnych kalkulacji | 2–6 | 6–10 | Wymagane (granty) |
| Regulatory Submission Dossier (FDA/MDR) | Pełna dokumentacja do zgłoszeń regulatorowych, raporty z badań, dane kliniczne | Planów marketingowych | 20–200+ | 50+ | Wymagane (medycyna) |
| Pharmacovigilance Plan / SAE Handling Guide | Procedury zgłaszania zdarzeń niepożądanych, eskalacje | Strategii sprzedaży | 5–15 | 10–20 | Wymagane (klinika/medycyna) |

---

## G. UX / Marketing / Localization

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Localization / Translation Glossary & Style Guide | Terminologia, ton, słownictwo, przykłady tłumaczeń | Kodów implementacji | 1–3 | 3–6 | Nice‑to‑Have (global) |
| Case Study / Customer Reference Template | Struktura studium przypadku, metryki, wyniki | Danych wrażliwych | 1–3 | 3–6 | Nice‑to‑Have (marketing) |
| VPAT / Accessibility Statement | Wyniki testów dostępności, zgodność z WCAG, rekomendacje | Kodów źródłowych | 2–6 | 4–10 | Przydatne (compliance) |

---

## H. Inne / organizacyjne / drobne

| **Nazwa dokumentu** | **Zawiera** | **Czego nie zawiera** | **Strony (suger.)** | **Punkty (suger.)** | **Kategoria** |
|---|---|---:|---:|---:|---|
| Records Retention Schedule / Retention Policy | Zasady retencji dokumentów/danych, RTO/RPO, okresy przechowywania | Szczegółów technicznych | 1–4 | 4–8 | Przydatne (governance) |
| Meeting Agendas + Action Item Tracker (template) | Szablony spotkań, lista zadań, przypisania odpowiedzialności | Treści techniczne | 1–2 | 2–4 | Nice‑to‑Have (org) |
| Feature Decision Log / Change Impact Analysis | Decyzje funkcjonalne, wpływ zmian, analiza wpływu | Implementacji kodu | 1–3 | 3–6 | Przydatne (product) |
| API Catalogue / Endpoint Inventory (machine‑readable) | Lista endpointów, właściciele, wersje, statusy | Treści marketingowe | 1–5 | 5–12 | Przydatne (integracje) |

---

**Uwaga:** wartości „Strony” i „Punkty” są orientacyjne i zależą od złożoności projektu. Tabela służy jako mapa referencyjna do generowania checklist, TODO i szablonów dokumentów.

Jeśli chcesz, mogę:
- wygenerować wszystkie powyższe szablony `.md` i umieścić je w `templates/extra/`,
- przygotować manifest CSV/JSON z metadanymi i estymacjami,
- wygenerować TODO dla każdego wpisu automatycznie (plik per dokument).

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: ALL-DOC-TYPES-*
    type: requires
    reason: "Comparison table requires comprehensive list of all document types"
    conditions:
      - when: "project.has_documentation === true"
        applies: true
    sections:
      - from: "Document Type Catalog §All types"
        to: "§A-H All tables"
        influence: "Document catalog defines rows in comparison table"

  - id: DOC-TEMPLATES-*
    type: requires
    reason: "Table attributes come from template specifications"
    sections:
      - from: "Templates §Content specifications"
        to: "§A-H Column: Zawiera"
        influence: "Template content defines what each document contains"
      - from: "Templates §Page estimates"
        to: "§A-H Column: Strony"
        influence: "Templates provide page count guidance"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: PROJECT-SCOPE-*
    type: informs
    reason: "Table helps scope projects by selecting required vs nice-to-have docs"
    conditions:
      - when: "project.phase === 'planning'"
        applies: true
    sections:
      - from: "§A-H Column: Kategoria"
        to: "Project Scope §1 Document selection"
        influence: "Category classifications guide document prioritization"

  - id: EFFORT-ESTIMATION-*
    type: informs
    reason: "Table page counts and sections inform effort estimation"
    sections:
      - from: "§A-H Column: Strony/Punkty"
        to: "Effort Estimation §1 Documentation effort"
        influence: "Page counts translate to estimated writing effort"

  - id: MANIFEST-*
    type: informs
    reason: "Table provides metadata for manifest generation"
    sections:
      - from: "§A-H All columns"
        to: "Manifest CSV/JSON §All records"
        influence: "Table data populates manifest metadata fields"

  - id: TODO-GENERATION-*
    type: informs
    reason: "Table entries generate TODO items for document creation"
    sections:
      - from: "§A-H All rows"
        to: "TODO §Per document"
        influence: "Each table row can generate a TODO for document creation"
```

### Related Documents

```yaml
related:
  - id: TOC-DOKUMENTACJA-*
    type: informs
    reason: "TOC provides hierarchical navigation complementing table view"

  - id: DIAGRAM-ZALEZNOSCI-*
    type: informs
    reason: "Dependency diagram shows relationships not visible in table"

  - id: TEMPLATES-README-*
    type: informs
    reason: "Template README provides usage guidance for documents in table"
```

### Satellite Documents

```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TABELA-*.md"
    required: false
    purpose: "Real project examples validating table estimates and categories"

  - type: TODO
    path: "satellites/todos/TODO-TABELA-*.md"
    required: false
    purpose: "Track table updates as new document types are added"
```
