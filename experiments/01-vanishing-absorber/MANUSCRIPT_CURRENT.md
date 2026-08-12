# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the anonymous **24-page Rev. 7**, validated against Rev. 5 before canonicalization.

**Canonical author metadata:** `Anonymous`.

Do **not** use `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, or historical Rev. 3/4/5 snapshots as the current source. Do not restore identifying author information from historical files, git history, account/profile information, public sources, or memory.

## Exact source

The canonical source is:

```text
MANUSCRIPT_REV7_ANON_2026-08-11.tex
```

and is preserved in six repository snapshot parts:

```text
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part06
```

Recover the exact editable baseline only with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor refuses to write a working source unless the snapshot hash, source hash, line count, and anonymous author metadata match:

```text
source SHA-256 = 9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8
gzip SHA-256   = 8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b
bytes = 75182
lines = 963
pages in matching compiled PDF = 24
author = Anonymous
PDF author metadata = Anonymous
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

Never reconstruct it from handoff notes or overwrite it with an older source.

## Rev. 7 status

Rev. 7 is a surgical response to the post-Rev. 6 hostile review. The report was treated as an attack list rather than authority: objections were independently checked and only scientifically useful corrections were adopted.

The core hierarchy is unchanged:

```text
rank detection
-> parameter resolution
-> physical root-law discrimination
```

Rev. 7 adds the following locks:

- classical Prony/ESPRIT/matrix-pencil algebra is cited explicitly and is **not** claimed as new;
- the proposed distinction is the calibrated spectral-depth + Shockley--Ramo + spatial-difference + classical finite-rank + cross-RF physical-constraint construction;
- the HgCdTe worked stress now uses the electron-affinity-anchored driving band edge `E_drive^grad=|(dE_g/dx-0.45) dx/dz|`, giving `xi_e~0.666--0.695`, instead of using `xi=1` as the headline baseline;
- the finite-width closure excess is about `-0.0220167 / -0.1064448 / -0.1942321 degree` at 100 / 500 / 1000 MHz;
- an intentionally steep 5-us-anchored spatial differential-recombination stress changes the closure by less than `4e-7 degree` over 0.1--1 GHz in this conditional model; do not generalize that result to high-injection, depleted, or arbitrary devices;
- the 1-D weighting-field theorem remains an effective axial observation-operator surrogate, not a generic finite-electrode electrostatic theorem;
- the hierarchy is structural model-selection logic; per-rung significance does not constitute a globally calibrated sequential test;
- a common-RF-reference, interleaved-wavelength, reference-photodiode/coherent-receiver architecture is specified as a plausible measurement path, but its residual calibration performance is not demonstrated.

Propagated design scales now include:

```text
conditioning optimum:             5.85 GHz
3-sigma current-step SNR:         90.9 / 82.9 / 77.1 / 71.4 dB at 100/250/500/1000 MHz
nonaffine coordinate RMS:         ~4.5 nm at 100--1000 MHz
irregular channel phase RMS:      1.88e-4 / 9.15e-4 / 1.71e-3 deg at 100/500/1000 MHz
1-D weighting change for <10%:    0.757% / 0.881% / 1.961%
same-optics baseline/excess:      17.3% / 17.9% / 19.8%
```

Detailed audit:

```text
REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md
numerics/rev7_review_regression.py
```

Rev. 6 and earlier revisions remain preserved historical provenance.

## Priority and feasibility blockers

Priority remains **OPEN / UNPROVEN**. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before submission-level priority/novelty language.

Experimental feasibility is also not demonstrated merely by deriving resource requirements. The few-nanometer nonaffine-coordinate and approximately `1e-4 degree` irregular-phase scales remain derived design requirements, and the baseline-model covariance requirement must eventually be demonstrated in a credible calibration architecture.

## Privacy rule

Pseudonymity is the default. Any author name, pseudonym, affiliation, email, location, signature, or other identifying metadata requires explicit approval for that specific artifact. Prior appearance is not continuing consent.

See root `PRIVACY_PROTOCOL.md`.

## Separate geometry result

The realistic finite-electrode/depletion calculation remains separately auditable in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
MANUSCRIPT_REV3_GEOMETRY_INTEGRATION_PLAN_2026-08-11.md
```

It continues to qualify mechanism assignment but is not a calibrated device prediction and does not authorize compression of manuscript content.

## Mandatory rule

Before any manuscript edit, read:

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. `MANUSCRIPT_BASELINE.md`;
4. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
5. this file;
6. `CURRENT_STATE_LIVE.md`;
7. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
9. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;
10. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identify only when explicitly approved by the user.**
