# DECISION-LOG: Lightweight Decision Log

---
**Meta (WYMAGANE):**
```yaml
id: DECISION-LOG-[NNN]
doctype: DECISION-LOG
status: [draft/approved/implemented/superseded]
version: "1.0"
owner: "[Decision Owner Name]"
project: "[Project Name]"
decision_type: "[feature_prioritization/technical_choice/process_change/bug_triage/resource_allocation/other]"
decision_date: "YYYY-MM-DD"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [RELATED-DOC-ID]
    type: [influences/requires/blocks]
    reason: "[Why this dependency exists]"

impacts:
  - id: [IMPACTED-DOC-ID]
    type: [informs/influences/blocks]
    reason: "[How this impacts the related document]"
```

---

## SEC-DL-QUESTION: Pytanie decyzyjne

> **Cel:** Jednoznaczne sformułowanie pytania, na które odpowiada ta decyzja.

[Sformułuj pytanie decyzyjne w formie jasnego pytania. Np. "Czy zbudować Feature A czy Feature B w następnym sprincie?" lub "Którą bibliotekę wybrać do obsługi PDF: PyPDF2 czy ReportLab?"]

---

## SEC-DL-CONTEXT: Kontekst (1-2 zdania)

> **Cel:** Krótkie wyjaśnienie sytuacji i dlaczego decyzja jest potrzebna.

[Opisz kontekst w 1-2 zdaniach. Przykład: "Sprint 15 capacity: 40 story points. Both features są requested by customers."]

**Kluczowe ograniczenia:**
- [Ograniczenie 1, np. "Budget: max $5K"]
- [Ograniczenie 2, np. "Deadline: 2 tygodnie"]
- [Ograniczenie 3, jeśli dotyczy]

---

## SEC-DL-OPTIONS: Opcje rozważane

> **Cel:** Lista rozważanych opcji (minimum 2).

### Opcja 1: [Nazwa opcji]
**Opis:** [Krótki opis opcji]
**Kluczowe właściwości:**
- [Właściwość 1]
- [Właściwość 2]

### Opcja 2: [Nazwa opcji]
**Opis:** [Krótki opis opcji]
**Kluczowe właściwości:**
- [Właściwość 1]
- [Właściwość 2]

### Opcja 3: [Nazwa opcji, jeśli dotyczy]
**Opis:** [Krótki opis opcji]
**Kluczowe właściwości:**
- [Właściwość 1]
- [Właściwość 2]

---

## SEC-DL-DECISION: Decyzja

> **Cel:** Jasne stwierdzenie podjętej decyzji.

**Wybrana opcja:** [Numer i nazwa wybranej opcji]

[Opcjonalnie: krótkie podsumowanie wybranej opcji]

---

## SEC-DL-RATIONALE: Uzasadnienie (1-3 zdania)

> **Cel:** Zwięzłe wyjaśnienie dlaczego ta opcja została wybrana.

[Wyjaśnij dlaczego wybrano tę opcję w 1-3 zdaniach. Skup się na kluczowych czynnikach decydujących.]

**Kluczowe czynniki:**
- [Czynnik 1, np. "Customer demand jest 2x wyższy"]
- [Czynnik 2, np. "Niższy koszt implementacji"]
- [Czynnik 3, jeśli dotyczy]

**Opcje odrzucone i dlaczego:**
- **[Opcja X]:** [Krótkie wyjaśnienie dlaczego odrzucona]
- **[Opcja Y]:** [Krótkie wyjaśnienie dlaczego odrzucona]

---

## SEC-DL-OWNER: Decision owner

> **Cel:** Wskazanie osoby odpowiedzialnej za decyzję i ewentualnych współdecydentów.

**Decision owner:** [Imię/Rola osoby głównie odpowiedzialnej]

**Współdecydenci/Konsultanci:**
- [Osoba 1 - Rola] - [Typ zaangażowania: approved/consulted/informed]
- [Osoba 2 - Rola] - [Typ zaangażowania]

**Data zatwierdzenia:** [YYYY-MM-DD, jeśli formalne zatwierdzenie było wymagane]

---

## Notatki dodatkowe (opcjonalne)

### Następne kroki
- [ ] [Akcja 1 wynikająca z decyzji]
- [ ] [Akcja 2]

### Terminy review
- **Pierwszy review:** [Data, np. po 1 miesiącu od implementacji]
- **Kryteria sukcesu:** [Jak będziemy oceniać czy decyzja była prawidłowa]

### Powiązane decyzje
- [Link do powiązanej decyzji 1]
- [Link do powiązanej decyzji 2]

---

**Szacowany czas wypełnienia:** 5-10 minut

**Różnica vs ADR:**
- Czas wypełnienia: 5-10 min (ADR: 1-2h)
- Scope: Tactical/operational (ADR: Strategic/architectural)
- Detail level: Medium - quick rationale (ADR: High - detailed analysis)
- Stakeholders: Single decision owner (ADR: Multiple with formal approval)
- Lifecycle: Short-term sprint/quarter (ADR: Long-term years)

**Kiedy używać:**
- Small-to-medium decisions (nie strategic)
- Decisions które wymagają dokumentacji, ale ADR jest overkill
- Daily team decisions (sprint planning, feature prioritization, bug triage)
- Decisions gdzie kontekst może być zapomniany po tygodniu

**Kiedy NIE używać:**
- Strategic/architectural decisions → użyj ADR
- Complex decisions wymagające weighted scoring → użyj TRADE-OFF-ANALYSIS
- Vendor/tool selection z 3+ opcjami → użyj OPTION-COMPARISON-MATRIX
- Binary launch decisions → użyj GO-NO-GO-DECISION
