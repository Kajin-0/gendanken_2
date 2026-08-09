# Experiment 01 — Artifact Status Map

**Date:** 2026-08-09  
**Purpose:** keep the active frontier distinct from supporting, corrected, superseded, and stopped branches.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

There is still **no manuscript**.

---

## A. Canonical active frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `HGCDTE_SPECTRAL_DELAY_PEAK.md`
4. `HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md`
5. `HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`
6. `HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md`
7. `HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md`
8. `HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`
9. `HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`
10. `HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md`
11. `HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md`
12. `RESEARCH_LOG.md`

### Current candidate prediction

In the stated high-optical-depth graded-transport model,

```math
\boxed{
T(E_\gamma)
\text{ has a maximum at }
E_\gamma=E_{g,\rm in}.
}
```

Equivalently,

```math
\boxed{
\lambda_{\rm peak}\simeq hc/E_{g,\rm in}.
}
```

Status:

**CANDIDATE DISTINCT / UNDEREXPLORED ANALYTIC PREDICTION — PRIORITY UNPROVEN.**

The timing peak survives the current deterministic mean-energy-relaxation robustness test but has not yet been tested with a full scattering model or experiment.

---

## B. Active spectral-timing derivations

### `HGCDTE_SPECTRAL_DELAY_PEAK.md`

**Status:** active candidate prediction.

Role: derives the nonmonotonic high-optical-depth timing curve and entrance-gap delay maximum.

### `HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md`

**Status:** active numerical robustness result.

Role: couples mean energy relaxation to Kane group velocity and shows the peak remains at the entrance gap across the tested parameter sweep.

### `HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`

**Status:** active falsification plan.

Role: proposes a tunable-wavelength timing sweep using differential group delay / normalized impulse centroid to reduce common readout contamination.

### `HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md`

**Status:** active corrected ballistic timing kernel.

Role: combines the exact optical-depth generation distribution with nonzero photoelectron initial energy.

### `HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md`

**Status:** active HgCdTe-specific specialization.

Role: shows why the flat-heavy-hole Kane limit gives `xi_e approximately 1` and derives the endpoint maximum of exit mean electron energy.

### `HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`

**Status:** active correction note.

Role: records the invalidation of the cold-downstream-photoelectron assumption and introduces `xi_e`.

### `HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`

**Status:** active exact optical statistic plus corrected energy mapping.

Role: derives the conditional truncated-exponential generation distribution in optical-depth coordinates.

### `HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md`

**Status:** active spectral geometry.

Role: maps wavelength to first allowed generation position and remaining graded transport distance.

### `HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md`

**Status:** active prior-art boundary.

Role: separates known graded-HgCdTe spectral/timing physics from the candidate entrance-gap timing peak.

---

## C. Active supporting graded-device branch

These files remain scientifically active because they define the material architecture behind the timing prediction, but they are no longer the immediate frontier.

### `HGCDTE_DIMENSIONLESS_DEVICE_PHASE_MAP.md`

Absorber nonlocal-II margin + boundary local-tunneling margin + normalized latency.

### `HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`

Exact deterministic mean-energy phase boundary inside the one-relaxation-length model.

### `HGCDTE_II_SAFE_TRANSIT_CEILING.md`

Lambert-W inversion giving required relaxation distance/time for aggressive grading.

### `HGCDTE_BALLISTIC_GRADING_SPAN_RULE.md`

Ballistic gap/cutoff-span sanity rule.

### `HGCDTE_BOUNDARY_COOLING_TRANSIT_FLOOR.md`

Combines boundary cooling length and local TAT/BTBT width floors.

### `HGCDTE_GRADED_ABSORBER_BOUNDARY_RELAXATION.md`

Shows that a minimally compensated wider-gap boundary can act as a relaxation region rather than adding downhill carrier work.

### `HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md`

Majority-band pinning in quasi-neutral p-type graded HgCdTe.

### `HGCDTE_LINEAR_GRADED_KANE_WKB.md`

Exact linear-profile direct-Zener WKB result at fixed conduction drive.

### `HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`

Local TAT/BTBT voltage-capacity and maximin field-allocation result.

### `HGCDTE_ELECTROSTATIC_COMPENSATION_PEAK_FIELD_BOUND.md`

Integral peak-field lower bound for barrier compensation.

---

## D. Corrected / superseded spectral statements

### Cold downstream photoelectron

**Status:** INVALIDATED.

Downstream absorption with `E_gamma > E_g(x)` creates nonzero photoelectron excess energy.

Use `HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md` and the corrected spectral files.

### Symmetric `xi_e=1/2` treated as HgCdTe material value

**Status:** STOPPED SHORTCUT.

It is exact only for the symmetric two-band optical transition. HgCdTe heavy-hole-to-electron transitions motivate a baseline closer to `xi_e=1` in the flat-heavy-hole simplified Kane limit.

### Monotonic `higher QE -> lower timing jitter`

**Status:** INVALIDATED GENERALIZATION.

The generation-position timing spread can be mildly nonmonotonic at finite optical depth before tending to zero in the optically thick limit.

---

## E. Earlier supporting/stopped branches

Preserve but do not restart casually:

- active-volume-only detector theorem;
- finite absorber count as one-photon limit;
- LDOS-only universal limit;
- fixed-target Hopfield branch as universal theorem;
- finite internal rank as always-on detector capacity;
- universal pump-bandwidth law;
- contact single-pole filter as universal speed/leakage law;
- low-field mobility extrapolation into high-field HgCdTe;
- direct BTBT assumed first high-field limiter;
- homogeneous nonuniform-field shaping as automatic improvement;
- local `F_II(x)` used in thin devices without energy history;
- pure grading assumed to eliminate all leakage.

These remain provenance in the claim ledger and research log.

---

## F. Current numerical regressions

```text
numerics/hgcdte_spectral_delay_relaxation.py
numerics/hgcdte_spectral_delay_peak.py
numerics/hgcdte_spectral_transit_statistics.py
numerics/hgcdte_dimensionless_device_phase_map.py
numerics/hgcdte_ii_safe_transit_ceiling.py
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
numerics/hgcdte_graded_kane_wkb.py
numerics/hgcdte_field_profile_variational.py
numerics/hgcdte_nonlocal_ii_surrogate.py
numerics/hgcdte_btbt_normalized_sweep.py
```

No CI is justified yet.

---

## G. Next active work

The next step should be one of only two things:

1. replace the deterministic mean-energy transport with a physically stronger momentum-scattering / drift-diffusion / Monte Carlo model and retest the timing peak; or
2. obtain/reanalyze wavelength-resolved timing data on a compositionally graded HgCdTe detector.

Do not add more abstract detector-resource branches before one of these tests.

If the entrance-gap timing maximum survives stronger transport physics and remains absent from prior literature, reassess manuscript readiness.
