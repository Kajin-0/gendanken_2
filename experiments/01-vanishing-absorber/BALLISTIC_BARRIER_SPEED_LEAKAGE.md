# Ballistic Single-Barrier Speed/Leakage Bound — Shrinking Collection Distance Removes the Tunneling Exponent

**Date:** 2026-08-08  
**Status:** exact optimization within an optimistic one-dimensional rectangular-barrier + parabolic-band model; not a universal semiconductor theorem; no novelty claim

## 1. Purpose

`FIELD_DRIVEN_COLLECTION_TUNNELING.md` showed that for fixed collection thickness, increasing electric field to obtain faster drift increases direct band-to-band tunneling.

But that tradeoff has an obvious escape:

```text
shrink collection thickness L
-> transit time falls
-> less field is needed for the same speed
-> field-driven tunneling can fall.
```

This note attacks the `L -> 0` escape with the smallest quantum-transport model.

Suppose optical absorption remains high through ideal photon trapping, so optical path length is no longer tied to electronic collection distance.

Can the electronic distance itself be sent to zero while dark carrier transport remains exponentially blocked?

For one rectangular energy barrier, no.

---

## 2. Minimal energy geometry

Consider one-dimensional parabolic-band transport through a barrier of thickness

```math
L.
```

Let

```math
E_d
```

be the relevant dark-carrier energy, such as the top of an occupied source/Fermi window.

Let

```math
E_s>E_d
```

be the useful photoelectron energy.

Place a rectangular barrier at energy

```math
U
```

such that

```math
\boxed{
E_d<U<E_s.
}
```

Define the total signal-dark energy separation

```math
\boxed{
\Delta E
=E_s-E_d.
}
```

Also define

```math
a=U-E_d>0,
```

```math
b=E_s-U>0,
```

so

```math
\boxed{a+b=\Delta E.}
```

The same effective mass `m` is used for the minimal derivation.

---

## 3. Dark tunneling

For the dark carrier below the barrier, the WKB decay constant is

```math
\boxed{
\kappa
=\frac{\sqrt{2ma}}{\hbar}.
}
```

In the opaque-barrier WKB limit, the dark transmission is

```math
\boxed{
\mathcal T_d
\simeq
\exp(-2\kappa L).
}
```

This is the most favorable simple exponential blocking mechanism.

Pre-exponential matching factors are omitted deliberately. The gedanken question concerns the exponent and its competition with useful transit time.

---

## 4. Useful photoelectron transit

The photoelectron lies above the barrier by energy

```math
b=E_s-U.
```

Its inside-barrier propagation speed in the parabolic model is

```math
\boxed{
v_s
=\sqrt{\frac{2b}{m}}.
}
```

Assume optimistically that interfaces are matched so that above-barrier reflection does not reduce useful collection.

The ballistic crossing time is

```math
\boxed{
\tau_{\rm tr}
=\frac{L}{v_s}.
}
```

Using the same rectangular induced-current convention as `FIELD_DRIVEN_COLLECTION_TUNNELING.md`, define

```math
\boxed{
B_{\rm tr}
=c_t\frac{v_s}{L},
\qquad
c_t\simeq0.44295.
}
```

Hence

```math
\boxed{
L
=c_t\frac{v_s}{B_{\rm tr}}.
}
```

---

## 5. Eliminate collection thickness

Substitute `L` into the WKB exponent:

```math
2\kappa L
=
\frac{2c_t\kappa v_s}
{B_{\rm tr}}.
```

Now

```math
\kappa v_s
=
\frac{\sqrt{2ma}}{\hbar}
\sqrt{\frac{2b}{m}}
=
\frac{2\sqrt{ab}}{\hbar}.
```

The effective mass cancels exactly.

Therefore

```math
\boxed{
\mathcal T_d
\simeq
\exp\!\left[
-
\frac{4c_t\sqrt{ab}}
{\hbar B_{\rm tr}}
\right].
}
```

This is already the thickness-eliminated speed/leakage relation for a chosen barrier height.

---

## 6. Optimize barrier height

Because

```math
a+b=\Delta E,
```

the arithmetic-geometric mean inequality gives

```math
\sqrt{ab}
\le
\frac{a+b}{2}
=\frac{\Delta E}{2}.
```

Equality occurs at

```math
\boxed{
a=b=\Delta E/2,}
```

or

```math
\boxed{
U_{\rm opt}
=\frac{E_s+E_d}{2}.
}
```

This barrier placement maximizes the WKB suppression exponent at fixed useful transit bandwidth.

Hence every barrier in this single-rectangular-barrier family obeys

```math
\boxed{
\mathcal T_d
\gtrsim
\exp\!\left[
-
\frac{2c_t\Delta E}
{\hbar B_{\rm tr}}
\right].
}
```

The `gtrsim` reminds the reader that the underlying WKB transmission omitted pre-exponential/interface factors; the exponent optimization itself is exact within the stated model.

If one defines inverse transit time directly,

```math
\Omega_{\rm tr}=1/\tau_{\rm tr}=v_s/L,
```

then the convention-independent exponent form is

```math
\boxed{
\mathcal T_d
\gtrsim
\exp\!\left[
-
\frac{2\Delta E}
{\hbar\Omega_{\rm tr}}
\right].
}
```

---

## 7. Physical meaning

The dimensionless control parameter is

```math
\boxed{
\frac{\Delta E}
{\hbar\Omega_{\rm tr}}
}
```

or equivalently

```math
\frac{c_t\Delta E}
{\hbar B_{\rm tr}}.
```

Thus the useful-dark energy separation must be large compared with the quantum energy scale associated with the desired transit rate if a single finite barrier is to remain exponentially selective.

As

```math
B_{\rm tr}\to\infty
```

at fixed `Delta E`, the exponent tends to zero and

```math
\mathcal T_d\to1
```

within the model.

So shrinking `L` removes the very spatial action that was blocking dark tunneling.

---

## 8. Convert transmission into a dark particle flux

To obtain an actual dark current, specify a transport window.

For one spinless Landauer channel with occupied-side electrochemical window

```math
\Delta\mu
```

and approximately energy-independent dark transmission over that narrow window, define the available quantum particle flux

```math
\boxed{
R_Q
=\frac{\Delta\mu}{h}.
}
```

Then

```math
R_d
\simeq
R_Q\mathcal T_d.
```

The optimized single-barrier result therefore gives the model lower envelope

```math
\boxed{
R_d
\gtrsim
R_Q
\exp\!\left[
-
\frac{2c_t\Delta E}
{\hbar B_{\rm tr}}
\right].
}
```

For charge current,

```math
I_d=qR_d
```

per channel.

This step requires a biased/open transport cycle. At strict equilibrium the opposing reservoir fluxes cancel in net current.

---

## 9. Maximum bandwidth for a dark-flux target

Suppose

```math
R_d\le D_*<R_Q.
```

A necessary condition in the optimized single-barrier model is

```math
R_Q
\exp\!\left[
-
\frac{2c_t\Delta E}
{\hbar B_{\rm tr}}
\right]
\le D_*.
```

Hence

```math
\boxed{
B_{\rm tr}
\lesssim
\frac{2c_t\Delta E}
{\hbar\ln(R_Q/D_*)}.
}
```

Equivalently in inverse transit time,

```math
\boxed{
\Omega_{\rm tr}
\lesssim
\frac{2\Delta E}
{\hbar\ln(R_Q/D_*)}.
}
```

This is not a universal detector speed limit. It is the optimized result for the stated single-barrier model.

---

## 10. Why the mass cancellation is interesting but not universal

For the same parabolic mass on both sides of the barrier,

```math
\kappa\propto\sqrt{m}
```

while

```math
v_s\propto1/\sqrt{m}.
```

Their product is mass independent.

Thus simply choosing a heavier barrier mass does not improve the optimized exponential once useful transit speed is fixed in this minimal model.

But real heterostructures can have different and energy-dependent effective masses, nonparabolic dispersion, multiband coupling, and interface band offsets.

HgCdTe in particular is strongly nonparabolic and is more accurately described by Kane-type band structure in many regimes.

Therefore the mass cancellation should be viewed as conceptual guidance, not a material theorem.

---

## 11. Relation to energy-time uncertainty

Again, do not replace the derivation by a slogan.

The `Delta E/(hbar Omega)` structure emerged from

1. a WKB tunneling action `kappa L` for dark carriers;
2. a ballistic flight time `L/v_s` for useful carriers;
3. a fixed total energy interval `a+b=Delta E`;
4. optimization of the barrier placement.

The coefficient `2` in the inverse-transit form follows from that concrete model.

---

## 12. Counterexamples / escape routes

### Multiple barriers / resonant tunneling

A multi-barrier structure can achieve near-unit resonant transmission for the signal while obtaining much steeper dark-energy rejection than a single barrier.

This is a real escape and is already used in infrared resonant-tunneling detectors.

But the preceding `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md` showed that adding filter poles introduces additional internal states and Wigner/group delay.

### Active switched barrier

If the barrier is opened only after an event is known, static dark tunneling can be suppressed. That spends timing/control resources and returns to the active branch.

### Inelastic cascade

Phonon-emitting cascades can carry a photoelectron through energy-selective steps rather than one elastic barrier.

Detailed balance then involves the phonon/electronic reservoirs and is a different resource problem.

### Different dispersion

Dirac/Kane/nonparabolic bands alter both evanescent action and signal group velocity.

This is particularly relevant for narrow-gap HgCdTe.

---

## 13. Relation to the multipole delay result

The single-barrier result is the spatial analogue of the single-Lorentzian filter result:

```text
one simple filter element
-> clean speed/leakage relation

add internal resonances / filter order
-> stronger rejection possible
-> more internal state/delay resource.
```

Established Friedel/Wigner-Smith scattering theory relates scattering phase derivatives to dwell time and density of states, so adding resonant electronic states naturally carries integrated delay/state-count weight.

That theory is prior art and does not by itself give a new detector theorem.

---

## 14. Claim boundary

### Derived within the stated single-barrier model

```math
\boxed{
\mathcal T_d
\gtrsim
\exp\!\left[
-
\frac{2c_t\Delta E}
{\hbar B_{\rm tr}}
\right]
}
```

with optimum barrier height midway between dark and useful carrier energies.

### Not established

- a universal quantum detector speed/dark-current bound;
- validity for HgCdTe Kane dispersion;
- optimality against multi-barrier structures;
- a universal relation between transport delay and detector electrical bandwidth;
- a minimum dark current without specifying reservoir occupation/bias window;
- novelty of this inequality.

---

## 15. Natural next question

There are now two possible directions.

### A. Keep abstracting

Generalize from one barrier to arbitrary passive scattering and attempt to combine

```text
transmission rejection
+
Wigner-Smith delay / density-of-states sum rules.
```

This risks reproducing established filter/scattering theory without a detector-specific result.

### B. Return to real infrared material physics

Replace the parabolic barrier with a narrow-gap/Kane semiconductor and include the two dominant realistic routes:

```text
field-driven collection
+
BTBT/TAT leakage.
```

Given how mature the abstract scattering theory is, **B is the preferred next move** unless a genuinely new scattering invariant appears.

For this project the logic now supports returning to a material-relevant model rather than adding more abstract filter families.