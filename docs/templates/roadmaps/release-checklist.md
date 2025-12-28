---
id: "REL-CHECK-001"
title: "Release Checklist — Release 1"
project: "NAZWA_PROJEKTU"
owner: "Release Manager"
version: "0.1"
status: "draft"
related: ["ROADMAP-PROD-001"]
---

# Release Checklist — Release 1

## Pre‑freeze
- [ ] All critical PRs merged into release branch
- [ ] DoR check for all epics: passed
- [ ] Release notes: draft

## Pre‑release
- [ ] QA smoke tests green on staging
- [ ] Security scans (SAST/DAST) passed
- [ ] DB migration scripts reviewed and rollback tested
- [ ] Ops runbook updated

## Release window
- [ ] Cutover: run idempotent deploy script
- [ ] Smoke tests on production passed
- [ ] Monitoring thresholds verified

## Post‑release
- [ ] Postmortem scheduled
- [ ] Stakeholder communication sent
- [ ] Changelog published
