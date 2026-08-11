# Four-Color Shockley-Ramo Closure — Internal-Coordinate Calibration

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** for one homogeneous raw-current spatial mode; no novelty claim

## 1. Main result

The four-color null does **not** require knowing the absolute internal depth origin or scale.

Let the spectral coordinate used to choose four channels be `mu`, with equal spacing

```math
\mu_m=\mu_0+mh.
```

Suppose the true physical source coordinate is related by

```math
z=f(\mu).
```

For one homogeneous raw Shockley-Ramo mode,

```math
J(\mu)=A+B e^{-\gamma f(\mu)}.
```

If

```math
\boxed{f(\mu)=a+b\mu,}
```

then the true source positions remain exactly equally spaced, with spacing `bh`.

Therefore

```math
\boxed{
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2)
}
```

holds **exactly for any offset `a` and nonzero scale `b`**.

Thus absolute depth offset and a common depth-scale error cannot create a false model-order failure.

The scale `b` does rescale the recovered physical propagation exponent, so calibrated depth scale is required for absolute `D,w,kappa` extraction even though it is unnecessary for the basic closure null.

---

## 2. Smooth nonlinear distortion

Let the quartet be centered at `mu_c` and let `h` be small.

The first differences obey

```math
\Delta J_m\simeq h J'(\mu_{m+1/2}).
```

Hence the logarithmic closure

```math
\mathcal C_4
=2\ln\Delta J_1-
\ln\Delta J_0-
\ln\Delta J_2
```

is the centered second difference of

```math
\ln J'(\mu)
=\mathrm{const}
+\ln f'(\mu)
-\gamma f(\mu).
```

Therefore

```math
\boxed{
\mathcal C_{4,coord}
=h^2
\left[
\gamma f''
-(\ln f')''
\right]_{\mu_c}
+O(h^4).
}
```

This is the leading coordinate-calibration distortion.

For a nearly identity map

```math
f(\mu)=\mu+\delta(\mu),
```

with small `delta`, this reduces to

```math
\boxed{
\mathcal C_{4,coord}
\simeq
h^2
\left[
\gamma\delta''-\delta'''
\right]
}
```

at first order in the calibration distortion.

---

## 3. Interpretation

The important calibration quantity is therefore not

```text
absolute depth error
```

but

```text
nonlinear curvature of the spectral-coordinate map across the quartet.
```

A common offset, common scale, or locally affine model discrepancy leaves the basic four-color null unchanged.

This is especially useful for graded absorbers, where an optical model may have uncertain absolute profile coordinates but a much better constrained local monotonic mapping.

---

## 4. Relation to other systematic-rejection results

The four-color observable now rejects several low-order nuisance classes:

```text
common complex RF gain/offset -> exact cancellation
rigid finite source width -> exact cancellation
absolute/affine depth calibration -> exact cancellation
constant/linear fractional amplitude calibration -> first-order cancellation
smooth source-variance evolution -> only third discrete difference at leading order.
```

The common theme is spatial finite-difference annihilation of low-order smooth structure.

This should be emphasized as a design principle, not as a claim that systematic calibration is unnecessary.

---

## 5. Numerical regression

`numerics/ramo_four_color_coordinate_calibration.py`

checks

```text
exact affine invariance for several offset/scale choices
and
C4/h^2 -> gamma f''-(ln f')''
```

for a nonlinear cubic coordinate map.

---

## 6. Paper consequence

A future experiment does not need nanometer-level knowledge of all four absolute generation depths simply to ask whether the one-mode closure holds.

It needs the **four source coordinates to be equally spaced in the true propagation coordinate to the required curvature tolerance**.

Absolute physical depth becomes necessary when converting the recovered dimensionless spatial multiplier into physical transport coefficients.
