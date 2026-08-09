# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; abstract universal routes repeatedly narrowed or invalidated; current active branch is material-specific HgCdTe extraction/BTBT normalization; no novelty claim

This ledger records what is known, derived here, invalidated, or still open. Historical detail remains in `RESEARCH_LOG.md` and the dedicated derivation files.

---

## 1. Active organizing question

The original target

```text
small active volume
+
high absorption
+
high speed
+
low noise
```

has evolved into the concrete semiconductor question

> **For HgCdTe at a specified cutoff wavelength, temperature, collection thickness, and allowed dark-current density, what carrier-transit speed is achievable before high-field transport and tunneling intervene?**

The current load-bearing unknown is the real high-field velocity law `v_d(F)` for a stated material/composition/temperature.

---

## 2. Established prior ingredients — not novelty targets

Do not claim novelty for

- temporal coupled-mode theory / critical coupling;
- `H_2`, Lyapunov, scattering-passive network theory;
- LDOS/material power-bandwidth bounds;
- deep-strong light-matter decoupling;
- quantum frequency conversion and Schmidt temporal modes;
- dynamically matched single-photon capture;
- adaptive quantum instruments / Kraus-rank accounting;
- Landauer/Holevo/bosonic information-capacity theory;
- Fermi-contact detailed balance;
- Breit-Wigner/Landauer resonant transport;
- Butterworth/filter-order and Wigner-Smith delay theory;
- HgCdTe Kane/nonparabolic band structure;
- HgCdTe BTBT, TAT, impact ionization, resonant-tunneling dark-current engineering;
- high-field Monte Carlo transport in HgCdTe.

---

## 3. Stopped / invalidated general routes

### H1 — universal active-volume law — STOPPED

A passive field-concentrating continuum counterexample has

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

Do not revive universal relations of the form

```text
eta^2 B <= C V_a
```

without new explicit constraints.

### H2 — finite absorber count as the one-photon speed limit — STOPPED

The one-photon one-excitation sector remains linear.

### H3 — finite detector storage rank as an always-on capacity — STOPPED

Adaptive branching gives

```math
\sum_j\eta_j\le rd,
```

and an unrestricted output continuum can make `d` effectively unbounded by exporting arrival-time information.

### H4 — local Landauer work as universal adaptive detector cost — STOPPED

Branch information can be exported in the useful output rather than erased locally. Output time-bandwidth can substitute for output energy.

### H5 — single-Lorentzian `R_leak ~ hB^2/(4Delta)` as universal electronic speed/leakage law — STOPPED

Higher-order filters can suppress the tail much more strongly at the same spectral FWHM.

### H6 — spectral FWHM as architecture-independent carrier speed — STOPPED

Multipole filters have growing group/Wigner delay at fixed FWHM.

### H7 — faster semiconductor collection always requires larger field — STOPPED

Reducing collection thickness can increase transit speed while reducing the field required for a specified speed.

### H8 — largest internal coupling anywhere as a universal detector control parameter — STOPPED

Disconnected/spectator strong-coupling sectors are counterexamples.

---

## 4. Retained passive finite-network result

For a finite stable passive strictly proper optical-to-detector network, with

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

### D1 — exact Gramian decomposition

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

### D2 — harmonic access bound

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

A matched one-mode passive resonance saturates it.

**Status:** exact detector-facing passivity corollary; standard mathematical ingredients; exact priority unassessed; no novelty claim.

---

## 5. Retained active/time-domain resource results

### D3 — finite pumped conversion strength

For

```math
H_{\rm conv}/\hbar
=\mathbf b^\dagger K\mathbf a+h.c.,
```

`M_c` orthogonal conversion channels with efficiency at least `eta` in time `tau` require

```math
\boxed{
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
}
```

### D4 — exact known-mode loading schedule

For one time-controlled storage mode,

```math
\boxed{
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
}
```

With bounded coupling,

```math
\boxed{
\eta_{\rm cap}
\le1-e^{-2\kappa_{\max}\tau}.
}
```

### D5 — adaptive finite-instrument capacity

For `d` successful branches each terminating in at most `r` retained modes,

```math
\boxed{
\sum_j\eta_j\le rd.
}
```

For equal-prior inputs and average success `eta_bar`, successful branch entropy obeys

```math
\boxed{
H_{\rm branch|succ}
\ge
\max\left[0,\ln(M\bar\eta/r)\right].
}
```

These results remain supporting insights, not current publication targets.

---

## 6. Semiconductor Fermi-contact result

Canonical file: `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`.

For one electronic state weakly coupled to a Fermi contact,

```math
\boxed{
\frac{k_{\rm in}}
{k_{\rm out}}
=
\zeta
\exp[-(E-\mu)/(k_BT)].
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

so

```math
\boxed{
k_{\rm out}
=2\pi\eta_{\rm col}B_{\rm evt},
}
```

and

```math
\boxed{
k_{\rm in}
=
2\pi\zeta\eta_{\rm col}B_{\rm evt}
\exp[-(E-\mu)/(k_BT)].
}
```

**Scope:** sequential weak tunneling. `k_in` is reverse loading hazard, not automatically dark current/count.

---

## 7. Lifetime-broadened resonant-filter result

Canonical file: `RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md`.

For a unit-peak Breit-Wigner resonance centered `Delta` above a zero-temperature filled source,

```math
\boxed{
R_{\rm leak}
=
\frac{\Gamma_E}{2h}
\left[
\frac\pi2
-
\arctan\left(\frac{2\Delta}{\Gamma_E}\right)
\right].
}
```

For a one-pole lifetime bandwidth `B_evt=Gamma_E/h`, sharp-filter asymptotic:

```math
\boxed{
R_{\rm leak}
\simeq
\frac{hB_{\rm evt}^2}{4\Delta}.
}
```

**Status:** exact one-resonance model result; not universal once higher-order filters are admitted.

---

## 8. Multipole energy-filter result

Canonical file: `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md`.

For

```math
\mathcal T_N(E)
=
\frac1{1+[2(E-E_0)/\Gamma_E]^{2N}},
```

sharp-stopband leakage is

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

Minimum-phase Butterworth center group delay:

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

**Interpretation:** filter order is a real rejection resource, but it carries internal-state/delay cost. No universal delay-leakage theorem was established.

---

## 9. Fixed-thickness field-driven collection

Canonical file: `FIELD_DRIVEN_COLLECTION_TUNNELING.md`.

For one constant-velocity transit under the rectangular Ramo-pulse convention,

```math
\boxed{
B_{\rm tr}
=c_t\frac{v_d}{L},
\qquad
c_t\simeq0.44295.
}
```

In the low-field drift model `v_d=mu F` and a generic Kane law

```math
J=A F^2e^{-F_K/F},
```

### D6 — fixed-thickness transit/BTBT relation

```math
\boxed{
J(B_{\rm tr})
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

At fixed `L`, this is monotonic increasing in `B_tr`.

**Scope:** low-field mobility model only. The branch explicitly records thinning `L` as a counterexample to universality.

---

## 10. Small-`L` ballistic barrier audit

Canonical file: `BALLISTIC_BARRIER_SPEED_LEAKAGE.md`.

For one rectangular barrier separating dark and useful carrier energies by `Delta E`, optimize barrier placement at fixed useful ballistic transit bandwidth.

### D7 — optimized one-barrier exponent

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

Equivalent inverse-transit-rate form:

```math
\mathcal T_d
\gtrsim
\exp[-2\Delta E/(\hbar\Omega_{\rm tr})].
```

The effective mass cancels in the ideal parabolic model.

**Scope:** one barrier only. Multi-barrier/resonant structures are explicit counterexamples.

---

## 11. HgCdTe Kane scaling

Canonical file: `HGCDTE_KANE_SCALE_AUDIT.md`.

Using the simplified narrow-gap relation

```math
E_g=2m_Kv_K^2,
```

with `v_K ~= 1.07e6 m/s`, and identifying the tunneling mass with `m_K` for a scaling audit:

### D8 — characteristic BTBT field

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

Hence

```math
\boxed{F_K\propto\lambda_c^{-2}.}
```

### D9 — Kane length

```math
\boxed{
\ell_K
=\frac{\hbar v_K}{E_g}
=\frac{v_K}{2\pi c}\lambda_c,
}
```

so

```math
\boxed{\ell_K\propto\lambda_c.}
```

**Status:** material scaling, not calibrated junction theory.

---

## 12. Current canonical HgCdTe BTBT normalization

Canonical file: `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`.

Start from the published uniform-field HgCdTe BTBT form

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

With `V=FL` and the simplified Kane-mass substitution

```math
m^*=E_g/(2v_K^2),
```

### D10 — HgCdTe simplified BTBT law

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

### D11 — universal normalized shape within this model

```math
\boxed{j=x^2e^{-1/x}.}
```

with

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

Thus

```math
F_K\propto\lambda_c^{-2},
\qquad
J_K\propto L\lambda_c^{-4}.
```

### D12 — exact inversion

```math
\boxed{
x(j)
=\frac1{2W_0[1/(2\sqrt j)]}.
}
```

Therefore

```math
\boxed{
F_{\max}^{\rm BTBT}
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
}
```

**Status:** exact nondimensionalization after explicit simplifying substitutions; no novelty claim.

Regression:

```text
numerics/hgcdte_btbt_normalized_sweep.py
```

---

## 13. Critical caveat on speed conversion

### H9 — using low-field `mu F` at the BTBT field ceiling — FORBIDDEN

Primary 77 K Monte Carlo work on `Hg_0.8Cd_0.2Te` reports hot-electron/non-ohmic and impact-ionization behavior around `100 V/cm`.

The direct-BTBT-only field ceilings from the simplified model can be several `kV/cm`.

Therefore the next speed calculation must use a traceable high-field `v_d(F)` model:

```math
\boxed{
B_{\rm tr,max}
=
\frac{c_t}{L}
\,v_d(F_{\max}^{\rm BTBT}).
}
```

Do not invent a generic saturation law merely to complete a plot.

---

## 14. Explicit non-claims

Do not claim

- a universal photodetector sensitivity-speed theorem;
- a universal HgCdTe speed-dark-current theorem;
- that direct BTBT is always the first practical dark-current limiter;
- that the simplified Kane tunneling mass is quantitatively exact at every cutoff;
- that `E_g=hc/lambda_c` is a precision bandgap model;
- that `v_K` is the drift saturation velocity;
- that the direct-BTBT-only field table is a safe operating-field table;
- novelty of the normalized `j=x^2 exp(-1/x)` collapse;
- readiness for a manuscript.

---

## 15. Current promotion criterion

The next result can be promoted only after a traceable high-field velocity model is coupled to the normalized BTBT inversion.

Required sequence:

1. obtain primary-source `v_d(F)` coefficients/curve for a specified HgCdTe composition, carrier density and temperature;
2. compute `F_max(J_*,lambda_c,L)`;
3. compute

```math
B_{\rm tr,max}=c_t v_d(F_{\max})/L;
```

4. identify whether hot-carrier/impact-ionization physics intervenes before the direct-BTBT target is reached;
5. only then add TAT/SRH and compare with real detector data;
6. perform a focused prior-art search on any resulting normalized frontier before novelty language.