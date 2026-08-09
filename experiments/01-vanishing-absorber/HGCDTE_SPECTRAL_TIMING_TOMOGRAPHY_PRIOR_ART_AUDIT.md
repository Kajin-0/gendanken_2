# Spectral Timing Transport Tomography — Focused Prior-Art Audit

**Date:** 2026-08-09  
**Status:** focused collision search; negative search is not priority evidence

## 1. Candidate statement under review

The current repository result is not the broad statement

```text
wavelength changes photodiode response time.
```

That is established.

The narrower candidate is:

> In a monotonic graded-gap absorber, photon energy labels the earliest allowed generation position. Under path-additive collection, the derivative of intrinsic timing with photon energy can therefore reconstruct a local or optically kernel-averaged inverse carrier velocity.

Sharp limit:

```math
\boxed{
v_{\rm eff}[x_g(E_\gamma)]
=\frac1{G\,dT/dE_\gamma}.
}
```

Finite-depth asymptotic form:

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=\int p(z)\frac{dz}{v_{\rm eff}(x_g+z)}.
}
```

This audit asks whether that inversion/tomographic interpretation is already explicit in primary photodetector literature.

---

## 2. Wavelength-dependent generation depth and bandwidth are established

### Jang et al., IEEE Photonics Technology Letters 15, 281–283 (2003)

Title:

`Wavelength Dependent Characteristics of High-Speed Metamorphic Photodiodes`

DOI:

`10.1109/LPT.2002.806886`

The authors measured photodiode RF response at `0.85`, `1.33`, and `1.55 um`.

They report bandwidths of approximately

```text
43 GHz at 0.85 um
54 GHz at 1.33 um
62 GHz at 1.55 um
```

for the stated operating condition.

The physical interpretation explicitly distinguishes which heterostructure layers absorb each wavelength and notes that carriers generated in the large-gap drift layer at shorter wavelength require additional transit time.

This is direct prior art for

```text
wavelength
-> generation location/layer
-> carrier transit
-> bandwidth.
```

Therefore none of those ingredients can be claimed as new.

---

## 3. Wavelength-dependent generation profiles remain an active high-speed-PD design issue

A 2026 primary high-speed InGaAs/GaAsSb photodetector paper reports different measured bandwidths at `1.55 um` and `2.0 um` and attributes the difference to wavelength-dependent carrier-generation profiles: shorter-wavelength photons are also absorbed in contact material, creating a diffusion contribution, while the longer wavelength is absorbed more selectively in the fast intrinsic region.

This reinforces that

```text
spectral generation profile
-> timing / bandwidth
```

is current, established photodiode physics rather than an HgCdTe-specific novelty.

---

## 4. Graded-bandgap structures are established high-speed tools

Primary high-speed photodiode literature uses graded-bandgap regions to create built-in fields and reduce carrier transit times.

Examples include

- graded collector/absorber structures in uni-traveling-carrier photodiodes;
- graded HgCdTe APDs where composition grading reduces diffusion and improves impulse response;
- zero-bias graded-band photodiodes designed to trade absorption thickness against transit response.

Thus

```text
gap grading
-> built-in carrier drive
-> faster transport
```

is established prior physics.

---

## 5. HgCdTe-specific prior art already links grading to impulse response

Singh et al., *Solid-State Electronics* 142, 41–46 (2018), DOI

`10.1016/j.sse.2018.02.002`

explicitly report the effect of bandgap grading on the impulse response of an HgCdTe e-APD and state that grading minimizes diffusion so the response becomes transit-time limited.

This is strong prior art adjacent to the active repository branch.

It does not, in the inspected source, formulate the wavelength sweep as a spatial transport inversion.

---

## 6. What the focused search did not locate

The inspected primary literature did **not** reveal an explicit photodiode method of the form

```text
known monotonic Eg(x)
+
wavelength-resolved intrinsic timing T(E_gamma)
->
dT/dE_gamma
->
local carrier velocity / inverse-velocity profile.
```

Nor did the inspected sources state the finite-depth generalization

```text
spectral timing derivative
-> known optical generation kernel convolved with inverse velocity
-> spatial deconvolution / transport tomography.
```

The literature located generally uses wavelength dependence to

- explain different bandwidths;
- identify slow absorption layers;
- optimize detector structure;
- compare responsivity/QE;
- probe hot-carrier dynamics in other spectroscopies.

That is not the same as explicitly using the spectral timing derivative as an internal spatial transport coordinate.

---

## 7. Important adjacent spectroscopy

Other semiconductor spectroscopies use excitation wavelength to probe carrier dynamics, density of states, penetration depth, or dynamic forces.

This means the general idea

```text
spectral excitation
-> internal spatial/energy selectivity
-> transport information
```

is not conceptually new.

Any future claim must therefore be detector- and equation-specific.

The potentially distinct object is the graded-photodiode inversion itself, not the broad notion of wavelength-dependent transport spectroscopy.

---

## 8. Current collision verdict

### Established — do not claim novelty

- wavelength-dependent absorption/generation depth in photodiodes;
- wavelength-dependent photodiode bandwidth and impulse response;
- transit-time differences caused by wavelength selecting different generation regions;
- graded-bandgap acceleration in high-speed photodiodes;
- graded HgCdTe timing improvement.

### Candidate underexplored formulation

The exact inversion

```math
\boxed{
v_{\rm eff}
=\frac1{G\,dT/dE_\gamma}
}
```

in the sharp linear-gradient/path-additive limit, and its finite-depth kernel form,

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=\int p(z)v^{-1}(x_g+z)dz,
}
```

were not found explicitly in the inspected primary detector literature.

**Status:** candidate underexplored detector-facing inverse method; priority unproven.

A negative search is not evidence of novelty.

---

## 9. Reviewer-level risk

A skeptical reviewer could reasonably say

> wavelength-dependent absorption depth and transit time are old; differentiating the integral transit time is elementary.

That criticism is currently credible.

For the result to become publication-relevant, the project should demonstrate that the inversion provides something experimentally useful that existing wavelength-dependent bandwidth studies did not:

- reconstruct a nonuniform transport profile;
- recover a known synthetic profile under finite optical depth/noise;
- identify a transport anomaly not visible in ordinary bandwidth data;
- validate against independent transport modeling or measurements.

The value must come from the **inverse measurement capability**, not from the algebra alone.

---

## 10. Next decisive work

Do not promote novelty yet.

Build a synthetic inverse problem with

```text
known nonuniform v(x)
+
finite alpha(E,x)
+
realistic wavelength sampling
+
timing noise / common readout delay
```

and determine

1. spatial resolution;
2. inversion bias;
3. noise amplification from differentiation;
4. whether regularized kernel inversion recovers `1/v(x)` robustly;
5. what experimental timing precision is required.

If the inversion is numerically useful under realistic conditions, then revisit the literature boundary and publication significance.
