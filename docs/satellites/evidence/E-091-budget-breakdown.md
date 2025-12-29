---
id: E-091
title: "Rozpisanie Budżetu - $48k Total"
type: evidence
evidence_type: cost
date: 2025-12-26

related_documents:
  - BIZ-CASE-001-V2
  - FUNDING-APPROVAL-001
  - E-090

source:
  type: internal_analysis
  date_collected: 2025-12-26
---

# Rozpisanie Budżetu - $48k Total

## Kontekst
Szczegółowe rozpisanie budżetu Year 1 (2026) dla projektu Ishkarim. Budget covers development (6 miesięcy), QA, infrastructure, tools, marketing, i contingency reserve. Analiza obejmuje breakdown kosztów, justification, i risk mitigation.

## Metodologia
- **Źródła**:
  - Market rates dla developers (Glassdoor, Payscale 2025)
  - Cloud pricing (AWS, DigitalOcean)
  - Tool licensing (Qt, JetBrains)
- **Timeline**: Styczeń-Czerwiec 2026 (6 miesięcy development)
- **Team**: 2 developers (contract/freelance)
- **Location**: Remote (Poland-based)

## Wyniki

### Total Budget Year 1: **$48,000**

---

### 1. **Development Costs: $36,000** (75% budżetu)

#### Breakdown
| Rola | Rate | Duration | Total |
|------|------|----------|-------|
| Senior Python Developer (Lead) | $7,000/month | 6 miesięcy | **$42,000** |
| Mid-level Python Developer | $5,000/month | 6 miesięcy | **$30,000** |
| **SUBTOTAL** |  |  | **$72,000** |

**Wait, $72k > $36k?**

**Corrected** (part-time):
| Rola | Rate | Duration | FTE | Total |
|------|------|----------|-----|-------|
| Senior Python Developer | $7,000/month | 6 miesięcy | 75% | **$31,500** |
| Junior Python Developer | $3,000/month | 6 miesięcy | 50% | **$9,000** |
| **SUBTOTAL** |  |  |  | **$40,500** |

**Still over budget. Re-adjust:**

#### **Final Development Budget**
| Rola | Rate | Duration | FTE | Total |
|------|------|----------|-----|-------|
| Senior Developer (You/Founder) | $0/month | 6 miesięcy | 100% | **$0** (sweat equity) |
| Mid-level Developer (Contractor) | $6,000/month | 6 miesięcy | 100% | **$36,000** |
| **TOTAL** |  |  |  | **$36,000** |

**Justification**:
- **Founder sweat equity**: Assumes founder (Jerzy) jest technical i może handle development work
- **1 contractor**: Mid-level Python/Qt developer (remote Poland: $6k/month realistic)
- **Scope**: 19.5 person-months effort (E-085) → 2 people × 6 months = 12 person-months
  - **Gap**: 7.5 person-months → handle through scope reduction or overtime

**Risk mitigation**:
- MVP scope może być zredukowany jeśli timeline tight
- Founder overtime (nights/weekends) covers gap
- Phase 1 (Alpha) delivers value nawet z partial features

---

### 2. **QA & Testing: $4,000** (8% budżetu)

#### Breakdown
| Item | Cost | Justification |
|------|------|---------------|
| External QA contractor | $2,000/month × 2 months | Manual testing pre-releases (Alpha, Beta) |
| Automated testing tools | $0 | pytest (free), GitHub Actions (free tier) |
| Beta tester incentives | $500 | $100 gift cards × 5 testers |
| Bug tracking | $0 | GitHub Issues (free) |
| **TOTAL** | **$4,500** | → Reduce to $4k (cut 1 beta incentive) |

**Justification**:
- **QA contractor**: 2 months coverage (M5-M6) dla final RC testing
- **Beta incentives**: Encourage active feedback from alpha/beta users
- **Tools**: Free tier sufficient dla MVP (GitHub Actions: 2,000 min/month free)

---

### 3. **Infrastructure: $3,000** (6% budżetu)

#### Breakdown
| Item | Monthly | Duration | Total |
|------|---------|----------|-------|
| **Hosting** |  |  |  |
| AWS S3 (docs storage) | $50 | 12 months | $600 |
| DigitalOcean droplet (web/API) | $12 | 12 months | $144 |
| **Domain & SSL** |  |  |  |
| Domain (ishkarim.com) | $15/year | 1 year | $15 |
| SSL certificate | $0 | Let's Encrypt (free) | $0 |
| **Email** |  |  |  |
| Google Workspace (2 accounts) | $12 | 12 months | $144 |
| **Backup & Monitoring** |  |  |  |
| Backup storage (Backblaze) | $6 | 12 months | $72 |
| Monitoring (UptimeRobot free tier) | $0 | 12 months | $0 |
| **Development Tools (Cloud)** |  |  |  |
| GitHub Pro (2 users) | $8 | 12 months | $96 |
| CI/CD (GitHub Actions) | $0 | Free tier | $0 |
| **TOTAL** |  |  | **$1,071** |

**Wait, $1,071 < $3,000. Where's rest?**

**Additional infrastructure costs**:
| Item | Cost | Justification |
|------|------|---------------|
| Qt Commercial License | $0 | Use LGPL PySide6 (free) instead Qt Commercial |
| CDN (Cloudflare) | $0 | Free tier |
| Analytics (Plausible) | $9/month × 12 | Privacy-friendly analytics |
| Error tracking (Sentry) | $26/month × 12 | Production error monitoring |
| **Subtotal additional** | **$420** |  |

**Revised infrastructure total**: $1,071 + $420 = **$1,491**

**Gap**: $3,000 - $1,491 = **$1,509 unallocated**

**Reallocation**: Move $1,500 do **Contingency** (zwiększa contingency do $6,500)

**Final Infrastructure**: **$1,500** (rounded, conservative estimate)

---

### 4. **Tools & Licenses: $1,800** (4% budżetu)

#### Breakdown
| Tool | Cost | Duration | Total |
|------|------|----------|-------|
| **Development** |  |  |  |
| PyCharm Professional (2 licenses) | $89/year × 2 | 1 year | $178 |
| Qt Designer (included w/ PySide6) | $0 | Free (LGPL) | $0 |
| GitHub Copilot (2 licenses) | $10/month × 2 × 6 months | 6 months | $120 |
| **Design** |  |  |  |
| Figma Pro | $12/month × 6 months | 6 months | $72 |
| **Documentation** |  |  |  |
| Notion Team (for internal docs) | $10/month × 6 months | 6 months | $60 |
| **Communication** |  |  |  |
| Slack (free tier) | $0 | Free | $0 |
| Zoom Pro | $15/month × 6 months | 6 months | $90 |
| **Project Management** |  |  |  |
| Linear (project tracking) | $8/month × 6 months | 6 months | $48 |
| **Total** |  |  | **$568** |

**Gap**: $1,800 - $568 = **$1,232**

**Additional tools needed**:
| Tool | Cost | Justification |
|------|------|---------------|
| macOS VM (testing) | $20/month × 6 | Cross-platform testing (Mac) |
| Windows Server (testing) | $15/month × 6 | Cross-platform testing (Windows) |
| Load testing tools (Locust) | $0 | Free open source |
| **Subtotal** | **$210** |  |

**Revised tools total**: $568 + $210 = **$778**

**Final Tools & Licenses**: **$800** (rounded)

**Remaining**: $1,800 - $800 = **$1,000 → move to Contingency**

---

### 5. **Marketing: $3,000** (6% budżetu)

#### Breakdown
| Item | Cost | Justification |
|------|------|---------------|
| **Website** |  |  |
| Landing page design (Figma template) | $49 | One-time purchase |
| Webflow hosting (or similar) | $16/month × 6 months | No-code website |
| **Content** |  |  |
| Blog setup (Ghost) | $9/month × 6 months | Content marketing |
| Technical writer (blog posts) | $200 × 5 posts | 5 launch blog posts |
| **Launch Campaign** |  |  |
| Product Hunt launch kit | $0 | DIY |
| LinkedIn ads (test budget) | $500 | User acquisition test |
| Reddit ads (test budget) | $300 | r/programming, r/productivity |
| **Community** |  |  |
| Discord server setup | $0 | Free |
| **Email Marketing** |  |  |
| ConvertKit (email list) | $29/month × 6 months | Newsletter for beta users |
| **Total** |  | **$2,278** |

**Remaining**: $3,000 - $2,278 = **$722**

**Additional marketing**:
| Item | Cost |
|------|------|
| Logo design (Fiverr) | $150 |
| Social media graphics (Canva Pro) | $13/month × 6 = $78 |
| Video explainer (DIY with Loom) | $0 |
| **Subtotal** | **$228** |

**Final Marketing**: $2,278 + $228 = **$2,506** ≈ **$2,500**

**Remaining**: $3,000 - $2,500 = **$500 → move to Contingency**

---

### 6. **Legal & Admin: $2,000** (4% budżetu)

#### Breakdown
| Item | Cost | Justification |
|------|------|---------------|
| LLC formation (Poland: sp. z o.o.) | $500 | One-time legal entity setup |
| Accounting software (Xero) | $13/month × 12 months | Bookkeeping |
| Accountant retainer | $100/month × 6 months | Tax compliance |
| Terms of Service + Privacy Policy | $300 | Legal templates (Termly) |
| Trademark search (optional) | $0 | DIY via USPTO |
| Business insurance | $50/month × 6 months | Liability coverage |
| **Total** |  | **$1,756** |

**Final Legal & Admin**: **$1,800** (rounded up dla buffer)

**Remaining**: $2,000 - $1,800 = **$200 → move to Contingency**

---

### 7. **Contingency: $5,000** (10% budżetu)

**Purpose**: Unplanned expenses, scope creep, market changes

**Reallocations** (from above):
- Infrastructure savings: +$1,500
- Tools savings: +$1,000
- Marketing savings: +$500
- Legal savings: +$200
- **Total reallocation**: +$3,200

**Final Contingency**: $5,000 + $3,200 = **$8,200**

**Contingency %**: $8,200 / $48,000 = **17%** (healthy reserve)

---

## Implikacje

### Final Budget Breakdown

| Category | Allocated | Adjusted | **Final** | % Total |
|----------|-----------|----------|-----------|---------|
| Development | $36,000 | $36,000 | **$36,000** | 75% |
| QA & Testing | $4,000 | -$500 | **$3,500** | 7.3% |
| Infrastructure | $3,000 | -$1,500 | **$1,500** | 3.1% |
| Tools & Licenses | $1,800 | -$1,000 | **$800** | 1.7% |
| Marketing | $3,000 | -$500 | **$2,500** | 5.2% |
| Legal & Admin | $2,000 | -$200 | **$1,800** | 3.8% |
| Contingency | $5,000 | +$3,700 | **$8,700** | 18.1% |
| **TOTAL** | **$54,800** | -$0 | **$54,800** | **100%** |

**Wait, total = $54,800, nie $48,000!**

### Budget Reconciliation

**Problem**: Initial allocations sum to $54,800, exceeds target $48,000

**Solution**: Trim categories to fit $48,000 constraint

#### **Revised Final Budget**

| Category | Target | % Total | Notes |
|----------|--------|---------|-------|
| Development | **$36,000** | 75% | 1 contractor + founder sweat equity |
| QA & Testing | **$3,000** | 6.25% | External QA 1.5 months (not 2) |
| Infrastructure | **$1,500** | 3.1% | Use free tiers aggressively |
| Tools & Licenses | **$800** | 1.7% | Essential tools only |
| Marketing | **$2,500** | 5.2% | Bootstrap approach, DIY content |
| Legal & Admin | **$1,700** | 3.5% | Templates instead custom legal |
| Contingency | **$2,500** | 5.2% | Reduced but still 5% buffer |
| **TOTAL** | **$48,000** | **100%** | ✅ Fits constraint |

---

### Key Assumptions
1. **Founder contributes**: Equivalent $42k salary jako sweat equity (not counted in budget)
2. **Part-time contractor**: $6k/month × 6 months = $36k
3. **Free tier maximization**: GitHub, AWS free tier, open source tools
4. **Bootstrap marketing**: DIY content, organic growth vs paid ads
5. **Remote team**: No office costs, equipment assumed owned

### Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Contractor unavailable | High | Medium | Have 2-3 backup contractors identified |
| Scope creep (+20% effort) | High | High | Strict MVP scope, defer post-MVP features |
| Tool costs higher than estimated | Low | Medium | Contingency covers $2.5k overrun |
| Marketing ineffective | Medium | Medium | Focus on organic (Product Hunt, Reddit) |
| Legal issues (IP, licensing) | High | Low | Upfront legal review ($300 budget) |

### Funding Source
**Total needed**: $48,000

**Options**:
1. **Personal savings** (founder investment)
2. **Angel investment** (if seeking external capital)
3. **Grants** (Poland/EU tech startup grants)
4. **Pre-sales** (beta users pay upfront)

**Recommended**: Personal savings ($48k) + sweat equity ($42k) = **$90k total investment**

**ROI**: 260% over 5 years (E-090) → **$234k return** on $90k investment

## Dane Raw

### Developer Rates (Poland Market, 2025)

| Seniority | Hourly Rate | Monthly (160h) | Source |
|-----------|-------------|----------------|--------|
| Junior Python Dev | $20-30/h | $3,200-4,800 | Glassdoor PL 2025 |
| Mid-level Python Dev | $35-50/h | $5,600-8,000 | Glassdoor PL 2025 |
| Senior Python Dev | $50-70/h | $8,000-11,200 | Glassdoor PL 2025 |

**Ishkarim contractor** ($6k/month) = **$37.50/h** → Mid-level rate (reasonable)

### Infrastructure Cost Comparison

| Provider | Service | Cost/Month | Notes |
|----------|---------|------------|-------|
| **AWS** | S3 (50GB) | $1.15 | Conservative estimate 10GB = $0.23 |
| **AWS** | EC2 t3.micro | $8.50 | Alternative: DigitalOcean cheaper |
| **DigitalOcean** | Basic Droplet | $6 | Better pricing dla startups |
| **Vercel** | Hosting (free tier) | $0 | For static landing page |
| **Cloudflare** | CDN + DNS | $0 | Free tier sufficient |
| **Backblaze** | B2 backup (50GB) | $0.30 | $0.005/GB/month |

**Optimized infra**: ~$100/month (nie $250) → **$1,200/year** (reallocate $1,800 savings)

### Tools Cost Optimization

**Free alternatives**:
- PyCharm → **VS Code** (free, with Python extension)
- Figma Pro → **Figma Free** (3 files limit OK dla MVP)
- Notion Team → **Obsidian** (free, dogfood own product later)
- Zoom Pro → **Google Meet** (free w/ Google Workspace)
- Linear → **GitHub Projects** (free)

**Optimized tools**: ~$200/year (vs $1,800 allocated) → **$1,600 savings**

**Trade-off**: Developer productivity slightly lower (free tools less integrated), ale acceptable dla bootstrap

### Marketing ROI Analysis

| Channel | Cost | Expected Users | CAC | Notes |
|---------|------|----------------|-----|-------|
| Product Hunt | $0 | 100 sign-ups | $0 | Organic launch |
| LinkedIn ads | $500 | 25 users | $20 | B2B targeting |
| Reddit organic | $0 | 50 users | $0 | r/productivity posts |
| Blog SEO | $1,000 (5 posts) | 200 users (1 year) | $5 | Long-tail |
| **Total** | **$1,500** | **375 users** | **$4** avg | Strong ROI |

**Benchmark**: SaaS CAC typically $50-200 → **Ishkarim CAC $4 = excellent** (bootstrap advantage)
