# Minimal Transport Fisher Bound — Precision Scaling After Structural Identifiability Is Solved

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** for the uniform two-depth DC + complex-RF gedanken experiment; no novelty/priority claim

## 1. Natural parameterization

The recombination identifiability theorem showed that the measurement-natural variables are

```math
\boxed{
\theta=(D,V_*,\gamma_0),
}
```

where

```math
V_* = \sqrt{v^2+4D\kappa}
```

and

```math
\gamma_0
=\frac{\sqrt{v^2+4D\kappa}-v}{2D}.
```

The DC-normalized RF spatial propagation constant obeys

```math
\boxed{
D\Gamma^2+V_*\Gamma=i\omega.
}
\tag{1}
```

The physical parameters follow from

```math
\boxed{
v=V_*-2D\gamma_0,
}
\tag{2}
```

```math
\boxed{
\kappa=V_*\gamma_0-D\gamma_0^2.
}
\tag{3}
```

---

# 2. Minimal two-depth data vector

Let two generation coordinates differ by

```math
\Delta z=x_2-x_1.
```

After common-gain cancellation, use the real data vector

```math
\boxed{
\mathbf m
=\Delta z
\begin{pmatrix}
\gamma_0\\
\operatorname{Re}\Gamma\\
\operatorname{Im}\Gamma
\end{pmatrix}.
}
\tag{4}
```

Interpret the three components as

```text
DC log-collection contrast,
RF log-magnitude contrast,
RF phase contrast.
```

Let their independent standard deviations be

```math
\sigma_0,
\qquad
\sigma_A,
\qquad
\sigma_\phi.
```

Then

```math
C
=\operatorname{diag}
(\sigma_0^2,\sigma_A^2,\sigma_\phi^2).
```

---

# 3. Exact RF sensitivities without differentiating the square root

Differentiate the implicit relation (1).

With respect to `D`:

```math
\Gamma^2
+(V_*+2D\Gamma)
\frac{\partial\Gamma}{\partial D}
=0.
```

Therefore

```math
\boxed{
\frac{\partial\Gamma}{\partial D}
=-\frac{\Gamma^2}
{V_*+2D\Gamma}.
}
\tag{5}
```

With respect to `V_*`:

```math
\Gamma
+(V_*+2D\Gamma)
\frac{\partial\Gamma}{\partial V_*}
=0,
```

so

```math
\boxed{
\frac{\partial\Gamma}{\partial V_*}
=-\frac{\Gamma}
{V_*+2D\Gamma}.
}
\tag{6}
```

These exact derivatives are numerically stable and make the Fisher structure transparent.

---

# 4. Exact Fisher matrix

The Jacobian of the real data vector is

```math
J
=\Delta z
\begin{pmatrix}
0&0&1\\
\operatorname{Re}\Gamma_D&
\operatorname{Re}\Gamma_V&0\\
\operatorname{Im}\Gamma_D&
\operatorname{Im}\Gamma_V&0
\end{pmatrix},
\tag{7}
```

where

```math
\Gamma_D=\partial_D\Gamma,
\qquad
\Gamma_V=\partial_{V_*}\Gamma.
```

For Gaussian measurement errors,

```math
\boxed{
F
=J^TC^{-1}J.
}
\tag{8}
```

The Cramer-Rao covariance bound in the natural variables is

```math
\boxed{
\operatorname{Cov}(D,V_*,\gamma_0)
\succeq F^{-1}.
}
\tag{9}
```

The DC slope is orthogonal to the RF block in this ideal noise model, so

```math
\boxed{
\sigma_{\gamma_0}
\ge\frac{\sigma_0}{\Delta z}.
}
\tag{10}
```

exactly.

All three information channels scale as

```math
F\propto(\Delta z)^2.
```

Therefore, before model-bias effects are included,

```math
\boxed{
\sigma_{\rm parameter}\propto\frac{1}{\Delta z}.
}
\tag{11}
```

This gives a simple design rule:

> **Use the largest generation-depth separation that still satisfies the local/uniform transport approximation.**

---

# 5. Low-frequency asymptotic precision laws

For

```math
D\omega/V_*^2\ll1,
```

```math
\Gamma
\simeq
\frac{i\omega}{V_*}
+
\frac{D\omega^2}{V_*^3}.
\tag{12}
```

Therefore the RF phase contrast is approximately

```math
\Delta\phi
\simeq
\Delta z\frac{\omega}{V_*},
```

while the RF log-magnitude contrast is approximately

```math
\Delta\ln|H|
\simeq
\Delta z\frac{D\omega^2}{V_*^3}.
```

If the two channels are treated separately at leading order,

```math
\boxed{
\sigma_{V_*}
\sim
\frac{V_*^2}{\Delta z\,\omega}
\sigma_\phi
}
\tag{13}
```

and

```math
\boxed{
\sigma_D
\sim
\frac{V_*^3}{\Delta z\,\omega^2}
\sigma_A.
}
\tag{14}
```

This predicts a fundamental asymmetry:

```text
velocity-like information improves ~omega
while
leading diffusion information improves ~omega^2.
```

Hence raising RF frequency initially helps diffusion estimation much faster than drift estimation, until high-frequency model breakdown, transfer attenuation, electrical parasitics, or WKB error intervene.

---

# 6. Lifetime precision and the long-lifetime limit

The DC slope is

```math
\gamma_0
=\frac{\sqrt{v^2+4D\kappa}-v}{2D}.
```

For weak recombination,

```math
\kappa\ll v^2/D,
```

```math
\boxed{
\gamma_0
\simeq
\frac{\kappa}{v}.
}
\tag{15}
```

Thus the DC log-collection contrast is

```math
\Delta\ln I_{\rm DC}
\simeq
\Delta z\frac{\kappa}{v}.
```

Since

```math
\sigma_{\gamma_0}=\sigma_0/\Delta z,
```

the relative recombination-rate uncertainty becomes approximately

```math
\boxed{
\frac{\sigma_\kappa}{\kappa}
\sim
\frac{\sigma_0}
{|\Delta\ln I_{\rm DC}|}.
}
\tag{16}
```

So extremely long lifetimes are intrinsically hard to determine from collection loss: the DC signal approaches unity and the information vanishes.

This is a physical identifiability/precision limit, not a failure of the RF method.

---

# 7. Transforming the CRLB to physical parameters

Let

```math
\psi=(D,v,\kappa).
```

From Eqs. (2)-(3), the Jacobian from natural to physical variables is

```math
\boxed{
K
=
\frac{\partial(D,v,\kappa)}
{\partial(D,V_*,\gamma_0)}
=
\begin{pmatrix}
1&0&0\\
-2\gamma_0&1&-2D\\
-\gamma_0^2&\gamma_0&v
\end{pmatrix}.
}
\tag{17}
```

Therefore

```math
\boxed{
\operatorname{Cov}(D,v,\kappa)
\succeq
K F^{-1}K^T.
}
\tag{18}
```

This gives the complete local Gaussian precision bound for the minimal experiment.

---

# 8. Bias-variance tradeoff in spatial separation

Equation (11) favors large `Delta z`.

But the slowly varying theory requires the transport parameters to remain sufficiently constant across the interval.

Therefore the ideal experiment has a real tradeoff:

```text
small Delta z
-> low model bias, poor statistical precision

large Delta z
-> high statistical precision, increasing nonuniform/WKB bias.
```

The WKB correction derived in

`SPECTRAL_DERIVATIVE_DRIFT_DIFFUSION_TOMOGRAPHY.md`

provides the model-bias scale.

Thus the optimal spatial/spectral separation should minimize a combined bias-plus-variance criterion rather than simply maximize phase difference.

This is the correct next experimental-design theory once real covariance is introduced.

---

# 9. Numerical regression

`numerics/minimal_transport_fisher_bound.py`

checks the analytic derivatives against finite differences and constructs the full Fisher and transformed physical covariance matrices.

For its explicit test point, the analytic complex derivatives agree with finite differences at roughly `1e-10` relative scale, and the Fisher matrix is full rank.

The exact DC bound

```math
\sigma_{\gamma_0}=\sigma_0/\Delta z
```

is recovered numerically.

---

# 10. Strong falsifiable precision predictions

### P1 — inverse depth-separation scaling

At fixed per-channel noise and within the uniform/local regime, parameter standard deviations must scale as `1/Delta z`.

### P2 — diffusion gains faster with RF frequency

At low normalized frequency, `sigma_D` improves as `omega^-2`, while `sigma_V` improves only as `omega^-1`.

### P3 — long-lifetime information collapse

As `kappa -> 0`, DC collection contrast vanishes and lifetime uncertainty diverges unless another lifetime-sensitive observable is added.

### P4 — full-complex advantage is quantitative

Removing RF log-magnitude removes the leading `D omega^2/V_*^3` channel and sharply degrades diffusion identifiability.

### P5 — local optimum must be finite

Real systems should exhibit an optimum generation-depth separation once increasing WKB/model bias offsets the `1/Delta z` statistical gain.

---

# 11. Next theory step

The next useful derivation is the **bias-variance optimum** for slowly varying transport:

1. express local model bias in terms of `gamma_1/gamma_0` and generation-kernel moments;
2. combine it with the Fisher variance above;
3. derive an optimal spectral/depth separation scaling;
4. then evaluate that scaling for HgCdTe only as a worked example.

This keeps the project on the theory-first path: exact structure first, material substitution last.
