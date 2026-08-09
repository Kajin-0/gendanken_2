# HgCdTe Quasi-Neutral Grading Self-Consistency — Majority-Band Pinning and Minority-Carrier Drive

**Date:** 2026-08-09  
**Status:** analytic quasi-neutral equilibrium result; conditional on nondegenerate statistics and local charge neutrality; no novelty claim

## 1. Purpose

`HGCDTE_GRADED_POISSON_ROBUSTNESS.md` showed that a uniformly depleted multi-micron graded layer would require an enormous bandgap headroom once ordinary `10^14 cm^-3`-scale net space charge is inserted into Poisson's equation.

That indicates that a realistic graded detector cannot generally be modeled as a uniformly depleted slab over many microns.

The natural alternative is a **quasi-neutral graded interior** with electrostatic adjustment confined mainly to screening/boundary regions.

This note asks:

> In a quasi-neutral graded HgCdTe region, does self-consistent equilibrium electrostatics cancel the useful gap-gradient carrier drive, or can it naturally realize the band geometry that suppresses direct Zener overlap?

For p-type material collecting minority electrons, the answer is favorable.

---

## 2. Equilibrium identities

At thermal equilibrium the Fermi level is spatially constant.

For nondegenerate holes,

```math
p(x)
=N_v(x)
\exp\!\left[
\frac{E_v(x)-E_F}{k_BT}
\right].
```

Taking a derivative,

```math
\boxed{
\frac{dE_v}{dx}
=k_BT\frac{d}{dx}
\ln\!\left(\frac{p}{N_v}\right).
}
```

Likewise for nondegenerate electrons,

```math
n(x)
=N_c(x)
\exp\!\left[
\frac{E_F-E_c(x)}{k_BT}
\right],
```

so

```math
\boxed{
\frac{dE_c}{dx}
=-k_BT\frac{d}{dx}
\ln\!\left(\frac{n}{N_c}\right).
}
```

These equations already include the self-consistent electrostatic potential because `E_c` and `E_v` are the total equilibrium band edges.

---

## 3. Quasi-neutral p-type graded region

Suppose the graded region is p type and quasi neutral:

```math
\boxed{p(x)\simeq N_A(x).}
```

Then

```math
\boxed{
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}
\ln\!\left(\frac{N_A}{N_v}\right).
}
```

Define the positive downhill valence slope

```math
S_v\equiv-\frac{dE_v}{dx}.
```

Therefore

```math
\boxed{
S_v
\simeq
-k_BT\frac{d}{dx}
\ln\!\left(\frac{N_A}{N_v}\right).
}
```

For nearly constant acceptor density and slowly varying valence-band density of states,

```math
\boxed{S_v\approx0.}
```

The equilibrium electrostatic potential has adjusted so that the majority-hole band is almost pinned.

---

## 4. The gap gradient then appears in the minority-electron band

The exact identity

```math
E_g=E_c-E_v
```

gives

```math
\frac{dE_c}{dx}
=\frac{dE_v}{dx}
+\frac{dE_g}{dx}.
```

Define

```math
G\equiv-\frac{dE_g}{dx}>0
```

for a gap decreasing in the electron-collection direction.

With

```math
S_c\equiv-\frac{dE_c}{dx},
```

one obtains identically

```math
\boxed{
S_c=S_v+G.
}
```

Therefore in the quasi-neutral p-type limit

```math
S_v\approx0,
```

```math
\boxed{
S_c\approx G.
}
```

Thus most of the composition-induced gap slope appears as useful downhill conduction-band drive for minority electrons.

This is precisely the `delta -> 1` geometry of the linear graded-Kane WKB branch, where the conventional same-direction valence turning point recedes.

---

## 5. Connection to the graded-Kane parameter

`HGCDTE_GRADED_POISSON_ROBUSTNESS.md` defined

```math
\delta=G/S_c.
```

Since

```math
S_c=S_v+G,
```

```math
\boxed{
\delta
=\frac{G}{G+S_v}.
}
```

Using the quasi-neutral p-type expression,

```math
\boxed{
\delta
\simeq
\frac{G}
{G-k_BT\,d\ln(N_A/N_v)/dx}.
}
```

For constant `N_A/N_v`,

```math
\boxed{\delta\to1.}
```

Hence the favorable Zener geometry does not require an externally imposed cancellation of the valence slope; it can emerge from ordinary equilibrium charge neutrality.

---

## 6. Doping-gradient correction

The same formula shows immediately how a doping gradient helps or hurts.

### If

```math
\frac{d}{dx}\ln(N_A/N_v)>0,
```

then

```math
S_v<0.
```

The valence edge rises in the electron-collection direction, making the direct same-direction Zener geometry even less favorable.

### If

```math
\frac{d}{dx}\ln(N_A/N_v)<0,
```

then

```math
S_v>0.
```

The valence band acquires a downhill component and the conventional overlap path can reopen.

Therefore the majority-carrier doping profile is not an independent afterthought; it directly controls the residual valence slope after electrostatic self-consistency.

---

## 7. Opposite polarity: quasi-neutral n-type material

For quasi-neutral n-type material,

```math
n(x)\simeq N_D(x).
```

Then

```math
\boxed{
\frac{dE_c}{dx}
\simeq
-k_BT\frac{d}{dx}
\ln\!\left(\frac{N_D}{N_c}\right).
}
```

For nearly constant `N_D/N_c`,

```math
\boxed{S_c\approx0.}
```

so the equilibrium electrostatic potential largely pins the conduction band instead.

The gap gradient then appears mainly in the valence band.

Thus, for **minority-electron collection**, a quasi-neutral p-type graded region is the natural polarity in this simple equilibrium picture.

Conversely, n-type grading naturally favors minority-hole band-edge drive.

This is a polarity-selection result, not a claim that one detector architecture is universally superior.

---

## 8. Why this does not violate equilibrium

A tilted minority-carrier band does not imply a steady equilibrium current.

At equilibrium there are no excess minority carriers to sustain a photocurrent.

After photoexcitation, the nonequilibrium minority population experiences the graded band-edge force and can be swept toward collection while the majority carriers continue to maintain quasi-neutral electrostatic screening.

This is the usual physical meaning of a composition-induced quasi-electric field in a graded semiconductor.

---

## 9. Screening-length consistency

The quasi-neutral approximation requires the interior length scale to exceed the electrostatic screening length and the doping not to be fully depleted.

A useful nondegenerate scale is the Debye length

```math
\boxed{
\lambda_D
=\sqrt{
\frac{\epsilon k_BT}
{q^2 n_{\rm maj}}
}.
}
```

Using the standard HgCdTe static-permittivity parameterization near `x=0.20`,

```math
\epsilon_s\approx17.6\epsilon_0.
```

At `T=77 K`, representative scales are approximately

```text
n_maj = 1e14 cm^-3  -> lambda_D ~ 0.25 um
n_maj = 1e15 cm^-3  -> lambda_D ~ 0.08 um
n_maj = 1e16 cm^-3  -> lambda_D ~ 0.025 um
```

Thus a several-micron graded interior can plausibly be quasi neutral while electrostatic curvature is concentrated in submicron boundary regions.

These numbers are only screening estimates; narrow-gap degeneracy and incomplete ionization may require Thomas-Fermi/Fermi-Dirac corrections.

---

## 10. Relation to realistic HgCdTe band offsets

Recent HgCdTe electron-affinity analysis reports that approximately two thirds of a composition-induced gap change appears in the conduction band before electrostatic self-consistency is imposed.

That result matters for the **electrostatic field and voltage required** to realize a given total band landscape.

However, once the total equilibrium `E_c(x)` and `E_v(x)` are used, the direct-Zener geometry depends only on

```math
S_c-S_v=G,
```

not on the bookkeeping parameter used to partition the bare composition shift.

Thus the quasi-neutral result and the band-offset-invariant WKB reparameterization are mutually consistent.

---

## 11. What has been established

### DERIVED / CONDITIONAL

Under local equilibrium, nondegenerate statistics and quasi neutrality:

```math
\boxed{
S_v
\simeq
-k_BT\frac{d}{dx}\ln(N_A/N_v)
}
```

for a p-type graded region, and therefore

```math
\boxed{
S_c
\simeq
G-k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

For nearly constant `N_A/N_v`,

```math
\boxed{
S_v\approx0,
\qquad
S_c\approx G,
\qquad
\delta\approx1.
}
```

### Physical interpretation

> **In a quasi-neutral p-type graded HgCdTe absorber, equilibrium screening tends to pin the majority-hole band while leaving the gap gradient available as a minority-electron conduction-band slope.**

This is exactly the band geometry that suppresses the conventional same-direction direct-Zener overlap in the ideal graded-Kane model.

---

## 12. Non-claims and remaining attacks

This note does not establish

- a quantitative dark-current reduction in a real HgCdTe detector;
- validity in a fully depleted multiplication region;
- validity under degenerate carrier statistics without modification;
- suppression of TAT or interface-assisted leakage;
- suppression of nonlocal impact ionization;
- that the favorable interior survives at contacts/junctions;
- that the result is novel.

The most dangerous remaining regions are now the **boundaries**:

```text
quasi-neutral graded interior
-> favorable minority-carrier drive / weak valence slope

junction or contact transition
-> charge redistribution
-> strong local electrostatic curvature
-> possible TAT / BTBT / interface leakage.
```

---

## 13. Next decisive model

The next model should therefore be a finite p-type graded absorber connected to an explicit collection junction:

1. specify `x_Cd(x)` and `N_A(x)`;
2. solve Fermi-Dirac charge neutrality in the graded interior;
3. solve Poisson through the collection/depletion boundary;
4. calculate `E_c(x)` and `E_v(x)` continuously;
5. evaluate full-profile direct Kane WKB action;
6. evaluate TAT through the highest-field boundary region;
7. propagate a photoelectron through the same profile to obtain transit time.

The key question is no longer whether the **interior** grading can escape direct Zener overlap. The next question is whether the unavoidable **junction/boundary layer** reintroduces the dark-current penalty.