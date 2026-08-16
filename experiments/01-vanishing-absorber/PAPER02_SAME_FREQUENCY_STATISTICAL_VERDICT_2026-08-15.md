# Paper 02 — Same-Frequency Statistical Verdict

**Status:** **CHECKED UNDER EXPLICIT THEORETICAL NOISE MODEL**

## Verdict: **FREQUENCY-DEPENDENT SAME-FREQUENCY HIDDEN-RISK ORDERING**

The ordering is not uniform across RF.  At the tested low-frequency point(s), the spectral-model check self-announces first (100 MHz: one-mode rejection 102.290 dB, positive-D detection 111.863 dB).  At the other tested point(s), positive apparent diffusion reaches the stated 90% detection power before the one-mode manifold reaches 90% rejection power, leaving finite RMS-channel-SNR hidden-risk windows (500 MHz: 70.044--88.192 dB; 1 GHz: 52.413--81.804 dB).  The example therefore supports conditional same-frequency hidden risk at those RF points but not a universal stealth claim.

## Reference noise/test model

```text
six complex spectral channels
independent equal Gaussian real/imag quadrature noise
S = RMS_m |J_m| / sigma_quadrature
alpha = 0.0027
power = 0.90
one-mode residual dof = 6
```

## Numerical ordering

| RF | D_eff [m^2/s] | SNR positive D [dB] | SNR one-mode rejection [dB] | D first? |
|---:|---:|---:|---:|:---:|
| 100 MHz | 2.609795e-03 | 111.863 | 102.290 | NO |
| 500 MHz | 2.548603e-03 | 70.044 | 88.192 | YES |
| 1000 MHz | 2.348945e-03 | 52.413 | 81.804 | YES |

## Interpretation rule

A hidden-risk window at one RF point means only that, under the stated covariance and power criterion, positive apparent diffusion reaches the chosen detection power before the same-frequency one-mode goodness-of-fit test reaches the chosen rejection power.  It is not a statement of universal model indistinguishability.

The deterministic full-vector residual `||J-J_fit||/||J||` remains useful as an approximation metric but must not be substituted for this covariance-aware model-selection result.

This verdict concerns only same-frequency channel-manifold rejection.  Multi-frequency homogeneous transport-law rejection is a separate test documented in `PAPER02_END_TO_END_REJECTION_SNR_RESULT_2026-08-15.md`.
