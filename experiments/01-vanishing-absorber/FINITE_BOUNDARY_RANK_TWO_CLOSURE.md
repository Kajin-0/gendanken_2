# Finite Boundary as an Exact Rank-Two Spatial Mode

**Date:** 2026-08-10  
**Status:** exact for uniform 1-D second-order transport with a finite reflecting upstream boundary and absorbing collector; connects the boundary correction to the spectral Hankel hierarchy; no novelty claim for linear-system/Hankel mathematics

## 1. Why the three-color law fails near a boundary

In an effectively interior homogeneous region, one admissible scalar first-passage propagation mode gives

```math
H(z)\propto e^{\Gamma z},
```

so equally spaced internal source coordinates obey the rank-one / three-color closure

```math
H_1^2=H_0H_2.
```

A finite reflecting boundary changes this even when the material transport coefficients remain perfectly uniform.

The reason is exact and simple:

> **the boundary activates the second spatial root of the same second-order transport equation.**

The response is then rank two in spatial step number rather than rank one.

---

## 2. Uniform finite-slab RF equation

For constant conditioned drift `w`, diffusion `D`, and complex frequency `s`,

```math
D u''+wu'-su=0.
```

The two spatial roots are

```math
\boxed{
r_\pm
=\frac{-w\pm\sqrt{w^2+4Ds}}{2D}.
}
\tag{1}
```

Thus the general solution is

```math
\boxed{
u(z)=A e^{r_+z}+B e^{r_-z}.
}
\tag{2}
```

In a semi-infinite/interior first-passage problem, regularity or radiation/decay selection removes one branch and leaves one effective exponential.

In a finite slab with reflecting upstream boundary

```math
u'(0)=0,
```

Eq. (2) instead requires

```math
A r_+ + B r_-=0,
```

so generically

```math
\boxed{
B=-A\frac{r_+}{r_-}\ne0.
}
\tag{3}
```

Both spatial modes are present.

---

## 3. Equally spaced source coordinates form a rank-two sequence

Sample the point-source response at equally spaced positions

```math
z_m=z_0+m\Delta z.
```

Then

```math
\begin{aligned}
y_m
&=A e^{r_+z_0}(e^{r_+\Delta z})^m
+B e^{r_-z_0}(e^{r_-\Delta z})^m\\
&=c_+q_+^m+c_-q_-^m.
\end{aligned}
```

Therefore

```math
\boxed{\operatorname{rank}\mathcal H\le2}
\tag{4}
```

for the spatial Hankel matrix

```math
\mathcal H_{ij}=y_{i+j}.
```

The three-color / rank-one determinant need not vanish:

```math
\boxed{
y_0y_2-y_1^2\ne0}
\tag{5}
```

generically.

But every `3x3` Hankel determinant does vanish:

```math
\boxed{
\det
\begin{pmatrix}
y_0&y_1&y_2\\
y_1&y_2&y_3\\
y_2&y_3&y_4
\end{pmatrix}=0.
}
\tag{6}
```

Thus five equally spaced internal source coordinates provide an exact rank-two finite-boundary closure test.

---

## 4. Rigid finite-width generation kernels preserve rank two

Let one fixed generation shape `g(u)` translate through the slab.

For center `z_m`,

```math
Y_m
=\int g(u)u(z_m+u)du.
```

Using Eq. (2),

```math
Y_m
=
A G_+ e^{r_+z_m}
+B G_- e^{r_-z_m},
```

where

```math
G_\pm=\int g(u)e^{r_\pm u}du.
```

The finite optical kernel changes only the two mode amplitudes.

Therefore

```math
\boxed{\operatorname{rank}\mathcal H_Y\le2}
\tag{7}
```

as long as the source shape translates rigidly and remains within the region described by the same boundary-value problem.

So broad fixed optical generation does not destroy the rank-two boundary prediction.

---

## 5. Connection to the low-RF boundary-curvature theorem

The reflecting-boundary mean-time result is

```math
m(z)
=\frac{L-z}{w}
-\frac{D}{w^2}
\left[e^{-zw/D}-e^{-Lw/D}\right].
```

Its nonlinear spatial term decays as

```math
\exp(-z/\ell_D),
\qquad
\ell_D=D/w.
```

That exponential is the low-frequency remnant of the second spatial root.

Thus two apparently different facts are the same boundary physics viewed from two limits:

```text
low RF / timing cumulants
-> exponentially decaying mean-time curvature

finite RF / full complex response
-> second spatial propagation mode and rank-two Hankel structure.
```

---

## 6. A stronger boundary diagnostic than three colors alone

A practical hierarchy becomes

### Three colors

Test rank one:

```math
H_1^2=H_0H_2.
```

If it fails, one scalar interior exponential is insufficient.

### Five colors

Test rank at most two:

```math
\det \mathcal H_3=0.
```

If the five-color rank-two closure passes while rank one fails, a finite boundary is one natural explanation.

### Move the triplet deeper

The low-frequency rank-one failure caused specifically by a reflecting boundary must decay on

```math
\ell_D=D/w.
```

Therefore the combination

```text
rank-1 fail
+
rank-2 pass
+
exponential weakening with depth
```

is a much more specific boundary signature than a single nonzero three-color residual.

---

## 7. Boundary versus hidden internal state

A hidden two-state transport model can also produce rank two.

Therefore rank two by itself does **not** uniquely prove a boundary.

The distinction comes from additional structure.

### Finite reflecting boundary

- second mode is fixed by the same scalar second-order transport equation;
- its amplitude changes predictably with source depth;
- low-RF curvature decays approximately/exactly with the boundary length `D/w` under the uniform model;
- moving farther into the interior suppresses the boundary mode.

### Genuine hidden transport state

- the second observable mode need not decay away from an interface;
- its RF dispersion can introduce its own characteristic scale;
- its spatial recurrence/eigenvalues need not match the two roots of one scalar drift-diffusion equation.

So the Hankel hierarchy supplies **state counting**, while depth/RF dependence supplies mechanism discrimination.

---

## 8. Important normalization caveat

For one scalar mode, DC normalization preserves rank one because the normalized response remains one exponential.

For general rank-two or higher hidden-state propagation, an arbitrary ratio

```math
H_{norm}(z)=N_{RF}(z)/N_{DC}(z)
```

need not retain the finite rank of either numerator or denominator.

Therefore a rigorous finite-rank test should use either

```text
absolute/de-embedded complex RF response per calibrated optical input
```

or reconstruct the RF numerator from the separately measured DC response.

For the simple scalar finite-boundary model treated here, the unnormalized RF spatial field itself is exactly rank two.

---

## 9. Numerical verification

`numerics/boundary_rank_two_hankel_closure.py`

solves the exact two-root finite-slab form and checks both point generation and an asymmetric rigid finite-width generation kernel.

In both cases:

```text
2x2/rank-1 Hankel determinant -> clearly nonzero
3x3/rank-2 Hankel determinant -> numerical zero.
```

The result does not rely on a narrow optical source.

---

## 10. Correction to the HgCdTe three-color interpretation

The first HgCdTe worked example showed a large rank-one/three-color phase closure in a finite slab.

The boundary-matched correction demonstrated that most of that signal comes from the reflecting entrance.

The present theorem explains **why**:

> the finite boundary changes the spatial propagation class from one exponential mode to two.

Therefore the original large closure is not evidence for anomalous bulk transport. It is exactly the sort of response expected when a rank-one interior null is applied to a rank-two finite-boundary problem.

---

## 11. New falsifiable prediction

A very simple finite-boundary gedanken experiment is now available:

> **If a homogeneous scalar second-order detector is probed close enough to a reflecting boundary, three-color rank-one closure may fail, but five-color rank-two Hankel closure must still hold. Moving the same spectral coordinate set deeper should suppress the rank-one failure on the boundary scale `D/w`.**

Failure of the rank-two closure would then require something beyond that simple finite-boundary scalar model.

This makes the boundary a controlled rung of the falsification ladder rather than an uncontrolled nuisance.
