# Paired A/B Temperature Design — Joint Iso-Kernel Constraint

**Date:** 2026-08-09  
**Status:** experimental-design correction; exact paired-source cancellation algebra, but joint iso-kernel feasibility remains open until sample-A optical profile is recovered; no novelty claim

## 1. Two individually strong controls do not combine automatically

Two promising ideas now exist:

1. **simultaneous A-B differential phase**, which cancels arbitrary wavelength-dependent common source phase when both devices see the same modulated source;
2. **temperature iso-kernel retuning**, which changes wavelength with temperature so one device's optical timing kernel remains approximately fixed.

It is tempting to combine them immediately into a clean temperature difference-in-differences experiment.

That is not generally valid.

The reason is simple:

> **source-phase cancellation requires a common wavelength for A and B, whereas exact iso-kernel matching generally requires a device-specific wavelength because A and B have different composition profiles.**

---

## 2. Paired phase at one common wavelength

At temperature `T` and common source wavelength `lambda`, after stable arm calibration the simultaneous device contrast is

```math
\boxed{
\Delta_{AB}\phi(T,\lambda)
=-\Omega
\left[
\mathbf A_A(T,\lambda)\mathbf q_A(T)
-
\mathbf A_B(T,\lambda)\mathbf q_B(T)
\right]
+\Delta c(T).
}
```

The arbitrary source phase cancels because both devices are driven coherently at the **same** `(T,lambda,Omega)`.

This remains a strong experimental advantage.

---

## 3. Temperature difference-in-differences

For reference condition `(T_0,lambda_0)` and comparison `(T,lambda)`, define

```math
\boxed{
D_{AB,T}
=
\Delta_{AB}\phi(T,\lambda)
-
\Delta_{AB}\phi(T_0,\lambda_0).
}
```

Expanding,

```math
D_{AB,T}
=-\Omega
\Big[
\mathbf A_A(T,\lambda)\mathbf q_A(T)
-
\mathbf A_B(T,\lambda)\mathbf q_B(T)
-
\mathbf A_A(T_0,\lambda_0)\mathbf q_A(T_0)
+
\mathbf A_B(T_0,\lambda_0)\mathbf q_B(T_0)
\Big]
+
\Delta_T\Delta c.
```

This is **not** a pure transport difference unless the optical kernels are controlled or modeled.

---

## 4. Exact joint iso-kernel condition

The ideal single common comparison wavelength would satisfy simultaneously

```math
\mathbf A_A(T,\lambda_*)
\approx
\mathbf A_A(T_0,\lambda_0),
```

and

```math
\mathbf A_B(T,\lambda_*)
\approx
\mathbf A_B(T_0,\lambda_0).
```

Because A and B have different composition profiles, there is no reason a priori that one `lambda_*` can satisfy both.

Define normalized row errors

```math
\epsilon_A^2(T,\lambda)
=
\frac{
\|\mathbf A_A(T,\lambda)-\mathbf A_A(T_0,\lambda_0)\|_2^2
}{
\|\mathbf A_A(T_0,\lambda_0)\|_2^2
},
```

```math
\epsilon_B^2(T,\lambda)
=
\frac{
\|\mathbf A_B(T,\lambda)-\mathbf A_B(T_0,\lambda_0)\|_2^2
}{
\|\mathbf A_B(T_0,\lambda_0)\|_2^2
}.
```

Then the **joint iso-kernel wavelength** is

```math
\boxed{
\lambda_*(T)
=
\arg\min_\lambda
\left[
w_A\epsilon_A^2(T,\lambda)
+w_B\epsilon_B^2(T,\lambda)
\right].
}
```

Weights may reflect scientific importance, expected phase precision, or covariance-whitened kernel errors.

---

## 5. What is known now

For sample B alone, the current literature-constrained calculation shows that several mid/deep 300 K kernels can be reproduced extremely well at `215 K` and `115 K` by wavelength retuning.

For example:

```text
300 K 3.632 um
-> 215 K 3.793 um, mismatch ~0.44%
-> 115 K 4.003 um, mismatch ~0.84%

300 K 3.840 um
-> 215 K 4.042 um, mismatch ~0.043%
-> 115 K 4.310 um, mismatch ~0.112%.
```

These are **sample-B-only** iso-kernel results.

They do not establish that sample A can use the same wavelengths.

---

## 6. Why sample A is likely to differ

The 2023 primary paper reports that

```text
sample B
-> nonlinear interdiffusion region removed
-> thickness ~3.7 um

sample A
-> part of nonlinear interdiffusion region retained
-> thickness ~7.6 um
-> local nonlinear-gradient field near 2e3 V/cm.
```

Therefore A and B have different `x(z)`, different optical depth versus wavelength, and different generation kernels.

This is precisely why A is scientifically useful as a contrast structure — and precisely why B's iso-kernel schedule cannot simply be copied to A.

---

## 7. Three valid experimental routes

### Route 1 — common-wavelength joint iso-kernel design

Preferred if the recovered A/B profiles show a common wavelength can keep both kernels sufficiently stable.

Advantages:

```text
common source phase cancels directly
simple simultaneous measurement
transport difference-in-differences is cleanest.
```

### Route 2 — common wavelength, explicit kernel modeling

If no good joint iso-kernel wavelength exists, retain simultaneous source cancellation but fit the known changes

```math
\mathbf A_A(T,\lambda),
\qquad
\mathbf A_B(T,\lambda)
```

explicitly in a joint inverse.

This is more model dependent but preserves the strongest phase-systematic cancellation.

### Route 3 — device-specific iso-kernel wavelengths

Illuminate A and B at separate optimized wavelengths.

This best controls optical spatial weighting but loses direct cancellation of arbitrary source phase unless the two optical sources/branches are coherently related and independently referenced.

Use only if the phase-reference architecture is strong enough to support it.

---

## 8. Bias from residual kernel mismatch

Let

```math
\delta\mathbf A_d
=
\mathbf A_d(T,\lambda_*)
-
\mathbf A_d(T_0,\lambda_0).
```

The residual optical reweighting contributes timing bias

```math
\boxed{
\delta T_{\rm opt,d}
=
\delta\mathbf A_d\mathbf q_d.
}
```

Without knowing `q_d`, a norm bound is

```math
\boxed{
|\delta T_{\rm opt,d}|
\le
\|\delta\mathbf A_d\|_2
\|\mathbf q_d\|_2.
}
```

Therefore a `1%` kernel mismatch is not automatically a `1%` timing error. The effect depends on where the residual kernel error overlaps the transport profile.

A realistic design should propagate kernel uncertainty directly through the joint inverse rather than using one mismatch percentage as the final error bar.

---

## 9. Correct difference-in-differences interpretation

If a good joint iso-kernel wavelength exists and static differential-chain terms are calibrated,

```math
\mathbf A_d(T,\lambda_*)
\approx
\mathbf A_d(T_0,\lambda_0),
```

then

```math
\boxed{
D_{AB,T}
\approx
-\Omega
\left\{
\mathbf A_{A,0}
[\mathbf q_A(T)-\mathbf q_A(T_0)]
-
\mathbf A_{B,0}
[\mathbf q_B(T)-\mathbf q_B(T_0)]
\right\}.
}
```

This would isolate how the temperature dependence of transport differs between the nonlinear-gradient sample A and smooth-gradient sample B.

That is a sharper causal observable than either device's static timing profile.

---

## 10. Claim boundary

### DERIVED

- same-source simultaneous A-B subtraction cancels arbitrary common source phase only when the two devices are measured at the same wavelength/frequency;
- exact iso-kernel matching for A and B is a two-device constraint, not two independent one-device optimizations;
- residual kernel mismatch produces an explicit transport-weighted timing bias.

### CHECKED FOR SAMPLE B ONLY

Several mid/deep sample-B kernels can be held nearly invariant with temperature by wavelength retuning.

### OPEN

- sample-A optical kernel matrix;
- existence of useful common A/B iso-kernel wavelengths;
- size of residual optical bias in the paired temperature experiment;
- actual transport difference-in-differences;
- novelty / priority.

---

## 11. Next decisive work

Recover or digitize the sample-A composition profile.

Then compute

```math
\mathbf A_A(T,\lambda)
\quad\text{and}\quad
\mathbf A_B(T,\lambda)
```

and answer one concrete question:

> **Is there a common wavelength schedule that keeps both device kernels sufficiently invariant with temperature while retaining enough optical signal for paired phase measurement?**

If yes, the paired temperature difference-in-differences experiment becomes the strongest validation design in the repository.

If no, keep simultaneous common-wavelength measurement and model the temperature-dependent optical kernels explicitly rather than claiming optical cancellation.
