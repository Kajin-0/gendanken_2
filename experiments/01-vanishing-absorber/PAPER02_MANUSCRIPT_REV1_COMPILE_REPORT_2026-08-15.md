# Paper 02 — Rev. 1 Compile and Canonicalization Report

**Date:** 2026-08-15  
**Status:** **COMPILE PASSED / REFERENCE CHECK PASSED / READY TO DESIGNATE AS FIRST CANONICAL WORKING REVISION**

## Source

```text
experiments/01-vanishing-absorber/PAPER02_MANUSCRIPT_REV1_ANON_2026-08-15.tex
```

Bibliography:

```text
experiments/01-vanishing-absorber/PAPER02_REFERENCES.bib
```

The manuscript is anonymous by design and follows the root privacy protocol.

## CI validation

Workflow:

```text
.github/workflows/paper02-manuscript-rev1.yml
```

GitHub Actions run:

```text
run id 31919234397
job id 95097377610
```

Uploaded artifact:

```text
paper02-manuscript-rev1
artifact id 9255848579
```

The artifact exists only after the sequential workflow steps

1. LaTeX installation;
2. `latexmk -pdf -interaction=nonstopmode -halt-on-error`;
3. unresolved citation/reference grep gate;
4. PDF reporting;
5. artifact upload

have completed successfully. The successful artifact therefore records that the source compiled and that the workflow did not detect unresolved LaTeX citations or references.

The workflow also emits a PDF SHA-256 in the job log. The canonical research identity remains the version-controlled source plus this run/artifact pair; binary PDFs are deliberately not committed to the research branch.

## Scientific pre-canonicalization checks

Before designation as the first working revision, the draft was checked against the Paper-02 locks for:

- Fourier convention `e^{-i omega t}`;
- coordinate increasing toward the collecting electrode;
- `gamma=-r` distinction;
- homogeneous law `D gamma^2 + w gamma = kappa - i omega`;
- explicit `D_micro=0` versus fitted `D_eff` distinction;
- retention of the finite calibrated generation kernels;
- retention of the mean-preserving zero-overlap causal control;
- retention of independent acceleration/deceleration sign tests;
- retention of the profiled parameter-bias law;
- retention of the covariance-aware RF rejection criterion;
- conservative prior-art framing without `first`, `fundamental`, or universal priority language;
- published-HgCdTe discussion labeled as an order-of-magnitude scale comparison rather than a calibrated device prediction.

The central sign chain has also been rechecked independently:

```text
e^{-i omega t}
-> dH/dz = -1/L + i omega H/v(z)
-> downstream acceleration gives positive quadratic real exponent term
-> Re(gamma) > 0 for the accelerating cases
-> D = -omega Re(gamma)/[Im(gamma)|gamma|^2] > 0 because Im(gamma) < 0.
```

No sign inconsistency was found.

## Figure status

Rev. 1 uses compile-safe figure placeholders rather than committed binary figures. The underlying working plots and CSV datasets are frozen separately in the canonical figure artifact indexed by

```text
PAPER02_FIGURE_BUNDLE_INDEX_2026-08-15.md
```

with workflow run `31918929841` and artifact `9255770675`.

This separation is intentional: the manuscript source is version controlled, while figures remain reproducible from executable numerical source.

## Canonicalization decision

Rev. 1 is suitable to become the **first canonical working Paper-02 manuscript**.

This does **not** mean submission-ready.

The next step is an adversarial scientific/manuscript review. Any material correction produced by that review must be implemented in a new

```text
PAPER02_MANUSCRIPT_REV2_ANON_<date>.tex
```

rather than rewriting Rev. 1 in place.
