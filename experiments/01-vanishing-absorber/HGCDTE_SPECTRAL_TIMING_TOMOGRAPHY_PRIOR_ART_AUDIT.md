# Spectral Timing Transport Tomography — Focused Prior-Art Audit

**Date:** 2026-08-09  
**Status:** focused collision search; negative search is not priority evidence

## 1. Candidate statement under review

The repository is **not** claiming that wavelength-dependent absorption depth changes photodiode response time. That is established.

The narrower candidate is:

> In a monotonic graded-gap absorber, photon energy provides an internal position coordinate. If the wavelength-dependent generation kernel is known, wavelength-resolved timing can be inverted to recover a spatial carrier-delay / effective-velocity profile.

Sharp limit:

```math
\boxed{
v_{\rm eff}[x_g(E_\gamma)]
=\frac1{G\,dT/dE_\gamma}.
}
```

Finite-depth linear inverse:

```math
\boxed{
\bar T_i
=\int_0^L K_i(s)q(s)ds,
\qquad
q(s)=1/v_{\rm eff}(s),
}
```

with

```math
\boxed{
K_i(s)
=P(X_g\le s|E_{\gamma,i},{\rm abs}).
}
```

---

## 2. Wavelength-dependent generation depth and photodiode bandwidth are established

### Jang et al., IEEE Photonics Technology Letters 15, 281–283 (2003)

DOI `10.1109/LPT.2002.806886`.

The authors measured RF response at `0.85`, `1.33`, and `1.55 um` and explicitly interpreted the wavelength dependence through different carrier-generation layers and corresponding transit paths.

This is direct prior art for

```text
wavelength
-> generation region
-> carrier transit
-> bandwidth.
```

None of those ingredients is new.

Modern high-speed photodiode work continues to attribute wavelength-dependent bandwidth to wavelength-dependent carrier-generation profiles.

---

## 3. Graded-bandgap acceleration is established

Primary high-speed detector literature uses graded bandgap / composition profiles to create internal carrier drive and reduce transit delay.

This includes

- uni-traveling-carrier photodiodes;
- zero-bias graded-band photodiodes;
- graded HgCdTe detectors and e-APDs.

Therefore

```text
graded bandgap
-> built-in carrier drive
-> faster response
```

is established.

---

## 4. HgCdTe already has direct position-resolved impulse-response prior art

### Perrais et al., Journal of Electronic Materials 38, 1790–1799 (2009)

DOI `10.1007/s11664-009-0802-7`.

The paper reports HgCdTe APD impulse-response measurements using **localized photoexcitation at varying positions in the depletion layer**.

Therefore the broad measurement concept

```text
choose carrier-generation position
-> measure impulse response / transit behavior
```

already exists directly in HgCdTe.

The repository cannot claim spatial transit-time mapping itself.

---

## 5. HgCdTe grading and timing are established

### Singh et al., Solid-State Electronics 142, 41–46 (2018)

DOI `10.1016/j.sse.2018.02.002`.

This work explicitly reports the effect of bandgap grading on HgCdTe e-APD impulse response and states that composition grading reduces diffusion so the response becomes transit-time limited.

Thus both

```text
position-dependent transit timing
```

and

```text
grading-dependent transit timing
```

are strong prior art in HgCdTe.

---

## 6. Major closer collision — 2022 graded HgCdTe already couples wavelength-dependent generation and response modeling

Sang, Xu, Qiao and Li,

`High speed uncooled MWIR infrared HgCdTe photodetector based on graded bandgap structure`,

*Journal of Infrared and Millimeter Waves* 41 (2022) 972–979,

DOI `10.11972/j.issn.1001-9014.2022.06.005`.

This paper is closer to the current repository method than a generic wavelength-dependent bandwidth study.

For a graded n-on-p HgCdTe photodiode, the authors explicitly write the wavelength- and depth-dependent photogeneration rate

```math
\boxed{
G_L(z,\lambda)
=\alpha(z,\lambda)\phi_0
\exp\!\left[-\int_0^z\alpha(u,\lambda)du\right].
}
```

They also model

```text
spatially varying composition / bandgap
+
gradient-built electric field
+
carrier continuity / current transport
+
quantum efficiency
+
response time.
```

The same article measures the VPE detector's high-speed response and attributes the improvement to the larger composition-gradient built-in field.

Therefore the repository must **not** claim that it is new to combine

```text
wavelength-dependent spatial generation
+
graded HgCdTe transport
+
response-time modeling.
```

That combined forward-model structure is already present in primary HgCdTe work.

---

## 7. Why the 2022 timing data still do not perform the proposed inversion

The 2022 timing experiment used approximately `1.55 um` excitation.

The authors explicitly note that the large absorption coefficient at `1550 nm` causes strong surface absorption.

Their VPE composition spans approximately `x=0.57 -> 0.31`, so `1.55 um` lies on the short-wave side where the entrance region is already optically allowed.

Thus the published timing measurement does not sweep the generation kernel through the graded layer.

It validates the **forward** graded-transport picture, but does not solve the inverse problem

```text
T(lambda)
->
q(z)=1/v_eff(z).
```

---

## 8. 2023 graded HgCdTe already uses spectral response to infer spatial collection differences

Xu et al.,

`Photoelectric characteristics of compositionally graded HgCdTe detector`,

*Journal of Infrared and Millimeter Waves* 42 (2023) 285–291,

DOI `10.11972/j.issn.1001-9014.2023.03.001`.

The study compares processed graded VPE samples of approximately `7.6 um` and `3.7 um` thickness and retains/removes different parts of a nonlinear composition-gradient region.

The authors attribute the samples' differing spectral/photoelectric behavior to the gradient-induced built-in field acting on minority-carrier motion.

This is strong prior art for

```text
spectral response
-> inference about spatial carrier collection in a graded HgCdTe structure.
```

Again, this substantially narrows any novelty claim.

---

## 9. What remains potentially distinct

After these collisions, the candidate is **not**

- wavelength-dependent generation depth;
- wavelength-dependent transit time;
- position-resolved HgCdTe timing;
- graded HgCdTe acceleration;
- wavelength-dependent generation plus graded-HgCdTe response modeling;
- using spectra qualitatively to infer spatial collection.

The narrower candidate is:

> **use the monotonic band-gap profile as an internal spectral position encoder and solve the measured wavelength-resolved timing dataset as an inverse problem for a spatial transport quantity such as `q(x)=1/v_eff(x)`.**

In other words, the possible value is not a new forward model.

It is an **inverse metrology method** that may replace or complement a physically localized excitation scan.

---

## 10. Full finite-depth inverse formulation

The repository writes the timing data as

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q+c\mathbf1,
}
```

where

```math
q_j\approx1/v_{\rm eff}(x_j)
```

and each row of `A` is calculated from the cumulative wavelength-dependent generation kernel.

This formulation provides several differences from ordinary forward bandwidth modeling:

- finite optical depth enters explicitly through the measured/calculated optical kernel;
- an unknown wavelength-independent electronics delay can be fitted as nuisance parameter `c`;
- regularization allows spatial transport reconstruction;
- the result is an internal delay-density profile rather than only a predicted total response time.

---

## 11. Synthetic inversion and conditioning results

The repository regressions show that the inverse is mathematically usable in controlled synthetic cases.

`numerics/hgcdte_spectral_timing_linear_inverse.py` uses

```text
nonuniform synthetic v(x)
finite optical generation kernels
unknown common delay
0.1% timing noise.
```

For the frozen regression case it reconstructs the velocity profile with roughly `0.9%` RMS relative error and localizes an imposed slow-transport region to about one numerical cell while recovering the common delay.

This is **not** an experimental performance claim.

The singular-value audit also shows the method is spatially band limited: broad optical kernels rapidly reduce the number of recoverable transport modes.

---

## 12. Reviewer-level risk is now high and explicit

A skeptical reviewer can say

> the forward physics is already in the 2022 HgCdTe paper, spatial timing is already in Perrais, and the remaining inversion is straightforward linear inverse mathematics.

That criticism is credible.

Therefore the algebra alone is not sufficient for publication significance.

The method becomes scientifically valuable only if spectral encoding demonstrates a practical capability such as

- reconstructing a buried/nonuniform transport profile without a spatially localized excitation scan;
- identifying a slow transport region that ordinary total bandwidth does not localize;
- working in a device geometry where physical spot scanning of the internal depth is impractical;
- agreeing quantitatively with an independent localized-position or Monte Carlo transport profile;
- producing an experimentally robust profile while fitting common readout delay simultaneously.

---

## 13. Current collision verdict

### Established — no novelty claim

- wavelength-dependent absorption / generation depth;
- wavelength-dependent photodiode bandwidth;
- wavelength-dependent generation layers controlling transit;
- graded-bandgap carrier acceleration;
- graded HgCdTe impulse-response improvement;
- localized-position HgCdTe transit-time measurements;
- wavelength- and depth-dependent photogeneration in a graded HgCdTe forward response model;
- spectral inference of spatial carrier collection in graded HgCdTe.

### Candidate underexplored method

The inspected primary sources did not locate the specific inversion

```text
known monotonic Eg(x)
+
known p(x|lambda)
+
wavelength-resolved timing dataset
->
regularized reconstruction of spatial delay density q(x).
```

**Status:** candidate underexplored inverse-metrology method; priority unproven.

Negative search is not evidence of novelty.

---

## 14. Best validation path

The strongest validation is now straightforward:

1. independently measure `E_g(x)` / `x_Cd(x)`;
2. calculate or measure `p(x|lambda)`;
3. measure wavelength-resolved group delay / impulse centroid under fixed device conditions;
4. invert for `q(x)`;
5. independently obtain position-resolved transit information using localized excitation or a validated transport model;
6. compare profiles.

Agreement would demonstrate the **inverse measurement capability**, which is the only part still plausibly distinct.

---

## 15. Next decisive work

Do not expand the analytic theory further for its own sake.

The next high-value work is real-device forward/inverse modeling:

- use a published dimensional composition profile;
- calculate wavelength-dependent generation kernels;
- quantify spatial resolution from optical kernel, wavelength resolution and timing noise;
- predict the timing dataset needed to recover a known synthetic or independently measured transport profile.

Only after that should publication significance be reassessed.
