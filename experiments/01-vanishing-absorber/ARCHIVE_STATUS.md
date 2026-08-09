# Experiment 01 — Artifact Status Map

**Date:** 2026-08-09  
**Purpose:** keep the active frontier distinct from supporting, superseded, and stopped branches.

> Live `main`, root `AGENTS.md`, `CURRENT_STATE.md`, and `CLAIM_LEDGER.md` are authoritative.

## A. Canonical active frontier

Read first:

1. `CURRENT_STATE.md`
2. `CLAIM_LEDGER.md`
3. `HGCDTE_LINEAR_GRADED_KANE_WKB.md`
4. `HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md`
5. `HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md`
6. `HGCDTE_TWO_REGION_FIELD_ALLOCATION.md`
7. `HGCDTE_VOLTAGE_TRANSIT_FIELD_ALLOCATION.md`
8. `HGCDTE_TAT_FIELD_SCALE.md`
9. `HGCDTE_TAT_BTBT_CROSSOVER.md`
10. `HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
11. `RESEARCH_LOG.md`

There is still **no manuscript**.

## B. Current strongest model-level corollary

### `HGCDTE_LINEAR_GRADED_KANE_WKB.md`

**Status:** active exact linear-profile WKB derivation; priority unassessed; no novelty claim.

For fixed useful conduction-band slope with grading fraction `eta`,

```math
\boxed{
\mathcal S_Z(\eta)/\mathcal S_Z(0)
=(1-\eta)^2/(1-2\eta)^{3/2}
}
```

for `0<=eta<1/2`.

Direct numerical WKB integration checks the closed action.

## C. Active field-engineering branch

### `HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md`

**Status:** active ideal two-band interpretation.

Role: separates common-mode band tilt from gap-gradient carrier drive and identifies finite band-edge drop as the grading resource.

### `HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md`

**Status:** active homogeneous no-go within local model.

Role: proves uniform field uniquely minimizes local WKB leakage at fixed transit time in the stated homogeneous high-field transport family.

### `HGCDTE_TWO_REGION_FIELD_ALLOCATION.md`

**Status:** active heterostructure allocation result.

Role: field should equalize marginal leakage cost per marginal transit-time reduction across regions.

### `HGCDTE_VOLTAGE_TRANSIT_FIELD_ALLOCATION.md`

**Status:** active bias-resource result.

Role: exact `VT` lower bound and two-region field contrast versus extra bias.

## D. Active competing leakage branch

### `HGCDTE_TAT_FIELD_SCALE.md`

**Status:** active TAT exponent-scale comparison.

### `HGCDTE_TAT_BTBT_CROSSOVER.md`

**Status:** active defect-density crossover/material-quality relation.

### `HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`

**Status:** active nonlocal II surrogate.

### `HGCDTE_RELAXATION_LENGTH_PHASE_BOUNDARY.md`

**Status:** active sensitivity boundary for missing `ell_E(F)` data.

### `HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md`

**Status:** active correction preventing bulk II onset from being misused as a finite-device threshold.

## E. Direct-BTBT / transport supporting files

- `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
- `HGCDTE_KANE_SCALE_AUDIT.md`
- `HGCDTE_FIELD_REGIME_MAP.md`
- `HGCDTE_TRANSPORT_BTBT_PHASE_BOUNDARY.md`
- `FIELD_DRIVEN_COLLECTION_TUNNELING.md`

These remain active provenance but are no longer the sole frontier.

## F. Earlier electronic-filter supporting branch

Retain:

- `FERMI_CONTACT_EXTRACTION_REVERSE_LOADING.md`
- `RESONANT_ENERGY_FILTER_SPEED_LEAKAGE.md`
- `MULTIPOLE_ENERGY_FILTER_DELAY_AUDIT.md`
- `BALLISTIC_BARRIER_SPEED_LEAKAGE.md`

These explain why contact detailed balance, linewidth broadening and filter delay were insufficient as universal limits.

## G. Earlier optical/control supporting branch

Retain for provenance:

- `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`
- `ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md`
- `TIME_DEPENDENT_CAPTURE_AUDIT.md`
- `TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md`
- `ADAPTIVE_FEEDFORWARD_MODE_CAPACITY.md`
- `OUTPUT_RECORD_INFORMATION_CAPACITY.md`
- `ALWAYS_ON_TEMPORAL_COVERAGE.md`
- Hopfield/LDOS/one-port supporting files.

These are no longer the active material direction.

## H. Permanent branch-closing artifacts

### `ACTIVE_VOLUME_COUNTEREXAMPLE.md`

Prevents resurrection of active-volume-only universal bounds.

### Homogeneous nonuniform-field escape — STOPPED within local model

`HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md` shows field shaping alone cannot improve the stated homogeneous speed/local-WKB tradeoff.

### Bulk `100 V/cm` II threshold interpretation — STOPPED

Finite-device II requires dead-space/energy-history treatment.

### Direct-BTBT-first ordinary-LWIR assumption — STOPPED

TAT, II and transport nonlinearity are separate and can intervene earlier.

## I. Numerical regressions

Active:

```text
numerics/hgcdte_graded_kane_wkb.py
numerics/hgcdte_field_profile_variational.py
numerics/hgcdte_relaxation_length_phase_boundary.py
numerics/hgcdte_nonlocal_ii_surrogate.py
numerics/hgcdte_impact_dead_space.py
numerics/hgcdte_field_regime_map.py
numerics/hgcdte_btbt_normalized_sweep.py
numerics/passive_multimode_h2_stress.py
numerics/one_port_time_domain_check.py
```

No CI workflow is justified yet.

## J. Prior-art status

Known prior anchors include

- Kane/Zener tunneling;
- WKB graded-gap HgCdTe;
- analytical HgCdTe heterojunction band profiles;
- composition-gradient built-in fields;
- HgCdTe APD field engineering;
- TAT/defect-limited HgCdTe leakage;
- nonlocal/dead-space avalanche transport.

The exact fixed-conduction-slope graded-action ratio has not been found in the focused search, but priority remains unassessed.

## K. Forward branch

Next:

1. choose a finite HgCdTe composition profile;
2. use realistic conduction/valence band-offset partition;
3. solve Poisson electrostatics;
4. compute `E_c(x),E_v(x)`;
5. compute transit and direct WKB action;
6. add TAT/interface states;
7. add nonlocal II;
8. rerun prior-art/publication audit.

Do not open a manuscript until this attack is complete.