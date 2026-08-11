# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the recovered **16-page Rev. 3** by Terence Fisher, immediately before the realistic 2-D geometry hardening result.

Do **not** use `MANUSCRIPT_DRAFT.tex` as the current source merely because it is an older plain-text file already present in the repository.

## Exact source

The exact source is preserved in six repository text parts:

```text
manuscript_history/Fisher_Spectral_Depth_Closure_Paper_REV3_2026-08-11.tex.gz.b64.part01
...
manuscript_history/Fisher_Spectral_Depth_Closure_Paper_REV3_2026-08-11.tex.gz.b64.part06
```

For normal manuscript work, recover the exact editable source with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor will refuse to write a working source unless both hashes and the line count match the audited baseline. The recovered source must verify as:

```text
source SHA-256 = 76a3c5c0d26734773a5c60151e005f9b11225fa337520cb18eb358064fb48ad4
gzip SHA-256   = 2732f2b64887c8694baddec54621795464ca4492f5b6f6d31de21ae738e6b29d
lines = 696
pages in matching compiled PDF = 16
author = Terence Fisher
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

`MANUSCRIPT_CURRENT.tex` is a recovered working copy of the immutable baseline snapshot. Do not reconstruct it from notes or copy an older `MANUSCRIPT_DRAFT.tex` over it. When a new manuscript revision is approved, preserve a new immutable snapshot and update the baseline metadata before changing the canonical pointer.

## Newer geometry result

The realistic finite-electrode/depletion calculation is recorded separately in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
MANUSCRIPT_REV3_GEOMETRY_INTEGRATION_PLAN_2026-08-11.md
```

Those files extend/qualify the 16-page baseline. They do not authorize replacement or compression of unrelated manuscript content.

## Mandatory rule

Before any manuscript edit, read:

1. root `AGENTS.md`;
2. `MANUSCRIPT_BASELINE.md`;
3. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
4. this file;
5. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**
