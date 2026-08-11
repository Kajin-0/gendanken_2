# Five-Color Boundary Root-Pair Closure — Distinguishing a Finite Boundary from Arbitrary Hidden Rank-Two Transport

**Date:** 2026-08-10  
**Status:** exact for uniform scalar second-order drift-diffusion in a finite slab; five-color spatial rank plus multi-frequency root-pair closure; no novelty claim for recurrence/Hankel mathematics

## 1. Rank two is not yet a mechanism

A reflecting finite boundary promotes the homogeneous scalar response from one spatial exponential to two:

```math
u(z)=A e^{r_+z}+B e^{r_-z}.
```

Therefore three-color/rank-one closure can fail while five-color/rank-two Hankel closure passes.

But a genuine hidden two-state transport model can also have spatial rank two.

So the next question is:

> **Can the two spatial modes themselves distinguish a simple finite boundary from an arbitrary hidden-state model?**

Yes.

The two boundary modes are not free. They are the two roots of one scalar drift-diffusion quadratic.

---

## 2. Exact finite-boundary spatial roots

For constant conditioned drift `w`, diffusion `D`, and Laplace/RF parameter `s`,

```math
D u''+w u'-s u=0.
```

The characteristic equation is

```math
\boxed{
D r^2+w r-s=0.
}
\tag{1}
```

Its roots are

```math
\boxed{
r_\pm
=\frac{-w\pm\sqrt{w^2+4Ds}}{2D}.
}
\tag{2}
```

Vieta's formulas therefore impose

```math
\boxed{
r_++r_-=-\frac{w}{D},
}
\tag{3}
```

and

```math
\boxed{
r_+r_-=-\frac{s}{D}.
}
\tag{4}
```

At RF,

```math
s=i\omega,
```

so

```math
\boxed{
r_+r_-=-\frac{i\omega}{D}.
}
\tag{5}
```

This is much stronger than merely saying that two spatial modes exist.

---

## 3. Five equally spaced colors identify the two spatial multipliers

Sample the de-embedded complex RF numerator at five equally spaced internal source coordinates

```math
z_m=z_0+m\Delta z,
\qquad m=0,1,2,3,4.
```

For rank-two homogeneous propagation,

```math
y_m=c_+q_+^m+c_-q_-^m,
```

with

```math
q_\pm=e^{r_\pm\Delta z}.
```

The sequence obeys the second-order recurrence

```math
\boxed{
y_{m+2}=S y_{m+1}-P y_m,
}
\tag{6}
```

where

```math
S=q_++q_-,
```

```math
P=q_+q_-.
```

Four points determine `S,P` in noiseless generic data. The fifth point is the exact rank-two closure check.

Equivalently,

```math
\boxed{
\det
\begin{pmatrix}
y_0&y_1&y_2\\
y_1&y_2&y_3\\
y_2&y_3&y_4
\end{pmatrix}=0.
}
\tag{7}
```

Once `q_+`, `q_-` are found as the roots of

```math
q^2-Sq+P=0,
```

the spatial exponents are

```math
\boxed{
r_\pm=\frac{1}{\Delta z}\log q_\pm,
}
\tag{8}
```

with logarithm branches followed continuously across RF frequency.

---

## 4. A second exact closure after rank two is established

The recovered roots must satisfy Eqs. (3)-(5).

Therefore define apparent coefficients

```math
\boxed{
D_{root}(\omega)
=-\frac{i\omega}{r_+r_-},
}
\tag{9}
```

and

```math
\boxed{
w_{root}(\omega)
=-D_{root}(\omega)(r_++r_-).
}
\tag{10}
```

For one uniform scalar finite-boundary drift-diffusion model,

```math
\boxed{
D_{root}(\omega)=D\in\mathbb R_{>0},
}
\tag{11}
```

```math
\boxed{
w_{root}(\omega)=w\in\mathbb R,
}
\tag{12}
```

and both are frequency independent.

Thus the complete boundary test has two nested stages:

```text
five colors
-> is spatial rank <=2?

if yes:
recover the two spatial roots
-> do their sum/product satisfy one real scalar DD quadratic across RF?
```

---

## 5. The root-pair signature in words

At every RF frequency a simple scalar finite-boundary drift-diffusion model predicts:

### Root sum

```math
\boxed{r_++r_-\ \text{is purely real and independent of RF}.}
```

### Root product

```math
\boxed{r_+r_-\ \text{is purely imaginary and exactly linear in }\omega.}
```

The slope of the product gives

```math
D.
```

The real root sum then gives

```math
w.
```

No boundary amplitude, optical-source amplitude, or mode weight is needed for these identities once the two spatial roots are resolved.

---

## 6. Why arbitrary hidden rank two generally fails this test

A two-state homogeneous transport model can produce

```math
y_m=c_1q_1^m+c_2q_2^m
```

and therefore satisfy every rank-two Hankel determinant.

But its two exponents need not be roots of

```math
D r^2+w r-i\omega=0
```

for one real, frequency-independent pair `D,w`.

Consequently it can show

```text
complex D_root,
complex w_root,
frequency-dependent D_root or w_root,
nonlinear root product versus omega,
or a root sum with RF-dependent imaginary part.
```

So

```text
rank two
```

and

```text
finite-boundary scalar drift-diffusion
```

are distinct hypotheses.

The latter is much more constrained.

---

## 7. Low-frequency boundary mode behavior

As

```math
s\to0,
```

the roots behave as

```math
r_+
=\frac{s}{w}+O(s^2),
```

```math
r_-
=-\frac{w}{D}-\frac{s}{w}+O(s^2).
```

Thus one mode becomes the slow bulk timing mode while the other tends to the real boundary-layer exponent

```math
\boxed{-w/D=-1/\ell_D.}
```

This is the same boundary length

```math
\ell_D=D/w
```

found independently from the low-RF mean-time-curvature theorem.

The full-RF root-pair analysis and the low-RF exponential boundary law are therefore two measurements of the same `D/w` scale.

That cross-check is itself falsifiable.

---

## 8. Broad rigid optical kernels do not change the recovered roots

For a translated generation shape `g(u)`, each spatial exponential is multiplied by its own fixed transform factor

```math
G_\pm=\int g(u)e^{r_\pm u}du.
```

Therefore

```math
Y_m
=\tilde c_+q_+^m+\tilde c_-q_-^m.
```

The mode amplitudes change, but the multipliers

```math
q_\pm
```

and hence the recovered roots remain the same.

So fixed finite optical width is not a structural problem for the root-pair closure.

Wavelength-dependent source-shape evolution can change the sequence and must be modeled/calibrated.

---

## 9. Important use of raw/de-embedded RF numerator

In a general multistate system, the ratio

```math
H_{norm}(z)=N_{RF}(z)/N_{DC}(z)
```

can have a more complicated rank than either numerator or denominator.

Therefore the five-color root-pair/Hankel test should preferably use

```text
absolute de-embedded complex RF response per calibrated incident optical amplitude,
```

or reconstruct the RF numerator from the separately measured DC response.

The DC-normalized timing response remains valuable for the separate conditioning and cumulant tests.

---

## 10. Minimal finite-boundary gedanken experiment

The experiment can be stated compactly:

> **Use five colors to sample five equally spaced internal generation coordinates. If three-color closure fails but the five-color rank-two closure passes, recover the two spatial propagation roots. Repeat at a second RF frequency. A simple finite reflecting-boundary drift-diffusion model survives only if the root sum stays real and constant and the root product stays purely imaginary and proportional to RF frequency.**

This uses

```text
5 internal coordinates
x
2 RF frequencies
```

and has no free extra boundary-state parameters once `D,w` are inferred.

---

## 11. Numerical regression

`numerics/five_color_boundary_root_pair_closure.py`

constructs exact finite-boundary scalar drift-diffusion sequences at several RF frequencies with arbitrary frequency-dependent mode amplitudes.

It verifies:

```text
five-color rank-two recurrence closure
3x3 Hankel determinant = numerical zero
recovered root sum/product
real frequency-independent D_root
real frequency-independent w_root.
```

The same script constructs an arbitrary hidden rank-two propagation model.

That model still passes the Hankel rank-two test but produces complex and/or frequency-dependent apparent root coefficients, thereby failing the stronger scalar-boundary closure.

---

## 12. Position in the falsification ladder

The spatial hierarchy is now:

```text
3 colors:
rank 1 / one scalar interior mode?

5 colors:
if rank 1 fails, does rank 2 suffice?

2 RF frequencies:
if rank 2 suffices, are its two roots the constrained pair of one scalar finite-boundary DD equation?

if no:
hidden state, spatially varying coefficients, nonlocal transport, optical-shape error, or another model is required.
```

This is a cleaner route than fitting a boundary correction and an arbitrary hidden-state model simultaneously.

---

## 13. Strong conceptual consequence

The finite boundary can now be identified at three independent theoretical levels:

1. **low-RF timing curvature** decays as `exp(-z/ell_D)`;
2. **spatial Hankel rank** rises from one to two;
3. **the two recovered roots** obey one scalar quadratic with real constant `D,w` across RF.

A genuine boundary interpretation should satisfy all three.

That turns a major confounder discovered in the HgCdTe worked example into an unusually overdetermined falsifiable model.
