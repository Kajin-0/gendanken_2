# Published 2023 Sample B — Dimensional Spectral-Timing Forward Matrix

**Date:** 2026-08-09  
**Status:** literature-constrained dimensional optical/timing-kernel calculation; not a calibrated reconstruction of sample-B transport; no novelty claim

## 1. Why sample B

Xu et al. 2023 report a processed graded-HgCdTe sample B with

```text
thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
PN junction at the high-Cd end
linear-gradient built-in field ~100-200 V/cm over the reported temperature range.
```

Primary source:

G.-Q. Xu et al., `Photoelectric characteristics of compositionally graded HgCdTe detector`, *Journal of Infrared and Millimeter Waves* 42 (2023) 285-291, DOI `10.11972/j.issn.1001-9014.2023.03.001`.

The authors explicitly infer that the remaining `100-200 V/cm` linear-gradient field in sample B does not strongly alter carrier motion. That makes sample B a useful **smooth calibration case** for the inverse. Sample A, which retains part of the nonlinear interdiffusion region and reaches local fields near `2e3 V/cm`, is the stronger later contrast/anomaly case.

---

## 2. Correct collection orientation

Use

```text
z=0 : high-Cd junction side
z=W : low-Cd side
```

with

```math
W=3.7\ {\rm um}.
```

For front collection,

```math
T(z)=\int_0^z q(s)ds.
```

Therefore

```math
\boxed{
\bar T_i
=\int_0^W S_i(s)q(s)ds,
}
```

where

```math
\boxed{
S_i(s)=P(Z_g\ge s|\lambda_i,{\rm abs}).
}
```

The sample-B timing kernel is the conditional generation **survival function**.

For a piecewise-constant delay density, use the cell-integrated matrix

```math
\boxed{
A_{ij}=\int_{\text{cell }j}S_i(s)ds.
}
```

---

## 3. Composition model and current envelope

The article gives the longitudinal fit model

```math
x(z)
=x_s+s(d-z)
+(1-x_s-sd)
\left\{
1-\left[
\operatorname{erf}\!\left(\frac{2z}{\Delta z}\right)
\right]^3
\right\}.
```

However, the fitted sample-B parameters are only available graphically in the accessible article.

The present calculation therefore treats

```math
x_{\rm low}=0.316
```

as a **conditional nominal low-Cd endpoint** and brackets the retained linear region by

```math
F_g=100,150,200\ {\rm V/cm}.
```

This envelope must eventually be replaced by the actual fitted/digitized `x(z)`.

---

## 4. Band-gap calibration

Use Hansen-Schmit-Casselman

```math
\boxed{
E_g(x,T)
=-0.302+1.93x
+5.35\times10^{-4}T(1-2x)
-0.81x^2+0.832x^3.
}
```

At `x=0.316`, `T=300 K`:

```math
\boxed{E_{g,\rm low}=0.312314\ {\rm eV},}
```

```math
\boxed{\lambda_{g,\rm low}=3.9699\ {\rm um}.}
```

The `+0.832x^3` coefficient is intentional.

Using `Delta Eg=F_g W`, the field bracket gives

| gradient | inferred `x_high` | `Eg,high` | `lambda_g,high` |
|---:|---:|---:|---:|
| 100 V/cm | 0.34348 | 0.34931 eV | 3.5494 um |
| 150 V/cm | 0.35721 | 0.36781 eV | 3.3708 um |
| 200 V/cm | 0.37091 | 0.38631 eV | 3.2094 um |

Thus the present 300 K local-gap encoding interval is approximately

```math
\boxed{3.2\text{-}3.55\ {\rm um}\to3.97\ {\rm um}.}
```

---

## 5. Optical model

Use Moazzami et al. 2005 above-gap absorption:

```math
\boxed{
\alpha(E,x,T)
=K(x,T)
\left(\frac{E-E_g}{E}\right)^{n(x,T)},
\qquad E>E_g,
}
```

with their published `K(x,T)` and `n(x,T)`.

For front illumination,

```math
\boxed{
g(z|\lambda)
=\alpha(z,\lambda)
\exp\!\left[-\int_0^z\alpha(u,\lambda)du\right].}
```

The current model sets sub-gap absorption to zero and omits Urbach-tail absorption, reflection, interference, and free-carrier optical effects.

---

## 6. Central 150 V/cm optical result

| wavelength | single-pass `Pabs` | conditional mean depth | RMS depth width |
|---:|---:|---:|---:|
| 2.80 um | 0.998 | 0.677 um | 0.621 um |
| 3.20 um | 0.975 | 1.155 um | 0.860 um |
| 3.37 um | 0.917 | 1.704 um | 0.896 um |
| 3.50 um | 0.786 | 2.369 um | 0.703 um |
| 3.70 um | 0.417 | 3.088 um | 0.383 um |
| 3.85 um | 0.115 | 3.459 um | 0.161 um |
| 3.88 um | 0.070 | 3.523 um | 0.120 um |

Therefore

```math
\boxed{
\Delta\langle z\rangle_{2.80\to3.88}
\approx2.85\ {\rm um}.
}
```

Near cutoff the optical kernel becomes spatially narrow, but the absorbed signal falls sharply.

---

## 7. RF phase scale

For illustration only, take

```math
v_{\rm eff}=10^5\ {\rm m/s}.
```

Then the `2.80 -> 3.88 um` depth shift gives

```math
\Delta T\approx28.5\ {\rm ps}
```

and

```math
\boxed{|\Delta\phi|\approx10.25^\circ}
```

at `1 GHz`.

This is a measurement scale, **not** a sample-B velocity prediction.

---

## 8. Corrected real-matrix conditioning

Use

```text
80 spatial cells
lambda = 2.80-3.95 um in 0.01 um steps
retain Pabs >= 0.05
cell-integrated survival kernels.
```

Relative singular-mode counts above `[1e-1,1e-2,1e-3,1e-4]` are

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

The earlier pre-cell-integration central count `[2,5,10,22]` is **SUPERSEDED**.

The field bracket changes the spectral coordinate much more than it changes the conditioning.

The safe interpretation is:

> **sample B supports a few-mode, band-limited internal transport inverse, not arbitrary pointwise depth reconstruction.**

The singular thresholds are conditioning diagnostics, not universal resolution limits.

---

## 9. Calibration/contrast strategy

The published devices naturally suggest

```text
sample B
-> smooth linear-gradient calibration case
-> test whether the inverse recovers only coarse/smooth transport

sample A
-> retained nonlinear high-field region
-> later test whether the inverse localizes a real transport contrast.
```

This is an inference from the authors' published carrier-collection interpretation, not a claim that either sample has already undergone the proposed timing inversion.

---

## 10. Claim boundary

### DERIVED / CHECKED under stated inputs

- front-collection survival-kernel orientation;
- 300 K gap/field-bracket envelope;
- several-micron wavelength-controlled generation-depth shift;
- only a few strongly conditioned spatial modes;
- weak dependence of mode count on the 100-200 V/cm field bracket.

### CONDITIONAL

- interpreting `x=0.316` as the low-Cd endpoint;
- replacing the unavailable sample-B fit by a linear profile;
- Moazzami above-gap optics without tail/reflection/interference corrections;
- illustrative phase based on `v_eff=1e5 m/s`.

### OPEN

- actual sample-B fitted `x(z)` parameters;
- calibrated carrier transport;
- wavelength-resolved complex response;
- instrument covariance;
- novelty / priority.

---

## 11. Reproducibility

Deterministic implementation:

`numerics/hgcdte_published_sample_b_forward_matrix.py`

Next use the real matrix with an instrument-level wavelength × frequency covariance model rather than adding more abstract inverse algebra.
