# Paper 03 Stage-A Gate — Kernel-Aware Blind One-Mode Test

**Date:** 2026-08-17  
**Status:** **CHECKED NUMERICAL / MODEL-CONSISTENCY RESULT; NON-CLAIM**  
**Decision:** the finite-contact/depletion fixed-field Stage-A response retains a small but numerically resolved failure of the calibrated arbitrary-kernel one-mode model. The same-physics planar control is much closer to one mode. Statistical detectability and higher-order physical interpretation remain open.

## 1. Why this gate was required

The six inherited HgCdTe optical generation profiles are not exact rigid translations of one shape. Therefore the historical geometric first-difference closure is not the exact one-mode null for these channels.

Paper 01 Rev. 9 gives the appropriate calibrated-kernel model

```math
M_m(r)=\int g_m(z)e^{rz}\,dz,
```

```math
J_m=A+B M_m(r).
```

The blind analysis must therefore ask whether one common complex spatial exponent `r` can explain the calibrated channel currents after profiling the complex affine coefficients `A,B`.

Implementation:

```text
numerics/paper03_stageA_kernel_blind_gate.py
```

The forward generator remains Stage A fixed-field drift-diffusion. It is **not** a self-consistent semiconductor Poisson/drift-diffusion model.

---

## 2. Authoritative workflow

```text
workflow = Paper 03 Stage A kernel-aware blind gate
run      = 32062748418
job      = 95487570450
head     = b3258a6c4e74347c9dbfb2ce738aea2278877189
conclusion = success
```

All workflow steps passed: checkout, Python setup, numerical dependencies, kernel-aware development gate, regression/numerical assertions, and artifact upload.

Artifact:

```text
name   = paper03-stageA-kernel-blind-gate
id     = 9298748370
digest = sha256:e0d2b8353a529cf9c90b4d0edbb3ee444bdc22eea3e13a4d5b4574bffb0a1ebb
```

The generated record remains

```text
science_interpretation_ready = false
```

by construction.

---

## 3. Internal regression of the nonlinear kernel fit

Before applying the fit to the detector forward result, an exactly generated six-channel one-mode sequence was tested with

```text
true r = -3.0 + 0.7 i 1/um
```

The recovered value was

```text
fit r = -2.999999999999999 + 0.6999999999999997 i 1/um
```

with contrast-normalized residual

```text
9.7907e-17.
```

This verifies the implemented nonlinear moment fit on a known exact case. It does not establish global root uniqueness for arbitrary noisy data.

---

## 4. Numerical continuation and source quadrature

The full optical support is included in this gate, with absorbing-contact values supplied directly by the resolvent grid.

### Spatial-grid continuation

For the finite 75%-contact + depletion case, full-support 161x121 -> 201x151 changes the raw historical four-color phase by

| RF | 161x121 | 201x151 | change / frozen target |
|---:|---:|---:|---:|
| 100 MHz | -0.00582177 deg | -0.00595479 deg | 0.0111053 |
| 500 MHz | -0.03105355 deg | -0.03172817 deg | 0.0114873 |
| 1 GHz | -0.06866112 deg | -0.06996171 deg | 0.0117802 |

Worst change is therefore

```text
1.1780% of the frozen transport target,
```

consistent with the earlier post-gate refinement result.

### Lateral source quadrature

Before reading the 17-point result, the lateral 13 -> 17 point readiness gate was fixed at

```text
<= 0.5% of the frozen transport phase at every nonzero RF.
```

Observed changes were

| RF | change / frozen target |
|---:|---:|
| 100 MHz | 4.7924e-5 |
| 500 MHz | 4.6494e-5 |
| 1 GHz | 4.1642e-5 |

Worst:

```text
4.7924e-5 = 0.00479% of target,
```

so the predeclared 0.5% source-quadrature gate passes by more than two orders of magnitude.

---

## 5. Same-physics planar reference

The finite geometry and the planar reference use the same

```text
D = 2.5e-3 m^2/s,
tau = infinity,
201 x 151 grid,
17-point lateral source quadrature,
six calibrated HgCdTe kernels.
```

Only the geometry/electrostatic boundary construction differs.

The raw historical phase diagnostic is

| RF | finite75 + depletion | planar same physics | finite - planar | fraction of frozen transport target |
|---:|---:|---:|---:|---:|
| 100 MHz | -0.00595479 deg | +0.00276940 deg | -0.00872419 deg | 0.72835 |
| 500 MHz | -0.03172817 deg | +0.01372110 deg | -0.04544927 deg | 0.77391 |
| 1 GHz | -0.06996171 deg | +0.02665473 deg | -0.09661644 deg | 0.87511 |

Thus adding diffusion to the checked geometry stress does **not** make the order-one finite-minus-planar phase confound disappear. This remains a comparison coordinate only; the raw geometric closure is not the exact arbitrary-kernel null.

---

## 6. Kernel-aware one-mode residual

For each RF independently, complex `A` and `B` are profiled linearly and complex `r` is fitted by bounded multistart nonlinear least squares.

Residual is reported as

```math
rho = ||J-J_fit||_2 / ||J-mean(J)||_2.
```

This is a deterministic model-mismatch coordinate. It is **not yet a p-value, sigma level, or experimental SNR threshold**.

### Central calibrated quartet: depths 2.5, 3.0, 3.5, 4.0 um

| RF | finite75 + depletion rho | planar rho | finite / planar |
|---:|---:|---:|---:|
| DC | 7.6086e-5 | 3.3963e-9 | 2.24e4 |
| 100 MHz | 7.7265e-5 | 3.9312e-9 | 1.97e4 |
| 500 MHz | 1.0420e-4 | 3.9045e-9 | 2.67e4 |
| 1 GHz | 1.8177e-4 | 3.8364e-9 | 4.74e4 |

For four complex channels, the affine one-mode model has two real residual degrees of freedom after fitting complex `A,B,r`, assuming the local parameterization is regular.

### All six calibrated channels

| RF | finite75 + depletion rho | planar rho | finite / planar |
|---:|---:|---:|---:|
| DC | 2.2949e-4 | 1.5977e-6 | 143.6 |
| 100 MHz | 2.3484e-4 | 1.5965e-6 | 147.1 |
| 500 MHz | 3.4852e-4 | 1.5652e-6 | 222.7 |
| 1 GHz | 6.4189e-4 | 1.4691e-6 | 436.9 |

For six complex channels, the local regular one-mode model leaves six real residual degrees of freedom.

The much smaller planar residual is important: the finite-detector residual is not explained merely by using evolving optical kernels in place of rigid translated kernels.

The all-six planar floor is larger than the central-quartet floor. It remains small relative to the finite case but should be treated as a numerical/model floor until its source is separately characterized.

---

## 7. Fitted exponent caution

The nonlinear fit also returns a best mathematical complex exponent `r`. Those fitted values are stored in the artifact, but they are **not yet physical transport roots**.

Reasons:

```text
spatial-log/branch control has not been applied;
physical cross-RF root laws have not been imposed;
DC can be ill-conditioned near a nearly constant exponential mode;
the finite geometry is known not to satisfy the one-dimensional homogeneous forward hypotheses;
statistical uncertainty is not yet calibrated.
```

Accordingly, do not infer `D`, drift, or recombination from these Stage-A fitted roots.

---

## 8. Scientific consequence at this gate

The checked statement is narrower than a Paper-03 claim:

```text
After using the correct calibrated arbitrary-kernel one-mode model,
a numerically converged finite-contact/depletion Stage-A forward response
still has a reproducible one-mode model mismatch far above the
same-physics planar numerical/model floor.
```

What is **not** yet known is whether that mismatch

```text
is experimentally resolvable before a false transport claim;
is adequately represented by one additional spatial mode;
requires still higher spatial order;
passes or fails physically constrained cross-RF root laws;
survives self-consistent semiconductor electrostatics and finite recombination.
```

Therefore this result supports continued Paper-03 development but does not yet satisfy standalone-paper GO criteria.

---

## 9. Immediate next gate

The next model-order question must also respect the calibrated kernels.

A natural diagnostic extension is

```math
J_m=A+B_1M_m(r_1)+B_2M_m(r_2),
```

fitted to all six channels.

This is **not** to be described as an already-proven Rev. 9 arbitrary-kernel rank-two theorem. It is a forward-model diagnostic extension used to ask whether one additional exponential spatial component explains the observed deterministic mismatch.

Because six complex channels supply only two real residual degrees of freedom after fitting complex `A,B_1,B_2,r_1,r_2`, the fit is flexible and must be accompanied by

```text
multistart/root-permutation handling;
conditioning and root-separation diagnostics;
known synthetic two-mode regression;
grid-stability checks;
and cross-RF physical-law tests before mechanism interpretation.
```

After model order is characterized, statistical calibration should convert the one-mode residual into an observable noise/SNR threshold rather than comparing bare residual magnitudes.

`science_interpretation_ready` remains false.