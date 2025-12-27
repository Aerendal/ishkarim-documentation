# Technical Design Document: NeuroRegen Project
## Data Pipeline, Analysis Infrastructure, and Laboratory Information Systems

**Project ID:** NSF-BIO-2024-7821
**PI:** Dr. Maria Kowalska
**Technical Lead:** Dr. Sarah Chen (Computational Biology)
**Version:** 2.4
**Date:** December 27, 2025

---

## 1. System Architecture Overview

### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA GENERATION LAYER                        │
├─────────────────────────────────────────────────────────────────┤
│  Sequencing Core → Raw FASTQ files (RNA-seq, scRNA-seq)        │
│  Lab Equipment → Experimental data (images, behavioral scores)   │
│  ELN (Benchling) → Metadata, protocols, sample annotations      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     DATA INGESTION LAYER                         │
├─────────────────────────────────────────────────────────────────┤
│  AWS S3 Bucket (neuroregen-raw) → Raw data storage              │
│  PostgreSQL Database → Metadata + sample tracking                │
│  MinIO (on-prem) → Image data (confocal, histology)             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   PROCESSING PIPELINE LAYER                      │
├─────────────────────────────────────────────────────────────────┤
│  Nextflow Pipelines → RNA-seq, scRNA-seq processing             │
│  Snakemake Workflows → Image analysis, feature extraction        │
│  SLURM Cluster (UCSD TSCC) → Compute resource management        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    ANALYSIS & MODELING LAYER                     │
├─────────────────────────────────────────────────────────────────┤
│  R/Bioconductor → Differential expression (DESeq2, Seurat)      │
│  Python (scikit-learn) → Machine learning, statistical modeling │
│  Jupyter Notebooks → Interactive exploration, visualization      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    RESULTS STORAGE LAYER                         │
├─────────────────────────────────────────────────────────────────┤
│  PostgreSQL → Results tables (DE genes, statistics)             │
│  AWS S3 (neuroregen-results) → Processed data, figures          │
│  MongoDB → Unstructured data (annotations, notes)               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                  VISUALIZATION & API LAYER                       │
├─────────────────────────────────────────────────────────────────┤
│  Flask REST API → Programmatic data access                      │
│  React Dashboard → Interactive web portal                        │
│  R Shiny Apps → Single-cell browser, gene expression viewer     │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Technology Stack

**Infrastructure:**
- **Cloud:** AWS (S3, EC2, RDS for backups)
- **On-Premises:** UCSD TSCC HPC cluster (Triton Shared Computing Cluster)
  - 336 compute nodes, 10,000+ cores
  - 2 PB shared storage (Lustre filesystem)
  - SLURM job scheduler

**Storage:**
- **Object Storage:** AWS S3 (raw FASTQ, processed results) - versioned, encrypted at rest
- **Relational Database:** PostgreSQL 14 (metadata, results tables)
- **Document Database:** MongoDB 6.0 (flexible schema for annotations)
- **Image Storage:** MinIO (on-prem S3-compatible, faster for large files)

**Compute:**
- **Workflow Management:** Nextflow 23.04 (DSL2), Snakemake 7.20
- **Containerization:** Docker 24.0, Singularity 3.11 (HPC compatibility)
- **Version Control:** Git + GitHub (code), DVC (data version control)

**Analysis:**
- **Languages:** R 4.3, Python 3.11, Bash
- **Key R Packages:** DESeq2 1.38, Seurat 4.3, ggplot2 3.4
- **Key Python Packages:** pandas 2.0, scikit-learn 1.3, scanpy 1.9

**Visualization:**
- **Web Framework:** React 18 + TypeScript, Flask 2.3 (backend)
- **Interactive Viz:** Plotly.js, D3.js, Vega-Lite
- **Reporting:** R Markdown, Jupyter Notebooks, Quarto

---

## 2. Data Models

### 2.1 Database Schema (PostgreSQL)

#### Table: `samples`
Primary sample tracking table

```sql
CREATE TABLE samples (
    sample_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sample_name VARCHAR(100) UNIQUE NOT NULL,
    species ENUM('zebrafish', 'mouse', 'axolotl') NOT NULL,
    condition ENUM('control', 'injured', 'sham') NOT NULL,
    timepoint_hours INTEGER NOT NULL,  -- hours post-injury (0 = baseline)
    biological_replicate INTEGER NOT NULL,
    sex ENUM('male', 'female', 'pooled', 'na') DEFAULT 'na',
    age_description VARCHAR(100),  -- e.g., "5dpf" (zebrafish) or "8 weeks" (mouse)
    tissue_type VARCHAR(50) DEFAULT 'spinal_cord',
    dissection_date DATE NOT NULL,
    dissected_by VARCHAR(100),

    -- RNA-seq specific
    rna_concentration_ng_ul DECIMAL(6,2),
    rin_score DECIMAL(3,1),  -- RNA integrity number
    library_prep_kit VARCHAR(100),
    library_prep_date DATE,

    -- Sequencing run info
    sequencing_run_id VARCHAR(50),
    sequencing_date DATE,
    read_count_millions DECIMAL(8,2),
    qc_pass BOOLEAN,
    qc_notes TEXT,

    -- File paths
    fastq_r1_path VARCHAR(500),  -- S3 path
    fastq_r2_path VARCHAR(500),
    bam_path VARCHAR(500),

    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    notes TEXT,

    -- Constraints
    CHECK (timepoint_hours >= 0),
    CHECK (rin_score BETWEEN 1.0 AND 10.0),
    CHECK (biological_replicate > 0)
);

CREATE INDEX idx_samples_species_condition ON samples(species, condition);
CREATE INDEX idx_samples_timepoint ON samples(timepoint_hours);
CREATE INDEX idx_samples_sequencing_run ON samples(sequencing_run_id);
```

#### Table: `genes`
Gene annotation table with cross-species orthologs

```sql
CREATE TABLE genes (
    gene_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ensembl_id VARCHAR(50) UNIQUE NOT NULL,
    gene_symbol VARCHAR(50) NOT NULL,
    gene_name TEXT,  -- full gene name
    species ENUM('zebrafish', 'mouse', 'axolotl') NOT NULL,
    chromosome VARCHAR(20),
    start_position BIGINT,
    end_position BIGINT,
    strand ENUM('+', '-'),
    gene_biotype VARCHAR(50),  -- e.g., protein_coding, lncRNA

    -- Orthology
    mouse_ortholog_id UUID REFERENCES genes(gene_id),
    zebrafish_ortholog_id UUID REFERENCES genes(gene_id),
    orthology_confidence ENUM('high', 'medium', 'low'),

    -- Functional annotation
    go_terms TEXT[],  -- Array of GO IDs
    kegg_pathways TEXT[],
    description TEXT,

    -- Metadata
    ensembl_version INTEGER DEFAULT 108,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_genes_symbol ON genes(gene_symbol);
CREATE INDEX idx_genes_species ON genes(species);
CREATE INDEX idx_genes_ensembl ON genes(ensembl_id);
CREATE INDEX idx_genes_orthologs ON genes(mouse_ortholog_id, zebrafish_ortholog_id);
```

#### Table: `expression_counts`
Raw gene expression counts (from featureCounts)

```sql
CREATE TABLE expression_counts (
    count_id BIGSERIAL PRIMARY KEY,
    sample_id UUID REFERENCES samples(sample_id) ON DELETE CASCADE,
    gene_id UUID REFERENCES genes(gene_id) ON DELETE CASCADE,
    raw_count INTEGER NOT NULL,
    normalized_count DECIMAL(12,4),  -- DESeq2 normalized
    tpm DECIMAL(12,4),  -- Transcripts per million

    UNIQUE(sample_id, gene_id)
);

CREATE INDEX idx_expression_sample ON expression_counts(sample_id);
CREATE INDEX idx_expression_gene ON expression_counts(gene_id);
```

#### Table: `differential_expression`
Results from DESeq2 analysis

```sql
CREATE TABLE differential_expression (
    de_id BIGSERIAL PRIMARY KEY,
    gene_id UUID REFERENCES genes(gene_id) ON DELETE CASCADE,
    comparison_id UUID REFERENCES comparisons(comparison_id),

    -- Statistics
    base_mean DECIMAL(12,4) NOT NULL,  -- mean normalized counts
    log2_fold_change DECIMAL(8,4) NOT NULL,
    log2fc_se DECIMAL(8,4),  -- standard error
    stat DECIMAL(10,4),  -- Wald statistic
    pvalue DECIMAL(20,16),
    adjusted_pvalue DECIMAL(20,16),

    -- Classification
    significant BOOLEAN GENERATED ALWAYS AS (adjusted_pvalue < 0.01 AND ABS(log2_fold_change) > 2) STORED,
    direction ENUM('up', 'down', 'ns') GENERATED ALWAYS AS (
        CASE
            WHEN adjusted_pvalue < 0.01 AND log2_fold_change > 2 THEN 'up'
            WHEN adjusted_pvalue < 0.01 AND log2_fold_change < -2 THEN 'down'
            ELSE 'ns'
        END
    ) STORED,

    -- Metadata
    analysis_date DATE DEFAULT CURRENT_DATE,
    deseq2_version VARCHAR(20),

    UNIQUE(gene_id, comparison_id)
);

CREATE INDEX idx_de_comparison ON differential_expression(comparison_id);
CREATE INDEX idx_de_significant ON differential_expression(significant) WHERE significant = TRUE;
CREATE INDEX idx_de_padj ON differential_expression(adjusted_pvalue);
```

#### Table: `comparisons`
Defines pairwise comparisons for DE analysis

```sql
CREATE TABLE comparisons (
    comparison_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    comparison_name VARCHAR(200) UNIQUE NOT NULL,
    description TEXT,

    -- Contrast definition
    species ENUM('zebrafish', 'mouse', 'axolotl'),
    condition_a VARCHAR(50),  -- e.g., "injured_7d"
    condition_b VARCHAR(50),  -- e.g., "control_0h"

    -- Sample lists
    group_a_sample_ids UUID[],
    group_b_sample_ids UUID[],

    -- Results summary
    num_significant INTEGER,
    num_upregulated INTEGER,
    num_downregulated INTEGER,

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_comparisons_species ON comparisons(species);
```

#### Table: `crispr_experiments`
CRISPR validation experiments

```sql
CREATE TABLE crispr_experiments (
    experiment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    gene_id UUID REFERENCES genes(gene_id),
    guide_rna_sequence VARCHAR(100) NOT NULL,
    guide_number INTEGER CHECK (guide_number IN (1, 2)),

    -- Injection details
    injection_date DATE NOT NULL,
    cas9_concentration_ng_ul DECIMAL(6,2),
    sgrna_concentration_ng_ul DECIMAL(6,2),
    num_embryos_injected INTEGER,
    num_embryos_survived INTEGER,
    survival_rate DECIMAL(5,2) GENERATED ALWAYS AS (
        CASE WHEN num_embryos_injected > 0
        THEN (num_embryos_survived::DECIMAL / num_embryos_injected * 100)
        ELSE NULL END
    ) STORED,

    -- Genotyping
    mutagenesis_rate_percent DECIMAL(5,2),
    frameshift_rate_percent DECIMAL(5,2),

    -- Phenotyping
    num_larvae_phenotyped INTEGER,
    mean_regeneration_index DECIMAL(4,3),
    regeneration_index_sd DECIMAL(4,3),
    mean_functional_score DECIMAL(3,2),
    functional_score_sd DECIMAL(3,2),

    -- Control comparison
    control_mean_regeneration_index DECIMAL(4,3),
    control_regeneration_index_sd DECIMAL(4,3),

    -- Statistics
    mannwhitney_u DECIMAL(10,2),
    pvalue DECIMAL(10,8),
    effect_size_cohens_d DECIMAL(5,3),
    validated BOOLEAN,  -- manually curated based on criteria

    -- Metadata
    experimenter VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_crispr_gene ON crispr_experiments(gene_id);
CREATE INDEX idx_crispr_validated ON crispr_experiments(validated) WHERE validated = TRUE;
```

#### Table: `aav_experiments`
Mouse AAV experiments

```sql
CREATE TABLE aav_experiments (
    experiment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    gene_id UUID REFERENCES genes(gene_id),

    -- AAV details
    aav_serotype VARCHAR(20) DEFAULT 'AAV9',
    promoter VARCHAR(50) DEFAULT 'CAG',
    vector_batch_id VARCHAR(50),
    titer_vg_per_ml DECIMAL(15,2),

    -- Mouse details
    mouse_id VARCHAR(50) UNIQUE NOT NULL,
    strain VARCHAR(50) DEFAULT 'C57BL/6J',
    sex ENUM('male', 'female'),
    age_weeks INTEGER,

    -- Surgery
    surgery_date DATE NOT NULL,
    surgeon VARCHAR(100),
    injection_volume_ul DECIMAL(4,2),
    total_vg DECIMAL(15,2),

    -- Outcomes (at 6 weeks post-injury)
    bbb_score_6w DECIMAL(4,2) CHECK (bbb_score_6w BETWEEN 0 AND 21),
    bda_axon_count INTEGER,  -- axons crossing lesion
    max_axon_length_mm DECIMAL(5,3),
    mep_detected BOOLEAN,
    mep_amplitude_uv DECIMAL(6,2),
    lesion_size_mm3 DECIMAL(6,3),

    -- Metadata
    sacrifice_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_aav_gene ON aav_experiments(gene_id);
CREATE INDEX idx_aav_surgery_date ON aav_experiments(surgery_date);
```

#### Table: `single_cell_data`
scRNA-seq cell metadata (main expression data in HDF5/Seurat object)

```sql
CREATE TABLE single_cell_data (
    cell_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cell_barcode VARCHAR(50) UNIQUE NOT NULL,
    sample_id UUID REFERENCES samples(sample_id),

    -- QC metrics
    n_genes_detected INTEGER,
    n_umis INTEGER,
    percent_mitochondrial DECIMAL(5,2),
    doublet_score DECIMAL(5,4),
    qc_pass BOOLEAN,

    -- Clustering results
    cluster_id INTEGER,
    cell_type VARCHAR(100),  -- annotated cell type
    cell_type_confidence DECIMAL(4,3),  -- from SingleR

    -- Dimensionality reduction
    umap_1 DECIMAL(10,6),
    umap_2 DECIMAL(10,6),
    pc_1 DECIMAL(10,6),
    pc_2 DECIMAL(10,6),

    -- Pseudotime (from Monocle3)
    pseudotime DECIMAL(10,6),

    -- File reference
    seurat_object_path VARCHAR(500),  -- S3 path to RDS file

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_sc_sample ON single_cell_data(sample_id);
CREATE INDEX idx_sc_celltype ON single_cell_data(cell_type);
CREATE INDEX idx_sc_cluster ON single_cell_data(cluster_id);
```

### 2.2 File Organization (S3 Buckets)

**Bucket: `neuroregen-raw`** (Raw data, immutable)
```
neuroregen-raw/
├── bulk-rnaseq/
│   ├── run_20240315_NovaSeq6000_A00987/
│   │   ├── fastq/
│   │   │   ├── zebrafish_injured_6h_rep1_R1.fastq.gz
│   │   │   ├── zebrafish_injured_6h_rep1_R2.fastq.gz
│   │   │   └── ... (360 samples × 2 files = 720 FASTQ files)
│   │   ├── metadata/
│   │   │   ├── samplesheet.csv
│   │   │   └── run_QC_report.html
│   └── run_20240822_NovaSeq6000_B01234/
│       └── ... (additional sequencing runs)
├── single-cell/
│   ├── 10x_run_20240520/
│   │   ├── sample_zebrafish_0h_rep1/
│   │   │   ├── raw_feature_bc_matrix/
│   │   │   ├── filtered_feature_bc_matrix/
│   │   │   └── analysis/
│   │   └── ... (9 samples)
├── images/
│   ├── confocal/
│   │   ├── 20240418_zebrafish_crispr_sox2_guide1/
│   │   │   ├── larva_001.lif  (Leica image format)
│   │   │   └── ... (30 larvae)
│   │   └── ...
│   └── histology/
│       ├── 20241015_mouse_aav_sox2/
│       │   ├── mouse_001_BDA_tracing.tif
│       │   └── ...
└── metadata/
    ├── sample_manifest_bulk_rnaseq.csv
    ├── sample_manifest_scrna_seq.csv
    └── experimental_timeline.xlsx
```

**Bucket: `neuroregen-results`** (Processed data, analysis outputs)
```
neuroregen-results/
├── bulk-rnaseq/
│   ├── aligned/
│   │   ├── zebrafish_injured_6h_rep1.bam
│   │   └── ... (360 BAM files)
│   ├── counts/
│   │   ├── featureCounts_all_samples.txt
│   │   └── count_matrix.csv
│   ├── differential_expression/
│   │   ├── DESeq2_zebrafish_7d_vs_0h.csv
│   │   ├── DESeq2_mouse_7d_vs_0h.csv
│   │   ├── volcano_plots/
│   │   └── heatmaps/
│   └── pathway_analysis/
│       ├── GSEA_results_zebrafish.xlsx
│       └── GO_enrichment_top200_genes.csv
├── single-cell/
│   ├── seurat_objects/
│   │   ├── integrated_all_timepoints.rds (Seurat object, 5GB)
│   │   └── ...
│   ├── cell_type_markers/
│   │   ├── cluster_markers_all.csv
│   │   └── neuron_subtype_markers.csv
│   └── trajectories/
│       ├── monocle3_pseudotime.rds
│       └── trajectory_plots/
├── crispr_validation/
│   ├── genotyping/
│   │   ├── T7EI_gels/
│   │   └── sanger_sequences/
│   ├── phenotyping/
│   │   ├── regeneration_index_measurements.csv
│   │   └── statistical_tests.csv
│   └── summary/
│       ├── validated_genes_list.csv
│       └── crispr_summary_plots.pdf
├── aav_mouse/
│   ├── behavior/
│   │   ├── BBB_scores_longitudinal.csv
│   │   └── BBB_plots.pdf
│   ├── histology/
│   │   ├── axon_counts.csv
│   │   ├── lesion_volume_measurements.csv
│   │   └── processed_images/
│   └── electrophysiology/
│       ├── MEP_data.csv
│       └── MEP_traces.png
├── figures/
│   ├── manuscript_figures/
│   │   ├── Fig1_experimental_design.pdf
│   │   ├── Fig2_transcriptomic_atlas.pdf
│   │   └── ...
│   └── supplementary/
└── publications/
    ├── paper1_comparative_transcriptomics/
    │   ├── manuscript.docx
    │   ├── supplementary_tables.xlsx
    │   └── code_archive.zip
    └── ...
```

---

## 3. Data Processing Pipelines

### 3.1 Bulk RNA-seq Pipeline (Nextflow)

**Pipeline:** `nf-core/rnaseq` v3.12.0 (community standard pipeline)

**Configuration File:** `nextflow.config`
```groovy
params {
    // Input
    input = 's3://neuroregen-raw/bulk-rnaseq/samplesheet.csv'
    outdir = 's3://neuroregen-results/bulk-rnaseq/'

    // Reference genome
    genome = 'GRCz11'  // or GRCm39 for mouse
    fasta = 's3://ngi-igenomes/igenomes/Danio_rerio/Ensembl/GRCz11/Sequence/WholeGenomeFasta/genome.fa'
    gtf = 's3://ngi-igenomes/igenomes/Danio_rerio/Ensembl/GRCz11/Annotation/Genes/genes.gtf'

    // Read trimming
    trim_nextseq = 20  // trim low-quality 3' ends

    // Alignment
    aligner = 'star'
    star_index = 's3://neuroregen-results/references/STAR_index_GRCz11/'

    // Quantification
    pseudo_aligner = null  // use STAR alignment, not pseudo-alignment
    featurecounts_group_type = 'gene_id'

    // QC
    skip_qc = false
    skip_fastqc = false
    skip_rseqc = false

    // Resources
    max_cpus = 16
    max_memory = '64.GB'
    max_time = '24.h'
}

process {
    executor = 'slurm'
    queue = 'hotel'  // UCSD TSCC partition

    withName: 'STAR_ALIGN' {
        cpus = 16
        memory = 64.GB
        time = 4.h
    }

    withName: 'FEATURECOUNTS' {
        cpus = 4
        memory = 16.GB
        time = 1.h
    }
}

singularity {
    enabled = true
    autoMounts = true
    cacheDir = '/home/kowalska/singularity_cache'
}

aws {
    accessKey = secrets.AWS_ACCESS_KEY_ID
    secretKey = secrets.AWS_SECRET_ACCESS_KEY
    region = 'us-west-2'
}
```

**Execution:**
```bash
nextflow run nf-core/rnaseq \
    -profile singularity,ucsd_tscc \
    -c nextflow.config \
    -resume  # resume from last checkpoint if interrupted
```

**Pipeline Steps:**
1. **FastQC** (v0.11.9): Quality control of raw FASTQ
2. **Trim Galore** (v0.6.7): Adapter trimming + quality filtering
3. **STAR** (v2.7.10b): Alignment to reference genome
4. **SAMtools** (v1.17): BAM sorting, indexing, stats
5. **featureCounts** (v2.0.3): Gene-level quantification
6. **MultiQC** (v1.14): Aggregate QC report
7. **RSeQC** (v4.0.0): RNA-seq specific QC (insert size, read distribution)

**Output:**
- `aligned/*.bam`: Aligned reads (for visualization in IGV)
- `counts/featureCounts_all_samples.txt`: Gene count matrix
- `multiqc_report.html`: Comprehensive QC report
- `pipeline_info/`: Execution logs, resource usage

**Performance:**
- **Time:** ~4 hours per sample (50M reads, 16 cores)
- **Total:** 360 samples × 4h = 1440 hours = 90 hours wall-clock time (with 16 parallel jobs)
- **Cost:** UCSD TSCC is free for researchers (NIH-funded cluster)

### 3.2 Single-Cell RNA-seq Pipeline

**Pipeline:** Custom Nextflow + CellRanger + Seurat

**Step 1: CellRanger Count** (10X Genomics)
```bash
#!/bin/bash
#SBATCH --job-name=cellranger
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=8:00:00

cellranger count \
    --id=sample_zebrafish_0h_rep1 \
    --transcriptome=/home/kowalska/references/refdata-gex-GRCz11-2020-A \
    --fastqs=s3://neuroregen-raw/single-cell/10x_run_20240520/fastq/ \
    --sample=zebrafish_0h_rep1 \
    --expect-cells=10000 \
    --localcores=16 \
    --localmem=64
```

**Output:**
- `filtered_feature_bc_matrix/`: Cell × gene count matrix (MTX format)
- `web_summary.html`: QC metrics (estimated cells, median genes/cell, etc.)
- `cloupe.cloupe`: For visualization in 10X Loupe Browser

**Step 2: Seurat Analysis** (R script)
```R
# File: scripts/seurat_analysis.R

library(Seurat)
library(dplyr)
library(ggplot2)

# Load 10X data
data_dir <- "s3://neuroregen-results/single-cell/cellranger/sample_zebrafish_0h_rep1/outs/filtered_feature_bc_matrix/"
counts <- Read10X(data.dir = data_dir)

# Create Seurat object
seurat_obj <- CreateSeuratObject(
    counts = counts,
    project = "NeuroRegen",
    min.cells = 3,  # gene must be in ≥3 cells
    min.features = 200  # cell must have ≥200 genes
)

# Add metadata
seurat_obj$sample <- "zebrafish_0h_rep1"
seurat_obj$species <- "zebrafish"
seurat_obj$timepoint <- 0
seurat_obj$condition <- "control"

# Calculate QC metrics
seurat_obj[["percent.mt"]] <- PercentageFeatureSet(seurat_obj, pattern = "^mt-")

# QC filtering
seurat_obj <- subset(seurat_obj, subset =
    nFeature_RNA > 200 &
    nFeature_RNA < 5000 &
    nCount_RNA > 500 &
    nCount_RNA < 30000 &
    percent.mt < 10
)

# Normalization (SCTransform - replaces NormalizeData + ScaleData + FindVariableFeatures)
seurat_obj <- SCTransform(seurat_obj, vars.to.regress = "percent.mt", verbose = FALSE)

# Dimensionality reduction
seurat_obj <- RunPCA(seurat_obj, npcs = 50, verbose = FALSE)
seurat_obj <- RunUMAP(seurat_obj, dims = 1:30, verbose = FALSE)

# Clustering
seurat_obj <- FindNeighbors(seurat_obj, dims = 1:30)
seurat_obj <- FindClusters(seurat_obj, resolution = 0.5)

# Save
saveRDS(seurat_obj, "s3://neuroregen-results/single-cell/seurat_objects/zebrafish_0h_rep1.rds")
```

**Step 3: Integration** (merge all timepoints)
```R
# Load all samples
sample_list <- lapply(sample_ids, function(id) {
    readRDS(paste0("s3://neuroregen-results/single-cell/seurat_objects/", id, ".rds"))
})

# Integrate using CCA (canonical correlation analysis)
features <- SelectIntegrationFeatures(object.list = sample_list, nfeatures = 3000)
sample_list <- PrepSCTIntegration(object.list = sample_list, anchor.features = features)
anchors <- FindIntegrationAnchors(
    object.list = sample_list,
    normalization.method = "SCT",
    anchor.features = features
)
integrated <- IntegrateData(anchorset = anchors, normalization.method = "SCT")

# Re-run PCA/UMAP on integrated data
integrated <- RunPCA(integrated, npcs = 50, verbose = FALSE)
integrated <- RunUMAP(integrated, dims = 1:30, reduction = "pca", verbose = FALSE)
integrated <- FindNeighbors(integrated, dims = 1:30, reduction = "pca")
integrated <- FindClusters(integrated, resolution = 0.5)

# Save integrated object
saveRDS(integrated, "s3://neuroregen-results/single-cell/seurat_objects/integrated_all_timepoints.rds")
```

**Step 4: Cell Type Annotation**
```R
library(SingleR)

# Load reference (zebrafish cell atlas)
ref <- celldex::DatabaseImmuneCellExpressionData()  # placeholder - use actual zebrafish reference

# Annotate
predictions <- SingleR(
    test = GetAssayData(integrated, slot = "data"),
    ref = ref,
    labels = ref$label.main
)

# Add to Seurat object
integrated$cell_type_singleR <- predictions$labels
integrated$cell_type_confidence <- predictions$scores

# Manual refinement based on marker genes
neuron_markers <- c("elavl3", "snap25", "tubb3")
oligodendrocyte_markers <- c("mbp", "plp1a", "mag")
astrocyte_markers <- c("gfap", "s100b", "aldh1l1")
# ... etc.

# Assign cell types
integrated$cell_type_manual <- case_when(
    integrated$seurat_clusters %in% c(0, 2, 5, 7) ~ "Neuron",
    integrated$seurat_clusters == 1 ~ "Oligodendrocyte",
    integrated$seurat_clusters == 3 ~ "Astrocyte",
    integrated$seurat_clusters == 4 ~ "Radial Glia",
    # ... etc.
)
```

### 3.3 Image Analysis Pipeline (Snakemake)

**Pipeline:** Automated axon quantification from confocal images

**Snakefile:**
```python
# File: workflows/image_analysis/Snakefile

SAMPLES = glob_wildcards("data/confocal/{sample}.lif").sample

rule all:
    input:
        expand("results/axon_quantification/{sample}_regeneration_index.csv", sample=SAMPLES),
        "results/summary/regeneration_index_all_samples.csv"

rule convert_lif_to_tif:
    """Convert Leica .lif to .tif using bioformats"""
    input:
        "data/confocal/{sample}.lif"
    output:
        "results/converted/{sample}_max_projection.tif"
    conda:
        "envs/bioformats.yaml"
    shell:
        """
        bfconvert -bigtiff -noflat -series 0 \
            -z 0-{params.z_slices} -projection max \
            {input} {output}
        """

rule segment_axons:
    """Segment axons using Fiji (ImageJ) macro"""
    input:
        "results/converted/{sample}_max_projection.tif"
    output:
        binary="results/segmented/{sample}_binary.tif",
        skeleton="results/segmented/{sample}_skeleton.tif"
    params:
        fiji_macro="scripts/segment_axons.ijm"
    shell:
        """
        fiji --headless \
            --run {params.fiji_macro} \
            'input={input},output_binary={output.binary},output_skeleton={output.skeleton}'
        """

rule measure_axon_length:
    """Quantify axon length beyond lesion"""
    input:
        skeleton="results/segmented/{sample}_skeleton.tif",
        lesion_mask="data/lesion_masks/{sample}_lesion.roi"
    output:
        "results/axon_quantification/{sample}_regeneration_index.csv"
    conda:
        "envs/python_analysis.yaml"
    script:
        "scripts/measure_axon_length.py"

rule aggregate_results:
    """Combine all measurements into single table"""
    input:
        expand("results/axon_quantification/{sample}_regeneration_index.csv", sample=SAMPLES)
    output:
        "results/summary/regeneration_index_all_samples.csv"
    script:
        "scripts/aggregate_measurements.py"
```

**Fiji Macro:** `scripts/segment_axons.ijm`
```javascript
// ImageJ macro for axon segmentation
#@ File (label="Input image") input
#@ File (label="Output binary") output_binary
#@ File (label="Output skeleton") output_skeleton

// Open image
open(input);

// Preprocessing
run("Subtract Background...", "rolling=50");
run("Gaussian Blur...", "sigma=2");

// Thresholding (Otsu method)
setAutoThreshold("Otsu dark");
run("Convert to Mask");

// Morphological operations
run("Despeckle");
run("Remove Outliers...", "radius=2 threshold=50 which=Bright");
run("Fill Holes");

// Save binary
saveAs("Tiff", output_binary);

// Skeletonize
run("Skeletonize");
saveAs("Tiff", output_skeleton);

// Clean up
close("*");
```

**Python Script:** `scripts/measure_axon_length.py`
```python
import numpy as np
from skimage import io, measure
import pandas as pd

# Load skeleton image
skeleton = io.imread(snakemake.input.skeleton)

# Load lesion ROI (manually drawn boundary)
lesion_boundary = load_roi(snakemake.input.lesion_mask)  # custom function

# Identify axons crossing lesion
labeled_skeleton = measure.label(skeleton)
regions = measure.regionprops(labeled_skeleton)

# Measure max extension beyond lesion
max_extension = 0
for region in regions:
    coords = region.coords
    # Check if axon crosses lesion boundary
    if crosses_boundary(coords, lesion_boundary):
        extension = max_distance_beyond_boundary(coords, lesion_boundary)
        max_extension = max(max_extension, extension)

# Calculate regeneration index
spinal_cord_length = measure_spinal_cord_length(skeleton)  # custom function
regeneration_index = max_extension / spinal_cord_length

# Save results
results = pd.DataFrame({
    'sample': [snakemake.wildcards.sample],
    'max_axon_extension_um': [max_extension],
    'spinal_cord_length_um': [spinal_cord_length],
    'regeneration_index': [regeneration_index]
})
results.to_csv(snakemake.output[0], index=False)
```

---

## 4. Integration Points

### 4.1 Electronic Lab Notebook (Benchling)

**API Integration:** Automatically link analysis results to ELN entries

**Script:** `scripts/sync_to_benchling.py`
```python
import benchling_sdk
from benchling_sdk.auth.api_key_auth import ApiKeyAuth
from benchling_sdk.benchling import Benchling

# Authenticate
auth = ApiKeyAuth(os.environ['BENCHLING_API_KEY'])
benchling = Benchling(url="https://ucsd.benchling.com", auth=auth)

# Create entry for RNA-seq run
entry = benchling.entries.create(
    schema_id="seq_rna_seq_run",  # custom schema
    fields={
        "Sequencing Run ID": "run_20240315_NovaSeq6000_A00987",
        "Num Samples": 96,
        "Sequencer": "NovaSeq 6000",
        "Sequencing Date": "2024-03-15",
        "Data Path": "s3://neuroregen-raw/bulk-rnaseq/run_20240315/",
        "MultiQC Report": "[Download](https://neuroregen-results.s3.amazonaws.com/multiqc_report.html)"
    },
    folder_id="lib_abc123",  # RNA-seq folder
    name=f"RNA-seq Run {run_id}"
)

# Upload QC plot as attachment
benchling.blobs.upload_file(
    file_path="results/multiqc_report.html",
    entry_id=entry.id
)
```

### 4.2 Slack Notifications

**Webhook Integration:** Notify team when pipeline completes

**Nextflow Config:**
```groovy
notification {
    enabled = true
    to = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX'
}
```

**Custom Notification Script:**
```python
import requests
import json

def send_slack_notification(message, webhook_url):
    payload = {
        "text": message,
        "username": "NeuroRegen Pipeline Bot",
        "icon_emoji": ":dna:"
    }
    response = requests.post(webhook_url, data=json.dumps(payload))
    return response.status_code

# Example usage
send_slack_notification(
    f"✅ RNA-seq pipeline completed! {num_samples} samples processed. MultiQC report: {report_url}",
    webhook_url=os.environ['SLACK_WEBHOOK_URL']
)
```

### 4.3 Public Data Portal (React + Flask)

**Architecture:**
```
Frontend (React) → API Gateway → Flask Backend → PostgreSQL + S3
```

**Flask API:** `api/app.py`
```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import boto3

app = Flask(__name__)
CORS(app)

# Database connection
def get_db():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        database='neuroregen',
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )

# Endpoint: Get gene expression data
@app.route('/api/genes/<gene_symbol>/expression', methods=['GET'])
def get_gene_expression(gene_symbol):
    species = request.args.get('species', 'zebrafish')

    conn = get_db()
    cur = conn.cursor()

    query = """
        SELECT
            s.sample_name,
            s.species,
            s.condition,
            s.timepoint_hours,
            ec.normalized_count,
            ec.tpm
        FROM expression_counts ec
        JOIN genes g ON ec.gene_id = g.gene_id
        JOIN samples s ON ec.sample_id = s.sample_id
        WHERE g.gene_symbol = %s AND s.species = %s
        ORDER BY s.timepoint_hours, s.biological_replicate;
    """

    cur.execute(query, (gene_symbol, species))
    results = cur.fetchall()

    cur.close()
    conn.close()

    # Format response
    expression_data = [
        {
            'sample': row[0],
            'species': row[1],
            'condition': row[2],
            'timepoint_hours': row[3],
            'normalized_count': float(row[4]),
            'tpm': float(row[5])
        }
        for row in results
    ]

    return jsonify({
        'gene_symbol': gene_symbol,
        'species': species,
        'num_samples': len(expression_data),
        'expression_data': expression_data
    })

# Endpoint: Get differential expression results
@app.route('/api/comparisons/<comparison_name>/genes', methods=['GET'])
def get_de_genes(comparison_name):
    # Query parameters
    padj_threshold = float(request.args.get('padj', 0.01))
    log2fc_threshold = float(request.args.get('log2fc', 2.0))
    limit = int(request.args.get('limit', 100))

    conn = get_db()
    cur = conn.cursor()

    query = """
        SELECT
            g.gene_symbol,
            g.gene_name,
            de.log2_fold_change,
            de.adjusted_pvalue,
            de.base_mean
        FROM differential_expression de
        JOIN genes g ON de.gene_id = g.gene_id
        JOIN comparisons c ON de.comparison_id = c.comparison_id
        WHERE c.comparison_name = %s
          AND de.adjusted_pvalue < %s
          AND ABS(de.log2_fold_change) > %s
        ORDER BY de.adjusted_pvalue ASC
        LIMIT %s;
    """

    cur.execute(query, (comparison_name, padj_threshold, log2fc_threshold, limit))
    results = cur.fetchall()

    cur.close()
    conn.close()

    de_genes = [
        {
            'gene_symbol': row[0],
            'gene_name': row[1],
            'log2FoldChange': float(row[2]),
            'padj': float(row[3]),
            'baseMean': float(row[4])
        }
        for row in results
    ]

    return jsonify({
        'comparison': comparison_name,
        'filters': {
            'padj': padj_threshold,
            'log2fc': log2fc_threshold
        },
        'num_genes': len(de_genes),
        'genes': de_genes
    })

# Endpoint: Download file from S3
@app.route('/api/files/<path:file_path>', methods=['GET'])
def download_file(file_path):
    s3 = boto3.client('s3')
    bucket = 'neuroregen-results'

    # Generate presigned URL (expires in 1 hour)
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': file_path},
        ExpiresIn=3600
    )

    return jsonify({'download_url': url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**React Frontend:** `frontend/src/components/GeneExpressionPlot.jsx`
```javascript
import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';

function GeneExpressionPlot({ geneSymbol, species }) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(
                    `https://api.neuroregen.ucsd.edu/api/genes/${geneSymbol}/expression`,
                    { params: { species } }
                );
                setData(response.data.expression_data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching gene expression:', error);
                setLoading(false);
            }
        };

        fetchData();
    }, [geneSymbol, species]);

    if (loading) return <div>Loading...</div>;

    // Prepare data for Plotly
    const timepoints = [...new Set(data.map(d => d.timepoint_hours))];
    const conditions = [...new Set(data.map(d => d.condition))];

    const traces = conditions.map(condition => {
        const filtered = data.filter(d => d.condition === condition);
        return {
            x: filtered.map(d => d.timepoint_hours),
            y: filtered.map(d => d.normalized_count),
            type: 'scatter',
            mode: 'lines+markers',
            name: condition,
        };
    });

    return (
        <div>
            <h3>Expression of {geneSymbol} in {species}</h3>
            <Plot
                data={traces}
                layout={{
                    xaxis: { title: 'Time post-injury (hours)' },
                    yaxis: { title: 'Normalized count' },
                    width: 800,
                    height: 500,
                }}
            />
        </div>
    );
}

export default GeneExpressionPlot;
```

---

## 5. Performance Requirements

### 5.1 Computational Performance

**RNA-seq Alignment (STAR):**
- **Throughput:** 1 sample in 4 hours (50M reads, 16 cores)
- **Memory:** 64GB peak RAM
- **Scaling:** Linear with read count, logarithmic with genome size

**Differential Expression (DESeq2):**
- **Throughput:** Full dataset (360 samples × 25k genes) in 30 minutes (8 cores)
- **Memory:** 32GB
- **Bottleneck:** Count matrix loading (optimize with HDF5 format)

**Single-cell Integration (Seurat):**
- **Throughput:** 50k cells in 2 hours (30 PCs, integration)
- **Memory:** 128GB (proportional to cell count)
- **Optimization:** Use `SCTransform` instead of `NormalizeData` (faster)

### 5.2 API Performance

**Response Time Targets:**
- Gene expression query: <200ms (95th percentile)
- DE gene list: <500ms (95th percentile)
- File download URL generation: <100ms

**Optimization Strategies:**
- Database indexing on frequently queried columns (gene_symbol, sample_id)
- Redis caching for popular queries (TTL 1 hour)
- Pagination for large result sets (limit 100 genes per page)

**Load Testing:**
- Tool: Apache JMeter
- Target: 100 concurrent users, 1000 requests/minute
- Scaling: Deploy on AWS ECS with autoscaling (2-10 containers)

### 5.3 Data Transfer

**S3 Upload/Download:**
- Network: 10 Gbps UCSD campus network
- Bandwidth: ~1 GB/s sustained (limited by disk I/O, not network)
- Optimization: Use `aws s3 sync` with `--include` filters, multipart uploads

**Benchmarks:**
- Upload 500GB RNA-seq data: ~10 minutes
- Download 5GB Seurat object: ~1 minute

---

## 6. Quality Assurance

### 6.1 Unit Testing (Python)

**Framework:** pytest

**Example:** `tests/test_axon_measurement.py`
```python
import pytest
import numpy as np
from scripts.measure_axon_length import calculate_regeneration_index

def test_regeneration_index_full_recovery():
    """Test that full regeneration gives index of 1.0"""
    max_extension = 500  # µm
    spinal_cord_length = 500  # µm
    assert calculate_regeneration_index(max_extension, spinal_cord_length) == 1.0

def test_regeneration_index_no_recovery():
    """Test that no regeneration gives index of 0.0"""
    max_extension = 0
    spinal_cord_length = 500
    assert calculate_regeneration_index(max_extension, spinal_cord_length) == 0.0

def test_regeneration_index_partial():
    """Test partial regeneration"""
    max_extension = 250
    spinal_cord_length = 500
    assert calculate_regeneration_index(max_extension, spinal_cord_length) == 0.5

def test_zero_spinal_cord_length():
    """Test that zero spinal cord length raises error"""
    with pytest.raises(ValueError):
        calculate_regeneration_index(100, 0)
```

**Coverage Target:** >80% code coverage (measured with `pytest-cov`)

### 6.2 Integration Testing (Pipelines)

**Test Dataset:**
- Small subset (1000 reads per sample, 10 samples)
- Known results (pre-computed on full dataset)
- Fast execution (~5 minutes for full pipeline)

**Validation:**
```bash
# Run pipeline on test data
nextflow run nf-core/rnaseq -profile test

# Compare to expected results
python scripts/validate_results.py \
    --test_output results/test_run/counts.txt \
    --expected_output tests/expected/counts.txt \
    --tolerance 0.05  # allow 5% deviation due to stochasticity
```

### 6.3 Reproducibility

**Docker Containers:**
- All analysis environments containerized
- Published to Docker Hub: `kowalska/neuroregen:v1.0`
- Includes exact package versions (pinned in Dockerfile)

**Dockerfile Example:**
```dockerfile
FROM bioconductor/bioconductor_docker:RELEASE_3_17

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libhdf5-dev

# Install R packages (with versions)
RUN R -e "BiocManager::install(c( \
    'DESeq2@1.38.0', \
    'Seurat@4.3.0', \
    'clusterProfiler@4.6.0' \
))"

# Install Python packages
RUN pip install \
    scanpy==1.9.3 \
    anndata==0.8.0 \
    scikit-learn==1.3.0

# Copy analysis scripts
COPY scripts/ /opt/scripts/
WORKDIR /opt/scripts

CMD ["/bin/bash"]
```

**Validation:**
- Compare DESeq2 results to edgeR (alternative DE method)
- Concordance target: >95% for top 100 DE genes
- Replicate analysis on independent dataset (public data)

---

## 7. Security & Compliance

### 7.1 Data Security

**Encryption:**
- At rest: AWS S3 server-side encryption (AES-256)
- In transit: TLS 1.3 for all API calls

**Access Control:**
- AWS IAM roles (principle of least privilege)
- Database: Role-based access (read-only for web portal, read-write for pipelines)

**Backup:**
- S3 versioning enabled (retain deleted objects for 90 days)
- Daily PostgreSQL backups (AWS RDS automated backups, 7-day retention)

### 7.2 Compliance

**Data Sharing (NSF Requirements):**
- Public release timeline: Upon publication or 4 years (whichever earlier)
- Metadata standards: MINSEQE for RNA-seq, following Encode guidelines

**IACUC:**
- All animal data linked to approved protocol numbers (#2024-0456, #2024-0457)
- Annual reporting of animal usage to IACUC

**IBC (Institutional Biosafety Committee):**
- AAV work logged (lot numbers, dates, personnel)
- Spill protocols documented in ELN

---

## 8. Deployment & Operations

### 8.1 Infrastructure Provisioning (Terraform)

**AWS Resources:**
```hcl
# File: terraform/main.tf

provider "aws" {
  region = "us-west-2"
}

# S3 buckets
resource "aws_s3_bucket" "raw_data" {
  bucket = "neuroregen-raw"

  versioning {
    enabled = true
  }

  lifecycle_rule {
    enabled = true
    transition {
      days          = 90
      storage_class = "GLACIER"  # archive old data to save costs
    }
  }
}

resource "aws_s3_bucket" "results" {
  bucket = "neuroregen-results"

  website {
    index_document = "index.html"
  }
}

# PostgreSQL database
resource "aws_db_instance" "neuroregen_db" {
  identifier              = "neuroregen-db"
  engine                  = "postgres"
  engine_version          = "14.7"
  instance_class          = "db.t3.medium"
  allocated_storage       = 100
  storage_type            = "gp3"

  db_name                 = "neuroregen"
  username                = var.db_username
  password                = var.db_password

  backup_retention_period = 7
  backup_window           = "03:00-04:00"

  vpc_security_group_ids  = [aws_security_group.db.id]
  publicly_accessible     = false
}

# ECS for Flask API
resource "aws_ecs_cluster" "api_cluster" {
  name = "neuroregen-api"
}

resource "aws_ecs_task_definition" "api" {
  family                   = "neuroregen-flask-api"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  container_definitions = jsonencode([{
    name  = "flask-api"
    image = "kowalska/neuroregen-api:latest"
    portMappings = [{
      containerPort = 5000
      hostPort      = 5000
    }]
    environment = [
      { name = "DB_HOST", value = aws_db_instance.neuroregen_db.address },
      { name = "DB_NAME", value = "neuroregen" }
    ]
    secrets = [
      { name = "DB_PASSWORD", valueFrom = aws_secretsmanager_secret.db_password.arn }
    ]
  }])
}
```

### 8.2 Monitoring

**CloudWatch Metrics:**
- API latency (p50, p95, p99)
- Database connections, CPU, memory
- S3 bucket size, request count

**Alerts:**
- API p95 latency >500ms → Slack notification
- Database CPU >80% → Email to tech lead
- Pipeline failure → Slack notification

**Logging:**
- Application logs: CloudWatch Logs (retention 30 days)
- Audit logs: S3 (immutable, 7-year retention for compliance)

---

## 9. Documentation

### 9.1 Code Documentation

**Standards:**
- Python: Google-style docstrings
- R: Roxygen2 comments
- SQL: Inline comments for complex queries

**Example:**
```python
def calculate_regeneration_index(max_extension_um, spinal_cord_length_um):
    """
    Calculate regeneration index for zebrafish spinal cord injury.

    The regeneration index is defined as the ratio of maximum axon extension
    beyond the lesion site to the total spinal cord length. A value of 1.0
    indicates complete regeneration, while 0.0 indicates no axon growth.

    Args:
        max_extension_um (float): Maximum distance of axon regrowth beyond
            lesion epicenter, measured in micrometers.
        spinal_cord_length_um (float): Total length of spinal cord from
            brain to tail, measured in micrometers.

    Returns:
        float: Regeneration index (0.0 to 1.0)

    Raises:
        ValueError: If spinal_cord_length_um is zero or negative.

    Examples:
        >>> calculate_regeneration_index(500, 500)
        1.0  # Full regeneration

        >>> calculate_regeneration_index(250, 500)
        0.5  # Partial regeneration
    """
    if spinal_cord_length_um <= 0:
        raise ValueError("Spinal cord length must be positive")

    return max_extension_um / spinal_cord_length_um
```

### 9.2 User Documentation

**README Files:**
- Repository root: Project overview, installation, quick start
- Each pipeline: Detailed usage, parameters, troubleshooting

**Wiki:**
- GitHub Wiki: Protocols, SOPs, FAQs
- Updated by all team members (encourage contributions)

**Video Tutorials:**
- YouTube playlist: Lab techniques (microinjection, mouse surgery)
- Data portal usage (search genes, download data)

---

## 10. Maintenance & Support

### 10.1 Update Schedule

**Software Updates:**
- Monthly: Security patches for OS, Docker images
- Quarterly: Dependency updates (R packages, Python libraries)
- Annual: Major version upgrades (after testing)

**Database:**
- Weekly: Vacuum analyze (optimize query performance)
- Monthly: Integrity checks (foreign key constraints)

### 10.2 Support Channels

**Internal (Lab):**
- Slack #neuroregen-tech channel
- Weekly data analysis meeting (Fridays 2pm)

**External (Community):**
- GitHub Issues: Bug reports, feature requests
- Email: neuroregen-support@ucsd.edu
- Response time: 3 business days

---

**Document Prepared By:** Dr. Sarah Chen (Computational Lead)
**Last Updated:** December 27, 2025
**Version:** 2.4
**Next Review:** March 2026

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Research Plan - Biology]** `biology-research-plan-example.md`
  - Type: `requires`
  - Status constraint: `approved`
  - Reason: System architecture implements research methodology and data workflows
  - Sections used: Methodology (defines data pipeline), Equipment (informs infrastructure), Timeline (capacity planning)
  - Validation: Data models must accommodate all assay types (RNA-seq, CRISPR, imaging)
  - Condition: `when domain === 'biology'`

- **[Executive Summary - Biology]** `biology-executive-summary-example.md`
  - Type: `informs`
  - Reason: Scale estimates (50k cells, 180 samples) drive storage/compute requirements
  - Sections used: Expected Outcomes (data volume), Team Composition (user accounts)

- **[Data Model Schema]** `schemas/biology_experiment_schema.json`
  - Type: `requires`
  - Reason: Database design requires formalized entity-relationship model
  - Evidence ID: `E-BIO-TDD-001`
  - Must include: Sample, Experiment, Assay, Result entities

- **[IRB/IACUC Data Requirements]** `compliance/IACUC_data_retention_policy.pdf`
  - Type: `requires`
  - Reason: Regulatory compliance drives retention and audit requirements
  - Condition: `when animal_research === true`

### Impacts (Downstream Documents)
- **[Implementation Tasks]** `jira/BIO-TDD-IMPLEMENTATION-EPIC`
  - Type: `blocks`
  - Until: `this.status == approved`
  - Reason: Cannot start development until technical design approved
  - Cascade: `true`
  - Generated tasks: Database setup, API development, Pipeline deployment

- **[Runbook]** `docs/ops/biology_data_platform_runbook.md`
  - Type: `informs`
  - Reason: Deployment procedures and monitoring plans based on architecture
  - Sections impacted: Start/Stop procedures, Monitoring dashboards, Incident response

- **[Test Plan]** `docs/testing/biology_system_test_plan.md`
  - Type: `informs`
  - Reason: API endpoints and performance requirements define test cases
  - Sections impacted: API tests, Load tests, Data integrity tests

- **[Security Plan]** `docs/security/biology_platform_security_plan.md`
  - Type: `blocks`
  - Until: `this.status == in-review`
  - Reason: Architecture decisions (cloud provider, encryption) inform security controls

### Related Documents
- **[Chemistry TDD]** `chemistry-tdd-example.md`
  - Relationship: `parallel-example`
  - Reason: Different data types (molecular structures vs genomic data) but similar architecture patterns
  - Shared patterns: AWS infrastructure, PostgreSQL for metadata, S3 for raw data

- **[Physics TDD]** `physics-tdd-example.md`
  - Relationship: `parallel-example`
  - Reason: Experimental data platform architecture comparison
  - Shared patterns: Time-series data handling, HPC integration

- **[Psychology TDD]** `psychology-tdd-example.md`
  - Relationship: `parallel-example`
  - Reason: Human subjects data with different compliance requirements (HIPAA vs IACUC)

### Satellite Documents
- **[TODO per Section]** `satellites/TODO-TDD-BIO-001.md`
  - Purpose: Track completion of each major component
  - Granularity: System Architecture, Data Models, API, Database, Security, Performance, Observability, Deployment
  - Status: `completed`

- **[DOR (Definition of Ready)]** `satellites/DOR-TDD-BIO-001.md`
  - Criteria before starting TDD:
    - [ ] Research Plan approved (methodology finalized)
    - [ ] Data model finalized (schema reviewed by bioinformatician)
    - [ ] Infrastructure budget approved ($150k AWS estimate)
    - [ ] Security requirements documented (IACUC compliance)
    - [ ] Tech Lead assigned
  - Status: `met`

- **[DOD (Definition of Done)]** `satellites/DOD-TDD-BIO-001.md`
  - Criteria before approval:
    - [ ] All major components detailed (architecture, DB, API, security)
    - [ ] API documented (OpenAPI spec generated)
    - [ ] Security controls specified (encryption, access control, audit)
    - [ ] Performance benchmarked (load test results for expected scale)
    - [ ] Deployment plan validated (staging environment tested)
    - [ ] Architecture review completed (senior engineer + security officer)
  - Status: `met`

- **[ADR Collection]** `satellites/ADR-TDD-BIO-*.md`
  - Key decisions:
    - ADR-TDD-BIO-001: PostgreSQL vs MongoDB for metadata
    - ADR-TDD-BIO-002: AWS vs Azure (chose AWS for better genomics tools)
    - ADR-TDD-BIO-003: Data retention policy (7 years per IACUC)
    - ADR-TDD-BIO-004: API authentication (OAuth2 vs API keys)
  - Status: All approved

### Conditional Cross-References

```yaml
conditions:
  - when: domain === 'biology'
    require_dependencies:
      - IACUC data handling requirements (if animal data)
      - Biosafety data security (if pathogen sequences)
    require_satellites:
      - ADR for database choice (genomic data has specific needs)
      - ADR for cloud provider (genomics-optimized instances)
    data_model_requirements:
      - Sample entity must track IACUC protocol number
      - Animal entity with welfare status tracking
      - Assay entity with biosafety level annotation

  - when: data_type === 'genomic'
    require_dependencies:
      - Data privacy assessment (if human genomic data → HIPAA)
      - De-identification plan (if sharing data publicly)
    require_satellites:
      - ADR for encryption at rest (HIPAA compliance)
      - ADR for data retention (NIH genomic data sharing policy)
    infrastructure_requirements:
      - Storage: ≥10 TB (raw FASTQ + processed BAM)
      - Compute: GPU-enabled for deep learning variant calling (optional)
      - Network: High-bandwidth for data transfer (10 Gbps)

  - when: infrastructure === 'cloud'
    require_dependencies:
      - Cloud cost estimates (E-TDD-BIO-002)
      - Disaster recovery plan
      - Backup strategy (cross-region replication)
    require_satellites:
      - ADR for cloud provider selection
      - ADR for data sovereignty (GDPR if EU collaborators)
    security_requirements:
      - Encryption in transit (TLS 1.3)
      - Encryption at rest (AES-256)
      - VPN access for administrative tasks

  - when: collaboration === true
    require_dependencies:
      - Data sharing agreements (who can access what)
      - Multi-tenant architecture design
    data_model_requirements:
      - Organization entity (multi-org support)
      - Permissions (role-based access control per org)

  - when: budget > 100000
    require_approvals:
      - IT Director
      - CFO (for multi-year cloud commitments)
      - Security Officer (for data protection controls)

  - when: involves_human_data === true
    require_dependencies:
      - HIPAA compliance architecture
      - IRB data security requirements
    security_requirements:
      - PHI encryption (HIPAA standard)
      - Audit logging (all data access tracked)
      - De-identification pipeline (if public sharing)

  - when: real_time_processing === true
    infrastructure_requirements:
      - Stream processing (Kafka or Kinesis)
      - Low-latency DB (Redis cache layer)
      - Event-driven architecture

  - when: machine_learning === true
    infrastructure_requirements:
      - GPU compute instances (NVIDIA T4 or better)
      - ML model registry (MLflow or SageMaker)
      - Feature store (for reproducibility)
```

### Validation Rules

**BLOCKER-level (must pass before approval):**
- [ ] All dependencies status ≥ `approved` (Research Plan, Data Model Schema)
- [ ] System architecture supports all assay types in Research Plan
- [ ] Data models accommodate all instrument outputs
- [ ] API documented (OpenAPI 3.0 spec generated)
- [ ] Security controls specified for IACUC compliance
- [ ] Performance benchmarked (meets 125% of expected load)
- [ ] Deployment tested in staging environment
- [ ] All ADRs approved (database, cloud, retention policy)

**ERROR-level (should fix before deployment):**
- [ ] Database schema has indexes on all foreign keys
- [ ] API has rate limiting (prevent abuse)
- [ ] Monitoring covers all critical metrics (CPU, memory, disk, API latency)
- [ ] Backup strategy tested (restore time <4 hours)
- [ ] Disaster recovery plan documented (RTO/RPO defined)

**WARN-level (recommended improvements):**
- [ ] API versioning strategy (v1, v2 with deprecation policy)
- [ ] Database migration strategy (zero-downtime deployments)
- [ ] Caching layer (Redis) for frequently accessed data
- [ ] CDN for static assets (if web UI)
- [ ] Cost optimization (reserved instances, auto-scaling policies)
