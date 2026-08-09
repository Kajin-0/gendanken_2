# Microscopic Single-Transition Absorber — What Finite Absorber Number Does and Does Not Fix

**Date:** 2026-08-08  
**Status:** derived within the single-excitation Markov/RWA model; strong prior-art overlap; no novelty claim  

## 1. Purpose

The active-volume counterexample showed that a continuum dielectric can keep finite optical loss while its geometric active volume tends to zero by increasing field concentration.

A natural hope is that the divergence disappears as soon as the absorber is replaced by a finite microscopic object such as one two-level transition.

This note tests that hope.

The result is important because it is negative:

> **A finite absorber count by itself does not restore a single-photon sensitivity-speed bound.**

Within the one-excitation sector, a two-level transition behaves linearly, and the same rate-matching physics reappears.

---

## 2. Minimal microscopic detector

Use three detector states:

- `|g>` — ground state;
- `|e>` — optically active excited state;
- `|d>` — optically dark localized/detected state.

The optical input is one Markovian propagation channel.

Define amplitude-decay rates

- `gamma_o` — radiative amplitude decay of `|e>` into the optical channel;
- `gamma_d` — amplitude decay associated with irreversible transfer `|e> -> |d>`.

The corresponding population jump rates are `2 gamma_o` and `2 gamma_d` in this convention.

No additional loss channels are included.

The detector begins in `|g>` and the optical field contains at most one photon.

---

## 3. Why two-level saturation does not matter for one photon

A two-level transition is nonlinear because it cannot hold two excitations.

But with one incoming photon and an initially unexcited detector, the dynamics never needs the two-excitation manifold.

The accessible coherent subspace contains only states of the form

```text
|g; one photon>
|e; vacuum>
```

plus the irreversible detected state

```text
|d; vacuum>.
```

Inside this one-excitation sector, the transition lowering operator acts exactly like a linear annihilation operator on the only occupied ladder step.

Therefore the usual saturation nonlinearity does **not** constrain single-photon absorption in this sector.

Saturation becomes relevant for multiphoton flux, dead time, dynamic range, and repeated excitation before reset, but not as a cure for the one-photon shrinking-absorber paradox.

---

## 4. Exact single-excitation input-output equation

In the Markov and rotating-wave approximations, the excited-state amplitude obeys the same linear equation as a single lossy resonance:

```math
\boxed{
\dot c_e
=
-(i\omega_0+\gamma_o+\gamma_d)c_e
+\sqrt{2\gamma_o}\,s_+(t).
}
```

Use the one-port output relation

```math
\boxed{
s_-
=
-s_+
+\sqrt{2\gamma_o}\,c_e.
}
```

The irreversible detection-event flux is

```math
\boxed{
R_d(t)
=
2\gamma_d|c_e(t)|^2.
}
```

This is the microscopic analog of

```math
P_{\rm abs}=2\gamma_a|a|^2
```

in the one-port cavity calculation.

---

## 5. Monochromatic detection probability

For a monochromatic input at detuning

```math
\Delta=\omega-\omega_0,
```

the steady-state amplitude is

```math
c_e
=
\frac{\sqrt{2\gamma_o}\,s_+}
{\gamma_o+\gamma_d-i\Delta}.
```

The probability that an incident photon is irreversibly transferred into the detection channel is therefore

```math
\boxed{
A_d(\omega)
=
\frac{4\gamma_o\gamma_d}
{\Delta^2+(\gamma_o+\gamma_d)^2}.
}
```

This is mathematically identical to the one-port absorptance derived for the macroscopic resonance after the replacements

```math
\gamma_e\rightarrow\gamma_o,
\qquad
\gamma_a\rightarrow\gamma_d.
```

At resonance,

```math
A_{d,0}
=
\frac{4\gamma_o\gamma_d}
{(\gamma_o+\gamma_d)^2}.
```

Hence perfect monochromatic transfer occurs at

```math
\boxed{\gamma_o=\gamma_d.}
```

The microscopic detector therefore reproduces critical coupling as **rate matching between optical emission/capture and irreversible localization**.

---

## 6. Microscopic absorber number does not create a rate ceiling inside this model

Set

```math
\gamma_o=\gamma_d=\Lambda.
```

Then

```math
A_{d,0}=1
```

for every positive `Lambda`.

The detection line is

```math
A_d(\omega)
=
\frac{4\Lambda^2}
{\Delta^2+4\Lambda^2}.
```

Its spectral width grows linearly with `Lambda`.

Thus, for a signal wavepacket with fixed finite bandwidth, the model permits the scaling

```math
\Lambda\to\infty
```

while maintaining near-unity transfer over the entire signal spectrum and shortening the characteristic localization time.

There is no absorber-volume or absorber-number parameter left to enforce a slowdown.

The model itself therefore contains no universal speed ceiling for one absorber.

---

## 7. Strong prior-art collision

This conclusion is not a new detector theorem.

Young, Sarovar & Leonard analyzed essentially the same physical principle in a fully quantum photodetector framework.

Their high-performance configuration uses:

1. an optically active state;
2. rapid incoherent transfer into an optically dark long-lived state;
3. measurement of that dark state so that amplification backaction does not disturb optical excitation.

They found that the optimal optical coupling can be made arbitrarily high within their model and that near-perfect detection is obtained when the optical and incoherent-transfer rates are matched and fast relative to the incident pulse.

They also found negligible dark counts and minimal jitter under their ideal assumptions.

Primary source:

Steve M. Young, Mohan Sarovar & Francois Leonard, **Fundamental Limits to Single-Photon Detection Determined by Quantum Coherence and Backaction**, *Physical Review A* 97, 033836 (2018), DOI `10.1103/PhysRevA.97.033836`.

Therefore this repository must not claim novelty for single-transition rate matching, dark-state protection, or the statement that a one-photon two-level system can approach ideal detection in an unconstrained Markov model.

---

## 8. The key negative result

The sequence of failed candidate resources is now:

```text
geometric active volume
    -> not fundamental because participation can remain finite

finite absorber number / two-level saturation
    -> not sufficient for one photon because the one-excitation sector is linear
```

Thus simply replacing a dielectric continuum by one two-level absorber does not close the loophole.

The unresolved parameter is the **rate** `gamma_o` itself.

What physical principle bounds the coupling of a finite optical transition to the desired input channel over a specified bandwidth?

---

## 9. Where `gamma_o` comes from microscopically

For an electric-dipole transition in free space, the spontaneous-emission rate is proportional to

```math
\Gamma_0
\propto
\omega_0^3|\mathbf d|^2,
```

where `d` is the transition dipole matrix element.

The dipole strength is not arbitrary: oscillator-strength sum rules constrain the total transition strength available to a finite set of charges.

However, the rate into a selected optical environment also depends on the electromagnetic local density of states.

Photonic and plasmonic structures can strongly modify spontaneous emission through Purcell/LDOS enhancement.

Therefore a finite oscillator strength by itself is not yet a bound on `gamma_o` unless the allowed electromagnetic environment is also constrained.

This is the microscopic analog of the earlier field-concentrator loophole.

---

## 10. Why arbitrarily large coupling eventually leaves the model's regime

The Markov/RWA equation treats `gamma_o` and `gamma_d` as freely specifiable rates.

That abstraction fails if the rates approach microscopic carrier frequencies or bath correlation scales.

Potential breakdowns include:

- rotating-wave approximation failure;
- non-Markovian reservoir dynamics;
- strong and ultrastrong light-matter coupling;
- counter-rotating interaction terms;
- diamagnetic / `A^2` contributions required by gauge-consistent microscopic electrodynamics;
- Thomas-Reiche-Kuhn oscillator-strength constraints;
- spatial nonlocality and finite electronic length scales.

These effects do not automatically imply a useful detector bound, but they identify the layer at which `gamma_o -> infinity` can no longer be treated as a free parameter.

For example, established ultrastrong-coupling theory shows that the Jaynes-Cummings/RWA description fails when light-matter coupling becomes comparable to the bare mode frequency, and gauge-consistent models must retain counter-rotating and diamagnetic terms.

---

## 11. Electromagnetic power-bandwidth limits become relevant again — but on LDOS

The natural electromagnetic object for a microscopic emitter is no longer absorber volume but the projected local density of optical states seen by its transition dipole.

Spontaneous-emission enhancement is controlled by this LDOS in the weak-coupling regime.

Known near-field power-bandwidth theory places material- and geometry-dependent limits on LDOS enhancement over a specified bandwidth when the allowed surrounding material and distance/geometry are constrained.

Primary context:

Hyungki Shim, Lingling Fan, Steven G. Johnson & Owen D. Miller, **Fundamental Limits to Near-Field Optical Response over Any Bandwidth**, *Physical Review X* 9, 011043 (2019), DOI `10.1103/PhysRevX.9.011043`.

This suggests a better candidate resource:

```text
finite transition strength
x
allowed LDOS over the required signal bandwidth
```

rather than geometric active volume.

No detector theorem is claimed from this observation yet.

---

## 12. Thermodynamic loophole remains separate

The irreversible transfer

```text
|e> -> |d>
```

is generated by a reservoir.

If that reservoir is thermal and the reverse transition is energetically allowed, detailed balance links forward and reverse rates.

Young et al. explicitly assume the active and dark states are sufficiently separated in energy that thermally excited return from the dark state can be neglected.

Thus very low internal false-event probability is not a consequence of optical coupling alone; it depends on the state energies and reservoir occupation.

A cyclic detector must also eventually reset after a detection event.

The energetic/entropic cost of localization, amplification, and reset is a separate resource from optical oscillator strength.

Do not combine these into a single bound without deriving the thermodynamics explicitly.

---

## 13. Current conclusion

The finite-absorber test removes another tempting but insufficient explanation:

> **Single-photon saturation does not stop the vanishing-absorber thought experiment.**

Within the one-excitation Markov model, one two-level transition plus an irreversible dark-state channel can reproduce the same matched-rate perfect-absorption physics as the macroscopic one-port resonance.

Therefore the next defensible fundamental question is not

```text
How small can the absorber be?
```

or even

```text
How few absorbers can there be?
```

but rather

> **How large can the useful optical coupling rate of a finite transition be over a required bandwidth, once transition-strength sum rules and the full electromagnetic environment are counted?**

A second, independent question is

> **What thermodynamic resource is required to make the irreversible detection channel effectively one-way and resettable with negligible false events?**

These two resource axes — electromagnetic coupling and thermodynamic irreversibility — should remain separate until the physics requires them to be combined.
