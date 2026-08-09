# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is an entrance-gap spectral initial-condition crossover in compositionally graded HgCdTe; the earlier universal timing-maximum interpretation is superseded; no novelty claim**

Read this file first.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, corrections, counterexamples, and prior-art collisions are part of the result.

**There is still no manuscript.**

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches;
6. make narrow edits where practical.

**Live `main` overrides snapshots and recovery notes.**

---

## 2. Epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and `CLAIM_LEDGER.md` update.

---

## 3. Current research path

```text
active-volume thought experiment
-> universal volume bound killed by field concentration

microscopic absorber / LDOS / ultrastrong coupling
-> successive loopholes

finite passive network
-> harmonic two-access transfer-area theorem

active/adaptive control
-> pump, timing, storage, output-record resources
-> unrestricted output continuum kills universal detector-only capacity

semiconductor contacts / energy filters
-> detailed balance, lifetime broadening, multipole delay

HgCdTe field-driven collection
-> normalized BTBT
-> low-field mobility shortcut killed

TAT / nonlocal II
-> defect spectrum + carrier energy history matter

homogeneous field shaping
-> no local speed/leakage benefit under stated homogeneous model

heterostructure / gap grading
-> direct-Zener geometry can be suppressed at fixed conduction drive

quasi-neutral p-type grading
-> majority-hole band nearly pinned
-> gap slope becomes minority-electron drive

collection boundary
-> unavoidable compensation voltage
-> local TAT/BTBT voltage capacity
-> minimum-compensation relaxation region

wavelength-resolved absorption
-> photon wavelength sets first allowed generation position
-> exact optical-depth generation distribution

photoexcitation correction
-> downstream photoelectrons are not cold
-> initial carrier momentum/energy matters

ballistic spectral timing
-> predicted entrance-gap timing maximum

momentum-scattering attack
-> maximum is not universal
-> drift-diffusion gives plateau
-> finite momentum memory allows multiple short-wave shapes

CURRENT FRONTIER
-> entrance-gap initial-condition switch
-> below Eg,in: wavelength moves generation position
-> above Eg,in: generation is pinned and wavelength changes injected carrier state
-> proposed tunable-wavelength timing crossover experiment.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md`
6. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_DRIFT_DIFFUSION_ROBUSTNESS.md`
7. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_MOMENTUM_SCATTERING_SURROGATE.md`
8. `experiments/01-vanishing-absorber/HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`
9. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`
10. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md`
11. `experiments/01-vanishing-absorber/HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`
12. `experiments/01-vanishing-absorber/HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md`
13. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md`
14. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
15. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

`HGCDTE_SPECTRAL_DELAY_PEAK.md` and its ballistic regressions are retained as provenance / a special transport limit, not as the canonical claim.

---

## 5. Active graded geometry

Use the quasi-neutral p-type baseline

```math
E_v\approx\text{constant},
```

```math
E_g(x)=E_{g,\rm in}-Gx,
```

```math
E_c(x)\approx E_v+E_g(x).
```

Thus

```math
\boxed{S_c=-dE_c/dx\approx G.}
```

This band-structure drive suppresses the ordinary same-direction direct-Zener geometry in the ideal graded-Kane model but does not remove TAT, interfaces, hot-electron physics, or impact ionization.

---

## 6. Robust spectral geometry

In the sharp high-optical-depth earliest-generation limit,

```math
\boxed{
x_g(E_\gamma)
=\max\!\left[
0,
\frac{E_{g,\rm in}-E_\gamma}{G}
\right].
}
```

Define local photon excess at that earliest point:

```math
\boxed{
\nu_g(E_\gamma)
=\max(0,E_\gamma-E_{g,\rm in}).
}
```

Therefore the role of photon energy switches at

```math
\boxed{E_\gamma=E_{g,\rm in}.}
```

Below it, changing photon energy moves the generation point.

Above it, the generation point is pinned and changing photon energy changes the injected carrier state.

This is the current strongest transport-independent spectral result.

---

## 7. General timing sensitivity

Let

```math
\mathcal T=\mathcal F(x_g,\varepsilon_g,\ldots),
```

with

```math
\varepsilon_g=\xi_e\nu_g.
```

Then in the sharp limit

```math
\boxed{
\frac{d\mathcal T}{dE_\gamma}
=-\frac1G\mathcal F_x,
\qquad E_\gamma<E_{g,\rm in},
}
```

while

```math
\boxed{
\frac{d\mathcal T}{dE_\gamma}
=\xi_e\mathcal F_\varepsilon,
\qquad E_\gamma>E_{g,\rm in}.
}
```

Do **not** claim a visible cusp is guaranteed. Finite optical depth smooths the transition and the two sensitivities can accidentally match.

---

## 8. Drift-diffusion limit

For

```math
dX=v_d dt+\sqrt{2D}\,dW_t,
```

and remaining distance `d`,

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

Thus generation-position jitter and transport/diffusion jitter are distinct.

At high optical depth with wavelength-independent transport coefficients, the spectral delay rises through the graded-gap interval and then approaches a plateau once `E_gamma >= Eg,in`.

---

## 9. Finite momentum-memory result

The underdamped stochastic surrogate

```math
dv=(v_d-v)dt/\tau_m
+\sqrt{2\sigma_v^2/\tau_m}\,dW_t
```

shows that the post-entrance-gap shape depends on the initial longitudinal momentum distribution.

```text
negligible directed memory
-> plateau

persistent positive directed memory
-> decline after entrance gap

symmetric hot initial longitudinal spread
-> decline is not guaranteed; mean/variance can rise.
```

Therefore the old entrance-gap timing maximum is **SUPERSEDED AS A UNIVERSAL CLAIM**.

Retain it only as a ballistic/persistent-memory special case.

---

## 10. Photoexcitation correction

Do not treat downstream photoelectrons as cold.

Use

```math
\boxed{\varepsilon_{\rm gen}=\xi_e(E_\gamma-E_g).}
```

The simplified flat-heavy-hole HgCdTe Kane limit motivates `xi_e approximately 1` as one relevant channel limit; a multiband optical calculation remains open.

Do not convert excess energy directly into persistent forward longitudinal velocity without a momentum-space transport model.

---

## 11. Primary transport literature boundary

Palermo et al., *Solid-State Electronics* 53, 70–78 (2009), DOI `10.1016/j.sse.2008.10.003`, use Monte Carlo transport for `Hg_0.8Cd_0.2Te` at 77 K and extract drift velocity, mean energy, diffusion, impact-ionization rate, velocity-relaxation and energy-relaxation quantities. They validate a hydrodynamic description against Monte Carlo / experiment.

Modern HgCdTe APD Monte Carlo work likewise treats momentum-changing phonon, alloy and impurity scattering explicitly or through calibrated reduced models.

Use this literature to constrain the next model. Do not invent relaxation coefficients from narrative statements.

---

## 12. Revised decisive experiment

Do not score the experiment only by whether a strict maximum appears.

Sweep wavelength through

```text
near output cutoff
-> graded-gap interval
-> entrance-gap wavelength
-> shorter wavelengths
```

under fixed detector conditions.

Prefer differential low-frequency group delay or normalized impulse centroid to suppress common readout delay.

The primary target is a reproducible crossover tied to

```math
\boxed{\lambda_{g,\rm in}\simeq hc/E_{g,\rm in}.}
```

The post-crossover shape is then a transport diagnostic.

---

## 13. Important stopped shortcuts

Do not restart casually:

- active-volume-only detector bound;
- finite absorber count as one-photon speed limit;
- spectral FWHM as universal carrier speed;
- low-field mobility extrapolated into high-field HgCdTe;
- direct BTBT assumed first limiter;
- local `F_II(x)` without local-equilibrium justification;
- downstream photoelectrons assumed cold;
- excess photon energy equated to forward drift velocity;
- entrance-gap timing maximum treated as transport independent;
- visible cusp treated as guaranteed.

---

## 14. Current numerical regressions

```text
numerics/hgcdte_spectral_momentum_scattering_surrogate.py
numerics/hgcdte_spectral_delay_relaxation.py
numerics/hgcdte_spectral_delay_peak.py
numerics/hgcdte_spectral_transit_statistics.py
numerics/hgcdte_dimensionless_device_phase_map.py
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
```

The ballistic peak regression is historical/supporting, not the current universal target.

---

## 15. Next decisive work

Do not add another abstract theorem.

Next priority:

1. build a reduced hydrodynamic wavelength-resolved model using published HgCdTe velocity and energy relaxation structure;
2. if interpolation coefficients cannot be recovered reliably, keep relaxation functions parametric rather than fitting figures;
3. search for or propose fixed-bias wavelength-resolved timing data to test the entrance-gap crossover.

Only after the crossover survives calibrated transport or experiment should publication significance be reassessed.
