# Technical Design Document: GreenCat Project
## Laboratory Information Management System & Data Infrastructure

**Project ID:** NSF-CHE-2024-8945
**Technical Lead:** Dr. Michael Chen (Computational)
**Lab Manager:** Dr. Sofia Patel (Experimental)
**Version:** 1.9
**Date:** December 27, 2025

---

## 1. System Architecture

### 1.1 Overview

```
┌──────────────────────────────────────────────────────────────┐
│                  EXPERIMENTAL DATA LAYER                      │
├──────────────────────────────────────────────────────────────┤
│  Chemspeed Robot → Reaction data (conditions, observations)  │
│  UPLC-MS → Chromatograms, mass spectra (yield quantification│
│  NMR → FIDs, spectra (structure confirmation)                │
│  XRD → CIF files (crystal structures)                        │
│  ELN (Benchling) → Protocols, notes, metadata                │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                  COMPUTATIONAL DATA LAYER                     │
├──────────────────────────────────────────────────────────────┤
│  Gaussian/ORCA → DFT output files (.log, .out)               │
│  Python Scripts → ML models, predictions                      │
│  Reaxys → Literature reaction data (API)                     │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                    DATA INGESTION LAYER                       │
├──────────────────────────────────────────────────────────────┤
│  File Watcher → Auto-detect new files (inotify)              │
│  Parser → Extract data (NMR peaks, UPLC yields, DFT energies)│
│  Validator → QC checks (mass balance, expected products)     │
│  PostgreSQL → Structured data (reactions, compounds)         │
│  MongoDB → Unstructured data (spectra, images)               │
│  S3 → Raw files (UPLC .raw, NMR FIDs, DFT .log)             │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                    ANALYSIS LAYER                             │
├──────────────────────────────────────────────────────────────┤
│  RDKit → Molecular descriptors, fingerprints                  │
│  Scikit-learn → ML models (Random Forest, XGBoost)           │
│  Jupyter Notebooks → Interactive analysis                     │
│  Custom Scripts → Automated reporting                         │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                 VISUALIZATION & API LAYER                     │
├──────────────────────────────────────────────────────────────┤
│  Django REST API → Programmatic data access                   │
│  React Dashboard → Interactive plots (Plotly, ChemDraw)       │
│  Jupyter Widgets → Parameter exploration                      │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Data Models

### 2.1 Relational Database Schema (PostgreSQL)

#### Table: `compounds`
```sql
CREATE TABLE compounds (
    compound_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    smiles VARCHAR(500) UNIQUE NOT NULL,
    inchi VARCHAR(1000),
    inchi_key VARCHAR(50) UNIQUE,  -- for fast lookup
    compound_name VARCHAR(200),

    -- Molecular properties
    molecular_weight DECIMAL(8,3),
    exact_mass DECIMAL(10,5),
    formula VARCHAR(100),

    -- Classification
    compound_type ENUM('ligand', 'catalyst', 'substrate', 'product', 'reagent'),

    -- Structure file
    mol_file TEXT,  -- MDL MOL format
    structure_image_path VARCHAR(500),  -- PNG rendering

    -- Metadata
    cas_number VARCHAR(50),
    supplier VARCHAR(100),
    catalog_number VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_compounds_inchi_key ON compounds(inchi_key);
CREATE INDEX idx_compounds_type ON compounds(compound_type);
```

#### Table: `ligands`
```sql
CREATE TABLE ligands (
    ligand_id UUID PRIMARY KEY REFERENCES compounds(compound_id),

    -- Synthesis details
    synthesis_date DATE,
    synthesis_method TEXT,
    synthesized_by VARCHAR(100),
    batch_number VARCHAR(50),

    -- Characterization
    nmr_h1_confirmed BOOLEAN DEFAULT FALSE,
    nmr_c13_confirmed BOOLEAN DEFAULT FALSE,
    hrms_confirmed BOOLEAN DEFAULT FALSE,
    purity_percent DECIMAL(5,2),

    -- Storage
    storage_location VARCHAR(100),  -- e.g., "Glovebox Freezer A, Shelf 2"
    amount_mg DECIMAL(10,2),

    -- Descriptors (computational)
    hammett_sigma DECIMAL(5,3),  -- Sum of substituent σ values
    steric_parameter DECIMAL(7,2),  -- Buried volume %V_bur

    -- DFT properties (from calculations)
    homo_energy_ev DECIMAL(8,4),
    lumo_energy_ev DECIMAL(8,4),

    notes TEXT
);
```

#### Table: `catalysts`
```sql
CREATE TABLE catalysts (
    catalyst_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ligand_id UUID REFERENCES ligands(ligand_id),
    metal ENUM('Ni', 'Fe', 'Co', 'Cu', 'Mn', 'Pd', 'Pt') NOT NULL,
    oxidation_state INTEGER,

    -- Structure
    coordination_geometry ENUM('tetrahedral', 'square_planar', 'octahedral', 'trigonal_bipyramidal'),

    -- Synthesis (if pre-formed complex)
    synthesis_date DATE,
    characterization_complete BOOLEAN DEFAULT FALSE,
    xrd_structure_available BOOLEAN DEFAULT FALSE,
    cif_file_path VARCHAR(500),

    -- ML-predicted performance
    predicted_activity_score DECIMAL(5,3),  -- 0-1 scale
    predicted_selectivity_score DECIMAL(5,3),
    confidence_score DECIMAL(5,3),

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_catalysts_metal ON catalysts(metal);
CREATE INDEX idx_catalysts_ligand ON catalysts(ligand_id);
```

#### Table: `reactions`
```sql
CREATE TABLE reactions (
    reaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    experiment_id VARCHAR(100) UNIQUE NOT NULL,  -- Human-readable: "EZ-2024-001"

    -- Reaction type
    reaction_class ENUM('suzuki', 'negishi', 'heck', 'hydrogenation', 'ch_activation', 'other'),

    -- Catalyst
    catalyst_id UUID REFERENCES catalysts(catalyst_id),
    catalyst_loading_mol_percent DECIMAL(5,3),

    -- Substrates (can be multiple, but main substrate for Suzuki)
    substrate_1_id UUID REFERENCES compounds(compound_id),
    substrate_1_mmol DECIMAL(8,3),
    substrate_2_id UUID REFERENCES compounds(compound_id),
    substrate_2_mmol DECIMAL(8,3),

    -- Reagents
    base VARCHAR(100),  -- e.g., "K3PO4"
    base_mmol DECIMAL(8,3),
    additive VARCHAR(100),

    -- Conditions
    solvent VARCHAR(100),
    solvent_ml DECIMAL(6,2),
    temperature_celsius INTEGER,
    time_hours DECIMAL(6,2),
    atmosphere ENUM('air', 'N2', 'Ar'),

    -- Execution
    reaction_date DATE NOT NULL,
    experimenter VARCHAR(100),
    plate_well VARCHAR(10),  -- e.g., "A1" for 96-well plate

    -- Outcomes
    product_id UUID REFERENCES compounds(compound_id),
    conversion_percent DECIMAL(5,2),
    yield_percent DECIMAL(5,2),
    selectivity_percent DECIMAL(5,2),
    tof DECIMAL(10,2),  -- Turnover frequency (h^-1)

    -- Analysis
    uplc_ms_file_path VARCHAR(500),
    nmr_confirmed BOOLEAN DEFAULT FALSE,

    -- Quality flags
    qc_pass BOOLEAN,
    qc_notes TEXT,

    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    notes TEXT
);

CREATE INDEX idx_reactions_catalyst ON reactions(catalyst_id);
CREATE INDEX idx_reactions_date ON reactions(reaction_date);
CREATE INDEX idx_reactions_class ON reactions(reaction_class);
CREATE INDEX idx_reactions_yield ON reactions(yield_percent);
```

#### Table: `dft_calculations`
```sql
CREATE TABLE dft_calculations (
    calculation_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    -- System
    catalyst_id UUID REFERENCES catalysts(catalyst_id),
    calculation_type ENUM('optimization', 'frequency', 'transition_state', 'single_point'),

    -- Method
    functional VARCHAR(50) DEFAULT 'wB97X-D3',
    basis_set VARCHAR(100) DEFAULT 'def2-TZVP',
    solvent VARCHAR(50),
    program ENUM('Gaussian16', 'ORCA5', 'QChem') DEFAULT 'Gaussian16',

    -- Computational details
    num_cores INTEGER DEFAULT 16,
    memory_gb INTEGER DEFAULT 64,
    wall_time_hours DECIMAL(8,2),

    -- Results
    electronic_energy_hartree DECIMAL(20,12),
    gibbs_free_energy_hartree DECIMAL(20,12),
    enthalpy_hartree DECIMAL(20,12),
    entropy_cal_mol_k DECIMAL(10,4),

    -- Geometry
    optimized_structure TEXT,  -- XYZ format

    -- Transition state specific
    imaginary_frequency_cm DECIMAL(10,2),  -- Should be negative for TS

    -- File paths
    input_file_path VARCHAR(500),
    output_file_path VARCHAR(500),

    -- Status
    calculation_status ENUM('queued', 'running', 'completed', 'failed'),
    error_message TEXT,

    -- Metadata
    submitted_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP,
    submitted_by VARCHAR(100)
);

CREATE INDEX idx_dft_catalyst ON dft_calculations(catalyst_id);
CREATE INDEX idx_dft_status ON dft_calculations(calculation_status);
```

#### Table: `ml_predictions`
```sql
CREATE TABLE ml_predictions (
    prediction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    -- Input
    catalyst_id UUID REFERENCES catalysts(catalyst_id),
    substrate_id UUID REFERENCES compounds(compound_id),
    reaction_class VARCHAR(50),

    -- Conditions (for prediction)
    temperature_celsius INTEGER,
    solvent VARCHAR(100),

    -- Model
    model_name VARCHAR(100),  -- e.g., "RandomForest_v2.3"
    model_version VARCHAR(20),

    -- Predictions
    predicted_yield_percent DECIMAL(5,2),
    predicted_selectivity_percent DECIMAL(5,2),
    confidence_interval_lower DECIMAL(5,2),
    confidence_interval_upper DECIMAL(5,2),

    -- Feature importance (JSON)
    feature_importance JSON,

    -- Experimental validation (if tested)
    experimental_yield_percent DECIMAL(5,2),
    prediction_error DECIMAL(6,2),  -- Absolute error

    -- Metadata
    predicted_at TIMESTAMP DEFAULT NOW(),
    validated BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_ml_catalyst ON ml_predictions(catalyst_id);
CREATE INDEX idx_ml_model ON ml_predictions(model_name);
```

---

## 3. Data Processing Pipelines

### 3.1 Automated UPLC-MS Data Processing

**Workflow:**

```python
# File: pipelines/uplc_processing.py

import pymzml
import pandas as pd
import numpy as np
from rdkit import Chem
import psycopg2

def process_uplc_file(file_path, reaction_id):
    """
    Parse UPLC-MS .raw file, extract yield, update database

    Args:
        file_path: Path to Waters .raw file
        reaction_id: UUID of reaction in database

    Returns:
        dict with yield, purity, detected masses
    """

    # Convert .raw to mzML (using ProteoWizard msconvert)
    mzml_path = convert_raw_to_mzml(file_path)

    # Parse mzML
    run = pymzml.run.Reader(mzml_path)

    # Extract chromatogram
    retention_times = []
    intensities = []

    for spectrum in run:
        if spectrum.ms_level == 1:  # TIC (Total Ion Chromatogram)
            retention_times.append(spectrum.scan_time_in_minutes())
            intensities.append(spectrum.highest_peak_intensity)

    # Identify peaks (simple peak-picking)
    peaks = find_peaks(retention_times, intensities, prominence=1e5)

    # Get expected product mass from database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.exact_mass, r.substrate_1_mmol
        FROM reactions r
        JOIN compounds c ON r.product_id = c.compound_id
        WHERE r.reaction_id = %s
    """, (reaction_id,))

    expected_mass, substrate_mmol = cur.fetchone()

    # Find product peak (match m/z within 0.05 Da)
    product_peak = None
    for peak in peaks:
        # Get mass spectrum at this retention time
        spectrum = get_spectrum_at_rt(run, peak['rt'])
        masses = spectrum.mz

        if any(abs(m - expected_mass) < 0.05 for m in masses):
            product_peak = peak
            break

    if product_peak is None:
        yield_percent = 0
    else:
        # Quantify using calibration curve
        product_area = product_peak['area']
        yield_percent = calibration_curve(product_area, expected_mass)

    # Update database
    cur.execute("""
        UPDATE reactions
        SET yield_percent = %s,
            uplc_ms_file_path = %s,
            qc_pass = %s
        WHERE reaction_id = %s
    """, (yield_percent, file_path, yield_percent > 10, reaction_id))

    conn.commit()
    cur.close()
    conn.close()

    return {
        'yield': yield_percent,
        'product_rt': product_peak['rt'] if product_peak else None,
        'product_area': product_peak['area'] if product_peak else 0
    }

def calibration_curve(area, mass):
    """Convert peak area to yield using 5-point calibration"""
    # Calibration data (obtained from standards)
    # Format: {mass_range: (slope, intercept)}
    calibrations = {
        (100, 200): (0.0012, -5.0),  # yield = 0.0012 * area - 5
        (200, 300): (0.0010, -3.0),
        # ... more ranges
    }

    for (low, high), (slope, intercept) in calibrations.items():
        if low <= mass < high:
            yield_percent = slope * area + intercept
            return max(0, min(100, yield_percent))  # Clamp 0-100%

    # Default if mass not in calibration range
    return 0.0
```

**Automation:**
- **File Watcher:** Monitor UPLC-MS output directory (inotify on Linux)
- **Trigger:** New .raw file detected → run `process_uplc_file()`
- **Notification:** Slack message when batch complete (96-well plate)

### 3.2 DFT Workflow (Gaussian 16)

**Automated Job Submission (SLURM):**

```python
# File: pipelines/dft_submit.py

import os
import uuid
from jinja2 import Template
import subprocess

def submit_dft_calculation(catalyst_id, calc_type='optimization'):
    """
    Generate Gaussian input file, submit to cluster

    Args:
        catalyst_id: UUID of catalyst
        calc_type: 'optimization', 'frequency', 'transition_state'

    Returns:
        calculation_id (UUID)
    """

    # Fetch catalyst structure from database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.catalyst_id, l.mol_file, c.metal
        FROM catalysts c
        JOIN ligands l ON c.ligand_id = l.ligand_id
        WHERE c.catalyst_id = %s
    """, (catalyst_id,))

    catalyst_id, mol_file, metal = cur.fetchone()

    # Parse MOL file to XYZ coordinates
    mol = Chem.MolFromMolBlock(mol_file)
    xyz = mol_to_xyz(mol, include_metal=metal)

    # Generate Gaussian input from template
    template = Template("""
%nprocshared={{ num_cores }}
%mem={{ memory_gb }}GB
%chk={{ checkpoint_file }}
#p {{ method }}/{{ basis_set }} {{ calc_keywords }} scrf=(smd,solvent={{ solvent }})

{{ calc_type }} for catalyst {{ catalyst_id }}

{{ charge }} {{ multiplicity }}
{{ xyz_coords }}

    """)

    calculation_id = str(uuid.uuid4())
    checkpoint_file = f"/scratch/{calculation_id}.chk"

    input_content = template.render(
        num_cores=16,
        memory_gb=64,
        checkpoint_file=checkpoint_file,
        method='wB97XD',
        basis_set='def2TZVP',
        calc_keywords='opt' if calc_type == 'optimization' else 'opt=(ts,noeigentest) freq',
        solvent='THF',
        calc_type=calc_type,
        catalyst_id=catalyst_id,
        charge=0,  # Neutral complex
        multiplicity=1,  # Singlet (adjust for high-spin complexes)
        xyz_coords=xyz
    )

    # Write input file
    input_file = f"/home/zhang/dft_calculations/{calculation_id}.gjf"
    with open(input_file, 'w') as f:
        f.write(input_content)

    # Create SLURM submit script
    slurm_script = f"""#!/bin/bash
#SBATCH --job-name=dft_{calculation_id[:8]}
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=24:00:00
#SBATCH --output=/home/zhang/dft_calculations/{calculation_id}.log

module load gaussian/16_C.01

g16 {input_file}
"""

    slurm_file = f"/home/zhang/dft_calculations/{calculation_id}.sh"
    with open(slurm_file, 'w') as f:
        f.write(slurm_script)

    # Submit job
    result = subprocess.run(['sbatch', slurm_file], capture_output=True, text=True)
    job_id = result.stdout.split()[-1]  # Extract SLURM job ID

    # Insert into database
    cur.execute("""
        INSERT INTO dft_calculations (
            calculation_id, catalyst_id, calculation_type,
            functional, basis_set, solvent, program,
            num_cores, memory_gb, input_file_path,
            output_file_path, calculation_status, submitted_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
    """, (
        calculation_id, catalyst_id, calc_type,
        'wB97X-D3', 'def2-TZVP', 'THF', 'Gaussian16',
        16, 64, input_file,
        f"/home/zhang/dft_calculations/{calculation_id}.log",
        'queued'
    ))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Submitted calculation {calculation_id} (SLURM job {job_id})")
    return calculation_id
```

**Result Parsing:**

```python
# File: pipelines/dft_parse.py

import re

def parse_gaussian_output(calculation_id):
    """Extract energies, frequencies from Gaussian .log file"""

    conn = get_db_connection()
    cur = conn.cursor()

    # Get output file path
    cur.execute("""
        SELECT output_file_path FROM dft_calculations WHERE calculation_id = %s
    """, (calculation_id,))
    output_file = cur.fetchone()[0]

    with open(output_file, 'r') as f:
        content = f.read()

    # Check for normal termination
    if "Normal termination" not in content:
        cur.execute("""
            UPDATE dft_calculations
            SET calculation_status = 'failed',
                error_message = 'Gaussian did not terminate normally'
            WHERE calculation_id = %s
        """, (calculation_id,))
        conn.commit()
        return

    # Extract electronic energy
    match = re.search(r'SCF Done:.*?=\s+([-\d.]+)', content)
    electronic_energy = float(match.group(1)) if match else None

    # Extract Gibbs free energy
    match = re.search(r'Sum of electronic and thermal Free Energies=\s+([-\d.]+)', content)
    gibbs_energy = float(match.group(1)) if match else None

    # Extract frequencies (check for imaginary)
    frequencies = re.findall(r'Frequencies --\s+([\d.\s-]+)', content)
    all_freqs = []
    for freq_line in frequencies:
        all_freqs.extend([float(f) for f in freq_line.split()])

    imaginary_freq = min(all_freqs) if all_freqs else None

    # Extract optimized geometry
    match = re.search(r'Standard orientation:.*?\n(.*?)\n -+\n', content, re.DOTALL)
    if match:
        geom_lines = match.group(1).strip().split('\n')[4:]  # Skip header
        xyz_coords = extract_xyz_from_gaussian_geom(geom_lines)
    else:
        xyz_coords = None

    # Update database
    cur.execute("""
        UPDATE dft_calculations
        SET electronic_energy_hartree = %s,
            gibbs_free_energy_hartree = %s,
            imaginary_frequency_cm = %s,
            optimized_structure = %s,
            calculation_status = 'completed',
            completed_at = NOW()
        WHERE calculation_id = %s
    """, (electronic_energy, gibbs_energy, imaginary_freq, xyz_coords, calculation_id))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Parsed calculation {calculation_id}: ΔG = {gibbs_energy:.6f} Hartree")
```

### 3.3 Machine Learning Pipeline

**Training Workflow:**

```python
# File: ml/train_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

def train_yield_prediction_model():
    """Train Random Forest model to predict reaction yields"""

    # Load data from database
    conn = get_db_connection()

    query = """
        SELECT
            r.reaction_id,
            r.yield_percent,
            r.temperature_celsius,
            r.time_hours,
            r.catalyst_loading_mol_percent,
            -- Catalyst descriptors
            l.hammett_sigma,
            l.steric_parameter,
            l.homo_energy_ev,
            l.lumo_energy_ev,
            c.metal,
            -- Substrate descriptors (compute with RDKit)
            s.molecular_weight,
            s.smiles AS substrate_smiles,
            -- DFT descriptors
            dft.gibbs_free_energy_hartree AS activation_barrier
        FROM reactions r
        JOIN catalysts c ON r.catalyst_id = c.catalyst_id
        JOIN ligands l ON c.ligand_id = l.ligand_id
        JOIN compounds s ON r.substrate_1_id = s.compound_id
        LEFT JOIN dft_calculations dft ON c.catalyst_id = dft.catalyst_id
            AND dft.calculation_type = 'transition_state'
        WHERE r.qc_pass = TRUE
          AND r.yield_percent IS NOT NULL
    """

    df = pd.read_sql(query, conn)
    conn.close()

    print(f"Loaded {len(df)} reactions for training")

    # Compute additional substrate descriptors with RDKit
    from rdkit import Chem
    from rdkit.Chem import Descriptors, rdMolDescriptors

    df['substrate_logP'] = df['substrate_smiles'].apply(
        lambda s: Descriptors.MolLogP(Chem.MolFromSmiles(s))
    )
    df['substrate_TPSA'] = df['substrate_smiles'].apply(
        lambda s: Descriptors.TPSA(Chem.MolFromSmiles(s))
    )

    # One-hot encode metal
    df = pd.get_dummies(df, columns=['metal'], prefix='metal')

    # Define features (X) and target (y)
    feature_cols = [
        'temperature_celsius', 'time_hours', 'catalyst_loading_mol_percent',
        'hammett_sigma', 'steric_parameter', 'homo_energy_ev', 'lumo_energy_ev',
        'molecular_weight', 'substrate_logP', 'substrate_TPSA',
        'activation_barrier'
    ] + [col for col in df.columns if col.startswith('metal_')]

    X = df[feature_cols].fillna(0)  # Fill missing DFT values with 0 (or use imputation)
    y = df['yield_percent']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.15, random_state=42
    )

    # Train Random Forest
    model = RandomForestRegressor(
        n_estimators=500,
        max_depth=20,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    # Evaluate
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)
    test_mae = mean_absolute_error(y_test, y_pred_test)

    print(f"Train R²: {train_r2:.3f}")
    print(f"Test R²: {test_r2:.3f}")
    print(f"Test MAE: {test_mae:.1f}%")

    # Cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
    print(f"5-Fold CV R²: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': feature_cols,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)

    print("\nTop 10 Important Features:")
    print(feature_importance.head(10))

    # Save model
    model_version = "v2.3"
    joblib.dump(model, f"models/random_forest_{model_version}.pkl")
    joblib.dump(feature_cols, f"models/feature_cols_{model_version}.pkl")

    print(f"\nModel saved as random_forest_{model_version}.pkl")

    return model, feature_cols

if __name__ == "__main__":
    train_yield_prediction_model()
```

---

## 4. Web Application (Django + React)

### 4.1 Backend API (Django REST Framework)

```python
# File: api/views.py

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import Compound, Catalyst, Reaction
from .serializers import CompoundSerializer, CatalystSerializer, ReactionSerializer

class CatalystViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for catalysts

    list: GET /api/catalysts/
    retrieve: GET /api/catalysts/{id}/
    performance: GET /api/catalysts/{id}/performance/
    """

    queryset = Catalyst.objects.all()
    serializer_class = CatalystSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['metal', 'ligand__compound_name']
    ordering_fields = ['predicted_activity_score', 'created_at']

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        """Get aggregate performance statistics for a catalyst"""

        catalyst = self.get_object()

        # Aggregate reaction statistics
        reactions = Reaction.objects.filter(catalyst=catalyst, qc_pass=True)

        stats = reactions.aggregate(
            num_reactions=Count('reaction_id'),
            avg_yield=Avg('yield_percent'),
            avg_selectivity=Avg('selectivity_percent'),
            avg_tof=Avg('tof')
        )

        # Top substrates (by yield)
        top_substrates = reactions.order_by('-yield_percent')[:10].values(
            'substrate_1__smiles',
            'substrate_1__compound_name',
            'yield_percent',
            'selectivity_percent'
        )

        return Response({
            'catalyst_id': str(catalyst.catalyst_id),
            'metal': catalyst.metal,
            'ligand_name': catalyst.ligand.compound_name,
            'statistics': stats,
            'top_substrates': list(top_substrates)
        })

class ReactionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for reactions

    list: GET /api/reactions/?catalyst__metal=Ni&yield_percent__gte=80
    retrieve: GET /api/reactions/{id}/
    """

    queryset = Reaction.objects.filter(qc_pass=True)
    serializer_class = ReactionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'catalyst__metal': ['exact'],
        'reaction_class': ['exact'],
        'yield_percent': ['gte', 'lte'],
        'temperature_celsius': ['gte', 'lte'],
        'reaction_date': ['gte', 'lte']
    }
    ordering_fields = ['yield_percent', 'tof', 'reaction_date']
```

### 4.2 Frontend Dashboard (React)

```javascript
// File: frontend/src/components/CatalystPerformancePlot.jsx

import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';

function CatalystPerformancePlot() {
    const [data, setData] = useState([]);
    const [metal, setMetal] = useState('Ni');

    useEffect(() => {
        fetchData();
    }, [metal]);

    const fetchData = async () => {
        const response = await axios.get('/api/reactions/', {
            params: {
                catalyst__metal: metal,
                qc_pass: true
            }
        });

        setData(response.data.results);
    };

    // Prepare scatter plot data
    const plotData = [{
        x: data.map(r => r.temperature_celsius),
        y: data.map(r => r.yield_percent),
        mode: 'markers',
        type: 'scatter',
        marker: {
            size: data.map(r => r.catalyst_loading_mol_percent * 5),
            color: data.map(r => r.selectivity_percent),
            colorscale: 'Viridis',
            colorbar: { title: 'Selectivity (%)' },
            showscale: true
        },
        text: data.map(r => `Substrate: ${r.substrate_1.compound_name}<br>Yield: ${r.yield_percent}%`),
        hoverinfo: 'text'
    }];

    return (
        <div>
            <h2>Catalyst Performance: {metal}-based catalysts</h2>

            <select value={metal} onChange={(e) => setMetal(e.target.value)}>
                <option value="Ni">Nickel</option>
                <option value="Fe">Iron</option>
                <option value="Co">Cobalt</option>
                <option value="Cu">Copper</option>
                <option value="Pd">Palladium (benchmark)</option>
            </select>

            <Plot
                data={plotData}
                layout={{
                    xaxis: { title: 'Temperature (°C)' },
                    yaxis: { title: 'Yield (%)' },
                    width: 800,
                    height: 600,
                    hovermode: 'closest'
                }}
            />

            <p>Marker size = catalyst loading (mol%)</p>
            <p>Color = selectivity (%)</p>
        </div>
    );
}

export default CatalystPerformancePlot;
```

---

## 5. Deployment & Infrastructure

### 5.1 Containerization (Docker)

```dockerfile
# File: Dockerfile (Django backend)

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations and start server
CMD ["gunicorn", "greencat.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
```

**Docker Compose:**

```yaml
# File: docker-compose.yml

version: '3.8'

services:
  db:
    image: postgres:14
    environment:
      POSTGRES_DB: greencat
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    command: gunicorn greencat.wsgi:application --bind 0.0.0.0:8000
    environment:
      DATABASE_URL: postgres://${DB_USER}:${DB_PASSWORD}@db:5432/greencat
      SECRET_KEY: ${DJANGO_SECRET_KEY}
    volumes:
      - ./backend:/app
      - static_files:/app/staticfiles
    ports:
      - "8000:8000"
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  nginx:
    image: nginx:alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_files:/usr/share/nginx/html/static
    ports:
      - "80:80"
    depends_on:
      - backend
      - frontend

volumes:
  postgres_data:
  static_files:
```

### 5.2 Monitoring (Prometheus + Grafana)

**Metrics to Track:**
- API response time (p50, p95, p99)
- Database query latency
- Number of DFT calculations (queued, running, completed)
- ML model prediction throughput
- Disk usage (S3 bucket size)

---

## 6. Security & Compliance

### 6.1 Data Access Control

**User Roles:**
- **Admin:** Full access (PI, Co-PI)
- **Researcher:** Read/write reactions, catalysts (postdocs, PhD students)
- **Viewer:** Read-only (collaborators, public after publication)

**Implementation (Django):**
```python
from rest_framework import permissions

class IsResearcherOrReadOnly(permissions.BasePermission):
    """
    Custom permission: read-only for everyone, write for researchers
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Researcher').exists()
```

---

**Document Prepared By:** Dr. Michael Chen & Dr. Sofia Patel
**Last Updated:** December 27, 2025
**Version:** 1.9

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Research Plan - Chemistry]** `chemistry-research-plan-example.md`
  - Type: `requires` | Status: `approved` | Condition: `when domain === 'chemistry'`
- **[Executive Summary - Chemistry]** `chemistry-executive-summary-example.md`
  - Type: `informs`
- **[Data Model Schema]** `schemas/chemistry_screening_schema.json`
  - Type: `requires` | Evidence ID: `E-CHEM-TDD-001`

### Impacts (Downstream Documents)
- **[Implementation Tasks]** `jira/CHEM-TDD-IMPLEMENTATION-EPIC`
  - Type: `blocks` | Until: `this.status == approved` | Cascade: `true`
- **[Runbook]** `docs/ops/chemistry_platform_runbook.md`
  - Type: `informs`
- **[Test Plan]** `docs/testing/chemistry_system_test_plan.md`
  - Type: `informs`

### Related Documents
- **[Biology TDD]** `biology-tdd-example.md` - Relationship: `parallel-example`
- **[Physics TDD]** `physics-tdd-example.md` - Relationship: `parallel-example`
- **[Psychology TDD]** `psychology-tdd-example.md` - Relationship: `parallel-example`

### Satellite Documents
- **[TODO]** `satellites/TODO-TDD-CHEM-001.md` - Status: `completed`
- **[DOR]** `satellites/DOR-TDD-CHEM-001.md` - Status: `met`
- **[DOD]** `satellites/DOD-TDD-CHEM-001.md` - Status: `met`
- **[ADR Collection]** `satellites/ADR-TDD-CHEM-*.md` - Key decisions on database, cloud provider, retention

### Conditional Cross-References
```yaml
conditions:
  - when: domain === 'chemistry'
    require_dependencies: [Chemical Safety data handling, MSDS database integration]
    require_satellites: [ADR for molecular structure storage]
  - when: high_throughput === true
    require_dependencies: [Robotic system API integration, Real-time data collection]
  - when: infrastructure === 'cloud'
    require_dependencies: [Cloud cost estimates, Disaster recovery plan]
```

### Validation Rules
**BLOCKER:** All dependencies approved, System supports all screening assays, API documented, Security specified
**ERROR:** Database schema optimized, API rate limiting, Monitoring complete
**WARN:** API versioning, Caching layer, Cost optimization
