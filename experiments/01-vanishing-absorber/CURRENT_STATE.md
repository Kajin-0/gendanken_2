# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is an entrance-gap spectral **initial-condition crossover** in compositionally graded HgCdTe; the earlier universal timing-maximum interpretation has been narrowed; no novelty claim

## 1. Current question

The project began by asking whether an ideal detector could be made arbitrarily small, fast, sensitive, and perfectly absorbing.

The active-volume route failed. The research then moved through optical access, microscopic coupling, active control, semiconductor transport, tunneling, HgCdTe band engineering, and finally wavelength-resolved carrier timing.

The strongest current detector-specific question is now:

> **Does a monotonic compositionally graded HgCdTe absorber produce a measurable timing crossover at the wavelength corresponding to its entrance band gap because photon energy changes the carrier problem through different physical variables on the two sides of that energy?**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md`
2. `HGCDTE_SPECTRAL_DRIFT_DIFFUSION_ROBUSTNESS.md`
3. `HGCDTE_SPECTRAL_MOMENTUM_SCATTERING_SURROGATE.md`
4. `HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`
5. `HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`
6. `HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md`
7. `HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`
8. `HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md`
9. `HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md`
10. `CLAIM_LEDGER.md`
11. `RESEARCH_LOG.md`
12. `ARCHIVE_STATUS.md`

`HGCDTE_SPECTRAL_DELAY_PEAK.md` is retained as a **ballistic special case / provenance file**, not as the transport-independent headline.

---

## 3. Material geometry retained from the graded-HgCdTe branch

Use the quasi-neutral p-type baseline

```math
E_v\approx\text{constant},
```

```math
E_g(x)=E_{g,\rm in}-Gx,
\qquad G>0,
```

so approximately

```math
E_c(x)\approx E_v+E_g(x),
```

```math
\boxed{S_c=-dE_c/dx\approx G.}
```

This band-structure slope can drive minority electrons while suppressing the ordinary same-direction direct-Zener geometry in the ideal graded-Kane model.

TAT, interfaces, carrier heating, impact ionization and contact/boundary physics remain separate constraints.

---

## 4. Robust spectral generation geometry

For

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

the first location where ordinary above-gap absorption is energetically allowed satisfies

```math
E_g(x_g)=E_\gamma.
```

Therefore

```math
\boxed{
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

For

```math
E_\gamma\ge E_{g,\rm in},
```

the physical entrance is already optically allowed and

```math
\boxed{x_g=0.}
```

The high-optical-depth earliest-generation rule is therefore

```math
\boxed{
x_g(E_\gamma)
=\max\!\left[
0,
\frac{E_{g,\rm in}-E_\gamma}{G}
\right].
}
```

This geometry is independent of the subsequent carrier transport model.

---

## 5. Exact entrance-gap initial-condition switch

Define local photon excess at the earliest allowed generation position:

```math
\boxed{
\nu_g(E_\gamma)
=\max(0,E_\gamma-E_{g,\rm in}).
}
```

Then, away from the switching point,

```math
\boxed{
\frac{dx_g}{dE_\gamma}
=
\begin{cases}
-1/G,&E_\gamma<E_{g,\rm in},\\
0,&E_\gamma>E_{g,\rm in},
\end{cases}
}
```

while

```math
\boxed{
\frac{d\nu_g}{dE_\gamma}
=
\begin{cases}
0,&E_\gamma<E_{g,\rm in},\\
1,&E_\gamma>E_{g,\rm in}.
\end{cases}
}
```

Thus at

```math
\boxed{E_\gamma=E_{g,\rm in}}
```

photon energy stops primarily moving the **generation position** and begins primarily changing the **photoelectron initial state**.

This is now the strongest transport-independent result in the spectral branch.

---

## 6. General timing-functional consequence

Let an intrinsic timing observable be

```math
\mathcal T=\mathcal F(x_g,\varepsilon_g,\mathcal P),
```

where

```math
\varepsilon_g=\xi_e\nu_g
```

and `mathcal P` represents the transport/device state.

In the sharp earliest-generation limit,

```math
\boxed{
\frac{d\mathcal T}{dE_\gamma}
=-\frac1G\frac{\partial\mathcal F}{\partial x_g},
\qquad E_\gamma<E_{g,\rm in},
}
```

whereas

```math
\boxed{
\frac{d\mathcal T}{dE_\gamma}
=\xi_e\frac{\partial\mathcal F}{\partial\varepsilon_g},
\qquad E_\gamma>E_{g,\rm in}.
}
```

Therefore the **spectral sensitivity channel changes** at the entrance gap.

A visible cusp or slope change is not mathematically guaranteed because the two sensitivities can accidentally match and finite optical depth smooths the switch.

The safe prediction is a crossover tied to the independently known `E_g,in`, not a mandatory curve shape.

---

## 7. Drift-diffusion robustness result

In the strong momentum-randomizing limit use

```math
dX=v_d\,dt+\sqrt{2D}\,dW_t.
```

For remaining distance `d`, the first-passage statistics are exactly

```math
\boxed{\langle T|d\rangle=d/v_d,}
```

```math
\boxed{\operatorname{Var}(T|d)=2Dd/v_d^3.}
```

For random generation position,

```math
\boxed{\langle T\rangle=\langle d\rangle/v_d,}
```

```math
\boxed{
\operatorname{Var}(T)
=\frac{2D\langle d\rangle}{v_d^3}
+\frac{\operatorname{Var}(d)}{v_d^2}.
}
```

The first term is transport/diffusion timing spread; the second is optical generation-position spread.

In the high-optical-depth constant-coefficient limit,

```math
\langle T\rangle
=\begin{cases}
(E_\gamma-E_{g,\rm out})/(Gv_d),
& E_\gamma<E_{g,\rm in},\\
L/v_d,
& E_\gamma\ge E_{g,\rm in}.
\end{cases}
```

Thus strong scattering gives **rise -> plateau**, not the earlier ballistic decline.

---

## 8. Finite momentum-memory stress test

A dimensionless underdamped Ornstein-Uhlenbeck surrogate was added:

```math
dv
=\frac{v_d-v}{\tau_m}dt
+\sqrt{2\sigma_v^2/\tau_m}\,dW_t,
```

```math
dx=v\,dt.
```

Three initial longitudinal momentum models were compared.

### Negligible directed initial velocity

Post-entrance-gap delay is approximately flat.

### Persistent positive directed hot-carrier velocity

Post-entrance-gap delay decreases, reproducing the ballistic-like maximum.

### Symmetric hot initial longitudinal distribution

The short-wave delay need not decrease; timing variance can increase strongly.

Therefore neither

```text
peak
```

nor

```text
plateau
```

is universal.

The post-crossover shape diagnoses momentum memory and energy-dependent transport.

---

## 9. Ballistic timing maximum is now model-specific

The earlier high-optical-depth forward-ballistic calculation predicted

```text
rise through graded gap
-> maximum at Eg,in
-> decline at higher photon energy.
```

That remains a valid result **inside that ballistic directed-velocity model**.

It is no longer the canonical transport-independent prediction.

The ballistic peak should now be interpreted as one possible realization of the entrance-gap switch when additional photon excess produces persistent forward carrier velocity.

---

## 10. Photoexcitation energy correction retained

Do not treat downstream-generated photoelectrons as cold.

Write

```math
\boxed{\varepsilon_{\rm gen}=\xi_e(E_\gamma-E_g).}
```

The symmetric two-band model gives `xi_e=1/2`.

The simplified HgCdTe flat-heavy-hole Kane limit motivates `xi_e approximately 1` as a relevant limiting baseline for heavy-hole-to-electron absorption.

`xi_e` is not a universal constant and a real multiband optical-transition calculation remains open.

---

## 11. Prior-art posture

Primary literature already establishes

- graded HgCdTe spectral response;
- grading-induced carrier drift and faster response;
- microscopic scattering / hot-electron transport in `Hg_0.8Cd_0.2Te` at 77 K;
- hydrodynamic models validated against HgCdTe Monte Carlo transport;
- tunable-pulse HgCdTe timing instrumentation.

The focused search has not found an inspected primary source explicitly organizing wavelength-resolved graded-HgCdTe timing around the transition

```text
photon energy changes generation position
->
photon energy changes injected carrier state
```

at the entrance-gap energy.

**Status:** CANDIDATE UNDEREXPLORED DETECTOR-FACING ORGANIZING PRINCIPLE — PRIORITY UNPROVEN.

Negative search is not novelty evidence.

---

## 12. Revised decisive experiment

Do not require a strict timing maximum.

Sweep pulsed wavelength through

```text
near output cutoff
-> graded-gap interval
-> entrance-gap wavelength
-> shorter wavelengths
```

under fixed bias, temperature, spot and readout.

Use differential low-frequency group delay or normalized impulse centroid to suppress common wavelength-independent electronics.

Look for a reproducible spectral crossover near

```math
\boxed{\lambda_{g,\rm in}\simeq hc/E_{g,\rm in}.}
```

Then use the post-crossover slope/variance as a transport diagnostic:

```text
negative slope
-> persistent directed hot-carrier memory / faster energy-dependent transport

near-zero slope
-> strong momentum randomization / drift-like saturation

positive slope or strong broadening
-> hot momentum spread, energy-dependent scattering, or another transport mechanism.
```

No effect would falsify or strongly narrow the simplified graded-generation picture.

---

## 13. Current numerical regressions

Relevant scripts now include

```text
numerics/hgcdte_spectral_momentum_scattering_surrogate.py
numerics/hgcdte_spectral_delay_relaxation.py
numerics/hgcdte_spectral_delay_peak.py
numerics/hgcdte_spectral_transit_statistics.py
numerics/hgcdte_dimensionless_device_phase_map.py
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
```

The ballistic peak regression remains as provenance; it no longer defines the universal claim boundary.

---

## 14. Next decisive work

Do not add another abstract theorem and do not defend the old peak by assumption.

The next high-value step is one of:

1. implement a calibrated 77 K `Hg_0.8Cd_0.2Te` hydrodynamic/Monte-Carlo transport closure using published velocity, momentum-relaxation and energy-relaxation physics;
2. obtain wavelength-resolved impulse/group-delay data on one known graded HgCdTe profile.

The immediate modeling target is the **spectral crossover shape**, not a predetermined maximum.

Only after a calibrated transport model or direct data collision should manuscript readiness be reassessed.
