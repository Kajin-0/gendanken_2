# Research Log — Experiment 01: The Vanishing Absorber

This file is chronological. It records **why the research direction changed**, including counterexamples, prior-art collisions, and branches that were deliberately stopped.

Detailed equations remain in the dedicated derivation files; this log preserves the path.

---

## 2026-08-08 — Experiment opened

Question:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

Initial intuition:

```text
smaller active volume
-> fewer bulk dark events

passive optical confinement
-> recover absorption

possible cost
-> photon dwell time / bandwidth.
```

No theorem was assumed.

---

## One-port resonance

The one-port absorber was derived exactly.

Critical coupling permits unity monochromatic absorption, but if the absorptive decay rate tends to zero the absorbed-power modulation bandwidth also tends to zero.

A separate toy bulk-dark-event optimization unexpectedly preferred mild overcoupling rather than exact critical coupling.

**Direction:** determine whether absorptive decay must scale with active volume.

---

## Active-volume route falsified

A shrinking-gap dielectric capacitor kept finite energy participation and finite absorptive decay while

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

The hoped-for active-volume-only theorem failed.

**Direction:** replace geometric volume by microscopic optical resources.

---

## Thermal input / microscopic absorber / LDOS chain

A one-channel thermal-background calculation produced a clean critical-coupling sensitivity-speed relation, but it was explicitly external background, not internal dark counts.

A finite two-level absorber remained linear in the one-photon one-excitation sector, so finite absorber count/saturation did not supply the missing speed limit.

Finite-transition LDOS bounds and finite-emitter form factors regularized some weak-coupling divergences, but oscillator-strength/extent inequalities still allowed the formal rate to approach `O(omega)` where perturbative Purcell/Markov theory failed.

**Direction:** treat light and matter nonperturbatively.

---

## Nonperturbative Hopfield branch

A TRK-consistent Hopfield model reproduced deep-strong light-matter decoupling in detector-transfer language: peak matching could survive while external transfer linewidth collapsed.

A stronger fixed-target retuning attack held one dressed mode at fixed positive detector frequency while `g -> infinity`. With fixed local optical/detector bath resources,

```math
\min(\Gamma_L,\Gamma_R)\to0.
```

A targeted literature search found extensive deep-strong-decoupling prior art but no inspected source stating that exact fixed-target two-reservoir corollary.

Status remained

> **candidate distinct supporting lemma; priority unproven.**

Allowing the external reservoirs themselves to scale showed the result could be escaped only by spending new reservoir resource; the minimum bare resource grew asymptotically as `sqrt(g)` for fixed peak/linewidth targets.

**Direction:** attack with multimode optics.

---

## Passive multimode branch

A disconnected spectator sector killed any theorem based only on the largest internal coupling anywhere in a multimode Hamiltonian.

A bank of narrow resonances showed that useful mode count/density could tile a broad band.

This motivated integrated transfer rather than individual linewidth.

The finite passive optical-to-detector transfer area became an `H2` norm. A preliminary

```math
\mathcal I\le2\min(L,R)
```

bound was immediately superseded by the exact harmonic result

```math
\boxed{
\mathcal I
\le
\frac{2LR}{L+R}.
}
```

The Gramian eigenbasis gives

```math
\frac{\mathcal I}{2}
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
```

A single matched resonance saturates the theorem.

Random passive-network stress tests found no violations.

**Direction:** attack direct feedthrough and structured continua.

---

## Direct feedthrough / continuum audits

An ideal frequency-independent prompt optical-to-detector block makes the all-frequency `H2` area divergent. This was retained as a real scope failure: the prompt path imports infinite Markov bandwidth.

Finite passive reaction-coordinate/pseudomode embeddings continued to obey the harmonic bound when terminal budgets and `H2` limits remained finite.

**Conclusion:** spectral complexity is not free under those assumptions, but unrestricted prompt/continuum resources lie outside the theorem.

---

## Optical-access / thermodynamic bridge and major prior-art collisions

Known one-channel thermodynamic optical-coupling theory was combined with the passive harmonic bound to obtain a receiving-side access requirement.

Local detailed balance then tied forward detector relaxation to reverse thermal activation.

Before building a generic detector cycle, a major prior-art collision appeared:

- Young, Sarovar & Leonard (2018) already treat incoming quantum fields, absorption, detector amplification, efficiency, dark counts, and timing.
- Schwarzhans et al. (2026) already treat autonomous nonequilibrium detector work, amplification/reset, internal dark counts, jitter, dead time, and entropy production.

The latter explicitly starts its thermodynamic analysis after the excitation is already captured.

A three-level capture-machine testbed was still useful for separating gross click rate from net thermodynamic current and for showing that readiness pumping restores, but does not exceed, a fully ready absorptive population factor unless actual optical gain is introduced.

A publication-boundary audit concluded:

> **Continue the research. Do not write a manuscript yet.**

**Direction:** attack with genuinely active/coherent capture.

---

## Active frequency conversion

A pumped two-mode converter gave a known architecture-level baseline:

```math
G_{\min}=W/(2\sqrt2),
```

and for `G=g_0 sqrt(N_p)`,

```math
N_p\ge W^2/(8g_0^2).
```

Multimode allocation showed the apparent gain from splitting the band disappears if total nonlinear coupling strength is fixed.

A traveling-wave calculation showed the pump exponent depends on the first nonzero phase-mismatch derivative; dispersion engineering migrates rather than universally removes the cost.

A singular-value formulation produced the finite-mode bookkeeping bound

```math
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
```

The unresolved physical quantity became the device's pump-to-conversion operator strength.

**Direction:** attack with explicit time dependence.

---

## Known-time time-dependent capture

For one controlled lossless storage mode, perfect zero-reflection loading of a known photon mode requires

```math
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
```

With bounded coupling over loading duration `tau`,

```math
\eta_{\rm cap}
\le
1-e^{-2\kappa_{\max}\tau}.
```

Thus dynamic control can beat a stationary frequency match for one scheduled temporal mode.

**Direction:** remove knowledge of arrival time.

---

## Unknown arrival and adaptive control

For a fixed linear map accepting `M` orthogonal possible temporal inputs into `r` retained modes,

```math
\sum_j\eta_j\le r.
```

Adaptive feedforward defeats the `r`-only statement. Modeling `d` successful Kraus branches gave the exact finite-instrument extension

```math
\boxed{
\sum_j\eta_j\le rd.
}
```

with a tight partition construction.

For a uniform input ensemble, successful branch entropy obeys

```math
H_{\rm branch|succ}
\ge
\max[0,\ln(M\bar\eta/r)].
```

A deterministic numerical regression was added.

---

## Output-continuum counterexample — abstract space-time branch closed

The tempting Landauer conclusion failed as a universal detector statement.

A detector can export branch/arrival-time information as its useful output instead of erasing it locally.

One output quantum spread among `D_out` orthogonal temporal modes can carry `ln D_out` nats at fixed event energy.

A restricted bosonic record condition was written as

```math
D_{\rm out}
g(N_{\rm out}/D_{\rm out})
\ge
\ln(M\bar\eta/r),
```

but the key counterexample was conceptual:

```text
unrestricted output continuum
-> arbitrarily large record dimension
-> no universal finite internal space-time detector capacity.
```

**Decision:** stop stacking abstract resource coordinates. Return to actual semiconductor physics.

---

## Semiconductor Fermi-contact mapping

For one photoexcited state coupled weakly to a Fermi contact,

```math
\frac{k_{\rm in}}{k_{\rm out}}
=
\zeta e^{-(E-\mu)/(k_BT)}.
```

If extraction competes with recombination,

```math
k_{\rm out}
=2\pi\eta_{\rm col}B_{\rm evt},
```

so

```math
k_{\rm in}
=
2\pi\zeta\eta_{\rm col}B_{\rm evt}
 e^{-(E-\mu)/(k_BT)}.
```

This made the access concept concrete: stronger tunnel coupling speeds extraction and reverse loading together; the directionality comes from energy/chemical-potential bias.

But moving the collecting level many `kBT` above the Fermi level looked like an escape.

**Direction:** include finite spectral linewidth.

---

## Resonant energy filter — zero-temperature lifetime-broadening leakage

For one unit-peak Breit-Wigner resonance centered `Delta` above a zero-temperature filled source,

```math
R_{\rm leak}
=
\frac{\Gamma_E}{2h}
\left[
\frac\pi2
-\arctan(2\Delta/\Gamma_E)
\right].
```

With the one-pole lifetime bandwidth `B=Gamma_E/h`, the sharp-filter limit gives

```math
R_{\rm leak}
\simeq
hB^2/(4\Delta).
```

This showed that zero thermal occupation does not eliminate leakage once extraction broadening overlaps the occupied Fermi sea.

**Direction:** attack with higher-order filters.

---

## Multipole energy-filter counterexample

An `N`th-order Butterworth-type probability can suppress the occupied-side tail as

```math
R_N
\sim
\frac{\Gamma_E}{2h(2N-1)}
\left(\frac{\Gamma_E}{2\Delta}\right)^{2N-1}.
```

Thus the single-Lorentzian `B^2/Delta` law is not universal at fixed FWHM.

But the causal minimum-phase group delay grows as

```math
\tau_g(0)
\sim
4N\hbar/(\pi\Gamma_E).
```

**Correction:** spectral FWHM is not an architecture-independent carrier-speed metric.

Wigner-Smith/Friedel theory gives mature delay/DOS/state-count structure, but pursuing another abstract filter theorem looked unlikely to add enough detector-specific physics.

**Direction:** return to narrow-gap field-driven collection.

---

## Fixed-thickness field-driven collection

For a carrier crossing thickness `L`, the rectangular Ramo-current convention gives

```math
B_{\rm tr}
=c_t v_d/L,
\qquad
c_t\simeq0.44295.
```

At low field `v_d=mu F`, with generic Kane BTBT `J=A F^2e^{-F_K/F}`, eliminating field gives

```math
J(B_{\rm tr})
=
A
\left(\frac{LB_{\rm tr}}{c_t\mu}\right)^2
\exp\left[-\frac{F_Kc_t\mu}{LB_{\rm tr}}\right].
```

At fixed thickness, more field-driven transit speed means more direct tunneling.

But shrinking `L` is a clean escape: it shortens transit and reduces the field needed for the same speed.

**Direction:** test the `L -> 0` quantum limit.

---

## Ballistic single-barrier small-`L` audit

For a rectangular barrier separating dark and useful carrier energies by `Delta E`, eliminating thickness and optimizing barrier placement gave

```math
\mathcal T_d
\gtrsim
\exp\left[-
\frac{2c_t\Delta E}
{\hbar B_{\rm tr}}
\right].
```

The effective mass cancels in the simple parabolic model.

Multi-barrier structures remain a real escape, and the associated quantum speed scale `Delta E/h` is typically tens of THz for MWIR/LWIR gaps.

**Verdict:** useful asymptotic ceiling, probably not the practical HgCdTe bottleneck.

---

## HgCdTe Kane scale audit

Using the simplified narrow-gap relation

```math
E_g=2m_Kv_K^2
```

with experimentally supported

```math
v_K\simeq1.07\times10^6\ {\rm m/s},
```

the characteristic direct-tunneling field becomes approximately

```math
F_K
\simeq
\frac{\pi E_g^2}{4q\hbar v_K}
\propto\lambda_c^{-2}.
```

The corresponding Kane length

```math
\ell_K=\hbar v_K/E_g
```

grows as

```math
\ell_K\propto\lambda_c.
```

Long wavelength therefore becomes less forgiving in both field and microscopic length scales.

The single-barrier quantum transit scale remained far above practical detector bandwidths, while BTBT field scales were technologically plausible.

**Direction:** normalize the actual HgCdTe BTBT law.

---

## Normalized HgCdTe direct-BTBT frontier

A published uniform-field HgCdTe BTBT expression was combined with `V=FL` and the simplified Kane-mass substitution

```math
m^*=E_g/(2v_K^2).
```

This gives

```math
J_{\rm BTBT}
=
\frac{q^3L}{4\pi^3\hbar^2v_K}
F^2e^{-F_K/F}.
```

Define

```math
x=F/F_K,
\qquad
j=J/J_K.
```

Then the full simplified family collapses to

```math
\boxed{j=x^2e^{-1/x}.}
```

with

```math
F_K
=\frac{\pi^3\hbar c^2}{qv_K\lambda_c^2},
```

```math
J_K
=\frac{q\pi^3c^4L}{4v_K^3\lambda_c^4}.
```

Thus

```math
F_K\propto\lambda_c^{-2},
\qquad
J_K\propto L\lambda_c^{-4}.
```

The exact inverse is

```math
F_{\max}^{\rm BTBT}
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
```

A standard-library regression script was added:

```text
numerics/hgcdte_btbt_normalized_sweep.py
```

The isolated direct-BTBT model gives multi-kV/cm field ceilings for representative low dark-current targets.

---

## High-field transport prevents the next shortcut

A primary Monte Carlo study of `Hg_0.8Cd_0.2Te` at 77 K reports non-ohmic/hot-electron and impact-ionization behavior already around `100 V/cm` and states that analytical velocity interpolation formulas were produced.

The currently accessible primary-source text does not expose the interpolation coefficients.

Therefore the project **refused** to extrapolate low-field mobility into the multi-kV/cm BTBT regime or invent an arbitrary saturation-velocity formula.

The physically correct next expression is

```math
\boxed{
B_{\rm tr,max}
=\frac{c_t}{L}
\,v_d(F_{\max}^{\rm BTBT}).
}
```

---

## Current direction

The project has finally earned a concrete HgCdTe transport question.

Next:

1. obtain a primary-source high-field `v_d(F)` interpolation or digitizable curve for a definite HgCdTe composition/density/temperature;
2. combine it with the normalized BTBT inversion;
3. determine whether BTBT actually reaches its target before hot-electron/impact-ionization physics becomes the controlling limit;
4. only then add TAT/SRH and compare to real detector response data.

If another mechanism intervenes first, that mechanism becomes the next branch.

**No manuscript yet. No novelty claim.**