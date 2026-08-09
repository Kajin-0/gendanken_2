# Experiment 01 — Artifact Status Map

**Date:** 2026-08-08  
**Purpose:** preserve the adversarial research trail without allowing stopped or superseded branches to compete with the live frontier.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

There is still **no manuscript**.

## A. Canonical current frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
4. `HGCDTE_KANE_SCALE_AUDIT.md`
5. `FIELD_DRIVEN_COLLECTION_TUNNELING.md`
6. `BALLISTIC_BARRIER_SPEED_LEAKAGE.md`
7. `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md`
8. `RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md`
9. `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`
10. `RESEARCH_LOG.md`
11. `ARCHIVE_STATUS.md`

## B. Active HgCdTe/material branch

### `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`

**Status:** current active material normalization; no novelty claim.

Key result after explicit simplified Kane substitution:

```math
j=x^2e^{-1/x},
\qquad
x=F/F_K,
\qquad
j=J/J_K,
```

with

```math
F_K\propto\lambda_c^{-2},
\qquad
J_K\propto L\lambda_c^{-4}.
```

Exact current-target inversion is recorded with Lambert `W`.

Next missing input: primary high-field `v_d(F)` for a definite HgCdTe composition/density/temperature.

Regression:

`numerics/hgcdte_btbt_normalized_sweep.py`.

### `HGCDTE_KANE_SCALE_AUDIT.md`

**Status:** active material-scale interpretation.

Maps simplified Kane velocity, tunneling field, microscopic length and cutoff wavelength. Establishes that the one-barrier quantum speed scale is generally far above practical detector response, whereas BTBT field scales can be technologically relevant.

### `FIELD_DRIVEN_COLLECTION_TUNNELING.md`

**Status:** active supporting fixed-thickness model.

At fixed thickness and in the low-field drift regime, increasing field-driven transit speed increases direct BTBT. Explicitly records thinning as a counterexample to universality.

### `BALLISTIC_BARRIER_SPEED_LEAKAGE.md`

**Status:** supporting small-length quantum audit.

One optimized parabolic rectangular barrier gives

```math
\mathcal T_d
\gtrsim
\exp[-2c_t\Delta E/(\hbar B_{\rm tr})].
```

Useful as an asymptotic warning, not the practical HgCdTe frontier.

## C. Electronic energy-filter branch

### `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`

**Status:** active supporting semiconductor detailed-balance result.

Links useful contact extraction and reverse Fermi loading. Reverse loading hazard is not automatically a dark current/count.

### `RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md`

**Status:** one-pole supporting model.

Derives exact zero-temperature occupied-side leakage through a finite-linewidth Breit-Wigner resonance and the sharp-filter `hB^2/(4Delta)` asymptotic.

The latter is **not universal**.

### `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md`

**Status:** direction-correcting counterexample/audit.

Shows higher-order filters can suppress occupied-side tails far more strongly at fixed FWHM, while group/Wigner delay grows with filter order.

Permanent lesson:

> spectral FWHM is not an architecture-independent electronic transport speed.

Further abstract Wigner-Smith/filter generalization is currently stopped.

## D. Abstract adaptive/output branch — closed as universal route

### `ADAPTIVE_FEEDFORWARD_MODE_CAPACITY.md`

**Status:** exact finite-instrument supporting theorem.

```math
\sum_j\eta_j\le rd.
```

Adaptive branching replaces storage rank with storage × branch rank.

Regression:

`numerics/adaptive_instrument_rank_stress.py`.

### `OUTPUT_RECORD_INFORMATION_CAPACITY.md`

**Status:** branch-closing output-continuum audit.

Shows why local Landauer work or finite internal storage rank cannot become universal always-on detector limits when branch/arrival information can be exported into a large output record continuum.

**Decision:** do not keep extending abstract space-time resource vectors without a concrete detector need.

## E. Strongest retained passive optical/network result

### `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`

**Status:** exact finite passive-network detector-facing corollary; no novelty claim.

```math
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
```

Tight; one matched passive resonance saturates.

Regression:

`numerics/passive_multimode_h2_stress.py`.

Keep as structural provenance, not the active material frontier.

## F. Active/time-dependent supporting branch

Retain as supporting resource/counterexample work:

- `ACTIVE_FREQUENCY_CONVERTER_BASELINE.md`
- `MULTIMODE_ACTIVE_PUMP_RESOURCE.md`
- `TRAVELING_WAVE_ACTIVE_CONVERTER.md`
- `ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md`
- `TIME_DEPENDENT_CAPTURE_AUDIT.md`
- `TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md`
- `ALWAYS_ON_TEMPORAL_COVERAGE.md`

These established that active and time-dependent control can beat passive stationary matching, but only by introducing pump/control/timing/output resources. Strong prior-art overlap prevents treating those generic mechanisms as current novelty targets.

## G. Passive/autonomous detector bridge

Retain for prior-art and resource provenance:

- `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`
- `THERMAL_IRREVERSIBILITY_COST.md`
- `AUTONOMOUS_DETECTOR_CAPTURE_GAP.md`
- `CAPTURE_TO_CLICK_COMPOSITION.md`
- `UNIFIED_THREE_LEVEL_CAPTURE_MACHINE.md`
- `READINESS_BANDWIDTH_AFFINITY.md`
- `NESS_OPTICAL_RESPONSE_AUDIT.md`
- `PUBLICATION_BOUNDARY_AUDIT.md`

Key prior-art boundary:

- Young, Sarovar & Leonard (2018) already cover incoming fields + absorption + amplification + efficiency/dark counts/timing.
- Schwarzhans et al. (2026) already cover autonomous work/reset + entropy + internal dark counts/jitter/dead time.

Publication audit remains:

> **Continue research; no manuscript yet.**

## H. Nonperturbative Hopfield supporting branch

Retain for mechanism/provenance:

- `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`
- `HOPFIELD_RETUNING_NO_GO.md`
- `HOPFIELD_RESERVOIR_RESOURCE_COST.md`
- `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`

The fixed-target retuning result remains **candidate distinct supporting lemma; priority unproven**.

## I. Earlier optical/microscopic provenance

Retain:

- `ACTIVE_VOLUME_COUNTEREXAMPLE.md`
- `ONE_PORT_RESONATOR_DYNAMICS.md`
- `THERMAL_INPUT_CHANNEL.md`
- `MICROSCOPIC_SINGLE_TRANSITION.md`
- `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`
- `FINITE_EMITTER_FORM_FACTOR.md`
- `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`

`ACTIVE_VOLUME_COUNTEREXAMPLE.md` is permanent because it prevents resurrection of the original false active-volume theorem.

## J. Stopped / invalidated general routes

Do not restart without a new explicit assumption that defeats the recorded counterexample:

- active-volume-only universal theorem;
- finite absorber count as missing one-photon speed limit;
- largest internal coupling as universal multimode parameter;
- preliminary `2 min(L,R)` passive bound — superseded;
- all-frequency passive theorem with ideal feedthrough;
- generic capture+amplification novelty;
- generic autonomous detector-thermodynamics novelty;
- universal active `pump ~ W^2` law;
- finite internal storage as always-on detector capacity;
- local Landauer erasure as universal adaptive detector cost;
- single-Lorentzian `B^2/Delta` leakage as universal electronic theorem;
- spectral FWHM as universal transport speed;
- fixed-thickness field-speed tradeoff as universal when thickness may shrink;
- low-field mobility extrapolation into HgCdTe high-field operation.

## K. Active numerical files

- `numerics/one_port_time_domain_check.py`
- `numerics/passive_multimode_h2_stress.py`
- `numerics/adaptive_instrument_rank_stress.py`
- `numerics/hgcdte_btbt_normalized_sweep.py`

No CI workflow is currently justified.

## L. Current forward branch

The next task is **not** another abstract theorem.

Obtain a traceable high-field electron velocity law for a definite HgCdTe composition and temperature, then combine it with

```math
F_{\max}^{\rm BTBT}
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}
```

and

```math
B_{\rm tr,max}
=\frac{c_t}{L}v_d(F_{\max}).
```

Then determine which mechanism intervenes first:

```text
direct BTBT
vs
hot-electron/impact-ionization transport
vs
TAT / SRH / another real device mechanism.
```

Follow whichever physics actually wins.