# 📄 Executive Summary

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: VISION-*
    type: requires
    reason: "Vision Document definiuje długoterminową wizję destylowaną w Executive Summary"
    sections:
      - from: "Vision §16 Wizja pozycji rynkowej"
        to: "§15 Nasze rozwiązanie i przewaga konkurencyjna"
        influence: "Pozycja rynkowa definiuje value proposition"

  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case dostarcza uzasadnienia ROI i korzyści biznesowych"
    sections:
      - from: "Business Case §17 Plan osiągnięcia ROI"
        to: "§17 Model biznesowy i szacowane przychody"
        influence: "Plan ROI definiuje model przychodów"

  - id: MARKET-ANALYSIS-*
    type: requires
    reason: "Market Analysis dostarcza danych o wielkości i potencjale rynku"
    sections:
      - from: "Market Analysis §12 Wielkość rynku (TAM, SAM, SOM)"
        to: "§16 Wielkość i potencjał rynku"
        influence: "Dane rynkowe definiują skalowalność biznesu"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PITCH-DECK-*
    type: blocks
    reason: "Pitch Deck wizualizuje kluczowe punkty z Executive Summary"
    sections:
      - from: "§14 Problem, który rozwiązujemy"
        to: "Pitch Deck §2 Problem Statement"
        influence: "Problem z Executive Summary jest core slide w Pitch Deck"

  - id: PROJECT-CHARTER-*
    type: informs
    reason: "Project Charter rozwija cele i zakres zasygnalizowane w Executive Summary"
    sections:
      - from: "§15 Nasze rozwiązanie i przewaga konkurencyjna"
        to: "Project Charter §13 Zakres wysokopoziomowy"
        influence: "Rozwiązanie definiuje zakres projektu"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: COMMUNICATION-PLAN-*
    type: informs
    reason: "Communication Plan używa Executive Summary jako baseline messaging dla stakeholders"

  - id: GO-TO-MARKET-*
    type: informs
    reason: "Go-to-Market strategy opiera się na value proposition z Executive Summary"

  - id: STAKEHOLDER-MAP-*
    type: informs
    reason: "Stakeholder Map identyfikuje odbiorców Executive Summary"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-EXEC-SUMMARY-*.md"
    required: false
    purpose: "Tracking refinement tasks for messaging clarity"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-EXEC-SUMMARY-*.md"
    required: false
    purpose: "Supporting data for claims (market size, competitive advantage)"

  - type: Approval
    path: "satellites/approvals/APPROVAL-EXEC-SUMMARY-*.md"
    required: true
    purpose: "C-level and investor approval on messaging"
```

---

## Cel biznesowy / techniczny

Dokument służy do szybkiego zaprezentowania istoty projektu decydentom lub inwestorom. Jego celem jest przyciągnięcie uwagi i pokazanie wartości przedsięwzięcia bez wchodzenia w detale techniczne.

## Zawartość

### Opening Statement
Jeden mocny statement wyjaśniający czym jest projekt i dlaczego ma znaczenie (elevator pitch).

### Problem Statement
Jaki problem rozwiązujemy? Pain points, skala problemu, wpływ na rynek.

### Our Solution
Opis rozwiązania i jego kluczowych cech (unique value proposition).

### Competitive Advantage
Dlaczego jesteśmy lepsi od konkurencji? Co nas wyróżnia?

### Market Opportunity
Wielkość rynku (TAM, SAM, SOM), potencjał wzrostu, trendy rynkowe.

### Business Model
Jak zarabiamy pieniądze? Model przychodów, pricing strategy (high-level).

### Financial Highlights
Kluczowe liczby: szacowane przychody, ROI, break-even, funding requirements (jeśli applicable).

### Go-to-Market Strategy
Jak zdobędziemy rynek? Kanały dystrybucji, strategia wejścia (bardzo high-level).

### Team & Expertise
Dlaczego my? Kluczowe kompetencje zespołu, track record, advisors.

### Traction & Milestones
Co już osiągnęliśmy? Proof of concept, piloty, kluczowi klienci, partnerships.

### Success Metrics
Jak zmierzymy sukces? Top 3-5 KPIs.

### Investment Ask (jeśli applicable)
Ile potrzebujemy finansowania i na co zostanie przeznaczone?

### Next Steps & Timeline
Co następne? Kluczowe milestone'y w najbliższych 6-12 miesiącach.

## Czego nie zawiera

- Kodów źródłowych
- Szczegółowych backlogów sprintów
- Analizy linii kodu
- Nadmiarowych detali technicznych

## Objętość

- 2–4 strony
- 10–15 punktów kluczowych

## Kategoria

- **Wymagane** (przedprodukcyjne)

## Odbiorcy

- Inwestorzy
- Decydenci strategiczni
- Zarząd / management
