# Technical Design Document: DigitalMinds Project
## Data Management, App Development, and Analysis Infrastructure

**Project ID:** NIH-R01-2024-8721
**Technical Lead:** Dr. Michael Roberts
**Data Manager:** Emily Johnson, MPH
**Version:** 3.3 | **Date:** December 27, 2025

---

## 1. System Architecture

```
┌──────────────────────────────────────────────────────────┐
│              PARTICIPANT-FACING LAYER                     │
├──────────────────────────────────────────────────────────┤
│  Mobile App (Android/iOS) → Screen time monitoring        │
│  REDCap Surveys → Self-report questionnaires (home)      │
│  MetricWire EMA → Real-time mood/activity prompts        │
│  Lab iPads → Cognitive testing (NIHTB)                   │
└──────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────┐
│              DATA COLLECTION LAYER                        │
├──────────────────────────────────────────────────────────┤
│  App Backend → Aggregate screen time logs (daily sync)   │
│  REDCap Server → Survey responses (HTTPS POST)           │
│  EMA API → Momentary assessments (JSON)                  │
│  NIHTB Portal → Cognitive test scores (CSV export)       │
│  MRI Console → DICOM files (neuroimaging)                │
└──────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────┐
│              DATA STORAGE LAYER                           │
├──────────────────────────────────────────────────────────┤
│  PostgreSQL → Structured data (participants, visits)     │
│  MongoDB → Semi-structured (app logs, EMA JSON)          │
│  XNAT → MRI data (DICOM storage + metadata)              │
│  AWS S3 → Raw files (video interviews, consent forms)    │
└──────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────┐
│              ANALYSIS LAYER                               │
├──────────────────────────────────────────────────────────┤
│  R (lme4, lavaan) → Longitudinal modeling, SEM           │
│  Python (pandas, scipy) → Data wrangling, statistics     │
│  FSL, SPM → fMRI preprocessing + analysis                │
│  Jupyter Notebooks → Reproducible analysis pipelines     │
└──────────────────────────────────────────────────────────┘
```

---

## 2. Data Models

### 2.1 Relational Database (PostgreSQL)

#### Table: `participants`

```sql
CREATE TABLE participants (
    participant_id VARCHAR(20) PRIMARY KEY,  -- e.g., "DM-001"
    enrollment_date DATE NOT NULL,

    -- Demographics
    date_of_birth DATE NOT NULL,
    age_at_enrollment DECIMAL(4,2),  -- computed: years
    gender ENUM('Male', 'Female', 'Non-binary', 'Prefer not to say'),
    race_ethnicity TEXT[],  -- array: can select multiple

    -- Family
    parent_name VARCHAR(200),
    parent_email VARCHAR(200),
    parent_phone VARCHAR(20),
    family_income_bracket ENUM('<$50k', '$50-100k', '$100-150k', '>$150k', 'Prefer not to say'),
    parent_education ENUM('Less than HS', 'HS diploma', 'Some college', 'College degree', 'Graduate degree'),

    -- Study eligibility
    has_smartphone BOOLEAN DEFAULT TRUE,
    english_fluent BOOLEAN DEFAULT TRUE,
    diagnosed_adhd BOOLEAN DEFAULT FALSE,
    diagnosed_autism BOOLEAN DEFAULT FALSE,

    -- Randomization (RCT)
    rct_eligible BOOLEAN DEFAULT FALSE,
    rct_randomized BOOLEAN DEFAULT FALSE,
    rct_arm ENUM('intervention', 'control', NULL),
    rct_randomization_date DATE,

    -- Retention
    active BOOLEAN DEFAULT TRUE,
    withdrawal_date DATE,
    withdrawal_reason TEXT,

    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_participants_age ON participants(age_at_enrollment);
CREATE INDEX idx_participants_rct ON participants(rct_arm) WHERE rct_randomized = TRUE;
```

#### Table: `visits`

```sql
CREATE TABLE visits (
    visit_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id VARCHAR(20) REFERENCES participants(participant_id),

    -- Visit info
    visit_type ENUM('baseline', 'month_6', 'month_12', 'month_18', 'month_24',
                    'month_30', 'month_36', 'month_42', 'month_48', 'month_54', 'month_60',
                    'rct_pre', 'rct_post'),
    scheduled_date DATE NOT NULL,
    actual_date DATE,
    visit_status ENUM('scheduled', 'completed', 'missed', 'rescheduled'),

    -- Completion
    consent_signed BOOLEAN DEFAULT FALSE,
    cognitive_testing_complete BOOLEAN DEFAULT FALSE,
    surveys_complete BOOLEAN DEFAULT FALSE,
    mri_complete BOOLEAN DEFAULT FALSE,
    blood_draw_complete BOOLEAN DEFAULT FALSE,  -- optional genetics

    -- Compensation
    compensation_amount DECIMAL(6,2),
    compensation_paid BOOLEAN DEFAULT FALSE,
    payment_method ENUM('check', 'gift_card', 'paypal'),

    -- Staff
    coordinator VARCHAR(100),
    ra_tester VARCHAR(100),

    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_visits_participant ON visits(participant_id);
CREATE INDEX idx_visits_type ON visits(visit_type);
CREATE INDEX idx_visits_status ON visits(visit_status);
```

#### Table: `cognitive_scores`

```sql
CREATE TABLE cognitive_scores (
    score_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    visit_id UUID REFERENCES visits(visit_id),
    participant_id VARCHAR(20) REFERENCES participants(participant_id),

    -- NIH Toolbox scores (age-corrected standard scores, M=100, SD=15)
    flanker_inhibition_score INTEGER,
    flanker_inhibition_percentile INTEGER,

    list_sorting_wm_score INTEGER,
    list_sorting_wm_percentile INTEGER,

    dccs_flexibility_score INTEGER,
    dccs_flexibility_percentile INTEGER,

    pattern_comparison_speed_score INTEGER,

    fluid_cognition_composite INTEGER,  -- overall executive function

    -- CPT (continuous performance task)
    cpt_omissions INTEGER,  -- missed targets (attention lapses)
    cpt_commissions INTEGER,  -- false alarms (impulsivity)
    cpt_mean_rt_ms DECIMAL(7,2),  -- reaction time
    cpt_rt_variability_sd DECIMAL(7,2),

    -- Achievement (WIAT-III, grade-level equivalent)
    reading_comprehension_grade_equiv DECIMAL(4,2),
    math_problem_solving_grade_equiv DECIMAL(4,2),

    -- Quality control
    valid_administration BOOLEAN DEFAULT TRUE,
    invalid_reason TEXT,  -- e.g., "child refused midway", "technical issues"

    administered_date DATE,
    administered_by VARCHAR(100),

    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `mental_health_scores`

```sql
CREATE TABLE mental_health_scores (
    score_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    visit_id UUID REFERENCES visits(visit_id),
    participant_id VARCHAR(20) REFERENCES participants(participant_id),

    -- Depression (CDI-2: 0-56, higher = more severe)
    cdi2_total INTEGER,
    cdi2_emotional_problems INTEGER,  -- subscale
    cdi2_functional_problems INTEGER,
    cdi2_clinical_cutoff BOOLEAN,  -- TRUE if >19

    -- Anxiety (SCARED: 0-82)
    scared_total INTEGER,
    scared_generalized_anxiety INTEGER,  -- subscale
    scared_social_phobia INTEGER,
    scared_separation_anxiety INTEGER,
    scared_panic INTEGER,

    -- Self-Esteem (Rosenberg: 0-30, higher = better)
    rosenberg_total INTEGER,

    -- Social Media Addiction (SMAS: 0-27, higher = more problematic)
    smas_total INTEGER,
    smas_compulsive_use INTEGER,
    smas_withdrawal INTEGER,
    smas_tolerance INTEGER,

    completed_date DATE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `screen_time_daily`

```sql
CREATE TABLE screen_time_daily (
    record_id BIGSERIAL PRIMARY KEY,
    participant_id VARCHAR(20) REFERENCES participants(participant_id),
    date DATE NOT NULL,

    -- Total screen time (minutes)
    total_screen_time_min INTEGER,
    num_pickups INTEGER,  -- phone unlocks

    -- App-specific (minutes per app)
    tiktok_min INTEGER DEFAULT 0,
    instagram_min INTEGER DEFAULT 0,
    snapchat_min INTEGER DEFAULT 0,
    facebook_min INTEGER DEFAULT 0,
    youtube_min INTEGER DEFAULT 0,
    twitter_min INTEGER DEFAULT 0,
    messaging_min INTEGER DEFAULT 0,  -- WhatsApp, Messenger, iMessage
    games_min INTEGER DEFAULT 0,
    other_min INTEGER DEFAULT 0,

    -- Time of day distribution
    morning_6am_12pm_min INTEGER,  -- 6am-12pm
    afternoon_12pm_6pm_min INTEGER,  -- 12pm-6pm
    evening_6pm_10pm_min INTEGER,  -- 6pm-10pm
    late_night_10pm_6am_min INTEGER,  -- 10pm-6am (sleep disruption)

    -- Data quality
    data_valid BOOLEAN DEFAULT TRUE,
    invalid_reason TEXT,  -- e.g., "app uninstalled", "phone off"

    synced_at TIMESTAMP DEFAULT NOW(),

    UNIQUE(participant_id, date)
);

CREATE INDEX idx_screentime_participant_date ON screen_time_daily(participant_id, date);
CREATE INDEX idx_screentime_date ON screen_time_daily(date);
```

#### Table: `ema_responses`

```sql
CREATE TABLE ema_responses (
    response_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id VARCHAR(20) REFERENCES participants(participant_id),

    -- Prompt info
    prompt_timestamp TIMESTAMP NOT NULL,
    response_timestamp TIMESTAMP,
    time_to_respond_seconds INTEGER,  -- latency

    -- Responses
    current_activity ENUM('social_media', 'homework', 'sports', 'tv', 'socializing_inperson',
                          'reading', 'video_games', 'other'),

    mood_happy INTEGER CHECK (mood_happy BETWEEN 1 AND 10),
    mood_anxious INTEGER CHECK (mood_anxious BETWEEN 1 AND 10),
    mood_lonely INTEGER CHECK (mood_lonely BETWEEN 1 AND 10),
    mood_bored INTEGER CHECK (mood_bored BETWEEN 1 AND 10),

    just_used_social_media BOOLEAN,
    social_media_duration_min INTEGER,  -- if yes, for how long?

    -- Compliance
    responded BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_ema_participant ON ema_responses(participant_id);
CREATE INDEX idx_ema_timestamp ON ema_responses(prompt_timestamp);
```

---

## 3. Mobile App Development

### 3.1 App Specification

**Platform:** Cross-platform (React Native)

**Features:**

1. **Screen Time Monitoring:**
   - Background service tracks app usage (Android: UsageStatsManager, iOS: ScreenTime API)
   - Aggregate daily totals (per app, total)
   - Upload to server daily (WiFi only, encrypted)

2. **Consent & Onboarding:**
   - Display informed consent document
   - Capture parent e-signature (via react-native-signature-capture)
   - Tutorial: How to grant permissions (usage access, notifications)

3. **EMA Integration:**
   - Receive push notifications (3× daily) from MetricWire server
   - Display 5-question survey (30 seconds to complete)
   - Save responses locally → sync when online

4. **Participant Dashboard:**
   - View own screen time trends (daily bar chart)
   - Upcoming visit reminders
   - Contact study team (email, phone)

**Privacy:**
- No content access (only app names + duration)
- End-to-end encryption (AES-256)
- Opt-out: User can pause monitoring anytime

**Technical Stack:**
- **Frontend:** React Native (JavaScript), React Navigation
- **Backend:** Node.js (Express), PostgreSQL
- **Push Notifications:** Firebase Cloud Messaging (FCM)
- **Deployment:** Apple App Store (TestFlight for beta), Google Play (internal testing track)

### 3.2 Backend API

**Architecture:** RESTful API (Node.js + Express)

**Endpoints:**

```javascript
// POST /api/screentime/upload
// Upload daily screen time data

router.post('/screentime/upload', authenticate, (req, res) => {
    const { participant_id, date, app_usage } = req.body;

    // Validate
    if (!participant_id || !date) {
        return res.status(400).json({ error: 'Missing required fields' });
    }

    // Insert into database
    const query = `
        INSERT INTO screen_time_daily (
            participant_id, date, total_screen_time_min,
            tiktok_min, instagram_min, snapchat_min, ...
        ) VALUES ($1, $2, $3, $4, $5, $6, ...)
        ON CONFLICT (participant_id, date)
        DO UPDATE SET
            total_screen_time_min = EXCLUDED.total_screen_time_min,
            tiktok_min = EXCLUDED.tiktok_min, ...
    `;

    db.query(query, [participant_id, date, app_usage.total, app_usage.tiktok, ...])
        .then(() => res.json({ success: true }))
        .catch(err => res.status(500).json({ error: err.message }));
});

// GET /api/participants/:id/visits
// Retrieve upcoming visits for participant

router.get('/participants/:id/visits', authenticate, (req, res) => {
    const { id } = req.params;

    const query = `
        SELECT visit_id, visit_type, scheduled_date, visit_status
        FROM visits
        WHERE participant_id = $1 AND visit_status IN ('scheduled', 'rescheduled')
        ORDER BY scheduled_date ASC
        LIMIT 5
    `;

    db.query(query, [id])
        .then(result => res.json({ visits: result.rows }))
        .catch(err => res.status(500).json({ error: err.message }));
});
```

**Authentication:**
- JWT tokens (JSON Web Token)
- Login: Parent provides email + password (set during enrollment) → receive token
- Token expires after 30 days (auto-refresh)

**Rate Limiting:**
- 100 requests/hour per participant (prevent abuse)

---

## 4. Data Management

### 4.1 REDCap Configuration

**Projects:**

1. **Main Study Database:**
   - Participant demographics, visit scheduling, cognitive scores, mental health
   - Instruments (forms):
     - Enrollment Form (demographics, contact info)
     - Cognitive Testing Form (NIHTB scores, manual entry by RA)
     - Mental Health Survey (CDI-2, SCARED, Rosenberg - participant self-report)
     - Visit Checklist (track completion: consent, testing, compensation)

2. **Longitudinal Setup:**
   - Events: Baseline, Month 6, Month 12, ..., Month 60
   - Repeating instruments: Mental Health Survey (every 6 months)

3. **Data Quality Rules:**
   - Logic checks: Age cannot be <8 or >14 at baseline
   - Required fields: Participant ID, enrollment date
   - Range checks: CDI-2 total must be 0-56

**Access Control:**
- **Full Access:** PI, Co-PIs, Data Manager (read/write all data)
- **Limited Access:** RAs (read/write only for assigned participants)
- **De-identified Export:** Statisticians (no names, birthdates)

### 4.2 MRI Data Management (XNAT)

**XNAT Server:** Harvard-hosted instance (https://xnat.harvard.edu/digitalminds)

**Workflow:**

1. **Acquisition:** MRI console → DICOM files saved to local server
2. **Upload:** Automated script (cron job) transfers DICOMs to XNAT (nightly)
3. **Organization:**
   - Project: DigitalMinds
   - Subject: Participant ID (e.g., DM-001)
   - Session: Visit type + date (e.g., DM-001_baseline_2024-06-15)
   - Scan: T1w, rs-fMRI, task-fMRI, dMRI

4. **Quality Control Pipeline:**
   - MRIQC (automated QC metrics: motion, SNR, contrast)
   - Flag scans with excessive motion (>3mm framewise displacement)
   - Radiologist review (incidental findings)

**Access:**
- Neuroimaging team (read/write)
- External collaborators (read-only, approved by PI)

### 4.3 Data Security & Compliance

**HIPAA Compliance:**
- Business Associate Agreement (BAA) with Harvard IT
- Encrypted data at rest (AES-256) and in transit (TLS 1.3)
- Audit logs (track all data access, downloads)

**IRB Requirements:**
- Annual renewal (report enrollment, adverse events)
- Consent forms stored separately from data (locked cabinet + encrypted PDF)
- Data retention: 7 years post-study completion (NIH requirement)

**Breach Protocol:**
- Incident response plan (notify IRB, participants, HIPAA officer within 72 hours)
- Annual security training for all staff (CITI program)

---

## 5. Analysis Infrastructure

### 5.1 Computational Environment

**Primary Analysis Server:**
- **Hardware:** Dell PowerEdge R740 (dual 16-core Xeon, 512GB RAM, 50TB RAID storage)
- **OS:** Ubuntu 22.04 LTS
- **Software:**
  - R 4.3 (lme4, lavaan, ggplot2)
  - Python 3.11 (pandas, scipy, scikit-learn)
  - FSL 6.0, SPM12 (fMRI analysis)
  - MATLAB R2023a (for SPM)

**Version Control:**
- GitHub repository (private during study, public post-publication)
- Pre-commit hooks (run code formatting, lint checks)

**Reproducibility:**
- Docker containers for analysis environment (ensure consistency)
- Renv (R) / Conda (Python) for package management
- Jupyter notebooks for all primary analyses (literate programming)

### 5.2 Statistical Analysis Scripts

**Example: Longitudinal Model (R)**

```r
# File: scripts/aim1_longitudinal_lmm.R

library(lme4)
library(dplyr)
library(ggplot2)

# Load data
data <- read.csv("data/processed/longitudinal_dataset.csv")

# Prepare variables
data$time_months <- as.numeric(difftime(data$visit_date, data$enrollment_date, units = "days")) / 30.44
data$social_media_hours <- data$total_screen_time_min / 60

# Fit linear mixed model
model <- lmer(
    fluid_cognition_composite ~
        social_media_hours * time_months +  # main effect + interaction
        age_at_enrollment + gender + family_income_bracket +  # covariates
        (1 + time_months | participant_id),  # random intercept + slope
    data = data,
    REML = FALSE  # maximum likelihood for model comparison
)

# Results
summary(model)

# Extract coefficients
coef_summary <- summary(model)$coefficients
write.csv(coef_summary, "results/aim1_lmm_coefficients.csv")

# Visualize
ggplot(data, aes(x = social_media_hours, y = fluid_cognition_composite)) +
    geom_point(alpha = 0.3) +
    geom_smooth(method = "lm", color = "blue") +
    facet_wrap(~visit_type) +
    labs(x = "Social Media Use (hours/day)",
         y = "Executive Function (Fluid Cognition Composite)",
         title = "Association between Social Media Use and Cognition") +
    theme_minimal()

ggsave("figures/aim1_scatterplot.png", width = 10, height = 6)
```

### 5.3 fMRI Analysis Pipeline

**Preprocessing (FSL FEAT):**

```bash
# File: scripts/fmri_preprocessing.sh

#!/bin/bash

SUBJECT_ID=$1
SESSION=$2

DATA_DIR="/data/xnat/${SUBJECT_ID}/${SESSION}"
OUTPUT_DIR="/data/processed/fmri/${SUBJECT_ID}/${SESSION}"

# Brain extraction (skull stripping)
bet ${DATA_DIR}/T1w.nii.gz ${OUTPUT_DIR}/T1w_brain.nii.gz -f 0.5 -g 0

# Motion correction (MCFLIRT)
mcflirt -in ${DATA_DIR}/rsfMRI.nii.gz -out ${OUTPUT_DIR}/rsfMRI_mc.nii.gz -plots

# Slice timing correction
slicetimer -i ${OUTPUT_DIR}/rsfMRI_mc.nii.gz -o ${OUTPUT_DIR}/rsfMRI_st.nii.gz -r 2

# Spatial smoothing (6mm FWHM)
fslmaths ${OUTPUT_DIR}/rsfMRI_st.nii.gz -s 2.55 ${OUTPUT_DIR}/rsfMRI_smooth.nii.gz

# High-pass temporal filter (128s)
fslmaths ${OUTPUT_DIR}/rsfMRI_smooth.nii.gz -bptf 64 -1 ${OUTPUT_DIR}/rsfMRI_filtered.nii.gz

# Registration to MNI152 standard space
flirt -in ${OUTPUT_DIR}/T1w_brain.nii.gz -ref /usr/share/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz \
    -out ${OUTPUT_DIR}/T1w_to_MNI.nii.gz -omat ${OUTPUT_DIR}/T1w_to_MNI.mat

echo "Preprocessing complete for ${SUBJECT_ID} ${SESSION}"
```

**Connectivity Analysis (Python + Nilearn):**

```python
# File: scripts/fmri_connectivity.py

from nilearn import datasets, input_data, plotting, connectome
import numpy as np
import pandas as pd

def compute_connectivity(subject_id, session):
    """Compute functional connectivity matrix"""

    # Load preprocessed fMRI
    fmri_file = f"/data/processed/fmri/{subject_id}/{session}/rsfMRI_filtered.nii.gz"

    # Define atlas (Power 264 ROIs)
    atlas = datasets.fetch_coords_power_2011()
    coords = np.vstack([atlas.rois['x'], atlas.rois['y'], atlas.rois['z']]).T

    # Extract time series
    masker = input_data.NiftiSpheresMasker(
        seeds=coords,
        radius=5,  # 5mm sphere around each coordinate
        detrend=True,
        standardize=True,
        low_pass=0.1,
        high_pass=0.01,
        t_r=2
    )
    time_series = masker.fit_transform(fmri_file)

    # Compute correlation matrix
    correlation_matrix = connectome.ConnectivityMeasure(kind='correlation')
    connectivity = correlation_matrix.fit_transform([time_series])[0]

    # Save
    np.save(f"results/connectivity/{subject_id}_{session}_connectivity.npy", connectivity)

    # Visualize
    plotting.plot_matrix(connectivity, figure=(10, 8),
                         title=f"{subject_id} - {session}")
    plotting.savefig(f"figures/connectivity/{subject_id}_{session}_matrix.png")

    return connectivity

# Run for all participants
participants = pd.read_csv("data/participant_list.csv")
for idx, row in participants.iterrows():
    compute_connectivity(row['participant_id'], 'baseline')
```

---

## 6. Deployment & Operations

### 6.1 Infrastructure (AWS)

**Services Used:**
- **EC2:** t3.xlarge instance for web server (Node.js API)
- **RDS:** PostgreSQL database (db.t3.large, 500GB storage)
- **S3:** Raw file storage (consent forms, video interviews) - 10TB
- **CloudWatch:** Monitoring (API latency, database CPU)

**Backup Strategy:**
- **Database:** Daily automated snapshots (RDS), retain 30 days
- **Files:** S3 versioning enabled, lifecycle policy (archive to Glacier after 90 days)
- **Disaster Recovery:** Cross-region replication (US East → US West)

### 6.2 Monitoring & Alerts

**Metrics:**
- API response time (target <500ms p95)
- Database connections (alert if >80% capacity)
- App sync success rate (alert if <90% of participants synced in last 7 days)

**Alerts:**
- Slack notifications for critical issues (database down, API errors >10/min)
- Weekly summary email (enrollment numbers, data quality flags)

---

## 7. Performance Requirements

### Data Volume Estimates

**Per Participant (5 years):**
- Screen time logs: 1 KB/day × 1,825 days = 1.8 MB
- Surveys: 50 KB/visit × 11 visits = 550 KB
- Cognitive tests: 100 KB/visit × 11 visits = 1.1 MB
- MRI scans: 5 GB/session × 3 sessions = 15 GB (for neuroimaging subsample)
- **Total:** ~15-20 GB/participant (if neuroimaging), ~5 MB (if behavioral only)

**Total Study:**
- N=800 participants × 5 MB = 4 GB (behavioral data)
- N=200 neuroimaging × 15 GB = 3 TB (neuroimaging data)
- **Grand Total:** ~3.1 TB (raw + processed data)

### Processing Throughput

- **Cognitive testing:** 20 participants/day (4 concurrent testing rooms, 90 min/participant)
- **MRI scanning:** 5 participants/day (2-hour slots: 1h scan + 30min setup/breakdown)
- **Data processing:** fMRI preprocessing 4 hours/participant (overnight batch jobs, 10 concurrent)

---

**Prepared by:** Dr. Michael Roberts & Emily Johnson, MPH
**Last Updated:** December 27, 2025
**Version:** 3.3

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Research Plan - Psychology]** `psychology-research-plan-example.md` - Type: `requires` | Status: `approved` | Condition: `when domain === 'psychology'`
- **[Executive Summary - Psychology]** `psychology-executive-summary-example.md` - Type: `informs`
- **[Data Model Schema]** `schemas/psychology_longitudinal_schema.json` - Type: `requires` | Evidence ID: `E-PSYCH-TDD-001`
- **[IRB Data Requirements]** `compliance/IRB_data_security_requirements.pdf` - Type: `requires`

### Impacts (Downstream Documents)
- **[Implementation Tasks]** `jira/PSYCH-TDD-IMPLEMENTATION-EPIC` - Type: `blocks` | Until: `this.status == approved` | Cascade: `true`
- **[Runbook]** `docs/ops/psychology_platform_runbook.md` - Type: `informs`
- **[Test Plan]** `docs/testing/psychology_system_test_plan.md` - Type: `informs`
- **[Security Plan]** `docs/security/psychology_hipaa_security_plan.md` - Type: `blocks` | Until: `this.status == in-review`

### Related Documents
- **[Biology TDD]** `biology-tdd-example.md` - Relationship: `parallel-example`
- **[Chemistry TDD]** `chemistry-tdd-example.md` - Relationship: `parallel-example`
- **[Physics TDD]** `physics-tdd-example.md` - Relationship: `parallel-example`

### Satellite Documents
- **[TODO]** `satellites/TODO-TDD-PSYCH-001.md` - Status: `completed`
- **[DOR]** `satellites/DOR-TDD-PSYCH-001.md` - Status: `met`
- **[DOD]** `satellites/DOD-TDD-PSYCH-001.md` - Status: `met`
- **[ADR Collection]** `satellites/ADR-TDD-PSYCH-*.md` - Key decisions on HIPAA compliance, data anonymization, mobile app integration

### Conditional Cross-References
```yaml
conditions:
  - when: domain === 'psychology'
    require_dependencies: [IRB data security requirements, HIPAA compliance architecture]
    require_satellites: [ADR for data anonymization, ADR for mobile data collection]
    data_model_requirements: [Participant entity with consent tracking, Data access audit trail]
  - when: involves_phi === true
    require_dependencies: [HIPAA compliance architecture, IRB data security]
    security_requirements: [PHI encryption HIPAA standard, Audit logging all access, De-identification pipeline]
  - when: mobile_data_collection === true
    require_dependencies: [Mobile app security assessment, App store compliance review]
    infrastructure_requirements: [Mobile backend API, Push notification service, Offline data sync]
  - when: longitudinal_study === true
    require_dependencies: [Participant retention system, Automated follow-up reminders]
    data_model_requirements: [Time-series data models, Missingness tracking, Attrition analysis]
```

### Validation Rules
**BLOCKER:** All dependencies approved, HIPAA compliance verified, IRB data security met, Consent tracking implemented
**ERROR:** Database optimized for longitudinal queries, Mobile app security tested, Backup/restore validated
**WARN:** Participant dashboard usability, Data export formats, Cost optimization for cloud services
