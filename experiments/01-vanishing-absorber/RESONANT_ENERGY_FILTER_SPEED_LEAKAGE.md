# Resonant Energy Filter — Lifetime Broadening Creates a Zero-Temperature Speed/Leakage Penalty

**Date:** 2026-08-08  
**Status:** exact Landauer/Breit-Wigner result for an ideal single spinless transport channel at zero temperature; detector interpretation derived here; strong prior resonant-tunneling overlap; no novelty claim

## 1. Purpose

`FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md` showed that in weak sequential tunneling

```math
\frac{k_{\rm in}}{k_{\rm out}}
\propto
\exp[-(E-\mu)/(k_BT)].
```

That model appears to offer a simple escape:

```text
put the collecting state far above the Fermi level
-> fast extraction can remain large
-> thermal reverse loading becomes exponentially small.
```

At `T -> 0` the sequential model predicts zero reverse thermal loading for any level above `mu`.

But an energy-selective extraction state cannot be both arbitrarily fast and arbitrarily sharp.

Finite lifetime produces finite spectral linewidth.

This note asks:

> If a resonant energy filter is broadened to make carrier transfer fast, do its spectral tails admit dark electronic leakage from occupied states even at zero temperature?

For a Breit-Wigner resonance, yes.

---

## 2. Minimal transport geometry

Consider one spinless electronic transport channel connecting

```text
occupied source reservoir
        |
        v
resonant energy filter
        |
        v
empty collecting/drain reservoir.
```

Take

```math
\mu
```

as the source chemical potential.

The collecting drain is assumed empty over the relevant energy range. This is an ideal large-bias limit chosen to isolate the energy-filter physics.

The resonance is centered at

```math
E_0=\mu+\Delta,
\qquad
\Delta>0.
```

The intent is to transmit photoexcited carriers near `E_0` while rejecting dark carriers in the occupied source sea below `mu`.

This is an idealized abstraction of resonant-tunneling / energy-selective photodetector transport.

Resonant-tunneling barriers are established tools for reducing dark current while selectively extracting photoexcited carriers in infrared detectors. Representative prior work includes Su et al., *IEEE Journal of Quantum Electronics* **41**, 974-979 (2005), DOI `10.1109/JQE.2005.848901`, and Dehdashti Jahromi et al., *Applied Optics* **55**, 8494-8499 (2016), DOI `10.1364/AO.55.008494`. Recent THz resonant-tunneling quantum-well detector work likewise uses double-barrier structures to suppress dark current while retaining photocurrent extraction.

No novelty is claimed for resonant-tunneling dark-current suppression or Breit-Wigner transport.

---

## 3. Unit-peak Breit-Wigner filter

Let the transmission probability be

```math
\boxed{
\mathcal T(E)
=
\frac{(\Gamma_E/2)^2}
{(E-E_0)^2+(\Gamma_E/2)^2}.
}
```

Here

```math
\Gamma_E
```

is the **energy FWHM** of the transmission resonance.

Thus

```math
\mathcal T(E_0)=1.
```

This unit-peak form corresponds to a critically/symmetrically coupled ideal resonance. More general asymmetric barriers reduce the peak transmission and do not improve the basic selectivity problem studied here.

---

## 4. Zero-temperature dark leakage

At

```math
T=0,
```

the source occupation is

```math
f_S(E)=\Theta(\mu-E).
```

With an empty drain, Landauer transport gives the particle leakage rate

```math
R_{\rm leak}
=
\frac1h
\int_{-\infty}^{\mu}
\mathcal T(E)\,dE.
```

The integral is elementary:

```math
\boxed{
R_{\rm leak}
=
\frac{\Gamma_E}{2h}
\left[
\frac{\pi}{2}
-
\arctan\!\left(
\frac{2\Delta}{\Gamma_E}
\right)
\right].
}
```

Thus leakage is nonzero for every finite linewidth, even though the resonance center lies above the zero-temperature Fermi sea.

This is not thermal activation.

It is lifetime-broadened quantum transport through the low-energy tail of the resonance.

---

## 5. Map linewidth to a carrier-transfer time

For a single resonant level with total energy linewidth `Gamma_E`, the resonant-state population lifetime is

```math
\boxed{
\tau_{\rm res}
=\frac{\hbar}{\Gamma_E}.
}
```

Define the associated first-order event bandwidth

```math
B_{\rm evt}
=\frac1{2\pi\tau_{\rm res}}.
```

Since

```math
h=2\pi\hbar,
```

```math
\boxed{
B_{\rm evt}
=\frac{\Gamma_E}{h}.
}
```

This is an event/lifetime bandwidth of the resonant extraction state, not automatically the total electrical bandwidth of a complete detector.

Substituting

```math
\Gamma_E=hB_{\rm evt}
```

into the exact leakage rate gives

```math
\boxed{
R_{\rm leak}
=
\frac{B_{\rm evt}}{2}
\left[
\frac{\pi}{2}
-
\arctan\!\left(
\frac{2\Delta}
{hB_{\rm evt}}
\right)
\right].
}
```

This is the central exact speed/selectivity relation of the model.

---

## 6. Sharp-filter asymptotic

For

```math
hB_{\rm evt}\ll\Delta,
```

use

```math
\frac{\pi}{2}-\arctan x
=\frac1x+O(x^{-3})
```

for large positive `x`.

Then

```math
\boxed{
R_{\rm leak}
\simeq
\frac{hB_{\rm evt}^2}
{4\Delta}.
}
```

This is qualitatively different from the sequential Fermi-contact result.

Sequential weak tunneling gave exponential thermal suppression

```text
reverse loading ~ B exp[-Delta/(kBT)].
```

Lifetime-broadened resonant transport instead leaves a zero-temperature algebraic tail

```text
leakage ~ h B^2 / Delta.
```

The two formulas describe different regimes and should not be added blindly.

---

## 7. Required energy separation for a leakage budget

Suppose the design requires

```math
R_{\rm leak}\le D_*.
```

The exact zero-temperature relation can be inverted whenever

```math
0<2D_*/B_{\rm evt}<\pi/2.
```

From

```math
\arctan\!\left(
\frac{2\Delta}{hB_{\rm evt}}
\right)
\ge
\frac\pi2-rac{2D_*}{B_{\rm evt}},
```

one obtains

```math
\boxed{
\Delta
\ge
\frac{hB_{\rm evt}}2
\cot\!\left(
\frac{2D_*}{B_{\rm evt}}
\right).
}
```

In the low-leakage limit

```math
D_*\ll B_{\rm evt},
```

```math
\boxed{
\Delta
\gtrsim
\frac{hB_{\rm evt}^2}
{4D_*}.
}
```

Thus fixed leakage combined with increasing extraction bandwidth demands an energy separation that grows approximately quadratically with `B_evt` in this ideal resonant-level asymptotic.

---

## 8. Why this does not contradict energy-time uncertainty slogans

The result should not be summarized merely as

```text
Delta E Delta t >= hbar.
```

The load-bearing physics is more specific:

1. finite coupling gives a Lorentzian spectral function / transmission line;
2. fast extraction increases its FWHM;
3. the occupied Fermi continuum extends up to `mu`;
4. the Lorentzian tail below `mu` carries real Landauer particle flux.

The numerical coefficient and the `B^2/Delta` leakage scaling follow from that complete transport model, not from a generic uncertainty-principle slogan.

---

## 9. Finite-temperature direction

At finite temperature, the exact leakage rate becomes

```math
R_{\rm leak}(T)
=
\frac1h
\int_{-\infty}^{\infty}
\mathcal T(E)
f(E-\mu,T)\,dE
```

in the empty-drain limit.

For `E_0 > mu`, low-temperature Sommerfeld expansion adds a positive correction because the Breit-Wigner transmission is rising with energy at the Fermi edge.

The `T=0` result therefore isolates a quantum-broadening leakage mechanism that survives even after thermal activation has been removed.

A full finite-temperature expression and crossover audit should be performed before quantitative semiconductor application.

---

## 10. Relation to actual resonant-tunneling photodetectors

Real resonant-tunneling infrared detectors deliberately exploit the opposite side of this physics: a narrow transmission window can suppress dark current while allowing photoexcited carriers near the designed resonance to escape.

Prior detector literature already models transmission coefficients, photocurrent, dark current, bias dependence, and noise in such structures.

Therefore do **not** claim novelty for the qualitative statement

```text
narrower resonant tunneling barriers suppress dark current.
```

The potentially useful role of the present gedanken derivation is its deliberately stripped-down limiting question:

> If peak extraction is held ideal, what leakage is unavoidable solely because a finite extraction lifetime gives the energy filter a finite linewidth?

Whether the closed-form speed/leakage expression or its detector interpretation is absent from prior literature requires a targeted search before any novelty claim.

---

## 11. Important model limitations

The exact formula above assumes

- one spinless transport channel;
- noninteracting coherent Landauer transport;
- unit-peak Breit-Wigner transmission;
- wide-band contacts;
- an occupied source and empty drain over the relevant energies;
- zero temperature for the closed form;
- no phonon-assisted transport;
- no Coulomb blockade;
- no disorder/interface roughness;
- no trap-assisted or band-to-band tunneling;
- no inelastic scattering;
- no additional parallel dark-current channel.

A degeneracy factor simply multiplies the single-channel Landauer rate when independent channels are equivalent.

---

## 12. Counterexamples and escape routes

### Increase energy separation

Large `Delta` suppresses the Lorentzian-tail leakage.

But at fixed allowed leakage, the required `Delta` rises with extraction speed.

### Use a non-Lorentzian filter

Higher-order / multi-resonance filters can have steeper tails than a single Breit-Wigner line.

This is the most obvious attack on the present `B^2/Delta` scaling.

### Use active/time-dependent extraction

A switched barrier can open only after a photon is known to have arrived, avoiding a permanently open dark-current path.

But that reintroduces the timing/control resources already documented in the active branch.

### Use inelastic energy-selective transport

Phonon-assisted or cascade extraction can change the spectral selectivity and detailed-balance bookkeeping.

### Use many-body blockade

Coulomb/spin selection can suppress unwanted injection beyond this single-particle model, while introducing additional state/preparation resources.

---

## 13. Next decisive attack

The single-Lorentzian result is not yet a general energy-selectivity theorem.

The next question should be adversarial:

> **Can a passive multi-pole electronic filter keep near-unit photoelectron transmission over the useful extraction window while making the occupied-side tail arbitrarily small at fixed carrier dwell time / bandwidth?**

This is the electronic analogue of the earlier multimode optical attack.

If arbitrary filter order beats the `B^2/Delta` law, then filter order/spatial extent becomes the new resource.

If a Bode-Fano-like or causality/sum-rule constraint survives, it could provide a much more general semiconductor extraction bound.

Do not specialize to HgCdTe until this filter-order escape is tested.