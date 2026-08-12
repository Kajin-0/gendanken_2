# Current Live State — Experiment 01

**Date:** 2026-08-11  
**Status:** anonymous Rev. 8 manuscript + adversarial hardening.  
**Priority:** unresolved; no novelty claim.

This is the current state pointer. Historical state files and older manuscript snapshots must not override it.

## 1. Canonical manuscript

The current approved manuscript baseline is the anonymous **26-page Rev. 8**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 8 was first judged against the established Rev. 7 preservation baseline in PR #13. Only after the manuscript-preservation and privacy gates passed was it made canonical.

Exact source:

```text
MANUSCRIPT_REV8_ANON_2026-08-11.tex
SHA-256 = 28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9
bytes = 81816
lines = 1023
compiled pages = 26
sections = 12
subsections = 18
bibliography items = 19
equation environments = 107
author/PDF metadata = Anonymous
```

Hash-verified recovery uses seven Rev. 8 snapshot parts under `manuscript_history/` and `python tools/extract_manuscript_baseline.py`.

Rev. 7, Rev. 6, Rev. 5, Rev. 4, Rev. 3, and `MANUSCRIPT_DRAFT.*` remain historical provenance only.

## 2. Current paper hierarchy

```text
spectral wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial first differences
-> four-color one-mode closure in multiplier q
-> branch-controlled continuous exponent gamma
-> if rank one fails: six-color Hankel rank-at-most-two determinant test
-> if rank two passes: recurrence-parameter resolution / conditioning
-> branch-free RF root invariants where available
-> branch/permutation-controlled physical root laws
-> higher ordinary finite rank if needed
-> mechanism assignment only after ordinary alternatives are excluded
```

The central one-mode terminal-current null remains

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).
```

For the six-color rung, the unconditional rank-at-most-two null is the `3x3` Hankel determinant `det(H)=0`. The adjacent-minor witness

```math
W_m=d_md_{m+2}-d_{m+1}^2=ab(q_1q_2)^m(q_1-q_2)^2
```

remains useful only after the model-order test and appropriate nondegeneracy checks. The old scalar closure `W1^2=W0W2` is not a general model-order null because it equals `-d2 det(H)`.

The four-color multiplier null is branch-independent. Physical inversion is not: `q=e^{-gamma h}` admits spatial-log aliases and therefore requires independent branch control.

## 3. Rev. 8 adversarial corrections — canonical

### Review discipline

Adversarial reviews are **attack vectors, not authority**. Independently verify the mathematical premise, physical regime, numerics, and scholarship before accepting, narrowing, rejecting, or marking an objection out of scope.

### Correct rank-two model-order null

The Rev. 7 six-color minor closure had a genuine blind component:

```math
W_1^2-W_0W_2=-d_2 det(H).
```

Therefore sequences with `d2=0` could satisfy the old scalar closure even at Hankel rank three. Rev. 8 replaces the unconditional model-order test by `det(H)=0` and adds the corresponding covariance-aware complex residual before parameter recovery.

Operational order:

```text
rank one rejected
-> rank at most two tested
-> rank-two parameters resolved
-> physical law tested
```

### Corrected weighting-field baseline

For the current finite-kernel transport model, a 1% linear weighting-field variation gives approximately:

```text
100 MHz -> 0.002947 deg
500 MHz -> 0.012140 deg
1 GHz   -> 0.010007 deg
```

The variations that place the false phase at 10% of the worked gradient target are approximately `0.757% / 0.881% / 1.961%`. The older prose values were stale; the referee's simple rescale of those stale values was not adopted.

### Differential recombination verification

The graded low-injection recombination correction remains about `3.8e-8 / 1.85e-7 / 3.45e-7 degree` at 100 / 500 / 1000 MHz. It is now checked by subtracting independently solved graded and matched-homogeneous cases in both finite-difference and adaptive-shooting implementations. The differential results agree within about `3e-9 degree` across tested environments. The coarser `1e-5 degree` absolute solver comparison is not claimed as validation of this tiny subtraction.

### HgCdTe force and DOS boundary

The electron-affinity relation anchors the composition-induced conduction-band force term only. It does not determine the self-consistent electrostatic field or total device drift. The worked calculation therefore remains a conditional composition-band-edge stress.

Under `m* proportional to Eg`, the DOS velocity is significant: `|v_DOS|/v_field ~= 8.8--18.3%`. The `alpha_DOS` sweep changes the 100-MHz closure from about `-0.01861 degree` at `alpha=0` to `-0.02349 degree` at `alpha=1.5`; the headline `alpha=1` result is `-0.02202 degree`.

### Two-carrier DC degeneracy

For nearly lossless electron-hole transport, integrated DC Shockley--Ramo path dependence can cancel, making the total DC sequence nearly depth-independent. Species-specific tracking can therefore require two or more nonzero RF frequencies even though the general recombining two-root theory remains valid.

Detailed Rev. 8 records:

```text
REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV8_PRESERVATION_REPORT_2026-08-11.md
numerics/rev8_review_regression.py
```

## 4. Earlier Rev. 4/5/6/7 corrections remain mandatory

Rev. 8 retains all prior hardening, especially:

```text
spatial-log aliasing / anti-alias bounds
known-unequal-spacing candidate-root language
singular s=kappa=0 weighting-field degree increase
low-RF q_weight=1 versus q_transport->1 mode coalescence
108.6 / 81.2 / 70.5 dB optimistic equal-mode separation scale
42.4 / 28.7 / 23.2 dB five-color annihilation penalty
branch-free finite-boundary multiplier-product prerequisite
two-root branch/permutation discipline
confluent q->1 DC limit
single-log complex closure statistic
same-optics baseline covariance
complex channel calibration and nonaffine source-coordinate tolerance
explicit HgCdTe transport and semi-infinite entrance prescription
rank-at-most-two precision plus the Rev. 8 Hankel-determinant model-order correction
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

The DOS/effective-mass contribution is a material-model uncertainty: in the retained reduced prescription it is about 8.8--18.3% of the field-driven velocity, and removing it changes the worked closure by roughly 15%.

The same-optics homogeneous subtraction remains part of the covariance budget; its nominal phase is about 17.3--19.8% of the quoted excess over 100 MHz--1 GHz and its uncertainty must be modeled rather than assumed zero.

The nonaffine-coordinate requirement remains about 4.5 nm RMS. The independent irregular spectral-phase stress remains about `1.88e-4 degree` at 100 MHz and `1.71e-3 degree` at 1 GHz. These are design requirements, not demonstrated calibration performance.

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
100 MHz -> -0.008841 deg = 0.402 x current Rev. 8 1-D gradient target
500 MHz -> -0.045827 deg = 0.431 x target
1 GHz   -> -0.095513 deg = 0.492 x target
```

Therefore `four-color failure != transport-gradient identification`. The geometry result is **CHECKED / CONDITIONAL**, not a calibrated detector simulation or theorem for arbitrary geometry.

## 7. Priority boundary — submission blocker

Priority remains **OPEN / UNPROVEN**. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before any submission-level novelty/priority claim. The broader OED literature is now represented more accurately, but related-paper searches and negative searches are not novelty evidence.

## 8. Current limitation and next decisive work

The central algebra has survived repeated hostile review under its stated hypotheses. The main remaining scientific question is now:

> **Does the hierarchy retain useful discriminating power when several ordinary departures coexist in one physically plausible detector?**

The next high-value attack is therefore one **self-consistent combined-physics synthetic detector challenge**, ideally including realistic electrostatics/Poisson, drift-diffusion with diffusion, finite geometry/weighting field, and more than one ordinary carrier/state contribution as appropriate. Its synthetic spectral/RF currents should be analyzed **blindly** through the same hierarchy.

The purpose is not to add another abstract theorem. It is to determine whether the practical sequence

```text
rank 1
-> rank 2 if resolved
-> parameter resolution
-> physical-law discrimination
-> higher ordinary finite rank if needed
```

retains useful discriminating power before the available color count becomes insufficient.

Separate open fronts are:

1. experimental/calibration architecture for the extreme residual depth/phase requirements;
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
7. `REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
9. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
10. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;
9. `PAPER_CLAIM_LEDGER.md` and newer claim-ledger addenda;
10. the exact extracted manuscript source when manuscript work is required.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
