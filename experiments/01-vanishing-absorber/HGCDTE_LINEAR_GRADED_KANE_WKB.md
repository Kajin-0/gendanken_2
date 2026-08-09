# HgCdTe Linear Graded-Gap Kane WKB — Exact Tunneling Action at Fixed Conduction-Band Drive

**Date:** 2026-08-09  
**Status:** exact WKB action for a linear two-band/Kane energy landscape; graded-gap/WKB ingredients are prior physics; exact detector-facing slope-ratio statement has unassessed priority; no novelty claim

## 1. Purpose

`HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md` argued qualitatively that carrier-driving conduction-band slope and common-mode electrostatic tilt are distinct resources in a graded semiconductor.

This note removes the heuristic step and solves the simplest graded two-band tunneling problem exactly.

Question:

> **At a fixed useful conduction-band downhill slope, how does replacing part of the common electrostatic tilt with a bandgap gradient change the direct interband WKB action?**

For a linear two-band profile, the answer is closed form.

---

## 2. Local two-band dispersion

Use the one-dimensional two-band/Kane dispersion

```math
\boxed{
(E-U)^2
=\Delta^2
+(\hbar v_K k)^2,
}
```

where

```math
\boxed{E_g=2\Delta.}
```

The local band edges are

```math
\boxed{
E_c=U+\Delta,
\qquad
E_v=U-\Delta.
}
```

For a fixed conserved energy `E`, the forbidden-region wavevector is imaginary whenever

```math
E_v(x)<E<E_c(x).
```

Write

```math
k=i\kappa.
```

Then

```math
\boxed{
\kappa(x)
=\frac{
\sqrt{[E_c(x)-E][E-E_v(x)]}
}
{\hbar v_K}.
}
```

The WKB transmission probability is

```math
\boxed{
\mathcal T(E)
\sim
\exp[-\mathcal S(E)],
}
```

with

```math
\boxed{
\mathcal S(E)
=2\int_{x_v}^{x_c}\kappa(x)dx.
}
```

---

## 3. Linear conduction and valence edges

Let

```math
\boxed{
E_c(x)
=E_{c0}-S_cx,
}
```

```math
\boxed{
E_v(x)
=E_{v0}-S_vx.
}
```

Assume first

```math
S_c>0,
\qquad
S_v>0,
```

so both band edges tilt downhill in the same spatial direction.

The turning points for energy `E` are

```math
\boxed{
x_c
=\frac{E_{c0}-E}{S_c},
}
```

```math
\boxed{
x_v
=\frac{E_{v0}-E}{S_v}.
}
```

Assume

```math
x_v<x_c.
```

Then

```math
E_c-E
=S_c(x_c-x),
```

```math
E-E_v
=S_v(x-x_v).
```

Therefore

```math
\boxed{
\kappa(x)
=\frac{\sqrt{S_cS_v}}
{\hbar v_K}
\sqrt{(x_c-x)(x-x_v)}.
}
```

---

## 4. Exact WKB integral

Use the elementary integral

```math
\int_a^b
\sqrt{(b-x)(x-a)}\,dx
=\frac{\pi}{8}(b-a)^2.
```

Hence

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}
(x_c-x_v)^2.
}
```

This is the exact WKB action for the linear two-edge model.

No uniform-field approximation has been made after specifying the linear edges.

---

## 5. Recover the ordinary Kane/BTBT exponent

Take constant gap and common electrostatic tilt:

```math
S_c=S_v=S.
```

Choose the reference energy at midgap at `x=0`:

```math
E=0,
```

```math
E_{c0}=+\Delta_0,
```

```math
E_{v0}=-\Delta_0.
```

Then

```math
x_c=\Delta_0/S,
```

```math
x_v=-\Delta_0/S,
```

so

```math
x_c-x_v=2\Delta_0/S.
```

The action becomes

```math
\boxed{
\mathcal S_0
=\frac{\pi\Delta_0^2}
{\hbar v_KS}.
}
```

With

```math
\Delta_0=E_g/2,
```

and

```math
S=qF,
```

```math
\boxed{
\mathcal S_0
=\frac{\pi E_g^2}
{4q\hbar v_KF}.
}
```

Thus

```math
\mathcal T
\sim e^{-F_K/F}
```

with

```math
\boxed{
F_K
=\frac{\pi E_g^2}
{4q\hbar v_K},
}
```

exactly matching the simplified HgCdTe Kane scale used elsewhere in the repository.

---

## 6. Decompose common tilt and gap gradient

Write

```math
U'(x)=-S_U,
```

```math
\Delta'(x)=-S_\Delta,
```

with

```math
S_U\ge0,
\qquad
S_\Delta\ge0.
```

Then

```math
E_c'=U'+\Delta'
=-(S_U+S_\Delta),
```

```math
E_v'=U'-\Delta'
=-(S_U-S_\Delta).
```

Therefore

```math
\boxed{
S_c=S_U+S_\Delta,
}
```

```math
\boxed{
S_v=S_U-S_\Delta.
}
```

The useful conduction-band downhill slope is `S_c`.

The gap-gradient contribution increases the conduction slope while **reducing** the same-direction valence slope.

---

## 7. Hold useful conduction drive fixed

Fix

```math
\boxed{S_c=S}
```

as the transport requirement.

Define the fraction supplied by gap grading

```math
\boxed{
\eta
=\frac{S_\Delta}{S},
}
```

so

```math
S_\Delta=\eta S.
```

Since

```math
S_U=S-S_\Delta,
```

```math
\boxed{
S_U=(1-\eta)S.
}
```

The valence-band downhill slope becomes

```math
\boxed{
S_v=(1-2\eta)S.
}
```

For

```math
0\le\eta<1/2,
```

both edges still tilt downhill and the two-turning-point WKB formula applies directly.

---

## 8. Exact graded-action ratio

Again choose

```math
E=0,
```

```math
E_{c0}=+\Delta_0,
```

```math
E_{v0}=-\Delta_0.
```

Then

```math
x_c=\Delta_0/S,
```

and

```math
x_v=-\frac{\Delta_0}
{(1-2\eta)S}.
```

Therefore

```math
x_c-x_v
=\frac{2(1-\eta)\Delta_0}
{(1-2\eta)S}.
```

Substitute into the exact action:

```math
\mathcal S_Z(\eta)
=\frac{\pi\Delta_0^2}
{\hbar v_KS}
\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}.
```

Since

```math
\mathcal S_Z(0)
=\frac{\pi\Delta_0^2}
{\hbar v_KS},
```

we obtain

```math
\boxed{
\frac{\mathcal S_Z(\eta)}
{\mathcal S_Z(0)}
=
\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}},
\qquad
0\le\eta<\frac12.
}
```

This is the central result.

---

## 9. Grading always suppresses this Zener channel at fixed conduction slope

Define

```math
R(\eta)
=\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}.
```

Then

```math
\frac{d\ln R}{d\eta}
=-\frac2{1-\eta}
+\frac3{1-2\eta}.
```

Therefore

```math
\boxed{
\frac{d\ln R}{d\eta}
=\frac{1+\eta}
{(1-\eta)(1-2\eta)}>0
}
```

for

```math
0\le\eta<1/2.
```

Thus

```math
\boxed{
\mathcal S_Z(\eta)
>\mathcal S_Z(0)
\quad
\text{for every }\eta>0.
}
```

At fixed useful conduction-band slope, transferring any positive fraction of the slope from common-mode tilt into a decreasing gap **strictly increases the WKB tunneling action** in this model.

Because transmission is exponential in minus the action, the interband channel is suppressed.

---

## 10. The action diverges as the valence slope approaches zero

As

```math
\eta\to1/2^{-},
```

```math
S_v=(1-2\eta)S\to0^+.
```

The valence turning point recedes to infinity:

```math
x_v
=-\frac{\Delta_0}{S_v}
\to-\infty.
```

Consequently

```math
\boxed{
\mathcal S_Z
\to\infty.
}
```

The standard same-energy spatial-overlap Zener path disappears continuously as the valence edge ceases to tilt toward the conduction edge.

---

## 11. What happens for `eta >= 1/2`?

For

```math
\eta\ge1/2,
```

```math
S_v\le0.
```

The valence edge is flat or tilts in the **opposite** direction from the conduction edge.

If the graded region is restricted to

```math
\Delta(x)>0
```

and terminates before the local gap closes/inverts, the valence turning point required by the conventional linear-profile Zener path is absent within the positive-gap region.

Therefore the particular two-turning-point direct-Zener channel solved above no longer exists inside that ideal domain.

This does **not** mean all interband transitions are impossible.

Potential remaining mechanisms include

- nonadiabatic transitions caused by rapid composition changes;
- interface/heterojunction tunneling;
- trap-assisted tunneling;
- phonon-assisted transitions;
- electrostatic `U(x)` generated self-consistently by charge redistribution;
- actual gap closure or band inversion if the grading is continued too far.

The statement is only about the ordinary smooth positive-gap same-energy WKB path of this minimal model.

---

## 12. Numerical size of the action enhancement

Representative values:

| grading fraction `eta` | `S_Z(eta)/S_Z(0)` |
|---:|---:|
| 0.10 | 1.132 |
| 0.20 | 1.377 |
| 0.30 | 1.935 |
| 0.40 | 4.025 |
| 0.45 | 9.562 |
| 0.49 | 93.0 |

Because the tunneling probability scales as

```math
\mathcal T\sim e^{-\mathcal S},
```

even a modest action increase can correspond to a very large current reduction when the ungraded exponent is already larger than unity.

These ratios are geometry-model results, not measured HgCdTe suppression factors.

---

## 13. Connection to compositionally graded HgCdTe experiments

The model captures a real design axis.

Primary HgCdTe work reports

- built-in fields generated by composition gradients that alter minority-carrier motion;
- calculated fields around `100–200 V/cm` for linear gradients in measured structures and much larger local values for nonlinear grading;
- graded-band MWIR devices designed specifically to accelerate minority-carrier evacuation and improve frequency response;
- recent graded-composition HgCdTe APDs using wide-gap gradient regions and built-in quasi-electric fields to suppress dark current/recombination while guiding carriers.

An uncooled graded-band HgCdTe detector has also been reported with approximately `1.33 ns` total response time (`750 MHz`) at zero bias, demonstrating that composition-gradient carrier drive can be technologically significant without a large externally applied field.

These prior devices are not tests of the exact `R(eta)` formula above.

---

## 14. Prior-art boundary

Graded-band HgCdTe, WKB modeling, Kane/Zener tunneling, band-edge engineering and built-in quasi-electric fields are established prior physics.

A focused search located primary work on

- WKB calculations in graded-gap HgCdTe;
- analytical conduction/valence band profiles in graded heterojunctions;
- classic uniform-field Kane/Zener tunneling;
- modern nonuniform-field Zener methods.

The exact fixed-conduction-slope ratio

```math
\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}
```

was not located in the inspected search results.

That is only a negative search result.

Current status:

> **exact internally derived linear-profile WKB corollary; mathematical/physical priority unassessed; no novelty claim.**

---

## 15. Why this is more important than the earlier heuristic

The earlier ideal argument said roughly

```text
replace electrostatic field with grading
-> less BTBT.
```

The exact calculation now says something much sharper:

> **At fixed conduction-band downhill slope, a gap gradient suppresses the direct linear-profile Zener path because it simultaneously reduces the valence-band slope that creates spatial band overlap.**

The mechanism is therefore not merely a smaller electric-field number.

It is a change in the **relative geometry of the conduction and valence bands**.

That is the correct energy-landscape interpretation.

---

## 16. Major caveats

The exact result assumes

- constant `v_K`;
- linear `E_c` and `E_v`;
- a smooth one-dimensional profile;
- fixed conserved tunneling energy;
- WKB validity;
- no transverse momentum;
- no interface reflection beyond the WKB barrier;
- no trap-assisted channel;
- no self-consistent charge redistribution;
- a positive-gap region that terminates before gap closure for the `eta >= 1/2` discussion.

Real HgCdTe composition grading changes `v_K`, band offsets, doping, carrier density, dielectric response, traps and electrostatics.

Do not use the formula as a quantitative device current without a full band profile.

---

## 17. Next decisive test

The result is strong enough to deserve an immediate adversarial attack.

Build a **finite graded region** with specified endpoint gaps and finite length.

Then ask simultaneously:

1. how much conduction-band energy drop can grading supply before the target cutoff/absorption is compromised?
2. does a self-consistent electrostatic potential restore a common-mode `U'` large enough to reopen the Zener path?
3. what band-offset partition between `E_c` and `E_v` is realistic in HgCdTe?
4. do TAT or interface states become dominant before the direct-Zener benefit matters?
5. is the resulting transit-time improvement competitive with the already demonstrated graded-band HgCdTe devices?

Only after those attacks should this graded-action corollary be considered for publication significance.