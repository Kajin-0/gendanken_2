# Manuscript Status - AJP Revision 3 Addendum

**Date:** 2026-08-13  
**Status:** science frozen; two adversarial review cycles incorporated; AJP submission package production complete

This addendum supersedes the workflow status in the older `MANUSCRIPT_STATUS.md` without deleting that history.

Current authoritative review stack:

- scientific base: `MANUSCRIPT_REV2.md`
- internal Rev. 3 review: `MANUSCRIPT_REVIEW_ROUND3.md`
- venue/final qualification: `MANUSCRIPT_REV3_FINAL_REVIEW.md`
- first external AJP-review disposition: `MANUSCRIPT_AJP_REV2_REVIEW_DISPOSITION.md`
- fresh AJP Rev. 3 review: `MANUSCRIPT_AJP_REV3_FRESH_REVIEW.md`

The external review first strengthened the embedding argument from preserve/discard to the partial-replacement family

```math
\mathcal T_\lambda(\rho)=\lambda\rho+(1-\lambda)\sigma_0,
```

with

```math
\mathcal D_\lambda=\lambda\mathcal D_Q,
\qquad
P_e(\lambda)=\frac12(1-\lambda\mathcal D_Q).
```

A fresh adversarial review then identified a residual precision issue: under the minimal criterion `P_e < 1/2`, every `lambda > 0` remains nontrivially informative. AJP Revision 3 therefore uses a declared task requirement. For `D_Q=0.30` and `P_e <= 0.40`,

```math
\lambda_c=\frac23.
```

Two nondegenerate embeddings now lie on opposite sides of the same task threshold:

```text
lambda = 0.80 -> P_e = 0.38 -> PASS
lambda = 0.50 -> P_e = 0.425 -> FAIL
```

Both preserve nonzero optical-hypothesis information; the active material and microscopic transduction channel are identical. The argument therefore no longer relies on complete erasure or a disconnected readout.

AJP-specific compression in Revision 3:

- main manuscript reduced to about 4,725 words and 18 review-format pages;
- `architecture-dependence proposition` rhetoric replaced by `same-material embedding argument/result`;
- `lambda` explicitly identified as a channel mixing weight / trace-distance contraction factor, not a universal fraction of information;
- first-transfer-lobe caveat added to the Tavis-Cummings `N_min` example;
- Blackwell/Buscemi/Jencova/quantum-network comparison material removed from the main AJP article but retained in the internal prior-art audit;
- reduced semiconductor geometry example moved to one-page supplementary material;
- abstract and subtitle simplified for a broad AJP audience.

Scope lock remains unchanged: no claim of a new POVM/instrument formalism, universal detector theory, universal atom-number bound, universal per-click thermodynamic cost, solution to the measurement problem, or replacement scalar for standard detector figures of merit.

No further Experiment-02 physics is recommended before external editorial/referee feedback.