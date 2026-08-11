# Current Live State — Experiment 01

**Date:** 2026-08-11  
**Status:** working theory manuscript + adversarial hardening.  
**Priority:** unresolved; no novelty claim.

This is the current state pointer. The older `CURRENT_STATE.md` remains historical provenance and must not override this file.

## 1. Canonical manuscript

The current approved manuscript baseline is the recovered **16-page Rev. 3** by Anonymous:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

The exact source is repository-preserved and hash-verified through:

```text
MANUSCRIPT_CURRENT.md
MANUSCRIPT_BASELINE.md
MANUSCRIPT_BASELINE.json
MANUSCRIPT_PRESERVATION_PROTOCOL.md
manuscript_history/MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part01 ... part06
tools/extract_manuscript_baseline.py
```

`MANUSCRIPT_DRAFT.tex` and `MANUSCRIPT_DRAFT.md` are older historical sources, not the current manuscript.

## 2. Current paper spine

The surviving framework is:

```text
spectral wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial first differences
-> four-color one-mode closure
-> DC/RF transport-law falsification
-> six-color model-order test when one mode fails
-> RF root laws before mechanism assignment
```

The central one-mode terminal-current null is

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).
```

The rank-two branch uses the adjacent Hankel-minor structure

```math
W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.
```

A second mode must be statistically resolved before roots are interpreted.

## 3. Important hardening already in Rev. 3

The canonical 16-page Rev. 3 already includes, among other material:

- full no-recombination and recombining DC+RF inversion;
- conditioning analysis with `D omega*/V*^2 = sqrt(3)` and the illustrative ~14.1 GHz balance scale;
- six-color rank-two closure and noise significance;
- finite-boundary and conventional two-carrier root tests;
- hot-to-cold thermalization as an ordinary rank-two mode, with quantitative stress cases;
- nonuniform weighting-field analysis, `q_weight = 1`, and the exact five-color polynomial-annihilation branch;
- the low-RF five-color SNR cost `~1.87/|rh|`;
- source-shape, amplitude-calibration, arbitrary-spacing, coordinate-error, and excess-energy corrections;
- independent-noise spacing optimization;
- the corrected graded-HgCdTe conditional prediction, recombination stresses, shooting cross-check, and measurement-resource table.

Do not accidentally remove these when integrating later work.

## 4. Current HgCdTe conditional target

For the current illustrative 7.6 um / 300 K graded-HgCdTe stress, the four mean source depths are

```text
2.5, 3.0, 3.5, 4.0 um
```

with wavelengths approximately

```text
2.134651, 2.215042, 2.301173, 2.393907 um.
```

The conditional one-dimensional gradient-sensitive four-color phase is approximately

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

These are theory sensitivity predictions, not calibrated performance claims for a named detector.

## 5. New realistic-geometry hardening result

The newest completed stress is recorded in:

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

The defensible hierarchy is therefore:

```text
four colors -> detect one-mode failure
six colors  -> determine whether another spatial mode is resolved
RF roots    -> test ordinary mechanism laws
only then   -> make a mechanism-specific transport interpretation
```

The geometry result is conditional on the tested family. It is not a theorem for arbitrary detector geometries.

## 6. Current limitation and next scientific step

The present 2-D geometry stress is deterministic high-Peclet transport. It does not yet include a fully self-consistent semiconductor Poisson/drift-diffusion solution with lateral diffusion, carrier coupling, trapping, or contact-transfer physics.

The next high-value scientific attack is therefore a plausible self-consistent 2-D detector calculation whose synthetic spectral/RF currents are analyzed blindly with the same four-/six-color/RF-root hierarchy.

Do not extend the abstract closure hierarchy merely to accumulate more theorems unless this realistic-device attack exposes a specific missing theorem.

## 7. Priority boundary

Established ingredients include Shockley-Ramo signal formation, wavelength-dependent photodiode timing/phase, photodetector Hankel/model identification, graded-HgCdTe high-speed response, and standard drift-diffusion inversion mathematics.

The complete chain

```text
spectral internal position
-> Ramo-aware spatial differencing
-> color-count model order
-> RF root-law falsification
```

has not been found in the sources examined to date. That is a negative search result, **not evidence of novelty**.

## 8. Mandatory recovery order

A new agent should read:

1. root `AGENTS.md`;
2. `MANUSCRIPT_CURRENT.md`;
3. `MANUSCRIPT_BASELINE.md`;
4. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
5. this file;
6. `PAPER_CLAIM_LEDGER.md` and newer claim-ledger addenda;
7. the exact manuscript source when manuscript work is required.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**
