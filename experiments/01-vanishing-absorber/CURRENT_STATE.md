# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is finite-length HgCdTe high-field mechanism ordering, with nonlocal impact ionization and TAT now explicit; no novelty claim

## 1. Current question

The project began by asking whether an ideal photodetector could be made arbitrarily small, fast, sensitive, and perfectly absorbing.

Successive counterexamples killed simple universal answers based on active volume, absorber count, finite storage rank, spectral FWHM, or one fixed optical architecture.

The active question is now concrete:

> **For narrow-gap HgCdTe, what carrier-transit speed is physically useful once high-field velocity, finite impact-ionization history, trap-assisted tunneling, and direct BTBT are treated as separate mechanisms?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_RELAXATION_LENGTH_PHASE_BOUNDARY.md`
2. `HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
3. `HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md`
4. `HGCDTE_TAT_FIELD_SCALE.md`
5. `HGCDTE_TAT_BTBT_CROSSOVER.md`
6. `HGCDTE_FIELD_REGIME_MAP.md`
7. `HGCDTE_TRANSPORT_BTBT_PHASE_BOUNDARY.md`
8. `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
9. `HGCDTE_KANE_SCALE_AUDIT.md`
10. `CLAIM_LEDGER.md`
11. `RESEARCH_LOG.md`
12. older derivations only for provenance.

---

## 3. Direct BTBT baseline

Within the published uniform-field HgCdTe BTBT form plus the simplified Kane-mass substitution,

```math
\boxed{
J_{\rm BTBT}
=
\frac{q^3L}{4\pi^3\hbar^2v_K}
F^2e^{-F_K/F},
}
```

with

```math
\boxed{
F_K
=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2},
}
```

and

```math
\boxed{
J_K
=\frac{q\pi^3c^4L}
{4v_K^3\lambda_c^4}.
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

Thus

```math
F_K\propto\lambda_c^{-2},
\qquad
J_K\propto L\lambda_c^{-4}.
```

This is a scaling model, not a calibrated total-dark-current model.

---

## 4. Bulk high-field onset is not a finite-device II ceiling

Primary Monte Carlo work on bulk `Hg_0.8Cd_0.2Te` at 77 K shows hot-electron / non-ohmic / impact-ionization physics becoming relevant at fields of order `10^2 V/cm`.

That must **not** be converted directly into

```text
finite 1 um detector ionizes at 100 V/cm.
```

A finite injected electron must acquire the ionization threshold energy over its actual history.

HgCdTe APD literature therefore treats impact ionization as history dependent and includes dead-space effects.

---

## 5. Cold-injection dead-space / Kane relation

Let

```math
E_{\rm th}=\chi E_g.
```

The cold field-work estimate is

```math
\boxed{
F_{\rm dead}
\simeq
\frac{\chi E_g}{qL}.
}
```

Using

```math
\ell_K
=\frac{\hbar v_K}{E_g},
```

```math
\boxed{
\frac{F_{\rm dead}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L}.
}
```

At this field the normalized direct-BTBT current is

```math
\boxed{
j_{\rm dead}
=
\left(
\frac{4\chi\ell_K}{\pi L}
\right)^2
\exp\left[-
\frac{\pi L}{4\chi\ell_K}
\right].
}
```

For `L >> ell_K`, direct BTBT remains exponentially suppressed even when a cold carrier can in principle acquire the II threshold energy.

This is a field-work threshold, not a stochastic II onset theorem.

---

## 6. Nonlocal mean-energy surrogate

Use

```math
\boxed{
\dot\varepsilon
=qFv-\varepsilon/\tau_E.
}
```

Define

```math
\ell_E=v\tau_E,
```

and

```math
\boxed{
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}).
}
```

Then

```math
\boxed{
\varepsilon(L)=qF L_{\rm eff},
}
```

and the **mean-energy** threshold field is

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=\frac{\Delta E_{\rm th}}
{qL_{\rm eff}}.
}
```

For cold injection, `E_th=chi E_g`,

```math
\boxed{
\frac{F_{\rm th}^{(\rm mean)}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L_{\rm eff}}.
}
```

This bridges

```text
L << ell_E
-> ballistic dead space

L >> ell_E
-> bulk-like energy-relaxation ceiling.
```

The mean trajectory does not represent the stochastic high-energy tail.

---

## 7. First closed nonlocal II probability surrogate

For the analytic energy-dependent rate test case

```math
\Gamma_{\rm II}(E)
=A(E/E_{\rm th}-1),
\qquad E\ge E_{\rm th},
```

let

```math
E_{\rm ss}=qF\ell_E,
\qquad
T=L/v.
```

If `E_ss > E_th`,

```math
\boxed{
t_d
=\tau_E
\ln\left[
\frac{E_{\rm ss}}
{E_{\rm ss}-E_{\rm th}}
\right].
}
```

For `T > t_d`,

```math
\boxed{
\Xi_{\rm II}
=
\frac{A}{E_{\rm th}}
\left\{
(E_{\rm ss}-E_{\rm th})(T-t_d)
+E_{\rm ss}\tau_E
[e^{-T/\tau_E}-e^{-t_d/\tau_E}]
\right\},
}
```

```math
\boxed{P_{\rm II}=1-e^{-\Xi_{\rm II}}.}
```

Define

```math
\theta=qF\ell_E/E_{\rm th},
\qquad
\ell=L/\ell_E,
\qquad
a=A\tau_E.
```

The mean trajectory reaches threshold before exit iff

```math
\boxed{
\theta(1-e^{-\ell})>1.
}
```

For this rate test case,

```math
\boxed{P_{\rm II}=1-e^{-aH(\theta,\ell)}.}
```

The closed hazard was independently checked by direct numerical time integration.

---

## 8. New sensitivity result — critical energy-relaxation length

Let `F_J` be the exact direct-BTBT field for a chosen current-density budget `J_*`.

Define

```math
\boxed{
r=F_{\rm dead}/F_J.}
```

Set the mean ionization threshold equal to the BTBT-budget field:

```math
F_{\rm th}^{(\rm mean)}=F_J.
```

With

```math
y=L/\ell_E,
```

the boundary is

```math
\boxed{
\frac{1-e^{-y}}{y}=r.
}
```

For `0<r<1`, the nonzero solution is

```math
\boxed{
y_*
=\frac1r
+W_0[-r^{-1}e^{-1/r}],
}
```

so

```math
\boxed{
\ell_{E,*}=L/y_*.
}
```

Interpretation inside the mean-energy surrogate:

```text
ell_E > ell_E,*
-> mean II threshold occurs before the chosen BTBT budget

ell_E < ell_E,*
-> BTBT budget occurs before the mean reaches threshold.
```

This is one-sided evidence only: a stochastic high-energy tail can still ionize when the mean stays below threshold.

For `L=1 um`, `chi=1`, `J_*=1e-12 A/cm2`:

| cutoff | `ell_E,*` |
|---:|---:|
| 8 um | 0.231 um |
| 10 um | 0.288 um |
| 12 um | 0.348 um |
| 17 um | 0.529 um |
| 24 um | 0.926 um |

At 10 um this corresponds to roughly `0.6–1.2 ps` over a `2.5–5e5 m/s` representative high-field velocity range; at 17 um, roughly `1.1–2.1 ps`.

The available target-material transport literature places the relevant relaxation physics on a comparable timescale but does not expose enough high-field coefficients to decide the ordering cleanly.

Do not infer the high-field `tau_E` from low-field mobility alone.

---

## 9. Trap-assisted tunneling now enters explicitly

A standard one-dimensional HgCdTe TAT exponent for a trap a depth

```math
\Delta_t=E_g-E_T
```

below the conduction band is

```math
\boxed{
F_{\rm TAT}
=
\frac{4\sqrt{2m^*}\Delta_t^{3/2}}
{3q\hbar}.
}
```

Compared with direct BTBT,

```math
\boxed{
\frac{F_{\rm TAT}}{F_K}
=
\frac{16}{3\pi}
\left(\frac{\Delta_t}{E_g}\right)^{3/2}.
}
```

Representative values:

```text
Delta_t = 0.5 Eg -> F_TAT/F_K = 0.600
0.3 Eg            -> 0.279
0.1 Eg            -> 0.0537
0.05 Eg           -> 0.0190.
```

Thus near-band-edge traps can reduce the tunneling exponent field by one to two orders of magnitude relative to direct BTBT.

This is why an exponentially tiny direct-BTBT current is **not** evidence that tunneling leakage is absent.

---

## 10. TAT–BTBT current crossover

Within the shared simplified current models,

```math
\boxed{
\frac{J_{\rm TAT}}{J_{\rm BTBT}}
=
\frac{\pi^2\kappa_d^2N_T\sqrt{m^*E_g}}
{2\sqrt2q\hbar\Delta_tF}
\exp[(F_K-F_T)/F].
}
```

Therefore the trap density at which TAT equals direct BTBT is

```math
\boxed{
N_{T,\times}
=
\frac{2\sqrt2q\hbar\Delta_tF}
{\pi^2\kappa_d^2\sqrt{m^*E_g}}
\exp[-(F_K-F_T)/F].
}
```

For an allowed TAT current `J_{T,*}` in a uniform region `V=FL`,

```math
\boxed{
N_{T,\max}
=
\frac{8\pi\hbar^3\Delta_t}
{q^2m^*FL\kappa_d^2}
J_{T,*}e^{F_T/F}.
}
```

This turns the field/speed requirement into a material-quality specification **once trap energy and defect matrix element are known**.

---

## 11. Real HgCdTe trap benchmarks

Primary HgCdTe detector studies support the practical relevance of this branch:

- 77 K LWIR numerical analysis found the most sensitivity-degrading trap near `0.7 E_g` for a `~10 um` cutoff detector and found TAT-related `1/f` noise dominant for `>11 um` sensors at trap density as low as `1e14 cm^-3`;
- measured `12.5 um` arrays were fitted with trap densities of approximately `1e13–1e14 cm^-3` and an ionization energy near `30 meV`, with TAT dominating the 50 K dark current;
- older HgCdTe diode analyses have fitted TAT using traps only a few meV below the conduction edge.

These are architecture/material-specific observations, not universal trap values.

But they show that the trap densities required for TAT relevance are technologically realistic, not pathological counterexamples.

---

## 12. Correct current mechanism ordering

The current hierarchy is now:

```text
low field
-> ohmic drift

bulk ~10^2 V/cm scale
-> non-ohmic / hot-electron distribution develops

finite device
-> II probability depends on available acceleration length, energy relaxation and high-energy tail

near-band-edge defects
-> TAT can open far below the direct-BTBT exponent scale

intrinsic full-gap tunneling
-> direct BTBT becomes important at still higher field / longer wavelength / more extreme geometry.
```

Therefore there is no single universal “tunneling field” and no single universal high-field speed limiter.

The practical optimization is

```math
\boxed{
F_{\rm opt}
=\arg\max_F v(F)
}
```

subject to separate constraints on

```math
P_{\rm II}(F,L),
```

```math
J_{\rm TAT}(F),
```

```math
J_{\rm BTBT}(F),
```

plus SRH/Auger/surface/contact/readout constraints.

---

## 13. Transit-speed scale retained

For a constant-velocity Ramo pulse,

```math
\boxed{
B_{\rm tr}
=c_t\frac{v}{L},
\qquad
c_t\simeq0.44295.
}
```

Published target-composition transport calculations give high-field velocity scales that vary with doping/model, roughly `2.5–5e5 m/s` in the recovered bulk calculations, with substantially larger transient overshoot possible in submicron structures.

Do not promote one value to a universal HgCdTe saturation velocity.

---

## 14. Reproducibility

Active material regressions:

```text
numerics/hgcdte_btbt_normalized_sweep.py
numerics/hgcdte_field_regime_map.py
numerics/hgcdte_impact_dead_space.py
numerics/hgcdte_nonlocal_ii_surrogate.py
numerics/hgcdte_relaxation_length_phase_boundary.py
```

No CI is needed yet.

---

## 15. External-data boundary

The exact target-composition high-field calibration remains incomplete.

Needed for II:

```text
tau_E(F) or ell_E(F)
+
Gamma_II(E) / calibrated energy-dependent rate.
```

Needed for TAT:

```text
trap-energy distribution
+
N_T
+
defect matrix/capture strength
+
local field profile / depletion width.
```

Do not reconstruct missing coefficients from narrative text and silently call them primary data.

---

## 16. Next decisive step

The next useful calculation is no longer another intrinsic scaling law.

Use the TAT density expression to ask:

> **At the field actually needed for a target transit time, are detector-grade HgCdTe trap densities low enough to keep TAT below the chosen dark-current budget?**

This requires a defined device geometry and trap model.

In parallel, the II phase boundary has reduced the missing energy-relaxation information to a sub-ps/few-ps classification problem rather than a full arbitrary interpolation.

After the diode-like high-field problem is stable, compare with HgCdTe photoconductors, where carrier lifetime and photoconductive gain may dominate the speed physics instead of transit time.
