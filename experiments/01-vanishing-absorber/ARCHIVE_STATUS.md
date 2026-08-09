# Experiment 01 — Artifact Status Map

**Date:** 2026-08-08  
**Purpose:** preserve the research trail without allowing invalidated or exploratory files to compete with the current frontier.

> Live `main`, root `AGENTS.md`, and `CURRENT_STATE.md` are authoritative.

---

## A. Canonical active state

Use these files first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `RESEARCH_LOG.md`
4. `ARCHIVE_STATUS.md`
5. `HOPFIELD_RETUNING_NO_GO.md`
6. `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`

There is no manuscript yet.

---

## B. Active supporting derivations

### `ONE_PORT_RESONATOR_DYNAMICS.md`

**Status:** closed at stated one-mode assumptions; active supporting derivation.

Role: fixes the one-port normalization; derives absorptance, critical coupling, energy lifetime, optical linewidth, absorbed-power modulation bandwidth, and the model-specific bulk-dark-event coupling optimum.

### `ACTIVE_VOLUME_COUNTEREXAMPLE.md`

**Status:** active counterexample; direction-changing result.

Role: constructs a shrinking constant-capacitance lossy dielectric family with `V_a -> 0`, fixed participation, fixed `gamma_a`, and `gamma_a/V_a -> infinity`.

This file is the canonical reason the active-volume-only theorem branch is stopped.

### `THERMAL_INPUT_CHANNEL.md`

**Status:** active restricted result.

Role: exact one-channel thermal photon counting through the Lorentzian absorber including Bose bunching; derives the critical-coupling optimum

```math
\mathcal C_{\rm th,max}^2
=1/[\pi\bar n(2+\bar n)].
```

Do not describe this as an internal-dark-count or full equilibrium detector theorem.

### `MICROSCOPIC_SINGLE_TRANSITION.md`

**Status:** active negative result / prior-art-overlapped branch.

Role: shows that one-photon dynamics of one two-level transition remains linear in the one-excitation sector, so finite absorber number / saturation alone does not create the missing speed bound.

### `FINITE_TRANSITION_LDOS_BANDWIDTH_BOUND.md`

**Status:** active conditional bound application.

Role: applies established bandwidth-averaged projected-LDOS theory to the matched microscopic detector and shows that useful optical coupling is finite for fixed passive material, nonzero bandwidth, allowed region, and finite emitter-environment separation.

The remaining `d -> 0` divergence is explicit.

### `FINITE_EMITTER_FORM_FACTOR.md`

**Status:** active microscopic regularization.

Role: analytically replaces the point-emitter `d^{-3}` divergence by a finite transition-density scale `a^{-3}` and records the oscillator-strength/state-extent inequality.

### `OSCILLATOR_STRENGTH_EXTENT_STRESS_TEST.md`

**Status:** active insufficiency result.

Role: shows that oscillator-strength plus finite-emitter extent does not algebraically close the perturbative problem when the selected transition strength is allowed to vary; the formal upper envelope runs into the nonperturbative regime instead.

### `NONPERTURBATIVE_HOPFIELD_CAPTURE.md`

**Status:** active nonperturbative supporting derivation.

Role: uses a TRK-consistent two-mode Hopfield model. In the symmetric resonant case, both dressed local reservoir rates remain exactly matched while their magnitude and the resolved-polariton transfer linewidth collapse at deep strong coupling.

### `HOPFIELD_RETUNING_NO_GO.md`

**Status:** **current strongest model-level candidate lemma**.

Role: proves that with

```math
g\to\infty,
\qquad
\omega_y=\omega_t>0
```

held fixed by arbitrary bare-frequency retuning, and with fixed positive local optical/detector bath coupling resources,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

Consequently resolved-polariton peak transfer and linewidth cannot both remain bounded away from zero.

**Novelty status:** unproven. Do not use priority language.

---

## C. Prior-art notes

### `HOPFIELD_RETUNING_PRIOR_ART_SWEEP.md`

**Status:** active targeted negative search; not proof of novelty.

Closest inspected prior work covers deep-strong light-matter decoupling, Purcell-effect collapse, gauge-consistent dressed dissipation, suppression of polariton decay/heat transport, and multimode decoupling.

No inspected source was found stating the exact fixed-dressed-frequency retuning theorem with two required local reservoir overlaps.

Current verdict:

> candidate distinct supporting lemma; priority unproven.

A broader search of older polariton transport/open-harmonic-network literature remains required before publication positioning.

---

## D. Numerics

Active directory: `numerics/`.

### `numerics/one_port_time_domain_check.py`

**Status:** active deterministic validation.

Role: independently integrates the one-port envelope under small modulation and verifies the analytic modulation response. Its coupling-ratio grid scan is only an algebra regression, not an independent physical derivation.

No CI workflow is justified yet.

A dedicated symbolic/numerical regression for the Hopfield retuning theorem may become worthwhile if the theorem survives the next adversarial extension.

---

## E. Stopped general branches

### Active-volume-only detector bound — STOP

Do not restart, absent a genuinely new explicit resource constraint:

```text
gamma_a/V_a <= constant
```

or

```text
eta^2 B <= C V_a.
```

The shrinking-capacitor counterexample kills these as general passive-continuum statements.

### Finite absorber number / saturation as universal one-photon bound — STOP

The one-excitation sector is linear and prior dark-state detector models already exploit this physics.

### TRK + finite extent automatically closes weak-coupling enhancement — STOP as sufficient argument

The oscillator-strength/extent stress test shows the retained inequalities do not close by themselves.

### Infinite Purcell/LDOS rate as a route to infinite detector speed — STOP

The weak-coupling rate model loses validity and the gauge-consistent Hopfield model exhibits deep-strong decoupling / linewidth collapse.

---

## F. Current forward branch

The next adversarial question is:

> Can a multimode optical environment or deliberately scaled reservoir engineering preserve both finite optical-to-detector peak transfer and finite transfer bandwidth at a fixed target frequency as the internal light-matter coupling becomes arbitrarily large?

Priority order:

1. multimode passive optical extension;
2. explicit scaling of optical/detector reservoir coupling resources with `g`;
3. strong/non-Markov reservoir counterexamples;
4. broader prior-art search if the fixed-target statement survives.

Do not add HgCdTe-specific transport yet.

---

## G. Artifact-growth rule

Documentation should grow because the physics demands separation, not because a mature repository is being imitated.

Create a new file only when it has a clear role such as a substantial derivation, counterexample, independent validation, approximation/error budget, focused prior-art comparison, or eventual manuscript snapshot.