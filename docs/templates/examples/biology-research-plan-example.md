# Research Plan: NeuroRegen Project
## Detailed Experimental Design and Methodology

**Project ID:** NSF-BIO-2024-7821
**PI:** Dr. Maria Kowalska
**Version:** 3.2
**Date:** December 27, 2025

---

## Research Questions

### Primary Research Questions

**RQ1:** Which genes and gene regulatory networks are differentially activated between regeneration-competent (zebrafish) and regeneration-incompetent (mouse) vertebrate neural tissue following spinal cord injury?

**RQ2:** Are the identified regeneration-associated genes both necessary (in zebrafish) and sufficient (in mouse) to drive neural regeneration?

**RQ3:** What are the cellular and molecular mechanisms through which these master regulators promote regeneration (e.g., dedifferentiation, proliferation, axon guidance)?

**RQ4:** Can mammalian regenerative capacity be enhanced to clinically meaningful levels through targeted expression of regeneration master regulators?

### Secondary Research Questions

**RQ5:** What is the single-cell transcriptomic landscape of regenerating zebrafish spinal cord, and which cell types express regeneration-associated genes?

**RQ6:** Are regeneration programs conserved across multiple regeneration-competent species (zebrafish vs. axolotl)?

**RQ7:** What is the temporal dynamics of regeneration gene activation (acute vs. chronic phases)?

---

## Hypotheses

### Central Hypothesis

**H0 (Null):** Regenerative capacity differences between zebrafish and mouse result from quantitative differences in broadly expressed genes, with no distinct master regulators.

**H1 (Alternative):** A discrete set of master transcription factors and signaling molecules (10-50 genes) are selectively activated in regeneration-competent species and are both necessary and sufficient for neural regeneration.

### Mechanistic Hypotheses

**H2:** Regeneration master regulators function by reactivating developmental gene programs, inducing partial cellular dedifferentiation at the injury site.

**H3:** These genes act in a combinatorial manner - multiple genes are required together to achieve full regenerative response.

**H4:** The regeneration program involves cell-type-specific responses, with distinct gene sets activated in neurons, glia, and neural stem/progenitor cells.

**H5:** Ectopic expression of zebrafish regeneration genes in mouse will partially restore regenerative capacity, measurable as increased axon regrowth (>20% vs. control) and functional improvement (>10% BBB score increase).

### Testable Predictions

- **P1:** Zebrafish will show >500 genes with |log2FC| > 2 (padj < 0.01) vs. mouse at peak regeneration timepoint (7d post-injury)
- **P2:** These genes will be enriched for GO terms: development, cell proliferation, axon guidance (hypergeometric test p < 1e-10)
- **P3:** CRISPR knockout of top candidates in zebrafish will reduce regeneration index by >40%
- **P4:** AAV-mediated expression in mouse will increase axon length beyond lesion by >2-fold vs. GFP control

---

## Methodology

### Aim 1: Comparative Transcriptomic Analysis

#### 1.1 Animal Models

**Zebrafish (*Danio rerio*):**
- Strain: AB wildtype
- Age: 5 days post-fertilization (dpf) larvae
- Rationale: Larvae are optically transparent, show robust spinal cord regeneration, cost-effective
- Sample size: N=30 per timepoint per condition (180 total for bulk RNA-seq)
- Housing: 28.5°C, 14:10 light:dark cycle, IACUC protocol #2024-0456

**Mouse (*Mus musculus*):**
- Strain: C57BL/6J (Jackson Labs #000664)
- Age: 8-10 weeks (young adult)
- Sex: Balanced (50% male, 50% female)
- Sample size: N=30 per timepoint per condition (180 total for bulk RNA-seq)
- Housing: Specific pathogen-free (SPF), 12:12 light:dark, IACUC protocol #2024-0457

#### 1.2 Injury Models

**Zebrafish Spinal Cord Transection:**
- **Procedure:** Complete transection at somite level 10-12 using sapphire blade (World Precision Instruments)
- **Anesthesia:** 0.02% tricaine (MS-222) in E3 medium
- **Post-injury care:** Return to 28.5°C E3 medium, monitor for 30min
- **Success criteria:** Complete transection confirmed by DIC microscopy (100% loss of GFP+ axons in Tg(mbp:GFP) reporter line)
- **Survival rate:** >95% expected

**Mouse Spinal Cord Hemisection:**
- **Procedure:** T10 dorsal hemisection (0.8mm depth) using Vibraknife (World Precision Instruments)
- **Anesthesia:** Isoflurane (2% induction, 1.5% maintenance) + pre-op carprofen (5mg/kg SC)
- **Surgical approach:** Dorsal laminectomy, dura intact
- **Post-injury care:**
  - Buprenorphine SR (1mg/kg SC, single dose, 72h coverage)
  - Manual bladder expression 2x daily until reflex returns (typically 7-10 days)
  - Antibiotics: Enrofloxacin in water (200mg/L) for 7 days
- **Success criteria:** Complete hemisection confirmed by post-sacrifice histology (loss of descending tracts on lesion side)
- **Survival rate:** >90% expected (based on pilot data)

#### 1.3 Tissue Collection

**Timepoints:** 0h (uninjured baseline), 6h, 24h, 3d, 7d, 14d post-injury

**Zebrafish:**
- Dissection: 2mm spinal cord segment centered on injury (±1mm from lesion epicenter)
- Protocol: Anesthetize in tricaine → decapitate → dissect under stereomicroscope
- Tissue preservation: Snap freeze in liquid N2 → store -80°C until RNA extraction
- RNA extraction: TRIzol (Invitrogen), followed by RNeasy cleanup (Qiagen)
- Quality control: Bioanalyzer (target RIN > 7.0)

**Mouse:**
- Dissection: 4mm spinal cord segment centered on injury (±2mm from lesion)
- Protocol: Transcardial perfusion with ice-cold PBS → dissect under stereomicroscope
- Tissue preservation: Snap freeze in liquid N2 → store -80°C
- RNA extraction: RNeasy Lipid Tissue Mini Kit (Qiagen)
- Quality control: Bioanalyzer (target RIN > 7.5)

#### 1.4 Bulk RNA Sequencing

**Library Preparation:**
- Kit: TruSeq Stranded mRNA Library Prep (Illumina)
- Input: 500ng total RNA per sample
- Poly-A selection: Yes (removes rRNA, enriches for mRNA)
- Fragmentation: 200bp average insert size
- Barcoding: Dual unique indexes (UDIs) to prevent index hopping
- Quantification: Qubit + Bioanalyzer

**Sequencing:**
- Platform: NovaSeq 6000 (Illumina)
- Configuration: Paired-end 150bp (PE150)
- Depth: 50 million read pairs per sample
- Multiplexing: 48 samples per S4 flow cell lane
- Provider: UCSD IGM Genomics Center
- Cost: $330/sample × 360 samples = $118,800

**Quality Control:**
- Per-base quality score: >Q30 for 85% of bases
- Adapter contamination: <5%
- Duplication rate: <30%
- Failed samples: Re-sequence once; exclude if second QC failure

#### 1.5 Bioinformatics Analysis

**Preprocessing:**
1. **Quality Control:** FastQC v0.12.1 → MultiQC v1.14 report
2. **Trimming:** Trim Galore v0.6.7 (remove adapters, quality trimming Q>20)
3. **Alignment:**
   - Zebrafish: STAR v2.7.10b to GRCz11 (Ensembl release 108)
   - Mouse: STAR v2.7.10b to GRCm39 (Ensembl release 108)
   - Parameters: --outFilterMultimapNmax 10 --alignSJoverhangMin 8
4. **Quantification:** featureCounts v2.0.3 (gene-level counts, Ensembl GTF annotation)

**Differential Expression:**
- **Software:** DESeq2 v1.38.0 (R/Bioconductor)
- **Design formula:** `~ species + timepoint + species:timepoint`
  - Tests for species-specific temporal responses
- **Normalization:** Median-of-ratios method (DESeq2 default)
- **Statistical test:** Wald test for pairwise comparisons
- **Multiple testing correction:** Benjamini-Hochberg FDR
- **Significance thresholds:**
  - Adjusted p-value (padj) < 0.01
  - |log2 Fold Change| > 2 (4-fold difference)
- **Contrasts of interest:**
  - Zebrafish 7d vs. 0h (peak regeneration vs. baseline)
  - Mouse 7d vs. 0h (peak response vs. baseline)
  - (Zebrafish 7d vs. 0h) - (Mouse 7d vs. 0h) [interaction term]

**Pathway Analysis:**
- **Gene Set Enrichment Analysis (GSEA):**
  - Software: fgsea v1.24.0 (R)
  - Gene sets: MSigDB Hallmarks, GO Biological Processes, KEGG pathways
  - Statistic: Ranked by log2FC × -log10(pvalue)
  - Permutations: 10,000
  - FDR threshold: <0.05

- **Over-representation Analysis (ORA):**
  - Software: clusterProfiler v4.6.0 (R)
  - Input: Significant DE genes (padj < 0.01, |log2FC| > 2)
  - Background: All detected genes (mean count > 5)
  - Test: Hypergeometric test + Benjamini-Hochberg correction

**Cross-Species Mapping:**
- **Ortholog identification:** Ensembl Compara database (v108)
- **Criteria:** 1-to-1 orthologs only (excludes paralogs to simplify interpretation)
- **Coverage:** ~15,000 genes with confident 1-to-1 mouse-zebrafish orthologs
- **Analysis:** Compare regeneration response for orthologous gene pairs

**Visualization:**
- MA plots: log2FC vs. mean expression (identify magnitude vs. abundance patterns)
- Volcano plots: log2FC vs. -log10(padj) (identify significant genes)
- Heatmaps: Hierarchical clustering of top 500 DE genes (identify co-regulated modules)
- PCA: Sample relationships (identify batch effects, verify biological replicates cluster)
- Temporal profiles: Expression trajectories for genes of interest

**Computational Resources:**
- Server: UCSD TSCC HPC cluster
- Alignment: 16 cores, 64GB RAM per job, ~4h per sample
- DE analysis: 8 cores, 32GB RAM, ~30min for full dataset

**Reproducibility:**
- Version control: GitHub repository (https://github.com/kowalska-lab/neuroregen)
- Environment: Conda environment YAML + Docker container (Docker Hub: kowalska/neuroregen:v1.0)
- Analysis scripts: R Markdown notebooks for full workflow
- Data availability: Raw FASTQ deposited to SRA, processed counts to GEO

#### 1.6 Candidate Gene Prioritization

**Criteria for CRISPR validation (score-based ranking):**

1. **Magnitude of differential expression** (0-25 points)
   - log2FC in zebrafish 7d vs. 0h
   - >6: 25pt, 4-6: 15pt, 2-4: 5pt

2. **Species-specificity** (0-25 points)
   - Upregulated in zebrafish but NOT in mouse
   - log2FC_zebrafish - log2FC_mouse
   - >4: 25pt, 2-4: 15pt, 0-2: 5pt

3. **Functional annotation** (0-20 points)
   - Transcription factor: 20pt
   - Secreted signaling molecule: 15pt
   - Cell surface receptor: 10pt
   - Other: 5pt

4. **Pathway enrichment** (0-15 points)
   - Member of enriched regeneration-related pathway (development, proliferation, axon guidance)
   - GSEA NES >2: 15pt, 1.5-2: 10pt, <1.5: 5pt

5. **Temporal dynamics** (0-10 points)
   - Early activation (6-24h): 10pt [rapid response genes]
   - Mid activation (3-7d): 10pt [sustained regeneration]
   - Late only (14d): 5pt [remodeling]

6. **Expression specificity** (0-5 points)
   - Injury-specific (low baseline, high post-injury): 5pt
   - Constitutively expressed: 0pt

**Selection:** Top 20 genes (score >60) advance to CRISPR validation

**Expected profile of top candidate:**
- Transcription factor (e.g., sox2, klf4, myc family)
- log2FC >6 in zebrafish, <1 in mouse at 7d
- Activated 24h-7d post-injury
- Enriched in "developmental process" GO term
- Example: *sox2* - pluripotency TF, upregulated in regenerating zebrafish neural progenitors

---

### Aim 2: Functional Validation via CRISPR/Cas9

#### 2.1 CRISPR Design

**Guide RNA Design:**
- **Software:** Benchling CRISPR Design Tool + CRISPRscan for scoring
- **Criteria:**
  - Target exon 1 or 2 (early knockout → nonsense-mediated decay)
  - On-target score >60 (CRISPRscan)
  - Off-target analysis: 0 sites with <3 mismatches (CRISPOR)
  - GC content: 40-70%
- **Redundancy:** 2 independent guides per gene (test for allele-specific effects, confirm phenotype reproducibility)
- **Total guides:** 20 genes × 2 guides = 40 sgRNAs

**Synthesis:**
- **Template:** DNA oligos from IDT (Alt-R CRISPR-Cas9 system)
- **In vitro transcription:** HiScribe T7 Quick High Yield RNA Synthesis Kit (NEB)
- **Purification:** RNA Clean & Concentrator-25 (Zymo Research)
- **QC:** Bioanalyzer (single peak at ~100nt for sgRNA)
- **Storage:** -80°C in nuclease-free water, 20µM aliquots

**Cas9 Protein:**
- **Source:** Alt-R S.p. Cas9 Nuclease V3 (IDT)
- **Rationale:** Protein injection (vs. mRNA) gives faster cutting, less toxicity in zebrafish embryos
- **Concentration:** 1µg/µL stock
- **Storage:** -80°C, avoid freeze-thaw (single-use aliquots)

#### 2.2 Zebrafish Microinjection

**Injection Mix (per guide):**
- Cas9 protein: 300ng/µL (final)
- sgRNA: 100ng/µL (final)
- Phenol red: 0.05% (visualization)
- Total volume: 10µL (sufficient for ~200 injections)

**Procedure:**
- **Embryo preparation:** AB wildtype crosses, collect 0-15min post-fertilization
- **Injection:** 1-2nL into cytoplasm of 1-cell stage embryo
  - Needle: Borosilicate capillary, pulled with Sutter P-97 micropipette puller
  - Injector: Pneumatic PicoPump PV820 (World Precision Instruments)
  - Microscope: Leica M80 stereomicroscope
- **Injection rate:** 50-100 embryos per hour (experienced injector)
- **Post-injection:** Incubate in E3 medium at 28.5°C
- **QC:** Monitor at 24hpf for gross morphological abnormalities (exclude embryos with severe developmental defects)

**Sample size per guide:**
- Injected embryos: N=200
- Expected survival to 5dpf: 150 (75% survival typical)
- Genotyped: N=20 (confirm mutagenesis rate)
- Phenotyped post-injury: N=30 CRISPR + 30 uninjected controls

#### 2.3 Genotyping

**DNA Extraction:**
- **Source:** Fin clip (adult) or whole embryo (larvae)
- **Method:** HotSHOT protocol (alkaline lysis)
  - 50mM NaOH, 95°C for 20min → neutralize with 1M Tris-HCl pH 8.0
- **Yield:** ~50ng/µL (sufficient for PCR)

**Mutagenesis Detection:**
- **Primary screen:** T7 Endonuclease I (T7EI) assay
  - PCR amplify 400-600bp region surrounding cut site
  - Denature + reanneal (heteroduplex formation between WT and mutant alleles)
  - T7EI digestion (cuts heteroduplexes)
  - Gel electrophoresis: 2% agarose, cleavage products indicate mutagenesis
  - Expected mutagenesis rate: 70-90% (based on pilot data)

- **Validation:** Sanger sequencing
  - PCR product → ExoSAP-IT cleanup → sequence with forward primer
  - TIDE analysis (Tracking of Indels by Decomposition) to quantify knockout efficiency
  - Target: >50% indels causing frameshift

**Primers:**
- Design: Primer3, 100-150bp flanking cut site
- Validation: Test on WT gDNA, confirm single band, no primer-dimers

#### 2.4 Regeneration Phenotyping

**Injury Procedure:**
- Same as Aim 1 (spinal cord transection at 5dpf)
- Blinding: Injector and phenotyper are different people; phenotyper blind to genotype

**Outcome Measures:**

1. **Axon Regeneration (Primary):**
   - **Assay:** Immunofluorescence for acetylated tubulin (axon marker)
   - **Quantification:** Maximum axon length beyond lesion site at 14dpi
   - **Metric:** Regeneration Index = (max axon length beyond lesion) / (total spinal cord length rostral to lesion)
   - **Imaging:** Confocal microscopy (Zeiss LSM 880), 10µm z-stacks
   - **Analysis:** Fiji (ImageJ), blinded scorer
   - **Expected:** WT regeneration index ~0.8 (80% restoration); knockouts <0.4 indicate regeneration defect

2. **Functional Recovery (Secondary):**
   - **Assay:** Touch-evoked escape response at 14dpi
   - **Protocol:** Gently touch tail with probe → score response (0=no movement, 1=tail flick only, 2=body bend, 3=full escape swim)
   - **Trials:** 3 trials per larva, average score
   - **Expected:** WT score ~2.5; knockouts <1.5 indicate functional deficit

3. **Cell Proliferation (Exploratory):**
   - **Assay:** EdU incorporation (4h pulse at 3dpi)
   - **Quantification:** EdU+ cells within 200µm of lesion
   - **Rationale:** Test if candidates regulate progenitor proliferation

**Statistical Analysis:**
- **Test:** Mann-Whitney U test (non-parametric, suitable for ordinal data like regeneration index)
- **Comparison:** Each CRISPR guide vs. uninjected control
- **Correction:** Benjamini-Hochberg FDR for 40 comparisons (20 genes × 2 guides)
- **Significance:** FDR < 0.05
- **Effect size:** Cohen's d >0.8 considered large effect
- **Power:** N=30/group gives 80% power to detect d=0.8 at α=0.05

#### 2.5 Validation Criteria

**Gene considered "validated" if:**
1. Both guides show significant regeneration deficit (FDR < 0.05)
2. Effect size >30% reduction in regeneration index (vs. control mean)
3. No severe developmental phenotype (<20% lethality at 5dpf)

**Expected outcome:** 10-15 genes validated (50-75% validation rate)

---

### Aim 3: Mammalian Proof-of-Concept

#### 3.1 AAV Vector Design

**Genes Selected:** Top 3 validated genes from Aim 2
- Criteria: Largest effect size in zebrafish + strong evolutionary conservation + druggable class (e.g., transcription factors)
- Example: sox2, klf4, stat3 (hypothetical - actual genes TBD from Aim 2)

**Vector Components:**
- **Serotype:** AAV9 (strong CNS tropism, crosses blood-brain barrier)
- **Promoter:** CAG (ubiquitous strong expression)
  - Alternative tested: hSyn (neuron-specific) for cell-type selectivity
- **Transgene:**
  - Zebrafish CDS (codon-optimized for mammalian expression, GeneArt)
  - OR mouse ortholog (if 1-to-1 ortholog exists)
- **Tag:** 3xFLAG C-terminal tag (enables expression verification by Western/IHC)
- **Regulatory:** WPRE (woodchuck post-transcriptional regulatory element, enhances expression)
- **Control:** AAV9-CAG-GFP (same vector backbone, GFP instead of gene)

**Vector Production:**
- **Provider:** Vector BioLabs (custom AAV production) or UPenn Vector Core
- **Method:** Triple transfection of HEK293 cells
- **Purification:** Iodixanol gradient + ion exchange chromatography
- **Titration:** qPCR (vg/mL) + SDS-PAGE (empty vs. full capsids)
- **QC targets:**
  - Titer: >1×10^13 vg/mL
  - Purity: >90% full capsids (SDS-PAGE)
  - Endotoxin: <5 EU/mL
- **Cost:** $8,000-12,000 per vector × 4 vectors (3 genes + GFP control) = $32,000-48,000

#### 3.2 Mouse Spinal Cord Injury + AAV Injection

**Animals:**
- Strain: C57BL/6J, 8-10 weeks, 50% male/50% female
- Sample size: 30 mice per gene (90 total) + 30 GFP controls = 120 mice total
  - Power analysis: 80% power to detect 20% improvement (d=0.8) at α=0.05

**Surgical Procedure:**

1. **Pre-operative:**
   - Anesthesia: Ketamine (100mg/kg) + xylazine (10mg/kg) IP
   - Analgesia: Buprenorphine SR (1mg/kg SC, single dose)
   - Eye lubrication: Artificial tears ointment
   - Surgical site: Shave + betadine scrub (3×) + alcohol rinse

2. **Laminectomy + Hemisection:**
   - Incision: 2cm midline incision at T10 level
   - Laminectomy: Remove T10 spinous process + lamina (micro-rongeurs)
   - Dura: Keep intact
   - Hemisection: Vibraknife (0.8mm depth, controlled by micromanipulator)
   - Verify: Complete hemisection on right side (visual confirmation)

3. **AAV Injection:**
   - **Timing:** Immediate (within 5min of injury) - rationale: target acute injury response
   - **Volume:** 2µL of 1×10^13 vg/mL (total 2×10^10 vg per mouse)
   - **Coordinates:** 2 injection sites flanking lesion (±1mm rostral/caudal to epicenter)
   - **Depth:** 0.4mm (mid-dorsal spinal cord)
   - **Rate:** 0.2µL/min (Hamilton syringe + syringe pump)
   - **Wait:** 5min post-injection (prevent backflow)
   - **Equipment:** Stereotaxic frame (Kopf), pulled glass micropipette

4. **Closure:**
   - Muscle: 5-0 Vicryl suture (absorbable)
   - Skin: 5-0 nylon suture (remove at 14dpi)
   - Post-op: Warm recovery cage, saline SC (1mL for hydration)

**Post-operative Care:**
- Analgesia: Carprofen (5mg/kg PO, daily for 3 days)
- Antibiotics: Enrofloxacin (200mg/L in water, 7 days)
- Bladder expression: 2× daily until reflex returns (~7-10 days)
- Monitoring: Daily for 7 days (weight, locomotion, signs of distress), then 3×/week

**Humane Endpoints:**
- >20% body weight loss
- Self-mutilation
- Signs of severe infection (lethargy, hunched posture, piloerection)
- Action: Euthanasia by CO2 + cervical dislocation

#### 3.3 Expression Verification

**Timepoint:** 2 weeks post-injection (N=5 mice per group)

**Western Blot:**
- **Tissue:** 4mm spinal cord segment (±2mm from lesion)
- **Lysis:** RIPA buffer + protease inhibitors
- **Protein:** 20µg per lane, 4-20% gradient gel
- **Detection:** Anti-FLAG M2 antibody (1:1000, Sigma), HRP-conjugated secondary
- **Loading control:** β-actin
- **Expected:** Band at predicted MW + 3kDa (FLAG tag)

**Immunohistochemistry:**
- **Tissue:** Perfusion-fixed (4% PFA), cryoprotection (30% sucrose), OCT embedding
- **Sections:** 20µm sagittal sections on cryostat
- **Staining:** Anti-FLAG (1:500) + DAPI (nuclei)
- **Imaging:** Confocal (Zeiss LSM 880), tile scan of injury site
- **Quantification:** % FLAG+ cells within 1mm of lesion
- **Expected:** >50% transduction efficiency in AAV9 (based on literature)

#### 3.4 Outcome Assessment

**Timeline:** 6 weeks post-injury (allows time for axon regrowth + functional recovery)

**Primary Outcome: Axon Regeneration**

*Anterograde Tract Tracing:*
- **Tracer:** Biotinylated dextran amine (BDA, 10kDa)
- **Injection:** 2µL of 10% BDA into motor cortex (stereotaxic coordinates: Bregma -0.5mm, lateral 1.5mm, depth 1.5mm)
- **Timing:** 4 weeks post-injury (allows 2 weeks for tracer transport before sacrifice)
- **Visualization:** Streptavidin-Alexa 594 (1:500)
- **Quantification:**
  - Count BDA+ axons crossing lesion border (defined as 1mm caudal to epicenter)
  - Measure axon length beyond lesion (max penetration distance)
  - Compare AAV-gene vs. AAV-GFP control

*Histology:*
- **Axon marker:** SMI-312 (pan-axonal neurofilament antibody, 1:1000)
- **Lesion size:** GFAP staining (astrocyte scar boundary)
- **Tissue sparing:** Cresyl violet (Nissl stain) for gray matter quantification

**Secondary Outcome: Functional Recovery**

*Basso-Beattie-Bresnahan (BBB) Locomotor Score:*
- **Assay:** Open field walking test (4min observation)
- **Scoring:** 0 (no movement) to 21 (normal gait)
- **Timepoints:** Baseline, 1d, 3d, 7d, 14d, 21d, 28d, 42d post-injury
- **Blinding:** Two independent scorers, video recorded
- **Inter-rater reliability:** >0.9 Pearson correlation required

*Electrophysiology - Motor Evoked Potentials (MEPs):*
- **Setup:** Transcranial magnetic stimulation (TMS) of motor cortex → record EMG from hindlimb muscle (tibialis anterior)
- **Timepoint:** 6 weeks post-injury (terminal procedure under anesthesia)
- **Metric:** MEP amplitude (µV) and latency (ms)
- **Interpretation:** Presence of MEP indicates functional connection across lesion

**Exploratory Outcomes:**

*Gene Expression Analysis:*
- RNA-seq of lesion site (4mm segment) at 2 weeks post-injury
- Compare AAV-gene vs. AAV-GFP
- Goal: Identify downstream pathways activated by transgene

*Cell Proliferation:*
- BrdU injection (50mg/kg IP) daily from 3-7dpi
- Sacrifice at 2 weeks
- Quantify BrdU+ cells at lesion border
- Test if transgene enhances endogenous progenitor response

#### 3.5 Statistical Analysis

**Primary Comparison:** AAV-gene vs. AAV-GFP for each gene (3 comparisons)

**Axon Regeneration:**
- **Metric:** Number of BDA+ axons crossing lesion border
- **Test:** Negative binomial regression (count data, often overdispersed)
- **Model:** `axon_count ~ treatment + sex + batch`
- **Post-hoc:** Tukey HSD for pairwise comparisons
- **Effect size:** Incidence rate ratio (IRR) - target IRR >2.0 (2-fold increase)

**Functional Recovery (BBB):**
- **Test:** Repeated measures mixed-effects model
- **Model:** `BBB ~ treatment × timepoint + (1|mouse_id) + sex + batch`
- **Software:** lme4 package in R
- **Comparison:** Treatment effect at 6 weeks (final timepoint)
- **Significance:** p < 0.05 for treatment main effect
- **Clinically meaningful:** >10% improvement (e.g., 10 vs. 9 on BBB scale)

**MEP:**
- **Test:** Two-way ANOVA (treatment × sex)
- **Metrics:** (1) % mice with detectable MEP, (2) MEP amplitude in responders
- **Effect size:** Cohen's d >0.8

**Multiple Testing Correction:**
- Bonferroni correction for 3 genes (α = 0.05/3 = 0.017)

**Power:**
- N=30 per group gives 80% power to detect 20% increase in axon counts (based on pilot variance estimates)

---

### Aim 4: Single-Cell RNA-Sequencing (scRNA-seq)

**Rationale:** Identify cell-type-specific regeneration programs and expression patterns of validated genes

#### 4.1 Sample Preparation

**Animals:** Zebrafish AB strain, 5dpf spinal cord transection

**Timepoints:** 0h (uninjured), 24h, 7d post-injury (captures acute + peak regeneration)

**Tissue Dissociation:**
- **Tissue:** 2mm spinal cord segment (±1mm from lesion)
- **N:** Pool 50 larvae per sample (needed for sufficient cell yield)
- **Protocol:**
  1. Dissect in ice-cold HBSS
  2. Enzymatic dissociation: Papain (Worthington, 20U/mL) at 37°C for 15min
  3. Mechanical trituration: P200 pipette, 20× passes
  4. Filtration: 40µm cell strainer (remove debris)
  5. Wash: 2× in HBSS + 0.04% BSA
  6. Count: Automated cell counter, trypan blue viability check (target >80%)
  7. Resuspend: 700-1200 cells/µL in HBSS + 0.04% BSA

**Cell Viability:** Target >85% (critical for scRNA-seq quality)

#### 4.2 10X Genomics Chromium

**Platform:** Chromium Controller (10X Genomics)

**Kit:** Chromium Single Cell 3' Reagent Kit v3.1

**Input:** 16,000 cells per sample (target 10,000 recovered cells)

**Procedure:**
1. Load cells + RT reagents + gel beads into chip
2. Run Chromium Controller (encapsulates cells in droplets with barcoded beads)
3. RT in droplets (cDNA synthesis with cell barcode + UMI)
4. Emulsion breakage + cDNA cleanup
5. Amplification: 12 cycles PCR
6. Library prep: Fragmentation, adapter ligation, sample indexing
7. Sequencing: NovaSeq 6000, PE150, target 50,000 reads/cell

**Samples:** 3 timepoints × 3 biological replicates = 9 samples

**Expected yield:** 10,000 cells × 9 samples = 90,000 cells total (>50,000 after QC)

**Cost:**
- 10X kit: $1,200/sample × 9 = $10,800
- Sequencing: $2,000/sample × 9 = $18,000
- Total: $28,800

#### 4.3 scRNA-seq Analysis

**Preprocessing (CellRanger):**
- Demultiplexing + alignment to GRCz11
- Cell barcode correction
- UMI counting
- Output: Feature-barcode matrix (genes × cells)

**Quality Control (Seurat v4):**
- Filter cells:
  - nFeature (genes detected): 200-5000 (exclude empty droplets + doublets)
  - nCount (total UMIs): 500-30,000
  - Mitochondrial %: <10% (exclude dying cells)
- Expected pass rate: 80-85% (50,000-60,000 cells retained)

**Normalization:** SCTransform (variance stabilization + batch correction)

**Dimensionality Reduction:**
- PCA: Top 30 principal components
- UMAP: 2D projection for visualization (n_neighbors=30, min_dist=0.3)

**Clustering:**
- Louvain algorithm (resolution=0.5, target 15-25 clusters)
- Expected clusters: Neurons (multiple subtypes), oligodendrocytes, astrocytes, radial glia, ependymal cells, immune cells, endothelial cells

**Cell Type Annotation:**
- Marker-based:
  - Neurons: elavl3, snap25
  - Oligodendrocytes: mbp, plp1a
  - Astrocytes: gfap, s100b
  - Radial glia/neural stem cells: sox2, vim, nestin
  - Microglia: mpeg1, csf1ra
- Automated: SingleR with zebrafish reference (if available)

**Differential Expression (Within Cell Types):**
- Compare 7d vs. 0h for each cell type
- Test: Wilcoxon rank-sum test (Seurat FindMarkers)
- Threshold: |log2FC| > 0.5, adjusted p < 0.01 (liberal for exploratory)
- Goal: Identify regeneration programs specific to neurons, glia, or NSCs

**Trajectory Analysis:**
- **Software:** Monocle 3
- **Goal:** Reconstruct differentiation trajectories during regeneration (e.g., NSC → neuron)
- **Focus:** Cells expressing top validated genes from Aim 2

**Integration with Bulk RNA-seq:**
- Cross-reference: Are bulk DE genes enriched in specific cell types?
- Example: If sox2 is bulk DE + scRNA-seq shows sox2 in radial glia → infer RG are key regeneration cell type

#### 4.4 Data Sharing

**Repository:**
- Raw data: GEO (Gene Expression Omnibus)
- Processed Seurat object: Zenodo
- Interactive portal: Custom website (https://neuroregen.ucsd.edu)
  - Built with R Shiny + Seurat
  - Features: UMAP visualization, gene expression plots, differential expression tables
  - Deployed on UCSD servers

**Publication:**
- Anticipated venue: *Nature Communications*, *Cell Reports*, or *eLife*
- Target: Companion paper to main regeneration study

---

## Timeline

### Year 1 (Months 1-12)

**Q1 (Months 1-3):**
- Personnel hiring (2 postdocs, 1 PhD student)
- Animal colony establishment (zebrafish + mouse)
- Equipment installation (10X Chromium, stereotaxic injector)
- Protocol optimization (injury models, tissue dissection)

**Q2 (Months 4-6):**
- Pilot RNA-seq (60 samples: 2 species × 3 timepoints × 10 replicates)
- Bioinformatics pipeline development
- CRISPR guide design + synthesis (20 genes × 2 guides)

**Q3 (Months 7-9):**
- Main bulk RNA-seq (remaining 300 samples)
- CRISPR microinjections begin (pilot 5 genes)
- Initial differential expression analysis

**Q4 (Months 10-12):**
- Complete bulk RNA-seq analysis
- Candidate gene prioritization (identify top 20)
- **Milestone M2:** DE analysis complete

### Year 2 (Months 13-24)

**Q1 (Months 13-15):**
- CRISPR validation (15 remaining genes)
- scRNA-seq sample collection (9 samples)
- 10X library prep + sequencing

**Q2 (Months 16-18):**
- CRISPR phenotyping complete
- scRNA-seq analysis
- **Milestone M3:** scRNA-seq manuscript submission

**Q3 (Months 19-21):**
- AAV vector design (top 3 genes)
- Vector production (outsourced, 3-month lead time)
- Mouse cohort breeding (N=120 mice)

**Q4 (Months 22-24):**
- AAV QC + titration
- Pilot mouse surgeries (N=10, optimize protocol)
- **Milestone M4:** CRISPR validation complete

### Year 3 (Months 25-36)

**Q1 (Months 25-27):**
- Mouse AAV experiments - Cohort 1 (N=60 mice)
- Expression verification (Western, IHC at 2 weeks)

**Q2 (Months 28-30):**
- Mouse AAV experiments - Cohort 2 (N=60 mice)
- Behavioral testing (BBB scoring, weekly)

**Q3 (Months 31-33):**
- Tract tracing (BDA injections at 4 weeks post-injury)
- **Milestone M6:** All mice injected

**Q4 (Months 34-36):**
- Sacrifice + histology (confocal imaging, axon counting)
- Electrophysiology (MEPs)
- **Milestone M7:** Behavioral data complete

### Year 4 (Months 37-48)

**Q1 (Months 37-39):**
- Data analysis (statistics, figure generation)
- Validation RNA-seq (lesion site, 2 weeks post-injury, N=30 samples)

**Q2 (Months 40-42):**
- Manuscript writing (main regeneration paper)
- **Milestone M8:** Draft manuscript complete

**Q3 (Months 43-45):**
- Manuscript submission + revisions
- Patent application (if results warrant - regeneration gene therapy)

**Q4 (Months 46-48):**
- Final data release (GEO, interactive portal)
- Conference presentations (Society for Neuroscience, ISSCR)
- Project closeout + final report to NSF

---

## Ethical Considerations

### Animal Ethics

**IACUC Approval:**
- Protocol #2024-0456 (Zebrafish) - approved through December 2027
- Protocol #2024-0457 (Mouse) - approved through December 2027
- Annual renewals required

**3Rs Compliance:**

*Replacement:*
- Justify vertebrate use: In vitro models insufficient for complex regeneration (requires tissue-level interactions)
- Literature search confirms no alternative models

*Reduction:*
- Power analysis ensures minimum N for statistical significance
- Pilot studies (N=10) to refine protocols before large cohorts
- Data sharing maximizes utility of animals used

*Refinement:*
- Pain management: Multimodal analgesia (NSAIDs + opioids)
- Refined injury models: Hemisection (vs. complete transection) allows some motor function
- Humane endpoints: Early euthanasia if severe distress
- Environmental enrichment: Nesting material (mice), plant cover (zebrafish)

**Personnel Training:**
- IACUC-required training: All personnel before animal work
- Surgical training: Hands-on workshops + supervised practice (>10 successful surgeries before independent work)
- Zebrafish microinjection: Training course + >100 practice injections

### Data Management

**Reproducibility:**
- Electronic Lab Notebook (ELN): Benchling (all protocols, data links)
- Version control: GitHub for analysis code
- Raw data backup: 3 copies (local server + AWS S3 + UCSD institutional storage)

**Data Sharing:**
- Timeline: Public release upon publication or 4 years (whichever earlier)
- Format: FASTQ (raw sequencing), count matrices (processed), metadata (MINSEQE compliant)
- Repository: GEO (NIH), interactive portal for exploration

### Human Subjects

**Not applicable** - this project uses animal models only

**Future considerations:**
- If proof-of-concept succeeds → IND-enabling studies → Phase I clinical trial
- Would require separate IRB approval, informed consent process

---

## Risk Mitigation

### Technical Risks

**Risk 1: Insufficient DE genes between species**
- Probability: Low (15%)
- Impact: High (threatens Aim 1 & 2)
- Mitigation:
  - Include axolotl as third species (highest regenerative capacity)
  - Use single-cell RNA-seq to resolve cell-type-specific differences (may be masked in bulk)
  - Explore epigenetic differences (ATAC-seq for chromatin accessibility)

**Risk 2: CRISPR validation negative (no regeneration phenotype)**
- Probability: Medium (30% - some genes will be false positives)
- Impact: Medium (reduces candidate pool but doesn't halt project)
- Mitigation:
  - Test 20 genes (redundancy)
  - Combinatorial testing: If single genes fail, test pairs (may require multiple factors)
  - Alternative validation: Pharmacological inhibition (if available)

**Risk 3: AAV expression too low in mouse**
- Probability: Low (20%)
- Impact: High (threatens Aim 3)
- Mitigation:
  - Optimize promoter (test CAG vs. hSyn vs. EF1α in pilot)
  - Increase dose (up to 5×10^10 vg tested in safety studies)
  - Alternative delivery: Lentivirus (integrating, sustained expression) or nanoparticles

**Risk 4: Mouse proof-of-concept fails (no functional improvement)**
- Probability: Medium (40% - mammalian regeneration is fundamentally limited)
- Impact: Medium (reduces translational impact but scientific value remains)
- Mitigation:
  - Scientific value: Even negative result advances field (defines limits of regeneration plasticity)
  - Alternative outcomes: Partial axon regrowth (even without function) validates target
  - Future directions: Combinatorial gene therapy, developmental timing studies (neonatal vs. adult)

### Operational Risks

**Risk 5: Key personnel departure**
- Probability: Low (20%)
- Impact: Medium (delays timeline)
- Mitigation:
  - Staggered hiring (not all start simultaneously)
  - Cross-training: 2 people trained on each critical technique
  - Detailed protocols in ELN (enable quick onboarding)
  - Competitive salaries + career development support

**Risk 6: Equipment failure**
- Probability: Medium (30% over 4 years)
- Impact: Low (delays but not critical)
- Mitigation:
  - Service contracts on major equipment (10X Chromium, confocal)
  - Backup arrangements with core facilities (IGM Genomics, Microscopy Core)
  - Redundant equipment for critical items (e.g., 2 stereotaxic frames)

**Risk 7: Sequencing delays**
- Probability: Low (10%)
- Impact: Medium (delays Aim 1 timeline)
- Mitigation:
  - Early booking of core facility (reserve capacity 6 months ahead)
  - Alternative providers identified (Novogene, Genewiz)
  - Pilot samples to troubleshoot library prep issues

### Budget Risks

**Risk 8: Cost overruns**
- Probability: Medium (25%)
- Impact: Medium (constrains scope)
- Mitigation:
  - 10% contingency built into budget
  - Prioritize experiments: Aims 1-2 are essential; Aim 4 (scRNA-seq) can be descoped if needed
  - Seek supplemental funding: NIH R21 for high-risk mouse validation

---

## Equipment & Facilities

### Major Equipment (>$10k)

**Acquired (Year 1 budget):**

1. **10X Genomics Chromium Controller** - $75,000
   - Single-cell RNA-seq platform
   - Shared with 2 other labs (cost-sharing arrangement)

2. **Zeiss LSM 880 Confocal Microscope** - Existing (institutional core facility)
   - $15/hour usage fee (included in budget)
   - Booked capacity: 100 hours/year

3. **Stereotaxic Injector (Stoelting)** - $25,000
   - Mouse brain/spinal cord injections
   - Includes micromanipulator + syringe pump

4. **NovaSeq 6000 Sequencer** - Existing (UCSD IGM Core)
   - Pay-per-sample model ($330/sample bulk RNA-seq)

### Laboratory Space

**Kowalska Lab (PI):**
- Location: UCSD Medical Teaching Facility, Room 4820 (1,200 sq ft)
- Equipment: Standard molecular biology (PCR, gel boxes, centrifuges, -80°C freezers)
- Zebrafish: On-site aquatics facility (500L capacity, 50 tanks)

**Nowak Lab (Co-PI):**
- Location: UCSD Medical Teaching Facility, Room 3640 (900 sq ft)
- Equipment: CRISPR/AAV infrastructure (biosafety cabinet, tissue culture)

**Mouse Facility:**
- Location: UCSD Animal Care Program (ACP), Building CTF (Climate-controlled)
- Capacity: 300 cages (sufficient for 150 mice at any time)
- Staff: Dedicated veterinary technician + ACP husbandry staff

### Core Facilities

**IGM Genomics Center (Institute for Genomic Medicine):**
- Services: Library prep, sequencing (NovaSeq, MiSeq), bioinformatics consultation
- Turnaround: 4-6 weeks (sample submission to data delivery)
- Cost: $330/sample (bulk RNA-seq, PE150, 50M reads)

**Microscopy Core:**
- Equipment: Confocal (Zeiss LSM 880), 2-photon, light sheet
- Staff: Imaging specialist (protocol optimization, training)
- Access: Online booking system, 24/7 access for trained users

**Viral Vector Core (UCSD):**
- Services: AAV design consultation, small-scale pilot production
- Note: Large-scale AAV production outsourced to Vector BioLabs (higher titer, GMP-grade)

---

## Compliance & Regulatory

### Institutional Biosafety Committee (IBC)

**Protocol #2024-IBC-098:** CRISPR/Cas9 use in zebrafish and AAV in mice
- Biosafety level: BSL-1 (zebrafish CRISPR), BSL-2 (AAV production/handling)
- Approval: Valid through December 2027
- Requirements:
  - Autoclave all biological waste
  - AAV handling in BSL-2 hood (even though AAV9 is replication-deficient)
  - Annual safety training for all personnel

### Export Control

**UCSD Export Control Office:**
- Review: No controlled technologies or international collaborators
- Determination: Not subject to export control (EAR99)

### Data Security

**HIPAA:** Not applicable (no human subjects)

**Data Protection:**
- Animal data: Not considered sensitive
- Backup: UCSD institutional storage (encrypted, access-controlled)
- Sharing: Public repositories (GEO) upon publication

---

## Dissemination Plan

### Publications (Target 4-5 Papers)

**Paper 1: Comparative Transcriptomic Atlas**
- Target journal: *Nature Communications* or *Cell Reports*
- Timeline: Month 18 (submission)
- Content: Bulk RNA-seq analysis, candidate gene identification
- Open access: Yes (required by NSF)

**Paper 2: Single-Cell Regeneration Atlas**
- Target journal: *Nature Methods*, *Cell*, or *eLife*
- Timeline: Month 24 (submission)
- Content: scRNA-seq analysis, cell-type-specific regeneration programs
- Open access: Yes

**Paper 3: Functional Validation (CRISPR)**
- Target journal: *Development*, *PLoS Biology*, or *eLife*
- Timeline: Month 30 (submission)
- Content: CRISPR screen results, mechanistic insights
- Open access: Yes

**Paper 4: Mouse Proof-of-Concept**
- Target journal: *Nature*, *Cell*, *Science Translational Medicine*
- Timeline: Month 45 (submission)
- Content: AAV validation in mouse, translational implications
- Open access: Yes (pay OA fees from budget)

**Paper 5: Integrative Analysis (Review/Perspective)**
- Target journal: *Nature Reviews Neuroscience* or *Trends in Neurosciences*
- Timeline: Month 48
- Content: Synthesis of findings, future directions for regeneration field

### Conferences

**Annual Presentations:**
- Society for Neuroscience (SfN) - 30,000 attendees, poster + talk
- International Society for Stem Cell Research (ISSCR) - 4,000 attendees
- Gordon Research Conference: Neural Regeneration - 200 attendees (invited talk)

**Invited Seminars:**
- Target 5-10 universities per year
- Emphasis on training institutions (expose students to regeneration research)

### Outreach

**Patient Advocacy:**
- Partnership: United Spinal Association (https://www.unitedspinal.org)
- Activity: Annual public lecture on regeneration research (open to SCI community)
- Advisory board: Include patient representative (Ms. Rachel Gomez, SCI survivor)

**K-12 Education:**
- Activity: Lab tours for local high schools (San Diego area)
- Frequency: 2-3 groups per year (20 students each)
- Content: Zebrafish regeneration demos, microscopy hands-on

**Media:**
- Press release: Upon high-impact publication (coordinate with UCSD communications)
- Target: Science journalists (e.g., *STAT News*, *The Scientist*)

---

## Success Metrics

### Scientific Outcomes

✓ Identify >200 differentially expressed genes between zebrafish and mouse (FDR < 0.01)
✓ Validate >10 genes as regeneration regulators via CRISPR (50% validation rate)
✓ Generate single-cell atlas with >50,000 cells, 15+ cell types resolved
✓ Demonstrate >20% axon regrowth improvement in mouse with at least 1 gene candidate
✓ Publish 4+ papers in high-impact journals (cumulative IF >100)

### Translational Outcomes

✓ File 1-2 provisional patents on regeneration gene therapy
✓ Establish collaboration with biotech/pharma for IND-enabling studies
✓ Secure follow-on funding (e.g., NIH R01, CIRM) for clinical development

### Community Impact

✓ Data resource accessed by >50 research groups within 2 years
✓ Train 5 early-career scientists (2 PhD students, 3 postdocs)
✓ Reach >500 patients/advocates through outreach activities
✓ Cited >300 times within 3 years of publication

---

**Prepared by:** Dr. Maria Kowalska
**Last Updated:** December 27, 2025
**Document Version:** 3.2

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Executive Summary - Biology]** `biology-executive-summary-example.md`
  - Type: `informs`
  - Reason: High-level objectives defined in exec summary guide research plan detail
  - Sections used: Research Objectives, Expected Outcomes
  - Validation: Research Questions here must align with Objectives there
  - Condition: `when domain === 'biology'`

- **[Literature Review]** `evidence/literature_review_neural_regeneration_2024.md`
  - Type: `requires`
  - Reason: Background section (Hypotheses) cites literature review findings
  - Evidence ID: `E-BIO-002`
  - Required depth: ≥50 papers reviewed, ≥15 directly cited

- **[Preliminary Data Report]** `evidence/pilot_data_zebrafish_injury_2023.pdf`
  - Type: `requires`
  - Reason: Feasibility claims (Aim 1) based on pilot results
  - Evidence ID: `E-BIO-003`
  - Must include: N=30 pilot animals, injury success rate ≥80%

### Impacts (Downstream Documents)
- **[TDD - Biology]** `biology-tdd-example.md`
  - Type: `blocks`
  - Until: `this.status == approved`
  - Reason: Technical design depends on finalized experimental methodology
  - Cascade: `true`
  - Specific impacts: Data Models section requires RNA-seq output schema, Storage Requirements based on sequencing volume

- **[Test Plan]** `docs/testing/biology_data_pipeline_test_plan.md`
  - Type: `informs`
  - Reason: Success metrics (QC pass rate >90%) define test acceptance criteria

- **[Implementation Backlog]** `jira/BIO-RESEARCH-EPIC`
  - Type: `generates`
  - Reason: Timeline milestones auto-generate JIRA tasks
  - Cascade: `true`

### Related Documents
- **[Chemistry Research Plan]** `chemistry-research-plan-example.md`
  - Relationship: `parallel-example`
  - Reason: Alternative domain example for methodology structure comparison

- **[Physics Research Plan]** `physics-research-plan-example.md`
  - Relationship: `parallel-example`
  - Reason: Experimental physics methodology pattern

- **[Psychology Research Plan]** `psychology-research-plan-example.md`
  - Relationship: `parallel-example`
  - Reason: Human subjects research methodology pattern

### Satellite Documents
- **[TODO per Section]** `satellites/TODO-RESPLAN-BIO-001.md`
  - Purpose: Track completion of each Aim and subsection
  - Granularity: Per Aim (4 TODOs: Aim 1-4)
  - Status: `completed`

- **[DOR (Definition of Ready)]** `satellites/DOR-RESPLAN-BIO-001.md`
  - Criteria before starting Research Plan:
    - [ ] Literature review complete (≥50 papers)
    - [ ] Pilot data analyzed and documented
    - [ ] Equipment access confirmed (RNA-seq facility, animal facility)
    - [ ] Personnel hired or recruitment approved
    - [ ] IACUC protocol submitted
  - Status: `met`

- **[DOD (Definition of Done)]** `satellites/DOD-RESPLAN-BIO-001.md`
  - Criteria before approval:
    - [ ] All 4 Aims detailed with protocols
    - [ ] Timeline validated (achievable milestones)
    - [ ] Equipment list complete with model numbers
    - [ ] Statistical power analysis included
    - [ ] IRB/IACUC approved
    - [ ] Peer review by 2 external experts
  - Status: `met`

### Conditional Cross-References

```yaml
conditions:
  - when: domain === 'biology'
    require_dependencies:
      - IRB/IACUC Approval (if animal/human subjects)
      - Biosafety approval (if recombinant DNA, pathogens, toxins)
      - Animal facility capacity letter
    require_satellites:
      - IACUC Protocol document (detailed animal procedures)
      - Veterinary consultation record
    require_evidence:
      - Animal welfare protocols (housing, euthanasia)
      - Breeding protocols (if generating transgenic lines)

  - when: methodology_includes === 'genomics'
    require_dependencies:
      - Sequencing facility access letter
      - Bioinformatics compute allocation
      - Data storage plan (institutional or cloud)
    require_evidence:
      - Sequencing cost quote
      - Data management plan (DMP) aligned with funding agency
      - Computational pipeline validation

  - when: methodology_includes === 'human_subjects'
    require_dependencies:
      - IRB Approval (protocol #)
      - HIPAA compliance plan (if PHI)
      - Informed consent templates (approved by IRB)
      - Recruitment materials (approved)
    require_satellites:
      - IRB approval letter
      - Consent forms repository

  - when: methodology_includes === 'molecular_biology'
    require_dependencies:
      - Institutional Biosafety Committee (IBC) approval
      - Recombinant DNA registration
      - Lab safety protocols (chemical, biological)
    require_evidence:
      - Biosafety level justification (BSL-1/BSL-2)
      - Waste disposal contracts

  - when: collaboration === true
    require_dependencies:
      - Collaboration agreements (MOU, subawards)
      - Data sharing agreements
      - IP ownership agreements
    require_evidence:
      - Letters of support (signed + letterhead)

  - when: funding === 'NIH'
    require_dependencies:
      - Vertebrate Animals section (detailed)
      - Human Subjects section (if applicable)
      - NIH-specific forms (PHS 398)
    budgeting_rules:
      - Personnel: Salary caps apply (NIH ~$210k)

  - when: budget > 500000 per_year
    require_approvals:
      - Department Chair
      - Dean of Research
      - Institutional Animal Care and Use Office (if animals)
```

### Validation Rules

**BLOCKER-level (must pass before approval):**
- [ ] All dependencies status ≥ `approved`
- [ ] Research Questions (RQ1-RQ4) align with Executive Summary Objectives
- [ ] Each hypothesis (H1-H6) has corresponding methodology
- [ ] Timeline achievable (expert review: senior investigator sign-off)
- [ ] Equipment access confirmed (letters for items >$50k)
- [ ] Statistical power analysis included and adequate (power ≥0.8)
- [ ] IACUC/IRB approved (if applicable)
- [ ] No placeholders in critical sections (Methodology, Timeline)

**ERROR-level (should fix before submission):**
- [ ] All methods include sufficient detail (replicable by expert)
- [ ] Sample sizes justified (statistical consultation)
- [ ] Controls appropriate (positive + negative for each experiment)
- [ ] Timeline buffer ≥20% (account for delays)
- [ ] Equipment backup plans (if core facility equipment)

**WARN-level (recommended improvements):**
- [ ] Reproducibility statement (data/code sharing plan)
- [ ] Rigor and reproducibility criteria (NIH emphasis)
- [ ] Alternative approaches if primary method fails
- [ ] Training plan for new techniques
- [ ] Preliminary data supports feasibility
