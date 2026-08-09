# HgCdTe Power-Law Absorption-Edge Generalization — Why the Transparent-Front Optimum Is Structurally Robust

**Date:** 2026-08-09  
**Status:** exact analytic generalization across local power-law absorption edges; generic optical model family, not a calibrated HgCdTe spectrum; no novelty claim

## 1. Purpose

Two previous models found the same qualitative graded-absorber behavior:

- a sharp absorption edge;
- a square-root direct-gap absorption edge.

Both produced a finite optimum in which the high-gap front of the absorber becomes transparent at a near-cutoff wavelength while absorption is concentrated closer to the collector.

This note asks whether the result depends on the particular edge exponent.

Take the entire local family

```math
\boxed{
\alpha
=C_m(E_\gamma-E_g)^m,
\qquad
m>-1,
}
```

above the local absorption edge and zero below it.

The main scaling survives for every `m` in this family.

---

## 2. Linear graded gap and active fraction

Use

```math
E_g(x)
=E_{g,\max}
-\frac{\Delta E_g}{L}x,
```

with collector at `x=L` and photon detuning

```math
\varepsilon
=E_\gamma-E_{g,\min}>0.
```

For

```math
\Delta E_g>\varepsilon,
```

the optically active segment has length

```math
\boxed{
\ell_a
=L\frac{\varepsilon}{\Delta E_g}
=rL,
}
```

where

```math
\boxed{
r=\varepsilon/\Delta E_g.}
```

---

## 3. Local detuning inside the active segment

Measure distance into the active segment by

```math
0\le y\le\ell_a.
```

The local photon detuning is

```math
\boxed{
E_\gamma-E_g(y)
=\frac{\Delta E_g}{L}y.
}
```

Thus

```math
\boxed{
\alpha(y)
=C_m
\left(
\frac{\Delta E_g}{L}y
\right)^m.
}
```

---

## 4. Total optical depth — exponent-independent grade scaling

Integrate over the active segment:

```math
\tau_{\rm opt,tot}
=
C_m
\left(
\frac{\Delta E_g}{L}
\right)^m
\int_0^{\ell_a}y^m dy.
```

For `m>-1`,

```math
\boxed{
\tau_{\rm opt,tot}
=
\frac{C_m}{m+1}
\left(
\frac{\Delta E_g}{L}
\right)^m
\ell_a^{m+1}.
}
```

Substitute

```math
\ell_a=L\varepsilon/\Delta E_g.
```

Then

```math
\boxed{
\tau_{\rm opt,tot}
=
\frac{C_mL\varepsilon^{m+1}}
{(m+1)\Delta E_g}.
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
=\frac{C_mL\varepsilon^m}{m+1}.}
```

Therefore

```math
\boxed{
a
\equiv
\tau_{\rm opt,tot}
=a_0r.
}
```

This is the first central result:

> **For every local power-law absorption edge `m>-1`, the total near-cutoff optical depth of a linear graded absorber decreases linearly with the active fraction `r`.**

The exponent changes the generation profile but not the `r` scaling of total optical depth.

---

## 5. Cumulative optical depth

Normalize position by

```math
u=y/\ell_a.
```

Then

```math
\tau_{\rm opt}(u)
=a u^{m+1}.
```

Therefore the probability per incident photon of absorption in `du` is

```math
\boxed{
dP_{\rm abs}
=(m+1)a u^m
 e^{-a u^{m+1}}du.
}
```

---

## 6. Transport scaling remains quadratic

In the pinned-valence graded-neutral drift model,

```math
v
=\frac{\mu_n\Delta E_g}{qL}.
```

The maximum travel distance of a carrier generated in the active region is

```math
\ell_a=rL.
```

Therefore

```math
T_a
=\frac{\ell_a}{v}
=
\frac{qL^2\varepsilon}
{\mu_n(\Delta E_g)^2}.
```

Define

```math
\boxed{
\chi
=\frac{qL^2}
{\mu_n\tau_n\varepsilon}.
}
```

Then

```math
\boxed{
\xi
=T_a/\tau_n
=\chi r^2.
}
```

Thus the second central result is unchanged by the optical edge model:

```text
optical depth
~ r

maximum transport/recombination penalty
~ r^2.
```

---

## 7. Exact external collected QE for arbitrary `m`

A carrier generated at normalized coordinate `u` survives to the collector with probability

```math
\exp[-\xi(1-u)].
```

Therefore

```math
\eta_{\rm ext}
=
\int_0^1
(m+1)a u^m
 e^{-a u^{m+1}}
 e^{-\xi(1-u)}du.
```

Now define

```math
t=u^{m+1}.
```

Then

```math
(m+1)u^mdu=dt,
```

and

```math
u=t^{1/(m+1)}.
```

Hence

```math
\boxed{
\eta_{\rm ext}(a,\xi;m)
=
a e^{-\xi}
\int_0^1
\exp\left[
-at+
\xi t^{1/(m+1)}
\right]dt.
}
```

Using

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
\exp\left[
-a_0rt
+\chi r^2t^{1/(m+1)}
\right]dt.
}
```

The step-edge case is `m=0`.

The square-root direct-edge surrogate is `m=1/2`.

---

## 8. Exact small-signal response

Define

```math
\Omega=\omega T_a,
```

and

```math
z=\xi+i\Omega.
```

The collected modulation response relative to incident photons is

```math
\boxed{
H_{\rm ext}(a,z;m)
=
a e^{-z}
\int_0^1
\exp\left[
-at+zt^{1/(m+1)}
\right]dt.
}
```

At DC,

```math
H_{\rm ext}(a,\xi;m)
=\eta_{\rm ext}.
```

Thus the family retains a one-dimensional quadrature for the full optical-generation + recombination + transit response.

---

## 9. Universal limiting behavior as `r -> 0`

For

```math
r\to0,
```

both

```math
a=a_0r\to0
```

and

```math
\xi=\chi r^2\to0.
```

The integral tends to one, so

```math
\boxed{
\eta_{\rm ext}
\sim a_0r
\to0.
}
```

Therefore infinite grading cannot maximize near-cutoff collected QE for any member of the power-law family.

---

## 10. Optically thick asymptotic

Now hold a finite `r>0` and finite `xi>0` while taking

```math
a=a_0r\to\infty.
```

The absorption distribution becomes concentrated near

```math
u=0,
```

the beginning of the active segment, which is the point farthest from the collector.

Mathematically, the factor

```math
a e^{-at}dt
```

approaches a unit mass near `t=0`.

Therefore

```math
\boxed{
\eta_{\rm ext}
\to e^{-\xi}
}
```

for every finite `m>-1`.

Since

```math
\xi=\chi r^2,
```

```math
\boxed{
\eta_{\rm ext}
\to e^{-\chi r^2}.
}
```

In this optically thick limit, reducing `r` below one **always increases** collected QE whenever

```math
\chi>0.
```

---

## 11. Interior-optimum existence result

For every finite power-law exponent

```math
m>-1
```

and every nonzero recombination penalty

```math
\chi>0,
```

consider sufficiently large ungraded optical thickness `a0`.

At `r=1`, the optically thick asymptotic gives

```math
\eta_{\rm ext}
\simeq e^{-\chi}.
```

Its local slope with respect to `r` approaches

```math
\boxed{
\frac{d\eta_{\rm ext}}{dr}
\to
-2\chi r e^{-\chi r^2}.
}
```

At `r=1`, this is strictly negative.

Therefore decreasing `r` slightly below one improves collected QE.

But as shown above,

```math
\eta_{\rm ext}\to0
```

when

```math
r\to0.
```

By continuity, there must be at least one maximum at

```math
\boxed{
0<r_*<1.
}
```

Hence:

> **For any finite power-law absorption-edge exponent `m>-1` and any finite recombination penalty `chi>0`, a sufficiently optically thick graded absorber necessarily develops a finite transparent-front / absorbing-rear optimum.**

This is the strongest general statement of the present graded-collection toy family.

---

## 12. What this does and does not depend on

The existence result does **not** depend on the exact power-law exponent.

It depends on three structural facts:

1. a linear grade makes the optically active length shrink as `r`;
2. any local power-law edge gives integrated optical depth proportional to `r`;
3. the same grade makes maximum carrier transit time shrink as `r^2`.

The result can fail if a real optical edge violates those assumptions strongly enough—for example if subgap tails allow the nominally transparent front to continue absorbing substantially.

---

## 13. Urbach-tail / disorder escape

A real HgCdTe high-gap front may not be transparent at the photon energy because of

- Urbach tails;
- disorder;
- defect absorption;
- free-carrier absorption;
- band-tail states.

That can alter the scaling because absorption no longer switches off when

```math
E_g>E_\gamma.
```

If the tail remains strong throughout the wide-gap region, photons can again generate carriers far from the collector, weakening the transparent-front advantage.

This is now the most direct optical counterexample to the power-law theorem.

---

## 14. Claim boundary

### DERIVED

For the full local power-law family `m>-1`:

```math
\boxed{a=a_0r,}
```

```math
\boxed{\xi=\chi r^2,}
```

and

```math
\boxed{
\eta_{\rm ext}
=ae^{-\xi}
\int_0^1
 e^{-at+\xi t^{1/(m+1)}}dt.
}
```

### DERIVED / CONDITIONAL existence result

For any

```math
m>-1,
\qquad
\chi>0,
```

sufficiently large `a0` implies at least one optimum

```math
\boxed{0<r_*<1.}
```

### KNOWN / PRIOR

- local power-law direct absorption edges;
- graded-band transport;
- recombination-limited minority-carrier collection.

### NON-CLAIM

This file does not establish

- a universal HgCdTe optical edge;
- a unique optimum;
- robustness to strong Urbach/subgap absorption tails;
- composition-independent mobility/lifetime;
- novelty of transparent-window / separate-absorption-region device concepts.

---

## 15. Next decisive attack

The power-law edge family is now too broad for changing the exponent alone to be a useful counterexample.

The next optical attack should target the assumption that the wide-gap front becomes truly transparent.

Use an **Urbach-tail absorption law** in the nominally forbidden region and ask:

> **How large must the subgap-tail energy be before far-from-collector absorption destroys the graded transparent-front optimum?**

That is a more physically discriminating test than choosing another above-gap exponent.