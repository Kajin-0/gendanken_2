# Gedanken 2 — Current Repository Status

First-principles thought experiments in photodetector physics. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.

**Privacy default:** pseudonymous/anonymous. Identifying information requires explicit user approval; see [`PRIVACY_PROTOCOL.md`](PRIVACY_PROTOCOL.md).

The pre-remediation README remains historical provenance in `README_LEGACY_2026-08-10.md` and git history; it must not override current state.

## Active experiment

`experiments/01-vanishing-absorber/`

The active result is a **Shockley-Ramo-aware spectral-depth closure hierarchy for adversarially falsifying photocarrier transport models**. HgCdTe is a conditional scaling/stress example. Priority remains unresolved; no novelty claim is made.

## Manuscript status

The current approved baseline is the anonymous **21-page Rev. 5**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 5 was validated against Rev. 4 before canonicalization. It preserves the complete paper spine and established equations while addressing the remaining hostile-review points: low-RF observation/transport mode coalescence, rank-two branch/permutation discipline, HgCdTe field-law terminology, modeled-baseline uncertainty, the confluent DC limit, and complex-log notation.

The exact source is stored as a hash-verified anonymous snapshot. Do not use older `MANUSCRIPT_DRAFT.*` files or historical Rev. 3/Rev. 4 snapshots as the current paper.

Start here:

1. [`AGENTS.md`](AGENTS.md)
2. [`MANUSCRIPT_CURRENT.md`](experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md)
3. [`MANUSCRIPT_BASELINE.md`](experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md)
4. [`MANUSCRIPT_PRESERVATION_PROTOCOL.md`](experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md)
5. [`CURRENT_STATE_LIVE.md`](experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md)
6. [`REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
7. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)

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
-> branch-free RF root invariants where available
-> branch/permutation-controlled physical root laws
-> mechanism assignment only after ordinary alternatives are tested
```

For the minimal homogeneous one-carrier planar terminal-current model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

The multiplier-level null is branch-independent. Physical inversion from `q` to `gamma` and then to `D,w,kappa` requires spatial unwrapping; a sufficient principal-branch condition is `|Im gamma| h < pi`.

For the homogeneous finite-boundary rank-two scalar model, Rev. 5 adds the branch-free prerequisite

```math
q_+q_-=e^{-wh/D}\in\mathbb R_{>0},
```

which must also be RF-independent before logarithmic root branches are interpreted.

## Rev. 5 low-RF mode-resolution boundary

A one-dimensional linear weighting field supplies `q_weight=1`, while the transport multiplier approaches unity at low RF. The rank-two witness therefore collapses quadratically as the modes coalesce.

For the manuscript's illustrative scale, even the optimistic equal-mode 3-sigma resolution requirement is approximately:

```text
100 MHz -> 116.2 dB
500 MHz ->  88.4 dB
1 GHz   ->  76.7 dB
```

The complementary five-color exact-annihilation method avoids explicit root separation but costs approximately:

```text
100 MHz -> 46.3 dB
500 MHz -> 32.3 dB
1 GHz   -> 26.4 dB
```

Thus low RF presents a real tradeoff between mode identification and polynomial annihilation rather than a free systematic-removal strategy.

## HgCdTe status

The manuscript's graded-HgCdTe calculation is a **conditional sensitivity/stress construction**, not a calibrated detector prediction. Rev. 5 correctly labels the inherited field-velocity expression as an empirical field-rolloff sensitivity law; the sampled field is only about 5% of its scale, so the rolloff changes the low-field velocity by roughly 0.15--0.18% and no reported closure value changes.

The same-optics homogeneous subtraction is also no longer treated as exact: its uncertainty enters the covariance budget. Its nominal phase is about 20.5--22.4% of the quoted gradient-sensitive excess.

## Separate geometry hardening result

The realistic finite-electrode/depletion study remains separately auditable in [`REALISTIC_GEOMETRY_CLOSURE_STRESS.md`](experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md). It shows that an ordinary geometry/depletion confound can generate an order-unity fraction of the current one-dimensional gradient target, so a four-color residual is not by itself a transport-gradient label.

## Priority blocker

The closest-looking 2024 graded-HgCdTe paper has verified bibliographic metadata but its full text has not yet been lawfully recovered and audited. That exact-source audit remains **OPEN** and blocks submission-level priority/novelty claims. Related-paper searches are not a substitute.

## Next scientific attack

Two fronts now dominate rather than more abstract closure algebra:

1. a plausible self-consistent 2-D semiconductor Poisson/drift-diffusion detector calculation including diffusion, analyzed blindly with the same hierarchy;
2. experimental/calibration feasibility and completion of the exact closest-source priority audit.

Do not restart older exploratory branches merely because they remain in historical documentation. Use `CURRENT_STATE_LIVE.md` and `AGENTS.md` for the live frontier.
