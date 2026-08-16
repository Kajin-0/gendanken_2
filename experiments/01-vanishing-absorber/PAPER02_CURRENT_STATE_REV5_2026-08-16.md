# Paper 02 — Current State Rev. 5

**Date:** 2026-08-16  
**Status:** **ANONYMOUS REV. 5 PROMOTED / NUMERICALLY CONVERGED / COMPILED / HOSTILE REVIEW PASSED / NOT SUBMISSION-READY**  
**Supersedes for navigation:** `PAPER02_CURRENT_STATE_REV4_2026-08-16.md`  
**Preservation rule:** all earlier manuscript/state revisions remain frozen provenance.

## 1. Canonical manuscript package

Main source:

```text
PAPER02_MANUSCRIPT_REV5_ANON_2026-08-16.tex
blob d61023ee44b7a8b365cf15f6dce579dff4f8a045
```

Supplement source:

```text
PAPER02_SUPPLEMENT_REV5_ANON_2026-08-16.tex
blob 5b6499c24be70164ea25791e19d143f61197195b
```

Bibliography:

```text
PAPER02_REFERENCES_REV4.bib
```

The Rev. 5 build workflow is GitHub Actions run `31949546540`. The uploaded package artifact is `paper02-manuscript-rev5-package`, artifact id `9264292338`.

Compiled PDFs:

```text
main manuscript: 9 pages
SHA-256 041f818b43f9cd2062690400cd03e69a56c8f7e36663af690c7556ea69a3451e

supplement: 3 pages
SHA-256 eefd607ee9171ce987b3454cf37efac9ca2f03576d032a2410e0a4da94e4ce6a
```

The workflow completed figure regeneration, source transformation guards, anonymity/priority/statistical guards, BibTeX/reference resolution, manuscript compilation, supplement compilation, source persistence, and artifact upload.

## 2. Why Rev. 5 supersedes Rev. 4

Rev. 4 compiled but was not promoted because hostile physics review found that the planar Poisson parameter `Delta = 0.05 V` had been described too literally as an added terminal drop / average added field.

Rev. 5 repairs that interpretation without changing the theorem, numerical counterexample, covariance model, optical kernels, figure data, or same-frequency statistical ordering.

The corrected planar definition is

```text
V'' = 2 Delta / W_d^2
```

with fixed terminal potentials. For the declared `V_bias = 0.30 V`, `L = 7.6 um`, `W_d = 3.0 um`, `Delta = 0.05 V` stress:

```text
characteristic curvature-field scale Delta/W_d = 166.7 V/cm
curved-region field magnitude = 328.9–662.3 V/cm
curved-region mean field = 495.6 V/cm
uniform-bias field = 394.7 V/cm
exact regional mean-field increment = 100.9 V/cm
actual extra potential drop across that region relative to the uniform profile = 0.030263 V
```

Therefore `Delta` is a Poisson-curvature parameter under fixed endpoint potentials, not an independently added 0.05-V terminal voltage.

## 3. Inferential numerical convergence remains checked

The stricter inference-level convergence result from the Rev. 4 state remains controlling evidence.

Independent refinement of field mesh, source/kernel quadrature, and trajectory step reported `overall_pass=true` under predeclared tolerances. The field mesh is the limiting coordinate; baseline-to-fine changes in same-frequency `D_eff` are:

```text
100 MHz  1.648%
500 MHz  1.641%
1 GHz    1.633%
```

Source quadrature changes are approximately `3.3e-5–3.8e-5` relative and trajectory-step changes approximately `5.0e-6–8.2e-6` relative.

The upstream point-source control remains at numerical-zero diffusion scale while the inside-nonuniform-region positive control remains near `4.87e-3 m^2/s`.

This establishes numerical stability of the declared deterministic surrogate and inverse. It does not establish experimental calibration, experimental feasibility, or uniqueness of the mechanism in a real detector.

## 4. Claim boundary after hostile review

The canonical claim remains:

> In deterministic zero-microscopic-diffusion photodetector models, finite wavelength-dependent generation kernels that are treated as known by the inverse and overlap spatial velocity heterogeneity can produce a positive effective diffusion coefficient when the resulting Shockley–Ramo terminal-current response is interpreted through a homogeneous drift–diffusion model. Causal-support controls, local bias theory, and covariance-aware same- and multi-frequency tests distinguish parameter bias from practical model rejection.

Required optical-kernel wording:

> theoretical wavelength-dependent generation kernels supplied exactly to the inverse

No experimental kernel calibration is claimed.

Required priority posture:

```text
DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT
NO SUPERLATIVE PRIORITY CLAIM
```

## 5. Same-frequency statistical result — locked

Do not regress this ordering:

```text
100 MHz: one-mode rejection occurs before positive-D detection
500 MHz: positive-D detection occurs before one-mode rejection
1 GHz:  positive-D detection occurs before one-mode rejection
```

Thus there is no same-frequency hidden-risk interval at 100 MHz under the reference covariance, while conditional hidden-risk intervals exist at 500 MHz and 1 GHz.

## 6. Hostile review disposition

A post-build review inspected both persisted Rev. 5 sources and the rendered 9-page manuscript / 3-page supplement.

Passed checks:

- no identity leakage; both documents remain anonymous;
- no superlative priority language;
- no unresolved references/citations in the final build logs;
- no clipping, broken figures, or visibly corrupted equations in the rendered PDFs;
- theoretical-kernel knowledge is explicitly separated from experimental calibration;
- deterministic transport truth remains `D_micro = 0`;
- the Poisson-curvature parameter is no longer described as an independently added terminal voltage/field;
- the exact field values agree between main text and supplement;
- the convergence result is reported with its predeclared scope and does not get promoted into an experimental validation claim;
- the 100/500/1000-MHz same-frequency statistical asymmetry is preserved;
- the HgCdTe section is explicitly a scale/plausibility comparison, not a calibrated-device prediction.

**Disposition: PASS for promotion to canonical working manuscript.**

## 7. What remains open

Rev. 5 is reviewable but **not submission-ready**. The remaining highest-value work is not another cosmetic revision. It is:

1. a final exact prior-art / closest-collision audit focused on the combined attribution framework;
2. a stronger experimental-feasibility discussion or independent public-data confrontation if a defensible dataset can be found;
3. covariance/model-uncertainty stress beyond the intentionally simple equal-quadrature reference model;
4. optional independent numerical implementation / solver cross-check of the planar counterexample;
5. journal targeting and final submission-format cleanup only after the scientific blockers above are dispositioned.

Paper 01 / anonymous Rev. 9 remains untouched.
