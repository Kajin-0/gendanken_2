# Experiment 01 — Artifact Status Map

**Date:** 2026-08-09  
**Purpose:** keep the active inverse-metrology frontier distinct from supporting, superseded, corrected, and stopped branches.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

There is still **no manuscript**.

---

## A. Canonical active frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
4. `HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md`
5. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
6. `HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`
7. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_RESOLUTION.md`
8. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
9. `HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`
10. `HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md`
11. `RESEARCH_LOG.md`

### Active candidate

Use a known monotonic graded `E_g(x)` / optical generation profile as an internal spectral position encoder and solve measured wavelength-resolved timing data as an inverse problem for internal transport.

Mean-delay inverse:

```math
\boxed{
\mu_i
=\int_0^L K_i(s)q_1(s)ds,
\qquad
K_i(s)=P(X_g\le s|E_{\gamma,i},{\rm abs}).
}
```

Discretely:

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q_1+c_1\mathbf1.
}
```

Optional second-moment inverse:

```math
\boxed{
\sigma_i^2
=\int_0^L K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].
}
```

Status:

**CANDIDATE UNDEREXPLORED INVERSE-METROLOGY METHOD — PRIORITY UNPROVEN.**

The forward wavelength/depth generation and graded-HgCdTe timing physics are already prior art.

---

## B. Active inverse-metrology files

### `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`

**Status:** active exact linear inverse under path-additive mean delay.

Role: derives the full finite-depth operator and common-delay nuisance parameter.

### `HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md`

**Status:** active finite-optical-depth analytic kernel result.

Role: shows that the timing derivative measures a kernel-averaged inverse velocity and identifies the optical point-spread scale.

### `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`

**Status:** active conditional extension.

Role: separates mean transport density from timing-broadening density using the law of total variance.

### `HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`

**Status:** active experimental implementation note.

Role: maps wavelength-dependent complex RF response to timing cumulants and shows how common wavelength-independent electronics can cancel or be fitted.

### `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_RESOLUTION.md`

**Status:** active resolution budget.

Role: tracks optical-kernel width, wavelength resolution, gap-profile uncertainty, timing/phase precision, and inverse conditioning.

### `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`

**Status:** active hard claim boundary.

Role: records strong prior-art collisions including wavelength-dependent transit physics, localized-position HgCdTe timing, and the 2022 graded-HgCdTe forward model.

### `HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`

**Status:** active real-device validation proposal.

Role: identifies the 2022/2023 VPE graded-HgCdTe structures as experimentally adjacent test cases without inventing missing profile parameters.

---

## C. Active numerical regressions

```text
numerics/hgcdte_spectral_timing_linear_inverse.py
numerics/hgcdte_spectral_timing_kernel_tomography.py
numerics/hgcdte_spectral_timing_svd_resolution.py
numerics/hgcdte_spectral_timing_two_moment_inverse.py
numerics/hgcdte_spectral_momentum_scattering_surrogate.py
```

Interpretation:

- synthetic nonuniform mean-delay profiles can be reconstructed in controlled cases;
- separate synthetic timing-broadening regions can be reconstructed in the two-moment case;
- optical-kernel broadening sharply reduces recoverable spatial modes;
- extreme-cutoff kernel truncation can invalidate naive point inversion.

These are **conditioning checks only**, not experimental performance claims.

---

## D. Entrance-gap crossover branch — supporting, not headline

### `HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md`

**Status:** active supporting geometry.

Role: below `E_g,in`, photon energy primarily moves the first allowed generation position; above `E_g,in`, generation is pinned and photon energy changes the injected carrier state.

This is the physical reason the wavelength sweep has spatial encoding power below the entrance gap and hot-carrier diagnostic power above it.

### `HGCDTE_SPECTRAL_DRIFT_DIFFUSION_ROBUSTNESS.md`

**Status:** supporting correction.

Role: shows that strong momentum randomization gives rise -> plateau, not a universal peak.

### `HGCDTE_SPECTRAL_MOMENTUM_SCATTERING_SURROGATE.md`

**Status:** supporting adversarial stress test.

Role: shows that post-crossover decline/plateau/rise depends on momentum-memory assumptions.

---

## E. Ballistic timing-peak branch — SUPERSEDED AS UNIVERSAL CLAIM

Retain:

```text
HGCDTE_SPECTRAL_DELAY_PEAK.md
HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md
HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md
numerics/hgcdte_spectral_delay_peak.py
numerics/hgcdte_spectral_delay_relaxation.py
```

These remain valid inside their directed-ballistic / mean-energy assumptions.

Do **not** present the entrance-gap timing maximum as transport independent.

---

## F. Photoexcitation correction files

Retain:

```text
HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md
HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md
HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md
HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md
```

Important permanent correction:

> downstream-generated photoelectrons are not generally cold; excess photon energy must be included before assigning carrier momentum/energy.

Do not equate excess energy to persistent forward longitudinal velocity without a scattering model.

---

## G. Graded-HgCdTe material branch — supporting architecture

Retain as active provenance:

```text
HGCDTE_LINEAR_GRADED_KANE_WKB.md
HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md
HGCDTE_GRADED_POISSON_ROBUSTNESS.md
HGCDTE_BOUNDARY_LAYER_TAT_TRADEOFF.md
HGCDTE_ELECTROSTATIC_COMPENSATION_PEAK_FIELD_BOUND.md
HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md
HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md
HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md
HGCDTE_GRADED_RELAXATION_SPEED_CEILING.md
HGCDTE_GRADED_ABSORBER_BOUNDARY_PHASE_MAP.md
```

These files explain why composition grading is physically interesting, but they are no longer the immediate publication frontier.

---

## H. Earlier abstract branches — provenance only

Retain but do not restart without a new reason:

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

These establish how the original universal-bound program progressively failed or narrowed.

---

## I. Hard prior-art boundary

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

Its metadata are confirmed, but the full technical paper has not been recovered in the current search.

---

## J. Current forward branch

Do not add more generic inverse mathematics.

Next work:

1. recover a dimensional published `x(z)` / `E_g(z)` profile;
2. obtain/calibrate `alpha(z,lambda)`;
3. build the real optical timing matrix `A`;
4. predict differential phase/magnitude versus wavelength and modulation frequency;
5. quantify recoverable singular modes and required phase precision;
6. compare the reconstructed transport profile against localized excitation or validated transport simulation;
7. read the 2024 laser-measurement paper before any novelty claim;
8. reassess publication readiness only after real-device inversion or experimental validation.
