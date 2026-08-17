# Paper 02 — Current State Rev. 4

**Date:** 2026-08-16  
**Status:** **INFERENTIAL NUMERICAL CONVERGENCE CHECKED / REV. 3 MANUSCRIPT REMAINS FROZEN / REV. 4 MANUSCRIPT DEVELOPMENT AUTHORIZED**  
**Supersedes for navigation:** `PAPER02_CURRENT_STATE_REV3_2026-08-15.md`  
**Preservation rule:** older Paper-02 state/result files remain provenance and must not be deleted.

## 1. What changed at this checkpoint

The previous state recorded a coarse/fine convergence test inherited from the original geometry stress calculation. That check acted primarily on the raw four-color closure phase and changed several numerical controls together. It was adequate for early model hardening but not for the current manuscript's nonlinear material-attribution result.

Paper 02 now has a stricter executable convergence gate on the **actual inferential chain**. The gate independently refines:

1. the 2-D electrostatic / Shockley-Ramo weighting-potential mesh;
2. the source and optical-kernel quadrature;
3. the deterministic trajectory integration step.

The corrected workflow run completed successfully and reported

```text
overall_pass = true
status = CHECKED numerical convergence gate passed
```

Workflow evidence:

```text
run      31948607702
job      95168474631
artifact paper02-inference-convergence
id       9264012168
SHA-256 ac9c9ade5e658fedd6ff846ee869dcc25d5bb0e4d85dd26a9657e6cf3dfaf275
```

The immediately preceding run completed all seven expensive numerical configurations but crashed in the reporting layer because `D_low` was mistakenly parsed as a frequency label. That run produced **no scientific verdict**. The failure is preserved in repository/Actions provenance and was repaired additively by `numerics/paper02_inference_convergence_runner.py` before rerunning the identical scientific gate.

---

## 2. Numerical configurations

Shared baseline:

```text
field mesh       nx=121, nz=91
source quadrature nx_src=13, nz_src=41
trajectory step  ds=0.020 um
```

Independent refinements:

```text
field mesh:        (81,61) -> (121,91) -> (161,121)
source quadrature: (9,31)  -> (13,41)  -> (17,61)
trajectory step:   0.035   -> 0.020    -> 0.0125 um
```

Seven unique configurations were solved because all three axes share the same baseline.

---

## 3. Predeclared gate

The decision was declared before the successful run. Baseline-to-fine changes had to satisfy:

```text
probe-frequency D_eff       <= 2% relative
probe-frequency w_eff       <= 0.5% relative
low-band D                   <= 2% relative
low-band w                   <= 0.5% relative
1-GHz law residual           <= 0.002 absolute change
one-mode kernel fit residual <= 2e-5 absolute change
upstream point D change      <= 1% of finite-kernel D100 scale
inside-depletion point D     <= 2% relative
DC Ramo identity error       <= 1e-10
collection fraction          >= 0.999
```

Positive-`D` sign stability was also required for the finite-kernel 100/500/1000-MHz inversions and the inside-depletion point-source positive control.

No tolerance was loosened after seeing the result.

---

## 4. Field-mesh convergence — limiting numerical coordinate

The field mesh is the dominant numerical uncertainty of the three tested axes.

For the finite-kernel same-frequency inverse:

```text
                coarse          baseline        fine             baseline->fine
D_eff 100 MHz   2.526515e-3     2.609795e-3     2.653537e-3      1.6484%
D_eff 500 MHz   2.467684e-3     2.548603e-3     2.591124e-3      1.6410%
D_eff 1 GHz     2.274809e-3     2.348945e-3     2.387949e-3      1.6334%
```

All are below the predeclared 2% gate, and the refinement change decreases relative to the coarse-to-baseline step (~3.16–3.19%).

The inferred drift scale is substantially more stable:

```text
w_eff 100 MHz   baseline->fine 0.1802%
w_eff 500 MHz   baseline->fine 0.1758%
w_eff 1 GHz     baseline->fine 0.1630%
```

The low-band joint fit changes by

```text
D_low  1.6447%
w_low  0.1798%
```

The 100-MHz-anchored homogeneous-law residual at 1 GHz changes only

```text
1.7520e-4 absolute
```

and the maximum one-mode finite-kernel fit residual through 1 GHz changes

```text
3.3610e-6 absolute.
```

Thus the mesh controls the numerical precision of the absolute apparent-`D` value, but not the existence, sign, causal attribution, or finite-band survival of the effect.

---

## 5. Source/kernel quadrature convergence

Source and kernel quadrature is far below the limiting error scale.

Baseline-to-fine relative changes are

```text
D_eff 100 MHz   3.33e-5
D_eff 500 MHz   3.43e-5
D_eff 1 GHz     3.76e-5

w_eff 100 MHz   2.03e-6
w_eff 500 MHz   2.00e-6
w_eff 1 GHz     1.90e-6
```

The 1-GHz law residual changes by `1.23e-7` absolute and the maximum one-mode fit residual through 1 GHz by `8.67e-9`.

The causal point-source controls are independent of this quadrature axis by construction and remain unchanged.

---

## 6. Trajectory-step convergence

The deterministic path integration is likewise strongly converged at the current baseline.

Baseline-to-fine relative changes are

```text
D_eff 100 MHz   4.99e-6
D_eff 500 MHz   5.74e-6
D_eff 1 GHz     8.21e-6

w_eff 100 MHz   8.43e-7
w_eff 500 MHz   8.59e-7
w_eff 1 GHz     8.99e-7
```

The 1-GHz law residual changes by `6.77e-8` absolute and the one-mode fit residual by `1.47e-9`.

---

## 7. Causal split survives refinement

The important causal controls remain qualitatively and quantitatively distinct across the numerical refinements.

### Upstream point-source null

For the six nominal point-source coordinates outside the nonuniform region:

```text
baseline D_eff = 1.7350e-12 m^2/s
fine-mesh D_eff = 9.1736e-12 m^2/s
fine-step D_eff = 1.5125e-12 m^2/s
```

The small mesh sequence is not monotone around exact zero, but the values are numerical-null scale. The baseline-to-fine mesh change is only `2.80e-9` of the finite-kernel `D_eff(100 MHz)` scale under the gate's scale-aware metric, versus the allowed `1e-2`.

### Inside-depletion positive control

For point sources wholly inside the nonuniform region:

```text
coarse-mesh D_eff   = 4.875711e-3 m^2/s
baseline D_eff      = 4.871054e-3 m^2/s
fine-mesh D_eff     = 4.868700e-3 m^2/s
```

The baseline-to-fine mesh change is only `4.83e-4` relative and the positive sign is stable.

Therefore the finite-kernel effect remains separated from the upstream point-source null under numerical refinement.

---

## 8. Integrity checks

Every one of the seven configurations passed:

```text
collection fraction >= 0.999
DC Shockley-Ramo identity error <= 1e-10
all upstream point trajectories reached
all inside-depletion point trajectories reached
positive-D sign stability where required
```

The central configurations report unit collection and DC Ramo errors at or near machine precision (`~1.11e-16`).

---

## 9. Scientific consequence

The stronger conclusion now justified is:

> Within the declared deterministic surrogate, the positive apparent diffusion returned by the kernel-aware homogeneous inverse is numerically stable under independent refinement of the field mesh, optical/source quadrature, and trajectory step. The limiting tested numerical coordinate is the field mesh, which changes the absolute inferred diffusion by about 1.6% from the current baseline to the finer grid while preserving the sign, causal controls, one-mode fit quality, and finite-frequency law mismatch.

This does **not** establish experimental feasibility, calibration of a real detector, or uniqueness of the mechanism in an experiment.

The optical-kernel wording remains:

> theoretical wavelength-dependent generation kernels supplied exactly to the inverse

not an experimental calibration claim.

---

## 10. Manuscript consequence

`PAPER02_MANUSCRIPT_REV3_ANON_2026-08-15.tex` remains the frozen current manuscript.

The convergence blocker for Rev. 4 is now removed. A new

```text
PAPER02_MANUSCRIPT_REV4_ANON_2026-08-16.tex
```

may be generated from the exact frozen Rev. 3 source, but Rev. 3 must not be edited in place.

Rev. 4 must at minimum:

1. replace ambiguous uses of "calibrated kernels" with the exact theoretical-kernel scope;
2. incorporate this inferential convergence result and its declared tolerances;
3. convert the frozen kernel-method record into actual Supplemental Material content;
4. preserve the corrected same-frequency statistical ordering;
5. preserve version-of-record bibliography metadata rather than globally normalizing author spellings;
6. compile with regenerated figures/data and no unresolved references;
7. undergo a new hostile scientific review before the current manuscript pointer moves.

Paper 01 / anonymous Rev. 9 remains untouched.
