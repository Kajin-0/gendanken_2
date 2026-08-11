# Manuscript Revision 2 — Adversarial Review Integration

**Date:** 2026-08-11  
**Status:** manuscript-level scientific revision; priority remains unresolved

This revision integrates the strongest objections from the external adversarial review into the actual paper architecture.

## 1. DC + RF inversion conditioning is now explicit

The manuscript no longer treats `Delta != 0` as an adequate practical condition.

With

```math
\delta g=\gamma(i\omega)-\gamma(0)=u+iv,
```

```math
\boxed{\Delta=-v(u^2+v^2).}
```

The inverse is rewritten through

```math
V_*=\sqrt{w^2+4D\kappa}
```

with exact intrinsic condition numbers and balanced point

```math
\boxed{D\omega_*/V_*^2=\sqrt3.}
```

For the current illustrative HgCdTe scale this lies near `14.1 GHz`; the current 100 MHz--1 GHz range is useful for closure/timing tests but intrinsically much poorer for precision diffusion extraction.

## 2. Nonuniform weighting field is promoted from a limitation to a testable observation mode

For arbitrary one-dimensional `E_w(z)`,

```math
\boxed{
D J''+wJ'-(\kappa+s)J
=-[wE_w+D E_w'].
}
```

A locally linear weighting field gives

```math
\Delta J_m=C+Bq^m,
```

so the simplest weighting-field nonuniformity is rank two with one exact RF-independent multiplier

```math
\boxed{q_{weight}=1.}
```

The paper also states the important degeneracy:

```text
low-RF linear weighting gradient
and
low-RF transport slowness gradient
```

are both phase-like and `O(omega)`, so RF scaling alone cannot distinguish them.

The current quartet stress requires approximately `<0.64-0.83%` unmodeled linear weighting-field variation across 1.5 um to keep this term below 10% of the present gradient-sensitive phase.

## 3. Equal spectral-depth spacing is no longer presented as fundamental

For known arbitrary source positions, the single-mode model remains overdetermined.

The first three positions determine one complex spatial exponent through the unequal-step first-difference ratio; the fourth remains a falsification point.

Therefore

```text
known nonlinear wavelength-to-depth map
```

is not itself a false-positive source.

The dangerous quantity is uncertainty in the inferred source coordinates.

## 4. Hot->cold thermalization is now an ordinary rank-two branch

For a hot carrier moving at `v_h` and relaxing at rate `rho` to a cold carrier moving at `v_c`,

```math
J_h(d,s)
=A+B_c e^{-sd/v_c}+B_h e^{-(s+\rho)d/v_h}.
```

The thermalization memory length is

```math
\boxed{\ell_h=v_h\tau_h.}
```

If the same hot fraction is initialized at every wavelength, the first-difference sequence is exactly rank two and belongs on the six-color branch.

The distinct source-state systematic is wavelength-dependent initialization.

## 5. Excess-energy invariance now has a precise manuscript role

The ideal graded-gap excess-energy theorem is no longer described as if it were a necessary assumption for the entire method.

Its role is narrower and stronger:

> if initial carrier-state probabilities depend only on total local excess energy, wavelength-invariant excess-energy generation preserves the fixed spatial model order.

For the current HgCdTe quartet, generation-weighted mean total excess energy varies by only about `0.125 meV` peak-to-peak.

In a generic long-memory two-state stress, hot-fraction changes of order `0.25-0.8 percentage points` across the quartet would produce a 100-MHz source-state error equal to 10% of the current gradient-sensitive target.

These are sensitivity numbers, not HgCdTe thermalization measurements.

## 6. Interpretation rule strengthened

A second mode can produce a detectable four-color failure before its six-color Hankel minor is significant enough for reliable mode identification.

The paper therefore now requires

```text
four-color failure + unresolved second-mode witness
-> mechanism unresolved at current SNR
```

and explicitly forbids

```text
four-color failure -> therefore velocity gradient.
```

## 7. Revised user-facing manuscript

A revised 15-page PDF/LaTeX build was generated after these scientific changes and visually checked page-by-page.

The repository theorem sources corresponding to this revision are:

- `DC_RF_INVERSION_CONDITIONING_THEOREM.md`
- `NONUNIFORM_WEIGHTING_FIELD_CLOSURE.md`
- `ARBITRARY_SPACING_AND_DEPTH_CALIBRATION.md`
- `HOT_CARRIER_TWO_STATE_CLOSURE.md`
- `PAPER_CLAIM_LEDGER_REVIEW_ADDENDUM_2026-08-11.md`
- `PAPER_CLAIM_LEDGER_HOT_STATE_ADDENDUM_2026-08-11.md`

and their associated numerical regression scripts.

## 8. Current scientific disposition

The strongest remaining risks are now narrower:

1. more realistic multi-dimensional/depletion weighting-potential structure beyond the linear 1-D stress;
2. material-specific microscopic mapping from the small residual HgCdTe excess-energy mismatch to actual nonequilibrium carrier-state populations;
3. exact prior-art priority for the combined spectral-depth/Ramo-aware closure protocol.

No broad new theorem branch should be opened unless one of these manuscript risks requires it.
