# Paper 02 — two-carrier follow-up after the predeclared gate

**Date:** 2026-08-16  
**Status:** POST-HOC DIAGNOSTIC PLAN AFTER INSPECTION OF PREDECLARED TWO-ROOT RESULT

## What the predeclared gate established cleanly

GitHub Actions run `31965377545` executed `paper02_two_carrier_exact_continuum.py` from a clean checkout and passed the hard Gate-A controls.

- maximum dc pair-identity error: `1.1102230246251565e-16`;
- maximum core uniform-pair `|D_down|`: `6.579444100145674e-09 m^2/s`;
- maximum core uniform-pair centered two-mode residual: `1.735154346493963e-13`.

Therefore the pair forward model, Ramo polarity, finite-kernel averaging, and two-mode representation of the *uniform* pair null are internally consistent.

## Why the automatic heterogeneous B2 label is not accepted

The first script classified the heterogeneous sweep as `B2_MECHANISM_SURVIVES_ONLY_PART_OF_IDENTIFIABLE_PAIR_SWEEP` because three core rows returned positive downstream D. That automatic classification used the passing uniform null as its principal identifiability flag.

Inspection of the heterogeneous fitted roots shows that this is insufficient. In many heterogeneous rows the second fitted root moves far from the known physical countercarrier root; in several cases its imaginary part lands on the sign-preserving near-zero bound. The downstream pseudo-root can simultaneously acquire very large positive or negative real parts, producing enormous and clearly unstable effective-D values.

This does **not** invalidate the uniform two-carrier control. It means that six complex spectral channels at one frequency, fit with two freely moving complex roots plus three profiled complex amplitudes, do not provide a sufficiently stable carrier decomposition once one carrier departs from the assumed homogeneous mode.

Accordingly:

```text
The predeclared raw rows remain valid.
The automatic B2 physical interpretation is SUPERSEDED.
The correct disposition is: free two-root heterogeneous decomposition is not a reliable carrier-closure test in this configuration.
```

## Cleaner follow-up question

The countercarrier in the forward stress is deliberately simple: it has a known uniform speed and therefore a known homogeneous source-coordinate root

```text
r_up = -i omega/v_up.
```

A stronger diagnostic is therefore to treat this known countercarrier shape as an explicitly modeled nuisance rather than asking the six-channel data to rediscover both roots simultaneously.

Fit

```text
J_m = C + K_down F_m(r_down) + K_up F_m(r_up,true),
```

profiling `C`, `K_down`, and `K_up` while optimizing only the complex downstream root. The countercarrier amplitude remains free, so the test does not subtract the forward signal by hand.

This asks the relevant physical question:

> If the second carrier is present in the measured terminal transient and its simple transport mode is correctly represented, does the heterogeneous downstream carrier still acquire positive apparent diffusion under the homogeneous downstream inverse?

## Interpretation boundary

A positive result would establish survival **conditional on an independently constrained/simple countercarrier mode**. It would not justify claiming that arbitrary electron-hole pair transients can be uniquely decomposed from six channels at one RF frequency.

A negative result would strengthen the case for narrowing the manuscript to a unipolar/single-mobile-carrier observable.

The free-two-root failure itself should be retained as an identifiability warning, not hidden or tuned away.
