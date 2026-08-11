# Manuscript Rev5 preservation report

**Date:** 2026-08-11  
**Candidate:** `MANUSCRIPT_REV5_ANON_2026-08-11.tex`  
**Base:** canonical anonymous Rev4 (`MANUSCRIPT_REV4_ANON_2026-08-11.tex`)

## Structural comparison

```text
Rev4 -> Rev5 source lines:       817 -> 863
compiled pages:                  19 -> 21
sections:                        12 -> 12
subsections:                     18 -> 18
bibliography items:              11 -> 11
equation environments:           87 -> 92
existing sections removed:        0
existing subsections removed:     0
references removed:               0
prior Rev4 lines changed/removed: 19 / 817 = 2.33%
```

The Rev5 edits are additive/surgical. No established section spine, subsection, reference, or unrelated derivation is removed.

## Exact candidate

```text
source SHA-256: 9d9c4686a152dcdbbfebae1db00a22f5cfd743b5948f825e79ba2acd75b812fb
source bytes: 59803
source lines: 863
compiled pages: 21
author metadata: Anonymous
PDF author metadata: Anonymous
```

Deterministic gzip snapshot:

```text
gzip SHA-256: ef1a05707690753bd3affd24909e1bedf6ad0681e409f09f92e479d6c0d22a65
gzip bytes: 20758
base64 parts: 6
```

## Scientific scope of changes

Rev5 responds only to the post-Rev4 adversarial review:

- quantifies low-RF coalescence of the weighting-field and transport multipliers;
- quantifies the complementary five-color annihilation penalty;
- adds a branch-free finite-boundary multiplier-product test and explicit rank-two branch/permutation discipline;
- renames the inherited HgCdTe field law accurately as a field-rolloff sensitivity law;
- includes same-optics baseline uncertainty in the covariance/nuisance budget;
- adds the confluent DC limit and single-log closure definition;
- removes notation overloading of `q` as local slowness;
- clarifies that extreme calibration numbers are design requirements, not demonstrated experimental performance;
- removes an internal audit-status sentence from Ref. 11 while retaining the unresolved priority boundary in the paper and repository audit record.

No reported HgCdTe closure values are changed.

## PDF QA

The 21-page PDF was compiled twice with `pdflatex`, rendered page-by-page, and visually inspected. No clipping or overlap was observed. The rank-two branch protocol, weighting-mode tradeoff table, one-log closure definition, HgCdTe rolloff language, baseline covariance equation, nuisance table, discussion, and bibliography were checked explicitly.
