# Same-Wafer Translated-Gradient Depth Series — A Stronger Causal Validation Architecture

**Date:** 2026-08-10  
**Status:** conditional information-design result; same-wafer HgCdTe selective-growth implementation remains OPEN; no novelty claim

## 1. Why move beyond a two-device pair?

The matched translated-gradient pair solved a major problem in the published sample-A geometry:

```text
move the internal gradient-related feature
while holding the contact/cap/junction design fixed.
```

But if `G1` and `G2` are grown separately, one remaining causal weakness survives:

```text
run-to-run bulk variation
contact/interface variation
cap/junction variation
and other process drift.
```

With only two devices, an unknown device-to-device shift cannot be distinguished structurally from a relocation signal merely by adding more phase precision.

This motivates a stronger experiment:

> **Measure several devices whose otherwise matched internal gradient feature occupies several known depths, preferably on one nominal epitaxial growth, and test whether the wavelength × RF fingerprint follows the predicted nonlinear depth dependence.**

The distinguishing object becomes a **translation law**, not one A-minus-B number.

---

## 2. Important fabrication boundary

HgCdTe MBE clearly supports

```text
precise composition programming through thickness
sub-micron and even nanometer-scale heterostructure growth
in-situ ellipsometric composition/thickness control
and spatial post-growth wafer mapping.
```

However, the present literature audit has **not** recovered a HgCdTe-specific demonstration of a moving knife-edge/shadow-mask scheme that places the same buried feature at different depths laterally on one wafer.

Moving-shutter wedge growth is established in MBE more generally, and selective shadow growth has been demonstrated in other II-VI compound-semiconductor systems.

Therefore:

> **the same-wafer implementation is technologically motivated but remains an OPEN HgCdTe process-development question.**

Do not describe it as an established HgCdTe fabrication method.

A sequential set of tightly matched MBE growths remains the fallback implementation.

---

## 3. Numerical question

Before investing in the selective-growth engineering, ask whether a depth series actually buys enough causal information.

Use the current programmed feature:

```text
L = 7.6 um
x_front = 0.55
x_back = 0.32
feature width = 1.0 um
edge ramps ~0.1 um
local gradient field ~2 kV/cm
illustrative feature-supported transport change = 25%.
```

Use

```text
lambda = 2.00-2.40 um
f = 0.25, 0.50, 1, 2, 3 GHz
phase + ln|H|
finite-RF deterministic-transit Jacobian
statistics-like Pabs weighting.
```

The short `2.00-2.40 um` band is inherited from the interface-safe joint depth/spectral optimization, where modeled absorption remains above about `0.99`.

---

## 4. Nuisance model

For every device, use the same physical nuisance basis:

### smooth bulk

```math
1,
\quad z/L,
\quad(z/L)^2,
\quad(z/L)^3,
```

### collection-side interface

```math
\exp(-z/\ell),
\qquad
\ell=0.30,0.50,0.75,1.00\ \mu{\rm m},
```

### back/interface side

```math
\exp[-(L-z)/\ell]
```

with the same four length scales.

Also remove an arbitrary wavelength-independent phase and log-magnitude intercept for each independent device contrast and RF frequency.

The important new stress is that a nuisance amplitude need **not** be identical across the device series.

Let the device/lateral coordinate be `xi`.

Allow each nuisance amplitude to follow

```math
\boxed{
a(\xi)=a_0+a_1\xi+\cdots+a_p\xi^p.
}
```

Thus

```text
p=0 -> perfectly common matched nuisance
p=1 -> arbitrary linear lateral/process drift
p=2 -> arbitrary quadratic drift
p=3 -> arbitrary cubic drift.
```

This is substantially more conservative than the ideal two-device matched-control calculation.

---

## 5. Why two devices cannot solve smooth process drift

For two device locations, any two nuisance amplitudes can be represented exactly by

```math
a_0+a_1\xi.
```

Therefore once arbitrary linear device-to-device nuisance drift is admitted, a two-point structural comparison has no independent way to determine whether a difference came from

```text
translated internal feature
or
ordinary device-to-device nuisance drift.
```

This is an experimental-design limitation, not a phase-noise problem.

More wavelengths or RF frequencies do not remove it automatically.

---

## 6. Three depths create curvature information

With three or more feature depths, a linear nuisance trend no longer spans an arbitrary depth-dependent response.

The translated-feature fingerprint is nonlinear in depth because both

```text
the optical generation distribution
and
the finite-RF transport sensitivity kernel
```

change relative to the buried feature.

The experiment can therefore test whether the measured response bends with depth as predicted rather than merely shifting monotonically from device to device.

This is the first qualitative advantage of the depth-series architecture.

---

## 7. Fixed-total-resource optimization

The numerical score is

```math
\boxed{
S=\frac{\|r_\perp\|}
{\sqrt{N_{\rm device}N_\lambda}},
}
```

where `r_perp` is the whitened complex target after projecting all allowed nuisance directions.

Because total measurement resource is held fixed, adding devices is not free.

The design must gain enough new mechanism geometry to justify dividing averaging time among more measurement states.

Candidate feature centers are scanned from

```text
2.0 to 5.6 um
in 0.2-um steps
```

with at least `0.4 um` between chosen centers.

The earlier interface-safe ideal two-device reference is

```text
4.1 / 5.6 um
```

with nuisance amplitudes assumed perfectly common.

---

## 8. Six depths tolerate quadratic nuisance drift

Allow every modeled bulk/front/back-interface nuisance amplitude to vary **quadratically** across the series.

The strongest six-depth design on the current grid is approximately

```text
2.0
2.4
2.8
4.6
5.2
5.6 um.
```

It forms two depth clusters rather than an evenly spaced ladder.

The fixed-total-resource score is approximately

```math
\boxed{0.87}
```

times the score of the ideal `4.1/5.6 um` two-device pair with perfectly common nuisance amplitudes.

That is a strong result:

> **the six-point series gives up only about 13% of ideal matched-pair information amplitude while buying immunity to arbitrary quadratic lateral trends in every modeled bulk/interface nuisance amplitude.**

Modeled absorption remains above `0.990`.

---

## 9. Seven depths tolerate cubic drift

Allow a cubic lateral trend in every nuisance amplitude.

The strongest seven-depth grid is approximately

```text
2.0
2.4
2.8
4.4
4.8
5.2
5.6 um.
```

Its fixed-total-resource information score is approximately

```math
\boxed{0.58}
```

times the ideal perfectly matched two-device reference.

Thus even after allowing a rather flexible smooth process drift, a large fraction of the structural relocation information survives.

This is much more conservative than assuming six or seven nominally identical devices.

---

## 10. Why the optimum forms two clusters

The cluster structure is physically sensible.

A polynomial drift is best constrained by samples spanning a broad lateral/depth range, while the relocation fingerprint itself changes most strongly where the wavelength/RF kernel responds rapidly to feature depth.

The optimizer therefore uses

```text
one shallower cluster
+
one deeper cluster
```

rather than spending equal resource at redundant intermediate depths.

Conceptually, the two clusters test two different internal positions while the multiple points inside each cluster determine whether a smooth fabrication trend can explain the observed variation.

This is analogous to having both **contrast** and **local process-control curvature** in the same wafer experiment.

---

## 11. Scientific advantage over G1/G2 alone

### Two-device pair

Can test

```text
feature at depth z1
vs
feature at depth z2.
```

But it relies heavily on fabrication matching.

### Depth series

Can test

```text
Does the entire wavelength x RF fingerprint evolve with feature depth
according to the forward optical/transport model?
```

while simultaneously fitting smooth lateral process drift.

That is a much harder prediction for a fixed contact artifact or broad wafer nonuniformity to mimic.

The experiment becomes a **spatial causality/falsification test** rather than merely a matched subtraction.

---

## 12. Same-wafer implementation concept

The most attractive implementation would create lateral regions in which the same internal composition feature is reached at different growth depths, then restore a common final cap/contact plane.

Possible generic MBE mechanisms include

```text
moving knife-edge / shutter thickness wedge
selective shadow growth
or another region-selective epitaxial exposure scheme.
```

However, this remains a **concept**, because the audit has not found a demonstrated HgCdTe process implementing the required translated internal profile across one wafer.

The next materials-engineering task is therefore not generic MBE feasibility.

It is specifically:

> **Can a HgCdTe MBE chamber implement a lateral growth-time offset for the internal feature while compensating the final thickness and preserving the intended composition profile/cap across all device regions?**

If not, use several sequential MBE runs and retain the depth-series statistical design to diagnose run-to-run drift.

---

## 13. Literature scale supporting the concept — but not proving it

Relevant established capabilities include:

- HgCdTe MBE composition and thickness can be monitored with high precision by in-situ ellipsometry;
- HgCdTe wafer composition/thickness can be spatially mapped post-growth;
- HgCdTe MBE can produce multilayer and compositionally graded detector structures;
- moving knife-edge shutters are established for wedge thickness growth in MBE generally;
- selective shadow MBE has been demonstrated for other II-VI compound-semiconductor heterostructures.

These ingredients make the same-wafer concept technically plausible enough to investigate.

They do **not** establish that the exact HgCdTe process has already been demonstrated.

---

## 14. Current decision

The strongest hierarchy is now

```text
physics validation target:
translated buried internal-gradient feature

preferred causal design:
multi-depth translation series

preferred fabrication target:
same-wafer MBE series if region-selective growth is feasible

fallback:
sequential closely matched MBE growths with post-growth x(z) characterization

not preferred for compact feature:
single-run slider LPE.
```

The depth series should therefore replace the simple `G1/G2` pair as the **strongest conceptual validation architecture**, while the two-device pair remains the minimum practical experiment.

---

## 15. Important nonclaims

Do not claim

```text
same-wafer translated HgCdTe profiles have been fabricated
moving-shutter HgCdTe MBE is established
quadratic/cubic nuisance drift is the true wafer-error model
the illustrative 25% transport perturbation is a real device prediction
or the remaining inverse method is novel.
```

The point of the calculation is narrower:

> **Once several translated depths are available, the experiment can distinguish the predicted nonlinear relocation fingerprint from low-order smooth fabrication drift in a way a two-device comparison cannot.**

---

## 16. Numerical regression

`numerics/hgcdte_same_wafer_translation_series.py`
