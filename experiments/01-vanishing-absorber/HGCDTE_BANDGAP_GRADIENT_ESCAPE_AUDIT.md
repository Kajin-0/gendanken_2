# HgCdTe Bandgap-Gradient Escape Audit — Replacing Part of the Electrostatic Drive with Band-Edge Slope

**Date:** 2026-08-09  
**Status:** idealized two-band/Kane energy-landscape audit motivated by established graded-HgCdTe detector physics; no novelty claim

## 1. Purpose

The field-profile theorem showed that in a homogeneous material, redistributing a single electric-field variable cannot improve the local transit–tunneling tradeoff at fixed transit time.

A compositionally graded semiconductor changes the problem more fundamentally:

```text
carrier-driving band-edge slope
```

and

```text
electrostatic common-mode band tilt
```

need not be the same quantity.

The question is:

> **Can a HgCdTe composition gradient supply part of the carrier-driving energy slope while reducing the electrostatic field that drives direct Zener/BTBT tunneling?**

In an ideal two-band model, yes.

Real devices require self-consistent band offsets, Poisson charge and transport, so this is an escape audit rather than a quantitative design result.

---

## 2. Minimal two-band energy landscape

Use the schematic one-dimensional Kane/Dirac Hamiltonian

```math
\boxed{
H
=U(x)I
+v_Kp\,\sigma_x
+\Delta(x)\sigma_z.
}
```

Here

```math
\boxed{E_g(x)=2\Delta(x)}
```

and `U(x)` is the local midgap/common-mode energy.

At zero wave vector the band edges are

```math
\boxed{
E_c(x)=U(x)+\Delta(x),
}
```

```math
\boxed{
E_v(x)=U(x)-\Delta(x).
}
```

The conduction-band force on an electron is controlled by

```math
-\frac{dE_c}{dx}
=-U'(x)-\Delta'(x).
```

Thus both a common-mode slope and a gap/mass slope can contribute to electron collection.

---

## 3. Common-mode slope reproduces the direct-BTBT scale

Take constant gap

```math
\Delta(x)=\Delta_0
```

and linear common-mode tilt

```math
|U'|=qF.
```

The spatial Landau-Zener/Kane exponent has the form

```math
\boxed{
\mathcal T_Z
\sim
\exp\left[
-\frac{\pi\Delta_0^2}
{\hbar v_K|U'|}
\right].
}
```

Since

```math
\Delta_0=E_g/2,
```

```math
\boxed{
\mathcal T_Z
\sim
\exp\left[
-\frac{\pi E_g^2}
{4q\hbar v_KF}
\right].
}
```

The characteristic field is therefore exactly the simplified Kane field already used in the repository:

```math
\boxed{
F_K
=\frac{\pi E_g^2}
{4q\hbar v_K}.
}
```

This identifies the earlier BTBT exponent as a **common-mode band-tilt penalty** in the minimal two-band picture.

---

## 4. Pure gap gradient is a different operation

Now set

```math
U'(x)=0
```

while allowing

```math
\Delta'(x)\ne0.
```

Then

```math
E_c'=\Delta',
```

```math
E_v'=-\Delta'.
```

So the conduction and valence band edges tilt in **opposite** directions.

A conduction electron can therefore move downhill in `E_c` even though there is no common-mode `U` tilt.

If

```math
\Delta(x)>0
```

everywhere and `U` is constant, the local conduction and valence bands remain separated by

```math
2\Delta(x)>0.
```

In this ideal static model, the ordinary constant-gap common-field Zener channel described above is absent.

A smooth mass/gap gradient can still cause reflection, mode conversion and nonadiabatic corrections, but it is not equivalent to the common-mode electric-field tilt that produced the `exp(-F_K/F)` law.

This is the conceptual escape.

---

## 5. Define an equivalent grading drive

Let the useful conduction-band energy drop supplied by composition grading across length `L` be

```math
\boxed{
\Delta E_c^{(g)}.
}
```

Define the equivalent grading field

```math
\boxed{
F_g
=\frac{\Delta E_c^{(g)}}{qL}.
}
```

Let the total conduction-band driving field required by a transit target be

```math
F_{\rm drv}.
```

In the simplest aligned-slope decomposition,

```math
\boxed{
F_{\rm drv}
=F_{\rm el}+F_g,
}
```

where `F_el` is the residual electrostatic/common-mode contribution.

Therefore

```math
\boxed{
F_{\rm el}
=F_{\rm drv}-F_g
}
```

as long as the grading and electrostatic slopes aid the same carrier direction.

---

## 6. Band-edge-drop resource

Define the fraction of the drive supplied by grading

```math
\boxed{
\eta_g
=F_g/F_{\rm drv}.
}
```

Then

```math
\boxed{
\Delta E_c^{(g)}
=q\eta_gF_{\rm drv}L.
}
```

For an ohmic transit target

```math
F_{\rm drv}
=\frac{L}{\mu T},
```

so

```math
\boxed{
\Delta E_c^{(g)}
=\eta_g
\frac{qL^2}{\mu T}.
}
```

Thus composition grading does not provide an unlimited free drive.

It spends a finite **band-edge offset/drop budget** set by the available composition range and band offsets.

---

## 7. Idealized tunneling reduction

Suppose, only for this comparison, that the local direct-tunneling exposure can still be written

```math
\boxed{
g(F_{\rm el})
=A F_{\rm el}^p
\exp(-K/F_{\rm el}).
}
```

If the same carrier drive were supplied entirely electrostatically, the reference leakage would be

```math
g_0
=A F_{\rm drv}^p
\exp(-K/F_{\rm drv}).
```

Using

```math
F_{\rm el}
=(1-\eta_g)F_{\rm drv},
```

the ideal reduction factor is

```math
\boxed{
\frac{g}{g_0}
=
(1-\eta_g)^p
\exp\left[
-\frac{K}{F_{\rm drv}}
\frac{\eta_g}{1-\eta_g}
\right].
}
```

Even modest grading fractions can therefore produce an exponentially large reduction in an electrostatic-field-driven tunneling channel.

This is an **idealized upper-bound argument** because real grading also changes `K`, band offsets, charge distribution and local electrostatics.

---

## 8. Why the escape is physically plausible in HgCdTe

Compositionally graded HgCdTe is established detector technology.

Primary HgCdTe studies report that

- composition gradients generate built-in carrier-driving fields;
- these fields materially affect minority-carrier transport and responsivity;
- linear gradients have been calculated to produce fields of order `100–200 V/cm` in measured structures, while strong nonlinear grading can create substantially larger local fields;
- graded-band MWIR detectors have been developed specifically to improve carrier evacuation and high-frequency response;
- recent graded-composition HgCdTe APDs use wide-gap gradient regions to generate built-in quasi-electric fields and suppress dark-current/recombination burdens.

Thus the grading field is not a hypothetical control knob.

---

## 9. But real grading is not a pure `Delta'(x)` knob

The ideal decomposition above is deliberately optimistic.

In a real HgCdTe heterostructure, changing composition also changes

```text
bandgap
conduction/valence offsets
electron affinity
carrier density
ionized dopant charge
permittivity
mobility
lifetime
absorption coefficient
trap energetics.
```

Charge redistribution generates an electrostatic potential `U(x)` through Poisson's equation.

Therefore the real structure generally has both

```math
U'(x)\ne0
```

and

```math
\Delta'(x)\ne0.
```

A quantitative tunneling calculation must use the **full conduction and valence band profiles**, not subtract a phenomenological quasi-field from the applied field and reuse a uniform-gap WKB law.

---

## 10. Barrier formation is also a real constraint

A graded band edge that helps one carrier can create a barrier for another carrier or at an interface.

HgCdTe heterojunction literature explicitly analyzes conditions under which composition/doping profiles avoid unwanted conduction- or valence-band barriers.

Therefore useful grading must satisfy simultaneously

```text
carrier-driving slope
+
no blocking barrier
+
adequate absorption
+
low tunneling
+
acceptable recombination.
```

The band-edge drop is a design resource, not automatically a benefit.

---

## 11. Minimal energy-landscape optimization

The correct continuous variables are no longer just `F(x)`.

Use

```math
\boxed{
E_c(x)=U(x)+\Delta(x),
}
```

```math
\boxed{
E_v(x)=U(x)-\Delta(x).
}
```

Then a detector design specifies

```text
carrier transport
-> slope of E_c or E_v

interband tunneling
-> full spatial relation between E_c and E_v

absorption
-> local E_g=E_c-E_v

electrostatics
-> U from Poisson / charge

composition
-> allowed Delta(x) and band offsets.
```

This is a more faithful formulation than treating every carrier-driving effect as one electric field.

---

## 12. Ideal pure-grading limit

In the ideal model with

```math
U'(x)=0,
```

```math
\Delta(x)>0,
```

and a monotonic conduction-band downhill slope, a photoelectron may acquire a finite drift-driving potential drop without the ordinary common-mode Zener tilt.

The available drive is bounded by

```math
\boxed{
|\Delta E_c^{(g)}|
\le
\text{available conduction-band offset across the composition range}.
}
```

This gives a clean physical interpretation:

> **Composition grading can exchange electrical-bias resource for band-structure resource.**

It does not create unlimited carrier acceleration.

---

## 13. Relation to the earlier uniform-field theorem

The homogeneous theorem is not contradicted.

That theorem assumed one fixed local relation

```math
v=v(F)
```

and

```math
g=g(F).
```

Composition grading changes the material Hamiltonian itself.

The transport drive and leakage barrier become separate spatial functions.

Therefore grading lies outside the theorem's assumptions and is a legitimate escape.

---

## 14. Claim boundary

### DERIVED within the ideal two-band model

Band edges:

```math
\boxed{E_c=U+\Delta,\qquad E_v=U-\Delta.}
```

Conduction-band drive:

```math
\boxed{-E_c'=-U'-\Delta'.}
```

Common-mode constant-gap tilt reproduces

```math
\boxed{
\mathcal T_Z
\sim
\exp[-\pi E_g^2/(4q\hbar v_KF)].
}
```

Equivalent grading-drive budget:

```math
\boxed{F_g=\Delta E_c^{(g)}/(qL).}
```

Ideal residual-field leakage ratio:

```math
\boxed{
\frac{g}{g_0}
=
(1-\eta_g)^p
\exp\left[-
\frac{K}{F_{\rm drv}}
\frac{\eta_g}{1-\eta_g}
\right].
}
```

### KNOWN / PRIOR

- compositionally graded HgCdTe creates built-in/quasi-electric carrier-driving fields;
- graded HgCdTe is used to modify responsivity, speed and dark-current behavior;
- barrier formation and band offsets are established heterojunction constraints.

### NON-CLAIM

This file does **not** establish

- zero tunneling in a real graded HgCdTe detector;
- that a real composition gradient has `U'=0`;
- that the uniform-gap BTBT law can simply use `F_el=F_drv-F_g` quantitatively;
- a universal optimal grading profile;
- a novelty claim.

---

## 15. Next decisive step

The most revealing next model is no longer a two-field resistor-like structure.

Build the smallest self-consistent **two-band energy-landscape** model with

1. a specified HgCdTe composition gradient `E_g(x)`;
2. a band-offset partition between `E_c` and `E_v`;
3. Poisson electrostatic potential `U(x)`;
4. photoelectron transit time from the resulting `E_c(x)` slope;
5. WKB interband action through the resulting full `E_c/E_v` profile.

That will determine whether composition grading truly buys faster collection at lower tunneling for a realistic HgCdTe band alignment, rather than only in the ideal pure-gap-gradient limit.