# Paper 02 — Exact Closest-Collision Audit after Rev. 5

**Date:** 2026-08-16  
**Status:** **FOCUSED PRIMARY-SOURCE COLLISION AUDIT / DISTINCT COMBINATION PLAUSIBLE / PRIORITY UNPROVEN**

## 1. Question being audited

The audit is not asking whether any ingredient of Paper 02 is new. Several are established.

The exact collision target is the combined claim:

> wavelength-dependent finite generation kernels, treated as known by a photodetector inverse, overlap deterministic spatial velocity/electrostatic heterogeneity; with microscopic diffusion fixed exactly to zero, the resulting Shockley-Ramo terminal-current data are fit by a homogeneous drift-diffusion inverse that returns positive effective diffusion; causal support controls and covariance-aware same-/multi-frequency tests then separate parameter bias from model rejection.

A prior paper need not use the same notation to collide. Any work containing the same physical/inferential content counts as a serious collision.

Negative search results are **not** evidence of priority. This document only records the strongest collisions found and the exact residual distinction.

---

## 2. Closest source family A — optoelectronic chromatic dispersion (OED)

### Glasser et al., Optics Express 29, 19839 (2021)

**Title:** *Optoelectronic chromatic dispersion and wavelength monitoring in a photodiode*  
**DOI:** `10.1364/OE.424157`

Publisher abstract establishes that light absorption and current formation inside a photodiode generate a large wavelength-dependent RF phase response and that the OED parameter is tied to wavelength-dependent absorption.

**Direct overlap with Paper 02**

- wavelength-dependent absorption depth is physically central;
- carrier transport inside a photodiode changes RF phase;
- wavelength therefore encodes internal transport information;
- the terminal electrical response is used as an optical/spectral observable.

**Missing relative to the exact Paper-02 collision target**

- no material-diffusion attribution test;
- no construction with `D_micro = 0` producing fitted `D_eff > 0`;
- no causal support ablation isolating remote overlap with a heterogeneous region;
- no tangent/normal decomposition of parameter bias versus model rejection;
- no covariance-aware test of whether a homogeneous drift-diffusion material interpretation is falsifiable.

**Collision severity:** **HIGH on measurement mechanism, LOW on the exact inverse-attribution theorem.**

---

### Dutta et al., Optics Letters 49, 2057 (2024)

**Title:** *Large and tunable optoelectronic chromatic dispersion in PIN-type photodiodes*  
**DOI:** `10.1364/OL.519164`

The publisher record reports a theoretical and experimental PIN-photodiode OED study and shows that the amount and sign of OED can be tuned electrically with bias.

**Direct overlap**

- wavelength-dependent photodiode RF phase;
- device field/bias changes the phase signature;
- sign changes demonstrate that device electrostatics can dominate a wavelength-dependent timing observable.

**Missing**

- no inference of microscopic diffusion from the OED data;
- no true-zero-diffusion counterexample;
- no finite-kernel support causality result;
- no statistical attribution hierarchy matching Paper 02.

**Collision severity:** **HIGH for the proposition that electrostatics control wavelength-dependent phase; MODERATE/LOW for the claimed attribution framework.**

---

### Kassa et al., arXiv:2605.18014 / CLEO 2026

**Title:** *Optoelectronic Chromatic Dispersion in a Single Photodiode for Machine-Learning-Based Computational Spectroscopy*  
**arXiv:** `2605.18014`

The 2026 work uses multi-frequency RF amplitude/phase features from a single photodiode for spectral reconstruction. Its abstract explicitly attributes the OED feature space to wavelength-dependent absorption depth and carrier diffusion delays.

**Direct overlap**

- finite wavelength-dependent absorption depth;
- multi-frequency electrical feature vectors;
- inversion of wavelength-dependent transport signatures.

**Missing**

- the inverse target is optical spectrum, not a material diffusion coefficient;
- diffusion is part of the assumed/physical OED mechanism, not a fitted false material parameter generated with `D_micro = 0`;
- no deterministic heterogeneity attribution counterexample or causal support control;
- no same-/multi-frequency material-model rejection test.

**Collision severity:** **HIGH on modern multi-frequency OED inversion, LOW on the exact false-diffusion attribution result.**

---

## 3. Closest source family B — field heterogeneity corrupting semiconductor transport extraction

### Emelianova, Arkhipov, and Adriaenssens, J. Non-Cryst. Solids 352, 1122 (2006)

**Title:** *Time-of-flight measurements in inhomogeneous electric fields*  
**DOI:** `10.1016/j.jnoncrysol.2005.12.045`

The paper explicitly analyzes TOF photocurrent under an inhomogeneous field and shows that imposing standard homogeneous-field interpretation can overestimate mobility and produce an apparent density-of-states distribution that differs strongly from the true one.

**Direct overlap**

- device-level field heterogeneity can masquerade as a material transport property;
- the failure is created by imposing an over-simple homogeneous inverse model;
- the measured photocurrent transient is altered by spatially varying carrier velocity.

**Missing**

- wavelength-dependent finite generation kernels are not the inference coordinate;
- the target false parameter is not homogeneous diffusion extracted from spectral/RF terminal-current data;
- no exact `D_micro = 0 -> D_eff > 0` construction;
- no kernel-support ablation or RF covariance rejection hierarchy.

**Collision severity:** **VERY HIGH conceptually. This is the strongest prior-art warning against broad claims such as “field heterogeneity can bias transport extraction.” It does not appear to collide with the narrow Paper-02 construction.**

---

## 4. Closest source family C — measured current is not microscopic carrier motion

### Hawks, Finck, and Schwartz, Physical Review Applied 3, 044014 (2015)

**Title:** *Theory of Current Transients in Planar Semiconductor Devices: Insights and Applications to Organic Solar Cells*  
**DOI:** `10.1103/PhysRevApplied.3.044014`

The paper derives rigorous transient-current relations for planar semiconductor devices and emphasizes that electrode charge, internal space charge, displacement current, and the externally measured current must be distinguished. It shows that a conventional extraction can produce an apparent carrier concentration differing by a factor of two.

**Direct overlap**

- terminal current is an electrode/device observable, not a direct microscopic carrier coordinate;
- inference of material properties from current transients can be systematically biased by the observation operator;
- full drift-diffusion/Poisson validation is used to check the formalism.

**Missing**

- wavelength-dependent generation kernels;
- deterministic spatial velocity gradient causing positive fitted diffusion with `D_micro = 0`;
- spectral root/tangent-space analysis;
- causal support and RF statistical tests.

**Collision severity:** **VERY HIGH for the observation-operator philosophy, LOW for the exact mechanism/theorem.**

---

## 5. Related but non-colliding forward-device literature

### Hu et al., Optics Express 23, 20402 (2015)

**Title:** *Simulation of a partially depleted absorber (PDA) photodetector*  
**DOI:** `10.1364/OE.23.020402`

This is strong prior art for treating photodiode electrostatics, absorption, transport, loading, and nonlinear response together in realistic forward simulation.

It substantially limits any claim that coupling optical generation, depletion, electric field, transport, and measured photodiode response is itself new.

It does **not** appear to pose the Paper-02 inverse-attribution question or demonstrate a zero-microscopic-diffusion response returning a positive homogeneous fitted diffusion coefficient.

**Collision severity:** **HIGH on coupled forward physics, LOW on the inverse-identifiability result.**

---

## 6. Older dispersive/TOF transport literature

Scher and Montroll (Phys. Rev. B 12, 2455, 1975) and the extensive multiple-trapping / dispersive-transport literature establish that photocurrent transients can encode non-Gaussian and model-dependent carrier transport. They preclude any broad novelty claim around transit-time dispersion, non-Fickian behavior, or using photocurrent to infer transport distributions.

This family does not by itself collide with the Paper-02 finite-spectral-kernel + deterministic-heterogeneity + false homogeneous-`D` construction.

---

## 7. Collision matrix

| Prior-art element | OED 2021/2024/2026 | Emelianova 2006 | Hawks 2015 | Hu 2015 | Paper 02 Rev. 5 |
|---|---:|---:|---:|---:|---:|
| wavelength-dependent generation/absorption depth | YES | no | no | YES/forward | YES |
| RF phase / frequency-domain photodiode observable | YES | no | no | modulation response | YES |
| deterministic/nonuniform device field or velocity matters | YES, especially bias tuning | YES | general electrostatics | YES | YES |
| externally measured current distinguished from microscopic motion | implicit | photocurrent model | YES, central | forward model | YES, Shockley-Ramo central |
| homogeneous inverse can misattribute device physics to material property | not the target | YES | YES, other parameter | not central | YES |
| microscopic diffusion explicitly fixed to zero | not for this purpose | no exact analogous gate found | no | no | YES |
| fitted homogeneous diffusion becomes positive | not found | not found | not found | not found | YES |
| finite-kernel support in remote nuisance region is causal variable | not found | no | no | no | YES |
| mean-preserving support ablation | not found | no | no | no | YES |
| local tangent-space parameter-bias law | not found | no | no | no | YES |
| same-frequency bias-vs-rejection comparison under covariance | not found | no | no | no | YES |
| multi-frequency homogeneous-law rejection power | multi-frequency features, different target | no | no | no | YES |

The table is a focused audit record, not proof that no unsearched paper contains an equivalent construction.

---

## 8. Exact residual distinction that currently survives

After stripping away established ingredients, the strongest potentially distinct contribution is:

> a photodetector-specific material-attribution theory showing constructively that finite wavelength-dependent generation support can couple to deterministic velocity heterogeneity so that a kernel-aware Shockley-Ramo response generated with `D_micro = 0` lies close to, and at low frequency is tangent to, a homogeneous drift-diffusion inverse with `D_eff > 0`; the theory then separates causal support, fitted-parameter bias, same-frequency structural rejection, and multi-frequency statistical falsification.

This is much narrower than any of the following, which must **not** be claimed as new:

- wavelength-dependent photodiode transit time or RF phase;
- OED;
- electric-field dependence of photodiode response;
- inhomogeneous-field bias in transport extraction;
- Shockley-Ramo terminal-current theory;
- effective/apparent transport coefficients in general;
- multi-frequency inverse measurements in general.

---

## 9. Priority disposition

Current evidence supports:

```text
DISTINCT COMBINATION PLAUSIBLE AFTER FOCUSED EXACT-COLLISION SEARCH
PRIORITY UNPROVEN
NO SUPERLATIVE PRIORITY CLAIM
```

The Rev. 5 manuscript's current conservative novelty language remains acceptable. There is no basis from this audit to add `first`, `first demonstration`, `novel mechanism`, `fundamental`, `universal`, or similar wording.

A later submission-grade priority audit should still perform citation-chaining around the strongest four collision families and inspect full texts where abstracts do not expose the inverse target clearly.

---

## 10. Scientific consequence

The audit does **not** reveal a fatal collision. It does reveal exactly where a referee will attack:

1. **OED already knows wavelength-dependent absorption changes carrier timing.** Paper 02 must emphasize material attribution, not wavelength-dependent delay itself.
2. **TOF literature already knows inhomogeneous fields corrupt transport extraction.** Paper 02 must emphasize the finite-kernel spectral/RF construction, true-zero-diffusion control, and quantitative rejection hierarchy.
3. **Transient-current theory already warns measured electrode current is not microscopic motion.** Paper 02 must use Shockley-Ramo as necessary machinery, not as a novelty claim.
4. **Realistic photodiode forward models already couple optical generation, electrostatics, and transport.** Paper 02's distinction is inverse identifiability and falsification, not coupled-device modeling.

This positioning should remain locked in future revisions.
