# HgCdTe Spectral Transit Prior-Art Audit — Does Grading Explicitly Couple Wavelength to Timing?

**Date:** 2026-08-09  
**Status:** focused primary-source collision search; negative search is not priority evidence

## 1. Candidate connection being tested

The current graded-detector calculation predicts

```text
photon wavelength
-> first/likely generation position in Eg(x)
-> remaining graded transport distance
-> ballistic/scattering transit
-> wavelength-resolved response delay and generation-position timing spread.
```

After correcting photoexcitation energy partition, the strongest high-optical-depth prediction is more specific:

> **intrinsic ballistic transit delay rises from the long-wave endpoint to a maximum at the photon energy equal to the entrance band gap, then decreases for higher photon energy because the generation point is pinned at the entrance while initial electron kinetic energy continues to rise.**

The narrow prior-art question is whether primary HgCdTe literature already derives or measures this spectral timing fingerprint.

---

## 2. Grading and response time are established prior physics

### Singh et al., Solid-State Electronics 142, 41-46 (2018)

`Impulse response measurement in the HgCdTe avalanche photodiode`

DOI: `10.1016/j.sse.2018.02.002`

The paper explicitly reports band-gap grading in an `n+/nu/p+` HgCdTe e-APD and attributes improved impulse response to reduced diffusion / transit-time-limited carrier transport.

Established:

```text
grading -> faster carrier transport -> faster response.
```

The accessible article record does not present a wavelength sweep of intrinsic transit time through the graded absorption edge.

### High speed uncooled MWIR infrared HgCdTe photodetector based on graded bandgap structure (2022)

DOI: `10.11972/j.issn.1001-9014.2022.06.005`

This work reports a graded HgCdTe detector with approximately `1.33 ns` response at room temperature and models the composition-gradient built-in field.

The impulse/frequency-response measurements described in the accessible primary article use fixed short-wave sources around `1.55 um`; switching measurements also use `2 um` illumination.

Thus the paper strongly establishes

```text
grading -> built-in field -> faster response
```

but does not provide the wavelength scan through the device's graded infrared absorption edge needed to test the present prediction.

### Martyniuk et al., Optical and Quantum Electronics 46, 1303-1312 (2014)

`Modeling of HOT (111) HgCdTe MWIR detector for fast response operation`

The work models response time versus architecture and bias in graded/multilayer HgCdTe and compares with experiment.

Again, this establishes sophisticated response modeling but not the present wavelength-resolved generation-position timing map.

---

## 3. Grading and spectral response are also established separately

### FDTD simulation of compositionally graded HgCdTe photodetectors, Infrared Physics & Technology 97, 203-209 (2019)

DOI: `10.1016/j.infrared.2018.12.041`

This work treats realistic composition profiles in full-wave optical calculations and shows that grading materially modifies spectral QE/cutoff behavior.

Established:

```text
grading -> spatial optical profile -> spectral QE.
```

The inspected work is not a spectral carrier-timing calculation.

### Graded-HgCdTe device optimization literature

Multiple HOT HgCdTe device papers optimize graded interfaces, absorber thickness, responsivity, dark current, and response time together.

These are important architectural prior art. They do not by themselves establish the present spectral timing extremum.

---

## 4. HgCdTe Kane optical-transition prior art

Primary magneto-optical HgCdTe work uses a simplified Kane model with

```text
conduction electron branch
light-hole branch
nearly flat heavy-hole branch.
```

Observed interband transitions include heavy-hole-to-electron transitions.

This makes the repository heavy-hole baseline

```math
\xi_e\approx1
```

a direct model consequence rather than a claimed new material property.

Therefore do not claim novelty for the statement that a heavy-hole transition can place most photon excess into the electron.

---

## 5. Existing wavelength-dependent HgCdTe timing measurements

### Soderman and Pinkston, Applied Optics 11, 2162-2168 (1972)

Response measurements were performed at several wavelengths.

The approximately `10 ns` detector-module response was reported as not strongly wavelength dependent because RC/amplifier bandwidth dominated. With a broadband amplifier, a secondary several-nanosecond carrier-transit contribution appeared.

This is useful caution:

> intrinsic spectral transit structure can be hidden by a common readout pole.

The device was not the graded architecture analyzed here.

### Grodecki et al., Metrology and Measurement Systems 24, 509-514 (2017)

A tunable OPO covering roughly `1.55-16 um` was available in the response-time experiment.

The inspected primary article presents spectral responsivity and time-response characterization, but does not report a systematic wavelength-resolved intrinsic timing curve through a graded absorption edge.

This remains one of the most relevant experimental templates for a future test.

---

## 6. Current collision verdict

### Established prior physics — no novelty claim

- compositionally graded HgCdTe detectors;
- grading-induced carrier drift / reduced diffusion;
- graded HgCdTe response-time improvement;
- spectral-QE modeling of graded HgCdTe;
- spatial generation distance as a carrier-transit variable;
- tunable-wavelength ultrafast HgCdTe characterization;
- heavy-hole-to-electron Kane optical transitions.

### Candidate underexplored analytic connection

The focused search has **not** located an inspected primary HgCdTe source explicitly deriving or plotting

```text
lambda
-> generation-position distribution in Eg(x)
-> corrected photoelectron initial energy
-> graded transit-time distribution.
```

### Stronger candidate prediction

The search also has not located an inspected primary source predicting the high-optical-depth intrinsic timing shape

```text
near output cutoff:
T -> 0 in the ideal transport model

within graded gap range:
T rises as generation moves upstream

at E_gamma = Eg,in:
T reaches a maximum

above entrance gap:
generation stays at entrance
initial electron kinetic energy rises
T decreases toward L/vK.
```

**Status:** CANDIDATE DISTINCT / UNDEREXPLORED ANALYTIC PREDICTION — PRIORITY UNPROVEN.

A negative search is not evidence of novelty.

---

## 7. Why the entrance-gap timing peak is a stronger target

Compared with the earlier abstract resource bounds, this prediction is

- material/device specific;
- dimensionless in shape;
- tied directly to the engineered composition profile;
- falsifiable with a tunable ultrafast source;
- predicted to have a specific extremum wavelength;
- separable, in principle, from a wavelength-independent RC/readout pole.

It is therefore a better experimental/theoretical target even before publication status is reconsidered.

---

## 8. Decisive next validation

The next validation should target one compositionally graded HgCdTe device and sweep pulse wavelength across

```text
output cutoff
-> graded absorption range
-> entrance-gap wavelength
-> shorter-than-entrance wavelengths.
```

Under fixed bias, temperature, spot geometry, and readout, extract

```text
pulse centroid / mean delay
rise time / fall time
frequency response where possible
spectral responsivity / absorbed fraction.
```

Then de-embed or jointly fit the common electrical transfer function.

If no suitable published data exist, formulate this as the concrete proposed experiment.

Do not claim the timing peak has been observed.
