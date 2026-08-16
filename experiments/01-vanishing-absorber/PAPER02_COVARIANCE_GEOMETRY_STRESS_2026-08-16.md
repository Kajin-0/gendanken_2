# Paper 02 — covariance geometry stress

**Date:** 2026-08-16  
**Status:** **CHECKED THEORETICAL ROBUSTNESS RESULT / MANUSCRIPT REV. 5 REMAINS FROZEN**  
**Scope:** measurement-covariance geometry only; optical-kernel uncertainty is excluded here and must be treated separately.

## 1. Question

The canonical same-frequency and multi-frequency discrimination calculations assumed independent equal Gaussian noise in every real/imaginary spectral-channel quadrature.

This stress asks whether the Paper-02 conclusions depend qualitatively on that special Euclidean metric.

The forward model is unchanged:

```text
D_micro = 0
recombination = 0
full-contact planar-depletion deterministic stress
same six theoretical wavelength-dependent generation kernels in forward and inverse
```

Only the measurement covariance / generalized-least-squares metric is changed.

The executable calculation is

```text
numerics/paper02_covariance_geometry_stress.py
.github/workflows/paper02-covariance-geometry-stress.yml
```

GitHub Actions evidence:

```text
run      31953328287
job      95180066781
artifact paper02-covariance-geometry-stress
id       9265260013
SHA-256 4a404ed8034287ea87fe128b14b9579ccc4cf8e537d3ba70d913db39d3cb8687
```

The job passed syntax, numerical solve, generalized covariance analysis, summary generation, and artifact upload.

---

## 2. Covariance families

Every same-frequency covariance shape is normalized to unit **mean quadrature variance**, so the channel-SNR definition remains comparable:

```text
S = RMS_m |J_m| / sqrt(mean quadrature variance).
```

Tested families:

1. IID reference;
2. channel equicorrelation, rho = 0.25, 0.50, 0.80;
3. channel AR(1) correlation, rho = 0.25, 0.50, 0.80;
4. rank-one common-channel covariance mode, 10:1 pre-normalization eigenvalue anisotropy;
5. rank-one spectral-slope covariance mode, same anisotropy;
6. rank-one spectral-curvature covariance mode, same anisotropy;
7. real/imaginary quadrature correlation q = -0.50, +0.50.

For the multi-frequency rejection test, each single-frequency marginal root covariance is preserved while standardized root errors are coupled across RF by either AR(1) or equicorrelated frequency covariance with rho = 0.25, 0.50, 0.80.

These are controlled theoretical stress directions, not claimed instrument covariance models.

---

## 3. Generalized metric used in the fit

Let the real-stacked six-complex-channel vector have covariance

```math
\Sigma = \sigma^2 R,
```

and one-mode Jacobian `G` for the six real parameters

```text
Re C, Im C, Re K, Im K, Re r, Im r.
```

The one-mode model is re-fit by generalized least squares for every covariance case; the old IID pseudo-true root is **not** held fixed.

At channel SNR 1,

```math
\operatorname{Cov}(\hat\theta)
=
(G^T\Sigma^{-1}G)^{-1}.
```

The post-fit deterministic alternative contributes noncentrality

```math
\lambda_1
=e^T\Sigma^{-1}e
```

at SNR 1, where `e` is the covariance-weighted post-fit residual. Both positive-`D` detection and one-mode rejection are then scaled to 90% power at `alpha=0.0027` using the same covariance.

This is the executable version of the existing tangent/normal theory: covariance changes the geometry of both parameter bias and model rejection.

---

## 4. Same-frequency result: the qualitative ordering is invariant

### 100 MHz

IID reference:

```text
S_D      = 111.863 dB
S_reject = 102.290 dB
```

so one-mode rejection occurs first.

Across **all** tested covariance shapes:

```text
S_D range      = 104.873 to 121.811 dB
S_reject range =  95.300 to 102.290 dB
hidden-risk cases = 0 / 12
```

The 100-MHz conclusion therefore survives every tested covariance stress:

> the same-frequency one-mode check warns before positive apparent diffusion reaches the stated detection power.

### 500 MHz

IID reference:

```text
S_D      = 70.044 dB
S_reject = 88.192 dB
```

Across all tested covariance shapes:

```text
S_D range      = 63.054 to 79.656 dB
S_reject range = 81.202 to 88.192 dB
hidden-risk cases = 12 / 12
```

Thus positive apparent diffusion remains detectable first in every tested covariance metric.

### 1 GHz

IID reference:

```text
S_D      = 52.413 dB
S_reject = 81.804 dB
```

Across all tested covariance shapes:

```text
S_D range      = 45.423 to 61.097 dB
S_reject range = 74.814 to 82.338 dB
hidden-risk cases = 12 / 12
```

Again the hidden-risk ordering survives every tested covariance metric.

### Checked conclusion

The previous frequency-dependent verdict is therefore robust over this deliberately broad covariance family:

```text
100 MHz: one-mode rejection first
500 MHz: positive-D detection first
1 GHz:  positive-D detection first
```

This is stronger than the Rev.-5 IID-only numerical statement, but it is still conditional on the declared covariance stress family rather than universal.

---

## 5. New result: the pseudo-true effective diffusion is metric-dependent

Although the **ordering** is robust, the fitted pseudo-true `D_eff` is not invariant to the generalized-least-squares metric because the homogeneous model is misspecified.

Across the tested covariance shapes:

```text
100 MHz: D_eff = 1.6602e-3 to 2.6098e-3 m^2/s
500 MHz: D_eff = 1.6577e-3 to 2.5683e-3 m^2/s
1 GHz:   D_eff = 1.6218e-3 to 2.4250e-3 m^2/s
```

The strongest shift is produced by the rank-one **spectral-curvature** covariance direction. At 100 MHz it moves the pseudo-true value from the IID

```text
2.609795e-3 m^2/s
```

to

```text
1.660158e-3 m^2/s,
```

a reduction of about 36%.

By contrast, channel equicorrelation and the common-channel low-rank mode leave the pseudo-true IID `D_eff` essentially unchanged while rescaling the statistical thresholds. This is consistent with those covariance directions acting primarily in channel subspaces already profiled by the one-mode offset/amplitude freedom.

### Interpretation

For a misspecified inverse, an effective parameter is not solely a property of the deterministic data vector. It is also a property of the metric used to define the best approximation.

Thus a reported `D_eff` under model misspecification should be interpreted as

```text
pseudo-true parameter of (forward data, inverse family, weighting/covariance metric),
```

not as a metric-independent material observable.

This is an analytically expected consequence of generalized projection geometry, but the present calculation shows that the magnitude can be large in the Paper-02 stress while the qualitative hidden-risk ordering remains unchanged.

---

## 6. Cross-frequency correlation does not destroy the bandwidth result

The cumulative multi-frequency homogeneous-law test was repeated with standardized root errors correlated across RF while preserving every single-frequency marginal covariance.

Required RMS-channel SNR for the IID reference and the full tested range is:

| Maximum RF | IID required SNR | Range across frequency-correlation stresses |
|---:|---:|---:|
| 200 MHz | 132.851 dB | 128.424–132.851 dB |
| 300 MHz | 121.800 dB | 117.766–121.800 dB |
| 500 MHz | 107.856 dB | 104.227–107.900 dB |
| 750 MHz | 97.576 dB | 93.696–97.825 dB |
| 1 GHz | 90.389 dB | 86.195–90.885 dB |
| 1.5 GHz | 79.922 dB | 75.475–80.356 dB |
| 2 GHz | 73.221 dB | 68.801–74.038 dB |
| 3 GHz | 64.225 dB | 59.872–65.309 dB |

The strongest degradation relative to IID over the tested cumulative bands is only about `+1.08 dB` at 3 GHz. Some correlated cases actually make the wrong law easier to reject because the deterministic departure lies in a low-noise differential direction of that covariance.

Therefore:

> correlation is not intrinsically equivalent to information loss. Rejection power is controlled by the orientation of the deterministic model discrepancy relative to the covariance ellipsoid.

The main Rev.-5 bandwidth conclusion survives this stress: extending usable RF bandwidth strongly lowers the required SNR for rejecting the wrong homogeneous dispersion law.

---

## 7. Exact common-mode invariance worth separating from covariance stress

A scalar complex gain applied equally to all spectral channels at one RF frequency,

```math
J_m \mapsto a J_m,
```

is exactly absorbable into the profiled complex `C,K` parameters of

```math
J_m=C+K F_m(r).
```

Therefore such a common complex gain/phase factor does not by itself change the fitted root `r`. The dangerous calibration directions are channel-dependent directions that overlap the root tangent or alter the kernels/wavelength-to-depth map.

This observation motivates treating optical-kernel uncertainty separately from generic measurement covariance.

---

## 8. What is established and what is not

**CHECKED in the declared theoretical stress:**

- the 100/500/1000-MHz same-frequency ordering survives all tested covariance shapes;
- a misspecified pseudo-true `D_eff` can move substantially when the covariance/weighting metric changes;
- strong common/equicorrelated channel noise need not move the pseudo-true root appreciably;
- cross-frequency correlation can either help or hurt model rejection depending on orientation;
- the strong benefit of extending RF bandwidth survives the tested cross-frequency correlations.

**NOT established:**

- robustness to arbitrary covariance matrices;
- any claim that the tested covariance families represent a specific instrument;
- robustness to optical-kernel misspecification;
- robustness to uncertain wavelength registration, absorber profile, interference, or optical calibration;
- experimental feasibility or experimental validation.

## 9. Next gate

The next scientific stress is **kernel/model uncertainty**, not another covariance sweep.

Linear theory should distinguish:

1. random zero-mean kernel uncertainty, which can be marginalized into an effective covariance;
2. fixed kernel misspecification, which creates deterministic parameter bias and cannot be cured by covariance inflation alone;
3. kernel-nuisance directions tangent to the transport root, which can make `D_eff` poorly identifiable even when same-frequency goodness-of-fit remains excellent.

Rev. 5 remains frozen until that separate gate is completed and its consequence is known.
