# Manuscript Status - Revision 3 / AJP Revision 2 Addendum

**Date:** 2026-08-13  
**Status:** science frozen; external adversarial review incorporated; submission production remains

This addendum supersedes the workflow status in the older `MANUSCRIPT_STATUS.md` without deleting that history.

Current authoritative manuscript/review stack:

- scientific base: `MANUSCRIPT_REV2.md`
- required Rev. 3 changes: `MANUSCRIPT_REVIEW_ROUND3.md`
- final qualification and venue disposition: `MANUSCRIPT_REV3_FINAL_REVIEW.md`
- canonical Rev. 3 pointer: `MANUSCRIPT_REV3_POINTER.md`
- external AJP adversarial-review disposition: `MANUSCRIPT_AJP_REV2_REVIEW_DISPOSITION.md`
- original canonical figure: `FIGURE_01_SAME_MATERIAL_EMBEDDING.svg`

The external review independently reported no physics or computational error and exposed one useful argumentative weakness plus one production defect.

The central embedding result is now strengthened from a binary preserve/discard construction to the continuous partial-replacement family

```math
\mathcal T_\lambda(\rho)=\lambda\rho+(1-\lambda)\sigma_0,
\qquad 0\le\lambda\le1,
```

which gives

```math
\mathcal D_\lambda=\lambda\mathcal D_Q,
\qquad
P_e(\lambda)=\frac12(1-\lambda\mathcal D_Q).
```

Thus completed-detection performance can vary continuously while the light-sensitive material subsystem and its microscopic transduction channel remain fixed. The previous complete-erasure construction is only the `lambda=0` endpoint.

The manuscript also now contains an explicit perfect-absorption/no-local-record construction, a narrow system-apparatus/decoherence prior-art connection, and an explicit statement that the eliminated material boundaries are informal Gedanken intuitions rather than positions attributed to particular authors.

Production correction: the AJP PDF had literal `textsuperscript...` citation strings caused by double-escaped LaTeX commands. These were corrected and the full 19-page PDF was recompiled, re-rendered, and visually checked.

Scope lock remains unchanged: no claim of a new POVM/instrument formalism, universal detector theory, universal atom-number bound, universal per-click thermodynamic cost, solution to the measurement problem, or replacement scalar for standard detector figures of merit.

Preferred manuscript route remains American Journal of Physics. No further Experiment-02 physics is recommended unless a genuinely new physical question is opened separately.