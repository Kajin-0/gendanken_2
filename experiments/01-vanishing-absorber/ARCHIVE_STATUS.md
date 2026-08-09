# Experiment 01 — Artifact Status Map

**Date:** 2026-08-09  
**Purpose:** separate the active few-mode inverse-metrology frontier from supporting, superseded, corrected, and stopped branches.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

There is still **no manuscript**.

---

## A. Canonical active frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
4. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
5. `HGCDTE_PUBLISHED_SAMPLE_B_PHASE_PRECISION.md`
6. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
7. `HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`
8. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
9. `HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`
10. `RESEARCH_LOG.md`

### Active candidate

Use a known monotonic graded-HgCdTe optical profile and wavelength-resolved complex response to recover a **finite set of differential internal transport modes** without physically scanning generation position.

Status:

**CANDIDATE UNDEREXPLORED INVERSE-METROLOGY METHOD — PRIORITY UNPROVEN.**

The forward wavelength/depth generation and graded-HgCdTe timing physics are prior art.

---

## B. Active core derivations

### `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`

**Status:** active exact operator / corrected.

Role:

- downstream collection -> CDF timing kernel;
- front collection -> survival timing kernel;
- cell-integrated matrix discretization;
- wavelength-independent boundary/common delay is not generically identifiable without calibration/gauge/prior.

### `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`

**Status:** active conditional extension / corrected.

Role:

- same orientation-correct matrix for mean-delay and conditional-broadening densities;
- law-of-total-variance subtraction of generation-position broadening;
- common first/second timing cumulants have the same boundary gauge ambiguity;
- local `q_1=1/v`, `q_2≈2D/v^3` interpretation is conditional.

### `HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`

**Status:** active measurement formulation.

Role: low-frequency complex response gives timing cumulants; differential phase removes wavelength-independent mean delay.

The old statement that a common delay can always be uniquely fitted should be interpreted through the corrected identifiability discussion in `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`.

---

## C. Published sample-B dimensional branch — ACTIVE FRONTIER

### `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`

**Status:** active literature-constrained dimensional result.

Primary published constraints:

```text
W ~ 3.7 um
nominal x ~ 0.316
nonlinear interdiffusion region removed
junction at high-Cd end
linear-gradient field ~100-200 V/cm.
```

Uses

- Hansen-Schmit-Casselman `E_g(x,T)` with `+0.832x^3`;
- Moazzami et al. above-gap `alpha(E,x,T)`;
- front-collection survival timing kernel.

Current central result:

```text
2.80 um -> mean generation depth ~0.677 um, Pabs ~0.998
3.88 um -> mean generation depth ~3.523 um, Pabs ~0.070
```

so

```math
\Delta\langle z\rangle\approx2.85\ {\rm um}.
```

At illustrative `v_eff=1e5 m/s`, this is approximately `28.5 ps` or `10.25 degrees` at `1 GHz`.

Real matrix singular-mode counts above relative thresholds `[1e-1,1e-2,1e-3,1e-4]`:

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

Interpretation: **few-mode, band-limited tomography**.

### `HGCDTE_PUBLISHED_SAMPLE_B_PHASE_PRECISION.md`

**Status:** active deterministic phase-noise stress test.

Synthetic anomaly:

```text
25% slowdown
center 2.30 um
sigma 0.35 um
baseline v=1e5 m/s.
```

Residual spectral anomaly phase is approximately `0.935 degree peak-to-peak` at `1 GHz`.

For a three-mode reconstruction at `0.10 degree` independent phase noise:

```text
median noise error vs recoverable target ~17.5%
90% peak-location error ~0.13 um.
```

At `0.25 degree`, localization degrades strongly. Five modes require substantially better phase precision for this anomaly.

This is conditioning, not an instrument/sample performance claim.

---

## D. Active numerical regressions

```text
numerics/hgcdte_published_sample_b_forward_matrix.py
numerics/hgcdte_published_sample_b_phase_noise.py
numerics/hgcdte_spectral_timing_linear_inverse.py
numerics/hgcdte_spectral_timing_kernel_tomography.py
numerics/hgcdte_spectral_timing_svd_resolution.py
numerics/hgcdte_spectral_timing_two_moment_inverse.py
```

Interpretation:

- published optical physics limits the practical spatial rank;
- a few coarse differential modes can survive realistic finite phase noise in the stated synthetic test;
- higher spatial rank is rapidly noise amplified;
- common timing offsets are gauge-like unless independently constrained.

---

## E. Supporting inverse files

### `HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md`

**Status:** supporting finite-optical-depth analytic result.

Role: derives stationary optical-kernel intuition and kernel-averaged inverse velocity in a simplified linear-gap/power-law absorption model.

The published sample-B Moazzami matrix now supersedes it as the active real-device optical model.

### `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_RESOLUTION.md`

**Status:** supporting general resolution budget.

Role: tracks optical width, spectral linewidth, composition-profile uncertainty, timing precision, and conditioning.

### `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`

**Status:** active hard claim boundary.

Role: records collisions with wavelength-dependent transit physics, localized-position HgCdTe timing, and graded-HgCdTe forward modeling.

### `HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`

**Status:** supporting primary-source device selection / validation proposal.

The new sample-B dimensional file is the more specific active calculation.

---

## F. Entrance-gap crossover branch — supporting geometry

Retain:

```text
HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md
HGCDTE_SPECTRAL_DRIFT_DIFFUSION_ROBUSTNESS.md
HGCDTE_SPECTRAL_MOMENTUM_SCATTERING_SURROGATE.md
```

The entrance-gap switch explains why wavelength can encode position, but a mandatory visible timing peak/cusp is not claimed.

---

## G. Ballistic timing-peak branch — SUPERSEDED AS UNIVERSAL CLAIM

Retain as provenance:

```text
HGCDTE_SPECTRAL_DELAY_PEAK.md
HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md
HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md
numerics/hgcdte_spectral_delay_peak.py
numerics/hgcdte_spectral_delay_relaxation.py
```

These remain valid only inside their directed-ballistic / mean-energy assumptions.

Do **not** present the entrance-gap timing maximum as transport independent.

---

## H. Photoexcitation / graded-material supporting branches

Retain as provenance/support:

```text
HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md
HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md
HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md
HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md
HGCDTE_LINEAR_GRADED_KANE_WKB.md
HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md
HGCDTE_GRADED_POISSON_ROBUSTNESS.md
HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md
HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md
```

Important permanent corrections:

- downstream-generated photoelectrons are not generally cold;
- excess energy is not automatically persistent forward velocity;
- nonlocal II cannot always be represented by a local threshold field.

---

## I. Earlier abstract branches — provenance only

Retain but do not restart without a new physical reason:

```text
ONE_PORT_RESONATOR_DYNAMICS.md
ACTIVE_VOLUME_COUNTEREXAMPLE.md
PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md
HOPFIELD_RETUNING_NO_GO.md
ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md
TIME_DEPENDENT_CAPTURE_AUDIT.md
ADAPTIVE_FEEDFORWARD_MODE_CAPACITY.md
OUTPUT_RECORD_INFORMATION_CAPACITY.md
```

These document how the original universal-bound program failed or narrowed.

---

## J. Hard prior-art boundary

Do not claim novelty for

- wavelength-dependent photodiode generation depth / bandwidth;
- graded-HgCdTe forward optical/transport response modeling;
- grading-induced HgCdTe timing improvement;
- localized-position HgCdTe transit measurement;
- spectral response revealing spatial collection differences.

Unresolved close source:

```text
Potential application of HgCdTe detector with composition gradient in laser measurement
Journal of Applied Optics (2024)
DOI 10.5768/JAO202445.0310009
```

Metadata are confirmed; full technical collision remains OPEN.

---

## K. Current forward branch

Do **not** add more generic inverse mathematics.

Next work:

1. obtain/digitize the actual 2023 sample-B `x(z)` fit;
2. construct an instrument-level wavelength × RF-frequency covariance model;
3. add Urbach/reflection/interference only if they materially change the kernel matrix;
4. fit multiple RF frequencies simultaneously;
5. validate recovered differential modes against localized-position timing or calibrated microscopic transport;
6. read the unresolved 2024 laser-measurement paper;
7. reassess publication readiness only after real-data or independently validated inversion.
