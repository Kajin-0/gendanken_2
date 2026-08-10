# Sample-A Interference Stress — Does the Provisional Joint A/B Temperature Schedule Survive Coherent Optical Modulation?

**Date:** 2026-08-09  
**Status:** conditional optical stress test using a coherent single-back-reflection model; not a calibrated transfer-matrix calculation; no novelty claim

## 1. Why this is the next collision

The sample-A profile-family calculation found a remarkably stable common-wavelength temperature schedule near

```text
300 K -> 3.632 um
215 K -> ~3.7935 um
115 K -> ~4.0045 um.
```

But the primary 2023 sample-A experiment explicitly reports interference structure near cutoff and attributes it to the thicker absorber/internal reflections.

That means pure Beer-Lambert generation is not a sufficient final model for sample A.

A directly relevant prior optical-model paper is

D. L. Lee, `Modeling of Optical Response in Graded Absorber Layer Detectors`, *Journal of Electronic Materials* **35** (2006) 1423, DOI `10.1007/s11664-006-0278-7`.

Its motivation is precisely that near cutoff the absorption coefficient falls, internal reflections become important, interference modulates detector spectral shape, and grading complicates the calculation.

Room-temperature infrared ellipsometry also shows strong HgCdTe refractive-index dispersion near the gap for compositions close to the present devices:

`The refractive index dispersion of Hg1-xCdxTe by infrared spectroscopic ellipsometry`, *Infrared Physics & Technology* **42** (2001) 77-80, DOI `10.1016/S1350-4495(01)00059-7`.

The exact Sellmeier coefficients, temperature-dependent complex index through the relevant graded sample, layer-stack details, and the real sample-A composition fit are not yet recovered well enough to justify a supposedly calibrated transfer matrix.

Therefore the useful immediate test is harsher and simpler:

> **Can a deliberately broad coherent standing-wave perturbation destroy the provisional common-wavelength schedule?**

---

## 2. Single-return coherent model

Let

```math
\tau(z)=\int_0^z\alpha(u)du,
\qquad
\tau_L=\tau(L).
```

The forward optical field has amplitude proportional to

```math
e^{-\tau(z)/2}.
```

Add one coherent wave returned from the back side with effective power ratio `R`.

The returned amplitude at depth `z` is proportional to

```math
\sqrt R\,
\exp\!\left[-\frac{2\tau_L-\tau(z)}{2}\right].
```

For effective refractive index `n_eff` and unknown reflection phase `theta`, the resulting two-wave intensity is

```math
\boxed{
I(z)
=e^{-\tau(z)}
+R e^{-[2\tau_L-\tau(z)]}
+2\sqrt R\,e^{-\tau_L}
\cos\!\left[
\frac{4\pi n_{\rm eff}(L-z)}{\lambda}
+\theta
\right].
}
```

This is simply

```math
|E_{\rm forward}+E_{\rm return}|^2,
```

so it is a physically interpretable coherent one-return perturbation rather than an arbitrary sinusoid multiplied onto the generation profile.

Use

```math
g(z)=\alpha(z)I(z)
```

and normalize `g(z)` to calculate the conditional generation distribution and front-collection survival kernel.

This is still **not** a full Fabry-Perot / transfer-matrix calculation because it omits repeated returns, real interface Fresnel coefficients, graded complex index, front-surface transmission, polarization and angle effects.

---

## 3. Deliberately broad interference stress coordinates

Do not pretend the missing optical constants are known.

Scan

```text
effective returned power R:
0.1, 0.5, 0.9

effective refractive index n_eff:
2.8, 3.5, 4.2

reflection phase theta:
0, pi/2, pi, 3pi/2.
```

`R=0.9` is intentionally extreme and should **not** be interpreted as a measured sample-A interface reflectivity.

Likewise `n_eff=2.8-4.2` is a broad stress coordinate, not an uncertainty interval.

Run every combination over **all 72** sample-A composition-profile sensitivity members from the preceding study.

Sample B remains on the current Beer-Lambert central envelope because the primary experiment reports incomplete/no comparable interference cycle there.

The reference is the provisional common band

```math
\lambda_0=3.632\ {\rm um}
```

at `300 K`.

At `215 K` and `115 K`, re-optimize the equal-weight joint full-kernel objective.

---

## 4. Primary result — fixed unknown optical index across temperature

In this first stress test, `n_eff` is unknown but held the same for the 300 K reference and lower-temperature comparison within each realization.

Across

```text
72 sample-A profiles
x 3 reflection powers
x 3 effective indices
x 4 phases
```

there are `2592` optical realizations per temperature pair when both lower temperatures are counted.

### 215 K

The optimized common wavelength remains inside

```math
\boxed{
3.792827\text{-}3.794207\ {\rm um}.
}
```

The full-kernel mismatch ranges remain approximately

```text
A: 0.278-0.877%
B: 0.439-0.481%.
```

### 115 K

The optimized common wavelength remains inside

```math
\boxed{
4.002469\text{-}4.007903\ {\rm um}.
}
```

The full-kernel mismatch ranges are approximately

```text
A: 0.591-1.957%
B: 0.843-1.003%.
```

Thus even a coherent returned-wave stress extending to the deliberately extreme `R=0.9` case does **not** destroy the common mid/deep temperature schedule.

The schedule broadens by only a few nanometres relative to the Beer-Lambert sensitivity result.

---

## 5. What actually becomes dangerous — temperature-dependent optical phase

The previous test keeps one unknown `n_eff` fixed across temperatures.

The real refractive index is temperature dependent, and the relevant uncertainty is therefore not merely interference amplitude but the **change of optical phase with temperature**.

To expose this sensitivity without inventing a thermo-optic model, perform an intentionally over-broad diagnostic:

```text
R = 0.9
six representative sample-A profiles
n_eff(300 K) independently chosen from {2.8, 4.2}
n_eff(T) independently chosen from {2.8, 4.2}
four reflection phases.
```

This allows an enormous, generally unphysical index jump across the full stress interval. It is not a prediction of HgCdTe thermo-optic behavior.

### 215 K extreme index-jump diagnostic

```text
common lambda = 3.790366-3.795869 um
A mismatch = 0.500-3.907%
B mismatch = 0.439-0.604%.
```

### 115 K extreme index-jump diagnostic

```text
common lambda = 3.999788-4.010301 um
A mismatch = 1.074-4.275%
B mismatch = 0.843-1.159%.
```

The common wavelength still remains close to `~4.00 um`, but the A-kernel mismatch can rise to several percent if the standing-wave phase is allowed to change by an unrealistically large amount.

This identifies the next optical quantity that matters:

> **temperature-dependent optical phase / complex refractive index, not reflection amplitude by itself.**

---

## 6. What this changes

The sample-A interference observation no longer looks like an immediate feasibility killer for the `3.632 um` reference.

The current hierarchy is now:

```text
unknown A composition fit
-> surprisingly weak effect on mid/deep joint wavelength

large coherent reflected-wave amplitude / unknown phase
-> still only few-nanometre schedule shift; <~2% A mismatch in the fixed-n stress

temperature-dependent optical phase
-> can become a several-percent A-kernel error if allowed to vary extremely.
```

Therefore the next optical task should be narrower than a generic transfer-matrix exercise:

> **obtain a defensible composition/wavelength/temperature-dependent complex refractive-index model for HgCdTe and propagate the physically allowed thermo-optic phase change through the sample-A cavity.**

That will determine whether the several-percent extreme-index diagnostic collapses back toward the `~1-2%` fixed-index stress envelope.

---

## 7. Important limitation — conditional generation shape, not absolute optical throughput

The one-return model is used here to stress the **normalized generation kernel**.

It is not an energy-conserving full device optical model because it does not include the complete interface scattering problem or repeated reflections.

Therefore do **not** interpret its integrated `g(z)` as a calibrated absorbed fraction or responsivity.

The earlier Beer-Lambert `Pabs` values remain only provisional signal-scale indicators until the full optical stack is modeled or measured.

---

## 8. Claim boundary

### DERIVED within the stated one-return model

```math
I(z)
=e^{-\tau(z)}
+R e^{-[2\tau_L-\tau(z)]}
+2\sqrt R e^{-\tau_L}
\cos\left[4\pi n_{\rm eff}(L-z)/\lambda+\theta\right].
```

### CHECKED NUMERICALLY / CONDITIONAL STRESS RESULT

For the 72-member sample-A profile family, `R=0.1-0.9`, `n_eff=2.8-4.2`, four reflection phases, and the current Hansen/Moazzami absorption model:

```text
3.632 um @300 K
-> 215 K joint lambda remains ~3.79283-3.79421 um
-> 115 K joint lambda remains ~4.00247-4.00790 um
```

with maximum A mismatch below approximately `0.9%` at 215 K and `2.0%` at 115 K in the fixed-index stress.

### CONDITIONAL WARNING

An intentionally extreme independent `n_eff=2.8 <-> 4.2` temperature jump can increase A-kernel mismatch to approximately `4.3%` and broaden the 115 K common-wavelength range to approximately `3.9998-4.0103 um`.

This is a sensitivity diagnostic, not a physical prediction.

### NOT ESTABLISHED

- real sample-A reflection coefficients;
- real sample-A interference phase;
- complex `n(x,lambda,T)` over the relevant graded layer;
- Fresnel stack / multiple-reflection transfer matrix;
- interference-corrected absolute absorbed fraction;
- exact real-device joint temperature wavelengths;
- novelty / priority.

---

## 9. Next decisive work

The next optical calculation should recover a physically defensible

```math
\tilde n(x,\lambda,T)=n+i\kappa
```

for the `~3.6-4.1 um`, `115-300 K`, `x~0.3-0.5` region and use it in a graded-layer transfer matrix.

The present interference stress test says that **generic reflection strength alone is unlikely to overturn the mid/deep schedule**. The question has narrowed to whether the physically allowed temperature-dependent optical phase is large enough to matter at the sub-percent/few-percent kernel level.

In parallel, the differential RF phase covariance remains an independent experimental blocker.

---

## 10. Reproducibility

Deterministic regression:

`numerics/hgcdte_sample_a_interference_stress.py`
