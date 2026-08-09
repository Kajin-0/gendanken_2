# Proposed Experiment — Tunable-Wavelength Timing Sweep of a Compositionally Graded HgCdTe Detector

**Date:** 2026-08-09  
**Status:** proposed falsification experiment for the spectral-delay-peak prediction; no claim that the effect has been observed

## 1. Prediction being tested

For a monotonic graded absorber with entrance gap `E_g,in` and narrow-gap output `E_g,out`, the current high-optical-depth transport model predicts

```text
near output cutoff:
short intrinsic collection delay

photon energy rises through graded gap range:
first allowed generation point moves upstream
collection delay rises

E_gamma = E_g,in:
intrinsic collection delay reaches a maximum

E_gamma > E_g,in:
generation point is pinned at the physical entrance
additional photon energy increases electron kinetic energy
delay decreases toward a full-length high-energy floor.
```

The predicted timing extremum occurs near

```math
\boxed{
\lambda_{\rm peak}
\simeq
hc/E_{g,\rm in}.
}
```

The experiment should try to falsify that shape.

---

## 2. Device requirement

Use a detector with a known monotonic composition/gap profile through the carrier-collection direction.

Required structural information:

```text
SIMS or equivalent Cd-composition profile x_Cd(z)
absorber thickness
junction / collection-side orientation
entrance and output compositions
operating temperature
bias condition.
```

Convert composition to `E_g(z,T)` using one documented HgCdTe gap model.

The experiment is most informative when the device is already known or designed to be close to transit limited rather than strongly RC limited.

---

## 3. Wavelength sweep

Sweep pulsed excitation across all three spectral regimes:

```text
A. near the narrow-gap output cutoff
B. through the graded-gap interval
C. shorter wavelength than the entrance-gap cutoff.
```

At minimum include points on both sides of the predicted peak.

If the output cutoff is `lambda_c,out` and the entrance gap corresponds to `lambda_c,in`, target a sweep such as

```text
slightly shorter than lambda_c,out
several points between lambda_c,out and lambda_c,in
one point near lambda_c,in
several points shorter than lambda_c,in.
```

Do not infer the peak from only two wavelengths.

---

## 4. Optical conditions

Keep fixed as closely as possible:

```text
incident pulse energy in the linear-response regime
spot position and diameter
polarization
angle of incidence
repetition rate
average detector heating
bias
temperature
readout chain.
```

Monitor the reference optical pulse at each wavelength so source timing and wavelength-dependent optical path delay are not mistaken for detector delay.

Avoid intensities that introduce

- two-photon absorption;
- carrier-density-dependent screening;
- nonlinear heating;
- avalanche changes unrelated to the small-signal transport under test.

---

## 5. Primary observable — differential group delay

Represent the measured small-signal transfer function as

```math
\boxed{
H_{\rm meas}(\Omega,\lambda)
=
H_{\rm det}(\Omega,\lambda)
H_{\rm common}(\Omega),
}
```

where `H_common` contains wavelength-independent electronics/readout response.

The low-frequency group delay is

```math
\tau_g(\lambda)
=-\left.
\frac{d}{d\Omega}
\arg H(\Omega,\lambda)
\right|_{\Omega\to0}.
```

For two wavelengths,

```math
\boxed{
\Delta\tau_g(\lambda_1,\lambda_2)
=
-\left.
\frac{d}{d\Omega}
\arg\left[
\frac{H_{\rm meas}(\Omega,\lambda_1)}
{H_{\rm meas}(\Omega,\lambda_2)}
\right]
\right|_{\Omega\to0}.
}
```

The common readout transfer cancels exactly if it is unchanged between the measurements.

This makes differential group delay a better primary observable than raw pulse FWHM or rise time.

---

## 6. Time-domain equivalent

If impulse responses are measured directly, normalize each response to unit area after background subtraction.

For a normalized causal impulse `h(t)`, define temporal centroid

```math
\boxed{
\bar t(\lambda)
=\int t h(t;\lambda)dt.
}
```

For convolution with a common normalized readout impulse,

```math
h_{\rm meas}
=h_{\rm det}*h_{\rm common},
```

centroids add:

```math
\boxed{
\bar t_{\rm meas}(\lambda)
=
\bar t_{\rm det}(\lambda)
+
\bar t_{\rm common}.
}
```

Therefore wavelength differences cancel the common centroid delay:

```math
\boxed{
\Delta\bar t_{\rm meas}
=
\Delta\bar t_{\rm det}.
}
```

This is the time-domain analogue of differential low-frequency group delay.

Raw rise time and FWHM do not enjoy this exact additive property.

---

## 7. Collection-kernel interpretation

The present theory predicts a distribution of carrier collection times rather than a complete terminal-current waveform.

For generation-position density

```math
p(x|\lambda,{\rm abs}),
```

and collection time

```math
T_c(x),
```

define the ideal collection-flux kernel

```math
\boxed{
h_{\rm col}(t|\lambda)
=
\int dx\,
p(x|\lambda,{\rm abs})
\delta[t-T_c(x)].
}
```

Its transfer function is

```math
\boxed{
H_{\rm col}(\Omega|\lambda)
=
\int dx\,
p(x|\lambda,{\rm abs})
e^{-i\Omega T_c(x)}.
}
```

and

```math
\boxed{
-\left.
\frac{d}{d\Omega}
\arg H_{\rm col}
\right|_{\Omega=0}
=\langle T_c\rangle.
}
```

Thus low-frequency group delay directly probes the first moment of the intrinsic collection-time distribution in this idealization.

A real terminal response can include weighting-field, diffusion, avalanche, junction and electronics effects; these must be modeled or de-embedded if they vary with wavelength.

---

## 8. Predicted qualitative result

Plot differential intrinsic delay versus photon energy or wavelength.

The target signature is

```text
long-wave side:
delay increases as wavelength becomes shorter and the first allowed generation point moves upstream

near lambda_c,in:
delay maximum

short-wave side:
delay decreases as photon energy continues to rise while the generation point remains pinned at the entrance.
```

The ballistic model predicts a sharp geometric regime change at `E_gamma=E_g,in`; finite optical depth and scattering should smooth it.

---

## 9. Strong falsifiers

The present theory would be seriously challenged if, after accounting for wavelength-dependent source timing and common electronics,

- no timing structure is seen across a device with a large known gap gradient and transit-limited response;
- the delay extremum occurs far from the entrance-gap wavelength without an identifiable optical/profile reason;
- the long-wave side does not shorten toward the narrow-gap endpoint despite a well-resolved graded generation region;
- a realistic drift-diffusion/Monte Carlo model using the measured composition profile predicts the opposite trend.

A null result is scientifically useful.

---

## 10. Controls

### Ungraded control detector

Measure an otherwise similar nearly uniform-gap detector.

It should not show the same entrance-gap timing extremum because there is no continuously moving first-allowed-generation boundary inside the absorber.

### Bias sweep

Repeat at several biases.

A composition-geometric spectral feature should have a comparatively stable characteristic wavelength even though the absolute delays may move with bias.

### Temperature sweep

Changing temperature moves the HgCdTe band gap. Therefore the predicted timing-peak wavelength should shift with the entrance-gap temperature dependence if the effect is genuinely tied to `E_g,in(T)`.

This is a particularly strong discriminator against a fixed electronic artifact.

---

## 11. Existing experimental precedent

Primary HgCdTe literature already demonstrates the required pieces of instrumentation:

- ultrafast impulse-response measurements on HgCdTe;
- tunable optical parametric sources spanning broad infrared wavelength ranges;
- graded HgCdTe devices whose response approaches transit limitation;
- fixed-wavelength high-speed measurements with tens-of-picoseconds to femtosecond optical excitation.

The focused prior-art search has not found the proposed spectral timing sweep across the graded absorption edge reported as such.

---

## 12. Minimum useful dataset

For each wavelength record

```text
reference optical pulse timing
incident pulse energy
spectral responsivity / absorbed signal amplitude
normalized detector impulse response
centroid delay
rise/fall metrics as secondary observables
bias
temperature.
```

Also retain the measured composition profile and device orientation so the predicted `lambda_peak` can be computed independently of the timing data.

---

## 13. Success criterion

The experiment is interesting even if the absolute timing cannot be matched perfectly.

The strongest first validation would be

```text
measured intrinsic/differential delay has a reproducible extremum
near the independently predicted entrance-gap wavelength
and the extremum shifts with entrance-gap temperature dependence.
```

That would justify replacing the current analytic transport kernel with a calibrated device model.

---

## 14. Publication posture

Do not claim this experiment is unprecedented until a broader experimental literature audit is complete.

At present it is a **concrete falsification experiment for a candidate underexplored analytic prediction**.
