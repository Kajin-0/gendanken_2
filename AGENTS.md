# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is a wavelength-resolved intrinsic timing prediction for compositionally graded HgCdTe plus a concrete tunable-wavelength falsification experiment; no novelty claim**

Read this file first.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, counterexamples, corrections, and prior-art collisions are part of the result.

**There is still no manuscript.**

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches;
6. make narrow edits where practical.

**Live `main` overrides all snapshots and recovery notes.**

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

semiconductor contact / energy filters
-> detailed balance, lifetime broadening, multipole delay

HgCdTe field-driven collection
-> normalized BTBT
-> low-field mobility shortcut killed

TAT / nonlocal II
-> defect spectrum + carrier energy history matter

homogeneous field shaping
-> no local speed/leakage benefit under stated model

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
-> HgCdTe flat-heavy-hole Kane limit gives xi_e approximately 1

CURRENT FRONTIER
-> intrinsic collection delay versus wavelength
-> high-optical-depth delay maximum at entrance-gap wavelength
-> peak survives finite mean energy relaxation
-> proposed tunable-wavelength falsification experiment.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_DELAY_PEAK.md`
6. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md`
7. `experiments/01-vanishing-absorber/HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`
8. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md`
9. `experiments/01-vanishing-absorber/HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md`
10. `experiments/01-vanishing-absorber/HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`
11. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`
12. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md`
13. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md`
14. `experiments/01-vanishing-absorber/HGCDTE_DIMENSIONLESS_DEVICE_PHASE_MAP.md`
15. `experiments/01-vanishing-absorber/HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`
16. `experiments/01-vanishing-absorber/HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`
17. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
18. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

---

## 5. Current device geometry

Use the quasi-neutral p-type graded baseline

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

This band-structure drive suppresses the ordinary same-direction direct-Zener geometry in the ideal graded-Kane model but does not remove TAT or hot-electron physics.

---

## 6. Spectral generation geometry

For

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

the first allowed generation position is

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

The maximum remaining transport distance is

```math
\boxed{
d_\gamma
=\frac{E_\gamma-E_{g,\rm out}}{G}.
}
```

This is the robust geometric basis of the active spectral branch.

---

## 7. Exact generation distribution

Let

```math
y(x)=\int_{x_\gamma}^{x}\alpha(E_\gamma,s)ds,
```

```math
\tau_\gamma=y(L).
```

Conditioned on absorption,

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}
{1-e^{-\tau_\gamma}}.
}
```

For the analytic local model

```math
\alpha=C(E_\gamma-E_g)^\beta,
```

this maps exactly to generation position and remaining carrier distance.

---

## 8. Critical photoexcitation correction

Do not treat every downstream-generated electron as cold.

Define local photon excess

```math
u=E_\gamma-E_g(x).
```

Parameterize electron excess at generation by

```math
\boxed{
\varepsilon_{\rm gen}=\xi_eu.
}
```

The symmetric two-band transition gives `xi_e=1/2`.

The experimentally validated simplified HgCdTe Kane model contains a nearly flat heavy-hole band and heavy-hole-to-electron transitions. In that limiting channel,

```math
\boxed{\xi_e\approx1.}
```

Treat `xi_e=1` as a physically relevant HgCdTe baseline, not a universal material constant.

A full multiband optical transition calculation remains open.

---

## 9. Corrected finite-relaxation exit energy

Define

```math
\delta E=E_\gamma-E_{g,\rm out},
```

```math
K=G\ell_E.
```

For local photon excess `u`,

```math
\boxed{
\varepsilon_{\rm out}(u)
=
K+(\xi_eu-K)
\exp[-(\delta E-u)/K].
}
```

The maximum over all generation positions occurs at an endpoint:

```math
\boxed{
\varepsilon_{\max}
=
\max\left[
K(1-e^{-\delta E/K}),
\xi_e\delta E
\right].
}
```

For the flat-heavy-hole limit,

```math
\boxed{
\xi_e=1
\Rightarrow
\varepsilon_{\max}=\delta E.
}
```

Energy relaxation can cool upstream-generated carriers but cannot cool a carrier created arbitrarily close to the output before collection.

---

## 10. Strongest current timing prediction

Let

```math
R=E_{g,\rm in}/E_{g,\rm out}>1,
```

```math
s=E_\gamma/E_{g,\rm out}-1.
```

### Inside the graded-gap range

For

```math
0<s\le R-1,
```

high optical depth places absorption near the first allowed point. The ballistic dimensionless delay is

```math
\boxed{
\theta_<(s)
=\frac{\sqrt s}{\sqrt{1+s}}
\left(1+\frac43s\right).
}
```

It rises with photon energy because generation moves upstream.

### Above the entrance gap

For

```math
s>R-1,
```

the whole absorber is optically allowed. Generation is pinned near the physical entrance and further photon energy increases the initial electron velocity.

For `xi_e>0`, transit time decreases.

Therefore

```math
\boxed{
T(E_\gamma)
\text{ has a maximum at }
E_\gamma=E_{g,\rm in}.
}
```

or

```math
\boxed{
\lambda_{\rm peak}
\simeq hc/E_{g,\rm in}.
}
```

This is the present candidate testable prediction.

---

## 11. First robustness result beyond ballistic transport

Use

```math
\frac{d\varepsilon}{dx}
=G-\frac{\varepsilon}{\ell_E}
```

with local Kane group velocity

```math
\boxed{
\frac{v}{v_K}
=
\frac{2\sqrt{\varepsilon(\varepsilon+E_g)}}
{2\varepsilon+E_g}.
}
```

Numerical integration over

```text
R = 1.5, 2, 3
L/ell_E = 0, 0.2, 0.5, 1, 2, 5, 10
```

kept the timing maximum at

```math
\boxed{E_\gamma=E_{g,\rm in}.}
```

Energy relaxation increased the peak delay but did not move it in the tested mean-energy model.

**Status:** CHECKED NUMERICALLY / CONDITIONAL, not a general scattering theorem.

---

## 12. Prior-art posture

Primary literature already establishes

- graded HgCdTe devices;
- grading-induced faster carrier response;
- graded spectral-QE effects;
- tunable-pulse HgCdTe timing instrumentation;
- heavy-hole-to-electron Kane transitions.

The focused search has not found an inspected primary source explicitly deriving or measuring

```text
wavelength
-> generation-position distribution
-> corrected graded transit distribution
```

or the specific entrance-gap timing maximum.

Status:

**CANDIDATE DISTINCT / UNDEREXPLORED ANALYTIC PREDICTION — PRIORITY UNPROVEN.**

Do not infer novelty from the negative search.

---

## 13. Proposed decisive experiment

See `HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`.

Use a detector with known composition profile and sweep pulsed wavelength across

```text
near output cutoff
-> graded-gap interval
-> entrance-gap wavelength
-> shorter wavelengths.
```

Primary observable should be differential low-frequency group delay or normalized impulse centroid, because a wavelength-independent readout transfer cancels in differences.

Strong validation would be a reproducible timing extremum near the independently predicted entrance-gap wavelength, ideally shifting with `E_g,in(T)` under a temperature sweep.

Do not claim the effect has been observed.

---

## 14. Important stopped shortcuts

Do not restart casually:

- active-volume-only detector bound;
- finite absorber count as one-photon speed limit;
- largest internal coupling as a universal resource;
- finite internal rank as always-on detector capacity;
- spectral FWHM as arbitrary carrier speed;
- low-field mobility extrapolated to high-field HgCdTe;
- direct BTBT assumed first high-field limiter;
- bulk II onset used as a finite-device threshold;
- nonuniform field assumed beneficial in homogeneous material;
- pure grading assumed to eliminate all leakage;
- local `F_II(x)` used without local-equilibrium justification;
- downstream photoelectrons assumed cold;
- `xi_e=1/2` treated as a real HgCdTe material constant;
- monotonic `higher QE -> lower jitter` claim.

---

## 15. Current numerical regressions

```text
numerics/hgcdte_spectral_delay_relaxation.py
numerics/hgcdte_spectral_delay_peak.py
numerics/hgcdte_spectral_transit_statistics.py
numerics/hgcdte_dimensionless_device_phase_map.py
numerics/hgcdte_ii_safe_transit_ceiling.py
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
numerics/hgcdte_graded_kane_wkb.py
```

No CI is justified yet.

---

## 16. Next decisive work

Do not add another abstract resource theorem.

The next two useful routes are:

1. **stronger transport robustness:** add momentum scattering / drift-diffusion or Monte Carlo structure and test whether the entrance-gap timing maximum survives;
2. **experimental collision:** locate or generate wavelength-resolved impulse/group-delay data on one compositionally graded HgCdTe detector under fixed bias/readout.

If the peak survives a physically stronger transport model and remains absent from prior literature, reassess manuscript readiness then.
