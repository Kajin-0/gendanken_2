# Prior-Art Boundary — Translated-Gradient Wavelength × RF Validation

**Date:** 2026-08-10  
**Status:** focused literature boundary; several essential forward/timing ingredients are established prior art; full text of one 2024 close collision remains unresolved; no novelty claim

## 1. Why this boundary matters

The purpose-built branch has become experimentally stronger, but that does not enlarge the novelty claim.

It narrows it.

The correct question is now:

> **Which parts of the proposed matched translated-gradient wavelength × RF experiment are already established HgCdTe physics/measurement practice, and what exact combination remains only a candidate distinction?**

---

## 2. Hard collision — graded HgCdTe already has measured high-speed response

M.-S. Sang, G.-Q. Xu, H. Qiao, and X.-Y. Li,
“High speed uncooled MWIR infrared HgCdTe photodetector based on graded bandgap structure,”
*Journal of Infrared and Millimeter Waves* **41** (2022) 972-979,
DOI `10.11972/j.issn.1001-9014.2022.06.005`.

This is a hard prior-art boundary.

The paper reports graded n-on-p HgCdTe photodiodes at room temperature and zero bias, including

```text
LPE device response ~8.7 ns / 115 MHz
VPE device response ~1.33 ns / 750 MHz.
```

Its one-dimensional model explicitly treats composition grading in the absorber as a built-in electric field that modifies carrier transport, quantum efficiency, and response time.

The device comparison is used experimentally to validate that mechanism.

Therefore **do not claim novelty** for

```text
composition-gradient-induced built-in fields in HgCdTe
composition-gradient modification of carrier transit/response time
high-speed graded-HgCdTe detector design
or RF/frequency-response measurement of graded HgCdTe.
```

---

## 3. The 2022 work also already uses ultrafast and RF laser measurements

The same paper reports

```text
1550-nm, ~100-fs, 80-MHz pulse excitation
with a 20-GHz sampling module
```

for impulse response.

For frequency response it uses a Lightwave Component Analyzer / network analyzer with

```text
lambda = 1550 nm
average optical power = 5 mW
frequency range = 50 MHz to 1 GHz.
```

It also reports device switching behavior under `2000 nm` laser excitation.

Thus **do not claim novelty** for

```text
using a short-wave laser to time graded HgCdTe transport
combining optical excitation with microwave/RF readout
or testing graded HgCdTe at more than one optical wavelength in separate experiments.
```

The critical distinction, if any, must involve how wavelength is used **systematically as an internal spatial coordinate**.

---

## 4. Graded-HgCdTe spectral response versus composition profile is also prior art

The current repository already treats the following as hard prior-art territory:

- B.-S. Cui et al. (2013): HgCdTe composition distribution affects device spectral response.
- M.-S. Sang et al. (2022): graded absorber transport/high-speed response.
- G.-Q. Xu et al. (2023): photoelectric characteristics of compositionally graded HgCdTe; processed A/B structures; wavelength/temperature response and large nonlinear-gradient region.
- Lee (2006): optical response modeling in graded absorber detectors.

Therefore the forward statement

```text
wavelength samples different parts of a graded absorber
```

is not a novelty claim.

Neither is

```text
the generation profile can be calculated from x(z), Eg(x,T), and alpha(E,x,T).
```

---

## 5. Localized HgCdTe transit measurements are prior art

Perrais et al., *Journal of Electronic Materials* **38** (2009) 1790-1799,
DOI `10.1007/s11664-009-0802-7`, studied transit-time limitations in HgCdTe APDs using localized/controlled excitation and time-response measurements.

This blocks any broad claim that

```text
spatially localized optical excitation can probe HgCdTe transit time
```

is new.

The candidate must instead concern **spectral encoding in a graded absorber** and the inverse/relocation protocol.

---

## 6. Optical-load-dependent HgCdTe transient response is prior art

The preceding audit also found HgCdTe transient-photovoltage/lifetime studies using variable steady optical background and pulsed excitation.

Therefore the discarded load-curvature branch must remain framed as a **measurement-control construction**, not a novelty claim.

Optical load does not create a new wavelength spatial operator if the normalized generation kernel is unchanged.

---

## 7. 2024 close collision — full technical text still unresolved

G.-Q. Xu et al.,
“Potential application of HgCdTe detector with composition gradient in laser measurement,”
*Journal of Applied Optics* **45** (2024) 549-556,
DOI `10.5768/JAO202445.0310009`.

The article's existence, authorship, journal, pagination, and DOI are verified.

However, the full technical text/abstract has not been recovered from a primary accessible source in the present audit.

ResearchGate exposes metadata but states that no full text is available there.

Therefore:

> **This paper remains an unresolved priority blocker for any novelty statement involving compositionally graded HgCdTe as a laser-measurement device.**

Do not infer its technical scope from the title alone.

---

## 8. 2024 LPE growth control is a materials collision, not a timing-inverse collision

Q. Huo et al.,
“Improved liquid phase epitaxy method for in-situ growth of HgCdTe with positive composition gradient,”
*Journal of Infrared and Millimeter Waves* **43** (2024) 307-315,
DOI `10.11972/j.issn.1001-9014.2024.03.003`.

This work establishes that LPE composition-gradient sign/magnitude can be deliberately controlled through mercury-loss and cooling conditions, with longitudinal composition confirmed by thinning spectroscopy and SIMS.

It blocks any broad materials novelty claim for

```text
intentionally engineered positive HgCdTe composition gradients by LPE.
```

It does **not**, in the recovered text, report the matched translated-gradient wavelength × RF inverse proposed here.

---

## 9. What the candidate distinction has now narrowed to

The potentially underexplored object is **not** any one ingredient below:

```text
graded HgCdTe
wavelength-dependent absorption depth
high-speed/RF response
built-in-gradient-field carrier acceleration
localized transit measurement
composition-profile engineering
matched-device differencing.
```

The surviving candidate is the combination:

```text
1. deliberately known graded x(z) used as a spectral position encoder;
2. complex response measured over wavelength AND RF frequency;
3. inversion restricted to differential/few-mode transport information;
4. a purpose-built matched control pair in which the same buried internal
   gradient feature is translated in depth while boundary conditions are held
   common;
5. causal validation by asking whether the wavelength x RF fingerprint moves
   with the internal feature.
```

A compact description is

> **matched-feature relocation tomography / metrology in a compositionally graded HgCdTe absorber.**

That phrase is descriptive, not a priority claim.

---

## 10. The relocation control is the scientifically strongest part

A simple A-versus-B comparison cannot uniquely attribute a spectral timing difference to an internal composition-gradient mechanism because contact/interface transport can mimic a near-boundary feature.

The purpose-built `G2-G1` control changes the logic:

```text
same contact/cap/junction environment
same endpoint compositions
same total composition change
same feature amplitude/width
but feature moved in depth.
```

If the measured wavelength × RF fingerprint moves as predicted by the optical spatial encoder, the mechanism attribution is substantially stronger.

This is the primary **validation logic** of the current project.

It is not yet established as novel.

---

## 11. The current interface-safe design makes the distinction cleaner

The latest numerical design also avoids claiming a special role for the published near-junction sample-A structure.

The current conservative purpose-built reference is approximately

```text
absorber thickness ~7.6 um
programmed feature width ~0.9-1.0 um
feature centers of order 4-6 um
feature kept ~1.5 um or more from both boundaries
wavelength band ~2.0-2.4 um
RF set currently 0.25-3 GHz.
```

That geometry is intentionally different from the earlier literature's boundary-adjacent gradient comparison.

Again, geometric difference is not proof of priority; it simply makes the experimental question more specific.

---

## 12. Claim discipline going forward

Until the 2024 Applied Optics paper is recovered and a broader search is complete, use only

> **candidate underexplored inverse-metrology / matched-relocation validation method; priority unproven.**

Do **not** use

```text
first
novel
new principle
previously impossible
first tomography of HgCdTe
or
first wavelength-dependent timing measurement.
```

The project should earn its contribution through a clean experimentally falsifiable inverse/relocation result, not through broad wording.

---

## 13. Next literature task

The highest-priority literature action is still to obtain the full technical content of

```text
Xu et al. 2024
DOI 10.5768/JAO202445.0310009.
```

Then search specifically for

```text
wavelength-resolved impulse response in compositionally graded HgCdTe
spectral transit-time inversion in graded semiconductor absorbers
translated/buried composition-gradient control structures
and matched relocation experiments in photodetectors.
```

Only after those collisions are resolved should novelty language be reconsidered.
