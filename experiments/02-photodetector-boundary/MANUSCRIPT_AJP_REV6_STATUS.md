# AJP Revision 6 Status

**Date:** 2026-08-13  
**Status:** pre-submission polish complete; no new physics introduced

Revision 6 incorporates the residual minor-to-moderate points from a fresh hostile review of Revision 5. That review found no new blocking mathematical error and judged the remaining publication risk primarily editorial/pedagogical rather than technical.

## Formal/self-containment fixes

- The partial-replacement map is now written in explicitly linear CPTP form:

```math
\mathcal T_\lambda(X)=\lambda X+(1-\lambda)\operatorname{Tr}(X)\sigma_0.
```

For normalized density operators this reduces to the previous `lambda rho + (1-lambda) sigma_0` expression.

- Total-variation distance is defined explicitly for discrete outcomes, with the continuous analogue stated.
- The restricted-measurement error formula now states that arbitrary classical processing of the allowed measurement outcome is permitted.
- The Hz-domain Fourier convention is defined explicitly.
- The Gaussian `Q` function is defined explicitly.
- The `d ~ tau^(-1/2)` benchmark now explicitly holds equal area, short-event energy `E`, and low-frequency `D*` fixed.

## Detector-physics clarification

The `material -> device -> readout -> task` hierarchy is now explicitly a classification of **roles in the measurement model**, not an immutable ontology of physical parameters. Constitutive material quantities may themselves depend on operating-state variables such as temperature, field, carrier density, strain, and surface condition.

Immediately after the abstract replacement-channel example, the manuscript now gives a physical detector realization: the same photodiode/front-end operating point feeding either a low-noise sufficiently wide-band readout or a noisier/bandwidth-limited readout. This makes clear that the channel construction abstracts ordinary downstream loading/noise/filtering changes rather than inventing an exotic quantum scenario.

## Pedagogical-significance sharpening

The Introduction now states the manuscript's recurring teaching sequence explicitly:

```text
candidate microscopic boundary
-> counterexample
-> missing level or condition
-> conditional physical threshold
```

The hierarchy plus this sequence are identified as the principal pedagogical objects. The partial-replacement equation remains only one controlled demonstration.

A bridge before the two quantitative examples also states that both examples instantiate the same move: a universal threshold fails, the missing resources are specified, and a conditional threshold/scaling law emerges.

## Production

- Main review-format PDF: 13 US-letter pages.
- Supplement: one page.
- Figure 1 secondary text enlarged modestly for print resizing.
- PDF preflight clean: openable, unencrypted, text-based; no broken `textsuperscript` citation strings.
- No new references were added in Revision 6.

## Disposition

Revision 6 should not be expanded with additional theory. The remaining risk is whether AJP finds the pedagogical organization sufficiently illuminating, not a known physics or mathematical defect. A final cold read or actual journal feedback is now more informative than further internal derivation.

Experiment 01 remains untouched. PR #17 remains draft and must not be merged without explicit user instruction.