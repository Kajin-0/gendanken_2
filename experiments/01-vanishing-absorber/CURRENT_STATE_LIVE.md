# Current Live State — Experiment 01

**Date:** 2026-08-11  
**Status:** anonymous Rev. 6 manuscript + adversarial hardening.  
**Priority:** unresolved; no novelty claim.

This is the current state pointer. Historical state files and older manuscript snapshots must not override it.

## 1. Canonical manuscript

The current approved manuscript baseline is the anonymous **22-page Rev. 6**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 6 was first judged against the established Rev. 5 preservation baseline. Only after the manuscript-preservation and privacy gates passed was it made canonical.

Exact source:

```text
MANUSCRIPT_REV6_ANON_2026-08-11.tex
SHA-256 = 2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4
bytes = 67837
lines = 924
compiled pages = 22
sections = 12
subsections = 18
bibliography items = 13
equation environments = 99
author/PDF metadata = Anonymous
```

Hash-verified recovery uses six Rev. 6 snapshot parts under `manuscript_history/` and `python tools/extract_manuscript_baseline.py`.

Rev. 5, Rev. 4, Rev. 3, and `MANUSCRIPT_DRAFT.*` remain historical provenance only.

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

## 3. Rev. 6 adversarial corrections — canonical

### Rank detection is not parameter resolution

Rev. 6 explicitly separates:

```text
rank-two detection
-> rank-two parameter resolution
-> physical root-law discrimination
```

For the recurrence product

```math
P=q_1q_2=W_1/W_0,
```

the first-order perturbation is

```math
delta P=(delta W_1-P delta W_0)/W_0,
```

with the proper-complex variance carrying the shared-minor covariance. In the deliberately optimistic independent equal-significance limit,

```math
sigma_P/|P| ~ sqrt(2)/Z.
```

Thus `Z=3` on both minors still permits about **47.1%** relative product uncertainty. About `Z=14.1` per minor is needed for 10% product precision in that simplified limit. The recurrence sum `S=q_1+q_2` is also propagated, and individual roots become additionally ill-conditioned as `S^2-4P -> 0`.

**Mandatory interpretation:** a statistically resolved second mode does not imply that the multiplier product, sum, or individual roots are precise enough for a physical-law test.

### Algebraic branch immunity is not statistical robustness

The Rev. 5 finite-boundary branch-free constraint remains:

```math
q_+q_-=e^{-wh/D}\in\mathbb R_{>0},
```

with RF independence required before logarithmic root recovery. Rev. 6 adds the explicit caveat that this algebraic branch immunity does not make `W_1/W_0` statistically robust when the underlying Hankel minors are small.

### One-dimensional weighting field is an effective surrogate

The Section 6 polynomial `E_w(z)` construction is an **effective one-dimensional observation-operator stress**. For a homogeneous dielectric with ideal infinite planar electrodes, the source-free weighting potential is linear and the weighting field is constant. Real finite-electrode nonuniformity generally requires multidimensional electrostatics, fringing fields, and lateral trajectories.

The one-dimensional polynomial-annihilation theorem remains exact for its stated surrogate; do not generalize it into a generic finite-pixel geometry theorem.

### HgCdTe force-partition sensitivity

Rev. 6 exposes the largest remaining arbitrariness of the conditional HgCdTe stress through

```math
E_{drive}^{grad}(z;xi)=xi |(dE_g/dx)(dx/dz)|,
0<xi<=1.
```

The previously reported finite-width benchmark is explicitly the `xi=1` baseline. `xi` is a sensitivity coordinate for the fraction of the total bandgap gradient assigned to the modeled carrier-driving band edge; it is **not** a claimed known HgCdTe band-offset fraction.

A 100-MHz point-source finite-diffusion sweep using the same backward equation and entrance match gives approximately:

```text
xi=0.3 -> v(zc)=8.379e3 m/s  -> C4 phase=-0.00740857 deg
xi=0.6 -> v(zc)=1.9698e4 m/s -> C4 phase=-0.01822428 deg
xi=1.0 -> v(zc)=3.4757e4 m/s -> C4 phase=-0.01245830 deg
```

The nonmonotonicity is retained rather than hidden: changing the force partition changes its competition with the fixed density-of-states term and the finite-frequency closure. Therefore the finite-width `-0.011978 degree` 100-MHz target and the nuisance/resource allocations normalized to it are **conditional `xi=1` design stresses**, not generic HgCdTe material specifications.

### OED prior-art boundary broadened

Rev. 6 adds adjacent primary OED work on commercial Ge PN photodiodes (2021) and bias-tunable Ge PIN photodiodes (2024). Those works use wavelength-dependent RF phase/amplitude as sensing observables. The present candidate distinction remains narrower:

```text
calibrated spectral internal coordinate
-> Ramo-aware spatial differencing
-> minimal-color model order
-> cross-RF physical closure
```

This is a literature boundary, not a novelty claim.

### Two-carrier and hierarchical statistics

Carrier labels are meaningful only after both modes are statistically resolved and continuously tracked. A DC root sign does not rescue an unresolved weak/degenerate mode.

The covariance `chi^2` statistic is a per-rung/conditional test. An experiment that first selects model order and then tests recovered roots using the same noisy data must control sequential-selection error; the current manuscript does not claim full hierarchical false-positive control.

Detailed Rev. 6 records:

```text
REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV6_PRESERVATION_REPORT_2026-08-11.md
numerics/rev6_review_regression.py
```

## 4. Earlier Rev. 4/5 corrections remain mandatory

Rev. 6 retains all prior hardening, especially:

```text
spatial-log aliasing / anti-alias bounds
known-unequal-spacing candidate-root language
singular s=kappa=0 weighting-field degree increase
low-RF q_weight=1 versus q_transport->1 mode coalescence
116.2 / 88.4 / 76.7 dB optimistic equal-mode separation scale
46.3 / 32.3 / 26.4 dB five-color annihilation penalty
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

The finite-width gradient-sensitive four-color phase at the **conditional `xi=1` baseline** remains approximately:

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

These are theory sensitivity coordinates, not calibrated predictions for a named detector.

The same-optics homogeneous subtraction remains part of the covariance budget. Its nominal contribution is roughly 20.5--22.4% of the quoted excess; its uncertainty must be modeled rather than assumed zero.

The existing few-nanometer nonaffine-coordinate and approximately `10^-4 degree` irregular-phase tolerances are derived design requirements under specified error stresses, not demonstrated experimental performance.

## 6. Separate realistic-geometry hardening result

The finite-electrode/depletion calculation remains separately auditable in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
numerics/realistic_geometry_closure_stress.py
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
```

For the representative 75%-contact + 3 um depletion-like stress, the geometry/depletion excess over the planar same-optics baseline is approximately:

```text
100 MHz -> -0.008841 deg = 0.738 x current 1-D gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
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
7. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as predecessor context;
9. `PAPER_CLAIM_LEDGER.md` and newer claim-ledger addenda;
10. the exact extracted manuscript source when manuscript work is required.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
