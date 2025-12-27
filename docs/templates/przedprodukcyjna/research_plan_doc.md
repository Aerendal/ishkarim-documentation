# 📄 Research Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: ROADMAP-*
    type: requires
    reason: "Innovation Roadmap definiuje innovation areas wymagające research"
    conditions:
      - when: "project.has_research_component === true"
        applies: true
    sections:
      - from: "Innovation Roadmap §12 Technologie do zbadania"
        to: "§11 Pytania badawcze"
        influence: "Technology exploration areas definiują research questions"
      - from: "Innovation Roadmap §14 Propozycje eksperymentów"
        to: "§13 Metodologia (narzędzia, techniki)"
        influence: "Experiment proposals są formalized w research methodology"

  - id: ETHICS-AI-GUIDELINES-*
    type: requires
    reason: "Ethics & AI Guidelines definiują ethical framework dla AI research"
    conditions:
      - when: "research.involves_ai === true"
        applies: true
    sections:
      - from: "Ethics AI Guidelines §15 Procedury audytów etycznych"
        to: "§16 Kryteria oceny wyników"
        influence: "Ethical audit procedures są embedded w research evaluation"

  - id: INNOVATION-LOG-*
    type: influences
    reason: "Innovation Log ideas może inspire research questions"
    sections:
      - from: "Innovation Log §11 Lista pomysłów i innowacji"
        to: "§11 Pytania badawcze"
        influence: "Innovation ideas wymagające validation są converted do research questions"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: INNOVATION-LOG-*
    type: informs
    reason: "Research Plan experiment results są logged w Innovation Log"
    sections:
      - from: "§16 Kryteria oceny wyników"
        to: "Innovation Log §15 Wnioski i rekomendacje"
        influence: "Research findings informują innovation recommendations"

  - id: ROADMAP-*
    type: influences
    reason: "Research Plan findings mogą evolve Innovation Roadmap"
    sections:
      - from: "§15 Harmonogram eksperymentów"
        to: "Innovation Roadmap §15 Orientacyjny harmonogram eksploracji"
        influence: "Research timeline wpływa na innovation exploration planning"

  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Research Plan może identify feasibility concerns wymagające assessment"
    sections:
      - from: "§16 Kryteria oceny wyników"
        to: "Feasibility Study §6 Technical Risks"
        influence: "Research validation failures reveal feasibility risks"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: MARKET-ANALYSIS-*
    type: informs
    reason: "Research może include market validation research"

  - id: TRAINING-PLAN-*
    type: informs
    reason: "Research tools i methodologies mogą wymagać team training"

  - id: FINANCIAL-PLAN-*
    type: informs
    reason: "Research budget allocation wpływa na R&D investment planning"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RESEARCH-*.md"
    required: false
    purpose: "Tracking research tasks, experiment execution, data collection"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RESEARCH-*.md"
    required: true
    purpose: "Experiment results, research data, literature reviews, validation reports"

  - type: DoR
    path: "satellites/dor/DOR-RESEARCH-*.md"
    required: true
    purpose: "Definition of Ready: research questions defined, methodology designed, ethics approved before research execution"

  - type: DoD
    path: "satellites/dod/DOD-RESEARCH-*.md"
    required: true
    purpose: "Definition of Done: experiments completed, results analyzed, conclusions documented, findings validated"
```

---

## Cel biznesowy / techniczny
Research Plan określa zakres, metodologię i harmonogram działań badawczo‑rozwojowych związanych z projektem. Dokument ten służy do planowania eksperymentów i pozyskiwania danych, które wspierają rozwój produktu.

## Zawartość
- Pytania badawcze
- Cele badawcze i hipotezy
- Metodologia (narzędzia, techniki)
- Źródła i dane wejściowe
- Harmonogram eksperymentów
- Kryteria oceny wyników

## Czego nie zawiera
- Kodów źródłowych
- Wewnętrznych backlogów sprintowych
- Detali implementacyjnych

## Objętość
- 3–5 stron
- 6–10 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Zespół badawczo‑rozwojowy
- Inwestorzy (przy projektach innowacyjnych)
- Project managerowie
