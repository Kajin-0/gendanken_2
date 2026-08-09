# HgCdTe General Graded-Absorption Kernel — Arbitrary Local Optical Edge Coupled to Exact Drift/Recombination Delay

**Date:** 2026-08-09  
**Status:** exact change-of-variables formulation for any local absorption law `alpha(E_gamma-E_g)` in a linear graded neutral absorber; no calibrated HgCdTe spectrum assumed; no novelty claim

## 1. Purpose

The sharp-edge, square-root-edge, and arbitrary power-law analyses all found the same structural competition:

```text
stronger grade
-> optically active region shrinks
-> absorption moves toward collector
-> carrier delay falls faster than optical depth.
```

The next obvious attack is a realistic smooth subgap tail such as an Urbach edge.

Before choosing any empirical fit, this note derives the **general local-absorption kernel** for a linear grade.

The result shows exactly which optical properties can overturn the previous conclusion.

---

## 2. Linear gap and detuning coordinate

Use

```math
E_g(x)
=E_{g,\max}
-\frac{\Delta E_g}{L}x,
\qquad
0\le x\le L,
```

with the collector at `x=L` and

```math
E_\gamma
=E_{g,\min}+\varepsilon,
\qquad
\varepsilon>0.
```

Define

```math
\boxed{
r=\frac{\varepsilon}{\Delta E_g}.}
```

No restriction `r<=1` is required for the algebra, although `r<1` is the partially nominally transparent regime emphasized below.

Define the local photon detuning

```math
\boxed{
\delta(x)
=E_\gamma-E_g(x).
}
```

Because the gap is linear,

```math
\frac{d\delta}{dx}
=\frac{\Delta E_g}{L}
=\frac{\varepsilon}{rL}.
```

Therefore

```math
\boxed{
dx
=\frac{Lr}{\varepsilon}\,d\delta.}
```

At the front surface `x=0`,

```math
\boxed{
\delta_f
=\varepsilon-\Delta E_g
=\varepsilon\left(1-\frac1r\right).
}
```

At the collector,

```math
\boxed{
\delta_c=\varepsilon.}
```

---

## 3. Arbitrary local intrinsic absorption law

Let

```math
\boxed{
\alpha(\delta)
\ge0
}
```

be any local absorption coefficient at the photon energy of interest.

This may include

- a sharp threshold;
- a power-law allowed-direct edge;
- a smooth Kane-band edge;
- an Urbach tail;
- another empirically measured intrinsic spectrum.

For now it is only assumed to be a local function of detuning.

The optical depth from the front to a point with local detuning `delta` is

```math
\boxed{
\mathcal T(\delta;r)
=
\frac{Lr}{\varepsilon}
\int_{\delta_f}^{\delta}
\alpha(u)du.
}
```

The total optical depth is

```math
\boxed{
\mathcal A(r)
=
\frac{Lr}{\varepsilon}
\int_{\delta_f}^{\varepsilon}
\alpha(u)du.
}
```

The incident intensity fraction reaching detuning `delta` is

```math
\boxed{
I(\delta)/I_0
=e^{-\mathcal T(\delta;r)}.
}
```

---

## 4. Exact absorption probability density in detuning space

The probability per incident photon of absorption in interval `d delta` is

```math
\boxed{
dP_{\rm abs}
=
\frac{Lr}{\varepsilon}
\alpha(\delta)
 e^{-\mathcal T(\delta;r)}d\delta.
}
```

Integrating gives

```math
\int_{\delta_f}^{\varepsilon}dP_{\rm abs}
=1-e^{-\mathcal A(r)}.
```

Thus the ordinary absorptance is recovered exactly.

---

## 5. Carrier delay as a function of absorption energy coordinate

In the ideal pinned-valence low-field drift model, the conduction-band drop across the full graded region is approximately

```math
\Delta E_c\simeq\Delta E_g
=\varepsilon/r.
```

Therefore the minority-electron drift speed is

```math
\boxed{
v
=\frac{\mu_n\varepsilon}
{qLr}.}
```

The spatial distance from a point with detuning `delta` to the collector is

```math
L-x
=
\frac{Lr}{\varepsilon}
(\varepsilon-\delta).
```

Hence the deterministic collection delay is

```math
\boxed{
t(\delta;r)
=
\frac{qL^2r^2}
{\mu_n\varepsilon^2}
(\varepsilon-\delta).
}
```

Define

```math
\boxed{
T_\varepsilon
=\frac{qL^2}
{\mu_n\varepsilon}.
}
```

Then

```math
\boxed{
t(\delta;r)
=T_\varepsilon r^2
\left(1-\frac{\delta}{\varepsilon}\right).}
```

At the nominal band edge `delta=0`,

```math
\boxed{t=T_\varepsilon r^2,}
```

which reproduces the earlier active-segment delay.

At the physical front surface,

```math
\delta=\delta_f
=\varepsilon(1-1/r),
```

so

```math
\boxed{
t_{\rm front}=T_\varepsilon r.}
```

Thus subgap-tail absorption in the nominally transparent front can create longer-delay carriers, but even the full-thickness delay tends to zero linearly as `r -> 0` because the band-edge drive grows as `1/r`.

---

## 6. General collected small-signal transfer function

Let minority carriers survive with lifetime

```math
\tau_n.
```

Let the incident photon flux be weakly modulated at angular frequency `omega`.

Each absorbed photon at detuning `delta` contributes the survival/delay factor

```math
\exp[-(1/\tau_n+i\omega)t(\delta;r)].
```

Therefore the external collected transfer relative to incident photons is

```math
\boxed{
H(\omega;r)
=
\frac{Lr}{\varepsilon}
\int_{\delta_f}^{\varepsilon}
\alpha(\delta)
 e^{-\mathcal T(\delta;r)}
 e^{-(1/\tau_n+i\omega)t(\delta;r)}
 d\delta.
}
```

This is the master equation for the local-absorption / deterministic-drift model.

At DC,

```math
\boxed{
\eta_{\rm ext}(r)
=H(0;r).
}
```

The normalized detector response is

```math
\boxed{
\widehat H(\omega;r)
=H(\omega;r)/H(0;r).
}
```

The previous sharp-edge and power-law models are special cases of this equation.

---

## 7. Extreme-grading asymptotic for an integrable optical edge

Consider

```math
r\to0^+.
```

Then

```math
\delta_f
=\varepsilon(1-1/r)
\to-\infty.
```

Suppose the local absorption spectrum has finite integrated weight up to the photon energy:

```math
\boxed{
\mathcal W_\alpha(\varepsilon)
\equiv
\int_{-\infty}^{\varepsilon}
\alpha(\delta)d\delta
<\infty.
}
```

Then

```math
\mathcal A(r)
=\frac{Lr}{\varepsilon}
\int_{\delta_f}^{\varepsilon}
\alpha(\delta)d\delta
```

has asymptotic form

```math
\boxed{
\mathcal A(r)
\sim
\frac{Lr}{\varepsilon}
\mathcal W_\alpha(\varepsilon).
}
```

Therefore

```math
\boxed{
\mathcal A(r)\to0
}
```

linearly in `r`.

The absorptance obeys

```math
\boxed{
1-e^{-\mathcal A}
\sim
\frac{Lr}{\varepsilon}
\mathcal W_\alpha.
}
```

So **any intrinsic absorption edge with finite integrated subgap/near-edge spectral weight becomes optically thin under an infinitely steep linear grade**.

This includes ordinary power-law edges and exponential Urbach tails.

---

## 8. Urbach tail specifically does not rescue infinite grading

For a subgap Urbach form

```math
\alpha(\delta)
=\alpha_Ue^{\delta/E_U},
\qquad
\delta<0,
```

the integrated subgap weight is finite:

```math
\boxed{
\int_{-\infty}^0
\alpha_Ue^{\delta/E_U}d\delta
=\alpha_UE_U.
}
```

Therefore its contribution to the extreme-grade optical depth scales as

```math
\boxed{
\mathcal A_U(r)
\sim
\frac{Lr}{\varepsilon}
\alpha_UE_U.
}
```

The spatial Urbach-tail region shrinks with the inverse gap slope.

Thus smoothing the edge with an ordinary exponential tail does not fundamentally overturn the `optical depth ~ r` asymptotic.

---

## 9. Carrier survival becomes perfect in the same limit

For every physical point inside the finite layer,

```math
0\le t(\delta;r)\le T_\varepsilon r.
```

Therefore

```math
\boxed{
\max t\to0
\quad
\text{as }r\to0.
}
```

At fixed finite lifetime,

```math
\boxed{
 e^{-t/\tau_n}\to1
}
```

uniformly across the layer.

Hence in the extreme-grade limit with an integrable intrinsic absorption spectrum,

```math
\boxed{
\eta_{\rm ext}(r)
\sim
\mathcal A(r)
\propto r
\to0.
}
```

Infinite grading fails because absorption disappears, not because collection fails.

---

## 10. What kind of optical channel can defeat this asymptotic?

The integrability condition identifies the true optical counterexample.

If

```math
\alpha(\delta)
\to\alpha_{\rm bg}>0
```

as

```math
\delta\to-\infty,
```

then

```math
\int_{-\infty}^{\varepsilon}\alpha(\delta)d\delta
```

diverges.

The total optical depth need not vanish as `r -> 0`.

But such a channel is **not an intrinsic band-edge tail**.

It represents a separate absorption mechanism such as

- defect / impurity optical absorption;
- free-carrier absorption;
- another band/interband transition;
- strongly disordered midgap-state absorption.

Whether that absorption produces a useful collected electron-hole signal must then be modeled separately.

Thus the next counterexample is a **new optical channel**, not merely a different smooth band-edge shape.

---

## 11. Relation to the power-law existence result

The earlier power-law theorem proved that for any `m>-1`, nonzero recombination and sufficiently large optical thickness force at least one interior optimum `0<r_*<1`.

The general kernel here does not claim the same existence theorem for every integrable `alpha(delta)`.

What it establishes more generally is the boundary condition

```math
\boxed{
\eta_{\rm ext}(r)\to0
\quad
(r\to0)
}
```

for every finite-integrated-weight local absorption spectrum.

Therefore an infinitely steep grade cannot maximize collected QE in that class.

Whether the optimum is at `r=1` or at an interior `r_*` depends on the detailed optical profile and recombination burden.

---

## 12. Why this is useful for real HgCdTe

Real HgCdTe intrinsic absorption can now be inserted directly as

```math
\alpha(\delta;x,T,n)
```

without changing the transport kernel.

A measured or k·p-derived absorption law only changes the one-dimensional optical-depth integrals.

The transport side remains

```math
\boxed{
t(\delta;r)
=T_\varepsilon r^2
(1-\delta/\varepsilon)
}
```

inside the ideal pinned-valence constant-mobility approximation.

So the next empirical step is modular rather than a new derivation.

---

## 13. Claim boundary

### DERIVED for any local absorption law in the linear-grade drift model

```math
\boxed{
\mathcal A(r)
=\frac{Lr}{\varepsilon}
\int_{\delta_f}^{\varepsilon}
\alpha(u)du,
}
```

```math
\boxed{
t(\delta;r)
=\frac{qL^2r^2}
{\mu_n\varepsilon^2}
(\varepsilon-\delta),
}
```

and the master transfer kernel

```math
\boxed{
H(\omega;r)
=
\frac{Lr}{\varepsilon}
\int_{\delta_f}^{\varepsilon}
\alpha(\delta)
 e^{-\mathcal T(\delta;r)}
 e^{-(1/\tau_n+i\omega)t(\delta;r)}d\delta.
}
```

### DERIVED / CONDITIONAL asymptotic

If

```math
\int_{-\infty}^{\varepsilon}
\alpha(\delta)d\delta<\infty,
```

then

```math
\boxed{
\eta_{\rm ext}(r)\to0
\text{ linearly as }r\to0.
}
```

### KNOWN / PRIOR

- Urbach tails have finite exponential integrated weight;
- HgCdTe intrinsic absorption spectra depend on composition, temperature and carrier occupation;
- defect/free-carrier optical absorption can add separate subgap channels.

### NON-CLAIM

This file does not establish

- a universal interior optimum for every integrable optical spectrum;
- that all subgap absorption is harmless;
- that defect absorption generates the same useful signal as intrinsic interband absorption;
- a calibrated HgCdTe absorption law;
- novelty of the coordinate transformation.

---

## 14. Next decisive step

The intrinsic-edge-shape attack is now largely reduced to data insertion.

The next physically distinct optical attack is:

> **Add a separate subgap defect/free-carrier absorption channel in the wide-gap transport region and determine whether it creates useful signal, parasitic heating, or long-delay false response.**

Alternatively, for a clean material model, insert measured intrinsic HgCdTe `alpha(E)` and calculate the optimum grade numerically.

Do not keep changing above-gap edge exponents; that branch is already structurally resolved.