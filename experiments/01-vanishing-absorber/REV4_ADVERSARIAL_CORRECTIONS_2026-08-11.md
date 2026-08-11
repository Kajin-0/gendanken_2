# Revision 4 adversarial-review corrections

**Date:** 2026-08-11  
**Status:** CHECKED / SURGICAL MANUSCRIPT REVISION  
**Scope:** mathematical qualification, calibration resource, reproducibility, and exposition only; no wholesale restructuring.

## 1. Spatial-logarithm aliasing

The four-color measurement identifies the spatial multiplier

```math
q=e^{-\gamma h}
```

but does not globally identify a unique continuous exponent. The complete branch family is

```math
\gamma_n=-\frac{\operatorname{Log}q+2\pi i n}{h},\qquad n\in\mathbb Z.
```

Therefore the four-color model-order closure is branch-independent, while physical recovery of `D,w,kappa` is conditional on a unique spatial-log branch. A sufficient principal-branch anti-alias condition is

```math
|\operatorname{Im}\gamma|h<\pi.
```

The explicit 100-MHz stress with `D=0.02327 m^2/s`, `w=3.5e4 m/s`, and `h=0.5 um` reproduces the adversarial counterexample: adding `2 pi i/h` to the physical root leaves `q` unchanged and yields another positive inverse near

```text
D' = 6.75e-11 m^2/s
w' = 49.9 m/s.
```

This corrects the global-identifiability wording without weakening the multiplier-level four-color theorem.

## 2. Known unequal source spacing

For known positions, the first three positions constrain the exponent to a candidate-root set rather than guaranteeing a unique root. For `Delta0=h`, `Delta1=2h`,

```math
R=q(q+1).
```

The explicit choice `R=-0.16` has two attenuating candidates `q=-0.2` and `q=-0.8`. The fourth point filters candidates; physical inversion is unique only when the fourth point plus branch/physical constraints leaves one admissible root. Noncommensurate spacing can provide additional spatial-unwrapping leverage.

## 3. Singular DC weighting-field theorem

For the one-dimensional weighting-field equation

```math
DJ''+wJ'-(\kappa+s)J=-[wE_w+DE_w'],
```

a polynomial forcing of degree `p` has a particular solution of the same degree when `kappa+s != 0`.

At the singular point `s=kappa=0` with downstream `w>0`, the degree generically increases by one. For a linear field

```math
E_w(z)=E_0+E_1 z,
```

an exact particular solution is

```math
J_p(z)=-E_0z-\frac{E_1}{2}z^2.
```

Thus a linear weighting field requires:

```text
kappa+s != 0 -> linear particular -> second differences -> five colors
s=kappa=0    -> quadratic particular -> third differences -> six colors.
```

The unit-root observation contribution is repeated in the singular limit rather than a single ordinary `q=1` mode.

## 4. Independent-error calibration stresses

The manuscript's coordinate-error formula was evaluated directly for the worked HgCdTe scale. If the four residual source-position errors are independent and equal-RMS, requiring coordinate-induced phase closure noise to remain below one third of the modeled gradient-sensitive phase gives

```text
100 MHz -> 3.828 nm RMS
500 MHz -> 3.780 nm RMS
1 GHz   -> 3.626 nm RMS.
```

These are tolerances on the nonaffine residual of the effective source coordinate, not absolute depth accuracy.

Treating relative channel calibration error as complex also covers spectral phase mismatch. In the low-RF affine-current approximation for the quartet, the independent channel-phase coefficient norm is approximately `39.023`. The same one-third-target stress gives

```text
100 MHz -> 1.023e-4 deg RMS -> 2.843 fs equivalent differential delay
500 MHz -> 5.017e-4 deg RMS -> 2.787 fs
1 GHz   -> 9.431e-4 deg RMS -> 2.620 fs.
```

These are independent/high-curvature residual stresses, not requirements on common spectral delay or an absolute clock.

## 5. HgCdTe transport prescription made explicit

The manuscript now writes the exact equations used by the existing numerical model:

```math
x(z)=x_f+(x_b-x_f)z/L,
```

```math
E_g(x,T)=-0.302+1.93x-0.81x^2+0.832x^3+5.35\times10^{-4}(1-2x)T,
```

```math
D=\mu k_BT/e,
```

```math
E_g^{\rm grad}=\left|\frac{dE_g}{dx}\frac{dx}{dz}\right|,
```

```math
v_{\rm field}=\frac{\mu E_g^{\rm grad}}{1+(E_g^{\rm grad}/E_{\rm sat})^{r_s}},
```

```math
v_{\rm DOS}=\frac{3D}{2}\frac{d}{dz}\ln E_g,
\qquad
v=v_{\rm field}+v_{\rm DOS},
```

followed by the stochastic backward equation

```math
DJ''+v(z)J'-(\kappa+s)J=-v(z).
```

The entrance Robin match to the bounded homogeneous continuation is also written explicitly. No numerical closure values were changed.

## 6. Statistical and exposition changes

- The existing per-frequency `3 sigma` SNR table is retained as an engineering resource for the specified signed phase target.
- A generic covariance-aware complex closure statistic is added for experimental falsification.
- Hot-state language is tightened from `exactly rank two` to `rank at most two`; the exact rank-two closure remains valid under degeneracy.
- The interpretation ladder is made explicit: rank one -> rank two -> higher ordinary finite rank -> only then richer/nonlocal transport.
- One conceptual figure now shows the color -> current -> difference -> model-order -> root-law hierarchy.

## Regression

`numerics/rev4_critique_regression.py` verifies the alias counterexample, unequal-spacing multiple roots, singular weighting particular solution and six-color annihilation, and both calibration-stress calculations.

## Scientific disposition

The central four-color theorem is unchanged. The revision narrows two overclaims and makes the experimental nuisance and HgCdTe assumptions more explicit. The scientific interpretation is therefore

```text
four-color multiplier closure survives
+
physical inversion requires spatial branch control
+
one observation theorem has a singular DC/no-recombination limit
+
experimental discrimination requires covariance-aware control of non-common calibration modes.
```
