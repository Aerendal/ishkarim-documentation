# Branżowa — Dokumenty Specyficzne dla Branży

## 📋 Przeznaczenie

Folder zawiera **szablony dokumentów specyficznych dla branży** — wymagań regulacyjnych, standardów branżowych i dokumentacji compliance wymaganej w określonych sektorach (finanse, zdrowie, energia, itp.).

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Compliance z regulacjami** (GDPR, HIPAA, SOX, PCI-DSS)
- **Standardy branżowe** (ISO, NIST, COBIT)
- **Audyty i certyfikacje** (audit trails, compliance reports)
- **Bezpieczeństwo sektorowe** (financial security, healthcare privacy)
- **Raportowanie regulacyjne** (regulatory filings, compliance dashboards)

## 👥 Kto używa?

- **Compliance Officers** — regulatory compliance, audit trails
- **Legal Teams** — legal compliance, contracts, agreements
- **Security Teams** — sector-specific security requirements
- **Auditors** — audit reports, compliance verification
- **Risk Managers** — regulatory risk assessment

## ⏱️ Kiedy używać?

**Faza:** Wszystkie fazy (Pre-Production → Production)
**Timing:** Przez cały lifecycle projektu, zwłaszcza przy audytach
**Lifecycle:** `draft → reviewed → approved → audited → archived`

## 📂 Kategorie dokumentów (16 szablonów)

### Compliance & Regulatory
- `gdpr_compliance_documentation.md` — GDPR Compliance
- `hipaa_compliance_checklist.md` — HIPAA (healthcare)
- `sox_compliance_controls.md` — SOX (financial reporting)
- `pci_dss_compliance.md` — PCI-DSS (payment card industry)
- `regulatory_filing.md` — Regulatory Filing Template
- `compliance_report.md` — Compliance Report

### Industry Standards
- `iso_27001_documentation.md` — ISO 27001 (information security)
- `iso_9001_quality_management.md` — ISO 9001 (quality)
- `nist_framework_implementation.md` — NIST Framework
- `cobit_controls.md` — COBIT (IT governance)

### Audits & Certifications
- `audit_trail.md` — Audit Trail Documentation
- `certification_documentation.md` — Certification Docs
- `external_audit_report.md` — External Audit Report
- `internal_audit_checklist.md` — Internal Audit Checklist

### Sector-Specific
- `financial_services_compliance.md` — Financial Services
- `healthcare_privacy_documentation.md` — Healthcare Privacy

## 🏢 Przykłady branż

**Financial Services:**
- SOX compliance
- PCI-DSS (dla płatności)
- Anti-Money Laundering (AML)
- Know Your Customer (KYC)

**Healthcare:**
- HIPAA compliance
- Patient privacy (GDPR + sector-specific)
- Medical device regulations (FDA, CE)

**Energy & Utilities:**
- NERC CIP (critical infrastructure)
- Environmental compliance
- Safety regulations

**Technology:**
- ISO 27001 (security)
- SOC 2 compliance
- Data privacy (GDPR, CCPA)

## 🔗 Powiązania

**Dependencies:**
- ⬅️ **Przedprodukcyjna** → Security Plan, DPIA są podstawą
- ⬅️ **Produkcyjna** → Compliance wymaga operational evidence

**Impacts:**
- ➡️ **All Projects** → regulatory requirements wpływają na wszystkie projekty
- ➡️ **Audits** → compliance docs są podstawą audytów
- ➡️ **Risk Management** → compliance gaps = risk items

## 📊 Statystyki

- **Liczba szablonów:** 16
- **Pokrycie Cross-References:** 100%
- **Połączenia w grafie:** ~150 dependencies/impacts
- **Średnia wielkość:** 200-400 linii per szablon (bardziej szczegółowe)

## 🚀 Quick Start

**Krok 1: Identyfikuj regulacje**
1. Określ branżę projektu
2. Zidentyfikuj applicable regulations (GDPR, HIPAA, SOX, etc.)

**Krok 2: Wybierz szablony**
3. `compliance_report.md` — Status compliance
4. Wybierz sector-specific templates (np. `gdpr_compliance_documentation.md`)

**Krok 3: Implementuj kontrole**
5. `audit_trail.md` — Setup audit logging
6. `certification_documentation.md` — Prepare for certification

**Krok 4: Audyt**
7. `internal_audit_checklist.md` — Self-assessment
8. `external_audit_report.md` — External audit preparation

## ⚠️ Uwagi

- **Compliance jest ciągły:** Nie jest to one-time effort, wymaga continuous monitoring
- **Multi-jurisdiction:** Projekty globalne mogą wymagać wielu standardów jednocześnie
- **Legal review:** Zawsze konsultuj z legal team przed finalizacją
- **Evidence required:** Compliance wymaga documented evidence (logi, screenshots, approvals)

## 📖 Zobacz też

- [../specs/](../specs/) — Specyfikacje doc types, error codes (validation)
- [../produkcyjna/README.md](../produkcyjna/README.md) — Security plans, DPIA, SIRP
- [../../dependency_graph.md](../../dependency_graph.md) — Graf zależności

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Branżowa (Industry-Specific / Regulatory Compliance)
**Uwaga:** Zawsze konsultuj z legal/compliance team przed użyciem
