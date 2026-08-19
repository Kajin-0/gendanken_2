# Paper 03 — Focused prior-art audit and novelty boundary

**Date:** 2026-08-17  
**Status:** **FOCUSED PRIMARY-SOURCE AUDIT / PROVISIONAL NOVELTY BOUNDARY / NON-CLAIM**

## Question audited

The audit was not a broad photodetector bibliography search. It targeted the actual prospective Paper-03 contribution:

> Can a calibrated spectral/RF hierarchy detect that a low-dimensional homogeneous transport inverse is inadequate, under independent multidimensional forward physics, at lower measurement precision than a false microscopic transport parameter becomes statistically defensible?

## Close prior art that must be treated as central

### Nonuniform generation can corrupt transport interpretation

Halme, Miettunen, and Lund, *J. Phys. Chem. C* **112** (2008) 20491–20504, DOI `10.1021/jp806512k`, developed small-signal photoresponse theory with arbitrary/nonuniform generation profiles and showed that generation/collection structure can materially alter time constants and inferred transport quantities.

**Consequence:** Paper 03 must not claim that nonuniform optical generation causing erroneous diffusion/lifetime interpretation is itself new.

### Wavelength-dependent absorption depth can create RF phase/amplitude dispersion

Glasser et al., *Optics Express* **29** (2021) 19839–19852, DOI `10.1364/OE.424157`, established optoelectronic chromatic dispersion arising from wavelength-dependent photodiode absorption/current formation.

Dutta et al., *Optics Letters* **49** (2024) 2057–2060, DOI `10.1364/OL.519164`, further demonstrated PIN-photodiode OED and bias-tunable RF phase dispersion.

Kassa et al., 2026, arXiv:`2605.18014` / CLEO 2026, use multi-frequency photodiode RF amplitude/phase features produced by wavelength-dependent absorption/transport for computational spectroscopy with a single photodiode.

**Consequence:** Paper 03 must not claim discovery of spectral-depth-dependent RF phase/amplitude structure, or the use of multi-frequency photodiode response to encode wavelength.

### Frequency-domain photoresponse already supports model/consistency diagnostics

The IMPS/IMVS/impedance literature contains explicit consistency relations and correlated small-signal methods designed to distinguish or constrain transport/recombination interpretations. Later reviews also emphasize that in spatially complex devices an observed small-signal time constant need not equal a unique microscopic lifetime.

**Consequence:** Paper 03 must not claim that frequency-domain consistency testing or caution about assigning time constants to microscopic parameters is new in general.

### General model inadequacy is established methodology

The broader inverse-problem/calibration literature already establishes that a structurally inadequate model can yield biased effective parameters and misleading uncertainty.

**Consequence:** the generic statement “wrong models can fit data and bias parameters” is motivation, not novelty.

## What the targeted audit did not find

The targeted primary-source audit did **not find a direct precedent** for the complete construction used here:

```text
one selected-terminal complex-current observable;
multiple explicitly calibrated optical generation kernels;
mechanism-blind low-dimensional kernel-space model-order testing;
cross-RF finite-boundary physical root-law admissibility;
independent multidimensional Shockley-Ramo forward generators;
predeclared nonlinear bootstrap calibration;
and an explicit precision ordering asking whether model inadequacy becomes rejectable before a false microscopic transport parameter reaches its own claim-level SNR.
```

This is not a proof that no precedent exists. It is the current result of a focused search and remains subject to referee/literature discovery.

## Safe candidate novelty framing

A defensible prospective contribution is therefore narrow:

> A mechanism-blind, calibrated-kernel falsification hierarchy for wavelength-resolved RF photodetector transport, designed to test whether neglected multidimensional detector physics self-announces through model order and cross-RF root-law failure **before** a false homogeneous microscopic transport inference becomes statistically defensible.

The evidence must come from independent forward models and predeclared precision comparisons, not from the mere existence of wavelength-dependent transit-time dispersion.

## Claims explicitly excluded

Do not claim novelty for:

```text
wavelength-dependent absorption depth affecting RF phase;
OED/chromatic dispersion in photodiodes;
arbitrary/nonuniform generation profiles in modulated photoresponse;
diffusion/recombination extraction from frequency-domain photocurrent;
generic multidimensional drift-diffusion photodetector modeling;
generic model inadequacy;
or generic consistency checking among frequency-domain observables.
```

## Standalone-paper effect

The audit does **not** collapse the prospective Paper-03 contribution into an obviously standard result, but it materially narrows the framing. Standalone GO still requires:

```text
broad first-family Outcome-A/B evidence;
a materially different geometry family;
Stage-B self-consistent semiconductor validation;
experimentally actionable SNR/observable consequences;
and final manuscript-level citation verification.
```

At this checkpoint:

```text
focused prior-art gate = provisionally favorable under narrow framing
absolute novelty = not claimed
science_interpretation_ready = false
Paper 03 standalone GO = false
```
