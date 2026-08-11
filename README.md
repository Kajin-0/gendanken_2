# Gedanken 2 — Current Repository Status

First-principles thought experiments in photodetector physics. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.

The pre-remediation README remains recoverable from git at commit `c034984b2ccf3ccc0a71638b0b197f7fa4c98645`; see `README_LEGACY_2026-08-10.md`. It is historical and must not be used as current scientific state.

## Active experiment

`experiments/01-vanishing-absorber/`

The active result is a **Shockley-Ramo-aware spectral-depth closure hierarchy for adversarially falsifying photocarrier transport models**. HgCdTe is the leading conditional worked example. Priority remains unresolved; no novelty claim is made.

## Manuscript status

A working manuscript **does exist**.

The current approved baseline is the recovered **16-page Rev. 3** by **Terence Fisher**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

The exact source is preserved inside the repository as a hash-verified snapshot. Do not use the older `MANUSCRIPT_DRAFT.*` files as the current paper.

Start here:

1. [`AGENTS.md`](AGENTS.md)
2. [`MANUSCRIPT_CURRENT.md`](experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md)
3. [`MANUSCRIPT_BASELINE.md`](experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md)
4. [`MANUSCRIPT_PRESERVATION_PROTOCOL.md`](experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md)
5. [`CURRENT_STATE_LIVE.md`](experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md)
6. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)

## Manuscript safety rule

The repository now enforces:

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
-> six-color model-order test if one mode fails
-> RF root laws before mechanism assignment
```

For the minimal homogeneous one-carrier planar terminal-current model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

If that one-mode closure fails, six source coordinates test whether a second spatial mode is statistically resolved before any physical mechanism is assigned.

## Current geometry hardening result

The newest adversarial calculation is:

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
six colors  -> establish model order
RF roots    -> test ordinary mechanisms
only then   -> assign a mechanism-specific transport interpretation
```

The geometry result is conditional on the tested model family and is not a theorem for arbitrary detector geometries.

## Next scientific attack

The current geometry calculation is deterministic high-Peclet transport. The next high-value falsification study is a plausible self-consistent 2-D semiconductor Poisson/drift-diffusion detector calculation, including diffusion, analyzed blindly with the same hierarchy.

Do not restart older tomography/fabrication branches merely because they appear in historical documentation. Use `CURRENT_STATE_LIVE.md` and `AGENTS.md` to recover the current frontier.
