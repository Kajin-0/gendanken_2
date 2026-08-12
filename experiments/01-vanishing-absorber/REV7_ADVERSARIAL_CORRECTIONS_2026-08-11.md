# Rev. 7 adversarial-review correction record

## Governing rule

The referee report was treated as an adversarial attack list, not as authority. Each objection was checked independently against the Rev. 6 equations, the numerical model, and primary literature where the objection depended on external physics or scholarship. Changes below were made only where they improve the scientific accuracy of the paper.

## Disposition of the review

### 1. Prony / ESPRIT / matrix-pencil scholarship — ACCEPTED

The one- and two-exponential identities are classical finite-exponential algebra. Rev. 7 now cites de Prony (1795), Roy and Kailath (ESPRIT, 1989), and Hua and Sarkar (matrix pencil, 1990), and states explicitly that neither the geometric identity nor the Hankel/Casoratian minor is claimed as new.

The candidate contribution is narrowed to the combination:

```text
calibrated spectral generation depth
-> Shockley-Ramo terminal-current observable
-> spatial differencing
-> classical finite-exponential model-order tests
-> branch-controlled / branch-free RF physical root constraints.
```

### 2. Free HgCdTe force-partition parameter xi — ACCEPTED, BUT REPAIRED MORE STRONGLY THAN REQUESTED

Rev. 6 used xi=1 as the headline force normalization and only exposed xi as a sensitivity coordinate. A 2025 HgCdTe electron-affinity analysis provides a physically motivated 300 K relation

```math
chi(x)=5.32+0.45 x-E_g(x,300 K)  eV
```

and finds that very nearly two thirds of the graded bandgap change appears in the conduction band (J. Appl. Phys. 138, 165701 (2025), DOI 10.1063/5.0300709).

Rev. 7 therefore replaces xi=1 as the headline baseline with

```math
E_drive^grad(z)=|(dE_g/dx-0.45) dx/dz|.
```

For the worked x=0.55 -> 0.32 profile, the explicit local fraction

```math
xi_e=1-0.45/(dE_g/dx)
```

runs from about 0.666 to 0.695. The old constant-xi rows are retained only as sensitivity stresses.

The finite-width optical-kernel gradient-sensitive excess becomes:

```text
100 MHz  -0.0220167 deg
500 MHz  -0.1064448 deg
1 GHz    -0.1942321 deg
```

The abstract and all downstream resource numbers were updated consistently.

### 3. Auger recombination criticism — NARROWED, THEN TESTED

The review's claim that Auger recombination is intrinsically incompatible with a first-order kappa is too strong. A nonlinear microscopic recombination law can be linearized for a small AC perturbation around a specified operating point, producing a differential first-order recombination rate. The material-specific issue is whether that differential rate is spatially varying.

Near-room-temperature low-injection HgCdTe measurements report Auger-limited lifetimes of roughly 5-11 us for about 4-um-cutoff material (Semicond. Sci. Technol. 36, 055003 (2021), DOI 10.1088/1361-6641/abea6d).

Rev. 7 therefore adds a deliberately steep spatial recombination sensitivity profile, explicitly not claimed as an exact Auger law:

```math
tau_gr(z)=5 us exp[(E_g(z)-E_g(x=0.325))/(k_B T)].
```

This spans about 3.9 us to 0.89 s. With a transit-weighted matched homogeneous baseline, the change relative to the no-recombination gradient-sensitive phase is only

```text
100 MHz  3.8e-8 deg
500 MHz  1.8e-7 deg
1 GHz    3.5e-7 deg
```

for the stated conditional model. Thus measured low-injection microsecond-scale recombination is far too slow to compete with the present 0.1-1 GHz phase target. This does not establish that high-injection nonlinear Auger, depleted-device recombination, or every device architecture is negligible.

### 4. One-dimensional weighting-field criticism — REVIEWER PREMISE REJECTED, MODEL BOUNDARY SHARPENED

The claim that finite-electrode weighting nonuniformity is overwhelmingly lateral is not generally correct. Finite/pixelated electrodes can produce strong depth-dependent weighting potential (the small-pixel effect); multidimensional Shockley-Ramo calculations explicitly show this behavior. Rev. 7 cites J. D. Eskin et al., J. Appl. Phys. 85, 647-659 (1999), DOI 10.1063/1.369198.

The manuscript nevertheless makes the correct narrower limitation explicit: the linear E_w(z) theorem is a low-order axial observation surrogate along a carrier trajectory, not a generic finite-pixel electrostatic solution. Real finite electrodes require multidimensional electrostatics and can contain both axial and lateral structure.

### 5. Sequential statistics — PARTLY ACCEPTED

The hierarchy is now explicitly labeled near its introduction as structural model-selection logic, not a globally calibrated sequential hypothesis test. Per-rung significance numbers remain conditional. The existing later warning about selection-aware error control is retained.

No large multiple-testing theory section was added because the manuscript does not claim an experiment-wide family-wise false-positive probability.

### 6. Practical feasibility — CONCERN ACCEPTED, "FALSIFIABILITY VANISHES" CONCLUSION NOT ACCEPTED

Rev. 7 adds a concrete measurement architecture: one common RF reference, interleaved wavelength acquisition, optical-power/reference-photodiode monitoring, one coherent DUT receiver chain, repeated reference wavelengths, and calibration of the non-common high-curvature spectral residual rather than absolute delay.

The paper remains explicit that this is an architecture, not demonstrated feasibility. With the revised HgCdTe target, the 100 MHz current-step SNR requirement is about 90.9 dB and the independent irregular phase tolerance is about 1.88e-4 degree, corresponding to about 5.2 fs. Whether an experiment can demonstrate those residuals remains OPEN.

## Propagated Rev. 7 numerical changes

Using D=0.0232668 m^2/s and the electron-affinity-anchored path-harmonic drift scale V*=2.2220e4 m/s:

```text
conditioning optimum              5.85 GHz
K_D(100 MHz)                     33.95
K_D(500 MHz)                      7.57
K_D(1 GHz)                        4.75

weighting-mode best-case rank-two SNR:
100 MHz                          108.6 dB
500 MHz                           81.2 dB
1 GHz                             70.5 dB

five-color annihilation penalty:
100 MHz                           42.4 dB
500 MHz                           28.7 dB
1 GHz                             23.2 dB

3-sigma current-step resource:
100 MHz                           90.9 dB
250 MHz                           82.9 dB
500 MHz                           77.1 dB
1 GHz                             71.4 dB

nonaffine coordinate RMS:
100 MHz                           4.54 nm
500 MHz                           4.55 nm
1 GHz                             4.51 nm

irregular channel phase RMS:
100 MHz                           1.88e-4 deg (~5.23 fs)
500 MHz                           9.15e-4 deg (~5.08 fs)
1 GHz                             1.71e-3 deg (~4.74 fs)

1-D linear weighting-field change for <10% target:
100 MHz                           0.757%
500 MHz                           0.881%
1 GHz                             1.961%

same-optics homogeneous phase / excess:
100 MHz                           17.3%
500 MHz                           17.9%
1 GHz                             19.8%
```

The hot-fraction nuisance thresholds were renormalized to the stronger 100 MHz target: about 0.46-1.5 percentage points for the same generic two-state stresses.

## Independent numerical cross-check

The sparse finite-difference boundary-value implementation was reconstructed with the new electron-affinity force. A separate adaptive DOP853 shooting construction, using the same physical equations but a different numerical solution strategy, reproduces the gradient-sensitive excess to better than 1e-5 degree at 100 MHz, 500 MHz, and 1 GHz.

This is numerical cross-verification of the specified conditional model, not physical validation of HgCdTe at that angular precision.

Regression file:

```text
numerics/rev7_review_regression.py
```

## Editorial corrections

- Internal draft header changed from Revision 5 to Revision 7.
- The dangling "-0.01254 deg quoted above" cross-reference was removed; the new point-source finite-diffusion value is stated directly.
- Xu et al. (2024) is now cited in the body with a strict priority caveat instead of remaining orphaned.
- "Stress" is defined on first use as a sensitivity/test scenario, not mechanical/thermal stress.
- "Exact minor identity" language is explicitly tied to classical finite-exponential algebra.

## Remaining open blockers

1. Exact full-text audit of the closest 2024 graded-HgCdTe laser-measurement paper before any submission-level priority claim.
2. Demonstrated calibration feasibility for the residual spectral phase/depth and modeled-baseline covariance requirements.
3. One self-consistent combined-physics synthetic detector challenge analyzed blindly through the hierarchy.

The core four-color theorem, branch corrections, rank-two hierarchy, singular weighting-field theorem, hot-state branch, unequal-spacing treatment, and preservation spine were not reopened because this review did not expose a defect in them.
