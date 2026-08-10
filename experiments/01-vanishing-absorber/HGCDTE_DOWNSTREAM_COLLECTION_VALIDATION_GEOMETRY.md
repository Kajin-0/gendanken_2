# Purpose-Built Validation Geometry — High-Gap Illumination, Low-Gap Collection

**Date:** 2026-08-09  
**Status:** conditional purpose-built geometry based on the repository's quasi-neutral p-type band-edge result plus a downstream-collection finite-RF design sweep; not a claim about the published Xu A/B carrier type or junction force direction; no fabrication prescription; no novelty claim

## 1. Why stop inheriting the published collection orientation?

The published A/B pair remains valuable as a real material/control system, but its distinguishing nonlinear region lies near the collecting boundary and is strongly confounded with contact/interface transport.

For a **purpose-built validation device**, the collection orientation itself is a design variable.

The strongest geometry should make three things compatible:

```text
wavelength-to-depth encoding
carrier drift direction
separation from the collecting contact.
```

That can be achieved more cleanly by illuminating from the high-gap side and collecting on the opposite low-gap side.

---

## 2. Start from a deliberately p-type quasi-neutral absorber

The repository previously derived, for a nondegenerate quasi-neutral p-type graded absorber,

```math
\boxed{
\frac{dE_v}{dz}
\simeq
k_BT\frac{d}{dz}\ln(N_A/N_v).
}
```

If

```math
N_A/N_v
```

is approximately constant through the active region, then

```math
\boxed{dE_v/dz\simeq0.}
```

and therefore

```math
\boxed{
\frac{dE_c}{dz}
\simeq
\frac{dE_g}{dz}.
}
```

This is a conditional quasi-neutral design relation, not a universal HgCdTe band-offset rule.

---

## 3. Choose the grading direction to align optics and electron collection

Let

```text
z=0
-> illuminated entrance
-> high Cd / high gap

z=L
-> collecting junction
-> low Cd / low gap.
```

Thus

```math
\boxed{dE_g/dz<0.}
```

Under the p-type pinning condition,

```math
\boxed{dE_c/dz<0.}
```

as well.

A minority electron lowers its conduction-band energy by moving toward increasing `z`, so the graded conduction-band slope drives it toward the **low-gap collector at `z=L`**.

This is the important design alignment:

```text
high-gap entrance
-> long wavelengths penetrate deeper

low-gap collector
-> minority electrons are driven in the same depth direction.
```

The force direction is now built into an explicit p-type thought-device assumption rather than inferred from `|dEg/dz|` alone.

---

## 4. Spectral position encoding survives this orientation

Because the gap decreases with depth, a photon with energy below the entrance gap but above a deeper local gap cannot be absorbed immediately at the entrance.

Its earliest allowed generation point moves deeper as wavelength increases.

That is exactly the desired internal spectral position encoder.

The optical physics therefore remains

```text
high-gap entrance
-> wavelength-dependent generation depth
-> long wavelength selects deeper / lower-gap material.
```

No reverse illumination or separate excitation-side access is required.

---

## 5. The timing inverse changes orientation

For collection at the downstream boundary `L`, the exact path-additive mean-delay kernel is the **CDF** rather than the survival function:

```math
\boxed{
\bar T_i
=
\int_0^L F_i(s)q(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

The common-delay boundary gauge now occurs near the **collector at `s=L`**, because

```math
F_i(L)=1
```

for every wavelength.

Therefore the mechanism-design rule remains the same in spirit:

> **do not place the distinguishing transport structure immediately adjacent to the collecting contact.**

The contact nuisance has simply moved to the low-gap side, where it can now be matched deliberately between control and contrast devices.

---

## 6. Reference control profile for the design sweep

Use

```text
L = 7.6 um
x(0) = 0.40 at illuminated entrance
x(L) = 0.32 at low-gap collector
linear x(z).
```

This produces a weak baseline composition-gradient field around

```text
~142 V/cm
```

near the middle of the layer at 300 K.

The profile is a validation coordinate, not an optimized detector design.

---

## 7. Downstream finite-RF Jacobian

For deterministic baseline transit

```math
T_0(z)=\frac{L-z}{v_0},
```

a small local delay perturbation is integrated only over the path from the generation point to the collector.

The finite-RF Jacobian therefore uses the downstream path overlap rather than the front-directed overlap used in the published-device calculations.

The measurement sweep uses

```text
lambda = 2.80-3.83 um
f = 0.25, 0.50, 1, 2, 3 GHz
phase + log-magnitude
```

with wavelength-independent complex response removed separately at each RF frequency.

---

## 8. Mechanism nuisance basis

Project each candidate buried feature against

```text
smooth bulk:
1, z/L, (z/L)^2

collecting-contact-like:
exp[-(L-z)/ell_c]
with ell_c = 0.2, 0.5, 0.75, 1.0 um.
```

This is the correct contact orientation for collection at `L`.

Evaluate equal-noise, statistics-like and additive-like absorbed-signal weightings.

---

## 9. Broad-feature optimum

Allow Gaussian transport support widths

```text
0.20, 0.35, 0.50, 0.75, 1.00 um.
```

With realistic signal weighting, the globally strongest feature in the present grid is broad:

```math
\boxed{
\sigma_z\approx1.0\ \mu\mathrm m,
\qquad
z_0\approx2.75\ \mu\mathrm m.
}
```

Target-to-contact/bulk nuisance angle:

```text
statistics-like ~3.26 deg
additive-like ~2.93 deg.
```

That is a substantially cleaner mechanism geometry than the published-like near-contact feature.

---

## 10. Narrow-feature optimum

A purpose-built composition-gradient perturbation may be narrower than `1 um`, so examine a fixed

```math
\sigma_z=0.50\ \mu\mathrm m
```

transport support.

Both realistic weighting models select

```math
\boxed{z_0\approx3.50\ \mu\mathrm m.}
```

The corresponding target-to-nuisance angle is approximately

```text
statistics-like ~2.17 deg
additive-like ~1.88 deg.
```

For the linear control profile, this depth has approximately

```text
x ~0.363
local 300 K gap wavelength ~3.30 um.
```

That is comfortably inside the strong-signal part of the optical scan rather than at the cutoff edge.

---

## 11. Moving the feature away from the collector produces a large information gain

Compare the same `0.50 um` feature at

```text
near-contact center ~6.75 um
```

and at the buried optimum

```text
center ~3.50 um.
```

After nuisance projection:

```text
statistics-like:
recoverable amplitude gain ~13.4x
-> information gain ~178x

additive-like:
recoverable amplitude gain ~12.9x
-> information gain ~165x.
```

Thus the purpose-built downstream geometry gains roughly two orders of magnitude in mechanism information simply by moving the distinguishing feature away from the contact while keeping it in a spectrally well-encoded region.

---

## 12. Why this geometry is stronger than the earlier front-collection thought device

The previous matched-contact construction improved contact separation but still had to treat the magnitude of the gap-gradient field as an assumed collection-assisting field because the carrier/band-edge direction was not specified.

The downstream p-type design removes that ambiguity at the **design-assumption level**:

```text
p-type quasi-neutral absorber
+
high-gap entrance
+
low-gap collector
+
valence-band pinning
-> conduction-band slope drives minority electrons toward collector.
```

It also keeps the optical spectral gate in its natural high-gap-to-low-gap direction.

This makes it the preferred purpose-built validation architecture to develop further.

---

## 13. What remains to be designed

The Gaussian support is still an abstract transport coordinate.

The next construction should use an explicit monotonic composition profile that

```text
keeps the low-gap collecting-side composition and gradient matched
keeps the collection contact/junction stack matched
preserves the same x(0), x(L), and thickness
adds a buried gradient enhancement around ~3.5 um
and places the compensating gradient reduction BEFORE the feature,
so carriers generated at/after the feature do not traverse the compensation on the way to z=L.
```

That is the downstream mirror of the previous front-collection compensation logic.

---

## 14. Next decisive calculation

Construct a downstream-collection gradient-strength ladder and verify

```text
strict monotonic x(z)
collector-side profile matching
band-edge force direction under the p-type assumption
optical kernel changes
mechanism separation
and drift-diffusion timing response.
```

The highest-value validation experiment is now conceptually:

```text
same p-type low-gap collector/contact stack
same high-gap entrance and endpoints
same thickness
several designed buried-gradient strengths near ~3.5 um
wavelength x RF complex response
and a smooth-gradient control.
```

A systematic timing response that appears at the designed internal coordinate and scales with buried-gradient strength would be a far stronger causal validation than the existing published A/B contrast alone.

Numerical implementation for the present geometry sweep:

`numerics/hgcdte_downstream_collection_buried_feature_design.py`
