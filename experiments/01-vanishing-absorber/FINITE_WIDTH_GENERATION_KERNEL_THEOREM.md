# Finite-Width Generation-Kernel Theorem — Broad Optical Generation Need Not Blur Complex Transport Slope

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** for uniform 1-D complex spatial propagation; slowly varying extension given as controlled expansion; no novelty/priority claim

## 1. The apparent problem

The spectral-derivative theorem was first written in the sharp-generation limit

```math
p_\lambda(z)\to\delta[z-z_g(\lambda)].
```

A real absorber instead generates carriers over a finite depth distribution.

At first sight this seems to imply an unavoidable spatial-resolution penalty.

For uniform transport, that conclusion is too pessimistic.

---

# 2. Uniform complex propagation

In a uniform drift-diffusion region, the localized-generation transfer has the form

```math
u(z,\omega)
=U_0(\omega)e^{\gamma(\omega)z},
```

where the exact propagation constant is

```math
\gamma(\omega)
=\frac{\sqrt{v^2+4iD\omega}-v}{2D}
```

up to an irrelevant collector-dependent multiplicative constant.

Let the wavelength-dependent normalized generation profile be

```math
p_\lambda(z).
```

The measured transport transfer is

```math
H(\lambda,\omega)
=G(\omega)
\int p_\lambda(z)e^{\gamma z}dz.
\tag{1}
```

---

# 3. Exact rigid-translation theorem

Suppose wavelength changes only the **position** of the generation distribution, not its shape:

```math
\boxed{
p_\lambda(z)
=g[z-z_g(\lambda)],
\qquad
\int g(y)dy=1.
}
\tag{2}
```

The kernel `g` may be narrow or broad.

Substitute

```math
y=z-z_g.
```

Then

```math
\begin{aligned}
H
&=G
\int g(y)e^{\gamma(y+z_g)}dy\\
&=G e^{\gamma z_g}
\underbrace{
\int g(y)e^{\gamma y}dy
}_{M_g(\gamma)}.
\end{aligned}
```

Therefore

```math
\boxed{
H(\lambda,\omega)
=G(\omega)M_g[\gamma(\omega)]
 e^{\gamma(\omega)z_g(\lambda)}.
}
\tag{3}
```

Since `G`, `M_g`, and `gamma` do not depend on the translated center,

```math
\boxed{
\frac{\partial}{\partial z_g}
\ln H
=\gamma(\omega).
}
\tag{4}
```

This is exact for **arbitrary generation width** as long as the distribution translates rigidly and is not clipped by a physical boundary.

## Main consequence

> **Finite optical generation width does not by itself bias the complex spatial slope in a uniform transport region.**

The critical optical error is **shape change**, not width alone.

---

# 4. Spectral form

If `z_g=z_g(lambda)`, then

```math
\boxed{
\frac{\partial\ln H}{\partial\lambda}
=\gamma(\omega)
\frac{dz_g}{d\lambda}.
}
\tag{5}
```

Hence

```math
\boxed{
\gamma(\omega)
=
\frac{
\partial_\lambda\ln H
}{dz_g/d\lambda}
}
\tag{6}
```

remains exact even when `g` is broad.

This substantially relaxes the earlier sharp-generation intuition behind spectral transport tomography.

---

# 5. Exact shape-change contamination

Now allow the centered kernel itself to change with wavelength:

```math
p_\lambda(z)
=g_\lambda[z-z_g(\lambda)].
```

Define its complex moment-generating factor

```math
M_\lambda(\gamma)
=\int g_\lambda(y)e^{\gamma y}dy.
```

Equation (1) becomes

```math
H
=G e^{\gamma z_g}M_\lambda(\gamma).
```

Therefore

```math
\boxed{
\frac{\partial\ln H}{\partial\lambda}
=
\gamma\frac{dz_g}{d\lambda}
+
\frac{\partial}{\partial\lambda}
\ln M_\lambda(\gamma).
}
\tag{7}
```

The first term is the desired spatial transport signal.

The second term is the **exact optical-shape contamination** in a uniform medium.

Thus the naive spectral estimate is

```math
\boxed{
\gamma_{\rm naive}
=
\gamma
+
\frac{1}{dz_g/d\lambda}
\partial_\lambda\ln M_\lambda(\gamma).
}
\tag{8}
```

This identifies precisely what optical calibration must control.

---

# 6. Gaussian generation family

For a Gaussian centered kernel with variance `sigma_z^2(lambda)`,

```math
M_\lambda(\gamma)
=\exp\left[
\frac{\gamma^2\sigma_z^2}{2}
\right].
```

Hence

```math
\boxed{
\frac{\partial\ln H}{\partial\lambda}
=
\gamma z_g'
+
\frac{\gamma^2}{2}
\frac{d\sigma_z^2}{d\lambda}.
}
\tag{9}
```

Several important cases follow immediately.

### Constant width

If

```math
\frac{d\sigma_z^2}{d\lambda}=0,
```

then

```math
\boxed{
\partial_\lambda\ln H
=\gamma z_g'
}
```

**exactly, no matter how broad the Gaussian is.**

### Changing width

The full complex bias is known:

```math
\boxed{
\delta\gamma
=
\frac{\gamma^2}{2}
\frac{d\sigma_z^2/d\lambda}
{dz_g/d\lambda}.
}
\tag{10}
```

Thus wavelength-dependent optical broadening can create both apparent phase and magnitude transport structure, but its direction and scale are calculable.

---

# 7. General cumulant interpretation

Let the centered generation kernel have cumulants

```math
\kappa_1=0,
\quad
\kappa_2=\sigma_z^2,
\quad
\kappa_3,
\ldots
```

Then

```math
\ln M_\lambda(\gamma)
=
\sum_{n=2}^{\infty}
\frac{\kappa_n(\lambda)}{n!}
\gamma^n.
```

Equation (7) gives

```math
\boxed{
\frac{\partial\ln H}{\partial\lambda}
=
\gamma z_g'
+
\sum_{n=2}^{\infty}
\frac{\kappa_n'(\lambda)}{n!}
\gamma^n.
}
\tag{11}
```

This is an exact expansion whenever the moment-generating series converges.

It makes the optical/transport separation unusually explicit:

```text
translation of the kernel center -> desired gamma term
change of kernel variance/skewness/etc. -> known higher-power contamination.
```

If the optical generation cumulants are independently modeled or measured, these terms can be propagated rather than absorbed into arbitrary transport parameters.

---

# 8. Slowly varying transport — finite-width bias

When `gamma(z)` varies with depth, the rigid-translation cancellation is no longer exact.

Let a centered generation kernel have mean `mu=z_g`, variance `sigma_z^2`, and small higher moments.

Expand the local transfer `u(z)` about `mu`:

```math
H
=u(\mu)
+
\frac{\sigma_z^2}{2}u''(\mu)
+\cdots.
```

Since

```math
\frac{u'}{u}=\gamma,
```

```math
\frac{u''}{u}
=\gamma'+\gamma^2.
```

Therefore

```math
\boxed{
\ln H
=\ln u(\mu)
+
\frac{\sigma_z^2}{2}
[\gamma'(\mu)+\gamma(\mu)^2]
+
O(\kappa_3,\sigma_z^4).
}
\tag{12}
```

Differentiate with respect to wavelength:

```math
\boxed{
\begin{aligned}
\frac{d\ln H}{d\lambda}
=&\ \gamma\mu'\\
&+\frac{(\sigma_z^2)'}{2}
(\gamma'+\gamma^2)\\
&+\frac{\sigma_z^2\mu'}{2}
(\gamma''+2\gamma\gamma')
+\cdots.
\end{aligned}
}
\tag{13}
```

Thus two different effects are separated:

```text
kernel-shape evolution
and
transport curvature across the finite optical depth distribution.
```

For a rigid kernel with constant variance,

```math
\boxed{
\gamma_{\rm spec}-\gamma
\simeq
\frac{\sigma_z^2}{2}
(\gamma''+2\gamma\gamma').
}
\tag{14}
```

This gives a concrete finite-width validity criterion.

---

# 9. A dimensionless optical-locality criterion

A simple conservative condition is

```math
\boxed{
\sigma_z^2
\left|
\frac{
\gamma''+2\gamma\gamma'
}{\gamma}
\right|
\ll1.
}
\tag{15}
```

Unlike the statement "generation must be narrow," Eq. (15) says something more physical:

> **the generation width matters only relative to spatial variation of the complex transport propagation field.**

A wide kernel can be harmless in a uniform region, while a much narrower kernel can still be biased near an abrupt transport feature.

---

# 10. Strong falsifiable predictions

### P1 — width invariance in a uniform region

Generation profiles of different widths but identical translated shape must give the same complex spatial slope `gamma`.

### P2 — shape-change law

If only the variance changes and the profile is Gaussian, the resulting complex spectral bias must follow Eq. (10), proportional to `gamma^2`.

### P3 — cumulant hierarchy

Variance evolution enters as `gamma^2`, skewness evolution as `gamma^3`, etc., Eq. (11).

### P4 — transport-curvature bias

In a nonuniform region, the first rigid-width correction follows Eq. (14). Its magnitude should grow with both optical variance and transport curvature.

### P5 — optical broadening is not synonymous with lost resolution

If a measured system violates the width-invariance prediction even where independent evidence shows uniform transport and rigid kernel translation, then the assumed generation kernels or common measurement-chain model are wrong.

---

# 11. Why this matters for the paper direction

The theory now has a clearer hierarchy:

```text
uniform drift-diffusion
-> exact gamma and exact v,D inversion

monotonic spectral depth coordinate
-> complex spectral derivative measures gamma

broad but rigid generation kernel
-> no bias at all in uniform transport

changing optical shape
-> exact calculable contamination

slowly varying transport
-> explicit WKB + finite-width corrections

translated internal perturbation
-> independent local witness / falsification test.
```

This is substantially more predictive than treating optical generation width as an arbitrary tomography-resolution penalty.

Numerical regression:

`numerics/generation_kernel_translation_invariance.py`
