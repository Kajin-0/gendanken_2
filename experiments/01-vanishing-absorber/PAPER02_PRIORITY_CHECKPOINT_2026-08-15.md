# Paper 02 — Priority Checkpoint

**Date:** 2026-08-15  
**Status:** **DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT / NO SUPERLATIVE PRIORITY CLAIM / MANUSCRIPT BLUEPRINT AUTHORIZED**

## Decision

The focused audit has reached the point where continued broad keyword searching has diminishing scientific value.

The current evidence supports a conservative publication posture:

```text
Broad transport phenomenon novelty:        NO
Wavelength-dependent RF photodiode physics: NO
Field-inhomogeneity inference bias:         NO
effective/apparent diffusion as a generic
inverse-model artifact:                     NO

Detector-specific integrated result:        DISTINCT COMBINATION SUPPORTED BY FOCUSED AUDIT
"first" / "fundamental" / universal claim: NOT AUTHORIZED
Standalone theory manuscript blueprint:     GO
Submission-level priority claim:            HOLD pending final source-by-source review during drafting
```

This is deliberately weaker than `NOVEL` and stronger than `PRIORITY UNPROVEN`.

It means the research is sufficiently differentiated to justify writing a manuscript around the **specific integrated result**, while the manuscript must avoid superlative priority language and must preserve the closest prior art as explicit boundary conditions.

---

## Exact candidate contribution

Safe working statement:

> We analyze a material-attribution failure mode in wavelength-resolved photodetector transport measurements. Finite calibrated generation-depth kernels can couple spatially remote deterministic velocity heterogeneity into a Shockley-Ramo terminal-current response that is locally consistent with positive homogeneous diffusion even when microscopic diffusion is zero. We derive support- and conditioning-based bias bounds, isolate the mechanism with zero-overlap and mean-preserving controls, and quantify the RF bandwidth/precision required to reject the false homogeneous model.

This statement describes what the present work actually demonstrates without asserting chronological priority.

---

## Claims that remain forbidden

Do not write:

```text
first demonstration that electric fields mimic diffusion
first proof that nonuniform fields bias diffusion
new fundamental diffusion law
first use of wavelength-dependent photodiode RF phase
first spectral-depth transport measurement
universal false-diffusion theorem
```

Reasons:

- OED literature already establishes wavelength-dependent absorption/carrier-delay RF phase;
- PIN/PDA literature already establishes absorption/depletion/field coupling in transient photodiodes;
- TOF literature already establishes transport-inference bias from field inhomogeneity;
- broader transport literature already contains apparent/effective diffusion inflation from electric-field-driven migration under simplified inverse models;
- generic tangent-space bias and noncentral-chi-square statistics are established mathematical tools.

The manuscript contribution is the **detector-specific synthesis, theorem stack, causal isolation, and design criterion**, not ownership of those ingredients.

---

## Why a standalone manuscript is now justified

The branch no longer contains merely one surprising simulation.

It has a coherent paper spine:

1. exact calibrated-kernel forward/inverse formulation;
2. a zero-microscopic-diffusion deterministic counterexample;
3. point-source versus finite-kernel causal separation;
4. direct kernel-tail ablation;
5. mean-preserving zero-overlap ablation;
6. independent linear/exponential acceleration/deceleration profile families;
7. tangent-space root-bias theorem;
8. low-frequency effective-diffusion equivalence;
9. deterministic field-gradient sign theorem;
10. remote-region kernel leakage bound;
11. validated parameter-bias propagation to `D`;
12. covariance-aware RF rejection criterion;
13. end-to-end required SNR versus bandwidth;
14. independent published HgCdTe thickness/field/timing scale check.

That is sufficient intellectual content for a standalone theoretical detector paper if written narrowly.

---

## Closest literature that must appear in the manuscript

The introduction/discussion must explicitly position against at least these families:

### Photodiode OED

- Glasser et al., *Optics Express* 29, 19839–19852 (2021), DOI `10.1364/OE.424157`.
- Liokumovitch et al., *Optics Letters* 46, 4061–4064 (2021).
- Liokumovitch et al., *Optics Letters* 47, 2622–2625 (2022), DOI `10.1364/OL.462018`.
- Dutta et al., *Optics Letters* 49, 2057–2060 (2024), DOI `10.1364/OL.519164`.
- Mudgal et al., *Optics Letters* 49, 2185–2188 (2024), DOI `10.1364/OL.514906`.
- Kassa et al., arXiv:2605.18014 (2026).

### Partially depleted / high-speed photodiode forward physics

- Hu et al., *Optics Express* 23, 20402–20417 (2015), DOI `10.1364/OE.23.020402`.
- *Solid-State Electronics* 37, 1841–1847 (1994), DOI `10.1016/0038-1101(94)90175-9`, transient PIN response including diffusion outside the high-field region.

### Transport-inference/systematic-error boundary

- Emelianova, Arkhipov, and Adriaenssens, *J. Non-Cryst. Solids* 352, 1122–1125 (2006), DOI `10.1016/j.jnoncrysol.2005.12.045`.
- Hattori, Okamoto, and Hamakawa, *Physical Review B* 45, 1126 (1992), DOI `10.1103/PhysRevB.45.1126`.
- Hawks, Finck, and Schwartz, *Physical Review Applied* 3, 044014 (2015), DOI `10.1103/PhysRevApplied.3.044014`.

### Generic apparent-diffusion inverse boundary

- Johnson et al., *Chemical Science* (2025), “Beyond diffusion: ion and electron migration contribute to charge transport in redox-conducting metal-organic frameworks.”

This last source is outside photodetectors but is important to prevent the manuscript from overclaiming the generic idea that electric-field-driven transport can inflate an apparent diffusion coefficient.

---

## What remains for submission-level priority

During manuscript drafting, source-by-source checks should answer only a small number of exact questions:

1. Does any OED paper invert its wavelength/RF response for a microscopic diffusion coefficient rather than treating `D` as a forward parameter?
2. Does any PDA/PIN transient paper deliberately set true microscopic `D=0`, introduce deterministic field heterogeneity, and show a positive `D` under a wrong homogeneous inverse?
3. Does inhomogeneous-field TOF literature contain an older explicit false-diffusion-coefficient construction rather than false mobility/DOS?
4. Does any source derive the finite-kernel remote-support attribution bound or an equivalent detector-specific result?
5. Does any source quantify the simultaneous survival of both a spectral model-order test and a multi-RF homogeneous transport law under that nuisance?

If a direct collision is found, the manuscript claim must be narrowed immediately. If not, retain the conservative `we show / we derive` language without claiming first priority.

---

## Manuscript readiness

The appropriate next artifact is now a **manuscript blueprint**, not more unstructured numerical sweeps.

The blueprint should specify:

- one central question;
- 3–4 theorem/results sections rather than a chronology of discoveries;
- a small figure set that demonstrates causality and practical discrimination;
- explicit prior-art boundaries in the introduction;
- one published-HgCdTe scale comparison;
- no dependence on a new physical experiment;
- supplementary material for the larger geometry sweep and secondary controls.

Full prose drafting may begin after the blueprint is internally coherent.
