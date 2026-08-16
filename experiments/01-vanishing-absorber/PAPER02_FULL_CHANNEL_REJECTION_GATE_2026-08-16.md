# Paper 02 — full-channel versus root-space multi-frequency rejection gate

**Date:** 2026-08-16  
**Status:** PREDECLARED REV. 8 METHODOLOGICAL CHECK

## Review issue

Rev. 7 quotes multi-frequency rejection thresholds after compressing each six-complex-channel spectral measurement to one fitted complex root `gamma(omega)`. That root-space test is valid but discards the same-frequency normal residual directions already used elsewhere in the paper.

This gate compares that protocol with a direct full-channel generalized-least-squares goodness-of-fit test under the **same declared theoretical noise model**.

## Forward data

Use the exact full-contact planar continuum heterogeneous downstream-carrier stress, not the 2-D mesh baseline. Microscopic diffusion and recombination remain zero.

Frequencies:

```text
100, 200, 300, 500, 750 MHz, 1, 1.5, 2, 3 GHz.
```

At each frequency there are six complex finite-kernel channels.

## Noise normalization

At each frequency, real and imaginary quadratures are independent with equal standard deviation. Define

```text
S = RMS_m |J_m| / sigma_quadrature
S_dB = 20 log10 S.
```

Use the same S at every included RF frequency and no cross-frequency correlation. This is the Rev. 7 reference noise family, not an instrument requirement.

## Root-space protocol

Recompute the Rev. 7 root-space test from the exact continuum channels:

1. fit one complex root at each frequency after profiling complex C,K;
2. propagate six-channel covariance to each fitted root at S=1;
3. jointly fit homogeneous D,w across cumulative frequency bands;
4. calculate the profiled noncentral distance and S required for alpha=0.0027, power=0.90.

Degrees of freedom for n complex roots after fitting D,w: `2n-2`.

## Full-channel protocol

For a trial common homogeneous `D,w`, calculate

```text
gamma_f(D,w)
r_f = -gamma_f
J_mf(model) = C_f + K_f F_m(r_f).
```

At every frequency profile its own complex `C_f,K_f` exactly. Fit only common `D,w` nonlinearly over all included frequencies.

At S=1, whiten each frequency by its own `RMS_m |J_m|`. The minimized squared full-channel residual is the alternative noncentrality. With six complex channels per frequency and four real profiled C,K nuisance coordinates per frequency, the asymptotic residual degrees of freedom are

```text
nu_full = 12 n - 4 n - 2 = 8 n - 2.
```

Use the same alpha and power as the root-space protocol.

## Interpretation

The full-channel calculation is expected to retain at least the same *data directions* as root compression, but its goodness-of-fit statistic also has more residual degrees of freedom. Therefore do not predeclare that its numerical SNR threshold must be lower.

Report both protocols side by side. The manuscript must call the old result `root-space multi-frequency rejection` regardless of outcome.

No claim of globally optimal experimental discrimination is permitted: the result is conditional on the declared homogeneous model, nuisance profiling, and covariance.
