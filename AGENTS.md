# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; abstract universal-resource branches have been stress-tested and narrowed; active frontier is normalized HgCdTe high-field transport/BTBT; no novelty claim**

Read this file first.

The project starts from thought experiments and follows the physics. Counterexamples are progress. Do not force the work back toward the original active-volume idea or prematurely toward a manuscript.

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when relevant;
3. fetch the exact current blob SHA immediately before replacing a file;
4. never overwrite a stale SHA;
5. preserve concurrent work, corrections, and failed branches.

**Live `main` overrides every snapshot.**

---

## 2. Mandatory epistemic labels

Use explicitly:

- **known result**;
- **derived result**;
- **checked result**;
- **candidate distinct lemma — priority unproven**;
- **conjecture**;
- **model assumption**;
- **invalidated result**;
- **superseded result**;
- **open question**.

Never turn a negative literature search into a novelty claim.

Do not use `new`, `first`, `fundamental`, `universal`, etc. without a focused primary-source audit and immediate `CLAIM_LEDGER.md` update.

---

## 3. Research path — what happened

```text
weak passive resonance
-> dwell-time / loss-rate bandwidth penalty

active volume
-> killed by ideal field concentration

finite absorber number
-> killed as a one-photon speed resource

finite transition / LDOS / emitter extent
-> conditional weak-coupling bounds
-> perturbative theory eventually fails

nonperturbative Hopfield
-> dressed optical/detector access can collapse

multimode passive network
-> exact harmonic integrated-transfer access law

active/time-dependent capture
-> pump/control resources identified
-> known-time temporal matching works

unknown arrival / adaptive control
-> finite storage-rank law generalized to storage x branch rank
-> output continuum exports the missing information
-> no universal finite internal space-time capacity survives unrestricted output

semiconductor Fermi contact
-> useful extraction and reverse thermal loading linked by detailed balance

finite-linewidth energy filter
-> fast resonant extraction creates zero-T spectral-tail leakage

multipole filter
-> tail can be made steeper
-> spectral FWHM is not architecture-independent speed
-> extra filter poles carry delay/state resources

field-driven narrow-gap diode
-> fixed-thickness speed vs BTBT tradeoff
-> thinning is a counterexample

small-L quantum barrier
-> one-barrier speed/leakage exponent
-> asymptotic quantum scale too high to be the practical HgCdTe bottleneck

HgCdTe Kane scaling
-> F_K ~ lambda_c^-2
-> ell_K ~ lambda_c

CURRENT FRONTIER
-> normalized HgCdTe direct-BTBT curve
-> real high-field v_d(F) needed before converting BTBT field ceiling into transit speed.
```

---

## 4. Canonical current files

Read after this file:

1. `README.md`
2. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
3. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
4. `experiments/01-vanishing-absorber/HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_KANE_SCALE_AUDIT.md`
6. `experiments/01-vanishing-absorber/FIELD_DRIVEN_COLLECTION_TUNNELING.md`
7. `experiments/01-vanishing-absorber/BALLISTIC_BARRIER_SPEED_LEAKAGE.md`
8. `experiments/01-vanishing-absorber/MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md`
9. `experiments/01-vanishing-absorber/RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md`
10. `experiments/01-vanishing-absorber/FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`
11. `experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
12. `experiments/01-vanishing-absorber/ADAPTIVE_FEEDFORWARD_MODE_CAPACITY.md`
13. `experiments/01-vanishing-absorber/OUTPUT_RECORD_INFORMATION_CAPACITY.md`
14. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
15. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`
16. older files only when auditing provenance.

There is still **no manuscript**.

---

## 5. Strongest retained passive finite-network theorem

For a finite stable passive strictly proper network,

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

In the controllability-Gramian eigenbasis,

```math
\boxed{
\frac{\mathcal I}{2}
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

For band width `W`,

```math
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
```

This is an external-access resource law, not an absolute bandwidth theorem.

The proof uses standard `H2`/Lyapunov/passivity machinery. Novelty is not claimed.

Keep this result as useful structure, but do not redirect the active research back toward proving a universal optical theorem unless new semiconductor work exposes a specific need.

---

## 6. Why the abstract space-time branch was stopped

### Fixed protocol

For `M` orthogonal possible inputs and retained detector rank `r`,

```math
\sum_j\eta_j\le r.
```

### Adaptive instrument

For `d` successful adaptive branches,

```math
\boxed{
\sum_j\eta_j\le rd.
}
```

### Output continuum escape

A normal detector can export branch/arrival-time information into a large output record space. One output quantum across `D` orthogonal time bins can carry `ln D` nats at fixed event energy.

Therefore neither finite storage rank nor local Landauer work is a universal always-on detector capacity without also constraining the output continuum.

**Decision:** do not keep stacking abstract resource variables unless a concrete detector problem demands them.

---

## 7. Semiconductor Fermi-contact baseline

Read `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`.

For one state weakly coupled to a Fermi contact,

```math
\frac{k_{\rm in}}
{k_{\rm out}}
=
\zeta e^{-(E-\mu)/(k_BT)}.
```

If useful extraction competes with recombination,

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
=
2\pi\zeta\eta_{\rm col}B_{\rm evt}
 e^{-(E-\mu)/(k_BT)}.
}
```

Do not call `k_in` dark current/count without an explicit transport/readout cycle.

---

## 8. Energy-filter lesson

### One Breit-Wigner resonance

At zero temperature, an occupied source below a finite-linewidth resonant level leaks through its Lorentzian tail:

```math
R_{\rm leak}
=
\frac{\Gamma_E}{2h}
\left[
\frac\pi2
-\arctan(2\Delta/\Gamma_E)
\right].
```

For `B_evt=Gamma_E/h` and a sharp filter,

```math
R_{\rm leak}\simeq hB_{\rm evt}^2/(4\Delta).
```

### Multipole counterexample

Higher-order filters can suppress the tail much more strongly at the same FWHM.

For the chosen Butterworth-type family,

```math
R_N
\simeq
\frac{\Gamma_E}{2h(2N-1)}
\left(
\frac{\Gamma_E}{2\Delta}
\right)^{2N-1}.
```

But center group delay grows approximately as

```math
\tau_g(0)
\sim
4N\hbar/(\pi\Gamma_E).
```

**Rule:** do not use spectral FWHM as an architecture-independent detector-speed metric when multiple transport poles are present.

Further Wigner-Smith/Friedel abstraction was stopped because it mainly reproduces mature scattering/filter theory without yet supplying enough detector-specific content.

---

## 9. Fixed-thickness field-driven HgCdTe logic

Read `FIELD_DRIVEN_COLLECTION_TUNNELING.md`.

For one constant-velocity carrier transit,

```math
\boxed{
B_{\rm tr}
=c_t\frac{v_d}{L},
\qquad
c_t\simeq0.44295.
}
```

At low field `v_d=mu F`, with generic Kane-type direct tunneling

```math
J=A F^2e^{-F_K/F},
```

```math
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
```

At fixed `L`, higher field-driven speed increases BTBT.

But shrinking `L` is a valid escape, so this is not universal.

---

## 10. Small-length quantum audit

Read `BALLISTIC_BARRIER_SPEED_LEAKAGE.md`.

For one optimized rectangular barrier separating useful and dark energies by `Delta E`, the parabolic one-barrier model gives

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

The mass cancels in that idealized optimization.

But multi-barrier filters are a real escape and the corresponding `Delta E/h` speed scale is typically tens of THz for MWIR/LWIR HgCdTe.

Treat this as an asymptotic quantum warning, not the practical HgCdTe frontier.

---

## 11. HgCdTe Kane scales

Read `HGCDTE_KANE_SCALE_AUDIT.md`.

Using the simplified relation

```math
E_g=2m_Kv_K^2,
```

with

```math
v_K\simeq1.07\times10^6\ {\rm m/s},
```

and identifying tunneling mass with `m_K` only for scaling,

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
F_K\propto\lambda_c^{-2}.
```

The Kane length is

```math
\boxed{
\ell_K
=\frac{\hbar v_K}{E_g}
=\frac{v_K}{2\pi c}\lambda_c
}
```

so

```math
\ell_K\propto\lambda_c.
```

Do not identify `v_K` with drift saturation velocity.

---

## 12. Current strongest material normalization

Read `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`.

Published uniform-field HgCdTe BTBT form:

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

For `V=FL` and the simplified Kane-mass substitution

```math
m^*=E_g/(2v_K^2),
```

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

Therefore

```math
F_K\propto\lambda_c^{-2},
\qquad
J_K\propto L\lambda_c^{-4},
```

while the normalized curve is unchanged.

Exact inversion:

```math
\boxed{
F_{\max}^{\rm BTBT}
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
}
```

Regression:

```text
experiments/01-vanishing-absorber/numerics/hgcdte_btbt_normalized_sweep.py
```

---

## 13. Critical rule: do not invent high-field velocity

A primary Monte Carlo study of `Hg_0.8Cd_0.2Te` at 77 K reports non-ohmic/hot-electron and impact-ionization behavior around `100 V/cm`.

The direct-BTBT-only field ceiling can lie in the `kV/cm` range.

Therefore **do not** use

```math
v_d=\mu F
```

at the BTBT ceiling merely to produce a speed curve.

The correct next relation is

```math
\boxed{
B_{\rm tr,max}
=\frac{c_t}{L}
\,v_d(F_{\max}^{\rm BTBT}).
}
```

`v_d(F)` must be traceable to a primary-source composition/temperature/density-specific model or data set.

The paper by Palermo et al., *Solid-State Electronics* **53**, 70-78 (2009), DOI `10.1016/j.sse.2008.10.003`, states that analytical interpolation formulas exist, but currently accessible primary-source text does not expose their coefficients.

Do not reconstruct coefficients from secondary reproductions without clearly labeling the source/uncertainty.

---

## 14. Numerical/reproducibility state

Active checks include

- `numerics/one_port_time_domain_check.py`;
- `numerics/passive_multimode_h2_stress.py`;
- `numerics/adaptive_instrument_rank_stress.py`;
- `numerics/hgcdte_btbt_normalized_sweep.py`.

Keep scripts small and deterministic. Do not add CI for appearance.

---

## 15. Invalidated routes — do not restart casually

- active-volume-only theorem;
- finite absorber count as missing one-photon speed limit;
- largest internal coupling as universal multimode parameter;
- all-frequency harmonic theorem with ideal feedthrough;
- generic capture+amplification novelty;
- generic autonomous detector thermodynamics novelty;
- universal active `pump ~ W^2` law;
- finite internal storage rank as always-on detector capacity;
- local Landauer erasure as universal adaptive detector cost;
- single-Lorentzian `B^2/Delta` leakage as universal electronic theorem;
- spectral FWHM as universal carrier speed;
- fixed-thickness field-speed relation as universal when `L` may vary;
- low-field mobility extrapolation to `kV/cm` HgCdTe fields.

---

## 16. Current next step

Do **not** return to abstract resource laws or start a manuscript.

The next calculation is narrowly material-specific:

> **Obtain a traceable high-field electron `v_d(F)` law for a definite HgCdTe composition and temperature, then combine it with the normalized BTBT inversion to calculate a direct-BTBT-limited transit-bandwidth frontier.**

Required sequence:

1. obtain primary `v_d(F)` interpolation coefficients or digitizable curve;
2. state composition, carrier density, temperature, and scattering assumptions;
3. compute `F_max(J_*,lambda_c,L)` from `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`;
4. evaluate

```math
B_{\rm tr,max}=c_t v_d(F_{\max})/L;
```

5. compare `F_max` against the onset of hot-electron transport and impact ionization;
6. if impact ionization or TAT intervenes before direct BTBT, follow that mechanism instead;
7. only after a clean pure-BTBT frontier exists, add TAT/SRH and compare to measured HgCdTe photodiode/APD response data;
8. perform focused prior-art comparison before any novelty positioning.

The project has now earned material-specific HgCdTe transport. It has **not** earned a paper yet.