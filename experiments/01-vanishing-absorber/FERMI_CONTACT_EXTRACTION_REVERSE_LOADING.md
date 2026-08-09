# Fermi-Contact Extraction and Reverse Loading — A Semiconductor Speed/Collection/Detailed-Balance Relation

**Date:** 2026-08-08  
**Status:** exact within a single-level weak sequential-tunneling model; semiconductor specialization of the earlier thermal-irreversibility logic; no novelty claim

## 1. Purpose

The abstract detector-reservoir work eventually reduced to the question of whether useful extraction can be made arbitrarily fast while the reverse reservoir process remains arbitrarily quiet.

This note asks the same question in explicitly semiconductor language.

Consider one relevant photoexcited electronic state of energy

```math
E
```

coupled weakly to a Fermi reservoir with chemical potential

```math
\mu
```

and temperature

```math
T.
```

The detector is prepared with that state empty. Absorption places one photoelectron in it. The desired process is extraction of that electron into the contact before it recombines.

The reverse process is thermal loading of the empty state from the same contact.

The central question is:

> If tunnel coupling is increased to make photoelectron extraction faster, can thermal reverse loading remain fixed without also changing energy bias or temperature?

Within the sequential-tunneling model, the answer is no.

---

## 2. Established Fermi-reservoir rates

Let

```math
f(E)
=
\frac{1}
{1+\exp[(E-\mu)/(k_BT)]}
```

be the reservoir Fermi occupation at the transition energy.

For one nondegenerate state with intrinsic tunnel scale `Gamma`, Fermi golden rule gives

```math
k_{\rm in}
=\Gamma f(E),
```

```math
k_{\rm out}
=\Gamma[1-f(E)].
```

These forms are standard and are directly measured in time-resolved quantum-dot tunneling experiments.

For example, Duprez et al., *Nature Communications* **15**, 9717 (2024), DOI `10.1038/s41467-024-54121-4`, write the corresponding in/out rates explicitly in terms of the intrinsic tunnel rate and Fermi function. Hofmann et al., *Physical Review Letters* **117**, 206803 (2016), DOI `10.1103/PhysRevLett.117.206803`, use energy-dependent tunneling-in/out rates and detailed balance to measure state degeneracies.

With degeneracy / multiplicity factors retained, write more generally

```math
k_{\rm in}
=g_{\rm in}\Gamma f(E),
```

```math
k_{\rm out}
=g_{\rm out}\Gamma[1-f(E)].
```

Define

```math
\zeta
\equiv
\frac{g_{\rm in}}{g_{\rm out}}.
```

Then

```math
\frac{f(E)}{1-f(E)}
=
\exp\!\left[-\frac{E-\mu}{k_BT}\right],
```

so

```math
\boxed{
\frac{k_{\rm in}}
{k_{\rm out}}
=
\zeta
\exp\!\left[-\frac{E-\mu}{k_BT}\right].
}
```

This is the fermionic local-detailed-balance relation relevant to the contact.

---

## 3. Desired photoelectron kinetics

Once a photon has created an electron in the collecting state, let two independent first-order processes compete:

```text
contact extraction:  k_out
recombination/loss:  k_r.
```

The conditional survival probability of that photoelectron is

```math
P_e(t)
=
\exp[-(k_{\rm out}+k_r)t].
```

Define the **conditional collection efficiency**

```math
\boxed{
\eta_{\rm col}
=
\frac{k_{\rm out}}
{k_{\rm out}+k_r}.
}
```

Define the associated event-response time

```math
\boxed{
\tau_{\rm evt}
=
\frac1{k_{\rm out}+k_r}.
}
```

and, by the standard first-order `-3 dB` convention,

```math
\boxed{
B_{\rm evt}
=
\frac{k_{\rm out}+k_r}
{2\pi}.
}
```

Important: `B_evt` is the bandwidth associated with the conditional single-photoelectron exponential response. It is not automatically the complete electrical bandwidth of a macroscopic photodetector.

The two definitions give exactly

```math
\boxed{
k_{\rm out}
=2\pi\eta_{\rm col}B_{\rm evt}.
}
```

---

## 4. Central semiconductor relation

Use detailed balance:

```math
k_{\rm in}
=
\zeta k_{\rm out}
\exp\!\left[-\frac{E-\mu}{k_BT}\right].
```

Substitute the exact extraction-rate identity above:

```math
\boxed{
k_{\rm in}
=
2\pi\zeta\,
\eta_{\rm col}B_{\rm evt}
\exp\!\left[-\frac{E-\mu}{k_BT}\right].
}
```

This is the central result of this note.

Interpretation:

> In a single weakly coupled Fermi contact, the same tunneling matrix element that provides fast useful extraction also provides reverse thermal loading. At fixed `E-mu` and `T`, increasing useful collection speed increases the absolute thermal loading attempt rate in direct proportion.

The ratio of bad to good contact events is controlled by the Fermi energy bias, not by the tunnel barrier alone.

---

## 5. Performance-floor form

Suppose the design requires

```math
\eta_{\rm col}\ge\eta_*,
```

and

```math
B_{\rm evt}\ge B_*.
```

Then

```math
k_{\rm out}
\ge
2\pi\eta_*B_*.
```

Therefore

```math
\boxed{
k_{\rm in}
\ge
2\pi\zeta\,
\eta_*B_*
\exp\!\left[-\frac{E-\mu}{k_BT}\right].
}
```

Within this model, any simultaneous speed/collection requirement places a minimum reverse thermal-loading attempt rate unless the level is moved farther above the contact Fermi level or the contact is cooled.

---

## 6. Required energy bias for a reverse-loading budget

If an empty ready state must satisfy

```math
k_{\rm in}\le D_{\rm load},
```

then a necessary condition is

```math
\boxed{
E-\mu
\ge
k_BT
\ln\!\left[
\frac{2\pi\zeta\eta_*B_*}
{D_{\rm load}}
\right]
}
```

whenever the logarithm argument exceeds unity.

Thus the required contact energy offset scales only logarithmically with the desired speed at fixed allowed reverse-loading rate:

```math
(E-\mu)_{\min}
\sim
k_BT\ln B_*.
```

Cooling supplies the same exponential suppression through the Fermi factor.

---

## 7. What is meant by reverse loading

The quantity

```math
k_{\rm in}
```

is the tunneling hazard **conditioned on the collecting state being empty**.

It is not automatically a measured dark-current rate or detector dark-count rate.

A thermally injected carrier becomes a false detector event only if the device architecture maps that occupation into the same downstream readout pathway as a photon-created carrier.

This distinction is crucial.

For one equilibrium contact and one isolated level, steady-state detailed balance gives zero net particle current even though gross tunneling-in and tunneling-out events continue.

Therefore do not identify

```math
k_{\rm in}
```

with conventional photodiode dark current without an explicit transport/readout cycle.

---

## 8. Exact small-signal occupancy rate is different

If reverse injection is not negligible, the dark occupancy obeys

```math
\dot p
=
k_{\rm in}(1-p)
-(k_{\rm out}+k_r)p.
```

Linearizing around its steady state gives occupancy relaxation rate

```math
\boxed{
\lambda_{\rm occ}
=k_{\rm in}+k_{\rm out}+k_r.
}
```

Thus the equilibrium small-signal occupation bandwidth would be

```math
B_{\rm occ}
=
\frac{k_{\rm in}+k_{\rm out}+k_r}
{2\pi},
```

not `B_evt`.

The event bandwidth used above was intentionally defined from the conditional response of a photon-created electron. This prevents the reverse thermal-loading process from being counted as if it were useful signal speed.

In the detector-relevant limit

```math
E-\mu\gg k_BT,
```

`k_in << k_out` and the two time scales approach each other.

---

## 9. Limiting-case audit

### Cold / high-energy contact

For

```math
E-\mu\gg k_BT,
```

```math
k_{\rm in}/k_{\rm out}
\to0.
```

Fast extraction and exponentially small reverse loading can coexist if sufficient energy bias is available.

### Level at the Fermi edge

For a nondegenerate state with

```math
E=\mu,
```

```math
k_{\rm in}=k_{\rm out}=\Gamma/2.
```

Increasing tunnel coupling speeds extraction and reverse loading equally.

### Weak tunnel barrier

Scaling

```math
\Gamma\to s\Gamma
```

at fixed `E-mu` multiplies both rates by `s`.

The contact becomes faster but no more one-way.

### Perfect conditional collection

For

```math
\eta_{\rm col}\to1,
```

contact extraction dominates recombination and

```math
k_{\rm out}\to2\pi B_{\rm evt}.
```

The reverse loading remains the detailed-balance fraction of that rate.

### Zero temperature

For

```math
T\to0,
\qquad
E>\mu,
```

reverse loading vanishes in the ideal Fermi model while extraction remains allowed.

---

## 10. Relation to the earlier thermal-irresversibility note

`THERMAL_IRREVERSIBILITY_COST.md` treated a generic thermal transition

```text
|e> <-> |d>
```

and derived

```math
k_\uparrow/k_\downarrow=e^{-\Delta/(k_BT)}.
```

The present note is the semiconductor/Fermi-contact specialization.

The conceptual correspondence is

```text
generic forward detector access
        -> contact extraction k_out

generic reverse thermal activation
        -> contact loading k_in

thermal energy bias Delta
        -> electrochemical offset E-mu.
```

The useful addition here is that `k_out` is now decomposed into directly detector-like quantities:

```math
k_{\rm out}
=2\pi\eta_{\rm col}B_{\rm evt}.
```

---

## 11. Explicit non-claims

Do **not** claim that this note proves

- a universal semiconductor dark-current limit;
- a universal detectivity-bandwidth theorem;
- that one Fermi contact describes an HgCdTe, InSb, avalanche, photoconductive, or p-n photodetector completely;
- that every thermal injection generates a registered false count;
- that tunneling remains sequential/Markovian under arbitrarily strong contact coupling;
- that `B_evt` equals every device's measured electrical `-3 dB` bandwidth;
- that an energy offset can be increased indefinitely without other device costs;
- novelty of the detailed-balance relation or the algebraic composition above.

Real semiconductor dark processes can include SRH generation, Auger generation-recombination, radiative processes, diffusion, surface leakage, trap-assisted tunneling, band-to-band tunneling, contact leakage, and optical background, among others.

---

## 12. The obvious escape — and the next gedanken experiment

The present relation can be made favorable by moving the contact Fermi level far below the photoelectron state:

```math
E-\mu\gg k_BT.
```

That appears to allow

```text
fast extraction
+
small reverse loading
```

simultaneously.

So this note does **not** establish a hard speed/dark-loading tradeoff.

The next adversarial question is more interesting:

> **Can I build an arbitrarily selective one-way energy filter that couples strongly to a photoelectron at energy `E` but completely rejects the thermally occupied electronic continuum below it?**

A finite-lifetime resonant extraction level has a finite energy linewidth. Making extraction faster broadens that level. The broadened spectral tail can overlap thermally occupied reservoir states even when the resonant energy lies above `mu`.

That suggests the next minimal semiconductor model:

```text
photoelectron state
<-> finite-linewidth resonant extraction/filter state
<-> Fermi reservoir.
```

The key question becomes whether energy selectivity and extraction time obey a useful speed-versus-thermal-injection relation once lifetime broadening is included.

This is directly relevant to resonant-tunneling and energy-selective photodetector architectures and should be attacked before adding full HgCdTe transport.