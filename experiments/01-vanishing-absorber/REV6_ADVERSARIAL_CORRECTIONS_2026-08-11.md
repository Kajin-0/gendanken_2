# Revision 6 adversarial corrections — 2026-08-11

## Status

Revision 6 is a surgical response to the Revision 5 hostile review. The review no longer identifies a fatal defect in the central four-color / rank-two hierarchy. The remaining attack surface is post-detection conditioning, physical interpretation of the one-dimensional weighting-field stress, the conditional normalization of the HgCdTe force model, adjacent optoelectronic-chromatic-dispersion prior art, and combined-physics feasibility.

No broad rewrite was performed.

## 1. Rank-two detection is separated from rank-two parameter resolution

Revision 5 already required the Hankel witness to be statistically resolved before fitting two roots. Revision 6 adds the next conditioning rung explicitly.

For

```math
P=q_1q_2=W_1/W_0,
```

the first-order perturbation is

```math
\delta P=(\delta W_1-P\delta W_0)/W_0,
```

with proper-complex variance

```math
\sigma_P^2 =
[\sigma_{W_1}^2+|P|^2\sigma_{W_0}^2
-2\Re(P^*\operatorname{Cov}(W_1,W_0))]/|W_0|^2.
```

The shared-minor covariance is retained because adjacent Hankel minors use overlapping current differences.

In the deliberately optimistic independent equal-significance limit,

```math
\sigma_P/|P| \simeq \sqrt2/Z.
```

Therefore:

- `Z=3` on both minors -> about **47.1%** relative product uncertainty;
- about **14.1 sigma** per minor is required for a 10% product measurement in that simplified limit.

The recurrence sum is also written explicitly,

```math
S=q_1+q_2=(d_2+Pd_0)/d_1,
```

with its first-order differential. Individual roots inherit additional ill-conditioning as `S^2-4P -> 0`.

The hierarchy is now stated as:

```text
rank-two detection
-> rank-two parameter resolution
-> physical root-law discrimination.
```

## 2. Branch immunity is distinguished from statistical robustness

The branch-free finite-boundary multiplier test

```math
q_+q_- \in R_{>0},  RF independent
```

is retained. Revision 6 now states that this algebraic branch immunity does not make the estimator statistically robust when the Hankel minors are small. The new product covariance governs whether the phase and RF invariance can actually be tested.

## 3. The 1-D weighting-field model is explicitly an observation surrogate

Section 6 now states directly that prescribed `E_w(z)` is an **effective one-dimensional observation-operator stress**.

For a homogeneous dielectric between ideal infinite planar electrodes, the source-free weighting potential is linear and the weighting field is constant. Real finite-electrode nonuniformity generally enters through multidimensional fringing fields and lateral trajectories.

The polynomial annihilation theorem remains exact for its stated one-dimensional surrogate; it is not presented as a generic finite-pixel electrostatic solution.

## 4. HgCdTe band-edge-force normalization is exposed with xi

Revision 6 introduces

```math
E_drive^grad(z;xi)
= xi |(dE_g/dx)(dx/dz)|,
0 < xi <= 1.
```

The existing reported calculation is explicitly the `xi=1` baseline. `xi` is a sensitivity coordinate for the fraction of the total bandgap gradient assigned to the carrier-driving band edge; it is **not** claimed to be a known HgCdTe band-offset fraction.

A point-source finite-diffusion 100-MHz sweep using the same backward equation and entrance match gives:

| xi | v(zc) (m/s) | point-source phase |
|---:|---:|---:|
| 0.3 | 8.379e3 | -0.00740857 deg |
| 0.6 | 1.9698e4 | -0.01822428 deg |
| 1.0 | 3.4757e4 | -0.01245830 deg |

The nonmonotonicity is not hidden: scaling the band-edge force changes its competition with the fixed density-of-states term and changes the finite-frequency closure. The published finite-width `-0.01198 deg` target is therefore explicitly conditional on `xi=1`.

The nuisance/resource table is also labeled as normalized to the baseline `xi=1` stress rather than a generic HgCdTe specification.

## 5. OED prior-art boundary broadened

Two adjacent primary Optica papers are added:

- E. Liokumovitch et al., *Optics Letters* 46, 4061-4064 (2021), DOI `10.1364/OL.435159` — Ge PN OED used for wavelength monitoring and FBG interrogation.
- A. Dutta et al., *Optics Letters* 49, 2057-2060 (2024), DOI `10.1364/OL.519164` — large, bias-tunable OED in Ge PIN photodiodes.

The manuscript now states the distinction more directly: adjacent OED work uses spectral dependence of RF phase/amplitude as a sensing observable; this manuscript treats calibrated spectral channels as an **internal spatial sequence** and imposes algebraic color-count model-order and cross-RF transport-law nulls.

This is a boundary statement, not a novelty claim.

## 6. Two-carrier and hierarchical-statistics refinements

The two-carrier subsection now states that carrier labeling is meaningful only after both modes are statistically resolved and continuously tracked; a DC root sign does not rescue an unresolved mode.

The covariance chi-square statistic is explicitly described as a **per-rung / conditional** test. A complete experimental implementation that selects model order and then tests roots using the same noisy data must control sequential-selection error.

## 7. Combined-physics detector challenge remains future work

Revision 6 does not add another large transport section. Instead the Discussion now names the decisive next validation:

> one self-consistent combined-physics synthetic detector, analyzed blindly through the same hierarchy.

This is required before strong device-physics / experimental feasibility claims, because several ordinary departures can coexist and raise the observable rank beyond six colors.

## Numerical regression

`numerics/rev6_review_regression.py` checks:

- the `sqrt(2)/Z` post-detection product-conditioning scale;
- the 47.14% value at `Z=3`;
- the 14.14 significance scale for 10% simplified product precision;
- the `xi=0.3, 0.6, 1.0` midpoint drift values;
- the three 100-MHz point-source finite-diffusion closure phases with an independent RK4 shooting implementation.

## Priority status

Priority remains **OPEN / UNPROVEN**. Adding adjacent OED papers narrows the literature boundary but does not establish novelty. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before submission-level priority language.
