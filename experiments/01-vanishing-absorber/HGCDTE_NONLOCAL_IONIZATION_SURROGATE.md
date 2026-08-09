# HgCdTe Nonlocal Impact-Ionization Surrogate — From Dead Space to Bulk Energy Relaxation

**Date:** 2026-08-09  
**Status:** analytic mean-energy surrogate that interpolates finite dead space and bulk energy relaxation; uses established energy-dependent HgCdTe II functional form only as a model input; no novelty claim

## 1. Purpose

`HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md` showed that a finite collection/multiplication region cannot be assigned a meaningful impact-ionization ceiling from a bulk field-onset statement alone.

The next requirement is an energy history.

A full Monte Carlo simulation would track electron momentum, nonparabolic dispersion, phonon emission/absorption, alloy/impurity scattering, and impact ionization event by event.

Before doing that, this note asks whether the **minimum nonlocal structure** can be written analytically.

The answer is yes if the carrier energy is represented by one relaxation time.

This is a surrogate, not a calibrated HgCdTe transport model.

---

## 2. Mean-energy equation

Let

```math
\varepsilon(t)
=E(t)-E_0
```

be the electron excess energy relative to its injected value.

Take constant field `F`, constant drift speed `v` over the region, and one energy-relaxation time `tau_E`:

```math
\boxed{
\frac{d\varepsilon}{dt}
=qFv-
\frac{\varepsilon}{\tau_E}.
}
```

The first term is electrical work rate.

The second term is a coarse-grained energy-loss term representing the tendency of phonon/scattering processes to relax the electron toward its injected energy.

With cold initial condition

```math
\varepsilon(0)=0,
```

the exact solution is

```math
\boxed{
\varepsilon(t)
=qFv\tau_E
\left(1-e^{-t/\tau_E}\right).
}
```

Define the energy-relaxation length

```math
\boxed{
\ell_E=v\tau_E.
}
```

For a region of length `L`, the transit time is

```math
T=L/v,
```

so the exit energy gain is

```math
\boxed{
\varepsilon(L)
=qF\ell_E
\left(1-e^{-L/\ell_E}\right).
}
```

---

## 3. Effective acceleration length

Define

```math
\boxed{
L_{\rm eff}
\equiv
\ell_E
\left(1-e^{-L/\ell_E}\right).
}
```

Then

```math
\boxed{
\varepsilon(L)=qF L_{\rm eff}.
}
```

This gives two exact limits of the surrogate.

### Short region

If

```math
L\ll\ell_E,
```

then

```math
L_{\rm eff}
=L+O(L^2/\ell_E),
```

so

```math
\varepsilon(L)\simeq qFL.
```

This reproduces the cold ballistic field-work dead-space result.

### Long region

If

```math
L\gg\ell_E,
```

then

```math
L_{\rm eff}\to\ell_E,
```

and

```math
\varepsilon\to qF\ell_E.
```

The mean electron energy saturates because energy loss balances field work.

This is the minimal bridge between finite dead space and a bulk-like stationary hot-electron energy.

---

## 4. Mean-energy threshold field

Let the impact-ionization threshold be

```math
E_{\rm th}
=E_0+\Delta E_{\rm th}.
```

The mean-energy trajectory reaches threshold somewhere within the region only if the exit energy does:

```math
qF L_{\rm eff}
\ge
\Delta E_{\rm th}.
```

Therefore

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=
\frac{\Delta E_{\rm th}}
{qL_{\rm eff}}
=
\frac{\Delta E_{\rm th}}
{q\ell_E(1-e^{-L/\ell_E})}.
}
```

For cold injection and

```math
E_{\rm th}=\chi E_g,
```

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=
\frac{\chi E_g}
{q\ell_E(1-e^{-L/\ell_E})}.
}
```

This is a **mean-energy threshold**, not a statement that the stochastic high-energy tail has zero ionization probability below it.

That distinction matters in bulk Monte Carlo transport.

---

## 5. Kane normalization

Use

```math
\ell_K
=\frac{\hbar v_K}{E_g}
```

and

```math
F_K
=\frac{\pi E_g^2}
{4q\hbar v_K}.
```

For cold injection with `E_th = chi E_g`, the mean threshold has the exact normalized form

```math
\boxed{
\frac{F_{\rm th}^{(\rm mean)}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L_{\rm eff}}.
}
```

This generalizes the dead-space result

```math
F_{\rm dead}/F_K
=(4\chi/\pi)(\ell_K/L)
```

by replacing the geometric length with the effective acceleration length.

Thus the relevant dimensionless variable is not always

```math
L/\ell_K,
```

but

```math
\boxed{
L_{\rm eff}/\ell_K.
}
```

---

## 6. Threshold time / threshold position

Let the steady mean excess energy be

```math
\boxed{
\varepsilon_{\rm ss}
=qF\ell_E.
}
```

If

```math
\varepsilon_{\rm ss}
\le
\Delta E_{\rm th},
```

the mean-energy trajectory never reaches threshold, even in an arbitrarily long region.

If

```math
\varepsilon_{\rm ss}
>
\Delta E_{\rm th},
```

the exact threshold time is obtained from

```math
\varepsilon(t_d)
=\Delta E_{\rm th}.
```

Hence

```math
\boxed{
t_d
=
\tau_E
\ln\!\left[
\frac{\varepsilon_{\rm ss}}
{\varepsilon_{\rm ss}-\Delta E_{\rm th}}
\right].
}
```

The corresponding mean-energy dead-space distance is

```math
\boxed{
x_d
=v t_d
=
\ell_E
\ln\!\left[
\frac{\varepsilon_{\rm ss}}
{\varepsilon_{\rm ss}-\Delta E_{\rm th}}
\right].
}
```

At very large field,

```math
\Delta E_{\rm th}/\varepsilon_{\rm ss}\ll1,
```

so

```math
x_d
\simeq
\frac{\Delta E_{\rm th}}{qF},
```

recovering the ballistic dead-space expression.

---

## 7. Add the energy-dependent ionization rate

The 2026 HgCdTe APD Monte Carlo model uses a Kinch/Keldysh-type rate

```math
\boxed{
\Gamma_{\rm II}(E)
=
A
\frac{(E/E_{\rm th}-1)^\alpha}
{(E/E_{\rm th})^\beta},
\qquad
E\ge E_{\rm th},
}
```

and zero below threshold.

The article reports that its comparison to full-band HgCdTe calculations favors a relatively soft onset near

```math
\alpha\simeq1,
\qquad
\beta\simeq0
```

for the studied SWIR/MWIR calibrations.

Those fitted parameters are **not** automatically transferable to `Hg_0.8Cd_0.2Te` at 77 K.

Nevertheless, `alpha=1`, `beta=0` is useful as an analytic test case.

---

## 8. Closed-form ionization hazard for the `alpha=1, beta=0` surrogate

For clarity set

```math
E_0=0,
\qquad
E_{\rm th}>0,
```

and define

```math
E_{\rm ss}=qF\ell_E.
```

The mean trajectory is

```math
E(t)
=E_{\rm ss}
\left(1-e^{-t/\tau_E}\right).
```

For

```math
E_{\rm ss}>E_{\rm th},
```

the threshold time is

```math
\boxed{
t_d
=\tau_E
\ln\!\left[
\frac{E_{\rm ss}}
{E_{\rm ss}-E_{\rm th}}
\right].
}
```

Let

```math
T=L/v.
```

If

```math
T\le t_d,
```

then this mean-energy surrogate gives

```math
\boxed{P_{\rm II}=0.}
```

If

```math
T>t_d,
```

and

```math
\Gamma_{\rm II}(E)
=A(E/E_{\rm th}-1),
```

the integrated hazard is

```math
\Xi_{\rm II}
=\int_{t_d}^{T}
\Gamma_{\rm II}[E(t)]dt.
```

Direct integration gives

```math
\boxed{
\Xi_{\rm II}
=
\frac{A}{E_{\rm th}}
\left\{
(E_{\rm ss}-E_{\rm th})
(T-t_d)
+
E_{\rm ss}\tau_E
\left[
e^{-T/\tau_E}
-e^{-t_d/\tau_E}
\right]
\right\}.
}
```

Equivalently, using

```math
e^{-t_d/\tau_E}
=1-E_{\rm th}/E_{\rm ss},
```

```math
\boxed{
\Xi_{\rm II}
=
\frac{A}{E_{\rm th}}
\left[
(E_{\rm ss}-E_{\rm th})
(T-t_d-\tau_E)
+
E_{\rm ss}\tau_E e^{-T/\tau_E}
\right].
}
```

The event probability under the Poisson-hazard approximation is

```math
\boxed{
P_{\rm II}
=1-e^{-\Xi_{\rm II}}.
}
```

This is the first closed nonlocal `P_II(F,L)` surrogate in the repository.

---

## 9. Why this is preferable to a guessed `alpha(F)`

The surrogate keeps three distinct pieces of physics visible:

```text
F, v
-> electrical power delivered to the carrier

tau_E
-> energy-loss / thermalization resource

Gamma_II(E)
-> microscopic pair-creation probability once threshold is reached.
```

A field-only ionization coefficient collapses these into one empirical curve.

That can be appropriate in a thick local-equilibrium multiplication region, but it obscures the nonlocal dead-space physics precisely when the detector is made thin and fast.

---

## 10. Important stochastic limitation

The mean-energy ODE is **not** a replacement for Monte Carlo transport.

In particular, impact ionization can be driven by the high-energy tail even when

```math
\langle E\rangle<E_{\rm th}.
```

Therefore

```math
F_{\rm th}^{(\rm mean)}
```

is not a strict onset field for the true stochastic process.

Its value is organizational:

- it recovers finite dead space in the short-device limit;
- it recovers a bulk energy-relaxation ceiling in the long-device limit;
- it identifies `L_eff/ell_K` as the natural dimensionless acceleration length;
- it provides an analytic trajectory on which a calibrated energy-dependent rate can be integrated.

---

## 11. Claim boundary

### Derived exactly within the stated one-relaxation-time surrogate

```math
\boxed{
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}),
}
```

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=\frac{\Delta E_{\rm th}}
{qL_{\rm eff}},
}
```

```math
\boxed{
\frac{F_{\rm th}^{(\rm mean)}}{F_K}
=\frac{4\chi}{\pi}
\frac{\ell_K}{L_{\rm eff}}
}
```

for cold injection and `E_th=chi E_g`, plus the closed hazard above for `alpha=1`, `beta=0`.

### Established prior physics

- HgCdTe II probability is energy dependent;
- threshold is close to `E_g` in the simplified e-APD models considered in current literature;
- history-dependent/dead-space treatment is required in thin avalanche regions;
- phonon energy exchange and hot-electron dynamics control the carrier energy history.

### Not established

- a calibrated `tau_E(F)` or `ell_E(F)` for `Hg_0.8Cd_0.2Te` at 77 K;
- a calibrated `A, alpha, beta` for that target composition and temperature;
- validity of constant `v` and constant `tau_E` over the full trajectory;
- a true stochastic II onset field;
- a complete APD gain/noise model;
- novelty of the surrogate.

---

## 12. Next decisive test

The next useful data target is now precise:

> recover `tau_E(F)` / energy-relaxation-rate data and an energy-dependent `Gamma_II(E)` for `Hg_0.8Cd_0.2Te` at 77 K.

Palermo et al. explicitly calculate energy relaxation rates and impact-ionization rates for this composition, but the accessible primary text does not currently expose the interpolation coefficients.

If those coefficients cannot be recovered, do not fit them from narrative statements.

Instead use this analytic surrogate to establish **parameter ranges** and identify which measurements or primary data would actually change the device-level conclusion.
