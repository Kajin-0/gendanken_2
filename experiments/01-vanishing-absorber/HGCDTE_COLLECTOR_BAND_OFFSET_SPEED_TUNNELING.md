# HgCdTe Wider-Gap Depleted Collector — Band-Offset Alignment, Transit Speed, and Direct-Zener Cost

**Date:** 2026-08-09  
**Status:** parametric two-band collector model; conduction-band offset fraction remains an external HgCdTe heterostructure input; no novelty claim

## 1. Purpose

`HGCDTE_TWO_ZONE_GRADED_DEPLETED_TRANSFER.md` moved the remaining high-field burden out of the quasi-neutral narrow-gap absorber and into a depleted collector.

The natural next escape is to make that collector wider gap so it tolerates electrostatic field better.

But a wider-gap region can create a conduction-band barrier for the photoelectron.

This note asks:

> **How much electrostatic drop is required to remove that barrier and obtain a target collector transit time, and what direct-Zener exponent does that field imply?**

The result is clean when written in terms of the collector Kane length.

---

## 2. Two-region endpoint gaps

Let the graded absorber terminate at gap

```math
\boxed{E_{g,a}}
```

and let the depleted collector have larger gap

```math
\boxed{E_{g,c}>E_{g,a}.}
```

Define

```math
\boxed{\Delta E_g^{ac}=E_{g,c}-E_{g,a}>0.}
```

Parameterize the conduction-band offset as

```math
\boxed{
\Delta E_c^{\rm off}
=Q_c\Delta E_g^{ac},
}
```

where `Q_c` is the fraction of the gap discontinuity assigned to the conduction band in the chosen band-alignment convention.

`Q_c` is **not assumed universal for HgCdTe** in this repository.

It depends on the actual heterojunction/composition/band-alignment model and must be supplied from reliable material data or a self-consistent band calculation.

---

## 3. Effective electron barrier

Let the electrostatic potential-energy drop available to lower the collector conduction band relative to the absorber be

```math
\boxed{\Delta U_d=qF_dW_d}
```

for collector width `W_d` and uniform field magnitude `F_d` in the first model.

The remaining effective barrier for an electron arriving near the absorber conduction-band edge is

```math
\boxed{
\Phi_{\rm eff}
=\Delta E_c^{\rm off}-\Delta U_d.
}
```

Barrierless transfer of a fully thermalized band-edge electron requires

```math
\boxed{
\Phi_{\rm eff}\le0,
}
```

or

```math
\boxed{
\Delta U_d
\ge
Q_c\Delta E_g^{ac}.
}
```

Thus the minimum alignment field is

```math
\boxed{
F_{\rm align}
=\frac{Q_c\Delta E_g^{ac}}
{qW_d}.
}
```

This is an energetic alignment requirement, not a detailed interface-transmission calculation.

---

## 4. Allow a small thermionic barrier

If cooled nondegenerate electrons cross a positive barrier thermally, the simplest Boltzmann factor is

```math
\eta_{\rm int}
\sim
\exp[-\Phi_{\rm eff}/(k_BT)].
```

For required interface transmission

```math
\eta_{\rm int}\ge\eta_{\rm int,*},
```

a sufficient energetic condition in this toy model is

```math
\boxed{
\Phi_{\rm eff}
\le
k_BT\ln\frac1{\eta_{\rm int,*}}.
}
```

Hence

```math
\boxed{
\Delta U_d
\ge
Q_c\Delta E_g^{ac}
-k_BT\ln\frac1{\eta_{\rm int,*}}.
}
```

If the right side is negative, no electrostatic alignment drop is required by this criterion.

Interface reflection, thermionic prefactors, tunneling through the offset, and hot-carrier injection are outside this simple condition.

---

## 5. Add a collector transit-time target

In the low-field ohmic baseline,

```math
v_d=\mu_dF_d.
```

The depleted transit time is

```math
T_d
=\frac{W_d}{\mu_dF_d}
=\frac{qW_d^2}
{\mu_d\Delta U_d}.
```

To require

```math
T_d\le T_{d,*},
```

the electrostatic energy drop must also obey

```math
\boxed{
\Delta U_d
\ge
\frac{qW_d^2}
{\mu_dT_{d,*}}.
}
```

Therefore the minimum collector energy drop in the ohmic model is

```math
\boxed{
\Delta U_{d,\min}
=
\max\left[
Q_c\Delta E_g^{ac}-\Phi_*,
\frac{qW_d^2}{\mu_dT_{d,*}}
\right],
}
```

where

```math
\boxed{
\Phi_*
=k_BT\ln\frac1{\eta_{\rm int,*}}.
}
```

and negative alignment requirements should be replaced by zero.

Then

```math
\boxed{
F_{d,\min}
=\frac{\Delta U_{d,\min}}
{qW_d}.
}
```

This separates

```text
interface-alignment cost
```

from

```text
speed cost.
```

---

## 6. Collector Kane scale

Use the same simplified narrow-gap Kane scale for the collector:

```math
\boxed{
F_{K,c}
=\frac{\pi E_{g,c}^2}
{4q\hbar v_K}.
}
```

Define the collector Kane length

```math
\boxed{
\ell_{K,c}
=\frac{\hbar v_K}
{E_{g,c}}.
}
```

Let the electrostatic energy drop be expressed as a fraction of the collector gap:

```math
\boxed{
\rho_U
=\frac{\Delta U_d}
{E_{g,c}}.
}
```

Then

```math
F_d
=\frac{\rho_UE_{g,c}}
{qW_d}.
```

Divide by `F_K,c`:

```math
\boxed{
\frac{F_d}{F_{K,c}}
=
\frac{4\rho_U}{\pi}
\frac{\ell_{K,c}}{W_d}.
}
```

Equivalently, the direct-Zener exponent is

```math
\boxed{
\mathcal S_c
\equiv
\frac{F_{K,c}}{F_d}
=
\frac{\pi}{4\rho_U}
\frac{W_d}{\ell_{K,c}}.
}
```

This is the central collector scaling.

---

## 7. Alignment-only specialization

For exactly barrierless alignment and no extra speed requirement,

```math
\Delta U_d
=Q_c(E_{g,c}-E_{g,a}).
```

Define the relative collector gap contrast

```math
\boxed{
\rho
=\frac{E_{g,c}-E_{g,a}}
{E_{g,c}}.
}
```

Then

```math
\boxed{
\rho_U=Q_c\rho.
}
```

Therefore

```math
\boxed{
\frac{F_{\rm align}}
{F_{K,c}}
=
\frac{4Q_c\rho}{\pi}
\frac{\ell_{K,c}}{W_d}.
}
```

and

```math
\boxed{
\mathcal S_{\rm align}
=
\frac{\pi}
{4Q_c\rho}
\frac{W_d}{\ell_{K,c}}.
}
```

This is structurally identical to the earlier dead-space/Kane-length relations:

> **the electrostatic field required to compensate a finite band offset is far below the direct-BTBT scale whenever the depleted collector is many Kane lengths thick.**

---

## 8. Thin-collector tradeoff

Shrinking `W_d` is attractive because

```math
T_d=W_d/v_d
```

falls directly at fixed velocity.

But the alignment field grows as

```math
F_{\rm align}\propto1/W_d.
```

The direct-Zener action therefore falls linearly with width:

```math
\boxed{
\mathcal S_{\rm align}
\propto W_d/\ell_{K,c}.
}
```

Thus the collector cannot be shrunk indefinitely while holding a finite electrostatic band-offset drop.

The microscopic length `ell_K,c` reappears as the asymptotic scale.

---

## 9. Example scale — illustrative only

Take, purely as a dimensionless example,

```text
E_ga = 0.124 eV
E_gc = 0.200 eV
Q_c  = 0.5
v_K  = 1.07e6 m/s.
```

Then

```math
\rho
=0.076/0.200
=0.38.
```

The collector Kane length is about

```math
\ell_{K,c}\sim3.5\ {\rm nm}.
```

For

```math
W_d=0.5\ {\rm um},
```

the alignment field is roughly

```text
760 V/cm
```

and

```math
\mathcal S_{\rm align}
\sim590.
```

So direct intrinsic Zener tunneling would be exponentially tiny in this stripped alignment model.

If the collector were reduced to `50 nm`, the same offset requires about ten times the field and the exponent falls to order `60`.

At only a few nanometers, the direct-Zener penalty becomes qualitatively different.

These numbers are not a prediction for an actual HgCdTe heterojunction because `Q_c`, field distribution, nonparabolicity, interface structure, and TAT have not been calibrated.

---

## 10. TAT can still intervene much earlier

The previous TAT result gives

```math
\boxed{
F_{\rm TAT}/F_{K,c}
=\frac{16}{3\pi}
(\Delta_t/E_{g,c})^{3/2}.
}
```

Therefore a near-band-edge trap can create substantial tunneling sensitivity even when

```math
F_d/F_{K,c}\ll1.
```

So the statement

```text
collector alignment field is far below F_K,c
```

does **not** establish a low dark current.

It establishes only that intrinsic full-gap direct BTBT need not be the limiting interface-alignment cost.

Interface traps / TAT are the obvious next attack.

---

## 11. High-field transport correction

The ohmic speed term

```math
qW_d^2/(\mu_dT_{d,*})
```

must not be used once `v_d(F)` becomes strongly nonlinear.

The general speed condition is

```math
\boxed{
v_d(F_d)
\ge
W_d/T_{d,*}.
}
```

Define the minimum field solving that relation on the physically useful rising branch as

```math
\boxed{F_{v,*}.}
```

Then the correct general minimum collector field is

```math
\boxed{
F_{d,\min}
=
\max(F_{\rm align,*},F_{v,*}),
}
```

where `F_align,*` is the interface-alignment field corresponding to the allowed residual barrier.

This keeps transport and band alignment modular.

---

## 12. Why a wider-gap collector is still attractive

A wider-gap collector can help in three distinct ways:

1. increase the direct-BTBT characteristic field `F_K,c ~ E_g,c^2`;
2. reduce intrinsic carrier generation in the high-field region;
3. allow the narrow-gap optical absorber to remain quasi-neutral / lower electrostatic field.

But it can hurt by

1. creating a conduction-band barrier;
2. introducing interface traps / TAT;
3. adding heterojunction resistance/reflection;
4. reducing carrier velocity depending on composition;
5. changing avalanche/ionization behavior if multiplication is desired.

The band-offset parameter is therefore a genuine design resource, not a nuisance correction.

---

## 13. Claim boundary

### DERIVED / CONDITIONAL

For the parametric band-offset + uniform collector model:

```math
\boxed{
F_{\rm align}
=Q_c(E_{g,c}-E_{g,a})/(qW_d),
}
```

```math
\boxed{
F_d/F_{K,c}
=(4\rho_U/\pi)(\ell_{K,c}/W_d),
}
```

and alignment-only

```math
\boxed{
F_{\rm align}/F_{K,c}
=(4Q_c\rho/\pi)(\ell_{K,c}/W_d).
}
```

### KNOWN / PRIOR

- semiconductor heterojunction band offsets;
- thermionic barrier suppression;
- HgCdTe Kane/Zener scaling;
- TAT/interface-state sensitivity of HgCdTe junctions.

### OPEN

- reliable `Q_c` for the intended HgCdTe composition transition;
- self-consistent interface electrostatics;
- carrier distribution entering the collector;
- interface-state density;
- collector-specific mobility / velocity law;
- realistic TAT current.

### NON-CLAIM

This file does not establish

- a universal HgCdTe conduction-band offset fraction;
- that a wider-gap collector is barrierless in a real device;
- low total dark current merely because direct BTBT is small;
- a complete heterojunction design;
- novelty of the scaling.

---

## 14. Next decisive step

The band-offset fraction `Q_c` is now the key external material input.

Do not assign it arbitrarily.

Next either

1. recover a defensible HgCdTe conduction/valence band-offset model for the intended composition range; or
2. keep `Q_c` parametric and derive a robust design map in `(Q_c,W_d,E_g,c/E_g,a)` showing where interface alignment, collector speed, TAT and direct BTBT dominate.

Given the variability of heterojunction assumptions in the literature, the parametric map may be more scientifically honest before a specific epitaxial structure is chosen.