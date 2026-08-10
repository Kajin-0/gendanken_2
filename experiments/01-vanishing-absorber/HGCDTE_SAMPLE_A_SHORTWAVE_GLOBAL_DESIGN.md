# Short-Wave Sample-A Contrast — Global Fixed-Time Wavelength Allocation

**Date:** 2026-08-09  
**Status:** conditional convex maximin wavelength-allocation calculation over the full 81-point short-wave grid and all 72 sample-A profile-family members; illustrative A-localized anomaly; smooth-mode calibration priors; no novelty claim

## 1. Why this calculation is needed

The exhaustive two-band design found that, for a phase-equivalent smooth-mode prior of

```math
\sigma_{\rm prior}=0.005^\circ,
```

the pair

```text
2.00 um / 2.69 um
```

with equal time gives

```text
worst-case illustrative anomaly significance ~3.093 sigma
```

across all 72 current sample-A profiles.

But that result alone does **not** prove that two wavelengths are the best use of the fixed measurement time.

A three-, four-, or continuously weighted multi-band design might in principle separate the A-localized anomaly from the six smooth A/B nuisance modes more effectively.

The correct next question is therefore:

> **If arbitrary nonnegative time can be distributed over all 81 wavelengths from 2.00 to 2.80 um, what allocation maximizes the worst-case anomaly significance across the sample-A profile family?**

This note solves that full fixed-time problem.

---

## 2. Full design vector

For each profile `p` and wavelength `i`, use the normalized spectral-response vector

```math
\mathbf x_{pi}
=
\begin{bmatrix}
h_{pi} &
\mathbf n_{pi}^T &
1
\end{bmatrix}^T,
```

containing

```text
1 A-localized anomaly amplitude
6 smooth A/B nuisance amplitudes
1 wavelength-independent differential phase intercept.
```

The six smooth nuisance amplitudes have independent Gaussian priors of phase-equivalent width

```math
\sigma_{\rm prior}.
```

The anomaly amplitude and common phase have no prior.

---

## 3. Fixed total measurement resource

Let

```math
w_i\ge0,
\qquad
\sum_i w_i=1
```

be the fraction of the total coherent integration time allocated to wavelength `i`.

Keep the same total resource as the dense reference scan:

```math
T_{\rm tot}=81
```

single-wavelength time units.

For white phase noise

```math
\sigma_{\phi,0}=0.10^\circ
```

per one time unit, the profile-specific Fisher matrix is

```math
\boxed{
\mathbf F_p(\mathbf w)
=
\frac{T_{\rm tot}}{\sigma_{\phi,0}^2}
\sum_i
w_i\mathbf x_{pi}\mathbf x_{pi}^T
+
\mathbf P,
}
```

where `P` contains the six smooth-mode prior precisions and zeros for the anomaly/common phase.

The anomaly variance is

```math
v_p(\mathbf w)
=
\mathbf e_0^T
\mathbf F_p^{-1}(\mathbf w)
\mathbf e_0.
```

If the illustrative physical anomaly RMS for profile `p` is `A_p`, define

```math
\boxed{
g_p(\mathbf w)
=
\frac{v_p(\mathbf w)}{A_p^2}
=
\frac{1}{\mathrm{SNR}_p^2}.
}
```

---

## 4. Why the global allocation problem is convex

The map

```math
\mathbf F\mapsto
\mathbf e_0^T\mathbf F^{-1}\mathbf e_0
```

is convex on the positive-definite cone.

`F_p(w)` is affine in the wavelength weights.

Therefore each

```math
g_p(\mathbf w)
```

is convex in `w`, and so is

```math
\max_p g_p(\mathbf w).
```

The global robust design is consequently the convex program

```math
\boxed{
\min_{\mathbf w}
\max_p g_p(\mathbf w)
}
```

subject to the wavelength simplex constraints.

The numerical implementation uses the equivalent epigraph form

```math
\min_{\mathbf w,z} z
```

with

```math
z\ge g_p(\mathbf w)
```

for every one of the 72 sample-A profiles, plus analytic gradients

```math
\boxed{
\frac{\partial v_p}{\partial w_i}
=-
\frac{T_{\rm tot}}{\sigma_{\phi,0}^2}
\left(
\mathbf x_{pi}^T
\mathbf F_p^{-1}
\mathbf e_0
\right)^2.
}
```

The solution is reproduced from both dense-uniform and sparse-pair initializations.

---

## 5. `0.002 deg` prior — the global solution is exactly the two-band result

For

```math
\sigma_{\rm prior}=0.002^\circ,
```

the global allocation is

```text
2.00 um -> 50% of total time
2.72 um -> 50% of total time.
```

Worst-case significance:

```math
\boxed{4.237\sigma.}
```

Thus at tight smooth-mode calibration the exhaustive two-band solution is also the full-grid optimum within numerical precision.

---

## 6. `0.005 deg` prior — the global solution still collapses to two spectral clusters

For the current useful design point

```math
\sigma_{\rm prior}=0.005^\circ,
```

the convex optimization gives approximately

```text
2.00 um -> 50.0%
2.68 um -> 9.0%
2.69 um -> 41.0%.
```

Equivalently:

```text
lower spectral cluster:
50% of time centered at 2.00 um

upper spectral cluster:
50% of time centered near 2.688 um.
```

The global worst-case significance is

```math
\boxed{3.09273\sigma.}
```

The simple equal-time

```text
2.00 / 2.69 um
```

pair gives

```math
3.09265\sigma.
```

The improvement from allowing **all 81 independent wavelength weights** is therefore only about

```math
\boxed{0.0028\%.}
```

This is negligible compared with the optical/material/instrument uncertainties still outstanding.

Hence a stronger statement is now justified:

> **Within the current fixed-time Fisher model, the `0.005 deg` robust design effectively collapses to two spectral bands.**

This is stronger than merely finding a good two-wavelength pair.

---

## 7. The decisive negative result — `0.010 deg` calibration cannot be rescued by more wavelength support

Set

```math
\sigma_{\rm prior}=0.010^\circ.
```

The globally optimized allocation spreads slightly within two clusters:

```text
lower cluster:
~50% total time
weighted center ~2.047 um

upper cluster:
~50% total time
weighted center ~2.688 um.
```

One representative numerical support is approximately

```text
2.00 um -> 32.8%
2.13 um -> 7.1%
2.14 um -> 10.1%
2.68 um -> 8.5%
2.69 um -> 41.5%.
```

But even this globally optimized arbitrary-support design reaches only

```math
\boxed{1.959\sigma}
```

worst case.

The best strict two-band pair gives about

```math
1.956\sigma.
```

Thus the full 81-weight optimization improves worst-case significance by only about

```math
0.16\%.
```

Most importantly:

> **At `0.010 deg` smooth-mode prior uncertainty, adding or redistributing wavelengths cannot restore a robust `3 sigma` detection at the same total measurement time.**

This removes an important escape route.

The problem is calibration/model separation, not inadequate wavelength sampling density.

---

## 8. Global calibration threshold

Repeat the convex optimization while varying `sigma_prior`.

The largest phase-equivalent smooth-mode prior width for which the **globally optimized arbitrary-support design** can still guarantee

```math
\mathrm{SNR}\ge3
```

for all 72 profiles is approximately

```math
\boxed{
\sigma_{\rm prior,max}
\approx0.00528^\circ.
}
```

This is essentially identical to the exhaustive two-band threshold.

Therefore the sharp transition near

```text
~0.0053 deg RMS per smooth nuisance mode
```

is not an artifact of restricting the design to two wavelengths.

---

## 9. What this changes experimentally

The short-wave validation strategy now has a clear resource hierarchy.

### First resource — calibration

The smooth A/B spectral contribution must be constrained to roughly

```math
\lesssim5\times10^{-3}\ {\rm deg\ RMS}
```

per normalized smooth-mode amplitude for the present illustrative anomaly/noise scale to be robustly detectable with the fixed time budget.

### Second resource — phase precision / total coherent time

Once that calibration level is reached, concentrating the available short-wave time into two separated spectral bands is substantially more efficient than a uniform dense scan.

### Wavelength count is not the dominant resource

At poor calibration, adding wavelengths alone does not solve the degeneracy.

This is the central design consequence of the global optimization.

---

## 10. Why the result is physically plausible

The unknown wavelength-independent phase forces the useful short-wave observable to depend on spectral **contrast**.

The localized A anomaly and six smooth nuisance responses vary smoothly with wavelength.

The optimizer therefore wants two well-separated spectral regions:

```text
one as short as the validated optical model allows
+
one near ~2.69 um where the anomaly-versus-nuisance contrast is maximized.
```

Within each region, nearby wavelengths carry nearly redundant information under the current smooth reduced model.

That is why the global solution allocates time to two narrow clusters rather than spreading it over the full interval.

---

## 11. Important caution — the 2.00 um solution is boundary-limited

The lower cluster repeatedly lands at or very near

```text
2.00 um,
```

the lower edge of the spectral range currently used for the Moazzami absorption model.

Do **not** infer that a still shorter wavelength would necessarily be better in the real device.

Instead this means:

> **the present design is limited by validated short-wave optical knowledge on its lower side.**

If a reliable absorption/optical model below `2 um` becomes available, the design should be re-run rather than extrapolated.

---

## 12. What remains conditional

The global optimization is exact only for the stated reduced model.

It still assumes

```text
illustrative 25% A-localized transport perturbation
six smooth A/B nuisance modes
current sample-A profile sensitivity family
central sample-B optical envelope
0.10 deg one-unit white phase noise
Gaussian independent smooth-mode priors
known wavelength coordinate
no additional wavelength-dependent differential path systematic.
```

It does **not** establish

- actual sample-A transport amplitude;
- experimental attainability of `~0.005 deg` smooth-mode calibration;
- absence of higher-order spectral systematics;
- a calibrated real-device wavelength prescription;
- novelty or manuscript readiness.

---

## 13. Current strongest conclusion

The short-wave branch can now be summarized compactly:

```text
mid/deep scan
-> calibrate smooth transport + instrument + temperature controls

short-wave spectral encoder
-> makes A's near-junction nonlinear region visible

global fixed-time design
-> effectively two spectral clusters near ~2.00 and ~2.69 um

smooth-mode prior <=~0.0053 deg
-> robust 3-sigma illustrative detection possible

smooth-mode prior ~0.010 deg
-> no wavelength allocation at the same total time can rescue the test.
```

This makes the next decisive work experimental rather than another wavelength-design exercise:

> **Can the sample-B / instrument calibration actually constrain the relevant smooth phase modes to the `~0.005 deg RMS` class over the short-wave measurement interval?**

Numerical implementation:

`numerics/hgcdte_sample_a_shortwave_global_design.py`
