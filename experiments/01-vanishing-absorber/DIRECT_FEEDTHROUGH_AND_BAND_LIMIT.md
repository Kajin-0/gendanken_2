# Direct Feedthrough Audit — Why a Prompt Path Adds a New Broadband Resource

**Date:** 2026-08-08  
**Status:** exact finite-band inequality within the passive linear model; no novelty claim  

## 1. Question

`PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md` assumes no direct optical-to-detector feedthrough. This note attacks that assumption.

Let the optical-to-detector transfer matrix be

```math
G_{RL}(i\omega)=D_{RL}+G_{\rm res}(i\omega),
```

where

- `D_RL` is a frequency-independent prompt/direct feedthrough in the Markov state-space model;
- `G_res` is the strictly proper transfer through internal dynamical degrees of freedom.

Can nonzero `D_RL` defeat the harmonic external-access bound?

Yes, if one asks for an all-frequency `H2` area. But that is because ideal feedthrough itself represents an infinite-bandwidth resource.

---

## 2. Why the old all-frequency integral fails

For the strictly proper network,

```math
\mathcal I_{\rm res}
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\|G_{\rm res}(i\omega)\|_F^2
```

is finite and obeys

```math
\boxed{
\mathcal I_{\rm res}
\le
\frac{2LR}{L+R},
}
```

with

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

If `D_RL != 0` is exactly frequency independent, however,

```math
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\|D_{RL}\|_F^2
=\infty.
```

Thus the full transfer is not an `H2` object.

This is not a failure of the finite-network proof. A nonzero state-space feedthrough asserts an instantaneous path with no high-frequency rolloff. It therefore inserts infinite bandwidth by assumption.

---

## 3. Exact finite-band inequality

Let `B` be a finite angular-frequency band of width

```math
W=|B|.
```

Define

```math
\mathcal I_B
=
\int_B
\frac{d\omega}{2\pi}
\|D_{RL}+G_{\rm res}(i\omega)\|_F^2.
```

The `L2` triangle inequality gives

```math
\sqrt{\mathcal I_B}
\le
\left[
\int_B\frac{d\omega}{2\pi}
\|D_{RL}\|_F^2
\right]^{1/2}
+
\left[
\int_B\frac{d\omega}{2\pi}
\|G_{\rm res}\|_F^2
\right]^{1/2}.
```

The direct term is

```math
\frac{W}{2\pi}\|D_{RL}\|_F^2,
```

while the resonant term is no larger than its full-frequency area. Therefore

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

Equivalently,

```math
\boxed{
\mathcal I_B
\le
\left(
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}
\right)^2.
}
```

This inequality includes coherent interference between prompt and resonant transfer because it is derived at the amplitude-matrix level before squaring.

It is generally not tight; its role is resource accounting.

---

## 4. Passivity of the direct block

For a passive scattering realization, the full prompt scattering matrix is contractive. Hence the direct optical-to-detector subblock cannot have singular values larger than unity.

If there are `M` independent incident optical channels, then

```math
\|D_{RL}\|_F^2\le M
```

is a simple channel-count ceiling.

Consequently the direct contribution over a finite band is at most of order

```math
\frac{MW}{2\pi}.
```

But this is not a small bound: an ideal prompt channel can transfer order-unity probability throughout its admitted band.

Thus allowing direct feedthrough changes the resource being counted from internal access rates to **direct channel bandwidth and channel number/strength**.

---

## 5. Explicit counterexample to an all-frequency access-only theorem

Take no internal state at all and one optical input channel mapped directly into one detector reservoir channel:

```math
G_{RL}(i\omega)=1.
```

This is passive as a scattering map and gives

```math
T(\omega)=1
```

for every frequency in the idealized Markov model.

Its full-frequency transfer area diverges.

Therefore no universal finite all-frequency theorem based only on finite internal traces `L` and `R` can include arbitrary nonzero frequency-independent feedthrough.

This is a genuine counterexample to such an extension.

It is **not** a physical prediction that a real photodetector can absorb every photon from zero to infinite frequency. The constant feedthrough approximation has inserted that bandwidth by construction.

---

## 6. Physical interpretation

A direct optical-to-detector path is not a free bypass of the resource picture. It is itself a new external-access resource:

```text
prompt detector coupling
x
usable spectral bandwidth
x
number of accepted channels.
```

In a microscopic electromagnetic detector, a truly irreversible direct path must still be implemented by material degrees of freedom and a dissipative continuum. Real material response is dispersive and cannot generally remain a constant Markov feedthrough over arbitrary frequency.

Thus the prompt-path attack moves the problem from a finite-mode `H2` theorem to causal/material-response or matching bounds.

Recent Bode-Fano work on passive optical absorption explicitly makes this same structural move: broadband absorption is cast as a passive impedance-matching problem constrained by causality and material dispersion. That is prior theory, not a repository novelty claim.

---

## 7. What survives

The harmonic theorem survives unchanged for the strictly proper **resonant excess**

```math
G_{\rm res}(s)=G_{RL}(s)-D_{RL}.
```

Hence

```math
\boxed{
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\|G_{RL}(i\omega)-D_{RL}\|_F^2
\le
\frac{2LR}{L+R}.
}
```

What does not survive is an all-frequency finite bound on the total transfer when an ideal white feedthrough is admitted.

---

## 8. Claim boundary

### Established here

1. Nonzero frequency-independent direct feedthrough makes the total all-frequency `H2` transfer area divergent.
2. The strictly proper resonant part remains bounded by the harmonic external-access theorem.
3. Over a finite band, the prompt and resonant contributions obey the exact triangle-inequality resource bound above.

### Not established

- a Maxwell-level bound on the physical bandwidth of a direct absorptive path;
- a universal material sum rule for arbitrary detector geometries;
- novelty of the finite-band inequality;
- any claim that direct feedthrough is impossible.

---

## 9. Next consequence

The direct-feedthrough loophole does **not** support a universal detector bound based only on finite internal access traces.

The next physically meaningful question is:

> When the prompt detector path is generated by an actual passive causal material continuum rather than an ideal constant `D`, what finite spectral-access resource replaces the state-space feedthrough?

That question connects directly to structured reservoirs, causal matching theory, oscillator-strength/material-response bounds, and thermodynamic bounds on external coupling.