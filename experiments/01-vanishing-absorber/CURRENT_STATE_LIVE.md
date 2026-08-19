# Current Live State — Spectral-Transport Program

**Date:** 2026-08-17  
**Status:** Paper 01 preserved; Paper 02 merged/frozen; Paper 03 Stage A now supports candidate Outcome A at the nominal finite-geometry coordinate.  
**Priority:** broaden Paper 03 beyond the nominal geometry before any standalone-paper GO decision.

This is the current state pointer. Detailed prior Paper-01 state is preserved byte-for-byte as

```text
CURRENT_STATE_ARCHIVE_2026-08-11.md
```

Current portfolio numbering is controlled by root `PUBLICATION_ROADMAP_CURRENT.md`.

---

## 1. Portfolio lock

```text
Paper 01
spectral-depth Shockley--Ramo closure / model-order falsification hierarchy
-> canonical anonymous Rev. 9 preserved

Paper 02
apparent diffusion / transport identifiability
-> Rev. 9 merged through PR #18
-> frozen except for material defect or submission-specific work

Paper 03
multidimensional geometry + combined ordinary detector physics
as a false spectral-transport signature
-> active draft research branch / PR #19

Paper 04 candidate
first-passage semigroup / timing-cumulant nulls
-> novelty gate before drafting
```

Historical geometry filenames containing `paper02` retain that old numbering for provenance only.

---

## 2. Paper 01 preservation and remaining blockers

The canonical Paper-01 source remains

```text
MANUSCRIPT_REV9_ANON_2026-08-11.tex
SHA-256 = df62813f764f051684ec52162095a5103296b71da1549b4c96829b0168fa1ce4
```

Do not rewrite it merely because Paper 03 advances.

Remaining submission fronts:

```text
closest-source priority audit;
calibration feasibility / covariance architecture;
combined-physics validation.
```

Paper 03 is the active attack on the third item.

---

## 3. Paper 03 governing records

Read in this order for current development:

```text
PAPER03_COMBINED_PHYSICS_CHALLENGE_2026-08-17.md
PAPER03_STAGEA_NUMERICAL_GATE_2026-08-17.md
PAPER03_STAGEA_RESOLVENT_GATE_2026-08-17.md
PAPER03_STAGEA_KERNEL_BLIND_GATE_2026-08-17.md
PAPER03_STAGEA_KERNEL_TWO_MODE_2026-08-17.md
PAPER03_STAGEA_RECOMBINATION_GATE_2026-08-17.md
PAPER03_STAGEA_STATISTICAL_PREDECLARATION_2026-08-17.md
PAPER03_STAGEA_STATISTICAL_BOOTSTRAP_2026-08-17.md
PAPER03_STAGEA_CROSS_FORMULATION_PREDECLARATION_2026-08-17.md
PAPER03_STAGEA_CROSS_FORMULATION_RESULT_2026-08-17.md
PAPER03_STAGEB_MODEL_SPEC_2026-08-17.md
```

The blind boundary remains mandatory: the analyzer may receive calibrated `J(lambda,omega)`, kernels/frequencies/noise information, but not hidden fields, true `D`, true lifetime, path histories, or generating-mechanism labels.

---

## 4. Stage-A forward solver status

### Brute-force stochastic paths

The Euler--Maruyama path implementation preserves the discrete endpoint Shockley--Ramo identity to approximately

```text
1.11e-16.
```

However, the predeclared particle-precision gate failed badly: even at 384 particles/source the independent-replica four-color phase half-spread was approximately `7.76 x` the entire frozen transport target rather than `<=0.05 x`.

Decision:

```text
Monte Carlo -> independent stochastic validation only
not the production estimator of the tiny nonlinear closure signal.
```

### Deterministic backward resolvent

For fixed-field drift-diffusion with optional exponential recombination,

```math
(\kappa+i\omega-L)H=L\phi_w.
```

A positive exponentially fitted nearest-neighbor Markov generator gives an exact discrete dc committor/Ramo identity.

The predeclared 2%-of-target spatial-grid gate passed on 121x91 -> 161x121 with worst phase change

```text
1.9941% of frozen target.
```

A post-gate 201x151 refinement strengthened this to

```text
1.1732%.
```

At 201x151, sparse linear residuals and the dc committor/Ramo identity remain at approximately `1e-13` and `1e-15` scales respectively.

This resolvent is the preferred Stage-A production formulation.

---

## 5. Correct calibrated-kernel one-mode test

The six HgCdTe generation kernels change shape with wavelength, so the exact one-mode model is

```math
J_m=A+B M_m(r),
```

```math
M_m(r)=\int g_m(z)e^{rz}\,dz.
```

The historical raw translated-kernel closure is retained only as a comparison diagnostic.

For the nominal Stage-A coordinate

```text
finite75 + depletion
D = 2.5e-3 m^2/s
tau = infinity
201 x 151
17-point lateral quadrature
```

the same-physics finite-minus-planar historical phase remains order one relative to the frozen transport target:

```text
100 MHz -> 0.728 x target
500 MHz -> 0.774 x target
1 GHz   -> 0.875 x target
```

The calibrated-kernel all-six one-mode residual is

```text
100 MHz -> 2.348e-4
500 MHz -> 3.485e-4
1 GHz   -> 6.419e-4
```

versus only about `1.5e-6` for the same-physics planar control.

Thus the surviving mismatch is not explained by the evolving optical-kernel shapes alone.

---

## 6. Kernel-aware model order and physical law

Diagnostic extension:

```math
J_m=A+B_1M_m(r_1)+B_2M_m(r_2).
```

This is a model-order diagnostic, not an asserted general arbitrary-kernel rank-two theorem.

For the 201x151 nominal finite case, two-mode residuals fall to approximately

```text
100 MHz -> 2.356e-6
500 MHz -> 1.839e-6
1 GHz   -> 2.349e-6
```

or approximately the planar one-mode floor, representing roughly `100x`, `190x`, and `273x` reductions from one mode.

The fitted root set is stable under 161x121 -> 201x151 refinement.

However, the homogeneous scalar finite-boundary law requires

```math
r_1+r_2=-w/D
```

to be real and RF-independent. The fitted root sums are instead approximately

```text
DC      -> +0.019686 - 0.000004 i 1/um
100 MHz -> +0.064608 + 0.258811 i 1/um
500 MHz -> -0.284871 + 13.309964 i 1/um
1 GHz   -> -0.035999 + 12.945011 i 1/um
```

so the compact two-mode mathematical description does **not** become a false ordinary homogeneous transport mechanism.

Current hierarchy:

```text
kernel-aware one mode -> reject
kernel-aware two-mode diagnostic -> compactly describes response
homogeneous physical root law -> reject strongly
```

---

## 7. Finite-recombination sensitivity

At

```text
D = 2.5e-3 m^2/s
tau = 5 ns
```

the spatial and lateral-quadrature numerical gates pass.

Same-physics finite-minus-planar mimic fractions become approximately

```text
100 MHz -> 0.745
500 MHz -> 0.795
1 GHz   -> 0.908
```

and the calibrated all-six finite one-mode residual remains roughly two to three orders of magnitude above the planar floor.

Thus this finite-lifetime sensitivity point does not rescue the one-mode interpretation.

---

## 8. Predeclared statistical gate — current strongest result

The statistical experiment was locked before execution:

```text
alpha = 0.002699796063260207
target power = 0.90
N_null = 4000 per SNR point
N_alt = 2000 per SNR point
SNR grid = analytic threshold + {-4,-2,0,+2,+4} dB
six complex channels
nonlinear kernel-aware one-mode refit for every realization
```

Noise convention:

```math
n_m=\sigma(\xi_R+i\xi_I),
```

with `sigma` the standard deviation of each real/imaginary current quadrature and

```math
SNR_{dB}=20\log_{10}(s_J/\sigma),
```

where `s_J` is the mean adjacent current-step magnitude.

Authoritative parallel RF run:

```text
run = 32065068757
head = ff3be81c695ab872607441b206adc0db47a2bba9
all three RF jobs = success
```

The predeclared early-warning condition passes at every RF:

| RF | lowest tested SNR with power >= 0.90 | frozen transport-claim SNR | conservative tested margin |
|---:|---:|---:|---:|
| 100 MHz | 76.545 dB | 96.1 dB | **19.55 dB** |
| 500 MHz | 73.137 dB | 82.3 dB | **9.16 dB** |
| 1 GHz | 65.892 dB | 76.7 dB | **10.81 dB** |

At 100 and 500 MHz the analytic-threshold bootstrap powers were `0.8945` and `0.8985`, so those points were correctly retained as failures and the next fixed `+2 dB` points were used. At 1 GHz the analytic point produced exactly `0.9000`, which passes the locked `>=0.90` rule; the next already-declared point gives `0.9975` power and still lies `8.81 dB` below the frozen transport-claim SNR.

No statistical threshold, sample count, SNR point, or pass rule was modified after seeing the result.

For the nominal Stage-A geometry this strongly supports candidate

```text
Outcome A: geometry self-announces before the mechanism-specific claim threshold.
```

It does **not** establish Outcome A over a broad domain yet.

---

## 9. Independent stochastic/resolvent cross-formulation result

The separately predeclared five-point cross-formulation check is formally

```text
OVERALL FAIL
```

and must remain recorded that way.

Reason: four `p_selected` comparisons saturated at `4000/4000` selected-contact trajectories, so the empirical Bernoulli SE was exactly zero while the fine deterministic probability differed from one by only `~1e-11` or less. The literal predeclared tolerance therefore became degenerate at the probability boundary.

Important independent signal result:

```text
35 / 35 declared direct Shockley--Ramo H components passed
maximum endpoint-Ramo path error = 1.11e-16
unresolved path fraction = 0.
```

Do not relabel the formal probability gate as a pass. If a nondegenerate fate-probability comparison becomes necessary, predeclare new source points and a binomial/exact-tail treatment separately.

---

## 10. Stage-B boundary

`PAPER03_STAGEB_MODEL_SPEC_2026-08-17.md` now reserves **self-consistent** for a coupled semiconductor dark/bias operating-state solve:

```text
Poisson + carrier continuity
-> converged operating state
-> dilute small-signal photocarrier transport
-> independent weighting-potential solve
-> blind spectral/RF analysis.
```

Required validation includes analytic Poisson limits, neutral/zero-space-charge limit, equilibrium current, steady-current conservation, three-mesh convergence, weighting/Ramo invariants, and backward-versus-forward small-signal agreement.

Stage B has not yet been implemented or demonstrated.

---

## 11. Current Paper-03 decision

For the nominal finite75 + depletion Stage-A coordinate:

```text
order-one geometry mimic -> YES
kernel-aware one-mode failure -> YES
compact kernel-aware two-mode description -> YES
homogeneous physical-root-law failure -> YES
predeclared early-warning bootstrap at all three RF -> YES
finite-recombination sensitivity survives -> YES
independent direct-H stochastic/resolvent agreement -> 35/35 checks
```

Therefore:

```text
candidate Outcome A at nominal Stage-A coordinate -> STRONGLY SUPPORTED
Paper 03 standalone GO -> NOT YET
science_interpretation_ready -> false
```

The missing standalone requirements are now concentrated:

```text
1. broad physically ordinary Stage-A geometry / diffusion / lifetime regime map;
2. materially different second geometry family;
3. Stage-B self-consistent semiconductor validation;
4. focused prior-art audit.
```

---

## 12. Immediate execution order

```text
1. predeclare and execute broad Stage-A regime-map screening;
2. refine predeclared boundary / worst / representative points on 201x151;
3. bootstrap only the predeclared selected screening points rather than every grid point;
4. test a materially different second geometry family;
5. implement and validate Stage B under PAPER03_STAGEB_MODEL_SPEC_2026-08-17.md;
6. perform focused prior-art audit before standalone manuscript drafting;
7. feed only defensible consequences back into Paper-01 submission readiness.
```

Do not launch another speculative manuscript branch while these Paper-03 gates remain unresolved.

---

## 13. Mandatory recovery order

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. root `PUBLICATION_ROADMAP_CURRENT.md`;
4. this file;
5. `PAPER03_COMBINED_PHYSICS_CHALLENGE_2026-08-17.md`;
6. Stage-A gate records listed in Section 3;
7. `PAPER03_STAGEB_MODEL_SPEC_2026-08-17.md`;
8. historical `REALISTIC_GEOMETRY_CLOSURE_STRESS.md` and `numerics/paper02_geometry_parameter_sweep.py` when regime-map provenance is needed;
9. canonical manuscript/preservation records only when Paper-01 manuscript work is required.

**Preserve first; integrate second; rewrite only when scientifically necessary.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
