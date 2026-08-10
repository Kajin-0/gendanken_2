# Local Recombination WKB Tomography — Leading-Order Maps of Drift, Diffusion, and Lifetime

**Date:** 2026-08-10  
**Status:** **DERIVED asymptotic extension / CHECKED numerically** on explicit smooth variable-coefficient stresses; no novelty/priority claim

## 1. Question

The exact uniform theorem proved that DC-normalized RF data identify

```math
D,
\qquad
V_* = \sqrt{v^2+4D\kappa},
```

but not `v` and `kappa` separately.

One DC collection spatial slope breaks the degeneracy exactly.

The next question is:

> **Does that identifiability structure survive locally when `v(z)`, `D(z)`, and `kappa(z)` vary with depth?**

At leading WKB order, yes.

---

# 2. Variable-coefficient first-passage equation

Use

```math
\boxed{
D(z)u''+v(z)u'-[\kappa(z)+s]u=0.
}
\tag{1}
```

Define

```math
\gamma_s(z)=\frac{u'(z,s)}{u(z,s)}.
```

Then exactly

```math
\boxed{
D(\gamma_s'+\gamma_s^2)
+v\gamma_s-(\kappa+s)=0.
}
\tag{2}
```

---

# 3. Leading local algebraic root

Neglect `gamma_s'` at zeroth order in slow spatial variation:

```math
D\gamma_{s,0}^2
+v\gamma_{s,0}
-(\kappa+s)=0.
```

Hence

```math
\boxed{
\gamma_{s,0}(z)
=
\frac{
\sqrt{v(z)^2+4D(z)[\kappa(z)+s]}-v(z)
}{2D(z)}.
}
\tag{3}
```

At DC,

```math
\gamma_{0,0}
=
\frac{\sqrt{v^2+4D\kappa}-v}{2D}.
```

At RF,

```math
\gamma_{\omega,0}
=
\frac{
\sqrt{v^2+4D(\kappa+i\omega)}-v
}{2D}.
```

Define the local DC-normalized complex propagation slope

```math
\boxed{
\Gamma_0(z,\omega)
=\gamma_{\omega,0}-\gamma_{0,0}.
}
\tag{4}
```

---

# 4. The uniform recombination degeneracy survives locally

Define

```math
\boxed{
V_*(z)
=\sqrt{v(z)^2+4D(z)\kappa(z)}.
}
\tag{5}
```

Then algebraically

```math
\boxed{
\Gamma_0(z,\omega)
=
\frac{
\sqrt{V_*(z)^2+4iD(z)\omega}-V_*(z)
}{2D(z)}.
}
\tag{6}
```

Thus at leading local order, DC-normalized RF again depends on `v` and `kappa` only through `V_*`.

This gives the local structural statement:

> **Normalized RF locally identifies `D(z)` and `V_*(z)`, not `v(z)` and `kappa(z)` separately, up to spatial-gradient corrections.**

---

# 5. Local algebraic inversion

Write

```math
\Gamma_0=a+ib.
```

Then pointwise

```math
\boxed{
D(z)
\simeq
\frac{\omega a}
{b(a^2+b^2)}
}
\tag{7}
```

and

```math
\boxed{
V_*(z)
\simeq
\frac{\omega(b^2-a^2)}
{b(a^2+b^2)}.
}
\tag{8}
```

The local DC collection logarithmic slope gives

```math
\gamma_{\rm DC}(z)
\simeq
\gamma_{0,0}(z).
```

Therefore

```math
\boxed{
v(z)
\simeq
V_*(z)-2D(z)\gamma_{\rm DC}(z)
}
\tag{9}
```

and

```math
\boxed{
\kappa(z)
\simeq
V_*(z)\gamma_{\rm DC}(z)
-D(z)\gamma_{\rm DC}(z)^2.
}
\tag{10}
```

Thus a local map of

```math
D(z),\quad v(z),\quad \tau(z)=1/\kappa(z)
```

is predicted from

```text
one local complex DC-normalized RF slope
+
one local DC collection slope.
```

---

# 6. First spatial-gradient correction

Differentiate the local algebraic equation

```math
D\gamma_{s,0}^2
+v\gamma_{s,0}
-(\kappa+s)=0.
```

Then

```math
D'\gamma_{s,0}^2
+(v+2D\gamma_{s,0})\gamma_{s,0}'
+v'\gamma_{s,0}
-\kappa'=0.
```

Hence

```math
\boxed{
\gamma_{s,0}'
=
\frac{
\kappa'
-D'\gamma_{s,0}^2
-v'\gamma_{s,0}
}{v+2D\gamma_{s,0}}.
}
\tag{11}
```

The Riccati equation gives the first WKB correction

```math
\boxed{
\gamma_{s,1}
\simeq
-\frac{D\gamma_{s,0}'}
{v+2D\gamma_{s,0}}
}
\tag{12}
```

or

```math
\boxed{
\gamma_{s,1}
\simeq
\frac{
D[D'\gamma_{s,0}^2+v'\gamma_{s,0}-\kappa']
}{(v+2D\gamma_{s,0})^2}.
}
\tag{13}
```

The normalized RF correction is

```math
\boxed{
\Gamma_1
=\gamma_{i\omega,1}-\gamma_{0,1}.
}
\tag{14}
```

This is important conceptually.

At strict local zeroth order, `(v,kappa)` are exactly confounded through `V_*`.

Spatial gradients can break that degeneracy only through the small correction (14).

Therefore trying to infer `v` and `kappa` from normalized RF alone by exploiting nonuniformity is inherently a **small-difference / potentially ill-conditioned strategy**.

The DC collection slope remains the clean way to break the degeneracy.

---

# 7. Spectral implementation

If wavelength provides a calibrated local generation coordinate `z_g(lambda)`, then

```math
\Gamma_{\rm spec}(z_g,\omega)
\simeq
\frac{
\partial_\lambda\ln H_{\rm norm}(\lambda,\omega)
}{dz_g/d\lambda}
```

and

```math
\gamma_{\rm DC,spec}(z_g)
\simeq
\frac{
\partial_\lambda\ln I_{\rm DC}(\lambda)
}{dz_g/d\lambda},
```

subject to the finite-generation-kernel corrections already derived in

`FINITE_WIDTH_GENERATION_KERNEL_THEOREM.md`.

Thus the local ideal spectral measurement becomes

```text
complex RF spectral derivative
+
DC spectral derivative
-> D(z), v(z), tau(z).
```

This is a much sharper target than generic multi-mode curve fitting.

---

# 8. Numerical stress

The regression

`numerics/local_recombination_wkb_tomography.py`

uses smooth nontrivial profiles

```text
v(z)=1.6[1+0.10 sin(pi z)]
D(z)=0.06[1+0.08 cos(pi z)]
kappa(z)=0.40[1+0.12 sin(2 pi z)]
omega=2.5
```

and integrates the exact Riccati equation along the slowly varying branch.

Applying the **zeroth-order local inversion formulas directly to the exact variable-coefficient solution** gives over the interior approximately

```text
D:
median relative error ~1.19%
maximum ~2.45%

V_*:
median ~0.56%
maximum ~1.09%

v after adding DC slope:
median ~0.59%
maximum ~1.13%

kappa after adding DC slope:
median ~1.53%
maximum ~2.59%.
```

This is not a universal accuracy statement.

It demonstrates that the local exact-uniform identifiability structure survives quantitatively in a nontrivial smooth variable-coefficient example, with the expected percent-level WKB bias.

---

# 9. Strong predictions

### P1 — leading local confounding

At each depth, normalized RF must primarily constrain

```math
D(z),\quad V_*(z)=\sqrt{v(z)^2+4D(z)\kappa(z)}.
```

### P2 — DC breaks the local confounding

Adding the DC collection slope must separate `v(z)` and `kappa(z)` according to Eqs. (9)-(10).

### P3 — nonuniform correction scale

Residual failure of the local inversion should scale with the gradient correction in Eqs. (11)-(14), not arbitrarily.

### P4 — normalized-RF-only separation should be fragile

Any apparent strong separation of `v` and `kappa` from normalized RF alone in a slowly varying region should be treated skeptically unless it is demonstrably coming from gradient-order information larger than model/systematic error.

### P5 — overdetermined RF prediction

Once local `D,v,kappa` are obtained, all additional frequencies are predicted by the local first-passage branch up to WKB/finite-kernel corrections.

---

# 10. Consequence for the project

This result changes the theoretical interpretation of the earlier calibration problem.

The clean theory-first strategy is now

```text
DC spectral depth dependence
-> local recombination information

complex RF spectral depth dependence
-> local drift/diffusion propagation

combined exact algebra
-> D(z), v(z), tau(z)

translated internal perturbation
-> independent local witness and falsification test.
```

The next high-value step is no longer another device geometry optimization.

It is to derive the **noise/Fisher information of this minimal local measurement set**, because the structural identifiability is now known exactly.
