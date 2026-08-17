# Paper 03 — Coplanar second-geometry hierarchy lock

**Date:** 2026-08-17  
**Status:** **POST-NUMERICAL / PRE-TWO-MODE AND PRE-BOOTSTRAP LOCK / NON-CLAIM**

The coplanar family passed `PAPER03_SECOND_GEOMETRY_NUMERICAL_LOCK_2026-08-17.md` before this file was created. The accepted numerical artifact already exposed that its calibrated-kernel one-mode residual is much larger than the first-family floor. This record therefore does **not** pretend that one-mode failure was still blind at lock time. It freezes only the downstream model-order, physical-root, and statistical decisions before those outputs are read.

## Frozen input

Use the already-declared centered coplanar detector only:

```text
16.0 um x 7.6 um absorber
left top electrode [-8,-2] um at 0 V
right selected electrode [+2,+8] um at +0.30 V
central top gap, bottom, sidewalls insulating
Laplace physical field
independent right-electrode weighting field
D = 2.5e-3 m^2/s
tau = infinity
beam x0 = 0, sigma = 1.0 um
same six calibrated HgCdTe optical kernels
```

No geometry or material coordinate is tuned after the numerical result.

## Model-order diagnostic

At 100 MHz, 500 MHz, and 1 GHz fit

```math
J_m=A+B_1M_m(r_1)+B_2M_m(r_2)
```

on 121x91 and 161x121 independently, using the already regression-tested global/multistart two-mode fitter.

A 161-grid second-mode description is called **compact and non-negligible** only if all are true:

```text
two-mode rho <= 0.20 * one-mode rho
profile design condition number <= 1e6
smaller/larger profiled modal amplitude >= 1e-3
```

Residual reduction alone is never treated as physical identification.

For a matched two-root set, numerical root stability at an RF requires

```text
max matched root change <= max(0.05 1/um, 0.10 * largest 161-grid root magnitude).
```

If this fails, the conservative classification is `one mode rejected / second mode not identifiable`; the physical root-law test is not forced.

## Homogeneous scalar root law

Where the two-root description is compact and numerically stable, the same homogeneous finite-boundary scalar law used in the first family requires

```math
r_1+r_2=-w/D,
```

so the root sum must be real and RF-independent.

For each RF define the numerical root-sum uncertainty proxy as the permutation-invariant sum of matched 121->161 root changes, `u_s`.

A gross imaginary-part violation is declared only if

```text
|Im(r1+r2)| > 0.005 1/um + 5*u_s.
```

For two usable RFs i,j, RF-independence is rejected only if

```text
|s_i-s_j| > 0.010 1/um + 5*(u_s_i+u_s_j).
```

These factors are deliberately conservative numerical-separation criteria, not fitted statistical confidence intervals.

## Statistical gate

The coplanar one-mode rejection uses the **unchanged** selected-point bootstrap contract:

```text
alpha = 0.002699796063260207
power target = 0.90
N_null = 4000
N_alt = 2000
SNR candidates = analytic + {-4,-2,0,+2,+4} dB
per-quadrature iid Gaussian complex-current noise
nonlinear calibrated-kernel one-mode refit for every realization
no interpolation between fixed SNR candidates
```

The same frozen transport-claim SNR comparison coordinates remain 96.1, 82.3, and 76.7 dB at 100 MHz, 500 MHz, and 1 GHz. They are a cross-architecture comparison scale, not a claim that the coplanar detector is the Paper-01 device.

## Decision

A second-family candidate Outcome-A result requires:

```text
formal numerical gate PASS;
one-mode inadequacy statistically rejectable before frozen claim SNR at all tested RFs;
and either
  (a) a stable compact higher-order fit that violates the homogeneous root law, or
  (b) conservative model-order non-identifiability / higher-order rejection.
```

A hidden low-dimensional homogeneous interpretation at claim-level precision would instead trigger Outcome B.

```text
science_interpretation_ready = false
Paper 03 standalone GO = false
```
