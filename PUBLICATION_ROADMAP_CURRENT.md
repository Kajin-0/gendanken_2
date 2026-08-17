# Current Publication Roadmap

**State date:** 2026-08-17  
**Status:** **CURRENT PORTFOLIO POINTER / NON-CLAIM**  
**Supersedes for numbering and execution order:** `PUBLICATION_ROADMAP_2026-08-15.md`

The dated 2026-08-15 roadmap remains a historical audit and should not be rewritten as if its manuscript numbering were still current. The scientific results recorded there remain provenance; this file resolves the subsequent Paper 02 merge and the resulting portfolio renumbering.

## Current portfolio

| Track | Scientific object | Current state | Action |
|---|---|---|---|
| **Paper 01** | spectral-depth Shockley--Ramo closure / model-order falsification hierarchy | canonical anonymous Rev. 9 retained | finish submission blockers; do not casually rewrite manuscript |
| **Paper 02** | apparent diffusion from deterministic velocity gradients / transport identifiability | Rev. 9 referee-response manuscript merged to `main` through PR #18 | **FROZEN / submission preparation only unless a material scientific defect appears** |
| **Paper 03** | multidimensional geometry + combined ordinary detector physics as a false spectral-transport signature | predeclared blind challenge; Stage A under development in PR #19 | **ACTIVE DEVELOPMENT** |
| **Paper 04 candidate** | spatial first-passage semigroup / timing-cumulant null tests | exact probability object exists; detector-specific novelty unresolved | primary-source novelty gate before drafting |
| Future metrology | graded-HgCdTe spectral timing tomography | finite-kernel inverse exists | hold pending independent validation/data |
| Supporting only | hot-carrier rank-two closure, finite-width optical corrections, recombination/root-law hierarchy | mature supporting theory | keep with Paper 01 |
| Closed | broad Experiment-02 detector-process framework and thickness optimum | prior-art overlap / architecture dependence | no manuscript recommended |
| Provenance | early universal absorber/capture-bound routes | narrowed or invalidated by counterexample | do not resurrect universal claims |

## Renumbering map from the 2026-08-15 audit

```text
2026-08-15 Paper 01  -> current Paper 01
2026-08-15 geometry Paper 02 -> current Paper 03
2026-08-15 first-passage Paper 03 -> current Paper 04 candidate
newly merged transport-identifiability manuscript -> current Paper 02
```

Historical filenames such as

```text
numerics/paper02_geometry_parameter_sweep.py
.github/workflows/paper02-geometry-quick.yml
```

retain their names for provenance. Their `paper02` prefix reflects the portfolio numbering at creation time and does **not** make them part of the merged current Paper 02 manuscript.

## Paper 01 remaining scientific blockers

The current substantive blockers remain:

1. closest-source priority audit against the strongest technically adjacent graded-HgCdTe / spectral-depth work;
2. calibration feasibility for depth coordinate, common scale, phase, optical kernel, and shared composition nuisance;
3. blind combined-physics validation.

The third blocker is now being attacked through current Paper 03. A successful Paper 03 benchmark can therefore harden Paper 01 without being folded into the Paper 01 manuscript unless a revision is scientifically necessary.

## Paper 02 boundary

Paper 02 is the merged Rev. 9 transport-identifiability manuscript developed on PR #18. Its central object is the appearance of a positive effective diffusion coefficient when deterministic nonuniform velocity is fit by the wrong homogeneous drift-diffusion inverse.

No geometry/combined-physics development file should now be described as Paper 02 in new prose. Existing dated filenames are historical exceptions only.

No new Paper 02 revision should be created merely to synchronize portfolio bookkeeping.

## Paper 03 — active question

> When several ordinary detector-physics departures coexist in an independent multidimensional forward model, can they produce a mechanism-specific false transport interpretation that survives the existing spectral-depth hierarchy at the precision required for the claim?

The predeclared contract is

```text
experiments/01-vanishing-absorber/PAPER03_COMBINED_PHYSICS_CHALLENGE_2026-08-17.md
```

The governing rule is conservative falsification rather than forced diagnosis. A blind result such as

```text
rank > 2
mechanism unresolved
```

is valid if the inadequate lower-order interpretation has been rejected.

### Development stages

```text
Stage A
checked 2-D geometry
+ diffusion
+ recombination
+ exact discrete Shockley-Ramo increments
-> recovery / numerical-convergence gate

Stage B
charge-coupled semiconductor Poisson / drift-diffusion
+ explicit contacts / recombination
+ separate weighting-potential solve
-> independently validated synthetic detector

Stage C
blind hierarchy analysis
+ declared parameter map
+ measurement-noise/SNR comparison
+ materially different geometry family
-> Paper 03 GO / NO-GO
```

Stage A is not to be described as a self-consistent semiconductor solution.

## Paper 03 standalone GO / NO-GO

**GO** only if:

- the forward calculation passes recovery and convergence gates;
- the blind-analysis boundary is preserved;
- a broad ordinary regime supports either a robust early-warning hierarchy or a robust hidden-confound result;
- the decisive behavior survives a materially different geometry family;
- the result has an actionable observable/SNR consequence;
- focused prior-art review leaves a defensible contribution.

**NO-GO** if the result is a narrow rectangular-pixel sensitivity, collapses under refinement, or requires revealing the hidden generating mechanism to make the inverse work.

## Paper 04 candidate

The old Paper 03 first-passage/cumulant object is now Paper 04 candidate. The mathematical semigroup/cumulant structure is established probability theory; only a detector-specific experimental/falsification construction could justify a paper.

Do not draft it before the focused novelty audit against time-of-flight, transient-current, first-passage, inverse-Gaussian transit, subordinator/system-identification, depth-resolved impulse-response, and cumulant-based transport literature.

## Current execution order

```text
1. preserve Paper 01 and frozen Paper 02;
2. execute Paper 03 combined-physics Stage A recovery/convergence work;
3. build and independently validate Paper 03 Stage B self-consistent forward model;
4. run Paper 03 blind regime map and second-geometry-family test;
5. feed only defensible validation consequences back into Paper 01 submission readiness;
6. run the Paper 04 prior-art gate before any drafting;
7. keep timing tomography on hold for genuinely independent validation/data.
```

## Recovery rule

For portfolio-level continuation, read this file before the dated `PUBLICATION_ROADMAP_2026-08-15.md`. Use the dated audit for the detailed provenance of the geometry and first-passage seeds, but use this file for current numbering and execution order.

For Paper 03 development, then read:

1. `experiments/01-vanishing-absorber/PAPER03_COMBINED_PHYSICS_CHALLENGE_2026-08-17.md`;
2. `experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md`;
3. `experiments/01-vanishing-absorber/numerics/realistic_geometry_closure_stress.py`;
4. historical `experiments/01-vanishing-absorber/numerics/paper02_geometry_parameter_sweep.py`;
5. `experiments/01-vanishing-absorber/numerics/paper03_combined_physics_challenge.py`.

Existing privacy, pseudonymity, manuscript-preservation, and claim-discipline rules remain mandatory.