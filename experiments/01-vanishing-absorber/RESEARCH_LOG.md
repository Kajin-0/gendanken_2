# Research Log — Experiment 01: The Vanishing Absorber

Chronological recovery log. Dedicated derivation files preserve full algebra; this file records **why the direction changed**.

---

## 2026-08-08 — Experiment opened

Starting question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project explicitly refused to assume the answer or optimize for a paper-shaped result.

---

## One-port absorber

A one-port resonator showed that unity monochromatic absorption can survive arbitrarily weak material loss through critical coupling, but useful temporal response narrows.

A factor-of-two distinction was established between optical absorption FWHM and small-signal absorbed-power bandwidth.

Direction: determine whether absorber loss rate must scale with active material volume.

---

## Active-volume route killed

A shrinking-gap field-concentration counterexample retained finite optical participation while active material volume tended to zero.

Conclusion:

> geometric active volume alone is not a universal detector resource.

Direction: descend to microscopic transition physics.

---

## Microscopic / LDOS / deep-strong branches

Finite absorber number did not impose a one-photon speed limit.

LDOS bounds became conditional on environment geometry and emitter extent.

Pushing weak-coupling enhancement eventually entered nonperturbative light-matter physics.

A Hopfield model reproduced deep-strong decoupling and yielded a fixed-target supporting lemma in which at least one required reservoir access vanished as internal coupling became arbitrarily large with fixed external resources.

Direction: generalize beyond one resonance.

---

## Finite passive network

A passive multimode network gave the harmonic integrated-transfer bound

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

This survived arbitrary finite internal mode overlap/interference under its assumptions.

Direct feedthrough and continuum reservoirs then exposed the scope: extra external channels are genuine extra resources.

Direction: test active/adaptive control.

---

## Active/adaptive control

Pumped conversion and time-dependent matching showed that active control can beat stationary matching only by spending pump/control resources.

Known-arrival temporal-mode capture can be perfect, but unknown arrival requires more storage/output capacity.

Adaptive feedforward can export the missing rank into the output record.

An unrestricted output continuum therefore kills a universal finite detector-only space-time capacity theorem.

Direction:

> stop adding abstract resource coordinates and return to a real semiconductor detector.

---

## Semiconductor contact / filter branch

Fermi-reservoir detailed balance linked fast extraction to reverse loading.

Lifetime broadening gave a single-resonance low-temperature leakage floor, but multipole filters showed that spectral width is not an architecture-independent speed variable: steeper filtering can be bought with more internal delay/state weight.

Direction: use narrow-gap HgCdTe high-field transport directly.

---

## HgCdTe BTBT / TAT / nonlocal impact ionization

A simplified HgCdTe/Kane direct-BTBT model collapsed onto

```math
j=x^2e^{-1/x}.
```

Primary high-field transport literature killed the shortcut `v=mu F` at high field.

TAT could activate before direct BTBT depending on trap spectrum.

A nonlocal mean-energy surrogate replaced a bulk impact-ionization onset field with carrier history:

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

Direction: ask whether heterostructure grading can preserve carrier drive while changing tunneling geometry.

---

## Homogeneous field shaping no-go

Within the stated homogeneous local transport/WKB model, nonuniform electric field alone did not improve the fixed-transit leakage optimum; uniform field won.

Conclusion:

> a real escape requires material heterogeneity, not merely electric-field reshaping.

---

## Graded-band HgCdTe direct-Zener escape

For linear conduction and valence edges,

```math
S_v=S_c-G,
```

with

```math
G=-dE_g/dx.
```

At fixed conduction slope, the direct-Zener WKB action increased strongly as the valence slope approached zero.

This separated

```text
useful conduction-band drive
```

from

```text
relative conduction/valence overlap geometry.
```

Direction: test self-consistent electrostatics.

---

## Quasi-neutral p-type self-consistency

A uniformly depleted multi-micron graded layer produced an excessive `N_eff L^2` Poisson burden.

For a quasi-neutral p-type region,

```math
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).
```

Nearly constant `N_A/N_v` gave

```math
E_v\approx\text{constant}
```

and therefore

```math
S_c\approx G.
```

So equilibrium charge neutrality can naturally produce the favorable graded band geometry.

Direction: locate the remaining electrostatic/leakage cost.

---

## Collection boundary

Barrier-free entry into a wider-gap collection region requires

```math
qV_b\ge\alpha\Delta E_g^{(b)}.
```

Any nonnegative field over width `w` obeys

```math
F_{\max}\ge V_b/w.
```

Thus delta doping can redistribute the field but cannot make the required compensation voltage field-free.

For local inverse-field tunneling constraints, the boundary has a finite voltage capacity

```math
V_b\le\int F_{\rm allow}(x)dx.
```

At minimum compensation the total conduction edge is flat, so the boundary can relax hot electrons while the local gap rises.

Direction: combine absorber hot-electron history and boundary local leakage.

---

## Graded nonlocal II phase boundary

For a linear quasi-neutral graded absorber and constant energy-relaxation length,

```math
\varepsilon(L)
=\Delta E_g
\frac{1-e^{-L/\ell_E}}
{L/\ell_E}.
```

With threshold surrogate

```math
E_{\rm th}=\chi E_g,
```

the deterministic mean-energy boundary became

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

This revealed a new penalty migration:

> grading can suppress direct-Zener geometry while preserving the conduction-band work that heats the useful electron.

A Lambert-W inversion converted aggressive grading into a required relaxation distance/time.

---

## Device phase map

The absorber and boundary constraints were kept separate:

```math
\mathcal M_{\rm II}
```

for nonlocal carrier-energy safety and

```math
\mathcal M_b
```

for local TAT/BTBT voltage capacity.

A boundary cooling length was added rather than treating the wide-gap boundary as a zero-time heat sink.

Direction: reconnect this transport model to the photon's absorption position.

---

## Optical reconnection — graded absorption length

For a photon inside the graded gap range, only the portion where

```math
E_g(x)<E_\gamma
```

can participate in ordinary above-gap absorption.

For a linear gap, the eligible fraction is

```math
f_{\rm opt}
=\frac{E_\gamma-E_{g,\rm out}}
{E_{g,\rm in}-E_{g,\rm out}}.
```

This reconnected transport to the original absorption gedanken.

---

## Spectral generation geometry

Critical correction to the full-span transport picture:

A photon with

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in}
```

cannot generate a carrier at the high-gap entrance.

Its first allowed generation position is

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

The maximum remaining transport distance is

```math
\boxed{
d_\gamma
=\frac{E_\gamma-E_{g,\rm out}}{G}.
}
```

Thus wavelength naturally sorts generation position and transit distance.

The exact conditional generation distribution in optical-depth coordinates is

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}
{1-e^{-\tau_\gamma}}.
}
```

Direction: calculate wavelength-resolved timing.

---

## Cold-downstream-photoelectron assumption corrected

The first spectral timing pass treated every generated electron as cold at the local conduction edge.

That was wrong when

```math
E_\gamma>E_g(x).
```

Introduce

```math
\varepsilon_{\rm gen}
=\xi_e(E_\gamma-E_g).
```

The symmetric two-band optical transition gives `xi_e=1/2`.

Primary HgCdTe Kane work instead contains a nearly flat heavy-hole band and observed heavy-hole-to-electron transitions. In that limiting channel,

```math
\xi_e\approx1.
```

The corrected finite-relaxation exit energy is

```math
\boxed{
\varepsilon_{\rm out}(u)
=
K+(\xi_eu-K)e^{-(\delta E-u)/K}.
}
```

Its maximum over generation position is

```math
\boxed{
\varepsilon_{\max}
=
\max\left[
K(1-e^{-\delta E/K}),
\xi_e\delta E
\right].
}
```

For `xi_e=1`, the maximum is simply `delta E`, independent of relaxation length.

This separated transit geometry from hot-electron energy more sharply.

---

## Corrected wavelength-resolved ballistic transit

A two-band/Kane transit kernel was derived for arbitrary initial photoelectron excess.

The exact generation distribution can be integrated against it to obtain mean collection time and generation-position timing spread.

Numerical checks showed that timing spread versus optical depth is not generically monotonic; the earlier simplified `higher QE -> lower jitter` statement was withdrawn.

---

## 2026-08-09 — Entrance-gap spectral timing peak

A stronger structure emerged when the photon sweep was extended above the entrance gap.

### Inside the graded gap range

As photon energy rises, the first allowed generation point moves upstream. High-optical-depth ballistic delay increases.

### Above the entrance gap

Once

```math
E_\gamma>E_{g,\rm in},
```

the entire absorber is optically allowed. Generation can move no farther upstream. Additional photon energy instead raises initial electron kinetic energy, reducing transit time.

Therefore the high-optical-depth ballistic model predicts

```math
\boxed{
T(E_\gamma)
\text{ is maximal at }
E_\gamma=E_{g,\rm in}.
}
```

or

```math
\boxed{
\lambda_{\rm peak}\simeq hc/E_{g,\rm in}.
}
```

The predicted shape is

```text
near output cutoff:
T -> 0 in the ideal transport limit

through graded gap range:
T rises

entrance-gap wavelength:
T maximum

shorter wavelength:
T falls

very high photon energy:
T -> L/v_K.
```

This is the strongest current detector-specific prediction.

---

## First relaxation robustness attack

The spectral timing calculation was repeated using

```math
\frac{d\varepsilon}{dx}
=G-\frac{\varepsilon}{\ell_E}
```

and local Kane group velocity

```math
\frac{v}{v_K}
=
\frac{2\sqrt{\varepsilon(\varepsilon+E_g)}}
{2\varepsilon+E_g}.
```

Across

```text
Eg,in/Eg,out = 1.5, 2, 3
L/ell_E = 0 to 10,
```

the delay maximum remained at the entrance-gap photon energy.

Energy relaxation increased the peak delay but did not move it in the tested deterministic mean-energy model.

This is not yet a drift-diffusion or Monte Carlo proof.

---

## Prior-art collision on the spectral timing prediction

Primary literature already covers

- graded HgCdTe response-time improvement;
- graded spectral QE;
- tunable-pulse HgCdTe timing;
- heavy-hole-to-electron Kane transitions.

The closest graded high-speed papers found use fixed short-wave excitation for impulse/frequency response rather than sweeping through the graded infrared absorption edge.

The focused search did not locate an inspected primary source explicitly deriving or measuring

```text
lambda
-> generation-position distribution
-> corrected graded transit distribution
```

or the entrance-gap timing maximum.

Status:

**candidate underexplored/testable analytic prediction; priority unproven.**

Negative search is not novelty evidence.

---

## Proposed decisive experiment

A tunable-wavelength impulse/group-delay experiment is now specified in

`HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`.

Measure one graded detector under fixed bias, temperature, spot, pulse energy, and readout while sweeping through

```text
near output cutoff
-> graded-gap range
-> entrance-gap wavelength
-> shorter wavelengths.
```

Use differential low-frequency group delay or normalized impulse centroid as the primary observable because a wavelength-independent common electronics transfer cancels in differences.

A strong validation would be a timing extremum near the independently predicted entrance-gap wavelength, ideally shifting with the temperature dependence of that entrance gap.

---

## Current frontier

Do not return to abstract detector resource theorems.

Do not write a manuscript yet.

The next decisive routes are

1. test the timing peak with a stronger momentum-scattering / drift-diffusion / Monte Carlo transport model; or
2. locate/reanalyze wavelength-resolved timing data on a compositionally graded HgCdTe detector.

If the spectral timing peak survives stronger transport physics and remains absent from prior literature, reassess publication significance then.
