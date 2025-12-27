# Pytania asystenta i propozycje dalszych działań

## Ogólny opis tematu
Meta-analiza sposobu pracy Assistant w projekcie dokumentacji. Pokazuje wzorce proaktywnych pytań i propozycji następnych kroków, które Assistant systematycznie oferowała użytkownikowi po każdym wykonanym zadaniu.

---

## Wzorce pytań i propozycji

### 1. Propozycje narzędzi i formatów

**Pair 1**: Propozycja tabelarycznego zestawienia (Excel/Markdown) dla łatwiejszego porównywania dokumentów

**Pair 2**: Propozycja pełnej tabeli porównawczej z kolumnami: Nazwa, Zawiera, Nie zawiera, Strony, Punkty, Kategoria

**Pair 3**: Propozycja rozwinięcia tabeli o cel biznesowy/techniczny każdego dokumentu

---

### 2. Pytania o zakres i kierunek pracy

**Pair 4**: Czy rozpisać każdy kolejny dokument z listy, czy najpierw tylko przedprodukcyjne?

**Pair 5**: Czy rozpisać przydatne przedprodukcyjne, czy przejść od razu do części produkcyjnej?

**Pair 7**: Czy przejść do produkcyjnych - wymaganych?

**Pair 8**: Czy przygotować produkcyjne - przydatne?

**Pair 9**: Czy rozpisać także produkcyjne - nice-to-have?

---

### 3. Proaktywne sugestie rozszerzenia

**Pair 11**: Sugestia dodania: Feasibility Study, Project Charter, Data Management Plan, Security Plan, Deployment Guide, UAT Plan, Postmortem Report

**Pair 14**: Propozycja dodania dokumentów zarządzania projektem (Project Management Plan, Communication Plan, etc.)

**Pair 17**: Sugestia dodania dokumentów testowania i zarządzania (Test Summary Report, RTM, ADR, Runbook, etc.)

**Pair 21**: Propozycja poszerzenia o DPIA, Ethics & AI Guidelines, Monitoring, Sustainability, etc.

**Pair 27**: Sugestia dodania zaawansowanych dokumentów enterprise (SIRP, Performance Test Report, Accessibility, API Docs, etc.)

**Pair 37**: Propozycja przygotowania wariantu branżowego dla medycyny, finansów, administracji publicznej

---

### 4. Regularnie powtarzane propozycje TOC

Assistant systematycznie, po każdym większym rozszerzeniu listy, proponowała utworzenie pełnego spisu treści:

- **Pair 13**: TOC dla dokumentacji przedprodukcyjnej i produkcyjnej
- **Pair 16**: TOC wszystkich dokumentów w jednej hierarchicznej liście
- **Pair 26**: TOC wszystkich dokumentów w formie hierarchicznej listy
- **Pair 34**: TOC wszystkich dokumentów w jednej hierarchicznej liście
- **Pair 39**: TOC w formie hierarchicznej listy dla całego zestawu
- **Pair 40**: Hierarchiczny TOC obejmujący wszystkie dokumenty (przedprodukcyjne, produkcyjne i branżowe)

---

### 5. Pytania weryfikacyjne

**Pair 11**: "Chcesz, żebym je od razu rozpisał w tej samej formie jak poprzednie?"

**Pair 12**: "Chcesz, żebym je także rozpisał jako osobne dokumenty?"

**Pair 15**: "Chcesz, żebym rozpisał je teraz jako osobne dokumenty?"

**Pair 35**: User pyta czy wszystko rozpisane - Assistant potwierdza i proponuje TOC

**Pair 36**: User pyta czy są jeszcze nowe - Assistant potwierdza kompletność katalogu

---

### 6. Pytania o dalsze rozpisywanie

Pattern powtarzający się wielokrotnie (pairs 19, 23, 25, 30, 31, 32, 33):
- "Chcesz, żebym od razu przygotował te pliki w pełnej formie?"
- "Chcesz, żebym od razu rozpisał te dokumenty?"
- "Chcesz, żebym od razu je wygenerował?"

---

## Obserwacje metodologiczne

### Proaktywność
Assistant **nigdy nie czekała** biernie na polecenie - zawsze kończyła odpowiedź konkretnym pytaniem lub propozycją następnego kroku.

### Systematyczność
Po każdym dodaniu nowych typów dokumentacji, Assistant:
1. Dodawała je do listy
2. Pytała czy rozpisać szczegółowo
3. Po rozpisaniu - proponowała TOC lub kolejne rozszerzenia

### Antycypacja potrzeb
Assistant wielokrotnie **proaktywnie sugerowała** nowe typy dokumentacji zanim User o nie zapytał (pairs 11, 14, 17, 21, 27, 37).

### Oferowanie struktury
Regularnie proponowała narzędzia nawigacyjne (TOC, tabele porównawcze) dla ułatwienia pracy z rosnącym katalogiem.

### Potwierdzanie kierunku
Po każdym User "tak" lub "rozpisz", Assistant **najpierw wykonywała zadanie**, a dopiero **potem** pytała o następny krok - nigdy nie blokowała progresu zbędnymi pytaniami wstępnymi.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: CONVERSATION-LOG-*
    type: requires
    reason: "Questions analysis requires conversation log to extract patterns"
    conditions:
      - when: "document.type === 'meta-analysis'"
        applies: true
    sections:
      - from: "Conversation Log §All pairs"
        to: "§1 Wzorce pytań"
        influence: "Conversation pairs define patterns of proactive questions"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: ASSISTANT-GUIDELINES-*
    type: informs
    reason: "Question patterns inform guidelines for proactive assistance"
    conditions:
      - when: "project.has_assistant_training === true"
        applies: true
    sections:
      - from: "§3 Proaktywne sugestie rozszerzenia"
        to: "Assistant Guidelines §1 Proactive behavior"
        influence: "Pattern analysis defines how to anticipate user needs"
      - from: "§5 Pytania weryfikacyjne"
        to: "Assistant Guidelines §2 Verification questions"
        influence: "Verification patterns ensure clarity before action"

  - id: WORKFLOW-DESIGN-*
    type: informs
    reason: "Work patterns inform workflow design and automation"
    sections:
      - from: "§6 Obserwacje metodologiczne"
        to: "Workflow Design §1 Iteration patterns"
        influence: "Systematic patterns guide workflow automation design"
```

### Related Documents

```yaml
related:
  - id: EXTENDING-NEW-TYPES-*
    type: informs
    reason: "Question patterns drove extension of documentation types"

  - id: VERIFICATION-TOC-*
    type: informs
    reason: "Verification questions led to TOC creation"

  - id: INITIALIZATION-STRUCTURE-*
    type: informs
    reason: "Initial questions established documentation structure"
```

### Satellite Documents

```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-QUESTIONS-*.md"
    required: false
    purpose: "Full conversation logs supporting pattern analysis"

  - type: TODO
    path: "satellites/todos/TODO-QUESTIONS-*.md"
    required: false
    purpose: "Track improvements to question patterns"
```
