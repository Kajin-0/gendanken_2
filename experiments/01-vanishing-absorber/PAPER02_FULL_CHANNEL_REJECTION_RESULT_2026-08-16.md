# Paper 02 — full-channel versus root-space rejection result

**Date:** 2026-08-16  
**Status:** **CHECKED / REVIEW ISSUE RESOLVED**

Workflow:

```text
run 31965712566
artifact paper02-full-channel-rejection
artifact id 9268427122
artifact SHA-256 63f6961bff5b343c792a1279d1ea3b75961932a4c0ff7acba8e98dea25c4b182
```

The comparison uses the exact planar continuum forward data and the same theoretical equal-quadrature noise normalization for both statistics:

```text
S = RMS_m |J_m| / sigma_quadrature
S_dB = 20 log10 S
alpha = 0.0027
power = 0.90
```

## Main result

| Maximum RF | Root-space required SNR | Full-channel required SNR | Full - root |
|---:|---:|---:|---:|
| 200 MHz | 132.83 dB | 96.34 dB | -36.49 dB |
| 300 MHz | 121.78 dB | 92.49 dB | -29.29 dB |
| 500 MHz | 107.84 dB | 88.42 dB | -19.42 dB |
| 750 MHz | 97.56 dB | 84.69 dB | -12.87 dB |
| 1 GHz | 90.37 dB | 81.51 dB | -8.86 dB |
| 1.5 GHz | 79.90 dB | 76.86 dB | -3.04 dB |
| 2 GHz | 73.20 dB | 72.28 dB | -0.93 dB |
| 3 GHz | 64.21 dB | 65.00 dB | +0.79 dB |

Through 1 GHz, retaining the same-frequency normal residual directions gives a substantial discrimination advantage relative to compressing each six-channel measurement to one complex root. By 3 GHz, the root-dispersion mismatch itself is strong enough that the lower-dimensional root-space statistic slightly wins after accounting for the full-channel statistic's larger residual degrees of freedom.

The best-fit homogeneous parameters from the two protocols agree closely. Through 1 GHz:

```text
root-space D = 2.388929748e-3 m^2/s
full-channel D = 2.388810336e-3 m^2/s
```

Through 3 GHz:

```text
root-space D = 1.028624337e-3 m^2/s
full-channel D = 1.028447145e-3 m^2/s
```

Thus the distinction is primarily statistical information retention, not a materially different pseudo-true homogeneous parameter in this stress.

## Rev. 8 consequence

The Rev. 7 thresholds must be described explicitly as a **root-space multi-frequency rejection test**. Rev. 8 should add the full-channel comparison and state:

- same-frequency residual directions can materially improve rejection in the low/intermediate bandwidth regime;
- root compression is not a sufficient statistic for general model rejection;
- neither protocol is globally optimal under arbitrary experiment design/covariance;
- at sufficiently broad bandwidth the simpler root-space dispersion test can become comparably or slightly more efficient because it carries fewer residual degrees of freedom.

This resolves the adversarial review's methodological qualification without overclaiming a universally optimal test.
