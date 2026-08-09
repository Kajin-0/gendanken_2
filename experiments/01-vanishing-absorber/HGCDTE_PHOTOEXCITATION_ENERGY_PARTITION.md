# HgCdTe Photoexcitation Energy Partition — Correction to the Wavelength-Resolved Transport Branch

**Date:** 2026-08-09  
**Status:** correction; exact within a parameterized direct-transition energy-partition model, with a symmetric two-band Kane special case; no novelty claim

## 1. Correction

The first wavelength-resolved transport note treated every generated electron as cold at the local conduction-band edge.

That is only exact at the earliest allowed generation point where

```math
E_\gamma=E_g(x).
```

If the photon is absorbed farther downstream, then

```math
E_\gamma>E_g(x)
```

and the photoelectron is born with nonzero excess energy.

This must be included before predicting wavelength-resolved hot-electron exposure or transit time.

---

## 2. Parameterize the electron share of photon excess

Define the local photon excess

```math
\boxed{
u
=E_\gamma-E_g(x)\ge0.}
```

Let the electron receive fraction

```math
\boxed{0\le\xi_e\le1}
```

of that excess at generation:

```math
\boxed{
\varepsilon_{\rm gen}
=\xi_e\nu.
}
```

The remainder belongs to the hole and/or other degrees of freedom of the optical transition.

For simple parabolic conduction/valence bands with vertical momentum conservation,

```math
\xi_e
=\frac{m_h}{m_e+m_h}.
```

For the symmetric two-band Kane model used elsewhere in this repository,

```math
\boxed{\xi_e=1/2.}
```

Real HgCdTe requires a multiband optical-transition model; do not assume `xi_e=1/2` as a calibrated material value.

---

## 3. Remaining downhill conduction-band drop

Let

```math
E_0=E_{g,\rm out}
```

and

```math
\delta E=E_\gamma-E_0.
```

For a photon absorbed at a point where its local excess is `u`, the local gap is

```math
E_g=E_\gamma-u.
```

The remaining downhill conduction-band drop to the output is therefore

```math
\boxed{
D(u)
=E_g-E_0
=\delta E-u.
}
```

The photoelectron starts with

```math
\boxed{
\varepsilon_{\rm gen}(u)
=\xi_e u.
}
```

So later generation reduces the remaining band-edge work but increases the initial kinetic energy.

---

## 4. Mean-energy propagation with relaxation

For constant downstream gap slope `G` and constant energy-relaxation length `ell_E`, the remaining distance is

```math
\boxed{d(u)=D(u)/G.}
```

The mean-energy equation

```math
\frac{d\varepsilon}{dx}
=G-\frac{\varepsilon}{\ell_E}
```

with nonzero initial condition

```math
\varepsilon(0)=\xi_eu
```

gives

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

This supersedes the cold-injection wavelength-resolved energy formula for downstream generation positions.

At the earliest allowed generation point

```math
u=0,
```

it reduces to the previous cold-injection result.

---

## 5. Ballistic limit

For

```math
\ell_E\to\infty,
```

```math
\boxed{
\varepsilon_{\rm out}^{\rm bal}(u)
=\delta E-(1-\xi_e)u.
}
```

Therefore the earliest allowed absorption position remains the largest-output-energy case:

```math
\boxed{
\varepsilon_{\rm out,max}^{\rm bal}
=\delta E.
}
```

The latest possible generation point at the output gives

```math
\boxed{
\varepsilon_{\rm out,min}^{\rm bal}
=\xi_e\delta E.
}
```

So the extent to which later generation reduces hot-electron energy depends strongly on `xi_e`.

### Symmetric two-band Kane special case

For

```math
\xi_e=1/2,
```

```math
\boxed{
\varepsilon_{\rm out}^{\rm bal}
=\delta E-u/2.
}
```

### Heavy-hole / light-electron limit

If

```math
\xi_e\to1,
```

then

```math
\boxed{
\varepsilon_{\rm out}^{\rm bal}
\to\delta E
}
```

independent of generation position.

Thus generation farther downstream can strongly reduce transit distance without proportionally reducing the final electron energy when most photon excess is initially placed in the electron.

This is especially important for narrow-gap HgCdTe, where a simple symmetric energy partition should not be assumed without checking the multiband transition physics.

---

## 6. Ballistic mean-II safety remains controlled by the earliest allowed position

The current threshold surrogate at the output is

```math
E_{\rm th,out}=\chi E_0.
```

Because

```math
\varepsilon_{\rm out}^{\rm bal}(u)
\le\delta E
```

for `0 <= xi_e <= 1`, the earliest allowed position `u=0` remains the worst ballistic generation position.

Therefore the sufficient all-generation-position ballistic mean-safety condition remains

```math
\boxed{
\delta E<\chi E_0.
}
```

or

```math
\boxed{
E_\gamma<(1+\chi)E_{g,\rm out}.
}
```

The earlier wavelength-level worst-case safety criterion therefore survives this correction.

What changes is the fraction of downstream-generated carriers that approach threshold and their transit-time distribution.

---

## 7. Exact symmetric two-band optical transition

Inside the symmetric two-band model

```math
E_\pm(k,x)
=U(x)
\pm
\sqrt{\Delta(x)^2+(\hbar v_Kk)^2},
```

with pinned valence-band edge

```math
U=\Delta=E_g/2.
```

A vertical interband transition of photon energy `E_gamma` obeys

```math
E_+(k)-E_-(k)=E_\gamma.
```

Hence

```math
\sqrt{(E_g/2)^2+(\hbar v_Kk)^2}
=E_\gamma/2.
```

The photoelectron energy is

```math
E_e
=E_g/2+E_\gamma/2,
```

so its excess above the local conduction edge is

```math
\boxed{
E_e-E_g
=\frac{E_\gamma-E_g}{2}.
}
```

Thus the exact symmetric-model partition is indeed

```math
\boxed{\xi_e=1/2.}
```

---

## 8. Exact ballistic transit for nonzero initial energy

Treat the downstream conduction band with the same two-band Kane dispersion and let the electron have conserved total energy

```math
\boxed{
\mathcal E
=E_g(x_s)+\varepsilon_{\rm gen}.
}
```

For the parameterized partition,

```math
\boxed{
\mathcal E
=E_\gamma-(1-\xi_e)u.
}
```

Define

```math
z_s
=\mathcal E-E_g(x_s)
=\xi_eu,
```

and

```math
z_0
=\mathcal E-E_0
=\delta E-(1-\xi_e)u.
```

For a linear gap slope `G`, direct integration gives

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

with

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

At `u=0`, this reduces to the earlier cold-edge ballistic formula.

At `u=delta E`, `z_s=z_0` and the geometric transit time correctly vanishes.

---

## 9. Corrected physical interpretation

The wavelength-resolved gradient still produces spectral sorting, but two effects must be kept separate:

```text
later generation
-> shorter remaining distance
-> shorter transit time

later generation
-> larger initial photon-excess energy
-> partially offsets the reduction in downstream band-edge work.
```

Therefore

> **generation closer to the contact is unambiguously favorable for transit distance, but not necessarily by the same factor for hot-electron energy.**

The degree of hot-electron benefit is controlled by the optical energy-partition factor `xi_e` and by subsequent energy relaxation.

---

## 10. Consequences for existing repository notes

The following statements remain valid:

- the earliest allowed generation position is set by `E_g(x)=E_gamma`;
- the remaining geometric distance is wavelength dependent;
- the earliest allowed generation point is the worst hot-electron case in the present model;
- the all-position ballistic safety condition `delta E < chi E_g,out` remains sufficient;
- the exact optical-depth generation distribution remains valid.

The following must be corrected:

- downstream-generated photoelectrons are not generally cold;
- mean-energy threshold fractions must include `epsilon_gen`;
- ballistic transit statistics must use the nonzero-initial-energy formula above;
- any claim that later generation removes the full corresponding hot-electron energy is too strong.

---

## 11. Next step

Update the wavelength-resolved generation/transport notes to use `xi_e` explicitly.

Then determine whether a realistic HgCdTe optical-transition model makes

```math
\xi_e\approx1/2
```

or instead strongly biases the photon excess into the conduction electron in the wavelength/composition regime of interest.

Until that is resolved, keep spectral transit **distance** predictions stronger than spectral hot-electron-energy predictions.
