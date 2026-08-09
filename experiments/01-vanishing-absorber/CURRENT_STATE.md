# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; abstract optical/control loopholes audited; research has returned to material-relevant HgCdTe transport; normalized direct-BTBT frontier derived; no novelty claim

## 1. Guiding question

The experiment began with

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The project did not assume the answer was no.

The original geometric-volume idea failed. The path progressively exposed deeper resources:

```text
active volume
-> electromagnetic participation
-> microscopic transition strength
-> nonperturbative light-matter access
-> aggregate optical/detector reservoir access
-> active pump/control resources
-> temporal-mode and output-record capacity
-> concrete semiconductor extraction, tunneling, and high-field transport.
```

The current frontier is no longer an abstract universal detector theorem.

It is the much more concrete question:

> **For narrow-gap HgCdTe, what transit speed is actually attainable before field-assisted dark transport becomes unacceptable, once the real high-field velocity law is used?**

---

## 2. Canonical reading order at the current frontier

After root `AGENTS.md`, read:

1. `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
2. `HGCDTE_KANE_SCALE_AUDIT.md`
3. `FIELD_DRIVEN_COLLECTION_TUNNELING.md`
4. `BALLISTIC_BARRIER_SPEED_LEAKAGE.md`
5. `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md`
6. `RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md`
7. `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`
8. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
9. `ADAPTIVE_FEEDFORWARD_MODE_CAPACITY.md`
10. `OUTPUT_RECORD_INFORMATION_CAPACITY.md`
11. `RESEARCH_LOG.md`
12. older branches only when tracing provenance.

`CLAIM_LEDGER.md` remains the epistemic boundary.

There is still no manuscript.

---

## 3. Major routes that were explicitly killed or narrowed

### Geometric active volume is not fundamental

An ideal shrinking-gap passive continuum family can retain finite optical energy participation and finite absorptive decay while

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

Therefore no universal active-volume-only law such as

```text
eta^2 B <= C V_a
```

survived.

### Finite absorber number is not enough

For one incident photon, a two-level absorber remains linear in the accessible one-excitation sector. Saturation/finite absorber number alone does not impose the hoped-for single-photon speed ceiling.

### A finite storage rank is not an always-on detector capacity

For a fixed linear capture map into `r` retained modes,

```math
\sum_j\eta_j\le r.
```

Adaptive branching generalizes this to

```math
\boxed{
\sum_j\eta_j\le rd,
}
```

where `d` is successful controller/output branch rank.

But a continuously operating detector can export the missing distinguishability into an effectively enormous output continuum. Thus no universal finite internal space-time detector capacity survived without constraining the output record itself.

### Output energy alone is not the missing resource

One output quantum distributed among many orthogonal time bins can encode a growing arrival-time record at fixed event energy. Output time-bandwidth can substitute for output energy.

This closed the attempt to build an abstract universal detector theorem from storage rank + Landauer cost alone.

---

## 4. Strongest retained passive-network result

For a finite stable passive strictly proper network with aggregate optical and irreversible detector access matrices `Gamma_L`, `Gamma_R`, define

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

The integrated optical-to-detector transfer obeys

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

In the left controllability-Gramian eigenbasis,

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

A one-mode matched passive resonance saturates the bound.

This is an exact detector-facing passivity corollary built from standard `H_2`/Lyapunov/passive-system theory. No novelty claim is made.

For band width `W`,

```math
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
```

This remains useful background, but the project no longer treats it as sufficient for a paper by itself.

---

## 5. Active/time-dependent branch — what survived

A coherent pump can beat a passive stationary match, but the pump-induced conversion strength is a resource.

For finite number-conserving conversion

```math
H_{\rm conv}/\hbar
=\mathbf b^\dagger K\mathbf a
+\mathbf a^\dagger K^\dagger\mathbf b,
```

converting `M_c` orthogonal singular channels with probability at least `eta` in time `tau` requires

```math
\boxed{
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
}
```

Known-mode time-dependent capture can also beat a stationary frequency-domain match. For one tunable cavity mode,

```math
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}
```

is the exact zero-reflection loading schedule.

With bounded coupling,

```math
\eta_{\rm cap}
\le
1-e^{-2\kappa_{\max}\tau}.
```

These are useful control-resource baselines, but the relevant mode-conversion and tunable-capture physics has strong prior-art overlap.

The adaptive/output-continuum attack showed why continuing to add abstract resource axes was unlikely to yield a clean universal photodetector theorem.

That motivated the return to semiconductor transport.

---

## 6. First semiconductor specialization — Fermi contact

For one photoexcited electronic state at energy `E` weakly coupled to a Fermi reservoir at chemical potential `mu`, sequential tunneling gives

```math
k_{\rm in}
=g_{\rm in}\Gamma f(E),
```

```math
k_{\rm out}
=g_{\rm out}\Gamma[1-f(E)].
```

With

```math
\zeta=g_{\rm in}/g_{\rm out},
```

```math
\boxed{
\frac{k_{\rm in}}
{k_{\rm out}}
=
\zeta
\exp[-(E-\mu)/(k_BT)].
}
```

If photoelectron extraction competes with recombination `k_r`, define

```math
\eta_{\rm col}
=\frac{k_{\rm out}}
{k_{\rm out}+k_r},
```

```math
B_{\rm evt}
=\frac{k_{\rm out}+k_r}
{2\pi}.
```

Then exactly

```math
\boxed{
k_{\rm out}
=2\pi\eta_{\rm col}B_{\rm evt},
}
```

and therefore

```math
\boxed{
k_{\rm in}
=
2\pi\zeta\eta_{\rm col}B_{\rm evt}
\exp[-(E-\mu)/(k_BT)].
}
```

`k_in` is a reverse loading hazard of an empty state, not automatically a measured dark current or count rate.

---

## 7. Lifetime-broadened energy filter

The weak sequential model can suppress reverse loading exponentially by taking `E-mu` large.

A finite-lifetime resonant filter exposes the next penalty.

For a unit-peak Breit-Wigner transmission centered `Delta=E_0-mu` above a filled source,

```math
\mathcal T(E)
=
\frac{(\Gamma_E/2)^2}
{(E-E_0)^2+(\Gamma_E/2)^2}.
```

At zero temperature with an empty drain,

```math
\boxed{
R_{\rm leak}
=
\frac{\Gamma_E}{2h}
\left[
\frac\pi2
-
\arctan\left(
\frac{2\Delta}{\Gamma_E}
\right)
\right].
}
```

For one resonance,

```math
B_{\rm evt}=\Gamma_E/h,
```

so in the sharp-filter limit

```math
\boxed{
R_{\rm leak}
\simeq
\frac{hB_{\rm evt}^2}
{4\Delta}.
}
```

This is zero-temperature lifetime-broadening leakage, not thermal activation.

---

## 8. Multipole counterexample — FWHM is not speed

The single-Lorentzian `B^2/Delta` scaling is not universal.

For an adversarial `N`th-order Butterworth-type probability

```math
\mathcal T_N(E)
=
\frac1
{1+[2(E-E_0)/\Gamma_E]^{2N}},
```

occupied-side leakage has the asymptotic

```math
\boxed{
R_N
\simeq
\frac{\Gamma_E}
{2h(2N-1)}
\left(
\frac{\Gamma_E}{2\Delta}
\right)^{2N-1}.
}
```

Thus at fixed FWHM, higher order can suppress leakage arbitrarily strongly.

But the minimum-phase Butterworth group delay is

```math
\boxed{
\tau_g(0)
=
\frac{2\hbar}{\Gamma_E}
\csc\left(\frac{\pi}{2N}\right)
\sim
\frac{4N\hbar}{\pi\Gamma_E}.
}
```

This killed the assumption that spectral FWHM can be used as an architecture-independent carrier-speed metric.

Adding filter poles buys rejection by spending internal states/dwell time.

Further abstraction through Wigner-Smith/Friedel sum rules was judged unlikely to add enough detector-specific content, because delay/DOS relations are mature scattering theory.

---

## 9. Field-driven collection in a narrow-gap diode

For one carrier crossing fixed thickness `L` at drift velocity `v_d`, the rectangular Ramo-pulse convention gives

```math
\boxed{
B_{\rm tr}
=c_t\frac{v_d}{L},
\qquad
c_t\simeq0.44295.
}
```

In the low-field regime `v_d=mu F`, and for a Kane-type BTBT law

```math
J_{\rm BTBT}=A F^2e^{-F_K/F},
```

eliminating field gives

```math
\boxed{
J_{\rm BTBT}(B_{\rm tr})
=
A
\left(
\frac{LB_{\rm tr}}
{c_t\mu}
\right)^2
\exp\left[-
\frac{F_Kc_t\mu}
{LB_{\rm tr}}
\right].
}
```

At fixed `L`, direct tunneling rises monotonically as field-driven transit bandwidth is increased.

However, shrinking `L` is a real counterexample: shorter collection distance can increase speed while reducing the field required for a specified speed.

Therefore this is a fixed-thickness tradeoff, not a universal one.

---

## 10. Quantum small-`L` audit

A one-dimensional rectangular barrier between dark energy `E_d` and useful photoelectron energy `E_s` gives, after eliminating collection thickness,

```math
\mathcal T_d
\simeq
\exp\left[-
\frac{4c_t\sqrt{ab}}
{\hbar B_{\rm tr}}
\right],
```

where

```math
a=U-E_d,
\qquad
b=E_s-U,
\qquad
a+b=\Delta E.
```

Optimizing barrier placement gives the midpoint `a=b=Delta E/2` and

```math
\boxed{
\mathcal T_d
\gtrsim
\exp\left[-
\frac{2c_t\Delta E}
{\hbar B_{\rm tr}}
\right].
}
```

The mass cancels in this ideal parabolic model.

But multi-barrier/resonant structures are a real escape and reintroduce internal state/delay resources.

For HgCdTe the resulting quantum speed scale is generally far above ordinary practical detector bandwidths, so this is currently treated as an asymptotic ceiling rather than the useful material frontier.

---

## 11. HgCdTe Kane material scales

Use the simplified Kane relation

```math
E_g=2m_Kv_K^2
```

with the experimentally supported near-universal narrow-gap velocity

```math
v_K\simeq1.07\times10^6\ {\rm m/s}.
```

A common direct-BTBT exponent then gives, after identifying the tunneling mass with the Kane band-edge mass for a scaling audit,

```math
\boxed{
F_K
\simeq
\frac{\pi E_g^2}
{4q\hbar v_K}
=
\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2}.
}
```

Thus

```math
\boxed{F_K\propto\lambda_c^{-2}.}
```

The corresponding Kane length

```math
\boxed{
\ell_K
=\frac{\hbar v_K}{E_g}
=\frac{v_K}{2\pi c}\lambda_c
}
```

grows as

```math
\boxed{\ell_K\propto\lambda_c.}
```

Representative scaling values:

| `lambda_c` | `E_g` | `F_K` | `ell_K` |
|---:|---:|---:|---:|
| 5 um | 0.248 eV | 6.86e5 V/cm | 2.84 nm |
| 8 um | 0.155 eV | 2.68e5 V/cm | 4.54 nm |
| 10 um | 0.124 eV | 1.71e5 V/cm | 5.68 nm |
| 12 um | 0.103 eV | 1.19e5 V/cm | 6.82 nm |
| 17 um | 0.0729 eV | 5.93e4 V/cm | 9.66 nm |
| 24 um | 0.0517 eV | 2.98e4 V/cm | 13.6 nm |

These are scaling estimates, not calibrated junction predictions.

---

## 12. Current strongest HgCdTe normalization

Start from the published uniform-field direct-BTBT formula

```math
J_{\rm BTBT}
=
\frac{q^3\sqrt{2m^*}F V}
{4\pi^3\hbar^2E_g^{1/2}}
\exp\left[-
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2q\hbar F}
\right].
```

For a uniform region `V=FL`, and the simplified Kane-mass substitution

```math
m^*=E_g/(2v_K^2),
```

this becomes

```math
\boxed{
J_{\rm BTBT}
=
\frac{q^3L}{4\pi^3\hbar^2v_K}
F^2e^{-F_K/F}.
}
```

Define

```math
x=F/F_K,
\qquad
j=J/J_K.
```

Then

```math
\boxed{j=x^2e^{-1/x}.}
```

The scales are

```math
\boxed{
F_K
=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2},
}
```

```math
\boxed{
J_K
=\frac{q\pi^3c^4L}
{4v_K^3\lambda_c^4}.
}
```

Therefore

```math
F_K\propto\lambda_c^{-2},
\qquad
J_K\propto L\lambda_c^{-4},
```

while the normalized shape is independent of wavelength.

The exact inverse is

```math
\boxed{
x(j)
=\frac1
{2W_0[1/(2\sqrt j)]}.
}
```

So for a direct-BTBT current-density target `J_*`,

```math
\boxed{
F_{\max}^{\rm BTBT}
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
}
```

This is the current cleanest material-normalized result.

Companion regression:

```text
numerics/hgcdte_btbt_normalized_sweep.py
```

---

## 13. Critical transport warning

Do **not** convert `F_max` to speed using low-field mobility at kilovolt-per-centimeter fields.

A primary Monte Carlo study of `Hg_0.8Cd_0.2Te` at 77 K reports non-ohmic/hot-electron and impact-ionization physics already at fields of order `100 V/cm` and provides analytical interpolation formulas in the full article.

The coefficients are not exposed in the currently accessible primary-source text.

Therefore the correct speed relation remains

```math
\boxed{
B_{\rm tr,max}
=
\frac{c_t}{L}
\,v_d\!\left(F_{\max}^{\rm BTBT}\right),
}
```

with `v_d(F)` imported from a traceable composition/temperature-specific transport model.

The Kane velocity supplies only an optimistic band-kinematic envelope

```math
B_{\rm tr}\lesssim c_t v_K/L,
```

not a practical drift prediction.

---

## 14. Prior-art/material boundary

Established HgCdTe theory and experiment already include

- field-dependent BTBT and TAT dark current;
- avalanche/impact-ionization competition;
- high-field non-ohmic electron transport;
- resonant-tunneling structures for dark-current suppression;
- Kane/nonparabolic narrow-gap band structure.

No novelty is claimed for those ingredients.

The current value of the repository is the explicit trail of counterexamples and the normalization/resource accounting connecting optical capture, detector access, and semiconductor extraction.

A paper is still **not** justified solely from the current formulas.

---

## 15. Next decisive calculation

The next step is now narrowly defined:

> **For one specified HgCdTe composition/temperature with a traceable high-field velocity law, combine `v_d(F)` with the normalized BTBT inversion and determine the transit-bandwidth frontier as a function of cutoff wavelength, collection thickness, and direct-BTBT current-density budget.**

Procedure:

1. obtain the primary-source `v_d(F)` interpolation coefficients or a digitizable primary curve for a definite HgCdTe composition and temperature;
2. compute `F_max(J_*,lambda_c,L)` from the normalized BTBT model;
3. evaluate

```math
B_{\rm tr,max}
=c_t v_d(F_{\max})/L;
```

4. compare `F_max` with the field where hot-electron transport and impact ionization already intervene;
5. add TAT only after the pure-BTBT frontier is clear;
6. then compare the theoretical frontier with reported HgCdTe photodiode/APD response times and fields.

If BTBT is not the first mechanism to limit speed, that is the result: follow the mechanism that intervenes first.

Do not return to abstract universal resource laws unless this concrete material branch exposes a genuine missing invariant.