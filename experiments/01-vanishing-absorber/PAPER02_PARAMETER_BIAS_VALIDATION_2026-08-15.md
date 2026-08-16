# Parameter-bias law validation at the zero-diffusion point

**Date:** 2026-08-15  
**Status:** **CHECKED / FIRST-ORDER DESIGN LAW VALIDATED IN CONDITIONAL MODEL / PRIORITY UNPROVEN**

## 1. Purpose

`PAPER02_PARAMETER_BIAS_BOUND_2026-08-15.md` derived the first-order calibrated-kernel root bias

```math
\delta r
=
\frac{\mathbf h_\perp^\dagger W\mathbf E}
{\mathbf h_\perp^\dagger W\mathbf h_\perp}
+O(\|\mathbf E\|^2),
```

where

- `E` is the channel-space model discrepancy;
- `h_perp` is the root-sensitivity vector after offset/amplitude directions are projected away.

The same note propagated the root shift into a diffusion bias and predicted, near pure drift,

```math
D_{\rm app}
\simeq
\frac{w^3}{\omega^2}\Re\gamma.
```

This file records an independent numerical validation of those first-order formulas.

---

## 2. Validation design

The optical kernels are held **fixed**.

The baseline device is exact uniform deterministic drift with

```text
microscopic diffusion       0
recombination               0
velocity                    2.65565e4 m/s
RF                          100 MHz
```

The baseline six-channel calibrated one-mode model is exact to numerical precision.

Only the true downstream velocity profile is perturbed. The nonuniform region begins at

```text
z = 4.6 um
```

and the endpoint velocity ratio is

```math
R=1+\epsilon.
```

Two independent families are tested:

- linear velocity variation;
- exponential velocity variation.

Small positive and negative perturbations are used:

```text
epsilon = +/-0.001, +/-0.002, +/-0.005,
          +/-0.01, +/-0.02, +/-0.05.
```

For each case the calculation independently computes:

1. the exact six-channel nuisance vector

```math
\mathbf E=\mathbf J(\epsilon)-\mathbf J(0);
```

2. the **predicted** root shift from the baseline Jacobian projection;
3. the **actual** root shift from a new nonlinear kernel-aware fit;
4. the **predicted** `delta D` from the local `D(gamma)` Jacobian;
5. the **actual** apparent `D` from the independently refitted root.

No fitted quantity from the perturbed case is used to construct the first-order root prediction.

---

## 3. Reproducibility

Script:

```text
experiments/01-vanishing-absorber/numerics/paper02_bias_bound_linearization.py
```

GitHub Actions run:

```text
run id       31918166467
artifact     paper02-bias-bound-linearization
artifact id  9255536182
sha256       5f2ee00a24d4fd088e0d8b61f0f509b84ac9477dc814a2c2814382575864ab2c
```

---

## 4. Baseline validation

The uniform zero-diffusion baseline gives

```math
\gamma
\simeq
-1.56\times10^{-9}
-i\,2.36597\times10^4\ \mathrm{m^{-1}},
```

```math
D_{\rm fit}
=-7.41\times10^{-14}\ \mathrm{m^2/s}\approx0,
```

```math
w_{\rm fit}
=2.65565\times10^4\ \mathrm{m/s}.
```

The calibrated one-mode fit residual is

```text
4.87e-16.
```

The numerical baseline is therefore effectively exact.

The root-sensitivity norm after offset/amplitude projection for the chosen unweighted metric is

```text
9.9586e-8
```

in the corresponding channel/root units.

At this operating point,

```math
\frac{\partial D}{\partial\Re\gamma}
=4.74409\times10^{-5}\ \mathrm{m^3/s},
```

while the sensitivity to the imaginary root component is negligible at the exact zero-diffusion point.

This is the expected near-pure-drift conditioning.

---

## 5. Root-bias prediction

For the smallest tested gradients,

```text
|epsilon| <= 0.002,
```

the maximum relative error between the projected first-order root shift and the independently refitted complex root shift is

```math
\boxed{2.65\times10^{-6}.}
```

For

```text
|epsilon| <= 0.01,
```

the maximum root-shift relative error is still only

```math
\boxed{1.33\times10^{-5}.}
```

Even at the largest tested perturbation

```text
|epsilon|=0.05,
```

the root-shift prediction remains accurate at roughly the `1e-4` relative level or better.

Thus the tangent-projection root formula is not merely qualitative; it quantitatively predicts the nonlinear fit displacement over a useful neighborhood.

---

## 6. Diffusion-bias prediction

For

```text
|epsilon| <= 0.002,
```

the maximum relative error of the first-order propagated diffusion bias is

```math
\boxed{3.53\times10^{-4}}
```

or about `0.035%`.

For

```text
|epsilon| <= 0.01,
```

the maximum error remains

```math
\boxed{1.77\times10^{-3}}
```

or about `0.18%`.

At `|epsilon|=0.05`, where first-order behavior is no longer expected to be asymptotically exact, the diffusion prediction is still within about `0.9%`.

The sign prediction is exact for every tested case:

```text
all positive epsilon -> D_eff > 0
all negative epsilon -> D_eff < 0.
```

This holds for both linear and exponential velocity families.

---

## 7. The nuisance is overwhelmingly tangent

The calculation also projects the channel perturbation onto the full local calibrated one-mode tangent space.

For weak gradients, the norm of the first-order post-fit residual relative to the total nuisance-vector norm is only approximately

```math
\boxed{3.44\times10^{-3}.}
```

That means only about `0.34%` of the nuisance **amplitude norm** is available to the same-frequency goodness-of-fit test at first order.

Equivalently, because the projection is orthogonal in the validation metric, the residual **energy fraction** is only of order

```math
(3.44\times10^{-3})^2
\simeq1.18\times10^{-5}.
```

More than `99.998%` of the first-order nuisance energy lies inside the local model tangent space.

This quantitatively explains the core Paper-02 identifiability problem:

> the device physics can move the fitted transport parameters far more efficiently than it produces a same-frequency model-rejection signal.

---

## 8. Representative apparent diffusion scale

At `epsilon=+0.01`, corresponding to only a 1% change in downstream endpoint velocity, the deterministic zero-diffusion model already gives approximately

```text
D_eff = +4.3e-5 m^2/s
```

with kernel-aware one-mode residual of order

```text
2.7e-7.
```

Changing the sign of the velocity gradient changes the sign of `D_eff` while leaving the first-order conditioning essentially symmetric.

Thus the effect does not require a large or visually obvious transport distortion.

---

## 9. Scientific implication

The Paper-02 mechanism now has a compact quantitative hierarchy:

### Exact physical leakage

```math
E_m=\int_R g_m(z)\delta H(z)dz.
```

### First-order root bias

```math
\delta r
=
\frac{h_\perp^\dagger W E}
{h_\perp^\dagger W h_\perp}.
```

### Remote-region bound

```math
|\delta r|
\le
H_R
\frac{(\sum_m w_mp_m^2)^{1/2}}
{\|h_\perp\|_W}.
```

### Diffusion propagation

```math
|\delta D|
\lesssim L_D|\delta r|.
```

### Near-drift asymptote

```math
D_{\rm app}
\simeq
\frac{w^3}{\omega^2}\Re\gamma.
```

The validation shows that the first-order middle steps accurately predict the full nonlinear inverse for small physical heterogeneity.

This is substantially stronger than a numerical counterexample because it provides a reusable attribution-sensitivity calculation for an arbitrary calibrated kernel set and measurement covariance.

---

## 10. Current publication consequence

The first-order parameter-bias gate is now substantially passed.

A standalone Paper 02, if the priority audit survives, can be structured around a general inference statement rather than around a particular HgCdTe geometry:

1. finite-kernel remote-region leakage theorem;
2. tangent-space root-bias law;
3. near-drift diffusion susceptibility;
4. deterministic velocity-gradient mechanism;
5. causal and sign-reversal numerical validation;
6. finite-band RF discrimination requirement.

The remaining major technical gate is the last item: turn the cubic-and-higher RF mismatch into an explicit significance / bandwidth / precision criterion.

Publication priority remains OPEN.
