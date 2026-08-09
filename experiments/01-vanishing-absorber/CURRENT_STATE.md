# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is finite-length HgCdTe high-field transport and nonlocal impact ionization; no novelty claim

## 1. Current question

The project began by asking whether an ideal photodetector could be made arbitrarily small, fast, sensitive, and perfectly absorbing.

Successive counterexamples killed simple universal answers based on active volume, absorber count, finite storage rank, spectral FWHM, or one fixed optical architecture.

The active question is now concrete:

> **For narrow-gap HgCdTe, what carrier-transit speed is physically useful once high-field velocity, finite impact-ionization dead space, direct BTBT, and later TAT are all treated on their proper length/energy scales?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
2. `HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md`
3. `HGCDTE_FIELD_REGIME_MAP.md`
4. `HGCDTE_TRANSPORT_BTBT_PHASE_BOUNDARY.md`
5. `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
6. `HGCDTE_KANE_SCALE_AUDIT.md`
7. `FIELD_DRIVEN_COLLECTION_TUNNELING.md`
8. `CLAIM_LEDGER.md`
9. `RESEARCH_LOG.md`
10. older derivations only for provenance.

---

## 3. Direct BTBT remains normalized cleanly

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

This is a scaling result, not a calibrated total-dark-current model.

---

## 4. Bulk high-field onset is not a finite-device II ceiling

Primary Monte Carlo work on bulk `Hg_0.8Cd_0.2Te` at 77 K shows hot-electron / non-ohmic / impact-ionization physics becoming relevant at fields of order `10^2 V/cm`.

That statement must **not** be converted directly into

```text
finite 1 um detector ionizes at 100 V/cm.
```

A finite injected electron must acquire the impact-ionization threshold energy over its available trajectory.

HgCdTe APD literature therefore treats impact ionization as history dependent and includes dead-space effects.

---

## 5. Cold-injection dead-space scale

Let

```math
E_{\rm th}=\chi E_g.
```

For a cold electron crossing a uniform field over distance `L`, the field-work estimate is

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
=\frac{\hbar v_K}{E_g}
```

and the BTBT scale above,

```math
\boxed{
\frac{F_{\rm dead}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L}.
}
```

This is the key dimensionless connection.

For `L >> ell_K`, the cold-carrier ionization energy scale becomes accessible at fields far below the direct-BTBT characteristic field.

For `chi=1`, `L=1 um`:

| cutoff | `F_dead` |
|---:|---:|
| 8 um | 1.55 kV/cm |
| 10 um | 1.24 kV/cm |
| 12 um | 1.03 kV/cm |
| 17 um | 729 V/cm |
| 24 um | 517 V/cm |

These are field-work thresholds, **not** calibrated ionization-probability thresholds.

---

## 6. Direct BTBT is still exponentially small near that scale

At the dead-space field,

```math
x_{\rm dead}
=\frac{4\chi\ell_K}{\pi L},
```

so

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

For micron-scale MWIR/LWIR regions, `L/ell_K` is large and this direct-BTBT term is exponentially suppressed.

Example, `L=1 um`, `chi=1`:

```text
10 um -> J_BTBT(F_dead) ~ 3.8e-57 A/cm2
17 um -> ~ 7.1e-33 A/cm2
24 um -> ~ 7.1e-23 A/cm2
```

These numbers are outputs of the isolated simplified BTBT model only.

---

## 7. Nonlocal mean-energy surrogate

The minimal finite-length model now uses

```math
\boxed{
\frac{d\varepsilon}{dt}
=qFv-\frac{\varepsilon}{\tau_E}.
}
```

Define

```math
\ell_E=v\tau_E.
```

For cold injection,

```math
\boxed{
\varepsilon(L)
=qF\ell_E
(1-e^{-L/\ell_E}).
}
```

This motivates the effective acceleration length

```math
\boxed{
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}).
}
```

Therefore the **mean-energy** threshold field is

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=\frac{\Delta E_{\rm th}}
{qL_{\rm eff}}.
}
```

For cold injection and `E_th=chi E_g`,

```math
\boxed{
\frac{F_{\rm th}^{(\rm mean)}}{F_K}
=
\frac{4\chi}{\pi}
\frac{\ell_K}{L_{\rm eff}}.
}
```

Limits:

```text
L << ell_E
-> L_eff -> L
-> finite dead-space result

L >> ell_E
-> L_eff -> ell_E
-> bulk-like energy-relaxation ceiling.
```

This is a surrogate for the mean trajectory, not a replacement for the stochastic hot-electron distribution.

---

## 8. First closed nonlocal ionization probability surrogate

Current HgCdTe APD modeling uses an energy-dependent rate of the form

```math
\Gamma_{\rm II}(E)
=A
\frac{(E/E_{\rm th}-1)^\alpha}
{(E/E_{\rm th})^\beta},
\qquad E\ge E_{\rm th}.
```

For the analytic test case

```math
\alpha=1,
\qquad
\beta=0,
```

define

```math
E_{\rm ss}=qF\ell_E,
\qquad
T=L/v.
```

If `E_ss > E_th`, the threshold time is

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

For `T > t_d`, the integrated hazard is

```math
\boxed{
\Xi_{\rm II}
=
\frac{A}{E_{\rm th}}
\left\{
(E_{\rm ss}-E_{\rm th})(T-t_d)
+E_{\rm ss}\tau_E
[e^{-T/\tau_E}-e^{-t_d/\tau_E}]
\right\}.
}
```

and

```math
\boxed{
P_{\rm II}=1-e^{-\Xi_{\rm II}}.
}
```

A deterministic numerical regression independently integrates the trajectory and reproduces this closed form.

---

## 9. Dimensionless nonlocal variables

Define

```math
\theta
=\frac{qF\ell_E}{E_{\rm th}},
\qquad
\ell=\frac{L}{\ell_E},
\qquad
a=A\tau_E.
```

The mean trajectory reaches threshold inside the device iff

```math
\boxed{
\theta(1-e^{-\ell})>1.
}
```

For the `alpha=1, beta=0` surrogate,

```math
\boxed{
P_{\rm II}
=1-e^{-aH(\theta,\ell)}
}
```

with `H` given exactly in `numerics/hgcdte_nonlocal_ii_surrogate.py` and the derivation file.

Thus the minimal nonlocal problem collapses to three dimensionless resources:

```text
field-work / threshold energy
length / energy-relaxation length
ionization time scale / energy-relaxation time scale.
```

---

## 10. Correct current mechanism ordering

The project should now state the hierarchy carefully:

```text
low field
-> ohmic transport

~10^2 V/cm in bulk x=0.20 at 77 K
-> hot-electron distribution and II rate become non-negligible

finite detector
-> actual II probability depends on L, energy relaxation and carrier history

L >> ell_K
-> II threshold can become accessible while simplified direct BTBT is still exponentially small

higher field / longer wavelength / shorter microscopic scale
-> direct BTBT eventually becomes important
```

Therefore the earlier working hypothesis that **direct BTBT is automatically the first high-field speed limiter in ordinary LWIR HgCdTe** is stopped.

The replacement statement is not “impact ionization starts at 100 V/cm in every device.”

It is:

> **The high-field problem is nonlocal and multi-mechanism; finite impact-ionization probability must be computed from carrier energy history before it can be compared quantitatively with BTBT or TAT.**

---

## 11. Transit-speed scale retained

For a constant-velocity Ramo pulse,

```math
\boxed{
B_{\rm tr}
=c_t\frac{v}{L},
\qquad
c_t\simeq0.44295.
}
```

The target-composition steady-state high-field velocity scale of order

```math
v\sim5\times10^5\ {\rm m/s}
```

gives approximately

```text
L=1 um -> 221 GHz transit envelope
L=5 um -> 44.3 GHz
L=10 um -> 22.1 GHz.
```

These are kinematic envelopes, not full detector bandwidths.

---

## 12. Reproducibility

Active material regressions:

```text
numerics/hgcdte_btbt_normalized_sweep.py
numerics/hgcdte_field_regime_map.py
numerics/hgcdte_impact_dead_space.py
numerics/hgcdte_nonlocal_ii_surrogate.py
```

No CI is needed yet.

---

## 13. External-data boundary

Palermo et al. explicitly calculate for `Hg_0.8Cd_0.2Te` at 77 K

- impact-ionization rate;
- velocity relaxation rate;
- energy relaxation rate;
- drift velocity and mean energy;
- analytical interpolation formulas for calculated quantities.

The accessible primary-source version does not expose the needed interpolation coefficients.

Do **not** reconstruct them from narrative text or secondary plots and silently treat them as primary data.

The required calibration inputs are now precisely identified:

```text
tau_E(F) or ell_E(F)
+
Gamma_II(E) / its calibrated parameters.
```

---

## 14. Next step

If the target `x=0.20`, 77 K interpolation coefficients remain inaccessible, do not stall the project.

Use the dimensionless nonlocal surrogate to determine **which ranges of `ell_E` and `A tau_E` would materially change the detector conclusion**.

Then either

1. identify a measurement / primary dataset capable of fixing those ranges; or
2. if the result is insensitive over all plausible ranges, promote the robust conclusion.

After the diode-like high-field problem is resolved, compare with HgCdTe photoconductors, where lifetime and photoconductive gain may dominate the speed physics instead of transit time.
