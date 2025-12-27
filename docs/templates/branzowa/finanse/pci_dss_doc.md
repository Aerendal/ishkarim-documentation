# 📄 PCI DSS Compliance Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Zapewnia zgodność z normami bezpieczeństwa PCI DSS dotyczącymi danych kart płatniczych.

## Zawartość
- Audyt systemów IT
- Procedury szyfrowania danych
- Testy penetracyjne
- Polityki dostępu i monitoringu
- Raporty zgodności

## Czego nie zawiera
- Szczegółowych planów sprzedażowych
- Strategii marketingowych

## Objętość
- 10–20 stron
- Raporty audytowe + rekomendacje

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Regulatorzy finansowi
- Banki
- Dostawcy usług płatniczych

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: SECURITY-ARCHITECTURE-*
    type: requires
    reason: "Architektura bezpieczeństwa definiuje mechanizmy ochrony danych kart płatniczych"
    conditions:
      - when: "project.processes_card_data === true"
        applies: true
      - when: "project.industry === 'finance'"
        applies: true
    sections:
      - from: "Security Architecture §8 Encryption & Data Protection"
        to: "§2 Procedury szyfrowania danych"
        influence: "Mechanizmy szyfrowania muszą spełniać wymogi PCI DSS dla danych kart"
      - from: "Security Architecture §9 Access Control"
        to: "§4 Polityki dostępu i monitoringu"
        influence: "Kontrola dostępu implementuje wymogi PCI DSS dla środowiska danych kart"
      - from: "Security Architecture §12 Network Segmentation"
        to: "§1 Audyt systemów IT"
        influence: "Segmentacja sieci definiuje zakres środowiska danych kart (CDE)"

  - id: PENETRATION-TEST-REPORT-*
    type: requires
    reason: "Testy penetracyjne są wymagane przez PCI DSS co najmniej rocznie"
    conditions:
      - when: "project.pci_dss_level >= '1'"
        applies: true
    sections:
      - from: "Penetration Test Report §6 Vulnerability Findings"
        to: "§3 Testy penetracyjne"
        influence: "Wyniki testów penetracyjnych są wymagane do certyfikacji PCI DSS"

  - id: VULNERABILITY-SCAN-REPORT-*
    type: requires
    reason: "Skanowanie podatności jest wymagane kwartalnie przez PCI DSS"
    conditions:
      - when: "project.processes_card_data === true"
        applies: true
    sections:
      - from: "Vulnerability Scan Report §5 Scan Results"
        to: "§1 Audyt systemów IT"
        influence: "Kwartalne skany ASV są wymagane dla zgodności PCI DSS"

  - id: NETWORK-ARCHITECTURE-*
    type: requires
    reason: "Architektura sieci definiuje topologię środowiska danych kart"
    sections:
      - from: "Network Architecture §4 Network Diagram"
        to: "§1 Audyt systemów IT"
        influence: "Diagram sieci dokumentuje przepływ danych kart wymagany przez PCI DSS"
```

### Impacts
```yaml
impacts:
  - id: PAYMENT-PROCESSING-IMPLEMENTATION-*
    type: blocks
    reason: "Implementacja przetwarzania płatności wymaga certyfikacji PCI DSS"
    conditions:
      - when: "project.processes_card_data === true"
        applies: true
    sections:
      - from: "§2 Procedury szyfrowania danych"
        to: "Payment Processing Implementation §7 Card Data Encryption"
        influence: "Procedury szyfrowania PCI DSS definiują implementację ochrony danych kart"
      - from: "§4 Polityki dostępu i monitoringu"
        to: "Payment Processing Implementation §9 Access Controls"
        influence: "Polityki dostępu PCI DSS są wymagane przed uruchomieniem przetwarzania płatności"

  - id: INCIDENT-RESPONSE-PLAN-*
    type: influences
    reason: "PCI DSS wymaga procedur reagowania na naruszenia danych kart"
    conditions:
      - when: "project.processes_card_data === true"
        applies: true
    sections:
      - from: "§4 Polityki dostępu i monitoringu"
        to: "Incident Response Plan §8 Data Breach Response"
        influence: "Monitoring PCI DSS wspiera wykrywanie naruszeń danych kart"

  - id: THIRD-PARTY-SECURITY-ASSESSMENT-*
    type: blocks
    reason: "Ocena bezpieczeństwa dostawców wymaga weryfikacji ich zgodności PCI DSS"
    conditions:
      - when: "project.uses_third_party_processors === true"
        applies: true
    sections:
      - from: "§5 Raporty zgodności"
        to: "Third-Party Security Assessment §6 PCI DSS Validation"
        influence: "Status PCI DSS dostawców jest wymagany przed integracją"

  - id: COMPLIANCE-AUDIT-REPORT-*
    type: informs
    reason: "Status PCI DSS wpływa na ogólne compliance finansowe"
    sections:
      - from: "§5 Raporty zgodności"
        to: "Compliance Audit Report §10 Payment Security Compliance"
        influence: "Certyfikacja PCI DSS jest częścią ogólnej oceny compliance"
```

### Related Documents
```yaml
related:
  - id: CHANGE-MANAGEMENT-PLAN-*
    type: informs
    reason: "Zmiany w środowisku CDE wymagają procedur change management PCI DSS"
    conditions:
      - when: "project.processes_card_data === true"
        applies: true

  - id: EMPLOYEE-TRAINING-PLAN-*
    type: informs
    reason: "PCI DSS wymaga szkoleń z zakresu bezpieczeństwa danych kart"
    conditions:
      - when: "project.has_card_data_handlers === true"
        applies: true

  - id: DISASTER-RECOVERY-PLAN-*
    type: informs
    reason: "PCI DSS wymaga planów odzyskiwania dla systemów przetwarzających dane kart"
    conditions:
      - when: "project.processes_card_data === true"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-PCI-DSS-*.md"
    required: false
    purpose: "Tracking PCI DSS compliance tasks and quarterly/annual requirements"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-PCI-DSS-*.md"
    required: true
    purpose: "ASV scan reports, penetration test results, audit logs required by PCI DSS"
    conditions:
      - when: "project.processes_card_data === true"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-PCI-DSS-*.md"
    required: true
    purpose: "Definition of Ready for PCI DSS compliance - CDE scoping and prerequisites"

  - type: DoD
    path: "satellites/dod/DOD-PCI-DSS-*.md"
    required: true
    purpose: "Definition of Done for PCI DSS compliance - all 12 requirements validation"
```
