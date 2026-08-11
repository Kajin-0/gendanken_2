# Reflecting-Boundary Timing Curvature — An Exact Confounder and a New Null

**Date:** 2026-08-10  
**Status:** exact low-frequency result for uniform 1-D drift-diffusion with one reflecting upstream boundary and one absorbing collector; derived after correcting the first HgCdTe three-color interpretation

## 1. Why this theorem became necessary

The first HgCdTe three-color worked example predicted an approximately

```text
0.12 degree phase closure at 100 MHz
0.58 degree at 500 MHz
~1 degree at 1 GHz.
```

That calculation used a finite slab with a **reflecting optical entrance**.

The comparison reference used an infinite/exponential homogeneous propagation law.

A boundary-matched recalculation showed that almost all of the low-RF phase curvature was already present in a **perfectly homogeneous finite slab with the same reflecting entrance**.

Therefore the old interpretation

> large three-color phase closure = bulk transport-gradient signature

is **invalidated** for that geometry.

The finite boundary is not merely a nuisance, however.

Its contribution has an exact analytic form and can be tested separately.

---

## 2. Uniform finite-slab mean first-passage problem

Take

```text
z=0 -> reflecting upstream entrance
z=L -> absorbing collector
```

with uniform downstream drift

```math
w>0
```

and diffusion

```math
D>0.
```

Let

```math
m(z)=E[T|X_0=z]
```

be mean time to the collector.

The backward equation is

```math
\boxed{
D m''(z)+w m'(z)=-1.
}
\tag{1}
```

Boundary conditions are

```math
\boxed{m'(0)=0,}
```

```math
\boxed{m(L)=0.}
```

---

## 3. Exact mean transit time

Define the boundary diffusion length

```math
\boxed{
\ell_D=\frac{D}{w}.
}
\tag{2}
```

Solving Eq. (1) gives

```math
\boxed{
m(z)
=
\frac{L-z}{w}
-
\frac{D}{w^2}
\left[
e^{-z/\ell_D}
-e^{-L/\ell_D}
\right].
}
\tag{3}
```

The first term is the familiar linear bulk drift time.

The second is an exponentially localized **reflecting-boundary correction**.

Therefore even perfectly uniform transport is not spatially affine when the source distribution samples the upstream boundary layer.

---

## 4. Exact three-point mean-time curvature

Take three point-generation coordinates

```math
z_1=z_0-h,
\qquad
z_2=z_0,
\qquad
z_3=z_0+h.
```

Define the same discrete timing curvature used by the three-color theorem:

```math
\boxed{
C_1
=2m(z_0)-m(z_0-h)-m(z_0+h).
}
\tag{4}
```

The linear bulk term in Eq. (3) cancels exactly.

So does the constant collector term.

The result is

```math
\boxed{
C_1^{\rm boundary}
=
\frac{2D}{w^2}
\,e^{-z_0/\ell_D}
\left[
\cosh\left(\frac{h}{\ell_D}\right)-1
\right].
}
\tag{5}
```

This is positive for `h>0`.

Thus a reflecting boundary necessarily produces low-RF three-color phase curvature even with spatially constant `D,w`.

---

## 5. Low-RF complex closure

For any timing distribution,

```math
\mathcal L(\omega)
=2\ln H_2-\ln H_1-\ln H_3
=-i\omega C_1+O(\omega^2).
```

Therefore the finite-boundary prediction is

```math
\boxed{
\Im\mathcal L_{boundary}
=
-\omega
\frac{2D}{w^2}
\,e^{-z_0w/D}
\left[
\cosh\left(\frac{hw}{D}\right)-1
\right]
+O(\omega^3).
}
\tag{6}
```

The boundary is therefore another source of an

```text
O(omega) phase closure.
```

This corrects the earlier overly strong statement that an `O(omega)` phase residual uniquely isolates bulk transport inhomogeneity from optical shape evolution.

The correct statement is:

> **mean-centered optical shape evolution begins at higher RF order, but finite boundaries and bulk mean-time inhomogeneity can both generate linear-in-RF phase curvature.**

They must be separated by spatial dependence or matched modeling.

---

## 6. Rigid finite-width generation kernel

Let one fixed normalized generation shape

```math
g(u)
```

be translated to center `z_g`.

Average Eq. (3) over

```math
z=z_g+u.
```

The boundary factor becomes

```math
\langle e^{-z/\ell_D}\rangle
=
 e^{-z_g/\ell_D}
\underbrace{
\int g(u)e^{-u/\ell_D}du
}_{M_g(-1/\ell_D)}.
```

Therefore for three equally spaced translated copies,

```math
\boxed{
C_{1,g}^{\rm boundary}
=
M_g(-1/\ell_D)
\frac{2D}{w^2}
\,e^{-z_0/\ell_D}
\left[
\cosh(h/\ell_D)-1
\right].
}
\tag{7}
```

Finite source width changes only one fixed multiplicative factor if the shape translates rigidly.

The exponential center-depth dependence survives exactly.

---

## 7. Boundary spectroscopy from two triplets

Take two equal-spacing triplets with the same `h` and same translated generation shape, but central coordinates separated by

```math
\Delta z.
```

Equation (7) gives

```math
\boxed{
\frac{
C_1(z_0+\Delta z)
}{
C_1(z_0)
}
=
 e^{-\Delta z/\ell_D}.
}
\tag{8}
```

Thus

```math
\boxed{
\ell_D
=
-rac{\Delta z}
{\ln[C_1(z_0+\Delta z)/C_1(z_0)]}.
}
\tag{9}
```

A finite-boundary confounder therefore has a **distinctive exponential spatial signature**.

Rather than merely avoiding it, one can test for it and infer the boundary diffusion length

```math
D/w.
```

---

## 8. Small-spacing limit

For

```math
h\ll\ell_D,
```

```math
\cosh(h/\ell_D)-1
\simeq
\frac{h^2}{2\ell_D^2}.
```

Equation (5) reduces to

```math
\boxed{
C_1^{\rm boundary}
\simeq
\frac{h^2}{D}
 e^{-z_0/\ell_D}.
}
\tag{10}
```

This shows directly that the three-point curvature is the local second derivative of the exponential boundary layer.

---

## 9. A quantitative boundary-negligibility criterion

Suppose the allowed mean-time-curvature contamination is

```math
\epsilon_T.
```

For point generation, Eq. (5) requires

```math
\frac{2D}{w^2}
 e^{-z_0/\ell_D}
[\cosh(h/\ell_D)-1]
<\epsilon_T.
```

Solving for central depth,

```math
\boxed{
z_0
>
\ell_D
\ln
\left[
\frac{
2D[\cosh(h/\ell_D)-1]
}{
w^2\epsilon_T
}
\right].
}
\tag{11}
```

when the logarithm is positive.

For finite kernels, include the known factor

```math
M_g(-1/\ell_D).
```

This is a concrete design rule for deciding whether an 'interior' spectral triplet is actually far enough from the reflecting entrance.

---

## 10. Correction to the first HgCdTe worked example

For the explicit `7.6 um`, `x=0.55 -> 0.32` profile used in the first material example,

```text
D ~0.02327 m^2/s
matched homogeneous drift ~3.45e4 m/s.
```

Hence

```math
\boxed{
\ell_D=D/w\approx0.67\ \mu m.
}
```

The real generation kernels centered at mean depths `2,4,6 um` are broad enough that the shallow kernel retains significant weight in this entrance boundary layer.

The direct moment calculation gives approximately

```text
graded finite slab C1 ~3.42 ps
homogeneous finite slab C1 ~3.46 ps.
```

Thus almost the entire low-RF three-color phase curvature previously attributed to the modest drift gradient is reproduced by the reflecting boundary.

The **gradient-only excess** is only about

```text
-0.04 ps
```

in mean-time curvature for this triplet.

---

## 11. Corrected RF comparison

Using the same real HgCdTe optical kernels and the same finite reflecting/absorbing boundaries:

| RF | Graded finite slab | Homogeneous boundary-matched slab | Gradient-only excess |
|---:|---:|---:|---:|
| `100 MHz` | `-0.1232 deg` | `-0.1246 deg` | `+0.0014 deg` |
| `500 MHz` | `-0.5833 deg` | `-0.5930 deg` | `+0.0097 deg` |
| `1 GHz` | `-0.9855 deg` | `-1.0255 deg` | `+0.0400 deg` |

Therefore the earlier statement that the `~0.1-1 degree` phase closure was dominantly a bulk-gradient signal is **SUPERSEDED / INVALIDATED**.

The full phase closure itself was numerically real; its interpretation was wrong.

---

## 12. Scientific consequence

This correction strengthens the theoretical hierarchy.

A three-color closure failure should now be classified in order:

```text
1. optical kernel shape/calibration
2. finite boundary layers
3. bulk spatial transport inhomogeneity
4. hidden-state / non-regenerative transport
5. more complex alternatives.
```

At low RF:

```text
mean-centered optical shape evolution
-> no O(omega) phase term in homogeneous interior propagation

reflecting boundary
-> O(omega) phase with exponential depth decay ~exp(-z/ell_D)

bulk mean-time curvature
-> O(omega) phase with its own spatial dependence.
```

The **depth dependence**, not RF order alone, separates boundary from bulk transport.

---

## 13. A new falsifiable use of the boundary

The boundary is not just an artifact.

Uniform drift-diffusion predicts that its low-RF timing curvature decays exponentially with internal source depth on exactly the scale

```math
\boxed{\ell_D=D/w.}
```

So a sequence of equally spaced three-color triplets moved deeper into the absorber should satisfy Eq. (8).

Failure of that exponential decay would falsify the simplest homogeneous reflecting-boundary drift-diffusion model even before bulk transport is reconstructed.

This is another simple gedanken experiment created by the correction itself.

---

## 14. Numerical regression

`numerics/reflecting_boundary_timing_curvature.py`

verifies the exact point-source formula Eq. (5), the fixed-shape finite-width scaling Eq. (7), and the depth-ratio inversion Eq. (9).

`numerics/hgcdte_three_color_boundary_matched_correction.py`

recomputes the full HgCdTe finite-RF example with the boundary matched between graded and homogeneous transport and verifies the corrected phase scales.

---

## 15. Current status of the material prediction

The initial HgCdTe example remains useful, but the claim is now narrower and more rigorous:

> **A finite reflecting entrance can dominate three-color low-RF phase curvature even when all mean generation depths appear several diffusion lengths away. Any bulk-gradient interpretation requires a boundary-matched control or a demonstrated interior asymptotic regime.**

The next material-level calculation should therefore optimize the internal color triplet for **boundary rejection**, not merely for equal mean-depth spacing.
