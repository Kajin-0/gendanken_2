# HgCdTe Spectral Generation and Transport — Wavelength Sets Generation Geometry, Not Necessarily Full Hot-Electron Energy

**Date:** 2026-08-09  
**Status:** corrected wavelength-resolved geometry and transport baseline for a linear quasi-neutral graded absorber; downstream photoexcitation excess energy handled explicitly; no novelty claim

## 1. Core geometric result

Use a linear decreasing gap

```math
\boxed{
E_g(x)=E_{g,\rm in}-Gx,
\qquad
0\le x\le L,
}
```

with

```math
E_{g,\rm out}=E_{g,\rm in}-GL.
```

Assume the favorable quasi-neutral p-type limit

```math
E_v\approx\text{constant},
```

so the conduction band falls with slope

```math
S_c=G.
```

For a photon with

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

ordinary above-gap absorption cannot begin until

```math
E_g(x_\gamma)=E_\gamma.
```

Therefore

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

The maximum remaining graded distance is

```math
\boxed{
d_\gamma
=L-x_\gamma
=\frac{E_\gamma-E_{g,\rm out}}{G}.
}
```

This geometry is exact inside the monotonic local-gap model.

---

## 2. Earliest allowed generation point

Define

```math
\boxed{
\delta E
=E_\gamma-E_{g,\rm out}.
}
```

At the earliest allowed generation point,

```math
E_g=E_\gamma,
```

so the photoelectron is born at the local absorption edge with zero photon-excess kinetic energy in the ideal direct-transition model.

Its remaining downhill conduction-band drop is exactly

```math
\boxed{D_{\max}=\delta E.}
```

Therefore the earliest allowed position remains the worst case for downstream band-edge work.

A transparent wider-gap section upstream of `x_gamma` does not add carrier work for that wavelength because the photon cannot be absorbed there in the ideal local-gap model.

---

## 3. Downstream generation is not cold — correction

If the photon is absorbed farther downstream, define the local photon excess

```math
\boxed{
u=E_\gamma-E_g(x)>0.}
```

The remaining downhill conduction-band drop is

```math
\boxed{D(u)=\delta E-u.}
```

But the electron is also born with nonzero kinetic excess.

Parameterize the electron share as

```math
\boxed{
\varepsilon_{\rm gen}=\xi_eu,
\qquad 0\le\xi_e\le1.
}
```

For the symmetric two-band Kane optical transition,

```math
\boxed{\xi_e=1/2.}
```

Real HgCdTe requires a multiband transition calculation; do not assume `xi_e=1/2` quantitatively.

See `HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`.

---

## 4. Wavelength-resolved mean-energy propagation

For constant downstream gradient `G` and energy-relaxation length `ell_E`, the remaining distance is

```math
\boxed{d(u)=(\delta E-u)/G.}
```

The mean energy obeys

```math
\frac{d\varepsilon}{ds}
=G-\frac{\varepsilon}{\ell_E}
```

with

```math
\varepsilon(0)=\xi_eu.
```

Hence the exit mean excess energy is

```math
\boxed{
\varepsilon_{\rm out}(u)
=
\xi_eu
\exp\!\left[-\frac{\delta E-u}{G\ell_E}\right]
+
G\ell_E
\left\{
1-
\exp\!\left[-\frac{\delta E-u}{G\ell_E}\right]
\right\}.
}
```

At the earliest allowed point `u=0`, this reduces to the earlier cold-injection expression

```math
\boxed{
\varepsilon_{\rm out}(0)
=G\ell_E
\left[1-e^{-\delta E/(G\ell_E)}\right].
}
```

---

## 5. Ballistic limit

For `ell_E -> infinity`,

```math
\boxed{
\varepsilon_{\rm out}^{\rm bal}(u)
=\delta E-(1-\xi_e)u.
}
```

Thus

```math
\boxed{
\varepsilon_{\rm out,max}^{\rm bal}
=\delta E
}
```

at the earliest allowed generation point.

At the latest possible generation point `u=delta E`,

```math
\boxed{
\varepsilon_{\rm out,min}^{\rm bal}
=\xi_e\delta E.
}
```

Consequently, later generation always reduces geometric transit distance, but how much it reduces final hot-electron energy depends on the optical energy-partition factor.

For `xi_e -> 1`, the final ballistic electron energy becomes nearly independent of generation position.

---

## 6. Wavelength-level worst-case mean-II safety

Use the output threshold surrogate

```math
E_{\rm th,out}=\chi E_{g,\rm out}.
```

Because the earliest allowed position has the largest remaining band-edge work and zero initial photon-excess energy, the all-generation-position **ballistic** sufficient condition remains

```math
\boxed{
\delta E<\chi E_{g,\rm out}.
}
```

Equivalently,

```math
\boxed{
E_\gamma<(1+\chi)E_{g,\rm out}.
}
```

or approximately

```math
\boxed{
\lambda_\gamma
>
\frac{\lambda_{c,\rm out}}{1+\chi}.
}
```

For `chi=1`, this is the conditional half-cutoff wavelength rule.

This is a deterministic mean-energy criterion, not a stochastic zero-ionization theorem.

---

## 7. Exact ballistic transit with photoexcitation excess

Let the local generation gap be

```math
E_g(x_s)=E_\gamma-u.
```

The electron total energy in the parameterized conduction-band trajectory is

```math
\boxed{
\mathcal E
=E_\gamma-(1-\xi_e)u.
}
```

Define

```math
z_s=\xi_eu,
```

```math
z_0=\delta E-(1-\xi_e)u.
```

For the two-band Kane conduction dispersion and linear downstream gap,

```math
\boxed{
T_{\rm bal}(u)
=
\frac1{Gv_K}
\left[
\Phi(z_0;\mathcal E)
-
\Phi(z_s;\mathcal E)
\right],
}
```

where

```math
\boxed{
\Phi(z;\mathcal E)
=
\sqrt{\mathcal Ez}
+
\frac{z^{3/2}}
{3\sqrt{\mathcal E}}.
}
```

At `u=0` this reduces to the cold-edge formula. At `u=delta E` the geometric transit time vanishes.

Thus wavelength and generation position still produce a strong transit-time distribution even after the initial kinetic-energy correction.

---

## 8. Corrected spectral sorting picture

The gradient creates the robust geometric chain

```text
longer wavelength
-> absorption becomes allowed farther downstream
-> smaller maximum remaining transport distance
-> shorter possible carrier transit.
```

Within a fixed wavelength channel,

```text
later generation
-> shorter remaining distance
-> larger initial photon-excess kinetic energy.
```

Therefore the strongest statements are

- **generation distance and transit geometry are wavelength dependent**;
- **hot-electron energy is wavelength and energy-partition dependent**.

Do not claim that later generation removes the full corresponding hot-electron energy.

---

## 9. Near-cutoff limit

As

```math
E_\gamma\to E_{g,\rm out}^{+},
```

```math
\delta E\to0,
```

so both the maximum eligible transport distance

```math
d_\gamma=\delta E/G
```

and the worst-case ballistic electron excess at the output tend to zero.

The opposing effect is optical: the eligible absorbing length and local absorption coefficient also shrink toward the band edge.

Thus the near-cutoff problem remains

```text
short transport
versus
weak absorption.
```

---

## 10. Claim boundary

### Exact / robust within the stated band geometry

```math
\boxed{x_\gamma=(E_{g,\rm in}-E_\gamma)/G}
```

and

```math
\boxed{d_\gamma=(E_\gamma-E_{g,\rm out})/G}
```

for photons whose energy lies inside the graded gap range.

### Conditional

Mean-energy and ballistic timing expressions depend on `ell_E`, the two-band Kane conduction model, and the electron photon-excess fraction `xi_e`.

### Not established

- calibrated HgCdTe `xi_e(E_gamma,x)`;
- actual generation-position distribution;
- scattering-limited transit times;
- stochastic II probability;
- full wavelength-resolved detector impulse response;
- novelty.

---

## 11. Next decisive calculation

Use the exact conditional optical-depth generation distribution from `HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`, but propagate each event with the corrected nonzero initial energy above.

The key material question is now explicit:

> **What fraction of direct-transition photon excess enters the conduction electron in the HgCdTe wavelength/composition regime of interest?**

Until that is calibrated, the generation-position / transit-distance prediction is stronger than the hot-electron-energy prediction.
