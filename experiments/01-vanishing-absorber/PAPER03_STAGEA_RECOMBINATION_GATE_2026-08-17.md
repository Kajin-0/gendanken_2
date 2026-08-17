# Paper 03 Stage-A Gate — Finite Recombination

**Date:** 2026-08-17  
**Status:** **CHECKED NUMERICAL / MODEL-CONSISTENCY RESULT; NON-CLAIM**  
**Coordinate:** `D=2.5e-3 m^2/s`, `tau=5 ns` on the finite75 + depletion fixed-field Stage-A model.

## 1. Authoritative workflow

```text
workflow = Paper 03 Stage A finite recombination gate
run      = 32063318206
job      = 95489386030
head     = e4fa9213ce282cdf57135e7b0c15a9561cd73acd
conclusion = success
```

Artifact:

```text
name   = paper03-stageA-finite-recombination
id     = 9298948935
digest = sha256:079551acda0ec2420912382fe119638fbd24179af19d120678ca59771ec360c1
```

All numerical and non-claim assertions passed. This remains a fixed-field backward-resolvent calculation, not Stage-B self-consistent semiconductor Poisson/drift-diffusion.

---

## 2. Numerical gates

### Spatial refinement

161x121 -> 201x151 raw historical phase changes were

| RF | change / frozen target |
|---:|---:|
| 100 MHz | 0.0114533 |
| 500 MHz | 0.0119067 |
| 1 GHz | 0.0123265 |

Worst:

```text
1.23265% of frozen target
```

against the retained `2%` readiness threshold: **PASS**.

### Lateral source quadrature

13 -> 17 point changes were

| RF | change / frozen target |
|---:|---:|
| 100 MHz | 4.9816e-5 |
| 500 MHz | 4.8354e-5 |
| 1 GHz | 4.3347e-5 |

Worst:

```text
4.9816e-5 = 0.00498% of target
```

against the retained `0.5%` source-quadrature threshold: **PASS**.

---

## 3. Same-physics planar comparison

Both finite and planar calculations use

```text
D = 2.5e-3 m^2/s
tau = 5 ns
201 x 151 grid
17-point lateral quadrature
the same six calibrated HgCdTe optical kernels
```

The raw historical phase comparison is

| RF | finite raw phase | planar raw phase | finite - planar | |excess / frozen target| |
|---:|---:|---:|---:|---:|
| 100 MHz | -0.00609802 deg | +0.00282733 deg | -0.00892535 deg | 0.74515 |
| 500 MHz | -0.03269905 deg | +0.01400967 deg | -0.04670872 deg | 0.79535 |
| 1 GHz | -0.07297125 deg | +0.02722504 deg | -0.10019629 deg | 0.90753 |

Compared with the infinite-lifetime Stage-A coordinate (`0.72835`, `0.77391`, `0.87511`), this finite-lifetime sensitivity point does not suppress the order-one finite-geometry confound; it modestly increases the raw finite-minus-planar fraction.

This comparison remains a coordinate, not a mechanism-specific transport claim.

---

## 4. Kernel-aware one-mode residual

The calibrated arbitrary-kernel model

```math
J_m=A+B M_m(r)
```

was refit independently at each RF.

### Central quartet

| RF | finite rho | planar rho |
|---:|---:|---:|
| DC | 8.1612e-5 | 3.8892e-9 |
| 100 MHz | 8.2783e-5 | 3.8880e-9 |
| 500 MHz | 1.0975e-4 | 3.8597e-9 |
| 1 GHz | 1.8829e-4 | 3.7867e-9 |

### All six channels

| RF | finite rho | planar rho |
|---:|---:|---:|
| DC | 2.4872e-4 | 1.5991e-6 |
| 100 MHz | 2.5394e-4 | 1.5978e-6 |
| 500 MHz | 3.6661e-4 | 1.5667e-6 |
| 1 GHz | 6.6318e-4 | 1.4708e-6 |

Thus the finite-lifetime coordinate retains the same qualitative structure as the infinite-lifetime calculation:

```text
planar control -> nearly one-mode under the calibrated-kernel fit;
finite-contact/depletion -> small but numerically resolved one-mode mismatch.
```

The finite all-six residual is approximately `159x`, `234x`, and `451x` the planar floor at 100 MHz, 500 MHz, and 1 GHz respectively.

---

## 5. Interpretation boundary

This gate establishes numerical robustness of one finite-recombination sensitivity coordinate only. It does not establish

```text
a physically calibrated HgCdTe lifetime;
a broad lifetime regime;
a physical interpretation of the fitted exponent r;
statistical detectability of the one-mode residual;
a stable second spatial mode;
or self-consistent semiconductor electrostatics.
```

The next relevant work is the kernel-aware model-order/statistical gate, followed by a broader dimensionless diffusion/lifetime map and Stage-B self-consistent forward physics.

`science_interpretation_ready` remains false.