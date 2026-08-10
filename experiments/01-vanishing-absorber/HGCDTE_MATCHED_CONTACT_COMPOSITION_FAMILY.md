# Matched-Contact Buried-Gradient Composition Family

**Date:** 2026-08-09  
**Status:** explicit monotonic endpoint-matched composition construction; preserves the collection-side profile to high precision while redistributing gradient into a buried region; conditional optical/finite-RF diagnostics; no fabrication or transport claim; no novelty claim

## 1. Purpose

The abstract matched-contact sweep found that a distinguishing transport feature near

```text
z ~4.75-5.0 um
```

is hundreds-fold more informative than the published-like near-junction geometry once contact and smooth-bulk mechanisms are treated as competitors.

The remaining question was whether such a buried feature can be represented by a physically constrained **monotonic HgCdTe composition profile** without changing the outer device conditions that should serve as controls.

This note constructs such a family explicitly.

---

## 2. Control profile

Use the same simple thought-device control:

```text
L = 7.6 um
x_front = 0.40
x_back = 0.32
linear x(z).
```

Thus

```math
\boxed{
x_0(z)
=x_f-\frac{\Delta x}{L}z,
\qquad
\Delta x=x_f-x_b=0.08.
}
```

The 300 K composition-gradient field is approximately

```text
~142 V/cm
```

through the middle of the layer.

---

## 3. Buried-gradient redistribution with exactly matched endpoints

Define a buried Gaussian gradient enhancement

```math
G(z)
=\exp\left[
-\frac{(z-z_0)^2}{2\sigma_g^2}
\right]
```

with

```text
z0 = 4.90 um
sigma_g = 0.35 um.
```

To keep the front region matched, do **not** compensate the extra integrated gradient near the contact.

Instead use a smooth compensation window that turns on deeper in the absorber:

```math
H(z)
=\frac12
\left[
1+\tanh\left(
\frac{z-z_c}{a}
\right)
\right],
```

with

```text
z_c = 1.50 um
a = 0.15 um.
```

For gradient-strength coordinate `beta`, define

```math
\boxed{
w_\beta(z)
=1+\beta G(z)-c_\beta H(z),
}
```

where

```math
\boxed{
c_\beta
=\beta
\frac{\int_0^L G(z)dz}
{\int_0^L H(z)dz}.
}
```

Then

```math
\int_0^L w_\beta(z)dz=L
```

exactly, so define

```math
\boxed{
\frac{dx_\beta}{dz}
=-\frac{\Delta x}{L}w_\beta(z)
}
```

and

```math
\boxed{
x_\beta(z)
=x_f
-\frac{\Delta x}{L}
\int_0^z w_\beta(u)du.
}
```

Every member therefore has exactly the same

```text
x_front
x_back
thickness
```

as the control.

---

## 4. The first micron is essentially unchanged

Because both `G(z)` and the compensation window are negligible near the collection side, the contrast family retains the control composition and gradient through the front region.

For `beta = 1, 3, 5`:

```text
maximum |Delta x| in first 1 um:
~1.4e-7
~4.3e-7
~7.2e-7
```

and the maximum fractional gradient difference in that front micron is only approximately

```text
0.018%
0.054%
0.091%.
```

Thus, at the level of the intended profile model,

> **the collection-side semiconductor environment is effectively identical while the buried gradient structure changes.**

Actual fabrication variation in junction, doping, passivation and contacts would still need independent characterization.

---

## 5. Strict monotonicity

A valid HgCdTe grading profile must not reverse composition direction merely to satisfy the endpoint constraint.

For the present geometry, monotonicity requires

```math
w_\beta(z)>0.
```

The compensation coefficient is proportional to `beta`, giving an approximate strict monotonicity ceiling

```math
\boxed{\beta<6.95.}
```

The proposed diagnostic ladder

```text
beta = 1, 3, 5
```

therefore remains comfortably monotonic.

---

## 6. Buried composition-gradient field ladder

Using the Hansen gap relation to convert `dx/dz` to composition-gradient field at 300 K:

### `beta = 1`

```text
peak buried field ~263 V/cm
minimum compensating field ~121 V/cm
max |Delta x| anywhere ~0.00388.
```

### `beta = 3`

```math
\boxed{
F_{\rm peak}\approx506\ \mathrm{V/cm}
}
```

with

```text
minimum compensating field ~80.6 V/cm
max |Delta x| ~0.01163.
```

### `beta = 5`

```text
peak buried field ~749 V/cm
minimum compensating field ~39.8 V/cm
max |Delta x| ~0.01939.
```

Thus one mathematical construction gives a controlled internal-gradient ladder while holding the front region and endpoints fixed.

This is more useful for validation than trying to reproduce the published sample-A `~2 kV/cm` surface field, because the purpose here is **mechanism attribution**, not maximizing field.

---

## 7. Where the buried field actually sits

The positive field-excess support remains centered near

```math
\boxed{z\approx4.90\ \mu\mathrm m}
```

with an RMS support width of approximately

```math
\boxed{0.27\ \mu\mathrm m.}
```

For the middle `beta=3` member, the peak occurs at local composition approximately

```math
x\approx0.3500,
```

corresponding at 300 K to local gap wavelength

```math
\boxed{\lambda_g\approx3.46\ \mu\mathrm m.}
```

That lands in the same intermediate-depth spectral region selected independently by the abstract signal-weighted optimization.

---

## 8. Optical-kernel difference is now an explicit design tradeoff

The control and contrast devices intentionally have different **internal** composition profiles, so their wavelength-dependent generation kernels are not identical.

That is not itself a flaw: those kernels are the known forward operators used by the inverse.

But the profile must be measured accurately enough to model them.

Across the retained `2.80-3.83 um` band, the maximum normalized control/contrast timing-kernel difference is approximately

```text
beta=1 -> 6.7%
beta=3 -> 21.6%
beta=5 -> 38.8%.
```

Therefore increasing buried gradient strength buys stronger material contrast at the price of larger optical-model dependence.

This supports a **strength series** rather than one aggressive contrast device.

---

## 9. Finite-RF separation survives the constrained composition construction

Use

```text
f = 0.25, 0.50, 1, 2, 3 GHz
phase + log-magnitude
statistics-like or additive-like Pabs weighting.
```

Allow

```text
independent smooth quadratic bulk changes in control and contrast
+
a matched-contact nuisance whose same near-junction transport perturbation acts in both devices.
```

Use the positive buried field excess only as the candidate transport-support location.

For `beta=3`:

```text
statistics-like target-to-nuisance angle ~0.72 deg
additive-like angle ~0.74 deg.
```

The exact number remains conditional on the simple deterministic baseline and nuisance basis.

The important result is structural:

> **once the front environment is matched and the distinguishing region is buried near 4.9 um, the candidate response is no longer almost exactly collinear with a contact-like perturbation.**

That is the main purpose of the design.

---

## 10. Why a strength ladder is scientifically stronger

A single control/contrast pair can always be challenged by an uncontrolled fabrication difference.

A family such as

```text
beta=0 -> smooth control
beta=1 -> weak buried gradient
beta=3 -> intermediate buried gradient
beta=5 -> strong buried gradient
```

keeps the outer profile constraints fixed while changing one internal design coordinate systematically.

A successful validation would ask whether the recovered differential timing mode

```text
appears at the designed buried depth
and
changes systematically with buried-gradient strength.
```

That is a much stronger causal test than

```text
published sample A differs from published sample B.
```

It also creates an internal falsification route: a reconstructed feature that stays fixed while the designed buried gradient changes would argue against the proposed mechanism.

---

## 11. What is still not established

The family is a mathematically realizable monotonic `x(z)` construction, not a complete epitaxial design.

Still missing:

- growth feasibility and achievable composition-gradient control;
- doping and junction placement consistent with the assumed collection orientation;
- strain / defect consequences of redistributing `dx/dz`;
- a microscopic HgCdTe transport model connecting the buried field ladder to timing;
- actual interface and contact reproducibility;
- experimentally measured complex optical kernels;
- realistic RF covariance and electrical de-embedding.

Therefore the field values above are **design coordinates**, not performance predictions.

---

## 12. Next decisive work

The next theoretical step should no longer optimize an abstract transport feature.

Use the explicit `beta` family in a physical carrier-transport forward model and ask:

> **Does a monotonic buried-gradient redistribution of this magnitude produce a timing change large enough to detect, while avoiding high-field tunneling / impact-ionization / space-charge pathologies?**

The first model should remain deliberately minimal:

```text
composition-dependent band edges
self-consistent built-in field
reasonable high-field velocity saturation
local or nonlocal carrier transit
and current optical generation kernels.
```

Only if the `beta=1/3/5` ladder creates a measurable, monotonic timing response should a more detailed device simulation be justified.

Numerical implementation:

`numerics/hgcdte_matched_contact_composition_family.py`
