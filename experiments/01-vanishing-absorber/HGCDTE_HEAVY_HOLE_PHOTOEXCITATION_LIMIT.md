# HgCdTe Heavy-Hole Photoexcitation Limit — Why the Electron Can Receive Nearly All Photon Excess

**Date:** 2026-08-09  
**Status:** HgCdTe-specific model specialization using the established simplified Kane heavy-hole/electron band structure plus the repository energy-relaxation model; no novelty claim

## 1. Purpose

The wavelength-resolved branch introduced a parameter

```math
\xi_e
```

for the fraction of local photon excess

```math
u=E_\gamma-E_g
```

placed in the conduction electron at generation:

```math
\varepsilon_{\rm gen}=\xi_eu.
```

A symmetric two-band optical transition gives `xi_e=1/2`.

That is not the most natural HgCdTe limit for the dominant heavy-hole-to-electron transition.

---

## 2. HgCdTe simplified Kane band structure

Primary magneto-optical work on bulk HgCdTe uses a simplified `6 x 6` Kane model containing

```text
conduction electron branch
light-hole branch
nearly flat heavy-hole branch.
```

The experimentally observed interband transitions include transitions from the heavy-hole branch into the electron branch.

In the idealized simplified Kane limit, set the heavy-hole energy to the valence-edge reference

```math
E_{hh}(k)\approx E_v\approx0.
```

Then for a vertical heavy-hole-to-electron transition,

```math
E_\gamma
=E_e(k)-E_{hh}(k)
\approx E_e(k).
```

The local conduction edge is

```math
E_c=E_g.
```

Therefore the photoelectron excess above the local conduction edge is

```math
\boxed{
\varepsilon_{\rm gen}
=E_e-E_c
\approx E_\gamma-E_g.
}
```

Thus

```math
\boxed{\xi_e\approx1}
```

in the flat-heavy-hole simplified Kane limit.

This contrasts with the symmetric electron/light-hole two-band transition, where `xi_e=1/2`.

---

## 3. Physical meaning

The result is simply momentum/energy sharing.

A very heavy or nearly flat valence band absorbs little of the transition excess as hole kinetic energy, so most of the photon excess appears in the electron.

In a simple parabolic two-band picture,

```math
\xi_e
=\frac{m_h}{m_e+m_h}.
```

Hence

```math
m_h\gg m_e
\quad\Rightarrow\quad
\xi_e\to1.
```

Real HgCdTe has multiband mixing, finite heavy-hole curvature, nonparabolicity, and additional allowed transitions, so `xi_e=1` is a limiting baseline rather than a universal material constant.

---

## 4. Exit mean energy for arbitrary generation position

Use the linear graded absorber of the spectral branch.

Define

```math
\delta E=E_\gamma-E_{g,\rm out},
```

and local photon excess at generation

```math
u=E_\gamma-E_g(x).
```

The remaining downhill conduction-band drop is

```math
D(u)=\delta E-u.
```

Let

```math
K=G\ell_E.
```

The repository mean-energy equation gives

```math
\boxed{
\varepsilon_{\rm out}(u)
=
K+
(\xi_eu-K)
\exp\!\left[-\frac{\delta E-u}{K}\right].
}
```

This form makes the generation-position dependence transparent.

---

## 5. Exact extremum structure

Differentiate with respect to generation photon excess `u`:

```math
\boxed{
\frac{d\varepsilon_{\rm out}}{du}
=
\exp\!\left[-\frac{\delta E-u}{K}\right]
\left[
(\xi_e-1)
+
\frac{\xi_eu}{K}
\right].
}
```

For

```math
0<\xi_e<1,
```

the derivative changes sign at most once, from negative to positive, at

```math
\boxed{
u_*
=K\frac{1-\xi_e}{\xi_e}.}
```

when that point lies inside the physical interval.

Therefore any interior extremum is a **minimum**.

The maximum exit mean energy over all generation positions must occur at one of the two endpoints:

```math
\boxed{
\varepsilon_{\max}
=
\max\left[
K\left(1-e^{-\delta E/K}\right),
\xi_e\delta E
\right].
}
```

This is the central result.

The two endpoint terms have distinct meanings:

```text
earliest allowed absorption, u=0
-> cold generation
-> maximum remaining graded acceleration
-> maximum distance available for relaxation

latest possible absorption, u=delta E
-> zero remaining graded distance
-> electron starts with xi_e delta E
-> no downstream relaxation opportunity.
```

---

## 6. Heavy-hole limit

For

```math
\xi_e=1,
```

```math
\frac{d\varepsilon_{\rm out}}{du}
=
\exp[-(\delta E-u)/K]
\frac{u}{K}
\ge0.
```

Thus the exit mean energy increases monotonically with later generation.

The maximum is

```math
\boxed{
\varepsilon_{\max}=\delta E.
}
```

This is independent of `ell_E`.

Energy relaxation can cool electrons generated upstream, but it cannot cool an electron generated arbitrarily close to the output before that electron reaches the output.

---

## 7. Ballistic limit

For

```math
K\to\infty,
```

the earliest-generation endpoint becomes

```math
K(1-e^{-\delta E/K})\to\delta E.
```

Hence for any

```math
0\le\xi_e\le1,
```

```math
\boxed{
\varepsilon_{\max}^{\rm bal}=\delta E.
}
```

The heavy-hole limit is stronger because the same maximum remains even when energy relaxation is finite.

---

## 8. All-generation-position mean-II safety condition

Use the output threshold surrogate

```math
E_{\rm th,out}=\chi E_{g,\rm out}.
```

The exact all-generation-position condition inside the parameterized mean-energy model is

```math
\boxed{
\max\left[
K(1-e^{-\delta E/K}),
\xi_e\delta E
\right]
<
\chi E_{g,\rm out}.
}
```

This separates two ways to fail:

```text
upstream generation
-> too much accumulated graded-band work

near-output generation
-> too much initial photoexcitation energy.
```

For the heavy-hole limit `xi_e=1`, this reduces to

```math
\boxed{
\delta E
<
\chi E_{g,\rm out}.
}
```

independent of energy-relaxation length.

Equivalently,

```math
\boxed{
E_\gamma
<(1+\chi)E_{g,\rm out}.
}
```

or approximately

```math
\boxed{
\lambda_\gamma
>
\lambda_{c,\rm out}/(1+\chi).
}
```

For `chi=1`, the model boundary is one-half of the endpoint cutoff wavelength.

This is a mean-energy accessibility condition, not a stochastic impact-ionization probability.

---

## 9. Important consequence for the graded design

The spectral sorting effect now separates even more cleanly into two observables.

### Transit

Later absorption always shortens geometric transport distance and generally shortens ballistic transit time.

### Hot-electron energy

For heavy-hole-dominated photoexcitation, later absorption does **not** necessarily make the collected electron colder. In the flat-heavy-hole limit it can make the electron hotter at the output because less relaxation distance remains.

Therefore

> **wavelength-dependent timing can remain strong even when generation-position dependence of final hot-electron energy is weak or reversed.**

This distinction should be preserved in all future spectral-response calculations.

---

## 10. Prior-art boundary

Established primary HgCdTe work shows that the simplified Kane spectrum contains a nearly flat heavy-hole band and that observed interband transitions occur from the heavy-hole sector to the electron branch.

The use of a flat heavy-hole transition to infer that essentially all local photon excess appears in the electron is a direct consequence of that model, not a claimed new material property.

Real-device use requires an 8-band or comparable optical-transition calculation over the intended composition, temperature, and wavelength range.

---

## 11. Next decisive calculation

Use the heavy-hole baseline `xi_e approximately 1` and the exact optical-depth generation distribution to calculate

```text
wavelength-resolved mean transit
+
generation-position jitter
+
mean exit energy distribution
+
fraction of absorbed events born / arriving above the chosen II threshold surrogate.
```

Then compare the timing part against published tunable-pulse experiments.

The hot-electron part should remain explicitly model-level until an energy-dependent stochastic II rate is available.
