# Gedanken 2

First-principles thought experiments in photodetector physics.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, counterexamples, observable corrections, numerical failures, and prior-art collisions are retained because they define the actual result.

## Active experiment

`experiments/01-vanishing-absorber/`

The project began with a broad question about whether an ideal photodetector could be made arbitrarily small, fast, sensitive, and perfectly absorbing. That route did not survive. The active result is now much narrower and experimentally testable:

> **Can wavelength-dependent generation depth be used as a calibrated internal spatial coordinate that forces simple photocarrier transport models to satisfy exact closure relations across color and RF frequency?**

## Current paper

The current integrated manuscript source is:

- `experiments/01-vanishing-absorber/MANUSCRIPT_REV3.tex`

The older `MANUSCRIPT_DRAFT.tex` is retained as provenance and should not be treated as the latest paper state.

Rev. 3 was locally compiled and visually checked as a 12-page PDF on 2026-08-11. The source is self-contained and includes its verified bibliography.

## Core hierarchy

### Four colors: one-mode null

For four equally spaced calibrated internal source coordinates in the homogeneous one-carrier planar Shockley-Ramo model,

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

The raw terminal current is affine-exponential in source depth. First differences remove the depth-independent observation term and isolate one spatial propagation multiplier.

### DC + RF: identify, then falsify

Uniform drift-diffusion-recombination obeys

```math
D\gamma^2+w\gamma=\kappa+s.
```

DC plus one nonzero RF point determine `D`, `w`, and `kappa` within the model. Every later RF frequency introduces no new transport coefficient and becomes a falsification measurement.

The inverse is identifiable whenever its determinant is nonzero, but practical conditioning is stricter. With `delta g=u+iv`,

```math
\boxed{\Delta=-v(u^2+v^2).}
```

The balanced inversion scale satisfies

```math
\boxed{D\omega_*/V_*^2=\sqrt3},
\qquad
V_*=\sqrt{w^2+4D\kappa}.
```

For the present illustrative HgCdTe scale this lies near 14.1 GHz, so 100 MHz-1 GHz is substantially better suited to closure/timing tests than precision diffusion extraction.

### Six colors: model order before mechanism

If four colors fail, six colors test whether two spatial modes are actually resolved. For

```math
d_m=a q_1^m+b q_2^m,
```

```math
\boxed{W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.}
```

A second-mode Hankel witness must be statistically significant before roots are interpreted.

Finite scalar boundaries then obey the additional RF constraint

```math
\boxed{r_++r_-=-w/D},
```

which must be real and RF-independent.

## Observation-field hardening

Low-order one-dimensional observation nonuniformity can be either identified as extra spatial rank or annihilated with higher spatial differences.

If

```math
J(z)=P_p(z)+B e^{rz},
```

then

```math
Y_m=\Delta^{p+1}J_m
```

is geometric and the required number of colors is

```math
\boxed{N_{\rm color}=p+4.}
```

A linear weighting-field trend therefore admits an exact five-color second-difference null. This is not free: relative to the four-color test, the low-RF raw-current SNR cost scales approximately as

```math
\boxed{\mathrm{cost}_5/\mathrm{cost}_4\sim1.87|rh|^{-1}.}
```

## Hot-carrier initialization

A minimal hot-to-cold thermalization model has

```math
J_h(d,s)=A+B_c e^{-sd/v_c}+B_h e^{-(s+\rho)d/v_h},
```

with thermalization memory length

```math
\boxed{\ell_h=v_h\tau_h.}
```

If the same hot fraction is initialized at every wavelength, finite thermalization is exactly a rank-two problem and belongs on the six-color branch. The dangerous effect is wavelength-dependent initialization.

For the current HgCdTe quartet the generation-weighted mean excess energy varies by only about 0.125 meV peak-to-peak. In a deliberately strong long-memory stress, about 0.25-0.8 percentage-point variation in initial hot fraction across the quartet is enough to create a 100-MHz false signal equal to 10% of the present transport-gradient target.

## Conditional HgCdTe worked example

Current one-dimensional graded-transport closure excess:

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

These are conditional theory predictions, not calibrated forecasts for an existing detector.

The corresponding approximate 3-sigma current-step amplitude SNR requirements are:

```text
100 MHz -> 96.1 dB
500 MHz -> 82.3 dB
1 GHz   -> 76.7 dB
```

## New 2-D geometry hardening result

The current adversarial geometry study is:

- `experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md`
- `experiments/01-vanishing-absorber/numerics/realistic_geometry_closure_stress.py`

It solves separate two-dimensional physical and Shockley-Ramo weighting potentials for finite top electrodes, follows saturated-drift trajectories, integrates the exact discrete Ramo weighting-potential increments, and applies the four-/five-/six-color diagnostics without fitting away the geometry first.

For a 75%-width top contact plus a controlled 3 um depletion-like Poisson curvature, the geometry/depletion four-color phase excess is approximately:

```text
100 MHz -> -0.008841 deg = 0.738 x current 1-D gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

So the four-color residual is **not geometry-proof**.

However, the same 100-MHz geometry produces a statistically resolvable second spatial mode at about 84.6 dB current-step amplitude SNR, roughly 11.5 dB before the 96.1 dB SNR required for the current gradient claim. The fitted effective roots also fail the homogeneous finite-boundary RF root law.

The present defensible hierarchy is therefore:

```text
four colors -> detect failure
six colors  -> classify spatial model order
RF roots    -> reject premature mechanism assignment
```

The exact five-color annihilator remains appropriate for a known approximately affine one-dimensional observation trend. It is not a universal cure for curved multidimensional weighting/depletion geometry.

## Priority boundary

Do not claim novelty for Shockley-Ramo signal formation, wavelength-dependent photodiode RF response, optoelectronic chromatic dispersion, photodetector Hankel identification, drift-diffusion inversion, or graded-HgCdTe high-speed response.

The candidate distinct application is the complete combination:

```text
calibrated spectral internal position
-> Ramo-aware spatial differencing
-> minimal color-count model-order tests
-> RF root-law falsification
```

**Status: CANDIDATE DISTINCT APPLICATION - PRIORITY UNPROVEN.**

A negative literature search is not evidence of novelty. The close 2024 graded-HgCdTe laser-measurement paper is bibliographically confirmed, but its full technical content has not yet been recovered in the current audit.

## Next decisive work

Do not expand the abstract closure hierarchy without a specific reviewer-driven need. The next high-value scientific step is a self-consistent two-dimensional semiconductor Poisson/drift-diffusion calculation for one plausible detector geometry, including diffusion, with the resulting synthetic measurement analyzed blind by the same hierarchy.

Before submission, the remaining high-value work is therefore:

1. self-consistent realistic-device geometry stress;
2. deeper primary-source priority audit, especially the close 2024 graded-HgCdTe paper;
3. final manuscript compression and reproducibility QA.
