# Revision 5 adversarial corrections

**Date:** 2026-08-11  
**Status:** surgical response to the post-Rev4 hostile review; no new broad theory branch.

## Disposition of the review

The Rev4 review no longer identified a fatal defect in the central four-color or rank-two constructions. Rev5 therefore targets the remaining narrow vulnerabilities rather than restructuring the paper.

## 1. Low-RF weighting-mode resolution is now an explicit result

For the one-dimensional linear-weighting-field branch, the observation multiplier is

```math
q_{\rm weight}=1,
```

while the transport multiplier is

```math
q_{\rm tr}=e^{-\gamma h}\to1\qquad(\omega\to0,\ \kappa\to0).
```

The rank-two witness therefore loses resolving power quadratically as the roots coalesce. Using the existing paper scale

```text
D = 0.02327 m^2/s
w = 3.45e4 m/s
h = 0.5 um
```

gives the best-case equal-mode 3-sigma amplitude-SNR requirements:

```text
100 MHz -> 116.2 dB
500 MHz ->  88.4 dB
1 GHz   ->  76.7 dB
```

The corresponding five-color annihilation penalties are

```text
100 MHz -> 46.3 dB
500 MHz -> 32.3 dB
1 GHz   -> 26.4 dB.
```

This exposes a genuine measurement-theory tradeoff: explicit rank-two identification suffers root coalescence at low RF, while exact polynomial annihilation suffers the `1/|rh|` noise penalty.

## 2. Rank-two physical-law testing now has a branch-free front end

Before taking logarithms, a homogeneous finite scalar boundary model requires

```math
q_+q_-
=e^{(r_++r_-)h}
=e^{-wh/D}
\in\mathbb R_{>0},
```

and the product must be RF-independent.

Only after this branch-free check does the manuscript unwrap each root. Rev5 now states that both logarithmic branch integers and root pairing/permutation across RF must be fixed by independent bounds, multiple spacings, and continuity—not selected to minimize the physical-law residual.

## 3. The HgCdTe field law is no longer mislabeled as saturation

The inherited numerical stress uses

```math
v_{\rm field}=\frac{\mu E}{1+(E/E_{\rm sat})^{r_s}},
\qquad r_s=2.2.
```

This does not asymptotically saturate for `r_s>1`; it rolls off. Rev5 calls it an **empirical field-rolloff sensitivity law**, explicitly says it is retained only to reproduce the numerical stress, and notes that the sampled grading fields satisfy `E/E_sat ~ 0.05`. The correction to the low-field linear velocity is only about 0.15--0.18%, so no reported closure value is changed.

## 4. Same-optics homogeneous baseline uncertainty enters the covariance budget

The flagship quantity is a modeled subtraction,

```math
C_{\rm exc}=C_{\rm meas}-C_{\rm hom}.
```

Rev5 adds

```math
\Sigma_{\rm exc}
=\Sigma_{\rm meas}+\Sigma_{\rm hom}
-\Sigma_{\rm cross}-\Sigma_{\rm cross}^{T}.
```

The nominal same-optics homogeneous phase is 20.5--22.4% of the quoted gradient-sensitive excess. It is now included explicitly in the nuisance table rather than treated as an exact correction.

## 5. Minor mathematical cleanup

Rev5 also:

- states the confluent `s=kappa=0`, `q->1` limit of the one-carrier current and shows the four-color closure remains exact for the limiting affine sequence;
- defines the complex closure statistic as one continuously tracked logarithm of the multiplicative closure ratio;
- renames local slowness from `q(z)` to `u(z)=1/v(z)` so `q` remains reserved for spatial multipliers;
- explicitly describes the few-nanometer source-coordinate and `~1e-4 degree` irregular-phase scales as **derived design requirements**, not demonstrated calibration performance.

## 6. Priority audit status

The closest-looking 2024 source remains:

> G. Xu et al., “Potential application of HgCdTe detector with composition gradient in laser measurement,” *Journal of Applied Optics* 45(3), 549--556 (2024), DOI 10.5768/JAO202445.0310009.

Bibliographic metadata is verified, but a lawful public full text was not recovered in this pass. The public ResearchGate record explicitly reports no full text and offers an author-request route. Therefore the full-text audit remains **OPEN** and blocks any priority/novelty claim at submission.

Two closely related accessible sources were audited for boundary-setting:

1. G. Xu et al., “Photoelectric characteristics of compositionally graded HgCdTe detector,” *Journal of Infrared and Millimeter Waves* 42(3), 285--291 (2023), DOI 10.11972/j.issn.1001-9014.2023.03.001. It studies composition-gradient built-in fields, temperature-dependent response spectra/responsivity, carrier motion, and saturation-threshold motivation.
2. J. Chen et al., “Performance Optimization of Hg1-xCdxTe Photovoltaic Detectors Under Strong Illumination Considering Temperature and Wavelength Dependencies,” *IEEE Photonics Journal* 16(5) (2024), DOI 10.1109/JPHOT.2024.3470871. It studies graded composition, strong-illumination saturation, wavelength/temperature dependence, and array electrodes.

Neither accessible source establishes the exact chain

```text
spectral internal coordinate
-> Shockley-Ramo-corrected spatial differencing
-> minimal-color model-order closure
-> cross-RF physical root-law falsification
```

in the text examined. This is **not evidence of novelty**. The exact 2024 Journal of Applied Optics paper must still be obtained and read in full before submission.

## Numerical regression

`numerics/rev5_review_regression.py` independently verifies the new mode-coalescence SNRs, five-color penalties, branch-free finite-boundary multiplier product, field-rolloff scale, and same-optics baseline fractions/budget.
