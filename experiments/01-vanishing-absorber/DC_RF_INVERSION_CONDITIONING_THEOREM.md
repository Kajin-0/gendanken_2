# DC + RF Transport Inversion Conditioning — Exact Root Geometry and Optimal Normalized Frequency

**Date:** 2026-08-11  
**Status:** **DERIVED / CHECKED / CONDITIONAL** for the homogeneous real drift-diffusion-recombination model; addresses the main conditioning gap identified in adversarial review; not a novelty claim for linear error propagation

## 1. Why `Delta != 0` was not enough

The manuscript currently proves structural identifiability from

```math
D\gamma^2+w\gamma=\kappa+s
```

using one DC spatial exponent and one nonzero-RF exponent.

That proof requires the real `2x2` determinant

```math
\Delta
=\Re A\Im B-\Im A\Re B
```

to be nonzero, with

```math
A=g_\omega^2-g_0^2,
\qquad
B=g_\omega-g_0.
```

A skeptical reviewer correctly asks a stronger question:

> **How badly does the inversion amplify noise as the RF root approaches the DC root?**

The determinant has an exact geometric simplification that makes this question transparent.

---

## 2. Use the RF root displacement

Let

```math
g_0=\gamma(0)\in\mathbb R,
```

and write

```math
\delta g
=g_\omega-g_0
=u+iv,
```

with

```math
u=\Re(g_\omega-g_0),
\qquad
v=\Im g_\omega.
```

Then

```math
A
=(g_0+u+iv)^2-g_0^2,
```

```math
B=u+iv.
```

Direct expansion gives

```math
\boxed{
\Delta=-v(u^2+v^2).
}
\tag{1}
```

Thus the inversion singularity has a simple meaning:

```text
the RF propagation root has not moved far enough away from the DC root
in the complex plane.
```

For the physical positive-frequency downstream branch, `v>0`; the singular limit is the small root-displacement limit.

---

## 3. A cleaner physical parameterization

Define

```math
\boxed{
V_*
=\sqrt{w^2+4D\kappa}
=w+2Dg_0.
}
\tag{2}
```

`V_*` is the effective conditioned drift scale appearing after DC killing/recombination is absorbed into the successful-carrier propagation law.

Using Eq. (1), the DC+RF inversion reduces exactly to

```math
\boxed{
D
=\frac{\omega u}
{v(u^2+v^2)},
}
\tag{3}
```

and

```math
\boxed{
V_*
=\frac{\omega(v^2-u^2)}
{v(u^2+v^2)}.
}
\tag{4}
```

The physical drift and recombination rate then follow from the DC root:

```math
\boxed{
w=V_*-2Dg_0,
}
\tag{5}
```

```math
\boxed{
\kappa=V_*g_0-Dg_0^2.
}
\tag{6}
```

This factorization is preferable to treating `(D,w,kappa)` as one opaque nonlinear inversion:

```text
RF displacement -> D and V_*
DC root          -> uncondition V_* into w and kappa.
```

---

## 4. Exact root displacement for uniform drift-diffusion

Since

```math
w^2+4D\kappa=V_*^2,
```

the RF-minus-DC root is

```math
\boxed{
\delta g(i\omega)
=\frac{
\sqrt{V_*^2+4Di\omega}-V_*
}{2D}.
}
\tag{7}
```

For low RF,

```math
u
=\frac{D\omega^2}{V_*^3}
+O(\omega^4),
```

```math
v
=\frac{\omega}{V_*}
-\frac{2D^2\omega^3}{V_*^5}
+O(\omega^5).
```

Therefore

```math
\boxed{
\Delta
\sim
-\frac{\omega^3}{V_*^3}
}
\tag{8}
```

at low RF.

This explains why a merely nonzero determinant can still be a badly conditioned experiment.

---

## 5. Dimensionless root geometry

Define

```math
\boxed{
\chi=\frac{u}{v}
=\frac{\Re\delta g}{\Im\delta g}.
}
\tag{9}
```

For the positive real drift-diffusion branch,

```math
\boxed{0<\chi<1.}
\tag{10}
```

Also define the dimensionless modulation frequency

```math
\boxed{
\xi=\frac{D\omega}{V_*^2}.
}
\tag{11}
```

The exact relation between the directly observable root-shape ratio `chi` and the physical normalized frequency is

```math
\boxed{
\xi
=\frac{\chi(1+\chi^2)}{(1-\chi^2)^2}.
}
\tag{12}
```

At low RF,

```math
\chi\simeq\xi.
```

Thus the small real part of the RF root displacement is precisely the diffusion information that becomes difficult to resolve at low normalized frequency.

---

## 6. Exact local conditioning of `D` and `V_*`

Let the recovered complex displacement `delta g=u+iv` suffer a small Euclidean perturbation in the `(u,v)` plane.

For

```math
r=|\delta g|=\sqrt{u^2+v^2},
```

define local relative condition numbers

```math
K_D
=\frac{r\,||\nabla_{u,v}D||}{|D|},
```

```math
K_V
=\frac{r\,||\nabla_{u,v}V_*||}{|V_*|}.
```

Direct differentiation of Eqs. (3)-(4) gives

```math
\boxed{
K_D(\chi)
=\frac{
\sqrt{\chi^4+6\chi^2+1}
}{\chi},
}
\tag{13}
```

and

```math
\boxed{
K_V(\chi)
=\frac{
\sqrt{1+\chi^2}
\sqrt{\chi^4+6\chi^2+1}
}{1-\chi^2}.
}
\tag{14}
```

These functions expose a real design tradeoff.

### Low RF

For `chi << 1`,

```math
\boxed{
K_D\sim\frac1\chi
\sim\frac{V_*^2}{D\omega},
}
\tag{15}
```

while

```math
\boxed{K_V\to1.}
\tag{16}
```

So the drift-like scale is well conditioned while diffusion is strongly noise amplified.

### Very high normalized RF

As `chi -> 1`, `K_V` diverges.

Therefore increasing RF indefinitely is not an optimal solution either.

---

## 7. Exact balanced-conditioning optimum

The minimax point occurs where

```math
K_D=K_V.
```

Using Eqs. (13)-(14), this gives

```math
\boxed{
\chi_*=\frac1{\sqrt3}.
}
\tag{17}
```

At that point

```math
\boxed{
K_D=K_V
=\sqrt{\frac{28}{3}}
\simeq3.055.
}
\tag{18}
```

Equation (12) then gives the corresponding normalized RF:

```math
\boxed{
\xi_*
=\frac{D\omega_*}{V_*^2}
=\sqrt3.
}
\tag{19}
```

or

```math
\boxed{
\omega_*
=\sqrt3\,\frac{V_*^2}{D}.
}
\tag{20}
```

This is an exact experimental-design result for isotropic root-displacement error under the stated model.

It is **not** a claim that the detector should always be driven at `omega_*`: parasitic electrical response, extra modes, nonlocal transport, bandwidth, and optical SNR can make a lower RF preferable. It is the intrinsic conditioning optimum of the algebraic homogeneous transport inversion itself.

---

## 8. Full first-order covariance map

For arbitrary covariance of the recovered roots, use the exact Jacobian rather than only Eqs. (13)-(14).

Let

```math
R^2=u^2+v^2.
```

Then

```math
\frac{\partial D}{\partial u}
=\frac{\omega(v^2-u^2)}
{vR^4},
```

```math
\frac{\partial D}{\partial v}
=-\frac{\omega u(u^2+3v^2)}
{v^2R^4},
```

```math
\frac{\partial V_*}{\partial u}
=-\frac{4\omega uv}{R^4},
```

```math
\frac{\partial V_*}{\partial v}
=\frac{\omega(u^4+4u^2v^2-v^4)}
{v^2R^4}.
```

Given the covariance of `(u,v,g0)`, first propagate to `(D,V_*,g0)`.

Then

```math
\delta w
=\delta V_*-2g_0\delta D-2D\delta g_0,
```

```math
\delta\kappa
=g_0\delta V_*-g_0^2\delta D+w\delta g_0.
```

Thus the full first-order covariance of `(D,w,kappa)` is obtained without finite-difference Monte Carlo or a nonlinear fit.

---

## 9. Implication for the current HgCdTe worked scale

Use the manuscript's illustrative homogeneous scale

```text
D ~ 0.02327 m^2/s
V_* ~ 3.45e4 m/s
```

for a no-recombination reference.

The intrinsic conditioning optimum is then approximately

```math
\boxed{
f_*\simeq14.1\ \mathrm{GHz}.}
```

At the current worked RF points, the normalized frequencies and root-condition numbers are approximately

| RF | `xi=D omega/V_*^2` | `chi` | `K_D` | `K_V` |
|---:|---:|---:|---:|---:|
| 100 MHz | 0.0123 | 0.0123 | 81.4 | 1.001 |
| 500 MHz | 0.0615 | 0.0608 | 16.6 | 1.017 |
| 1 GHz | 0.123 | 0.118 | 8.82 | 1.063 |

This is a major practical distinction:

> **The four-color closure residual may already be measurable at sub-GHz/GHz RF, while a precise algebraic extraction of diffusion from the same low-normalized-frequency roots can be much more demanding.**

The manuscript should not imply that detectability of the closure signal and good conditioning of all recovered transport coefficients are the same requirement.

---

## 10. Paper consequence

The adversarial-review gap is real and now has an exact answer.

The revised paper should state:

1. structural identifiability requires `Delta != 0`;
2. practical diffusion identifiability is controlled by `chi=Re(delta g)/Im(delta g)`;
3. low RF is intrinsically ill-conditioned for `D` because the real root displacement is `O(omega^2)` while the imaginary displacement is `O(omega)`;
4. the intrinsic balanced-conditioning point is `D omega/V_*^2=sqrt(3)`;
5. full covariance should be propagated through the analytic Jacobian before quoting `D,w,kappa` precision.

This strengthens the falsification philosophy: a model can pass an algebraic closure while some of its individual coefficients remain poorly measurable at the chosen RF.

Numerical regression:

`numerics/dc_rf_inversion_conditioning.py`
