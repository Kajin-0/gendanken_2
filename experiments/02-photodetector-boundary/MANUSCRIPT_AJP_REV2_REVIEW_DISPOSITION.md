# AJP Manuscript Revision 2 - Adversarial Review Disposition

**Date:** 2026-08-13  
**Status:** review incorporated; no new broad novelty claim

The external adversarial review found no physics or numerical error. The useful comments were incorporated as follows.

## 1. Continuous partial-information embedding

The former preserve-versus-discard construction is now embedded in

```math
\mathcal T_\lambda(\rho)=\lambda\rho+(1-\lambda)\sigma_0,
\qquad 0\le\lambda\le1.
```

For fixed material output states,

```math
\mathcal D_\lambda=\lambda\mathcal D_Q,
```

and therefore

```math
P_e(\lambda)=\frac12(1-\lambda\mathcal D_Q).
```

A task requirement `P_e <= epsilon` needs

```math
\lambda\ge\frac{1-2\epsilon}{\mathcal D_Q}
```

when feasible. Thus completed-detection performance varies continuously while the material subsystem and microscopic transduction channel remain unchanged. The old total-erasure case survives only as the `lambda=0` endpoint.

## 2. Explicit absorption-not-sufficient construction

The manuscript now gives an explicit sequence

```math
|1\rangle_S|g\rangle_M|0\rangle_E
\to
|0\rangle_S|e\rangle_M|0\rangle_E
\to
|0\rangle_S|g\rangle_M|1\rangle_E.
```

Perfect intermediate absorption occurs, but the local material state at the declared readout can be identical under photon/no-photon hypotheses, so the local material trace distance can be zero. Information has been exported to `E`; measuring `E` would enlarge the architecture.

## 3. Scope and prior-art tightening

The introduction now states that the eliminated material boundaries are plausible informal intuitions invited by the Gedanken question, not positions attributed to particular authors.

A short system-apparatus/decoherence paragraph was added, with Zurek and Schlosshauer cited, while explicitly stating that the manuscript does not address unique outcome emergence or claim to solve the measurement problem.

The standalone claim-taxonomy section was compressed for AJP readability. Formal comparison theory remains optional background, not a prerequisite.

## 4. Production fix

The reviewer correctly identified literal `textsuperscript1`, `textsuperscript2,3`, etc. in the compiled AJP PDF. The LaTeX citation commands were double escaped. They have been corrected, the PDF recompiled, and the full document re-rendered for visual QA.

## 5. Suggestions intentionally not adopted

- No device-specific low-pass or threshold-discriminator model was added; the partial-replacement channel supplies the needed continuous non-degenerate degradation without creating a second device-specific theory problem.
- The Landauer discussion was not expanded.
- The decoherence connection was not expanded into a foundations section.
- No citation to a private/unpublished companion manuscript was added; use a stable public preprint/DOI if one later exists.

## Current scientific disposition

The review strengthened the argumentative core but did not change the experiment-level conclusion. Experiment 02 remains a conceptual/pedagogical synthesis grounded in established measurement theory. The architecture-dependence result is a photodetector-specific application, not a new general theorem of quantum information.