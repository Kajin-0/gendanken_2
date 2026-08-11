# Six-Color Shockley-Ramo Closure — Noise Significance of the Second Mode

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** high-SNR covariance result for independent equal complex current-sample noise; not a universal estimator bound

## 1. Why a pre-fit significance test is needed

The exact two-mode separation theorem gives

```math
W_0=d_0d_2-d_1^2
=ab(q_1-q_2)^2.
```

This is the first observable that distinguishes a genuine two-mode first-difference sequence from rank one.

Root fitting should not begin merely because exact arithmetic gives `W_0 != 0`.

The correct first question is:

> **Is the measured Hankel minor significantly nonzero relative to its propagated current noise?**

---

## 2. Linearized current-noise propagation

Let four consecutive raw current samples be

```math
J_0,J_1,J_2,J_3
```

with

```math
d_0=J_1-J_0,
```

```math
d_1=J_2-J_1,
```

```math
d_2=J_3-J_2.
```

Define

```math
\boxed{
W_0=d_0d_2-d_1^2.
}
```

Let the measured currents contain small complex errors

```math
J_m^{meas}=J_m+\epsilon_m.
```

To first order,

```math
\boxed{
\delta W_0
=-d_2\epsilon_0
+(d_2+2d_1)\epsilon_1
-(d_0+2d_1)\epsilon_2
+d_0\epsilon_3.
}
\tag{1}
```

For independent circular complex errors with

```math
E|\epsilon_m|^2=\sigma_J^2,
```

Eq. (1) gives

```math
\boxed{
\sigma_{W_0}^2
=\sigma_J^2
\left[
|d_2|^2
+|d_2+2d_1|^2
+|d_0+2d_1|^2
+|d_0|^2
\right].
}
\tag{2}
```

---

## 3. Exact two-mode signal

For

```math
d_m=a q_1^m+b q_2^m,
```

the signal being tested is not an arbitrary fit residual.

It is exactly

```math
\boxed{
W_0=ab(q_1-q_2)^2.
}
\tag{3}
```

Therefore a natural mode-detection statistic is

```math
\boxed{
Z_2
=\frac{|W_0|}{\sigma_{W_0}}.
}
\tag{4}
```

Under a full experiment one should use the complete complex covariance and an appropriate likelihood/null distribution rather than treating `Z_2` as an exact Gaussian p-value.

Its role here is a transparent high-SNR design scale.

---

## 4. Near-equal-step limit

If

```math
d_0\simeq d_1\simeq d_2=d,
```

Eq. (1) becomes

```math
\delta W_0
\simeq
d(-\epsilon_0+3\epsilon_1-3\epsilon_2+\epsilon_3).
```

Hence

```math
\boxed{
\sigma_{W_0}
\simeq
\sqrt{20}\,|d|\sigma_J.
}
\tag{5}
```

The same third-difference stencil seen in the one-mode four-color closure reappears.

That is expected: `W_0=0` is precisely the unlogged one-mode closure condition.

---

## 5. Quadratic collapse of second-mode significance

For fixed nonzero observable amplitudes and fixed current-noise scale,

```math
|W_0|
\propto
|q_1-q_2|^2.
```

The noise coefficient in Eq. (2) remains finite as the two roots merge, provided the combined one-mode current step remains finite.

Therefore

```math
\boxed{
Z_2
\propto
|q_1-q_2|^2
}
\tag{6}
```

near root coalescence.

Halving the spatial-root separation therefore costs approximately a factor of four in the pre-fit second-mode detection significance.

This is a clean experimental resolution law for model order.

---

## 6. Why root fitting comes after the minor test

The recurrence estimator has determinant

```math
W_0.
```

Thus its numerical conditioning deteriorates exactly where the pre-fit second-mode witness becomes statistically weak.

The correct order is therefore

```text
measure four/six channels
-> test whether W_m are significantly nonzero
-> test rank-two closure W1^2=W0 W2 / 3x3 Hankel
-> only then recover q1,q2
-> only then apply boundary/electron-hole RF root laws.
```

Trying to fit two roots when `|W_0| <= sigma_W` manufactures unstable parameter estimates from data that do not actually resolve two modes.

---

## 7. Relation to mode amplitude

Equation (3) contains

```math
ab.
```

Therefore a physically present second carrier/boundary mode can become experimentally invisible if its current amplitude is too weak.

That is not a failure of the hierarchy.

It means the measured observable is effectively rank one over that spectral/RF band.

The model order should describe **observable dynamics**, not every microscopic degree of freedom in the device.

---

## 8. Numerical regression

`numerics/ramo_two_mode_witness_noise.py`

verifies

```text
linearized covariance against Monte Carlo
sqrt(20)|d| equal-step noise scale
quadratic loss of witness/noise ratio as root separation is halved.
```

---

## 9. Paper-level consequence

The six-color claim can now be stated precisely:

> **Six colors can discriminate a two-mode first-difference model only when the exact Hankel-minor witness `ab(q1-q2)^2` is statistically resolved.  The second-mode significance collapses quadratically as the spatial roots merge or linearly as either observable mode amplitude vanishes.**

This turns a formal system-identification result into a quantitative falsifiability condition suitable for the reduced photodetector theory paper.
