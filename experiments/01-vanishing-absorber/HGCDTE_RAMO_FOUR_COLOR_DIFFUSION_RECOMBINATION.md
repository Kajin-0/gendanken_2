# HgCdTe Four-Color Shockley-Ramo Closure — Diffusion and Recombination Stress

**Date:** 2026-08-10  
**Status:** **CONDITIONAL / CHECKED** stochastic robustness stress using the corrected raw-current observable; not a calibrated device prediction and no novelty claim

## 1. Question

The corrected material worked example used deterministic/high-Peclet propagation and found a gradient-sensitive four-color phase scale around

```text
-0.0124 deg at 100 MHz.
```

That analytic limit is useful, but real HgCdTe minority carriers diffuse and recombine.

The next adversarial question is:

> **Does ordinary Einstein diffusion or a finite uniform lifetime erase the corrected four-color bulk-gradient signal before any exotic transport physics is invoked?**

For the explicit theory stress used here, no.

---

## 2. Same optical and velocity profile

Retain the previous material model:

```text
T = 300 K
L = 7.6 um
linear x=0.55 -> 0.32
Hansen gap
Moazzami Beer-Lambert generation
mobility sensitivity scale = 9000 cm2/Vs
quasi-neutral gap-gradient drive
8 kV/cm velocity-saturation sensitivity scale
reduced DOS-gradient correction.
```

The four mean generation depths remain

```text
2.5, 3.0, 3.5, 4.0 um
```

with wavelengths approximately

```text
2.134651, 2.215042, 2.301173, 2.393907 um.
```

All modeled absorbed fractions remain above `0.9993`.

The Einstein diffusion coefficient is

```math
\boxed{
D\simeq0.02327\ \mathrm{m^2/s}.
}
```

The graded drift is the same approximately

```text
3.76e4 -> 3.21e4 m/s
```

profile used in the deterministic example.

---

## 3. Stochastic raw-current backward resolvent

For uniform planar weighting and one signal carrier, define the expected discounted induced-current functional `J(z,s)`.

With constant `D`, spatially varying drift `v(z)`, and uniform Markov recombination rate `kappa`, it obeys

```math
\boxed{
D J''(z)
+v(z)J'(z)
-(\kappa+s)J(z)
=-v(z).
}
\tag{1}
```

The irrelevant common factor `qE_w` has been removed.

At the collector,

```math
\boxed{J(L,s)=0.}
```

because a carrier beginning at the collecting boundary has no remaining induced-current trajectory.

---

## 4. Remove the upstream-boundary confound explicitly

The previous three-color HgCdTe calculation was badly confounded by a reflecting entrance boundary.

This stress deliberately does **not** impose a reflecting or absorbing surface at `z=0`.

Instead extend the medium conceptually to `z<0` with constant drift equal to `v(0)` and the same `D,kappa`.

The bounded semi-infinite solution there is

```math
J(z)=J_p+A e^{r_+z},
```

with

```math
J_p=\frac{v_0}{\kappa+s},
```

```math
r_+
=\frac{-v_0+\sqrt{v_0^2+4D(\kappa+s)}}{2D}.
```

Matching at `z=0` gives the Robin condition

```math
\boxed{
J'(0)=r_+[J(0)-J_p].
}
\tag{2}
```

This is a mathematical **bulk continuation**, not a model of a real detector surface.

Its sole purpose is to prevent a finite entrance boundary from generating the closure signal being attributed to the graded bulk.

---

## 5. Homogeneous same-optics reference

For each `kappa`, construct the homogeneous comparison using

```text
same D
same kappa
same four real optical generation kernels
constant drift = path-harmonic mean of v(z).
```

The homogeneous point-source exponent is

```math
\gamma
=\frac{\sqrt{w^2+4D(\kappa+i\omega)}-w}{2D}.
```

Its raw current has

```math
J_{hom}(z)\propto1-e^{-\gamma(L-z)}.
```

Averaging over the same optical kernels gives the finite-width optical-shape reference.

Subtracting its logarithmic four-color closure from the graded result defines the **gradient-sensitive excess** for this explicit stochastic stress.

---

## 6. No-recombination diffusion result

With finite Einstein diffusion but

```math
\kappa=0,
```

the approximate phase closures are

| RF | Variable stochastic transport | Homogeneous same-optics | Excess |
|---:|---:|---:|---:|
| 100 MHz | `-0.00952 deg` | `+0.00246 deg` | `-0.01198 deg` |
| 500 MHz | `-0.04643 deg` | `+0.01230 deg` | `-0.05873 deg` |
| 1 GHz | `-0.08572 deg` | `+0.02470 deg` | `-0.11041 deg` |

The deterministic high-Peclet excess at `100 MHz` was approximately

```text
-0.01238 deg.
```

Thus the full finite-diffusion result changes the low-RF scale by only a few percent in this example.

This is notable because the quartet spacing is not asymptotically high-Peclet on the scale of a single `0.5 um` step.

---

## 7. Uniform recombination does not erase the signal

Use uniform first-order lifetimes as sensitivity stresses.

### `tau = 10 ns`

At `100 MHz`,

```text
gradient-sensitive excess ~ -0.01205 deg.
```

### `tau = 1 ns`

At `100 MHz`,

```text
gradient-sensitive excess ~ -0.01275 deg.
```

For the `1 ns` stress the excess is approximately

```text
-0.0627 deg at 500 MHz
-0.1188 deg at 1 GHz.
```

The exact numbers depend on the conditional transport model, but the qualitative result is robust in this range:

> **ordinary finite diffusion and uniform Markov recombination do not wash out the four-color bulk-gradient closure in the stated HgCdTe stress.**

---

## 8. Why this is consistent with the exact uniform-recombination theorem

For spatially uniform drift/diffusion/recombination, raw Ramo current still has only one exponential propagation mode after removing the constant particular term:

```math
J(d,s)=C(s)[1-e^{-\gamma(s)d}].
```

Uniform recombination therefore changes `gamma` but does not create an independent spatial mode.

The graded sample violates homogeneous closure because `v(z)` changes with depth, not merely because recombination exists.

This explains why finite `kappa` perturbs but does not destroy the gradient-sensitive closure.

---

## 9. Relation to the low-RF analytic theorem

The deterministic point-source theorem gave at `100 MHz`

```text
~ -0.01254 deg
```

for the same profile and spacing.

The full stochastic finite-width no-recombination calculation gives

```text
~ -0.01198 deg
```

for the gradient-sensitive excess.

The difference is the ordinary stochastic/diffusive correction expected when moving away from the strict high-Peclet limit.

The close scale agreement strengthens, rather than proves, the physical interpretation of the closure as a bulk slowness-gradient probe within this controlled model.

---

## 10. What is still missing

This stress has deliberately removed rather than modeled several conventional complications:

```text
real entrance surface/boundary
second carrier contribution
nonuniform weighting field
junction/depletion-region signal
wavelength-dependent electronics
contact response
non-Markov trapping
nonlocal/hot-carrier transport.
```

Those should be added **one at a time**.

A model should not receive multiple new nuisance mechanisms simultaneously merely to improve a fit.

---

## 11. Falsification consequence

The result closes one obvious skeptical objection:

```text
"The four-color gradient signal exists only because diffusion was artificially switched off."
```

That objection is false for this explicit theory stress.

A more serious next challenge is ordinary multimode signal formation:

```text
finite boundary
or
electron-hole coexistence.
```

Those effects do not merely perturb the one-mode closure; they can raise the spatial rank and must be diagnosed by the six-color hierarchy.

Numerical implementation:

`numerics/hgcdte_ramo_four_color_diffusion_recombination.py`
