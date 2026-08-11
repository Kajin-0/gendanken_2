# Six-Color Shockley-Ramo Closure — Dimensionless Two-Mode Resolution Scaling

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** near-coalescence design law using the Hankel-minor witness and independent equal complex current noise

## 1. Start from the exact two-mode signal

For first differences

```math
d_m=a q_1^m+b q_2^m,
```

the second-mode witness is

```math
\boxed{
W_0=ab(q_1-q_2)^2.
}
```

Near one-mode behavior let the current-step scale be

```math
|d|\simeq|a+b|
```

and define the per-channel complex current noise fraction

```math
\boxed{
\eta=\sigma_J/|d|.
}
```

The equal-step witness-noise scale is

```math
\sigma_{W_0}\simeq\sqrt{20}|d|\sigma_J.
```

Therefore the approximate second-mode significance is

```math
\boxed{
Z_2
\simeq
\frac{|ab|}{|a+b|^2}
\frac{|q_1-q_2|^2}
{\sqrt{20}\,\eta}.
}
\tag{1}
```

---

## 2. Equal visible modes

For equal in-phase mode amplitudes

```math
a=b,
```

```math
\frac{|ab|}{|a+b|^2}=\frac14.
```

Hence

```math
\boxed{
Z_2
\simeq
\frac{|q_1-q_2|^2}
{4\sqrt{20}\,\eta}.
}
\tag{2}
```

For target significance `Z`,

```math
\boxed{
|q_1-q_2|
\gtrsim
\left(4\sqrt{20}\,Z\eta\right)^{1/2}.
}
\tag{3}
```

At `Z=3`,

```math
\boxed{
|q_1-q_2|
\gtrsim
7.33\sqrt{\eta}.
}
\tag{4}
```

Examples:

```text
eta = 1e-3 -> Delta q ~0.232
eta = 1e-4 -> Delta q ~0.0733
eta = 1e-5 -> Delta q ~0.0232
eta = 1e-6 -> Delta q ~0.00733.
```

Thus the two-mode theorem has a finite, explicit resolution region rather than being useful only for widely separated roots.

---

## 3. Weak second mode

Let

```math
r=b/a.
```

Then the observable amplitude factor is

```math
\boxed{
F(r)
=\frac{|r|}{|1+r|^2}.
}
```

Equation (1) becomes

```math
Z_2
\simeq
F(r)
\frac{|\Delta q|^2}
{\sqrt{20}\eta}.
```

For positive in-phase amplitudes, `F(r)` is maximal at

```math
r=1
```

with maximum

```math
F=1/4.
```

As the second mode weakens,

```math
F(r)\to0,
```

and the required root separation increases.

For `eta=1e-4` and `Z=3`:

```text
r = 1.0  -> Delta q ~0.073
r = 0.3  -> ~0.085
r = 0.1  -> ~0.127
r = 0.03 -> ~0.216.
```

The exact values depend also on complex relative phase; Eq. (1) keeps that dependence explicit.

---

## 4. Spatial-exponent interpretation

For nearby spatial exponents

```math
q_j=e^{r_jh},
```

```math
q_1-q_2
\simeq
q\,h(r_1-r_2).
```

Therefore the mode-resolution condition can be translated to

```math
\boxed{
h|r_1-r_2|
\gtrsim
\frac{1}{|q|}
\left[
\frac{\sqrt{20}\,Z\eta}{F(r)}
\right]^{1/2}.
}
```

This exposes the design tradeoff directly:

```text
larger internal-source spacing h
-> greater separation of the spatial multipliers
-> easier model-order discrimination
```

until optical-kernel evolution, coefficient inhomogeneity, boundaries, or phase wrapping invalidate the local finite-mode approximation.

---

## 5. What this does not claim

Equation (1) is a high-SNR near-equal-step scaling, not a universal minimax bound.

A full experiment should use

```text
all six complex-current covariance,
all available Hankel minors,
correlated calibration uncertainty,
and a likelihood/model-selection statistic.
```

The result is useful because it exposes the **correct parametric scaling** before any elaborate estimator is chosen:

```math
\boxed{
Z_2\propto
|ab|\,|q_1-q_2|^2/\sigma_J.
}
```

---

## 6. Paper-level role

This closes the concern that six-color mode counting is formally exact but practically empty.

The defensible statement is:

> **The second spatial mode is resolvable over a finite parameter region.  Its pre-fit significance scales quadratically with spatial-multiplier separation and with the geometric visibility of both mode amplitudes.  For equal visible modes, the 3-sigma root-separation threshold is approximately `7.33 sqrt(sigma_J/|d|)`.**

Numerical implementation:

`numerics/ramo_two_mode_resolution_scaling.py`
