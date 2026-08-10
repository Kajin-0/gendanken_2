# Exact Local Drift–Diffusion Inverse — Arbitrary 1-D Profiles from DC + One Complex RF Field

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** for the stated one-dimensional local backward generator; no WKB or slow-variation assumption; no novelty/priority claim

## 1. The strongest theory result so far

Consider a one-dimensional minority-carrier first-passage model

```math
\boxed{
D(z)u''(z,s)
+v(z)u'(z,s)
-[\kappa(z)+s]u(z,s)=0.
}
\tag{1}
```

Here

```text
D(z)       local diffusion coefficient
v(z)       local drift coefficient of the backward generator
kappa(z)   local loss/recombination rate
s          Laplace frequency
```

and the collecting boundary condition is imposed elsewhere.

The coefficients may vary **arbitrarily rapidly** with depth, provided the required derivatives exist.

The question is:

> **If the complex first-passage response can be resolved as a function of generation depth, can `D(z)`, `v(z)`, and `kappa(z)` be reconstructed exactly?**

Yes.

---

# 2. Exact Riccati identity

Define the local logarithmic spatial slope

```math
\boxed{
\gamma_s(z)
=\frac{\partial}{\partial z}\ln u(z,s)
=\frac{u'(z,s)}{u(z,s)}.
}
\tag{2}
```

Since

```math
\frac{u''}{u}=\gamma_s'+\gamma_s^2,
```

dividing (1) by `u` gives the exact Riccati equation

```math
\boxed{
D(z)[\gamma_s'(z)+\gamma_s(z)^2]
+v(z)\gamma_s(z)
=\kappa(z)+s.
}
\tag{3}
```

No approximation has been made.

---

# 3. Use directly observable DC-normalized fields

At DC define the real spatial log-collection slope

```math
\boxed{
c(z)
\equiv
\gamma_0(z)
=\partial_z\ln u(z,0).
}
\tag{4}
```

At one nonzero RF frequency define the **DC-normalized** transfer

```math
h(z,\omega)
\equiv
\frac{u(z,i\omega)}{u(z,0)}.
```

Its complex spatial logarithmic slope is

```math
\boxed{
r(z,\omega)
\equiv
\partial_z\ln h(z,\omega)
=\gamma_{i\omega}(z)-c(z).
}
\tag{5}
```

Thus

```math
\gamma_{i\omega}=c+r.
```

These are precisely the quantities suggested by a spectral generation-depth coordinate:

```text
DC spectral/spatial slope -> c(z)
complex normalized-RF spectral/spatial slope -> r(z,omega).
```

---

# 4. Subtract the DC and RF equations

The DC Riccati equation is

```math
\boxed{
D(c'+c^2)+vc=\kappa.
}
\tag{6}
```

The RF Riccati equation is

```math
D[(c+r)'+(c+r)^2]
+v(c+r)
=\kappa+i\omega.
\tag{7}
```

Subtract (6):

```math
\boxed{
D Z+v r=i\omega,
}
\tag{8}
```

where

```math
\boxed{
Z(z,\omega)
\equiv
r'+2cr+r^2.
}
\tag{9}
```

This is the key simplification.

The unknown recombination rate cancels completely from the RF-minus-DC relation.

---

# 5. Exact algebraic recovery of D and v

Write

```math
r=r_R+i r_I,
\qquad
Z=Z_R+i Z_I.
```

Equation (8) gives two real equations:

```math
\boxed{
D Z_R+v r_R=0,
}
\tag{10}
```

```math
\boxed{
D Z_I+v r_I=\omega.
}
\tag{11}
```

Define the local identifiability determinant

```math
\boxed{
\Delta(z,\omega)
=Z_R r_I-Z_I r_R.
}
\tag{12}
```

Whenever

```math
\Delta\neq0,
```

the inversion is exact:

```math
\boxed{
D(z)
=-\frac{\omega r_R}{\Delta},
}
\tag{13}
```

```math
\boxed{
v(z)
=\frac{\omega Z_R}{\Delta}.
}
\tag{14}
```

This is a local algebraic inverse for arbitrary spatially varying coefficients.

There is no WKB/local-uniform approximation.

---

# 6. Exact recovery of recombination/loss

Once `D` and `v` are known, return to the DC identity (6):

```math
\boxed{
\kappa(z)
=D(z)[c'(z)+c(z)^2]
+v(z)c(z).
}
\tag{15}
```

Therefore

```math
\boxed{
\{c,c',r,r'\}
\quad\Longrightarrow\quad
\{D,v,\kappa\}
}
\tag{16}
```

point by point wherever the determinant is nonzero.

This is the central exact inverse theorem.

---

# 7. The uniform theorem is a special case

For uniform coefficients in an effectively unbounded upstream region,

```math
c'=0,
\qquad
r'=0.
```

Without recombination,

```math
c=0,
```

so

```math
Z=r^2.
```

Equation (8) becomes

```math
Dr^2+vr=i\omega,
```

which is exactly the earlier uniform complex-propagation theorem.

Thus

`DRIFT_DIFFUSION_COMPLEX_PROPAGATION_THEOREM.md`

is not a separate mathematical mechanism. It is the constant-coefficient limit of the exact local inverse.

---

# 8. Why the earlier WKB theory remains useful

The WKB approximation is no longer needed **in principle**.

However, the exact inverse requires spatial derivatives

```math
c',\qquad r'.
```

Differentiating noisy measurements can be expensive.

The WKB/local-uniform approximation replaces derivative information by the assumption

```math
|\gamma'|\ll|\gamma|^2+\cdots
```

and therefore trades exactness for noise robustness.

The two approaches now have a clean interpretation:

```text
exact local inverse
-> unbiased in the ideal 1-D model
-> requires first and second spatial derivatives of log response

WKB/local-uniform inverse
-> fewer derivatives / lower noise sensitivity
-> controlled spatial-gradient bias.
```

This sets up a rigorous bias–variance comparison rather than choosing one approach heuristically.

---

# 9. Spectral implementation

Suppose a monotonic optical encoder maps wavelength to a calibrated generation coordinate

```math
z=z_g(\lambda).
```

In the ideal localized-generation limit,

```math
u_0(\lambda)
\propto
u[z_g(\lambda),0],
```

```math
H_{\rm norm}(\lambda,\omega)
\propto
\frac{u[z_g(\lambda),i\omega]}
{u[z_g(\lambda),0]}.
```

Then

```math
\boxed{
c(z_g)
=
\frac{
\partial_\lambda\ln I_{\rm DC}
}{dz_g/d\lambda},
}
\tag{17}
```

and

```math
\boxed{
r(z_g,\omega)
=
\frac{
\partial_\lambda\ln H_{\rm norm}
}{dz_g/d\lambda}.
}
\tag{18}
```

Their spatial derivatives follow by another calibrated derivative with respect to `z_g`.

Thus the ideal spectral prediction is remarkable:

> **DC spectral response plus one complex RF spectral response can, in principle, determine arbitrary depth-dependent `D(z)`, `v(z)`, and `kappa(z)` exactly in the stated 1-D local first-passage model.**

Additional RF frequencies are then pure model tests.

---

# 10. Exact identifiability condition

The determinant

```math
\Delta
=\operatorname{Re}Z\operatorname{Im}r
-\operatorname{Im}Z\operatorname{Re}r
```

has a direct meaning.

The two complex vectors

```math
Z
\quad\text{and}\quad
r
```

must not be collinear in the complex plane.

If

```math
\boxed{\Delta=0,}
\tag{19}
```

then one RF frequency cannot distinguish the local drift and diffusion coefficients through Eq. (8).

This is the exact local structural-identifiability boundary.

Near

```math
|\Delta|\ll1,
```

the inverse is noise amplified even though it remains formally unique.

Thus the determinant is the natural local experimental-conditioning diagnostic.

---

# 11. Physical interpretation of the determinant

Diffusion and drift affect the complex response differently:

```text
D multiplies the curvature/log-slope combination Z
v multiplies the first log-slope r.
```

If those two response directions become complex-collinear, their effects are indistinguishable at that RF frequency.

In the uniform limit this reduces to the familiar need for a nonzero real part of the complex propagation constant: phase alone cannot identify diffusion.

So the exact theorem generalizes the earlier statement

> magnitude contains essential diffusion information

into an arbitrary-profile condition.

---

# 12. Numerical falsification stress

The regression

`numerics/exact_local_drift_diffusion_inverse.py`

uses strongly nonuniform profiles

```text
v(z)=1.5[1+0.25 sin(2 pi z)+0.08 sin(6 pi z)]
D(z)=0.06[1+0.20 cos(3 pi z)]
kappa(z)=0.50[1+0.30 sin(4 pi z)]
```

with a reflecting entrance and absorbing collecting boundary.

The full DC and complex RF boundary-value problems are solved numerically at

```text
omega = 5.
```

The exact inversion then recovers the original profiles over the tested interior with maximum relative errors at approximately machine precision (`~1e-14`).

The profiles vary far too rapidly for this result to be explained as a slow-variation approximation.

---

# 13. Strong falsifiable predictions

The theorem generates unusually direct tests.

### P1 — one-frequency local closure

At every depth and one chosen RF frequency,

```math
D Z+v r=i\omega
```

must hold with **real positive** `D` and physically admissible `v`.

### P2 — recombination closure

The independently reconstructed DC field must satisfy

```math
\kappa=D(c'+c^2)+vc\ge0
```

for a pure loss/recombination model.

### P3 — RF-frequency invariance

Perform the exact inversion at multiple frequencies.

The reconstructed

```math
D(z),\quad v(z),\quad\kappa(z)
```

must be independent of `omega`.

Frequency dependence directly falsifies the local Markov drift-diffusion generator or reveals unmodeled electrical/optical systematics.

### P4 — determinant failure predicts loss of recoverability

Where

```math
|\Delta|\to0,
```

the reconstruction must become noise sensitive.

This can be predicted from the measured response itself.

### P5 — extra frequencies are predictions

One DC field plus one complex RF field determines the model coefficients.

Every additional RF field is overdetermined.

There is therefore no need to fit a separate `D,v,tau` at each frequency.

---

# 14. Relation to the translated-feature theorem

The exact local inverse assumes the generation-depth coordinate is already known sufficiently well to form spatial derivatives.

The translated internal perturbation theorem provides an independent witness:

```text
translated feature magnitude
-> tests/maps generation density

translated feature phase structure
-> tests local deterministic/path assumptions

exact local DC+RF inverse
-> reconstructs stochastic drift-diffusion coefficients.
```

These are complementary rather than competing experiments.

A paper can therefore progress from the minimal mathematically ideal coordinate to increasingly physical validation without changing its logical core.

---

# 15. Important model boundary

Equation (1) is the backward generator assumed here.

If a physical model with spatially varying diffusivity uses a different stochastic convention or effective drift, the recovered `v(z)` is the drift coefficient appearing in that backward generator.

Mapping it to a microscopic mobility/electric-field law is a **separate physical interpretation step**.

Likewise, nonlocal hot-carrier transport, trapping with internal states, memory kernels, ballistic propagation, carrier-carrier interaction, or multidimensional current flow can violate the local second-order generator.

Those are not nuisances to hide.

They are precisely what the RF-frequency closure tests are capable of falsifying.

---

# 16. Consequence for the theory program

This result supersedes the idea that slowly varying transport is required for local reconstruction.

The strongest hierarchy is now

```text
exact arbitrary-profile inverse
-> highest information / derivative sensitive

local-uniform WKB inverse
-> lower derivative order / controlled bias

finite-difference two-depth experiment
-> simplest laboratory test / explicit bias-variance tradeoff.
```

The next theoretical problem is therefore clear:

> **What is the optimal amount of spatial/spectral differentiation in noisy data?**

The exact inverse establishes what is structurally possible.

The Fisher and central-difference calculations should now establish the fundamental resolution/noise tradeoff between exact high-derivative reconstruction and robust local averaging.
