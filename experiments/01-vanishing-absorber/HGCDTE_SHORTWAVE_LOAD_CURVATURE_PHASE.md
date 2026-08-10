# Short-Wave Optical-Load Curvature Phase — A Causal Route Around the Static Sample-A Baseline

**Date:** 2026-08-09  
**Status:** derived load-differential observable plus conditional white-noise resource calculation; illustrative A-localized curvature amplitude; no real strong-injection timing data; no novelty claim

## 1. Why change the causal perturbation?

The current inverse has reached a structural conflict:

```text
short wavelengths
-> give the strongest leverage on sample A's near-junction nonlinear region

but

temperature changes
-> move the full short-wave optical kernel too strongly for clean subtraction.
```

Static spectral self-calibration also fails badly because the leading short-wave A smooth mode is almost invisible in the mid/deep scan.

Therefore the next perturbation should ideally

1. change carrier transport;
2. leave temperature and wavelength fixed;
3. leave the normalized optical generation kernel approximately fixed;
4. cancel the unknown static A/B transport baseline.

Optical loading is a natural candidate.

---

## 2. Why optical load is physically relevant but not novel forward physics

The published 2023 sample-A/B study interprets the effect of composition-gradient field partly in terms of reducing space-charge accumulation under large injection and increasing saturation threshold.

Related 2023 and 2024 HgCdTe modeling explicitly treats

```text
strong illumination
carrier accumulation
heating
zero-bias impedance change
composition-gradient electric fields
responsivity/saturation
wavelength and temperature dependence.
```

Relevant sources include:

- G.-Q. Xu et al., `Photoelectric characteristics of compositionally graded HgCdTe detector`, *Journal of Infrared and Millimeter Waves* 42 (2023) 285-291, DOI `10.11972/j.issn.1001-9014.2023.03.001`;
- X.-Y. Li et al., `Simulation on the saturation properties of room-temperature mid-wave infrared HgCdTe detectors`, *Journal of Infrared and Millimeter Waves* 42 (2023) 143-148, DOI `10.11972/j.issn.1001-9014.2023.02.001`;
- J. Chen et al., `Multi-Physics Field Based Simulation on the Response and Saturation Properties of Hg1-xCdxTe Based Photovoltaic Detectors With Composition Gradients`, *IEEE Photonics Journal* 16 (2024), DOI `10.1109/JPHOT.2024.3427322`;
- J. Chen et al., `Performance Optimization of Hg1-xCdxTe Photovoltaic Detectors Under Strong Illumination Considering Temperature and Wavelength Dependencies`, *IEEE Photonics Journal* 16 (2024), DOI `10.1109/JPHOT.2024.3470871`.

Therefore **illumination-dependent saturation or composition-gradient mitigation of strong-injection effects is not a novelty claim**.

The candidate use here is narrower:

> use wavelength-resolved **RF timing phase versus optical load** as a causal inverse observable for the spatial transport response.

Priority for that measurement remains unproven.

---

## 3. Fixed-temperature, fixed-wavelength load model

Let `P` denote a controlled optical-load coordinate at fixed temperature and fixed photon wavelength.

Write the device phase as

```math
\phi_d(\lambda,\Omega,P)
=
\phi_{\rm src}
+
\phi_{{\rm chain},d}
-
\Omega\,
\mathbf A_d(\lambda)\mathbf q_d(P).
```

The key conditional assumption is that over the chosen load range the **normalized optical generation kernel**

```math
\mathbf A_d(\lambda)
```

is effectively independent of load.

This is true in the simple linear Beer-Lambert model but must be experimentally checked against

```text
heating
state filling / nonlinear absorption
field redistribution / electroabsorption
or other strong-injection optical changes.
```

The paired same-source phase is

```math
D(\lambda,P)
=
\phi_A-\phi_B.
```

Arbitrary common source phase cancels at each wavelength/load state.

---

## 4. First load difference cancels the static A/B baseline

Between two load states `P_1` and `P_2`, define

```math
\Delta_P D
=D(P_2)-D(P_1).
```

If the optical kernels are unchanged,

```math
\boxed{
\Delta_P D
=
-\Omega
\left[
\mathbf A_A\Delta_P\mathbf q_A
-
\mathbf A_B\Delta_P\mathbf q_B
\right]
+
\Delta_P\phi_{\rm chain}.
}
```

The unknown static transport profiles

```text
q_A(P_1)
q_B(P_1)
```

do not appear separately.

This is already a major advantage over static spectral inversion.

However, an arbitrary smooth transport response linear in load can still mimic a localized A response.

---

## 5. Second finite difference removes static and linear load response

Choose three equally spaced values of a load coordinate

```math
P_-=P_0-\Delta P,
\qquad
P_0,
\qquad
P_+=P_0+\Delta P.
```

Define the load curvature

```math
\boxed{
C_P D
=
D(P_+)-2D(P_0)+D(P_-).
}
```

Taylor expansion gives

```math
C_P D
=
(\Delta P)^2
\frac{\partial^2D}{\partial P^2}
+O(\Delta P^4).
```

Hence both

```text
load-independent phase
and
phase linear in load
```

cancel exactly in the discrete observable.

For load-independent optical kernels:

```math
\boxed{
C_P D
=
-\Omega
\left[
\mathbf A_A C_P\mathbf q_A
-
\mathbf A_B C_P\mathbf q_B
\right]
+
C_P\phi_{\rm chain}.
}
```

This directly targets **nonlinear transport response / saturation curvature**.

---

## 6. Add wavelength differencing

A wavelength-independent nonlinear differential-chain curvature can be removed by taking the difference between two wavelengths:

```math
\boxed{
\mathcal C
=
C_P D(\lambda_1)
-
C_P D(\lambda_2).
}
```

The transport part becomes

```math
\boxed{
\mathcal C_{\rm tr}
=
-\Omega
\left[
(\mathbf A_{A1}-\mathbf A_{A2})
C_P\mathbf q_A
-
(\mathbf A_{B1}-\mathbf A_{B2})
C_P\mathbf q_B
\right].
}
```

This has the same useful short-wave differential-kernel geometry that previously produced strong leverage on sample A's retained nonlinear region.

It no longer requires the **static** A smooth baseline to be known to `~0.005 deg`.

It does not, by itself, prove that the nonlinear load response is localized; smooth nonlinear load-response modes remain possible nuisances.

---

## 7. Optimal white-noise allocation for the three load states

For one wavelength the curvature coefficients are

```text
+1, -2, +1.
```

Suppose one-unit phase noise is `sigma_0` and white variance after time `t_i` is

```math
\sigma_0^2/t_i.
```

For a fixed total time, minimizing

```math
\sum_i a_i^2\sigma_0^2/t_i
```

gives

```math
\boxed{t_i\propto|a_i|.}
```

Therefore the exact optimum load-state dwell ratio is

```math
\boxed{1:2:1.}
```

For two wavelengths and the wavelength difference, the six coefficients are

```text
+1, -2, +1,
-1, +2, -1.
```

The total absolute coefficient sum is `8`.

Thus the optimum six-state time fractions are

```text
lambda_1:
P_-  12.5%
P_0  25.0%
P_+  12.5%

lambda_2:
P_-  12.5%
P_0  25.0%
P_+  12.5%.
```

---

## 8. White-noise penalty of curvature

For total time `T`, the minimum variance of a linear combination with coefficients `a_i` is

```math
\boxed{
\operatorname{Var}_{\min}
=
\sigma_0^2
\frac{\left(\sum_i|a_i|\right)^2}{T}.
}
```

### Ordinary two-wavelength difference

```math
\sum|a_i|=2
```

so

```math
\sigma_{2\lambda}
=
\frac{2\sigma_0}{\sqrt T}.
```

### Load curvature + wavelength difference

```math
\sum|a_i|=8
```

so

```math
\boxed{
\sigma_{\rm curv}
=
\frac{8\sigma_0}{\sqrt T}.
}
```

Therefore the causal curvature observable costs exactly

```math
\boxed{4\times}
```

more white-noise phase standard deviation than an ordinary two-wavelength difference at the same total integration time.

This is the price paid for removing static, linear-load, and wavelength-independent nonlinear phase terms.

---

## 9. Illustrative phase-resource scale

To compare with previous repository calculations only, interpret the same

```text
25% support-shaped sample-A transport perturbation
```

as the magnitude of a second-difference transport curvature.

This is **not** a prediction of real illumination nonlinearity.

With no smooth nonlinear-curvature nuisance, the robust spectral pair is

```text
2.00 / 2.80 um
```

and the worst-profile phase-difference signal is approximately

```math
\boxed{0.1081^\circ.}
```

At the earlier reference resource

```text
sigma_0 = 0.10 deg
T = 81 one-wavelength time units,
```

the curvature-combination phase noise is

```math
\sigma_{\rm curv}
=\frac{8(0.10^\circ)}{9}
\approx0.0889^\circ.
```

Worst-profile significance is therefore only

```math
\boxed{\sim1.22\sigma.}
```

---

## 10. Resource needed for a robust illustrative `3 sigma` curvature signal

For the same assumed curvature amplitude, require

```math
0.1081^\circ
\ge
3\frac{8\sigma_0}{\sqrt T}.
```

At `sigma_0=0.10 degree`, this gives approximately

```math
\boxed{T\approx493\ \text{time units}.}
```

Relative to the 81-unit reference:

```math
\boxed{T/T_0\approx6.1.}
```

Equivalently, with `T=81` fixed, one-unit phase precision would need to improve to roughly

```math
\boxed{\sigma_0\approx0.0405^\circ.}
```

for the worst current A profile to reach `3 sigma` at the illustrative curvature amplitude.

This is substantially more white-noise time than an ordinary two-band measurement, but radically less than attempting to infer the leading A smooth baseline from mid/deep phase data in the current cross-band model.

---

## 11. What the curvature observable does and does not solve

### It does remove

- the static A transport baseline;
- the static B transport baseline;
- phase terms linear in the chosen load coordinate;
- wavelength-independent nonlinear differential-chain curvature after the wavelength difference;
- arbitrary common source phase through simultaneous A/B subtraction.

### It does not automatically remove

- nonlinear **wavelength-dependent** detector/readout phase;
- illumination-induced detector impedance changes;
- thermal phase shifts;
- nonlinear absorption / band filling;
- smooth nonlinear transport curvature in A or B;
- source pointing or spectral changes with optical power;
- device mismatch unrelated to the nonlinear-gradient region.

Therefore the curvature is a causal observable, not yet a localized-mechanism proof.

---

## 12. The most serious known systematic — illumination-dependent impedance

Published strong-injection HgCdTe work reports that illumination can reduce zero-bias impedance and that detector heating affects saturation behavior.

A change in detector impedance changes the electrical RF transfer function and can therefore generate phase curvature even if carrier transit time were unchanged.

This systematic must be de-embedded or measured independently.

The next metrology calculation should quantify how accurately the load-dependent detector/readout electrical pole must be known so its phase curvature remains below the transport target.

---

## 13. Current prior-art boundary

Do not claim novelty for

```text
HgCdTe saturation versus illumination
space-charge accumulation under strong injection
composition-gradient improvement of saturation
wavelength/temperature dependence under strong illumination
applied-field/composition-gradient coupling.
```

Those are already in the literature.

The remaining candidate measurement concept is narrower:

> **wavelength-resolved RF phase curvature versus optical load, used with a known graded optical kernel to infer the nonlinear internal transport response rather than only static responsivity or saturation amplitude.**

Priority remains unproven and requires a focused timing/frequency-domain literature audit.

---

## 14. Next decisive work

Before adding a nonlinear transport model, quantify the electrical de-embedding requirement created by illumination-dependent device impedance.

Then determine whether a realistic load range exists in which

```text
transport curvature is measurable
while
thermal / electro-optical kernel change remains independently bounded.
```

Numerical implementation for the white-noise resource result:

`numerics/hgcdte_shortwave_load_curvature.py`
