# Six-Color Shockley-Ramo Boundary Closure — Uniform Recombination Included

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED / CONDITIONAL** for one-dimensional uniform scalar drift-diffusion with uniform Markov recombination and raw planar terminal current; no novelty claim for recurrence/Hankel mathematics

## 1. Why this extension matters

A finite boundary is one of the most ordinary reasons the one-mode four-color closure can fail.

A boundary introduces a second homogeneous spatial root even when the underlying transport law is still the simplest scalar drift-diffusion equation.

Uniform recombination adds another physical parameter but, importantly, does **not** add another spatial root.

Thus six colors can test the boundary model and recover

```text
D
w
kappa
```

without fitting arbitrary boundary amplitudes.

---

## 2. Uniform raw-current resolvent

For constant

```text
diffusion D > 0
drift w
uniform recombination kappa >= 0,
```

the raw-current backward equation at `s` is

```math
\boxed{
D J''+wJ'-(\kappa+s)J=-g,
}
\tag{1}
```

where `g` is the uniform local Shockley-Ramo current source in the reduced planar model.

Any linear finite-boundary conditions determine only the solution amplitudes.

The general spatial solution is

```math
\boxed{
J(z,s)
=J_p(s)
+A(s)e^{r_+z}
+B(s)e^{r_-z},
}
\tag{2}
```

where the particular solution is depth independent and the two homogeneous roots satisfy

```math
\boxed{
D r^2+w r-(\kappa+s)=0.
}
\tag{3}
```

---

## 3. First differences remove the Ramo particular mode

Sample six equally spaced internal source coordinates

```math
z_m=z_0+mh,
\qquad m=0,\ldots,5.
```

Define

```math
\Delta J_m=J_{m+1}-J_m.
```

The constant `J_p` cancels, leaving

```math
\boxed{
\Delta J_m
=c_+q_+^m+c_-q_-^m,
}
\tag{4}
```

where

```math
q_\pm=e^{r_\pm h}.
```

Therefore the five first differences have spatial Hankel rank at most two.

The exact six-color null is

```math
\boxed{
\det
\begin{pmatrix}
\Delta J_0&\Delta J_1&\Delta J_2\\
\Delta J_1&\Delta J_2&\Delta J_3\\
\Delta J_2&\Delta J_3&\Delta J_4
\end{pmatrix}=0.
}
\tag{5}
```

Four differences identify the second-order recurrence; the fifth is an exact rank-two closure check in noiseless generic data.

---

## 4. Root constraints including recombination

Vieta's formulas applied to Eq. (3) give

```math
\boxed{
r_++r_-=-\frac{w}{D},
}
\tag{6}
```

and

```math
\boxed{
r_+r_-
=-\frac{\kappa+s}{D}.
}
\tag{7}
```

At RF,

```math
s=i\omega,
```

so

```math
\boxed{
r_+r_-
=-\frac{\kappa}{D}
-i\frac{\omega}{D}.
}
\tag{8}
```

This supplies three strong signatures.

### Root sum

```math
\boxed{
r_++r_-
\text{ is real and RF-independent}.}
```

### Real root-product part

```math
\boxed{
\Re(r_+r_-)
=-\kappa/D
\text{ is RF-independent}.}
```

### Imaginary root-product part

```math
\boxed{
\Im(r_+r_-)
=-\omega/D
}
```

is exactly linear in RF with zero intercept.

---

## 5. Direct coefficient recovery

Once the roots are obtained,

```math
\boxed{
D
=-\frac{\omega}{\Im(r_+r_-)},
}
\tag{9}
```

```math
\boxed{
w
=-D\Re(r_++r_-),
}
\tag{10}
```

```math
\boxed{
\kappa
=-D\Re(r_+r_-).
}
\tag{11}
```

The imaginary part of the root sum should vanish within uncertainty.

Every RF frequency must recover the same real `D,w,kappa`.

Thus the boundary amplitudes

```text
A(s)
B(s)
J_p(s)
```

are nuisance quantities that do not have to be modeled to test the transport law.

---

## 6. Relation to the no-recombination boundary theorem

For

```math
\kappa=0,
```

Eq. (8) reduces to

```math
r_+r_-=-i\omega/D,
```

which is the previously derived root-pair closure.

At low RF one root approaches the bulk timing mode while the other approaches the boundary-layer exponent

```math
-w/D.
```

Uniform recombination shifts the product's real part but leaves the root sum unchanged.

---

## 7. Why this remains distinct from a conventional electron-hole pair

A deterministic planar electron-hole pair can also have first-difference rank two.

Its two spatial exponents satisfy instead

```math
r_e+r_h
=i\omega(1/v_e-1/v_h),
```

```math
r_er_h
=\omega^2/(v_ev_h).
```

Thus in that limiting conventional two-carrier case

```text
root sum -> imaginary and linear in RF
root product -> real and quadratic in RF,
```

whereas one scalar finite-boundary drift-diffusion-recombination model predicts

```text
root sum -> real constant
root product -> real constant + imaginary linear RF.
```

The mode count alone is not enough; the **RF root geometry** carries the mechanism test.

More general diffusive/recombining two-carrier models need their own root laws and should not be forced into the deterministic signature.

---

## 8. Broad rigid source kernels

Each exponential spatial mode can be averaged over one rigidly translated source shape.

That changes the mode amplitudes but not

```math
q_\pm
```

or

```math
r_\pm.
```

Thus finite source width does not alter the exact rank-two/root-pair theorem under rigid translation.

Wavelength-dependent source-shape evolution remains a systematic correction.

---

## 9. Numerical regression

`numerics/ramo_six_color_boundary_recombination.py`

constructs arbitrary frequency-dependent boundary amplitudes with known

```text
D=0.13
w=1.55
kappa=0.37.
```

At several RF frequencies it verifies

```text
six-color first-difference Hankel determinant = numerical zero
recovery of both spatial roots
real/RF-independent root sum
root-product real constant
root-product imaginary part linear in omega
recovery of D,w,kappa to numerical precision.
```

The arbitrary boundary amplitudes never enter Eqs. (9)-(11).

---

## 10. Paper-level role

This theorem is the natural next rung after a failed one-mode four-color test.

The logic is

```text
4 colors:
does one first-difference spatial mode suffice?

if no:

6 colors:
do two modes suffice?

if yes:
are those two modes the constrained roots of one scalar finite-boundary DD + recombination equation?
```

A boundary explanation survives only if both the **rank** and **RF root algebra** pass.

This turns a common detector confounder into an overdetermined falsifiable model rather than a flexible nuisance fit.
