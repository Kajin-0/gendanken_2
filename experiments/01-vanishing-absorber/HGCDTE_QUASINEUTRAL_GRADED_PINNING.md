# HgCdTe Quasi-Neutral Graded Pinning — Why a p-Type Graded Absorber Naturally Approaches the Zener-Suppression Geometry

**Date:** 2026-08-09  
**Status:** equilibrium nondegenerate carrier-statistics derivation composed with the repository linear graded-Kane WKB result; graded-band transport is established prior physics; no novelty claim

## 1. Purpose

`HGCDTE_LINEAR_GRADED_KANE_WKB.md` found that the conventional direct-Zener action diverges as the valence-band downhill slope tends to zero while the useful conduction-band slope stays finite.

That raised an immediate realism question:

> Is `S_v -> 0` merely an artificial tuning of the band edges, or can a real graded semiconductor naturally approach it?

In a quasi-neutral p-type graded semiconductor, majority-carrier equilibrium does exactly that to leading order.

The valence band is approximately pinned by the majority holes, while the conduction band inherits most of the gap gradient.

---

## 2. Nondegenerate p-type equilibrium

For nondegenerate holes,

```math
\boxed{
p(x)
=N_v(x)
\exp\left[
\frac{E_v(x)-E_F}{k_BT}
\right].
}
```

At thermal equilibrium,

```math
E_F=\text{constant}.
```

Differentiate:

```math
\frac{d\ln p}{dx}
=
\frac{d\ln N_v}{dx}
+\frac1{k_BT}
\frac{dE_v}{dx}.
```

Therefore

```math
\boxed{
E_v'
=k_BT
\left[
\frac{d\ln p}{dx}
-
\frac{d\ln N_v}{dx}
\right].
}
```

In a quasi-neutral uniformly doped p-type region,

```math
p\simeq N_A
```

and `p` is approximately spatially constant.

Then

```math
\boxed{
E_v'
\simeq
-k_BT\frac{d\ln N_v}{dx}.
}
```

If the valence-band density of states changes only weakly along the grade,

```math
\boxed{E_v'\approx0.}
```

Thus the majority-carrier band is approximately pinned.

---

## 3. Minority-electron conduction-band slope

Because

```math
\boxed{E_c=E_v+E_g,}
```

```math
E_c'
=E_v'+E_g'.
```

Using the quasi-neutral relation,

```math
\boxed{
E_c'
\simeq
E_g'
-k_BT\frac{d\ln N_v}{dx}.
}
```

If the gap decreases in the electron-collection direction, define

```math
\boxed{
G\equiv-\frac{dE_g}{dx}>0.
}
```

Also define the density-of-states correction

```math
\boxed{
b
\equiv
k_BT\frac{d\ln N_v}{dx}.
}
```

Then the downhill slopes are

```math
\boxed{
S_c=-E_c'
=G+b,
}
```

```math
\boxed{
S_v=-E_v'
=b.
}
```

Thus, when

```math
|b|\ll G,
```

```math
S_c\simeq G,
```

while

```math
S_v\simeq0.
```

The gap gradient drives the minority electron while the majority-hole band remains nearly flat.

---

## 4. Map directly onto the graded-WKB parameter `eta`

The graded-Kane derivation wrote

```math
S_c=S_U+S_\Delta,
```

```math
S_v=S_U-S_\Delta.
```

Therefore

```math
S_U=\frac{S_c+S_v}{2},
```

```math
S_\Delta=\frac{S_c-S_v}{2}.
```

Using

```math
S_c=G+b,
```

```math
S_v=b,
```

we obtain

```math
\boxed{
S_\Delta=G/2,
}
```

and

```math
\boxed{
S_U=G/2+b.
}
```

The grading fraction at fixed useful conduction slope is

```math
\eta
=\frac{S_\Delta}{S_c}.
```

Hence

```math
\boxed{
\eta
=\frac{G}
{2(G+b)}.
}
```

If

```math
b\to0,
```

then

```math
\boxed{\eta\to1/2.}
```

This is exactly the boundary where the conventional linear direct-Zener turning-point separation diverged in the earlier WKB model.

---

## 5. Physical interpretation

The result is not that the electrostatic potential disappears.

In fact, if `E_v` is pinned while the gap changes, the self-consistent midgap/common-mode energy `U` also shifts.

Using

```math
E_v=U-\Delta,
```

valence pinning gives

```math
U'\simeq\Delta'.
```

So the real equilibrium contains both

```text
common-mode band bending
and
gap grading.
```

What matters is their **combination**:

```text
conduction edge slopes strongly
valence edge remains nearly flat.
```

That is precisely the band geometry that suppresses spatial conduction/valence overlap for the ordinary direct-Zener path.

---

## 6. Density-of-states correction to the WKB action

For

```math
b>0,
```

the valence band still tilts downhill weakly, so the two-turning-point WKB formula applies.

Define

```math
\boxed{
\zeta\equiv b/G.
}
```

Then

```math
\boxed{
S_v/S_c
=\frac{\zeta}{1+\zeta}.
}
```

From the graded-action relation,

```math
1-2\eta
=\frac{S_v}{S_c}.
```

Therefore

```math
\boxed{
\eta
=\frac1{2(1+\zeta)}.
}
```

The action enhancement at fixed conduction slope becomes

```math
\boxed{
\frac{\mathcal S_Z}
{\mathcal S_Z^{(\rm common)}}
=
\frac{(1+2\zeta)^2}
{4\zeta^{3/2}\sqrt{1+\zeta}},
\qquad \zeta>0.
}
```

As

```math
\zeta\to0^+,
```

the action diverges.

Thus even a small density-of-states correction can leave the direct-Zener action much larger than the all-common-tilt reference with the same conduction-band slope.

---

## 7. Representative dimensionless values

| `zeta = b/G` | `eta` | action ratio |
|---:|---:|---:|
| 1.0 | 0.250 | 1.59 |
| 0.5 | 0.333 | 2.18 |
| 0.2 | 0.417 | 4.69 |
| 0.1 | 0.455 | 12.1 |
| 0.05 | 0.476 | 32.9 |
| 0.02 | 0.490 | 126 |

These are model ratios, not measured HgCdTe current reductions.

---

## 8. If `b <= 0`

If

```math
b=0,
```

the valence edge is flat and the conventional same-energy valence turning point recedes.

If

```math
b<0,
```

the valence edge tilts opposite to the conduction edge.

Provided the finite graded region remains positive-gap and terminates before band inversion, the ordinary same-energy two-turning-point direct-Zener path considered here is absent inside that region.

Other leakage channels remain possible.

---

## 9. Why this connection is plausible in HgCdTe

Primary HgCdTe graded-gap theory and experiment already establish the underlying carrier physics:

- bandgap gradients produce an effective/quasi-electric field for minority carriers;
- composition profiles strongly affect minority-carrier transport;
- p-type graded regions are a standard context for minority-electron collection;
- graded-band HgCdTe devices have been developed to accelerate minority-carrier evacuation and improve speed;
- nonlinear composition grading can generate very large local built-in fields.

The new point here is only the connection of that familiar quasi-neutral band pinning to the exact graded-Kane WKB slope ratio derived in this repository.

No priority is claimed.

---

## 10. Where the quasi-neutral approximation fails

The useful pinning relation depends on

```math
p\simeq N_A
```

and weak spatial variation of the majority carrier density.

It fails or changes in

- depleted regions;
- very low-doped material;
- strong injection;
- degenerate statistics;
- regions with strong recombination/generation imbalance;
- abrupt interfaces;
- strong fixed/interface charge;
- regions where `N_v(x)` varies strongly.

In those cases Poisson and carrier statistics must be solved self-consistently.

This is especially important because the strongest tunneling fields in real photodiodes often occur in depleted regions, not in quasi-neutral material.

---

## 11. n-Type analogue

For nondegenerate electrons,

```math
n
=N_c
\exp\left[
\frac{E_F-E_c}{k_BT}
\right].
```

In a quasi-neutral uniformly doped n-type region,

```math
n\simeq N_D
```

and equilibrium gives

```math
\boxed{
E_c'
\simeq
+k_BT\frac{d\ln N_c}{dx}.
}
```

So the **conduction band** is approximately pinned, while the valence band inherits most of the gap gradient.

Thus the natural minority-carrier quasi-field reverses roles:

```text
p-type graded region
-> minority electrons feel most of gap gradient

n-type graded region
-> minority holes feel most of gap gradient.
```

This is the expected graded-gap minority-carrier picture.

---

## 12. Important equilibrium caveat

A static graded band does not create perpetual equilibrium current.

At equilibrium, drift-like forces are balanced by carrier statistics/diffusion so the net current vanishes.

The quasi-field becomes useful after photoexcitation because the excess minority carriers are out of equilibrium and relax/transport through the built-in energy landscape.

Therefore the grading resource is a **collection bias for nonequilibrium photocarriers**, not a thermodynamic free-energy source producing DC current without excitation.

---

## 13. Claim boundary

### DERIVED from nondegenerate equilibrium statistics

For quasi-neutral p-type material,

```math
\boxed{
E_v'
\simeq
-k_BT(d\ln N_v/dx),
}
```

```math
\boxed{
E_c'
\simeq
E_g'-k_BT(d\ln N_v/dx).
}
```

With `G=-E_g'` and `b=k_BT dlnN_v/dx`,

```math
\boxed{S_c=G+b,\qquad S_v=b.}
```

Hence

```math
\boxed{
\eta=G/[2(G+b)].
}
```

and for `b>0`,

```math
\boxed{
\frac{\mathcal S_Z}
{\mathcal S_Z^{(\rm common)}}
=
\frac{(1+2\zeta)^2}
{4\zeta^{3/2}\sqrt{1+\zeta}},
\qquad
\zeta=b/G.
}
```

### KNOWN / PRIOR

- quasi-electric fields in graded-gap semiconductors;
- graded HgCdTe minority-carrier transport;
- quasi-neutral carrier statistics;
- absence of equilibrium net current despite built-in fields.

### NON-CLAIM

This file does not establish

- that every p-type HgCdTe graded absorber has `E_v'=0`;
- zero direct tunneling in a real detector;
- validity in the depletion region;
- absence of TAT/interface tunneling;
- novelty of graded-band pinning.

---

## 14. Next decisive attack

The result identifies the exact place where the ideal escape is most plausible:

> **quasi-neutral p-type graded absorption/transport regions.**

The next finite model should therefore separate

```text
quasi-neutral graded absorber
+
depleted junction / multiplication region.
```

Then ask:

1. how much transit time can the quasi-neutral grade remove before the carrier reaches the depletion region?
2. how much applied field can be kept out of the narrow-gap absorber?
3. does the remaining depleted region still dominate TAT/BTBT/II?
4. does the full response become lifetime/diffusion limited rather than transit limited?

This is the smallest architecture that connects the exact graded-band result to an actual infrared detector.