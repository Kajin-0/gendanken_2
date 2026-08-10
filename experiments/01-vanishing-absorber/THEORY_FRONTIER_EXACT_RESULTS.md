# Theory Frontier — Exact Results, Minimal Gedanken Experiments, and Falsification Program

**Date:** 2026-08-10  
**Status:** active theory-first frontier; exact/asymptotic statements are separated from HgCdTe implementation; no novelty/priority claim; not yet a manuscript

## 1. Research objective

The project should now optimize for the following sequence:

```text
simple gedanken experiment
-> exact first-principles mathematics
-> parameter-free or minimally parameterized prediction
-> explicit structural identifiability statement
-> falsification test
-> only then a material-specific worked example.
```

Fabrication feasibility remains supporting context only.

The goal is not to design a device that the present researcher must build.

The goal is to derive strong predictions that an independent laboratory could test.

---

# 2. Gedanken experiment A — translate one weak internal delay feature

Assume deterministic monotonic downstream transport

```math
T(x)=\int_x^Lq(z)dz.
```

Translate a weak known slowness feature

```math
q(z)\to q(z)+\epsilon h(z-z_0).
```

The exact low-frequency relocation identity is

```math
\boxed{
\frac{d}{dz_0}
\left.
\frac{\partial\bar T_\lambda}{\partial\epsilon}
\right|_0
=
\int p_\lambda(z)h(z-z_0)dz.
}
```

For a point feature of area `A_h`,

```math
\boxed{
\frac{dD_\lambda}{dz_0}
=A_h p_\lambda(z_0).
}
```

So the translated response directly measures the generation PDF.

Finite displacement gives the exact probability-window law

```math
\boxed{
D_\lambda(z_2)-D_\lambda(z_1)
=A_hP_\lambda(z_1<X<z_2).
}
```

This is already directly falsifiable.

Full derivation:

`TRANSLATION_RESPONSE_THEOREM.md`

---

# 3. Gedanken experiment A at finite RF — exact optical/transport separation

For deterministic local transit,

```math
H_\lambda(\omega)
=\int p_\lambda(z)e^{-i\omega T(z)}dz.
```

The position derivative of the linear logarithmic response to a point perturbation is

```math
\boxed{
R_{\lambda,\omega}(z)
=-\frac{i\omega A_h}{H_\lambda(\omega)}
 p_\lambda(z)e^{-i\omega T(z)}.
}
```

Therefore

```math
\boxed{
p_\lambda(z)
=
\frac{|R(z)|}{\int|R(u)|du}
}
```

and

```math
\boxed{
q(z)
=
\frac{1}{\omega}
\frac{d}{dz}\arg R(z).
}
```

The same complex relocation field separates

```text
magnitude -> optical generation density
phase gradient -> local transit slowness.
```

There is also the exact complex sum rule

```math
\boxed{
\int R_{\lambda,\omega}(z)dz
=-i\omega A_h,
}
```

independent of wavelength and baseline transport.

This is the strongest ideal deterministic theorem in the current project.

---

# 4. Gedanken experiment B — two generation depths in uniform drift-diffusion

For constant downstream drift `v` and diffusion `D`, the first-passage transform is

```math
U(x,i\omega)
=\exp[-\gamma(\omega)(L-x)],
```

with

```math
\boxed{
\gamma(\omega)
=
\frac{\sqrt{v^2+4iD\omega}-v}{2D}.
}
```

Two known generation depths determine `gamma` after common electronics cancellation:

```math
\boxed{
\gamma
=
\frac{
\ln H_2-\ln H_1
}{x_2-x_1}.
}
```

Writing

```math
\gamma=a+ib,
```

gives the exact algebraic inverse

```math
\boxed{
D
=
\frac{\omega a}{b(a^2+b^2)}
}
```

and

```math
\boxed{
v
=
\frac{\omega(b^2-a^2)}{b(a^2+b^2)}.
}
```

Thus one complex RF frequency plus two spatial coordinates determines both `v` and `D` exactly in the uniform no-recombination model.

Full derivation:

`DRIFT_DIFFUSION_COMPLEX_PROPAGATION_THEOREM.md`

---

# 5. Major prediction — magnitude reveals diffusion before phase does

For

```math
\eta=D\omega/v^2\ll1,
```

```math
\gamma
=
\frac{i\omega}{v}
+
\frac{D\omega^2}{v^3}
-
\frac{2iD^2\omega^3}{v^5}
+\cdots.
```

Therefore

```math
\operatorname{Re}\gamma
\sim D\omega^2/v^3
```

while the relative diffusion correction to phase-derived slowness begins only at order

```math
(D\omega/v^2)^2.
```

Prediction:

> **A detector can look nearly deterministic in RF phase while its RF magnitude already contains leading-order diffusion information.**

A phase-only test is therefore structurally less informative than full complex response.

---

# 6. Gedanken experiment C — wavelength replaces mechanical source scanning

Let a monotonic optical structure map wavelength to generation center

```math
z_g(\lambda).
```

In the local-generation limit,

```math
H(\lambda,\omega)
=G(\omega)u[z_g(\lambda),i\omega].
```

Then

```math
\boxed{
\gamma_{\rm meas}
=
\frac{\partial_\lambda\ln H}
{dz_g/d\lambda}.
}
```

For a sharp monotonic bandgap coordinate

```math
E_g[z_g(\lambda)]=hc/\lambda,
```

```math
\boxed{
\gamma_{\rm meas}
=-\frac{\lambda^2E_g'(z_g)}{hc}
\partial_\lambda\ln H.
}
```

The local algebraic formulas above then predict `v(z)` and `D(z)`.

For slowly varying transport the leading correction is controlled by

```math
\boxed{
\epsilon_{\rm WKB}
=
\left|
\frac{
D(D'\gamma_0+v')
}{(v+2D\gamma_0)^2}
\right|.
}
```

Full derivation:

`SPECTRAL_DERIVATIVE_DRIFT_DIFFUSION_TOMOGRAPHY.md`

---

# 7. Major optical correction — width is not the real problem

In a uniform region, suppose wavelength translates an arbitrary normalized generation profile without changing its shape:

```math
p_\lambda(z)=g[z-z_g(\lambda)].
```

Then exactly

```math
\boxed{
\frac{\partial\ln H}{\partial z_g}
=\gamma
}
```

for **any generation width**.

A broad kernel is therefore not intrinsically a spatial-resolution error.

Only shape evolution contributes an optical bias.

For a Gaussian with wavelength-dependent variance,

```math
\boxed{
\frac{d\ln H}{d\lambda}
=
\gamma z_g'
+
\frac{\gamma^2}{2}
\frac{d\sigma_z^2}{d\lambda}.
}
```

Full derivation:

`FINITE_WIDTH_GENERATION_KERNEL_THEOREM.md`

---

# 8. Gedanken experiment D — add recombination

For constant recombination rate

```math
\kappa=1/\tau,
```

DC-normalized RF propagation is

```math
\Gamma(\omega)
=\gamma(\kappa+i\omega)-\gamma(\kappa).
```

Define

```math
\boxed{
V_*=\sqrt{v^2+4D\kappa}.
}
```

Then exactly

```math
\boxed{
\Gamma(\omega)
=
\frac{
\sqrt{V_*^2+4iD\omega}-V_*
}{2D}.
}
```

Therefore perfect DC-normalized RF measurements identify

```text
D and V_*
```

but cannot separately identify

```text
v and kappa.
```

This is an exact structural non-identifiability theorem.

One additional DC collection spatial slope

```math
\gamma_0
=\partial_x\ln U(x,0)
```

breaks the degeneracy:

```math
\boxed{
v=V_*-2D\gamma_0,
}
```

```math
\boxed{
\kappa=V_*\gamma_0-D\gamma_0^2.
}
```

Full derivation:

`RECOMBINATION_IDENTIFIABILITY_THEOREM.md`

---

# 9. Minimal sufficient ideal experiment

In a uniform region, the complete local parameter set

```math
v,\quad D,\quad \tau
```

can therefore be determined from

```text
two known generation coordinates
+
relative DC collection at those coordinates
+
one complex nonzero RF measurement at those coordinates.
```

Once those three parameters are inferred, every additional RF frequency becomes a **prediction**, not a fit parameter.

That makes the model strongly falsifiable.

---

# 10. Current falsification hierarchy

A serious paper should emphasize predictions that can fail.

## F1 — translation probability law

A moved point-delay feature must produce the generation probability between its old and new positions.

## F2 — translation sum rule

The integrated complex relocation gradient must equal `-i omega A_h` in the deterministic first-order model.

## F3 — wavelength collapse of deterministic phase gradient

Every wavelength must give the same reconstructed `q(z)` where the deterministic model applies.

## F4 — RF collapse of local drift-diffusion parameters

Different frequencies must give the same `v,D` in a uniform/local-WKB region.

## F5 — finite-width invariance

Rigidly translated generation kernels of different width must return the same `gamma` in a uniform region.

## F6 — exact recombination degeneracy

DC-normalized RF cannot distinguish `(v,kappa)` pairs with identical `v^2+4D kappa`.

## F7 — DC degeneracy breaking

Adding the DC collection slope must recover the unique `v,kappa` pair.

These are much stronger tests than comparing one fitted bandwidth number with one simulation.

---

# 11. Candidate paper logic

A future manuscript, if the novelty audit survives, should be understandable from four pictures.

### Figure 1 — two-point first-passage gedanken experiment

```text
carrier generated at x1 or x2
-> drift + diffusion
-> complex phase/magnitude at collector
```

Exact `v,D` inversion follows.

### Figure 2 — graded absorber turns wavelength into depth

```text
lambda1 -> generation distribution near z1
lambda2 -> distribution near z2
```

Complex spectral derivative gives local propagation.

### Figure 3 — translate a weak internal feature

```text
same feature at z1, z2, z3...
```

Magnitude traces optical generation; phase-gradient tests local transit.

### Figure 4 — falsification map

```text
frequency collapse succeeds -> local drift-diffusion supported
phase succeeds but magnitude fails -> diffusion/non-common optics issue
normalized RF degeneracy broken without DC -> model missing physics
translated sum rule fails -> deterministic/local-perturbation assumption fails.
```

The conceptual explanation can remain simple while the appendices carry the derivations.

---

# 12. Prior-art boundary right now

Known prior art already covers

```text
analytic photodiode frequency-response models with drift and diffusion,
wavelength-dependent photodiode frequency response,
frequency-domain extraction of semiconductor transport coefficients,
graded-HgCdTe built-in-field transport,
and localized-position HgCdTe transit measurements.
```

Therefore none of those ingredients alone can be the paper claim.

The unresolved candidate is the combined inverse structure:

```text
monotonic spectral depth coordinate
+
complex spatial/spectral derivative inversion
+
exact DC-normalized recombination identifiability boundary
+
translated internal perturbation as a local witness and sum-rule test.
```

Priority is **OPEN** until a focused primary-source audit specifically targeting these inverse identities and translated-perturbation methods is completed.

---

# 13. Immediate next work

Do not return to fabrication optimization.

The next theoretical priorities are:

1. extend the recombination identifiability theorem to slowly varying `v(z),D(z),kappa(z)` and derive the first WKB correction;
2. derive the exact first-passage adjoint/Green-function sensitivity for a translated drift perturbation and compare it to the deterministic translation factorization;
3. derive noise/Fisher bounds for the minimal two-depth/DC/RF experiment;
4. perform a focused prior-art audit on **spectral derivative inversion** and **translated internal perturbation tomography**;
5. only then substitute HgCdTe parameter ranges and produce quantitative falsifiable curves.

The theory should remain material-independent until steps 1-4 are stable.
