# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the anonymous **26-page Rev. 8**, validated against Rev. 7 before canonicalization.

**Canonical author metadata:** `Anonymous`.

Do **not** use `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, or historical Rev. 3/4/5/6/7 snapshots as the current source. Do not restore identifying author information from historical files, git history, account/profile information, public sources, or memory.

## Exact source

The canonical source is:

```text
MANUSCRIPT_REV8_ANON_2026-08-11.tex
```

and is preserved in seven repository snapshot parts:

```text
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part06
manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part07
```

Recover the exact editable baseline only with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor refuses to write a working source unless the snapshot hash, source hash, line count, and anonymous author metadata match:

```text
source SHA-256 = 28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9
gzip SHA-256   = 44af67c407d07b6e7d60bbc6760f14cbe0f44cf763a74e972a9b3322a5d8d2f7
bytes = 81816
lines = 1023
pages in matching compiled PDF = 26
author = Anonymous
PDF author metadata = Anonymous
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

Never reconstruct it from handoff notes or overwrite it with an older source.

## Rev. 8 status

Rev. 8 is a surgical correction of canonical Rev. 7. The hostile review was not followed mechanically: one theorem-level defect was accepted, several physical/numerical criticisms were narrowed and repaired, and suggestions that did not survive independent checking were not adopted as stated.

The critical model-order lock is:

```text
rank one rejected
-> rank-at-most-two determinant null tested
-> two-mode parameters resolved
-> physical root-law discrimination
```

For five first differences `d0...d4`, define the `3x3` Hankel matrix `H`. The unconditional six-color rank-at-most-two null is `det(H)=0`. The older scalar minor identity is no longer a general null because

```math
W1^2-W0W2 = -d2 det(H),
```

so it also vanishes spuriously when `d2=0`. Adjacent minors remain valid conditioning and parameter-recovery objects when nondegenerate.

Rev. 8 additionally locks in:

- a noise-aware covariance test for the complex Hankel determinant before rank-two root recovery;
- corrected finite-kernel weighting-field values: `0.002947 / 0.012140 / 0.010007 degree` false phase for 1% variation at 100 / 500 / 1000 MHz and allowable 10%-target variations `0.757% / 0.881% / 1.961%`;
- a dedicated differential recombination cross-check agreeing within about `3e-9 degree` across tested numerical environments;
- explicit separation of the electron-affinity-anchored composition-band-edge force from unknown self-consistent electrostatic drift;
- DOS/effective-mass sensitivity: `|v_DOS|/v_field ~= 8.8--18.3%` and a nontrivial `alpha_DOS` closure sweep;
- the nearly lossless two-carrier DC degeneracy, for which two or more nonzero RF frequencies may be required.

The worked finite-width HgCdTe closure remains approximately `-0.0220167 / -0.1064448 / -0.1942321 degree` at 100 / 500 / 1000 MHz. It remains a conditional composition-band-edge transport stress, not a calibrated device prediction.

Detailed audit:

```text
REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV8_PRESERVATION_REPORT_2026-08-11.md
numerics/rev8_review_regression.py
```

Rev. 7 and earlier revisions remain preserved historical provenance.

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
7. `REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
9. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
10. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;
11. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identify only when explicitly approved by the user.**
