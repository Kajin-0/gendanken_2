# Paper 02 — Prior-Art Boundary

**Date:** 2026-08-15  
**Status:** **TARGETED AUDIT IN PROGRESS — PRIORITY UNPROVEN**  
**Rule:** absence of a located collision is not novelty evidence.

## 1. Candidate claim under audit

The claim being tested for possible distinctness is **not** any of the following broad statements:

- wavelength changes photodiode absorption depth;
- absorption depth changes carrier transit/diffusion response;
- nonuniform electric fields alter semiconductor transients;
- space charge can bias extracted transport parameters;
- photodiode RF phase can be wavelength dependent;
- partially depleted absorbers require coupled optical/electrical modeling.

Those are established territories.

The narrower candidate is:

> **In a wavelength-resolved Shockley-Ramo transport inverse with calibrated finite generation kernels, deterministic spatial velocity/electrostatic heterogeneity can alias into a positive, apparently admissible homogeneous diffusion coefficient even when microscopic diffusion is zero; the alias can remain near both the calibrated one-mode spectral manifold and the homogeneous low-RF dispersion manifold. The alias is controlled by generation-kernel support in the nonuniform region rather than nominal mean generation depth.**

The repository currently supports this statement analytically and numerically only in labeled theoretical/conditional models. Publication priority is not claimed.

---

## 2. Directly relevant established lineages

### 2.1 Inhomogeneous-field errors in time-of-flight inference

E. V. Emelianova, V. I. Arkhipov, and G. J. Adriaenssens,
“Time-of-flight measurements in inhomogeneous electric fields,”
*Journal of Non-Crystalline Solids* **352**, 1122–1125 (2006),
DOI: `10.1016/j.jnoncrysol.2005.12.045`.

Boundary established by this source:

- TOF transport extraction commonly assumes a homogeneous internal field;
- field inhomogeneity from doping/depletion can distort photocurrent transients;
- the resulting analysis can overestimate mobility and produce an apparent DOS distribution different from the true one.

Consequence for Paper 02:

> Do not claim the generic discovery that inhomogeneous electric fields bias transport inference.

---

### 2.2 Space-charge assumptions biasing diffusion-length inference

K. Hattori, H. Okamoto, and Y. Hamakawa,
“Theory of the steady-state-photocarrier-grating technique for obtaining accurate diffusion-length measurements in amorphous silicon,”
*Physical Review B* **45**, 1126 (1992),
DOI: `10.1103/PhysRevB.45.1126`.

Boundary established by this source:

- transport inversion under an incorrect local-space-charge-neutrality assumption can severely overestimate the inferred diffusion length.

Consequence:

> Do not claim broadly that electrostatic-model error can contaminate a diffusion-related inferred parameter.

The current Paper-02 distinction, if it survives, must depend on the specific wavelength-programmed Shockley-Ramo inverse, false positive homogeneous `D`, calibrated finite kernels, and model-manifold conditioning.

---

### 2.3 Terminal-current observation physics

S. A. Hawks, B. Y. Finck, and B. J. Schwartz,
“Theory of Current Transients in Planar Semiconductor Devices: Insights and Applications to Organic Solar Cells,”
*Physical Review Applied* **3**, 044014 (2015),
DOI: `10.1103/PhysRevApplied.3.044014`.

Boundary established by this source:

- externally measured planar current transients cannot in general be equated naively with internal carrier motion;
- internal space charge, electrode charge, applied bias, and displacement-current contributions must be treated consistently.

Consequence:

> Do not present Shockley-Ramo/electrode observation effects in transient material inference as a new general idea.

---

### 2.4 Partially depleted absorber photodiodes

Y. Hu, T. F. Carruthers, C. R. Menyuk, M. N. Hutchinson, V. J. Urick, and K. J. Williams,
“Simulation of a partially depleted absorber (PDA) photodetector,”
*Optics Express* **23**, 20402–20417 (2015),
DOI: `10.1364/OE.23.020402`.

Boundary established by this source:

- partially depleted photodiodes are already modeled with coupled two-dimensional drift-diffusion/electrostatic physics;
- modulation-frequency behavior and nonlinear response depend on device-level field and transport structure.

Related older transient-response work:

“Transient response of high-speed p-i-n photodiodes including diffusion effects,”
*Solid-State Electronics* **37**, 1841–1847 (1994),
DOI: `10.1016/0038-1101(94)90175-9`.

Boundary from this lineage:

- absorption outside the high-field region and diffusion contributions to photodiode transient response are established device physics;
- wavelength/absorption location and depleted versus undepleted transport regions are not new concepts.

Consequence:

> The Paper-02 claim cannot be “finite absorption width overlaps a depleted/nondepleted boundary and changes the transient.”

---

### 2.5 Photodiode optoelectronic chromatic dispersion (OED)

This is now the closest neighboring lineage for the wavelength/RF observable itself.

Representative sources:

E. Liokumovitch, Z. Glasser, and S. Sternklar,
“Optoelectronic chromatic dispersion in germanium PN photodiodes: wavelength monitoring and FBG interrogation,”
*Optics Letters* **46**, 4061–4064 (2021).

E. Liokumovitch, Z. Glasser, and S. Sternklar,
“Femtometer-resolved wavelength monitor based on photodiode optoelectronic chromatic dispersion with RF phase-shift amplification,”
*Optics Letters* **47**, 2622–2625 (2022),
DOI: `10.1364/OL.462018`.

S. Mudgal, P. K. Dubey, Z. Glasser, and S. Sternklar,
“Large optoelectronic chromatic dispersion in PN-type silicon photodiodes and photovoltaic cells,”
*Optics Letters* **49**, 2185–2188 (2024),
DOI: `10.1364/OL.514906`.

A. Dutta, E. Liokumovitch, Z. Glaser, and S. Sternklar,
“Large and tunable optoelectronic chromatic dispersion in PIN-type photodiodes,”
*Optics Letters* **49**, 2057–2060 (2024),
DOI: `10.1364/OL.519164`.

E. E. Kassa, Z. Glasser, U. K. Saint, R. Yozevitch, and S. Sternklar,
“Optoelectronic Chromatic Dispersion in a Single Photodiode for Machine-Learning-Based Computational Spectroscopy,”
arXiv:`2605.18014` (2026).

Boundary established by this lineage:

- wavelength-dependent internal photodiode transport can produce measurable RF phase signatures;
- those signatures have already been exploited for wavelength monitoring and spectroscopy;
- multi-frequency RF amplitude/phase features from one photodiode are already being treated as an inverse/spectral-reconstruction data space.

Consequence:

> Paper 02 must not claim wavelength-programmed RF phase, optoelectronic chromatic dispersion, or multi-frequency photodiode spectral inference as new.

This lineage is especially important because it is conceptually close to the repository’s wavelength-programmed internal-depth observable even though its scientific target is spectral sensing rather than material-transport identifiability.

---

## 3. Additional conceptual collision outside semiconductor detector literature

A broader inverse-measurement analogy exists in optical flow measurements: deterministic velocity gradients can broaden a measured spectrum and be represented as an “equivalent diffusivity” if the wrong model attributes that broadening to Brownian motion.

This is conceptually important because it means the general mathematical idea

> “unresolved deterministic velocity heterogeneity can masquerade as diffusion in an inverse measurement”

is not detector-specific novelty by itself.

Therefore the candidate contribution must remain tied to the semiconductor photodetector observable, finite generation kernels, remote electrostatic support, and the particular spectral/RF identifiability hierarchy.

No general claim of discovering “false diffusion from velocity gradients” should be made.

---

## 4. What the current targeted search has not yet located

No directly matching source has yet been located that combines all of the following:

1. wavelength-programmed internal photogeneration depth in a semiconductor detector;
2. calibrated finite generation kernels rather than point-source approximation;
3. terminal-current / Shockley-Ramo response;
4. deterministic spatial velocity or electrostatic heterogeneity;
5. inversion to a homogeneous drift-diffusion spatial exponent;
6. a **positive apparent diffusion coefficient when microscopic diffusion is exactly zero**;
7. same-frequency one-mode residual remaining small;
8. low-RF homogeneous dispersion-law residual remaining small over a finite band;
9. causal isolation by zero-overlap and mean-preserving kernel-support ablation;
10. a bound or design law linking remote kernel overlap and inverse-conditioning to transport-parameter bias.

This list defines the exact novelty search target.

**A negative result from this search is not evidence that the combination is novel.**

---

## 5. Current risk assessment

### High collision risk

- wavelength-dependent absorption depth;
- drift versus diffusion partition in photodiodes;
- partially depleted absorber frequency response;
- electric-field inhomogeneity distorting TOF transients;
- space-charge bias in diffusion-related inversion;
- RF phase / wavelength sensing via photodiode OED.

### Medium collision risk

- fitting deterministic heterogeneity with an effective diffusion parameter;
- generic tangent/model-manifold identifiability language;
- using higher-order frequency structure to distinguish heterogeneous from homogeneous transport.

### Lower collision risk, but still unproven

The exact detector-specific combination of

```text
finite calibrated generation kernels
+ remote electrostatic/velocity heterogeneity
+ Shockley-Ramo spectral-depth inverse
+ false positive homogeneous D
+ same-frequency one-mode survival
+ finite-band RF-law survival
+ support-ablation causality
```

appears more distinct in the current audit.

The eventual manuscript, if any, should be built around this narrow combination and a reusable attribution bound rather than around any ingredient separately.

---

## 6. What must be read in full before a novelty claim

Priority should remain OPEN until at least these source families are compared claim-by-claim in full text where accessible:

1. Emelianova–Arkhipov–Adriaenssens inhomogeneous-field TOF;
2. Hattori–Okamoto–Hamakawa SSPG diffusion-length bias;
3. Hawks–Finck–Schwartz planar transient-current theory;
4. Hu et al. partially depleted absorber simulation;
5. classical PIN transient-response / absorption-outside-depletion analyses;
6. the 2021–2026 OED series, especially the 2024 PIN paper and 2026 multi-frequency computational-spectroscopy preprint;
7. any papers cited by those sources that explicitly fit spatially nonuniform deterministic transport to an effective homogeneous diffusion coefficient.

Only after this should the status be upgraded from

```text
CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN
```

to a manuscript-level novelty statement.
