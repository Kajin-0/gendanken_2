# HgCdTe Impact-Ionization Dead Space — Bulk Onset Is Not a Finite-Detector Field Ceiling

**Date:** 2026-08-09  
**Status:** finite-length cold-injection field-work audit using established HgCdTe impact-ionization threshold physics; model-level correction, no novelty claim

## 1. Why this correction is necessary

`HGCDTE_FIELD_REGIME_MAP.md` compared the field at which bulk `Hg_0.8Cd_0.2Te` transport becomes non-ohmic / impact-ionization-sensitive with the direct-BTBT field scale.

That comparison is useful for identifying the onset of high-field physics, but it is **not** yet a finite-device impact-ionization ceiling.

A bulk steady-state electron distribution can develop a high-energy tail after repeated acceleration/scattering over a long history.

A photoelectron injected near the band edge into a finite collection region has a different problem: before it can impact-ionize, it must first acquire the threshold energy.

HgCdTe APD theory therefore uses **history-dependent / dead-space** impact-ionization models rather than treating the ionization coefficient as a purely local function of field in thin multiplication regions.

---

## 2. Threshold-energy model

Let

```math
E_{\rm th}
=\chi E_g,
```

where `chi` is of order unity.

Recent simplified HgCdTe APD Monte Carlo work takes

```math
E_{\rm th}\simeq E_g
```

because full-band calculations place the electron ionization threshold close to the bandgap.

Consider a cold injected electron with initial excess kinetic energy

```math
E_0\simeq0
```

crossing a uniform field `F` over distance `L`.

In the ideal field-work-only limit, the maximum energy supplied by the field over the full device is

```math
qFL.
```

Thus reaching threshold requires

```math
E_0+qFL
\gtrsim
E_{\rm th}.
```

For cold injection,

```math
\boxed{
F_{\rm dead}
\simeq
\frac{E_{\rm th}}
{qL}
=\frac{\chi E_g}{qL}.
}
```

Equivalently, at a stated field the ballistic threshold distance is

```math
\boxed{
d_{\rm dead}
\simeq
\frac{E_{\rm th}-E_0}{qF}.
}
```

This is a **cold-injection field-work estimate**, not a universal impossibility theorem. Phonon absorption, pre-heated injection, nonuniform fields, and full stochastic carrier histories modify the actual dead space.

Energy-losing scattering generally increases the distance required to reach threshold.

---

## 3. Connection to the HgCdTe Kane length

From the simplified Kane scaling used elsewhere in the repository,

```math
\ell_K
=\frac{\hbar v_K}{E_g},
```

and

```math
F_K
=\frac{\pi E_g^2}
{4q\hbar v_K}.
```

Therefore

```math
\frac{F_{\rm dead}}{F_K}
=
\frac{\chi E_g/(qL)}
{\pi E_g^2/(4q\hbar v_K)}.
```

Hence

```math
\boxed{
\frac{F_{\rm dead}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L}.
}
```

This is the cleanest result of this audit.

It shows that the relative ordering of the **cold-carrier ionization threshold field** and the **direct-BTBT characteristic field** is controlled by one dimensionless geometric/material ratio:

```math
\boxed{L/\ell_K.}
```

For ordinary detector dimensions

```math
L\gg\ell_K,
```

we have

```math
F_{\rm dead}\ll F_K.
```

Only when the active high-field distance approaches the nanometric Kane length do the two characteristic fields become comparable.

---

## 4. Direct BTBT evaluated at the cold-carrier ionization threshold

The normalized direct-BTBT curve is

```math
j=x^2e^{-1/x},
\qquad
x=F/F_K.
```

At the cold-carrier threshold field,

```math
x_{\rm dead}
=\frac{4\chi\ell_K}{\pi L}.
```

Therefore

```math
\boxed{
j_{\rm dead}
=
\left(
\frac{4\chi\ell_K}{\pi L}
\right)^2
\exp\!\left[
-\frac{\pi L}{4\chi\ell_K}
\right].
}
```

For

```math
L\gg\ell_K,
```

the exponential is extremely small.

Thus, within the same simplified Kane/BTBT framework, a finite device can reach the **energy scale where impact ionization becomes kinematically accessible** while direct BTBT is still exponentially suppressed.

That is a stronger and cleaner reason for the mechanism ordering than comparing the BTBT model directly with the `~100 V/cm` bulk Monte Carlo onset.

---

## 5. Representative HgCdTe values

Use

```math
E_g\simeq hc/\lambda_c
```

only as a scaling estimate and set

```math
\chi=1.
```

Then

```math
F_{\rm dead}
\simeq
\frac{hc}{q\lambda_c L}.
```

Representative field-work thresholds are:

| cutoff | `F_dead`, L=0.5 um | `F_dead`, L=1 um | `F_dead`, L=2 um | `F_dead`, L=5 um |
|---:|---:|---:|---:|---:|
| 8 um | 3.10 kV/cm | 1.55 kV/cm | 775 V/cm | 310 V/cm |
| 10 um | 2.48 kV/cm | 1.24 kV/cm | 620 V/cm | 248 V/cm |
| 12 um | 2.07 kV/cm | 1.03 kV/cm | 517 V/cm | 207 V/cm |
| 17 um | 1.46 kV/cm | 729 V/cm | 365 V/cm | 146 V/cm |
| 24 um | 1.03 kV/cm | 517 V/cm | 258 V/cm | 103 V/cm |

These numbers explain how a bulk onset around `10^2 V/cm` can coexist with a substantially higher dead-space threshold in a micron-scale cold-injection detector.

Thicker multiplication/transport distances move the finite-device threshold toward the bulk high-field scale.

---

## 6. Direct BTBT remains tiny at this threshold for micron-scale devices

For `L=1 um`, `chi=1`, the simplified direct-BTBT model evaluated at `F_dead` gives approximately:

| cutoff | `F_dead` | `J_BTBT(F_dead)` |
|---:|---:|---:|
| 8 um | 1.55 kV/cm | `5.8e-72 A/cm2` |
| 10 um | 1.24 kV/cm | `3.8e-57 A/cm2` |
| 12 um | 1.03 kV/cm | `2.7e-47 A/cm2` |
| 17 um | 729 V/cm | `7.1e-33 A/cm2` |
| 24 um | 517 V/cm | `7.1e-23 A/cm2` |

Again, these are isolated direct-BTBT-model values. They are **not** predictions of total device dark current.

The point is the parametric ordering:

```text
cold-carrier ionization threshold becomes accessible
well before
simplified direct BTBT becomes appreciable
```

for micron-scale ordinary MWIR/LWIR dimensions.

---

## 7. Correct impact-ionization probability after the dead space

Crossing the threshold does not mean an ionization event occurs immediately.

The 2026 HgCdTe APD Monte Carlo model uses an energy-dependent rate of the Kinch/Keldysh form

```math
P_{\rm II}(E)
=
A
\frac{(E/E_{\rm th}-1)^\alpha}
{(E/E_{\rm th})^\beta}
\,dt,
\qquad
E\ge E_{\rm th},
```

and zero below threshold.

Therefore a finite-device probability must retain the carrier energy history.

For one trajectory `E(t)`, the no-ionization survival probability has the generic form

```math
S
=\exp\!\left[
-\int \Gamma_{\rm II}(E(t))dt
\right],
```

so

```math
\boxed{
P_{\rm II}
=1-
\exp\!\left[
-\int \Gamma_{\rm II}(E(t))dt
\right].
}
```

This is why a purely local field coefficient `alpha(F)` is unsafe in a short multiplication/collection region unless it has already been calibrated to include nonlocal history effects.

---

## 8. Correction to the previous field-regime interpretation

The previous material branch used the bulk statement

```text
impact-ionization / hot-electron physics appears around 100 V/cm
```

as evidence that direct BTBT was not the first high-field phenomenon.

That broad conclusion remains useful for **bulk transport nonlinearity**, but it was too strong if read as a finite-device ionization ceiling.

The corrected hierarchy is:

```text
~50-100 V/cm in bulk x=0.20, 77 K
-> distribution becomes non-ohmic/hot-electron and II rate is no longer negligible

finite detector
-> actual II probability also depends on available acceleration distance and carrier history

cold-injection field-work scale
-> F_dead ~ E_th/(qL)

above F_dead
-> II becomes energetically accessible, but probability still requires an energy-history/rate model

direct BTBT
-> remains exponentially suppressed near F_dead for L >> ell_K in the simplified model.
```

This correction must be preserved in the canonical state.

---

## 9. Physical interpretation

The useful dimensionless variable is now

```math
\boxed{L/\ell_K.}
```

For `L >> ell_K`, there is a broad field interval in which

- hot-carrier transport is strongly non-ohmic;
- a sufficiently accelerated electron can become capable of impact ionization;
- direct interband tunneling remains exponentially small in the simplified model.

As `L` is reduced toward `ell_K`, the separation collapses.

This is another example of the project's recurring pattern:

> removing one macroscopic penalty by shrinking a length eventually exposes a microscopic material length.

Here that microscopic length is the HgCdTe Kane length.

---

## 10. Claim boundary

### Derived within the cold-injection field-work + simplified Kane model

```math
\boxed{
F_{\rm dead}
=\frac{\chi E_g}{qL},
}
```

```math
\boxed{
\frac{F_{\rm dead}}{F_K}
=\frac{4\chi}{\pi}
\frac{\ell_K}{L},
}
```

and

```math
\boxed{
j_{\rm dead}
=
\left(
\frac{4\chi\ell_K}{\pi L}
\right)^2
\exp\left[-
\frac{\pi L}{4\chi\ell_K}
\right].
}
```

### Established prior physics

- HgCdTe electron impact ionization has a threshold energy close to the bandgap in the models used for e-APDs;
- thin HgCdTe avalanche regions require history-dependent/nonlocal treatment and exhibit dead-space effects;
- impact-ionization probability depends on the carrier energy history, not only the instantaneous field.

### Not established

- exact `chi` for every HgCdTe composition/temperature;
- a strict no-ionization theorem in the presence of energy-gaining phonon/bath processes;
- a calibrated `P_II(F,L)` for `Hg_0.8Cd_0.2Te` at 77 K;
- a complete dark-current or speed frontier;
- novelty of the dead-space scaling.

---

## 11. Next decisive calculation

The next correct calculation is no longer a field-only `alpha_II(F)` fit.

Build the **minimal finite-length energy-history model**:

```text
field work
+
nonparabolic E(k)
+
phonon energy loss / absorption
+
energy-dependent impact-ionization rate
-> P_II(F,L).
```

Start with a deterministic mean-energy model if necessary, then test it against Monte Carlo literature.

Only after `P_II(F,L)` is available should impact ionization be compared quantitatively with direct BTBT and TAT as a field ceiling.
