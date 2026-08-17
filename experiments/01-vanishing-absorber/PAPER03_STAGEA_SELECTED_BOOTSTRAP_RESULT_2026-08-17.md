# Paper 03 Stage-A selected-point bootstrap result

**Date:** 2026-08-17  
**Status:** **CHECKED PREDECLARED BROAD FIRST-FAMILY STATISTICAL RESULT / NON-CLAIM**

## Decision

The two non-nominal coordinates selected by the predeclared refined-regime rules both satisfy the locked early-warning condition at 100 MHz, 500 MHz, and 1 GHz. Together with the already-complete nominal bootstrap, the first geometry family therefore supports candidate Outcome A across the complete predeclared expensive-bootstrap set.

This remains a Stage-A fixed-field result. It is not a standalone Paper-03 GO and does not set `science_interpretation_ready=true`.

## Selection provenance

The 60-point coarse screen and S0--S7 selection rules were fixed before output inspection. Six unique detector coordinates were refined at 161x121 and 201x151 under the unchanged numerical gate. The refined selection rules promoted only:

```text
R2_A04  = S2/S3 boundary/worst-warning coordinate
R1_B04  = distinct S1 maximum-confound optical-position coordinate
R0_A21  = nominal coordinate; existing predeclared bootstrap reused
```

No S4/S5/S7 case was promoted post hoc.

## Locked statistical contract

The selected-point shards reuse the nominal bootstrap contract unchanged:

```text
per-quadrature independent Gaussian complex noise
alpha = 0.002699796063260207
power target = 0.90
N_null = 4000 per SNR candidate
N_alt  = 2000 per SNR candidate
SNR candidates = analytic threshold + {-4,-2,0,+2,+4} dB
empirical null quantile method = higher
calibrated-kernel nonlinear one-mode refit for every realization
fast bounded refit spot-checked against the full multistart fitter
```

Frozen transport-claim SNR comparison coordinates:

```text
100 MHz = 96.1 dB
500 MHz = 82.3 dB
1 GHz   = 76.7 dB
```

## Authoritative run

```text
workflow run = 32079076004
workflow head = 9b5fc44be8e3fbcd0809dbaf314b6e389d8c7780
jobs = 6/6 completed successfully
```

The workflow's structural assertions verified the locked alpha, power target, bootstrap populations, five SNR offsets, `science_interpretation_ready=false`, and fast/full refit residual-ratio limit <=1.001.

## Results

| coordinate | RF | analytic SNR (dB) | lowest tested SNR with power >=0.90 (dB) | claim SNR (dB) | conservative tested warning margin (dB) | supported |
|---|---:|---:|---:|---:|---:|---|
| R2_A04 | 100 MHz | 60.359568 | 62.359568 | 96.1 | **33.740432** | yes |
| R2_A04 | 500 MHz | 59.313200 | 61.313200 | 82.3 | **20.986800** | yes |
| R2_A04 | 1 GHz | 57.657850 | 57.657850 | 76.7 | **19.042150** | yes |
| R1_B04 | 100 MHz | 60.273205 | 62.273205 | 96.1 | **33.826795** | yes |
| R1_B04 | 500 MHz | 57.923011 | 59.923011 | 82.3 | **22.376989** | yes |
| R1_B04 | 1 GHz | 56.689559 | 56.689559 | 76.7 | **20.010441** | yes |

The nominal R0_A21 result remains:

| coordinate | RF | lowest tested SNR with power >=0.90 (dB) | claim SNR (dB) | conservative tested warning margin (dB) |
|---|---:|---:|---:|---:|
| R0_A21 | 100 MHz | 76.545 | 96.1 | **19.55** |
| R0_A21 | 500 MHz | 73.137 | 82.3 | **9.16** |
| R0_A21 | 1 GHz | 65.892 | 76.7 | **10.81** |

All nine predeclared nominal/selected RF tests therefore support the same directional conclusion: the calibrated-kernel one-mode mismatch becomes statistically detectable before the SNR required for the frozen false homogeneous-transport claim.

## Artifact provenance

```text
R2_A04 / 100 MHz
artifact id = 9305003275
digest = sha256:2c1416f5ddb89c05c00d8a2687604397be67b14e29418ffa6469c473138e4629

R2_A04 / 500 MHz
artifact id = 9304779194
digest = sha256:677e6ca88309ecb96c285dc317ffbbe1e2d9e96a36ba2fb61f3e1eb2a415b79d

R2_A04 / 1 GHz
artifact id = 9304710879
digest = sha256:9d88943113c06e3fbaf35f86aa64d05c4cdae8f4e331e4ceecb590220b862f28

R1_B04 / 100 MHz
artifact id = 9304872682
digest = sha256:7a9bc3940f6308d5e0e0ae4870b96347ce72d9a647c8a7a0b744a00815bbc31c

R1_B04 / 500 MHz
artifact id = 9304901849
digest = sha256:5975c2205265731225675dc743e52483134cbbbe91c93f3031307285ebbe54c7

R1_B04 / 1 GHz
artifact id = 9304867657
digest = sha256:a5469ee8c16e002ff0575fae28a31cbc623da38b45aa47149ef99a9ee38fad5b
```

## Scientific boundary

Supported at this stage:

> In the predeclared first Stage-A geometry family, including the nominal detector coordinate and the two non-nominal coordinates selected for expensive statistical testing by rules fixed before the broad-screen result was read, the calibrated-kernel one-mode falsification becomes detectable before the frozen false homogeneous-transport claim threshold at all three tested RFs.

Not supported yet:

```text
universality across detector topology;
self-consistent semiconductor validity;
absolute novelty;
Paper 03 standalone GO;
science_interpretation_ready = true.
```

The next independent gates remain the materially different coplanar geometry family and Stage-B self-consistent semiconductor operating-state validation.
