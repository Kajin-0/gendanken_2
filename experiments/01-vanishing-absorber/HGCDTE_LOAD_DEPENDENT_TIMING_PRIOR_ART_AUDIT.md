# HgCdTe Optical-Load-Dependent Timing — Focused Prior-Art Audit

**Date:** 2026-08-09  
**Status:** focused literature boundary for optical-load-dependent transient/RF timing; generic load-dependent HgCdTe timing is established prior art; spatial inverse use remains candidate only; priority unproven

## 1. Question being audited

The short-wave branch proposed a causal observable based on HgCdTe timing versus optical load:

```text
paired A-B phase
at fixed temperature and wavelength
measured at several optical-load states
with a second finite difference in load
and a difference between short-wave wavelengths.
```

The construction is useful because static A/B transport and linear-in-load phase terms cancel.

But usefulness is not novelty.

The question for this audit is:

> **Has HgCdTe transient response already been measured as a function of optical/bias-light intensity, including attempts to separate RC/interface effects from carrier dynamics?**

The answer is unequivocally **yes**.

---

## 2. 2013 — bias-light-dependent HgCdTe transient decay was already measured

H. Cui et al.,

`Influence of trap filling and junction capacitance charging on photovoltage transients in HgCdTe-based infrared photodiode`,

*Optical and Quantum Electronics* **46** (2014) 1049-1054, published online 2013,
DOI `10.1007/s11082-013-9819-5`.

The authors performed open-circuit transient-photovoltage decay measurements on HgCdTe photodiodes at **different steady bias-light powers** using a picosecond pulsed laser at `4.5 um`.

They explicitly report that the transient decay constants contain contributions from

```text
junction-capacitance discharge
trap emission
photocarrier recombination,
```

and that the inferred minority-carrier lifetime depends on carrier injection level.

This is already very close to the physical issue encountered in the present load-curvature branch:

> changing illumination can alter the measured transient through both carrier physics and electrical/trap states.

Therefore neither

```text
HgCdTe transient timing vs background illumination
```

nor

```text
recognition that RC/traps contaminate the transient
```

is available as a new claim.

---

## 3. 2014 — transient waveform versus bias-light intensity is direct prior art

H. Cui et al.,

`Dependence of transient photovoltage characteristics on bias light intensity for HgCdTe-based photovoltaic infrared detector pixel arrays`,

*Optical and Quantum Electronics* **46** (2014) 1359-1364,
DOI `10.1007/s11082-014-9887-1`.

The experiment used pulsed-laser transient photovoltaic response while varying steady bias-light intensity.

The reported waveform changed strongly with optical load, including a peak-to-valley polarity inversion.

The authors attributed that behavior primarily to a Schottky barrier at the metal-semiconductor interface and used the transient behavior as a device/interface diagnostic.

This is a hard collision with any broad statement such as

> measure HgCdTe transient response versus optical intensity to reveal internal physics.

That has already been done experimentally.

---

## 4. 2013/2014 interface work is also a warning about mechanism attribution

H. Cui et al.,

`The Effect of Metal-Semiconductor Contact on the Transient Photovoltaic Characteristic of HgCdTe PV Detector`,

*The Scientific World Journal* (2013), open access.

The authors measured pulsed transient photovoltage of an HgCdTe photodiode and showed a nontrivial negative-valley / positive-peak transient associated with the metal-semiconductor contact.

They varied excitation intensity and examined both one-photon and two-photon excitation conditions.

The crucial lesson for the present project is methodological:

> **a dramatic load-dependent transient feature can originate at a contact/interface rather than in bulk carrier transit.**

Therefore a future graded-HgCdTe load-phase experiment must de-embed or independently falsify contact, junction-capacitance, trap, and packaging mechanisms before assigning spatial structure to the graded absorber.

---

## 5. 2015 — background illumination was deliberately used to extract HgCdTe lifetime

H. Cui et al.,

`Experimental Determination of Effective Minority Carrier Lifetime in HgCdTe Photovoltaic Detectors Using Optical and Electrical Methods`,

*Advances in Condensed Matter Physics* (2015), article 482738,
DOI `10.1155/2015/482738`.

This work used HgCdTe photodiodes with several Cd compositions and combined

```text
photo-induced open-circuit voltage decay
small-parallel-resistance transient photovoltage
pulse recovery measurements.
```

The optical experiments used a picosecond pulsed infrared source together with variable steady background illumination.

Important details:

- increasing bias-light intensity was used to saturate the junction photovoltage;
- the transient decay was then used to infer minority-carrier lifetime;
- a small parallel resistance was used in another configuration specifically to suppress junction-RC influence;
- under that low-RC condition the authors reported that changing bias light nearly did not alter the transient curve, supporting a carrier-lifetime interpretation.

Thus prior work already contains the conceptual sequence

```text
vary background light
measure HgCdTe transient
manipulate electrical loading
separate RC contribution
infer carrier dynamics.
```

This substantially narrows the present branch.

---

## 6. Wavelength-tunable HgCdTe transient measurements also exist

Related work by the same research line used wavelength-tunable picosecond infrared excitation to study transient photovoltage and its dependence on Cd composition, temperature, and contact effects.

For example:

`Dependence of Cd compositione on transient photovoltage characteristics in Hg1-xCdxTe photodiode`, NUSOD 2015, DOI `10.1109/NUSOD.2015.7292822`.

The available abstract reports a wavelength-tunable pulsed infrared source and transient waveforms whose negative-valley behavior changes with composition and temperature.

This does **not** appear, from accessible material, to use wavelength as a calibrated depth kernel and invert a spatial transport profile.

But it means that

```text
wavelength-tunable laser + HgCdTe transient response
```

is itself already established experimental territory.

---

## 7. Graded-HgCdTe impulse and RF response are also established

The 2022 graded-HgCdTe high-speed detector work already measured both impulse and frequency response of compositionally graded HgCdTe devices.

The reported experiment includes

```text
1.55 um femtosecond impulse excitation
50 MHz-1 GHz lightwave-component/network-analyzer response
zero-bias room-temperature operation
measured 3 dB bandwidths around 115 MHz and 750 MHz for two structures.
```

The authors interpret the bandwidth contrast in terms of the composition-gradient built-in field altering minority-carrier transport.

Therefore the present project cannot claim novelty for

```text
graded HgCdTe high-speed response
graded HgCdTe RF-frequency response
or
composition-gradient acceleration inferred from timing/bandwidth.
```

---

## 8. Strong-injection / saturation physics in graded HgCdTe is established

The 2023-2024 Shanghai/SITP research line also directly studies strong illumination and composition-gradient effects:

- `Simulation on the saturation properties of room-temperature mid-wave infrared HgCdTe detectors`, JIRMMW 42 (2023) 143-148, DOI `10.11972/j.issn.1001-9014.2023.02.001`;
- `Photoelectric characteristics of compositionally graded HgCdTe detector`, JIRMMW 42 (2023) 285-291, DOI `10.11972/j.issn.1001-9014.2023.03.001`;
- `Multi-Physics Field Based Simulation on the Response and Saturation Properties of Hg1-xCdxTe Based Photovoltaic Detectors With Composition Gradients`, *IEEE Photonics Journal* (2024), DOI `10.1109/JPHOT.2024.3427322`;
- `Performance Optimization of Hg1-xCdxTe Photovoltaic Detectors Under Strong Illumination Considering Temperature and Wavelength Dependencies`, *IEEE Photonics Journal* (2024), DOI `10.1109/JPHOT.2024.3470871`.

These works establish forward physics involving

```text
strong illumination
space-charge accumulation
heating
load-dependent impedance / response
composition-gradient fields
wavelength and temperature dependence
saturation-threshold optimization.
```

None of that is candidate novelty here.

---

## 9. The unresolved 2024 laser-measurement paper is now even more important

Closest unresolved paper:

G.-Q. Xu et al.,

`Potential application of HgCdTe detector with composition gradient in laser measurement`,

*Journal of Applied Optics* **45** (2024),
DOI `10.5768/JAO202445.0310009`.

Accessible metadata confirm the title/authors and that it belongs to the same graded-HgCdTe / laser-measurement research line.

The full technical text remains inaccessible through the sources recovered so far.

Page metadata are inconsistent across indexes:

```text
ResearchGate -> 549-556
one journal TOC mirror -> 543-548.
```

Do not use page numbering as an epistemic issue; the technical content is the real blocker.

Given the present pivot toward load-dependent laser timing, this paper is now a **high-priority collision** and must be read before any novelty language involving graded HgCdTe under laser loading.

---

## 10. Hard non-novelty boundary after this audit

Do **not** claim novelty for any of the following:

```text
HgCdTe transient response versus optical intensity
bias-light-dependent HgCdTe transient photovoltage
using background illumination to alter/saturate HgCdTe junction response
extracting HgCdTe carrier lifetime from optical transients
recognizing junction capacitance / traps / contacts as transient contaminants
wavelength-tunable HgCdTe transient excitation
graded-HgCdTe impulse response
graded-HgCdTe RF-frequency response
strong-injection / saturation effects in graded HgCdTe
composition-gradient mitigation of space-charge / saturation effects.
```

The second finite difference in load is elementary nuisance rejection and is **not** itself a scientific novelty claim.

---

## 11. What remains potentially distinctive

The current candidate is now much narrower:

> **Use the known monotonic graded-HgCdTe optical profile as an internal wavelength-to-depth encoder and invert wavelength-resolved complex timing response for a small number of differential spatial transport modes, with paired A/B material controls and controlled perturbations used for validation.**

For the optical-load branch specifically:

> **Use wavelength-resolved RF load curvature only as a causal validation observable for the spatial inverse, not as the claimed advance by itself.**

Potential distinct ingredients are therefore the combination of

```text
calibrated wavelength-dependent depth kernels
+
few-mode spatial inverse
+
complex RF phase/magnitude
+
paired smooth/nonlinear graded structures
+
causal perturbation / nuisance rejection.
```

Whether that combination is publishably distinct is still OPEN.

---

## 12. Reviewer-level risk after the new collision

A skeptical reviewer can now fairly say:

> `HgCdTe transient response versus illumination intensity was measured more than a decade ago; graded HgCdTe bandwidth and strong-injection saturation have also been studied. Why is this more than repackaging known transient photovoltage and graded-device physics with an inverse matrix?`

That is a serious objection.

The project must answer it empirically, not rhetorically.

A convincing response would require showing something prior methods do not provide, for example:

```text
reconstruction of buried differential transport structure without scanning the excitation spot
validated against an independent material perturbation or localized-position timing reference
quantitative spatial-mode uncertainty / resolution
and a falsifiable failure on the smooth control sample when the model is wrong.
```

If those capabilities cannot be demonstrated, the work may remain a useful specialized measurement analysis rather than a significant research advance.

---

## 13. Next literature / experimental boundary

Two tasks now dominate:

1. recover the full 2024 `Potential application...` paper;
2. stop treating optical-load timing as the novelty axis and use it only to test whether the **spatial spectral inverse** can recover validated internal transport contrast.

The next numerical work should therefore focus on whether the load-curvature observable adds an **independent spatial mode** beyond static wavelength response once realistic electrical/contact nuisance directions are included.

If it does not, the load branch should be demoted to a control rather than expanded further.
