# Paper 03 — focused prior-art audit

**Date:** 2026-08-17  
**Status:** **FOCUSED PRIMARY-SOURCE AUDIT / NON-EXHAUSTIVE / NON-CLAIM**

## Question

Does prior detector literature already publish the specific Paper-03 hierarchy in which wavelength-dependent generation kernels and nonuniform geometry/weighting fields can create an apparent homogeneous transport signature, followed by a calibrated-kernel inverse test that rejects one spatial mode, permits a higher-mode descriptive rescue, applies a physical root-law consistency test, and statistically warns before the SNR needed for the false transport claim?

This audit is deliberately narrower than a generic search for Shockley–Ramo theory, photodiode bandwidth, distributed absorption, or geometry effects. Those ingredients are established separately in prior work.

## Primary-source anchors found

### Kahraman et al., OSA Annual Meeting (1990)

G. Kahraman, W. Sargeant, M. Hayat, B. E. A. Saleh, and M. C. Teich, “Time and frequency response of avalanche photodiodes with arbitrary structure,” OSA Annual Meeting, Technical Digest Series, paper MH6 (1990). DOI: `10.1364/OAM.1990.MH6`.

Relevant scope:

- coupled carrier transport equations for APDs of arbitrary structure;
- localized or spatially distributed injection;
- position-dependent coefficients;
- total current as a function of time/frequency;
- explicit study of layout, injection position, ionization and bandwidth.

This is strong prior art for spatially distributed generation and position-dependent transport shaping detector frequency response. It is not, from the abstract and accessible record, an inverse-identifiability/falsification construction of the Paper-03 type.

### Tan et al., Journal of Lightwave Technology (2003)

C. H. Tan, P. J. Hambleton, J. P. R. David, R. C. Tozer, and G. J. Rees, “Calculation of APD Impulse Response Using a Space-and Time-Dependent Ionization Probability Distribution Function,” *Journal of Lightwave Technology* **21**, 155 (2003).

Relevant scope:

- arbitrary carrier-transport model;
- arbitrary space/time distribution of ionization events after injection;
- mean and variance of APD impulse response;
- diffusion effects on temporal response.

This is prior art for spatially and temporally distributed microscopic detector response. It does not appear to pose the calibrated multi-wavelength inverse ambiguity addressed here.

### Dai and Bowers, Journal of Lightwave Technology (2010)

D. Dai and J. E. Bowers, “Simple Matrix-Method Modeling for Avalanche Photodetectors With Arbitrary Layer Structures and Absorption/Multiplication Coefficients,” *Journal of Lightwave Technology* **28**, 1404–1413 (2010).

Relevant scope:

- arbitrary layer structures;
- spatially varying absorption and multiplication represented by thin layers;
- short-circuit frequency response and impedance;
- explicit optical-absorption/transport structure dependence.

This is strong forward-model prior art for layer-dependent absorption and detector frequency response. It does not appear to contain the Paper-03 inverse model-order/root-law/statistical hierarchy.

### Song and Levitov, Physical Review B (2014)

J. C. W. Song and L. S. Levitov, “Shockley-Ramo theorem and long-range photocurrent response in gapless materials,” *Physical Review B* **90**, 075415 (2014). DOI: `10.1103/PhysRevB.90.075415`.

Relevant scope:

- Shockley–Ramo-type weighting-field description of geometry-dependent nonlocal photocurrent;
- global electrical response to local photoexcitation;
- geometry/inhomogeneity can strongly shape measured photocurrent patterns.

This is direct prior art for nonlocal geometry-dependent Shockley–Ramo photoresponse. Its scientific question is different from wavelength-resolved RF transport identifiability.

### Kunc et al., Physical Review Applied (2018)

J. Kunc, P. Praus, E. Belas, V. Dědič, J. Pekárek, and R. Grill, “Efficient Charge Collection in Coplanar-Grid Radiation Detectors,” *Physical Review Applied* **9**, 054020 (2018).

Relevant scope:

- finite-element Poisson solution in a coplanar-grid detector;
- laser-induced transient-current waveforms;
- induced currents computed using the Shockley–Ramo theorem;
- charge-collection waveform depends on coplanar geometry and weighting field.

This is particularly relevant to the deliberately different coplanar second geometry family. It establishes that coplanar weighting-field topology can shape transient currents; therefore Paper 03 must not claim discovery of that basic effect.

## Boundary between established ingredients and the candidate contribution

The focused audit finds mature prior art for each of the following separately or in forward combinations:

```text
spatially distributed optical generation;
position-dependent carrier transport;
frequency-dependent detector response;
arbitrary/layered detector structures;
geometry-dependent Shockley–Ramo weighting fields;
coplanar weighting-field control of transient current.
```

The candidate Paper-03 contribution, if the remaining numerical gates survive, is narrower:

```text
an explicit inverse-identifiability failure in wavelength-resolved complex RF current,
caused by realistic nonuniform geometry/weighting/transport physics;

plus a calibrated-kernel falsification hierarchy that can detect the mismatch
before the SNR required to accept the false homogeneous transport interpretation.
```

The hierarchy presently under test is:

```text
order-one apparent homogeneous-transport confound
-> calibrated-kernel one-mode rejection
-> higher-mode descriptive rescue
-> homogeneous physical root-law rejection
-> predeclared statistical early warning.
```

No primary source located in this focused audit was found to publish that full hierarchy or the same inverse question.

## Novelty language allowed at this stage

Allowed:

> “A focused primary-source audit located extensive prior work on distributed generation, position-dependent photodiode transport, arbitrary detector structures, and geometry-dependent Shockley–Ramo response, but did not identify the same calibrated-kernel inverse falsification hierarchy.”

Not allowed:

> “This is the first demonstration ever.”

> “No prior work exists.”

A publication-stage novelty claim still requires a broader citation-chain and keyword audit, including papers that cite the primary anchors above.

## Current boundary

```text
focused prior-art blocker = substantially reduced, not eliminated
basic geometry/weighting-field effect = established prior art
candidate novelty = inverse falsification hierarchy, conditional on remaining gates
second-family numerical result = not interpreted here
Stage B self-consistent semiconductor validation = pending
science_interpretation_ready = false
Paper 03 standalone GO = false
```
