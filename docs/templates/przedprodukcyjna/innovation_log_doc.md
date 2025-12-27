# 📄 Innovation Log

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: VISION-*
    type: influences
    reason: "Vision Document może inspirować innovation ideas logged w Innovation Log"
    conditions:
      - when: "project.encourages_innovation === true"
        applies: true
    sections:
      - from: "Vision §15 Potencjalne innowacje i nowe funkcje"
        to: "§11 Lista pomysłów i innowacji"
        influence: "Vision innovation ideas są logged jako starting point dla exploration"

  - id: RESEARCH-PLAN-*
    type: influences
    reason: "Research Plan experiments mogą generować innovation ideas"
    conditions:
      - when: "project.has_research_component === true"
        applies: true
    sections:
      - from: "Research Plan §4 Experiment Design"
        to: "§11 Lista pomysłów i innowacji"
        influence: "Research experiments outcomes są captured jako innovations"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: ROADMAP-*
    type: informs
    reason: "Innovation Log validated ideas mogą być promoted do Innovation Roadmap"
    conditions:
      - when: "innovation.status === 'validated'"
        applies: true
    sections:
      - from: "§14 Status (nowy, w trakcie, odrzucony, wdrożony)"
        to: "Innovation Roadmap §11 Obszary potencjalnych innowacji"
        influence: "Wdrożone innovations are incorporated w roadmap planning"
      - from: "§15 Wnioski i rekomendacje"
        to: "Innovation Roadmap §14 Propozycje eksperymentów"
        influence: "Innovation learnings inform future experiment proposals"

  - id: VISION-*
    type: influences
    reason: "Innovation Log learnings mogą wpłynąć na future vision updates"
    conditions:
      - when: "innovation.is_strategic === true"
        applies: true
    sections:
      - from: "§15 Wnioski i rekomendacje"
        to: "Vision §15 Potencjalne innowacje i nowe funkcje"
        influence: "Strategic innovations mogą evolve product vision"

  - id: RESEARCH-PLAN-*
    type: informs
    reason: "Innovation Log może identify research needs dla further exploration"
    sections:
      - from: "§14 Status (nowy, w trakcie, odrzucony, wdrożony)"
        to: "Research Plan §2 Research Questions"
        influence: "New innovation ideas wymagające research są converted do research questions"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: ETHICS-AI-GUIDELINES-*
    type: informs
    reason: "AI innovations w Innovation Log mogą wymagać ethical review"

  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Innovation ideas mogą trigger feasibility assessments"

  - id: MARKET-ANALYSIS-*
    type: informs
    reason: "Market trends mogą inspirować logged innovations"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-INNOVATION-LOG-*.md"
    required: false
    purpose: "Tracking follow-up actions dla innovation ideas (experiments, validation, implementation)"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-INNOVATION-LOG-*.md"
    required: false
    purpose: "Supporting documentation dla innovations: prototypes, experiment results, user feedback"

  - type: DoD
    path: "satellites/dod/DOD-INNOVATION-LOG-*.md"
    required: false
    purpose: "Definition of Done for innovation evaluation: tested, validated, decision made (implement/reject)"
```

---

## Cel biznesowy / techniczny
Innovation Log dokumentuje pomysły, eksperymenty i innowacyjne rozwiązania generowane w trakcie projektu. Umożliwia ich późniejszą analizę i wykorzystanie.

## Zawartość
- Lista pomysłów i innowacji
- Data i autor pomysłu
- Krótki opis
- Status (nowy, w trakcie, odrzucony, wdrożony)
- Wnioski i rekomendacje

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych planów implementacyjnych
- Prognoz finansowych

## Objętość
- Dokument ciągły (ciągle rozwijany)

## Kategoria
- **Nice-to-Have** (przedprodukcyjne)

## Odbiorcy
- Project managerowie
- Zespół badawczo-rozwojowy
- Zarząd
