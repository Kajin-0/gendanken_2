# Exact Complex Propagation Inversion for 1-D Drift-Diffusion

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** for constant-coefficient 1-D downstream drift-diffusion with an absorbing collector and effectively remote upstream boundary; no novelty/priority claim

## 1. Second gedanken experiment

Consider a uniform one-dimensional semiconductor region.

A minority carrier is generated at a known point `x<L` and undergoes

```text
constant downstream drift velocity v > 0
constant diffusion coefficient D > 0
```

until it first reaches the collecting boundary `L`.

Ignore recombination for the first theorem.

Let

```math
U(x,s)=\mathbb E_x[e^{-s\tau_L}]
```

be the Laplace transform of the first-passage time `tau_L`.

The backward equation is

```math
\boxed{
D U''+vU'-sU=0,
\qquad
U(L,s)=1.
}
\tag{1}
```

Taking the upstream boundary sufficiently far away selects the decaying solution.

---

# 2. Exact complex spatial propagation constant

The characteristic equation is

```math
D r^2+vr-s=0.
```

Choose the root that gives the physical bounded solution for `x<L`:

```math
\boxed{
\gamma(s)
=\frac{\sqrt{v^2+4Ds}-v}{2D}.
}
\tag{2}
```

Then

```math
\boxed{
U(x,s)
=\exp[-\gamma(s)(L-x)].
}
\tag{3}
```

At RF angular frequency `omega`, set

```math
s=i\omega.
```

Therefore

```math
\boxed{
\gamma(\omega)
=\frac{\sqrt{v^2+4iD\omega}-v}{2D}.
}
\tag{4}
```

The real part controls frequency-dependent attenuation with propagation distance; the imaginary part controls transit phase.

---

# 3. Two generation depths determine gamma without electronics calibration

Generate carriers at two known depths `x_1` and `x_2` in the same device.

Let their measured carrier-transport transfer functions be

```math
H_1(\omega)=G(\omega)U(x_1,i\omega),
```

```math
H_2(\omega)=G(\omega)U(x_2,i\omega),
```

where `G(omega)` is any common wavelength/depth-independent complex electronics/optical transfer factor.

Take the ratio:

```math
\frac{H_2}{H_1}
=
\exp[\gamma(\omega)(x_2-x_1)].
```

Hence, after continuous phase unwrapping,

```math
\boxed{
\gamma(\omega)
=
\frac{
\ln H_2(\omega)-\ln H_1(\omega)
}{x_2-x_1}.
}
\tag{5}
```

The common chain `G(omega)` cancels exactly.

This is the simplest possible complex spatial transport measurement.

---

# 4. Exact algebraic recovery of v and D

Write

```math
\gamma=a+ib,
\qquad a>0,\ b>0.
```

Because `gamma` obeys

```math
\boxed{
D\gamma^2+v\gamma=i\omega,
}
\tag{6}
```

separate real and imaginary parts:

```math
D(a^2-b^2)+va=0,
\tag{7}
```

```math
2Dab+vb=\omega.
\tag{8}
```

Solving gives

```math
\boxed{
D
=
\frac{\omega a}
{b(a^2+b^2)}
}
\tag{9}
```

and

```math
\boxed{
v
=
\frac{\omega(b^2-a^2)}
{b(a^2+b^2)}.
}
\tag{10}
```

Thus **one nonzero RF frequency and two localized generation depths determine both drift velocity and diffusion coefficient exactly in this model.**

No time-domain transient fit is required.

---

# 5. Why full complex response matters

Define

```math
\eta
=\frac{D\omega}{v^2}.
```

Then

```math
\gamma
=\frac{v}{2D}
\left[
\sqrt{1+4i\eta}-1
\right].
```

For `eta << 1`, expand:

```math
\boxed{
\gamma
=
\frac{i\omega}{v}
+
\frac{D\omega^2}{v^3}
-
\frac{2iD^2\omega^3}{v^5}
-
\frac{5D^3\omega^4}{v^7}
+\cdots.
}
\tag{11}
```

Therefore

```math
\boxed{
\operatorname{Im}\gamma
=
\frac{\omega}{v}
\left[
1-2\left(\frac{D\omega}{v^2}\right)^2+\cdots
\right],
}
\tag{12}
```

while

```math
\boxed{
\operatorname{Re}\gamma
=
\frac{D\omega^2}{v^3}
+O(\omega^4).
}
\tag{13}
```

This gives an important physical prediction:

> **Diffusion appears in log-magnitude at lower order than it alters the transit phase.**

A phase-only experiment can therefore look almost perfectly ballistic/deterministic while the complex magnitude already contains measurable diffusion information.

This independently explains why the active project should use full complex RF response rather than phase alone.

---

# 6. Exact closed form for apparent phase slowness

From (4),

```math
\operatorname{Im}\gamma
=
\frac{1}{2D}
\sqrt{
\frac{
\sqrt{v^4+16D^2\omega^2}-v^2
}{2}
}.
```

A phase-only measurement would infer an apparent slowness

```math
q_{\rm phase}(\omega)
=\frac{\operatorname{Im}\gamma}{\omega}.
```

Hence

```math
\boxed{
q_{\rm phase}(\omega)
=
\frac{1}{2D\omega}
\sqrt{
\frac{
\sqrt{v^4+16D^2\omega^2}-v^2
}{2}
}.
}
\tag{14}
```

At low frequency this tends to `1/v`, but it becomes frequency dependent once diffusion broadening is dynamically important.

Thus **frequency collapse of phase-derived velocity is itself a falsifiable deterministic-transport test.**

---

# 7. Spectral version of the gedanken experiment

A physical source need not be mechanically moved if the detector itself maps wavelength to generation depth.

Suppose a monotonic graded-gap absorber generates sufficiently narrow distributions around

```math
z_g(\lambda).
```

Then two wavelengths `lambda_1`, `lambda_2` approximately realize the two-depth experiment:

```math
x_1\simeq z_g(\lambda_1),
\qquad
x_2\simeq z_g(\lambda_2).
```

Equation (5) becomes

```math
\boxed{
\gamma(\omega)
\simeq
\frac{
\ln H(\lambda_2,\omega)
-
\ln H(\lambda_1,\omega)
}{
z_g(\lambda_2)-z_g(\lambda_1)
}.
}
\tag{15}
```

Then (9)-(10) predict `D` and `v`.

This is the simplest theoretical bridge from first-passage transport to wavelength-resolved detector metrology.

Real finite generation width turns the point-source relation into an averaging problem rather than invalidating the underlying propagation law.

---

# 8. A sharp falsification hierarchy

The uniform drift-diffusion model predicts simultaneously:

### P1 — exponential spatial transfer

```math
\ln H(x,\omega)
=\text{common}(\omega)-\gamma(\omega)(L-x).
```

At fixed `omega`, complex log-transfer must be linear in generation depth.

### P2 — depth-pair consistency

Every pair of generation depths must return the same `gamma(omega)`.

### P3 — exact algebraic transport closure

The recovered `a,b` must give positive `D` and physically consistent `v` through (9)-(10).

### P4 — RF consistency

The same physical `v,D` must fit every RF frequency through (4).

### P5 — low-frequency asymmetry

Magnitude attenuation must appear at order `omega^2`, while the first diffusion correction to phase-derived slowness appears at order `omega^2` relative to `1/v`, Eqs. (12)-(13).

Failure patterns distinguish

```text
spatially varying v or D,
recombination,
boundary reflections,
nonlocal/hot-carrier transport,
finite generation-width bias,
or electrical non-common-mode contamination.
```

---

# 9. Extension with recombination

For uniform bulk recombination rate

```math
\kappa=1/\tau,
```

the unnormalized first-passage transform uses

```math
\gamma(\kappa+i\omega)
=\frac{
\sqrt{v^2+4D(\kappa+i\omega)}-v
}{2D}.
```

Conditioning the RF transfer on DC-collected carriers gives the effective complex propagation constant

```math
\boxed{
\Gamma(\omega)
=
\gamma(\kappa+i\omega)-\gamma(\kappa).
}
\tag{16}
```

Now one complex frequency no longer generically determines all three quantities `(v,D,kappa)`.

Multiple RF frequencies or independent lifetime information are required.

This connects directly to the active repository requirement for independent minority-carrier transport calibration.

---

# 10. Relation to the translation-response theorem

The two exact gedanken results complement each other.

### Localized generation / spectral-depth experiment

```text
complex spatial propagation
-> exact v and D in uniform drift-diffusion
```

### Translated weak internal perturbation

```text
position derivative of response
-> local complex sensitivity field
-> deterministic limit separates p(z) and q(z)
```

Together they suggest a strong theory-first paper architecture:

```text
1. exact uniform first-passage propagation law
2. exact inversion of v and D from complex spatial response
3. wavelength as an internal generation-depth coordinate
4. exact translated-perturbation theorem
5. deterministic local reconstruction and sum rules
6. drift-diffusion deviations as falsifiable physics
7. graded HgCdTe as the concrete worked example.
```

---

# 11. Immediate next derivation

The next high-value calculation is to combine these two results in the **slowly varying drift-diffusion** limit.

Starting from

```math
D(z)u''+v(z)u'-i\omega u=0,
```

seek a WKB/local-propagation form

```math
u(z)\sim A(z)
\exp\left[
-\int_z^L\gamma(s,\omega)ds
\right].
```

The central question is whether the measured spatial/spectral complex gradient gives a controlled local estimate of

```math
D(z),\qquad v(z)
```

and what dimensionless parameters bound the error.

That would turn the exact uniform theorem into a genuine local transport-tomography prediction.

Numerical regression:

`numerics/drift_diffusion_complex_propagation_theorem.py`
