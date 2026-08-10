# Matched-Contact Translated-Gradient Validation Design

**Date:** 2026-08-10  
**Status:** conditional purpose-built device-design study; self-consistent monotonic composition profiles with matched endpoints; finite-RF deterministic-transit forward model; no fabrication claim and no novelty claim

## 1. Why the published A/B pair is no longer the strongest causal experiment

The preceding mechanism-confounding test found that the published sample-A near-junction timing fingerprint can be reproduced very closely by a generic near-junction/contact contribution plus smooth bulk transport changes.

That is not merely a phase-noise problem. It is a **mechanism-identifiability problem**.

The most direct way to attack it is to design the material pair so the suspected internal mechanism moves while the contact does not.

The validation question becomes

> **If the internal nonlinear-gradient region is translated in depth while the collection-side composition/contact stack and total composition change remain fixed, does the wavelength × RF fingerprint translate in the way predicted by the spectral-position encoder?**

That is a stronger causal test than

```text
sample A differs from sample B.
```

---

## 2. Mean-preserving translated composition-gradient profile

Use a conceptual `7.6 um` absorber with fixed endpoint compositions

```text
x(0) = 0.55
x(L) = 0.32.
```

These are design coordinates, not measured values for a fabricated device.

Let

```math
g(z;z_0,\sigma)
=\exp\!\left[-\frac{(z-z_0)^2}{2\sigma^2}\right].
```

Instead of adding composition directly, modulate the **composition-slope magnitude**:

```math
\boxed{
s(z)
=s_0\left[1+a\left(g(z)-\langle g\rangle\right)\right]
}
```

with

```math
s_0=\frac{x(0)-x(L)}{L}.
```

Then define

```math
\boxed{
x(z)=x(0)-\int_0^z s(u)\,du.
}
```

Because

```math
\int_0^L[g(z)-\langle g\rangle]dz=0,
```

the endpoint compositions remain identical for every translated feature:

```text
same front composition
same back composition
same total composition change
same nominal absorber thickness.
```

For the current first design use

```text
sigma = 0.35 um
a = 4.
```

The profile remains monotonic.

---

## 3. The translated feature naturally reproduces the relevant field scale

Using the Hansen gap gradient

```math
F_{\rm grad}(z)
=\left|\frac{dE_g}{dx}\frac{dx}{dz}\right|,
```

the translated profiles produce approximately

```text
surrounding/background gradient field ~220 V/cm
local buried maximum ~1.9 kV/cm.
```

For the eventual optimal pair on the tested grid:

```text
feature center 2.6 um -> max ~1907 V/cm
feature center 3.2 um -> max ~1899 V/cm.
```

Thus the design moves a field-enhancement scale comparable to the `~2 kV/cm` nonlinear-region scale that motivated the original sample-A branch while keeping the endpoints fixed.

This is still a **conceptual composition design**, not a claim that a particular growth/anneal process can yet fabricate the profile with those exact tolerances.

---

## 4. Measurement model

The current stress uses

```text
lambda = 2.00-2.80 um, 0.01 um spacing
f = 0.25, 0.50, 1, 2, 3 GHz
phase + ln|H|
finite-RF deterministic-transit Jacobian
baseline v0 = 1e5 m/s
illustrative 25% support-shaped transport perturbation.
```

The sign and `25%` magnitude are not device predictions.

The purpose is to compare **mechanism geometry** under one fixed perturbation scale.

At each RF frequency a wavelength-independent complex response is projected out.

---

## 5. The short-wave optical encoder remains strong for the purpose-built pair

For the selected `2.6 / 3.2 um` feature-center pair, the current Beer-Lambert model gives

```text
minimum Pabs over both devices and 2.00-2.80 um > 0.996
minimum |H| over 0.25-3 GHz > 0.987.
```

Representative mean generation depths are approximately

### Feature centered at `2.6 um`

```text
2.00 um -> 2.06 um
2.80 um -> 4.11 um.
```

### Feature centered at `3.2 um`

```text
2.00 um -> 2.15 um
2.80 um -> 4.49 um.
```

The wavelength scan therefore sweeps the conditional generation distribution across the buried feature locations while both devices remain strongly absorbing.

---

## 6. Matched nuisance model

The purpose-built comparison is valuable only if the two devices are genuinely matched outside the translated internal feature.

Represent residual **common** matched bulk/contact transport changes by

```math
1,
\quad z/L,
\quad (z/L)^2,
\quad (z/L)^3,
```

plus effective near-junction shapes

```math
\exp(-z/0.30),
\quad
\exp(-z/0.50),
\quad
\exp(-z/0.75),
\quad
\exp(-z/1.00).
```

The same nuisance amplitude acts in both devices.

Because the optical kernels differ slightly, the differential nuisance response is not zero. It is

```math
\boxed{
\delta y_{\rm common}
=(J_2-J_1)q_{\rm nuisance}.
}
```

This is deliberately more conservative than assuming perfect cancellation.

---

## 7. Grid search finds a strong translated pair

Sweep feature centers

```text
0.8-3.2 um in 0.2 um steps
```

with separation at least `0.4 um`.

On this explicit grid, the **same pair** maximizes both

```text
principal angle from the common matched-nuisance span
and
absolute nuisance-orthogonal complex-response norm.
```

The optimum is

```math
\boxed{
2.6\ {\rm um}
\rightarrow
3.2\ {\rm um}.
}
```

For the illustrative transport perturbation:

```text
1-GHz differential phase peak-to-peak ~0.145 deg.
```

That is already above the current `~0.1 deg` phase scale before using the other RF frequencies or magnitude response.

---

## 8. The key result — matched fabrication rotates the target away from contact/bulk nuisance

For the `2.6 / 3.2 um` pair:

### Full complex wavelength × RF response

Against the shared matched nuisance span,

```math
\boxed{
\theta_{\rm matched}^{\rm complex}
\approx5.48^\circ
}
```

with nuisance-orthogonal complex-response norm

```math
\boxed{0.002459.}
```

### Phase only

```math
\boxed{
\theta_{\rm matched}^{\rm phase}
\approx2.00^\circ
}
```

with residual phase-vector norm

```math
\boxed{0.0514^\circ.}
```

These are far larger mechanism-separation angles than the near-junction published-A branch produced under flexible contact/bulk confounding.

The important change is not merely moving the feature deeper.

It is **moving the same internal feature while keeping the boundary conditions matched**.

---

## 9. Matching is an identifiability condition

Now perform an adversarial stress in which the smooth/contact nuisance amplitudes are allowed to vary independently in the two devices.

Then the same `2.6 / 3.2 um` target falls to

```text
complex principal angle ~0.0656 deg
phase-only principal angle ~0.0273 deg.
```

Thus the gain disappears if the two devices are treated as unrelated samples.

This gives a very strong design rule:

> **The experiment is not merely “make two graded devices.” It is “make a matched pair in which the internal gradient feature is intentionally translated while the contact/cap/junction and broad process variables are held common.”**

Without that matching, the inverse again becomes nearly non-identifiable.

---

## 10. Provisional phase/noise resource

Under the explicitly optimistic convention that phase and `ln|H|` components each have equal independent noise corresponding to `0.10 deg` in radians, the matched-pair complex residual gives

```text
SNR ~1.41
```

for the current dense wavelength × RF data set.

A `3 sigma` no-prior detection would require an equivalent per-component noise of approximately

```math
\boxed{0.047^\circ}
```

or about

```text
~4.5x
```

more white-noise integration resource than the `0.10 deg` reference.

Using phase only gives a stricter provisional requirement:

```math
\boxed{
\sigma_\phi\lesssim0.017^\circ
}
```

or about

```text
~34x
```

more white-noise integration.

These are not yet instrument specifications because the real phase/magnitude covariance is still unmeasured.

The important point is qualitative but quantitative enough to guide the next step:

> **with matched nuisances, the translated-gradient design moves the problem from an essentially structural degeneracy into a demanding but finite measurement-precision problem.**

---

## 11. Strongest current validation architecture

A useful physical program is now a matched **three-device family** rather than relying solely on the published A/B pair.

### `C` — smooth/end-point-matched control

```text
same front composition/cap/contact
same back composition
same thickness
smooth internal grading.
```

### `G1` — translated-gradient device 1

```text
same endpoints/contact stack
buried nonlinear-gradient enhancement at z1.
```

### `G2` — translated-gradient device 2

```text
same endpoints/contact stack
same feature width/amplitude
feature translated to z2.
```

Then use two distinct observables:

```text
G - C
-> high-signal detection that an additional internal transport component exists

G2 - G1
-> causal relocation test: does the spectral/RF fingerprint move with the
   internal feature rather than remaining attached to the contact/interface?
```

The second observable is the stronger mechanism test.

---

## 12. Why this is stronger than simply improving sample-A phase precision

The original published-A branch had three linked problems:

```text
feature close to collecting boundary
common-delay gauge
contact/interface mechanism confounding.
```

The translated-gradient pair attacks all three by experimental design:

```text
bury the feature in a spectrally addressable region
hold the collection boundary fixed
translate the suspected mechanism itself.
```

This does not prove that the composition-gradient field will produce a measurable transport change in a real device.

It creates a substantially cleaner experiment **if** such a change exists.

---

## 13. Hard claim boundary

Do not claim yet that

```text
2.6 and 3.2 um are fabrication-optimal positions
```

or that

```text
a=4, sigma=0.35 um is a realizable growth profile.
```

The current result is conditional on

```text
Hansen gap
Moazzami Beer-Lambert absorption
chosen endpoint compositions
finite-RF deterministic baseline transport
illustrative 25% transport perturbation
chosen nuisance family
and idealized matched nuisance amplitudes.
```

The `2.6 / 3.2 um` result is the optimum **on the stated numerical grid**, not a universal optimum.

---

## 14. Next decisive work

The next calculation should not be another generic wavelength search.

It should quantify **how well the two translated-gradient devices must actually be matched**.

Specifically:

> **Introduce differential fabrication mismatch in front composition, contact time constant, feature position/width, and smooth background gradient, then determine the tolerances required for the `~5.5 degree` matched-nuisance separation to survive.**

After that, the purpose-built profile needs a materials-growth/anneal feasibility audit and a focused prior-art search for translated or position-controlled composition-gradient HgCdTe validation structures.

Numerical implementation:

`numerics/hgcdte_matched_contact_translated_gradient_design.py`
