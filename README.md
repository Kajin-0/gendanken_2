# Gedanken 2 — Current Repository Status

First-principles thought experiments in photodetector physics. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.

**Privacy default:** pseudonymous/anonymous. Identifying information requires explicit user approval; see [`PRIVACY_PROTOCOL.md`](PRIVACY_PROTOCOL.md).

The pre-remediation README remains historical provenance in `README_LEGACY_2026-08-10.md` and git history; it must not override current state.

## Active experiment

`experiments/01-vanishing-absorber/`

The active result is a **Shockley-Ramo-aware spectral-depth closure hierarchy for adversarially falsifying photocarrier transport models**. HgCdTe is a conditional scaling/stress example. Priority remains unresolved; no novelty claim is made.

## Manuscript status

The current approved baseline is the anonymous **26-page Rev. 8**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 8 was validated against Rev. 7 before canonicalization. The central four-color theorem and branch-qualified inversion remain intact. The main new correction is a genuine six-color algebra fix: the unconditional rank-at-most-two model-order null is the full `3x3` Hankel determinant, because the older minor closure also vanished spuriously at `d2=0`.

Rev. 8 also adds the missing noisy rank-two determinant test, reconciles weighting-field numerics, validates the tiny recombination subtraction differentially, separates composition-band-edge force from total drift, quantifies DOS/effective-mass sensitivity, and states the nearly lossless two-carrier DC degeneracy.

The exact source is stored as a hash-verified anonymous seven-part snapshot. Older revisions remain provenance only.

Start here:

1. [`AGENTS.md`](AGENTS.md)
2. [`MANUSCRIPT_CURRENT.md`](experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md)
3. [`MANUSCRIPT_BASELINE.md`](experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md)
4. [`MANUSCRIPT_PRESERVATION_PROTOCOL.md`](experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md)
5. [`CURRENT_STATE_LIVE.md`](experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md)
6. [`REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
7. [`REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
8. [`REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
9. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)

## Manuscript safety rule

> **Preserve first; integrate second; rewrite only when explicitly requested by the user.**

A new theorem, simulation, review response, or correction must not silently compress or restructure unrelated manuscript work. `tools/check_manuscript_preservation.py` and the GitHub Actions preservation check enforce the structural baseline. A deliberate large rewrite requires explicit current-user authorization and the repository justification defined by `MANUSCRIPT_PRESERVATION_PROTOCOL.md`.

## Core experimental logic

```text
wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial differencing
-> four-color one-mode closure in q-space
-> branch-controlled continuous-root recovery
-> six-color Hankel rank-at-most-two determinant test if rank one fails
-> rank-two parameter-resolution check if the determinant null passes
-> higher finite-rank tests if rank two fails
-> branch-free RF root invariants where available
-> branch/permutation-controlled physical root laws
-> mechanism assignment only after ordinary alternatives are tested
```

For the minimal homogeneous one-carrier planar terminal-current model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

The multiplier-level null is branch-independent. Physical inversion from `q` to `gamma` and then to `D,w,kappa` requires spatial unwrapping; a sufficient principal-branch condition is `|Im gamma| h < pi`.

## Rev. 8 rank-two model-order boundary

The six-color rung now separates **existence of a second mode**, **rank-at-most-two model order**, and **parameter resolution**.

For five first differences, the unconditional rank-at-most-two null is

```math
det(H)=0,
```

for the `3x3` Hankel matrix of `d0...d4`. The older identity obeys

```math
W1^2-W0W2=-d2 det(H),
```

so it is not an unconditional model-order null. Adjacent minors remain useful after the determinant test for separation, conditioning, and recurrence recovery.

The live hierarchy is:

```text
rank one rejected
-> rank at most two tested
-> two-mode parameters resolved
-> physical root law tested
```

The Rev. 6 covariance result for recurrence parameters remains mandatory: statistically detecting a second mode does not guarantee accurate roots.

## Low-RF observation-mode boundary

The Rev. 5 result remains: a one-dimensional linear weighting-field surrogate supplies `q_weight=1`, while the transport multiplier approaches unity at low RF. The rank-two witness collapses quadratically as the modes coalesce. On the manuscript scale the optimistic equal-mode 3-sigma resolution requirement is approximately 108.6 / 81.2 / 70.5 dB at 100 / 500 / 1000 MHz, while the complementary five-color exact-annihilation penalty is approximately 42.4 / 28.7 / 23.2 dB.

The prescribed one-dimensional nonuniform weighting field is now explicitly an **effective observation-operator surrogate**. Real finite-electrode weighting fields generally require multidimensional electrostatics and lateral trajectories.

## HgCdTe status

The graded-HgCdTe calculation remains a **conditional composition-band-edge transport stress**, not a calibrated detector prediction. The 2025 electron-affinity relation anchors the composition-induced electron band-edge force and gives `xi_e~0.666--0.695`; it does **not** anchor the omitted self-consistent electrostatic field or total carrier drift.

The finite-width phase remains about `-0.0220 / -0.1064 / -0.1942 degree` at 100 / 500 / 1000 MHz.

Rev. 8 exposes the retained DOS/effective-mass approximation as a significant uncertainty: `|v_DOS|/v_field` is about 8.8--18.3% across the layer, and an `alpha_DOS` sensitivity moves the worked closure appreciably. A deliberately steep 5-us-anchored differential-recombination stress remains negligible on the gradient-signal scale, with the tiny subtraction cross-checked independently to about `3e-9 degree` between implementations across tested environments.

The corrected 1% weighting-field false phases are `0.002947 / 0.012140 / 0.010007 degree` at 100 / 500 / 1000 MHz. The allowable variation for a 10%-of-target contamination is `0.757% / 0.881% / 1.961%`.

The same-optics homogeneous subtraction remains part of the covariance budget rather than assumed exact.

## Prior-art boundary

Rev. 7 explicitly places the finite-exponential algebra in the classical Prony / ESPRIT / matrix-pencil lineage. It also retains adjacent primary OED work on commercial Ge PN photodiodes (2021) and bias-tunable Ge PIN photodiodes (2024). Those works use wavelength-dependent RF phase/amplitude as sensing observables.

This manuscript's candidate distinction remains narrower: calibrated spectral channels are treated as an internal spatial sequence, mapped through Shockley--Ramo terminal current, and subjected to classical color-count model-order tests plus cross-RF physical root constraints.

This is a boundary statement, **not** evidence of novelty. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before any submission-level priority claim.

## Separate geometry hardening result

The realistic finite-electrode/depletion study remains separately auditable in [`REALISTIC_GEOMETRY_CLOSURE_STRESS.md`](experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md). It shows that an ordinary geometry/depletion confound can generate an order-unity fraction of the current one-dimensional gradient target, so a four-color residual is not by itself a transport-gradient label.

## Next scientific attack

The decisive remaining device-physics validation is **one self-consistent combined-physics synthetic detector challenge**, including simultaneous ordinary departures, with its synthetic spectral/RF currents analyzed blindly through the same hierarchy. This tests whether the method retains useful discriminating power when observable rank can exceed two.

Experimental/calibration feasibility, the exact closest-source priority audit, and the blind combined-physics challenge remain separate open fronts. Adversarial referee reports are inputs to test, not instructions to follow automatically. Do not restart older exploratory branches merely because they remain in historical documentation; use `CURRENT_STATE_LIVE.md` and `AGENTS.md` for the live frontier.
