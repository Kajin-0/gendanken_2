# Independent deterministic velocity-profile generality test

**Date:** 2026-08-15  
**Status:** **CHECKED / GENERALITY GATE PASSED IN CONDITIONAL MODEL / PRIORITY UNPROVEN**

## 1. Purpose

The original Paper-02 false-diffusion example used a finite-difference electrostatic solver with a quadratic space-charge source inside a collector-side depletion region.

Even after point-source controls and mean-preserving optical-tail ablation isolated the mechanism, one concern remained:

> the result might depend on the specific Poisson surrogate, field mesh, or saturated-drift implementation.

This test removes all of those ingredients.

The device is reduced to the exact one-dimensional planar Shockley-Ramo source-response equation with an externally prescribed deterministic velocity profile.

No Poisson solve is performed.
No finite-electrode geometry is present.
No microscopic diffusion is present.
No recombination is present.

The same six calibrated HgCdTe generation kernels and the same kernel-aware one-mode inverse are retained.

---

## 2. Exact 1-D forward problem

For planar weighting potential and deterministic velocity `v(z)`, the source response obeys

```math
\boxed{
\frac{dH}{dz}
=-\frac1L+\frac{i\omega}{v(z)}H,
\qquad
H(L)=0.
}
```

The calculation solves this ODE directly to high numerical precision and then forms

```math
J_m(\omega)=\int g_m(z)H(z,\omega)dz.
```

Each frequency is subsequently fit with the exact calibrated-kernel one-mode model already used in the Paper-02 stress program.

The recovered root is forced onto the homogeneous no-recombination drift-diffusion law at 100 MHz to obtain `D_eff,w_eff`.

The 1 GHz point is then an overdetermined physical-law test.

---

## 3. Independent velocity families

Common parameters:

```text
absorber thickness          7.6 um
nonuniform-region start     4.6 um
upstream velocity           2.65565e4 m/s
microscopic diffusion       0
recombination               0
planar weighting field      exact
```

For `z<4.6 um`, all profiles have the same constant velocity.

For `z>=4.6 um`, two unrelated prescribed families are used.

### Linear family

```math
v(z)=v_0[1+(R-1)\xi],
```

### Exponential family

```math
v(z)=v_0R^\xi,
```

where

```math
\xi=\frac{z-z_d}{L-z_d}.
```

Endpoint ratios tested:

```text
R = 0.50, 0.75, 1.00, 1.25, 1.50, 2.00.
```

Thus both downstream acceleration and deceleration are tested.

---

## 4. Reproducibility

Script:

```text
experiments/01-vanishing-absorber/numerics/paper02_independent_velocity_profiles.py
```

GitHub Actions run:

```text
run id       31917901867
artifact     paper02-independent-velocity-profiles
artifact id  9255463448
sha256       ca806190ad18e63c22ad21576d7a5089c1685066c1a65f0d89b8b820fbb650b9
```

RF points:

```text
0, 25, 50, 100, 200, 500, 750, 1000 MHz.
```

---

## 5. Uniform control

For uniform deterministic velocity,

```math
\boxed{
D_{\rm eff}=2.67\times10^{-14}\ {\rm m^2/s}\approx0.
}
```

The calibrated one-mode residual is

```text
1.19e-14,
```

and the 1 GHz homogeneous-law residual is

```text
2.42e-13.
```

This validates the ODE forward model and inverse against the exact homogeneous zero-diffusion limit.

---

## 6. Acceleration produces positive apparent diffusion

### Linear acceleration

| endpoint ratio `R` | `D_eff` [m^2/s] | `w_eff` [m/s] | 1 GHz law residual | max one-mode residual |
|---:|---:|---:|---:|---:|
| 1.25 | 1.008e-3 | 2.6229e4 | 0.00327 | 6.63e-5 |
| 1.50 | 1.877e-3 | 2.5948e4 | 0.00630 | 1.24e-4 |
| 2.00 | 3.296e-3 | 2.5485e4 | 0.01152 | 2.20e-4 |

### Exponential acceleration

| endpoint ratio `R` | `D_eff` [m^2/s] | `w_eff` [m/s] | 1 GHz law residual | max one-mode residual |
|---:|---:|---:|---:|---:|
| 1.25 | 9.362e-4 | 2.6253e4 | 0.00304 | 6.16e-5 |
| 1.50 | 1.651e-3 | 2.6023e4 | 0.00552 | 1.09e-4 |
| 2.00 | 2.687e-3 | 2.5692e4 | 0.00934 | 1.78e-4 |

Every acceleration case returns a positive, apparently physical homogeneous diffusion coefficient even though the true microscopic diffusion coefficient is exactly zero.

---

## 7. Deceleration reverses the sign

### Linear deceleration

```text
R=0.75 -> D_eff = -1.175e-3 m^2/s
R=0.50 -> D_eff = -2.530e-3 m^2/s
```

### Exponential deceleration

```text
R=0.75 -> D_eff = -1.305e-3 m^2/s
R=0.50 -> D_eff = -3.297e-3 m^2/s
```

Thus every tested deceleration profile gives negative apparent diffusion and fails the usual physical admissibility condition `D>0`.

The sign is not random numerical bias.

It tracks the direction of the deterministic downstream velocity gradient across two independent functional families.

---

## 8. Generality gate

The predeclared gate was:

```text
uniform velocity       -> D_eff ~= 0
independent acceleration families -> D_eff > 0
independent deceleration families -> D_eff < 0
```

All three requirements are satisfied.

Therefore the positive false diffusion seen in the original depletion calculation is not specific to

- the 2-D field solver;
- the quadratic space-charge profile;
- finite-contact geometry;
- a particular field discretization.

It is a generic consequence, within the tested class, of combining

1. finite optical generation support extending into a downstream nonuniform-velocity region;
2. planar Shockley-Ramo path integration;
3. inversion onto a homogeneous drift-diffusion dispersion model.

---

## 9. Relationship to the analytical theorem

The local deterministic field-gradient theorem predicted

```math
D_{\rm eff}\sim\frac12(L-z)^2v'(z)
```

for weak gradients and point-source probing inside the gradient region.

The current finite-kernel inversion does not equal that local formula quantitatively because

- most kernel mass lies upstream;
- each channel samples a distribution of source positions;
- only the kernel tails overlap the nonuniform region;
- the inverse compresses the resulting six averaged channels into one effective root.

Nevertheless, the **sign prediction survives exactly** across both independent families:

```text
v' > 0 -> D_eff > 0
v' = 0 -> D_eff = 0
v' < 0 -> D_eff < 0.
```

This is strong evidence that the local theorem and the remote-kernel leakage theorem describe two limits of the same underlying mechanism.

---

## 10. Practical severity

The false homogeneous model remains difficult to reject at moderate RF even for substantial velocity gradients.

Examples:

```text
linear R=1.25       1 GHz residual = 0.327 %
linear R=1.50       1 GHz residual = 0.630 %
linear R=2.00       1 GHz residual = 1.152 %

exponential R=1.25  1 GHz residual = 0.304 %
exponential R=1.50  1 GHz residual = 0.552 %
exponential R=2.00  1 GHz residual = 0.934 %
```

The same-frequency calibrated one-mode residuals remain only `O(10^-4)`.

Thus a deterministic heterogeneous device can look simpler than it is in both the spectral-channel and low-RF frequency directions.

---

## 11. Scientific conclusion

The result now has three independent causal layers:

### Support control

Point sources wholly outside the nonuniform region give `D_eff ~= 0`.

### Optical causal control

Removing only remote-region kernel support collapses `D_eff` by orders of magnitude, even when all six mean depths are preserved exactly.

### Transport-family control

Independent deterministic acceleration profiles restore positive `D_eff`; deceleration reverses its sign.

The resulting candidate phenomenon can therefore be stated without reference to the original geometry solver:

> **Finite generation-depth distributions can alias deterministic spatial velocity heterogeneity into an apparently physical diffusion coefficient in wavelength-resolved Shockley-Ramo transport inversion.**

A further distinctive feature is that the alias can remain near both the calibrated one-mode spectral manifold and the homogeneous drift-diffusion RF manifold over a useful finite bandwidth.

**Publication priority remains unproven.**

---

## 12. Next publication gate

The physics mechanism is now sufficiently hardened that more arbitrary numerical examples have diminishing value.

The strongest next work is:

1. complete a focused primary-source audit of wavelength-dependent/partially-depleted photodiode impulse-response inverse methods;
2. derive a first-order closed-form parameter-bias expression in terms of restricted kernel overlap and the inverse Jacobian;
3. translate the RF-law residual into an experimental precision/bandwidth requirement;
4. decide whether the result is sufficiently distinct for a standalone Paper 02 or belongs as a major omitted-nuisance stress in Paper 01.
