# HgCdTe Spectral Transit Prior-Art Audit — Does Grading Explicitly Couple Wavelength to Timing?

**Date:** 2026-08-09  
**Status:** focused primary-source collision search; negative search is not priority evidence

## 1. Candidate connection being tested

The current graded-detector calculation predicts the chain

```text
photon wavelength
-> earliest/local generation position from Eg(x)
-> generation-position probability distribution
-> remaining graded conduction-band drop
-> carrier transit time / hot-electron exposure
-> wavelength-resolved response delay and generation-position jitter.
```

The question for this audit is not whether graded HgCdTe or fast HgCdTe detectors are known. They are.

The narrow question is:

> **Has primary HgCdTe literature already made this explicit wavelength -> generation-position -> graded-transit/timing connection?**

## 2. Primary work that already covers grading and response time

### Singh et al., Solid-State Electronics 142, 41-46 (2018)

Title: `Impulse response measurement in the HgCdTe avalanche photodiode`

DOI: `10.1016/j.sse.2018.02.002`

The paper explicitly reports the effect of band-gap grading on impulse response in an `n+/nu/p+` HgCdTe e-APD. Its stated mechanism is reduction of carrier diffusion so that the response becomes transit-time limited.

This establishes

```text
composition grading -> carrier transport -> response time
```

as prior HgCdTe physics.

It does not, in the inspected abstract/metadata, state the wavelength-resolved generation-position timing map derived in this repository.

### Grodecki et al., Metrology and Measurement Systems 24, 509-514 (2017)

Title: `Fast Response Hot (111) HgCdTe MWIR Detectors`

DOI: `10.1515/mms-2017-0044`

The response was measured using approximately 25 ps pulses from a tunable OPO covering `1.55-16 um`.

The inspected article reports spectral responsivity separately and presents the time response primarily as a function of bias/readout conditions. It does not appear to extract a wavelength-resolved transit-time law from the tunable source.

This paper is especially relevant experimental prior art because the measurement apparatus could in principle probe the effect now predicted.

### Martyniuk et al., Optical and Quantum Electronics 46, 1303-1312 (2014)

Title: `Modeling of HOT (111) HgCdTe MWIR detector for fast response operation`

The paper models fast response in a graded/multilayer HgCdTe detector and compares against experiment. The inspected article states that the time-response simulation used a particular laser wavelength and treats device architecture/bias dependence.

This establishes sophisticated coupled detector-response modeling but not the explicit spectral timing map found here.

## 3. Primary work that already covers grading and spectral response

### FDTD simulation of compositionally graded HgCdTe photodetectors, Infrared Physics & Technology 97, 203-209 (2019)

DOI: `10.1016/j.infrared.2018.12.041`

This work treats realistic composition profiles in full-wave optical calculations and shows that grading can materially affect quantum-efficiency spectra and cutoff estimates.

This establishes

```text
composition grading -> spatial optical properties -> spectral QE
```

as prior physics.

The inspected paper is an electromagnetic/spectral modeling paper rather than a wavelength-resolved carrier-timing treatment.

### High speed uncooled MWIR infrared HgCdTe photodetector based on graded bandgap structure (2022)

The primary journal article models a linearly graded p-type region, composition-induced built-in field, quantum efficiency / spectral response, and response time of graded HgCdTe photodiodes.

This is the closest inspected collision because optical and transport properties are treated in the same graded device.

The available text explicitly links grading to carrier evacuation and improved frequency response. However, the inspected sections do not state the specific mapping

```text
photon wavelength
-> first allowed generation position
-> remaining graded transport distance
-> wavelength-dependent delay distribution.
```

## 4. Related non-graded wavelength-response timing result

Soderman and Pinkston, Applied Optics 11, 2162-2168 (1972), measured HgCdTe photodiode response using several optical wavelengths.

They reported no strong wavelength dependence in the approximately `10 ns` module response under their conditions because electronics/RC limitations dominated. A much faster broadband readout exposed a secondary carrier-transit timescale.

This is useful caution:

> even if a graded absorber has an intrinsic wavelength-dependent transit contribution, ordinary RC/readout poles can hide it experimentally.

## 5. Current collision verdict

### Established prior physics

Do not claim novelty for

- graded HgCdTe photodetectors;
- grading-induced carrier drift / reduced diffusion;
- the effect of grading on detector response time;
- spectral-response / QE modeling of compositionally graded HgCdTe;
- spatial generation distance as a contributor to drift/diffusion response time;
- tunable-wavelength ultrafast characterization of HgCdTe detectors.

### Candidate underexplored connection

The focused search did **not** locate an inspected primary HgCdTe source explicitly deriving or plotting

```text
lambda
-> conditional generation-position distribution in Eg(x)
-> remaining graded carrier drive
-> wavelength-resolved mean transit and timing spread.
```

The repository currently has closed-form expressions for that connection in the simplified linear/Kane/Beer-Lambert model.

**Status:** candidate underexplored detector-facing synthesis / analytic reduction; priority unproven.

A negative literature search is not evidence of novelty.

## 6. Why this direction is stronger than the earlier abstract branches

The candidate connection is

- specific to a real photodetector material architecture;
- directly measurable with a tunable pulsed IR source;
- naturally linked to both spectral QE and time response;
- capable of making a wavelength-dependent prediction rather than only a broad resource statement;
- already adjacent to existing graded-HgCdTe experiments, which makes validation plausible.

This does not make it publishable yet.

## 7. Decisive next validation

The next step should not be another generic literature search.

Build the wavelength-resolved analytic baseline for a realistic example profile and predict

```text
absorptance(lambda)
mean generation position(lambda)
mean ballistic transit(lambda)
generation-position timing spread(lambda)
mean-II margin(lambda).
```

Then compare the trend against any published tunable-pulse HgCdTe data that expose multiple wavelengths under otherwise fixed bias/readout conditions.

If published data are insufficient, the result becomes a concrete proposed experiment rather than a claimed observed effect.
