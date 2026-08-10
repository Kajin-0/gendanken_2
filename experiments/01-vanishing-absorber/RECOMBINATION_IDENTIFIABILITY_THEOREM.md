# Recombination Identifiability Theorem — What DC-Normalized RF Can and Cannot Determine

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** for constant-coefficient 1-D downstream drift-diffusion with uniform bulk recombination; exact structural non-identifiability result; no novelty/priority claim

## 1. Why this matters

The active first-passage detector model normalizes the complex RF response by the DC-collected signal:

```math
H(\omega)
=\frac{N_{i\omega}}{N_0}.
```

That is physically sensible because it separates timing from simple collection loss.

But normalization can also remove information.

The simplest possible uniform drift-diffusion problem reveals exactly what is lost.

---

# 2. Uniform drift-diffusion with recombination

Let

```text
v > 0       downstream drift velocity
D > 0       diffusion coefficient
kappa >= 0  bulk recombination rate = 1/tau
```

For a carrier generated at `x<L`, define the Laplace-weighted successful first-passage transform `U(x,s)`.

The backward equation is

```math
\boxed{
D U''+vU'-(\kappa+s)U=0,
\qquad U(L,s)=1.
}
\tag{1}
```

For an effectively remote upstream boundary,

```math
\boxed{
U(x,s)
=\exp[-\gamma(s)(L-x)],
}
\tag{2}
```

with

```math
\boxed{
\gamma(s)
=
\frac{
\sqrt{v^2+4D(\kappa+s)}-v
}{2D}.
}
\tag{3}
```

The DC collection probability from depth `x` is

```math
U(x,0)
=\exp[-\gamma_0(L-x)],
```

where

```math
\boxed{
\gamma_0
=
\frac{\sqrt{v^2+4D\kappa}-v}{2D}.
}
\tag{4}
```

---

# 3. DC-normalized RF propagation

Condition the RF response on carriers that are collected at DC:

```math
H_x(\omega)
=\frac{U(x,i\omega)}{U(x,0)}.
```

Then

```math
\boxed{
H_x(\omega)
=\exp[-\Gamma(\omega)(L-x)],
}
\tag{5}
```

with

```math
\boxed{
\Gamma(\omega)
=\gamma(i\omega)-\gamma_0.
}
\tag{6}
```

Now define

```math
\boxed{
V_*
\equiv
\sqrt{v^2+4D\kappa}.
}
\tag{7}
```

Using (3)-(4),

```math
\boxed{
\Gamma(\omega)
=
\frac{
\sqrt{V_*^2+4iD\omega}-V_*
}{2D}.
}
\tag{8}
```

This is **exactly the same functional form as recombination-free drift-diffusion**, but with `v` replaced by `V_*`.

---

# 4. Structural non-identifiability theorem

Equation (8) proves:

> **All noiseless DC-normalized RF data in this uniform model depend on `v` and `kappa` only through the combination `V_* = sqrt(v^2+4D kappa)`.**

Therefore the transformation

```math
(v,\kappa)
\longrightarrow
(\tilde v,\tilde\kappa)
```

that preserves

```math
v^2+4D\kappa
=
\tilde v^2+4D\tilde\kappa
```

leaves the complete normalized RF propagation function unchanged.

Thus

```math
\boxed{
\text{DC-normalized RF alone cannot separately identify }v\text{ and }\kappa.
}
\tag{9}
```

This is not a signal-to-noise limitation.

It is an exact many-to-one map in parameter space.

---

# 5. What normalized RF does identify

Write

```math
\Gamma=a+ib.
```

Because (8) has the same algebraic form as the recombination-free theorem,

```math
\boxed{
D
=
\frac{\omega a}
{b(a^2+b^2)}
}
\tag{10}
```

and

```math
\boxed{
V_*
=
\frac{
\omega(b^2-a^2)
}{b(a^2+b^2)}.
}
\tag{11}
```

So one nonzero complex RF frequency and two localized generation depths determine

```text
D
and
V_* = sqrt(v^2 + 4D kappa)
```

exactly in the uniform model.

They do **not** determine `v` and `kappa` separately.

---

# 6. One DC observable breaks the degeneracy

The DC collection depth dependence supplies `gamma_0`:

```math
\boxed{
\gamma_0
=
\frac{\partial}{\partial x}
\ln U(x,0).
}
\tag{12}
```

From (4),

```math
V_*=v+2D\gamma_0.
```

Therefore

```math
\boxed{
v
=V_*-2D\gamma_0.
}
\tag{13}
```

The DC characteristic equation gives

```math
D\gamma_0^2+v\gamma_0=\kappa.
```

Substitute (13):

```math
\boxed{
\kappa
=V_*\gamma_0-D\gamma_0^2.
}
\tag{14}
```

Thus the minimal ideal information set is

```text
one complex nonzero RF spatial propagation measurement
+
one DC collection spatial slope.
```

It yields

```math
\boxed{
D,\quad v,\quad \kappa=1/\tau
}
```

algebraically.

---

# 7. Minimal two-depth gedanken experiment

Take two known generation depths `x_1,x_2`.

At DC measure collected amplitudes

```math
I_1(0),\qquad I_2(0).
```

Any common depth-independent gain cancels:

```math
\boxed{
\gamma_0
=
\frac{
\ln I_2(0)-\ln I_1(0)
}{x_2-x_1}.
}
\tag{15}
```

At one nonzero RF frequency, measure DC-normalized complex responses

```math
H_1(\omega),\qquad H_2(\omega).
```

Then

```math
\boxed{
\Gamma
=
\frac{
\ln H_2(\omega)-\ln H_1(\omega)
}{x_2-x_1}.
}
\tag{16}
```

Equations (10)-(11) give `D,V_*`; Eqs. (13)-(14) then give `v,kappa`.

So in the ideal uniform model:

> **Two spatial coordinates, one DC measurement, and one complex RF frequency are sufficient to determine drift velocity, diffusion coefficient, and recombination lifetime.**

This is an unusually compact falsifiable prediction.

---

# 8. Spectral implementation

In a monotonic graded absorber, two wavelengths may provide two generation-depth coordinates:

```math
x_j\simeq z_g(\lambda_j).
```

Then the same equations apply after replacing physical source translation by calibrated spectral depth translation.

The finite-width generation theorem further shows that broad generation kernels do not bias the complex spatial slope in a uniform medium if they translate rigidly.

Thus the ideal spectral experiment becomes

```text
DC spectral collection slope
+
one complex RF spectral slope
-> D, v, tau.
```

This is precisely the sort of large, simple prediction the theory program is seeking.

---

# 9. Falsification structure

The theorem predicts several simultaneous closures.

### P1 — normalized-RF degeneracy

Different `(v,kappa)` pairs with equal `v^2+4D kappa` must be indistinguishable in normalized RF.

### P2 — DC breaks the degeneracy

Their DC spatial collection slopes must differ unless the parameter pairs are identical.

### P3 — one-frequency closure

The recovered `D,V_*` from any RF frequency must be the same.

### P4 — reconstructed lifetime positivity

Using the independently measured `gamma_0`, Eq. (14) must give

```math
\kappa\ge0.
```

A negative reconstructed `kappa` falsifies the uniform local drift-diffusion model or the assumed spatial coordinate calibration.

### P5 — overdetermined multi-frequency prediction

Once `D,v,kappa` are obtained from the minimal data, **all other RF frequencies are predictions**, not fit parameters:

```math
\Gamma_{\rm pred}(\omega)
=
\frac{
\sqrt{v^2+4D(\kappa+i\omega)}
-
\sqrt{v^2+4D\kappa}
}{2D}.
\tag{17}
```

This makes the experiment strongly falsifiable.

---

# 10. Why this changes the interpretation of earlier work

The repository repeatedly found that normalized timing/RF data could not cleanly separate transport changes from recombination/lifetime assumptions.

The uniform theorem now shows a precise reason:

```math
v\quad\text{and}\quad\kappa
```

are **exactly confounded** in DC-normalized RF through `V_*`.

Therefore the earlier requirement for independent minority-carrier lifetime/transport information was not merely conservative experimental practice.

It reflects a real structural identifiability boundary already present in the simplest solvable first-passage model.

---

# 11. Next theory question

The next high-value question is whether an analogous local degeneracy survives in the slowly varying case.

The likely WKB form is

```math
\Gamma(z,\omega)
\simeq
\gamma[z,\kappa(z)+i\omega]
-
\gamma[z,\kappa(z)],
```

which would imply a **local** effective velocity

```math
V_*(z)
=\sqrt{v(z)^2+4D(z)\kappa(z)}.
```

If true to controlled order, a complex RF spectral derivative plus DC spectral collection derivative would provide local maps of

```math
D(z),\quad v(z),\quad \tau(z)
```

with explicit WKB and optical-kernel error terms.

Numerical regression:

`numerics/recombination_identifiability_theorem.py`
