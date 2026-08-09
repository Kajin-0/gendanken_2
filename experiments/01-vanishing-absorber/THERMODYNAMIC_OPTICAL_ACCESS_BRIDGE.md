# Thermodynamic Optical-Access Bridge — From a One-Sided Free-Space Coupling Bound to a Two-Access Detector Requirement

**Date:** 2026-08-08  
**Status:** derived restricted corollary combining prior thermodynamic light-coupling theory with the repository harmonic access theorem; strong prior-art overlap; no novelty claim  

## 1. Purpose

The passive multimode theorem says that useful optical-to-detector transfer is limited by the harmonic mean of two aggregate access resources:

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

By itself this does not bound `L` or `R` physically.

This note asks whether established electromagnetic/thermodynamic theory supplies a bound on the optical side `L`, and what follows for the required irreversible detector access `R`.

The answer is yes in a restricted free-space slab/channel setting already analyzed by Yu, Raman & Fan (2012).

---

## 2. Important convention audit

The repository state-space convention is

```math
\dot a
=
\left(-i\omega_0-\Gamma_L-\Gamma_R\right)a+
\sqrt{2\Gamma_L}\,s_L,
```

so `Gamma` denotes an **amplitude-decay rate**.

Stored energy therefore decays at twice that rate.

Yu, Raman & Fan use external modal coupling rates `gamma` in the standard energy-decay convention. Their Lorentzian denominator is

```math
(\omega-\omega_m)^2
+\frac{(\gamma_m+\tilde\gamma_m)^2}{4}.
```

Therefore the conversion is

```math
\boxed{
\gamma_{\rm energy}=2\Gamma_{\rm amplitude}.
}
```

This factor of two is load-bearing and must not be blurred.

---

## 3. Prior thermodynamic bound for one free-space channel

For optical modes in an angular-frequency interval of width

```math
W=\Delta\omega,
```

Yu, Raman & Fan derive, for any specified free-space radiation channel `n`,

```math
\boxed{
\sum_m \gamma_{m,n}
\le
\frac{W}{2\pi}.
}
```

Their `gamma_{m,n}` is the **energy-decay** rate from mode `m` into that free-space channel.

In the repository amplitude convention,

```math
\Gamma_{m,n}=\frac{\gamma_{m,n}}{2},
```

so the aggregate optical access associated with that one incident/radiative channel satisfies

```math
\boxed{
L_B
\equiv
\sum_m\Gamma_{m,n}
\le
\frac{W}{4\pi}.
}
```

This is established prior theory, not a result of this repository.

The original proof uses thermal equilibrium/Kirchhoff reasoning to show that a structure cannot emit more photon flux into a free-space channel than a blackbody; the resulting coupling-rate bound itself is then used for broadband absorption.

---

## 4. Combine with the two-access harmonic theorem

Now consider only the passive detector degrees of freedom relevant to that optical band and assume

- no direct optical-to-detector feedthrough;
- a finite or conditionally admissible passive network of the class covered by the harmonic theorem;
- the selected optical input is one free-space channel of the thermodynamic bound;
- modes sufficiently far outside the chosen band do not provide a material transfer contribution inside the band, or the analysis band is enlarged to include them;
- `R_B` is the total **amplitude-decay** access budget from the relevant detector network into the irreversible detector reservoir.

Then

```math
\mathcal I_B
\le
\mathcal I_{\rm all}
\le
\frac{2L_BR_B}{L_B+R_B}.
```

Because the harmonic expression increases monotonically with `L_B`, the thermodynamic optical ceiling gives

```math
\boxed{
\mathcal I_B
\le
\frac{
2\left(W/4\pi\right)R_B
}{
W/4\pi+R_B
}.
}
```

---

## 5. Average transfer over the band

Define the one-channel band-averaged transfer probability

```math
\overline T_B
\equiv
\frac{2\pi}{W}\mathcal I_B.
```

Then

```math
\boxed{
\overline T_B
\le
\frac{R_B}
{R_B+W/(4\pi)}.
}
```

This is the cleanest detector-facing form of the restricted corollary.

It says that once the optical side is pushed all the way to its thermodynamic one-channel coupling ceiling, the remaining bottleneck is the aggregate irreversible detector access.

---

## 6. Required detector-reservoir access for target broadband efficiency

Demand

```math
\overline T_B\ge\eta,
\qquad
0<\eta<1.
```

A necessary condition is then

```math
\eta
\le
\frac{R_B}{R_B+W/(4\pi)}.
```

Solving for `R_B`,

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

Thus within this restricted model:

1. required irreversible detector access grows **linearly with desired optical bandwidth**;
2. at fixed bandwidth it grows as `eta/(1-eta)`;
3. approaching perfect **band-averaged** transfer requires `R_B` to become large even after the optical side has already reached its thermodynamic maximum.

This is a necessary condition, not a sufficiency theorem.

---

## 7. Sanity checks

### Unlimited detector access

If

```math
R_B\to\infty,
```

then

```math
\overline T_B\le1.
```

The result reduces to the obvious probability ceiling.

### Weak detector access

If

```math
R_B\ll W/(4\pi),
```

then

```math
\overline T_B
\lesssim
\frac{4\pi R_B}{W}.
```

Broadening the accepted optical band with fixed irreversible access therefore reduces the maximum average transfer inversely with bandwidth.

### Narrow band

For fixed `R_B` and

```math
W\to0,
```

the bound tends to unity. Narrowband critical matching remains compatible with near-perfect transfer.

These limits are physically sensible.

---

## 8. Strong prior-art overlap

This corollary must be positioned conservatively.

Yu, Raman & Fan already connect an upper bound on sums of external modal coupling rates to broadband absorption. Their broadband absorption formula contains the familiar rate-matching structure

```text
external rate x internal absorption rate
----------------------------------------
          total decay rate
```

for individual resonances.

More recent multiresonant theory extends broadband absorption bounds to multiple overlapping resonances and explicitly treats mode density plus radiative/nonradiative decay as resources.

Therefore the repository must **not** claim discovery of

- critical/rate matching;
- the thermodynamic external-coupling sum bound;
- the idea that broadband absorption depends on radiative and absorptive rate resources;
- multiresonant broadband absorption limits.

The only useful distinction of the repository formulation is that its harmonic theorem was derived for an arbitrary finite passive internal network with coherent mode overlap/interference and an explicitly separate irreversible detector reservoir.

Whether the combined corollary is mathematically or conceptually distinct enough to publish is unassessed.

---

## 9. Scope limitations

The formula

```math
\overline T_B
\le
\frac{R_B}{R_B+W/(4\pi)}
```

is **not universal**.

It inherits assumptions from both ingredients, including

- the free-space radiation-channel setting of the thermodynamic coupling theorem;
- a band-limited modal description;
- passive linear dynamics;
- no ideal direct feedthrough;
- consistent mode accounting near band edges;
- a finite aggregate detector-reservoir access `R_B`;
- the repository amplitude-rate normalization.

It is not automatically applicable to waveguides, near-field channels, active/time-varying systems, arbitrary continua, or strongly nonlinear detectors without a new derivation.

---

## 10. What this exposes

The optical side now has a known physical resource bound in at least one important geometry.

The unresolved side is the irreversible detector reservoir:

```math
R_B.
```

The next natural question is therefore no longer purely optical:

> **What physical law limits how large `R_B` can be while false reverse transitions, thermal activation, reset cost, and detector stability remain controlled?**

That points directly to local detailed balance and thermodynamic irreversibility.

A minimal next model should separate

```text
forward detection/localization rate
```

from

```text
thermally activated reverse rate
```

rather than treating the detector bath as an arbitrarily strong one-way sink.