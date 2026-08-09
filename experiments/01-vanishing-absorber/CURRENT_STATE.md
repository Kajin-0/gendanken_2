# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** geometric-volume and finite-absorber-number routes tested; neither supplies a universal bound; no novelty claim  

## 1. Guiding question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The research has now passed through four logical steps:

1. **One-port optical loss:** if the active loss rate `gamma_a -> 0`, maintaining unity resonant absorption makes the absorbed-power response narrow.
2. **Active-volume counterexample:** `V_a -> 0` does not force `gamma_a -> 0`; ideal field concentration can keep active participation and `gamma_a` finite.
3. **Thermal input channel:** when background photons enter through the same optical channel as the signal, an exact sensitivity-speed relation appears that depends on thermal occupation, not active volume.
4. **Microscopic single transition:** replacing the continuum absorber by one two-level transition still does not create a one-photon speed bound, because the one-excitation sector is linear and rate matching reappears.

The surviving unresolved resource is therefore not simply geometric volume or absorber number.

---

## 2. Canonical supporting notes

1. `ONE_PORT_RESONATOR_DYNAMICS.md`
2. `ACTIVE_VOLUME_COUNTEREXAMPLE.md`
3. `THERMAL_INPUT_CHANNEL.md`
4. `MICROSCOPIC_SINGLE_TRANSITION.md`

The claim boundary is maintained in `CLAIM_LEDGER.md`.

---

## 3. One-port result

For a passive one-port resonance,

```math
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2}.
```

The resonant absorbed-power modulation bandwidth is

```math
\boxed{
B_{3\rm dB}
=
\frac{\gamma_e+\gamma_a}{2\pi}.
}
```

At critical coupling,

```math
\boxed{
\gamma_e=\gamma_a,
\qquad
A_0=1,
\qquad
B_{3\rm dB}=\frac{\gamma_a}{\pi}.
}
```

Thus **if `gamma_a -> 0`**, unity monochromatic absorption becomes proportionally slow/narrow in this architecture.

For the earlier independent Poisson bulk-dark-event toy model, the dimensionless metric

```math
\mathcal C
=
\frac{h\nu\sqrt{B_{3\rm dB}}}{\mathrm{NEP}}
```

was optimized at

```math
\boxed{
\gamma_e=2\gamma_a,
\qquad
A_0=\frac89.
}
```

That optimum is not universal; it depends on the assumed noise source.

---

## 4. Geometric active volume is not fundamental

For weak dielectric loss,

```math
\boxed{
\gamma_a
=
\frac{\omega}{2}p_a\tan\delta,
}
```

where `p_a` is active electric-energy participation.

The explicit shrinking-capacitor family

```math
d=s d_0,
\qquad
A=s A_0,
\qquad
s\to0
```

keeps

```math
C=\frac{\epsilon_0\epsilon' A}{d}
```

fixed while

```math
V_a=Ad\propto s^2\to0.
```

For fixed modal energy,

```math
|E|^2\propto s^{-2},
```

so

```math
|E|^2V_a=\text{constant}.
```

Hence fixed participation and fixed `gamma_a` can coexist with

```math
\boxed{V_a\to0}
```

and therefore

```math
\boxed{\gamma_a/V_a\to\infty.}
```

So passivity alone does **not** yield an active-volume-only optical bound when arbitrary ideal field concentration is allowed.

The earlier schematic target

```text
eta^2 B <= C V_a
```

is no longer an active conjecture.

---

## 5. Thermal photons entering through the signal channel

`THERMAL_INPUT_CHANNEL.md` considers one thermal spatial/polarization input channel with approximately constant Bose occupation over the resonance,

```math
\bar n_0
=
\frac{1}
{\exp(\hbar\omega_0/k_BT)-1}.
```

Define

```math
I_1
=
\int\frac{d\omega}{2\pi}A(\omega),
```

```math
I_2
=
\int\frac{d\omega}{2\pi}A^2(\omega).
```

For the one-port Lorentzian,

```math
\boxed{
I_1
=
\frac{2\gamma_e\gamma_a}
{\gamma_e+\gamma_a},
}
```

```math
\boxed{
I_2
=
\frac{4\gamma_e^2\gamma_a^2}
{(\gamma_e+\gamma_a)^3}.
}
```

Long-time thermal photon counting gives

```math
\boxed{
R_{\rm th}=\bar n_0 I_1,
}
```

and

```math
\boxed{
K_{\rm th}
=
\lim_{T_m\to\infty}
\frac{\operatorname{Var}N}{T_m}
=
\bar n_0 I_1+\bar n_0^2I_2.
}
```

The second term is Bose bunching.

Using the same one-sided count-noise convention and the dimensionless sensitivity-speed metric gives, with

```math
x=\frac{\gamma_e}{\gamma_a},
```

```math
\boxed{
\mathcal C_{\rm th}^2(x)
=
\frac{2x}
{\pi\bar n_0\left[(1+x)^2+2\bar n_0x\right]}.
}
```

The unique positive optimum is

```math
\boxed{x=1.}
```

So thermal input-channel noise is optimized at **critical coupling**, in contrast to the independent bulk-dark-event model.

At critical coupling,

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
\sqrt{\pi\bar n_0(2+\bar n_0)}.
}
```

The absorber rate `gamma_a`, loaded `Q`, and active volume cancel from this **restricted one-channel background relation**.

This is not an internal-dark-count theorem or a complete equilibrium detector bound.

Representative single-channel thermal occupations:

| wavelength | background temperature | `n_bar` | `C_th,max` |
|---|---:|---:|---:|
| `3 um` | `300 K` | `1.14e-7` | `1.18e3` |
| `5 um` | `300 K` | `6.83e-5` | `48.3` |
| `10 um` | `300 K` | `8.33e-3` | `4.36` |
| `12 um` | `300 K` | `1.87e-2` | `2.90` |
| `10 um` | `77 K` | `7.67e-9` | `4.55e3` |

These numbers are per spatial/polarization mode and are not complete optical-system background calculations.

---

## 6. Finite absorber number does not fix the one-photon problem

`MICROSCOPIC_SINGLE_TRANSITION.md` replaces the dielectric absorber by one optically active transition `|g> <-> |e>` plus an irreversible dark detection state `|d>`.

Define amplitude-decay rates

- `gamma_o` into the optical port;
- `gamma_d` into the irreversible detection channel.

With at most one incident photon and the detector initially in its ground state, the dynamics remains in the one-excitation sector.

The two-level saturation nonlinearity is therefore not accessed.

The excited-state amplitude obeys the same linear one-resonance equation, giving the irreversible detection probability

```math
\boxed{
A_d(\omega)
=
\frac{4\gamma_o\gamma_d}
{(\omega-\omega_0)^2+(\gamma_o+\gamma_d)^2}.
}
```

Perfect monochromatic transfer occurs at

```math
\boxed{\gamma_o=\gamma_d.}
```

If both rates are scaled together,

```math
\gamma_o=\gamma_d=\Lambda,
```

the model permits the detection line to broaden with `Lambda` while preserving unit on-resonance transfer.

Thus **finite absorber number and two-level saturation do not by themselves impose a single-photon speed ceiling**.

---

## 7. Major prior-art collision

Young, Sarovar & Leonard, *Physical Review A* 97, 033836 (2018), developed a fully quantum photodetector model with an optically active state, rapid incoherent transfer to a long-lived optically dark state, and measurement of that dark state.

Within their ideal assumptions they found that high optical coupling combined with matched rapid incoherent transfer can approach unit efficiency, negligible dark counts, and minimal jitter.

They explicitly assume thermal reverse transfer from the dark state to the optically active state is negligible.

Therefore this repository must **not** claim novelty for:

- single-transition rate matching;
- dark-state protection of optical absorption from measurement backaction;
- the claim that finite absorber number alone imposes an efficiency-speed tradeoff;
- a universal quantum efficiency-dark-count-jitter tradeoff without thermodynamic constraints.

Their result does not answer the present full resource-accounting question, but it closes several tempting branches.

---

## 8. What resource is left?

The unresolved optical quantity is now the useful coupling rate of a **finite transition** to a desired input channel over a specified signal bandwidth.

For an electric-dipole transition, free-space radiative coupling depends on the transition dipole / oscillator strength. Total oscillator strength is constrained by microscopic sum rules.

But an engineered electromagnetic environment can alter the radiative rate through the projected local density of optical states (LDOS).

So the natural combined optical resource is closer to

```text
finite transition strength
x
allowed LDOS over the required bandwidth
```

than to active volume.

Known near-field power-bandwidth theory already constrains LDOS enhancement when surrounding material and geometry are specified. This is prior theory, not a new result here.

If coupling is pushed toward the bare optical frequency, the Markov/RWA model itself fails and gauge-consistent ultrastrong-coupling physics, counter-rotating terms, diamagnetic contributions, and oscillator-strength constraints become unavoidable.

---

## 9. Separate thermodynamic resource

The irreversible localization step

```text
|e> -> |d>
```

requires coupling to a reservoir.

Suppressing the reverse process depends on level spacings and reservoir occupation; a cyclic detector must eventually reset.

Thus optical coupling strength and thermodynamic irreversibility are distinct resource axes.

Do not combine them into one universal bound without explicitly modeling:

- forward and reverse transition rates;
- reservoir temperatures or chemical potentials;
- amplification backaction;
- reset/free-energy cost;
- the detector's operating cycle.

---

## 10. Current claim boundary

### Established within stated models

1. One-port modulation bandwidth is `B_3dB=(gamma_e+gamma_a)/(2 pi)`.
2. If `gamma_a -> 0`, critical-coupling unity absorption becomes narrow.
3. `V_a -> 0` does not imply `gamma_a -> 0`; an explicit passive local-linear counterexample has fixed `gamma_a` and `gamma_a/V_a -> infinity`.
4. For one thermal input channel, exact Bose counting gives `C_th,max^2 = 1/[pi n_bar(2+n_bar)]` at critical coupling.
5. For one incoming photon, a two-level absorber remains linear in the accessible one-excitation sector; finite absorber number alone does not create a speed ceiling in the Markov/RWA model.

### Invalidated / stopped as general claims

- `gamma_a/V_a` bounded by passivity alone;
- a universal active-volume law `eta^2 B <= C V_a`;
- universal active-volume cancellation;
- finite absorber number / saturation as the missing single-photon bound;
- a universal efficiency-dark-count-jitter tradeoff without resource assumptions.

### Not established

- a universal upper bound on finite-transition optical coupling over bandwidth;
- a detector theorem obtained from oscillator-strength/LDOS bounds;
- a full equilibrium fluctuation-dissipation detector limit;
- a minimum thermodynamic work/reset cost for a specified detector capability;
- novelty of any detector-level closed form in this repository.

---

## 11. Next decisive question

The cleanest forward direction is now:

> **For a finite optical transition with fixed oscillator strength, how large can the coupling to one useful propagating channel be over a required bandwidth when the entire passive electromagnetic environment is constrained?**

This should be attacked using projected LDOS / spontaneous-emission power-bandwidth bounds rather than active material volume.

In parallel, keep the independent thermodynamic question explicit:

> **What reservoir/free-energy resource is required to make the detection transition effectively irreversible and resettable while suppressing false events?**

Do not add HgCdTe-specific transport yet. The project has not yet reached the material-specific layer.