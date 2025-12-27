# Research Plan: DigitalMinds Project
## Detailed Methods and Statistical Analysis Plan

**Project ID:** NIH-R01-2024-8721
**PI:** Dr. Sarah Chen
**Version:** 4.2 | **Date:** December 27, 2025

---

## Research Questions

**RQ1:** What is the prospective association between social media use intensity (hours/day, frequency of checking) and cognitive development trajectories in children ages 8-14?

**RQ2:** Do specific content types (passive scrolling vs. active posting, violent/sexual content vs. educational) have differential effects on cognition?

**RQ3:** What are the neural mechanisms linking social media use to cognitive outcomes (altered reward processing, attentional control deficits, sleep disruption)?

**RQ4:** Which children are most vulnerable (age, gender, baseline cognition, family environment, genetic factors)?

**RQ5 (Causal):** Does experimentally reducing social media use to <1 hour/day for 3 months causally improve executive functions and mental health?

---

## Hypotheses

**H1 (Dose-Response):** Greater social media use (hours/day) will predict steeper declines in executive functions (inhibitory control, working memory) over 5 years, with threshold effect at ~3 hours/day.

**H2 (Content Type):** Passive consumption (scrolling feeds) will show stronger negative associations with cognition than active creation (posting, commenting).

**H3 (Neural Mechanism - Reward):** Heavy social media users will show heightened ventral striatum activation to social feedback (likes, comments) and reduced frontoparietal control network connectivity.

**H4 (Neural Mechanism - Attention):** Social media use will predict reduced sustained attention (measured by continuous performance task) and increased distractibility (Flanker task).

**H5 (Moderation):** Effects will be stronger for:
- Younger children (ages 8-10 vs. 12-14) - more sensitive developmental period
- Girls (social comparison, body image concerns)
- Children with lower baseline executive functions (less self-regulation)

**H6 (Causal):** RCT participants randomized to social media reduction (<1 hour/day) will show:
- +0.3 SD improvement in executive functions vs. control (Cohen's d=0.3, small-medium effect)
- 20% reduction in depressive symptoms (CDI-2 scores)
- Increased frontoparietal connectivity (fMRI)

---

## Methodology

### Participants

**Sample Size:** N=800 children (ages 8-14 at baseline)

**Power Analysis:**
- Longitudinal associations: N=800 provides 90% power to detect small effects (r=0.15) at α=0.001 (Bonferroni-corrected)
- RCT (N=200, 100 per arm): 80% power to detect d=0.4 effect at α=0.05

**Recruitment:**
- **Sources:**
  - Boston Public Schools (partnerships with 15 middle schools, 8 elementary schools)
  - Community centers, churches, Boys & Girls Clubs
  - Social media ads (Facebook, Instagram - targeted to parents)
- **Eligibility:**
  - Age 8-14 years
  - English-speaking (child + parent)
  - Have smartphone or tablet (for monitoring app)
  - No diagnosed intellectual disability, autism, or ADHD (confounds cognition)
- **Stratification:** Recruit balanced by age (±50 per year 8-14), gender (50% female), race/ethnicity (40% non-White to match Boston demographics)

**Retention Strategies:**
- **Compensation:** $150 (baseline), $200 (each annual follow-up), $100 (6-month check-ins)
- **Engagement:** Birthday cards, quarterly newsletters with study updates, exclusive "study participant" t-shirts
- **Flexibility:** Evening/weekend appointments, make-up visits (up to 3 reschedules), home visits for transportation barriers
- **Expected Attrition:** 15%/year → 55% retention at Year 5 (N=440 complete)

---

### Measures

#### 1. Social Media Use (Primary Predictor)

**Passive Monitoring (Objective):**
- **App:** Custom Android/iOS app (similar to Screentime or QualityTime)
- **Data Collected:**
  - Total screen time (minutes/day)
  - App-specific usage (TikTok, Instagram, Snapchat, YouTube, etc.)
  - Session frequency (pickups/day)
  - Time of day distribution (morning, school hours, evening, late night)
  - Content categorization (via API access to app data - requires parental consent)
- **Privacy:** Data encrypted, stored on secure Harvard server (not shared with third parties)
- **Compliance:** 80% target (days with valid data) - incentivize with monthly $10 gift cards

**Self-Report (Subjective):**
- **Social Media Use Questionnaire (SMUQ):** 20 items
  - "How many hours per day do you usually spend on social media?"
  - "How often do you check social media (never, hourly, every 30 min, constantly)?"
  - Content: "What do you mainly do? (scroll feeds, post photos, chat with friends, watch videos)"
- **Problematic Use:** Social Media Addiction Scale (SMAS, 9 items) - measures compulsive use, withdrawal, tolerance

#### 2. Cognitive Functions (Primary Outcome)

**NIH Toolbox Cognition Battery (NIHTB-CB):**
- **Executive Functions:**
  - **Flanker Inhibitory Control:** Inhibit prepotent responses (score: RT + accuracy)
  - **List Sorting Working Memory:** Hold + manipulate information (score: # correct)
  - **Dimensional Change Card Sort:** Cognitive flexibility (score: accuracy)
  - **Composite Score:** Fluid cognition composite (standardized, M=100, SD=15)
- **Attention:**
  - **Continuous Performance Task (CPT):** Sustained attention (30 min, detect target letter)
- **Processing Speed:**
  - **Pattern Comparison:** Match patterns quickly (score: # correct in 90s)

**Standardized Achievement Tests:**
- **WIAT-III (Wechsler Individual Achievement Test):**
  - Reading Comprehension (grade-level passage, answer questions)
  - Math Problem Solving

**Administration:**
- Trained research assistants (RAs), blind to social media use
- iPad-based (NIHTB app)
- Duration: 90 minutes (with breaks)
- Timing: Baseline, 12, 24, 36, 48, 60 months

#### 3. Mental Health (Secondary Outcome)

**Depression:**
- **CDI-2 (Children's Depression Inventory):** 28 items, self-report
- Example: "I am sad... (Never, Sometimes, Often, Always)"
- Score: 0-56 (higher = more depressed), clinical cutoff >19

**Anxiety:**
- **SCARED (Screen for Child Anxiety Related Disorders):** 41 items
- Subscales: Generalized anxiety, social phobia, separation anxiety, panic

**Self-Esteem:**
- **Rosenberg Self-Esteem Scale:** 10 items (e.g., "I feel that I am a person of worth")

**Administered:** Every 6 months (REDCap online survey, completed at home)

#### 4. Neuroimaging (Mechanism)

**Participants:** Subsample N=200 (ages 10-14, due to MRI motion concerns with younger children)

**Scanning Protocol (3 Tesla Siemens Prisma):**

**Structural MRI:**
- T1-weighted MPRAGE (1mm isotropic, 5 min)
- Measure cortical thickness, subcortical volumes

**Resting-State fMRI (rs-fMRI):**
- 10 min, eyes open (fixation cross)
- TR=2s, 300 volumes
- Analyze functional connectivity:
  - **Default Mode Network (DMN):** Medial prefrontal cortex, posterior cingulate (self-referential processing)
  - **Frontoparietal Control Network:** Dorsolateral PFC, posterior parietal (executive control)
  - **Salience Network:** Anterior insula, ACC (attention switching)

**Task fMRI:**
- **Monetary Incentive Delay (MID):** Reward anticipation task (20 min)
  - Cue → anticipate reward ($0, $0.20, $1) → fast button press → feedback (win/lose)
  - Measure ventral striatum activation during anticipation
- **Social Feedback Task:** Custom task
  - View own "social media" profile → receive likes (10, 50, 200) → rate mood
  - Measure striatum activation to social rewards

**Diffusion MRI (dMRI):**
- 64 directions, b=1000 s/mm²
- Measure white matter integrity (fractional anisotropy in fronto-striatal tracts)

**Timing:** Baseline, 24 months (Year 2), 48 months (Year 4)

**Quality Control:**
- Motion: Exclude scans with >3mm framewise displacement
- Visual inspection: Neuroradiologist reviews all scans, flag incidental findings

#### 5. Ecological Momentary Assessment (EMA)

**Purpose:** Capture real-time experiences (mood, context) when using social media

**Protocol:**
- **Frequency:** 3× daily prompts (morning, afternoon, evening) for 7 consecutive days/month
- **Platform:** MetricWire app (sends push notifications)
- **Questions (30 seconds to complete):**
  - "What are you doing right now?" (social media, homework, sports, socializing in-person)
  - "How do you feel?" (1-10 scale: happy, anxious, lonely, bored)
  - "Did you just use social media? If yes, for how long?"
- **Analysis:** Multi-level modeling (Level 1: within-person fluctuations, Level 2: between-person differences)

#### 6. Covariates (Potential Confounders)

**Demographics:**
- Age, gender, race/ethnicity
- Family income (<$50k, $50-100k, >$100k)
- Parent education (high school, some college, college degree, graduate)

**Family Environment:**
- **Home Chaos:** Confusion, Hubbub, and Order Scale (15 items) - measure household disorder
- **Parental Monitoring:** "How often do you know where your child is?" (1-5 scale)
- **Parent-Child Relationship:** Network of Relationships Inventory (warmth, conflict)

**Baseline Cognition:**
- IQ (WASI-II, 2-subtest: Vocabulary + Matrix Reasoning, 20 min)

**Physical Health:**
- **Sleep:** Pittsburgh Sleep Quality Index (PSQI) - hours/night, quality
- **Physical Activity:** Accelerometer (ActiGraph worn for 7 days, captures daily steps)
- **BMI:** Height, weight measured in lab

**Genetics (Optional, Saliva Sample):**
- Dopamine receptor genes (DRD2, DRD4) - linked to reward sensitivity
- 5-HTTLPR (serotonin transporter) - linked to depression vulnerability
- Polygenic risk score for ADHD, depression

---

### Statistical Analysis Plan

#### Aim 1: Longitudinal Associations (Social Media → Cognition)

**Model:** Linear mixed-effects model (LMM)

```
Cognition_it = β0 + β1*SocialMedia_it + β2*Time_it + β3*SocialMedia_it*Time_it
              + β4*Age_i + β5*Gender_i + β6*SES_i
              + u_0i + u_1i*Time_it + ε_it

Where:
- i = individual, t = time point
- u_0i = random intercept (person-specific baseline cognition)
- u_1i = random slope (person-specific rate of change)
- ε_it = residual error
```

**Primary Test:**
- **Cross-sectional:** β1 (association between social media and cognition at baseline)
- **Longitudinal:** β3 (interaction - does social media predict rate of cognitive change?)

**Dose-Response:**
- Bin social media use (0-1h, 1-2h, 2-3h, 3-4h, >4h/day)
- Test linear vs. quadratic vs. threshold (piecewise) models
- Compare AIC/BIC to select best-fitting model

**Content Type:**
- Separate predictors: Passive_scrolling_hours, Active_posting_hours, Video_watching_hours
- Test which has strongest association with cognition

**Software:** R (lme4 package), Python (statsmodels)

**Multiple Comparisons:**
- Bonferroni correction for 5 cognitive outcomes (α = 0.05/5 = 0.01)

#### Aim 2: Neural Mechanisms (fMRI)

**Preprocessing:**
- FSL FEAT pipeline: Motion correction, slice-timing, spatial smoothing (6mm FWHM), high-pass filter (128s)
- Registration to MNI152 standard space

**Connectivity Analysis (rs-fMRI):**
- **Seed-based:** Place sphere (6mm radius) in key regions (mPFC, striatum)
  - Correlate seed time-series with all brain voxels → connectivity map
- **Graph Theory:** Construct whole-brain network (264 nodes, Power et al. parcellation)
  - Metrics: Global efficiency, modularity, rich-club coefficient

**Task fMRI (Reward):**
- GLM with 3 regressors: Anticipation_low, Anticipation_medium, Anticipation_high
- Contrast: High > Low reward anticipation
- ROI analysis: Ventral striatum (anatomically defined, Harvard-Oxford atlas)
- Extract β-weights → correlate with social media use

**Association Model:**
```
Brain_Measure_i = β0 + β1*SocialMedia_i + β2*Age_i + β3*Gender_i + ε_i
```

**Mediation Analysis:**
- Test if brain measures mediate social media → cognition link
- Method: Structural equation modeling (SEM) with lavaan R package
```
SocialMedia → Brain_Connectivity → Cognition
```

#### Aim 3: RCT (Causal Test)

**Design:** Parallel-group RCT (N=200, 100 per arm, 3-month intervention)

**Randomization:**
- Stratified by age (8-10, 11-12, 13-14) and baseline social media use (3-5h, >5h/day)
- Blocked randomization (block size 4) to ensure balance

**Intervention Group:**
- **Goal:** Reduce to <1 hour/day social media use
- **Methods:**
  - App blocker (Freedom or Moment - blocks apps after 60 min/day)
  - Family contract (parent + child sign agreement)
  - Weekly coaching calls (20 min with study clinician, problem-solve barriers)
  - Alternative activities (vouchers for sports, arts, $50/month)

**Control Group:**
- Maintain current usage
- Monitor with app (for measurement) but no restrictions
- Weekly check-in calls (matched attention control)

**Outcomes:**
- **Primary:** Change in executive function composite (NIHTB) from pre to post (3 months)
- **Secondary:** Depression (CDI-2), anxiety (SCARED), fMRI connectivity (N=50 per arm)

**Analysis:**
- **Intent-to-Treat:** Include all randomized (even if drop out)
- **Model:** ANCOVA
```
Cognition_post = β0 + β1*Treatment + β2*Cognition_pre + β3*Age + β4*Gender + ε
```
- **Effect Size:** Cohen's d = (M_treatment - M_control) / SD_pooled
- **Target:** d=0.3-0.5 (small to medium effect)

**Compliance:**
- Monitor with app (verify <1h/day in intervention group)
- Define "adherent" as ≥70 days/90 days with <1h social media
- Compare adherers vs. non-adherers (complier-average causal effect)

**Blinding:**
- Outcomes assessors blind to group assignment
- Participants not blind (impossible for behavioral intervention)

---

### Timeline

**Year 1:**
- Months 1-3: IRB approval, app development, RA hiring + training
- Months 4-12: Baseline data collection (N=800)
- Month 12: First neuroimaging wave (N=200)

**Year 2:**
- Months 13-24: 6-month, 12-month, 18-month follow-ups
- Month 24: Second neuroimaging wave

**Year 3:**
- Months 25-36: 24-month, 30-month follow-ups
- Begin RCT recruitment (identify high-users, N=200)

**Year 4:**
- Months 37-39: RCT pre-intervention assessments + randomization
- Months 40-42: 3-month intervention period
- Months 43-45: RCT post-intervention assessments (outcomes)
- Month 48: Third neuroimaging wave (subset)

**Year 5:**
- Months 49-60: Final 54-month, 60-month follow-ups
- Data analysis, manuscript writing, dissemination

---

## Ethical Considerations

### Human Subjects Protection

**IRB Approval:** Harvard Committee on the Use of Human Subjects (protocol #IRB24-0512)

**Informed Consent:**
- **Parent:** Written consent (explains risks, benefits, procedures)
- **Child:** Assent (age-appropriate explanation, 8-11 years: verbal, 12-14: written)
- **Opt-Out:** Participant can withdraw anytime (no penalty)

**Risks:**
- **Minimal Risk:** Cognitive testing (boredom, fatigue)
- **MRI:** Claustrophobia, incidental findings (managed by neuroradiologist review, parent notification)
- **App Monitoring:** Privacy concerns (mitigated by encryption, data security)
- **RCT Intervention:** Social isolation (if reduce social media) - monitored with weekly calls, provide alternative activities

**Benefits:**
- Compensation ($150-500 per visit)
- Contribute to science
- Learn about healthy technology use
- Free cognitive + mental health assessment (provide report to parents)

**Privacy:**
- **Data Security:** HIPAA-compliant servers, encrypted, access-controlled
- **Identifiers:** Separate ID numbers (no names in dataset)
- **Data Sharing:** De-identified data (no personally identifiable information)

**Vulnerable Populations:**
- Children (additional protections: parental consent + child assent)
- Minors cannot consent alone

**Incidental Findings:**
- MRI: Neuroradiologist reviews all scans
- Clinically significant findings (tumors, malformations) → notify parents, refer to pediatrician
- Cognitive testing: Significant delays (>2 SD below age norms) → offer referral for evaluation

### Diversity, Equity, Inclusion (DEI)

**Recruitment:**
- Target 40% non-White participants (reflect Boston demographics)
- Bilingual RAs (Spanish) to recruit Latino families
- Partner with community organizations serving underrepresented groups

**Barriers:**
- **Transportation:** Provide Uber/Lyft vouchers or home visits
- **Childcare:** On-site childcare during visits
- **Technology Access:** Provide loaner smartphones if family lacks device

**Cultural Sensitivity:**
- Measures validated in diverse samples
- Avoid stigmatizing language ("screen addiction" → "screen time")

---

## Equipment & Facilities

**Neuroimaging:**
- Harvard Center for Brain Science: 3T Siemens Prisma MRI
- Cost: $600/hour (includes technician)
- Access: Reserved 200 hours/year

**Cognitive Testing:**
- 20 iPads (NIHTB app pre-installed)
- Private testing rooms (Harvard Psychology Department)

**Data Management:**
- REDCap server (Harvard Catalyst IT)
- Secure file server (10 TB storage)

---

## Success Metrics

✓ Recruit N=800 participants within 12 months
✓ Retain ≥55% at Year 5 follow-up
✓ 80% compliance with app monitoring
✓ Detect longitudinal association (p<0.001) if true effect size r≥0.15
✓ RCT shows ≥20% symptom reduction (depression)
✓ Publish 8+ papers in top-tier journals
✓ Influence AAP guidelines (cited in policy update)

---

**Prepared by:** Dr. Sarah Chen & Team
**Last Updated:** December 27, 2025
**Version:** 4.2

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Executive Summary - Psychology]** `psychology-executive-summary-example.md` - Type: `informs` | Condition: `when domain === 'psychology'`
- **[IRB Approval]** `compliance/IRB-2024-1234.pdf` - Type: `requires` | Status: `approved`
- **[Literature Review]** `evidence/social_media_literature_review_2024.md` - Type: `requires` | Evidence ID: `E-PSYCH-002`

### Impacts (Downstream Documents)
- **[TDD - Psychology]** `psychology-tdd-example.md` - Type: `blocks` | Until: `this.status == approved` | Cascade: `true`
- **[Test Plan]** `docs/testing/psychology_data_test_plan.md` - Type: `informs`

### Related Documents
- **[Biology Research Plan]** `biology-research-plan-example.md` - Relationship: `parallel-example`
- **[Chemistry Research Plan]** `chemistry-research-plan-example.md` - Relationship: `parallel-example`
- **[Physics Research Plan]** `physics-research-plan-example.md` - Relationship: `parallel-example`

### Satellite Documents
- **[TODO]** `satellites/TODO-RESPLAN-PSYCH-001.md` - Status: `completed`
- **[DOR]** `satellites/DOR-RESPLAN-PSYCH-001.md` - Status: `met`
- **[DOD]** `satellites/DOD-RESPLAN-PSYCH-001.md` - Status: `met`

### Conditional Cross-References
```yaml
conditions:
  - when: domain === 'psychology'
    require_dependencies: [IRB Approval, HIPAA compliance, Informed consent, Recruitment materials]
    require_satellites: [IRB Protocol, Consent Repository, Data Privacy Assessment]
  - when: involves_children === true
    require_dependencies: [Parental consent, Child assent, Mandated reporter training]
  - when: involves_fmri === true
    require_dependencies: [MRI Safety Screening, Radiologist oversight, Scanner access]
  - when: clinical_trial === true
    require_dependencies: [ClinicalTrials.gov registration, DSMB charter, Adverse event plan]
  - when: longitudinal_study === true
    require_dependencies: [Retention strategy, Data management for repeated measures]
```

### Validation Rules
**BLOCKER:** All dependencies approved, IRB current, Recruitment feasible, Sample size justified
**ERROR:** Attrition realistic, Measurement instruments validated, Statistical plan appropriate
**WARN:** DEI in recruitment, Open science practices, Community engagement
