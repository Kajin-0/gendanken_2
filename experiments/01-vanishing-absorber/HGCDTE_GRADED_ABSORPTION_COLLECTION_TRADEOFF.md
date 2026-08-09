# HgCdTe Graded Absorption–Collection Tradeoff — When a Transparent Front Region Improves Collected QE

**Date:** 2026-08-09  
**Status:** exact sharp-absorption-edge toy model composed with the graded neutral drift/recombination result; intentionally simplified optical model; no novelty claim

## 1. Purpose

`HGCDTE_GRADED_NEUTRAL_COLLECTION_TRANSFER.md` showed that a finite conduction-band drop can accelerate minority electrons through a quasi-neutral graded p-type absorber.

That analysis temporarily treated the photogeneration profile as independent of the grade.

But grading changes the local bandgap. For photons near the low-gap cutoff, the wide-gap part of the absorber may become transparent.

The obvious concern is

```text
more grading
-> less absorbing material
-> lower quantum efficiency.
```

The countervailing effect is

```text
more grading
-> absorption pushed closer to collector
-> shorter carrier travel distance
-> less recombination.
```

This note combines those effects in the simplest exactly solvable model.

---

## 2. Linear gap profile

Let the neutral graded absorber occupy

```math
0\le x\le L,
```

with the collecting boundary at

```math
x=L.
```

Take a linearly decreasing bandgap toward the collector:

```math
\boxed{
E_g(x)
=E_{g,\max}
-\frac{\Delta E_g}{L}x,
}
```

with

```math
\boxed{
\Delta E_g
=E_{g,\max}-E_{g,\min}>0,
}
```

and

```math
E_g(L)=E_{g,\min}.
```

In the ideal p-type pinned-valence limit, the minority-electron conduction band follows the gap slope and the constant drift velocity is

```math
\boxed{
v
=\frac{\mu_n\Delta E_g}{qL}.
}
```

---

## 3. Photon detuning above the low-gap edge

Let the photon energy be

```math
E_\gamma
=E_{g,\min}+\varepsilon,
\qquad
\varepsilon>0.
```

Thus

```math
\boxed{
\varepsilon
=E_\gamma-E_{g,\min}
}
```

is the photon detuning above the minimum gap.

The most interesting case is

```math
\Delta E_g>\varepsilon,
```

so part of the graded layer has a local gap larger than the photon energy.

---

## 4. Sharp-edge absorption model

Use an intentionally crude local optical law:

```math
\boxed{
\alpha(x)
=
\begin{cases}
0,&E_g(x)>E_\gamma,\\
\alpha_0,&E_g(x)\le E_\gamma.
\end{cases}
}
```

This is **not** a realistic HgCdTe absorption edge.

It is used because it isolates the geometry exactly before importing measured intrinsic absorption, Urbach tails, Burstein-Moss shifts, etc.

The threshold position satisfies

```math
E_g(x_a)=E_\gamma.
```

Therefore

```math
x_a
=L\left(1-rac{\varepsilon}{\Delta E_g}\right).
```

Only the final segment

```math
\boxed{
\ell_a
=L-x_a
=L\frac{\varepsilon}{\Delta E_g}
}
```

absorbs the near-cutoff photon.

Define the active absorbing fraction

```math
\boxed{
r
\equiv
\frac{\ell_a}{L}
=\frac{\varepsilon}{\Delta E_g},
\qquad
0<r\le1.
}
```

Thus

```math
\boxed{
\Delta E_g
=\frac{\varepsilon}{r}.
}
```

Stronger grading means smaller `r`.

---

## 5. Optical thickness of the active segment

Define the full-thickness optical parameter

```math
\boxed{
a_0
=\alpha_0L.
}
```

The actually absorbing segment has optical thickness

```math
\boxed{
a
=\alpha_0\ell_a
=a_0r.
}
```

Ignoring reflection, its absorptance is

```math
\boxed{
A_{\rm abs}
=1-e^{-a_0r}.
}
```

As

```math
r\to0,
```

absorptance vanishes linearly:

```math
A_{\rm abs}\simeq a_0r.
```

So arbitrarily strong grading cannot preserve near-cutoff absorption in this model.

---

## 6. Collection time falls quadratically with active fraction

The drift speed is

```math
v
=\frac{\mu_n\Delta E_g}{qL}
=\frac{\mu_n\varepsilon}{qLr}.
```

The farthest absorbing point is `ell_a=rL` from the collector.

Therefore the maximum collection time of a near-cutoff generated electron is

```math
T_a
=\frac{\ell_a}{v}.
```

Substitute `ell_a=rL` and the drift velocity:

```math
\boxed{
T_a
=\frac{qL^2\varepsilon}
{\mu_n(\Delta E_g)^2}
=\frac{qL^2}{\mu_n\varepsilon}r^2.
}
```

This is the key countervailing scaling:

```text
absorbing length
~ r

maximum collection delay
~ r^2.
```

Thus making the front region transparent loses absorbing length only linearly while reducing the worst transit delay quadratically.

---

## 7. Dimensionless recombination parameter

Let the minority lifetime be

```math
\tau_n.
```

Define

```math
\boxed{
\chi
\equiv
\frac{qL^2}
{\mu_n\tau_n\varepsilon}.
}
```

Then the transport/recombination ratio across the optically active segment is

```math
\boxed{
\xi_a
=\frac{T_a}{\tau_n}
=\chi r^2.
}
```

The entire near-cutoff problem therefore depends on only

```math
\boxed{a_0,\quad\chi,\quad r.}
```

---

## 8. Exact external collected QE

Light enters from `x=0` and propagates through the transparent graded front region without absorption.

At `x=x_a` it enters the active segment.

Measure distance into the active segment by

```math
0\le y\le\ell_a,
```

where `y=0` is the beginning of absorption and `y=ell_a` is the collector.

The generation profile is

```math
\alpha_0e^{-\alpha_0y}.
```

An electron generated at `y` must drift distance

```math
\ell_a-y
```

and survives with probability

```math
\exp[-(\ell_a-y)/(v\tau_n)].
```

Therefore the collected electrons per incident photon are

```math
\eta_{\rm ext}
=\int_0^{\ell_a}
\alpha_0e^{-\alpha_0y}
\exp[-(\ell_a-y)/(v\tau_n)]dy.
```

Define

```math
a=a_0r,
```

```math
\xi=\chi r^2.
```

The integral is exact:

```math
\boxed{
\eta_{\rm ext}
=
\frac{a(e^{-\xi}-e^{-a})}
{a-\xi}.
}
```

The apparent singularity at

```math
a=\xi
```

is removable, with

```math
\boxed{
\eta_{\rm ext}
\to
 a e^{-a}.
}
```

Substituting `a=a_0r` and `xi=chi r^2` gives the compact grade equation

```math
\boxed{
\eta_{\rm ext}(r)
=
\frac{
a_0
\left[
 e^{-\chi r^2}
-e^{-a_0r}
\right]
}
{a_0-\chi r},
\qquad
0<r\le1.
}
```

This is the central result of the toy model.

---

## 9. Required limiting cases

### Perfect carrier survival

If

```math
\chi\to0,
```

then

```math
\boxed{
\eta_{\rm ext}
\to
1-e^{-a_0r}.
}
```

Only optical absorption matters, so the largest active fraction `r=1` is best.

### Vanishing active fraction

As

```math
r\to0,
```

```math
\boxed{
\eta_{\rm ext}\sim a_0r\to0.
}
```

Infinite grading fails because the active optical thickness disappears.

### Very optically thick active segment

If

```math
a\gg1,
```

generation occurs near the beginning of the active segment, farthest from the collector.

Then

```math
\boxed{
\eta_{\rm ext}
\to e^{-\xi}.
}
```

The detector becomes recombination limited by the longest active-segment delay.

### Weakly absorbing active segment

If

```math
a\ll1,
```

then generation is nearly uniform over the active segment and

```math
\boxed{
\eta_{\rm ext}
\simeq
 a\frac{1-e^{-\xi}}{\xi}.
}
```

This is absorptance times the uniform-generation collection factor.

---

## 10. There must be a finite optimum when recombination matters strongly enough

The two extremes are

```text
r -> 1
-> maximum absorbing length
-> longest carrier path / weakest grade

r -> 0
-> fastest collection
-> zero absorbing length.
```

Because `eta_ext -> 0` as `r -> 0`, arbitrarily strong grading cannot maximize external QE.

If recombination is sufficiently weak, `r=1` remains optimal.

If recombination is significant while the full absorber is optically thick, a finite interior optimum

```math
\boxed{0<r_*<1}
```

appears.

The optimum solves the one-dimensional equation

```math
\boxed{
\frac{d\eta_{\rm ext}}{dr}=0.
}
```

No simpler universal closed form is claimed.

---

## 11. Representative dimensionless optima

Numerical maximization of the exact formula gives:

| `a0` | `chi` | `r_*` | `eta_ext(r=1)` | `eta_ext(r_*)` |
|---:|---:|---:|---:|---:|
| 0.5 | 0.1 | 1.000 | 0.373 | 0.373 |
| 0.5 | 3 | 0.562 | 0.111 | 0.155 |
| 1 | 1 | 0.778 | 0.368 | 0.390 |
| 3 | 0.3 | 0.763 | 0.768 | 0.799 |
| 3 | 1 | 0.544 | 0.477 | 0.670 |
| 10 | 0.1 | 0.478 | 0.914 | 0.974 |
| 10 | 1 | 0.306 | 0.409 | 0.891 |

These are dimensionless toy-model examples, not HgCdTe device predictions.

The trend is physically clear:

> **The more optically redundant the absorber and the more recombination-limited its transport, the more useful it becomes to concentrate near-cutoff absorption near the collector.**

---

## 12. The front region becomes a transparent transport region

For

```math
r_*<1,
```

the wide-gap front portion

```math
L(1-r_*)
```

is transparent at the chosen near-cutoff photon energy.

But it still contributes to the bandgap drop that drives the minority electron toward the collector.

Thus the graded layer naturally separates functions:

```text
wide-gap front
-> supplies band-edge slope / transport drive
-> does not absorb the near-cutoff photon

low-gap rear near collector
-> supplies optical absorption
-> generated carriers travel only a short distance.
```

This is qualitatively similar to the broader detector-design strategy of separating absorption and transport/multiplication functions in heterostructures, although the present formula is not a model of any specific published architecture.

---

## 13. Exact small-signal response relative to incident photons

Let the incident photon flux be weakly modulated at angular frequency `omega`.

Define

```math
\Omega
=\omega T_a,
```

and

```math
z
=\xi+i\Omega.
```

The exact collected modulation transfer relative to incident photons is

```math
\boxed{
H_{\rm ext}(\Omega)
=
\frac{a[e^{-z}-e^{-a}]}
{a-z}.
}
```

At DC,

```math
H_{\rm ext}(0)
=\eta_{\rm ext}.
```

The normalized modulation response is

```math
\boxed{
\widehat H_{\rm ext}
=\frac{H_{\rm ext}(\Omega)}
{\eta_{\rm ext}}.
}
```

Thus the same model supplies

```text
absorptance
+
collection efficiency
+
frequency response
```

from one pair of dimensionless optical/transport parameters `a` and `xi`.

---

## 14. A key warning about apparently fast response

As grading becomes strong, near-cutoff absorption is forced closer to the collector.

This can increase the normalized electrical response speed even while the total absorbed/collected photon fraction falls.

Therefore a bandwidth increase caused by making much of the absorber optically inactive is not automatically a detector-performance improvement.

The correct comparison must keep at least

```text
external collected QE
+
frequency response
```

together.

This is the graded-absorber analogue of the earlier result that recombination can make a slow detector look fast by selecting only short-delay carriers.

---

## 15. Where the sharp-edge model will fail first

Real HgCdTe does not have a step-function absorption edge.

Primary intrinsic absorption spectroscopy reports

- composition- and temperature-dependent absorption edges;
- finite absorption tails;
- Urbach-like subgap behavior;
- doping-dependent Burstein-Moss shifts in degenerate material.

Therefore the transparent/absorbing boundary will be smoothed in a real graded HgCdTe layer.

The exact toy model should be treated as the limiting geometry to be attacked next with a realistic `alpha(E_gamma,E_g,T,n)`.

---

## 16. Claim boundary

### DERIVED within the sharp-edge + constant-drift + exponential-recombination model

For `Delta E_g > epsilon`,

```math
\boxed{
r=\varepsilon/\Delta E_g,}
```

```math
\boxed{
\ell_a=rL,
}

```math
\boxed{
T_a
=\frac{qL^2}{\mu_n\varepsilon}r^2,
}

```math
\boxed{
a=a_0r,\qquad \xi=\chi r^2,}
```

and

```math
\boxed{
\eta_{\rm ext}(r)
=
\frac{a_0[e^{-\chi r^2}-e^{-a_0r}]}
{a_0-\chi r}.
}
```

The full small-signal external transfer function is also derived exactly.

### CHECKED

Representative optima should be protected by numerical regression.

### KNOWN / PRIOR

- graded-gap carrier quasi-fields;
- Beer-Lambert absorption;
- recombination-limited minority transport;
- measured non-step HgCdTe absorption edges.

### NON-CLAIM

This file does not establish

- a realistic HgCdTe absorption coefficient;
- a universal optimal grade;
- that the front region is perfectly transparent;
- that mobility/lifetime stay constant with composition;
- that reflection/cavity effects are negligible;
- novelty of absorption/collection separation as a detector-design concept.

---

## 17. Next decisive step

Replace the sharp edge by a minimal continuous HgCdTe absorption law.

Use primary intrinsic absorption spectroscopy to construct or recover

```math
\alpha(E_\gamma;E_g,T,x,n).
```

Then numerically integrate

```math
H(\omega)
=\int_0^L
G(x;E_\gamma)
\exp[-(1/\tau_n+i\omega)t(x)]dx
```

through a linear or measured composition profile.

The research question becomes:

> **Does the interior optimum survive a realistic HgCdTe absorption edge, or was it an artifact of the step-edge model?**
