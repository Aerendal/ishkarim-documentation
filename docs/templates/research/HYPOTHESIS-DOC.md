# HYPOTHESIS-DOC: [Project Name] - [Short Hypothesis Description]

---

## Document Metadata

```yaml
id: HYPOTHESIS-[XXX]
doctype: HYPOTHESIS-DOC
status: draft  # draft | in-review | approved | rejected | validated | invalidated
version: 1.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: [Owner Name]
project: [Project Name]
hypothesis_type: [technical | business | ux | research]
```

---

## Cross-References

```yaml
dependencies:
  - id: PRODUCT-BACKLOG
    type: research_input
    reason: "Unknowns z backlogu generują hipotezy do zbadania"
  - id: INNOVATION-ROADMAP
    type: strategic_alignment
    reason: "Hipotezy są aligned ze strategicznymi priorytetami innowacji"

impacts:
  - id: EXPERIMENT-LOG
    type: blocks
    reason: "Eksperyment nie może się rozpocząć bez zdefiniowanej hipotezy"
  - id: ADR
    type: influences
    reason: "Zwalidowane hipotezy informują decyzje architektoniczne"
```

---

## SEC-HYP-CONTEXT: Kontekst i motywacja

### Problem do rozwiązania
[Opisz problem lub pytanie biznesowe/techniczne, które prowadzi do sformułowania hipotezy]

### Dlaczego teraz
[Uzasadnienie, dlaczego ta hipoteza jest ważna w obecnym momencie projektu]

### Background
[Dodatkowy kontekst, poprzednie badania, znane fakty]

---

## SEC-HYP-STATEMENT: Stwierdzenie hipotezy (H0/H1)

### Hipoteza zerowa (H0)
[Stwierdzenie hipotezy zerowej - status quo lub przeciwieństwo tego, co chcesz udowodnić]

### Hipoteza alternatywna (H1)
[Stwierdzenie hipotezy alternatywnej - to, co chcesz zwalidować]

### Scope
**W zakresie:**
- [Element 1 w zakresie]
- [Element 2 w zakresie]

**Poza zakresem:**
- [Element 1 poza zakresem]
- [Element 2 poza zakresem]

---

## SEC-HYP-ASSUMPTIONS: Założenia

### Założenia techniczne
- [Założenie 1]
- [Założenie 2]

### Założenia biznesowe
- [Założenie 1]
- [Założenie 2]

### Założenia dotyczące zasobów
- [Założenie 1]
- [Założenie 2]

### Ograniczenia
- [Ograniczenie 1]
- [Ograniczenie 2]

---

## SEC-HYP-SUCCESS-CRITERIA: Kryteria sukcesu/porażki

### Kryteria sukcesu (walidacja H1)
- [ ] [Kryterium 1 - konkretne, mierzalne]
- [ ] [Kryterium 2 - konkretne, mierzalne]
- [ ] [Kryterium 3 - konkretne, mierzalne]

### Kryteria porażki (odrzucenie H1)
- [ ] [Kryterium 1 - konkretne, mierzalne]
- [ ] [Kryterium 2 - konkretne, mierzalne]

### Metryki
| Metryka | Baseline (obecny) | Target (oczekiwany) | Measurement method |
|---------|------------------|---------------------|-------------------|
| [Metryka 1] | [Wartość] | [Wartość] | [Metoda pomiaru] |
| [Metryka 2] | [Wartość] | [Wartość] | [Metoda pomiaru] |

---

## SEC-HYP-METHODOLOGY: Metodologia walidacji

### Podejście
[Opisz, jak będziesz testować hipotezę - eksperyment, PoC, spike, A/B testing, itp.]

### Procedura
1. [Krok 1]
2. [Krok 2]
3. [Krok 3]

### Narzędzia i technologie
- [Narzędzie 1]
- [Narzędzie 2]

### Środowisko testowe
[Opis środowiska, w którym będzie przeprowadzany eksperyment]

---

## SEC-HYP-RESOURCES: Wymagane zasoby

### Zespół
- [Rola 1]: [Liczba osób] - [Zadania]
- [Rola 2]: [Liczba osób] - [Zadania]

### Infrastruktura
- [Zasób 1]
- [Zasób 2]

### Budget
- [Item 1]: [Koszt]
- [Item 2]: [Koszt]
- **Total:** [Suma]

---

## SEC-HYP-TIMELINE: Timeboxing

### Harmonogram
- **Start date:** YYYY-MM-DD
- **End date:** YYYY-MM-DD
- **Duration:** [X dni/tygodni]

### Milestones
- [ ] [Milestone 1] - [Data]
- [ ] [Milestone 2] - [Data]
- [ ] [Final validation] - [Data]

### Timebox constraint
[Uzasadnienie wybranego timeboxu - dlaczego X dni/tygodni]

---

## TODO_SECTION: Zadania do wykonania

### Do zrobienia
- [ ] [Zadanie 1]
- [ ] [Zadanie 2]
- [ ] [Zadanie 3]

### W trakcie
- [Zadanie obecnie realizowane]

### Zrealizowane
- [x] [Zadanie zakończone 1]
- [x] [Zadanie zakończone 2]

---

## EVIDENCE: Dowody i dane wspierające

### Wstępne badania
[Linki do dokumentów, artykułów, danych rynkowych, itp.]

### Poprzednie eksperymenty
[Odniesienia do wcześniejszych prób, jeśli istnieją]

### Data sources
- [Źródło 1]
- [Źródło 2]

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| YYYY-MM-DD | 1.0 | [Imię Nazwisko] | Initial creation |
|  |  |  |  |

---

## Notatki i uwagi

[Miejsce na dodatkowe notatki, obserwacje, pytania]

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** innovation
