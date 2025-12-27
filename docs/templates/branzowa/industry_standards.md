# Dokumentacje branżowe

## Ogólny opis tematu
Rozszerzenie katalogu dokumentacji o standardy i dokumenty specyficzne dla różnych branż: medycyna (HIPAA, MDR), finanse (PCI DSS, SOX, Basel III), administracja publiczna (GDPR, eIDAS) oraz obronność (STANAG, cyber defense).

---

## Pair 37 (messages 73+74)

### User zapytał
> a dodatkowych nowych jakie jeszcze nie zostały wymienione są?

### Assistant wykonał
- Stwierdziła, że obecna lista obejmuje już wszystkie typy dokumentacji stosowane w projektach enterprise
- Zaproponowała dodanie dokumentów w kontekście **branżowym**:
  - HIPAA (dla medycyny)
  - PCI DSS (dla finansów)
  - Normy militarne

### Assistant zaproponował
> Chcesz, żebym przygotował wariant branżowy katalogu dokumentacji (np. dla medycyny, finansów, administracji publicznej)?

---

## Pair 38 (messages 75+76)

### User zapytał
> a dodaj, może nie będzie potrzeba

### Assistant wykonał
- Dodała sekcję **branżową** obejmującą dokumentację specyficzną dla:
  - **Medycyna**: HIPAA, MDR
  - **Finanse**: PCI DSS, SOX, Basel III
  - **Administracja**: GDPR, eIDAS
  - **Obronność**: STANAG, cyber defense

### Assistant zaproponował
> Chcesz, żebym rozpisał te branżowe dokumenty tak samo szczegółowo jak resztę?

---

## Pair 39 (messages 77+78)

### User zapytał
> tak

### Assistant wykonał
- Rozwinęła sekcję **branżową**
- Każdy dokument (HIPAA, PCI DSS, GDPR, STANAG itd.) ma teraz pełny opis:
  - Cel
  - Zawartość
  - Czego nie zawiera
  - Objętość
  - Odbiorcy

### Assistant zaproponował
> Chcesz, żebym przygotował do tego również spis treści (TOC) w formie hierarchicznej listy dla całego zestawu dokumentacji?

---

## Pair 40 (messages 79+80)

### User zapytał
> rozpisz mi jeszcze te dokumentacje branżowe

### Assistant wykonał
- Rozwinęła dokumentacje branżowe
- Każda (HIPAA, PCI DSS, GDPR, STANAG itd.) ma teraz pełne sekcje:
  - Cel
  - Zawartość
  - Czego nie zawiera
  - Objętość
  - Kategoria
  - Odbiorcy

### Assistant zaproponował
> Chcesz, żebym przygotował teraz hierarchiczny spis treści (TOC) obejmujący wszystkie dokumenty (przedprodukcyjne, produkcyjne i branżowe)?

---

## Document Cross-References

### Dependencies (Required Inputs)
- **External Industry Standards** (ISO, IEEE, regulatory frameworks)
  - Type: `references` | Reason: Industry standards document references external compliance requirements
- **[Doc Types Spec]** `../specs/specs_doc_types.md`
  - Type: `informs` | Reason: Industry standards may influence required sections in doc types

### Impacts (Downstream Documents)
- **ALL Domain-Specific Templates** `../examples/*-*-example.md`
  - Type: `informs` | Reason: Industry standards guide compliance requirements for domain-specific documents | Cascade: `false` (advisory only)
- **[Gates Spec]** `../specs/specs_gates.md`
  - Type: `informs` | Reason: Industry compliance may define gate requirements | Example: ISO 27001 audit gates

### Related Documents
- **[Specs]** `../specs/*.md` - Core system specifications
- **[Examples]** `../examples/*.md` - Domain-specific implementations
- **External Standards Documents** - ISO, IEEE, FDA, NIST, etc.

### Satellite Documents
- **[Compliance Checklist]** `satellites/COMPLIANCE-CHECKLIST-{{STANDARD}}.md` - Per-standard compliance tracking
- **[Audit Records]** `satellites/AUDIT-{{STANDARD}}-{{YEAR}}.md` - Annual compliance audits

### Conditional Cross-References
```yaml
when industry === 'healthcare':
  require_dependencies: [HIPAA compliance framework, FDA 21 CFR Part 11 (if software), ISO 13485 (medical devices)]
  require_satellites: [HIPAA Compliance Checklist, Privacy Impact Assessment]

when industry === 'finance':
  require_dependencies: [SOX compliance, PCI-DSS (if payment data), GDPR (if EU customers)]
  require_satellites: [SOX Controls Matrix, Financial Audit Records]

when industry === 'aerospace':
  require_dependencies: [DO-178C (software), AS9100 (quality), ITAR (export control)]
  require_satellites: [AS9100 Audit Records, ITAR Compliance Log]

when industry === 'pharmaceuticals':
  require_dependencies: [GxP (Good Practice), 21 CFR Part 11, ISO 17025 (testing labs)]
  require_satellites: [GxP Compliance Checklist, Validation Master Plan]

when data_privacy_required === true:
  require_dependencies: [GDPR (EU), CCPA (California), Privacy Shield framework]
  require_satellites: [Data Privacy Impact Assessment, Consent Management Records]
```

### Validation Rules
- [ ] All cited standards include version/year (e.g., ISO 27001:2013)
- [ ] Compliance requirements mapped to document types
- [ ] Audit schedule defined for applicable standards
- [ ] Responsible parties assigned for compliance maintenance
- [ ] Gap analysis completed for new standards (within 90 days of identification)
