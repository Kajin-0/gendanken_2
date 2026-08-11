# Spectral Depth and Initial Carrier State — Excess-Energy Invariance Theorem

**Date:** 2026-08-10  
**Status:** **DERIVED / CHECKED** exact ideal theorem plus **CONDITIONAL** HgCdTe numerical stress; no claim that electron/hole energy partition is universally invariant

## 1. The adversarial question

The spectral-depth program uses wavelength as an internal generation coordinate.

A strong objection is immediate:

> **Changing wavelength changes photon energy as well as absorption depth.  Could a four-color closure failure come from different carrier initial energies rather than spatially varying transport?**

In a useful ideal graded-absorber limit, wavelength translates the generation depth **without changing the initial total excess-energy distribution at all**.

The current HgCdTe quartet is numerically close to that limit.

---

## 2. Ideal monotonic graded absorber

Let the local bandgap decrease linearly with depth:

```math
\boxed{
E_g(z)=E_{g0}-Gz,
\qquad G>0.
}
```

For photon energy `E`, define the local total photon excess energy above the gap

```math
\boxed{
u
=E-E_g(z).
}
```

The absorption threshold occurs at

```math
z_t(E)=\frac{E_{g0}-E}{G},
```

so

```math
u=G[z-z_t(E)].
```

Now impose the ideal local optical law

```math
\boxed{
\alpha(z;E)=A(\nu),
}
```

with

```math
A(\nu)=0
```

for `nu<=0`.

Thus absorption depends on photon energy and depth only through the **local excess-energy coordinate**.

---

## 3. Generation distribution in the excess-energy coordinate

For one-pass Beer-Lambert propagation, the generation density after threshold is

```math
p_z(z|E)
=A(\nu)
\exp\left[
-\int_{z_t(E)}^z A(E-E_g(x))dx
\right].
```

Because

```math
d\nu=G dz,
```

the optical depth becomes

```math
\int_{z_t}^z A(E-E_g(x))dx
=\frac1G\int_0^\nu A(u)du.
```

Therefore the generation density expressed in `nu` is

```math
\boxed{
p_\nu(\nu)
=\frac{A(\nu)}{G}
\exp\left[
-\frac1G\int_0^\nu A(u)du
\right].
}
\tag{1}
```

Equation (1) contains **no photon energy `E`**.

For a sufficiently deep/full-absorption domain, it is normalized directly.  With finite truncation, only the downstream cutoff/conditioning can reintroduce `E` dependence.

---

## 4. Exact theorem

Under

```text
affine monotonic gap,
absorption depending only on local total excess energy,
and no wavelength-dependent boundary truncation,
```

changing photon energy does two things:

### Generation depth

The threshold and the complete generation profile translate by

```math
\boxed{
\Delta z_t=-\frac{\Delta E}{G}
}
```

(up to the coordinate sign convention).

### Initial total excess energy

The entire probability distribution of

```math
\nu=E-E_g(z)
```

is unchanged.

Hence

```math
\boxed{
p_\nu(\nu|E_1)=p_\nu(\nu|E_2).}
\tag{2}
```

All excess-energy moments are common:

```math
\boxed{
\langle\nu^n\rangle_{E_1}
=\langle\nu^n\rangle_{E_2}.
}
\tag{3}
```

This is the spectral-depth / initial-excess-energy invariance theorem.

---

## 5. Physical interpretation

A monotonic graded gap can act as more than a spatial wavelength encoder.

In the ideal limit it maps different photon energies onto different **positions with the same local excitation condition above the band edge**.

Conceptually:

```text
higher-energy photon
-> allowed absorption begins earlier in the higher-gap material

lower-energy photon
-> allowed absorption begins deeper in the lower-gap material

but

local photon excess above the gap at generation
-> same statistical distribution.
```

Thus wavelength need not introduce an independent hot-carrier initial-state coordinate.

This is a strong reason graded absorbers are unusually suitable for the spectral-depth falsification program.

---

## 6. What breaks exact invariance

Real semiconductors violate the ideal assumptions through

```text
nonlinear Eg(z),
composition-dependent absorption prefactor,
composition-dependent absorption exponent,
explicit photon-energy factors in alpha,
reflection/interference,
finite absorber truncation,
Urbach/subgap absorption,
carrier-band nonparabolicity,
and wavelength/composition dependence of electron-hole excess-energy partition.
```

Those effects create a calculable initial-state mismatch rather than invalidating the ideal theorem.

The relevant question becomes its size.

---

## 7. Current graded-HgCdTe quartet

Use the same corrected theory example:

```text
T = 300 K
L = 7.6 um
linear x=0.55 -> 0.32
Hansen gap
Moazzami absorption
mean generation depths = 2.5,3.0,3.5,4.0 um.
```

The corresponding wavelengths are approximately

```text
2.134651
2.215042
2.301173
2.393907 um.
```

All modeled absorbed fractions exceed `0.9993`.

For each real generation kernel, evaluate the local total photon excess

```math
\nu(z)=hc/\lambda-E_g[x(z),T].
```

and average it over the conditional generation distribution.

Results:

| Mean generation depth | Mean excess energy | Std. dev. | Skewness |
|---:|---:|---:|---:|
| `2.5 um` | `52.353 meV` | `33.235 meV` | `0.959` |
| `3.0 um` | `52.428 meV` | `33.118 meV` | `0.947` |
| `3.5 um` | `52.478 meV` | `32.958 meV` | `0.927` |
| `4.0 um` | `52.473 meV` | `32.694 meV` | `0.892` |

The mean excess-energy span is only about

```math
\boxed{0.24\%}
```

of its mean value.

The standard-deviation span is about

```math
\boxed{1.6\%}.
```

Thus the total excess-energy distribution is not exactly invariant, but its first two moments are remarkably stable over the present quartet.

---

## 8. Mean-depth point comparison

At the four **mean generation positions**, the local differences

```math
hc/\lambda-E_g[z_{mean}]
```

are approximately

```text
52.554
52.609
52.638
52.611 meV.
```

Their total range is less than

```text
0.09 meV.
```

This independently shows why the quartet behaves close to a constant-excess-energy translation.

---

## 9. What is not yet proved

The theorem concerns the **total photon energy above the local bandgap**.

It does not by itself prove that the initial minority-electron distribution is identical across wavelength.

The partition of excess energy between electron and hole can depend on

```text
effective masses,
nonparabolicity,
valence-band structure,
composition,
and scattering during ultrafast thermalization.
```

Likewise the carrier can retain momentum/energy memory over a finite thermalization length.

Therefore the paper should state the conservative conclusion:

> **The dominant total-excess-energy coordinate is nearly matched by the graded spectral design; residual electron/hole partition and thermalization-memory effects remain an ordinary initial-condition correction that can be tested by RF closure rather than assumed absent.**

---

## 10. Falsification implication

If the four-color closure fails while

```text
source-shape evolution is controlled,
spatial mode count remains one,
and total excess-energy distributions are matched,
```

then a persistent wavelength-dependent propagation exponent can be interpreted more sharply.

Possible causes include

```text
residual carrier-energy partition differences,
finite thermalization memory,
nonlocal transport,
or genuine depth-dependent transport coefficients.
```

The second-RF closure remains valuable because initial-state memory generally introduces frequency dependence rather than merely a static spatial coefficient shift.

---

## 11. Numerical regression

`numerics/spectral_depth_excess_energy_invariance.py`

checks

```text
exact photon-energy invariance of p_nu for an affine-gap ideal absorber
translation of mean generation depth by Delta E/G
and
near-invariance of the real Hansen/Moazzami HgCdTe quartet's excess-energy moments.
```

---

## 12. Paper-level role

This result belongs in the systematic/assumption section, not as a separate paper theme.

Its purpose is to answer a strong reviewer concern:

> **"Your wavelength coordinate also changes hot-carrier initial conditions."**

The correct response is not to deny the issue.

It is:

1. derive the exact ideal condition under which the initial excess-energy distribution is wavelength invariant;
2. show that the chosen graded-HgCdTe quartet is numerically close to that condition in its first two excess-energy moments;
3. leave residual partition/thermalization effects as a falsifiable higher-level correction.
