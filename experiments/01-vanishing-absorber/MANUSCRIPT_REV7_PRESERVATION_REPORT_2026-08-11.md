# Rev. 7 manuscript preservation report

## Candidate

```text
source: MANUSCRIPT_REV7_ANON_2026-08-11.tex
source SHA-256: 9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8
source bytes: 75182
source lines: 963
compiled pages: 24
author: Anonymous
PDF author metadata: Anonymous
```

Deterministic gzip snapshot:

```text
gzip SHA-256: 8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b
gzip bytes: 26026
snapshot parts: 6
```

## Preservation comparison

```text
Rev. 6 -> Rev. 7
source lines:                    924 -> 963
compiled pages:                  22 -> 24
sections:                         12 -> 12
subsections:                      18 -> 18
bibliography items:               13 -> 19
equation environments:            99 -> 102
existing sections removed:         0
existing subsections removed:      0
references removed:                0
prior Rev. 6 lines changed/deleted: 63 / 924 = 6.82%
```

The 6.82% prior-line replacement/deletion fraction is below the repository's 15% destructive-edit alarm threshold. The candidate is longer, preserves all required section/subsection structure, adds equations and primary/classical references, and does not require a destructive-edit justification.

## Scientific scope of edits

Rev. 7 changes only material motivated by the post-Rev. 6 adversarial review:

- classical Prony/ESPRIT/matrix-pencil attribution;
- electron-affinity-anchored HgCdTe band-edge force;
- graded small-signal recombination sensitivity stress;
- propagated HgCdTe conditioning/resource/nuisance numbers;
- 1-D weighting-field interpretation boundary;
- early sequential-statistics disclaimer;
- experimental architecture paragraph;
- four editorial defects.

Unrelated derivations and the 12-section manuscript spine were preserved.

## Numerical validation

`rev7_review_regression.py` independently verifies:

- local electron-driving fraction 0.6657-0.6945;
- path-harmonic drift 2.2220e4 m/s;
- optical wavelengths / absorbed fraction;
- finite-width closure excess -0.0220167, -0.0546244, -0.1064448, -0.1942321 deg at 100, 250, 500, 1000 MHz;
- independent adaptive-shooting agreement better than 1e-5 degree at 100, 500, 1000 MHz;
- graded 5-us-anchored activated recombination change below 4e-7 degree over 0.1-1 GHz;
- 90.9/82.9/77.1/71.4 dB 3-sigma current-step resources;
- phase and coordinate calibration stresses;
- 1-D weighting-field thresholds;
- 5.85 GHz conditioning optimum.

Local regression result: **PASS**.

## PDF QA

The candidate was compiled twice with `pdflatex`, rendered page-by-page, and visually inspected.

```text
pages: 24
page size: US Letter
PDF author metadata: Anonymous
LaTeX fatal errors: 0
undefined references/citations after second pass: 0
overfull boxes after second pass: 0
```

All 24 rendered pages were checked for clipping, overlaps, broken equations, and broken glyphs. The revised abstract, hierarchy discussion, HgCdTe force/recombination pages, prediction/resource tables, nuisance table, discussion, conclusion, and expanded bibliography render cleanly.

## Privacy

No identifying author metadata was introduced. Visible author and embedded PDF author remain `Anonymous`. Scientific revision does not authorize identity disclosure.

## Canonicalization rule

This candidate must first be judged by the repository preservation/privacy workflows against canonical Rev. 6. Only after that scientific PR passes and merges may the manifest, extractor, recovery documentation, and current-state pointers be changed to Rev. 7 in a separate pointer-only PR.
