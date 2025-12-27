# 📄 eIDAS Compliance Documentation

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Zapewnia zgodność z regulacjami eIDAS dotyczącymi podpisu elektronicznego i identyfikacji cyfrowej w UE.

## Zawartość
- Procedury autoryzacji użytkowników
- Certyfikaty kwalifikowane
- Wyniki audytów bezpieczeństwa
- Dokumentacja procesów podpisu elektronicznego

## Czego nie zawiera
- Implementacji kodu
- Strategii biznesowych

## Objętość
- 3–6 stron
- Raporty + checklisty zgodności

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Regulatorzy
- Urzędy publiczne
- Zespoły IT odpowiedzialne za identyfikację cyfrową

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: SECURITY-ARCHITECTURE-*
    type: requires
    reason: "Architektura bezpieczeństwa definiuje infrastrukturę PKI i mechanizmy podpisu elektronicznego"
    conditions:
      - when: "project.requires_digital_signature === true"
        applies: true
      - when: "project.region === 'EU'"
        applies: true
    sections:
      - from: "Security Architecture §10 PKI Infrastructure"
        to: "§2 Certyfikaty kwalifikowane"
        influence: "Infrastruktura PKI zapewnia wymagane certyfikaty kwalifikowane eIDAS"
      - from: "Security Architecture §11 Authentication Mechanisms"
        to: "§1 Procedury autoryzacji użytkowników"
        influence: "Mechanizmy autentykacji implementują wymogi eIDAS dla identyfikacji cyfrowej"

  - id: IDENTITY-MANAGEMENT-PLAN-*
    type: requires
    reason: "Plan zarządzania tożsamością definiuje procesy identyfikacji zgodne z eIDAS"
    conditions:
      - when: "project.requires_user_identity === true"
        applies: true
    sections:
      - from: "Identity Management Plan §4 User Registration & Verification"
        to: "§1 Procedury autoryzacji użytkowników"
        influence: "Procedury rejestracji użytkowników muszą spełniać poziomy pewności eIDAS"

  - id: SECURITY-AUDIT-REPORT-*
    type: requires
    reason: "Audyty bezpieczeństwa weryfikują zgodność z wymogami technicznymi eIDAS"
    conditions:
      - when: "project.requires_eidas_certification === true"
        applies: true
    sections:
      - from: "Security Audit Report §7 Cryptographic Controls"
        to: "§3 Wyniki audytów bezpieczeństwa"
        influence: "Audyty kryptografii weryfikują zgodność z wymogami technicznymi eIDAS"
```

### Impacts
```yaml
impacts:
  - id: DIGITAL-SIGNATURE-IMPLEMENTATION-*
    type: blocks
    reason: "Implementacja podpisu elektronicznego wymaga certyfikacji eIDAS"
    conditions:
      - when: "project.requires_digital_signature === true"
        applies: true
    sections:
      - from: "§2 Certyfikaty kwalifikowane"
        to: "Digital Signature Implementation §5 Certificate Integration"
        influence: "Certyfikaty kwalifikowane eIDAS są wymagane do implementacji podpisu"
      - from: "§4 Dokumentacja procesów podpisu elektronicznego"
        to: "Digital Signature Implementation §8 Signature Workflows"
        influence: "Procesy podpisu muszą być zgodne z procedurami eIDAS"

  - id: CROSS-BORDER-AUTHENTICATION-*
    type: blocks
    reason: "Autentykacja transgraniczna w UE wymaga zgodności z eIDAS"
    conditions:
      - when: "project.cross_border === true"
        applies: true
      - when: "project.region === 'EU'"
        applies: true
    sections:
      - from: "§1 Procedury autoryzacji użytkowników"
        to: "Cross-Border Authentication §6 eIDAS Node Integration"
        influence: "Procedury autoryzacji definiują integrację z węzłami eIDAS"

  - id: COMPLIANCE-AUDIT-REPORT-*
    type: informs
    reason: "Status zgodności eIDAS wpływa na ogólne compliance regulacyjne"
    sections:
      - from: "§3 Wyniki audytów bezpieczeństwa"
        to: "Compliance Audit Report §9 Digital Identity Compliance"
        influence: "Audyty eIDAS są częścią ogólnej oceny compliance"
```

### Related Documents
```yaml
related:
  - id: GDPR-COMPLIANCE-*
    type: informs
    reason: "GDPR i eIDAS współpracują w zakresie ochrony danych tożsamości"
    conditions:
      - when: "project.handles_identity_data === true"
        applies: true

  - id: TRUST-SERVICE-PROVIDER-CONTRACT-*
    type: informs
    reason: "Umowy z dostawcami usług zaufania wspierają implementację eIDAS"
    conditions:
      - when: "project.uses_qualified_tsp === true"
        applies: true

  - id: INTEROPERABILITY-SPECIFICATION-*
    type: informs
    reason: "Specyfikacje interoperacyjności zapewniają zgodność z eIDAS"
    conditions:
      - when: "project.cross_border === true"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-EIDAS-*.md"
    required: false
    purpose: "Tracking eIDAS compliance tasks and certification milestones"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-EIDAS-*.md"
    required: true
    purpose: "Audit logs, certificate chains, conformity assessment reports required by eIDAS"
    conditions:
      - when: "project.requires_eidas_certification === true"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-EIDAS-*.md"
    required: true
    purpose: "Definition of Ready for eIDAS compliance - technical prerequisites and PKI setup"

  - type: DoD
    path: "satellites/dod/DOD-EIDAS-*.md"
    required: true
    purpose: "Definition of Done for eIDAS compliance - certification and testing criteria"
```
