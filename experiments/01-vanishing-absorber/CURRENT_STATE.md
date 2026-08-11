# Current State - Experiment 01: The Vanishing Absorber

**Date:** 2026-08-11  
**Status:** **working Rev. 3 theory manuscript + adversarial hardening**. The strongest surviving result is a Shockley-Ramo-aware spectral-depth closure hierarchy for falsifying simple photocarrier transport models. HgCdTe is the leading worked example. **Priority remains unproven.**

## 1. Authoritative current paper state

Use:

- `MANUSCRIPT_REV3.tex` - current integrated paper source
- `REALISTIC_GEOMETRY_CLOSURE_STRESS.md` - current 2-D geometry hardening result
- `numerics/realistic_geometry_closure_stress.py` - executable geometry regression

`MANUSCRIPT_DRAFT.tex` is retained as provenance but is no longer the latest integrated manuscript.

Rev. 3 was compiled locally on 2026-08-11 as a 12-page PDF and visually checked page-by-page after fixing the only overfull line. The current Rev. 3 source is self-contained and includes its bibliography.

## 2. Current paper question

The active question is not unrestricted transport tomography.

It is:

> **Can wavelength-dependent generation depth be calibrated as an internal spatial coordinate that makes simple photocarrier transport hypotheses overdetermined across color and RF frequency?**

The paper is organized as a falsification hierarchy rather than a general inverse solver.

## 3. Lowest rung: four-color one-mode closure

For the homogeneous one-carrier planar Shockley-Ramo observable,

```math
J_m=A+Bq^m,
```

so first differences are geometric and four equally spaced internal source coordinates obey

```math
\boxed{(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).}
```

Three colors estimate one spatial multiplier. The fourth is a parameter-free null.

Common complex gain and additive offset cancel. A rigidly translated finite generation kernel also preserves the closure exactly.

Known unequal source positions are still overdetermined; equal spacing is a convenience, not a fundamental requirement. The dangerous quantity is uncertainty in the calibrated source coordinates.

## 4. DC + RF transport law

Uniform drift-diffusion-recombination obeys

```math
D\gamma^2+w\gamma=\kappa+s.
```

DC plus one nonzero RF point determine `D`, `w`, and `kappa` within the model. Every later RF frequency must reproduce the same coefficients and is therefore a falsification point.

The inversion determinant admits the exact form

```math
\boxed{\Delta=-v(u^2+v^2)},
```

for

```math
\delta g=\gamma(i\omega)-\gamma(0)=u+iv.
```

Therefore nonzero determinant is not enough for a useful experiment. The intrinsic conditioning parameter is `D omega / V_*^2`, with

```math
V_*=\sqrt{w^2+4D\kappa}
```

and balanced point

```math
\boxed{D\omega_*/V_*^2=\sqrt3}.
```

For the current illustrative HgCdTe scale this lies near 14.1 GHz. The current 100 MHz-1 GHz range is useful for closure/timing measurements but intrinsically poor for precision diffusion extraction.

## 5. Second rung: six-color rank-two closure

If the four-color law fails, do not assign a mechanism immediately.

For five first differences from six colors,

```math
d_m=a q_1^m+b q_2^m,
```

adjacent Hankel minors obey

```math
\boxed{W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.}
```

A second mode must be statistically resolved before roots are interpreted.

For a homogeneous scalar finite-boundary drift-diffusion mechanism,

```math
\boxed{r_++r_-=-w/D}
```

must be real and RF-independent. Root-law failure therefore provides a further falsification rung after model-order detection.

Interpretation rule:

```text
four-color failure + unresolved rank-two witness
-> mechanism unresolved at current SNR
```

not

```text
four-color failure -> therefore velocity gradient.
```

## 6. Observation-field hierarchy

A low-order one-dimensional observation forcing does not necessarily have to be engineered away.

If

```math
J(z)=P_p(z)+B e^{rz},
```

with `P_p` a polynomial of degree at most `p`, then

```math
Y_m=\Delta^{p+1}J_m
```

is exactly geometric, so

```math
\boxed{Y_1^2=Y_0Y_2},
\qquad
\boxed{N_{color}=p+4}.
```

Thus:

```text
constant forcing  -> first differences  -> 4 colors
linear forcing    -> second differences -> 5 colors
quadratic forcing -> third differences  -> 6 colors
```

For a linear weighting field,

```math
\boxed{(\Delta^2J_1)^2=(\Delta^2J_0)(\Delta^2J_2)}
```

is exact under the homogeneous one-dimensional hypothesis.

Alternatively, a linear observation trend can be identified on the ordinary rank-two branch as a root `q_weight=1`.

The statistical cost is substantial. The raw-noise coefficients progress as

```text
sqrt(20), sqrt(70), sqrt(252), ...
```

and the five-color versus four-color low-RF SNR cost scales approximately as

```math
\boxed{\mathrm{cost}_5/\mathrm{cost}_4\sim1.87|rh|^{-1}}.
```

## 7. Hot-carrier initialization

A minimal hot-to-cold model gives

```math
J_h(d,s)=A+B_c e^{-sd/v_c}+B_h e^{-(s+\rho)d/v_h},
```

with

```math
\boxed{\ell_h=v_h\tau_h}.
```

If the same hot fraction is initialized at each wavelength, finite thermalization produces exactly two spatial exponentials and belongs on the ordinary six-color rank-two branch.

The dangerous effect is wavelength-dependent initialization.

For the present HgCdTe quartet, the generation-weighted mean total excess energy varies by only about

```text
0.125 meV peak-to-peak.
```

In a deliberately strong long-memory two-state stress, approximately

```text
0.25-0.8 percentage-point
```

variation in hot fraction across the quartet creates a 100-MHz false signal equal to 10% of the present gradient-sensitive target.

These are sensitivity numbers, not measurements of HgCdTe hot-carrier populations.

## 8. Conditional HgCdTe one-dimensional target

Current graded-transport gradient-sensitive closure phase:

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

The point-source low-RF theorem gives approximately `-0.01254 deg` at 100 MHz for the same velocity profile.

The stochastic boundary-value calculation and an independent adaptive shooting implementation agree to approximately `10^-6 degree` or better at the reported RF points.

Approximate `3 sigma` current-step amplitude SNR requirements:

```text
100 MHz -> 96.1 dB
500 MHz -> 82.3 dB
1 GHz   -> 76.7 dB
```

These are **CONDITIONAL theory predictions**, not calibrated forecasts for a named detector.

## 9. New 2-D finite-electrode/depletion falsification stress

The previous major open objection was whether a realistic weighting potential and depletion region could generate a false transport-gradient phase.

The new calculation solves:

```text
2-D physical Poisson potential
+
separate 2-D Shockley-Ramo weighting potential
+
saturated deterministic carrier trajectories
+
exact discrete Ramo weighting-potential increments
+
six optical source-depth channels
```

and then applies the existing hierarchy without correcting the synthetic data first.

### Internal check

All sampled refined trajectories collect successfully, and at DC

```math
H(0|r_0)=1-\phi_w(r_0)
```

is satisfied to numerical machine precision (`<10^-12` in the executable assertions).

### Four-color confound

For a 75%-width top contact plus a controlled 3 um depletion-like Poisson curvature, the excess over the planar same-optics baseline is

```text
100 MHz -> -0.008841 deg = 0.738 x current gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

Therefore:

```text
four-color phase residual alone is not geometry-specific.
```

### Model-order rescue

The same six-color response is not rank one but is close to rank two over the tested spectral window.

For the refined 75%-contact depletion case:

```text
RF        sigma2/sigma1   sigma3/sigma2
DC        4.771e-4        8.202e-3
100 MHz   4.804e-4        8.611e-3
500 MHz   5.635e-4        1.352e-2
1 GHz     8.581e-4        1.531e-2
```

At 100 MHz the exact linearized first-minor noise law gives a `3 sigma` second-mode threshold of approximately

```text
84.6 dB current-step amplitude SNR.
```

The current gradient-specific claim requires about `96.1 dB`, so this representative geometry mode becomes statistically resolvable about

```text
11.5 dB earlier.
```

For the 50%-contact depletion stress the corresponding second-mode threshold is about `71.5 dB`, giving approximately `24.6 dB` margin.

This is the strongest new geometry result:

> **In the tested geometries, the confound becomes visible as higher spatial model order before the SNR needed for the present HgCdTe gradient claim is reached.**

### RF root-law rejection

For the refined 75%-contact depletion stress, the fitted effective root-sum imaginary part is approximately

```text
DC       -> 0.000 1/um
100 MHz  -> +0.141 1/um
500 MHz  -> +0.568 1/um
1 GHz    -> +0.680 1/um
```

so the geometry-generated second mode does not satisfy the homogeneous finite-boundary requirement that the root sum be real and RF-independent.

### Five-color limit

The five-color second-difference null does **not** annihilate the curved multidimensional geometry. For the 75%-contact depletion case its phase is approximately

```text
100 MHz -> -0.370 deg
500 MHz -> -0.089 deg
1 GHz   -> -0.096 deg
```

Therefore the five-color theorem is a targeted tool for known low-order one-dimensional observation trends, not a universal cure for finite-pixel geometry.

### Numerical refinement

The key 75%-contact depletion four-color phase changes by about 5% when simultaneously refining the electrostatic grid, source sampling, and trajectory step.

This is sufficient for the current classification result but not for percent-level device prediction.

## 10. Current scientific claim boundary

The defensible hierarchy is now:

```text
four colors -> detect one-mode failure
six colors  -> establish whether a second spatial mode is resolved
RF roots    -> test whether that mode matches an ordinary physical mechanism
```

Only after optical source-state variation, weighting/depletion geometry, and lower-order model-order explanations are controlled should a residual be interpreted through the local slowness-gradient theorem.

The hierarchy survived the first realistic multidimensional attack, but in a weaker and more defensible form: **not because geometry is negligible, but because representative geometry confounds become visible at a lower inference rung.**

## 11. Priority boundary

Do not claim novelty for:

```text
Shockley-Ramo theory
wavelength-dependent absorption depth
wavelength-dependent photodiode phase/bandwidth
optoelectronic chromatic dispersion
multi-frequency photodiode characterization
Hankel/Prony model identification
drift-diffusion propagation or inversion
graded-HgCdTe high-speed response
```

Candidate distinct application:

```text
calibrated spectral internal position
-> Shockley-Ramo-aware spatial differencing
-> minimal color-count model-order testing
-> RF root-law falsification of ordinary transport mechanisms
```

**Status: CANDIDATE DISTINCT APPLICATION - PRIORITY UNPROVEN.**

The narrow literature audit has not recovered the full combined construction. This is a negative search, not novelty evidence. The close 2024 graded-HgCdTe laser-measurement paper is bibliographically confirmed, but its full technical content remains unresolved in the present audit.

## 12. Next decisive work

Do not extend the abstract difference hierarchy unless a specific reviewer objection requires it.

Highest-value remaining tasks:

1. build one self-consistent 2-D semiconductor Poisson/drift-diffusion detector stress including diffusion and analyze its synthetic measurement blind with the same hierarchy;
2. deepen the primary-source priority audit, especially the close 2024 graded-HgCdTe paper;
3. perform final Rev. 3 manuscript compression, cross-reference cleanup, and reproducibility QA before journal selection.
