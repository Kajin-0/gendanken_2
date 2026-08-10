# Sample-A Constraint Family — Robustness of a Common A/B Temperature Iso-Kernel Schedule

**Date:** 2026-08-09  
**Status:** conditional sensitivity calculation using the published 2023 sample-A fit law and textual constraints; **not** a digitization or calibrated reconstruction of sample A; Beer-Lambert optics only; no novelty claim

## 1. Purpose

The paired temperature experiment requires samples A and B to be illuminated at the **same wavelength** so arbitrary common tunable-source phase cancels.

The earlier sample-B-only calculation showed that several mid/deep timing kernels can be reproduced closely at lower temperature by wavelength retuning, but exact joint A/B feasibility remained OPEN because the numerical sample-A composition fit is embedded graphically in the 2023 article.

This note asks a narrower question that can be answered without pretending the missing curve is known:

> **Across a broad family of sample-A profiles constrained by the published fit law and textual sample-A facts, does a useful common A/B temperature iso-kernel wavelength remain stable?**

If the answer is yes, exact sample-A digitization remains necessary for a calibrated A inverse but is no longer a hard prerequisite for deciding whether the mid/deep paired temperature control is structurally plausible.

---

## 2. What the primary 2023 article actually gives

Primary source:

G.-Q. Xu et al., `Photoelectric characteristics of compositionally graded HgCdTe detector`, *Journal of Infrared and Millimeter Waves* **42** (2023) 285-291, DOI `10.11972/j.issn.1001-9014.2023.03.001`.

The article gives the longitudinal fit form

```math
\boxed{
x(z)
=x_s+s(d-z)
+(1-x_s-sd)
\left\{
1-\left[
\operatorname{erf}\!\left(\frac{2z}{\Delta z}\right)
\right]^3
\right\}.
}
```

It defines

```text
z       distance from the substrate interface
x_s     epitaxial growth-surface composition
d       epitaxial thickness
s       linear composition gradient
Delta z interdiffusion-region width.
```

The composition-gradient field is calculated from

```math
\boxed{
E=\frac{1}{q}\frac{dE_g}{dz}
}
```

using the Hansen-Schmit-Casselman gap relation.

For the A/B devices the text further reports

```text
FTIR-derived nominal x:
A ~0.320
B ~0.316

nonlinear interdiffusion-region thickness:
~4 um

processed thickness:
A ~7.6 um
B ~3.7 um

sample A:
retains part of nonlinear composition region

sample B:
nonlinear region removed

linear-region gradient:
A larger than B

linear-gradient built-in fields at 115/215/300 K:
both in ~100-200 V/cm range
A-B difference at the same temperature ~30 V/cm

processed sample-A nonlinear surface field:
up to ~2000 V/cm.
```

The paper also reports clear interference structure near sample A's cutoff and attributes it to the thicker absorber and internal reflections. This is important because a simple Beer-Lambert model is least trustworthy exactly where the deepest optical kernel is most localized.

---

## 3. What is still unavailable

The accessible article text does **not** expose the fitted numerical tuples

```math
(x_s,d,s,\Delta z)_A,
\qquad
(x_s,d,s,\Delta z)_B
```

as machine-readable values.

The numerical curves are embedded in Fig. 3.

Therefore this note does **not** claim to recover the real sample-A `x(z)`.

The purpose is only to ask whether the proposed common-wavelength temperature control is sensitive to the unresolved A-profile degrees of freedom.

---

## 4. Explicit sample-A sensitivity family

Use the published functional form after interface removal.

The remaining processed thickness is

```math
W_A=7.6\ {\rm um},
```

so if the original-coordinate cut occurs at `z_cut`, then

```math
d=z_{\rm cut}+W_A.
```

### Conditional endpoint convention

As in the existing sample-B envelope, conditionally interpret the reported FTIR nominal value

```math
x_A=0.320
```

as the low-Cd growth-surface endpoint `x_s`.

This is an explicit modeling assumption, not a recovered fit parameter.

### Linear-field family

The article states that both A and B linear-region fields lie in `100-200 V/cm`, while A exceeds B by approximately `30 V/cm` at the same temperature.

Use sample-A 300 K sensitivity values

```text
130, 150, 180, 200 V/cm.
```

The local linear slope is set through

```math
E_{\rm lin}
=\left|\frac{dE_g}{dx}\frac{dx}{dz}\right|.
```

### Interdiffusion-width sensitivity

The article says the nonlinear region is close to `4 um` thick.

Use

```text
Delta z = 3.5, 4.0, 4.5 um.
```

The `+/-0.5 um` span is a **sensitivity range**, not a reported uncertainty interval.

### Surface-field sensitivity

The article reports the processed A surface field reaching approximately

```math
2000\ {\rm V/cm}.
```

Use

```text
1800, 2000, 2200 V/cm
```

as a sensitivity span, again **not** as an experimental error bar.

### Do not choose the surface-field branch from prose

For the nonlinear fit, a specified surface-field magnitude can occur on both the rising and falling sides of the nonlinear field profile.

Both mathematical roots are retained.

The resulting family contains

```math
\boxed{72\ \text{sample-A sensitivity profiles}.}
```

Across this deliberately broad family:

```text
processed front composition x_front ~0.456-0.988
original-coordinate cut z_cut ~0.375-3.089 um.
```

The very large front-composition spread is useful: the calculation does not quietly assume one graphical reading of Fig. 3.

---

## 5. Optical model

Use the same optical physics as the current sample-B calculation:

```text
Hansen-Schmit-Casselman Eg(x,T)
Moazzami above-gap alpha(E,x,T)
front illumination
conditional Beer-Lambert generation density
cell-integrated front-collection survival kernels
80 spatial cells.
```

For sample B retain the current central envelope

```text
W_B = 3.7 um
x_low = 0.316
300 K linear field = 150 V/cm.
```

Important omissions:

```text
reflection
thin-film interference
Urbach-tail absorption
free-carrier optical effects.
```

The interference omission is a substantially larger concern for sample A than for sample B because the primary 2023 experiment directly observes interference near A's cutoff.

---

## 6. Joint iso-kernel objective

For common 300 K reference wavelength `lambda_0`, define each device's normalized kernel error at lower temperature:

```math
\epsilon_A(T,\lambda)
=\frac{
\|\mathbf A_A(T,\lambda)-\mathbf A_A(300,\lambda_0)\|_2
}{
\|\mathbf A_A(300,\lambda_0)\|_2
},
```

```math
\epsilon_B(T,\lambda)
=\frac{
\|\mathbf A_B(T,\lambda)-\mathbf A_B(300,\lambda_0)\|_2
}{
\|\mathbf A_B(300,\lambda_0)\|_2
}.
```

Use equal device weights:

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\left[
\epsilon_A^2(T,\lambda)
+\epsilon_B^2(T,\lambda)
\right].
}
```

The optimization is repeated independently for all 72 A-profile family members.

---

## 7. Result — `3.410 um` common reference

At 300 K:

```text
A modeled Pabs ~0.738-0.874
B modeled Pabs ~0.886.
```

### 215 K

```text
joint lambda        3.520559-3.521797 um
A kernel mismatch   0.754-1.250 %
B kernel mismatch   2.453-2.460 %
A Pabs               0.659-0.811
B Pabs               0.821-0.822.
```

### 115 K

```text
joint lambda        3.658486-3.662135 um
A kernel mismatch   1.561-2.583 %
B kernel mismatch   5.081-5.099 %
A Pabs               0.537-0.697
B Pabs               0.703-0.706.
```

This band has strong signal but only approximate optical invariance, especially for B at 115 K.

---

## 8. Result — `3.632 um` common reference

At 300 K:

```text
A modeled Pabs ~0.350-0.485
B modeled Pabs ~0.560.
```

### 215 K

```text
\boxed{
\lambda_*=3.793356\text{-}3.793566\ {\rm um}
}
```

with

```text
A kernel mismatch   0.215-0.229 %
B kernel mismatch   0.447-0.453 %
A Pabs               0.290-0.410
B Pabs               ~0.474.
```

### 115 K

```text
\boxed{
\lambda_*=4.004157\text{-}4.004870\ {\rm um}
}
```

with

```text
A kernel mismatch   0.400-0.445 %
B kernel mismatch   0.857-0.873 %
A Pabs               0.213-0.309
B Pabs               0.357-0.358.
```

The striking feature is not merely the small mismatch.

The optimized wavelength itself moves by only about

```text
0.00021 um across the full A family at 215 K
0.00071 um across the full A family at 115 K.
```

Thus the mid/deep common-wavelength schedule is very weakly sensitive to the unresolved sample-A profile within this explicit family.

---

## 9. Result — `3.840 um` common reference

Mathematically this is the cleanest kernel match.

At 300 K:

```text
A Pabs ~0.030-0.045
B Pabs ~0.131.
```

### 215 K

```text
joint lambda        4.041975-4.042093 um
A kernel mismatch   0.046-0.057 %
B kernel mismatch   0.053-0.063 %
A Pabs               0.024-0.037
B Pabs               ~0.106.
```

### 115 K

```text
joint lambda        4.309101-4.309402 um
A kernel mismatch   0.115-0.144 %
B kernel mismatch   0.136-0.156 %
A Pabs               0.017-0.027
B Pabs               ~0.076.
```

This is an important experimental rejection:

> **the deepest kernel is not automatically the best paired temperature measurement.**

Its optical invariance is exceptional, but sample A becomes signal starved and this is also the spectral region where the primary experiment reports interference.

---

## 10. Strongest provisional joint temperature band

Within the present Beer-Lambert model, the best first common-wavelength temperature probe is therefore not the deepest `3.840 um` reference.

The stronger compromise is

```math
\boxed{
300\ {\rm K}:\ 3.632\ {\rm um}
}
```

```math
\boxed{
215\ {\rm K}:\ \sim3.7935\ {\rm um}
}
```

```math
\boxed{
115\ {\rm K}:\ \sim4.0045\ {\rm um}.
}
```

It combines

```text
sub-percent full-kernel mismatch in both devices
+
moderate absorbed signal in both devices
+
very weak sensitivity of the optimized wavelength to the unresolved A profile.
```

This is a **provisional experimental-design result**, not a calibrated wavelength prescription.

---

## 11. Why the result is unexpectedly robust

The unresolved part of sample A is concentrated near its high-Cd processed front.

For the mid/deep wavelengths used here, that high-gap region contributes relatively little absorption; generation is weighted mainly toward the lower-Cd portion deeper in the absorber.

Consequently, even the two mathematically different surface-field branches produce nearly the same mid/deep optical timing kernels.

This explains why the common temperature wavelength is far less sensitive to the uncertain high-Cd front profile than a shallow/short-wave mode would be.

This interpretation is conditional on the present absorption model.

---

## 12. What changes in the project

The earlier statement

```text
joint A/B iso-kernel feasibility is completely blocked until the exact sample-A x(z) is recovered
```

is now too strong.

A better statement is:

> **The exact A profile remains required for calibrated A transport inversion, shallow-mode design, and final uncertainty propagation, but the existence and approximate wavelength of a useful mid/deep common A/B temperature kernel are robust across the current text-constrained A-profile family.**

This removes one theoretical feasibility blocker.

It does **not** remove the optical-model blocker created by sample-A interference.

---

## 13. Claim boundary

### KNOWN from the primary 2023 source

- sample-A processed thickness is approximately `7.6 um`;
- sample-B processed thickness is approximately `3.7 um`;
- the nonlinear interdiffusion region is approximately `4 um` thick;
- A retains part of that region while B removes it;
- A's linear gradient exceeds B's;
- both linear-region fields are in the `100-200 V/cm` range over the reported temperatures and differ by about `30 V/cm` at equal temperature;
- processed A has a nonlinear surface field up to roughly `2000 V/cm`;
- sample A exhibits interference near cutoff.

### CHECKED NUMERICALLY / CONDITIONAL

For the explicit 72-member sensitivity family, current Hansen/Moazzami Beer-Lambert optics, and central sample-B envelope:

- a `3.632 um` 300 K reference has a common lower-temperature wavelength near `3.7935 um` at 215 K and `4.0045 um` at 115 K;
- the optimized wavelength is extremely insensitive to the stated sample-A family;
- both A and B retain sub-percent kernel mismatch for that band;
- the `3.840 um` reference is more exactly kernel matched but is signal starved in sample A.

### NOT ESTABLISHED

- the actual fitted sample-A profile;
- the actual sample-A `x_s,d,s,Delta z` parameters;
- an experimental uncertainty interval for the sensitivity family;
- an interference-corrected sample-A kernel;
- actual A/B absorbed optical powers;
- actual joint phase covariance;
- transport contrast;
- novelty / priority.

---

## 14. Next decisive work

The next optical calculation should no longer wait passively for Fig. 3.

Priority is now:

1. add **interference-aware / transfer-matrix optics** for sample A and test whether the `3.632 -> 3.7935 -> 4.0045 um` joint schedule survives;
2. recover/digitize Fig. 3 when a usable image/PDF becomes available and collapse the sensitivity family to the real fitted profile;
3. measure or model the two-arm differential phase covariance at the candidate common wavelengths and adaptive RF frequencies;
4. only then optimize wavelength × RF frequency × averaging time for the paired temperature experiment.

The exact sample-A profile remains important, but the present result shifts the immediate feasibility risk toward **sample-A interference and differential phase metrology**.

---

## 15. Reproducibility

Deterministic regression:

`numerics/hgcdte_sample_a_constraint_family_joint_iso_kernel.py`
