> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

```yaml
version: 1

# Kody błędów i ich domyślne zachowanie.
# "todo_action" steruje automatyzacją:
# - TODO: generuj pojedyncze TODO (root cause)
# - BATCH_TODO: grupuj w jeden TODO (np. Warnings)
# - RFC: generuj propozycję/decision request (sprzeczności)
# - NONE: nie generuj (np. agregaty typu gate blocked)
# - SECURITY_INCIDENT: osobna ścieżka (nie ujawniać wrażliwych danych w treści TODO)

codes:

  E100:
    title: "Missing file"
    severity_default: BLOCKER
    todo_action: TODO
    message_template: "Brak wymaganego pliku dokumentu: {required_path_or_id}."
    remediation_template: "Utwórz plik {required_path_or_id} na bazie szablonu typu {doctype} i uzupełnij wymagane sekcje."

  E110:
    title: "Missing required section"
    severity_default: BLOCKER
    todo_action: TODO
    message_template: "Brak wymaganej sekcji '{section_title}' ({section_id}) w {doc_id}."
    remediation_template: "Dodaj sekcję '{section_title}' w {doc_id} zgodnie z szablonem. Uzupełnij treść (bez placeholderów) i dodaj evidence, jeśli wymagane."

  E120:
    title: "Placeholder present"
    severity_default: ERROR
    todo_action: TODO
    message_template: "W sekcji '{section_title}' w {doc_id} wykryto placeholder: {token}."
    remediation_template: "Zastąp placeholder realną treścią albo przenieś brak do 'Open questions/Assumptions'."

  E130:
    title: "Missing evidence"
    severity_default: ERROR
    todo_action: TODO
    message_template: "Brak evidence dla tezy/parametru: {claim_key} w {doc_id}."
    remediation_template: "Dodaj plik dowodowy do evidence/ oraz wpis do evidence-index: co udowadnia i gdzie jest użyty."

  E140:
    title: "Missing dependency link"
    severity_default: ERROR
    todo_action: TODO
    message_template: "Brak wymaganej zależności '{required_doctype}' w polu related/requires dokumentu {doc_id}."
    remediation_template: "Uzupełnij front-matter (requires/related) w {doc_id} i dodaj brakujący dokument, jeśli nie istnieje."

  E150:
    title: "Gate blocked (aggregate)"
    severity_default: BLOCKER
    todo_action: NONE
    message_template: "Gate {gate_id} jest zablokowany przez {n_root_causes} przyczyn(y)."
    remediation_template: "Napraw root-cause błędy (E100/E110/E120/E130/E160/E200)."

  E160:
    title: "Missing approval/sign-off"
    severity_default: BLOCKER
    todo_action: TODO
    message_template: "Brak wymaganego zatwierdzenia (approval) dla {doc_id} (wymaga: {approver_role})."
    remediation_template: "Utwórz/uzupełnij approval record (APPROVAL-*) i ustaw status dokumentu zgodnie z procesem."

  E200:
    title: "Contradiction / conflicting facts"
    severity_default: BLOCKER
    todo_action: RFC
    message_template: "Sprzeczność faktów: {fact_key} ma różne wartości w {doc_a} i {doc_b}."
    remediation_template: "Ustal źródło prawdy (facts.yaml), zaktualizuj dokumenty oraz dodaj decyzję (RFC/Decision) + approval."

  E210:
    title: "ID collision"
    severity_default: ERROR
    todo_action: TODO
    message_template: "Duplikat ID: {id} (w {doc_a} i {doc_b})."
    remediation_template: "Nadaj nowe, unikalne ID zgodnie z konwencją i zaktualizuj powiązania (related)."

  W310:
    title: "Recommended section missing"
    severity_default: WARN
    todo_action: BATCH_TODO
    message_template: "Brak zalecanej sekcji '{section_title}' w {doc_id}."
    remediation_template: "Rozważ dodanie sekcji, jeśli zwiększa czytelność i wartość dokumentu."

  S900:
    title: "Secret/PII detected"
    severity_default: BLOCKER
    todo_action: SECURITY_INCIDENT
    message_template: "Wykryto potencjalne dane wrażliwe w {doc_id} (nie ujawniać treści w raporcie)."
    remediation_template: "Usuń dane wrażliwe, przenieś do bezpiecznego vaulta, przeprowadź rotację sekretów (jeśli dotyczy) i dodaj wpis incident."

# Uwaga praktyczna:
# - E150 jest agregatem → nie generuje TODO.
# - E200 generuje RFC/Decision, nie TODO.
# - Warnings grupujemy (BATCH_TODO), żeby nie spamować backlogu.
```

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Doc Types Spec]** `specs_doc_types.md`
  - Type: `requires`
  - Reason: Error messages reference doc types and sections

- **[Gates Spec]** `specs_gates.md`
  - Type: `requires`
  - Reason: E150 (Gate blocked) references gate definitions

### Impacts (Downstream Documents)
- **Validation System** `scripts/validate_documents.py`
  - Type: `defines`
  - Reason: Validation script uses these error codes for reporting
  - Cascade: `true`

### Related Documents
- **[Doc Types Spec]** `specs_doc_types.md`
- **[Gates Spec]** `specs_gates.md`
- **[Satellites Spec]** `satelitarne_artefakty_dokumentacyjne_kanwa_opisowa.md`

### Satellite Documents
- **[Changelog]** `satellites/CHANGELOG-ERRORS-SPEC-001.md`

### Validation Rules
- [ ] All error codes unique (E100, E110, E120, etc.)
- [ ] All codes have severity (BLOCKER, ERROR, WARN)
- [ ] All codes have todo_action (TODO, RFC, BATCH_TODO, NONE, SECURITY_INCIDENT)
- [ ] All message_templates use valid placeholders
- [ ] All remediation_templates actionable
