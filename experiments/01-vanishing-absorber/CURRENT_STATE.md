# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; abstract universal routes repeatedly narrowed; active frontier is now HgCdTe high-field mechanism ordering; no novelty claim

## 1. Guiding question

The experiment began with

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The original geometric-volume route failed. After successive optical, quantum, control, and information-theoretic counterexamples, the research returned to a concrete semiconductor question:

> **For narrow-gap HgCdTe, which physical mechanism actually intervenes first when electric field is increased to make carrier collection faster?**

The current answer is narrower than a universal detector theorem but more directly useful for detector physics.

---

## 2. Canonical reading order

After root `AGENTS.md`, read:

1. `HGCDTE_FIELD_REGIME_MAP.md`
2. `HGCDTE_TRANSPORT_BTBT_PHASE_BOUNDARY.md`
3. `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
4. `HGCDTE_KANE_SCALE_AUDIT.md`
5. `FIELD_DRIVEN_COLLECTION_TUNNELING.md`
6. `BALLISTIC_BARRIER_SPEED_LEAKAGE.md`
7. `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md`
8. `RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md`
9. `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`
10. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
11. `RESEARCH_LOG.md`
12. older files only for provenance.

`CLAIM_LEDGER.md` is the epistemic boundary.

There is still **no manuscript**.

---

## 3. Current material result — normalized direct BTBT

Using a published uniform-field HgCdTe BTBT expression, a uniform region `V=FL`, and the simplified Kane-mass substitution

```math
m^*=E_g/(2v_K^2),
\qquad
v_K\simeq1.07\times10^6\ {\rm m/s},
```

the direct-BTBT law becomes

```math
\boxed{
J_{\rm BTBT}
=
\frac{q^3L}{4\pi^3\hbar^2v_K}
F^2e^{-F_K/F}.
}
```

With

```math
x=F/F_K,
\qquad
j=J/J_K,
```

```math
\boxed{j=x^2e^{-1/x},}
```

where

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

The exact field inversion for a direct-BTBT budget `J_*` is

```math
\boxed{
F_J
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
}
```

This is a scaling model, not a calibrated junction model.

---

## 4. New result — transport/BTBT phase boundary

A broad empirical high-field envelope used in HgCdTe APD transport modeling is

```math
v(F)
=\frac{\mu F}{1+(F/d)^r}.
```

For `r>1`, it has an exact velocity maximum at

```math
\boxed{
F_{\rm pk}
=d(r-1)^{-1/r}.
}
```

Because direct BTBT increases monotonically with field, the fastest field allowed by this transport envelope and a direct-BTBT budget is simply

```math
\boxed{
F_{\rm opt}
=\min(F_{\rm pk},F_J).
}
```

This is a generic model-level phase boundary. No `Hg_0.8Cd_0.2Te`, 77 K coefficients are invented for it.

---

## 5. Stronger target-composition conclusion — direct BTBT is not first for ordinary LWIR

Primary transport work on `Hg_0.8Cd_0.2Te` at 77 K establishes that

```text
~50 V/cm and below
-> approximately ohmic transport

~10^2 V/cm scale
-> hot-electron / non-ohmic / impact-ionization physics already matters

high field
-> steady-state electron drift approaches a scale of order 5e5 m/s,
   with submicron transient overshoot possible above that value.
```

Compare those fields with the simplified direct-BTBT model.

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

For any reference field `F_R`, the cutoff at which direct BTBT reaches a stated current-density budget `J_*` is exactly

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

For `L=1 um`, even an unusually strict direct-BTBT budget of `1e-12 A/cm2` gives approximately

```text
F_R = 100 V/cm  -> lambda_x = 74.4 um
F_R = 500 V/cm  -> lambda_x = 31.7 um
F_R = 1.0 kV/cm -> lambda_x = 22.0 um
F_R = 1.5 kV/cm -> lambda_x = 17.7 um.
```

At `500 V/cm`, the same model gives roughly

```text
10 um -> 8.8e-147 A/cm2
17 um -> 2.1e-49 A/cm2
24 um -> 9.8e-24 A/cm2.
```

Therefore the working hypothesis

> **direct BTBT is the first high-field mechanism that limits transit-speed improvement in ordinary 8–14 um HgCdTe at 77 K**

is **invalidated within the stated comparison**.

The material reaches nonlinear hot-carrier / impact-ionization physics much earlier.

This does **not** mean direct BTBT is unimportant in reverse-biased HgCdTe. It means it is not the first field physics encountered in this particular speed-pushing thought experiment for ordinary LWIR.

---

## 6. Transport-speed envelope

For the rectangular Ramo-current-pulse convention,

```math
\boxed{
B_{\rm tr}
=c_t\frac{v}{L},
\qquad
c_t\simeq0.44295.
}
```

Using the target-composition steady-state high-field velocity scale

```math
v_{\rm sat}\sim5\times10^5\ {\rm m/s},
```

gives the kinematic transit envelope

| `L` | `c_t v_sat/L` |
|---:|---:|
| 0.2 um | 1.11 THz |
| 0.5 um | 443 GHz |
| 1 um | 221 GHz |
| 2 um | 111 GHz |
| 5 um | 44.3 GHz |
| 10 um | 22.1 GHz |

These are **not complete detector bandwidth predictions**. Carrier lifetime, diffusion, trapping, contacts, RC loading, avalanche dynamics, and readout can all be slower.

The reported `~1.1e6 m/s` submicron overshoot is a transient nonlocal effect and is not a universal bulk saturation velocity.

---

## 7. General field-efficiency identity

For

```math
J_{\rm BTBT}\propto F^2e^{-F_K/F},
```

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln F}
=2+\frac{F_K}{F}.
}
```

Define local drift-velocity elasticity

```math
\boxed{
s_v(F)
=\frac{d\ln v}{d\ln F}.
}
```

Since `B_tr proportional to v`, wherever `s_v != 0`,

```math
\boxed{
\frac{d\ln J_{\rm BTBT}}
{d\ln B_{\rm tr}}
=
\frac{2+F_K/F}{s_v(F)}.
}
```

Interpretation:

```text
s_v ~ 1
-> field still buys speed efficiently

s_v -> 0+
-> marginal field becomes extremely inefficient for transit-speed improvement

s_v < 0
-> more field raises BTBT while reducing speed; the field range is dominated.
```

The absolute BTBT current may still be tiny when this marginal cost becomes large. This identity is therefore a field-selection diagnostic, not a claim that BTBT itself already dominates dark current.

---

## 8. Impact ionization must be a separate constraint

Do not bury impact ionization inside a fitted velocity curve.

If the local impact-ionization event rate is `Gamma_II(F)`, a carrier crossing length `L` at speed `v(F)` has mean event count

```math
\boxed{
\Xi_{\rm II}(F)
=\Gamma_{\rm II}(F)\frac{L}{v(F)}.
}
```

Under a Poisson-event model,

```math
\boxed{
P_{\rm II}
=1-e^{-\Xi_{\rm II}}.
}
```

Thus an allowed probability `p_*` requires

```math
\boxed{
\alpha_{\rm II}(F)L
\le
-\ln(1-p_*),
}
```

where

```math
\alpha_{\rm II}=\Gamma_{\rm II}/v.
```

The next quantitative material frontier is therefore a defensible `alpha_II(F)` or `Gamma_II(F)` relation for the target composition/temperature, followed by TAT and other leakage constraints.

---

## 9. Reproducibility

Current material regressions:

```text
numerics/hgcdte_btbt_normalized_sweep.py
numerics/hgcdte_field_regime_map.py
```

The new field-regime regression checks

- crossover wavelengths `lambda_x(F_R,J_*)`;
- direct-BTBT current at selected cutoffs/fields;
- the `v=5e5 m/s` transit envelope.

It is a scaling regression, not a device simulator.

---

## 10. Important stopped / superseded ideas

Do not restart without defeating the recorded counterexample or scope failure:

- universal active-volume-only detector bound;
- finite absorber count as the one-photon speed resource;
- finite internal storage rank as an always-on detector capacity;
- local Landauer erasure as a universal detector cost;
- single-Lorentzian `B^2/Delta` leakage as a universal electronic theorem;
- spectral FWHM as architecture-independent carrier speed;
- fixed-thickness `v=mu F` extrapolation as a universal speed-dark-current law;
- direct BTBT as the assumed first high-field speed limiter for ordinary LWIR HgCdTe;
- low-field mobility extrapolation into `kV/cm` fields.

The retained passive harmonic access theorem remains useful background but is not the active paper direction.

---

## 11. Explicit non-claims

We have **not** established

- a universal HgCdTe speed-dark-current limit;
- a complete diode dark-current model;
- a calibrated `Hg_0.8Cd_0.2Te`, 77 K impact-ionization field ceiling;
- a universal saturation field;
- that BTBT is negligible in all LWIR device geometries;
- that transient overshoot can be used as a steady-state detector velocity;
- a full device bandwidth including lifetime/RC/readout;
- novelty of the normalized BTBT or field-regime algebra;
- readiness for a manuscript.

---

## 12. Next decisive calculation

The next question is now explicit:

> **At a specified collection length and allowed multiplication/ionization probability, what field is permitted by impact ionization in `Hg_0.8Cd_0.2Te` at 77–80 K, and how does that field compare with the transit-velocity plateau, TAT onset, and direct-BTBT ceiling?**

Do not invent an impact-ionization coefficient.

Use a primary-source Monte Carlo/experiment relation if recoverable. If only energy-dependent ionization rates are available, propagate the carrier-energy history rather than replacing it with an arbitrary field-only fit.

After the diode-like high-field problem is closed, compare it with HgCdTe **photoconductors**, where lifetime and photoconductive gain may dominate the speed physics rather than transit time.
