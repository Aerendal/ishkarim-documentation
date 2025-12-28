---
id: "KPI-001"
title: "KPI & Dashboard Spec"
project: "NAZWA_PROJEKTU"
owner: "Product Ops"
version: "0.1"
status: "draft"
related: ["ROADMAP-PROD-001"]
---

# KPI & Dashboard Spec

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: ROADMAP-PROD-*
    type: requires
    reason: "Product Roadmap defines KPIs and success metrics to be tracked"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Roadmap §8 KPIs & success metrics"
        to: "§1 Metrics"
        influence: "Roadmap KPIs define what dashboard must track"
      - from: "Roadmap §3 Milestones & Releases"
        to: "§1 Metrics (progress tracking)"
        influence: "Milestone progress becomes key dashboard metric"

  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case defines business success metrics and ROI tracking"
    conditions:
      - when: "project.has_business_case === true"
        applies: true
    sections:
      - from: "Business Case §15 Success Metrics"
        to: "§1 Metrics"
        influence: "Business metrics (revenue, cost savings, user growth) become KPIs"
      - from: "Business Case §8 Financial Analysis"
        to: "§2 Dashboards (exec dashboard)"
        influence: "Financial metrics require executive dashboard visibility"

  - id: PRD-*
    type: influences
    reason: "PRD success metrics inform product KPIs"
    conditions:
      - when: "project.has_prd === true"
        applies: true
    sections:
      - from: "PRD §11 Success Metrics"
        to: "§1 Metrics"
        influence: "PRD feature success metrics become product KPIs"

  - id: SPRINT-CORE-*
    type: influences
    reason: "Sprint metrics inform delivery dashboard KPIs"
    conditions:
      - when: "project.uses_agile === true"
        applies: true
    sections:
      - from: "Sprint Core §7 Velocity & Metrics"
        to: "§1 Metrics (velocity, burndown)"
        influence: "Sprint velocity and burndown become delivery dashboard metrics"
      - from: "Sprint Core §3 Sprint Backlog"
        to: "§2 Dashboards (delivery dashboard)"
        influence: "Story completion and sprint progress tracked on delivery dashboard"

  - id: MONITORING-PLAN-*
    type: influences
    reason: "Monitoring metrics and SLAs feed into operational dashboards"
    conditions:
      - when: "project.has_monitoring === true"
        applies: true
    sections:
      - from: "Monitoring Plan §2 Metrics & KPIs"
        to: "§1 Metrics (system health)"
        influence: "System health metrics (uptime, latency, errors) become KPIs"

  - id: SLA-*
    type: influences
    reason: "SLA targets become dashboard metrics"
    conditions:
      - when: "project.has_sla === true"
        applies: true
    sections:
      - from: "SLA §3 Service Level Targets"
        to: "§1 Metrics (SLA compliance)"
        influence: "SLA targets and compliance rates become dashboard KPIs"

  - id: TEST-SUMMARY-REPORT-*
    type: influences
    reason: "Test metrics inform quality KPIs"
    conditions:
      - when: "project.has_testing === true"
        applies: true
    sections:
      - from: "Test Summary Report §3 Test Metrics"
        to: "§1 Metrics (quality metrics)"
        influence: "Test coverage, pass rate, defect density become quality KPIs"
```

### Impacts
```yaml
impacts:
  - id: ROADMAP-PROD-*
    type: influences
    reason: "KPI dashboard provides data-driven roadmap adjustments"
    conditions:
      - when: "kpi.trend === 'negative'"
        applies: true
    sections:
      - from: "§1 Metrics (underperforming KPIs)"
        to: "Roadmap §8 KPIs & success metrics"
        influence: "Underperforming KPIs trigger roadmap priority adjustments"

  - id: SPRINT-CORE-*
    type: influences
    reason: "Delivery metrics inform sprint planning and capacity"
    conditions:
      - when: "project.uses_agile === true"
        applies: true
    sections:
      - from: "§2 Dashboards (delivery dashboard)"
        to: "Sprint Core §2 Sprint Planning"
        influence: "Velocity trends inform sprint capacity planning"

  - id: POSTMORTEM-REPORT-*
    type: influences
    reason: "KPI anomalies may trigger postmortem investigations"
    conditions:
      - when: "kpi.has_anomaly === true"
        applies: true
    sections:
      - from: "§1 Metrics (KPI anomalies)"
        to: "Postmortem §1 Summary"
        influence: "Sudden KPI degradation triggers incident investigation"

  - id: STAKEHOLDER-COMMUNICATION-*
    type: blocks
    reason: "KPI dashboard drives stakeholder reporting"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§2 Dashboards (exec dashboard)"
        to: "Stakeholder Communication §3 Status Reports"
        influence: "Executive dashboard KPIs populate stakeholder status reports"

  - id: CAPACITY-PLAN-*
    type: influences
    reason: "Delivery metrics may reveal capacity constraints"
    conditions:
      - when: "delivery_metrics.show_bottlenecks === true"
        applies: true
    sections:
      - from: "§2 Dashboards (delivery dashboard)"
        to: "Capacity Plan §4 Gaps & mitigation"
        influence: "Consistent velocity drops indicate capacity issues"

  - id: RISK-REGISTER-*
    type: influences
    reason: "KPI deterioration may indicate emerging risks"
    conditions:
      - when: "kpi.trend === 'worsening'"
        applies: true
    sections:
      - from: "§1 Metrics (declining KPIs)"
        to: "Risk Register §1 Risk table"
        influence: "Declining KPIs become early warning signals for risks"

  - id: BUSINESS-REVIEW-*
    type: blocks
    reason: "KPI dashboard is primary input to business reviews"
    conditions:
      - when: "project.has_business_reviews === true"
        applies: true
    sections:
      - from: "§2 Dashboards (exec dashboard)"
        to: "Business Review §2 Performance Analysis"
        influence: "Dashboard KPIs drive business review discussions"
```

### Related
```yaml
related:
  - id: RTM-*
    type: informs
    reason: "Requirements traceability can be visualized as dashboard metric"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "Compliance status may be tracked as KPI"

  - id: TIMELINE-*
    type: informs
    reason: "Timeline adherence can be tracked as dashboard metric"

  - id: BUDGET-PLAN-*
    type: informs
    reason: "Budget vs actual spend can be tracked as financial KPI"

  - id: USER-GUIDE-*
    type: informs
    reason: "User adoption metrics may be tracked as product KPI"

  - id: PERFORMANCE-TEST-REPORT-*
    type: informs
    reason: "Performance metrics feed into operational KPIs"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-KPI-*.md"
    required: false
    purpose: "Track dashboard implementation tasks, data source integration, KPI threshold tuning"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-KPI-*.md"
    required: true
    purpose: "Store KPI definitions, calculation methodology, data source documentation, stakeholder KPI approvals"

  - type: Approval
    path: "satellites/approvals/APPROVAL-KPI-*.md"
    required: true
    purpose: "Product Ops and stakeholder approval of KPI definitions and dashboard design"

  - type: DoR
    path: "satellites/dor/DOR-KPI-*.md"
    required: true
    purpose: "Prerequisites: roadmap KPIs defined, data sources identified, dashboard tools selected, measurement methodology agreed"
```

## Metrics
- % complete (by epic) — metoda pomiaru
- Delivered value vs forecast — metoda pomiaru
- Lead time for features — definicja

## Dashboards
- Exec dashboard: metrics & SLA
- Delivery dashboard: progress per release

## Data sources
- Data warehouse tables, ETL jobs
