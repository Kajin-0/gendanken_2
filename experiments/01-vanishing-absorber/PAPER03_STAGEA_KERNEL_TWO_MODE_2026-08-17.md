# Paper 03 Stage-A Gate — Kernel-Aware Two-Mode Diagnostic

**Date:** 2026-08-17  
**Status:** **CHECKED MODEL-ORDER DIAGNOSTIC / NON-CLAIM**  
**Decision:** for the converged finite75 + depletion Stage-A response, one additional calibrated-kernel exponential mode reduces the deterministic channel mismatch to approximately the planar numerical/model floor. The fitted two-root set is grid-stable but fails the homogeneous scalar physical root-sum law. Therefore the geometry can be represented compactly without becoming a false ordinary homogeneous transport mechanism.

## 1. Model and scope

The diagnostic extension is

```math
J_m=A+B_1M_m(r_1)+B_2M_m(r_2),
```

with

```math
M_m(r)=\int g_m(z)e^{rz}\,dz.
```

All six calibrated optical channels are used.

This is **not** asserted to be an already-proven Paper-01 Rev. 9 arbitrary-kernel rank-two theorem. It is a model-order diagnostic extension.

Six complex channels provide 12 real data values. A regular distinct-root model contains 10 real parameters (`A,B1,B2,r1,r2` complex), leaving only two real residual degrees of freedom. Residual reduction alone is therefore insufficient; conditioning, root separation, grid stability, and physical root laws are required.

---

## 2. Authoritative workflow

```text
workflow = Paper 03 Stage A kernel-aware two-mode diagnostic
run      = 32063155600
job      = 95488868118
head     = 42785734d72a51e118127134f11b90c10a8b7c4b
conclusion = success
```

Artifact:

```text
name   = paper03-stageA-kernel-two-mode
id     = 9299001081
digest = sha256:3a3de4be4c3031a0e5c85cc9ca408f2c401f39814107f02bf2d46e6e3ce5d84a
```

The global/multistart nonlinear fit, exact synthetic regression, non-claim assertions, and artifact upload all passed.

---

## 3. Exact synthetic regression

A known six-channel two-mode signal with

```text
r1 = -3.0 + 0.7 i 1/um
r2 = +1.4 - 0.45 i 1/um
```

was recovered as

```text
r1 = -3.000000000000001 + 0.6999999999999984 i 1/um
r2 = +1.3999999999999586 - 0.4500000000001593 i 1/um
```

with

```text
max root error = 1.65e-13 1/um
contrast-normalized residual = 4.60e-16.
```

This verifies the implementation on a well-conditioned exact distinct-root construction. It does not guarantee identifiability for arbitrary noisy detector data.

---

## 4. Finite geometry: one mode versus two modes

At the refined 201x151 grid:

| RF | one-mode rho | two-mode rho | reduction |
|---:|---:|---:|---:|
| DC | 2.2949e-4 | 2.2528e-6 | 101.9x |
| 100 MHz | 2.3484e-4 | 2.3558e-6 | 99.7x |
| 500 MHz | 3.4852e-4 | 1.8387e-6 | 189.5x |
| 1 GHz | 6.4189e-4 | 2.3491e-6 | 273.2x |

The two-mode residual is therefore of order `2e-6`, comparable to the all-six planar one-mode floor (`~1.5e-6`).

This is strong evidence that, over these six calibrated kernels, the converged Stage-A finite-geometry response is **approximately low order** rather than an arbitrary high-rank channel distortion.

It is not yet evidence that the two fitted roots are microscopic transport roots.

---

## 5. Grid stability of the fitted root set

The two-root set was fit independently at 161x121 and 201x151. Root matching for the stability diagnostic is permutation-invariant.

| RF | max root change (1/um) | max change / largest root magnitude | rho 161 | rho 201 |
|---:|---:|---:|---:|---:|
| DC | 1.065e-3 | 1.632e-2 | 2.2551e-6 | 2.2528e-6 |
| 100 MHz | 2.995e-3 | 1.323e-2 | 2.3587e-6 | 2.3558e-6 |
| 500 MHz | 8.218e-4 | 6.239e-5 | 1.8126e-6 | 1.8387e-6 |
| 1 GHz | 8.307e-4 | 6.552e-5 | 2.2183e-6 | 2.3491e-6 |

The fitted set is therefore numerically stable under this grid refinement, especially at 500 MHz and 1 GHz.

---

## 6. Fitted roots and conditioning

### 201x151 finite75 + depletion

| RF | r1 (1/um) | r2 (1/um) | separation | profile cond. | smaller/larger profiled amplitude |
|---:|---:|---:|---:|---:|---:|
| DC | -0.04468 - 0.000002i | +0.06436 - 0.000002i | 0.1090 | 2.63e3 | 0.754 |
| 100 MHz | +0.00247 + 0.04114i | +0.06214 + 0.21767i | 0.1863 | 1.27e3 | 0.0150 |
| 500 MHz | -0.29573 + 13.16779i | +0.01085 + 0.14217i | 13.0292 | 2.70e2 | 0.269 |
| 1 GHz | -0.04185 + 12.67762i | +0.00586 + 0.26739i | 12.4103 | 72.3 | 0.910 |

The low-RF fits are more ill-conditioned, particularly at DC, and the secondary profiled amplitude at 100 MHz is only about 1.5% of the larger amplitude. These facts must remain part of any later statistical interpretation.

At 500 MHz and 1 GHz the two modes are well separated in the fitted mathematical parameterization and the profile conditioning is substantially better.

---

## 7. Homogeneous scalar physical-root law fails

For a homogeneous scalar finite-boundary drift-diffusion operator under the same root convention, the two spatial roots must obey

```math
r_1+r_2=-w/D,
```

so their sum must be **real and RF-independent**.

For the 201x151 finite fit:

```text
DC:
  r1+r2 = +0.019686 - 0.000004 i 1/um

100 MHz:
  r1+r2 = +0.064608 + 0.258811 i 1/um

500 MHz:
  r1+r2 = -0.284871 + 13.309964 i 1/um

1 GHz:
  r1+r2 = -0.035999 + 12.945011 i 1/um
```

The violation is qualitative, not marginal. The sum develops a large imaginary part and changes strongly with RF.

Because root sum is permutation invariant, swapping the two fitted roots cannot repair this failure.

No microscopic `D`, `w`, or recombination coefficient should therefore be extracted from these effective two-mode roots.

---

## 8. Planar control exposes overfitting behavior

The planar response already has an all-six one-mode residual only around `1.5e-6`. A two-mode fit can reduce that residual further to `~2e-9 -- 1e-8`, but its second profiled mode amplitude is only about `1e-19` to `1e-23` of the dominant mode and the DC profile condition number reaches `~4e7`.

That is the expected warning for a needlessly flexible second mode: residual reduction alone can overfit a response that is already one-mode to the numerical/model floor.

The finite detector differs materially:

```text
one-mode mismatch is ~1e2--4e2 above the planar floor;
two-mode residual falls to ~the planar floor;
second profiled amplitude is non-negligible in the finite fit;
the fitted root set is stable under grid refinement;
but the physical homogeneous root law then fails.
```

This combination is substantially stronger than relying on a raw rank-two residual alone.

---

## 9. Current Stage-A classification

For the tested finite75 + depletion coordinate with diffusion and infinite lifetime:

```text
calibrated-kernel one-mode model
-> numerically resolved failure

calibrated-kernel two-mode diagnostic
-> describes six-channel response to near planar-floor residual
-> root set stable under grid refinement

homogeneous scalar physical root law
-> fails strongly across RF

therefore
-> lower-dimensional homogeneous mechanism rejected;
-> ordinary multidimensional geometry/nonuniform transport remains required.
```

This is the kernel-aware analogue of the earlier historical raw-Hankel rescue.

It is consistent with a candidate **Outcome A: geometry self-announces**, but Outcome A is not yet promoted to a Paper-03 result because statistical detectability, broad parameter-domain survival, a second geometry family, and Stage-B self-consistent semiconductor validation remain open.

---

## 10. Next decisive gate

The next question is quantitative detectability:

> At what raw-current measurement SNR would the calibrated-kernel one-mode residual be rejected with a declared false-alarm probability and power, and is that SNR lower than the frozen transport-claim SNR?

The deterministic nonlinear residual must be converted into a statistically calibrated model-rejection threshold. A local noncentral-chi-square approximation may be used as an analytic first pass only if its regularity assumptions are stated; it should then be checked by a null-constrained parametric bootstrap because nonlinear root fitting can become nonregular near coalescence or weak mode contrast.

`science_interpretation_ready` remains false.