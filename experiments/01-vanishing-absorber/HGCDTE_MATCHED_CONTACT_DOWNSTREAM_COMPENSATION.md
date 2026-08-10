# Matched-Contact Buried Gradient — Put the Endpoint Compensation Behind the Feature

**Date:** 2026-08-09  
**Status:** improved monotonic endpoint-matched composition construction; preserves the carrier path from the buried feature to the collecting contact more cleanly than the earlier broad-compensation family; no fabrication/transport prediction; no novelty claim

## 1. Correction to the first matched-contact composition family

The first explicit composition family preserved the front contact region extremely well, but its compensating reduction in composition gradient began near `1.5 um`.

For collection at the front (`z=0`), a carrier generated around the buried feature at `z~4.9 um` then traverses

```text
the intended high-gradient region
and
part of the compensating low-gradient region
```

on its way to the junction.

That weakens the causal interpretation of the timing perturbation.

The smarter construction is:

> **put the compensating gradient reduction behind the feature, toward the back side.**

Then carriers generated at or before the buried feature experience the enhanced region but do not traverse the compensation on their path to collection.

---

## 2. Control structure

Retain

```text
L = 7.6 um
x_front = 0.40
x_back = 0.32
linear control profile
median composition-gradient field ~142 V/cm.
```

The same front/contact/junction stack is assumed for control and contrast.

---

## 3. Improved derivative redistribution

Use

```math
w_\beta(z)
=1+\beta G(z)-c_\beta H_{\rm back}(z),
```

with buried enhancement

```math
G(z)
=\exp\left[-\frac{(z-4.90)^2}{2(0.20)^2}\right]
```

and a smooth back-side compensation window

```math
H_{\rm back}(z)
=\frac12
\left[
1+\tanh\left(\frac{z-5.70}{0.12}\right)
\right].
```

Choose

```math
c_\beta
=\beta\frac{\int Gdz}{\int H_{\rm back}dz}
```

so

```math
\int_0^L w_\beta dz=L.
```

Then

```math
\frac{dx_\beta}{dz}
=-\frac{\Delta x}{L}w_\beta(z)
```

preserves both composition endpoints exactly.

---

## 4. The collection-side path is now essentially identical

For the strongest current member `beta=3`:

```text
maximum composition mismatch in first 1 um:
machine-zero at current numerical resolution

maximum composition mismatch through z=4.2 um:
~3.6e-6.
```

Thus almost the entire path from the collecting contact to the vicinity of the buried feature remains the same as the control.

This is a much stronger matched-contact condition than merely matching `x_front`.

---

## 5. Strictly monotonic field ladder

The back-compensation coefficient is approximately

```math
c_\beta\approx0.26386\beta.
```

Hence strict monotonicity requires approximately

```math
\boxed{\beta<3.79.}
```

Use the diagnostic ladder

```text
beta = 0 -> smooth control
beta = 1
beta = 2
beta = 3.
```

The buried 300 K composition-gradient peaks are approximately

```text
beta=1 -> 284 V/cm
beta=2 -> 425 V/cm
beta=3 -> 567 V/cm.
```

The compensating back-side minima are

```text
104 V/cm
67 V/cm
30 V/cm,
```

respectively.

These fields are design coordinates, not predictions of drift velocity.

---

## 6. Spatial support remains at the desired buried coordinate

Using only the positive gradient-field excess relative to the control as a support template:

```text
centroid ~4.90 um
RMS width ~0.20 um.
```

The feature is therefore both

```text
well separated from the contact
and
well separated from the compensation region behind it.
```

---

## 7. Optical-model tradeoff

The profiles have identical endpoints but intentionally different internal `x(z)`, so their optical kernels differ.

Maximum normalized control/contrast timing-kernel difference over the retained `2.80-3.83 um` band is approximately

```text
beta=1 -> 8.2%
beta=2 -> 15.7%
beta=3 -> 22.6%.
```

This means the internal profile must be measured accurately enough to construct the correct optical forward matrix.

The optical difference is **not** itself a mechanism confound if the profile is independently characterized; it is part of the known spectral encoder.

---

## 8. Mechanism separation improves substantially

Use finite-RF complex data

```text
0.25, 0.50, 1, 2, 3 GHz
phase + log-magnitude
```

and project the candidate buried response against

```text
independent smooth quadratic bulk changes in control and contrast
+
a matched-contact nuisance whose same near-junction perturbation acts in both devices.
```

With statistics-like absorbed-signal weighting:

```text
beta=1 -> principal angle ~1.91 deg
beta=2 -> ~1.69 deg
beta=3 -> ~1.46 deg.
```

With additive-like weighting:

```text
~1.51, 1.40, 1.40 deg.
```

These angles are still not large enough to call the mechanism self-identifying from timing alone.

But they are dramatically cleaner than the published-like near-junction geometry, where a contact term plus smooth bulk changes could reduce the target-to-nuisance angle to around `0.01 deg` or less.

---

## 9. Why the weaker members may be experimentally attractive

Increasing `beta` strengthens the material contrast but also

```text
increases optical-kernel difference
reduces the compensating back-side field
and pushes the local transport farther from the low-field regime.
```

The `beta=1` member is therefore scientifically valuable even though its buried field is only `~284 V/cm`:

```text
front path essentially identical
max optical-kernel change only ~8%
strongest mechanism angle of the current ladder
and a clean intermediate perturbation relative to the control.
```

A dose-response series can test all three members rather than choosing one before the transport physics is known.

---

## 10. This supersedes the broad-compensation construction

`HGCDTE_MATCHED_CONTACT_COMPOSITION_FAMILY.md` remains useful provenance because it proved that endpoint matching and a buried gradient are compatible.

But its compensation begins too early for the cleanest carrier-path interpretation.

Current preferred thought-device family:

```text
buried enhancement center ~4.90 um
sigma ~0.20 um
compensation begins ~5.70 um
beta=0,1,2,3
same front profile/path to the feature
same endpoints
strict monotonicity.
```

---

## 11. Next collision — transport model dependence

The remaining question is no longer whether the profile can be constructed geometrically.

It is:

> **What timing change does this field redistribution actually cause?**

That cannot be answered by assuming local speed is proportional to field.

At fixed endpoint bandgap drop, a deterministic drift-only model penalizes low-field compensation, while drift-diffusion can behave differently because diffusion and boundary conditions matter.

The next calculation should therefore compare at least

```text
deterministic local drift
vs
Einstein drift-diffusion first passage
```

before any claim is made about the sign or magnitude of the timing response.

Numerical implementation:

`numerics/hgcdte_matched_contact_downstream_compensation.py`
