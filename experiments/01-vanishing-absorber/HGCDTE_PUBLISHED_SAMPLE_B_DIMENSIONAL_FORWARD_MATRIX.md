# Published 2023 Sample B — Dimensional Spectral-Timing Forward Matrix

**Date:** 2026-08-09  
**Status:** literature-constrained dimensional optical/timing-kernel calculation; not a calibrated reconstruction of the published device transport; no novelty claim

## 1. Purpose

The spectral timing inverse has so far been tested mostly with normalized or synthetic graded profiles.

The 2023 graded-HgCdTe study by Xu et al. contains a particularly useful real structure:

```text
sample B
processed thickness about 3.7 um
nominal x about 0.316 from FTIR
nonlinear interdiffusion region removed
junction prepared at the high-Cd end
linear-gradient field reported in the 100-200 V/cm range.
```

Primary source:

G.-Q. Xu et al., `Photoelectric characteristics of compositionally graded HgCdTe detector`, *Journal of Infrared and Millimeter Waves* 42 (2023) 285-291, DOI `10.11972/j.issn.1001-9014.2023.03.001`.

This note asks:

> Using only those published dimensional constraints plus established HgCdTe band-gap and absorption models, what spectral position encoding and inverse conditioning should sample B provide at 300 K?

The result is a **literature-constrained envelope**, not a reanalysis of raw sample-B data.

---

## 2. Critical geometry correction

The 2023 device is not oriented like the earlier generic downstream-collection model.

The paper states that the PN junction is fabricated at the **high-Cd end** of the retained graded material. Long-wave photoelectrons generated in the lower-Cd material deeper toward the sapphire-supported side must return toward the junction; the authors explicitly discuss deep long-wave photoelectrons diffusing to the junction and, in sample A, being opposed by the composition-gradient field.

Define

```text
z = 0 : high-Cd / junction-side entrance
z = W : low-Cd side
```

with

```math
W=3.7\ {\rm um}.
```

If the local mean delay density is

```math
q(s)=1/v_{\rm eff}(s),
```

then for a carrier generated at depth `z`,

```math
\boxed{
T(z)=\int_0^z q(s)ds.
}
```

Therefore the wavelength-dependent mean delay is

```math
\bar T_i
=\int_0^W p_i(z)
\left[
\int_0^z q(s)ds
\right]dz.
```

Swap integrals:

```math
\boxed{
\bar T_i
=\int_0^W
S_i(s)q(s)ds,
}
```

where

```math
\boxed{
S_i(s)
=P(Z_g\ge s|\lambda_i,{\rm abs})
=1-F_i(s).
}
```

Thus the correct timing kernel for this **front-collection** geometry is the conditional generation **survival function**, not the CDF used for collection at `z=W`.

The inverse remains linear.

---

## 3. Published sample-B inputs

The 2023 paper reports

```text
processed sample-B thickness: ~3.7 um
nominal FTIR composition: x ~ 0.316
nonlinear interdiffusion region: removed
linear composition-gradient built-in field: within ~100-200 V/cm across the measured temperature set.
```

The exact 300 K sample-B `x(z)` curve is shown graphically in the paper but is not machine-readable in the accessible text.

Therefore the present calculation uses

```math
x_{\rm low}=0.316
```

as a **nominal low-Cd endpoint** and brackets the retained linear gradient by

```math
F_g=100,150,200\ {\rm V/cm}.
```

This endpoint interpretation is conditional and must eventually be replaced by the authors' actual fitted `x(z)` parameters or digitized/raw profile.

---

## 4. Correct HgCdTe gap law

Use the Hansen-Schmit-Casselman expression

```math
\boxed{
E_g(x,T)
=-0.302
+1.93x
+5.35\times10^{-4}T(1-2x)
-0.81x^2
+0.832x^3
}
```

in eV.

At

```math
x_{\rm low}=0.316,
\qquad
T=300\ {\rm K},
```

this gives

```math
\boxed{E_{g,\rm low}=0.312314\ {\rm eV}}
```

and

```math
\boxed{\lambda_{g,\rm low}=3.9699\ {\rm um}.}
```

The `+0.832x^3` coefficient is intentional. The machine-readable 2022 graded-detector article appears to print `0.132x^3`; that is not the standard Hansen coefficient and is not used here.

---

## 5. Infer the high-Cd endpoint from the measured field bracket

The gradient field is defined by

```math
F_g
=\frac1q\left|\frac{dE_g}{dz}\right|.
```

Across the retained thickness,

```math
\Delta E_g\simeq F_g W
```

when `E_g` is expressed in eV and `F_g W` in volts.

For

```math
W=3.7\ {\rm um},
```

the 100-200 V/cm bracket implies

```text
100 V/cm -> Delta Eg = 0.0370 eV
150 V/cm -> Delta Eg = 0.0555 eV
200 V/cm -> Delta Eg = 0.0740 eV.
```

Inverting the Hansen relation gives

| gradient field | inferred high-Cd `x` | `Eg,high` | high-end gap wavelength |
|---:|---:|---:|---:|
| 100 V/cm | 0.34348 | 0.34931 eV | 3.5494 um |
| 150 V/cm | 0.35721 | 0.36781 eV | 3.3708 um |
| 200 V/cm | 0.37091 | 0.38631 eV | 3.2094 um |

Thus the local-gap spectral coordinate for this literature-constrained sample-B envelope is approximately

```math
\boxed{
3.2\text{-}3.55\ {\rm um}
\;\to\;
3.97\ {\rm um},
}
```

with the exact short-wave endpoint set by the actual sample-B gradient.

---

## 6. Linear composition profile is nearly a constant-gap-slope profile

For each field bracket, construct

```math
x(z)
=x_{\rm high}
+\left(x_{\rm low}-x_{\rm high}\right)\frac{z}{W}.
```

Because the Hansen `E_g(x)` curve is nearly linear over this narrow composition interval, the resulting field is almost constant.

The deterministic regression gives approximately

```text
target 100 V/cm -> 99.98 to 100.05 V/cm
target 150 V/cm -> 149.92 to 150.22 V/cm
target 200 V/cm -> 199.77 to 200.57 V/cm.
```

Therefore the distinction between a linear-`x` and linear-`E_g` profile is negligible at the level of the present optical calculation.

---

## 7. Published above-gap absorption law

Use the empirical above-bandgap model of Moazzami et al., *Journal of Electronic Materials* 34 (2005) 773-778, DOI `10.1007/s11664-005-0019-3`:

```math
\boxed{
\alpha(E,x,T)
=K(x,T)
\left(
\frac{E-E_g(x,T)}{E}
\right)^{n(x,T)},
\qquad E>E_g.
}
```

with

```math
\boxed{
K(x,T)
=-20060
+115750x
+32.43T
-64170x^2
+0.43231T^2
-101.92xT
}
```

and

```math
\boxed{
n(x,T)
=0.74487
-0.44513x
+\left(0.000799-0.000757x\right)T.
}
```

`alpha` is in `cm^-1`.

The Moazzami model was fitted over approximately

```text
x = 0.22-0.60
T = 40-300 K,
```

so the nominal sample-B composition and 300 K calculation fall inside its stated data range.

The current implementation sets

```math
\alpha=0
```

below the local gap.

Therefore Urbach-tail absorption, reflection, interference, and free-carrier optical effects are not included.

---

## 8. Generation kernel

For front illumination at wavelength `lambda`, define

```math
E_\gamma=hc/\lambda.
```

The unnormalized absorbed-generation density is

```math
\boxed{
g(z|\lambda)
=\alpha(z,\lambda)
\exp\!\left[-\int_0^z\alpha(u,\lambda)du\right].
}
```

Total single-pass absorbed fraction is

```math
\boxed{
P_{\rm abs}(\lambda)
=1-\exp[-\tau(\lambda)],
}
```

with

```math
\tau(\lambda)=\int_0^W\alpha(z,\lambda)dz.
```

Conditioned on absorption,

```math
\boxed{
p(z|\lambda,{\rm abs})
=\frac{g(z|\lambda)}{P_{\rm abs}(\lambda)}.
}
```

The timing row for front collection is the corresponding survival function.

---

## 9. Central 150 V/cm generation-depth calculation

For the central bracket profile, the calculation gives:

| wavelength | single-pass `Pabs` | conditional mean depth | conditional RMS width |
|---:|---:|---:|---:|
| 2.80 um | 0.998 | 0.677 um | 0.621 um |
| 3.20 um | 0.975 | 1.155 um | 0.860 um |
| 3.37 um | 0.917 | 1.704 um | 0.896 um |
| 3.50 um | 0.786 | 2.369 um | 0.703 um |
| 3.70 um | 0.417 | 3.087 um | 0.383 um |
| 3.85 um | 0.115 | 3.459 um | 0.161 um |
| 3.88 um | 0.070 | 3.522 um | 0.120 um |

Several points are important.

### Short wavelengths do not probe exactly `z=0`

Even when the whole layer is above gap, finite absorption length places the conditional mean generation depth hundreds of nanometers inside the material.

### Near cutoff the spatial kernel becomes narrow

The mean moves toward the low-Cd rear side and the conditional RMS generation width becomes small.

### The cost is optical signal

At `3.88 um`, the simple single-pass model gives only about `7%` absorbed fraction.

The inverse therefore has a real depth-localization versus optical-SNR tradeoff.

---

## 10. Measurable differential phase scale

For a constant illustrative effective velocity

```math
v_{\rm eff}=10^5\ {\rm m/s},
```

the mean-depth shift between

```text
2.80 um -> 3.88 um
```

is

```math
\boxed{\Delta\langle z\rangle\approx2.845\ {\rm um}.}
```

The corresponding mean transit-delay difference is

```math
\boxed{\Delta T\approx28.45\ {\rm ps}.}
```

At

```math
f=1\ {\rm GHz},
```

```math
\Delta\phi
\simeq
-2\pi f\Delta T,
```

so

```math
\boxed{|\Delta\phi|\approx10.24^\circ.}
```

This is **not** a velocity prediction for sample B.

It is a transparent measurement scale showing that the wavelength-induced depth shift is large enough to generate multi-degree RF-phase changes for a `10^5 m/s` transport scale.

Because phase scales as `1/v`, a slower effective collection process gives a larger phase contrast at fixed frequency, subject to the low-frequency cumulant condition.

---

## 11. Real-matrix conditioning

Use an 80-cell spatial discretization, wavelength samples from `2.80` to `3.95 um` in `0.01 um` steps, and retain only wavelengths with

```math
P_{\rm abs}\ge0.05.
```

The relative singular-mode counts are:

| field bracket | wavelengths retained | modes >1e-1 | modes >1e-2 | modes >1e-3 | modes >1e-4 |
|---:|---:|---:|---:|---:|---:|
| 100 V/cm | 2.80-3.91 um | 2 | 5 | 10 | 20 |
| 150 V/cm | 2.80-3.89 um | 2 | 5 | 10 | 22 |
| 200 V/cm | 2.80-3.88 um | 2 | 5 | 11 | 23 |

This is one of the most important practical results.

The exact field bracket moves the wavelength coordinate substantially but barely changes the number of recoverable spatial modes.

At a rough relative singular-value floor of `1e-2`, the optical forward problem supports only about

```math
\boxed{5}
```

well-conditioned transport modes across the `3.7 um` layer.

At `1e-3`, about `10-11` modes remain.

Do **not** interpret these thresholds as universal experimental resolutions. They depend on wavelength sampling, noise covariance, regularization, and the actual profile.

The robust conclusion is narrower:

> **the published sample-B optical physics supports a few-mode, band-limited internal transport tomography rather than arbitrary fine depth reconstruction.**

---

## 12. Approximate spatial interpretation

Five independent smooth modes across

```math
W=3.7\ {\rm um}
```

correspond to a crude characteristic scale of order

```math
W/5\sim0.7\ {\rm um},
```

while ten modes correspond to roughly

```math
W/10\sim0.4\ {\rm um}.
```

These numbers are only intuition for the singular spectrum, not point-spread-function guarantees.

The formal resolution must be obtained from the regularized estimator and experimental noise level.

---

## 13. New practical picture

The real sample changes the way the method should be described.

It is not

```text
wavelength -> exact generation point -> exact local velocity.
```

It is

```text
wavelength
-> known broad generation kernel
-> survival timing kernel
-> several recoverable smooth spatial transport modes.
```

Near cutoff the generation kernel localizes more strongly, but the absorbed signal collapses.

At shorter wavelength the signal is strong, but the optical kernel is broad.

This tradeoff is the physical origin of the limited singular spectrum.

---

## 14. What this calculation establishes

### DERIVED / CHECKED under stated inputs

- the correct front-collection survival-kernel orientation;
- the 100-200 V/cm field bracket maps to an approximate high-Cd endpoint `x=0.3435-0.3709` if `x=0.316` is used as the nominal low-Cd endpoint;
- the resulting local-gap interval is approximately `3.21-3.55 um` to `3.97 um` at 300 K;
- the Moazzami optical model shifts conditional mean generation depth by several microns across a practical MWIR wavelength sweep;
- the real optical matrix has only a few strongly conditioned spatial modes;
- the conditioning is relatively insensitive to the field bracket.

### CONDITIONAL

- interpreting the reported `x=0.316` as the low-Cd endpoint of the retained sample-B linear region;
- using a perfectly linear composition profile;
- ignoring Urbach-tail absorption, reflection, interference, and free-carrier optical effects;
- using a 5% single-pass absorption floor;
- any illustrative phase number that assumes `v_eff=10^5 m/s`.

### OPEN

- the exact FTIR-fitted sample-B `x(z)` parameters;
- calibrated minority-carrier transport in sample B;
- experimental wavelength-dependent phase/group-delay data;
- reconstruction accuracy with real measurement noise and systematic wavelength-dependent phase;
- novelty / priority of the inverse metrology method.

---

## 15. Next decisive calculation

The next step should **not** add another abstract inverse formula.

Use the dimensional sample-B matrix and test reconstruction under a realistic phase-noise model:

```text
known smooth q(z)
+
actual Moazzami optical kernels
+
0.1-1 degree wavelength-dependent phase noise
+
unknown common phase/group delay
->
recoverable spatial modes and bias.
```

This will turn the singular-value diagnostic into a direct experimental requirement.

Then the remaining decisive inputs are experimental:

1. obtain the actual sample-B `x(z)` fit parameters / curve data;
2. obtain or measure wavelength-resolved complex response;
3. compare the spectral inverse against an independent spatially localized excitation or validated transport calculation.

---

## 16. Reproducibility

Deterministic implementation:

`numerics/hgcdte_published_sample_b_forward_matrix.py`

The script contains the literature inputs, Hansen gap law, Moazzami absorption law, front-collection kernel, field-bracket calculation, singular-value regression, and illustrative differential-phase scale.
