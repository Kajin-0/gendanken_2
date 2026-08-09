# HgCdTe Continuous Absorption-Edge Audit — The Graded Collection Optimum Survives a Smooth Direct-Gap Edge

**Date:** 2026-08-09  
**Status:** exact reduction for a simple square-root direct-absorption edge plus numerical optimization; optical law is a deliberate surrogate, not a calibrated HgCdTe spectrum; no novelty claim

## 1. Purpose

`HGCDTE_GRADED_ABSORPTION_COLLECTION_TRADEOFF.md` used a sharp step-function absorption edge and found that, when recombination matters and the absorber is optically thick, the best external collected QE can occur with

```math
0<r_*<1,
```

meaning a wide-gap transparent transport region followed by a lower-gap absorbing region near the collector.

The obvious criticism is that the result may be an artifact of the discontinuous optical edge.

This note attacks that concern with the simplest continuous allowed-direct-transition edge:

```math
\boxed{
\alpha
\propto
\sqrt{E_\gamma-E_g}
}
```

above threshold.

The interior optimum survives.

---

## 2. Linear graded gap

Use the same geometry:

```math
E_g(x)
=E_{g,\max}
-\frac{\Delta E_g}{L}x,
```

with collector at `x=L` and

```math
E_\gamma
=E_{g,\min}+\varepsilon.
```

For

```math
\Delta E_g>\varepsilon,
```

only the final segment

```math
\boxed{
\ell_a
=L\frac{\varepsilon}{\Delta E_g}
=rL
}
```

has local gap below the photon energy.

Again

```math
\boxed{r=\varepsilon/\Delta E_g.}
```

---

## 3. Continuous square-root absorption law

Measure distance into the optically active segment by

```math
0\le y\le\ell_a.
```

The local detuning above the band edge is

```math
E_\gamma-E_g(y)
=
\frac{\Delta E_g}{L}y.
```

Take

```math
\boxed{
\alpha(y)
=C_\alpha
\sqrt{
\frac{\Delta E_g}{L}y
},
}
```

where `C_alpha` collects the optical matrix-element / unit factors.

This square-root law is the standard parabolic allowed-direct-edge surrogate.

HgCdTe is strongly nonparabolic, so this is a **stress-test optical law**, not a quantitative HgCdTe absorption coefficient.

---

## 4. Cumulative optical depth

The optical depth from the start of the active region to position `y` is

```math
\tau_{\rm opt}(y)
=\int_0^y\alpha(y')dy'.
```

Therefore

```math
\boxed{
\tau_{\rm opt}(y)
=
\frac23C_\alpha
\sqrt{\frac{\Delta E_g}{L}}
 y^{3/2}.
}
```

At the collector `y=ell_a`,

```math
\tau_{\rm opt}(\ell_a)
=
\frac23C_\alpha
\sqrt{\frac{\Delta E_g}{L}}
\left(
L\frac{\varepsilon}{\Delta E_g}
\right)^{3/2}.
```

Hence

```math
\boxed{
\tau_{\rm opt,tot}
=
\frac23C_\alpha L
\frac{\varepsilon^{3/2}}
{\Delta E_g}.
}
```

The crucial scaling is

```math
\boxed{
\tau_{\rm opt,tot}
\propto
1/\Delta E_g.
}
```

Since

```math
r=\varepsilon/\Delta E_g,
```

define

```math
\boxed{
a_0
=\frac23C_\alpha L\sqrt\varepsilon.}
```

Then

```math
\boxed{a=a_0r.}
```

Thus the total optical thickness falls **linearly** with active fraction `r`, just as in the sharp-edge model.

---

## 5. Normalized coordinate

Define

```math
u=y/\ell_a,
\qquad
0\le u\le1.
```

Then

```math
\boxed{
\tau_{\rm opt}(u)
=a u^{3/2}.
}
```

The probability per incident photon of absorption between `u` and `u+du` is

```math
-d(e^{-\tau_{\rm opt}})
=
\frac32 a u^{1/2}
 e^{-a u^{3/2}}du.
```

---

## 6. Transport survival

The drift velocity from the bandgap quasi-field is unchanged from the previous toy model:

```math
v
=\frac{\mu_n\Delta E_g}{qL}.
```

The maximum active-segment transit time is

```math
T_a
=\frac{qL^2\varepsilon}
{\mu_n(\Delta E_g)^2}.
```

Let

```math
\boxed{
\xi
=T_a/\tau_n
=\chi r^2,
}
```

where

```math
\boxed{
\chi
=\frac{qL^2}
{\mu_n\tau_n\varepsilon}.
}
```

A carrier generated at normalized coordinate `u` is distance

```math
\ell_a(1-u)
```

from the collector and survives with probability

```math
\boxed{
\exp[-\xi(1-u)].
}
```

---

## 7. Exact external collected QE integral

Multiply the generation probability by the survival probability:

```math
\eta_{\rm ext}
=
\int_0^1
\frac32 a u^{1/2}
 e^{-a u^{3/2}}
 e^{-\xi(1-u)}du.
```

Now substitute

```math
t=u^{3/2}.
```

Then

```math
u=t^{2/3}
```

and

```math
\frac32u^{1/2}du=dt.
```

Therefore the exact one-dimensional form is

```math
\boxed{
\eta_{\rm ext}(a,\xi)
=
a e^{-\xi}
\int_0^1
\exp[-at+\xi t^{2/3}]dt.
}
```

With

```math
a=a_0r,
\qquad
\xi=\chi r^2,
```

```math
\boxed{
\eta_{\rm ext}(r)
=
a_0r\,e^{-\chi r^2}
\int_0^1
\exp[-a_0rt+\chi r^2 t^{2/3}]dt.
}
```

This replaces the elementary sharp-edge formula with one benign quadrature.

---

## 8. Optical-only limit

If

```math
\xi=0,
```

then

```math
\eta_{\rm ext}
=a\int_0^1e^{-at}dt.
```

Hence

```math
\boxed{
\eta_{\rm ext}
=1-e^{-a}.
}
```

So the optical limit is exactly the absorptance associated with the total integrated optical depth.

---

## 9. Infinite grading still fails

As

```math
r\to0,
```

```math
a=a_0r\to0
```

and

```math
\xi=\chi r^2\to0.
```

Therefore

```math
\boxed{
\eta_{\rm ext}\sim a_0r\to0.
}
```

So the continuous edge preserves the same essential boundary condition:

> arbitrarily strong grading eventually destroys near-cutoff absorption.

---

## 10. Exact modulation transfer function

Let the incident photon flux be weakly modulated at angular frequency `omega`.

Define

```math
\Omega=\omega T_a,
```

and

```math
\boxed{z=\xi+i\Omega.}
```

Each generated carrier contributes the factor

```math
\exp[-z(1-u)].
```

Therefore

```math
H_{\rm ext}
=
\int_0^1
\frac32 a u^{1/2}
 e^{-a u^{3/2}}
 e^{-z(1-u)}du.
```

The same substitution gives

```math
\boxed{
H_{\rm ext}(a,z)
=
ae^{-z}
\int_0^1
\exp[-at+z t^{2/3}]dt.
}
```

At DC,

```math
H_{\rm ext}(a,\xi)
=\eta_{\rm ext}.
```

The normalized detector response is

```math
\boxed{
\widehat H
=H_{\rm ext}(a,\xi+i\Omega)
/\eta_{\rm ext}.
}
```

Thus the smooth optical model still gives the full collected-QE / modulation response from only `a` and `xi`.

---

## 11. Numerical stress test of the interior optimum

Optimize over

```math
0<r\le1.
```

Representative results:

| `a0` | `chi` | `r_*` | `eta_ext(r=1)` | `eta_ext(r_*)` |
|---:|---:|---:|---:|---:|
| 0.5 | 0.1 | 1.000 | 0.373 | 0.373 |
| 0.5 | 3 | 0.627 | 0.145 | 0.165 |
| 1 | 1 | 0.833 | 0.427 | 0.434 |
| 3 | 0.3 | 0.797 | 0.782 | 0.807 |
| 3 | 1 | 0.601 | 0.562 | 0.693 |
| 10 | 0.1 | 0.505 | 0.938 | 0.979 |
| 10 | 1 | 0.323 | 0.521 | 0.907 |

The values shift relative to the sharp-edge model, but the qualitative result survives:

> **When optical depth is abundant and recombination penalizes long carrier paths, the collected-QE optimum can place part of the graded absorber above the photon energy so that near-cutoff generation is concentrated closer to the collector.**

---

## 12. Why the result survives smoothing

The key competition is structural rather than step-edge-specific.

For the linear grade and square-root absorption edge:

```text
integrated optical depth
~ r
```

while

```text
maximum collection delay
~ r^2.
```

Therefore the transport benefit initially improves faster with stronger grading than the optical depth is lost.

Eventually optical depth becomes too small and external QE falls to zero.

That naturally permits a finite optimum.

---

## 13. What a realistic HgCdTe edge can change

Real HgCdTe absorption differs from the simple square-root edge because of

- Kane nonparabolicity;
- temperature-dependent band structure;
- Fermi occupation / Pauli blocking;
- doping and Burstein-Moss shifts;
- Urbach/subgap tails;
- heavy-hole/light-hole contributions;
- spatial composition dependence of optical matrix elements.

Primary HgCdTe literature contains intrinsic absorption spectroscopy and k·p calculations across temperature/composition, so a realistic replacement is possible.

The interior optimum may shift or disappear if the real absorption tail supplies enough useful absorption in the nominally high-gap region.

That is precisely the next test.

---

## 14. Claim boundary

### DERIVED within the continuous square-root-edge surrogate

```math
\boxed{
a=a_0r,}
```

```math
\boxed{
\xi=\chi r^2,
}

```math
\boxed{
\eta_{\rm ext}
=ae^{-\xi}
\int_0^1e^{-at+\xi t^{2/3}}dt,
}
```

and

```math
\boxed{
H_{\rm ext}(a,z)
=ae^{-z}
\int_0^1e^{-at+zt^{2/3}}dt.
}
```

### CHECKED

Numerical optimization shows interior optima for broad optically thick / recombination-sensitive parameter ranges.

### KNOWN / PRIOR

- allowed-direct square-root absorption edge as a simple parabolic-band model;
- intrinsic HgCdTe absorption spectroscopy and more detailed band-structure calculations;
- graded-band carrier transport.

### NON-CLAIM

This file does not establish

- that HgCdTe follows an exact square-root edge;
- a universal optimum `r_*`;
- that near-cutoff transparency is abrupt;
- that mobility/lifetime are composition independent;
- novelty of function-separating graded absorbers.

---

## 15. Next step

The step-edge criticism is now closed at the level of one smooth analytic edge.

Next:

1. recover a primary HgCdTe intrinsic absorption model or dataset near the target cutoff;
2. parameterize `alpha(E_gamma,x,T)` along a realistic composition grade;
3. retain the exact transport kernel rather than fitting a new speed law;
4. ask whether `r_*<1` survives for realistic MWIR/LWIR parameters;
5. if it does, compare the predicted transparent-front / absorbing-rear architecture with published graded-band HgCdTe detector structures.