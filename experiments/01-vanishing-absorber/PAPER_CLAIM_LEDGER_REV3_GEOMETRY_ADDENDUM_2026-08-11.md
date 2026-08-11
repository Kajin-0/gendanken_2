# Paper Claim Ledger Addendum - Rev. 3 Geometry Hardening

**Date:** 2026-08-11  
**Status:** claim-boundary update after two-dimensional finite-electrode/depletion stress

This addendum records the claim changes forced by `REALISTIC_GEOMETRY_CLOSURE_STRESS.md` and `numerics/realistic_geometry_closure_stress.py`.

## 1. Claim: four-color phase residual is geometry-proof

**Status: INVALIDATED GENERALIZATION.**

A finite top electrode plus a controlled depletion-like physical-field curvature can create a four-color phase residual of the same order as the current one-dimensional HgCdTe transport-gradient target.

For the refined 75%-contact + 3 um depletion stress, excess over the planar same-optics baseline is approximately:

```text
100 MHz -> -0.008841 deg = 0.738 x current gradient target
500 MHz -> -0.045827 deg = 0.780 x target
1 GHz   -> -0.095513 deg = 0.865 x target
```

Therefore a nonzero four-color phase cannot be assigned to a transport gradient without controlling geometry/model order.

## 2. Claim: the closure hierarchy remains useful under the tested 2-D geometry

**Status: CHECKED / CONDITIONAL.**

The same geometry response is not rank one. Over the six-channel depth window it is close to rank two:

```text
75% contact + depletion
RF        sigma2/sigma1   sigma3/sigma2
DC        4.771e-4        8.202e-3
100 MHz   4.804e-4        8.611e-3
500 MHz   5.635e-4        1.352e-2
1 GHz     8.581e-4        1.531e-2
```

The geometry confound therefore tends to announce itself as an additional spatial mode rather than remain hidden as a clean one-mode gradient in this tested family.

This is not a theorem for arbitrary device geometries.

## 3. Claim: the second geometry mode is visible before a gradient-specific inference is justified

**Status: CHECKED / CONDITIONAL for the tested geometry family.**

Using the exact linearized noise law for the first Hankel minor, the 100-MHz `3 sigma` second-mode threshold is approximately:

```text
75% contact + depletion -> 84.6 dB current-step amplitude SNR
50% contact + depletion -> 71.5 dB current-step amplitude SNR
```

The current one-dimensional HgCdTe gradient claim requires approximately `96.1 dB` at 100 MHz.

Thus the representative geometry mode becomes statistically resolvable about:

```text
75% contact -> 11.5 dB before gradient claim threshold
50% contact -> 24.6 dB before gradient claim threshold
```

This supports the stronger interpretation rule:

```text
high-SNR four-color residual
without a model-order check
is insufficient for a gradient-specific claim.
```

## 4. Claim: geometry-generated rank two can be mistaken for a homogeneous finite boundary

**Status: REJECTED in the tested 75%-contact depletion stress.**

For a homogeneous scalar finite-boundary mechanism,

```math
r_1+r_2=-w/D
```

must be real and RF-independent.

The fitted effective root-sum imaginary part for the 75%-contact depletion geometry is approximately:

```text
DC       -> 0.000 1/um
100 MHz  -> +0.141 1/um
500 MHz  -> +0.568 1/um
1 GHz    -> +0.680 1/um
```

Therefore the geometry-generated second mode fails the next ordinary finite-boundary RF root-law test.

## 5. Claim: five-color polynomial observation annihilation removes arbitrary geometry

**Status: INVALIDATED GENERALIZATION.**

The theorem remains exact for one-dimensional polynomial observation forcing,

```math
J(z)=P_p(z)+B e^{rz},
```

but not for a curved two-dimensional weighting potential with bent carrier trajectories.

For the 75%-contact depletion stress, the five-color second-difference phase closure is approximately:

```text
100 MHz -> -0.370 deg
500 MHz -> -0.089 deg
1 GHz   -> -0.096 deg
```

Therefore:

```text
known low-order 1-D observation trend
-> higher-difference annihilation is legitimate;

unknown curved/multidimensional geometry
-> use model-order + RF-root tests or explicit electrostatic modeling.
```

## 6. Numerical reliability claim

**Status: CHECKED for classification, not precision device prediction.**

The trajectory implementation satisfies the DC Ramo telescoping identity to machine precision in the refined runs and collects all sampled trajectories.

Simultaneous refinement from

```text
81 x 61 electrostatic grid
9 lateral source points
31 depth trajectory points
0.035 um step
```

to

```text
121 x 91 electrostatic grid
13 lateral source points
41 depth trajectory points
0.020 um step
```

changes the key 75%-contact depletion four-color phase by approximately 5% across 100 MHz-1 GHz.

This is sufficient for the present model-order/confound classification but not for percent-level device-specific prediction.

## 7. Revised paper-level interpretation

The defensible hierarchy is now:

```text
four colors -> detect one-mode failure
six colors  -> determine whether a second spatial mode is resolved
RF roots    -> test whether that mode matches an ordinary mechanism
```

Only after source-state variation, weighting/depletion geometry, and lower-order model-order explanations are controlled should the local slowness-gradient theorem be used for mechanism-specific interpretation.

## 8. Remaining open geometry risk

**Status: OPEN.**

The current 2-D calculation is deterministic high-Peclet transport. It does not include self-consistent semiconductor carrier densities, lateral/longitudinal diffusion, electron-hole coupling, trapping, or contact transfer kinetics.

The next submission-relevant falsification stress should therefore use one plausible self-consistent 2-D Poisson/drift-diffusion detector structure and analyze the resulting synthetic measurement blind with the same hierarchy.
