# Manuscript Status Addendum — Current AJP Revision 5

**Date:** 2026-08-13  
**Current status:** Revision 5 is the authoritative pre-submission manuscript state. Science is frozen pending a fresh adversarial review and external editorial/referee feedback.

This file preserves the earlier Revision-3/4 route while updating the repository pointer. The detailed current Revision-5 state is recorded in `MANUSCRIPT_AJP_REV5_STATUS.md`.

## Current authoritative manuscript direction

Revision 5 is a structural rewrite rather than a patch. Its principal pedagogical hierarchy is

```text
material -> device -> readout -> task
```

The central claim is deliberately narrow:

> Intrinsic material properties alone do not determine end-to-end photodetection performance across all measurement embeddings.

Revision 5 does not attempt to define which component deserves the ordinary device-physics noun `photodetector`. It distinguishes material response, device transduction, readout accessibility, and task-level performance.

The manuscript now uses `P_e < 1/2` only to mean that an accessible output is informative about an optical hypothesis. Detector-performance pass/fail statements require an explicit task criterion such as `P_e <= epsilon`.

## Mandatory mathematical correction incorporated in Revision 5

The earlier Tavis-Cummings perfect-discrimination ceiling formula was incorrect. Revision 5 removes it.

For

```math
P_e(\tau)=\frac12\cos^2(g\tau\sqrt N),
```

a first-lobe finite-error requirement gives the integer candidate

```math
N_c=\left\lceil
\left[
\frac{\arcsin\sqrt{1-2\epsilon}}{g\tau}
\right]^2
\right\rceil,
```

only when

```math
g\tau\sqrt{N_c}\le\frac{\pi}{2}.
```

Otherwise no integer first-lobe solution exists. Exact perfect discrimination requires the exact phase condition

```math
g\tau\sqrt N=\frac{(2k+1)\pi}{2},
```

and cannot be obtained by rounding an arbitrary real-valued `N` upward.

## Other Revision-5 corrections

- The controlled object is the fixed front-end/device channel, not bare material alone.
- Restricted physically allowed measurements are distinguished from unrestricted Helstrom-optimal measurements.
- Data-processing language is restricted to deterministic hypothesis-independent CPTP processing; postselection must include success probability and the full outcome record.
- Absorption/QND wording is narrowed to obtaining distinguishable optical-hypothesis outcomes rather than legislating the word `photodetection`.
- Persistent-memory claims explicitly refer to persistent local memory in the light-sensitive element.
- The one-pole `D*` benchmark explicitly states that `d ~ tau^(-1/2)` is not universal when signal and dominant noise share the same transfer function or when the noise spectrum changes with lifetime/bandwidth.
- Foundational photodetection references were broadened to include Glauber and Kelley-Kleiner.
- Main review-format manuscript length was compressed from 18 pages to 12 pages; the semiconductor geometry example remains supplementary.

## Preserved earlier review path

The prior files remain part of the research record and should not be deleted:

- `MANUSCRIPT_REV2.md`
- `MANUSCRIPT_REVIEW_ROUND3.md`
- `MANUSCRIPT_REV3_FINAL_REVIEW.md`
- `MANUSCRIPT_AJP_REV2_REVIEW_DISPOSITION.md`
- `MANUSCRIPT_AJP_REV3_FRESH_REVIEW.md`
- `MANUSCRIPT_AJP_REV4_FINAL_DISPOSITION.md`
- `MANUSCRIPT_AJP_REV5_STATUS.md`

Earlier partial-replacement work remains valid as an illustrative readout example:

```math
\mathcal T_\lambda(\rho)=\lambda\rho+(1-\lambda)\sigma_0,
\qquad
\mathcal D_\lambda=\lambda\mathcal D_Q,
\qquad
P_e(\lambda)=\frac12(1-\lambda\mathcal D_Q).
```

However, Revision 5 no longer presents this as the manuscript's principal theoretical result. It is one demonstration inside the broader material/device/readout/task teaching framework.

## Repository controls

Experiment 01 remains untouched. Experiment 02 remains isolated on draft PR #17. Do not merge PR #17 without explicit user instruction.