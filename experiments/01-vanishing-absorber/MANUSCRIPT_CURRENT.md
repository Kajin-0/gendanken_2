# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the recovered **16-page Rev. 3**, immediately before the realistic 2-D geometry hardening result.

**Canonical author metadata:** `Anonymous`.

Do **not** use `MANUSCRIPT_DRAFT.tex` as the current source merely because it is an older plain-text file already present in the repository. Do not restore a real author identity from historical files, git history, account/profile information, or memory.

## Exact source

The exact pseudonymous source is preserved in two repository text parts:

```text
manuscript_history/MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part02
```

For normal manuscript work, recover the exact editable source with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor will refuse to write a working source unless both hashes, line count, and anonymous author metadata match the audited baseline. The recovered source must verify as:

```text
source SHA-256 = 3ba57ed7c7bbe264038ffa4e6eabfc1ea90c1075d4989d4075d2589352cf6d8c
gzip SHA-256   = e413c1be218f4f3d33611381b6407137169abafb6fc22a6087f33f77b3c2ae3e
lines = 696
pages in matching compiled PDF = 16
author = Anonymous
PDF author metadata = Anonymous
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

`MANUSCRIPT_CURRENT.tex` is a recovered working copy of the immutable baseline snapshot. Do not reconstruct it from notes or copy an older `MANUSCRIPT_DRAFT.tex` over it. When a new manuscript revision is approved, preserve a new immutable snapshot and update the baseline metadata before changing the canonical pointer.

## Privacy rule

Pseudonymity is the default. Any author name, pseudonym, affiliation, email, location, signature, or other identifying metadata requires explicit approval for that specific artifact. Prior appearance of identifying information is not continuing consent.

See root `PRIVACY_PROTOCOL.md`.

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

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. `MANUSCRIPT_BASELINE.md`;
4. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
5. this file;
6. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identify only when explicitly approved by the user.**
