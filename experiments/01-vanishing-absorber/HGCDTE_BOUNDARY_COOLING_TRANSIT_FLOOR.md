# HgCdTe Boundary Cooling Transit Floor — Voltage Handling and Energy Relaxation Cannot Both Be Zero-Length

**Date:** 2026-08-09  
**Status:** exact combination of the repository minimum-compensation, local tunneling-margin, energy-relaxation, and Kane-velocity models; conditional device-level lower bound; no novelty claim

## 1. Purpose

The current architecture separates two jobs:

```text
quasi-neutral graded absorber
-> minority-electron drive
-> direct-Zener suppression
-> nonlocal hot-electron constraint

wider-gap collection boundary
-> barrier-free band alignment
-> local TAT / BTBT voltage handling
-> hot-electron relaxation at minimum compensation.
```

The boundary cannot perform the last two jobs in zero physical length.

This note combines them into one minimum-width and minimum-transit-time condition.

---

## 2. Minimum-compensation boundary

Let the boundary raise the material band gap by

```math
\Delta E_g^{(b)}>0,
```

and let `alpha` be the conduction-band share of that material gap increase.

The minimum electrostatic voltage for barrier-free electron extraction is

```math
\boxed{
V_b
=\frac{\alpha\Delta E_g^{(b)}}{q}.
}
```

At this voltage the total conduction edge is flat across the boundary:

```math
\boxed{\Delta E_c^{(b)}=0.}
```

Therefore the boundary adds no mean downhill carrier work in the present model.

---

## 3. Cooling length

With no total conduction-band drive, the mean excess electron energy obeys

```math
\frac{d\varepsilon}{ds}
=-\frac{\varepsilon}{\ell_{E,b}}.
```

Hence

```math
\boxed{
\varepsilon(s)
=\varepsilon_{\rm in}
e^{-s/\ell_{E,b}}.
}
```

Suppose the boundary must reduce the mean excess energy to a fraction

```math
0<c<1
```

of its input value:

```math
\varepsilon_{\rm out}
\le c\varepsilon_{\rm in}.
```

Then necessarily

```math
\boxed{
w
\ge
w_{\rm cool}
\equiv
\ell_{E,b}\ln\frac1c.
}
```

Thus a desired cooling factor is itself a finite-length resource.

---

## 4. Local TAT width requirement

Let the local boundary TAT exponent be represented by

```math
\exp(-F_{\rm TAT}/F).
```

For a required exponent margin `Sigma_t`, the field must obey

```math
F\le F_{\rm TAT}/\Sigma_t.
```

For a uniform boundary material, carrying the minimum compensation voltage therefore requires

```math
\boxed{
w
\ge
w_{\rm TAT}
\equiv
\frac{\alpha\Delta E_g^{(b)}}
{qF_{\rm TAT}}
\Sigma_t.
}
```

This is the earlier boundary TAT width floor.

---

## 5. Direct-BTBT width requirement

Using a local direct-Zener/Kane characteristic field `F_K` and required exponent margin `Sigma_Z`,

```math
\boxed{
w
\ge
w_Z
\equiv
\frac{\alpha\Delta E_g^{(b)}}
{qF_K}
\Sigma_Z.
}
```

In a trap-limited boundary, `w_TAT` can be much larger than `w_Z`.

---

## 6. Combined minimum boundary width

All three requirements must hold simultaneously.

Therefore

```math
\boxed{
w
\ge
w_{\min}^{(b)}
=
\max\left[
\ell_{E,b}\ln\frac1c,
\frac{\alpha\Delta E_g^{(b)}\Sigma_t}{qF_{\rm TAT}},
\frac{\alpha\Delta E_g^{(b)}\Sigma_Z}{qF_K}
\right].
}
```

This is the central boundary result.

It separates three physical reasons a boundary cannot be made arbitrarily thin:

```text
energy relaxation
+
trap-assisted tunneling margin
+
direct interband tunneling margin.
```

If a process/fabrication peak-field ceiling is also required, add its corresponding width term to the maximum.

---

## 7. Kinematic transit-time floor

In the simplified two-band/Kane model, the electron group speed magnitude is bounded by `v_K`.

Hence crossing any width `w` requires

```math
T_b\ge w/v_K.
```

Combining with the width result gives

```math
\boxed{
T_b
\ge
\frac1{v_K}
\max\left[
\ell_{E,b}\ln\frac1c,
\frac{\alpha\Delta E_g^{(b)}\Sigma_t}{qF_{\rm TAT}},
\frac{\alpha\Delta E_g^{(b)}\Sigma_Z}{qF_K}
\right].
}
```

This is a best-case lower bound. Real scattering, diffusion after thermalization, interface transmission, and non-ballistic transport can only increase the actual boundary transit time.

---

## 8. Combine with the graded-absorber II-safe length

`HGCDTE_II_SAFE_TRANSIT_CEILING.md` gives the absorber mean-II-safe requirement

```math
L_a\ge\ell_{E,a}r_{\min}(\zeta,\chi)
```

when the chosen fractional downhill gap drop `zeta` exceeds the ballistic-safe value.

Therefore a sequential absorber + minimum-compensation boundary satisfies the conditional total kinematic bound

```math
\boxed{
T_{\rm total}
\ge
\frac1{v_K}
\left[
\ell_{E,a}r_{\min}
+
w_{\min}^{(b)}
\right].
}
```

where `r_min=0` in the ballistic mean-II-safe grading regime.

Written explicitly,

```math
\boxed{
T_{\rm total}
\ge
\frac1{v_K}
\left\{
\ell_{E,a}r_{\min}
+
\max\left[
\ell_{E,b}\ln\frac1c,
\frac{\alpha\Delta E_g^{(b)}\Sigma_t}{qF_{\rm TAT}},
\frac{\alpha\Delta E_g^{(b)}\Sigma_Z}{qF_K}
\right]
\right\}.
}
```

This is the first repository relation that combines the graded absorber's nonlocal hot-electron constraint with the collection boundary's local tunneling and cooling constraints in one transit-time expression.

---

## 9. Dimensionless form

Normalize lengths by the absorber energy-relaxation length `ell_E,a` and define

```math
\rho_E=\ell_{E,b}/\ell_{E,a}.
```

Define

```math
\tau_*
\equiv
T_{\rm total}v_K/\ell_{E,a}.
```

Then

```math
\boxed{
\tau_*
\ge
r_{\min}
+
\max\left[
\rho_E\ln\frac1c,
\frac{w_{\rm TAT}}{\ell_{E,a}},
\frac{w_Z}{\ell_{E,a}}
\right].
}
```

This form is suitable for a parametric phase map before the absolute target-composition `ell_E` scale is known.

---

## 10. Interpretation

The architecture does not evade every speed penalty. It **spatially separates them**.

The absorber is allowed to spend composition-gradient energy on fast carrier drive until nonlocal heating requires a minimum relaxation distance.

The boundary is allowed to spend electrostatic voltage in a wider-gap region, but it must be long enough to

- keep local TAT/BTBT fields below the chosen margins; and
- cool the incoming hot carrier by the desired amount.

This is a more precise version of the recurring project theme:

> removing one penalty does not necessarily remove the resource cost; it can relocate it to a different physical part of the detector.

---

## 11. Important caveats

The result assumes

- one-dimensional monotonic transport;
- minimum boundary compensation;
- uniform boundary `F_TAT` and `F_K` for the explicit width formula;
- exponential mean-energy relaxation with one `ell_E,b`;
- a constant Kane velocity scale for the kinematic bound;
- no stochastic II tail;
- no interface reflection;
- no diffusion-limited slowdown after strong cooling;
- local WKB validity for TAT/BTBT.

For a heterogeneous boundary, replace the simple tunneling width terms by the integrated voltage-capacity condition in `HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`.

---

## 12. Next use

Use this relation as the backbone of the dimensionless finite-device phase map.

The phase map should show separately

```text
absorber nonlocal-II margin
boundary local-tunneling voltage margin
required cooling factor
best-case normalized transit time.
```

Do not insert a numerical `ell_E` until trustworthy target-composition data are recovered.
