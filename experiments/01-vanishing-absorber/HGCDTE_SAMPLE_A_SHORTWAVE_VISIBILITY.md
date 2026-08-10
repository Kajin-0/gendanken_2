# Sample-A Nonlinear-Region Visibility — The Mid/Deep Scan Is Nearly Blind Near the Junction, but a 2.0–2.8 µm Contrast Scan Recovers Leverage

**Date:** 2026-08-09  
**Status:** conditional spectral-visibility calculation over the 72-member sample-A profile family; nonlinear composition-gradient field is used only as a spatial support template; illustrative transport amplitude; no novelty claim

## 1. The collision

The sample-A validation strategy has focused increasingly on the retained nonlinear/high-field composition region because the 2023 experiment attributes the A/B photoelectric difference to that structure.

But the inverse has a known boundary gauge:

```math
S_i(0)=1
```

for every wavelength in front collection.

Therefore transport located close enough to the collecting junction contributes almost the same delay to every wavelength and is difficult to distinguish from a wavelength-independent device delay.

The crucial question is therefore:

> **Does the wavelength band currently used for the sample-B few-mode inverse actually have enough spectral leverage on sample A's retained nonlinear region?**

The answer for the current `2.8-3.83 um` band is largely **no**.

A shorter-wave scan changes that conclusion.

---

## 2. Use the published gradient field only to define where the nonlinear region is

For each of the 72 sample-A composition sensitivity profiles, calculate the composition-gradient field from the published fit law.

Let

```math
F_{\rm lin}
```

be that profile's fitted linear-region field.

Define a nonnegative spatial support function

```math
\boxed{
w_A(z)
\propto
\left[F_{\rm grad}(z)-F_{\rm lin}\right]_+.
}
```

Normalize its peak to one.

This is **not** a transport law.

The calculation does not assume

```text
velocity proportional to field
```

or

```text
delay proportional to field.
```

`w_A(z)` is used only to identify the part of the processed layer associated with the nonlinear-gradient excess.

Across the 72-profile family:

```text
support centroid:
~0.46-1.43 um from the collecting junction
median ~0.88 um

90% cumulative support depth:
~1.03-2.65 um
median ~1.76 um.
```

Thus the physically interesting A-specific region is concentrated near the boundary where the differential timing operator is least sensitive.

---

## 3. Direct visibility of that region in the current band is extremely small

For each profile, build the `2.8-3.83 um` front-collection timing matrix and remove its common wavelength mode:

```math
\mathbf A_\Delta
=\mathbf A-\mathbf1\overline{\mathbf A}.
```

For spatial cell `j`, define a relative spectral visibility

```math
\boxed{
V_j
=\frac{\|\mathbf A_{\Delta,:,j}\|_2}
{\max_k\|\mathbf A_{\Delta,:,k}\|_2}.
}
```

Then average this visibility over the nonlinear-field support `w_A`.

Across the A-profile family, the field-support-weighted visibility is only

```math
\boxed{
0.0025\text{-}0.0430
}
```

with median

```math
\boxed{0.0089.}
```

In other words, the current mid/deep spectral operator gives the retained nonlinear region typically **less than 1% of the maximum differential spatial leverage available elsewhere in the layer**.

This is the common-delay gauge made concrete on the published sample-A geometry.

---

## 4. Put the visibility on the same phase scale as the previous inverse tests

For comparison only, impose an illustrative perturbation

```math
\boxed{
v(z)
=10^5\ {\rm m/s}
\left[1-0.25w_A(z)\right].
}
```

Thus the nonlinear support contains up to a `25%` slowdown relative to the same `1e5 m/s` baseline used in the sample-B stress tests.

This is **not** a prediction of sample A.

A speedup of comparable inverse-delay magnitude would generate the same order of differential phase with opposite sign.

At `1 GHz`, the current `2.8-3.83 um` band produces only

```text
phase RMS:
0.00046-0.01162 deg
median 0.00420 deg

phase peak-to-peak:
0.00233-0.04687 deg
median 0.01731 deg.
```

That is below the current `~0.1 degree` differential-phase precision target for every member of the profile family.

So the mid/deep scan is **not** the correct first wavelength band for testing an A-specific transport change concentrated in the retained nonlinear region.

---

## 5. The reason shorter wavelengths help

At 300 K, the local band-edge coordinate selected by photon wavelength moves toward higher Cd composition as wavelength decreases.

Using the current Hansen gap relation:

```text
2.8 um -> x_edge ~0.4125
2.6 um -> x_edge ~0.4373
2.4 um -> x_edge ~0.4660
2.2 um -> x_edge ~0.4993
2.0 um -> x_edge ~0.5385.
```

The current `2.8 um` short-wave anchor therefore cannot generate carriers in any part of sample A with local composition much above `x~0.41`.

But the retained nonlinear region extends to substantially higher composition in many of the profile-family realizations.

Moving toward `2.0 um` shifts the first allowed generation position progressively toward the collecting boundary and into the nonlinear-gradient region.

This is exactly the spectral-position-encoding mechanism the inverse requires.

---

## 6. Short-wave phase leverage rises by more than an order of magnitude

Repeat the same illustrative `25%` support-shaped perturbation while progressively extending the wavelength scan downward.

### `2.4-2.8 um`

```text
phase peak-to-peak:
0.0329-0.1723 deg
median 0.0627 deg.
```

### `2.2-2.8 um`

```text
phase peak-to-peak:
0.0637-0.2934 deg
median 0.1305 deg.
```

### `2.0-2.8 um`

```math
\boxed{
\Delta\phi_{\rm pp}
=0.1081\text{-}0.3706^\circ
}
```

with median

```math
\boxed{0.2110^\circ.}
```

Thus every member of the current 72-profile family exceeds approximately `0.108 degree` peak-to-peak for this illustrative anomaly when the scan reaches `2.0 um`.

Compared with the current mid/deep band, the median peak-to-peak signal rises from

```text
~0.017 deg
```

to

```text
~0.211 deg,
```

or approximately a **12-fold increase**.

This is a wavelength-selection effect, not a change in the imposed transport perturbation.

---

## 7. The short-wave A/B contrast is unusually favorable optically

The `2.0-2.8 um` band also avoids the near-cutoff absorbed-signal collapse that complicates the mid/deep inverse.

### Sample A

Across the 72-profile family:

```text
Pabs(2.0 um) >0.99999
Pabs(2.8 um) >0.997.
```

Its mean generation depth moves strongly:

```text
2.0 um:
0.48-2.83 um
median ~1.50 um

2.8 um:
1.72-4.38 um
median ~3.33 um.
```

The median generation-depth shift is therefore approximately

```math
\boxed{1.83\ {\rm um}.}
```

### Sample B

The same band remains almost completely absorbed:

```text
Pabs(2.0 um) ~0.99996
Pabs(2.8 um) ~0.99772.
```

But B's mean generation depth moves only

```text
0.380 -> 0.677 um,
```

or

```math
\boxed{0.296\ {\rm um}.}
```

Thus the common short-wave scan naturally produces

```text
sample A:
large internal generation-position sweep through the retained nonlinear region

sample B:
comparatively shallow, weakly moving generation distribution

both devices:
near-unity absorbed fraction.
```

That is an unusually clean geometry for a paired A/B transport-contrast measurement.

---

## 8. This changes the experimental architecture

The project should no longer assume that one wavelength band serves every scientific purpose.

The optical physics now suggests **two complementary spectral regimes**.

### Mid/deep band — sample-B tomography and temperature control

Approximately

```text
3.4-4.0 um
```

with the current strongest temperature reference near

```text
300 K: 3.632 um
215 K: ~3.793 um
115 K: ~4.005 um.
```

Use this band for

```text
sample-B few-mode calibration
mid/deep transport modes
iso-kernel temperature comparisons
optical-model validation.
```

### Short-wave band — sample-A nonlinear-region contrast

Approximately

```text
2.0-2.8 um
```

at 300 K under the current absorption model.

Use this band to

```text
move the A generation boundary through the retained nonlinear/high-field region
keep both A and B strongly absorbing
maximize A-specific differential phase leverage
use B as a shallow control.
```

The two bands answer different questions and should not be forced into one D-optimal design.

---

## 9. Important model-range boundary

The current Moazzami above-gap absorption fit was established over approximately

```text
600-5000 cm^-1,
```

so

```math
\lambda=2.0\ {\rm um}
```

is at the short-wavelength edge of the presently validated spectral range.

Therefore

```text
2.0 um is usable as a boundary stress point
```

but the project should **not** extend below `2.0 um` using the same absorption formula without additional validation.

This matters because the very highest-Cd/frontmost parts of some sample-A family members would require wavelengths shorter than `2 um` for direct local-gap encoding.

The present result therefore establishes strong leverage on a substantial part of the nonlinear region, not guaranteed pointwise access to its entire high-Cd extreme.

---

## 10. Relation to the common-delay gauge

This result is not an escape from the gauge by mathematics.

It is a physical change in the experiment.

At wavelengths too long to generate inside the near-junction nonlinear region, every generated carrier traverses that region and its delay contribution is nearly wavelength independent:

```text
nonlinear-region delay
-> common mode
-> spectrally unidentifiable.
```

At sufficiently short wavelengths, the first allowed generation point itself moves through the nonlinear region:

```text
some wavelengths generate before a local segment
other wavelengths generate after it
-> that segment enters/leaves the path weighting
-> differential visibility returns.
```

That is exactly what the spectral encoder was supposed to do.

---

## 11. Claim boundary

### DERIVED / GEOMETRIC

A front-boundary transport perturbation becomes spectrally invisible when all retained wavelength kernels approach the same survival probability there.

Shorter wavelengths can restore differential leverage by moving the generation boundary into that region.

### CHECKED NUMERICALLY / CONDITIONAL

For the 72-member sample-A profile family, current Hansen/Moazzami Beer-Lambert optics, and the field-excess support template:

- nonlinear support centroid is approximately `0.46-1.43 um` from the junction;
- current `2.8-3.83 um` support-weighted relative visibility is only `~0.0025-0.043`;
- an illustrative 25% support-shaped perturbation gives only `~0.0023-0.0469 deg` p-p at 1 GHz in that band;
- the same perturbation gives `~0.108-0.371 deg` p-p in a `2.0-2.8 um` scan;
- sample-A median generation depth shifts by about `1.83 um` across `2.0-2.8 um`, while sample B shifts by only about `0.30 um`;
- both samples remain nearly fully absorbing across that short-wave band in the current model.

### NOT ESTABLISHED

- actual A transport perturbation magnitude or sign;
- transport proportionality to composition-gradient field;
- exact real sample-A profile;
- interference-aware short-wave kernels;
- optical model validity below `2.0 um`;
- achievable phase covariance across the full `2-4 um` source range;
- novelty / priority.

---

## 12. Next decisive work

The strongest next experiment/model is no longer a single broad wavelength scan.

It should be designed explicitly as

```text
A. short-wave A/B contrast scan:
~2.0-2.8 um
-> target retained sample-A nonlinear region

B. mid/deep calibration/temperature scan:
~3.4-4.0 um
-> sample-B few-mode inverse + iso-kernel temperature control.
```

Next calculations should therefore:

1. optimize a sparse short-wave wavelength set for an A-localized nonlinear-region contrast mode;
2. propagate realistic phase covariance over `2.0-2.8 um` rather than reusing near-cutoff noise scaling;
3. test interference/reflection sensitivity in the short-wave band, where absorption is high and coherent return should be weaker;
4. quantify how smooth-mode calibration uncertainty limits recovery of the A-localized contrast template;
5. retain the mid/deep temperature schedule as a separate controlled perturbation rather than the primary localizer of the nonlinear region.

This is currently a more physically aligned experiment than forcing the A high-field test through the sample-B-optimized mid/deep scan.

---

## 13. Reproducibility

Deterministic regression:

`numerics/hgcdte_sample_a_shortwave_visibility.py`
