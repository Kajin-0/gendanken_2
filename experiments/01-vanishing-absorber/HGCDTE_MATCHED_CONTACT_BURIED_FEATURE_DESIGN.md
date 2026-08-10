# Matched-Contact Validation Structure — Move the Distinguishing Transport Feature Away From the Junction

**Date:** 2026-08-09  
**Status:** conditional purpose-built validation-geometry calculation; finite-RF complex response; physical contact/smooth-bulk nuisance projection; no fabrication prescription, calibrated transport, or novelty claim

## 1. Why the published sample-A geometry is not the ideal validation structure

The published sample-A nonlinear-gradient region sits close to the collecting junction.

That creates three simultaneous problems:

```text
front-collection survival kernel -> weak differential leverage near the boundary
contact/interface timing -> lives in the same spatial region
published A/B front semiconductor environments -> not perfectly matched.
```

The resulting finite-RF timing fingerprint can be reproduced extremely closely by a combination of smooth bulk transport and one simple near-junction/contact template.

Therefore the strongest next validation geometry is not merely a more precise measurement of the published A/B pair.

It is a **matched-contact pair** in which the collection-side stack is held fixed and the distinguishing internal structure is buried farther from the interface.

---

## 2. Reference thought-device profile

Use a simple monotonic control absorber

```text
HgCdTe thickness L = 7.6 um
front / collecting-side composition x = 0.40
back composition x = 0.32
linear composition profile.
```

At 300 K this corresponds to a composition-gradient field of approximately

```math
\boxed{142\ \mathrm{V/cm}}
```

near `x~0.36`, comparable to the weak linear-gradient scale reported for the published devices.

This is not proposed as an optimized detector.

It is a clean validation coordinate because a control and contrast device can, in principle, share

```text
same front composition
same contact/junction stack
same total thickness
same back composition
same endpoint band gaps
```

while differing mainly in the **internal distribution of composition gradient**.

---

## 3. Abstract buried transport-feature sweep

Before constructing a realizable composition profile, represent the distinguishing transport response by

```math
\boxed{
w(z)
=\exp\left[-\frac{(z-z_0)^2}{2\sigma_z^2}\right].
}
```

Sweep

```text
center z0 = 0.25-7.00 um
width sigma_z = 0.20, 0.35, 0.50, 0.75, 1.00 um.
```

Use

```text
lambda = 2.80-3.83 um, Pabs >=0.05
f = 0.25, 0.50, 1, 2, 3 GHz
phase + log-magnitude finite-RF Jacobian.
```

At each RF frequency remove a wavelength-independent complex response.

---

## 4. Mechanism nuisance span

Project the candidate response against a deliberately physical nuisance basis:

### Smooth bulk transport

```math
1,
\qquad
z/L,
\qquad
(z/L)^2.
```

### Near-junction/contact-like transport

```math
e^{-z/\ell_c},
```

with

```text
ell_c = 0.20, 0.50, 0.75, 1.00 um.
```

The exponentials are effective response supports, not literal contact-thickness models.

The design metric is the norm of the candidate response left after orthogonal projection onto this nuisance span.

That residual norm is proportional to Fisher detection SNR for a fixed feature amplitude and normalized covariance.

---

## 5. Realistic wavelength-dependent signal weighting matters

Near cutoff, equal phase/magnitude noise is optimistic.

Therefore evaluate three diagnostics:

```text
equal response noise
statistics-like: sigma ~ Pabs^(-1/2)
additive-like:   sigma ~ Pabs^(-1).
```

The corresponding whitening factors are

```text
1
sqrt(Pabs)
Pabs.
```

The equal-noise optimum moves very deep because it overvalues weak near-cutoff measurements.

The two realistic signal-weighted models give a much more useful and consistent design.

---

## 6. Statistics-like optimum

For

```math
\sigma_{\rm response}\propto P_{\rm abs}^{-1/2},
```

the strongest buried feature in the current grid is

```math
\boxed{
z_0\approx5.00\ \mu\mathrm m,
\qquad
\sigma_z\approx0.50\ \mu\mathrm m.
}
```

Its target-to-nuisance principal angle is about

```math
\boxed{1.18^\circ.}
```

More importantly, compare the same `0.50 um`-width feature near the junction and at the buried optimum:

```text
near-junction center = 0.75 um
recoverable residual norm ~9.55e-5

buried center = 5.00 um
recoverable residual norm ~2.19e-3.
```

Thus

```math
\boxed{
\text{recoverable amplitude gain}\approx23.0\times
}
```

or approximately

```math
\boxed{
\text{information gain}\approx5.3\times10^2.
}
```

---

## 7. Additive-like optimum

For

```math
\sigma_{\rm response}\propto P_{\rm abs}^{-1},
```

the optimum shifts only slightly:

```math
\boxed{
z_0\approx4.75\ \mu\mathrm m,
\qquad
\sigma_z\approx0.50\ \mu\mathrm m.
}
```

Principal angle:

```math
\boxed{\sim0.99^\circ.}
```

For a `0.50 um` width:

```text
near-junction center = 0.75 um
recoverable residual norm ~8.87e-5

buried center = 4.75 um
recoverable residual norm ~1.76e-3.
```

Hence

```math
\boxed{
\text{recoverable amplitude gain}\approx19.8\times
}
```

and

```math
\boxed{
\text{information gain}\approx3.9\times10^2.
}
```

---

## 8. Why the optimum sits near 4.75-5.0 um

For the reference linear profile,

```text
z = 4.75 um -> x ~0.3500
z = 5.00 um -> x ~0.3474.
```

At 300 K those compositions correspond to local gap wavelengths of approximately

```text
~3.46 um
~3.50 um.
```

This region is deep enough to be spatially separated from contact-like nuisances but not so deep that the only useful wavelengths are signal-starved at cutoff.

In the current control profile, modeled absorption is still substantial around those wavelengths.

That produces a natural compromise:

```text
too shallow
-> contact/gauge degeneracy

too deep
-> near-cutoff signal collapse

~5 um depth
-> strong spectral leverage while retaining usable signal.
```

---

## 9. The design consequence is much stronger than another wavelength optimization

The published-like near-junction geometry loses hundreds-fold information **before** instrument noise is optimized, simply because the target mechanism occupies the same response space as contact and smooth-bulk effects.

Moving the distinguishing region inward changes the physical response geometry itself.

This is qualitatively different from

```text
adding more wavelengths
adding more RF frequencies
or
integrating longer.
```

Those improve measurement precision but do not remove a mechanism degeneracy that is built into the device geometry.

---

## 10. What this calculation does not yet establish

The Gaussian feature is only an abstract **transport-support coordinate**.

This note does not yet specify

- a realizable monotonic composition profile that produces it;
- a microscopic relation between composition-gradient field and transport change;
- doping / junction design;
- interface passivation;
- strain or growth constraints;
- actual noise covariance;
- exact fabrication tolerances.

The next step is therefore to translate the geometric optimum into a composition profile while preserving matched-contact conditions.

---

## 11. Stronger validation architecture

The emerging experiment is:

### Control

```text
fixed front/contact/junction stack
smooth monotonic internal grading
fixed endpoints and thickness.
```

### Contrast

```text
same front/contact/junction stack
same endpoints and thickness
+
a buried redistribution of composition gradient centered near ~4.8-5.0 um.
```

A still stronger experiment would use several buried-gradient strengths with the same outer structure and test whether the recovered timing mode scales systematically with the designed buried perturbation.

That would provide a causal dose-response test rather than relying on one A-versus-B difference.

---

## 12. Next decisive calculation

Construct an explicit family of **monotonic endpoint-matched composition profiles** that

```text
preserve the first ~1 um near the collecting contact
preserve x_front
preserve x_back
preserve total thickness
but redistribute dx/dz into the ~4.8-5.0 um buried region.
```

Then quantify

```text
peak composition-gradient field
minimum compensating field elsewhere
front-region mismatch
optical-kernel change
finite-RF mechanism separation
and monotonicity limits.
```

That will determine whether the excellent abstract buried-feature geometry survives a physically constrained graded-HgCdTe construction.

Numerical implementation for the present sweep:

`numerics/hgcdte_matched_contact_buried_feature_design.py`
