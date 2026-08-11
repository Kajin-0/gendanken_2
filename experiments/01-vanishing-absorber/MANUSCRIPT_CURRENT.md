# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the anonymous **19-page Rev. 4**, validated against Rev. 3 before canonicalization.

**Canonical author metadata:** `Anonymous`.

Do **not** use `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, or the historical Rev. 3 snapshot as the current source merely because they are older repository files. Do not restore a real author identity from historical files, git history, account/profile information, or memory.

## Exact source

The exact canonical source is tracked as:

```text
MANUSCRIPT_REV4_ANON_2026-08-11.tex
```

and preserved in three repository snapshot parts:

```text
manuscript_history/MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV4_ANON_2026-08-11.tex.gz.b64.part03
```

For normal manuscript work, recover the exact editable baseline with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor will refuse to write a working source unless both hashes, line count, and anonymous author metadata match the audited baseline. The recovered source must verify as:

```text
source SHA-256 = 9da8c6094a58109873382b6b3c73c519b26f519e327f5ec8058009bc4896df00
gzip SHA-256   = fad3aeee778de42a7c9de278abec5676d6fb3d0effebd4994c7bbdb0950a3f68
lines = 817
pages in matching compiled PDF = 19
author = Anonymous
PDF author metadata = Anonymous
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

`MANUSCRIPT_CURRENT.tex` is a recovered working copy of the immutable canonical snapshot. Do not reconstruct it from notes or copy an older source over it.

## Rev. 4 status

Rev. 4 surgically addresses the latest hostile review while preserving the existing paper spine. The central four-color multiplier closure is unchanged. The revision adds branch control for physical inversion, fixes the singular DC/no-recombination weighting-field case, corrects arbitrary-spacing uniqueness language, quantifies non-common calibration stresses, makes the HgCdTe transport prescription explicit, adds covariance-aware falsification language, and includes one conceptual hierarchy figure.

Detailed audit:

```text
REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV4_PRESERVATION_REPORT_2026-08-11.md
numerics/rev4_critique_regression.py
```

Rev. 3 remains preserved as historical provenance but is not the current manuscript.

## Privacy rule

Pseudonymity is the default. Any author name, pseudonym, affiliation, email, location, signature, or other identifying metadata requires explicit approval for that specific artifact. Prior appearance of identifying information is not continuing consent.

See root `PRIVACY_PROTOCOL.md`.

## Separate geometry result

The realistic finite-electrode/depletion calculation remains deliberately separate in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
MANUSCRIPT_REV3_GEOMETRY_INTEGRATION_PLAN_2026-08-11.md
```

Those files extend/qualify the manuscript but were **not** integrated into Rev. 4 as a calibrated device claim. They do not authorize replacement or compression of unrelated manuscript content.

## Mandatory rule

Before any manuscript edit, read:

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. `MANUSCRIPT_BASELINE.md`;
4. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
5. this file;
6. `CURRENT_STATE_LIVE.md`;
7. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identify only when explicitly approved by the user.**
