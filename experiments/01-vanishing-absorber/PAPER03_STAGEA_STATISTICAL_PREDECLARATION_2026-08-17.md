# Paper 03 Stage-A Statistical Gate — Predeclaration

**Date:** 2026-08-17  
**Status:** **PREDECLARED BEFORE PARAMETRIC-BOOTSTRAP EXECUTION / NON-CLAIM**

## 1. Question

The deterministic Stage-A result now shows that the finite75 + depletion response fails the calibrated arbitrary-kernel one-mode model and is well described by a kernel-aware two-mode diagnostic whose physical homogeneous root law fails.

The next decisive question is statistical:

> At what raw-current measurement SNR does the six-channel calibrated-kernel one-mode model become rejectable, after nonlinear refitting, and is that SNR below the frozen transport-claim SNR at the same RF?

This record fixes the statistical convention and bootstrap procedure before the bootstrap result is examined.

---

## 2. Forward coordinate locked for this gate

Use the already numerically validated Stage-A finite response

```text
scenario = finite75_depletion
D = 2.5e-3 m^2/s
tau = infinity
spatial grid = 201 x 151
lateral source quadrature = 17 points
six calibrated HgCdTe optical kernels
```

Do not tune the detector coordinate during the statistical calculation.

The finite-recombination coordinate is a separate sensitivity result and is not substituted into this gate after seeing its answer.

---

## 3. Null model

At each nonzero RF independently, fit the six complex channels to

```math
J_m=A+B M_m(r),
```

```math
M_m(r)=\int g_m(z)e^{rz}\,dz.
```

Complex `A`, `B`, and `r` give six real fitted parameters. With six complex data channels, the regular local residual dimension is therefore

```text
nu = 12 - 6 = 6 real degrees of freedom.
```

The null bootstrap generating mean is the best-fit six-channel one-mode prediction at that RF, not the planar detector response.

The deterministic alternative generating mean is the actual converged finite75 + depletion six-channel forward current at that RF.

---

## 4. Noise and SNR convention

Let

```math
s_J = mean_m |J_{m+1}-J_m|
```

across the five adjacent differences of the six-channel deterministic alternative.

For every channel add independent noise

```math
n_m = sigma (xi_{m,R}+i xi_{m,I}),
```

with all `xi` independent standard normal variables.

Thus `sigma` is the standard deviation of **each real and imaginary current quadrature**.

Define the raw-current step-amplitude SNR coordinate by

```math
SNR = s_J/sigma,
```

or

```math
SNR_dB = 20 log10(s_J/sigma).
```

This convention is explicit so that any future complex-RMS convention can be converted rather than silently introducing a `sqrt(2)` / approximately `3.01 dB` ambiguity.

The existing frozen comparison coordinates are retained as

```text
100 MHz -> 96.1 dB
500 MHz -> 82.3 dB
1 GHz   -> 76.7 dB
```

from the repository's current-step transport-claim SNR record. The final report must state the quadrature convention above when comparing margins.

---

## 5. Analytic first-pass reference

Before bootstrap, compute the local regular nonlinear-least-squares approximation

```math
T=||J-J_fit||^2/sigma^2.
```

Under the regular one-mode null,

```math
T \sim chi^2_nu,
```

and under a fixed local alternative approximately

```math
T \sim chi'^2_nu(lambda),
```

with

```math
lambda=||J_true-J_null^*||^2/sigma^2.
```

This analytic result is a reference only. It is not accepted as the final statistical calibration because the kernel root is nonlinear and can become weakly conditioned.

---

## 6. False-alarm probability and power

Fix

```text
alpha = 0.002699796063260207
```

corresponding to the usual two-sided normal `3 sigma` tail probability.

Fix target detection power

```text
power = 0.90.
```

These values are not changed after the bootstrap output is inspected.

---

## 7. Bootstrap SNR grid

For each of

```text
100 MHz
500 MHz
1 GHz
```

first calculate the local analytic SNR threshold.

Then evaluate bootstrap candidates at

```text
analytic threshold + {-4, -2, 0, +2, +4} dB.
```

Do not recenter that grid after examining intermediate powers.

If 90% power is not bracketed by this fixed grid, report it as unbracketed rather than silently extending the grid and describing the result as predeclared. A later explicitly post-gate extension may be run if scientifically necessary.

---

## 8. Parametric-bootstrap sample counts

At every RF/SNR candidate use

```text
N_null = 4000
N_alt  = 2000
```

independent realizations.

Fixed random seeds must be stored in the result. Separate deterministic seed streams are required for null and alternative samples.

The empirical null critical value is the `1-alpha` quantile of the minimized refit statistic using a conservative discrete quantile (`method='higher'`).

Empirical alternative power is the fraction of alternative realizations whose minimized refit statistic exceeds that empirical null critical value.

Because `alpha` is small, the finite-null-sample critical value is itself noisy. Report the number of null exceedance-tail samples implied by the quantile and do not quote more precision than the bootstrap supports.

---

## 9. Nonlinear refit requirement

Each noisy realization must be refit to the calibrated-kernel one-mode model. Do not evaluate noise against a frozen noiseless fitted curve without parameter reoptimization.

For computational tractability a local nonlinear refit may start from the deterministic best-fit root because all tested SNRs are high. However:

1. use deterministic bounded least squares with complex `A,B` profiled at every root evaluation;
2. include at least small deterministic root perturbation starts around the baseline root;
3. spot-check a fixed subset against the full multistart fitter;
4. report any case in which the fast refit has materially larger residual than the full fitter.

A fast-refit discrepancy is a bootstrap implementation failure, not evidence for the scientific alternative.

---

## 10. Primary bootstrap outputs

For each RF/SNR candidate report

```text
sigma / step;
raw-current SNR dB;
analytic chi-square critical value;
empirical null critical value;
empirical null statistic median/quantiles;
empirical alternative power;
Monte-Carlo standard error of the estimated power;
fast-versus-full-refit spot-check discrepancy.
```

For each RF report the lowest tested SNR with empirical power >=0.90.

If adjacent tested points straddle 90% power, a monotone interpolation may be reported as a descriptive estimate but the bracketing tested values remain primary.

---

## 11. Decision rule

The candidate **early-warning condition** at an RF is supported by this gate if

```text
at least one tested SNR at or below the frozen transport-claim SNR
has empirical power >= 0.90
```

under the explicit noise convention above.

The warning margin is bounded conservatively using the lowest tested SNR point that achieves 90% power; interpolation may not be used to manufacture a pass.

A result that needs higher SNR than the frozen transport claim is not an early warning at that RF.

---

## 12. Scope boundary

Even if all three RFs pass this statistical gate, Paper 03 is not yet standalone-GO. Remaining requirements include

```text
broader geometry/diffusion/lifetime parameter domain;
a materially different second geometry family;
stochastic-versus-resolvent coarse-observable cross-check;
Stage-B self-consistent semiconductor forward-model validation;
and focused prior-art audit.
```

No statistical result may be used to weaken those scientific requirements.