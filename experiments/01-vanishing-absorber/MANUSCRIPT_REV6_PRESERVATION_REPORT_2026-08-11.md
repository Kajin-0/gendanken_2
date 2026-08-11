# Manuscript Revision 6 preservation report — 2026-08-11

## Baseline

Validated canonical predecessor:

```text
MANUSCRIPT_REV5_ANON_2026-08-11.tex
SHA-256: 9d9c4686a152dcdbbfebae1db00a22f5cfd743b5948f825e79ba2acd75b812fb
lines: 863
pages: 21
sections: 12
subsections: 18
bibliography items: 11
equation environments: 92
author/PDF metadata: Anonymous
```

## Revision 6 candidate

```text
MANUSCRIPT_REV6_ANON_2026-08-11.tex
SHA-256: 2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4
bytes: 67837
lines: 924
pages: 22
sections: 12
subsections: 18
bibliography items: 13
equation environments: 99
author/PDF metadata: Anonymous
```

Deterministic gzip snapshot:

```text
SHA-256: aa7ab9e3271599bf9cdaa5ef37618cb2b9757ee0e08c867303a83e06e61adb8e
bytes: 23386
```

## Preservation audit

```text
Rev5 -> Rev6 lines:                  863 -> 924
compiled pages:                       21 -> 22
sections:                              12 -> 12
subsections:                           18 -> 18
bibliography items:                   11 -> 13
equation environments:                92 -> 99
existing sections removed:             0
existing subsections removed:          0
references removed:                    0
prior Rev5 lines changed/removed:      21 / 863 = 2.43%
```

The edits are additive/surgical. No established theorem section, conditioning derivation, branch proposition, hot-state treatment, singular weighting-field theorem, source-coordinate analysis, or nuisance-budget logic was deleted.

## New scientific content

Revision 6 adds only the hostile-review targets:

1. post-detection covariance/conditioning for `P=W1/W0=q1q2` and the recurrence sum;
2. explicit separation of rank detection, parameter resolution, and physical-law discrimination;
3. explicit interpretation of the one-dimensional weighting field as an effective observation surrogate;
4. an HgCdTe band-edge-force sensitivity coordinate `xi` plus a 100-MHz point-source finite-diffusion sweep;
5. two adjacent primary OED references and a sharper prior-art distinction;
6. two-carrier identifiability and sequential-statistics qualifications;
7. explicit combined-physics blind synthetic validation as future work.

## PDF QA

The candidate was compiled twice with `pdflatex`, producing a 22-page PDF. Metadata reports:

```text
author: Anonymous
pages: 22
```

No overfull boxes were reported. The PDF was rendered page-by-page at 160 dpi and visually inspected, with specific checks of:

- pages 8-9: post-detection rank-two covariance and finite-boundary test;
- page 11: one-dimensional weighting-field surrogate language and low-RF table;
- page 17: `xi` force-partition sweep and baseline covariance;
- pages 19-21: nuisance/statistical/discussion/conclusion changes;
- page 22: expanded bibliography.

No clipping, overlap, broken equations, or metadata identity regression was found.

## Privacy

Visible authorship and PDF author metadata remain exactly:

```text
Anonymous
```

No identifying author information was added.
