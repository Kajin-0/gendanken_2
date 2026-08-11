# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the anonymous **21-page Rev. 5**, validated against Rev. 4 before canonicalization.

**Canonical author metadata:** `Anonymous`.

Do **not** use `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, or historical Rev. 3/Rev. 4 snapshots as the current source. Do not restore identifying author information from historical files, git history, account/profile information, public sources, or memory.

## Exact source

The canonical source is:

```text
MANUSCRIPT_REV5_ANON_2026-08-11.tex
```

and is preserved in six repository snapshot parts:

```text
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV5_ANON_2026-08-11.tex.gz.b64.part06
```

Recover the exact editable baseline with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor refuses to write a working source unless the snapshot hash, source hash, line count, and anonymous author metadata match:

```text
source SHA-256 = 9d9c4686a152dcdbbfebae1db00a22f5cfd743b5948f825e79ba2acd75b812fb
gzip SHA-256   = ef1a05707690753bd3affd24909e1bedf6ad0681e409f09f92e479d6c0d22a65
bytes = 59803
lines = 863
pages in matching compiled PDF = 21
author = Anonymous
PDF author metadata = Anonymous
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

Never reconstruct it from handoff notes or overwrite it with an older source.

## Rev. 5 status

Rev. 5 surgically addresses the post-Rev. 4 hostile review while preserving the existing paper spine. It adds:

```text
low-RF weighting/transport root-coalescence limit
branch-free rank-two finite-boundary multiplier-product test
two-root branch/permutation protocol
accurate HgCdTe field-rolloff terminology
same-optics baseline covariance and nuisance budget
confluent q -> 1 DC limit
single-log complex closure ratio
unambiguous local-slowness notation
```

The best-case weighting-mode rank-two resolution requirements are approximately:

```text
100 MHz -> 116.2 dB
500 MHz ->  88.4 dB
1 GHz   ->  76.7 dB
```

while the corresponding five-color exact-annihilation penalties are approximately:

```text
100 MHz -> 46.3 dB
500 MHz -> 32.3 dB
1 GHz   -> 26.4 dB
```

These expose a real low-RF tradeoff rather than invalidating the hierarchy.

Detailed audit:

```text
REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV5_PRESERVATION_REPORT_2026-08-11.md
numerics/rev5_review_regression.py
```

No reported HgCdTe closure value changed. Rev. 4 and Rev. 3 remain historical provenance.

## Priority blocker

The closest-looking 2024 graded-HgCdTe source has verified bibliographic metadata but has not yet been audited in full text. That task remains **OPEN** and must be completed before any submission-level priority/novelty claim. Related-paper searches do not substitute for reading that exact source.

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
7. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identify only when explicitly approved by the user.**
