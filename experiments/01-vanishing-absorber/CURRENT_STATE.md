# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is graded HgCdTe carrier drive versus nonlocal hot-electron physics plus boundary TAT/BTBT; no novelty claim

## 1. Current question

The original active-volume hypothesis was falsified. The research path has moved through optical confinement, microscopic transitions, passive/active network resources, semiconductor extraction, tunneling, and finally HgCdTe band engineering.

The current question is:

> **Can a realistic graded HgCdTe detector use a composition-induced conduction-band slope for fast minority-electron collection, remain below the nonlocal impact-ionization regime in the absorber, and then place the unavoidable collection-boundary voltage in sufficiently wide-gap, low-defect material that TAT and direct BTBT remain controlled?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`
2. `HGCDTE_GRADED_ABSORBER_BOUNDARY_RELAXATION.md`
3. `HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md`
4. `HGCDTE_LINEAR_GRADED_KANE_WKB.md`
5. `HGCDTE_BOUNDARY_LAYER_TAT_TRADEOFF.md`
6. `HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`
7. `HGCDTE_ELECTROSTATIC_COMPENSATION_PEAK_FIELD_BOUND.md`
8. `HGCDTE_TAT_FIELD_SCALE.md`
9. `HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
10. `HGCDTE_GRADED_POISSON_ROBUSTNESS.md`
11. `CLAIM_LEDGER.md`
12. `RESEARCH_LOG.md`

Older optical/control branches remain provenance, not the current frontier.

---

## 3. Self-consistent graded absorber

For nondegenerate p-type HgCdTe in a quasi-neutral graded interior,

```math
p=N_v\exp[(E_v-E_F)/(k_BT)],
```

so

```math
\boxed{
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

For nearly constant `N_A/N_v`,

```math
\boxed{E_v\approx\text{constant}.}
```

With a gap decreasing in the electron-collection direction,

```math
G=-dE_g/dx>0,
```

and `E_c=E_v+E_g`, therefore

```math
\boxed{
S_c\equiv-dE_c/dx\approx G.
}
```

Thus ordinary equilibrium charge neutrality can naturally produce the favorable geometry

```text
majority-hole band nearly pinned
+
minority-electron conduction band downhill.
```

A uniformly depleted multi-micron picture is generally not the appropriate starting point because ordinary uncompensated charge gives an `N_eff L^2` Poisson penalty.

---

## 4. Direct-Zener geometry can be strongly suppressed by grading

For linear band edges, define

```math
S_c=-dE_c/dx,
\qquad
S_v=-dE_v/dx,
\qquad
G=-dE_g/dx.
```

Because `E_g=E_c-E_v`, identically

```math
\boxed{S_v=S_c-G.}
```

At fixed useful conduction slope `S_c=S`, define

```math
\delta=G/S.
```

The linear two-band/Kane WKB model gives

```math
\boxed{
\frac{\mathcal S_Z(\delta)}
{\mathcal S_Z(0)}
=
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}},
\qquad 0\le\delta<1.
}
```

The action increases monotonically and diverges as

```math
\delta\to1^-.
```

In the ideal quasi-neutral p-type limit,

```math
S_v\approx0,
\qquad
S_c\approx G,
\qquad
\delta\approx1.
```

So grading can suppress the ordinary same-direction direct-Zener path **without removing useful conduction-band drive**.

This is conditional on the smooth two-band/WKB model and does not eliminate TAT, interface tunneling, or hot-carrier processes.

---

## 5. New nonlocal penalty migration — carrier heating survives the grading escape

The carrier energy is controlled by the total conduction-band slope, not by how that slope is decomposed between electrostatic and composition terms.

Use the mean-energy equation

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

For cold injection,

```math
\boxed{
\varepsilon(x)
=
\int_0^x
S_c(s)
\exp\!\left[-\int_s^x\frac{du}{\ell_E(u)}\right]ds.
}
```

This is path dependent. Nonlocal impact ionization must therefore not be hidden inside a purely local field ceiling in the thin/fast regime.

For the favorable linear quasi-neutral graded absorber,

```math
E_g(x)=E_{g0}-Gx,
\qquad
S_c=G,
```

with constant `ell_E`,

```math
\boxed{
\varepsilon(x)=G\ell_E(1-e^{-x/\ell_E}).
}
```

Let

```math
\zeta=\Delta E_g/E_{g0},
\qquad
r=L/\ell_E.
```

Using the common HgCdTe APD threshold surrogate

```math
E_{\rm th}(x)=\chi E_g(x),
```

the exact mean-energy threshold boundary is

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

Threshold access occurs when

```math
\boxed{\zeta\ge\zeta_{\rm II}.}
```

### Ballistic limit

For `L/ell_E -> 0`,

```math
\boxed{
\zeta_{\rm II}\to\frac{\chi}{1+\chi}.
}
```

For `chi=1`,

```math
\boxed{\zeta_{\rm II}=1/2.}
```

Interpretation:

> in a ballistic quasi-neutral graded region, an electron has gained the lost gap energy. If the II threshold is approximately the local gap, mean threshold access occurs when the local gap has fallen to roughly half its entrance value.

Thus grading can eliminate one Zener geometry while leaving a separate hot-electron constraint.

---

## 6. Collection boundary — unavoidable voltage, but it can be put in better material

Let a wider-gap boundary increase the material gap by

```math
\Delta E_g^{(b)}>0
```

and let `alpha` be the conduction-band share of that material gap increase.

Barrier-free minority-electron extraction requires

```math
\boxed{
qV_b\ge\alpha\Delta E_g^{(b)}.
}
```

For any nonnegative one-dimensional field over boundary width `w`,

```math
V_b=\int_0^wF(x)dx,
```

so

```math
\boxed{F_{\max}\ge V_b/w.}
```

Delta doping or depletion shaping can move the field but cannot make this integral electrostatic resource disappear.

---

## 7. Local TAT/BTBT voltage-handling capacity

For local inverse-field tunneling constraints, define mechanism-specific characteristic fields `F_m(x)` and required exponent margins `Sigma_m`.

The local allowable field is

```math
\boxed{
F_{\rm allow}(x)
=
\min_m\frac{F_m(x)}{\Sigma_m}.
}
```

For the current boundary branch, the appropriate local mechanisms are TAT and direct BTBT where the local WKB approximations are valid.

A required compensation voltage is feasible under those local constraints iff

```math
\boxed{
V_b
\le
\int_0^wF_{\rm allow}(x)dx.
}
```

At minimum barrier-free compensation,

```math
\boxed{
\frac{\alpha\Delta E_g^{(b)}}{q}
\le
\int_0^wF_{\rm allow}(x)dx.
}
```

This gives the boundary an integrated **local tunneling voltage capacity**.

For a single exponent scale, the maximin field allocation is proportional to the local tolerance field:

```math
\boxed{F_{\rm opt}(x)\propto F_T(x).}
```

So more of the unavoidable field should be placed in wide-gap / deep-trap / low-leakage material.

Do not include nonlocal II in this local envelope unless a local-equilibrium reduction has been justified.

---

## 8. Minimum-compensation boundary is a hot-electron relaxation region

At the minimum barrier-free voltage,

```math
\boxed{qV_b=\alpha\Delta E_g^{(b)},}
```

so the net conduction-edge change is

```math
\boxed{\Delta E_c^{(b)}=0.}
```

The boundary therefore supplies no additional downhill conduction-band work.

The mean-energy equation becomes

```math
\boxed{
\frac{d\varepsilon}{ds}
=-\frac{\varepsilon}{\ell_{E,b}},
}
```

so

```math
\boxed{
\varepsilon_b(s)
=\varepsilon_a e^{-s/\ell_{E,b}}.
}
```

Meanwhile the local gap and therefore the approximate II threshold increase.

Hence, if the electron enters the boundary below mean threshold,

```math
\boxed{
\varepsilon_a<\chi E_{g,a},
}
```

then the minimally compensated monotonic wider-gap boundary cannot create a new mean-threshold crossing in this model.

This gives the architecture a natural division of labor:

```text
quasi-neutral graded absorber
-> use band-structure slope for fast collection
-> avoid direct-Zener overlap
-> respect the nonlocal carrier-energy phase boundary

wide-gap collection boundary
-> carry unavoidable electrostatic voltage
-> place field in high-tolerance material
-> suppress local TAT/BTBT
-> at minimum compensation allow hot carriers to relax.
```

Overcompensation makes the boundary conduction edge downhill again, increasing both local tunneling stress and hot-electron drive in exchange for additional boundary acceleration.

---

## 9. What current primary literature already establishes

Do not claim novelty for

- compositionally graded HgCdTe carrier drive / built-in quasi-electric fields;
- graded HgCdTe heterojunction and barrier engineering;
- TAT and BTBT in HgCdTe;
- electron-dominated impact ionization and dead-space physics in narrow-gap HgCdTe;
- energy-dependent Monte Carlo treatment of HgCdTe e-APDs;
- graded APD architectures with carrier relaxation regions.

The exact repository reductions above have not received a complete mathematical-priority audit.

---

## 10. Current numerical check

```text
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
```

checks

- the ballistic `zeta_c -> chi/(1+chi)` limit;
- monotonic movement of the phase boundary with relaxation strength;
- analytic phase-boundary equality against direct scanning of the graded energy trajectory.

The calculation is a regression of the surrogate, not a calibrated material simulation.

---

## 11. Current missing material inputs

The main quantitative uncertainty is no longer the algebra.

It is the target-composition transport data:

```text
energy-relaxation length / rate versus carrier energy and composition
+
energy-dependent electron impact-ionization rate
+
actual boundary trap spectrum, density and capture cross sections
+
real finite band profile under doping and bias.
```

Primary HgCdTe Monte Carlo work contains the required physics but the target `x approximately 0.20`, 77 K interpolation needed for a quantitative device frontier is not yet recovered.

---

## 12. Next decisive model

Build one finite piecewise-smooth device profile with

1. a quasi-neutral p-type graded absorber;
2. explicit `E_g(x)` and `E_c(x)`;
3. a wide-gap collection boundary at minimum and overcompensated bias;
4. local TAT + direct-BTBT constraints;
5. the nonlocal carrier-energy state propagated through the whole profile;
6. a parameterized `ell_E` sweep until target-specific transport data are available;
7. transit time calculated from a defensible velocity law rather than low-field mobility extrapolation.

The immediate goal is a **phase map**, not a manuscript:

```text
fast collection
vs
local tunneling margin
vs
nonlocal hot-electron margin.
```

Only after that map should publication significance be reassessed.
