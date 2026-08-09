# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; active frontier is finite-length HgCdTe high-field transport / nonlocal impact ionization; no novelty claim

This is the epistemic boundary. Detailed history remains in `RESEARCH_LOG.md` and dedicated derivation files.

## Status vocabulary

- **KNOWN:** established prior theory / experiment used as input.
- **DERIVED:** follows analytically from stated repository assumptions.
- **CHECKED:** independently/numerically verified.
- **CONDITIONAL:** derived but dependent on a deliberately simplified model.
- **INVALIDATED:** explicit counterexample or corrected interpretation found.
- **OPEN:** unresolved.
- **NON-CLAIM:** explicitly not asserted.

---

## 1. Major invalidated universal routes

### H1 — active-volume-only detector limit — INVALIDATED

An ideal passive field-concentrating family permits

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

Do not revive universal relations such as `eta^2 B <= C V_a` without new explicit constraints.

### H2 — finite absorber count as one-photon speed limit — INVALIDATED

The accessible one-photon / one-excitation sector remains linear.

### H3 — finite internal storage rank as always-on detector capacity — INVALIDATED AS UNIVERSAL

Fixed protocol:

```math
\sum_j\eta_j\le r.
```

Adaptive instrument:

```math
\sum_j\eta_j\le rd.
```

But an unrestricted output continuum can export arbitrarily large arrival-time/branch distinguishability.

### H4 — local Landauer erasure as universal adaptive-detector cost — INVALIDATED

The useful output can carry branch information; local erasure need not occur at the detector.

### H5 — single-Lorentzian `B^2/Delta` leakage law as universal — INVALIDATED

Higher-order filters suppress occupied-side tails much faster at fixed FWHM, while spending states/delay.

### H6 — spectral FWHM as architecture-independent electronic speed — INVALIDATED

Multipole group/Wigner delay can grow at fixed FWHM.

### H7 — direct BTBT is automatically the first high-field speed limiter for ordinary LWIR HgCdTe — INVALIDATED AS WORKING HYPOTHESIS

The corrected finite-length analysis shows that high-field transport becomes non-ohmic before direct BTBT is important, while finite impact-ionization probability must be treated with dead space / energy history rather than equating bulk `~100 V/cm` onset with a micron-device ionization ceiling.

### H8 — bulk II onset field equals finite-device II threshold — INVALIDATED INTERPRETATION

Bulk Monte Carlo rate onset and finite-device one-pass ionization probability are different observables.

---

## 2. Retained passive-network result

For a finite stable passive strictly proper optical-to-detector network with

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

### D1 — exact Gramian decomposition — DERIVED

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

### D2 — harmonic transfer-area bound — DERIVED / CHECKED

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

A matched one-mode passive resonance saturates it.

**Novelty status:** standard `H_2`/Lyapunov/passivity ingredients; exact mathematical priority unassessed; no novelty claim.

This is retained structure, not the active material frontier.

---

## 3. Semiconductor Fermi-contact baseline

For one electronic state weakly coupled to a Fermi contact,

### D3 — extraction / reverse-loading ratio — KNOWN + DERIVED COMPOSITION

```math
\boxed{
\frac{k_{\rm in}}
{k_{\rm out}}
=
\zeta e^{-(E-\mu)/(k_BT)}.
}
```

If extraction competes with recombination,

```math
\eta_{\rm col}
=\frac{k_{\rm out}}
{k_{\rm out}+k_r},
```

```math
B_{\rm evt}
=\frac{k_{\rm out}+k_r}{2\pi},
```

then

```math
\boxed{
k_{\rm in}
=2\pi\zeta\eta_{\rm col}B_{\rm evt}
 e^{-(E-\mu)/(k_BT)}.
}
```

`k_in` is a reverse-loading hazard, not automatically a measured dark current/count.

---

## 4. Electronic energy-filter results

### D4 — one Breit-Wigner zero-temperature leakage — DERIVED

```math
\boxed{
R_{\rm leak}
=
\frac{\Gamma_E}{2h}
\left[
\frac\pi2-
\arctan(2\Delta/\Gamma_E)
\right].
}
```

Sharp-filter one-pole asymptotic:

```math
R_{\rm leak}\simeq hB_{\rm evt}^2/(4\Delta).
```

### D5 — multipole tail / delay counterexample — DERIVED

For the stated Butterworth-type family,

```math
R_N
\simeq
\frac{\Gamma_E}{2h(2N-1)}
\left(\frac{\Gamma_E}{2\Delta}\right)^{2N-1},
```

while

```math
\tau_g(0)
=\frac{2\hbar}{\Gamma_E}
\csc\left(\frac{\pi}{2N}\right).
```

Thus filter order is a rejection resource and FWHM alone is not speed.

---

## 5. Fixed-thickness field-driven collection

For a constant-velocity transit,

```math
\boxed{
B_{\rm tr}
=c_t\frac{v_d}{L},
\qquad
c_t\simeq0.44295.
}
```

In the low-field approximation `v_d=mu F` with generic Kane-type

```math
J=A F^2e^{-F_K/F},
```

### D6 — fixed-thickness speed/BTBT relation — DERIVED / CONDITIONAL

```math
\boxed{
J(B_{\rm tr})
=
A\left(
\frac{LB_{\rm tr}}{c_t\mu}
\right)^2
\exp\left[-
\frac{F_Kc_t\mu}{LB_{\rm tr}}
\right].
}
```

Shrinking `L` is an explicit escape; this is not universal.

Low-field `mu F` extrapolation into the HgCdTe high-field regime is forbidden.

---

## 6. HgCdTe Kane / direct-BTBT normalization

Using the simplified narrow-gap relation

```math
E_g=2m_Kv_K^2,
\qquad
v_K\simeq1.07\times10^6\ {\rm m/s},
```

and identifying the BTBT mass with `m_K` only for this scaling model:

### D7 — characteristic BTBT field — DERIVED / CONDITIONAL

```math
\boxed{
F_K
=\frac{\pi E_g^2}{4q\hbar v_K}
=\frac{\pi^3\hbar c^2}
{qv_K\lambda_c^2}.
}
```

Thus

```math
F_K\propto\lambda_c^{-2}.
```

### D8 — Kane length — DERIVED

```math
\boxed{
\ell_K
=\frac{\hbar v_K}{E_g}
=\frac{v_K}{2\pi c}\lambda_c.
}
```

### D9 — normalized direct-BTBT shape — DERIVED / CHECKED

For a uniform region `V=FL`,

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
j=J/J_K,
```

with

```math
\boxed{
J_K
=\frac{q\pi^3c^4L}
{4v_K^3\lambda_c^4}.
}
```

Then

```math
\boxed{j=x^2e^{-1/x}.}
```

Exact inversion:

```math
\boxed{
F_J
=\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
}
```

**Status:** exact nondimensionalization after stated simplifying substitutions; no novelty claim.

---

## 7. Field-regime crossover

Write

```math
J_{\rm BTBT}
=C L F^2
\exp[-D/(F\lambda_c^2)],
```

where

```math
C=\frac{q^3}{4\pi^3\hbar^2v_K},
\qquad
D=\frac{\pi^3\hbar c^2}{qv_K}.
```

### D10 — exact crossover cutoff at a stated field/current budget — DERIVED / CHECKED

```math
\boxed{
\lambda_\times
=
\left[
\frac{D}
{F_R\ln(CLF_R^2/J_*)}
\right]^{1/2}.
}
```

For `L=1 um`, `J*=1e-12 A/cm2`, the simplified model gives

```text
F_R=100 V/cm  -> lambda_x~74.4 um
F_R=500 V/cm  -> lambda_x~31.7 um
F_R=1 kV/cm   -> lambda_x~22.0 um.
```

This demonstrates that ordinary 8–14 um direct BTBT is still exponentially closed across much of the non-ohmic transport regime in this stripped model.

### D11 — local marginal field-cost identity — DERIVED

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln F}
=2+\frac{F_K}{F}.
}
```

For

```math
s_v=d\ln v/d\ln F,
```

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln B_{\rm tr}}
=\frac{2+F_K/F}{s_v(F)}.
}
```

As `s_v -> 0+`, field becomes an inefficient way to buy additional transit speed even if absolute BTBT remains small.

---

## 8. Finite impact-ionization dead space

Let

```math
E_{\rm th}=\chi E_g.
```

### D12 — cold-injection field-work threshold — DERIVED / CONDITIONAL

```math
\boxed{
F_{\rm dead}
\simeq
\frac{\chi E_g}{qL}.
}
```

This is a cold-injection field-work estimate, not a universal stochastic onset field.

### D13 — dead-space / Kane-scale relation — DERIVED

```math
\boxed{
\frac{F_{\rm dead}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L}.
}
```

### D14 — normalized direct BTBT at the dead-space scale — DERIVED

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

For `L >> ell_K`, this is exponentially small.

This gives a cleaner reason why finite impact-ionization accessibility can precede strong direct BTBT than simply comparing a bulk `100 V/cm` onset against a BTBT field table.

---

## 9. Nonlocal mean-energy surrogate

### D15 — effective acceleration length — DERIVED

For

```math
\dot\varepsilon
=qFv-\varepsilon/\tau_E,
```

with

```math
\ell_E=v\tau_E,
```

```math
\boxed{
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}),
}
```

and

```math
\boxed{
\varepsilon(L)=qF L_{\rm eff}.
}
```

### D16 — mean threshold field — DERIVED / CONDITIONAL

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=\frac{\Delta E_{\rm th}}
{qL_{\rm eff}}.
}
```

For cold injection, `E_th=chi E_g`:

```math
\boxed{
\frac{F_{\rm th}^{(\rm mean)}}{F_K}
=\frac{4\chi}{\pi}
\frac{\ell_K}{L_{\rm eff}}.
}
```

Limits:

```text
L << ell_E -> finite ballistic dead space
L >> ell_E -> bulk-like energy-relaxation limit.
```

This is a mean-trajectory criterion, not a true stochastic II onset; a high-energy distribution tail can ionize while the mean remains below threshold.

---

## 10. First closed nonlocal II probability surrogate

Prior HgCdTe APD models use

```math
\Gamma_{\rm II}(E)
=A
\frac{(E/E_{\rm th}-1)^\alpha}
{(E/E_{\rm th})^\beta}
```

above threshold.

For the analytic test case

```math
\alpha=1,
\qquad
\beta=0,
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
\boxed{
P_{\rm II}=1-e^{-\Xi_{\rm II}}.
}
```

### D17 — dimensionless collapse — DERIVED / CHECKED

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

The analytic test-case probability becomes

```math
\boxed{
P_{\rm II}=1-e^{-aH(\theta,\ell)}.
}
```

The closed hazard was independently checked by direct numerical time integration.

**Status:** analytic surrogate only. The target-composition calibration of `tau_E(F)` and `A,alpha,beta` remains OPEN.

---

## 11. Established external HgCdTe facts used now

### K1 — KNOWN

Primary Monte Carlo work specifically for `Hg_0.8Cd_0.2Te` at 77 K calculates drift velocity, mean energy, impact-ionization rate, velocity relaxation and energy relaxation, and reports hot-electron / II physics at fields of order `10^2 V/cm` in bulk.

### K2 — KNOWN

The same literature states that analytical interpolation formulas were provided, but the currently accessible primary-source text does not expose the coefficients required for direct reuse.

### K3 — KNOWN

Modern HgCdTe APD modeling evaluates II probability from carrier energy history; dead-space / history-dependent treatment is established and necessary in thin multiplication regions.

### K4 — KNOWN

A steady-state electron velocity scale of order `5e5 m/s` is consistent with target-composition high-field transport studies; submicron transient overshoot can be larger and must not be substituted as universal steady-state drift.

---

## 12. Current open quantities

### O1 — OPEN

Target `Hg_0.8Cd_0.2Te`, 77 K energy-relaxation law

```text
tau_E(F)
or
ell_E(F).
```

### O2 — OPEN

Target energy-dependent impact-ionization rate

```text
Gamma_II(E)
```

or calibrated `A,alpha,beta` suitable for the target composition/temperature.

### O3 — OPEN

Trap-assisted tunneling field/current relation for the same geometry and defect assumptions.

### O4 — OPEN

Full detector speed after combining transit with lifetime, diffusion, contacts, RC, readout, etc.

---

## 13. Explicit non-claims

Do **not** claim

- a universal photodetector limit;
- a universal HgCdTe speed-dark-current theorem;
- that `100 V/cm` is the II ceiling of a `1 um` detector;
- that the mean-energy surrogate reproduces the stochastic high-energy tail;
- that `E_th=E_g` is exact for every HgCdTe composition;
- that direct BTBT is negligible in every LWIR junction geometry;
- that BTBT is always secondary to II/TAT;
- a complete HgCdTe dark-current model;
- novelty of the dead-space or nonlocal surrogate ingredients;
- readiness for a manuscript.

---

## 14. Current promotion criterion

The next material result should either

1. calibrate the nonlocal surrogate from primary `x=0.20`, 77 K transport/II data; or
2. prove that the device-level mechanism ordering is insensitive over a physically defensible range of `ell_E` and `A tau_E`.

Only then add TAT and compare the diode-like field problem with HgCdTe photoconductors, where lifetime/gain may replace transit as the dominant speed physics.
