# Paper 03 Stage-B blind six-channel analysis lock

**Date:** 2026-08-18  
**Status:** **PREDECLARED FINAL GENERIC STAGE-B BLIND GATE / NON-CLAIM**

## 1. Purpose

This is the B2 gate required by `PAPER03_COMBINED_PHYSICS_CHALLENGE_2026-08-17.md` and the minimum Stage-B milestone in `PAPER03_STAGEB_MODEL_SPEC_2026-08-17.md`.

It is deliberately narrow. It asks whether six calibrated spectral channels generated from the converged generic self-consistent semiconductor operating state can be analyzed through the Paper-03 hierarchy **without exposing the self-consistent field, carrier density, contact labels, or generating parameters to the blind analysis**.

No HgCdTe material claim is made. The operating-state parameter set remains the explicit synthetic validation case.

## 2. Required upstream gate

The workflow must first execute the unchanged refined Stage-B mesh / weighting / reciprocity validation under

```text
PAPER03_STAGEB_MESH_WEIGHTING_RECIPROCITY_LOCK_2026-08-17.md
PAPER03_STAGEB_MESH_REFINEMENT_LOCK_2026-08-18.md
```

and must abort before the blind result is accepted unless the frozen `51x39 -> 61x47` convergence pair and all weighting/Ramo/forward-backward checks pass.

No Stage-B blind result may be promoted from a numerically rejected operating state.

## 3. Forward structures

Generate two synthetic structures with the same declared semiconductor parameters:

```text
finite geometry: selected top contact fraction = 0.75
same-physics planar reference: selected top contact fraction = 1.00
```

Both retain

```text
W = 16 um
L = 7.6 um
T = 100 K
eps_r = 12
mu_n = 0.50 m^2/(V s)
N_D = 1e19 m^-3
built-in selected-top offset = -10 mV
external finite bias = +30 mV
bottom full reservoir contact
uncontacted top / sidewalls insulating where applicable
D_n = mu_n kT/q
```

The finite structure is the Stage-B test object. The full-top structure is a same-physics / same-optics reference, not a claim that either structure represents a named material device.

## 4. Spectral source calibration

Use the same six optical depth kernels already frozen for the Paper-03 program, with nominal mean-depth coordinates

```text
2.0, 2.5, 3.0, 3.5, 4.0, 4.5 um.
```

At each Stage-B mesh, sample each calibrated depth kernel on the cell-center z grid and normalize its discrete depth weights exactly. Use one common centered lateral Gaussian source envelope

```text
sigma_x = 2.0 um
support |x| <= 3.5 um
```

for all six channels. Normalize every full 2-D source distribution to unit total injected carrier number. The source normalization may set only an overall linear amplitude; it may not alter spectral shape after the result is inspected.

The blind analyzer is given the **actual discrete calibrated depth weights** used at its mesh, not an idealized translated-kernel surrogate.

## 5. RF observable

Use the selected-electrode Shockley-Ramo response at

```text
0, 100 MHz, 500 MHz, 1 GHz.
```

For each frequency solve the frozen-field backward response with the independently assembled Stage-B generator and Ramo source. The six complex currents are the source-weighted responses.

Forward-only fields, carrier densities, generator entries, contact absorption rates, and operating-state parameters remain outside the blind input object.

## 6. Blind input contract

The blind function may receive only

```text
six complex selected-terminal currents at each RF;
RF frequencies;
cell-center depth coordinate;
the six normalized calibrated depth-kernel weights;
and the frozen measurement-noise / false-claim comparison convention.
```

It may not receive

```text
psi(x,z);
n(x,z);
physical electric field;
weighting potential array;
true mobility or diffusion coefficient;
contact fraction;
forward generator;
true recombination or transport labels;
or a finite/planar mechanism flag.
```

Forward diagnostics and blind outputs must be stored in separate result blocks.

## 7. Blind calibrated-kernel models

### One-mode null

Fit all six channels independently at each RF to

```math
J_m = A + B M_m(r),
```

where the moment is computed from the actual discrete calibrated depth weights,

```math
M_m(r)=\sum_j g_{mj}\exp[r(z_j-z_{ref})].
```

Profile complex `A,B` exactly and fit complex `r` with the same bounded multistart domain used by the Stage-A kernel-aware analysis:

```text
Re r in [-25,25] /um
Im r in [-15,15] /um.
```

Report contrast-normalized residual, fitted root, design conditioning, and predicted/residual channel vectors.

### Two-mode diagnostic

Fit

```math
J_m=A+B_1M_m(r_1)+B_2M_m(r_2)
```

using all six complex channels. This remains a flexible diagnostic extension, not a theorem that arbitrary-kernel rank two identifies a physical mechanism.

Report one/two-mode residual reduction, root separation, coefficient balance, and root sums. Do not physically interpret an unstable root set.

## 8. Blind-observable mesh convergence

Generate six-channel observables independently at

```text
51 x 39
61 x 47.
```

Before scientific interpretation require, at each RF:

```text
best complex-affine coarse->fine six-channel shape residual
    / fine six-channel contrast norm <= 0.02
```

and for nonzero RF

```text
absolute change in the historical raw four-color closure phase
    / |frozen transport target phase| <= 0.02.
```

The raw four-color phase is only a historical comparison coordinate because the optical kernels are not exact translations; the physical one-mode null remains the calibrated-kernel fit.

If either unchanged 2% observable-convergence threshold fails, the Stage-B blind gate is numerically unresolved and must be refined rather than re-thresholded.

## 9. Warning-before-claim precision convention

For each nonzero RF use exactly the established Paper-03 analytic convention:

```text
per-real/imag-quadrature Gaussian sigma
step = mean absolute adjacent-channel complex-current difference
SNR = 20 log10(step/sigma)
alpha = 0.002699796063260207
power target = 0.90
regular all-six one-mode residual dof = 6
```

Use the noncentral-chi-square required noncentrality already established by the Stage-A statistical implementation to calculate the **analytic** SNR needed to reject the calibrated-kernel one-mode null.

Compare only with the frozen false homogeneous-transport claim coordinates

```text
100 MHz = 96.1 dB
500 MHz = 82.3 dB
1 GHz = 76.7 dB.
```

This final generic Stage-B gate does **not** add a new expensive parametric bootstrap. The paper's finite-sample bootstrap claims remain the already-predeclared first-family and coplanar tests. Stage B is a self-consistent-forward-model validation layer; its new SNR result must be labeled analytic.

## 10. Two-root physical-law diagnostic

Fit the two-mode model on both Stage-B meshes. A fine-grid root set may be treated as numerically stable only if the permutation-minimized maximum root change from `51x39 -> 61x47`, divided by the largest root magnitude in the matched pair, is <= 0.05.

For a stable pair, define the root sum

```math
S_r(f)=r_1(f)+r_2(f).
```

A homogeneous scalar finite-boundary drift-diffusion model requires this sum to be real and RF independent.

Use the observed coarse/fine root-sum difference as the numerical uncertainty coordinate. A fine-grid imaginary root sum is declared incompatible with a real sum only if

```text
|Im S_r(f)| > 5 |S_r,fine(f)-S_r,coarse(f)|.
```

A pair of RF root sums is declared incompatible with RF independence only if

```text
|S_r(f_i)-S_r(f_j)|
  > 5 ( |S_r,fine(f_i)-S_r,coarse(f_i)|
       +|S_r,fine(f_j)-S_r,coarse(f_j)| ).
```

If root stability fails, the correct classification is higher-order / mechanism unresolved; do not force a physical root-law conclusion.

## 11. Predeclared scientific outcomes

### B2-A — self-consistent physics self-announces

The self-consistent finite structure produces an order-one transport-like spectral/RF deviation (maximum finite-minus-planar historical mimic fraction >= 0.5), while calibrated-kernel model inadequacy and/or a numerically stable physical-root-law violation becomes detectable below the frozen false-transport claim precision.

This is consistent with Paper-03 Outcome A.

### B2-B — hidden-risk Stage-B point

An order-one self-consistent finite-minus-planar deviation is present, but the self-consistent structure remains effectively compatible with the homogeneous low-dimensional interpretation through the frozen false-claim precision.

This is a genuine adverse result and must narrow the manuscript; it may not be tuned away.

### B2-C — small self-consistent confound

The generic synthetic Stage-B point has maximum finite-minus-planar historical mimic fraction < 0.5. This still validates the self-consistent forward/observable/blind-analysis machinery if all numerical and leakage gates pass, but it is not additional evidence that an order-one self-consistent confound self-announces. The standalone Paper-03 Outcome-A evidence then remains the already-predeclared broad Stage-A domain and materially different coplanar family.

### B2-D — conservative unresolved higher order

An order-one deviation is present and the one-mode model is rejected below false-claim precision, but two-mode roots are unstable or fail to support a unique mechanism-level interpretation.

This is a successful safety/falsification outcome and must be reported as mechanism unresolved.

## 12. Stage-B completion / Paper-03 effect

The generic Stage-B minimum milestone is satisfied only if

```text
refined operating-state / weighting / reciprocity gate passes;
six-channel observable convergence passes;
blind-analysis input contract is respected;
and the six-channel analysis executes deterministically with finite outputs.
```

If B2-A, B2-C, or B2-D is obtained, the self-consistent generic validation does not expose a hidden failure of the Paper-03 falsification logic. Combined with the already-checked broad first-family Outcome-A result, materially different coplanar topology, actionable bootstrap SNR margins, and focused prior-art boundary, this is sufficient to evaluate the predeclared standalone Paper-03 GO criteria.

If B2-B is obtained, standalone framing must be reconsidered before drafting is frozen.

`science_interpretation_ready` remains false until this gate is executed and the complete GO checklist is recorded.
