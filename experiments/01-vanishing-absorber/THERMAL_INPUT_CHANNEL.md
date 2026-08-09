# Thermal Input-Channel Background — Exact One-Port Counting Model

**Date:** 2026-08-08  
**Status:** derived within a single thermal input channel plus one-port Lorentzian absorber; no novelty claim  

## 1. Purpose

The active-volume counterexample showed that geometric absorber volume cannot by itself support a universal sensitivity-speed bound.

This note asks a narrower question that does not depend on geometric active volume:

> If the unwanted counts are thermal photons entering through the **same optical channel** as the desired signal, what relation follows between absorptance, modulation bandwidth, and background-limited sensitivity?

This is **not** a complete equilibrium detector model and is **not** an internal-dark-count theorem.

The detector's internal reverse-excitation processes are neglected here. The thermal state belongs to the external optical input channel, representing scene/background photons that are physically real but may be indistinguishable from a desired signal photon.

---

## 2. Optical model

Use the one-port absorptance already derived:

```math
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
```

Define

```math
\Gamma=\gamma_e+\gamma_a.
```

The resonant small-signal absorbed-power modulation bandwidth is

```math
\boxed{
B_{3\rm dB}
=
\frac{\Gamma}{2\pi}.
}
```

The resonant absorptance is

```math
\boxed{
A_0
=
\frac{4\gamma_e\gamma_a}{\Gamma^2}.
}
```

---

## 3. Thermal input occupation

For one propagating bosonic spatial/polarization channel at temperature `T`, the mean photon occupation at angular frequency `omega` is

```math
\boxed{
\bar n(\omega,T)
=
\frac{1}
{\exp(\hbar\omega/k_B T)-1}.
}
```

Assume the optical resonance is narrow enough that

```math
\bar n(\omega,T)\approx \bar n_0
```

across the absorptance linewidth.

This approximation requires the linewidth to be small compared with the frequency scale over which the Planck occupation changes appreciably.

---

## 4. Long-time thermal photon counting

Observe the input for a time `T_m` long compared with the optical correlation time.

The continuum can be represented by independent frequency bins of width approximately

```math
\Delta\omega=\frac{2\pi}{T_m}.
```

A thermal input frequency mode with mean occupation `n_bar` passed through an absorptive channel of probability `A(omega)` produces a thermal absorbed mode with mean

```math
\mu(\omega)=\bar n_0 A(\omega).
```

For one thermal bosonic mode,

```math
\operatorname{Var}N
=
\mu(1+\mu).
```

Summing independent frequency bins and taking the long-time limit gives

```math
\boxed{
\frac{\langle N\rangle}{T_m}
=
\bar n_0 I_1,
}
```

and

```math
\boxed{
\frac{\operatorname{Var}N}{T_m}
=
\bar n_0 I_1
+\bar n_0^2 I_2,
}
```

where

```math
I_1
\equiv
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}A(\omega),
```

```math
I_2
\equiv
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}A^2(\omega).
```

The first term is the particle/shot contribution. The second is the Bose bunching contribution.

Thermal bunching must not be discarded unless the low-occupation limit is explicitly invoked.

---

## 5. Exact Lorentzian integrals

Using

```math
\int_{-\infty}^{\infty}
\frac{d\Delta}{\Delta^2+\Gamma^2}
=
\frac{\pi}{\Gamma}
```

and

```math
\int_{-\infty}^{\infty}
\frac{d\Delta}{(\Delta^2+\Gamma^2)^2}
=
\frac{\pi}{2\Gamma^3},
```

the one-port Lorentzian gives

```math
\boxed{
I_1
=
\frac{2\gamma_e\gamma_a}{\Gamma},
}
```

and

```math
\boxed{
I_2
=
\frac{4\gamma_e^2\gamma_a^2}{\Gamma^3}.
}
```

Therefore the mean thermal-background absorption rate is

```math
\boxed{
R_{\rm th}
=
\bar n_0
\frac{2\gamma_e\gamma_a}{\Gamma}.
}
```

The long-time count-variance rate is

```math
\boxed{
K_{\rm th}
\equiv
\lim_{T_m\to\infty}
\frac{\operatorname{Var}N}{T_m}
=
\bar n_0
\frac{2\gamma_e\gamma_a}{\Gamma}
+
\bar n_0^2
\frac{4\gamma_e^2\gamma_a^2}{\Gamma^3}.
}
```

---

## 6. One-sided count-noise and input-referred NEP convention

Use the same one-sided low-frequency counting convention used in the earlier Poisson toy model.

For a stationary counting process whose long-time variance grows as

```math
\operatorname{Var}N\sim K T_m,
```

the one-sided zero-frequency count-rate noise spectral density is

```math
\boxed{S_R(0)=2K.}
```

Assume every absorbed desired signal photon produces one detected event.

For an infinitesimal coherent signal tone on resonance,

```math
\frac{dR_s}{dP_s}
=
\frac{A_0}{h\nu_0}.
```

The input-referred thermal-background NEP is therefore

```math
\boxed{
\mathrm{NEP}_{\rm th}^2
=
\frac{2(h\nu_0)^2K_{\rm th}}{A_0^2}.
}
```

This NEP refers only to the thermal photons entering the specified optical channel. It excludes internal detector dark processes, readout noise, generation-recombination noise, and additional spatial/polarization channels.

---

## 7. Dimensionless sensitivity-speed quantity

Retain the earlier definition

```math
\boxed{
\mathcal C_{\rm th}
\equiv
\frac{h\nu_0\sqrt{B_{3\rm dB}}}
{\mathrm{NEP}_{\rm th}}.
}
```

Then

```math
\mathcal C_{\rm th}^2
=
\frac{A_0^2B_{3\rm dB}}
{2K_{\rm th}}.
```

Let

```math
x=\frac{\gamma_e}{\gamma_a}.
```

Using

```math
A_0
=
\frac{4x}{(1+x)^2},
```

```math
B_{3\rm dB}
=
\frac{\gamma_a(1+x)}{2\pi},
```

```math
I_1
=
\frac{2x\gamma_a}{1+x},
```

and

```math
I_2
=
\frac{4x^2\gamma_a}{(1+x)^3},
```

gives

```math
\boxed{
\mathcal C_{\rm th}^2(x)
=
\frac{2x}
{\pi\bar n_0\left[(1+x)^2+2\bar n_0x\right]}.
}
```

All dependence on `gamma_a` cancels.

This cancellation is qualitatively different from the earlier active-volume cancellation: here it follows because both thermal background counts and useful temporal response are controlled by the **same optical absorption channel**.

---

## 8. Coupling optimization

Differentiate the `x`-dependent factor:

```math
f(x)
=
\frac{x}
{1+2(1+\bar n_0)x+x^2}.
```

Then

```math
f'(x)
\propto
1-x^2.
```

For positive coupling rates, the unique optimum is

```math
\boxed{x=1.}
```

Therefore

```math
\boxed{\gamma_e=\gamma_a}
```

is optimal for this thermal-input-channel sensitivity-speed metric.

This differs from the earlier independent bulk-dark-event toy model, where the optimum was

```math
\gamma_e=2\gamma_a.
```

The reason is physical: increasing optical coupling changes the thermal-background count rate because the noise photons enter through the same optical channel, whereas the earlier volumetric dark-event rate was assumed independent of external optical coupling.

---

## 9. Exact optimized relation

At critical coupling,

```math
A_0=1,
```

```math
B_{3\rm dB}
=
\frac{\gamma_a}{\pi},
```

```math
I_1=\gamma_a,
```

and

```math
I_2=\frac{\gamma_a}{2}.
```

Thus

```math
\boxed{
R_{\rm th}^{\rm crit}
=
\bar n_0\gamma_a,
}
```

and

```math
\boxed{
K_{\rm th}^{\rm crit}
=
\gamma_a
\left(
\bar n_0+rac{\bar n_0^2}{2}
\right).
}
```

The thermal bunching increases the long-time count variance over the Poisson value by the factor

```math
\boxed{
\frac{K_{\rm th}^{\rm crit}}
{R_{\rm th}^{\rm crit}}
=
1+\frac{\bar n_0}{2}.
}
```

The optimized dimensionless capability is

```math
\boxed{
\mathcal C_{\rm th,max}^2
=
\frac{1}
{\pi\bar n_0(2+\bar n_0)}.
}
```

Equivalently,

```math
\boxed{
\frac{\mathrm{NEP}_{\rm th,min}}
{h\nu_0\sqrt{B_{3\rm dB}}}
=
\sqrt{
\pi\bar n_0(2+\bar n_0)
}.
}
```

This is the clean result of this restricted model.

It is independent of `gamma_a`, cavity Q, and geometric active volume.

---

## 10. Low-occupation limit

For

```math
\bar n_0\ll1,
```

thermal bunching is a small correction and

```math
\boxed{
\mathcal C_{\rm th,max}^2
\approx
\frac{1}{2\pi\bar n_0}.
}
```

Equivalently,

```math
\mathrm{NEP}_{\rm th,min}^2
\approx
2\pi(h\nu_0)^2\bar n_0 B_{3\rm dB}.
```

The exact formula should be retained whenever occupation is not negligible.

---

## 11. Representative infrared occupations

Using

```math
\bar n_0
=
\frac{1}
{\exp(hc/\lambda k_B T)-1},
```

representative single-mode occupations and optimized dimensionless capabilities are approximately:

| wavelength | background temperature | `n_bar` | `C_th,max` |
|---|---:|---:|---:|
| `3 um` | `300 K` | `1.14e-7` | `1.18e3` |
| `5 um` | `300 K` | `6.83e-5` | `48.3` |
| `10 um` | `300 K` | `8.33e-3` | `4.36` |
| `12 um` | `300 K` | `1.87e-2` | `2.90` |
| `10 um` | `77 K` | `7.67e-9` | `4.55e3` |

These values are **per spatial/polarization input channel** and do not represent a complete infrared system background calculation.

For example, at `10 um`, `300 K`, and an arbitrarily chosen

```math
B_{3\rm dB}=1\ \mathrm{MHz},
```

critical coupling requires

```math
\gamma_a=\pi B\approx3.14\times10^6\ \mathrm{s}^{-1}.
```

The mean absorbed thermal-background rate is then approximately

```math
R_{\rm th}\approx2.62\times10^4\ \mathrm{s}^{-1},
```

and the corresponding one-channel input-referred thermal-background NEP is approximately

```math
\mathrm{NEP}_{\rm th}
\approx4.55\times10^{-18}\ \mathrm{W}/\sqrt{\mathrm{Hz}}.
```

The numerical example is illustrative only; real detector optics generally admit many spatial, angular, polarization, and spectral modes.

---

## 12. Interpretation

This result gives a useful conceptual split between two noise classes already encountered in the project.

### Noise independent of optical coupling

For the earlier assumed bulk dark-event process,

```math
D=g_dV_a,
```

changing `gamma_e` did not change the dark-event rate.

That model optimized at

```math
\gamma_e=2\gamma_a.
```

### Noise entering through the same optical channel

For thermal background photons,

```math
R_{\rm th}
\propto
\int A(\omega)d\omega,
```

so changing optical coupling changes both signal response and noise admission.

The optimum is instead

```math
\gamma_e=\gamma_a.
```

Thus the coupling optimum itself contains information about **where the dominant noise enters the detector**.

This is physically more informative than treating all dark/background noise as one scalar NEP.

---

## 13. What this result does not say

This note does **not** establish:

- a universal internal dark-count bound;
- a complete passive-equilibrium fluctuation-dissipation theorem for a detector;
- a bound for many optical spatial/polarization channels;
- a bound when the thermal occupation varies strongly over the resonance;
- a bound for nonequilibrium reservoirs, active cooling, dark-state localization, gain, or time-varying systems;
- a claim that thermal photon arrivals are Poissonian;
- a claim of novelty.

The bunching term was included explicitly precisely because a thermal field is not Poissonian.

---

## 14. Relation to prior work

Thermal photon fluctuations and their bunching correlations are established quantum-optical detector physics.

Primary context:

- Jonas Zmuidzinas, **Thermal noise and correlations in photon detection**, *Applied Optics* 42, 4989-5008 (2003), DOI `10.1364/AO.42.004989`. The paper develops a scattering-matrix/noise-correlation treatment for thermal photon noise and explicitly includes Hanbury Brown-Twiss bunching correlations.
- Steve M. Young, Mohan Sarovar & Francois Leonard, **Fundamental Limits to Single-Photon Detection Determined by Quantum Coherence and Backaction**, *Physical Review A* 97, 033836 (2018), DOI `10.1103/PhysRevA.97.033836`. Their nonequilibrium dark-state detector construction is an important reminder that the present thermal-input result is a restricted background limit, not a universal detector tradeoff.
- Steve M. Young, Mohan Sarovar & Francois Leonard, **General modeling framework for quantum photodetectors**, *Physical Review A* 98, 063835 (2018), DOI `10.1103/PhysRevA.98.063835`.

The present calculation specializes standard thermal-mode counting to the already-derived one-port Lorentzian absorber and its independently defined modulation bandwidth. No priority claim is made for the resulting closed form.

---

## 15. Next question

The thermal-input calculation did not restore an active-volume bound. Instead it produced a resource-independent relation for one specific source of noise.

The unresolved fundamental problem remains microscopic:

> Can a finite absorber with explicit oscillator strength, saturation, irreversible localization, and thermal reverse rates reproduce the apparent continuum divergence, or does a new constraint appear when the absorber contains only a finite number of optical degrees of freedom?

The next model should therefore replace the dielectric `epsilon''` by explicit quantum transitions rather than adding more continuum detector engineering.