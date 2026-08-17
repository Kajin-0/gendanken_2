# Paper 02 — Rev. 9 targeted adversarial-response ledger

**Date:** 2026-08-16  
**Status:** REV. 8 FROZEN / REV. 9 TARGETED CANDIDATE / FULL GATE PENDING

## Trigger

An independent extreme adversarial re-review of the compiled Rev. 8 main manuscript and supplement found no blocking technical flaw and recommended a minor-to-moderate targeted revision before submission. Rev. 8 remains immutable provenance and canonical until the Rev. 9 gate passes.

## Required targeted repairs

### R9-1 — Link Eq. (10) explicitly to the finite-support reference response

The reference response `H0=A+B exp(rz)` in the finite-support theorem must be identified as the analytic continuation of the actual upstream affine-plus-exponential solution, not necessarily the response of a globally uniform physical device. For the central downstream-heterogeneity construction, use `A=v0/(i omega L)`, `B=C(omega)`, and `r=i omega/v0`, making `delta H=0` exactly on the uniform upstream interval.

### R9-2 — Make the pair-aware audit independently interpretable

The supplement must state the seven core countercarrier speed ratios, the three RF frequencies, the two-mode finite-kernel model, complex-amplitude profiling, root branch/bounds/multistart convention, quantitative instability of the free two-root fit, and the complete 21-case known-countercarrier-root sign matrix. The sole positive known-countercarrier core case must be identified explicitly.

### R9-3 — State the multi-frequency residual degrees of freedom

For `n` frequencies, document the exact conventions:

- root space: `2n` real root coordinates minus two real global parameters -> `nu_root=2n-2`;
- full channel: `12n` real quadratures minus `4n` real per-frequency nuisance coordinates and two real global parameters -> `nu_full=8n-2`;
- fixed heterogeneous alternative evaluated with the corresponding noncentral chi-square distribution using the same residual dimension.

The 3-GHz reversal must be described as test-specific power, not as an information-ordering claim.

### R9-4 — Update Figure 5

The upper panel must show both root-space and direct full-channel rejection thresholds. The caption must state why full channel is stronger at intermediate bandwidth and why root space can have slightly greater power against this particular alternative at 3 GHz despite compression.

### R9-5 — Give one concrete physical unipolar context

Add one carefully scoped example of a real photodetector architecture where strongly carrier-asymmetric transport is deliberately engineered. A uni-traveling-carrier photodiode is acceptable as an existence example only; the manuscript must not imply that the conditional planar surrogate is a UTC-PD device model.

## Non-goals

- Do not broaden the theorem back to a generic electron-hole photodiode transient.
- Do not add a self-consistent HgCdTe device simulation merely for editorial realism.
- Do not reopen already passed covariance, kernel-ablation, exact-continuum, or numerical-convergence gates unless a Rev. 9 edit touches their scientific content.
- Do not make a superlative priority claim.

## Promotion rule

Rev. 9 may replace Rev. 8 as canonical only after: fresh recomputation of the pair/full-channel claim-affecting outputs; exact table/threshold guards; regenerated Figure 5; successful main and supplement compilation with resolved references; rendered inspection; and preservation of anonymous submission-facing text.
