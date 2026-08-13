# AJP Revision 5 Status

**Date:** 2026-08-13
**Status:** Revision 5 complete locally; manuscript science frozen pending fresh review/editorial feedback.

Revision 5 is a structural rewrite of the AJP manuscript rather than a patch to Revision 4.

## Main changes

- The pedagogical hierarchy is now `material -> device -> readout -> task`.
- The manuscript no longer treats `P_e < 1/2` as a definition of a photodetector. It means only that the accessible output is informative about the optical hypothesis. Actual pass/fail statements use an explicit task threshold `P_e <= epsilon`.
- The central claim is narrowed to: intrinsic material properties alone do not determine end-to-end photodetection performance across all measurement embeddings.
- The controlled comparison now holds the front-end/device input-output channel fixed, rather than implying that this channel is determined by bare material properties alone.
- The Tavis-Cummings integer-threshold error from Revision 4 is corrected. The finite-error first-lobe candidate requires an explicit integer feasibility condition; exact perfect discrimination is stated only through the exact phase condition, not through a ceiling formula.
- Restricted measurement accessibility is distinguished from unrestricted Helstrom trace distance.
- The data-processing statement is restricted to deterministic hypothesis-independent CPTP processing; postselected branches must be assessed together with success probability and the full outcome record.
- The absorption/QND and persistent-memory claims are narrowed to optical-hypothesis discrimination and persistent local memory in the light-sensitive element.
- The `D*` benchmark now explicitly states that the `tau^(-1/2)` scaling is not universal when dominant signal and noise experience the same transfer function or when the noise spectrum changes with lifetime/bandwidth.
- Foundational photodetection references were broadened to include Glauber and Kelley-Kleiner.
- Repetition and peripheral theory were compressed. The main review-format manuscript is now 12 pages; the semiconductor geometry example remains supplementary.

## Current title

**From Material Response to Photodetection**

*Separating Material, Device, Readout, and Measurement Task*

## Current disposition

Do not restore the broader Revision-4 language about universal `photodetector status` or `phase of matter`. Revision 5 intentionally avoids legislating ordinary device-physics terminology and instead distinguishes material response, device transduction, readout accessibility, and task-level performance.

A completely fresh adversarial review of Revision 5 is recommended before submission because the logical center changed substantially.

Experiment 01 remains untouched. PR #17 remains draft and must not be merged without explicit user instruction.