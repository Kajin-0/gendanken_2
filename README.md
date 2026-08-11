# Gedanken 2 — Current Repository Status

First-principles thought experiments in photodetector physics. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.

**Privacy default:** pseudonymous/anonymous. Identifying information requires explicit user approval; see [`PRIVACY_PROTOCOL.md`](PRIVACY_PROTOCOL.md).

The pre-remediation README remains recoverable from git at commit `c034984b2ccf3ccc0a71638b0b197f7fa4c98645`; see `README_LEGACY_2026-08-10.md`. It is historical and must not be used as current scientific state.

## Active experiment

`experiments/01-vanishing-absorber/`

The active result is a **Shockley-Ramo-aware spectral-depth closure hierarchy for adversarially falsifying photocarrier transport models**. HgCdTe is the leading conditional worked example. Priority remains unresolved; no novelty claim is made.

## Manuscript status

A working manuscript **does exist**.

The current approved baseline is the anonymous **19-page Rev. 4**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 4 was validated against the previous Rev. 3 baseline before canonicalization. It preserves the established paper spine while correcting the latest hostile-review findings: spatial-log branch ambiguity, the singular DC/no-recombination weighting-field limit, arbitrary-spacing candidate-root language, quantitative calibration stresses, explicit HgCdTe transport equations, and covariance-aware falsification language. The central four-color theorem and reported HgCdTe closure values are unchanged.

The exact source is preserved inside the repository as a hash-verified anonymous snapshot. Do not use older `MANUSCRIPT_DRAFT.*` files or the historical Rev. 3 snapshot as the current paper.

Start here:

1. [`AGENTS.md`](AGENTS.md)
2. [`MANUSCRIPT_CURRENT.md`](experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md)
3. [`MANUSCRIPT_BASELINE.md`](experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md)
4. [`MANUSCRIPT_PRESERVATION_PROTOCOL.md`](experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md)
5. [`CURRENT_STATE_LIVE.md`](experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md)
6. [`REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
7. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)

## Manuscript safety rule

The repository enforces:

> **Preserve first; integrate second; rewrite only when explicitly requested by the user.**

A new theorem, simulation, review response, or correction must not silently compress or restructure unrelated manuscript work. `tools/check_manuscript_preservation.py` and the GitHub Actions preservation check flag unexpected section/subsection/reference/equation loss, substantial shrinkage, author/title changes, or large replacement of established source.

A deliberate large rewrite can bypass the guard only when the current user explicitly requests compression/restructuring and the required justification contains that instruction verbatim. An agent may not infer rewrite permission from ordinary requests to revise, integrate, harden, improve, update, or review the paper.

## Core experimental logic

The surviving hierarchy is:

```text
wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial differencing
-> four-color one-mode closure
-> branch-controlled spatial exponent recovery
-> six-color/higher finite-rank model-order tests if needed
-> RF root laws before mechanism assignment
```

For the minimal homogeneous one-carrier planar terminal-current model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

This multiplier-level four-color null is branch-independent. Physical inversion from the measured spatial multiplier `q` to a continuous exponent `gamma` and then to `D,w,kappa` requires a uniquely selected spatial-logarithm branch; a sufficient principal-branch condition is `|Im gamma| h < pi`.

If the one-mode closure fails, six source coordinates test whether a second spatial mode is statistically resolved before any physical mechanism is assigned. Failure of rank two does not by itself imply exotic transport; higher ordinary finite-rank mechanisms must be considered first.

## Rev. 4 adversarial corrections

The complete correction record is:

- [`REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
- [`MANUSCRIPT_REV4_PRESERVATION_REPORT_2026-08-11.md`](experiments/01-vanishing-absorber/MANUSCRIPT_REV4_PRESERVATION_REPORT_2026-08-11.md)
- [`rev4_critique_regression.py`](experiments/01-vanishing-absorber/numerics/rev4_critique_regression.py)

Important corrected boundary: for a one-dimensional linear weighting field, the ordinary five-color second-difference annihilation result applies when `kappa+s != 0`. At the singular point `s=kappa=0`, the particular solution is quadratic and exact annihilation requires third differences / six colors.

## Separate geometry hardening result

The realistic finite-electrode/depletion calculation remains separately auditable:

- [`REALISTIC_GEOMETRY_CLOSURE_STRESS.md`](experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md)
- [`realistic_geometry_closure_stress.py`](experiments/01-vanishing-absorber/numerics/realistic_geometry_closure_stress.py)

For the representative 75%-contact + 3 um depletion-like stress, the 2-D geometry/depletion phase excess is approximately:

```text
100 MHz -> -0.008841 deg = 0.738 x current 1-D gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

Thus a four-color residual is **not** by itself a transport-gradient label. In the tested geometry the confound also produces additional spatial rank before the SNR required for the current gradient-specific inference, and the effective rank-two roots fail the homogeneous finite-boundary RF root law.

The defensible interpretation order is:

```text
four colors -> detect one-mode failure
six colors  -> establish whether rank two suffices
higher ordinary finite rank if needed
RF roots    -> test ordinary mechanism laws
only then   -> assign a mechanism-specific transport interpretation
```

The geometry result is conditional on the tested model family and is not a theorem for arbitrary detector geometries. It was not promoted into Rev. 4 as a calibrated device result.

## Next scientific attack

The current geometry calculation is deterministic high-Peclet transport. The next high-value falsification study remains a plausible self-consistent 2-D semiconductor Poisson/drift-diffusion detector calculation, including diffusion, analyzed blindly with the same hierarchy.

Do not restart older tomography/fabrication branches merely because they appear in historical documentation. Use `CURRENT_STATE_LIVE.md` and `AGENTS.md` to recover the current frontier.
