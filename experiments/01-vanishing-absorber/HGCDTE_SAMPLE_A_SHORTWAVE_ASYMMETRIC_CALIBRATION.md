# Short-Wave Sample-A Contrast — Asymmetric A/B Calibration Budget

**Date:** 2026-08-09  
**Status:** conditional convex fixed-time design with separate smooth-mode priors for sample A and sample B; illustrative A-localized anomaly; no novelty claim

## 1. Why split the calibration prior?

The previous global short-wave design assigned one common phase-equivalent prior width to all six smooth nuisance modes:

```text
3 smooth A modes
+
3 smooth B modes.
```

That produced a robust `3 sigma` threshold near

```math
\sigma_{\rm prior}\approx0.00528^\circ
```

when all six modes were given equal priors.

But this does not tell us which calibration matters most.

A tempting experimental interpretation would be

```text
sample B is the control
-> calibrate B extremely well
-> paired A-B data will expose A's nonlinear-region contribution.
```

That is not automatically true because the A-localized anomaly is also nearly degenerate with **sample A's own smooth transport baseline**.

The useful question is therefore:

> **How do the allowable A-smooth and B-smooth prior uncertainties trade against each other?**

---

## 2. Separate prior blocks

Use the same globally optimized fixed-time short-wave Fisher model as

`HGCDTE_SAMPLE_A_SHORTWAVE_GLOBAL_DESIGN.md`.

The parameter vector is

```text
1 A-localized anomaly
3 smooth A nuisance amplitudes
3 smooth B nuisance amplitudes
1 common differential phase.
```

Assign independent Gaussian prior widths

```math
\sigma_A
```

to all three smooth A coefficients and

```math
\sigma_B
```

to all three smooth B coefficients.

The prior-information block is therefore

```math
\boxed{
\mathbf P
=
\operatorname{diag}
\left(
0,
\sigma_A^{-2},\sigma_A^{-2},\sigma_A^{-2},
\sigma_B^{-2},\sigma_B^{-2},\sigma_B^{-2},
0
\right).
}
```

The wavelength-time allocation is re-optimized globally for every `(sigma_A,sigma_B)` pair.

---

## 3. Perfect sample A does not rescue a `0.010 deg` sample-B prior

Set

```text
sample-A smooth modes known exactly
sigma_B = 0.010 deg.
```

The global optimizer gives worst-case significance only

```math
\boxed{2.529\sigma}
```

for the current illustrative anomaly/profile family.

Thus even perfect knowledge of A's smooth baseline cannot compensate for a `0.010 deg` B-mode prior.

---

## 4. Perfect sample B does not rescue a `0.010 deg` sample-A prior

Reverse the test:

```text
sample-B smooth modes known exactly
sigma_A = 0.010 deg.
```

The optimized worst-case significance is only

```math
\boxed{2.502\sigma.}
```

Therefore excellent sample-B calibration by itself is also insufficient.

This is an important correction to the intuitive control-sample story:

> **sample B is necessary, but the sample-A smooth baseline must also be constrained.**

---

## 5. One-sided calibration limits

Find the largest one-device prior width that still permits a globally optimized fixed-time `3 sigma` result when the other device's smooth modes are treated as exactly known.

### A-side limit with B known

```math
\boxed{
\sigma_{A,\max}
\approx0.00740^\circ.
}
```

### B-side limit with A known

```math
\boxed{
\sigma_{B,\max}
\approx0.00757^\circ.
}
```

The limits are similar but not exactly identical because the A and B nuisance spectral shapes are not identical.

Neither side can be allowed to drift to the `0.01 degree` class even if the opposite side were calibrated perfectly.

---

## 6. The A/B calibration trade space is approximately elliptical

The two nuisance blocks contribute independent phase-equivalent variance after marginalization.

Numerically, the robust `3 sigma` boundary is extremely well summarized by

```math
\boxed{
\left(
\frac{\sigma_A}{0.00740^\circ}
\right)^2
+
\left(
\frac{\sigma_B}{0.00757^\circ}
\right)^2
\lesssim1.
}
```

This is a **conditional design law**, not a universal physical relation.

It is a compact approximation to the globally re-optimized Fisher boundary for the current

```text
72-profile A family
illustrative 25% A-localized anomaly
0.10 degree one-unit white phase noise
81-unit total short-wave time budget
3 A + 3 B smooth nuisance modes.
```

---

## 7. Equal calibration recovers the previous threshold

Setting

```math
\sigma_A=\sigma_B=\sigma
```

in the approximate ellipse gives

```math
\sigma
\approx
\left[
\frac1{(0.00740^\circ)^2}
+
\frac1{(0.00757^\circ)^2}
\right]^{-1/2}
\approx0.00529^\circ.
```

This reproduces the independent global optimization result

```math
\sigma_{\rm prior,max}\approx0.00528^\circ.
```

The agreement is a useful internal consistency check.

---

## 8. Practical calibration consequences

The budget can be spent asymmetrically, but there is no free side.

Representative interpretations:

```text
if B is nearly perfect:
A may relax only to ~0.0074 deg

if A is nearly perfect:
B may relax only to ~0.0076 deg

if A and B are comparable:
each must be near ~0.0053 deg or better.
```

Thus improving one side far beyond the `~0.005 deg` class produces diminishing benefit unless the other side improves as well.

This changes the experimental hierarchy from

```text
calibrate B
-> measure A-B
```

into

```text
calibrate instrument
+
constrain B smooth transport
+
constrain A smooth baseline
-> then measure the localized A-B short-wave contrast.
```

---

## 9. Why this matters for identifiability

The paired observable is

```math
\Delta\phi_{AB}
\sim
\mathbf A_A\mathbf q_A
-
\mathbf A_B\mathbf q_B.
```

An A-localized anomaly is not compared against a fixed B curve in isolation.

It competes with

```text
smooth A transport adjustments
and
smooth B transport adjustments.
```

Because both smooth response families overlap strongly with the localized anomaly spectrum, uncertainty on either side can absorb the feature.

That is why the budget adds approximately in quadrature.

---

## 10. What this does not mean

The numbers

```text
0.00740 deg
0.00757 deg
0.00529 deg
```

are not universal instrument specifications.

They depend on the current reduced model and illustrative anomaly amplitude.

They also refer to **normalized smooth spectral phase-mode amplitudes**, not raw single-wavelength phase accuracy, local carrier velocity, or device-to-device manufacturing tolerance.

A real experiment must propagate the actual sample-B and sample-A calibration posterior into these nuisance coordinates.

---

## 11. Next step — translate the mode budget into measurement resources

The calibration target is now structurally clear.

The next question is quantitative:

> **How much coherent phase information is required to estimate each relevant smooth mode at the `~0.005 degree RMS` class, and what integration time / differential drift / wavelength-repeatability limits does that imply?**

An ideal orthogonal-mode lower bound is already informative.

If a normalized spectral mode has RMS one over `N` equal-information wavelengths, independent per-point phase noise `sigma_phi` gives approximately

```math
\sigma_{\rm mode}
\simeq
\frac{\sigma_\phi}{\sqrt N}
```

before nuisance correlations and systematics.

For `N=81`, reaching

```math
\sigma_{\rm mode}\approx0.0053^\circ
```

would require approximately

```math
\sigma_\phi\lesssim0.0475^\circ
```

per equal-information wavelength in this ideal limit, or about `4.4x` the coherent information of the current `0.10 degree`-per-point reference.

That is only a lower bound; the real calibration matrix and covariance must be propagated next.

Numerical implementation:

`numerics/hgcdte_sample_a_shortwave_asymmetric_calibration.py`
