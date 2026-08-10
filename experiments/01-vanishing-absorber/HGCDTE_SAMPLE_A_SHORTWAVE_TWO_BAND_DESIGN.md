# Short-Wave Sample-A Contrast — Robust Two-Band Measurement Design

**Date:** 2026-08-09  
**Status:** conditional exhaustive two-wavelength design over the 72-member sample-A profile family; fixed total white-noise averaging resource; illustrative 25% A-localized transport perturbation; smooth-mode calibration priors; no novelty claim

## 1. Why optimize the short-wave scan again?

The preceding short-wave calculation established two facts:

```text
2.00-2.80 um gives much stronger raw leverage on sample A's retained nonlinear region
```

but

```text
the resulting localized spectral response is almost contained in the six-mode smooth A/B transport subspace.
```

Therefore the useful experimental question is no longer simply

> Which wavelengths produce the largest raw phase swing?

It is

> **For a fixed total measurement time and a stated smooth-mode calibration precision, which wavelength pair maximizes the worst-case detectability of an A-localized contrast after the unknown common phase and smooth A/B nuisance modes are accounted for?**

This note answers that narrower two-band design problem exactly on the current `0.01 um` grid.

---

## 2. Reference resource and parameterization

Use the same 300 K short-wave model as

`HGCDTE_SAMPLE_A_SHORTWAVE_CALIBRATION_REQUIREMENT.md`:

```text
lambda = 2.00-2.80 um
step = 0.01 um
81 wavelengths
72 sample-A profile-family members
central sample-B optical envelope
three smooth A transport modes
three smooth B transport modes
one illustrative A-localized nonlinear-region anomaly.
```

The illustrative anomaly remains

```math
v(z)
=10^5\ {\rm m/s}
\left[1-0.25w_A(z)\right],
```

where `w_A(z)` is only a support template derived from the excess nonlinear composition-gradient field.

This is not a prediction that sample A actually has a 25% slowdown.

Each anomaly/nuisance spectral response is normalized to unit RMS over the dense 81-point grid. Smooth-mode prior widths therefore remain **phase-equivalent spectral-mode amplitudes**, not microscopic velocity uncertainties.

The white phase-noise reference is

```math
\sigma_{\phi,0}=0.10^\circ
```

for one unit of coherent integration at one wavelength.

The dense reference scan spends one unit at each of 81 wavelengths, so define the fixed total resource

```math
\boxed{T_{\rm tot}=81\ \text{time units}.}
```

---

## 3. Why a two-band measurement must use equal time

At a given wavelength, simultaneous A-B subtraction removes arbitrary common source phase, but a wavelength-independent differential device/path/electronics phase can remain.

With only two wavelengths `lambda_1` and `lambda_2`, that offset is removed exactly by their phase difference:

```math
\Delta y
=y(\lambda_1)-y(\lambda_2).
```

For white phase variance scaling as `1/t`,

```math
\operatorname{Var}(\Delta y)
=\sigma_{\phi,0}^2
\left(
\frac{1}{t_1}+\frac{1}{t_2}
\right).
```

At fixed

```math
t_1+t_2=T_{\rm tot},
```

the arithmetic-harmonic inequality gives the exact optimum

```math
\boxed{
t_1=t_2=T_{\rm tot}/2.
}
```

Thus the two-band time split is not a numerical coincidence:

> **50/50 time is exactly optimal for the gauge-free two-wavelength phase difference under the stated white-noise model.**

---

## 4. Nuisance-marginalized pair information

Let the normalized anomaly spectral shape be `h(lambda)` and the six normalized smooth nuisance shapes be collected in `n(lambda)`.

For a wavelength pair define

```math
\Delta h
=h(\lambda_1)-h(\lambda_2),
```

```math
\Delta\mathbf n
=\mathbf n(\lambda_1)-\mathbf n(\lambda_2).
```

If each smooth nuisance amplitude has an independent Gaussian prior

```math
b_j\sim\mathcal N(0,\sigma_{\rm prior}^2),
```

then after nuisance marginalization the pair-difference variance is

```math
\boxed{
V_{\rm eff}
=
\frac{4\sigma_{\phi,0}^2}{T_{\rm tot}}
+
\sigma_{\rm prior}^2
\|\Delta\mathbf n\|_2^2.
}
```

The posterior uncertainty of the anomaly RMS amplitude is therefore

```math
\boxed{
\sigma_A
=
\frac{\sqrt{V_{\rm eff}}}{|\Delta h|}.
}
```

For each pair, calculate the anomaly detection SNR for all 72 sample-A profiles and use the robust objective

```math
\boxed{
J(\lambda_1,\lambda_2)
=
\min_{p=1,\ldots,72}
\frac{A_p}{\sigma_{A,p}}.
}
```

The pair search is exhaustive over all

```math
\binom{81}{2}=3240
```

wavelength pairs.

---

## 5. Result with perfectly known smooth nuisance amplitudes

If the six smooth nuisance amplitudes are treated as known exactly,

```text
best pair:
2.00 um / 2.80 um

worst-case SNR:
4.863 sigma

median SNR:
9.496 sigma

all 72 profiles:
>3 sigma.
```

This is the intuitive limit: with no nuisance penalty, maximize the short-wave spectral separation.

The optimum sitting at the `2.00 um` lower bound is important. The present Moazzami optical model should **not** be extrapolated below that bound merely because the mathematical design would like more short-wave leverage.

---

## 6. `0.002 deg` smooth-mode prior

For

```math
\sigma_{\rm prior}=0.002^\circ,
```

the robust optimum becomes

```math
\boxed{
(\lambda_1,\lambda_2)
=(2.00,2.72)\ {\rm um}.
}
```

At the same total time as the 81-point dense reference scan:

```text
worst-case SNR = 4.237
median SNR = 8.066
fraction >=3 sigma = 100%.
```

The second wavelength moves inward from `2.80 um` because the objective is no longer raw anomaly span alone. It balances anomaly contrast against sensitivity to the six calibrated smooth nuisance modes.

---

## 7. `0.005 deg` prior — current useful design point

For

```math
\boxed{
\sigma_{\rm prior}=0.005^\circ,
}
```

the exhaustive optimum is

```math
\boxed{
(\lambda_1,\lambda_2)
=(2.00,2.69)\ {\rm um}.
}
```

with equal time at the two wavelengths.

Across all 72 sample-A profiles:

```text
worst-case SNR = 3.093
median SNR = 5.789
maximum SNR = 10.974
fraction >=3 sigma = 100%.
```

This is the first current design that simultaneously has

```text
full A-profile-family coverage
fixed total time equal to the dense scan
explicit common-phase rejection
explicit smooth-mode calibration uncertainty.
```

### The optimum is not a fragile single-grid-point accident

Pairs within about `1%` of the best worst-case SNR occupy a small neighborhood roughly spanning

```text
short band: 2.00-2.02 um
upper band: 2.66-2.71 um,
```

although not every cross-combination in that rectangle is equally good.

So `2.00 / 2.69 um` should be interpreted as the center of a robust design region on the present model/grid, not as a physically exact wavelength requirement.

---

## 8. Why concentrating time helps

At `sigma_prior=0.005 deg`, the original 81-point dense scan with one time unit at every wavelength gives

```text
worst-case SNR = 2.388.
```

The optimized two-band design with the **same total time** gives

```text
worst-case SNR = 3.093.
```

To make the dense uniform scan reach the same worst-case `3.093 sigma` under this model requires approximately

```math
\boxed{2.31\times}
```

as much total integration time.

Equivalently, the two-band allocation uses about

```math
\boxed{57\%\ \text{less total time}}
```

than uniform dense sampling for the same worst-case significance in this reduced design problem.

This is a conditional resource comparison, not a universal measurement-time saving.

Dense wavelength scans remain valuable during initial model validation and for discovering unmodeled spectral structure.

---

## 9. There is a sharp calibration threshold for the two-band strategy

Continue increasing the independent phase-equivalent smooth-mode prior width and re-optimize the wavelength pair each time.

The largest prior width for which **any** pair on the current grid still guarantees `>=3 sigma` for all 72 profiles is approximately

```math
\boxed{
\sigma_{\rm prior,max}\approx0.00528^\circ.
}
```

Near that threshold the best pair is approximately

```text
2.01 um / 2.69 um.
```

Therefore the `0.005 deg` design point is not arbitrary: it lies just inside the robust two-band feasibility boundary for the current illustrative anomaly and noise model.

---

## 10. `0.010 deg` prior cannot be rescued by pair selection alone

At

```math
\sigma_{\rm prior}=0.010^\circ,
```

the best two-band pair moves slightly to approximately

```text
2.04 um / 2.69 um
```

but reaches only

```text
worst-case SNR = 1.956
median SNR = 3.731
fraction >=3 sigma = 59.7%.
```

Thus

> **better choice of two wavelengths cannot compensate for `0.01 deg` smooth-mode calibration uncertainty under the current model.**

At that point the experiment must improve at least one of

```text
smooth-mode calibration
phase precision
independent physical constraints
or spectral dimensionality beyond a two-band difference.
```

This is a useful negative result because it prevents treating sparse wavelength optimization as a substitute for calibration.

---

## 11. Current experimental interpretation

The emerging architecture is now more specific.

### Mid/deep branch

Use the broader/mid-deep wavelength program to establish

```text
sample-B smooth transport calibration
instrument covariance
RF validity
common-mode cancellation
temperature iso-kernel behavior.
```

### Short-wave contrast branch

Then test the A-specific nonlinear-region contrast with a concentrated short-wave measurement near

```text
~2.00 um
and
~2.69 um,
```

provided the smooth spectral nuisance amplitudes are constrained to roughly the `0.005 deg RMS` phase-equivalent level or better.

The short-wave pair is therefore **not** a replacement for the calibration scan.

It is the efficient follow-up observable once calibration exists.

---

## 12. What is established and what is not

### Established inside the current model

- the exhaustive best **two-band** pair can be computed exactly on the `0.01 um` grid;
- equal time is analytically optimal for a two-wavelength difference under white `1/t` phase variance;
- `2.00/2.69 um` gives worst-case `~3.09 sigma` at a `0.005 deg` smooth-mode prior;
- all 72 current A-profile family members exceed `3 sigma` at that design point;
- the robust two-band feasibility threshold is approximately `0.00528 deg` phase-equivalent prior uncertainty;
- a `0.010 deg` nuisance prior is too loose for a guaranteed two-band detection of the illustrative anomaly.

### Not established

- that sample A actually has the illustrative 25% transport perturbation;
- that real measurement covariance is equal, independent, or exactly white;
- that six smooth nuisance modes are the complete systematic model;
- that `0.005 deg` smooth-mode calibration is experimentally achievable;
- that `2.00/2.69 um` is the globally optimal arbitrary multi-band design;
- that wavelengths below `2.00 um` can be used with the present absorption model;
- that wavelength-dependent differential optical/electrical path phase is negligible;
- manuscript readiness or novelty.

---

## 13. Next collision

Do not simply add more wavelengths by intuition.

The next numerical question should be:

> **If the smooth-mode prior is worse than `~0.005 deg`, can a rigorously optimized three- or few-band design recover enough independent spectral shape to beat the two-band calibration floor at fixed total measurement time?**

If not, the conclusion becomes particularly strong: calibration—not spectral sampling density—is the dominant experimental resource for the A-localized validation test.

Numerical implementation:

`numerics/hgcdte_sample_a_shortwave_two_band_design.py`
