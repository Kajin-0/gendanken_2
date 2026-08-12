# Current Live State — Experiment 01

**Date:** 2026-08-11  
**Status:** anonymous Rev. 7 manuscript + adversarial hardening.  
**Priority:** unresolved; no novelty claim.

This is the current state pointer. Historical state files and older manuscript snapshots must not override it.

## 1. Canonical manuscript

The current approved manuscript baseline is the anonymous **24-page Rev. 7**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 7 was first judged against the established Rev. 6 preservation baseline in PR #11. Only after the manuscript-preservation and privacy gates passed was it made canonical.

Exact source:

```text
MANUSCRIPT_REV7_ANON_2026-08-11.tex
SHA-256 = 9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8
bytes = 75182
lines = 963
compiled pages = 24
sections = 12
subsections = 18
bibliography items = 19
equation environments = 102
author/PDF metadata = Anonymous
```

Hash-verified recovery uses six Rev. 7 snapshot parts under `manuscript_history/` and `python tools/extract_manuscript_baseline.py`.

Rev. 6, Rev. 5, Rev. 4, Rev. 3, and `MANUSCRIPT_DRAFT.*` remain historical provenance only.

## 2. Current paper hierarchy

```text
spectral wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial first differences
-> four-color one-mode closure in multiplier q
-> branch-controlled continuous exponent gamma
-> six-color/higher finite-rank model-order tests when needed
-> rank-two parameter-resolution check
-> branch-free RF root invariants where available
-> branch/permutation-controlled physical root laws
-> mechanism assignment only after ordinary alternatives are excluded
```

The central one-mode terminal-current null remains

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).
```

The rank-two witness remains

```math
W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.
```

The four-color multiplier null is branch-independent. Physical inversion is not: `q=e^{-gamma h}` admits spatial-log aliases and therefore requires independent branch control.

## 3. Rev. 7 adversarial corrections — canonical

### Review discipline

Adversarial reviews are **attack vectors, not authority**. For every criticism: independently verify the mathematical premise, physical regime, numerics, and scholarship; then accept, narrow, reject, or mark out-of-scope. Do not alter a correct result merely because a referee states an objection strongly, and do not defend the manuscript reflexively when an objection is valid.

### Classical exponential-sum lineage

The one- and two-mode spatial identities belong to classical finite-exponential algebra. Rev. 7 explicitly cites Prony (1795), ESPRIT (1989), and the matrix-pencil method (1990). The manuscript does not claim those algebraic identities as new.

The candidate distinction is narrower:

```text
calibrated spectral generation depth
-> Shockley-Ramo terminal-current observable
-> spatial differencing
-> classical finite-exponential model-order tests
-> branch-controlled / branch-free RF physical root constraints
```

Priority remains unproven.

### Literature-anchored HgCdTe force

The headline HgCdTe stress no longer uses the free `xi=1` normalization. A 2025 electron-affinity relation gives

```math
chi(x)=5.32+0.45x-E_g(x,300 K),
```

so the modeled electron-driving band-edge gradient is

```math
E_drive^grad(z)=|(dE_g/dx-0.45) dx/dz|.
```

For the worked `x=0.55 -> 0.32` profile,

```math
xi_e=1-0.45/(dE_g/dx) \simeq 0.666--0.695.
```

The resulting finite-width gradient-sensitive closure excess is approximately:

```text
100 MHz -> -0.0220167 deg
500 MHz -> -0.1064448 deg
1 GHz   -> -0.1942321 deg
```

The former constant-`xi` calculations remain sensitivity stresses, not the current headline material baseline.

### Spatial recombination stress

A nonlinear microscopic Auger law can be linearized around an operating point into a differential small-signal recombination rate. The relevant graded-material question is therefore whether that differential rate varies enough with depth to mimic the closure.

Rev. 7 tests an intentionally steep profile anchored at `5 us`:

```math
tau_gr(z)=5 us exp[(E_g(z)-E_g(x=0.325))/(k_B T)].
```

With a transit-weighted matched homogeneous baseline, its additional closure shift is only about `3.8e-8 / 1.8e-7 / 3.5e-7 degree` at 100 / 500 / 1000 MHz in the specified model. This is **CHECKED / CONDITIONAL**, not a universal statement about high-injection, depleted, or arbitrary HgCdTe devices.

### Observation operator and statistics

The one-dimensional polynomial `E_w(z)` theory remains an exact effective axial surrogate. It is not a generic finite-pixel electrostatic theorem; real finite electrodes can produce both axial and lateral weighting structure.

The hierarchy is structural model-selection logic. Per-rung covariance statistics remain conditional, and reusing the same noisy data for model-order selection and physical-root tests requires selection-aware error control in a full experiment.

### Measurement architecture and propagated resources

Rev. 7 specifies a plausible architecture using one common RF reference, interleaved wavelength acquisition, optical-power/reference-photodiode monitoring, one coherent DUT receiver chain, repeated reference wavelengths, and calibration of the non-common high-curvature spectral residual rather than absolute path delay. This is an architecture, **not demonstrated feasibility**.

Key propagated scales are:

```text
conditioning optimum                         5.85 GHz
K_D at 100 / 500 / 1000 MHz                33.95 / 7.57 / 4.75
weighting-mode rank-two SNR                 108.6 / 81.2 / 70.5 dB
five-color annihilation penalty             42.4 / 28.7 / 23.2 dB
3-sigma current-step SNR                    90.9 / 82.9 / 77.1 / 71.4 dB (100/250/500/1000 MHz)
nonaffine coordinate RMS                    4.54 / 4.55 / 4.51 nm
irregular channel phase RMS                 1.88e-4 / 9.15e-4 / 1.71e-3 deg
1-D weighting change for <10% target        0.757% / 0.881% / 1.961%
same-optics homogeneous phase / excess      17.3% / 17.9% / 19.8%
```

Detailed Rev. 7 records:

```text
REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md
numerics/rev7_review_regression.py
```

## 4. Earlier Rev. 4/5 corrections remain mandatory

Rev. 6 retains all prior hardening, especially:

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
rank-at-most-two precision
```

Do not regress to earlier unrestricted claims.

## 5. Current HgCdTe conditional baseline

For the illustrative 7.6 um / 300 K graded-HgCdTe stress:

```text
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
wavelengths ~ 2.134651, 2.215042, 2.301173, 2.393907 um
```

The current literature-anchored electron-driving force uses the 2025 electron-affinity relation and `xi_e~0.666--0.695`, not the historical `xi=1` headline normalization.

The finite-width gradient-sensitive four-color phase is approximately:

```text
100 MHz -> -0.0220167 deg
250 MHz -> -0.0546244 deg
500 MHz -> -0.1064448 deg
1 GHz   -> -0.1942321 deg
```

These remain conditional theory stresses, not calibrated predictions for a named detector.

The same-optics homogeneous subtraction remains part of the covariance budget; its nominal phase is about **17.3--19.8%** of the quoted excess over 100 MHz--1 GHz and its uncertainty must be modeled rather than assumed zero.

The derived nonaffine-coordinate requirement is about **4.5 nm RMS**. The independent irregular spectral-phase stress is about **1.88e-4 degree at 100 MHz** (about 5.2 fs differential timing) and rises to `1.71e-3 degree` at 1 GHz. These are design requirements, not demonstrated calibration performance.

The graded 5-us-anchored differential-recombination sensitivity changes the closure by less than `4e-7 degree` over the stated RF range in the specified model.

## 6. Separate realistic-geometry hardening result

The finite-electrode/depletion calculation remains separately auditable in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
numerics/realistic_geometry_closure_stress.py
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
```

For the representative 75%-contact + 3 um depletion-like stress, the geometry/depletion excess over the planar same-optics baseline is approximately:

```text
100 MHz -> -0.008841 deg = 0.402 x current Rev. 7 1-D gradient target
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
7. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
9. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;
9. `PAPER_CLAIM_LEDGER.md` and newer claim-ledger addenda;
10. the exact extracted manuscript source when manuscript work is required.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
