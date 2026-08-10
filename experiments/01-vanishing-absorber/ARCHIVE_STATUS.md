# Experiment 01 — Artifact Status Map

**Date:** 2026-08-10  
**Purpose:** separate the active matched-relocation frontier from benchmark, supporting, superseded, rejected, and stopped branches.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

There is still **no manuscript**.

---

## A. Canonical active frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `HGCDTE_TRANSLATED_GRADIENT_PRIOR_ART_BOUNDARY.md`
4. `HGCDTE_PROGRAMMED_INTERFACE_SAFE_JOINT_DESIGN.md`
5. `HGCDTE_RELOCATION_EDGE_ENCODING.md`
6. `HGCDTE_PROGRAMMED_WIDTH_INTERDIFFUSION.md`
7. `HGCDTE_PROGRAMMED_TRANSLATED_GRADIENT_FEASIBILITY.md`
8. `HGCDTE_TRANSLATED_GRADIENT_MATCHING_TOLERANCES.md`
9. `HGCDTE_CONTACT_INTERFACE_CONFOUNDING.md`
10. `HGCDTE_SHORTWAVE_FINITE_RF_JACOBIAN.md`
11. `HGCDTE_SAMPLE_A_CROSSBAND_SELF_CALIBRATION.md`
12. `HGCDTE_SAMPLE_A_SHORTWAVE_GLOBAL_DESIGN.md`
13. `HGCDTE_PAIRED_AB_JOINT_IDENTIFIABILITY.md`
14. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
15. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
16. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
17. `RESEARCH_LOG.md`

### Active candidate

> **Use a known graded HgCdTe absorber as a wavelength-dependent internal position encoder, then validate differential transport by translating the same buried gradient feature between otherwise matched devices and testing whether the complex wavelength × RF fingerprint translates with it.**

**Status:** CANDIDATE UNDEREXPLORED INVERSE-METROLOGY / MATCHED-RELOCATION VALIDATION METHOD — PRIORITY UNPROVEN.

---

## B. Active exact/operator files

### `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`

**Status:** ACTIVE exact operator.

Contains

```text
downstream CDF kernel
front-collection survival kernel
cell-integrated discretization
boundary/common-delay gauge.
```

### `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`

**Status:** SUPPORTING conditional extension.

Useful for timing-broadening modes and conditional drift-diffusion interpretation. Not the current mechanism-validation bottleneck.

### `HGCDTE_SHORTWAVE_FINITE_RF_JACOBIAN.md`

**Status:** ACTIVE finite-RF correction / negative result.

RF diversity rotates the sensitivity operator but does not rescue the published near-junction A/B geometry by itself.

---

## C. Purpose-built matched-relocation branch — ACTIVE

### `HGCDTE_CONTACT_INTERFACE_CONFOUNDING.md`

**Status:** ACTIVE mechanism-attribution correction.

The published sample-A near-junction fingerprint can be closely mimicked by interface/contact transport plus smooth bulk changes.

This is the decisive reason the project moved away from using published A/B as the final causal proof.

### `HGCDTE_MATCHED_CONTACT_TRANSLATED_GRADIENT_DESIGN.md`

**Status:** SUPPORTING prototype / corrected.

Introduces endpoint-preserving translated internal gradient features and shows that matched nuisance amplitudes are essential.

The early `2.6 -> 3.2 um` geometry came from a restricted depth grid and is **not** the current final depth design.

### `HGCDTE_TRANSLATED_GRADIENT_MATCHING_TOLERANCES.md`

**Status:** SUPPORTING prototype tolerance framework.

Provides the exact common/mismatch decomposition

```math
J_2q_2-J_1q_1
=(J_2-J_1)c+\frac{J_2+J_1}{2}\delta.
```

Its numerical tolerances around the shallow prototype are provenance, not final interface-safe specifications.

### `HGCDTE_PROGRAMMED_TRANSLATED_GRADIENT_FEASIBILITY.md`

**Status:** ACTIVE materials feasibility boundary.

Current growth interpretation:

```text
MBE   -> strongest direct profile-programming precedent
MOCVD -> strong graded-layer precedent with measurable interdiffusion
LPE   -> 2024 work demonstrates controllable longitudinal gradient sign/magnitude.
```

No recovered source has yet demonstrated the exact matched translated internal feature.

### `HGCDTE_PROGRAMMED_INTERFACE_SAFE_JOINT_DESIGN.md`

**Status:** ACTIVE strongest depth/spectral design.

Includes

```text
front + back interface nuisance modes
fixed total wavelength-time resource
Pabs-dependent phase precision
arbitrary complex intercept per RF
feature-edge clearance from both boundaries.
```

Conservative reference envelope:

```text
feature centers ~4.1 and ~5.5-5.6 um
feature width ~1 um
lambda ~2.00-2.40 um
RF = 0.25, 0.5, 1, 2, 3 GHz.
```

The exact tenth-micron depth is not a universal fabrication target.

### `HGCDTE_RELOCATION_EDGE_ENCODING.md`

**Status:** ACTIVE explanatory identity + numerical convergence.

Relocation probes the spatial derivative of sensitivity; for a flat feature

```math
\partial y/\partial z_0=A[K(b)-K(a)].
```

At 320 cells, `25-100 nm` edge ramps form an approximately `1%` information plateau; `200 nm` costs roughly `30%` relative to `100 nm`.

### `HGCDTE_PROGRAMMED_WIDTH_INTERDIFFUSION.md`

**Status:** ACTIVE shape/process robustness.

At fixed peak gradient near `1.95 kV/cm`:

```text
useful unblurred width ~0.9-1.1 um
Gaussian sigma_d=0.05 um -> ~8% information-amplitude loss
sigma_d=0.10 um -> ~20%
sigma_d=0.15 um -> ~33%.
```

The statistics-like and additive-like phase-noise envelopes select essentially the same design family.

### `HGCDTE_TRANSLATED_GRADIENT_PRIOR_ART_BOUNDARY.md`

**Status:** ACTIVE hard literature boundary.

Explicitly blocks novelty claims for graded-HgCdTe high-speed response, built-in-field transport, wavelength/depth forward physics, localized timing, optical-load transients, and programmable positive LPE grading.

The 2024 Applied Optics close collision remains unresolved.

---

## D. Published A/B rescue branch — SUPPORTING / SUPERSEDED AS FINAL VALIDATION

These files remain important because they revealed the failure modes that motivated the purpose-built control.

### `HGCDTE_PAIRED_AB_JOINT_IDENTIFIABILITY.md`

**Status:** SUPPORTING negative result.

Arbitrary smooth A/B transport modes overlap strongly; paired data are contrast data, not two independent profile inverses.

### `HGCDTE_SAMPLE_A_SHORTWAVE_VISIBILITY.md`

**Status:** SUPPORTING positive/negative result.

Short-wave access restores raw visibility of sample A's near-junction nonlinear region.

### `HGCDTE_SAMPLE_A_SHORTWAVE_CALIBRATION_REQUIREMENT.md`

**Status:** SUPPORTING negative result.

Raw visibility does not remove smooth-mode degeneracy; the static A-localized anomaly requires few-millidegree smooth-mode knowledge in the current illustrative model.

### `HGCDTE_SAMPLE_A_SHORTWAVE_TWO_BAND_DESIGN.md`

**Status:** SUPPORTING reduced design.

At fixed total time, a two-band design near `2.00` and `~2.69 um` improves the illustrative short-wave detection problem when smooth-mode priors are already tight.

### `HGCDTE_SAMPLE_A_SHORTWAVE_GLOBAL_DESIGN.md`

**Status:** SUPPORTING global negative result.

The arbitrary-support fixed-time optimizer confirms rather than removes the smooth-mode calibration floor.

### `HGCDTE_SAMPLE_A_CROSSBAND_SELF_CALIBRATION.md`

**Status:** SUPPORTING negative result.

Mid/deep A data cannot cheaply supply the short-wave smooth baseline prior; broad no-prior spectral self-calibration remains severely ill-conditioned.

### Short-wave temperature/load branches

**Status:** SUPPORTING / STOPPED AS PRIMARY ROUTES.

Short-wave temperature retuning does not preserve the full kernel well enough for a clean baseline-canceling difference.

Optical-load-dependent HgCdTe transients are prior art; load differencing remains only a possible control construction.

---

## E. Published sample-B calibration branch — ACTIVE BENCHMARK / SECONDARY CONTROL

### `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`

**Status:** ACTIVE benchmark.

The published smooth sample B gives real multi-wavelength depth leverage and only a few strongly conditioned transport modes.

### `HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md`

**Status:** ACTIVE covariance lesson.

Optical rank is not experimental rank when absorbed signal changes strongly with wavelength.

### `HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md`

**Status:** ACTIVE benchmark optimal-design result.

Reduced sample-B calibration uses a few information-rich wavelength bands rather than uniform dense sampling.

### `HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md`

**Status:** ACTIVE benchmark RF-validity diagnostic.

Optical-only deterministic timing gives an illustrative usable-frequency envelope; not a universal device bandwidth.

---

## F. Mid/deep temperature-control branch — ACTIVE SECONDARY CONTROL

### `HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md`

**Status:** ACTIVE secondary experimental design.

Fixed wavelength across temperature is optically confounded.

### `HGCDTE_SAMPLE_A_CONSTRAINT_FAMILY_JOINT_ISO_KERNEL.md`

**Status:** ACTIVE conditional robustness result.

The 72-profile A sensitivity family supports a useful mid/deep common A/B temperature schedule near

```text
300 K -> 3.632 um
215 K -> ~3.793 um
115 K -> ~4.005 um.
```

### `HGCDTE_SAMPLE_A_THERMO_OPTIC_INTERFERENCE.md`

**Status:** ACTIVE supporting stress.

Empirical composition/temperature-dependent refractive index and one-return interference do not destroy the wavelength location of that mid/deep control schedule.

This branch is no longer the primary localizer of the internal high-gradient feature.

---

## G. Phase/metrology resource branch — ACTIVE SUPPORT

### `HGCDTE_PHASE_PRECISION_SNR_REQUIREMENT.md`

**Status:** ACTIVE white-noise resource calculation.

Representative scale:

```text
0.10 degree single phase -> ~55.2 dB coherent power-SNR
0.10 degree A-B differential target with equal independent channels -> ~58.2 dB/channel.
```

### `HGCDTE_PAIRED_PHASE_COMMON_MODE_REQUIREMENTS.md`

**Status:** ACTIVE covariance/systematic requirement.

Correlated phase and reciprocal-swap drift must be measured rather than assumed.

### Wavelength-independent electrical pole cancellation

**Status:** ACTIVE derived result.

Any device/readout transfer depending only on RF frequency cancels after fitting one arbitrary wavelength-independent complex intercept per RF.

Wavelength-dependent electrical-state effects remain open.

---

## H. Prior-art / novelty boundary — ACTIVE

Hard prior art includes

```text
wavelength-dependent absorption/generation depth
graded-HgCdTe spectral response
graded-HgCdTe built-in-field transport
high-speed/RF response of graded HgCdTe
localized HgCdTe transit timing
optical-load-dependent HgCdTe transients
programmable positive composition gradients by LPE.
```

### Unresolved closest source

```text
Potential application of HgCdTe detector with composition gradient in laser measurement
Journal of Applied Optics 45(3), 2024, 549-556
DOI 10.5768/JAO202445.0310009
```

Metadata are confirmed; full technical content remains unavailable in the current audit.

Allowed wording remains:

> **candidate underexplored inverse-metrology / matched-relocation validation method; priority unproven.**

---

## I. Entrance-gap / ballistic branch — SUPPORTING OR SUPERSEDED

Supporting geometry:

```text
HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md
HGCDTE_SPECTRAL_DRIFT_DIFFUSION_ROBUSTNESS.md
HGCDTE_SPECTRAL_MOMENTUM_SCATTERING_SURROGATE.md
```

Superseded as universal claim:

```text
HGCDTE_SPECTRAL_DELAY_PEAK.md
HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md
HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md
```

A mandatory entrance-gap timing maximum/cusp is **not** claimed.

---

## J. Graded-material / tunneling provenance

Retain as supporting history:

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

---

## K. Earlier abstract branches — PROVENANCE ONLY

Retain but do not restart casually:

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

These document why the original universal-bound program failed/narrowed.

---

## L. Current numerical regressions

Most important active scripts:

```text
numerics/hgcdte_programmed_joint_depth_spectral_design.py
numerics/hgcdte_programmed_width_interdiffusion.py
numerics/hgcdte_relocation_edge_convergence.py
numerics/hgcdte_programmed_gradient_tolerances.py
numerics/hgcdte_matched_contact_translated_gradient_design.py
numerics/hgcdte_shortwave_finite_rf_jacobian.py
numerics/hgcdte_contact_confounding.py
numerics/hgcdte_sample_a_crossband_self_calibration.py
```

Older sample-B/A scripts remain benchmark/provenance regressions.

---

## M. Current forward branch

Do **not** add more generic inverse mathematics or continue free geometric optimization.

Priority:

1. select one HgCdTe growth route;
2. replace generic Gaussian blur with that process's reachable `x(z)` family;
3. pass reachable matched translated profiles through the interface-safe fixed-resource wavelength × RF objective;
4. recompute final differential mismatch tolerances;
5. recover the unresolved 2024 Applied Optics paper before any novelty language;
6. obtain realistic wavelength × RF covariance, drift, and wavelength-dependent electrical-state data;
7. characterize realized `x(z)` independently;
8. obtain matched-device data;
9. reassess manuscript readiness only after real-data or independently validated inversion.
