# Current Live State — Experiment 01

**Date:** 2026-08-11  
**Status:** anonymous Rev. 5 manuscript + adversarial hardening.  
**Priority:** unresolved; no novelty claim.

This is the current state pointer. Historical state files and older manuscript snapshots must not override it.

## 1. Canonical manuscript

The current approved manuscript baseline is the anonymous **21-page Rev. 5**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 5 was first judged against the established Rev. 4 preservation baseline. Only after the manuscript-preservation and privacy gates passed was it made canonical.

Exact source:

```text
MANUSCRIPT_REV5_ANON_2026-08-11.tex
SHA-256 = 9d9c4686a152dcdbbfebae1db00a22f5cfd743b5948f825e79ba2acd75b812fb
bytes = 59803
lines = 863
compiled pages = 21
sections = 12
subsections = 18
bibliography items = 11
equation environments = 92
author/PDF metadata = Anonymous
```

Hash-verified recovery uses six snapshot parts under `manuscript_history/` and `python tools/extract_manuscript_baseline.py`.

Rev. 4, Rev. 3, and `MANUSCRIPT_DRAFT.*` remain historical provenance only.

## 2. Current paper hierarchy

```text
spectral wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial first differences
-> four-color one-mode closure in multiplier q
-> branch-controlled continuous exponent gamma
-> six-color/higher finite-rank model-order tests when needed
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

## 3. Rev. 5 adversarial corrections — canonical

### Low-RF weighting/transport mode coalescence

For the one-dimensional linear-weighting-field branch,

```math
q_{weight}=1,
```

while the homogeneous transport multiplier approaches

```math
q_{tr}=e^{-\gamma h}\to1
```

at low RF with small recombination. The existing rank-two witness then loses resolving power quadratically through `(q_1-q_2)^2`.

For the manuscript's illustrative `D=0.02327 m^2/s`, `w≈3.45e4 m/s`, `h=0.5 um` scale, the best-case equal-mode 3-sigma amplitude-SNR requirements are approximately:

```text
100 MHz -> 116.2 dB
500 MHz ->  88.4 dB
1 GHz   ->  76.7 dB
```

This is especially important at 100 MHz because the present gradient-specific measurement-resource estimate is about 96.1 dB: even equal-amplitude weighting and transport modes would be harder to resolve from one another than the target gradient effect is to detect.

### Complementary five-color penalty

Exact second-difference annihilation of the non-singular linear weighting-field contribution avoids explicit mode identification but carries the existing low-RF cost `cost_5/cost_4 ~ 1.87/|rh|`.

For the same scale:

```text
100 MHz -> 46.3 dB amplitude-SNR penalty
500 MHz -> 32.3 dB
1 GHz   -> 26.4 dB
```

Thus low RF presents a genuine tradeoff:

```text
identify q_weight=1 -> transport/observation roots coalesce
annihilate q_weight=1 -> severe low-RF noise penalty
```

Neither method is a free systematic-removal step.

### Rank-two branch/permutation discipline

For the homogeneous finite-boundary scalar model,

```math
r_++r_-=-w/D.
```

Therefore the product of measured spatial multipliers obeys the branch-free constraint

```math
q_+q_-=e^{(r_++r_-)h}=e^{-wh/D}\in\mathbb R_{>0},
```

and must be RF-independent.

This should be tested before taking logarithms. Only afterward are individual roots unwrapped. Both logarithmic branch integers and root pairing/permutation across RF must be fixed using independent physical bounds, multiple spacings when available, and continuity. Branches must never be selected merely because they make the hypothesized root law fit.

### Confluent DC limit and complex closure notation

At `s=kappa=0`, the finite-`s` exponential representation is understood in its confluent `q->1` limit. The terminal-current sequence becomes affine in source depth, its first differences become constant, and the four-color closure remains exact.

The complex closure statistic is now defined as one continuously tracked logarithm of the branch-free multiplicative ratio rather than as three separately branched logarithms.

### HgCdTe field law

The inherited formula

```math
v_field = mu E / [1 + (E/E_scale)^{r_s}]
```

with `r_s=2.2` is **not** asymptotically velocity-saturating; it is retained only as an empirical field-rolloff sensitivity law used by the existing numerical stress. The sampled grading fields are only roughly `4.1--4.5e4 V/m` versus an `8e5 V/m` scale, so the correction to low-field linear velocity is only about 0.15--0.18%. The reported closure values therefore remain unchanged.

The HgCdTe example remains a conditional sensitivity/stress construction, not a calibrated device prediction.

### Same-optics homogeneous baseline uncertainty

The flagship gradient-sensitive quantity is a modeled subtraction,

```math
C_exc = C_meas - C_hom.
```

Rev. 5 explicitly carries the homogeneous-baseline uncertainty into the covariance:

```math
Sigma_exc = Sigma_meas + Sigma_hom - Sigma_cross - Sigma_cross^T.
```

The nominal same-optics homogeneous phase is approximately 20.5--22.4% of the quoted gradient-sensitive excess, so treating it as exact is not justified. The nuisance table now includes an explicit 10%-of-target allocation for this modeled baseline.

### Calibration requirements

The existing few-nanometer nonaffine source-coordinate and approximately `10^-4 degree` irregular-phase numbers are **derived design requirements under the stated independent-error stresses**. They are not demonstrations that an experiment has already achieved those calibrations.

Detailed Rev. 5 records:

```text
REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV5_PRESERVATION_REPORT_2026-08-11.md
numerics/rev5_review_regression.py
```

## 4. Earlier Rev. 4 corrections remain mandatory

Rev. 5 retains all Rev. 4 hardening, especially:

```text
spatial-log aliasing / anti-alias bounds
known-unequal-spacing candidate-root language
singular s=kappa=0 weighting-field degree increase
complex channel calibration
nonaffine source-coordinate tolerance
explicit HgCdTe transport and semi-infinite entrance prescription
covariance-aware falsification language
rank-at-most-two precision
```

Do not regress to the earlier unrestricted claims.

## 5. Current HgCdTe conditional target

For the illustrative 7.6 um / 300 K graded-HgCdTe stress:

```text
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
wavelengths ~ 2.134651, 2.215042, 2.301173, 2.393907 um
```

The conditional one-dimensional gradient-sensitive four-color phase remains:

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

No Rev. 5 correction changes these values.

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

The closest-looking 2024 graded-HgCdTe paper has verified bibliographic metadata, but its exact full text has not yet been lawfully recovered and audited. That task remains **OPEN** and blocks any submission-level novelty/priority claim.

Accessible related sources establish composition-gradient built-in fields, wavelength-dependent response, strong-illumination behavior, and graded-HgCdTe high-speed response. None of the related texts examined establishes the exact full chain below, but this negative result is **not evidence of novelty**:

```text
spectral internal coordinate
-> Ramo-aware differencing
-> minimal-color model order
-> cross-RF physical closure
```

The exact closest source must still be read in full.

## 8. Current limitation and next work

The mathematical skeleton now survives repeated hostile review under its stated hypotheses. The largest remaining risks have shifted toward **experimental feasibility, modeled-systematic control, realistic-device transport, and priority**.

Highest-value next work:

1. obtain and fully audit the exact closest 2024 graded-HgCdTe paper;
2. build one plausible self-consistent 2-D semiconductor Poisson/drift-diffusion detector calculation including diffusion and analyze its synthetic spectral/RF currents blindly with the same hierarchy;
3. develop a credible calibration architecture for the extreme residual phase/depth requirements rather than merely quoting them;
4. continue literature audit only around the exact claimed spectral-depth/Ramo/model-order/RF-closure combination.

Do not add broad new abstract theorems unless one of these attacks exposes a specific missing theorem.

## 9. Mandatory recovery order

A new agent should read:

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. `MANUSCRIPT_CURRENT.md`;
4. `MANUSCRIPT_BASELINE.md`;
5. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
6. this file;
7. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
9. `PAPER_CLAIM_LEDGER.md` and newer claim-ledger addenda;
10. the exact extracted manuscript source when manuscript work is required.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
