# Research Plan: QuantMat Project
## Detailed Experimental Protocols and Theoretical Framework

**Project ID:** NSF-DMR-2024-9112
**PI:** Dr. David Park | **Co-PI:** Dr. Lisa Nakamura
**Version:** 3.1 | **Date:** December 27, 2025

---

## Research Questions

**RQ1:** Can strain-engineered Fe(Se,Te)/SrTiO₃ heterostructures host topologically-protected Majorana zero modes with coherence times >1 ms?

**RQ2:** What is the relationship between film quality (defect density, interface roughness) and Majorana mode localization length?

**RQ3:** Can voltage-controlled domain walls enable non-Abelian braiding operations with gate fidelity >99%?

**RQ4:** How do environmental decoherence mechanisms (phonons, charge fluctuations) limit topological qubit performance?

---

## Hypotheses

**H1:** Fe(Se,Te) films grown on SrTiO₃ with <1% defect density will exhibit quantized thermal Hall conductance κ_xy = (π²/3)(k_B²T/h), confirming topological superconductivity.

**H2:** Majorana zero modes will manifest as zero-bias conductance peaks with width Γ <50 µeV, robust to magnetic fields 0-5 Tesla.

**H3:** Braiding two Majorana modes via domain wall manipulation will produce conductance oscillations G(θ) = G₀[1 + cos(θ)] where θ is braiding angle.

**H4:** Topological protection will yield T₂ coherence times >100× longer than conventional transmon qubits (1 ms vs. 100 µs).

---

## Methodology

### Aim 1: MBE Growth of Topological Superconductors

#### 1.1 Molecular Beam Epitaxy (MBE) System

**Equipment:** Custom UHV-MBE chamber (base pressure <5×10⁻¹¹ Torr)

**Components:**
- **Effusion Cells:** Fe (1500°C max), Se (400°C), Te (450°C)
- **Substrate Heater:** Radiative, RT-900°C, ±1°C stability
- **RHEED:** 15 keV electron gun, CCD camera (real-time diffraction monitoring)
- **Flux Monitors:** Beam flux monitors (BFM) + quartz crystal microbalance

**Growth Protocol:**

1. **Substrate Preparation:**
   - SrTiO₃ (001) substrates (CrysTec GmbH, 10×10mm, epi-polished)
   - Ex situ: Sonicate in acetone/IPA, dry N₂
   - In situ: Heat to 600°C for 2h (desorb adsorbates), verify TiO₂-terminated surface (RHEED streaks)

2. **Buffer Layer:** Deposit 5nm Fe seed layer at 200°C (improves wetting)

3. **Fe(Se,Te) Growth:**
   - **Temperature:** T_substrate = 320-380°C (optimize via AI model)
   - **Flux Rates:**
     - Fe: 0.5 Å/s (measured by BFM)
     - Se:Te ratio = 0.5:0.5 (co-deposition)
     - Total chalcogen flux: 2:1 excess over Fe (ensures stoichiometry)
   - **Thickness:** 10-100 nm (varies by device application)
   - **Growth Rate:** 0.2 Å/s (verified by RHEED oscillations)
   - **RHEED Monitoring:** Streaky pattern indicates 2D growth; spotty = 3D islands (undesirable)

4. **Se Capping:** 2nm amorphous Se layer (prevent oxidation during transfer)

**Quality Metrics:**
- RHEED: Streaky pattern throughout growth
- XRD: (001) peak FWHM <0.1° (low mosaicity)
- AFM: RMS roughness <0.5 nm over 1×1 µm²
- Transport: Superconducting T_c >10 K, residual resistivity ratio RRR >10

#### 1.2 AI-Optimized Growth (Reinforcement Learning)

**Approach:** Bayesian optimization + RL agent

**State Space:**
- RHEED intensity (32×32 pixel region), substrate temperature, flux rates

**Action Space:**
- Adjust T_substrate (±5°C), Fe flux (±10%), Se/Te ratio (±5%)

**Reward Function:**
- R = +10 (RHEED streaky) + 5×(T_c/10K) - 20×(defect_count) - 0.1×(time)

**Training:**
- Simulate 1,000 growth runs (kinetic Monte Carlo model)
- Deploy RL agent on real MBE (10 trial growths)
- Expected: 30% reduction in defect density vs. manual optimization

---

### Aim 2: STM/STS Characterization of Majorana Modes

#### 2.1 Scanning Tunneling Microscopy

**Instrument:** Omicron LT-STM (T=4.5K, base pressure 5×10⁻¹¹ Torr)

**Sample Transfer:** UHV suitcase (transfer from MBE to STM without air exposure)

**Tip Preparation:**
- Tungsten tip (electrochemically etched)
- In situ: Field emission cleaning + indentation on Au(111) (verify atomic resolution)

**Topography Imaging:**
- Scan size: 500×500 nm² (large area) → 50×50 nm² (atomic resolution)
- Setpoint: V_sample = +50 mV, I_tunnel = 100 pA
- Goal: Identify vortex cores (magnetic field B=2T applied perpendicular)

#### 2.2 Scanning Tunneling Spectroscopy (dI/dV)

**Protocol:**
- Position tip above vortex core (or nanowire end)
- Lock-in detection: V_ac = 1 mV RMS, f = 973 Hz
- Sweep V_bias = -5 to +5 mV (step 0.05 mV)
- Record dI/dV vs. V (proportional to local density of states)

**Majorana Signature:**
- **Zero-Bias Conductance Peak (ZBCP):** Peak at V=0, width Γ <50 µeV
- **Height:** dI/dV ≈ 2e²/h (quantized conductance)
- **Spatial Localization:** Decay length ξ <100 nm from vortex core

**Control Experiments:**
- Measure dI/dV away from vortex (should show BCS gap, no ZBCP)
- Vary magnetic field 0-5T (ZBCP should persist = topological)
- Compare to trivial superconductor (NbSe₂) - ZBCP only in Fe(Se,Te)

**Data Analysis:**
- Fit ZBCP to Lorentzian: dI/dV = A / [1 + (eV/Γ)²]
- Extract Γ (peak width), A (amplitude)
- Statistical significance: N=20 vortices, average Γ = 30±10 µeV

---

### Aim 3: Device Fabrication & Transport Measurements

#### 3.1 Nanowire Device Architecture

**Design:** Planar Josephson junction with 4 Majorana modes ("tetron")

**Fabrication Steps:**

1. **Photolithography:** Pattern contact pads (Cr/Au, 5/100 nm) via e-beam evaporation
2. **E-beam Lithography:** Define nanowire (width W=100 nm, length L=2 µm, PMMA resist)
3. **Reactive Ion Etch:** Etch Fe(Se,Te) using SF₆ plasma (rate 10 nm/min)
4. **Gate Electrodes:** Deposit Al₂O₃ dielectric (20 nm, ALD) + top gates (Ti/Au)

**Critical Parameters:**
- Nanowire width W=100 nm (< superconducting coherence length ξ ≈300 nm)
- Induced superconducting gap Δ_ind ≈ 1 meV (measured by Andreev reflection)

#### 3.2 Cryogenic Transport Measurements

**Dilution Refrigerator:**
- Base temperature T=20 mK
- Magnetic field B=0-9 Tesla (vector magnet)

**Measurement Setup:**
- **Lock-in amplifier:** SR830 (V_ac = 10 µV, f=17 Hz)
- **Pre-amplifier:** Low-noise I-V converter (gain 10⁷ V/A, noise 1 fA/√Hz)
- **Wiring:** Heavily filtered (π-filters at 4K, 1K, 100mK stages)

**Conductance Measurement:**
- Apply V_bias = -2 to +2 mV (across nanowire)
- Measure I → compute dI/dV (differential conductance)
- Look for:
  - **Majorana signature:** Conductance quantization G = 2e²/h at V=0
  - **Coulomb blockade:** Peaks in G vs. V_gate (tune chemical potential)

**Non-Abelian Braiding Protocol:**

1. **Initialize:** 4 Majorana modes at positions (x₁, x₂, x₃, x₄) along nanowire
2. **Braid:** Use voltage gates to move domain walls (exchange γ₁ ↔ γ₂)
3. **Measure:** Conductance G vs. braiding parameter θ (0 to 2π)
4. **Signature:** G(θ) = G₀[1 + cos(θ)] → oscillations confirm non-Abelian statistics

**Expected Result:** Period-2π oscillations with amplitude 10% of G₀

---

### Aim 4: Qubit Encoding & Quantum Gate Operations

#### 4.1 Topological Qubit Encoding

**Basis States:**
- |0⟩ = γ₁γ₂ (Majorana modes 1 & 2 occupied)
- |1⟩ = γ₃γ₄ (Majorana modes 3 & 4 occupied)

**Readout:** Capacitively-coupled SET (single-electron transistor)
- Charge sensor detects parity of occupied Majorana modes
- Fidelity >99% (demonstrated in GaAs quantum dots, adapt to topological system)

#### 4.2 Quantum Gate Implementation

**Braiding Gate (CNOT equivalent):**
- Exchange γ₂ ↔ γ₃ via voltage-controlled domain wall motion
- Gate time: τ_gate = 100 ns (limited by domain wall velocity ~1 m/s)

**Measurement Protocol (Quantum Process Tomography):**
- Prepare input state: |0⟩, |1⟩, |+⟩, |−⟩ (via initialization)
- Apply braiding gate
- Measure output state in X, Y, Z bases
- Reconstruct process matrix χ → extract fidelity F = Tr(χ_ideal χ_exp)

**Target:** F >99% (vs. 99.9% for superconducting qubits, but topological protection compensates)

#### 4.3 Decoherence Measurements

**T₁ (Energy Relaxation Time):**
- Initialize |1⟩ → wait time τ → measure P(1) → fit P(1) = e^(-τ/T₁)

**T₂ (Dephasing Time):**
- Ramsey interferometry: π/2 pulse → wait τ → π/2 pulse → measure
- Fit fringe visibility V(τ) = e^(-τ/T₂)

**Environmental Noise Sources:**
- Phonons: T₁ ∝ T⁻³ (reduce by cooling to 10 mK)
- Charge fluctuations: Gate voltage noise (mitigate with filtering)
- Magnetic field noise: Superconducting shields

**Target:** T₁ >10 ms, T₂ >1 ms (10-100× improvement over transmon qubits)

---

## Timeline

### Year 1
- Q1: MBE commissioning, substrate optimization
- Q2: First Fe(Se,Te) films, transport characterization (T_c measurements)
- Q3: STM/STS - detect ZBCP in vortex cores
- Q4: AI model training (RL agent for growth optimization)

### Year 2
- Q1-Q2: Optimize film quality (reduce defects to <1%)
- Q3: Thermal Hall measurement (confirm topological phase)
- Q4: Begin nanowire device fabrication

### Year 3
- Q1-Q2: Cryogenic transport - measure quantized conductance
- Q3: First braiding experiment (conductance vs. θ)
- Q4: Qubit readout circuit integration

### Year 4
- Q1: Gate fidelity measurements (quantum process tomography)
- Q2: Decoherence studies (T₁, T₂)
- Q3: Final validation, reproducibility tests
- Q4: Manuscript preparation, symposium

---

## Equipment & Facilities

**Stanford Nano Shared Facilities (SNSF):**
- E-beam lithography (JEOL JBX-6300FS, $180/hour)
- Reactive ion etching (Oxford Plasmalab 100, $120/hour)
- AFM, SEM (included in access fee)

**Stanford Low Temperature Lab:**
- Dilution refrigerator (Bluefors LD400, shared access)
- Vector magnet (9-3-3 Tesla, X-Y-Z)

**SLAC National Lab:**
- ARPES beamline 5-4 (angle-resolved photoemission - band structure mapping)

---

## Success Metrics

✓ ZBCP width <50 µeV (Majorana confirmation)
✓ Thermal Hall conductance within 10% of κ_xy = (π²/3)(k_B²T/h)
✓ Non-Abelian braiding oscillations with >3σ significance
✓ Gate fidelity F >99%
✓ T₂ >1 ms (100× improvement over transmons)

---

**Prepared by:** Dr. David Park & Dr. Lisa Nakamura
**Last Updated:** December 27, 2025
**Version:** 3.1

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Executive Summary - Physics]** `physics-executive-summary-example.md` - Type: `informs` | Condition: `when domain === 'physics'`
- **[Radiation Safety Approval]** `compliance/radiation_safety_2024.pdf` - Type: `requires` | Status: `approved`
- **[Literature Review]** `evidence/topological_materials_review_2024.md` - Type: `requires` | Evidence ID: `E-PHYS-002`

### Impacts (Downstream Documents)
- **[TDD - Physics]** `physics-tdd-example.md` - Type: `blocks` | Until: `this.status == approved` | Cascade: `true`
- **[Test Plan]** `docs/testing/physics_quantum_test_plan.md` - Type: `informs`

### Related Documents
- **[Biology Research Plan]** `biology-research-plan-example.md` - Relationship: `parallel-example`
- **[Chemistry Research Plan]** `chemistry-research-plan-example.md` - Relationship: `parallel-example`
- **[Psychology Research Plan]** `psychology-research-plan-example.md` - Relationship: `parallel-example`

### Satellite Documents
- **[TODO]** `satellites/TODO-RESPLAN-PHYS-001.md` - Status: `completed`
- **[DOR]** `satellites/DOR-RESPLAN-PHYS-001.md` - Status: `met`
- **[DOD]** `satellites/DOD-RESPLAN-PHYS-001.md` - Status: `met`

### Conditional Cross-References
```yaml
conditions:
  - when: domain === 'physics'
    require_dependencies: [Radiation Safety, Laser Safety, Cryogenic Safety, High-voltage Safety]
    require_satellites: [Laboratory Safety Protocols, Equipment Operating Procedures]
  - when: nanofabrication === true
    require_dependencies: [Clean room access, Nanofab training, Material compatibility clearance]
  - when: quantum_computing === true
    require_dependencies: [Dilution refrigerator access, Quantum control software]
```

### Validation Rules
**BLOCKER:** All dependencies approved, All safety approvals current, Clean room access confirmed
**ERROR:** Experimental protocols feasible, Equipment available, Timeline realistic
**WARN:** IP strategy, Reproducibility plan, Calibration procedures
