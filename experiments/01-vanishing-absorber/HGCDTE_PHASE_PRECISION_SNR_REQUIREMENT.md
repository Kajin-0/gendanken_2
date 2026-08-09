# Phase Precision from Coherent SNR — White-Noise Requirement for the HgCdTe Timing Inverse

**Date:** 2026-08-09  
**Status:** analytic high-SNR white-noise requirement for coherent phase estimation; establishes a lower-level measurement resource equation, not a complete instrument covariance model; no novelty claim

## 1. Purpose

The dimensional sample-B inverse indicates that

```text
~0.1 degree differential phase precision
```

is a useful scale for recovering approximately three coarse transport modes in the stated synthetic anomaly test.

The next question is experimental:

> **What coherent signal-to-noise ratio is fundamentally required to estimate phase with that precision?**

This note derives the simplest white-noise limit. It is intentionally narrower than a full VNA/source/readout error model.

---

## 2. Signal and noise convention

Let the measured current contain a coherent sinusoidal component

```math
\boxed{
i(t)
=I_1\cos(\Omega t+\phi)+n(t),
}
```

where `I_1` is the **peak** current amplitude.

Let `n(t)` be additive zero-mean white current noise with one-sided power spectral density

```math
\boxed{S_I\quad[{\rm A^2/Hz}].}
```

Estimate the two quadratures over coherent integration time `t`:

```math
X=\frac{2}{t}\int_0^t i(t')\cos\Omega t'\,dt',
```

```math
Y=\frac{2}{t}\int_0^t i(t')\sin\Omega t'\,dt'.
```

For an integer or sufficiently coherent number of periods,

```math
\langle X\rangle=I_1\cos\phi,
```

```math
\langle Y\rangle=-I_1\sin\phi.
```

With the stated one-sided PSD convention, each quadrature has variance

```math
\boxed{
\operatorname{Var}(X)
=\operatorname{Var}(Y)
\simeq\frac{S_I}{t}.
}
```

---

## 3. High-SNR phase variance

For small quadrature fluctuations about a coherent phasor,

```math
\delta\phi
\simeq
\frac{\delta Q_\perp}{I_1}.
```

Therefore

```math
\boxed{
\sigma_\phi^2
\simeq
\frac{S_I}{I_1^2t}.
}
```

Equivalently define the coherent power-SNR-like quantity

```math
\boxed{
\rho
\equiv
\frac{I_1^2t}{S_I}.
}
```

Then

```math
\boxed{
\sigma_\phi
\simeq
\rho^{-1/2}.
}
```

This is the central resource relation.

---

## 4. Required coherent SNR for phase precision

For target phase standard deviation `sigma_phi`,

```math
\boxed{
\rho_{\rm req}
\simeq
\frac1{\sigma_\phi^2}.
}
```

Representative values:

| phase precision | `rho_req` | amplitude SNR `sqrt(rho)` | `10 log10 rho` |
|---:|---:|---:|---:|
| 0.25 deg | `5.25e4` | 229 | 47.2 dB |
| 0.10 deg | `3.28e5` | 573 | 55.2 dB |
| 0.05 deg | `1.31e6` | 1146 | 61.2 dB |
| 0.03 deg | `3.65e6` | 1910 | 65.6 dB |
| 0.01 deg | `3.28e7` | 5730 | 75.2 dB |

Thus the current coarse-tomography target

```math
\sigma_\phi\sim0.1^\circ
```

corresponds to approximately

```math
\boxed{55\ {\rm dB}}
```

of coherent power-SNR for **one** phase estimate in this ideal white-noise limit.

---

## 5. Differential A-B phase

For independent phase estimates from samples A and B,

```math
\Delta\phi_{AB}=\phi_A-\phi_B,
```

so

```math
\boxed{
\sigma_{AB}^2
=\sigma_A^2+\sigma_B^2.
}
```

If the two channels contribute equally and the target **difference** precision is `sigma_AB`, then

```math
\sigma_A
=\sigma_B
=\frac{\sigma_{AB}}{\sqrt2}.
```

Therefore each channel needs

```math
\boxed{
\rho_{A,B}
\simeq
\frac{2}{\sigma_{AB}^2}.
}
```

For a `0.10 degree` A-B differential phase target,

```text
single-channel requirement ~58.2 dB each.
```

For `0.03 degree` differential precision,

```text
~68.6 dB each.
```

Correlated noise can either improve or worsen the differential variance depending on its covariance. The independent-channel formula is not universal.

---

## 6. Current-noise / averaging-time form

Rearrange:

```math
\boxed{
t
\simeq
\frac{S_I}
{I_1^2\sigma_\phi^2}.
}
```

Using current-noise amplitude density

```math
i_n=\sqrt{S_I},
```

```math
\boxed{
t
\simeq
\left(
\frac{i_n}{I_1\sigma_\phi}
\right)^2.
}
```

This explicitly shows why weak long-wave signal increases the required averaging resource rapidly.

---

## 7. Optical NEP form

If the detector/readout can be represented by an incident-power-referred one-sided NEP amplitude density `NEP` and the coherent **peak** modulated optical-power amplitude is `P_1`, then

```math
I_1=R_I P_1,
```

```math
S_I=R_I^2{\rm NEP}^2.
```

Hence the responsivity cancels:

```math
\boxed{
\sigma_\phi
\simeq
\frac{{\rm NEP}}
{P_1\sqrt t},
}
```

and

```math
\boxed{
t
\simeq
\left(
\frac{{\rm NEP}}
{P_1\sigma_\phi}
\right)^2.
}
```

This form is valid only when a single incident-power-referred NEP meaningfully describes the white noise at the RF frequency of interest.

It does not include coherent source phase noise, drift, multiplicative intensity noise, or nonlinear optical loading.

---

## 8. Connection to wavelength-dependent absorbed signal

If incident modulation amplitude is fixed while only a fraction `P_abs(lambda)` contributes to the useful detector signal, then approximately

```math
I_1(\lambda)
\propto
P_{\rm abs}(\lambda).
```

For additive wavelength-independent white current noise,

```math
\boxed{
\sigma_\phi(\lambda)
\propto
\frac1{P_{\rm abs}(\lambda)\sqrt t}.
}
```

Thus

```math
\boxed{
t\propto P_{\rm abs}^{-2}}
```

for equal phase precision at fixed incident power.

This recovers the additive-noise scaling used in the heteroscedastic sample-B Monte Carlo.

If the noise itself scales with signal/photon statistics, the exponent changes, giving the previously used statistics-like `t proportional to 1/P_abs` limit.

---

## 9. Reciprocal swap and random noise

A reciprocal A/B arm swap is valuable because it cancels stable differential path/channel phase.

But if the two swapped measurements simply divide a fixed total integration time and have independent equal white noise, the swap does **not** create free random-noise SNR.

It trades measurement time for systematic cancellation.

Therefore the swap should be judged by how much systematic phase bias it removes, not by claiming a statistical sensitivity gain.

---

## 10. Main practical conclusion

The ideal white-noise requirement for `0.1 degree` phase is demanding but not absurd:

```math
\rho\sim3.3\times10^5
```

for one channel, or roughly `55 dB` coherent power-SNR.

For a two-channel differential phase target of the same precision, each independent equal channel needs about `58 dB`.

This makes the dominant experimental risk increasingly clear:

> **once coherent amplitude SNR is adequate, wavelength-dependent systematic/correlated phase errors can dominate before white detector noise does.**

That is why the paired same-source A/B protocol, reciprocal arm calibration, and full covariance measurement are more important than simply increasing integration time indefinitely.

---

## 11. What this does not include

The relation does not yet include

- 1/f or colored RF noise;
- VNA/source residual phase noise;
- coherent reference jitter;
- wavelength-tuning repeatability;
- correlated A/B noise;
- amplitude-to-phase conversion;
- detector impedance and packaging;
- temperature drift;
- optical speckle/etalon phase;
- nonlinear response versus optical loading.

These belong in the next instrument-level covariance model.

---

## 12. Claim boundary

### DERIVED / CONDITIONAL ON THE STATED WHITE-NOISE ESTIMATOR

```math
\boxed{
\sigma_\phi^2
\simeq
\frac{S_I}{I_1^2t}
}
```

and

```math
\boxed{
\rho_{\rm req}\simeq1/\sigma_\phi^2.
}
```

### CHECKED NUMERICAL SCALES

```text
0.10 degree -> ~55.2 dB single phase
0.10 degree differential A-B -> ~58.2 dB per equal independent channel
0.03 degree single phase -> ~65.6 dB
0.03 degree differential -> ~68.6 dB per equal independent channel.
```

### NOT ESTABLISHED

- actual sample-A/B coherent SNR;
- actual phase covariance of a tunable MWIR system;
- actual integration time;
- whether white noise dominates;
- novelty / priority.

---

## 13. Next decisive work

The next instrument model should separate

```text
white incoherent noise
+
common source phase noise
+
A/B differential path drift
+
wavelength-dependent systematic phase.
```

Only the first term is reduced indefinitely by simple averaging.

The paired/swap protocol should then be evaluated by its ability to reject the correlated/systematic terms rather than by white-noise SNR alone.
