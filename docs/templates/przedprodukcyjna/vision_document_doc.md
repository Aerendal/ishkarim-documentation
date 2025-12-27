# 📄 Vision Document (Extended)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies: []
# Vision Document jest dokumentem inicjującym - nie ma wymaganych dependencies
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: BIZ-CASE-*
    type: blocks
    reason: "Business Case wymaga wizji strategicznej jako fundamentu dla uzasadnienia ROI"
    sections:
      - from: "§12 Długofalowa roadmapa rozwoju"
        to: "Business Case §17 Plan osiągnięcia ROI"
        influence: "Roadmapa definiuje timeline dla realizacji korzyści biznesowych"
      - from: "§15 Potencjalne innowacje i nowe funkcje"
        to: "Business Case §14 Uzasadnienie wyboru projektu"
        influence: "Innowacje uzasadniają competitive advantage"

  - id: EXEC-SUMMARY-*
    type: blocks
    reason: "Executive Summary destyluje Vision Document do kluczowych punktów dla decydentów"
    sections:
      - from: "§16 Wizja pozycji rynkowej"
        to: "Executive Summary §15 Nasze rozwiązanie i przewaga konkurencyjna"
        influence: "Pozycja rynkowa definiuje value proposition"

  - id: PROJECT-CHARTER-*
    type: blocks
    reason: "Project Charter formalizuje cele strategiczne z Vision Document"
    sections:
      - from: "§13 Strategiczne cele biznesowe"
        to: "Project Charter §12 Cele projektu"
        influence: "Cele strategiczne mapują się na cele projektowe"

  - id: ROADMAP-*
    type: blocks
    reason: "Innovation Roadmap szczegółowo rozbija timeline z Vision Document"
    sections:
      - from: "§14 Długofalowa roadmapa rozwoju"
        to: "Innovation Roadmap §3 Timeline i Milestones"
        influence: "Vision roadmap definiuje high-level phases dla szczegółowej roadmapy"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: MARKET-ANALYSIS-*
    type: informs
    reason: "Market Analysis dostarcza danych rynkowych wspierających wizję pozycjonowania"

  - id: INNOVATION-LOG-*
    type: informs
    reason: "Innovation Log dokumentuje emerging ideas wspierające przyszłe funkcje z Vision"

  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck wizualizuje kluczowe aspekty Vision Document dla inwestorów"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-VISION-*.md"
    required: false
    purpose: "Tracking action items per vision section"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-VISION-*.md"
    required: false
    purpose: "Market research and competitive analysis supporting vision claims"
```

---

## Cel biznesowy / techniczny
Vision Document określa długoterminową wizję rozwoju produktu i jego roli w rynku. Pomaga inwestorom i zespołowi zrozumieć strategiczny kierunek projektu na 2–3 lata.

## Zawartość
- Opis docelowego kształtu produktu
- Strategiczne cele biznesowe
- Długofalowa roadmapa rozwoju
- Potencjalne innowacje i nowe funkcje
- Wizja pozycji rynkowej
- Zarys wartości dla klientów i partnerów

## Czego nie zawiera
- Planów sprintów i backlogów
- Detali implementacyjnych
- Kodów źródłowych

## Objętość
- 4–5 stron
- 7–10 punktów kluczowych

## Kategoria
- **Nice-to-Have** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy długoterminowi
- Zarząd
- Zespół strategiczny
