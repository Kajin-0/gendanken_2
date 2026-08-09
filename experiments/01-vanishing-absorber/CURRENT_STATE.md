# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is **few-mode wavelength × frequency inverse metrology** of internal transport in a real graded-HgCdTe geometry; no novelty claim

## 1. Current question

The original active-volume hypothesis and the later universal entrance-gap timing-peak interpretation are both stopped branches.

The active detector-specific question is now:

> **Can a known graded HgCdTe composition profile act as an internal spectral encoder so wavelength-resolved complex response data recover a small number of useful internal carrier-transport modes without physically scanning the excitation position?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
2. `HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
3. `HGCDTE_PUBLISHED_SAMPLE_B_PHASE_PRECISION.md`
4. `HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
5. `HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`
6. `HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
7. `HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`
8. `CLAIM_LEDGER.md`
9. `RESEARCH_LOG.md`
10. `ARCHIVE_STATUS.md`

Older ballistic timing-peak files and normalized inverse tests are supporting provenance only.

---

## 3. Prior-art boundary

Do **not** claim novelty for

- wavelength-dependent generation depth;
- wavelength-dependent detector bandwidth / response time;
- composition-gradient carrier transport;
- graded HgCdTe spectral response;
- wavelength- and depth-dependent graded-HgCdTe generation models;
- graded-HgCdTe response-time modeling;
- localized-position HgCdTe transit measurements.

The 2022 Sang et al. paper already combines wavelength/depth-dependent generation with a graded-HgCdTe forward transport/response model.

The 2009 Perrais et al. work already measures HgCdTe timing as a function of localized generation position.

A 2024 same-group paper titled `Potential application of HgCdTe detector with composition gradient in laser measurement` remains an unresolved close collision.

Current status:

> **candidate underexplored inverse-metrology method; priority unproven.**

---

## 4. Correct orientation-dependent linear inverse

Let

```math
p_i(x)=p(x|\lambda_i,{\rm abs})
```

be the known conditional generation density and

```math
q_1(x)
```

the path-additive mean-delay density.

### Collection at `L`

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

### Collection at `0`

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

The 2023 sample-B device is a **front-collection** case because its junction is at the high-Cd end and long-wave carriers are generated deeper toward the low-Cd side.

Discretely,

```math
\boxed{
\mathbf T=\mathbf A\mathbf q_1.
}
```

Under a local path-additive interpretation,

```math
q_1=1/v_{\rm eff}.
```

The orientation correction is now canonical.

---

## 5. Common-delay identifiability correction

A wavelength-independent delay cannot generally be separated from arbitrary boundary-localized internal delay density by wavelength data alone.

At the collecting boundary the timing kernel tends to unity for every wavelength.

Therefore

```math
\mathbf T^{\rm meas}
=\mathbf A\mathbf q+c\mathbf1
```

has a gauge-like ambiguity unless additional information is supplied.

The safe observable is **differential transport structure**.

Use one of

```text
differential timing / phase
independent common-delay calibration
boundary transport prior
lower-dimensional physical parameterization.
```

Earlier synthetic recovery of a fitted common constant was regularization dependent and is not structural identifiability evidence.

---

## 6. Published 2023 sample-B dimensional model

Primary sample facts from Xu et al. 2023:

```text
processed thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
linear-gradient field ~100-200 V/cm across the reported temperature set.
```

The exact machine-readable 300 K `x(z)` fit parameters are unavailable, so the current dimensional model is a literature-constrained envelope.

Use

```math
x_{\rm low}=0.316
```

as a conditional nominal low-Cd endpoint and bracket the retained linear field by

```math
F_g=100,150,200\ {\rm V/cm}.
```

With the correct Hansen relation,

```math
E_{g,\rm low}(300K)=0.312314\ {\rm eV},
```

```math
\lambda_{g,\rm low}=3.9699\ {\rm um}.
```

The inferred high-Cd endpoints are

```text
100 V/cm -> x_high=0.34348 -> lambda_g,high=3.5494 um
150 V/cm -> x_high=0.35721 -> lambda_g,high=3.3708 um
200 V/cm -> x_high=0.37091 -> lambda_g,high=3.2094 um.
```

Thus sample B plausibly supplies an internal local-gap coordinate spanning approximately

```math
\boxed{3.2\text{-}3.55\ {\rm um}\to3.97\ {\rm um}.}
```

---

## 7. Real HgCdTe absorption model

The dimensional forward matrix now uses Moazzami et al. 2005:

```math
\boxed{
\alpha(E,x,T)
=K(x,T)
\left(\frac{E-E_g}{E}\right)^{n(x,T)},
\qquad E>E_g,
}
```

with their published composition/temperature-dependent `K` and `n`.

The model was fitted over approximately

```text
x=0.22-0.60
T=40-300 K.
```

Current simplifications:

```text
no Urbach tail
no reflection/interference
no free-carrier optical correction
single-pass absorption.
```

---

## 8. Dimensional generation-depth result

For the central `150 V/cm` profile:

| wavelength | single-pass absorbed fraction | conditional mean depth | RMS generation width |
|---:|---:|---:|---:|
| 2.80 um | 0.998 | 0.677 um | 0.621 um |
| 3.20 um | 0.975 | 1.155 um | 0.860 um |
| 3.37 um | 0.917 | 1.704 um | 0.896 um |
| 3.50 um | 0.786 | 2.369 um | 0.703 um |
| 3.70 um | 0.417 | 3.088 um | 0.383 um |
| 3.85 um | 0.115 | 3.459 um | 0.161 um |
| 3.88 um | 0.070 | 3.523 um | 0.120 um |

Therefore the conditional mean generation depth shifts by about

```math
\boxed{2.85\ {\rm um}}
```

between `2.80` and `3.88 um` while retaining at least several-percent single-pass absorption.

For an illustrative

```math
v_{\rm eff}=10^5\ {\rm m/s},
```

this corresponds to

```math
\Delta T\approx28.5\ {\rm ps}
```

or about

```math
\boxed{10.25^\circ}
```

of differential phase at `1 GHz`.

This is a measurement scale, not a sample-B velocity prediction.

---

## 9. Real-matrix spatial rank

Use an 80-cell discretization, `0.01 um` wavelength steps, and keep only wavelengths with

```math
P_{\rm abs}\ge0.05.
```

The cell-integrated front-collection matrix gives:

| field | modes >1e-1 | modes >1e-2 | modes >1e-3 | modes >1e-4 |
|---:|---:|---:|---:|---:|
| 100 V/cm | 2 | 5 | 10 | 20 |
| 150 V/cm | 2 | 5 | 10 | 21 |
| 200 V/cm | 2 | 5 | 11 | 23 |

The exact field bracket moves the wavelength coordinate but barely changes the inverse conditioning.

The robust conclusion is

> **sample B supports a few-mode, band-limited transport tomography rather than a point-by-point depth reconstruction.**

The relative singular thresholds are diagnostics, not universal experimental resolution claims.

---

## 10. Phase-noise stress test

A transparent synthetic anomaly was imposed on the central sample-B matrix:

```text
baseline v = 1e5 m/s
25% local slowdown
center = 2.30 um
Gaussian sigma = 0.35 um.
```

This produces only

```math
\boxed{0.935^\circ}
```

peak-to-peak **residual anomaly phase** at `1 GHz` after the smooth baseline/common mode is removed.

### Three-mode inversion

Noiseless projection:

```text
peak location ~2.336 um
peak amplitude ~66% of true
full-profile truncation error ~40%.
```

At `0.10 degree` independent phase noise per wavelength:

```text
median noise error vs recoverable 3-mode target ~17.5%
90% peak-location error ~0.13 um.
```

At `0.25 degree`, localization degrades strongly.

### Five-mode inversion

Noiseless projection improves amplitude recovery to about `86%`, but the fifth mode is highly noise sensitive.

At `0.10 degree` phase noise the five-mode reconstruction is already noise dominated for this anomaly.

Therefore the first realistic experimental target is approximately

```math
\boxed{3\text{-}4\ \text{smooth differential transport modes},}
```

not a high-resolution velocity curve.

---

## 11. Two timing moments

For the correct orientation-specific kernel `K_i`, additive conditional timing cumulants give

```math
\boxed{
\mu_i=\int K_iq_1,
}
```

```math
\boxed{
\sigma_i^2
=\int K_iq_2
+\operatorname{Var}_{p_i}[m(X)].
}
```

After the optical generation-position variance is removed, the same spatial matrix acts on `q_2`.

In a local high-Peclet drift-diffusion approximation only,

```math
q_1=1/v,
```

```math
q_2\simeq2D/v^3.
```

Common first- and second-cumulant offsets have the same boundary/gauge ambiguity and require calibration or differential treatment.

---

## 12. Current scientific interpretation

The active idea should now be stated as

```text
known graded composition profile
+
known wavelength-dependent optical kernels
+
complex RF response versus wavelength
->
recover a finite set of differential internal transport modes.
```

Not:

```text
wavelength gives an exact generation point
-> exact local velocity.
```

The actual optical physics imposes substantial spatial smoothing.

---

## 13. What remains missing

### Experimental / primary-data inputs

- actual fitted sample-B `x(z)` parameters or digitized/raw composition profile;
- realistic reflection/interference/Urbach corrections if needed;
- wavelength-resolved complex response data;
- instrument/source phase covariance versus wavelength and RF frequency;
- independent validation data.

### Prior-art input

- full technical content of the 2024 `Potential application ... in laser measurement` paper.

### Transport interpretation

- calibrated mapping from reconstructed `q_1,q_2` modes to microscopic HgCdTe `v,D`, scattering, field, or interface physics.

---

## 14. Next decisive work

Do **not** derive another abstract inverse theorem.

Next priority:

1. obtain/digitize the real 2023 sample-B `x(z)` curve;
2. build an instrument-level covariance model for tunable-MWIR differential phase/magnitude;
3. use multiple RF frequencies to fit the full complex response rather than one phase point;
4. compare the recovered modes against localized-position timing or validated transport simulation;
5. only then reassess publication significance.
