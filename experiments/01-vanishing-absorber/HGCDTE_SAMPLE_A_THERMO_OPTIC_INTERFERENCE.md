# Sample-A Thermo-Optic Interference — Empirical HgCdTe Index Preserves the Mid/Deep Joint Schedule

**Date:** 2026-08-09  
**Status:** conditional composition-resolved thermo-optic interference stress; empirical real-index model plus one coherent returned wave; not a calibrated full transfer matrix; no novelty claim

## 1. Why this calculation matters

The previous sample-A interference stress found that a large coherent returned wave does not by itself destroy the provisional common-wavelength temperature schedule

```text
300 K -> 3.632 um
215 K -> ~3.7935 um
115 K -> ~4.0045 um.
```

The only way the deliberately broad stress produced several-percent sample-A kernel error was by allowing the effective refractive index to jump independently across an absurdly broad `2.8 <-> 4.2` interval between temperatures.

That was a sensitivity diagnostic, not HgCdTe physics.

The next question is therefore specific:

> **When a published composition- and temperature-dependent HgCdTe refractive-index relation is used in the standing-wave phase, does the common A/B schedule remain stable?**

---

## 2. Empirical HgCdTe refractive index

Liu, Chu and Tang measured intrinsic absorption for HgCdTe compositions

```text
x = 0.276-0.443
```

over

```text
T = 4.2-300 K
```

and obtained the refractive-index dispersion near and below the band gap from the Kramers-Kronig relation:

K. Liu, J. H. Chu, D. Y. Tang, `Composition and temperature dependence of the refractive index in Hg1-xCdxTe`, *Journal of Applied Physics* **75** (1994) 4176, DOI `10.1063/1.356001`.

The empirical form is

```math
\boxed{
n^2(\lambda,x,T)
=A+
\frac{B}{1-(C/\lambda)^2}
+D\lambda^2,
}
```

where `lambda` is in microns.

The explicit coefficient parameterization, reproduced in later HgCdTe optical modeling, is

```math
\boxed{
A
=13.173-9.852x+2.909x^2
+10^{-3}(300-T),
}
```

```math
\boxed{
B
=0.83-0.246x-0.0961x^2
+8\times10^{-4}(300-T),
}
```

```math
\boxed{
C
=6.706-14.437x+8.531x^2
+7\times10^{-4}(300-T),
}
```

```math
\boxed{
D
=1.953\times10^{-4}
-0.00128x
+1.853\times10^{-4}x^2.
}
```

The imaginary part of the index remains tied to absorption through

```math
\kappa=\frac{\lambda\alpha}{4\pi}.
```

The current one-return model already carries attenuation through the local optical depth `tau(z)`, so this calculation uses the empirical real `n(x,lambda,T)` only for coherent optical phase.

---

## 3. The candidate schedule follows an almost fixed composition coordinate

Before propagating interference, solve

```math
E_g(x_*,T)=\frac{hc}{\lambda}
```

for the three nominal candidate points.

The results are

| temperature | wavelength | local band-edge composition `x_*` |
|---:|---:|---:|
| 300 K | 3.6320 um | 0.337580 |
| 215 K | 3.7935 um | 0.337746 |
| 115 K | 4.0045 um | 0.337837 |

Thus

```math
\boxed{
\Delta x_*<2.6\times10^{-4}
}
```

across the entire `300 -> 115 K` schedule.

This is a major physical interpretation of the earlier numerical robustness:

> **the retuned wavelength is approximately following one fixed internal composition / local-gap coordinate.**

At those same local-gap points, the empirical real index is approximately

```text
300 K: n ~3.464
215 K: n ~3.482
115 K: n ~3.502.
```

The thermo-optic change is therefore of order only a few `10^-2`, not order unity.

---

## 4. Why the measured composition range is sufficient for this mid/deep interference test

Some members of the deliberately broad sample-A sensitivity family have processed front composition far above `x=0.443`.

That does **not** invalidate the returned-wave phase calculation for these wavelengths.

For a carrier-generating point at depth `z`, local above-gap absorption requires

```math
x(z)\le x_*\approx0.338.
```

The sample-A profiles decrease in composition toward the back / low-Cd side.

Therefore every point on the returned-wave optical path from that generating position to the back side has

```math
x\le0.338,
```

well inside Liu et al.'s measured `0.276-0.443` interval.

The high-Cd processed front lies **upstream** of the generating point and is not traversed by the returned-wave round trip between that point and the back surface.

For numerical continuity the implementation clips `x>0.443` when constructing a cumulative index integral, but the physically used phase interval for nonzero generation never depends on that clipped segment.

---

## 5. Composition-resolved one-return phase

Replace the previous constant-index phase

```math
4\pi n_{\rm eff}(L-z)/\lambda
```

by the graded optical-path integral

```math
\boxed{
\Phi_{\rm rt}(z;T,\lambda)
=\frac{4\pi}{\lambda}
\int_z^L n[x(u),T,\lambda]du
+\theta.
}
```

The one-return intensity remains

```math
\boxed{
I(z)
=e^{-\tau(z)}
+R e^{-[2\tau_L-\tau(z)]}
+2\sqrt R e^{-\tau_L}
\cos\Phi_{\rm rt}(z).
}
```

Use

```math
g(z)=\alpha(z)I(z)
```

and normalize to obtain the conditional generation distribution and front-collection survival timing kernel.

This is still only a **one-return coherent stress model**, not a repeated-reflection transfer matrix.

---

## 6. Stress scan

Run the empirical thermo-optic phase model over

```text
all 72 sample-A composition sensitivity profiles
R = 0.1, 0.5, 0.9
reflection phase = 0, pi/2, pi, 3pi/2
T = 215, 115 K.
```

`R` remains a stress coordinate rather than a measured reflection coefficient.

Sample B retains the current central Beer-Lambert model.

At every realization, re-optimize the equal-weight joint A/B full-kernel objective relative to the common

```text
300 K, 3.632 um
```

reference.

---

## 7. Result

### 215 K

Across all profile/reflection/phase realizations:

```math
\boxed{
\lambda_*=3.792986\text{-}3.794120\ {\rm um}.
}
```

Kernel mismatch ranges:

```text
sample A: 0.264-0.735%
sample B: 0.440-0.476%.
```

### 115 K

```math
\boxed{
\lambda_*=4.002940\text{-}4.007453\ {\rm um}.
}
```

Kernel mismatch ranges:

```text
sample A: 0.565-1.733%
sample B: 0.843-0.979%.
```

Thus the empirical composition- and temperature-dependent index leaves the mid/deep schedule essentially where the earlier broad fixed-index interference stress placed it.

---

## 8. Comparison of successive optical models

The candidate `3.632 um` reference has now survived three increasingly restrictive calculations.

### Beer-Lambert A-profile family

```text
215 K: 3.793356-3.793566 um
115 K: 4.004157-4.004870 um
```

with A mismatch below approximately `0.23%` and `0.45%`.

### Broad constant-index coherent-return stress

```text
215 K: 3.792827-3.794207 um
115 K: 4.002469-4.007903 um
```

with A mismatch below approximately `0.88%` and `1.96%`.

### Empirical composition/temperature-index coherent-return stress

```text
215 K: 3.792986-3.794120 um
115 K: 4.002940-4.007453 um
```

with A mismatch below approximately `0.74%` and `1.73%`.

The physically anchored thermo-optic model therefore **tightens**, rather than worsens, the intentionally broad interference envelope.

---

## 9. What this changes

The leading optical uncertainty is no longer simply

```text
sample-A interference might invalidate the common schedule.
```

That concern has survived a substantial stress test.

The more precise remaining optical questions are

```text
actual interface reflection coefficients
repeated coherent reflections / full Fabry-Perot response
real sample-A x(z)
uncertainty / validity of n(x,lambda,T) very near the local gap
sample-B interference if finer data reveal it
absolute optical throughput / signal covariance.
```

But the mid/deep temperature-control **wavelength itself** now looks structurally robust.

A practical pre-calibrated experimental bracket is approximately

```text
215 K: 3.793 +/- 0.001 um
115 K: 4.005 +/- 0.003 um
```

where these are model-stress envelopes, **not experimental confidence intervals**.

---

## 10. Important distinction from a full transfer matrix

The present model does not yet include

- front- and back-interface Fresnel coefficients derived from the actual stack;
- repeated reflections;
- complex graded index in one self-consistent propagation calculation;
- sapphire/CdZnTe/passivation/epoxy stack details;
- polarization or incidence-angle dependence;
- experimentally measured fringe contrast.

Therefore it cannot predict the measured spectral fringe amplitude or absolute responsivity.

Its purpose is narrower:

> **stress the normalized generation-position kernel that enters the timing inverse.**

For that purpose, the common-wavelength schedule has now survived both very broad interference strength and a published thermo-optic phase relation.

---

## 11. Claim boundary

### KNOWN / PUBLISHED INPUT

Liu et al. provide a composition- and temperature-dependent HgCdTe refractive-index dispersion model over `x=0.276-0.443`, `T=4.2-300 K` near/below the band gap. Later published HgCdTe device modeling reproduces the explicit coefficient parameterization used here.

### DERIVED

The nominal candidate wavelengths correspond to nearly one fixed local band-edge composition:

```text
x_* = 0.337580, 0.337746, 0.337837
```

at `300, 215, 115 K`, respectively.

### CHECKED NUMERICALLY / CONDITIONAL

For the empirical thermo-optic real index, current Hansen/Moazzami absorption, 72-member A-profile family, `R=0.1-0.9`, and four reflection phases:

```text
215 K joint lambda = 3.792986-3.794120 um
A mismatch <= ~0.74%
B mismatch <= ~0.48%

115 K joint lambda = 4.002940-4.007453 um
A mismatch <= ~1.73%
B mismatch <= ~0.98%.
```

### NOT ESTABLISHED

- exact real-device A/B joint wavelengths;
- exact sample-A profile;
- full optical stack transfer matrix;
- measured sample-A reflectivity/fringe phase;
- absolute absorbed fraction under interference;
- actual phase covariance at the retuned wavelengths;
- transport contrast;
- novelty / priority.

---

## 12. Next decisive work

Do **not** keep elaborating arbitrary optical stress coordinates.

The next useful optical step is now either

1. a full graded transfer matrix using actual/reasonably constrained interface optical constants and repeated reflections, **or**
2. direct use of measured sample-A spectral fringes to calibrate effective cavity phase/reflectivity.

But neither should displace the independent experimental blocker:

> **measure the two-arm differential RF phase covariance and drift around the candidate `3.63-4.01 um` wavelength set.**

At this point the phase-metrology calibration is at least as important as further refinement of the optical wavelength schedule.

---

## 13. Reproducibility

Deterministic regression:

`numerics/hgcdte_sample_a_thermo_optic_interference.py`
