# Experiment 01 — Artifact Status Map

**Date:** 2026-08-08  
**Purpose:** preserve the adversarial research trail without allowing stopped or superseded branches to compete with the current frontier.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

---

## A. Canonical current frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
4. `DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`
5. `STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`
6. `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`
7. `THERMAL_IRREVERSIBILITY_COST.md`
8. `HOPFIELD_RESERVOIR_RESOURCE_COST.md`
9. `HOPFIELD_RETUNING_NO_GO.md`
10. `RESEARCH_LOG.md`
11. `ARCHIVE_STATUS.md`

There is still **no manuscript**.

---

## B. Current strongest general supporting result

### `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`

Status: **active exact finite-network theorem / detector-facing passivity corollary; novelty unassessed and not claimed**.

For finite stable passive strictly proper transfer with total optical and detector access budgets

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

The proof uses an exact controllability-Gramian decomposition. A single passive resonance saturates the bound.

The earlier `2 min(L,R)` result is historical only.

---

## C. Current loophole audits

### `DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`

Status: **active scope audit / explicit counterexample to an overgeneralized all-frequency theorem**.

Key result: ideal frequency-independent prompt feedthrough makes the total all-frequency `H2` area divergent. Over finite angular bandwidth `W`,

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\,\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

Interpretation: prompt coupling is an additional boundary resource with its own bandwidth/channel strength.

### `STRUCTURED_RESERVOIR_ACCESS_AUDIT.md`

Status: **active conditional continuum extension**.

If passive finite augmented realizations converge in `H2` and their terminal access budgets converge to finite `L,R`, then the limiting structured-reservoir transfer obeys the same harmonic bound.

This is not a universal continuum theorem.

---

## D. Current optical-to-thermodynamic bridge

### `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`

Status: **active restricted corollary with strong prior-art overlap**.

Uses the established one-free-space-channel thermodynamic coupling-rate ceiling, converted carefully from energy-decay to repository amplitude-decay convention:

```math
L_B\le\frac{W}{4\pi}.
```

Combining with the harmonic theorem gives

```math
\boxed{
\overline T_B
\le
\frac{R_B}{R_B+W/(4\pi)}
}
```

and the necessary detector-access condition

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

Do not claim rate matching or the optical thermodynamic bound as new.

### `THERMAL_IRREVERSIBILITY_COST.md`

Status: **active restricted thermal detector-reservoir result**.

Local detailed balance for a localization transition with energy release `Delta` gives

```math
k_\uparrow/k_\downarrow=e^{-\Delta/(k_BT)}.
```

With `k_down = 2R_B`, desired band-averaged efficiency/bandwidth imposes

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
 e^{-\Delta/(k_BT)}.
}
```

For allowed reverse thermal activation `D_rev`,

```math
\boxed{
\Delta
\ge
k_BT
\ln\!\left[
\frac{\eta W}
{2\pi(1-\eta)D_{\rm rev}}
\right].
}
```

`D_rev` is not automatically an observable dark-count rate. A complete detector cycle is now required.

---

## E. Active nonperturbative supporting branch

### `HOPFIELD_RETUNING_NO_GO.md`

Status: **active supporting theorem; candidate distinct lemma; priority unproven**.

Shows that with fixed target dressed frequency and fixed local bath resources, arbitrarily increasing TRK-consistent internal coupling drives at least one dressed optical/detector access to zero.

### `HOPFIELD_RESERVOIR_RESOURCE_COST.md`

Status: **active supporting resource result**.

Shows that defeating the fixed-bath Hopfield collapse while preserving target peak transfer and linewidth requires at least one bare reservoir resource to grow asymptotically as `sqrt(g)`.

### `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`

Status: targeted negative literature search. Deep-strong decoupling is established; priority of the exact fixed-target corollary remains unproven.

### `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`

Status: supporting derivation with strong prior-art overlap.

---

## F. Multimode branch

### `MULTIMODE_ESCAPE_AUDIT.md`

Status: active adversarial provenance.

Records that

- spectator strong-coupling sectors defeat any theorem based only on the largest internal coupling;
- growing useful mode density can tile bandwidth;
- mode count is an explicit resource;
- integrated transfer is the more robust object.

---

## G. Earlier supporting derivations

These remain scientifically useful but are not the frontier:

- `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`
- `FINITE_EMITTER_FORM_FACTOR.md`
- `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`
- `MICROSCOPIC_SINGLE_TRANSITION.md`
- `THERMAL_INPUT_CHANNEL.md`
- `ONE_PORT_RESONATOR_DYNAMICS.md`

---

## H. Direction-changing counterexample

### `ACTIVE_VOLUME_COUNTEREXAMPLE.md`

Status: **branch-closing counterexample retained permanently**.

It prevents resurrection of the original active-volume-only conjecture.

---

## I. Stopped / superseded general routes

Do not restart without a concrete new assumption defeating the recorded failure.

### Active-volume-only theorem — STOPPED

### Finite absorber count as the missing one-photon speed limit — STOPPED

### Largest multimode coupling as a universal control parameter — STOPPED

### Preliminary `2 min(L,R)` multimode bound — SUPERSEDED

### All-frequency harmonic theorem with arbitrary ideal feedthrough — INVALID EXTENSION

A constant prompt path is an explicit counterexample because it carries infinite Markov bandwidth.

---

## J. Numerical material

Active directory: `numerics/`.

### `one_port_time_domain_check.py`

Validates the one-port modulation transfer function.

### `passive_multimode_h2_stress.py`

Validates the Gramian identity, harmonic bound, single-mode saturation, and direct frequency integration.

No CI workflow is justified yet.

---

## K. Literature state

Important established prior areas now include

- passive/scattering linear-system theory;
- Maxwell and quantum passive realizations;
- optical material/LDOS bounds;
- thermodynamic free-space coupling-rate bounds;
- multiresonant broadband absorption;
- Bode-Fano matching limits;
- reaction-coordinate / pseudomode reservoir mappings;
- local/KMS detailed balance;
- dark-state quantum detector models;
- deep-strong light-matter decoupling.

The project still has no integrated novelty audit because the detector-specific target continues to evolve.

---

## L. Current forward branch

Build the complete minimal cyclic detector:

```text
|g> -- photon --> |e>
|e> <-> |d>       thermal detector bath
|d> -- readout/reset --> |g>.
```

The next calculation must define

1. the counted transition;
2. reverse thermal pathways;
3. reset/readout resource;
4. spontaneous false-count pathways;
5. steady-state count rate and dead time;
6. net thermodynamic cycle current versus raw count events.

Do not call reverse activation a dark count until this cycle is explicit.

Do not add HgCdTe-specific transport yet.

---

## M. Archival rule

When a result is superseded or invalidated:

1. update `CURRENT_STATE.md`;
2. update `CLAIM_LEDGER.md`;
3. record the chronology in `RESEARCH_LOG.md`;
4. mark status here;
5. retain derivations that document important failures, corrections, or narrowing of scope.