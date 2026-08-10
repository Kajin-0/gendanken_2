# Spectral-Derivative Drift–Diffusion Tomography — Local Transport from a Monotonic Generation-Depth Encoder

**Date:** 2026-08-10  
**Status:** **DERIVED asymptotic theory** for slowly varying 1-D drift-diffusion plus sharply localized generation depth; numerical WKB branch **CHECKED** on explicit variable-coefficient stresses; no novelty/priority claim

## 1. Why this is the next gedanken step

The exact uniform theorem showed that two localized generation depths determine the complex propagation constant

```math
\gamma(\omega)
=\frac{\sqrt{v^2+4iD\omega}-v}{2D},
```

and therefore determine `v` and `D` algebraically.

The real graded-detector question is harder:

> **If `v(z)` and `D(z)` vary with depth, can a monotonic wavelength-to-generation-depth map recover them locally rather than merely fitting a few global modes?**

The answer is yes in a controlled slowly varying limit.

---

# 2. Exact Riccati form of the first-passage equation

Start from the recombination-free backward equation

```math
\boxed{
D(z)u''(z)+v(z)u'(z)-s u(z)=0.
}
\tag{1}
```

Define the exact local complex logarithmic slope

```math
\boxed{
\gamma(z,s)
=\frac{u'(z,s)}{u(z,s)}.
}
\tag{2}
```

Then

```math
u''=(\gamma'+\gamma^2)u,
```

so (1) becomes the exact Riccati equation

```math
\boxed{
D(\gamma'+\gamma^2)+v\gamma-s=0.
}
\tag{3}
```

No WKB approximation has yet been made.

---

# 3. Local algebraic propagation law

If `v(z)` and `D(z)` vary slowly over the complex propagation length, neglect `gamma'` at leading order.

Then

```math
D\gamma_0^2+v\gamma_0-s=0,
```

with physical branch

```math
\boxed{
\gamma_0(z,s)
=
\frac{
\sqrt{v(z)^2+4D(z)s}-v(z)
}{2D(z)}.
}
\tag{4}
```

Thus each depth behaves locally like the exact uniform drift-diffusion problem.

At RF frequency,

```math
s=i\omega.
```

---

# 4. First gradient correction

Write

```math
\gamma=\gamma_0+\gamma_1+\cdots.
```

Insert into (3) and retain first order in slow spatial variation:

```math
D\gamma_0'
+
(v+2D\gamma_0)\gamma_1
\simeq0.
```

Therefore

```math
\boxed{
\gamma_1
\simeq
-\frac{D\gamma_0'}
{v+2D\gamma_0}.
}
\tag{5}
```

Differentiate the local algebraic equation

```math
D\gamma_0^2+v\gamma_0-s=0
```

to obtain

```math
\gamma_0'
=-\frac{
D'\gamma_0^2+v'\gamma_0
}{v+2D\gamma_0}.
```

Hence

```math
\boxed{
\gamma_1
\simeq
\frac{
D(D'\gamma_0^2+v'\gamma_0)
}{(v+2D\gamma_0)^2}.
}
\tag{6}
```

A natural local control parameter is therefore

```math
\boxed{
\epsilon_{\rm WKB}
\equiv
\left|
\frac{\gamma_1}{\gamma_0}
\right|
=
\left|
\frac{
D(D'\gamma_0+v')
}{(v+2D\gamma_0)^2}
\right|.
}
\tag{7}
```

When

```math
\epsilon_{\rm WKB}\ll1,
```

the uniform inversion may be applied locally with controlled error.

---

# 5. Transparent low-frequency interpretation

At small `s`,

```math
\gamma_0
=\frac{s}{v}
-\frac{Ds^2}{v^3}
+O(s^3).
```

To leading order,

```math
\frac{\gamma_1}{\gamma_0}
\simeq
\frac{Dv'}{v^2}.
```

Thus one especially simple slow-variation condition is

```math
\boxed{
\frac{D}{v}
\left|\frac{d\ln v}{dz}\right|
\ll1.
}
\tag{8}
```

The length

```math
\ell_D=D/v
```

is the drift-diffusion length scale. Equation (8) says that the drift velocity should not change appreciably over that local scale.

---

# 6. Spectral depth encoding

Now introduce the optical part of the gedanken experiment.

Assume a monotonic graded absorber for which each wavelength generates carriers narrowly around a known depth

```math
z_g(\lambda).
```

In the ideal localization limit,

```math
p_\lambda(z)\to\delta[z-z_g(\lambda)].
```

Let the measured complex detector response be

```math
H(\lambda,\omega)
=G(\omega)u[z_g(\lambda),i\omega],
```

where `G(omega)` is any wavelength-independent complex measurement chain.

Differentiate with respect to wavelength:

```math
\frac{\partial}{\partial\lambda}
\ln H
=
\frac{u'}{u}
\frac{dz_g}{d\lambda}.
```

The common chain disappears because it has no wavelength dependence.

Therefore

```math
\boxed{
\gamma_{\rm meas}[z_g(\lambda),\omega]
=
\frac{
\partial_\lambda\ln H(\lambda,\omega)
}{dz_g/d\lambda}.
}
\tag{9}
```

This is the central spectral-derivative result.

A **complex derivative with respect to wavelength becomes a local complex spatial propagation constant.**

---

# 7. Direct local recovery of drift and diffusion

Write

```math
\gamma_{\rm meas}=a+ib.
```

When the WKB/local-uniform approximation is valid, apply the exact algebraic inversion point by point:

```math
\boxed{
D(z)
\simeq
\frac{\omega a}
{b(a^2+b^2)}
}
\tag{10}
```

and

```math
\boxed{
v(z)
\simeq
\frac{
\omega(b^2-a^2)
}{b(a^2+b^2)}.
}
\tag{11}
```

The leading asymptotic bias is controlled by `epsilon_WKB`, Eq. (7), plus the finite width of the optical generation kernel.

This is much stronger than a generic multi-parameter fit:

> **In the sharp-generation / slowly varying limit, the local complex spectral slope determines the local drift velocity and diffusion coefficient algebraically.**

---

# 8. Graded-gap form

For an ideal sharp absorption coordinate set by the local gap,

```math
E_g[z_g(\lambda)]
=\frac{hc}{\lambda}.
```

Differentiate:

```math
E_g'(z_g)
\frac{dz_g}{d\lambda}
=-\frac{hc}{\lambda^2}.
```

Hence

```math
\boxed{
\frac{dz_g}{d\lambda}
=-\frac{hc}
{\lambda^2 E_g'(z_g)}.
}
\tag{12}
```

Insert into (9):

```math
\boxed{
\gamma_{\rm meas}
=
-\frac{
\lambda^2 E_g'(z_g)
}{hc}
\frac{\partial}{\partial\lambda}
\ln H(\lambda,\omega).
}
\tag{13}
```

For a compositionally graded semiconductor,

```math
E_g'(z)
=\frac{dE_g}{dx}\frac{dx}{dz}.
```

Thus a known composition profile converts a measured complex spectral derivative directly into a local transport propagation constant.

---

# 9. Immediate large prediction for graded photodetectors

Equations (10)-(13) predict that a graded detector can, in principle, reveal **both** local drift and diffusion using only wavelength-dependent complex RF response, provided

```text
the wavelength-to-depth map is sufficiently localized,
transport varies slowly on D/v,
the measurement chain is common across wavelength,
and recombination/boundary corrections are controlled.
```

This predicts something much more specific than "wavelength changes detector bandwidth":

> **The real and imaginary parts of the local complex spectral slope must satisfy the drift-diffusion closure relation (6) of the uniform theorem and reconstruct the same physical `v(z),D(z)` across RF frequency.**

That is directly falsifiable.

---

# 10. RF-frequency collapse test

For every wavelength/depth, define

```math
(a_\omega,b_\omega)
=\operatorname{Re/Im}\gamma_{\rm meas}(z,\omega).
```

Compute

```math
D_\omega(z)
=
\frac{\omega a_\omega}
{b_\omega(a_\omega^2+b_\omega^2)},
```

```math
v_\omega(z)
=
\frac{
\omega(b_\omega^2-a_\omega^2)
}{b_\omega(a_\omega^2+b_\omega^2)}.
```

The local drift-diffusion hypothesis predicts

```math
\boxed{
D_\omega(z)\approx D(z),
\qquad
v_\omega(z)\approx v(z)
}
\tag{14}
```

for all RF frequencies inside the model's validity range.

A systematic failure to collapse with frequency diagnoses nonlocal/high-field transport, recombination conditioning, finite generation-width effects, or breakdown of the slowly varying approximation.

---

# 11. Why the translated-feature experiment remains important

Equation (9) assumes that wavelength itself provides a sufficiently narrow and known generation coordinate.

Real optical kernels are broad.

The translation-response theorem gives an independent way to test this assumption:

```text
translated weak feature
-> relocation slope
-> local generation PDF in deterministic limit
```

Therefore the two gedanken experiments close a logical loop:

```text
spectral derivative uses the optical depth map to infer transport

translated perturbation independently tests the optical depth map
and the locality of the transport response.
```

This is far more falsifiable than fitting one flexible forward model to one spectral dataset.

---

# 12. Numerical asymptotic check

The regression

`numerics/slowly_varying_drift_diffusion_wkb.py`

uses explicit smooth profiles

```text
v(z)=1.5[1+0.15 sin(pi z)]
D(z)=0.05[1+0.10 cos(pi z)]
omega=3
```

and integrates the exact Riccati equation along the slowly varying branch.

Over the interior stress region, the current numerical check gives approximately

```text
leading local root gamma0:
median relative error ~0.7%
maximum ~1.4%

first-corrected gamma0+gamma1:
median relative error ~0.1%
maximum ~0.13%.
```

This is not a universal accuracy claim. It is a regression showing that the asymptotic correction behaves as derived in a nontrivial variable-coefficient example.

---

# 13. Strong falsifiable predictions from this theorem

### P1 — complex spectral derivative closure

The measured quantity in Eq. (13) must lie on a local drift-diffusion branch parameterized by positive `v,D`.

### P2 — simultaneous local `v` and `D`

The same complex spectral derivative predicts both through Eqs. (10)-(11).

### P3 — frequency collapse

Independent RF frequencies must reconstruct the same local `v(z),D(z)` where WKB and first-passage assumptions hold.

### P4 — predictable breakdown near sharp transport structure

The local inversion must fail when `epsilon_WKB` approaches unity; the leading correction is explicitly Eq. (6), so the direction and scale of failure are predicted rather than arbitrary.

### P5 — magnitude is indispensable

Because diffusion enters `Re gamma` at leading `omega^2` order while phase remains close to `omega/v`, phase-only reconstruction must systematically lose diffusion information before full complex reconstruction does.

---

# 14. Next theoretical step

The largest remaining gap is **finite optical generation width**.

Instead of

```math
p_\lambda(z)=\delta[z-z_g(\lambda)],
```

a real detector measures

```math
H(\lambda,\omega)
=\int p_\lambda(z)u(z,i\omega)dz.
```

The next derivation should obtain a controlled expansion in the generation-depth variance and determine the bias it causes in the local spectral estimate (9)-(11).

That will give a quantitative spatial-resolution criterion before any HgCdTe-specific parameter substitution.
