# HgCdTe Graded Optical Absorption Length — The Long-Wavelength Photon Only Sees Part of the Accelerator

**Date:** 2026-08-09  
**Status:** exact geometry plus conditional local-absorption bounds for a monotonic linear band-gap gradient; no novelty claim

## 1. Purpose

The material branch has so far treated the graded absorber mainly as a carrier-transport structure.

That is incomplete for a photodetector.

A photon of fixed energy can produce an ordinary interband transition only where the local band gap is sufficiently small.

Question:

> **If the absorber uses a large downhill band-gap span to accelerate minority electrons, how much of that same region can still absorb photons near the long-wavelength operating edge?**

For a linear gradient, the geometry is exact.

---

## 2. Linear graded gap

Let

```math
\boxed{
E_g(x)
=E_{g,\rm in}-Gx,
\qquad
0\le x\le L,
}
```

with

```math
G>0.
```

The exit gap is

```math
E_{g,\rm out}
=E_{g,\rm in}-GL.
```

Define the total downhill gap span

```math
\boxed{
\Delta E_g
=E_{g,\rm in}-E_{g,\rm out}
=GL.
}
```

Take a photon energy satisfying

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in}.
```

Define its excess above the narrow-gap endpoint

```math
\boxed{
\delta E
=E_\gamma-E_{g,\rm out}>0.
}
```

---

## 3. Absorption begins only after the local gap crosses the photon energy

The threshold position satisfies

```math
E_g(x_\gamma)=E_\gamma.
```

Hence

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

Only the remaining distance

```math
L_{\rm opt}=L-x_\gamma
```

can contribute to ordinary above-gap absorption at that photon energy.

Using the definitions above,

```math
\boxed{
L_{\rm opt}
=\frac{\delta E}{G}
=L\frac{\delta E}{\Delta E_g}.
}
```

Therefore the geometrically eligible optical fraction is

```math
\boxed{
f_{\rm opt}
=\frac{L_{\rm opt}}{L}
=\frac{\delta E}{\Delta E_g}.
}
```

This is clipped to `0 <= f_opt <= 1` outside the stated energy ordering.

---

## 4. Immediate interpretation

At fixed photon energy above the narrow-gap endpoint,

```text
larger downhill gap span Delta Eg
-> stronger total available band-edge drive
-> smaller fraction of the accelerator lies below E_gamma
-> less geometrical length is available for long-wavelength absorption.
```

Thus the same gap span that helps transport can work against near-edge optical absorption.

This is a distinct mechanism from direct-Zener tunneling and impact ionization.

---

## 5. General single-pass absorption bound

Let

```math
\alpha(E_\gamma,x)
```

be the local absorption coefficient in the eligible region.

The single-pass optical depth is

```math
\boxed{
\tau_{\rm opt}
=\int_{x_\gamma}^{L}
\alpha(E_\gamma,x)dx.
}
```

Suppose only that

```math
\alpha(E_\gamma,x)\le\alpha_{\max}
```

through that region.

Then

```math
\boxed{
\tau_{\rm opt}
\le
\alpha_{\max}L
\frac{\delta E}{\Delta E_g}.
}
```

For a desired single-pass absorptance

```math
\eta_{\rm opt}
=1-e^{-\tau_{\rm opt}},
```

the required optical depth is

```math
\tau_*
=-\ln(1-\eta_{\rm opt}).
```

Therefore a necessary graded-region length is

```math
\boxed{
L
\ge
L_{\rm abs}^{\rm min}
\equiv
\frac{\Delta E_g}{\delta E}
\frac{-\ln(1-\eta_{\rm opt})}
{\alpha_{\max}}.
}
```

This is a deliberately conservative geometry-plus-absorption bound. It does not assume a detailed HgCdTe absorption spectrum.

---

## 6. Near-edge direct-absorption model

For an illustrative local direct-edge law

```math
\boxed{
\alpha(E_\gamma,x)
=C[E_\gamma-E_g(x)]^\beta,
\qquad
E_\gamma>E_g(x),
}
```

with

```math
\beta>-1,
```

the optical depth can be integrated exactly.

Use

```math
u
=E_\gamma-E_g(x).
```

Across the eligible region,

```math
0\le u\le\delta E,
```

and

```math
dx=du/G.
```

Therefore

```math
\boxed{
\tau_{\rm opt}
=\frac{C}{G}
\frac{(\delta E)^{\beta+1}}
{\beta+1}.
}
```

Using `G=Delta Eg/L`,

```math
\boxed{
\tau_{\rm opt}
=
\frac{CL}{(\beta+1)\Delta E_g}
(\delta E)^{\beta+1}.
}
```

Hence the required length for optical depth `tau_*` is

```math
\boxed{
L
\ge
\frac{(\beta+1)\Delta E_g}
{C(\delta E)^{\beta+1}}
\tau_*.
}
```

For the familiar parabolic direct-edge exponent `beta=1/2`,

```math
\boxed{
\tau_{\rm opt}
=\frac{2CL}{3\Delta E_g}
(\delta E)^{3/2}.
}
```

HgCdTe is strongly nonparabolic, so `beta=1/2` should be treated only as an illustrative analytic baseline rather than a precision HgCdTe law.

---

## 7. Combine optical length with the hot-electron relaxation length

The absorber must satisfy both

```math
L\ge L_{\rm abs}^{\rm min}
```

and, when the chosen grading span is beyond the ballistic mean-II-safe regime,

```math
L\ge\ell_Er_{\min}(\zeta,\chi).
```

Therefore

```math
\boxed{
L_a
\ge
\max\left[
L_{\rm abs}^{\rm min},
\ell_Er_{\min}
\right].
}
```

With the simplified Kane group-velocity ceiling,

```math
\boxed{
T_a
\ge
\frac1{v_K}
\max\left[
L_{\rm abs}^{\rm min},
\ell_Er_{\min}
\right].
}
```

This is the first direct reconnection of the graded transport branch to an optical absorption requirement.

---

## 8. Add the collection boundary

Using the minimum boundary width from `HGCDTE_BOUNDARY_COOLING_TRANSIT_FLOOR.md`,

```math
w_b^{\min}
=
\max\left[
\ell_{E,b}\ln(1/c),
 w_{\rm TAT},
 w_Z
\right],
```

the conditional total transit bound becomes

```math
\boxed{
T_{\rm total}
\ge
\frac1{v_K}
\left\{
\max\left[
L_{\rm abs}^{\rm min},
\ell_{E,a}r_{\min}
\right]
+
w_b^{\min}
\right\}.
}
```

This combines three previously separate resources:

```text
optical absorption length
+
absorber energy-relaxation length
+
boundary voltage-handling / cooling length.
```

The actual device can be slower.

---

## 9. What passive optical trapping changes

A resonator, waveguide, photon-trapping structure, or antenna can increase the optical path length relative to the physical absorbing length.

That can relax the single-pass `L_abs` requirement.

But the opening branches of this repository already showed that optical concentration/trapping introduces separate coupling, dwell-time, bandwidth, and access resources.

Therefore optical trapping is a legitimate escape, but it should be represented as an explicit optical-path enhancement factor rather than silently setting `L_abs -> 0`.

A future model may introduce

```math
\mathcal P_{\rm opt}
=\frac{\text{effective absorbing path}}
{\text{physical eligible absorbing length}}
```

and replace

```math
L_{\rm opt}
```

by

```math
\mathcal P_{\rm opt}L_{\rm opt}.
```

Then the optical-resource question reconnects naturally to the earlier passive-access bounds.

---

## 10. Design consequence

The wide-gap range has three asymmetric uses:

```text
large downhill gap span in absorber
-> more carrier drive
-> more hot-electron risk
-> smaller long-wavelength-eligible absorbing fraction

large gap rise in collection boundary
-> higher leakage tolerance potential
-> larger compensation voltage
-> no added downhill carrier work at minimum compensation

optical trapping
-> can recover absorption from short eligible material
-> spends a separate optical coupling/path-length resource.
```

This is much closer to the original thought experiment than an active-volume-only law.

---

## 11. Claim boundary

### Derived / conditional

For a linear monotonic gap and photon energy inside the gap range,

```math
\boxed{
f_{\rm opt}=\delta E/\Delta E_g.}
```

Under `alpha <= alpha_max`,

```math
\boxed{
L\ge
\frac{\Delta E_g}{\delta E}
\frac{-\ln(1-\eta_{\rm opt})}{\alpha_{\max}}.
}
```

and the absorber must obey

```math
\boxed{
L_a\ge
\max[L_{\rm abs}^{\rm min},\ell_Er_{\min}].
}
```

### Not established

- a calibrated HgCdTe absorption coefficient near the target wavelength;
- the role of Urbach tails / disorder-assisted absorption;
- excitonic or many-body corrections;
- a universal path-enhancement factor;
- novelty of the geometry rearrangement;
- a complete external quantum-efficiency model.

---

## 12. Next decisive question

The next useful optimization is now well posed:

> **For a target photon energy and desired quantum efficiency, what grading span minimizes total response time when the design must simultaneously provide enough optically eligible absorbing path and remain below the nonlocal hot-electron phase boundary?**

That optimization can be done dimensionlessly first and will reveal whether the fastest absorber prefers

- weak grading and more physical absorption length;
- stronger grading plus more energy-relaxation length;
- or strong optical path enhancement with a very short narrow-gap absorbing section.
