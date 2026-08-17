# Paper 02 — Rev. 7 model-uncertainty priority checkpoint

**Date:** 2026-08-16  
**Status:** **FOCUSED CLOSEST-COLLISION AUDIT COMPLETE / NO FATAL DIRECT COLLISION FOUND / PRIORITY UNPROVEN**  
**Scope:** the enlarged covariance + optical-kernel-nuisance framing proposed for Rev. 7.  This note does not upgrade the manuscript to any superlative priority claim.

## 1. Question

Rev. 5 / Rev. 6 centered on a detector-specific attribution failure:

```text
finite wavelength-dependent generation kernels
+ deterministic spatial velocity heterogeneity
+ D_micro = 0
+ Shockley-Ramo terminal current
+ homogeneous drift-diffusion inverse
-> apparent D_eff > 0.
```

The Rev. 7 development adds a second question:

> if the wavelength-to-generation-kernel map or measurement metric is itself uncertain, can a nuisance direction bias the fitted transport root before same-frequency model rejection becomes statistically visible?

The closest-collision audit therefore has to distinguish **new detector-specific integration** from several broad ideas that are already well established.

---

## 2. Broad ingredients that are not novel

### A. Spectral photoresponse can be used to infer photodiode diffusion properties

**M. Ashry and S. Fares, "Diffusion length analysis and measurement in the base region of photodiodes," Journal of Physics and Chemistry of Solids 64, 2429--2431 (2003), DOI 10.1016/S0022-3697(03)00285-3.**

This is the closest newly identified collision for the Rev. 7 optical-model-uncertainty discussion.  It extracts minority-carrier diffusion length from wavelength-dependent silicon-photodiode photoresponse using an absorption-coefficient-dependent model and nonlinear least squares.  The paper explicitly states that small errors in the absorption coefficient can produce overall error in the inferred diffusion length in a sensitive regime.

**Consequence:** Rev. 7 must not claim that recognizing optical-model error as a source of diffusion-parameter bias is new.  Ashry--Fares should be cited explicitly in the manuscript.

**What it does not contain:** RF-phase transport inversion, finite known generation kernels treated as depth channels, deterministic zero-microscopic-diffusion transport producing positive apparent diffusion, Shockley--Ramo terminal-current geometry, a tangent/normal statistical ordering, an affine-depth null control, or the signed kernel-nuisance counterexample developed here.

### B. Incorrect transport assumptions can bias inferred diffusion length

**K. Hattori, H. Okamoto, and Y. Hamakawa, "Theory of the steady-state-photocarrier-grating technique for obtaining accurate diffusion-length measurements in amorphous silicon," Physical Review B 45, 1126--1138 (1992), DOI 10.1103/PhysRevB.45.1126.**

This paper shows that a commonly used transport assumption can severely overestimate diffusion length and develops corrected theory.

**Consequence:** generic statements that model mismatch can bias an inferred diffusion quantity are prior art.  Paper 02 must remain focused on the particular spectral-depth / terminal-current mechanism and its attribution geometry.

### C. Inhomogeneous electric fields can create apparent transport parameters

**E. V. Emelianova, V. I. Arkhipov, and G. J. Adriaenssens, "Time-of-flight measurements in inhomogeneous electric fields," Journal of Non-Crystalline Solids 352, 1122--1125 (2006), DOI 10.1016/j.jnoncrysol.2005.12.045.**

The authors show that analyzing TOF data under a homogeneous-field assumption can overestimate mobility and can create an apparent density-of-states structure strongly different from the true one.

**Consequence:** the broad principle "inhomogeneous field + homogeneous inverse -> apparent transport quantity" is explicitly established prior art.

### D. The electrode current is an observation functional, not direct microscopic motion

**S. A. Hawks, B. Y. Finck, and B. J. Schwartz, "Theory of Current Transients in Planar Semiconductor Devices: Insights and Applications to Organic Solar Cells," Physical Review Applied 3, 044014 (2015), DOI 10.1103/PhysRevApplied.3.044014.**

This is a load-bearing observation-physics collision for Paper 02 and already appears in the bibliography.  Terminal-current transients can be misread if observation physics is conflated with carrier motion.

### E. Wavelength-dependent RF phase is already a photodiode observable and inverse resource

The OED literature already establishes that wavelength-dependent carrier generation/transport produces measurable RF phase in photodiodes and can be used for wavelength monitoring and spectroscopy. Relevant primary sources include:

- Z. Glasser et al., Optics Express 29, 19839--19852 (2021), DOI 10.1364/OE.424157;
- E. Liokumovitch et al., Optics Letters 46, 4061--4064 (2021), DOI 10.1364/OL.435159;
- E. Liokumovitch, Z. Glasser, and S. Sternklar, Optics Letters 47, 2622--2625 (2022), DOI 10.1364/OL.462018;
- A. Dutta et al., Optics Letters 49, 2057--2060 (2024), DOI 10.1364/OL.519164;
- S. Mudgal et al., Optics Letters 49, 2185--2188 (2024), DOI 10.1364/OL.514906;
- E. E. Kassa et al., CLEO 2026 paper AW2B.1, photodiode-only computational spectroscopy based on OED.

**Consequence:** wavelength-dependent photodiode RF phase, its high spectral sensitivity, and its use for inverse spectroscopy are not priority claims available to Paper 02.

### F. Small wavelength-registration errors can strongly bias an inverse model

**P. Martinsen, V. A. McGlone, R. B. Jordan, and P. Gaastra, "Temporal Sensitivity of the Wavelength Calibration of a Photodiode Array Spectrometer," Applied Spectroscopy 64, 1325--1329 (2010).**

This work applies controlled wavelength perturbations to calibrated spectroscopic inverse models and reports approximately linear prediction bias with wavelength shift, while also showing that such sensitivity can be mitigated by including perturbed examples in calibration.

**Consequence:** the generic inverse-model statement "small wavelength error can generate large parameter bias" is not novel.  This source is less detector-transport-specific than Ashry--Fares, so it is useful chiefly as a boundary marker rather than a load-bearing manuscript citation.

---

## 3. What the focused audit did not find

No searched primary source was found that combines all of the following in the same detector-transport argument:

1. wavelength-dependent finite generation kernels used as depth channels;
2. Shockley--Ramo terminal-current response;
3. an exact `D_micro = 0` deterministic transport truth;
4. a homogeneous drift--diffusion inverse that returns `D_eff > 0`;
5. causal kernel-support controls separating remote velocity heterogeneity from nominal source means;
6. a same-frequency tangent/normal decomposition that separates parameter bias from model rejection;
7. covariance-aware power ordering for positive-`D` detection versus model-manifold rejection;
8. explicit relaxation of the exact-kernel assumption using a **uniform-velocity zero-diffusion null**;
9. an exact affine-depth calibration control showing that a global depth-scale error preserves `D=0`;
10. signed non-affine kernel perturbations shown to create positive apparent diffusion while remaining bias-first;
11. multi-frequency dispersion used as a second axis for nuisance rejection.

This absence in a focused search is **not evidence of universal or first priority**.  It only supports the narrower working posture below.

---

## 4. Recommended priority posture for Rev. 7

```text
DISTINCT DETECTOR-SPECIFIC COMBINATION PLAUSIBLE AFTER FOCUSED COLLISION AUDIT
BROAD INGREDIENTS ARE ESTABLISHED PRIOR ART
PRIORITY UNPROVEN
NO SUPERLATIVE PRIORITY CLAIM
```

The defensible contribution is the integrated detector-specific attribution framework and explicit counterexamples/controls, not any one of:

- wavelength-dependent photodiode phase;
- diffusion extraction from spectral response;
- model misspecification bias;
- inhomogeneous-field transport bias;
- generalized least squares;
- tangent projection;
- Schur complements;
- covariance propagation;
- wavelength-calibration sensitivity.

---

## 5. Manuscript requirement created by this audit

Before Rev. 7 can be promoted:

1. cite **Ashry--Fares (2003)** in the model-uncertainty discussion as direct prior art for absorption-model error affecting photodiode diffusion-length inference;
2. retain Hattori, Emelianova, Hawks, and the OED series in the broader prior-art boundary;
3. explicitly label generalized covariance/nuisance projection as standard inverse geometry rather than a mathematical novelty claim;
4. do not interpret the controlled sub-nanometer kernel-perturbation amplitudes as experimentally required wavelength-meter accuracy;
5. keep deterministic velocity heterogeneity as the manuscript's central physical counterexample and kernel misspecification as a separate attribution nuisance;
6. retain `PRIORITY UNPROVEN` after the revision.

This audit does not by itself make the paper submission-ready.
