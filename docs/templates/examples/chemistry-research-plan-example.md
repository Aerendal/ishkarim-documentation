# Research Plan: GreenCat Project
## Detailed Experimental Design and Computational Methodology

**Project ID:** NSF-CHE-2024-8945
**PI:** Dr. Emily Zhang
**Co-PI:** Dr. Michael Chen
**Version:** 2.8
**Date:** December 27, 2025

---

## Research Questions

### Primary Research Questions

**RQ1:** Can rational ligand design enable earth-abundant metal catalysts (Fe, Co, Ni, Cu, Mn) to achieve catalytic performance (activity, selectivity, scope) comparable to precious metal catalysts (Pd, Pt, Rh, Ir) in cross-coupling and hydrogenation reactions?

**RQ2:** What are the structure-activity relationships between ligand electronic/steric properties and catalytic performance for earth-abundant metals?

**RQ3:** Can machine learning models trained on computational and experimental data predict catalyst performance with sufficient accuracy (<1 kcal/mol barrier prediction error) to guide synthesis prioritization?

**RQ4:** What are the mechanistic pathways for earth-abundant metal catalysts, and how do they differ from precious metal analogues?

### Secondary Research Questions

**RQ5:** Can continuous flow chemistry enable scalable (kilogram), economically viable synthesis using earth-abundant metal catalysts?

**RQ6:** What is the techno-economic and environmental life-cycle impact of replacing precious metal catalysts with earth-abundant alternatives in industrial processes?

---

## Hypotheses

### Central Hypothesis

**H0 (Null):** Earth-abundant metals have intrinsic limitations (electronic structure, redox potentials) that prevent them from achieving precious metal-level catalytic performance, regardless of ligand design.

**H1 (Alternative):** Appropriately designed ligands can modulate earth-abundant metal electronic structures and stabilize key catalytic intermediates, enabling performance parity with precious metals.

### Mechanistic Hypotheses

**H2:** Redox-active ligands (NNN-pincer architecture) facilitate challenging oxidative addition steps for Ni/Cu by serving as electron reservoirs, lowering activation barriers.

**H3:** Steric bulk around the metal center controls selectivity by disfavoring β-hydride elimination (common decomposition pathway) while permitting productive reductive elimination.

**H4:** Earth-abundant metal catalysts operate via single-electron transfer (SET) mechanisms (Ni(I)/Ni(III) cycles) rather than traditional two-electron pathways (Pd(0)/Pd(II)), requiring different ligand design principles.

**H5:** Machine learning models can identify non-obvious correlations between ligand descriptors (Sterimol parameters, buried volume, Hammett constants) and reaction outcomes, accelerating optimization beyond human intuition.

### Testable Predictions

- **P1:** Ni-NNN pincer catalysts will achieve TOF >1,000 h⁻¹ for Suzuki coupling (vs. Pd: 5,000 h⁻¹) - within 5× of precious metal
- **P2:** Ligand electronic parameter (Hammett σ) will correlate with reaction rate (ρ >2.0, indicating charge buildup in transition state)
- **P3:** DFT-calculated oxidative addition barrier will correlate with experimental TOF (R² >0.8)
- **P4:** Fe-based hydrogenation catalysts will achieve >95% enantioselectivity for chiral amine synthesis (matching Rh-BINAP)

---

## Methodology

### Aim 1: Computational Catalyst Design

#### 1.1 Density Functional Theory (DFT) Calculations

**Software:**
- **Gaussian 16** (Revision C.01) - For small molecule calculations, geometry optimizations
- **ORCA 5.0** - For large systems, multi-reference calculations
- **Software License:** MIT site license (unlimited cores)

**Computational Resources:**
- **MIT SuperCloud:** 512-core partition, 2 TB RAM aggregate
- **AWS EC2:** c5.24xlarge instances (96 vCPU) for on-demand scaling
- **Allocation:** 500,000 CPU-hours/year (Year 1), 1M CPU-hours/year (Years 2-4)

**Functional & Basis Set Selection:**
- **Functional:** ωB97X-D3 (range-separated hybrid with dispersion correction)
  - Rationale: Accurately models transition metal complexes, non-covalent interactions critical for substrate binding
  - Validation: Benchmarked against CCSD(T) for Pd/Ni model systems (MAE <2 kcal/mol)
- **Basis Set:**
  - Def2-TZVP for metal centers (Ni, Fe, Co, Cu, Mn)
  - Def2-SVP for ligand atoms (C, N, O, H)
  - Rationale: Balance between accuracy and computational cost
- **Solvation:** SMD implicit solvent model (THF, toluene, DMF - common reaction solvents)

**Workflow:**

1. **Ligand Library Design (In Silico):**
   - **Starting Point:** NNN-pincer scaffold (bis(imino)pyridine framework)
   - **Variations:** Systematically vary substituents on pyridine (R₁) and imine (R₂, R₃)
     - Electron-donating: -OMe, -NMe₂, -tBu
     - Electron-withdrawing: -CF₃, -NO₂, -CN
     - Sterically bulky: -iPr, -tBu, -Mes (mesityl)
   - **Total combinations:** 5 R₁ × 5 R₂ × 5 R₃ = 125 ligands (computationally screen)

2. **Metal-Ligand Complex Geometry Optimization:**
   ```
   Input: Ligand structure + metal (Ni²⁺, Fe²⁺, Co²⁺, Cu¹⁺, Mn²⁺)
   Output: Optimized ground state geometry

   Gaussian 16 input file:
   %nprocshared=16
   %mem=64GB
   #p opt freq wb97xd/def2svp empiricaldispersion=gd3 scrf=(smd,solvent=thf)

   Ni(II)-NNN complex optimization

   0 1  (charge, multiplicity)
   Ni  0.000  0.000  0.000
   N   1.950  0.000  0.000
   ...
   ```

3. **Reaction Pathway Calculation (Suzuki Coupling Example):**
   - **Step 1:** Oxidative addition (Ar-Br + Ni(0)-L → Ar-Ni(II)-Br-L)
   - **Step 2:** Transmetalation (Ar-Ni(II)-Br-L + Ar'-B(OH)₂ → Ar-Ni(II)-Ar'-L)
   - **Step 3:** Reductive elimination (Ar-Ni(II)-Ar'-L → Ar-Ar' + Ni(0)-L)

   **For each step:**
   - Locate transition state (TS) using QST3 or nudged elastic band (NEB)
   - Verify TS (single imaginary frequency, IRC confirms reactant/product connection)
   - Calculate free energy barrier: ΔG‡ = G(TS) - G(reactant)

4. **Descriptor Calculation:**
   - **Electronic:** NBO charges on metal, HOMO/LUMO energies, Mayer bond orders
   - **Steric:** Buried volume (%V_bur, calculated with SambVca 2.1), Sterimol parameters
   - **Kinetic:** ΔG‡ for rate-determining step (typically oxidative addition)

**Output:**
- Database of 125 ligands × 5 metals = 625 catalyst candidates
- For each: Optimized geometry, ΔG‡ values, molecular descriptors
- Ranked priority list (top 50 with lowest ΔG‡ < 25 kcal/mol)

**Validation:**
- Compare DFT predictions to known Pd/Ni systems (10 literature benchmarks)
- Target accuracy: ΔG‡ within ±2 kcal/mol of experimental activation energy

#### 1.2 Machine Learning Models

**Objective:** Predict reaction outcomes (yield, TOF, selectivity) from catalyst/substrate descriptors

**Data Sources:**

1. **Literature Mining:**
   - Reaxys database: Extract 10,000+ Pd/Ni cross-coupling reactions
   - Fields: Catalyst structure, substrate SMILES, conditions (T, solvent), yield
   - Automated extraction: Python script with Reaxys API

2. **Internal Experimental Data:**
   - High-throughput screening results (generated in Aim 2)
   - 1,000-5,000 reactions (50 catalysts × 20-100 substrates)

**Feature Engineering:**

*Catalyst Descriptors (100+ features):*
- DFT-derived: ΔG‡, HOMO-LUMO gap, NBO charges
- Ligand: Hammett σ, Tolman cone angle, %V_bur
- Metal: Electronegativity, ionic radius, d-electron count

*Substrate Descriptors (200+ features):*
- Molecular: MW, logP, # rotatable bonds
- Electronic: Hammett σ for substituents, pKa
- Topological: Morgan fingerprints (2048-bit), 3D shape descriptors

*Reaction Conditions (50+ features):*
- Temperature, solvent (one-hot encoded), base (pKa), catalyst loading

**Model Architecture:**

**Random Forest Regressor** (scikit-learn 1.3)
- Rationale: Handles non-linear relationships, robust to overfitting, interpretable
- Hyperparameters:
  - n_estimators: 500 trees
  - max_depth: 20
  - min_samples_split: 5
- Feature importance: Identify key descriptors driving performance

**Gradient Boosting (XGBoost 1.7):**
- Alternative model for comparison
- Often achieves higher accuracy than Random Forest

**Neural Network (Keras/TensorFlow 2.12):**
- Architecture: 3 hidden layers (512-256-128 neurons), ReLU activation, dropout (0.3)
- For complex, high-dimensional descriptor space

**Training/Validation:**
- **Split:** 70% train, 15% validation, 15% test (stratified by yield bins)
- **Cross-validation:** 5-fold CV on training set
- **Metrics:**
  - Regression: R² (target >0.7), MAE (mean absolute error <10% yield)
  - Classification (yield >80% = success): ROC-AUC >0.85

**Active Learning Loop:**
1. Train initial model on literature data
2. Predict outcomes for untested catalyst-substrate pairs
3. Select high-uncertainty predictions for experimental testing (balances exploration/exploitation)
4. Update model with new experimental data
5. Iterate (3-5 cycles over project duration)

**Output:**
- Trained ML model (saved as .pkl file for reproducibility)
- Feature importance rankings (which descriptors matter most?)
- Predictions for 50 catalyst candidates → prioritize top 25 for synthesis

---

### Aim 2: High-Throughput Synthesis and Screening

#### 2.1 Ligand Synthesis

**Target:** Synthesize 50 ligands (prioritized from Aim 1)

**Synthetic Route (NNN-Pincer Ligand Example):**

```
Step 1: Imine Formation
  2,6-Diacetylpyridine + 2 R-aniline → NNN-ligand
  Conditions: EtOH, AcOH (cat.), reflux 12h
  Yield: 70-90% (typical)

Step 2: Purification
  Recrystallization from EtOH or column chromatography (SiO₂, EtOAc/hexanes)
```

**Automated Synthesis (Chemspeed SWING XL):**
- **Platform:** Robotic synthesizer with 16 reaction vessels (10-50 mL)
- **Capability:** Liquid handling, heating/cooling (-15°C to 150°C), inert atmosphere, filtration
- **Throughput:** 16 ligands/day (if 1-step synthesis); ~3 weeks for 50 ligands
- **Advantages:** Parallel synthesis, reproducibility, reduced manual labor

**Characterization:**
- **¹H NMR:** Confirm structure (Bruker 500 MHz, CDCl₃)
  - Expected: Characteristic imine CH=N singlet at δ ~8.5 ppm
- **¹³C NMR:** Verify all carbons accounted for
- **HRMS (ESI):** Confirm molecular formula ([M+H]⁺ within 5 ppm)
- **Purity:** >95% (assessed by NMR integration, GC-MS)

**Storage:**
- N₂-filled glovebox, -20°C freezer
- Weighed aliquots (100 mg) for screening

#### 2.2 Catalyst Complex Preparation

**In Situ Generation (Preferred for Screening):**
- Mix ligand (L) + metal precursor (e.g., NiCl₂·6H₂O) in situ during reaction setup
- Ratio: L:Ni = 1.1:1 (slight excess ligand ensures saturation)
- Activation: Reduce Ni(II) to Ni(0) with Zn powder or use Ni(COD)₂ (pre-reduced)

**Pre-Formed Complex (For Mechanistic Studies):**
- **Synthesis:**
  ```
  NiCl₂·DME + NNN-ligand → [Ni(NNN)Cl₂]
  THF, RT, 2h
  Precipitate with pentane, filter
  Yield: 60-80%
  ```
- **Characterization:**
  - X-ray crystallography: Confirm coordination geometry (expect square planar Ni(II))
  - UV-Vis: Metal-to-ligand charge transfer (MLCT) bands
  - Elemental analysis (C, H, N): Within ±0.4% of calculated

#### 2.3 High-Throughput Catalytic Screening

**Reaction Setup (96-Well Plate Format):**

**Example Reaction: Suzuki Coupling**
```
ArBr + Ar'B(OH)₂ → Ar-Ar' (biaryl product)
Catalyst: Ni(NNN), 1-5 mol%
Base: K₃PO₄ (2 equiv)
Solvent: THF/H₂O (10:1)
Temperature: 60-80°C
Time: 2-24h
```

**Automated Workflow:**

1. **Stock Solution Preparation:**
   - Catalyst: 10 mM in THF (prepared in glovebox)
   - Substrate: 1 M in THF
   - Base: 2 M K₃PO₄ in H₂O

2. **Liquid Handler (Chemspeed or Tecan):**
   - Dispense catalyst (100 µL, 1 µmol) into each well
   - Add aryl bromide (100 µL, 100 µmol)
   - Add boronic acid (110 µL, 110 µmol, 1.1 equiv)
   - Add base (100 µL, 200 µmol, 2 equiv)
   - Final volume: 1 mL per well

3. **Reaction Execution:**
   - Seal plate with aluminum foil or septum mat (prevent evaporation)
   - Heat on 96-well heating block (80°C, 12h)
   - Quench: Cool to RT, add 100 µL MeOH

4. **Online Analysis (GC-MS or UPLC-MS):**
   - Autodilute: Robot transfers 10 µL reaction mixture + 90 µL MeCN to UPLC vial
   - UPLC-MS (Waters Acquity):
     - Column: C18 (2.1 × 50 mm, 1.7 µm)
     - Gradient: 5-95% MeCN in H₂O (0.1% formic acid), 3 min
     - Detection: UV (254 nm) + MS (ESI+, detect [M+H]⁺ for product)
   - Quantification: Calibration curve (5-point, 1-100 µM product)

**Screening Matrix:**
- **Variables:**
  - Catalyst: 50 different Ni-NNN complexes
  - Substrate: 20 aryl bromides (vary electronics, sterics)
    - Electron-rich: 4-MeO-C₆H₄Br
    - Electron-poor: 4-CF₃-C₆H₄Br
    - Sterically hindered: 2,6-dimethyl-C₆H₃Br
  - Temperature: 60°C, 80°C, 100°C (subset)

- **Total Reactions:** 50 catalysts × 20 substrates = 1,000 reactions (first round)

**Success Criteria (Hit Identification):**
- Yield >80%
- Selectivity >95% (biaryl product, minimal homocoupling Ar-Ar)
- TOF >500 h⁻¹ (calculated from time-course data)

**Expected Hit Rate:** 5-10% (50-100 hits advance to optimization)

#### 2.4 Optimization (Hit-to-Lead)

**For Top 5 Catalysts:**

**Condition Optimization:**
- **Design of Experiments (DoE):** Full factorial design
  - Variables: Temperature (60-100°C, 3 levels), Catalyst loading (0.5-5 mol%, 3 levels), Solvent (THF, dioxane, DMF, 3 levels)
  - Runs: 3³ = 27 experiments per catalyst
- **Response Surface Methodology:** Model yield as f(T, loading, solvent) → identify optimum

**Substrate Scope:**
- Test 30-50 diverse substrates (pharma-relevant: heteroaryls, ortho-substituted, etc.)
- Include challenging examples:
  - Ar-Cl (less reactive than Ar-Br)
  - Heteroaryl bromides (pyridine, thiophene)
  - Sterically hindered (2,6-disubstituted)

**Functional Group Tolerance:**
- Substrates with: -OH, -NH₂, -CO₂H, -CN, -NO₂ (test for side reactions)

**Kinetic Analysis:**
- Time-course: Sample reaction at 0.5, 1, 2, 4, 8, 12, 24h
- Plot [product] vs. time → determine TOF (initial rate)
- Determine reaction order (vary [substrate], [catalyst])

**Benchmark Comparison:**
- Run identical substrate scope with Pd(PPh₃)₄ (standard Suzuki catalyst)
- Direct comparison: Ni-NNN vs. Pd performance

---

### Aim 3: Mechanistic Studies

#### 3.1 Spectroscopic Characterization of Intermediates

**NMR Spectroscopy:**

**In Situ ¹H NMR Monitoring:**
- **Setup:** Mix Ni(NNN) catalyst + ArBr in J-Young NMR tube (sealed, inert)
- **Instrument:** Bruker 500 MHz, variable temperature (25-80°C)
- **Time-resolved:** Acquire spectra every 5 min (30 scans each)
- **Goal:** Observe oxidative addition intermediate [Ni(NNN)(Ar)(Br)]

**Low-Temperature NMR:**
- Cool to -40°C (slow down reactions)
- Capture transient intermediates (short-lived at RT)

**¹⁹F NMR (if substrate has -CF₃):**
- Track substrate consumption, product formation, detect Ni-aryl intermediate

**UV-Vis Spectroscopy:**
- Monitor MLCT bands (indicate Ni oxidation state changes)
- Ni(0): λmax ~350 nm
- Ni(II): λmax ~450 nm
- Stopped-flow UV-Vis: Millisecond time resolution for fast steps

**X-ray Absorption Spectroscopy (XAS):**
- **XANES (X-ray Absorption Near Edge Structure):** Ni oxidation state
- **EXAFS (Extended X-ray Absorption Fine Structure):** Ni coordination number, bond lengths
- **Beamline:** Stanford Synchrotron Radiation Lightsource (SSRL) - beamline 9-3
- **Experiment:** In situ XAS cell (follow catalyst under reaction conditions)

#### 3.2 Kinetic Studies

**Initial Rate Kinetics:**
- Vary [ArBr]: 0.05, 0.1, 0.2, 0.4 M (constant [catalyst], [boronic acid], [base])
- Plot rate vs. [ArBr] → determine order in substrate
- Repeat for [catalyst], [boronic acid]

**Hammett Study:**
- Substrate series: 4-OMe, 4-Me, 4-H, 4-Cl, 4-CF₃, 4-NO₂ (aryl bromides)
- Measure relative rates: k_X / k_H
- Plot log(k_X/k_H) vs. σ (Hammett constant) → ρ (reaction constant)
- Interpretation:
  - ρ > 0: Positive charge builds up in TS (favored by electron-donating groups)
  - ρ < 0: Negative charge in TS

**Kinetic Isotope Effect (KIE):**
- Compare k_H vs. k_D (deuterated substrate)
- C-H activation: Expect primary KIE ~2-7
- No C-H breaking: KIE ~1

**Eyring Analysis:**
- Measure rate at 5 temperatures (40-100°C)
- Plot ln(k/T) vs. 1/T → extract ΔH‡, ΔS‡
- Compare to DFT-calculated values

#### 3.3 Computational Validation

**DFT Refinement:**
- Use experimental intermediate structures (from XRD) as starting points
- Recalculate barriers with higher-level methods (DLPNO-CCSD(T) single-point energies)
- Compare calculated ΔG‡ to experimental E_a (Eyring analysis)
- Validation target: Agreement within ±1 kcal/mol

**Mechanistic Pathway Elucidation:**
- Test alternative mechanisms (SET vs. two-electron, inner-sphere vs. outer-sphere)
- Calculate rate constants for each pathway (transition state theory)
- Compare to experimental kinetics → rule out inconsistent mechanisms

---

### Aim 4: Scale-Up and Process Development

#### 4.1 Batch Scale-Up (100g)

**Reaction:** Suzuki coupling (optimized conditions from Aim 2)

**Procedure:**
```
Reagents:
- Aryl bromide: 100 g (e.g., 4-bromobenzonitrile, 550 mmol)
- Boronic acid: 1.1 equiv (82 g, 605 mmol)
- Ni-NNN catalyst: 1 mol% (5.5 mmol, ~2g complex)
- Base: K₃PO₄, 2 equiv (233 g, 1.1 mol)
- Solvent: THF (1 L) + H₂O (100 mL)

Equipment:
- 2L round-bottom flask
- Reflux condenser
- Mechanical stirrer (overhead)
- Heating mantle
- N₂ inlet (maintain inert atmosphere)

Protocol:
1. Charge flask with aryl bromide, boronic acid, base
2. Add THF/H₂O, stir to dissolve
3. Add catalyst (as solution in 50 mL THF)
4. Heat to 80°C, stir 12h
5. Cool, filter through Celite (remove inorganic salts)
6. Concentrate on rotovap
7. Purify: Column chromatography or recrystallization
8. Isolate product: 85-95% yield (90-100g)
```

**Quality Control:**
- **Purity:** NMR, HPLC (target >98%)
- **Metal Contamination:** ICP-MS (Ni content <10 ppm, meets pharma standards)
- **Impurity Profiling:** GC-MS (identify/quantify side products)

#### 4.2 Continuous Flow Chemistry

**Rationale:** Flow chemistry offers better heat/mass transfer, safer handling, easier scale-up

**Flow Reactor (Vapourtec R-Series):**
- **Design:** Tubular reactor (PFA tubing, 10 mL volume), heated jacket
- **Flow rate:** 1-10 mL/min
- **Residence time:** 1-10 min (faster than batch!)

**Flow Setup:**
```
Pump A: ArBr + Boronic acid in THF (0.5 M each)
Pump B: Ni-NNN catalyst in THF (5 mM)
Pump C: K₃PO₄ in H₂O (2 M)

→ T-mixer (combine A+B+C) → Heated reactor (80°C, 10 mL) → Back-pressure regulator → Collection

Flow rate: 5 mL/min → 10 min residence time
Throughput: 5 mL/min × 0.5 M × 60 min/h = 150 mmol/h = 20 g/h product
```

**Optimization:**
- Screen residence time (1-30 min)
- Optimize temperature (60-120°C, higher temps possible in flow due to pressure)
- Inline monitoring: UV-Vis (track conversion in real-time)

**Scale-Up:**
- Numbering-up: Run 10 reactors in parallel → 200 g/h
- Continuous operation: 24h run → 4.8 kg product (vs. batch: 100g every 24h)

**Economic Analysis:**
- Cost comparison: Batch vs. flow (capital, operating, labor)
- Ni catalyst cost: $20/kg product (vs. Pd: $5,000/kg product)
- Total cost of goods (COGS): Target <$100/kg for commodity chemicals

#### 4.3 Catalyst Recovery and Recycling

**Heterogeneous Catalyst Development:**
- Immobilize Ni-NNN on solid support (e.g., silica, polymer resin)
- Filter catalyst after reaction → reuse 5-10 times
- Monitor activity loss per cycle (target <10% after 5 cycles)

**Homogeneous Catalyst Recovery:**
- Ligand extraction: Aqueous wash with EDTA (chelate Ni, separate from product)
- Crystallization: Crash out Ni complex by adding anti-solvent
- Recycling rate: >80% Ni recovery

---

## Timeline

### Year 1 (Months 1-12)

**Q1 (M1-3):**
- Hire personnel (2 postdocs, 1 PhD student)
- Setup computational infrastructure (AWS accounts, software installation)
- Literature data mining (10,000+ reactions from Reaxys)

**Q2 (M4-6):**
- DFT calculations (125 ligands × 5 metals = 625 candidates)
- Benchmark DFT against experimental data
- **Milestone M1:** Computational screening complete

**Q3 (M7-9):**
- ML model training (literature data)
- Prioritize top 50 catalysts for synthesis
- Begin ligand synthesis (manual, 10 ligands)

**Q4 (M10-12):**
- Complete ligand synthesis (50 ligands via Chemspeed)
- Characterization (NMR, MS)
- **Milestone M2:** ML model trained

### Year 2 (Months 13-24)

**Q1 (M13-15):**
- High-throughput screening Round 1 (50 catalysts × 20 substrates)
- Data analysis (identify 5-10 hits)

**Q2 (M16-18):**
- Optimization (DoE for top 5 catalysts)
- Substrate scope expansion (30 substrates per catalyst)
- **Milestone M3:** Ligand library complete

**Q3 (M19-21):**
- Update ML model with experimental data (active learning)
- Design 2nd generation ligands (25 new designs)
- Synthesize + screen 2nd generation

**Q4 (M22-24):**
- Mechanistic studies (NMR, UV-Vis, kinetics)
- **Milestone M4:** High-throughput screening complete (Round 1)

### Year 3 (Months 25-36)

**Q1 (M25-27):**
- Crystal structure determination (XRD, 10 complexes)
- In situ XAS (Stanford SSRL beamtime)

**Q2 (M28-30):**
- DFT mechanistic studies (validate experimental intermediates)
- Hammett studies, KIE measurements
- **Milestone M5:** Top catalyst optimization complete

**Q3 (M31-33):**
- Batch scale-up (100g, 3 products)
- Flow chemistry development (Vapourtec)

**Q4 (M34-36):**
- Industrial collaboration (Merck pilot study)
- **Milestone M6:** Mechanistic studies complete

### Year 4 (Months 37-48)

**Q1 (M37-39):**
- Final validation (reproduce top 3 catalysts, robustness tests)
- Techno-economic analysis (COGS calculation)

**Q2 (M40-42):**
- Database development (web portal, https://greencat.mit.edu)
- **Milestone M7:** Pilot-scale demonstration complete

**Q3 (M43-45):**
- Manuscript writing (4 papers)
- Patent filing (top 3 catalyst systems)

**Q4 (M46-48):**
- Final data release, publication
- Workshop (Computational Catalyst Design, 50 attendees)
- **Milestone M8:** Database launch

---

## Ethical Considerations

### Chemical Safety

**Hazardous Materials:**
- Nickel salts: Carcinogenic (Category 1B), respiratory sensitizer
  - Handling: Fume hood, nitrile gloves, minimize dust generation
  - Disposal: Collect Ni waste, send to certified recycler (not landfill)

- Boronic acids: Some are skin/eye irritants
  - PPE: Safety glasses, gloves

- Solvents (THF, toluene): Flammable, toxic vapors
  - Storage: Solvent cabinet, grounded containers
  - Fire suppression: Class B extinguisher in lab

**Standard Operating Procedures (SOPs):**
- All procedures documented in ELN (Benchling)
- New personnel: Safety training (MIT EHS course) before lab work
- Annual refresher training

### Environmental Impact

**Green Chemistry Principles:**
- This project aligns with **Principle 7:** Use renewable feedstocks (earth-abundant metals vs. scarce precious metals)
- **Principle 9:** Catalysis (superior to stoichiometric reagents)
- **Waste Minimization:** High-throughput screening uses µmol-scale reactions (vs. traditional mmol-gram scale)

**Life Cycle Assessment (LCA):**
- Partner with Prof. Julie Zimmerman (Yale) - LCA expert
- Compare Ni vs. Pd catalysts: Cradle-to-gate CO₂ emissions, water use, toxicity
- Publish results in *Green Chemistry* or *ACS Sustainable Chem. Eng.*

### Data Sharing and Reproducibility

**Open Science Commitment:**
- All data (structures, conditions, yields) publicly released upon publication
- Code: GitHub (MIT License, permissive)
- Computational files: DFT inputs, ML training data → Zenodo

**FAIR Principles (Findable, Accessible, Interoperable, Reusable):**
- Metadata: CIF files (crystallography), NMR FIDs (raw data)
- Standard formats: SMILES (structures), CSV (results)

---

## Risk Mitigation

*(Repeat from Executive Summary, with additional experimental details)*

**Risk: Ligand synthesis fails (low yields, purification issues)**
- **Mitigation:**
  - Backup routes: Purchase commercial analogues if custom synthesis problematic
  - Contract synthesis: Outsource difficult ligands to CRO (e.g., Sigma-Aldrich custom synthesis)

**Risk: Catalyst decomposition during reaction**
- **Mitigation:**
  - Stabilize with additional ligands (phosphines, NHCs)
  - Lower temperature (sacrifice rate for stability)
  - Continuous flow (minimize catalyst lifetime required)

**Risk: Substrate scope limited (only works for activated aryl bromides)**
- **Mitigation:**
  - Diversify ligand library (include electron-rich and electron-poor variants)
  - Multi-catalyst toolbox approach (different catalysts for different substrates)
  - Publish negative results (document limitations transparently)

---

## Equipment & Facilities

### Major Equipment

**Synthesis:**
- **Chemspeed SWING XL:** $250k (shared with 2 other labs, contribution: $80k)
- **Glovebox (MBraun):** $60k (N₂ atmosphere, <1 ppm O₂/H₂O)
- **Flow reactor (Vapourtec R-Series):** $75k (rental option: $3k/month)

**Characterization:**
- **NMR (Bruker 500 MHz):** MIT DCIF core facility, $30/hour
- **UPLC-MS (Waters Acquity):** Shared, $25/hour
- **XRD (Bruker D8 Venture):** MIT X-ray facility, $50/sample
- **ICP-MS (Agilent 7900):** MIT CMSE, $60/sample

**Computation:**
- **MIT SuperCloud:** Free for MIT users (allocation-based)
- **AWS EC2:** Pay-as-you-go, ~$2/hour for c5.24xlarge

---

## Success Metrics

### Technical Metrics

✓ Synthesize 50 ligands, >90% success rate, >95% purity
✓ Identify ≥3 catalysts with TOF >1,000 h⁻¹
✓ Achieve >95% selectivity for ≥30 substrates
✓ ML model R² >0.7 for yield prediction
✓ Scale-up to 100g with >85% isolated yield

### Scientific Metrics

✓ Publish 4 papers in high-impact journals (cumulative IF >80)
✓ 500+ citations within 5 years
✓ Database: 1,000+ users, 10,000+ data points

### Translational Metrics

✓ 2 industrial partnerships (pilot studies)
✓ 2-3 patents filed
✓ Cost reduction: Ni catalyst <$50/kg product (vs. Pd >$5,000/kg)

---

**Prepared by:** Dr. Emily Zhang & Dr. Michael Chen
**Last Updated:** December 27, 2025
**Document Version:** 2.8

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Executive Summary - Chemistry]** `chemistry-executive-summary-example.md`
  - Type: `informs` | Condition: `when domain === 'chemistry'`
- **[Chemical Safety Approval]** `compliance/EHS_hazmat_approval.pdf`
  - Type: `requires` | Status: `approved`
- **[Literature Review]** `evidence/catalyst_literature_review_2024.md`
  - Type: `requires` | Evidence ID: `E-CHEM-002`

### Impacts (Downstream Documents)
- **[TDD - Chemistry]** `chemistry-tdd-example.md`
  - Type: `blocks` | Until: `this.status == approved` | Cascade: `true`
- **[Test Plan]** `docs/testing/chemistry_screening_test_plan.md`
  - Type: `informs`

### Related Documents
- **[Biology Research Plan]** `biology-research-plan-example.md` - Relationship: `parallel-example`
- **[Physics Research Plan]** `physics-research-plan-example.md` - Relationship: `parallel-example`
- **[Psychology Research Plan]** `psychology-research-plan-example.md` - Relationship: `parallel-example`

### Satellite Documents
- **[TODO]** `satellites/TODO-RESPLAN-CHEM-001.md` - Status: `completed`
- **[DOR]** `satellites/DOR-RESPLAN-CHEM-001.md` - Status: `met`
- **[DOD]** `satellites/DOD-RESPLAN-CHEM-001.md` - Status: `met`

### Conditional Cross-References
```yaml
conditions:
  - when: domain === 'chemistry'
    require_dependencies: [Chemical Safety Approval, MSDS for all reagents, Waste disposal plan]
    require_satellites: [Chemical Hazard Assessment, Lab Safety Protocols]
  - when: high_throughput_screening === true
    require_dependencies: [Equipment access (robotic synthesizer), Data management infrastructure]
  - when: computational_design === true
    require_dependencies: [HPC allocation, Software licenses (Gaussian, ORCA)]
```

### Validation Rules
**BLOCKER:** All dependencies approved, Chemical Safety current, Synthetic routes feasible
**ERROR:** Computational resources adequate, Timeline realistic for synthesis cycles
**WARN:** IP strategy documented, Scale-up considerations addressed
