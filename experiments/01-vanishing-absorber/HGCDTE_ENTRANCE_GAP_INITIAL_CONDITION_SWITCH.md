# HgCdTe Entrance-Gap Initial-Condition Switch — The Transport-Independent Core of the Spectral Timing Branch

**Date:** 2026-08-09  
**Status:** exact high-optical-depth generation-geometry identity plus transport-functional chain rule; supersedes the entrance-gap timing maximum as the strongest transport-independent statement; no novelty claim

## 1. Purpose

The spectral branch has now been attacked with

```text
forward ballistic Kane transport
mean-energy relaxation
strong-scattering drift-diffusion
finite momentum-memory stochastic transport.
```

Those models do **not** agree on the exact short-wave timing curve.

They do agree on something more basic:

> At the photon energy equal to the entrance band gap, changing photon energy stops moving the first allowed generation position and begins changing the local photon-excess initial state instead.

This note isolates that statement from any particular transport closure.

---

## 2. Linear monotonic gap

Use

```math
\boxed{
E_g(x)=E_{g,\rm in}-Gx,
\qquad 0\le x\le L,
}
```

with

```math
G>0,
```

and

```math
E_{g,\rm out}=E_{g,\rm in}-GL.
```

Assume sufficiently high optical depth that absorption is strongly weighted toward the earliest energetically allowed region.

---

## 3. Earliest allowed generation position

For

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

the first location supporting ordinary above-gap interband absorption satisfies

```math
E_g(x_g)=E_\gamma.
```

Hence

```math
\boxed{
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

For

```math
E_\gamma\ge E_{g,\rm in},
```

the physical entrance is already optically allowed, so

```math
\boxed{x_g(E_\gamma)=0.}
```

Combine the two branches:

```math
\boxed{
x_g(E_\gamma)
=\max\!\left[
0,
\frac{E_{g,\rm in}-E_\gamma}{G}
\right].
}
```

Thus

```math
\boxed{
\frac{dx_g}{dE_\gamma}
=
\begin{cases}
-1/G, & E_\gamma<E_{g,\rm in},\\
0, & E_\gamma>E_{g,\rm in}.
\end{cases}
}
```

The generation-position sensitivity switches off at the entrance-gap energy.

---

## 4. Local photon excess at the earliest generation point

Define

```math
u_g(E_\gamma)
=E_\gamma-E_g[x_g(E_\gamma)].
```

Below the entrance gap, the earliest allowed point lies at the local edge, so

```math
\nu_g=0.
```

Above the entrance gap, generation is pinned at the physical entrance and

```math
\nu_g=E_\gamma-E_{g,\rm in}.
```

Therefore

```math
\boxed{
\nu_g(E_\gamma)
=\max(0,E_\gamma-E_{g,\rm in}).
}
```

and

```math
\boxed{
\frac{d\nu_g}{dE_\gamma}
=
\begin{cases}
0, & E_\gamma<E_{g,\rm in},\\
1, & E_\gamma>E_{g,\rm in}.
\end{cases}
}
```

The photon-energy sensitivity has moved from **position** to **initial excess energy**.

---

## 5. Electron initial-energy parameter

Write the electron share of the local photon excess as

```math
\boxed{
\varepsilon_g
=\xi_e\nu_g,
}
```

where `xi_e` depends on the optical transition and band structure.

In the simplified flat-heavy-hole HgCdTe Kane limit,

```math
\xi_e\approx1
```

is a physically relevant baseline, but no universal value is assumed here.

Then

```math
\boxed{
\frac{d\varepsilon_g}{dE_\gamma}
=
\begin{cases}
0, & E_\gamma<E_{g,\rm in},\\
\xi_e, & E_\gamma>E_{g,\rm in},
\end{cases}
}
```

if `xi_e` is locally treated as constant.

---

## 6. General transport functional

Let a measured intrinsic timing observable be represented schematically as

```math
\boxed{
\mathcal T
=\mathcal F(
x_g,
\varepsilon_g,
\mathcal P
),
}
```

where `mathcal P` contains the rest of the device/transport state:

```text
band profile
momentum-relaxation physics
energy relaxation
diffusion
contacts
recombination
etc.
```

The detailed form of `mathcal F` may come from

- ballistic transport;
- drift-diffusion;
- hydrodynamic moments;
- Boltzmann transport;
- Monte Carlo;
- experiment.

The chain rule gives two different spectral sensitivities on the two sides of the entrance gap.

### Below the entrance gap

```math
\boxed{
\frac{d\mathcal T}{dE_\gamma}
=-\frac1G
\frac{\partial\mathcal F}{\partial x_g}
}
```

when the earliest-generation approximation removes local photon excess.

Photon energy changes timing by moving the generation position.

### Above the entrance gap

```math
\boxed{
\frac{d\mathcal T}{dE_\gamma}
=\xi_e
\frac{\partial\mathcal F}{\partial\varepsilon_g}
}
```

when the generation position is pinned at the entrance.

Photon energy changes timing through the carrier initial state instead.

---

## 7. Entrance-gap slope-change diagnostic

Define the one-sided timing slopes at

```math
E_\gamma=E_{g,\rm in}.
```

Then, in the ideal sharp high-optical-depth limit,

```math
\boxed{
\left.\frac{d\mathcal T}{dE_\gamma}\right|_-
=-\frac1G\mathcal F_x,
}
```

and

```math
\boxed{
\left.\frac{d\mathcal T}{dE_\gamma}\right|_+
=\xi_e\mathcal F_\varepsilon,
}
```

with the derivatives evaluated at the entrance-generation state.

Thus the slope change is

```math
\boxed{
\Delta \mathcal T'
=\xi_e\mathcal F_\varepsilon
+\frac1G\mathcal F_x.
}
```

There is no theorem that this quantity must be nonzero.

An exact cancellation is possible.

Therefore even a visible cusp is not universal.

The robust statement is more modest:

> **the physical control variable through which wavelength perturbs the carrier problem changes at `E_gamma = Eg_in`.**

A measurable timing feature is expected only to the extent that the detector is sensitive differently to generation position and initial carrier state.

---

## 8. How previous transport models fit this identity

### Forward ballistic model

Below the entrance gap,

```text
upstream motion of x_g
-> longer path
-> timing increases.
```

Above the entrance gap,

```text
increasing epsilon_g
-> larger forward group velocity
-> timing decreases.
```

This gives a local maximum.

### Strong-scattering drift-diffusion model

Below the entrance gap,

```text
upstream motion of x_g
-> longer mean first-passage distance
-> timing increases.
```

Above the entrance gap, if effective drift coefficients forget the injection energy,

```math
\mathcal F_\varepsilon\approx0,
```

so timing approaches a plateau.

### Finite momentum-memory stochastic model

Above the entrance gap, the sign of the timing change depends on the longitudinal initial momentum distribution and its relaxation.

The short-wave slope can be negative, nearly zero, or positive in different admissible surrogates.

All are consistent with the same entrance-gap initial-condition switch.

---

## 9. Finite optical depth

A real detector does not generate every absorbed photon exactly at `x_g`.

The exact conditional generation distribution already derived in

`HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`

spreads generation over the optically eligible region.

Finite optical depth therefore smooths the sharp `max()` functions above.

The entrance-gap switch becomes a crossover over a finite spectral interval set by

```text
absorption coefficient
profile gradient
optical thickness
interference / photon trapping.
```

So even the word `knee` should be used carefully unless the calculated optical profile is sufficiently sharp.

The correct experimental expectation is

> **a spectral crossover tied to the independently known entrance-gap energy, not necessarily a mathematical cusp.**

---

## 10. Experimental consequence

The wavelength-sweep experiment should no longer be scored only by whether it shows a strict delay peak.

Instead compare the observed timing derivative or local spectral shape across the independently predicted

```math
\boxed{
\lambda_{g,\rm in}=hc/E_{g,\rm in}.
}
```

The post-crossover behavior becomes a transport diagnostic:

```text
negative slope
-> persistent directed hot-carrier memory / energy-dependent faster transport

near-zero slope
-> strong momentum randomization / saturated drift-like transport

positive slope or strong broadening
-> hot initial momentum spread, energy-dependent scattering, or another transport mechanism.
```

The location of the crossover tests the graded-generation geometry.

The shape around and beyond it tests the carrier dynamics.

---

## 11. Prior-art posture

The ingredients are established:

- graded HgCdTe spectral absorption;
- graded HgCdTe carrier transport;
- wavelength-dependent generation depth in semiconductors;
- drift-diffusion / hydrodynamic / Monte Carlo transport.

The focused repository search has not found an inspected primary HgCdTe source explicitly using the **entrance-gap initial-condition switch** to organize wavelength-resolved timing.

That remains only a negative search result.

**Status:** candidate detector-facing organizing principle / analytic reduction; priority unproven.

---

## 12. Next decisive work

The next model should stop asking whether a preselected peak survives.

Instead use a calibrated `Hg_0.8Cd_0.2Te`, 77 K transport closure and predict

```text
location of entrance-gap crossover
spectral slope below crossover
spectral slope above crossover
timing variance / impulse shape
sensitivity to momentum and energy relaxation.
```

If the spectral crossover remains tied to `Eg_in` under realistic optical generation and transport, that is the stronger result to take toward experiment and any later manuscript.
