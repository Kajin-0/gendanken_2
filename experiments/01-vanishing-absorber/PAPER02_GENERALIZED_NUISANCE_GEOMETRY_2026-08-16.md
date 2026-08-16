# Paper 02 — generalized covariance and kernel-nuisance geometry

**Date:** 2026-08-16  
**Status:** **DERIVED / MODEL-UNCERTAINTY EXTENSION / PRIORITY UNPROVEN**  
**Scope:** local inverse geometry. This note does not claim that generalized least-squares projection, nuisance profiling, or Fisher/Schur-complement identities are novel mathematical results.

## 1. Purpose

Paper 02 already separates two effects under an explicit equal-quadrature reference covariance:

```text
parameter bias  <-> tangent component of model discrepancy
model rejection <-> normal component of model discrepancy.
```

The natural extension is to arbitrary covariance and uncertain optical kernels.

The key conceptual distinction is:

```text
measurement covariance != model misspecification.
```

A random zero-mean nuisance may be represented by an effective covariance after marginalization. A fixed or biased nuisance shifts the pseudo-true inverse parameter and cannot be made harmless merely by inflating error bars.

---

## 2. Real-stacked local model

Let the measured real-stacked data vector be

```math
y=f(\theta)+B\eta+n,
```

where

- `theta` are the fitted inverse parameters;
- `eta` are nuisance/model-error coordinates not included in the fitted model;
- `B = partial f / partial eta` is the local nuisance Jacobian;
- `n ~ N(0,Sigma)` is measurement noise;
- `W = Sigma^{-1}`.

Let

```math
G=\frac{\partial f}{\partial\theta}
```

be the fitted-model Jacobian at the reference point.

For Paper 02 at one RF frequency,

```text
theta = (Re C, Im C, Re K, Im K, Re r, Im r)
```

in a 12-real-dimensional six-complex-channel data space.

---

## 3. Deterministic nuisance bias under arbitrary covariance

Suppose `eta` is fixed but small. The generalized least-squares pseudo-true displacement obeys

```math
\boxed{
\delta\theta
=(G^T W G)^{-1}G^T W B\eta
+O(\|\eta\|^2).
}
```

Define the `W`-orthogonal tangent projector

```math
\boxed{
P_W
=G(G^T W G)^{-1}G^T W.
}
```

Then the first-order post-fit discrepancy is

```math
\boxed{
e_{\rm post}=(I-P_W)B\eta.
}
```

The covariance-weighted noncentrality driving a local goodness-of-fit test is

```math
\boxed{
\lambda
=e_{\rm post}^T W e_{\rm post}
=(B\eta)^T W(I-P_W)(B\eta).
}
```

Thus covariance changes both:

1. which component of a nuisance is interpreted as parameter motion;
2. which component is statistically visible as model failure.

There is no covariance-independent ordering between parameter bias and rejection power.

---

## 4. The pseudo-true parameter is a metric-dependent object

If the inverse model is misspecified, the pseudo-true parameter is the minimizer

```math
\theta_*(W)
=\arg\min_\theta
\|y-f(\theta)\|_W^2.
```

Therefore, in general,

```math
\boxed{
\theta_*(W_1)\neq\theta_*(W_2).
}
```

even for the **same deterministic data vector**.

This is not merely an uncertainty-bar effect. The reported effective parameter can change because the metric changes the point on the wrong model manifold that is declared "closest" to the data.

For Paper 02 this means a misspecified `D_eff` should be interpreted as a property of the tuple

```text
(forward response, inverse family, covariance/weighting metric),
```

not as a metric-independent material observable.

The executable covariance stress in

```text
PAPER02_COVARIANCE_GEOMETRY_STRESS_2026-08-16.md
```

confirms that this dependence is quantitatively important in the declared surrogate.

---

## 5. Root sensitivity after profiling offset and amplitude

Partition the fitted tangent into

```math
G=[X\;H],
```

where `X` contains the profiled offset/amplitude columns and `H` contains the two real root columns.

The `W`-orthogonal projector onto `X` is

```math
P_X=X(X^T W X)^{-1}X^T W.
```

The root-identification Jacobian after profiling `X` is

```math
\boxed{
H_\perp=(I-P_X)H.
}
```

The local root Fisher information is

```math
\boxed{
I_r=H_\perp^T W H_\perp.
}
```

and the root covariance is

```math
\operatorname{Cov}(\hat r)=I_r^{-1}
```

when the fitted model is locally correct and covariance is known.

A covariance direction that is large only inside the already-profiled `X` subspace need not degrade root information appreciably. Conversely, noise concentrated along `H_perp` is especially damaging.

This explains why "more correlation" is not synonymous with "less information": orientation matters.

---

## 6. Exact same-frequency invariances

The Paper-02 one-mode model is

```math
J=C\mathbf 1+K F(r).
```

### 6.1 Common additive complex offset

For any complex `b`,

```math
J' = J+b\mathbf 1
=(C+b)\mathbf 1+K F(r).
```

Therefore the fitted root `r` is unchanged exactly.

### 6.2 Common complex gain / phase

For any nonzero complex scalar `a`,

```math
J'=aJ
=(aC)\mathbf 1+(aK)F(r).
```

Again the same root `r` fits exactly.

Hence a spectral-channel-common complex gain or phase factor at one RF frequency cannot by itself create a root bias in the ideal one-mode inverse. It lies entirely in the profiled `(C,K)` freedom.

The dangerous calibration directions are channel-dependent directions that overlap the root tangent or alter `F_m(r)` itself.

---

## 7. Kernel misspecification as a deterministic nuisance

Let each nominal generation kernel depend on nuisance coordinates `alpha`:

```math
g_m(z;\alpha).
```

The true channel is

```math
J_m^{\rm true}
=\int g_m(z;\alpha+\delta\alpha)H_{\rm true}(z)\,dz,
```

while the inverse uses the nominal `alpha`.

To first order,

```math
\delta J_m
=\sum_j B_{mj}\,\delta\alpha_j,
```

with

```math
\boxed{
B_{mj}
=\int
\frac{\partial g_m(z;\alpha)}{\partial\alpha_j}
H_{\rm true}(z)\,dz.
}
```

This `B delta alpha` enters the same tangent/normal decomposition as any other model discrepancy.

If `delta alpha` is fixed, the root is biased according to Sec. 3.

If `delta alpha` is random with zero mean and covariance `C_alpha`, then at linear order its contribution may instead be marginalized into

```math
\boxed{
\Sigma_{\rm eff}
=\Sigma_n+B C_\alpha B^T.
}
```

These are different epistemic statements. A systematic calibration bias with nonzero mean is not removed by using `Sigma_eff`; its mean still produces parameter bias.

---

## 8. Jointly fitting kernel nuisance: Schur-complement criterion

Suppose kernel nuisance coordinates are explicitly fitted or calibrated jointly with the transport root.

Let

```math
A=[X\;B]
```

collect offset/amplitude and free kernel-nuisance directions.

Without an external prior on the kernel nuisance, the root information after profiling all nuisance directions is

```math
\boxed{
I_{r\mid A}
=H^T W(I-P_A)H,
}
```

where

```math
P_A=A(A^TWA)^{-1}A^TW.
```

Equivalently, this is the Schur complement of the nuisance block in the joint Fisher matrix.

### Structural non-identifiability condition

If a root tangent direction lies in the nuisance span,

```math
Hc\in\operatorname{col}(A)
```

for some nonzero root-coordinate vector `c`, then

```math
I_{r\mid A}c=0.
```

That root combination is locally unidentifiable from the same-frequency data regardless of raw measurement SNR.

This gives a precise version of the calibration danger:

> if kernel uncertainty can reproduce the transport-root tangent after offset and amplitude are profiled, better detector/readout SNR alone cannot separate the two.

---

## 9. Finite kernel prior / calibration information

If external kernel calibration supplies a Gaussian prior

```math
\delta\alpha\sim N(0,C_\alpha),
```

then the joint local information matrix is

```math
\mathcal I=
\begin{bmatrix}
G^TWG & G^TWB\\
B^TWG & B^TWB+C_\alpha^{-1}
\end{bmatrix}.
```

The transport-root information is the appropriate Schur complement of the nuisance block.

This makes the role of calibration quantitative:

- weak prior (`C_alpha` large): kernel nuisance can absorb root-like channel structure;
- strong prior (`C_alpha` small): the root approaches the known-kernel limit;
- exact degeneracy in the data can be broken only by external information or an additional measurement axis whose nuisance and transport tangents differ.

RF frequency is one such additional axis in Paper 02 because a kernel-induced root perturbation and the homogeneous drift-diffusion dispersion law need not share the same frequency dependence.

---

## 10. Affine depth-coordinate calibration corollary

For an ideal exponential point-response basis, suppose the true depth coordinate and inverse coordinate are related by

```math
z_{\rm true}=a+bz_{\rm inv}.
```

Then

```math
e^{r z_{\rm true}}
=e^{ra}e^{(br)z_{\rm inv}},
```

so the inverse recovers

```math
\boxed{r_{\rm eff}=br.}
```

The offset `a` is absorbed into amplitude; the scale factor `b` rescales the root.

If the true root obeys the homogeneous law

```math
D\gamma^2+w\gamma=-i\omega,
```

then under `gamma_eff=b gamma`, an exactly equivalent parameterization is

```math
\boxed{
D_{\rm eff}=\frac{D}{b^2},
\qquad
w_{\rm eff}=\frac{w}{b}.
}
```

Therefore a pure affine depth-scale error **does not create positive diffusion from exact zero diffusion** in the ideal homogeneous exponential problem: `D=0` remains `D_eff=0`.

Positive false diffusion from kernel error requires a non-affine kernel-shape/registration effect, finite-boundary effect, observation-operator effect, or coupling to device heterogeneity.

This gives the executable kernel-misspecification stress a useful null expectation.

---

## 11. Experimental-design consequence

The generalized danger is controlled by the relative geometry of three subspaces:

```text
transport tangent
kernel/calibration nuisance tangent
noise covariance ellipsoid.
```

A robust experiment should therefore seek measurement axes for which

```text
transport changes strongly
while kernel nuisance changes differently.
```

Adding RF frequency, temperature, bias, or an independently calibrated optical observable can help only insofar as it rotates/separates these tangent directions. Merely increasing the number of data points is not sufficient if the new points preserve the same local degeneracy.

---

## 12. What is established

**DERIVED:**

- arbitrary covariance changes both pseudo-true parameter bias and goodness-of-fit geometry;
- under model misspecification, an effective parameter can depend on the weighting/covariance metric;
- common complex gain and common additive offset are exact same-frequency root invariances of the Paper-02 one-mode model;
- fixed kernel misspecification is a deterministic bias problem, whereas zero-mean random kernel uncertainty may be marginalized into an effective covariance;
- jointly free kernel nuisance reduces root information through a Schur complement;
- if the root tangent lies in the kernel-nuisance span, the corresponding root combination is locally unidentifiable regardless of SNR;
- a pure affine depth-coordinate error rescales homogeneous `D,w` but cannot create positive `D` from exact `D=0` in the ideal exponential homogeneous limit.

**CHECKED numerically elsewhere:**

- the frequency-dependent hidden-risk ordering survives a broad covariance stress;
- pseudo-true `D_eff` can shift substantially under covariance metric changes.

**OPEN at creation of this note:**

- numerical magnitude of realistic controlled kernel misspecification in the exact planar counterexample;
- whether kernel error alone can generate positive `D_eff` in the uniform-velocity zero-diffusion null under non-affine kernel perturbations;
- calibration precision needed to keep kernel-induced root bias below the deterministic heterogeneity-induced effect;
- experimental values for any specific detector/instrument.
