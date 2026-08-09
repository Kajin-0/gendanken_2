# HgCdTe Graded-Poisson Robustness — Band-Offset-Invariant Zener Geometry

**Date:** 2026-08-09  
**Status:** exact linear-edge reparameterization plus a uniform-space-charge Poisson robustness condition; no novelty claim

## 1. Purpose

The live graded-Kane result was written using the symmetric two-band variables `U` and `Delta`.

A realistic HgCdTe composition gradient does not generally split the gap change equally between the conduction and valence edges. Recent HgCdTe electron-affinity work finds that approximately two thirds of a composition-induced gap change appears in the conduction band.

This note asks two questions:

1. does the direct-Zener suppression result survive an arbitrary band-offset partition?
2. how much extra grading headroom is required when Poisson space charge makes the electrostatic field nonuniform?

The first answer is stronger than expected: the decisive Zener geometry is independent of the partition parameter.

---

## 2. General linear band-edge partition

Let the local band gap decrease along `+x` at a constant rate

```math
\boxed{
G\equiv-\frac{dE_g}{dx}>0.
}
```

Let

```math
0<\alpha<1
```

be the fraction of the composition-induced gap change appearing in the conduction band.

Then the composition contribution to the band-edge slopes is

```math
\left.\frac{dE_c}{dx}\right|_{\rm grad}
=-\alpha G,
```

```math
\left.\frac{dE_v}{dx}\right|_{\rm grad}
=+(1-\alpha)G.
```

Let an electrostatic field `F` contribute the common electron-energy slope

```math
-qF
```

to both band edges.

Define positive downhill slopes by

```math
E_c'= -S_c,
\qquad
E_v'= -S_v.
```

Then

```math
\boxed{
S_c=qF+\alpha G,
}
```

```math
\boxed{
S_v=qF-(1-\alpha)G.
}
```

Subtracting gives the exact identity

```math
\boxed{
S_v=S_c-G.
}
```

The band-offset partition `alpha` cancels.

This identity is simply the differential statement of

```math
E_g=E_c-E_v.
```

---

## 3. Natural grading parameter

Hold the useful conduction-band downhill slope fixed at

```math
\boxed{S_c=S>0.}
```

Define

```math
\boxed{
\delta\equiv\frac{G}{S}.
}
```

Then

```math
\boxed{
S_v=(1-\delta)S.
}
```

The conventional same-direction two-turning-point direct-Zener geometry therefore requires

```math
0\le\delta<1.
```

As

```math
\delta\to1^{-},
```

the valence-band downhill slope tends to zero.

For

```math
\delta\ge1,
```

the valence band is locally flat or rises while the conduction band continues downhill.

---

## 4. Exact action ratio for arbitrary band-offset partition

Use the exact linear-edge action already derived in

`HGCDTE_LINEAR_GRADED_KANE_WKB.md`:

```math
\mathcal S
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
```

Choose a symmetric local reference gap at the tunneling energy,

```math
E_c(0)-E=E-E_v(0)=\Delta_0.
```

With

```math
S_c=S,
\qquad
S_v=(1-\delta)S,
```

the turning points are

```math
x_c=\frac{\Delta_0}{S},
```

```math
x_v=-\frac{\Delta_0}{(1-\delta)S}.
```

Therefore

```math
x_c-x_v
=\frac{(2-\delta)\Delta_0}
{(1-\delta)S}.
```

Substitution gives

```math
\boxed{
\mathcal S_Z(\delta)
=\mathcal S_Z(0)
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}},
\qquad
0\le\delta<1.
}
```

Hence

```math
\boxed{
\frac{\mathcal S_Z(\delta)}
{\mathcal S_Z(0)}
=
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}}.
}
```

This is exactly equivalent to the earlier symmetric result after identifying

```math
\delta=2\eta.
```

The important improvement is conceptual:

> the action enhancement is controlled by the ratio of the gap slope to the useful conduction slope, not by a convention-dependent decomposition of the gap change between the two bands.

---

## 5. Monotonicity

Define

```math
R(\delta)
=\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}}.
```

Then

```math
\frac{d\ln R}{d\delta}
=-\frac{2}{2-\delta}
+\frac{3}{2(1-\delta)}.
```

Therefore

```math
\boxed{
\frac{d\ln R}{d\delta}
=\frac{2+\delta}
{2(2-\delta)(1-\delta)}>0
}
```

for

```math
0\le\delta<1.
```

So any positive gap slope at fixed conduction slope strictly increases the direct-Zener WKB action in this linear model.

As

```math
\delta\to1^{-},
```

```math
\boxed{\mathcal S_Z\to\infty.}
```

---

## 6. Finite grading resource

Over a finite graded length `L`,

```math
\Delta E_g=GL.
```

The useful conduction-band energy drop is

```math
\Delta E_c=SL.
```

Thus

```math
\boxed{
\delta
=\frac{\Delta E_g}{\Delta E_c}.
}
```

The ideal direct-Zener closure condition is therefore simply

```math
\boxed{
\Delta E_g\ge\Delta E_c.
}
```

This statement is independent of `alpha`.

The band-offset partition does, however, determine how much common electrostatic tilt remains.

Since

```math
qF=S-\alpha G,
```

```math
\boxed{
qF
=S(1-\alpha\delta).
}
```

At the ideal closure point `delta=1`,

```math
\boxed{
qF=(1-\alpha)S.
}
```

For HgCdTe with `alpha approximately 2/3`, about one third of the useful conduction slope can still be electrostatic even when the valence slope is locally zero.

Across length `L`, the corresponding electrostatic voltage-energy drop is

```math
\boxed{
qV
=(1-\alpha\delta)\Delta E_c.
}
```

At `delta=1` and `alpha=2/3`,

```math
qV\approx\Delta E_c/3.
```

Thus direct-Zener geometric closure does not require zero applied field.

---

## 7. Add self-consistent Poisson curvature

Now allow a uniform net space-charge density

```math
\rho=qN_{\rm eff}
```

across the graded region.

With approximately constant permittivity,

```math
\boxed{
\frac{dF}{dx}
=\frac{qN_{\rm eff}}{\epsilon}.
}
```

Choose the coordinate origin at the region center so

```math
F(x)
=\bar F
+\frac{qN_{\rm eff}}{\epsilon}x,
\qquad
-L/2\le x\le L/2.
```

The local valence downhill slope is

```math
S_v(x)
=qF(x)-(1-\alpha)G.
```

Using the average conduction slope

```math
\bar S_c=q\bar F+\alpha G,
```

this becomes

```math
\boxed{
S_v(x)
=\bar S_c-G
+q[F(x)-\bar F].
}
```

Again, `alpha` cancels.

---

## 8. Robust no-downhill-valence condition

A sufficient condition that the valence band never tilts downhill anywhere in the finite region is

```math
S_v(x)\le0
```

for every `x`.

The largest field excursion from the mean is

```math
\max|F-\bar F|
=\frac{q|N_{\rm eff}|L}{2\epsilon}.
```

Therefore a sufficient worst-case condition is

```math
\boxed{
G-\bar S_c
\ge
\frac{q^2|N_{\rm eff}|L}
{2\epsilon}.
}
```

Multiplying by `L`,

```math
\boxed{
\Delta E_g-\Delta E_c
\ge
\frac{q^2|N_{\rm eff}|L^2}
{2\epsilon}.
}
```

This is the central finite-Poisson robustness result of this note.

Interpretation:

```text
ideal linear closure:
Delta Eg = Delta Ec

space-charge-robust closure:
Delta Eg must exceed Delta Ec
by enough bandgap headroom to absorb the Poisson field excursion.
```

The extra term scales as

```math
N_{\rm eff}L^2/\epsilon.
```

Thus long or heavily depleted graded regions demand more gap swing than the charge-neutral idealization.

---

## 9. Dimensionless Poisson headroom

Define

```math
\Pi_P
=\frac{q^2|N_{\rm eff}|L^2}
{2\epsilon\Delta E_c}.
```

Then the sufficient robust condition is

```math
\boxed{
\frac{\Delta E_g}{\Delta E_c}
\ge1+\Pi_P.
}
```

For

```math
\Pi_P\ll1,
```

the constant-field linear-edge approximation is self-consistent at the level of this criterion.

For

```math
\Pi_P\gtrsim1,
```

space charge is not a perturbation; the ideal linear-profile closure picture is no longer quantitatively trustworthy.

---

## 10. What has and has not been proved

### DERIVED

Within the stated one-dimensional linear-composition / uniform-space-charge model:

1. `S_v=S_c-G` exactly, independent of band-offset partition;
2. at fixed conduction slope,

```math
\mathcal S_Z(\delta)/\mathcal S_Z(0)
=(2-\delta)^2/[4(1-\delta)^{3/2}];
```

3. ideal direct-Zener geometric closure occurs at `Delta Eg = Delta Ec`;
4. a sufficient uniform-space-charge robustness condition is

```math
\Delta E_g-\Delta E_c
\ge q^2|N_{\rm eff}|L^2/(2\epsilon).
```

### KNOWN INPUT

HgCdTe electron-affinity/band-offset work indicates that approximately two thirds of a composition-induced gap change appears in the conduction band in technologically relevant graded HgCdTe.

### NON-CLAIMS

This note does not establish

- that satisfying the robust slope condition eliminates the full direct BTBT current;
- that no nonlocal interband path remains in a curved finite profile;
- that `N_eff` is uniform in a real detector;
- that mobile carriers can be neglected;
- that TAT, interface tunneling, or impact ionization are suppressed;
- that the result is novel.

---

## 11. Next decisive calculation

The next model should stop prescribing `N_eff` and instead solve it.

For a specific graded HgCdTe profile:

1. choose `x_Cd(x)` and compute `E_g(x)`;
2. use a modern HgCdTe electron-affinity relation for `E_c(x)` / `E_v(x)` partition;
3. specify donor/acceptor profiles;
4. solve Poisson with Fermi statistics at the operating temperature and bias;
5. evaluate the full Kane WKB action numerically from the resulting curved edges;
6. compare the result against TAT and nonlocal impact-ionization surrogates already in the repository.

The analytic condition above should then serve as a regression limit for the weak-space-charge case.