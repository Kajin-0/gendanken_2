# RF rejection precision and bandwidth criterion

**Date:** 2026-08-15  
**Status:** **DERIVED / STATISTICAL DESIGN CRITERION — PRIORITY UNPROVEN**

## 1. Purpose

The homogeneous drift-diffusion hierarchy uses additional RF frequencies as overdetermined falsification measurements.

The Paper-02 nuisance calculation shows why the statement

> “the next RF tries to kill the model”

must be separated into two questions:

1. **structural:** does the wrong mechanism lie exactly on the homogeneous model manifold?
2. **statistical:** is the departure from that manifold large enough relative to the propagated measurement covariance to reject it with specified significance and power?

The first question is binary mathematics.
The second is an experimental-design calculation.

This note gives the required statistic.

---

## 2. Root-space formulation

At RF frequencies `omega_j`, collect the recovered complex spatial exponents into a real vector

```math
\mathbf x
=
[\Re\gamma_1,\Im\gamma_1,\ldots,
 \Re\gamma_M,\Im\gamma_M]^T.
```

Let

```math
\mathbf m(\mathbf p)
```

be the corresponding homogeneous drift-diffusion-recombination prediction for parameter vector

```math
\mathbf p=(D,w,\kappa)
```

or the relevant reduced parameterization.

Let `C_gamma` be the covariance of the real-stacked recovered roots.

The generalized least-squares model-rejection statistic is

```math
\boxed{
T
=
\min_{\mathbf p}
[\mathbf x-\mathbf m(\mathbf p)]^T
C_\gamma^{-1}
[\mathbf x-\mathbf m(\mathbf p)].
}
```

For a locally regular model and correctly specified Gaussian covariance, the null statistic is asymptotically chi-square with

```math
\nu=N_{\rm data}-N_{\rm fitted\ parameters}
```

degrees of freedom after accounting for any independent constraints and correlations.

---

## 3. Local profiled mismatch

Let `p_*` be the closest homogeneous-model point to the deterministic nuisance system under the chosen covariance metric.

Define the deterministic root discrepancy

```math
\mathbf d
=\mathbf x_{\rm nuisance}-\mathbf m(\mathbf p_*).
```

Let

```math
J_p
=\frac{\partial\mathbf m}{\partial\mathbf p}
```

be the real model Jacobian at `p_*`.

The covariance-weighted precision projected normal to the fitted-parameter tangent is

```math
\boxed{
Q_\perp
=C_\gamma^{-1}
-C_\gamma^{-1}J_p
(J_p^TC_\gamma^{-1}J_p)^{-1}
J_p^TC_\gamma^{-1}.
}
```

The noncentrality parameter under the nuisance alternative is

```math
\boxed{
\Lambda
=\mathbf d^TQ_\perp\mathbf d.
}
```

This is the correct scalar measure of practical distinguishability.

A large raw complex residual at one frequency can contribute little if it lies along a poorly constrained parameter direction or has large covariance.

A smaller residual can be decisive if it lies in a low-noise direction normal to the model manifold.

---

## 4. Significance and power

Choose false-rejection probability `alpha` and desired detection power `1-beta`.

Let

```math
q_\alpha
=F^{-1}_{\chi^2_\nu}(1-\alpha)
```

be the null rejection threshold.

Under the nuisance alternative,

```math
T\sim\chi^2_\nu(\Lambda),
```

a noncentral chi-square distribution.

The experiment has the desired power when

```math
\boxed{
P[\chi^2_\nu(\Lambda)>q_\alpha]
\ge1-\beta.
}
```

This defines a required noncentrality

```math
\Lambda_{\rm req}(\nu,\alpha,\beta).
```

The design requirement is therefore

```math
\boxed{
\mathbf d^TQ_\perp\mathbf d
\ge
\Lambda_{\rm req}.
}
```

No arbitrary “3-sigma SNR” translation is necessary once the full covariance is available.

---

## 5. Propagating spectral-channel noise to root covariance

At one RF frequency, the calibrated one-mode root estimator has first-order influence

```math
\delta r
=
\frac{\mathbf h_\perp^\dagger W\mathbf n}
{\mathbf h_\perp^\dagger W\mathbf h_\perp},
```

where `h_perp` is the profiled root-sensitivity vector derived in `PAPER02_PARAMETER_BIAS_BOUND_2026-08-15.md`.

For proper complex channel covariance `Sigma_y` and optimal weighting

```math
W=\Sigma_y^{-1},
```

the complex root-error second moment is

```math
\boxed{
E[|\delta r|^2]
=\frac{1}
{\mathbf h_\perp^\dagger\Sigma_y^{-1}\mathbf h_\perp}
}
```

under the corresponding complex-noise convention.

Since

```math
\delta\gamma=-\delta r,
```

this directly supplies the local root covariance, with real/imaginary factors handled according to whether `Sigma_y` is represented in complex or real-stacked form.

Thus the same inverse-conditioning quantity that controls systematic bias also controls statistical precision.

---

## 6. Law-residual formulation

Instead of working directly with roots, define the complex homogeneous physical-law residual

```math
F_j
=D\gamma_j^2+w\gamma_j-\kappa+i\omega_j
```

for the Fourier convention used in the current Paper-02 tests.

The local sensitivity to root noise is

```math
\boxed{
\frac{\partial F_j}{\partial\gamma_j}
=2D\gamma_j+w.
}
```

Therefore, once the root covariance is known, the covariance of the complex law residual follows by ordinary Jacobian propagation.

A convenient normalized residual is

```math
\rho_j=\frac{F_j}{\omega_j},
```

whose magnitude is the dimensionless relative physical-law mismatch quoted in the current numerical records.

The covariance of `rho_j`, not `|rho_j|` alone, determines statistical rejectability.

---

## 7. Simple one-new-frequency special case

Suppose all homogeneous parameters have been fixed independently by lower-frequency measurements and one additional complex RF point is used purely as a falsification measurement.

Let the real and imaginary parts of its normalized law residual have equal independent standard deviation `s_rho`.

If the deterministic wrong-model residual has magnitude

```math
R=|\rho|,
```

then

```math
\boxed{
\Lambda=\frac{R^2}{s_\rho^2}
}
```

with two real degrees of freedom.

For the illustrative choice

```text
alpha = 0.0027
power = 0.90
nu    = 2
```

(the false-rejection probability often associated approximately with a two-sided “3 sigma” convention, but treated here through the exact chi-square calculation), the required noncentrality is

```math
\boxed{\Lambda_{\rm req}\simeq21.106}
```

or

```math
\boxed{\sqrt{\Lambda_{\rm req}}\simeq4.594.}
```

Therefore the per-quadrature normalized-law standard deviation must satisfy

```math
\boxed{
s_\rho
\lesssim
\frac{R}{4.594}
}
```

for 90% power under this simple independent-point design.

This is an illustration, not a replacement for the full covariance calculation.

---

## 8. Current planar-depletion example

For the kernel-aware deterministic zero-diffusion depletion stress, the wrong homogeneous model identified at 100 MHz has relative law mismatch approximately

```text
25 MHz     0.000090
50 MHz     0.000071
100 MHz    0        [identification point]
200 MHz    0.000280
300 MHz    0.000745
500 MHz    0.002219
750 MHz    0.005044
1 GHz      0.008885
1.5 GHz    0.019201
2 GHz      0.032276
3 GHz      0.063461
```

Under the deliberately simplified one-new-complex-point criterion above (`alpha=0.0027`, 90% power), the required per-quadrature normalized-law precision would be approximately

| RF | wrong-model mismatch `R` | required `s_rho <= R/4.594` |
|---:|---:|---:|
| 200 MHz | 0.0280% | 0.0061% |
| 300 MHz | 0.0745% | 0.0162% |
| 500 MHz | 0.2219% | 0.0483% |
| 750 MHz | 0.5044% | 0.1098% |
| 1 GHz | 0.8885% | 0.1934% |
| 1.5 GHz | 1.9201% | 0.4179% |
| 2 GHz | 3.2276% | 0.7026% |
| 3 GHz | 6.3461% | 1.3814% |

These numbers are **normalized physical-law precision**, not raw photodetector amplitude SNR and not channel-by-channel instrument specifications.

The mapping from detector measurements to this table must pass through the calibrated-kernel root Fisher information and all relevant covariance/correlation structure.

---

## 9. Why higher RF becomes powerful

The low-frequency effective-diffusion theorem shows that a heterogeneous deterministic response can match the homogeneous model through `O(omega^2)`.

After those coefficients are fitted, the first local mismatch appears at cubic and higher order.

Consequently, as long as the analytic expansion remains valid,

```math
|F_{\rm mismatch}|
```

grows more rapidly with frequency than the lower-order fitted terms.

The numerical example shows this transition directly: the mismatch is only `O(10^-4)` below a few hundred MHz but reaches percent scale above roughly 1 GHz.

This does not imply that “highest frequency is always best.” The root covariance, device amplitude, electronic bandwidth, parasitics, and model validity all change with frequency.

The correct experiment chooses frequencies that maximize the **Mahalanobis normal distance**

```math
\boxed{
\mathbf d^TQ_\perp\mathbf d,
}
```

not merely raw frequency or raw residual magnitude.

---

## 10. Combined systematic and statistical attribution requirement

Paper 02 now has two complementary inequalities.

### Systematic bias

From remote-kernel leakage,

```math
|\delta D|_{\rm sys}
\le
L_D H_R
\frac{(\sum_m w_mp_m^2)^{1/2}}
{\|h_\perp\|_W}
```

to first order.

### Statistical model rejection

For the competing homogeneous model,

```math
\mathbf d^TQ_\perp\mathbf d
\ge
\Lambda_{\rm req}(\nu,\alpha,\beta).
```

A defensible microscopic-diffusion attribution therefore requires both:

1. the claimed material `D` to exceed the bounded device-level systematic bias;
2. the measured frequency dependence to have sufficient covariance-weighted normal distance to reject plausible nuisance alternatives when they are explicitly modeled.

This is stronger than reporting a positive best-fit `D` and a small same-frequency residual.

---

## 11. Experimental design interpretation

The current theoretical program suggests that a future spectral-depth RF measurement should be designed by maximizing information in **two orthogonal directions**:

### Parameter direction

Enough spectral sensitivity to estimate the intended homogeneous transport parameters with useful precision.

### Falsification direction

Enough additional frequency/kernel diversity that realistic device-level nuisances acquire a measurable normal component outside the homogeneous model tangent.

The optimal channels are not necessarily those that maximize responsivity or source-depth separation individually.

They are those that maximize parameter information **and** nuisance discrimination under the actual covariance.

---

## 12. Current status of Gate C

The statistical criterion is now derived.

What remains before treating Gate C as fully checked is a numerical end-to-end covariance example using a specified channel noise model:

1. assign or parameterize complex channel covariance `Sigma_y`;
2. propagate it through the kernel-aware root estimator;
3. fit the homogeneous transport parameters across the identification frequencies;
4. compute the profiled noncentrality `Lambda` for the deterministic nuisance alternatives;
5. report required channel SNR / phase precision as a function of RF bandwidth.

That calculation can remain theoretical. No physical experiment is required.
