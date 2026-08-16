# Paper 02 — exact-planar two-carrier closure gate

**Date:** 2026-08-16  
**Status:** PREDECLARED BEFORE RESULT INSPECTION / REV. 8 PHYSICS GATE

## Question

Does the Rev. 7 deterministic apparent-diffusion mechanism survive when the measured planar Shockley–Ramo transient contains both members of a fully collected electron–hole pair rather than one mobile carrier only?

This gate is designed to answer that question without forcing a two-carrier signal through the Rev. 7 one-mode inverse.

## Pair forward model

Use the same planar coordinate `0 <= z <= L` and weighting potential `phi_w=z/L`.

For the carrier moving downstream from creation depth `z` to `L`, retain the exact Rev. 7 deterministic point transfer

```text
H_down(z,omega) = (1/L) integral_z^L exp[-i omega tau_down(x;z)] dx.
```

For a counterpropagating carrier moving from `z` to `0` with positive speed magnitude `v_up(x)`, use the output polarity for which the two induced-current contributions add:

```text
H_up(z,omega) = (1/L) integral_0^z exp[-i omega tau_up(x;z)] dx,
tau_up(x;z) = integral_x^z du/v_up(u).
```

For the first closure stress, `v_up` is spatially uniform and independently variable. The downstream carrier is tested both with uniform velocity and with the exact Rev. 7 collector-side heterogeneous velocity profile.

Hard dc identity:

```text
H_down(z,0) = (L-z)/L
H_up(z,0)   = z/L
H_pair(z,0) = 1
```

The maximum sampled dc pair-identity error must be <= `1e-12` before any finite-frequency result is interpreted.

## Why the inverse must be two-mode

Even a uniform two-carrier device contains two source-coordinate exponentials with opposite propagation directions. Therefore applying the old one-mode inverse to the pair transient would deliberately misspecify the uniform null.

Use instead

```text
J_m = C + K_down F_m(r_down) + K_up F_m(r_up),
```

where `F_m(r)` is the same finite-kernel basis already validated in Rev. 7. For fixed roots, profile the three complex linear coefficients exactly by least squares; optimize only the two complex roots.

For uniform velocities the expected roots are

```text
r_down = +i omega/v_down
r_up   = -i omega/v_up.
```

The downstream transport convention remains `gamma_down=-r_down` for comparison with Rev. 7.

## Countercarrier speed sweep

Let `v_down,ref` be the exact upstream/downstream-carrier speed in the uniform portion of the Rev. 7 field profile. Test

```text
v_up/v_down,ref = 0.05, 0.10, 0.25, 0.50, 1, 2, 4, 10, 20.
```

Primary probe frequencies:

```text
100 MHz, 500 MHz, 1 GHz.
```

The extreme ratios are diagnostic conditioning stresses; they are not asserted to represent a particular material.

## Gate A — uniform-pair null

For every speed ratio and probe frequency:

1. generate both carriers with uniform velocity;
2. fit the pair-aware two-mode inverse;
3. report root errors, centered/differential channel residual, and root-separation/conditioning diagnostics.

Acceptance for interpreting the heterogeneous sweep:

- dc pair identity <= `1e-12`;
- centered two-mode relative residual <= `1e-8` for the well-conditioned core sweep `0.10 <= v_up/v_down,ref <= 10`;
- each fitted root must be continuously associable with the expected sign of its imaginary part;
- inferred downstream `|D_eff| <= 1e-7 m^2/s` in the uniform null for the well-conditioned core sweep.

If root recovery becomes ill-conditioned at an extreme speed ratio, that case must be labeled non-identifiable rather than forced into the sign tally.

## Gate B — heterogeneous downstream carrier

Replace only the downstream carrier by the exact Rev. 7 heterogeneous planar profile while retaining the same uniform countercarrier. Refit the same two-mode model.

For each identifiable case report:

- downstream fitted root and `D_eff`, `w_eff`;
- countercarrier fitted root;
- centered pair-model residual;
- difference between downstream `D_eff` and the Rev. 7 single-carrier exact-continuum value;
- root separation and local conditioning.

Classification:

### B1 — mechanism survives pair-aware observation

Supported if positive downstream apparent diffusion persists across a nontrivial well-conditioned range of countercarrier speed ratios and the uniform-pair null remains at zero diffusion.

The manuscript may then claim only the checked pair-aware family and the unipolar limit.

### B2 — mechanism survives only in separable regimes

If positive apparent diffusion persists only when the two carrier modes are sufficiently separable, narrow the claim to pair responses for which the carrier modes are independently identifiable. Treat near-degenerate regimes as an identifiability limit.

### B3 — mechanism does not survive the pair-aware model

If a physically coherent pair-aware fit removes or reverses the downstream apparent diffusion throughout the identifiable sweep, the manuscript must narrow its central physical scope to a single-mobile-carrier/unipolar observable. Do not reinterpret numerical noise as survival.

## Reproducibility requirements

The implementation must:

- import/reuse the frozen exact-planar Rev. 7 downstream transfer and finite kernels rather than rebuilding them independently;
- preserve all raw rows and a compact JSON summary;
- include deterministic optimizer seeds tied to the known uniform roots plus bounded multistart checks;
- record optimizer convergence and root-label assignment;
- run in GitHub Actions from a clean checkout;
- never edit Rev. 7 manuscript sources.
