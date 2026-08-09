# Paired A/B Phase — Common-Mode Correlation and Reciprocal-Swap Stability Requirements

**Date:** 2026-08-09  
**Status:** analytic covariance requirements for the paired differential-phase protocol; no complete instrument model and no novelty claim

## 1. Purpose

The paired A/B protocol is intended to cancel wavelength-dependent tunable-source phase.

That benefit depends on how nearly common-mode the phase fluctuation actually is at the two detector channels.

Question:

> **How correlated must the two phase channels be to reach the sub-degree differential precision required by the few-mode inverse?**

A second question concerns the reciprocal A/B arm swap:

> **How stable must the differential arm phase remain between the two swap measurements?**

---

## 2. General two-channel phase covariance

Let the random phase errors at one wavelength/frequency be

```math
\delta\phi_A,
\qquad
\delta\phi_B,
```

with

```math
\operatorname{Var}(\delta\phi_A)=\sigma_A^2,
```

```math
\operatorname{Var}(\delta\phi_B)=\sigma_B^2,
```

and correlation coefficient

```math
\rho
=\frac{\operatorname{Cov}(\delta\phi_A,\delta\phi_B)}
{\sigma_A\sigma_B}.
```

The differential phase error is

```math
\delta\phi_{AB}
=\delta\phi_A-\delta\phi_B.
```

Therefore

```math
\boxed{
\sigma_{AB}^2
=\sigma_A^2+\sigma_B^2
-2\rho\sigma_A\sigma_B.
}
```

This is the fundamental paired-phase covariance relation.

---

## 3. Equal-channel limit

For

```math
\sigma_A=\sigma_B=\sigma,
```

```math
\boxed{
\sigma_{AB}
=\sigma\sqrt{2(1-\rho)}.
}
```

Thus a large absolute phase fluctuation can be harmless if it is truly common mode.

Conversely, using the same laser/source is not enough by itself. The source/path fluctuation must remain highly correlated at the two detector inputs.

---

## 4. Required correlation for a 0.10-degree differential target

Solve

```math
\sigma_{AB}
\le\sigma_{\rm target}
```

for `rho`:

```math
\boxed{
\rho
\ge
1-
\frac{\sigma_{\rm target}^2}
{2\sigma^2}.
}
```

For

```math
\sigma_{\rm target}=0.10^\circ,
```

representative equal-channel absolute phase fluctuations require:

| individual phase RMS | required correlation `rho` | RMS suppression `sigma/sigma_target` |
|---:|---:|---:|
| 0.25 deg | >0.9200 | 2.5 |
| 0.50 deg | >0.9800 | 5 |
| 1.0 deg | >0.9950 | 10 |
| 2.0 deg | >0.99875 | 20 |
| 5.0 deg | >0.99980 | 50 |
| 10 deg | >0.99995 | 100 |

In amplitude-ratio language, suppressing

```text
1 degree -> 0.1 degree
```

is `20 dB` RMS common-mode rejection, while

```text
10 degree -> 0.1 degree
```

is `40 dB`.

This is not an electrical CMRR specification; it is simply a useful phase-noise suppression ratio.

---

## 5. Exact common source phase cancels algebraically

If the two channels contain an exactly common source phase

```math
\phi_{\rm src}(\lambda,\Omega),
```

then

```math
\phi_A
=\phi_{\rm src}+\psi_A,
```

```math
\phi_B
=\phi_{\rm src}+\psi_B,
```

and

```math
\boxed{
\phi_A-\phi_B
=\psi_A-\psi_B.
}
```

The magnitude of `phi_src` is irrelevant.

The practical problem is imperfect common-mode delivery:

```text
path-length fluctuations
splitter/optic dispersion
beam pointing
reference-channel mismatch
wavelength-dependent coupling
separate receiver-chain phase.
```

Those terms reduce effective correlation below unity.

---

## 6. Common + differential noise decomposition

A useful measurement model is

```math
\delta\phi_A
=c+d_A,
```

```math
\delta\phi_B
=c+d_B,
```

where `c` is common and `d_A,d_B` are residual differential errors.

Then

```math
\boxed{
\delta\phi_{AB}=d_A-d_B.
}
```

The common phase cancels exactly regardless of its variance.

This representation is often more physically meaningful than describing everything by one correlation coefficient.

The experiment should therefore measure the residual differential phase spectrum directly with the two optical/electrical arms terminated in a known common reference condition.

---

## 7. Reciprocal arm-swap cancellation

Let the device transport contrast be

```math
\Phi_{AB}.
```

Let the static differential arm/channel phase be `psi`.

Configuration 1:

```math
D_1
=\Phi_{AB}+\psi(t_1)+n_1.
```

After swapping A and B between the two arms/channels:

```math
D_2
=\Phi_{AB}-\psi(t_2)+n_2.
```

Use

```math
\boxed{
\hat\Phi_{AB}
=\frac{D_1+D_2}{2}.
}
```

Then

```math
\boxed{
\hat\Phi_{AB}-\Phi_{AB}
=\frac{\psi(t_1)-\psi(t_2)}{2}
+\frac{n_1+n_2}{2}.
}
```

The static arm mismatch cancels only to the extent that it remains stable between the two swapped measurements.

---

## 8. Swap-stability requirement

Define differential-arm drift between swap measurements

```math
\Delta\psi
=\psi(t_2)-\psi(t_1).
```

Its residual contribution is

```math
\boxed{
\delta\phi_{\rm swap}
=-\frac{\Delta\psi}{2}.
}
```

Therefore to keep this systematic alone below target `sigma_target`, require approximately

```math
\boxed{
\sigma_{\Delta\psi}
\lesssim2\sigma_{\rm target}.
}
```

For a `0.10 degree` target:

```math
\boxed{
\sigma_{\Delta\psi}
\lesssim0.20^\circ.
}
```

For `0.03 degree`:

```math
\boxed{
\sigma_{\Delta\psi}
\lesssim0.06^\circ.
}
```

This gives an experimentally measurable stability requirement for the swap cadence.

---

## 9. Random-noise cost of the swap

The swap is a systematic-rejection procedure, not a free SNR gain.

If a fixed total measurement time is split equally between two statistically independent swap configurations, white-noise variance from each configuration rises because each receives half the averaging time.

Averaging the two then approximately returns the same net white-noise information that one full-time configuration would have had.

Therefore:

> **the scientific value of the reciprocal swap is removal of stable arm bias, not improvement of the white-noise floor.**

---

## 10. Temperature difference-in-differences adds another stability axis

At each temperature, simultaneous A-B subtraction cancels common source phase.

A temperature difference then contains the change in differential arm/device-chain phase:

```math
\Delta_T\Delta\phi_{\rm chain}
=\Delta\phi_{\rm chain}(T_2)
-\Delta\phi_{\rm chain}(T_1).
```

This term does not cancel merely because the same source is used.

Temperature-dependent

```text
detector impedance
cable/connector phase
cryostat-window phase
mechanical path length
package parasitics
```

must therefore be calibrated or included as nuisance parameters.

The paired temperature design is strongest if electronics/reference paths remain outside the temperature-varying region and the device-specific transfer can be independently characterized.

---

## 11. Calibration experiment before using HgCdTe transport data

Before interpreting A-B phase as transport, measure the differential phase covariance with a configuration in which both channels receive the **same known optical/electrical transfer** as nearly as practical.

The calibration should determine

```text
sigma_A(lambda,f)
sigma_B(lambda,f)
rho(lambda,f)
residual differential phase PSD
drift/Allan deviation versus time
swap repeatability.
```

This directly answers whether the experiment can support

```text
0.1 degree
0.05 degree
0.03 degree
```

differential precision over the wavelength/RF grid of interest.

---

## 12. Main experimental implication

The current few-mode inverse needs sub-degree **differential** phase, not necessarily sub-degree absolute source phase.

That distinction is critical.

For example, `1 degree` RMS absolute phase fluctuations can still support `0.1 degree` differential precision if their effective A/B correlation exceeds about

```math
\boxed{0.995.}
```

If absolute fluctuations are `5 degrees`, the required correlation rises to about

```math
\boxed{0.9998.}
```

Thus the experiment should be optimized for **common-mode phase delivery and differential stability**, not merely absolute source phase quality.

---

## 13. Claim boundary

### DERIVED

```math
\boxed{
\sigma_{AB}^2
=\sigma_A^2+\sigma_B^2
-2\rho\sigma_A\sigma_B
}
```

and, for equal channels,

```math
\boxed{
\sigma_{AB}=\sigma\sqrt{2(1-\rho)}.
}
```

Reciprocal swap residual:

```math
\boxed{
\delta\phi_{\rm swap}
=[\psi(t_1)-\psi(t_2)]/2.
}
```

### CHECKED NUMERICAL SCALES

For a `0.10 degree` differential target:

```text
1 degree individual RMS -> rho >0.995
5 degree -> rho >0.9998
10 degree -> rho >0.99995
swap differential drift should be <~0.20 degree RMS if it alone uses the error budget.
```

### NOT ESTABLISHED

- actual source/common-mode correlation;
- actual arm drift spectrum;
- achievable swap cadence/stability;
- actual temperature-dependent differential-chain phase;
- novelty / priority.

---

## 14. Next decisive work

The next instrument-level experiment should measure

> **the differential phase covariance and drift of the proposed two-arm setup before any HgCdTe transport inversion is attempted.**

That empirical covariance can then replace the current equal/statistics/additive toy noise models in the optimal wavelength × RF-frequency design.
