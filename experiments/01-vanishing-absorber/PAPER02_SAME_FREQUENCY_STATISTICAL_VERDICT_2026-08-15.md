# Paper 02 — Same-Frequency Statistical Verdict

**Status:** **CHECKED UNDER EXPLICIT THEORETICAL NOISE MODEL**

## Verdict: **SAME-FREQUENCY HIDDEN-RISK ORDERING FAILED UNDER THE REFERENCE NOISE MODEL**

At 100 MHz, the six-channel one-mode model is rejectable at an RMS-channel SNR no greater than that required to establish positive apparent diffusion.  The current example therefore does not support a claim that a statistically established positive diffusion coefficient is hidden from the same-frequency spectral model check.  The paper must retain the result as an effective-parameter bias / low-frequency dispersion alias and avoid claiming same-frequency statistical stealth for this case.

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

At 100 MHz:

```text
SNR_D          = 391859.924
SNR_1mode      = 130167.969
SNR_1mode/SNR_D= 0.332179844
```

## Interpretation rule

The deterministic full-vector residual `||J-J_fit||/||J||` remains useful as an approximation metric but must not be substituted for this covariance-aware model-selection result.

This verdict concerns only same-frequency channel-manifold rejection.  Multi-frequency homogeneous transport-law rejection is a separate test documented in `PAPER02_END_TO_END_REJECTION_SNR_RESULT_2026-08-15.md`.
