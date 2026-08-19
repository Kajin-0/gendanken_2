# Paper 03 — Second Geometry Numerical Gate Lock

**Date:** 2026-08-17  
**Status:** **LOCKED BEFORE SECOND-GEOMETRY NUMERICAL OUTPUT / NON-CLAIM**

This file instantiates the numerical-convergence requirement in `PAPER03_SECOND_GEOMETRY_PREDECLARATION_2026-08-17.md` before any coplanar-family result is calculated or read.

## Frozen geometry and physics

No geometric or physical coordinate is changed from the family predeclaration:

```text
absorber: 16.0 um wide x 7.6 um thick
left top contact:  x in [-8,-2] um, V=0
right top contact: x in [+2,+8] um, V=+0.30 V
central top gap:   x in (-2,+2) um, insulating
bottom: insulating
sidewalls: insulating
selected terminal: right top contact
physical field: Laplace only
weighting field: independent Laplace solve, right=1 and left=0
D = 2.5e-3 m^2/s
tau = infinity
same velocity-field law as first Stage-A family
same six calibrated HgCdTe vertical optical kernels
beam center x0 = 0
beam sigma = 1.0 um
```

For the finite numerical source integral, use a Gauss-Legendre lateral interval

```text
x in [-3.5,+3.5] um
```

with the truncated Gaussian renormalized on that fixed interval. This support contains the declared centered beam and is frozen before output. It is not changed in response to the result.

## Spatial-grid ladder

Use exactly the initially declared ladder:

```text
81 x 61
121 x 91
161 x 121
```

The contact edges at `x=+-2 um` lie exactly on all three lateral grids.

Before any model-order interpretation require on every grid:

```text
physical-potential linear backward error < 1e-8
weighting-potential linear backward error < 1e-8
RF resolvent relative residual < 1e-8
selected-contact committor relative residual < 1e-8
DC committor/Ramo max-absolute identity error < 1e-8
```

## Topology-appropriate finest-pair convergence

The first-family `2% of frozen raw phase` criterion is deliberately not reused as the sole gate.

At each nonzero RF, define

```text
e_J = ||J_161 - J_121||_2 / ||J_161||_2

e_dJ = ||Delta J_161 - Delta J_121||_2 / ||Delta J_161||_2
```

where each norm is over all six calibrated complex channels and `Delta` is the adjacent-wavelength first difference.

Also fit the calibrated-kernel all-six one-mode model independently at each grid and define

```text
rho = contrast-normalized one-mode residual
Delta_rho = |rho_161 - rho_121|.
```

The finest spatial pair is accepted only if, at every nonzero RF,

```text
e_J <= 0.005                 # 0.5% direct complex-current response

e_dJ <= 0.020               # 2% spectral first-difference response

Delta_rho <= max(2e-5, 0.10*rho_161)
```

The mixed absolute/relative residual rule prevents a numerically tiny one-mode floor from failing only because its relative percentage is ill-conditioned.

Failure does not permit threshold relaxation. It requires a finer grid ladder to be declared and run.

## Source-quadrature convergence

At the finest `161 x 121` grid, compare 13-point and 17-point Gauss-Legendre lateral source quadrature on the same fixed `[-3.5,+3.5] um` support.

At each nonzero RF require

```text
e_J(13->17) <= 0.0025        # 0.25% direct response

e_dJ(13->17) <= 0.010       # 1% spectral first-difference response

Delta_rho(13->17) <= max(1e-5, 0.05*rho_17)
```

Again, failure requires more source quadrature; the limits are not moved after inspection.

## First scientific readout after numerical acceptance

Only after all above gates pass may the first coplanar result be examined for:

```text
calibrated-kernel one-mode residual;
model-order extension if needed;
physical root-law consistency;
statistical rejection SNR if warranted.
```

No vertical-planar subtraction is used as a same-physics control. Any raw phase relative to the frozen Paper-01 target is cross-architecture scale only.

## Scope boundary

```text
second-family numerical output = not yet read at lock time
Stage A fixed-field only
science_interpretation_ready = false
Paper 03 standalone GO = false
```
