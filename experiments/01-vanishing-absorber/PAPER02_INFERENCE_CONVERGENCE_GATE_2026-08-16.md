# Paper 02 inferential convergence gate — 2026-08-16

**Status:** OPEN — EXECUTION REQUIRED  
**Epistemic class:** methodological hardening; no new physical claim until the executable gate passes  
**Manuscript consequence:** Rev. 3 remains the frozen reviewable manuscript. Rev. 4 must not be frozen from the current numerical values until this gate is resolved.

## Why this gate was added

The original two-dimensional geometry stress calculation contained a coarse/fine numerical check on the four-color closure phase. That check is no longer sufficient for Paper 02.

The current paper's headline counterexample is nonlinear and inferential: a deterministic planar depletion-field surrogate with microscopic diffusion fixed to zero is passed through finite wavelength-dependent generation kernels and then interpreted with the wrong homogeneous drift-diffusion inverse. The inverse returns an apparent positive `D_eff`.

Therefore the quantity that must converge is the **inferred transport result and its causal/statistical diagnostics**, not merely the raw closure phase.

## Exact numerical axes

The executable gate is

`numerics/paper02_inference_convergence_gate.py`.

It changes one numerical coordinate at a time around the current baseline:

| coordinate | coarse | baseline | fine |
|---|---:|---:|---:|
| electrostatic / weighting mesh `(nx,nz)` | `(81,61)` | `(121,91)` | `(161,121)` |
| source quadrature `(nx_src,nz_src)` | `(9,31)` | `(13,41)` | `(17,61)` |
| trajectory step `ds` | `0.035 um` | `0.020 um` | `0.0125 um` |

This produces seven unique configurations because the same baseline is shared by all three refinement axes.

## Inferential quantities under test

For each configuration the gate executes the same kernel-aware root fit used in the Paper 02 frequency-law calculation and records:

1. same-frequency `D_eff` and `w_eff` at 100, 500, and 1000 MHz;
2. the joint low-band `D,w` fit;
3. the 100-MHz-anchored homogeneous-law residual at 1 GHz;
4. the maximum one-mode finite-kernel fit residual through 1 GHz;
5. the upstream point-source control, whose nominal source coordinates lie outside the depletion region;
6. the point-source positive control wholly inside the depletion region;
7. collection fraction and the exact-DC Shockley-Ramo identity error.

The point-source controls are deliberately included because numerical stability of `D_eff` alone would not establish stability of the causal split used by the paper.

## Predeclared pass tolerances

The hard decision uses the final refinement step, baseline -> fine. Coarse -> baseline is retained as a trend diagnostic but is not itself a gate because cancellation in a multistage nonlinear inverse can make convergence non-monotone.

- probe-frequency `D_eff`: <= 2% relative change;
- probe-frequency `w_eff`: <= 0.5% relative change;
- low-band `D`: <= 2% relative change;
- low-band `w`: <= 0.5% relative change;
- 1-GHz law residual: <= 0.002 absolute change;
- maximum one-mode kernel-fit residual through 1 GHz: <= `2e-5` absolute change;
- upstream point-control `D` change: <= 1% of the fine finite-kernel `D_eff(100 MHz)` scale;
- inside-depletion point-control `D`: <= 2% relative change;
- DC Ramo error: <= `1e-10`;
- collection fraction: >= 0.999.

Positive-`D` sign stability is also required for the finite-kernel 100/500/1000-MHz inversions and the inside-depletion point-source positive control, because the paper's counterexample specifically concerns a positive apparent diffusion coefficient generated from a microscopic `D=0` deterministic model.

## Interpretation boundary

A PASS would establish that the stated counterexample and its causal controls are numerically stable under these declared refinements of the present deterministic surrogate.

It would **not** establish:

- experimental feasibility;
- calibration of a real detector;
- uniqueness of the physical explanation in a real device;
- that the theoretical optical kernels are experimentally calibrated;
- that the chosen HgCdTe-like geometry corresponds to a specific published detector.

Accordingly, the correct wording for the current kernel treatment is:

> theoretical wavelength-dependent generation kernels supplied exactly to the inverse

not simply "calibrated kernels."

## Required evidence before closure

This gate moves from OPEN to CHECKED only when an actual execution produces all three persisted outputs with `overall_pass=true`:

- `numerics/results/paper02_inference_convergence_summary.json`
- `numerics/results/paper02_inference_convergence.csv`
- `numerics/results/PAPER02_INFERENCE_CONVERGENCE.md`

The workflow `.github/workflows/paper02-inference-convergence.yml` syntax-checks the complete calculation chain, executes the gate, and uploads these outputs as an artifact. A workflow definition or queued run is not evidence; only a completed successful numerical run is.
