# Programmed Translated-Gradient HgCdTe — Materials Feasibility and Stronger Validation Geometry

**Date:** 2026-08-10  
**Status:** conditional materials/design synthesis using published HgCdTe epitaxial capabilities plus the repository finite-RF model; no fabrication demonstration and no novelty claim

## 1. Question

The Gaussian translated-gradient profile was useful mathematically, but the next question is physical:

> **Can HgCdTe epitaxy plausibly place the same internal high-gradient region at two depths separated by roughly `0.6 um` while keeping the collection-side composition and overall endpoints matched?**

The literature answer is now strong enough to separate the growth methods.

---

## 2. MBE makes sub-micron profile placement technologically plausible

HgCdTe molecular-beam epitaxy has long been used for compositionally tailored heterostructures with in-situ composition/thickness control.

A particularly useful scale comes from Mikhailov et al., *Photonics* 10, 430 (2023), DOI `10.3390/photonics10040430`.

Their HgCdTe multiple-quantum-well structures were grown by MBE with in-situ ellipsometry, and the reported composition/thickness measurement accuracies were approximately

```text
Delta x = 0.0005
Delta d = 0.5 nm.
```

That does **not** mean a `0.5 nm` arbitrary HgCdTe gradient-placement tolerance can automatically be achieved in our structure.

It does show that the relevant epitaxial control/metrology scale is far finer than

```text
feature displacement ~0.6 um
feature edge ramp ~0.1 um
feature total width ~1.0 um.
```

Earlier MBE work also explicitly demonstrated composition-controlled HgCdTe heterostructures using in-situ ellipsometry; see Varavin et al., *Journal of Crystal Growth* 159 (1996) 1161-1166, DOI `10.1016/0022-0248(95)00845-4`.

Thus **MBE is the cleanest first fabrication route** for the translated-gradient control experiment.

---

## 3. MOCVD is also a credible route, but interdiffusion must be treated as part of the design

Madejczyk et al., *Infrared Physics & Technology* 81 (2017) 276-281, DOI `10.1016/j.infrared.2017.01.020`, report HgCdTe MOCVD heterostructures with designed internal graded-gap sublayers and SIMS-measured composition profiles.

Their work is particularly relevant because the real interfaces are not perfectly abrupt: interdiffusion during growth broadens the programmed layer structure.

That suggests a practical MOCVD workflow:

```text
program desired composition segments
-> grow
-> measure realized x(z) by SIMS / optical methods
-> update the timing forward model with the realized profile.
```

For this experiment, interface broadening is not automatically fatal because the target feature itself is intentionally broad, of order `1 um`.

But the **realized** profile, not the nominal recipe, must enter the inverse model.

---

## 4. Ordinary single-run LPE/interdiffusion is less natural for this particular control

LPE can certainly produce HgCdTe heterostructures and even buried/multijunction devices. Gawron and Rogalski, *Infrared Physics & Technology* 43 (2002) 157-163, DOI `10.1016/S1350-4495(02)00135-4`, demonstrated buried HgCdTe structures by LPE and discuss multiple epitaxy/selective-growth routes for more complex bandgap engineering.

However, the longitudinal composition profile in conventional HgCdTe LPE is strongly tied to

```text
growth temperature history
solidification from the melt
substrate/layer interdiffusion
and subsequent thermal processing.
```

That makes the specific operation

```text
translate one internal high-gradient segment by 0.6 um
while holding the same front/back compositions and contact-side cap
```

less direct than with time-programmable MBE/MOCVD.

So the present ranking is

```text
MBE   -> strongest first route
MOCVD -> credible, with diffusion-aware profile reconstruction
LPE   -> possible only through a more elaborate multiple-growth/profile-engineering route;
         not ruled out, but not the simplest implementation of this control.
```

---

## 5. Replace the Gaussian by a growth-programmable graded segment

The Gaussian was not required by the physics.

Use instead a compact unit feature `h(z)` in the **composition-slope magnitude**:

```text
total feature width = 1.00 um
entrance slope ramp  = 0.10 um
flat high-gradient   = 0.80 um
exit slope ramp      = 0.10 um.
```

Let

```math
\boxed{
s(z)=s_0[1+a(h(z)-\langle h\rangle)],
\qquad a=4,
}
```

and

```math
x(z)=x(0)-\int_0^z s(u)du.
```

Use the same conceptual endpoints as the earlier translated-pair design:

```text
L = 7.6 um
x_front = 0.55
x_back = 0.32.
```

The mean subtraction keeps the integral of `s(z)` fixed, so translating the feature leaves both endpoints unchanged.

This profile is continuous in composition, monotonic, and can be represented directly as a sequence of programmed composition ramps rather than as an abstract Gaussian tail.

---

## 6. The programmed profile reproduces the desired field contrast

For a feature centered at `2.6 um`, the composition-slope magnitude is approximately

```text
background dx/dz ~0.01593 /um
high-gradient dx/dz ~0.13698 /um.
```

Using the Hansen gap derivative at 300 K, the resulting built-in-gradient field spans roughly

```text
background ~214 V/cm
feature maximum ~1.96 kV/cm.
```

For the translated `3.2 um` device, the maximum is about `1.95 kV/cm`.

Thus the piecewise-programmable version naturally reproduces the same

```text
~200 V/cm background
vs
~2 kV/cm localized gradient
```

contrast that motivated the original published sample-A branch.

---

## 7. Concrete nominal composition coordinates

For the `2.6 um` feature-center device, the programmed region spans roughly

```text
z = 2.1 to 3.1 um
```

with `0.1 um` transition ramps.

Representative compositions are

```text
x(0.0) = 0.5500
x(2.1) ~0.5166
x(2.2) ~0.5089
x(3.0) ~0.3993
x(3.1) ~0.3917
x(7.6) = 0.3200.
```

For the `3.2 um` translated device:

```text
x(0.0) = 0.5500
x(2.7) ~0.5070
x(2.8) ~0.4993
x(3.6) ~0.3898
x(3.7) ~0.3821
x(7.6) = 0.3200.
```

These are **nominal design coordinates**, not required final growth targets.

A real epitaxial design should be adjusted around process-specific composition limits, doping, cap/junction requirements, and measured interdiffusion.

---

## 8. Strong numerical result — the fabrication-like profile improves identifiability

Use the same finite-RF experiment:

```text
lambda = 2.00-2.80 um
f = 0.25, 0.50, 1, 2, 3 GHz
phase + ln|H|
baseline v = 1e5 m/s
illustrative 25% feature-supported transport perturbation
common cubic bulk + four near-junction exponential nuisance shapes.
```

The maximum **absolute nuisance-orthogonal complex signal** on the tested feature-position grid remains

```math
\boxed{2.6\rightarrow3.2\ {\rm um}.}
```

For this programmed profile:

```text
minimum Pabs >0.9967
minimum |H| >0.987
1-GHz differential phase p-p ~0.1843 deg

matched-common-nuisance complex angle ~14.41 deg
matched complex residual norm ~0.007871

matched phase-only angle ~8.76 deg
matched phase residual-vector norm ~0.2755 deg.
```

For comparison, the Gaussian profile at the same `2.6/3.2 um` centers gave

```text
complex angle ~5.48 deg
complex residual ~0.002459
phase residual ~0.0514 deg.
```

So the more fabrication-like segment is not merely acceptable.

> **It substantially strengthens the mechanism-separation geometry in the current model.**

---

## 9. Angle-only optimum is again not the experimental optimum

The largest principal angle on the programmed-profile grid occurs around

```text
1.4 -> 1.8 um
```

with

```text
complex angle ~22.0 deg
complex residual ~0.00469.
```

The `2.6 -> 3.2 um` pair has a smaller angle but a larger surviving signal:

```text
angle ~14.41 deg
residual ~0.00787.
```

Therefore the design objective remains

```text
maximize nuisance-orthogonal signal / expected covariance
```

rather than principal angle alone.

---

## 10. Measurement resource improves sharply

Under the same provisional convention that phase and `ln|H|` components each have independent `0.10 degree`-equivalent noise, the programmed `2.6/3.2 um` pair gives

```math
\boxed{{\rm SNR}_{\rm complex}\approx4.51.}
```

The corresponding `3 sigma` equivalent component-noise ceiling is roughly

```math
\boxed{0.150^\circ.}
```

Thus the illustrative signal is already above `3 sigma` at the `0.10 degree` reference **if the nuisance amplitudes are genuinely common/matched**.

Phase-only data are close:

```text
SNR @0.10 deg ~2.75
3-sigma phase-noise ceiling ~0.0918 deg
```

which corresponds to only about `1.19x` the white-noise integration needed to move from `0.10` to `0.0918 degree`.

This is a qualitative change from the published-A near-junction geometry.

---

## 11. Matching remains essential

Allow the same bulk/contact nuisance shapes to vary independently in the two devices.

Then even the programmed pair drops to approximately

```text
complex principal angle ~0.235 deg
phase-only principal angle ~0.053 deg.
```

So the stronger profile does **not** eliminate the need for a matched-control experiment.

The key experimental claim remains:

> **Move the internal gradient feature while holding the contact/cap/junction and broad process variables common.**

---

## 12. Materials conclusion

The current purpose-built experiment is no longer blocked by an obviously unphysical composition profile.

The strongest route is now:

```text
MBE or diffusion-aware MOCVD
+
programmed ~1-um internal graded segment
+
~0.6-um controlled relocation
+
identical collection-side cap/contact design
+
post-growth x(z) characterization
+
wavelength x RF matched-pair measurement.
```

The `2.6 / 3.2 um` coordinates are still conditional numerical optima, not final layer specifications.

But the relevant length scales are comfortably larger than demonstrated HgCdTe epitaxial layer-control scales.

---

## 13. What remains before calling the structure experimentally ready

- choose a specific epitaxial platform and realistic growth temperature;
- include expected interdiffusion/smoothing in the programmed profile;
- specify doping and junction geometry while holding contact-side conditions matched;
- propagate measured `x(z)` uncertainty through the optical/RF forward model;
- recompute mismatch tolerances for the programmed profile rather than the Gaussian prototype;
- audit prior art for deliberately **translated** internal graded-gap HgCdTe control pairs;
- obtain real wavelength-dependent phase/magnitude covariance.

---

## 14. Primary materials references used for this feasibility boundary

1. N. N. Mikhailov et al., “Interband Electron Transitions Energy in Multiple HgCdTe Quantum Wells at Room Temperature,” *Photonics* **10**, 430 (2023), DOI `10.3390/photonics10040430`.
2. V. S. Varavin et al., “Molecular beam epitaxy of high quality Hg1-xCdxTe films with control of the composition distribution,” *Journal of Crystal Growth* **159**, 1161-1166 (1996), DOI `10.1016/0022-0248(95)00845-4`.
3. P. Madejczyk et al., “Engineering steps for optimizing high temperature LWIR HgCdTe photodiodes,” *Infrared Physics & Technology* **81**, 276-281 (2017), DOI `10.1016/j.infrared.2017.01.020`.
4. W. Gawron and A. Rogalski, “HgCdTe buried multi-junction photodiodes fabricated by the liquid phase epitaxy,” *Infrared Physics & Technology* **43**, 157-163 (2002), DOI `10.1016/S1350-4495(02)00135-4`.

Numerical implementation:

`numerics/hgcdte_programmed_translated_gradient_design.py`
