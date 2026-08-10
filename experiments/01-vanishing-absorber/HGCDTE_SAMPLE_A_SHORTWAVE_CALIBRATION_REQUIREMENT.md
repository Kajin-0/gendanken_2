# Short-Wave Sample-A Contrast — Smooth-Mode Calibration Requirement

**Date:** 2026-08-09  
**Status:** conditional Fisher/identifiability calculation over the 72-member sample-A profile family; illustrative 25% A-localized transport perturbation; equal independent phase-noise model; no novelty claim

## 1. Why raw short-wave phase amplitude is not enough

The `2.0-2.8 um` calculation substantially improved visibility of sample A's retained nonlinear/high-field region:

```text
illustrative 25% support-shaped perturbation
-> 0.108-0.371 deg peak-to-peak at 1 GHz
-> median ~0.211 deg.
```

That is much larger than the same perturbation produces in the mid/deep scan.

But paired data are still

```math
\Delta\phi_{AB}
=-\Omega
\left(
\mathbf A_A\mathbf q_A
-
\mathbf A_B\mathbf q_B
\right)
+\cdots.
```

Therefore an A-localized phase pattern can be confused with ordinary smooth transport changes in either A or B.

The decisive question becomes:

> **How tightly must the smooth A/B transport contribution be calibrated before the short-wave A-localized contrast is statistically identifiable?**

---

## 2. Parameterization

Use at 300 K

```text
lambda = 2.00-2.80 um
spacing = 0.01 um
N = 81 wavelengths.
```

For every one of the 72 sample-A profile-family members:

1. build the short-wave sample-A timing matrix;
2. build the central sample-B timing matrix;
3. remove wavelength-independent phase;
4. retain the first three smooth transport modes of A;
5. retain the first three smooth transport modes of B;
6. add one A-localized anomaly response.

The illustrative A anomaly remains

```math
\boxed{
v(z)
=10^5\ {\rm m/s}
\left[1-0.25w_A(z)\right],
}
```

where `w_A(z)` is only the normalized nonlinear-gradient-field excess **support template**.

This is not a claim that

```text
sample A actually slows by 25%
```

and it is not a claim that carrier velocity is proportional to composition-gradient field.

---

## 3. Phase-equivalent nuisance coordinates

Let the seven spectral response columns be

```text
1 A-localized anomaly
+
3 smooth A modes
+
3 smooth B modes.
```

After common-phase projection, normalize every spectral column to unit RMS over the 81 wavelengths.

Then each coefficient has units of

```text
degrees RMS spectral phase.
```

This is important.

A nuisance prior such as

```math
\sigma_{\rm prior}=0.01^\circ
```

means that the calibrated uncertainty in each smooth-mode **spectral phase amplitude** is `0.01 deg RMS` across the short-wave wavelength grid.

It is **not** directly a `0.01 deg` uncertainty in a local carrier velocity or delay density.

---

## 4. Fisher model

Use a provisional equal independent per-wavelength phase noise

```math
\sigma_\phi=0.10^\circ.
```

Let

```math
\mathbf X
=
[\mathbf h_A,
 \mathbf n_{A1},\mathbf n_{A2},\mathbf n_{A3},
 \mathbf n_{B1},\mathbf n_{B2},\mathbf n_{B3}]
```

contain the normalized spectral shapes.

The data Fisher matrix is

```math
\mathbf F_{\rm data}
=\frac{\mathbf X^T\mathbf X}{\sigma_\phi^2}.
```

Give each of the six nuisance coefficients an independent Gaussian prior of width `sigma_prior`:

```math
\boxed{
\mathbf F
=\mathbf F_{\rm data}
+\operatorname{diag}
\left(
0,
\sigma_{\rm prior}^{-2},\ldots,
\sigma_{\rm prior}^{-2}
\right).
}
```

The posterior uncertainty in the A-localized phase-RMS amplitude is

```math
\boxed{
\sigma_A
=\sqrt{(\mathbf F^{-1})_{00}}.
}
```

---

## 5. The anomaly spectral shape is almost contained in the smooth A/B subspace

The principal angle from the physical A-localized anomaly response to the six-dimensional smooth A/B nuisance subspace is only

```math
\boxed{
0.0063^\circ\text{-}0.708^\circ
}
```

across the 72 sample-A profiles, with median

```math
\boxed{0.029^\circ.}
```

This is an extremely strong degeneracy.

The short-wave scan solves the earlier **raw visibility** problem but does not, by itself, solve the **model separation** problem.

A localized nonlinear-region response can be reproduced very closely by a suitable combination of ordinary smooth A and B transport modes.

Thus:

> **short-wave wavelength leverage and sample-B/smooth-mode calibration are both required.**

---

## 6. Physical signal scale for the illustrative anomaly

At 1 GHz the same 25% support-shaped perturbation has spectral phase RMS

```math
\boxed{
0.0315^\circ\text{-}0.1206^\circ
}
```

with median

```math
\boxed{0.0651^\circ.}
```

across the profile family.

This RMS amplitude, rather than peak-to-peak phase, is the signal coordinate used in the Fisher calculation.

---

## 7. If smooth nuisance modes were known perfectly

With six nuisance coefficients fixed by perfect prior calibration, only one normalized anomaly amplitude remains.

For `N=81` equal-noise wavelengths,

```math
\sigma_A
=\frac{0.10^\circ}{\sqrt{81}}
=0.01111^\circ.
```

The illustrative anomaly then gives detection significance

```text
minimum  ~2.83 sigma
median   ~5.86 sigma
maximum ~10.85 sigma.
```

Approximately

```math
\boxed{91.7\%}
```

of the 72 profile-family members exceed `3 sigma`.

This establishes an important lower-level result:

> even with perfect smooth-mode knowledge, `0.10 deg` per-wavelength precision is just slightly too weak to guarantee `3 sigma` for the least favorable profile in the present family.

---

## 8. Detection degrades rapidly with smooth-mode uncertainty

At the same

```math
\sigma_\phi=0.10^\circ
```

per wavelength:

| nuisance prior per smooth mode | posterior anomaly sigma | detection SNR range | median SNR | fraction `>=3 sigma` |
|---:|---:|---:|---:|---:|
| known | 0.01111 deg | 2.83-10.85 | 5.86 | 91.7% |
| 0.005 deg | ~0.01317 deg | 2.39-9.16 | 4.94 | 79.2% |
| 0.010 deg | ~0.01796-0.01798 deg | 1.75-6.71 | 3.62 | 50.0% |
| 0.020 deg | ~0.03030-0.03038 deg | 1.04-3.98 | 2.14 | 31.9% |
| 0.030 deg | ~0.04359-0.04383 deg | 0.72-2.76 | 1.49 | 0% |
| 0.050 deg | ~0.07044-0.07146 deg | 0.44-1.69 | 0.91 | 0% |
| 0.100 deg | ~0.134-0.141 deg | 0.22-0.86 | 0.46 | 0% |

Thus a phase-equivalent smooth-mode uncertainty of order

```math
0.03^\circ
```

already makes the illustrative A-localized anomaly undetectable at `3 sigma` throughout the current profile family under this covariance model.

A `0.01 deg` nuisance prior is much better, but still gives `>=3 sigma` for only half the profile family at `0.10 deg` per-wavelength measurement noise.

---

## 9. Joint calibration / measurement precision requirement

Invert the Fisher calculation to ask:

> **What equal per-wavelength phase noise would guarantee at least `3 sigma` for every current sample-A profile, for the illustrative 25% anomaly?**

Results:

### Smooth nuisance effectively known

```math
\boxed{
\sigma_\phi\lesssim0.0944^\circ.
}
```

### Smooth-mode prior `0.002 deg RMS`

```math
\boxed{
\sigma_\phi\lesssim0.0909^\circ.
}
```

### Smooth-mode prior `0.005 deg RMS`

```math
\boxed{
\sigma_\phi\lesssim0.0697^\circ.
}
```

These are conditional thresholds for the current 81-wavelength dense scan, equal independent phase noise, and the stated illustrative anomaly.

They are not instrument specifications.

But they make the calibration/precision trade concrete.

---

## 10. What the result says about sample-B calibration

The earlier paired-identifiability calculation already showed that several arbitrary smooth A and B profiles cannot be decomposed symmetrically from A-B data.

The short-wave calculation now strengthens that conclusion:

> **sample-B calibration is not merely useful for interpreting the paired experiment; uncertainty in the smooth A/B transport subspace directly sets the detectability floor for the A-specific nonlinear-region contrast.**

This means the experiment should not be designed as one joint unconstrained fit.

The better sequence is:

```text
1. calibrate sample B smooth transport
2. constrain sample A smooth baseline with wavelengths/conditions that do not primarily target the nonlinear region
3. perform the short-wave A-B contrast scan
4. fit the A-localized contrast with those smooth-mode posteriors carried forward as priors.
```

---

## 11. Why more wavelengths are not automatically the solution

The anomaly-to-nuisance principal angle is extremely small.

That means the limitation is not simply

```text
insufficient number of wavelength samples.
```

The dense `81`-point short-wave scan already contains many measurements.

The problem is that most of those measurements probe nearly the same low-dimensional smooth spectral manifold.

Therefore the next design objective should not be

```text
sample even more wavelengths uniformly.
```

It should be

> **choose wavelengths, RF frequencies, temperatures, or biases that rotate the A-localized response away from the smooth A/B nuisance subspace.**

That is a fundamentally different optimal-design criterion from maximizing raw anomaly amplitude alone.

---

## 12. Current experimental interpretation

The project now has two separate necessary ingredients for detecting the retained nonlinear-region transport contrast:

### Spectral access

The scan must extend short enough that the generation boundary moves through the near-junction A region.

Current useful boundary:

```text
~2.0-2.8 um at 300 K.
```

### Baseline calibration / orthogonalization

The smooth A/B transport contribution must be constrained strongly enough that it cannot absorb the localized A response.

At nominal `0.10 deg` phase noise, phase-equivalent smooth-mode priors at or below approximately the `0.005-0.01 deg` scale are already scientifically consequential for the illustrative anomaly.

The exact requirement must eventually be recomputed with measured covariance and real A/B profiles.

---

## 13. Claim boundary

### CHECKED NUMERICALLY / CONDITIONAL

For the current 72-member sample-A profile family, central B optical model, `2.0-2.8 um` dense scan, first three smooth transport modes per device, independent `0.10 deg` phase noise, and the illustrative 25% A-localized slowdown:

- anomaly-to-six-mode nuisance principal angle is approximately `0.006-0.708 deg`, median `0.029 deg`;
- physical anomaly phase RMS is `~0.0315-0.1206 deg`, median `~0.0651 deg`;
- perfect nuisance knowledge gives `~2.83-10.85 sigma`, median `~5.86 sigma`;
- `0.005 deg` nuisance priors give `~2.39-9.16 sigma`, median `~4.94 sigma`;
- `0.010 deg` priors give `~1.75-6.71 sigma`, median `~3.62 sigma`;
- `0.030 deg` priors leave no profile at `>=3 sigma`;
- guaranteed `3 sigma` across the current profile family requires approximately `sigma_phi<=0.0944 deg` with known nuisance, `<=0.0909 deg` with `0.002 deg` nuisance priors, or `<=0.0697 deg` with `0.005 deg` nuisance priors.

### NOT ESTABLISHED

- actual sample-A anomaly magnitude/sign;
- actual smooth-mode priors achievable experimentally;
- independent equal wavelength noise;
- covariance-weighted optimal short-wave wavelengths;
- whether bias/temperature/RF diversity can substantially increase the anomaly-to-nuisance angle;
- calibrated real-device detection significance;
- novelty / priority.

---

## 14. Next decisive work

The next calculation should **not** simply maximize short-wave phase amplitude.

It should optimize experimental settings for the conditional information on the A-localized contrast after marginalizing smooth A/B nuisance modes.

In practical order:

1. optimize a sparse short-wave wavelength design using the posterior/Fisher anomaly variance, not raw `Delta phi`;
2. test whether adding a second RF frequency rotates the localized response relative to smooth nuisance once the full complex transfer is used;
3. test bias or temperature as an orthogonal perturbation if physically justified;
4. replace equal `0.10 deg` noise with the measured two-arm covariance;
5. carry a sample-B calibration posterior directly into the paired A fit.

The current result makes the experimental bottleneck precise:

> **short-wave spectral access gives enough raw signal; calibrated separation from smooth A/B transport is now the limiting inverse problem.**

---

## 15. Reproducibility

Deterministic regression:

`numerics/hgcdte_sample_a_shortwave_calibration_prior.py`
