# Paper 02 tangent-confound theorem

**Date:** 2026-08-15  
**Status:** **DERIVED / CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN**  
**Scope:** local structure of the rank-one spectral-depth model; this note does not claim that the theorem itself is novel.

## 1. Motivation

The refined 2-D geometry sweep produced a specific pattern that the existing model-order discussion did not explain cleanly.

For the 75%-contact geometry, adding the 3.0 um depletion / space-charge perturbation changes the transport-mimic strength by more than an order of magnitude at 500 MHz and 1 GHz, while the second singular-value ratio changes very little. At the refined numerical resolution and centered beam:

| RF | finite 75%, no depletion: mimic | finite 75% + depletion: mimic | `sigma2/sigma1`, no depletion | `sigma2/sigma1`, + depletion |
|---|---:|---:|---:|---:|
| 100 MHz | 0.0932 | 0.7381 | 4.839e-4 | 4.804e-4 |
| 500 MHz | 0.0610 | 0.7803 | 6.206e-4 | 5.635e-4 |
| 1 GHz | 0.0358 | 0.8651 | 8.805e-4 | 8.582e-4 |

At 500 MHz and 1 GHz the resulting warning margin is negative, so the reference transport-sized signature becomes statistically usable before the higher-rank warning.

This suggests that a confound can move the measured sequence mainly **along** the local rank-one model manifold instead of away from it.

The following statement makes that intuition exact.

---

## 2. Rank-one sequence

Let the adjacent spectral-depth differences at a fixed frequency be

```math
d_m = A q^m,
```

with nonzero complex `A` and `q` and integer channel index `m`.

For any three consecutive differences define the local rank-one closure

```math
C_m = 2\log d_{m+1} - \log d_m - \log d_{m+2}.
```

On a consistent local logarithm branch,

```math
C_m=0
```

for the exact rank-one sequence.

Now perturb the measured sequence:

```math
d_m(\epsilon)=d_m+\epsilon g_m+O(\epsilon^2).
```

Define the normalized perturbation

```math
h_m = \frac{g_m}{d_m}.
```

All statements below are local in `epsilon`, so they do not depend on a global logarithm-branch choice.

---

## 3. Theorem: closure measures curvature, fitted multiplier measures slope

Differentiating the closure at `epsilon=0` gives

```math
\boxed{
\frac{dC_m}{d\epsilon}\bigg|_0
=2h_{m+1}-h_m-h_{m+2}
=-\Delta^2 h_m.
}
```

Thus the first-order rank-one closure is sensitive to the **discrete curvature** of the normalized perturbation across channel index.

By contrast, define the local adjacent-ratio multiplier estimator

```math
R_m(\epsilon)=\log\frac{d_{m+1}(\epsilon)}{d_m(\epsilon)}.
```

Then

```math
\boxed{
\frac{dR_m}{d\epsilon}\bigg|_0
=h_{m+1}-h_m
=\Delta h_m.
}
```

Therefore an apparent shift of the fitted spatial multiplier is driven by the **discrete slope** of the same normalized perturbation.

The two diagnostics are not ordered by any general inequality.

---

## 4. Corollary: exact first-order hidden confound

Suppose

```math
h_m=a+b m.
```

Then

```math
\Delta^2 h_m=0,
```

so

```math
\frac{dC_m}{d\epsilon}\bigg|_0=0
```

for every adjacent closure, while

```math
\frac{dR_m}{d\epsilon}\bigg|_0=b.
```

Hence `b != 0` gives a first-order apparent transport-multiplier shift with **zero first-order rank-one closure residual**.

This is not an accidental algebraic degeneracy. The perturbation is exactly tangent to the rank-one manifold because

```math
g_m=d_m(a+b m)
=a\,\frac{\partial d_m}{\partial\log A}
+b\,\frac{\partial d_m}{\partial\log q}.
```

So the two tangent directions are amplitude change and multiplier change.

---

## 5. Finite-amplitude version

The local result has an exact finite counterpart.

If a confound transforms one rank-one sequence into another,

```math
d'_m=A' q'^m,
```

then all same-frequency rank-one closures remain exactly zero even when `q' != q`.

Equivalently,

```math
\log\frac{d'_m}{d_m}
=\log\frac{A'}{A}
+m\log\frac{q'}{q}
```

is exactly affine in channel index.

Therefore no model-order test operating only on that fixed-frequency sequence can distinguish a true change in the intended transport parameter from a nuisance mechanism that maps the data to another point on the same model manifold.

This is an identifiability statement, not merely an SNR statement.

---

## 6. Noise-weighted geometric interpretation

Let `J` be the Jacobian of the rank-one model with respect to its local parameters and let `W` define the measurement-noise metric.

For a small nuisance perturbation `g`, decompose

```math
g=P_T g+(I-P_T)g,
```

where `P_T` is the `W`-orthogonal projection onto the tangent space of the rank-one model manifold.

To first order:

- fitted-parameter bias is controlled by the tangential component `P_T g`;
- goodness-of-fit / rank-breaking residual is controlled by the normal component `(I-P_T)g`.

Thus a nuisance can create a large fitted transport bias and an arbitrarily small same-frequency rank-breaking signal when it is nearly tangent to the model manifold.

The appropriate danger metric is therefore not nuisance magnitude alone but a **tangent-to-normal ratio**.

A strong geometric distortion may actually be easier to reject if it has a large normal component, while an intermediate perturbation can be more dangerous if it aligns with the model tangent.

---

## 7. Connection to the refined geometry sweep

The refined quick sweep is consistent with this mechanism.

For centered illumination at 500 MHz:

- finite 75%, no depletion: `mimic = 0.0610`, `sigma2/sigma1 = 6.206e-4`;
- finite 75% + depletion: `mimic = 0.7803`, `sigma2/sigma1 = 5.635e-4`.

The nuisance signal grows by about a factor of 12.8 while the second-mode ratio becomes slightly smaller.

At 1 GHz:

- finite 75%, no depletion: `mimic = 0.0358`, `sigma2/sigma1 = 8.805e-4`;
- finite 75% + depletion: `mimic = 0.8651`, `sigma2/sigma1 = 8.582e-4`.

The nuisance signal grows by about a factor of 24.2 with essentially no increase in the second-mode amplitude.

By contrast, the 50%-contact geometries produce larger absolute mimic ratios but also much larger second-mode signatures and positive warning margins. This is qualitatively what the tangent/normal picture predicts: the most distorted geometry need not be the most dangerous geometry.

This agreement is **supporting evidence only**. The current CSV records aggregate closure/rank diagnostics, not the full noise-weighted tangent projection of each six-channel complex sequence.

---

## 8. Immediate falsification test

The next numerical step is not a broad parameter sweep.

First perform a factorial decomposition at fixed optical kernels and fine numerical resolution:

1. planar contact, no depletion;
2. planar contact + depletion;
3. 75% contact, no depletion;
4. 75% contact + depletion;
5. 50% contact, no depletion;
6. 50% contact + depletion.

This separates:

- depletion/electrostatic-field contribution;
- finite-contact / weighting-field contribution;
- nonlinear interaction between them.

If the hidden 75%+depletion result is already present for planar+depletion, then the current Paper-02 framing must be broadened from purely multidimensional geometry to **device electrostatics as a material-transport confound**.

If neither component alone reproduces it but their combination does, the interaction itself becomes the relevant physical result.

After that, the full six-channel complex sequences should be stored so the nuisance vector can be projected explicitly onto the rank-one tangent and normal subspaces.

---

## 9. What is established

**DERIVED:**

- rank-one closure responds at first order to discrete curvature of the normalized perturbation;
- apparent multiplier bias responds at first order to discrete slope;
- affine normalized perturbations are tangent to the rank-one manifold and can shift the inferred multiplier with no first-order closure signal;
- an exact nuisance mapping between two rank-one sequences is fundamentally invisible to same-frequency rank/model-order tests;
- model-bias magnitude and model-rejection magnitude therefore have no universal monotonic relation.

**NUMERICALLY OBSERVED IN THE CURRENT CONDITIONAL MODEL:**

- the refined 75%+depletion geometry produces four order-one hidden-risk rows;
- refinement from the coarse to the original fine discretization preserves all four;
- the depletion perturbation greatly increases transport-mimic strength for the 75%-contact case without a comparable increase in `sigma2/sigma1`.

**NOT YET ESTABLISHED:**

- whether depletion alone or contact/depletion interaction causes the near-tangent perturbation;
- the explicit tangent/normal projection of the full complex six-channel nuisance vector;
- robustness over broader device geometry;
- experimental magnitude in any calibrated detector;
- novelty relative to detector-systematics / inverse-problem literature.

The theorem should therefore be used as a design principle for the next calculations, not as a publication claim by itself.
