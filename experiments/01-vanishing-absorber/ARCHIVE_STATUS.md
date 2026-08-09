# Experiment 01 — Artifact Status Map

**Date:** 2026-08-09  
**Purpose:** separate the active few-mode inverse-metrology frontier from supporting, superseded, rejected, and stopped branches.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

There is still **no manuscript**.

---

## A. Canonical active frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
4. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
5. `HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md`
6. `HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md`
7. `HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md`
8. `HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md`
9. `HGCDTE_PAIRED_SAMPLE_AB_DIFFERENTIAL_PHASE.md`
10. `HGCDTE_PAIRED_AB_TEMPERATURE_DESIGN.md`
11. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
12. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
13. `RESEARCH_LOG.md`

### Active candidate

> **Use known graded-HgCdTe optical kernels and wavelength × RF complex response to recover a finite set of differential internal timing/transport modes, then validate those modes against the published smooth-gradient sample B and nonlinear-gradient sample A.**

**Status:** CANDIDATE UNDEREXPLORED INVERSE-METROLOGY METHOD — PRIORITY UNPROVEN.

Forward wavelength/depth generation, graded-HgCdTe transport/response modeling, and localized-position transit timing are prior art.

---

## B. Active exact/corrected inverse files

### `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`

**Status:** active exact operator / corrected.

Contains:

```text
downstream collection -> CDF kernel
front collection -> survival kernel
cell-integrated discretization
common-delay boundary gauge.
```

### `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`

**Status:** active conditional extension / corrected.

Contains:

```text
first timing moment -> q1 modes
second timing moment -> q2 modes after generation-position variance subtraction
common broadening gauge
conditional q1=1/v, q2~2D/v^3 interpretation.
```

### `HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`

**Status:** active frequency-domain formulation.

Low-frequency differential phase probes differential mean delay; log-magnitude curvature probes timing variance. Full complex fitting replaces low-order cumulants at higher normalized RF frequency.

---

## C. Published sample-B calibration branch — ACTIVE

### `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`

**Status:** active literature-constrained dimensional model.

Published constraints:

```text
W ~3.7 um
nominal x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
linear-gradient field ~100-200 V/cm.
```

Current central result:

```text
2.80 um -> Pabs~0.998, mean generation depth~0.677 um
3.88 um -> Pabs~0.070, mean generation depth~3.523 um.
```

Thus

```math
\Delta\langle z\rangle\approx2.85\ {\rm um}.
```

At illustrative `v_eff=1e5 m/s`, this is about `28.5 ps` or `10.25 degrees` at `1 GHz`.

Cell-integrated front-kernel singular-mode counts above `[1e-1,1e-2,1e-3,1e-4]`:

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

Interpretation: **few-mode band-limited tomography**.

### `HGCDTE_PUBLISHED_SAMPLE_B_PHASE_PRECISION.md`

**Status:** supporting equal-noise stress test.

Useful as a baseline, but equal wavelength phase noise is no longer the preferred experimental model.

### `HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md`

**Status:** active experimental-covariance correction.

At fixed incident power, near-cutoff phase precision degrades with falling `Pabs`; optical rank is therefore not experimental rank.

### `HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md`

**Status:** active reduced-rank experimental design.

For `3` smooth transport modes + `1` common phase nuisance, D-optimal design uses about four information-rich wavelength bands rather than uniform dense sampling.

### `HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md`

**Status:** active optical-only RF-validity diagnostic.

For deterministic `T=z/v`, current sample-B kernels give the illustrative condition

```math
f_{\max}\approx0.13\,v/W
```

for `|H|>0.98`. This is not a universal device bandwidth.

---

## D. Temperature-control branch — ACTIVE

### `HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md`

**Status:** active sample-B experimental-design result.

Fixed wavelength across temperature is optically confounded because `A=A(T,lambda)`.

Several mid/deep 300 K sample-B kernels can be reproduced at 215 K and 115 K with sub-percent to few-percent full-kernel mismatch by wavelength retuning.

The shallow `2.80 um` 300 K kernel cannot be cleanly reproduced at 115 K inside the spectral region used to establish the current absorption model; do not use the unconstrained short-wave mathematical optimum as a validated prediction.

### `HGCDTE_PAIRED_AB_TEMPERATURE_DESIGN.md`

**Status:** active compatibility correction / OPEN feasibility.

Simultaneous A-B source-phase cancellation requires a **common wavelength**, while independent iso-kernel matching generally gives device-specific wavelengths.

Need a joint common-wavelength schedule

```math
\lambda_*(T)
=\arg\min_\lambda
[w_A\epsilon_A^2+w_B\epsilon_B^2].
```

Feasibility is OPEN until sample A's actual optical/composition profile is recovered.

---

## E. Paired A/B validation branch — ACTIVE

### `HGCDTE_PAIRED_SAMPLE_AB_DIFFERENTIAL_PHASE.md`

**Status:** active measurement protocol.

Same-source simultaneous A-B subtraction cancels arbitrary wavelength-dependent common source phase.

A reciprocal device/arm swap can cancel stable arm/channel asymmetry under the stated reciprocity assumptions.

The paired observable measures **transport contrast**, not either absolute profile.

### Published physical roles

```text
sample B
-> nonlinear interdiffusion region removed
-> weak ~100-200 V/cm linear gradient
-> smooth calibration/control case

sample A
-> part of nonlinear region retained
-> local field near ~2e3 V/cm
-> nonlinear/high-field contrast case.
```

The actual fitted A/B `x(z)` parameters remain unavailable in machine-readable form.

---

## F. Active numerical regressions

```text
numerics/hgcdte_published_sample_b_forward_matrix.py
numerics/hgcdte_published_sample_b_phase_noise.py
numerics/hgcdte_published_sample_b_heteroscedastic_phase.py
numerics/hgcdte_published_sample_b_optimal_design.py
numerics/hgcdte_sample_b_frequency_validity.py
numerics/hgcdte_sample_b_iso_kernel_temperature.py
numerics/hgcdte_spectral_timing_two_moment_inverse.py
```

---

## G. Supporting inverse files

```text
HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md
HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_RESOLUTION.md
HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md
```

These provide general analytic/resolution context. The published-sample Moazzami matrix supersedes the earlier power-law kernel as the active device model.

---

## H. Entrance-gap / ballistic branch — SUPPORTING OR SUPERSEDED

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

## I. Graded-material / tunneling provenance

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

## J. Earlier abstract branches — PROVENANCE ONLY

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

## K. Rejected current branch

### Reverse/sapphire-side illumination

**Status:** REJECTED FOR NOW.

It changes optical kernels but adds little to the strongly conditioned sample-B rank while introducing sapphire/epoxy/passivation dispersion and alignment complexity.

Preferred route remains front illumination + optimized wavelengths + paired A/B differential phase.

---

## L. Hard prior-art boundary

Do not claim novelty for

```text
wavelength-dependent generation depth / bandwidth
graded-HgCdTe forward optical/transport modeling
grading-induced HgCdTe timing improvement
localized-position HgCdTe transit measurement
spectral response revealing spatial collection differences.
```

Unresolved close source:

```text
Potential application of HgCdTe detector with composition gradient in laser measurement
Journal of Applied Optics 45(3), 2024, pp. 549-556
DOI 10.5768/JAO202445.0310009
```

Metadata are confirmed; technical collision remains OPEN because accessible sources do not expose an abstract/full text.

---

## M. Current forward branch

Do **not** add more generic inverse mathematics.

Priority:

1. recover/digitize sample A's `x(z)` profile;
2. build `A_A(T,lambda)` and `A_B(T,lambda)`;
3. test whether useful common joint iso-kernel temperature schedules exist;
4. obtain realistic wavelength × RF-frequency covariance;
5. validate sample B first, then paired A/B transport contrast;
6. read the unresolved 2024 laser-measurement paper before any novelty language;
7. reassess manuscript readiness only after real-data or independently validated inversion.
