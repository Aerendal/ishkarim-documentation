# Technical Design Document: QuantMat Project
## Data Acquisition, Analysis Infrastructure, and Device Control Systems

**Project ID:** NSF-DMR-2024-9112
**Technical Lead:** Dr. Lisa Nakamura
**Version:** 2.2 | **Date:** December 27, 2025

---

## 1. System Architecture

```
┌─────────────────────────────────────────────────────────┐
│              EXPERIMENTAL CONTROL LAYER                  │
├─────────────────────────────────────────────────────────┤
│  MBE Control → RHEED imaging, flux monitoring           │
│  STM Control → Tip positioning, spectroscopy acquisition│
│  Cryostat Control → Temperature, magnetic field          │
│  Transport Measurement → Lock-in amps, voltage sources   │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              DATA ACQUISITION LAYER                      │
├─────────────────────────────────────────────────────────┤
│  NI DAQmx → Analog/digital I/O (16-bit, 100 kS/s)       │
│  GPIB/USB → Instrument communication (lock-ins, DMMs)   │
│  Camera API → RHEED images (1 fps during growth)        │
│  Custom FPGA → Real-time feedback (gate voltage tuning) │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              DATA STORAGE LAYER                          │
├─────────────────────────────────────────────────────────┤
│  HDF5 Files → Time-series data (transport, spectroscopy)│
│  PostgreSQL → Metadata (growth runs, device parameters) │
│  MinIO (S3) → Images (RHEED, AFM, SEM)                  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              ANALYSIS LAYER                              │
├─────────────────────────────────────────────────────────┤
│  Python (NumPy, SciPy) → Signal processing, fitting     │
│  COMSOL → Finite element modeling (electric fields)     │
│  Kwant → Tight-binding transport simulations            │
│  TensorFlow → ML models (growth optimization, ZBCP ID)  │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Data Models

### 2.1 Database Schema (PostgreSQL)

#### Table: `mbe_growth_runs`
```sql
CREATE TABLE mbe_growth_runs (
    run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    run_date DATE NOT NULL,
    operator VARCHAR(100),

    -- Substrate
    substrate_type VARCHAR(50) DEFAULT 'SrTiO3(001)',
    substrate_size_mm INTEGER DEFAULT 10,

    -- Growth parameters
    substrate_temperature_celsius DECIMAL(5,2),
    fe_flux_angstrom_per_sec DECIMAL(6,4),
    se_flux_angstrom_per_sec DECIMAL(6,4),
    te_flux_angstrom_per_sec DECIMAL(6,4),
    growth_time_minutes DECIMAL(6,2),
    final_thickness_nm DECIMAL(7,2),

    -- RHEED observations
    rheed_pattern_quality ENUM('streaky', 'spotty', 'mixed'),
    rheed_video_path VARCHAR(500),

    -- Post-growth characterization
    xrd_peak_fwhm_degrees DECIMAL(6,4),
    afm_roughness_nm DECIMAL(5,3),
    transport_tc_kelvin DECIMAL(5,2),
    transport_rrr DECIMAL(6,2),

    -- AI model predictions (if used)
    predicted_tc_kelvin DECIMAL(5,2),
    predicted_defect_density DECIMAL(8,2),

    -- Quality flag
    qc_pass BOOLEAN,
    notes TEXT,

    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `stm_measurements`
```sql
CREATE TABLE stm_measurements (
    measurement_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sample_id UUID REFERENCES mbe_growth_runs(run_id),
    measurement_date DATE NOT NULL,

    -- Scan parameters
    scan_type ENUM('topography', 'spectroscopy'),
    scan_area_nm2 DECIMAL(8,2),  -- e.g., 500x500 = 250000
    temperature_kelvin DECIMAL(5,3) DEFAULT 4.5,
    magnetic_field_tesla DECIMAL(5,3),

    -- Spectroscopy (if applicable)
    spectroscopy_type ENUM('IV', 'dIdV', NULL),
    bias_voltage_min_mv DECIMAL(6,3),
    bias_voltage_max_mv DECIMAL(6,3),
    num_points INTEGER,

    -- Majorana detection
    zbcp_detected BOOLEAN DEFAULT FALSE,
    zbcp_width_uev DECIMAL(6,2),  -- micro-eV
    zbcp_amplitude DECIMAL(10,6),  -- conductance in units of 2e²/h

    -- File paths
    data_file_path VARCHAR(500),  -- HDF5 with full I-V curves
    image_path VARCHAR(500),  -- PNG rendering

    -- Analysis
    analyzed BOOLEAN DEFAULT FALSE,
    analysis_notes TEXT,

    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `transport_devices`
```sql
CREATE TABLE transport_devices (
    device_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sample_id UUID REFERENCES mbe_growth_runs(run_id),
    device_name VARCHAR(100) UNIQUE NOT NULL,

    -- Geometry
    nanowire_width_nm INTEGER,
    nanowire_length_um DECIMAL(5,2),
    num_majorana_modes INTEGER,  -- 2, 4, or 6

    -- Fabrication details
    fabrication_date DATE,
    lithography_type ENUM('ebeam', 'photolithography'),
    etch_depth_nm DECIMAL(6,2),

    -- Electrical characteristics
    resistance_ohms DECIMAL(10,2),
    induced_gap_mev DECIMAL(5,3),

    -- Qubit parameters (if measured)
    t1_microseconds DECIMAL(10,2),
    t2_microseconds DECIMAL(10,2),
    gate_fidelity_percent DECIMAL(5,2),

    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `transport_measurements`
```sql
CREATE TABLE transport_measurements (
    measurement_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    device_id UUID REFERENCES transport_devices(device_id),
    measurement_date TIMESTAMP NOT NULL,

    -- Measurement type
    measurement_type ENUM('conductance_vs_bias', 'conductance_vs_gate', 'braiding', 'ramsey'),

    -- Experimental conditions
    temperature_mk DECIMAL(6,2),  -- millikelvin
    magnetic_field_tesla DECIMAL(5,3),

    -- Gate voltages
    gate_voltage_1_mv DECIMAL(8,3),
    gate_voltage_2_mv DECIMAL(8,3),

    -- Results (summary)
    max_conductance_2e2h DECIMAL(6,4),  -- in units of 2e²/h
    quantization_detected BOOLEAN,

    -- Braiding results (if applicable)
    braiding_angle_radians DECIMAL(5,3),
    oscillation_amplitude DECIMAL(6,4),

    -- Data file
    data_file_path VARCHAR(500),  -- HDF5 with full traces

    analyzed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 3. Experimental Control Software

### 3.1 MBE Control System (Python + LabVIEW)

**Architecture:**
- **LabVIEW Real-Time:** Low-level control (shutter timing, flux PID loops)
- **Python Wrapper:** High-level sequencing, data logging

**Python Script: `mbe_control.py`**

```python
import numpy as np
import h5py
import time
from mbe_interface import MBEController  # Custom hardware interface

class GrowthRecipe:
    def __init__(self, substrate_temp, fe_flux, se_flux, te_flux, duration):
        self.substrate_temp = substrate_temp  # Celsius
        self.fe_flux = fe_flux  # Angstrom/sec
        self.se_flux = se_flux
        self.te_flux = te_flux
        self.duration = duration  # minutes

def execute_growth(recipe, run_id):
    """Execute MBE growth with real-time monitoring"""

    mbe = MBEController()

    # Ramp substrate temperature
    print(f"Ramping substrate to {recipe.substrate_temp}°C...")
    mbe.set_substrate_temp(recipe.substrate_temp)
    while abs(mbe.get_substrate_temp() - recipe.substrate_temp) > 1:
        time.sleep(5)
    print("Temperature stable.")

    # Open shutters (start deposition)
    print("Opening shutters...")
    mbe.set_flux('Fe', recipe.fe_flux)
    mbe.set_flux('Se', recipe.se_flux)
    mbe.set_flux('Te', recipe.te_flux)
    mbe.open_shutter('Fe')
    mbe.open_shutter('Se')
    mbe.open_shutter('Te')

    # Monitor RHEED + log data
    start_time = time.time()
    duration_sec = recipe.duration * 60
    log_data = []

    while time.time() - start_time < duration_sec:
        # Acquire RHEED image
        rheed_image = mbe.get_rheed_image()

        # Log parameters
        log_entry = {
            'time': time.time() - start_time,
            'substrate_temp': mbe.get_substrate_temp(),
            'fe_flux': mbe.get_flux('Fe'),
            'se_flux': mbe.get_flux('Se'),
            'te_flux': mbe.get_flux('Te'),
            'rheed_intensity': np.mean(rheed_image)  # Simple metric
        }
        log_data.append(log_entry)

        # Save RHEED image every 10 seconds
        if len(log_data) % 10 == 0:
            timestamp = int(time.time())
            cv2.imwrite(f"rheed_{run_id}_{timestamp}.png", rheed_image)

        time.sleep(1)  # 1 Hz logging

    # Close shutters
    print("Closing shutters...")
    mbe.close_shutter('Fe')
    mbe.close_shutter('Se')
    mbe.close_shutter('Te')

    # Save log to HDF5
    with h5py.File(f"growth_log_{run_id}.h5", 'w') as f:
        f.create_dataset('time', data=[d['time'] for d in log_data])
        f.create_dataset('substrate_temp', data=[d['substrate_temp'] for d in log_data])
        f.create_dataset('fe_flux', data=[d['fe_flux'] for d in log_data])
        # ... other datasets

    print(f"Growth complete. Run ID: {run_id}")
    return log_data

# Example usage
recipe = GrowthRecipe(
    substrate_temp=350,
    fe_flux=0.5,
    se_flux=0.5,
    te_flux=0.5,
    duration=30  # 30 minutes
)

run_id = "20250115_001"
execute_growth(recipe, run_id)
```

### 3.2 STM Control (Nanonis + Python)

**STM Controller:** Nanonis SPM controller (commercial, SPECS)

**Python API Integration:**

```python
import nanonis_spm
import numpy as np

def acquire_sts_spectrum(x_nm, y_nm, v_min_mv, v_max_mv, num_points):
    """
    Acquire dI/dV spectrum at specified position

    Args:
        x_nm, y_nm: Tip position in nm
        v_min_mv, v_max_mv: Bias voltage range in mV
        num_points: Number of points in sweep

    Returns:
        voltages, didv: Arrays of voltage and dI/dV
    """

    stm = nanonis_spm.get_controller()

    # Position tip
    stm.move_tip(x_nm, y_nm)
    time.sleep(0.5)  # Allow stabilization

    # Configure lock-in
    stm.set_lockin_amplitude(1.0)  # 1 mV RMS
    stm.set_lockin_frequency(973)  # Hz

    # Sweep bias voltage
    voltages = np.linspace(v_min_mv, v_max_mv, num_points)
    didv = []

    for v in voltages:
        stm.set_bias_voltage(v)
        time.sleep(0.01)  # Wait for settling
        didv_value = stm.read_lockin_output()
        didv.append(didv_value)

    return voltages, np.array(didv)

# Example: Scan for ZBCPs in grid pattern
for x in np.arange(0, 500, 10):  # 500 nm scan, 10 nm step
    for y in np.arange(0, 500, 10):
        voltages, didv = acquire_sts_spectrum(x, y, -5, 5, 200)

        # Detect ZBCP
        center_idx = len(voltages) // 2
        zbcp_amplitude = didv[center_idx]

        if zbcp_amplitude > threshold:
            print(f"ZBCP detected at ({x}, {y}) nm")
            # Save full spectrum for detailed analysis
            save_spectrum(x, y, voltages, didv)
```

### 3.3 Cryogenic Transport Measurement

**Equipment:**
- Lock-in amplifier: SR830 (GPIB interface)
- Voltage source: Keithley 2400 (USB/GPIB)
- DAQ: National Instruments PCIe-6363 (16-bit, 2 MS/s)

**Python Script: `transport_measurement.py`**

```python
import pyvisa
import numpy as np
import h5py

class TransportSetup:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self.lockin = rm.open_resource('GPIB0::8::INSTR')  # SR830
        self.vgate = rm.open_resource('GPIB0::24::INSTR')  # Keithley

    def measure_conductance_vs_bias(self, v_min, v_max, num_points, gate_voltage):
        """Measure dI/dV as function of bias voltage"""

        # Set gate voltage
        self.vgate.write(f"SOUR:VOLT {gate_voltage}")
        self.vgate.write("OUTP ON")

        # Configure lock-in
        self.lockin.write("SLVL 1e-5")  # 10 µV excitation
        self.lockin.write("FREQ 17")  # 17 Hz

        voltages = np.linspace(v_min, v_max, num_points)
        conductance = []

        for v in voltages:
            # Apply DC bias (would need separate bias source, simplified here)
            # In practice: use DAC channel to control bias via voltage divider

            time.sleep(0.1)  # Lock-in time constant

            # Read X, Y from lock-in
            x = float(self.lockin.query("OUTP? 1"))
            y = float(self.lockin.query("OUTP? 2"))
            r = np.sqrt(x**2 + y**2)  # Magnitude

            # Convert to conductance (calibrated by known resistor)
            g = r / (1e-5)  # Assuming 10 µV excitation → G = I/V

            conductance.append(g)

        return voltages, np.array(conductance)

# Example usage
setup = TransportSetup()
v_bias, G = setup.measure_conductance_vs_bias(-2e-3, 2e-3, 400, gate_voltage=0.5)

# Check for quantization
G_quantum = 2 * (1.6e-19)**2 / 6.626e-34  # 2e²/h in Siemens
quantized = np.any(np.abs(G - G_quantum) / G_quantum < 0.05)  # Within 5%

if quantized:
    print("Quantized conductance detected!")
```

---

## 4. Data Analysis Pipelines

### 4.1 ZBCP Detection (ML Model)

```python
# train_zbcp_detector.py

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load training data (simulated + experimental spectra)
# Format: X = (N_samples, 200) - dI/dV curves
#         y = (N_samples, 1) - labels (1=ZBCP, 0=no ZBCP)

X_train, X_test, y_train, y_test = load_sts_dataset()

# Build 1D CNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(32, kernel_size=5, activation='relu', input_shape=(200, 1)),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Conv1D(64, kernel_size=5, activation='relu'),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32)

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.3f}")

# Save model
model.save("zbcp_detector_v1.h5")
```

### 4.2 Tight-Binding Simulations (Kwant)

```python
# simulate_nanowire.py

import kwant
import numpy as np

# Define nanowire Hamiltonian (Kitaev chain + spin-orbit coupling)
def make_nanowire(L=100, mu=-0.5, delta=0.3, alpha=0.5):
    """
    L: Length (sites)
    mu: Chemical potential
    delta: Superconducting pairing
    alpha: Spin-orbit coupling
    """

    lat = kwant.lattice.chain(norbs=2)  # 2 orbitals (spin up/down)

    syst = kwant.Builder()

    # Define Hamiltonian
    for i in range(L):
        syst[lat(i)] = -mu * tau_z  # On-site energy

    for i in range(L-1):
        syst[lat(i), lat(i+1)] = -1 * tau_z + 1j * alpha * sigma_y  # Hopping + SOC

    # Superconducting pairing
    syst = syst.finalized()

    # Compute spectrum
    energies = kwant.physics.Bands(syst)

    return energies

# Analyze
energies = make_nanowire(L=100)
plot_spectrum(energies)  # Should show gap with zero-energy modes at ends
```

---

## 5. Deployment

### 5.1 Lab Server Infrastructure

**Hardware:**
- Dell PowerEdge R740 (dual Xeon, 256GB RAM, 10TB storage)
- UPS backup (4 hours runtime)
- 10 Gbps network to measurement systems

**Software Stack:**
- OS: Ubuntu 22.04 LTS
- Database: PostgreSQL 14 + TimescaleDB (time-series optimization)
- Storage: MinIO (S3-compatible object storage)
- Monitoring: Prometheus + Grafana

### 5.2 Data Backup

**Strategy:**
- Real-time: PostgreSQL streaming replication to standby server
- Daily: Full backup to Stanford Research Computing Facility (100 TB allocation)
- Long-term: Raw data archived to AWS Glacier (cost-effective, infrequent access)

---

## 6. Performance Requirements

### Measurement Throughput
- STM spectroscopy: 100 spectra/hour (automation script)
- Transport measurement: 1 full IV sweep per 5 minutes
- RHEED logging: 1 fps (1 MB/image × 3600 images/hour = 3.6 GB/hour)

### Data Storage
- MBE growth run: ~5 GB (RHEED video + time-series logs)
- STM scan: ~500 MB (high-resolution topography + spectroscopy)
- Transport measurement: ~10 MB (time-series data)
- Total project: ~50 TB (4 years × 12 months × 1 TB/month)

---

**Prepared by:** Dr. Lisa Nakamura
**Last Updated:** December 27, 2025
**Version:** 2.2

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Research Plan - Physics]** `physics-research-plan-example.md` - Type: `requires` | Status: `approved` | Condition: `when domain === 'physics'`
- **[Executive Summary - Physics]** `physics-executive-summary-example.md` - Type: `informs`
- **[Data Model Schema]** `schemas/physics_quantum_schema.json` - Type: `requires` | Evidence ID: `E-PHYS-TDD-001`

### Impacts (Downstream Documents)
- **[Implementation Tasks]** `jira/PHYS-TDD-IMPLEMENTATION-EPIC` - Type: `blocks` | Until: `this.status == approved` | Cascade: `true`
- **[Runbook]** `docs/ops/physics_platform_runbook.md` - Type: `informs`
- **[Test Plan]** `docs/testing/physics_system_test_plan.md` - Type: `informs`

### Related Documents
- **[Biology TDD]** `biology-tdd-example.md` - Relationship: `parallel-example`
- **[Chemistry TDD]** `chemistry-tdd-example.md` - Relationship: `parallel-example`
- **[Psychology TDD]** `psychology-tdd-example.md` - Relationship: `parallel-example`

### Satellite Documents
- **[TODO]** `satellites/TODO-TDD-PHYS-001.md` - Status: `completed`
- **[DOR]** `satellites/DOR-TDD-PHYS-001.md` - Status: `met`
- **[DOD]** `satellites/DOD-TDD-PHYS-001.md` - Status: `met`
- **[ADR Collection]** `satellites/ADR-TDD-PHYS-*.md` - Key decisions on real-time data acquisition, time-series DB

### Conditional Cross-References
```yaml
conditions:
  - when: domain === 'physics'
    require_dependencies: [Real-time data acquisition systems, HPC integration]
    require_satellites: [ADR for time-series database, ADR for data compression]
  - when: quantum_measurements === true
    require_dependencies: [Cryogenic data logging, Quantum control interfaces]
  - when: high_frequency_data === true
    require_dependencies: [High-bandwidth storage, Real-time processing pipeline]
```

### Validation Rules
**BLOCKER:** All dependencies approved, System supports all measurement types, Real-time performance verified
**ERROR:** Database optimized for time-series, Data compression effective, Monitoring complete
**WARN:** API versioning, Disaster recovery, Cost optimization
