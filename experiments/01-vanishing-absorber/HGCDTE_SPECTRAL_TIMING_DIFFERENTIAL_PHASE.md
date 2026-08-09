# HgCdTe Spectral Timing by Differential Phase — Frequency-Domain Access to Differential Transport

**Date:** 2026-08-09  
**Status:** exact low-frequency cumulant relation plus experimental scaling; common-delay identifiability corrected; no novelty claim

## 1. Purpose

The active inverse reconstructs **differential internal transport modes** from wavelength-dependent timing.

Directly resolving picosecond changes in a nanosecond-scale impulse response is awkward. Frequency-domain phase provides a cleaner observable.

The 2022 graded-HgCdTe study already used an LCA / network-analyzer chain from roughly `50 MHz` to `1 GHz`, but with fixed `1550 nm` excitation that strongly surface absorbs. The proposed method requires a tunable/modulated MWIR source across the graded absorption interval.

---

## 2. Timing transfer function

For carrier collection time `T_lambda`,

```math
\boxed{
H_\lambda(\Omega)
=\left\langle e^{-i\Omega T_\lambda}\right\rangle.
}
```

The cumulant expansion is

```math
\ln H_\lambda
=-i\Omega\kappa_1
-\frac{\Omega^2}{2}\kappa_2
+\frac{i\Omega^3}{6}\kappa_3
+O(\Omega^4).
```

Hence

```math
\boxed{
\arg H_\lambda(\Omega)
=-\Omega\langle T_\lambda\rangle
+O(\Omega^3),
}
```

and

```math
\boxed{
\ln|H_\lambda(\Omega)|
=-\frac{\Omega^2}{2}\operatorname{Var}(T_\lambda)
+O(\Omega^4).
}
```

The exact zero-frequency group delay is

```math
\boxed{
-\left.\frac{d}{d\Omega}\arg H_\lambda\right|_{0}
=\langle T_\lambda\rangle.
}
```

---

## 3. Differential phase

If the measured transfer approximately factorizes as

```math
H_{\rm meas}(\Omega,\lambda)
=H_{\rm det}(\Omega,\lambda)H_{\rm common}(\Omega),
```

with wavelength-independent `H_common`, then

```math
\boxed{
\Delta\phi_{12}
\simeq
-\Omega
\left[
\bar T(\lambda_1)-\bar T(\lambda_2)
\right].
}
```

Therefore

```math
\boxed{
\Delta T_{12}
\simeq-\frac{\Delta\phi_{12}}{\Omega}.
}
```

This cancels a truly wavelength-independent common phase/delay exactly.

It does **not** recover the absolute wavelength-independent internal boundary-delay component. That component is gauge-like with common electronics unless independently calibrated or constrained.

---

## 4. Finite-frequency validity

A conservative diagnostic for interpreting phase as the first timing moment is

```math
\boxed{\Omega\sigma_T\ll1.}
```

The first phase correction is

```math
\delta\phi_3=\frac{\Omega^3}{6}\kappa_3.
```

If the low-frequency condition fails, do not extrapolate the linear phase formula. Fit the **full complex transfer function** instead.

Thus

```text
low RF frequency
-> differential mean-delay inversion

higher RF frequency
-> full timing-distribution fit.
```

---

## 5. Phase precision scale

For a local effective speed `v_eff`,

```math
\Delta T\simeq\frac{\Delta x}{v_{\rm eff}},
```

so

```math
\boxed{
|\Delta\phi|
\simeq
\Omega\frac{|\Delta x|}{v_{\rm eff}}.
}
```

Therefore

```math
\boxed{
\sigma_{x,\phi}
\sim
\frac{v_{\rm eff}\sigma_\phi}{\Omega}.
}
```

For illustration only, with

```math
v_{\rm eff}=10^5\ {\rm m/s},
\qquad
f=1\ {\rm GHz},
```

one degree corresponds to about

```math
0.28\ {\rm um}.
```

This is not an instrument-performance or sample-velocity claim.

---

## 6. Correct phase-domain inverse

Let the orientation-correct timing matrix be `A`:

```math
\mathbf T=\mathbf A\mathbf q.
```

A measured common delay adds

```math
\mathbf T^{\rm meas}
=\mathbf A\mathbf q+c\mathbf1.
```

Because `c` is not generically distinguishable from arbitrary boundary-localized internal delay, the robust phase inverse should project out or difference the common wavelength mode:

```math
\boxed{
\mathbf T_\Delta
=\mathbf P_\perp\mathbf A\mathbf q,
}
```

with

```math
\mathbf P_\perp
=\mathbf I-\frac1N\mathbf1\mathbf1^T
```

for simple equal-weight mean subtraction.

At low RF frequency,

```math
\boxed{
\boldsymbol\phi_\Delta
\simeq
-\Omega\mathbf P_\perp\mathbf A\mathbf q.
}
```

For nonuniform measurement covariance, use the corresponding weighted projection / generalized least-squares treatment rather than unweighted mean subtraction.

---

## 7. Multiple RF frequencies

A realistic experiment should measure complex response at several `Omega_k`.

Low-order phase:

```math
\phi_{ik}
=-\Omega_k\mu_i
+\frac{\Omega_k^3}{6}\kappa_{3,i}
+\phi_{\rm common}(\Omega_k)+\cdots.
```

Log magnitude:

```math
\ln|H_{ik}|
=-\frac{\Omega_k^2}{2}\sigma_i^2
+\frac{\Omega_k^4}{24}\kappa_{4,i}
+\cdots.
```

A multi-frequency fit can test whether the assumed first/second-moment regime is valid and, when justified, constrain both differential mean-delay and differential broadening modes.

---

## 8. Experimental systematics

Differential wavelength phase removes only a **wavelength-independent** common transfer.

Dangerous contaminants include

```text
source modulation phase changing with wavelength
optical-path phase/group-delay changes
wavelength-dependent detector impedance
penetration into passivation/contact layers
reference-path drift
power/SNR changes across the scan.
```

These must be measured or included in the covariance/forward model. Uncalibrated source phase must never be interpreted as carrier transit.

---

## 9. Current published-sample scale

The literature-constrained 2023 sample-B calculation gives a conditional mean-generation-depth shift of about

```math
2.85\ {\rm um}
```

from `2.80` to `3.88 um`.

At illustrative `v_eff=1e5 m/s`, this gives about

```math
28.5\ {\rm ps}
```

or

```math
10.25^\circ
```

at `1 GHz`.

A much subtler synthetic `25%` localized slowdown produces only about

```math
0.935^\circ
```

peak-to-peak residual spectral phase at `1 GHz`.

Thus detecting wavelength-dependent delay is much easier than reconstructing internal spatial structure.

---

## 10. Claim boundary

### DERIVED / KNOWN TRANSFORM CONSEQUENCE

- low-frequency phase measures the first timing cumulant;
- log-magnitude curvature measures the second cumulant;
- differential phase cancels a truly wavelength-independent common transfer;
- phase sensitivity scales linearly with RF frequency before higher cumulants matter.

### CORRECTED LIMIT

A wavelength-independent internal boundary-delay component is not generically identifiable from spectral timing alone. Differential phase intentionally removes that mode.

### OPEN

- tunable-MWIR phase covariance;
- source/reference architecture;
- achievable usable RF frequency before full-transfer fitting is required;
- real HgCdTe transport reconstruction;
- novelty / priority.

---

## 11. Next decisive work

Build an **instrument-level wavelength × RF-frequency covariance model** and perform a multi-frequency complex-response inverse on the published sample-B matrix.

Do not add another abstract timing formula unless it changes the experimental identifiability.
