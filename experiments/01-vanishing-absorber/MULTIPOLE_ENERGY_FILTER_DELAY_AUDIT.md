# Multipole Energy Filter Audit — Steeper Dark-Current Rejection Costs Filter Order and Delay

**Date:** 2026-08-08  
**Status:** adversarial filter-family calculation; exact within the chosen Butterworth-type transmission family; not a universal electronic-filter theorem; no novelty claim

## 1. Purpose

`RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md` derived for one Breit-Wigner resonance

```math
R_{\rm leak}
\simeq
\frac{hB_{\rm evt}^2}{4\Delta}
```

in the sharp-filter, zero-temperature limit.

The obvious counterexample is a higher-order energy filter.

Passive multi-resonance structures can have much steeper stop-band tails than a single Lorentzian.

This note deliberately constructs such a family and asks:

> Can filter order suppress occupied-side electronic leakage arbitrarily strongly while useful extraction remains equally fast?

At fixed spectral FWHM, yes.

But spectral width ceases to be a faithful measure of carrier latency as filter order grows.

The cost migrates into pole count / stored-state count and Wigner/group delay.

---

## 2. Adversarial maximally-flat transmission family

Take the idealized unit-peak transmission probability

```math
\boxed{
\mathcal T_N(E)
=
\frac{1}
{1+\left[2(E-E_0)/\Gamma_E\right]^{2N}}.
}
```

Here

- `N >= 1` is filter order;
- `E_0 = mu + Delta`;
- `Gamma_E` is the transmission FWHM for every `N`.

At

```math
|E-E_0|=\Gamma_E/2,
```

```math
\mathcal T_N=1/2.
```

For `N=1` this reduces exactly to the Lorentzian/Breit-Wigner probability used in the preceding note.

For larger `N`, the pass band becomes progressively flatter and the tails become progressively steeper.

This is the magnitude-squared form of a Butterworth-type filter. Butterworth synthesis itself is established passive filter theory. The present use is an adversarial model of an electronic energy filter, not a claim that every resonant-tunneling heterostructure realizes this exact function.

---

## 3. Zero-temperature occupied-side leakage

As before, use one occupied source channel with

```math
f(E)=\Theta(\mu-E)
```

and an empty receiving drain.

Landauer particle leakage is

```math
R_N
=
\frac1h
\int_{-\infty}^{\mu}
\mathcal T_N(E)\,dE.
```

Set

```math
u
=\frac{2(E_0-E)}{\Gamma_E},
```

so the Fermi edge is at

```math
u_0
=\frac{2\Delta}{\Gamma_E}.
```

Then

```math
\boxed{
R_N
=
\frac{\Gamma_E}{2h}
\int_{2\Delta/\Gamma_E}^{\infty}
\frac{d\nu}{1+\nu^{2N}}.
}
```

This is exact for the chosen family.

---

## 4. Sharp-filter asymptotic

For

```math
2\Delta/\Gamma_E\gg1,
```

```math
\frac1{1+\nu^{2N}}
\simeq
\nu^{-2N}.
```

Therefore

```math
\boxed{
R_N
\simeq
\frac{\Gamma_E}
{2h(2N-1)}
\left(
\frac{\Gamma_E}
{2\Delta}
\right)^{2N-1}.
}
```

For `N=1`,

```math
R_1
\simeq
\frac{\Gamma_E^2}
{4h\Delta},
```

which reproduces the preceding Breit-Wigner result.

For every fixed

```math
\Gamma_E/(2\Delta)<1,
```

the leakage falls rapidly with `N`.

Thus:

> **The single-resonance `B^2/Delta` leakage scaling is not universal at fixed transmission FWHM. Filter order is a genuine escape resource.**

---

## 5. Why fixed FWHM is not fixed speed

A higher-order causal filter contains more poles / internal reactive or resonant degrees of freedom.

Its phase response changes even when its power FWHM is kept fixed.

For the minimum-phase `N`th-order Butterworth transfer function with half-power angular-frequency detuning

```math
\Omega_c
=\frac{\Gamma_E}{2\hbar},
```

the on-center group delay is

```math
\boxed{
\tau_g(0)
=
\frac1{\Omega_c}
\csc\!\left(\frac{\pi}{2N}\right)
=
\frac{2\hbar}{\Gamma_E}
\csc\!\left(\frac{\pi}{2N}\right).
}
```

For large order,

```math
\boxed{
\tau_g(0)
\sim
\frac{4N\hbar}
{\pi\Gamma_E}.
}
```

So at fixed spectral FWHM

```math
\Gamma_E,
```

the central transport delay grows approximately linearly with filter order.

This is why the filter can become spectrally selective without remaining equally fast in the time domain.

Wigner-Smith delay is established scattering theory and is closely related to the density of states / energy stored in an open scattering region. Do not claim novelty for this connection.

---

## 6. Correcting the meaning of `speed`

The single Breit-Wigner resonance had one natural lifetime

```math
\tau_{\rm res}=\hbar/\Gamma_E,
```

so using

```math
B_{\rm evt}=\Gamma_E/h
```

as a speed proxy was reasonable for that one-pole architecture.

For `N > 1`, no architecture-independent identification

```text
spectral FWHM = inverse carrier latency
```

exists.

The chosen Butterworth family gives explicitly

```math
\boxed{
\Gamma_E
=
\frac{2\hbar}{\tau_g(0)}
\csc\!\left(\frac{\pi}{2N}\right).
}
```

Thus maintaining a fixed group delay while raising `N` requires broadening the spectral filter.

---

## 7. Fixed-delay consequence

Let

```math
\tau_g
```

be fixed.

Define the dimensionless energy-time separation

```math
X
\equiv
\frac{\Delta\tau_g}{\hbar}.
```

Using the delay relation,

```math
\frac{2\Delta}{\Gamma_E}
=
X
\sin\!\left(\frac{\pi}{2N}\right).
```

For large `N`,

```math
\frac{2\Delta}{\Gamma_E}
\sim
\frac{\pi X}{2N}.
```

Therefore at fixed `Delta` and fixed allowed delay, sending

```math
N\to\infty
```

does **not** keep the occupied Fermi edge deep in the stop band.

The filter must be broadened so aggressively to preserve latency that eventually the Fermi edge moves into the transition/pass region.

The apparent arbitrary stop-band improvement at fixed FWHM has disappeared because the physically relevant time resource was restored.

---

## 8. Order ceiling if the Fermi edge must remain outside the half-power point

A minimal selectivity requirement is

```math
\Delta\ge\Gamma_E/2,
```

or equivalently

```math
\frac{2\Delta}{\Gamma_E}\ge1.
```

Using the fixed-delay relation gives

```math
X
\sin\!\left(\frac{\pi}{2N}\right)
\ge1.
```

For

```math
X>1,
```

this implies the exact family-specific order ceiling

```math
\boxed{
N
\le
\frac{\pi}
{2\arcsin(1/X)}
=
\frac{\pi}
{2\arcsin[\hbar/(\Delta\tau_g)]}.
}
```

For

```math
\Delta\tau_g\gg\hbar,
```

```math
\boxed{
N_{\max}
\sim
\frac{\pi\Delta\tau_g}
{2\hbar}.
}
```

This is not a universal quantum speed limit.

It is a clean statement within this filter family showing that

```text
energy separation x tolerated delay / hbar
```

sets how much filter order can be exploited before fixed latency forces the spectral passband into the occupied reservoir.

---

## 9. Physical interpretation

The adversarial result is now

```text
single resonant level
-> leakage tail limited by linewidth

add filter poles
-> leakage tail becomes much steeper

hold only FWHM fixed
-> arbitrarily strong rejection is possible as N grows

restore temporal speed
-> group delay grows with N

hold delay fixed
-> spectral width must grow with N
-> Fermi edge eventually re-enters the pass/transition band.
```

So filter order does not give free speed plus selectivity.

But it **does** invalidate any theorem stated only in terms of the single-resonance linewidth.

---

## 10. Relation to resonant-tunneling photodetectors

Real resonant-tunneling infrared photodetectors already use multi-barrier / multi-well quantum structures to improve photocurrent selectivity and suppress dark current.

Examples include

- Su et al., *IEEE Journal of Quantum Electronics* **41**, 974-979 (2005), DOI `10.1109/JQE.2005.848901`;
- Xiong et al., *Chinese Physics Letters* **24**, 3283-3285 (2007);
- Dehdashti Jahromi et al., *Applied Optics* **55**, 8494-8499 (2016), DOI `10.1364/AO.55.008494`;
- recent double-barrier resonant-tunneling THz quantum-well detector work reporting strong dark-current suppression while preserving photocurrent extraction.

Therefore the repository must not claim novelty for multi-barrier dark-current filtering.

---

## 11. Prior scattering theory already points to the next abstraction

Wigner-Smith time delay is related to how long an excitation resides in a scattering region and to the open-system density of states.

Adding poles/resonant states therefore has a natural time-delay/state-count interpretation.

This suggests a more architecture-independent next question:

> **Can the leakage suppression of an arbitrary passive electronic scattering filter be related to an integrated Wigner-Smith delay / number-of-states resource?**

That would be the electronic transport analogue of the passive optical move from one resonance to an integrated multimode theorem.

The relevant scattering machinery is established prior theory (Friedel phase/density-of-states relations, Wigner-Smith delay matrices, passive network synthesis). Any detector-level result would need to be a new composition or restricted corollary, not a claim that the scattering theory itself is new.

---

## 12. Claim boundary

### Established within this chosen filter family

```math
R_N
=
\frac{\Gamma_E}{2h}
\int_{2\Delta/\Gamma_E}^{\infty}
\frac{d\nu}{1+\nu^{2N}},
```

and for large `2Delta/Gamma_E`,

```math
R_N
\simeq
\frac{\Gamma_E}
{2h(2N-1)}
\left(
\frac{\Gamma_E}{2\Delta}
\right)^{2N-1}.
```

The minimum-phase Butterworth realization has

```math
\tau_g(0)
=
\frac{2\hbar}{\Gamma_E}
\csc\!\left(\frac{\pi}{2N}\right).
```

### Invalidated as a general claim

The single-Lorentzian scaling

```math
R_{\rm leak}\sim hB^2/(4\Delta)
```

is not universal once higher-order filters are allowed.

### Not established

- a universal leakage-delay-filter-order theorem;
- that Butterworth magnitude is optimal for electronic dark-current suppression;
- a universal relation between detector electrical bandwidth and Wigner delay;
- a Maxwell/Schrodinger material bound on realizable filter order per device size;
- novelty of any detector-level composition here.

---

## 13. Next decisive step

Do not add more arbitrary filter families.

The natural next move is to ask whether established scattering sum rules give a useful invariant:

```text
number / strength of resonant electronic states
<-> integrated Wigner-Smith delay / density of states
<-> achievable spectral selectivity
<-> device spatial/material resource.
```

If that route only reproduces standard filter theory without a detector-specific consequence, stop the abstract generalization and specialize to a realistic semiconductor transport model.