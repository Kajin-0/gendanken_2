# Paper 02 — Manuscript Preservation Protocol

**Status:** MANDATORY once an anonymous Paper-02 manuscript source exists.

This protocol is independent of the canonical Paper-01 / Rev. 9 preservation lock. Paper 02 must never overwrite, replace, or silently become the canonical Paper-01 manuscript.

## 1. Privacy default

Paper 02 follows the repository root privacy protocol.

Default manuscript author:

```text
Anonymous
```

Do not insert legal name, affiliation, contact information, identifying account handle, acknowledgments that reveal identity, or PDF metadata identifying the user unless explicitly authorized for this manuscript.

## 2. Canonical pointer

Read

```text
PAPER02_MANUSCRIPT_CURRENT.md
```

before editing any Paper-02 manuscript source.

The source named there is the canonical working manuscript.

Older revisions are immutable scientific provenance. Do not replace them with a newer revision under the old filename.

## 3. Mandatory reading order before manuscript edits

1. root `PRIVACY_PROTOCOL.md`;
2. `PAPER02_MANUSCRIPT_CURRENT.md`;
3. `PAPER02_CURRENT_STATE_REV3_2026-08-15.md` or a newer explicitly superseding state file;
4. `PAPER02_PRIORITY_CHECKPOINT_2026-08-15.md`;
5. `PAPER02_EXACT_PRIORITY_MATRIX_2026-08-15.md`;
6. `PAPER02_MANUSCRIPT_BLUEPRINT_2026-08-15.md`;
7. `PAPER02_NOTATION_LOCK_2026-08-15.md`;
8. `PAPER02_FIGURE_BUNDLE_INDEX_2026-08-15.md`;
9. exact theorem/result files only as needed.

Research logs and summaries are navigation aids, not manuscript source-of-truth text.

## 4. Revision rule

For a material manuscript change:

```text
PAPER02_MANUSCRIPT_REV1_ANON_2026-08-15.tex
PAPER02_MANUSCRIPT_REV2_ANON_<date>.tex
...
```

Create a new revision file rather than rewriting the previous revision in place once that revision has been designated by `PAPER02_MANUSCRIPT_CURRENT.md`.

Update the current pointer only after the new source has been checked for:

- section preservation;
- equation/sign consistency;
- citation boundary;
- numerical consistency against canonical datasets;
- privacy.

## 5. Scientific preservation

Do not silently remove:

- the distinction `D_micro=0` versus `D_eff`;
- the exact finite-kernel forward model;
- the mean-preserving zero-overlap control;
- the independent acceleration/deceleration sign test;
- the first-order parameter-bias result;
- the statistical distinction between structural and practical falsification;
- the explicit prior-art boundary.

If a later result invalidates one of these, preserve the old statement in the revision history and document why it was changed.

## 6. Claim discipline

The current priority checkpoint authorizes manuscript development around a **distinct integrated combination**, not a superlative novelty claim.

Without a later explicit priority upgrade, manuscript text must not state or strongly imply:

```text
first
first-ever
fundamental new mechanism
universal false diffusion
previously unknown transport law
```

Broad ingredients must be credited to the established OED, PIN/PDA, TOF, transient-current, and apparent-diffusion lineages.

## 7. Numerical source discipline

Main numerical values must trace to:

- the canonical figure/data bundle indexed in `PAPER02_FIGURE_BUNDLE_INDEX_2026-08-15.md`;
- or a newer explicitly canonicalized workflow artifact.

Do not reconstruct manuscript numbers by copying prose from older development notes when executable source or canonical CSV data exist.

## 8. Notation discipline

`PAPER02_NOTATION_LOCK_2026-08-15.md` controls:

- coordinate orientation;
- Fourier sign;
- `r` versus `gamma`;
- `D_micro` versus `D_eff`;
- kernel/support notation;
- statistical notation.

Any notation change must update the notation lock first and document the reason.

## 9. Relation to Paper 01

Paper 02 may cite or discuss the general spectral-depth hierarchy conceptually, but it must not modify or claim to supersede the anonymous Rev. 9 manuscript.

If the Paper-02 result is later integrated into Paper 01 as an adversarial qualification, that must occur in a separate Paper-01 manuscript revision under the Paper-01 preservation protocol.

## 10. Preserve first

Default rule:

> **Preserve the last canonical revision; create a new revision for material changes; narrow claims rather than deleting inconvenient evidence.**
