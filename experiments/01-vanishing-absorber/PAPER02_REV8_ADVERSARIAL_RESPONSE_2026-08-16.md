# Paper 02 — Rev. 8 adversarial-response ledger

**Date:** 2026-08-16  
**Status:** REV. 7 FROZEN / SUBMISSION READINESS REOPENED / REV. 8 CANDIDATE NOT YET CREATED

## Trigger

A new independent extreme adversarial review of the compiled Rev. 7 manuscript + supplement concluded **major revision before submission while the central zero-microscopic-diffusion counterexample appears mathematically sound**.

Rev. 7 remains immutable provenance. This ledger governs new scientific work. No Rev. 8 manuscript source is to be created or promoted until the major physics checks below are dispositioned.

## Priority-ordered issues

### R8-1 — Carrier-species closure — MAJOR / OPEN

The current point-source Shockley–Ramo transfer is a single-mobile-carrier / unipolar contribution. Rev. 7 does not scope this sharply enough while discussing photogenerated carriers broadly.

Required work before prose revision:

1. derive the exact planar two-carrier terminal transfer with correct charge/velocity signs;
2. verify the dc full-collection identity for an electron–hole pair;
3. add an exact-continuum pair stress in which the heterogeneous downstream carrier retains the Rev. 7 velocity profile and the counterpropagating carrier has independently controlled velocity;
4. sweep the second-carrier velocity ratio broadly and determine whether the apparent-positive-diffusion mechanism survives, changes sign, or becomes non-identifiable;
5. include limiting one-carrier/unipolar behavior explicitly.

Decision rule: if positive apparent diffusion survives a physically coherent two-carrier family, Rev. 8 may broaden only to that checked family. If not, the manuscript must narrow its claim to a unipolar/single-mobile-carrier observable.

### R8-2 — Mean-upstream versus genuinely weak-tail coupling — MODERATE/MAJOR / OPEN

Rev. 7 demonstrates that all kernel means may lie upstream while finite support in the heterogeneous region drives the bias, but the deepest baseline kernel has substantial direct overlap. The stronger word `remote` is therefore not yet justified by the baseline alone.

Required stress: construct a family with maximum heterogeneous-region probability at or below 5%, preferably also 1%, while preserving enough spectral channel diversity to perform the same inverse. Measure apparent D, inverse conditioning, and model residual. If a meaningful effect survives, retain carefully quantified weak-tail language; otherwise replace `remote` with `finite-support coupling to a mean-upstream heterogeneous region` or equivalent.

### R8-3 — Exact upstream one-mode bridge — MODERATE / OPEN

For a uniform upstream region with velocity v0, derive explicitly

    dH/dz - i omega H/v0 = -1/L

and hence

    H(z,omega) = v0/(i omega L) + C(omega) exp(i omega z/v0)

for source positions upstream of the heterogeneous region. Downstream heterogeneity enters only through C(omega). This should explain analytically why upstream point sources remain an affine-plus-single-exponential sequence and return numerical-zero apparent diffusion although their trajectories subsequently cross the heterogeneous region.

### R8-4 — Exact planar continuum as primary numerical calculation — MODERATE / OPEN

Rev. 7 labels the mesh-free exact planar solution as a post-hoc cross-check. For Rev. 8, invert the presentation: exact continuum is primary for the full-contact planar result; the 2-D mesh/trajectory solver is an independent numerical reproduction/generalization check. Preserve the original predeclared convergence record as provenance but do not present a nonmonotonic mesh sequence as the preferred central value when an exact solution is available.

### R8-5 — Root-space versus full-channel multi-frequency rejection — MODERATE / OPEN

Rev. 7 multi-frequency thresholds are based on fitted roots and therefore discard same-frequency normal residual directions. Required work:

1. relabel the existing thresholds explicitly as `root-space multi-frequency rejection`;
2. implement a direct full-channel joint GLS/likelihood-ratio stress against the homogeneous transport manifold using the same declared covariance assumptions;
3. compare required SNR with the root-space test.

The full-channel result must not be claimed optimal outside the declared model/covariance family.

### R8-6 — Manuscript/reproducibility polish — OPEN

Before Rev. 8 compilation:

- remove phrases such as `hostile review` and internal failed-run/helper-history language from the scientific article and supplement; retain those details in repository provenance records;
- state the dB convention explicitly as S_dB = 20 log10 S for amplitude/RMS-channel SNR;
- add a defensible code-availability statement or remove unactionable raw workflow IDs from the submission-facing PDF; do not fabricate a DOI;
- preserve anonymity/privacy protocol.

### R8-7 — HgCdTe self-consistency/significance — OPEN / NOT A CORRECTNESS GATE

Rev. 7 intentionally uses one theoretical HgCdTe optical-kernel construction and a separate deterministic transport/electrostatic stress. This is acceptable for a systematic-error/theory paper if stated clearly, but it limits device-specific significance.

Potential high-value extension, only if it can be done without importing poorly justified material assumptions:

    x(z) -> Eg(z) -> electrostatic/band-gradient model -> ve(z), vh(z)
         -> gm(z) -> Jm(omega) -> D_eff

Do not force a nominally self-consistent HgCdTe device model using unvalidated mobility/field/recombination inputs merely to satisfy editorial realism.

## Results from Rev. 7 that remain accepted unless a new stress overturns them

- exact single-carrier point-source ODE;
- low-frequency tangent equivalence and cubic consistency condition;
- deterministic velocity-gradient sign result and weak-gradient apparent-diffusion law;
- independent linear/exponential acceleration/deceleration sign controls;
- finite-support leakage identity and bound;
- mean-preserving support ablation;
- profiled tangent/normal parameter-bias geometry;
- exact planar single-carrier continuum result;
- same-frequency conditional hidden-risk ordering under the stated exact-kernel covariance;
- structured-covariance robustness within the tested family;
- optical-model uncertainty and affine-depth null results.

## Revision rule

Do not create `PAPER02_MANUSCRIPT_REV8...` merely to change wording. First resolve R8-1. Then resolve R8-2 and R8-5, because they may alter scientific claims/numbers. Only after those gates pass should a deterministic Rev. 8 builder transform the frozen Rev. 7 sources and compile a candidate.
