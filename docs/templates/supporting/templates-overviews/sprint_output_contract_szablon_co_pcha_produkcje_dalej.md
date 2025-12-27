# Sprint Output Contract

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Ten dokument jest **kontraktem rezultatów sprintu**. Jego celem jest wyeliminowanie sytuacji, w której sprint produkuje wyłącznie notatki lub „postęp deklaratywny”, zamiast realnych artefaktów, które **pchają produkcję dalej**.

**Zasada nadrzędna:** każdy element sprintu musi wskazać **konkretny artefakt wyjściowy (output)** umieszczony w jednym z kanonicznych miejsc: kod/infra, dokumentacja, QA, release, ops, governance.

> Uwaga: w sekcji „Szablon pliku” celowo występują pola typu `...` — to są **placeholdery**. Żeby nie było „pusto”, w dalszej części dodałem też **w pełni wypełniony przykład** (realistyczna instancja sprintu), gotowy do skopiowania i edycji.

---

## 1) Jak używać

- Umieść **jedną instancję** tego pliku w: `docs/<project>/sprints/SXX/sprint-output-contract.md`.
- Każdy wpis w `sprint-backlog.md` musi mieć jednoznacznie zdefiniowane: `output_type`, `output_location`, `verification`.
- Sprint **DoR** (wejście) i Sprint **DoD** (wyjście) powinny wymagać zgodności z tym kontraktem.

---

## 2) Kanoniczne typy output (dozwolone)

Używaj jednego (lub kilku) z poniższych typów. To są miejsca, które realnie „pchają produkcję dalej”:

1. **CODE** — commit/PR/merge/tag w repo (implementacja).
2. **INFRA** — IaC (Terraform/Ansible), konfiguracje, manifesty (wdrożenia).
3. **DOC-REQ** — dokumentacja wymagań i produktu (PRD/BRD/RTM).
4. **DOC-DESIGN** — dokumentacja techniczna (TDD + ADR).
5. **DOC-BIZ** — dokumentacja biznesowa/inwestorska (Executive Summary, Business Case, Feasibility, Grant pack).
6. **QA** — test cases, test summary, performance report.
7. **RELEASE** — release checklist, changelog/release notes, release plan.
8. **OPS** — runbook, deployment guide, monitoring spec, SLO/SLI.
9. **GOV** — approval/sign-off, change request, risk register (aktualizacja).
10. **EVID** — dowód: arkusz, raport audytu, log z CI (załącznik w `evidence/`).

> Jeśli output nie pasuje do żadnego typu, istnieje ryzyko „informacji dla informacji”. W takim przypadku należy doprecyzować zakres albo przeredagować element backlogu tak, aby miał mierzalny rezultat.

---

## 3) Szablon pliku (do skopiowania)

Skopiuj poniższy blok jako `docs/<project>/sprints/SXX/sprint-output-contract.md`:

```markdown
---
id: "SPRINT-OUT-SXX"
title: "Sprint Output Contract — SXX"
project: "NAZWA_PROJEKTU"
owner: "Delivery Lead"
status: "draft"                 # draft|approved|closed
version: "0.1"
period: "YYYY-MM-DD..YYYY-MM-DD"
related:
  - "SPRINT-PLAN-SXX"
  - "SPRINT-BACKLOG-SXX"
  - "SPRINT-DOR-SXX"
  - "SPRINT-DOD-SXX"
---

# Sprint Output Contract — SXX

## 1. Sprint Goal
- (jedno zdanie)

## 2. Reguła obowiązkowa
Każdy element sprintu musi mieć zdefiniowane:
- **output_type** (CODE/INFRA/DOC-REQ/DOC-DESIGN/DOC-BIZ/QA/RELEASE/OPS/GOV/EVID)
- **output_location** (konkretny path lub link)
- **verification** (jak udowodnimy, że output istnieje i jest poprawny)
- **owner** (osoba odpowiedzialna)

## 3. Backlog z deklaracją output

| Item ID | Title | Owner | Estimate | Output type | Output location | Verification | Gate impact |
|---|---|---|---:|---|---|---|---|
| SXX-001 | ... | ... | 3 | CODE | PR: <link> | CI green + review approved | Release readiness |
| SXX-002 | ... | ... | 2 | DOC-REQ | docs/<client>/PRD.md | DoD(PRD) met + approval | Requirements freeze |
| SXX-003 | ... | ... | 1 | OPS | docs/runbook.md | ops checklist passed | Ops handover |

## 4. Wymagania dowodowe (Evidence)
Jeśli output opiera się o dane zewnętrzne (finanse, audyt, rynek):
- evidence file: `docs/<project>/sprints/SXX/evidence/<name>`
- opis: co udowadnia i gdzie jest użyte

## 5. Zależności i blokery
- Dependency A → wpływa na item SXX-002
- Blocker B → wymaga eskalacji (IMP-001)

## 6. Akceptacja kontraktu (gates)
- **Approved by:** ...
- **Date:** ...
- **Notes:** ...

---

## Appendix A — definicje Verification (przykłady)
- CODE: PR merged + CI green + reviewer approved
- DOC: plik `.md` w repo + review + approval record
- QA: raport testów w `qa/` + link w sprint-review
- OPS: runbook updated + monitoring spec + dry-run
```

---

## 4) Przykład wypełniony (instancja sprintu)

Poniższy przykład pokazuje sprint nastawiony na **dowożenie dokumentacji inwestorskiej + fundamentów produktu**. Skopiuj i zmień nazwy projektu/klienta.

```markdown
---
id: "SPRINT-OUT-S26"
title: "Sprint Output Contract — S26"
project: "CLIENT_ALPHA"
owner: "Delivery Lead"
status: "approved"
version: "1.0"
period: "2025-12-29..2026-01-11"
related:
  - "SPRINT-PLAN-S26"
  - "SPRINT-BACKLOG-S26"
  - "SPRINT-DOR-S26"
  - "SPRINT-DOD-S26"
---

# Sprint Output Contract — S26

## 1. Sprint Goal
- Dostarczyć pakiet inwestorski v1 (Executive Summary + Business Case + Financials) oraz PRD v0.3 gotowe do review i podpisu.

## 2. Backlog z deklaracją output

| Item ID | Title | Owner | Estimate | Output type | Output location | Verification | Gate impact |
|---|---|---|---:|---|---|---|---|
| S26-001 | Executive Summary v1 | BizDev Lead | 1 | DOC-BIZ | docs/client_alpha/investor/Executive_Summary.md | Review + APPROVAL-EXSUM-001 | Go/No-Go |
| S26-002 | Business Case v1 | CFO/Fin Lead | 3 | DOC-BIZ | docs/client_alpha/investor/Business_Case.md | Review + APPROVAL-BUSCASE-001 | Go/No-Go |
| S26-003 | Financial Model (xlsx) | Finance Analyst | 2 | EVID | docs/client_alpha/investor/evidence/financial_model_v1.xlsx | Hash + link in Business Case | Go/No-Go |
| S26-004 | Market sources pack | Research Lead | 1 | EVID | docs/client_alpha/investor/evidence/market_sources.md | Sources list complete | Go/No-Go |
| S26-005 | PRD v0.3 (MVP scope) | Product Owner | 3 | DOC-REQ | docs/client_alpha/product/PRD.md | DoD(PRD) + APPROVAL-PRD-001 | Requirements freeze |
| S26-006 | RTM draft (MVP) | QA Lead | 2 | QA | docs/client_alpha/product/rtm.csv | RTM covers all PRD P0 | Requirements freeze |
| S26-007 | Approval pack (sign-offs) | PM | 1 | GOV | docs/client_alpha/approvals/ | Approvals present for P0 docs | Go/No-Go |

## 3. Wymagania dowodowe (Evidence)
- docs/client_alpha/investor/evidence/financial_model_v1.xlsx — model finansowy wykorzystywany w Business Case.
- docs/client_alpha/investor/evidence/market_sources.md — źródła dla TAM/SAM/SOM.

## 4. Zależności i blokery
- Dependency: dane finansowe od klienta → wpływa na S26-002.
- Blocker: brak potwierdzenia cen (pricing) → eskalacja do stakeholdera.

## 5. Akceptacja kontraktu (gates)
- **Approved by:** Sponsor / CPO
- **Date:** 2026-01-11
- **Notes:** Zatwierdzono pakiet inwestorski v1 do złożenia wniosku grantowego.
```

---

## 5) Integracja z DoR i DoD sprintu

### Sprint DoR powinien wymagać

- każdy item ma `output_type`, `output_location`, `verification`, `owner`,
- zależności są jawne i mają ownera,
- dla dokumentów P0 istnieje plan review i plan approval.

### Sprint DoD powinien wymagać

- każdy output istnieje w zadeklarowanym miejscu,
- `verification` jest wykonane (dowód: link/artefakt/approval),
- `sprint-review.md` zawiera linki do wszystkich outputów.

---

## 6) Minimalna checklista (planowanie sprintu)

**Cel:** zanim element trafi do sprintu, ma mieć jednoznacznie określony rezultat (output) oraz sposób weryfikacji. To eliminuje pracę „dla informacji”.

## Obowiązkowe

- Każdy item ma `output_type`.
- Każdy item ma `output_location` (path/link).
- Każdy item ma `verification` (jakim dowodem potwierdzamy ukończenie: PR/CI, approval, raport QA, link do pliku).
- Każdy item ma ownera (osobę odpowiedzialną).
- Każdy item ma określony wpływ na gate (`Gate impact`: Go/No-Go, Requirements freeze, Release readiness, Ops handover).
- Zależności są jawne (ID/link) i mają ownera (jeśli blokują — wpis do impediments).
- Itemy bez output: usunąć albo doprecyzować tak, aby miały mierzalny rezultat.

### Dodatkowe (gdy sprint obejmuje release / compliance)

- Dla outputów typu DOC (PRD/TDD/Biz) jest wskazany plan review + plan approval (kto zatwierdza).
- Dla outputów typu EVID jest wskazany plik w `evidence/` + opis „co udowadnia i gdzie jest użyty”.
- Jeżeli sprint zmienia zakres (scope), z góry przygotowany jest mechanizm CR (`sprint-scope-change.md`).

---

## 7) Rekomendowana lokalizacja w repo

- Szablon: `templates/sprints/sprint-output-contract.md`
- Instancja: `docs/<project>/sprints/SXX/sprint-output-contract.md`
- Dowody: `docs/<project>/sprints/SXX/evidence/`

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: SPRINT-PLAN-*
    type: requires
    reason: "Sprint Output Contract requires sprint plan to define output expectations"
    conditions:
      - when: "project.methodology === 'agile'"
        applies: true
      - when: "project.size < 'small'"
        applies: false
    sections:
      - from: "Sprint Plan §1 Sprint Goal"
        to: "§1 Sprint Goal"
        influence: "Sprint goal defines what outputs are needed to achieve success"
      - from: "Sprint Plan §2 Zakres"
        to: "§3 Backlog z deklaracją output"
        influence: "Scope defines items requiring output declaration"

  - id: SPRINT-BACKLOG-*
    type: requires
    reason: "Backlog items need output type, location, and verification defined in contract"
    sections:
      - from: "Sprint Backlog §1 Lista itemów"
        to: "§3 Backlog z deklaracją output"
        influence: "Each backlog item must have output_type, output_location, verification"

  - id: SPRINT-DOR-*
    type: requires
    reason: "DoR ensures items entering sprint have defined outputs"
    sections:
      - from: "Sprint DoR §1 Kryteria wejścia"
        to: "§2 Reguła obowiązkowa"
        influence: "DoR validates that items have output declarations before sprint entry"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: SPRINT-DOD-*
    type: blocks
    reason: "Sprint DoD cannot be satisfied without verifiable outputs from contract"
    conditions:
      - when: "sprint.has_deliverables === true"
        applies: true
    sections:
      - from: "§3 Backlog z deklaracją output"
        to: "Sprint DoD §1 Kryteria wyjścia"
        influence: "Output verification criteria define DoD completion requirements"

  - id: SPRINT-REVIEW-*
    type: blocks
    reason: "Sprint review requires concrete outputs to demonstrate progress"
    sections:
      - from: "§3 Backlog z deklaracją output"
        to: "Sprint Review §2 Delivered"
        influence: "Output locations provide links to deliverables for review"

  - id: DOC-*
    type: informs
    reason: "Contract output declarations generate documentation artifacts"
    conditions:
      - when: "output_type IN ['DOC-REQ', 'DOC-DESIGN', 'DOC-BIZ']"
        applies: true
    sections:
      - from: "§3 Backlog z deklaracją output"
        to: "Various Document §All"
        influence: "DOC output types create PRD, TDD, Business Case artifacts"

  - id: CODE-*
    type: informs
    reason: "Contract CODE outputs drive implementation artifacts"
    conditions:
      - when: "output_type === 'CODE'"
        applies: true
    sections:
      - from: "§3 Backlog z deklaracją output"
        to: "Repository PRs"
        influence: "CODE outputs define PR locations and verification criteria"
```

### Related Documents

```yaml
related:
  - id: SPRINT-IMPEDIMENTS-*
    type: informs
    reason: "Impediments blocking outputs are tracked and escalated"

  - id: EVIDENCE-*
    type: informs
    reason: "Evidence files support output verification claims"

  - id: APPROVAL-*
    type: informs
    reason: "Approvals validate contract fulfillment at gates"
```

### Satellite Documents

```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SPRINT-OUT-*.md"
    required: true
    purpose: "External data and proof supporting output claims"

  - type: TODO
    path: "satellites/todos/TODO-SPRINT-OUT-*.md"
    required: false
    purpose: "Action items for completing contract outputs"

  - type: DoD
    path: "satellites/dod/DOD-SPRINT-OUT-*.md"
    required: true
    purpose: "Definition of Done per output type"
```
