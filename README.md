# Gedanken 2 — Current Repository Status

First-principles thought experiments in photodetector physics. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.

**Privacy default:** pseudonymous/anonymous. Identifying information requires explicit user approval; see [`PRIVACY_PROTOCOL.md`](PRIVACY_PROTOCOL.md).

The pre-remediation README remains historical provenance in `README_LEGACY_2026-08-10.md` and git history; it must not override current state.

## Active experiment

`experiments/01-vanishing-absorber/`

The active result is a **Shockley-Ramo-aware spectral-depth closure hierarchy for adversarially falsifying photocarrier transport models**. HgCdTe is a conditional scaling/stress example. Priority remains unresolved; no novelty claim is made.

## Manuscript status

The current approved baseline is the anonymous **28-page Rev. 9**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 9 was validated against Rev. 8 before canonicalization. The central four-color theorem, branch-qualified inversion, corrected Hankel rank-at-most-two null, weighting-field treatment, and Rev. 8 numerical fixes remain intact.

The main new mathematical correction is the explicit **confluent/repeated-root rank-two branch**. Hankel rank two is now classified by the recurrence discriminant before physical root interpretation. Rev. 9 also separates common depth-scale calibration from closure calibration, adds a kernel-aware homogeneous one-mode null for independently calibrated arbitrary generation kernels, treats composition as a shared optical/transport nuisance, broadens the spectral-depth prior-art boundary, and adds free DC physical-admissibility checks.

The exact source is stored as a hash-verified anonymous seven-part snapshot. Older revisions remain provenance only.

Start here:

1. [`AGENTS.md`](AGENTS.md)
2. [`MANUSCRIPT_CURRENT.md`](experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md)
3. [`MANUSCRIPT_BASELINE.md`](experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md)
4. [`MANUSCRIPT_PRESERVATION_PROTOCOL.md`](experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md)
5. [`CURRENT_STATE_LIVE.md`](experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md)
6. [`REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
7. [`PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md)
8. [`REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
9. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)

## Manuscript safety rule

> **Preserve first; integrate second; rewrite only when explicitly requested by the user.**

A new theorem, simulation, review response, or correction must not silently compress or restructure unrelated manuscript work. `tools/check_manuscript_preservation.py` and the GitHub Actions preservation check enforce the structural baseline. A deliberate large rewrite requires explicit current-user authorization and the repository justification defined by `MANUSCRIPT_PRESERVATION_PROTOCOL.md`.

## Core experimental logic

```text
wavelength
-> calibrated internal source coordinate / known optical kernels
-> Shockley-Ramo-aware terminal-current observable
-> four-color translated-kernel one-mode closure, or kernel-aware one-mode consistency test
-> branch-controlled continuous-root recovery
-> six-color Hankel rank-at-most-two determinant test if rank one fails
-> recurrence-parameter resolution
-> distinct-root versus confluent/repeated-root classification
-> higher finite-rank tests if rank two fails
-> branch-free RF root invariants where available
-> multiplicity/branch/permutation-controlled physical root laws
-> mechanism assignment only after ordinary alternatives are tested
```

For the minimal homogeneous one-carrier planar terminal-current model with rigidly translated source kernels,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

For independently calibrated arbitrary kernels `g_m(z)`, define

```math
M_m(r)=\int g_m(z)e^{rz}\,dz,
```

so the homogeneous one-mode model is `J_m=A+B M_m(r)`. Four channels still overdetermine the same `r`; the geometric identity is the translated-kernel special case.

The multiplier-level null is branch-independent. Physical inversion from `q` to `gamma` and then to `D,w,kappa` requires spatial unwrapping; a sufficient principal-branch condition is `|Im gamma| h < pi`.

## Rev. 9 rank-two model-order boundary

For five first differences, the unconditional rank-at-most-two null remains

```math
det(H)=0,
```

for the `3x3` Hankel matrix of `d0...d4`. The Rev. 8 correction remains mandatory: `W1^2-W0W2=-d2 det(H)`, so the scalar minor identity is not the unconditional model-order null.

After rank two is accepted and recurrence parameters `S,P` are resolved, Rev. 9 requires

```math
Delta_q=S^2-4P.
```

The live hierarchy is:

```text
rank one rejected
-> rank at most two tested
-> recurrence parameters resolved
-> Delta_q != 0: distinct-root rank two
   Delta_q = 0 with nonzero rank-two contrast: confluent rank two, d_m=(A+Bm)q^m
-> multiplicity-aware physical root law tested
```

A repeated recurrence root is not automatically unphysical; a second-order physical model can itself become confluent. Near exact rank one the determinant statistic is nonregular, so null-constrained simulation/bootstrap calibration is preferred when first-order covariance linearization fails.

## Calibration boundary

A common spatial-coordinate rescaling cancels from the model-order closure but not from recovered dimensional coefficients. If `h_cal=c h`,

```math
D_cal=c^2D,\qquad w_cal=cw,\qquad kappa_cal=kappa.
```

Thus the few-nanometer nonaffine-depth requirement and the absolute/common depth-scale requirement are separate calibration budgets.

## Low-RF observation-mode boundary

The earlier low-RF result remains: a one-dimensional linear weighting-field surrogate supplies `q_weight=1`, while the transport multiplier approaches unity at low RF. The rank-two witness collapses quadratically as the modes coalesce. The prescribed one-dimensional nonuniform weighting field remains an **effective observation-operator surrogate**; real finite-electrode weighting fields generally require multidimensional electrostatics and lateral trajectories.

## HgCdTe status

The graded-HgCdTe calculation remains a **conditional composition-band-edge transport stress**, not a calibrated detector prediction. The 2025 electron-affinity relation anchors the composition-induced electron band-edge force and gives `xi_e~0.666--0.695`; it does **not** anchor the omitted self-consistent electrostatic field or total carrier drift.

The finite-width phase remains about `-0.0220 / -0.1064 / -0.1942 degree` at 100 / 500 / 1000 MHz. The DOS/effective-mass term remains a significant model uncertainty. The local Peclet numbers are only about `0.48` per 0.5-um source step and `0.75` over the 0.79-um kernel width, so the high-Peclet formula is asymptotic intuition rather than the quantitative explanation of the worked result.

The same composition profile enters both the wavelength-to-depth/kernels and the modeled composition-induced transport force. Experimental inference must therefore constrain that profile independently or propagate it as a shared nuisance.

The cited electron-affinity paper's quoted `67.1%` average partition and approximately `±1%` two-thirds comparison are tied to its stated `0.15<x<0.45` averaging interval; the explicit formula is still evaluated over the worked profile reaching `x=0.55` without extending that quoted validation range by assumption.

## Prior-art boundary

Spectral-depth carrier probing itself is established. Classical surface-photovoltage/diffusion-length and photodiode spectral-response work already used wavelength-dependent absorption/generation depth to infer or model carrier transport. Wavelength-dependent RF phase and finite-exponential/Hankel model identification are also established lineages.

This manuscript's candidate distinction is therefore narrower:

```text
calibrated spectral/internal-depth channels
-> Shockley-Ramo terminal-current observable
-> spatial differencing / finite-rank model-order closure
-> branch-controlled or branch-free RF root constraints
-> cross-RF physical-law falsification
```

This is a boundary statement, **not** evidence of novelty. The exact closest 2024 graded-HgCdTe paper still requires a direct technical full-text comparison before any submission-level priority claim.

## Separate geometry hardening result

The realistic finite-electrode/depletion study remains separately auditable in [`REALISTIC_GEOMETRY_CLOSURE_STRESS.md`](experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md). It shows that an ordinary geometry/depletion confound can generate an order-unity fraction of the current one-dimensional gradient target, so a four-color residual is not by itself a transport-gradient label.

## Next scientific attack

The decisive remaining device-physics validation is **one self-consistent combined-physics synthetic detector challenge**, including simultaneous ordinary departures, with its synthetic spectral/RF currents analyzed blindly through the same hierarchy. The hierarchy should be allowed to return `rank>2, mechanism unresolved`; failing safely is part of the validation.

Experimental/calibration feasibility, the exact closest-source priority audit, and the blind combined-physics challenge remain separate open fronts. Adversarial referee reports are inputs to test, not instructions to follow automatically. Do not restart older exploratory branches merely because they remain in historical documentation; use `CURRENT_STATE_LIVE.md` and `AGENTS.md` for the live frontier.
