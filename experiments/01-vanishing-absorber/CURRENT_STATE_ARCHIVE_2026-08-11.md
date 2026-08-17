# Current Live State — Experiment 01

**Date:** 2026-08-11  
**Status:** anonymous Rev. 9 manuscript + adversarial hardening.  
**Priority:** unresolved; no novelty claim.

This is the current state pointer. Historical state files and older manuscript snapshots must not override it.

## 1. Canonical manuscript

The current approved manuscript baseline is the anonymous **28-page Rev. 9**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 9 was first judged against the established Rev. 8 preservation baseline in PR #15. Only after the manuscript-preservation and privacy gates passed was it made canonical.

Exact source:

```text
MANUSCRIPT_REV9_ANON_2026-08-11.tex
SHA-256 = df62813f764f051684ec52162095a5103296b71da1549b4c96829b0168fa1ce4
bytes = 92749
lines = 1086
compiled pages = 28
sections = 12
subsections = 19
bibliography items = 21
equation environments = 116
author/PDF metadata = Anonymous
```

Hash-verified recovery uses seven Rev. 9 snapshot parts under `manuscript_history/` and `python tools/extract_manuscript_baseline.py`.

Rev. 8 and earlier revisions plus `MANUSCRIPT_DRAFT.*` remain historical provenance only.

## 2. Current paper hierarchy

```text
spectral wavelength
-> calibrated internal source coordinate / known generation kernels
-> Shockley-Ramo terminal-current observable
-> translated-kernel four-color closure OR kernel-aware one-mode consistency test
-> branch-controlled continuous exponent gamma
-> if rank one fails: six-color Hankel rank-at-most-two determinant test
-> if rank two passes: recurrence-parameter resolution / conditioning
-> classify distinct-root versus confluent/repeated-root rank two
-> branch-free RF root invariants where available
-> multiplicity/branch/permutation-controlled physical root laws
-> higher ordinary finite rank if needed
-> mechanism assignment only after ordinary alternatives are excluded
```

For rigid translated kernels, the central one-mode terminal-current null remains

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).
```

For independently calibrated arbitrary normalized generation kernels `g_m(z)`, define

```math
M_m(r)=\int g_m(z)e^{rz}\,dz,
```

so a homogeneous one-mode response has `J_m=A+B M_m(r)`. Four channels still overdetermine the same continuous root `r`; the geometric identity is the translated-kernel special case.

For the six-color rung, the unconditional rank-at-most-two null remains the `3x3` Hankel determinant `det(H)=0`. The Rev. 8 correction remains mandatory:

```math
W_1^2-W_0W_2=-d_2 det(H).
```

After rank two is accepted and recurrence parameters `S,P` are resolved, Rev. 9 requires

```math
Delta_q=S^2-4P.
```

- `Delta_q != 0`: distinct-root rank two.
- `Delta_q = 0` with nonzero rank-two contrast: confluent/repeated-root rank two with `d_m=(A+Bm)q^m`.

A repeated root is not automatically nonphysical; second-order physical transport can itself become confluent. Physical testing must therefore be multiplicity-aware.

The four-color multiplier null is branch-independent. Physical inversion is not: `q=e^{-gamma h}` admits spatial-log aliases and therefore requires independent branch control.

## 3. Rev. 9 adversarial corrections — canonical

### Review discipline

Adversarial reviews are **attack vectors, not authority**. Independently verify the mathematical premise, physical regime, numerics, and scholarship before accepting, narrowing, rejecting, or marking an objection out of scope.

### Confluent rank-two branch

Hankel rank two does not imply two distinct exponential roots. For

```math
d_m=(A+Bm)q^m,
```

one has `det(H)=0` and nonzero adjacent minors `W_m=-B^2q^(2m+2)`, while the recurrence discriminant vanishes. Rev. 9 inserts this classification before physical root interpretation.

### Rank-boundary statistics

At exact rank one all `2x2` cofactors of the `3x3` Hankel matrix vanish, so the first derivative of `det(H)` vanishes. First-order covariance calibration is therefore nonregular at that boundary. Use null-constrained Monte Carlo / parametric bootstrap when linearization is inadequate.

### Common depth-scale calibration

Closure/model-order testing and dimensional parameter extraction have separate calibration budgets. If the calibrated scale is `h_cal=c h`,

```math
D_cal=c^2D,
w_cal=cw,
kappa_cal=kappa.
```

Thus a 2% common scale error implies about 4% bias in `D` and 2% in `w` even if the closure null itself is unaffected.

### Known arbitrary generation kernels

The realistic experiment is no longer described as transport-only parameter-free when wavelength-dependent kernels evolve. Independently calibrated kernels enter through `M_m(r)`, and a common `r` must satisfy the kernel-aware four-channel consistency conditions. Raw geometric-closure failure without this correction rejects the combined transport+optical idealization.

### Shared composition nuisance

The same graded-HgCdTe composition profile `x(z)` controls both wavelength-to-depth/kernels and the modeled composition-induced band-edge force. A real inference must constrain that profile independently or propagate it jointly rather than treating those uncertainties as independent.

### HgCdTe interpretation refinements

The electron-affinity relation anchors the composition-induced conduction-band force term only. The source's quoted `67.1%` average partition and approximately `±1%` two-thirds comparison are tied to `0.15<x<0.45`; the worked profile reaches `x=0.55`, where the explicit relation is evaluated without extending the quoted validation range by assumption.

The local Peclet numbers are only about `0.48` per 0.5-um source step and `0.75` over the 0.79-um optical-kernel width. The high-Peclet local formula remains asymptotic intuition; the quantitative headline uses the full finite-diffusion boundary-value solve.

The inherited hot-to-cold calculation remains an independent deliberately strong two-state benchmark, not the same Rev. 9 HgCdTe realization.

### Prior-art boundary

Classical surface-photovoltage/diffusion-length and photodiode spectral-response work already used wavelength-dependent absorption/generation depth to infer or model carrier transport. The manuscript does not claim spectral-depth probing itself as new. The candidate distinction is the specific spectral-depth + Shockley-Ramo + finite-rank + cross-RF physical-law hierarchy.

### Free DC admissibility

Before RF overdetermination, the stated homogeneous downstream model already requires

```math
q(0)\in(0,1],\qquad D>0,\qquad kappa\ge0,
```

plus the assumed drift-direction sign.

Detailed Rev. 9 records:

```text
REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV9_PRESERVATION_REPORT_2026-08-11.md
PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md
numerics/rev9_review_regression.py
```

## 4. Earlier Rev. 4–8 corrections remain mandatory

Rev. 9 retains all prior hardening, especially:

```text
Shockley-Ramo terminal-current observable rather than first-passage-flux substitution
spatial-log aliasing / anti-alias bounds
known-unequal-spacing candidate-root language
singular s=kappa=0 weighting-field degree increase
low-RF q_weight=1 versus q_transport->1 mode coalescence
branch-free finite-boundary multiplier-product prerequisite
two-root branch/permutation discipline
confluent q->1 DC limit
single-log complex closure statistic
same-optics baseline covariance
complex channel calibration and nonaffine source-coordinate tolerance
explicit HgCdTe transport and semi-infinite entrance prescription
classical Prony / ESPRIT / matrix-pencil attribution
Rev. 8 full Hankel determinant rank-at-most-two correction
Rev. 8 weighting-field and differential-recombination numerical corrections
Rev. 8 DOS/effective-mass uncertainty and composition-force versus total-drift distinction
```

Do not regress to earlier unrestricted claims.

## 5. Current HgCdTe conditional baseline

For the illustrative 7.6 um / 300 K graded-HgCdTe stress:

```text
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
wavelengths ~ 2.134651, 2.215042, 2.301173, 2.393907 um
```

The current literature-anchored composition-band-edge force uses the 2025 electron-affinity relation and `xi_e~0.666--0.695`; this anchors that band-edge term, not the total self-consistent drift.

The finite-width gradient-sensitive four-color phase remains approximately:

```text
100 MHz -> -0.0220167 deg
250 MHz -> -0.0546244 deg
500 MHz -> -0.1064448 deg
1 GHz   -> -0.1942321 deg
```

The DOS/effective-mass contribution remains a material-model uncertainty: in the retained reduced prescription it is about 8.8--18.3% of the field-driven velocity, and removing it changes the worked closure by roughly 15%.

The same-optics homogeneous subtraction remains part of the covariance budget; its nominal phase is about 17.3--19.8% of the quoted excess over 100 MHz--1 GHz. That means the realistic HgCdTe experiment is conditional on independently constrained optical kernels/baseline, not a transport-only parameter-free null.

The nonaffine-coordinate requirement remains about 4.5 nm RMS. The independent irregular spectral-phase stress remains about `1.88e-4 degree` at 100 MHz and `1.71e-3 degree` at 1 GHz. These are design requirements, not demonstrated calibration performance. The common absolute depth scale is a separate requirement because it directly biases recovered `D` and `w`.

The graded 5-us-anchored differential-recombination sensitivity changes the closure by less than `4e-7 degree`; the dedicated cross-solver subtraction agrees within about `3e-9 degree` across tested environments.

## 6. Separate realistic-geometry hardening result

The finite-electrode/depletion calculation remains separately auditable in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
numerics/realistic_geometry_closure_stress.py
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
```

For the representative 75%-contact + 3 um depletion-like stress, the geometry/depletion excess over the planar same-optics baseline is approximately:

```text
100 MHz -> -0.008841 deg = 0.402 x current 1-D gradient target
500 MHz -> -0.045827 deg = 0.431 x target
1 GHz   -> -0.095513 deg = 0.492 x target
```

Therefore `four-color failure != transport-gradient identification`. The geometry result is **CHECKED / CONDITIONAL**, not a calibrated detector simulation or theorem for arbitrary geometry.

## 7. Priority boundary — submission blocker

Priority remains **OPEN / UNPROVEN**. The manuscript now explicitly concedes older spectral-depth transport probing, wavelength-dependent RF sensing, and classical finite-exponential/Hankel identification as prior art.

The exact closest 2024 graded-HgCdTe paper still requires a direct technical full-text comparison before any submission-level novelty/priority claim. Related-paper searches, metadata, and negative searches are not novelty evidence.

## 8. Current limitation and next decisive work

The central translated-kernel one-mode theorem and its generalized kernel-aware formulation have survived repeated hostile review under their stated hypotheses. The main remaining device-physics question is:

> **Does the hierarchy retain useful discriminating power when several ordinary departures coexist in one physically plausible detector?**

The next high-value attack is one **self-consistent combined-physics synthetic detector challenge**, ideally including realistic electrostatics/Poisson, drift-diffusion with diffusion, finite geometry/weighting field, realistic optical kernels, recombination, contacts, and multiple carrier/state contributions as appropriate. Synthetic spectral/RF currents should be generated independently of the closure model and analyzed **blindly** through the same hierarchy.

The hierarchy should be allowed to return:

```text
rank > 2
mechanism unresolved
```

That is a valid safe outcome rather than a failure of the validation.

Separate open fronts are:

1. experimental/calibration architecture for residual depth/phase, common depth scale, and kernel/composition requirements;
2. exact closest-source priority audit;
3. baseline optical/model covariance feasibility.

## 9. Mandatory recovery order

A new agent should read:

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. `MANUSCRIPT_CURRENT.md`;
4. `MANUSCRIPT_BASELINE.md`;
5. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
6. this file;
7. `REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md`;
9. `REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
10. earlier adversarial records and `PAPER_CLAIM_LEDGER.md` as historical context;
11. the exact extracted manuscript source when manuscript work is required.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
