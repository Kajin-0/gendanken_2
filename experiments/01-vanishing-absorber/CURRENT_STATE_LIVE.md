# Current Live State — Experiment 01

**Date:** 2026-08-11  
**Status:** anonymous Rev. 4 manuscript + adversarial hardening.  
**Priority:** unresolved; no novelty claim.

This is the current state pointer. The older `CURRENT_STATE.md` remains historical provenance and must not override this file.

## 1. Canonical manuscript

The current approved manuscript baseline is the anonymous **19-page Rev. 4**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 4 was first checked against the established Rev. 3 preservation baseline in PR #4. Only after that guard and the privacy gate passed was Rev. 4 made canonical.

The exact source is repository-preserved and hash-verified through:

```text
MANUSCRIPT_REV4_ANON_2026-08-11.tex
MANUSCRIPT_CURRENT.md
MANUSCRIPT_BASELINE.md
MANUSCRIPT_BASELINE.json
MANUSCRIPT_PRESERVATION_PROTOCOL.md
manuscript_history/MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part01 ... part03
tools/extract_manuscript_baseline.py
```

Canonical source anchors:

```text
SHA-256 = 9da8c6094a58109873382b6b3c73c519b26f519e327f5ec8058009bc4896df00
lines = 817
compiled pages = 19
author/PDF metadata = Anonymous
```

`MANUSCRIPT_DRAFT.*` and the anonymous Rev. 3 snapshot are historical provenance, not the current manuscript.

## 2. Current paper spine

The surviving framework is:

```text
spectral wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial first differences
-> four-color one-mode closure in q-space
-> branch-controlled recovery of gamma
-> DC/RF transport-law inference and falsification
-> six-color/higher finite-rank model-order tests when needed
-> RF root laws before mechanism assignment
```

The central one-mode terminal-current null remains

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).
```

The rank-two branch uses

```math
W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.
```

A second mode must be statistically resolved before roots are interpreted.

## 3. Rev. 4 adversarial corrections — now canonical

The hostile review found two genuine mathematical qualifications and several experimental/reproducibility gaps. Rev. 4 addresses them surgically without changing the central closure theorem.

### Spatial-logarithm aliasing

The four-color sequence identifies

```math
q=e^{-\gamma h}
```

but the continuous exponent has the branch family

```math
\gamma_n=-\frac{\operatorname{Log}q+2\pi i n}{h}.
```

Therefore the four-color multiplier null is branch-independent, while physical recovery of `D,w,kappa` is conditional on branch selection. A sufficient principal-branch condition is

```math
|\operatorname{Im}\gamma|h<\pi.
```

The regression contains an explicit positive alternate inverse for the alias stress.

### Known unequal spacing

The first three known positions constrain one or more candidate spatial roots; they do not guarantee a unique exponent. The fourth position filters candidates. Physical inversion is unique only when the fourth-point constraint plus branch/physical restrictions leave one admissible root.

### Singular weighting-field limit

For

```math
DJ''+wJ'-(\kappa+s)J=-[wE_w+DE_w'],
```

a polynomial observation forcing of degree `p` gives a particular solution of the same degree when `kappa+s != 0`.

At the singular point

```text
s = 0
kappa = 0
w > 0
```

the particular degree generically increases by one. For a linear field,

```math
E_w(z)=E_0+E_1z,
```

an exact particular solution is

```math
J_p(z)=-E_0z-\frac{E_1}{2}z^2.
```

Thus:

```text
kappa+s != 0 -> linear particular -> second differences -> five colors
s=kappa=0    -> quadratic particular -> third differences -> six colors
```

The former blanket five-color wording must never be resurrected.

### Calibration resources

Under deliberately independent residual-error stresses, the current HgCdTe quartet requires approximately:

```text
nonaffine source-coordinate RMS:
100 MHz -> 3.828 nm
500 MHz -> 3.780 nm
1 GHz   -> 3.626 nm

irregular channel-phase RMS:
100 MHz -> 1.023e-4 deg
500 MHz -> 5.017e-4 deg
1 GHz   -> 9.431e-4 deg
```

These are **not absolute depth or common-delay requirements**. Common/affine spectral errors cancel strongly; the numbers quantify the residual high-curvature/independent component under the stated stress.

### HgCdTe reproducibility

Rev. 4 now states the exact transport prescription used by the existing numerical code: linear `x(z)`, Hansen gap and derivative, Einstein diffusion, the conditional saturation law, the reduced density-of-states gradient correction, the stochastic backward equation, and the semi-infinite homogeneous entrance match.

The `~10^-6 degree` solver agreement is explicitly numerical cross-verification of the same conditional model, **not physical validation at that precision**.

Detailed records:

```text
REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV4_PRESERVATION_REPORT_2026-08-11.md
numerics/rev4_critique_regression.py
```

## 4. Established material preserved in Rev. 4

Rev. 4 still contains:

- the full Shockley-Ramo observable correction and four-color theorem;
- the no-recombination and recombining DC+RF inversion;
- the conditioning result `D omega*/V*^2 = sqrt(3)` and illustrative ~14.1 GHz balance scale;
- six-color rank-two/Hankel closure and mode-resolution significance;
- finite-boundary and conventional two-carrier root tests;
- hot-to-cold thermalization as an ordinary **rank-at-most-two** mechanism with quantitative stresses;
- nonuniform weighting-field analysis, including the corrected singular limit;
- controlled slowness-gradient theory;
- source-shape, complex channel-calibration, arbitrary-spacing, coordinate-error, and excess-energy corrections;
- independent-noise spacing optimization;
- the corrected graded-HgCdTe conditional prediction, recombination stresses, independent shooting cross-check, nuisance budget, and measurement-resource table.

Do not accidentally remove these when integrating later work.

## 5. Current HgCdTe conditional target

For the illustrative 7.6 um / 300 K graded-HgCdTe stress, the four mean source depths are

```text
2.5, 3.0, 3.5, 4.0 um
```

with wavelengths approximately

```text
2.134651, 2.215042, 2.301173, 2.393907 um.
```

The conditional one-dimensional gradient-sensitive four-color phase remains approximately

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

These are theory sensitivity predictions, not calibrated performance claims for a named detector. Rev. 4 did not change these values.

## 6. Separate realistic-geometry hardening result

The finite-electrode/depletion calculation remains recorded separately in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
numerics/realistic_geometry_closure_stress.py
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
```

A deterministic 2-D finite-electrode + depletion-like field stress shows that geometry can produce a four-color phase excess equal to an order-unity fraction of the current one-dimensional gradient target. For the representative 75%-contact + 3 um depletion stress:

```text
100 MHz -> -0.008841 deg = 0.738 x target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

Therefore:

```text
four-color failure != transport-gradient identification.
```

The same tested geometry tends to announce itself as additional spatial rank. At 100 MHz the nominal 3-sigma second-mode threshold is about `84.6 dB` current-step amplitude SNR, versus `96.1 dB` for the present gradient-specific inference. The fitted effective rank-two roots also fail the homogeneous finite-boundary real/RF-independent root-sum law.

This geometry result is **CHECKED / CONDITIONAL**, not a calibrated device simulation or theorem for arbitrary geometry. It was intentionally not integrated into Rev. 4 as a definitive detector prediction.

## 7. Interpretation hierarchy

The defensible order is now explicitly:

```text
rank 1 / four-color null
-> rank 2 if statistically resolved
-> higher ordinary finite-rank mechanisms if needed
-> RF root-law tests within the resolved order
-> only after ordinary alternatives fail, richer/nonlocal transport
```

Failure of rank two alone does not imply nonlocal or exotic physics.

## 8. Current limitation and next scientific step

The present 2-D geometry stress is deterministic high-Peclet transport. It does not yet include a fully self-consistent semiconductor Poisson/drift-diffusion solution with lateral diffusion, carrier coupling, trapping, or contact-transfer physics.

The next high-value scientific attack remains a plausible self-consistent 2-D detector calculation whose synthetic spectral/RF currents are analyzed blindly with the same four-/six-color/higher-rank/RF-root hierarchy.

Do not extend the abstract closure hierarchy merely to accumulate more theorems unless this realistic-device attack exposes a specific missing theorem.

## 9. Priority boundary

Established ingredients include Shockley-Ramo signal formation, wavelength-dependent photodiode timing/phase, photodetector Hankel/model identification, graded-HgCdTe high-speed response, and standard drift-diffusion inversion mathematics.

The complete chain

```text
spectral internal position
-> Ramo-aware spatial differencing
-> color-count model order
-> RF root-law falsification
```

has not been found in the sources examined to date. That is a negative search result, **not evidence of novelty**.

## 10. Mandatory recovery order

A new agent should read:

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. `MANUSCRIPT_CURRENT.md`;
4. `MANUSCRIPT_BASELINE.md`;
5. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
6. this file;
7. `REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `PAPER_CLAIM_LEDGER.md` and newer claim-ledger addenda;
9. the exact extracted manuscript source when manuscript work is required.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identifying information only when explicitly approved for that artifact.**
