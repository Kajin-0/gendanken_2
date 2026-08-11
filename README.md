# Gedanken 2 — Current Repository Status

First-principles thought experiments in photodetector physics. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.

**Privacy default:** pseudonymous/anonymous. Identifying information requires explicit user approval; see [`PRIVACY_PROTOCOL.md`](PRIVACY_PROTOCOL.md).

The pre-remediation README remains historical provenance in `README_LEGACY_2026-08-10.md` and git history; it must not override current state.

## Active experiment

`experiments/01-vanishing-absorber/`

The active result is a **Shockley-Ramo-aware spectral-depth closure hierarchy for adversarially falsifying photocarrier transport models**. HgCdTe is a conditional scaling/stress example. Priority remains unresolved; no novelty claim is made.

## Manuscript status

The current approved baseline is the anonymous **22-page Rev. 6**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 6 was validated against Rev. 5 before canonicalization. It preserves the complete paper spine and established theorem chain while addressing the latest hostile-review points: post-detection rank-two conditioning, interpretation of the 1-D weighting-field stress, HgCdTe force-partition sensitivity, adjacent OED prior art, two-carrier identifiability, and sequential statistical testing.

The exact source is stored as a hash-verified anonymous snapshot. Do not use older `MANUSCRIPT_DRAFT.*` files or historical Rev. 3/4/5 snapshots as the current paper.

Start here:

1. [`AGENTS.md`](AGENTS.md)
2. [`MANUSCRIPT_CURRENT.md`](experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md)
3. [`MANUSCRIPT_BASELINE.md`](experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md)
4. [`MANUSCRIPT_PRESERVATION_PROTOCOL.md`](experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md)
5. [`CURRENT_STATE_LIVE.md`](experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md)
6. [`REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
7. [`REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
8. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)

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
-> six-color/higher finite-rank model-order tests if needed
-> rank-two parameter-resolution check
-> branch-free RF root invariants where available
-> branch/permutation-controlled physical root laws
-> mechanism assignment only after ordinary alternatives are tested
```

For the minimal homogeneous one-carrier planar terminal-current model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

The multiplier-level null is branch-independent. Physical inversion from `q` to `gamma` and then to `D,w,kappa` requires spatial unwrapping; a sufficient principal-branch condition is `|Im gamma| h < pi`.

## Rev. 6 post-detection conditioning boundary

A statistically resolved second Hankel mode is necessary but not sufficient for a useful physical root-law test. For

```math
P=q_1q_2=W_1/W_0,
```

Rev. 6 carries the first-order covariance including the shared-minor covariance. In the deliberately optimistic independent equal-significance limit,

```math
sigma_P/|P| ~ sqrt(2)/Z.
```

Thus `Z=3` on each minor still corresponds to about **47.1%** relative product uncertainty. Roughly `Z=14.1` per minor is required for 10% product precision in that simplified limit. The live hierarchy is therefore:

```text
rank-two detection
-> rank-two parameter resolution
-> physical root-law discrimination
```

Algebraic branch immunity is not the same as statistical robustness.

## Low-RF observation-mode boundary

The Rev. 5 result remains: a one-dimensional linear weighting-field surrogate supplies `q_weight=1`, while the transport multiplier approaches unity at low RF. The rank-two witness collapses quadratically as the modes coalesce. On the manuscript scale the optimistic equal-mode 3-sigma resolution requirement is approximately 116.2 / 88.4 / 76.7 dB at 100 / 500 / 1000 MHz, while the complementary five-color exact-annihilation penalty is approximately 46.3 / 32.3 / 26.4 dB.

The prescribed one-dimensional nonuniform weighting field is now explicitly an **effective observation-operator surrogate**. Real finite-electrode weighting fields generally require multidimensional electrostatics and lateral trajectories.

## HgCdTe status

The manuscript's graded-HgCdTe calculation is a **conditional sensitivity/stress construction**, not a calibrated detector prediction. Rev. 6 introduces

```math
E_{drive}^{grad}(z;xi)=xi |(dE_g/dx)(dx/dz)|,  0<xi<=1,
```

so the previously reported finite-width benchmark and nuisance/resource table are explicitly the conditional `xi=1` baseline rather than generic HgCdTe specifications. A 100-MHz point-source finite-diffusion sweep at `xi=0.3, 0.6, 1.0` demonstrates material dependence of the benchmark scale rather than hiding it.

The same-optics homogeneous subtraction remains part of the covariance budget; its uncertainty is a required modeling resource rather than assumed zero.

## Prior-art boundary

The manuscript now includes adjacent primary OED work on commercial Ge PN photodiodes (2021) and bias-tunable Ge PIN photodiodes (2024). Those works use wavelength-dependent RF phase/amplitude as sensing observables. This manuscript's candidate distinction remains narrower: calibrated spectral channels are treated as an internal spatial sequence and subjected to algebraic color-count model-order and cross-RF transport-law nulls.

This is a boundary statement, **not** evidence of novelty. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before any submission-level priority claim.

## Separate geometry hardening result

The realistic finite-electrode/depletion study remains separately auditable in [`REALISTIC_GEOMETRY_CLOSURE_STRESS.md`](experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md). It shows that an ordinary geometry/depletion confound can generate an order-unity fraction of the current one-dimensional gradient target, so a four-color residual is not by itself a transport-gradient label.

## Next scientific attack

The decisive remaining device-physics validation is **one self-consistent combined-physics synthetic detector challenge**, including simultaneous ordinary departures, with its synthetic spectral/RF currents analyzed blindly through the same hierarchy. This tests whether the method retains useful discriminating power when observable rank can exceed two.

Experimental/calibration feasibility and the exact closest-source priority audit remain separate open fronts. Do not restart older exploratory branches merely because they remain in historical documentation; use `CURRENT_STATE_LIVE.md` and `AGENTS.md` for the live frontier.
