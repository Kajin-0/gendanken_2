# HgCdTe Trap-Assisted Tunneling Field Scale — Why Traps Can Open a Leakage Path Long Before Direct BTBT

**Date:** 2026-08-09  
**Status:** exponent-scale comparison between established HgCdTe TAT and direct-BTBT models; trap-prefactor/density remains device-specific; no novelty claim

## 1. Purpose

The current material branch has shown that direct band-to-band tunneling can remain exponentially small over a large portion of the high-field transport regime.

That does **not** imply that tunneling leakage as a whole is negligible.

HgCdTe photodiode literature repeatedly identifies trap-assisted tunneling (TAT) as an important or dominant reverse-bias leakage mechanism, particularly when deep levels or dislocation-associated states are present.

The reason can be seen directly from the tunneling exponent.

---

## 2. Simple one-dimensional HgCdTe TAT model

A standard HgCdTe TAT model writes the tunneling rate from an occupied trap toward a conduction-band state with an exponential factor of the form

```math
\boxed{
\exp\!\left[
-
\frac{4\sqrt{2m^*}
(E_g-E_T)^{3/2}}
{3q\hbar F}
\right].
}
```

Here

- `E_T` is measured upward from the valence-band edge in this convention;
- therefore

```math
\boxed{
\Delta_t
\equiv
E_g-E_T
}
```

is the remaining energy barrier from the trap to the conduction band;
- `m*` is the tunneling effective mass;
- `F` is the local electric field.

The complete TAT current also contains trap density, matrix element, depletion width, trap occupation, and device electrostatics.

This note compares only the **exponential field scale**.

---

## 3. Define the TAT characteristic field

Write the exponent as

```math
\exp(-F_{\rm TAT}/F).
```

Then

```math
\boxed{
F_{\rm TAT}
=
\frac{4\sqrt{2m^*}
\Delta_t^{3/2}}
{3q\hbar}.
}
```

This should be compared with the direct-BTBT characteristic field used elsewhere in the repository,

```math
\boxed{
F_K
=
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2 q\hbar}.
}
```

---

## 4. Exact exponent-scale ratio

Divide the two characteristic fields:

```math
\frac{F_{\rm TAT}}{F_K}
=
\frac{4\sqrt2/3}
{\pi/(2\sqrt2)}
\left(\frac{\Delta_t}{E_g}\right)^{3/2}.
```

Therefore

```math
\boxed{
\frac{F_{\rm TAT}}{F_K}
=
\frac{16}{3\pi}
\left(\frac{\Delta_t}{E_g}\right)^{3/2}.
}
```

Define the fractional trap depth below the conduction band

```math
\boxed{
\delta_t
=\frac{\Delta_t}{E_g}.
}
```

Then

```math
\boxed{
F_{\rm TAT}/F_K
=\frac{16}{3\pi}\delta_t^{3/2}.
}
```

This is the central scaling result.

---

## 5. Representative exponent reductions

| trap depth below conduction band | `F_TAT/F_K` |
|---:|---:|
| `0.50 E_g` | 0.600 |
| `0.20 E_g` | 0.152 |
| `0.10 E_g` | 0.0537 |
| `0.05 E_g` | 0.0190 |
| `0.02 E_g` | 0.00480 |

Thus a trap close to the conduction band can lower the exponential field scale by **one to two orders of magnitude** relative to direct band-to-band tunneling.

The prefactor can still determine whether that channel is experimentally important, but the exponent explains why TAT can turn on much earlier in field.

---

## 6. Connection to reported HgCdTe traps

HgCdTe junction analyses have reported fits involving trap levels only a few meV below the conduction band.

For illustration, if

```text
E_g = 100 meV
Delta_t = 6 meV,
```

then

```math
\delta_t=0.06
```

and

```math
\boxed{
F_{\rm TAT}/F_K
\simeq0.02495.
}
```

So the TAT exponential scale is only about `2.5%` of the direct-BTBT scale.

For the simplified 10 um HgCdTe Kane scaling, where

```math
F_K\sim1.7\times10^5\ {\rm V/cm},
```

this corresponds to a TAT characteristic exponent field of order

```math
F_{\rm TAT}\sim4.3\times10^3\ {\rm V/cm}.
```

This does **not** mean that TAT begins only at `4.3 kV/cm`.

The current contains a prefactor proportional to trap density and other device parameters, and an exponential `exp(-F_TAT/F)` has no sharp onset field.

---

## 7. Kane substitution

Using the same simplified narrow-gap relation

```math
m^*=E_g/(2v_K^2),
```

the TAT field becomes

```math
F_{\rm TAT}
=
\frac{4\sqrt2}{3q\hbar}
\sqrt{\frac{E_g}{2v_K^2}}
\Delta_t^{3/2}.
```

Therefore

```math
\boxed{
F_{\rm TAT}
=
\frac{4}{3q\hbar v_K}
E_g^{1/2}\Delta_t^{3/2}.
}
```

This exposes two physically different trap-scaling cases.

---

## 8. Case A — trap stays at a fixed fraction of the gap

If

```math
\Delta_t=\delta_tE_g
```

with fixed `delta_t`, then

```math
F_{\rm TAT}
=
\frac{4\delta_t^{3/2}}
{3q\hbar v_K}
E_g^2.
```

Hence

```math
\boxed{
F_{\rm TAT}
\propto E_g^2
\propto\lambda_c^{-2}.
}
```

It scales with cutoff wavelength in the same way as the simplified direct-BTBT field, with a reduced dimensionless coefficient set by trap location.

---

## 9. Case B — trap stays a fixed absolute energy below the conduction band

If the physical defect gives approximately fixed

```math
\Delta_t=\text{constant},
```

then

```math
\boxed{
F_{\rm TAT}
\propto E_g^{1/2}
\propto\lambda_c^{-1/2}.
}
```

Meanwhile

```math
F_K\propto E_g^2.
```

Thus

```math
\boxed{
\frac{F_{\rm TAT}}{F_K}
\propto E_g^{-3/2}
\propto\lambda_c^{3/2}.
}
```

Interpretation:

> If a trap remains a fixed number of meV below the conduction band while the HgCdTe gap is reduced, **direct BTBT catches up rapidly with TAT at very long wavelength**.

Conversely, for a fixed fractional trap depth, both exponent scales fall together as `lambda_c^-2`.

This distinction is important for extrapolating trap physics across MWIR/LWIR/VLWIR compositions.

---

## 10. TAT current is not determined by the exponent alone

The simple one-dimensional TAT current contains factors such as

```text
N_T        trap density
Delta_t    trap energy depth
matrix element / capture strength
depletion width
trap occupation
electric-field profile.
```

Modern HgCdTe TAT expressions likewise contain

```math
J_{\rm TAT}
\propto
N_T
\exp[-F_{\rm TAT}/F]
```

up to model-specific prefactors and geometrical factors.

Therefore two devices with identical `E_g` and field can have radically different TAT current if their defect populations differ.

This is why TAT is a **materials-quality-dependent field constraint**, unlike the intrinsic direct-BTBT exponent.

---

## 11. Relation to the present speed problem

The stripped field-driven collection problem now has at least three distinct mechanisms:

```text
transport nonlinearity / velocity saturation
-> limits how much speed extra field buys

impact ionization
-> nonlocal probability controlled by energy history and dead space

trap-assisted tunneling
-> defect-mediated leakage with a much smaller tunneling exponent when traps sit near a band edge

direct BTBT
-> intrinsic full-gap tunneling, strongly suppressed until higher field for ordinary LWIR in the simplified model.
```

So the correct optimization is not

```text
maximize field until BTBT current reaches J*.
```

It is

```math
\boxed{
F_{\rm opt}
=\arg\max_F v(F)
}
```

subject to independent constraints on

```math
P_{\rm II}(F,L),
```

```math
J_{\rm TAT}(F),
```

```math
J_{\rm BTBT}(F),
```

and the other detector dark-current/readout mechanisms.

---

## 12. Claim boundary

### DERIVED within the stated simple TAT/BTBT exponent models

```math
\boxed{
F_{\rm TAT}
=\frac{4\sqrt{2m^*}\Delta_t^{3/2}}
{3q\hbar},
}
```

```math
\boxed{
\frac{F_{\rm TAT}}{F_K}
=\frac{16}{3\pi}
(\Delta_t/E_g)^{3/2},
}
```

and under the simplified Kane mass

```math
\boxed{
F_{\rm TAT}
=\frac{4E_g^{1/2}\Delta_t^{3/2}}
{3q\hbar v_K}.
}
```

### KNOWN

HgCdTe literature reports substantial TAT leakage and experimentally fitted trap states near band edges in some diode technologies.

### OPEN

- target-device `N_T`;
- target trap energy distribution rather than one discrete `E_T`;
- capture/matrix element;
- local depletion-field profile;
- self-consistent trap occupation;
- whether TAT or II limits a particular `x=0.20`, 77 K device first.

### NON-CLAIM

This note does not establish

- a universal TAT onset field;
- a universal trap depth;
- that TAT dominates every HgCdTe detector;
- that the simple one-dimensional trap model is quantitatively adequate for optimized heterostructures;
- novelty of the TAT exponent scaling.

---

## 13. Next decisive step

The high-field problem has now separated naturally into

```text
intrinsic material scales
-> E_g, v_K, ell_K, direct BTBT

defect scales
-> N_T, Delta_t, capture strength, TAT

nonlocal carrier dynamics
-> ell_E, Gamma_II(E), impact ionization

transport/readout
-> v(F), L, lifetime, RC, contacts.
```

Next, do **not** attempt one arbitrary total-current fit.

Instead ask a more experimentally useful question:

> For a specified maximum field needed to obtain a target transit time, what upper bound on trap density `N_T` is required so that TAT remains below a chosen dark-current budget?

That will convert the field/speed requirement into a material-quality specification.