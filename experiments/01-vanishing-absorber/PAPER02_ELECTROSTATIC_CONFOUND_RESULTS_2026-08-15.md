# Paper 02 electrostatic-confound results

**Date:** 2026-08-15  
**Status:** **CHECKED in conditional model / PRIORITY UNPROVEN**  
**Supersedes the geometry-only interpretation of the initial Paper-02 stress.**

## Executive result

The original finite-electrode stress suggested a possible separate paper about multidimensional Shockley-Ramo geometry masquerading as a material-transport gradient.

The expanded calculations show that this framing is too narrow.

A **perfectly planar, full-width contact** with a deterministic depletion/space-charge field already creates the stronger hidden confound. It can

1. produce a spectral-depth phase signature comparable to the reference microscopic transport-gradient signal;
2. remain extremely close to the one-mode channel manifold;
3. survive calibrated finite-optical-kernel one-mode fitting;
4. return a positive homogeneous diffusion coefficient even though the simulation contains **no microscopic diffusion**;
5. satisfy the wrong homogeneous drift-diffusion RF law to sub-percent residual through 1 GHz for the current parameter point.

The active Paper-02 question is therefore now:

> **When can device electrostatics and Shockley-Ramo path structure be distinguished from microscopic material transport in spectral-depth RF measurements?**

Finite-electrode geometry remains important, but it is now one member of the nuisance family rather than the central mechanism.

---

## 1. Numerical model

The stress model is intentionally conditional rather than calibrated.

Common parameters:

```text
detector lateral width        16 um
total bias                    0.30 V
mobility parameter            0.90 m^2/(V s)
velocity saturation           6.0e4 m/s
spectral source means         2.0 to 4.5 um in 0.5 um steps
RF points in initial sweep    0, 100, 500, 1000 MHz
beam sigma                    2.0 um
```

Fine numerical resolution:

```text
field mesh                    121 x 91
lateral source quadrature     13
source-depth quadrature       41
trajectory step               0.020 um
```

The 2-D solver computes separately:

- physical electrostatic potential;
- Shockley-Ramo weighting potential;
- deterministic saturated-drift trajectories;
- the path transfer

```math
H(\omega)=\int e^{-i\omega t}\,d\phi_w;
```

- six calibrated HgCdTe optical-kernel averages.

No microscopic diffusion is included in the trajectory solver used for the electrostatic-confound demonstration.

---

## 2. Initial quick sweep

GitHub Actions run:

```text
run id       31916800184
artifact     paper02-geometry-quick
artifact id  9255131125
sha256       d4832d3bd717975ab08a4c5080a31e3ee55e6d6912068c5adddb8edbe4aa8f74
```

Result:

```text
24 RF rows total
12 rows with mimic ratio >= 0.5
4 hidden-risk rows
minimum warning margin = -6.09 dB
```

All four hidden-risk rows were the 75%-contact + 3 um depletion case at 500 MHz and 1 GHz for the two beam positions.

This motivated a numerical refinement rather than immediate interpretation.

---

## 3. Fine-resolution convergence

GitHub Actions run:

```text
run id       31916853136
artifact     paper02-geometry-refined
artifact id  9255160359
sha256       eabdea6e9f714e89817b7543985f1350563d9fdbcff1d39234ba84a2d3cb4135
```

The same four hidden-risk rows survived.

Centered beam:

| RF | mimic ratio | geometry phase excess | rank-warning threshold | reference claim threshold | warning margin |
|---|---:|---:|---:|---:|---:|
| 500 MHz | 0.7803 | -0.045827 deg | 83.990 dB | 82.3 dB | -1.690 dB |
| 1 GHz | 0.8651 | -0.095513 deg | 81.786 dB | 76.7 dB | -5.086 dB |

At the 1 um offset beam:

| RF | mimic ratio | geometry phase excess | warning margin |
|---|---:|---:|---:|
| 500 MHz | 0.8003 | -0.046997 deg | -1.457 dB |
| 1 GHz | 0.8848 | -0.097686 deg | -4.844 dB |

The coarse-to-fine change in mimic strength was only about 3--4%, and the hidden-risk classification was unchanged.

---

## 4. Factorial decomposition: contact versus depletion

A 2 x 2 causal decomposition was then performed at fine resolution.

GitHub Actions run:

```text
run id       31917052026
artifact     paper02-factorial
artifact id  9255227347
sha256       039a2f60cbcf6ff3c4dcf7a1814d639b693e5d8c0a56df69495b7c3318b8a3d0
```

Scenarios:

```text
planar
planar + depletion
75% contact
75% contact + depletion
50% contact
50% contact + depletion
```

### Crucial result

The **planar + depletion** case is already a stronger hidden confound than the original 75%-contact example.

For a full-width planar contact with 3.0 um depletion width and 0.05 V space-charge drop:

| RF | mimic ratio | phase excess | sigma2/sigma1 | rank-warning threshold | claim threshold | warning margin |
|---|---:|---:|---:|---:|---:|---:|
| 100 MHz | 1.1401 | -0.013656 deg | 1.35e-4 | 102.664 dB | 96.1 dB | -6.564 dB |
| 500 MHz | 1.1003 | -0.064617 deg | 6.74e-4 | 88.708 dB | 82.3 dB | -6.408 dB |
| 1 GHz | 0.9756 | -0.107715 deg | 1.338e-3 | 82.746 dB | 76.7 dB | -6.046 dB |

Collection fraction is unity and the DC Shockley-Ramo consistency error is at numerical roundoff.

Because the contact is full-width and planar, lateral beam offset leaves these values unchanged.

### Interpretation

The dangerous effect does not require a multidimensional weighting field.

It is already generated by the **physical electric-field gradient itself**.

This does not constitute a false positive for the broad statement "transport is nonuniform." The velocity really is nonuniform. It is a false attribution if the inferred nonuniformity or diffusion is interpreted as a microscopic material coefficient while the device electrostatics are not independently constrained.

---

## 5. Contact/depletion interaction

The finite-contact cases are still nonlinear and physically important.

For centered illumination, the signed four-color phase decomposition is:

### 75% contact

```text
100 MHz: contact +0.001116 deg; depletion -0.013656 deg;
         combined -0.008841 deg; interaction +0.003698 deg

500 MHz: contact +0.003583 deg; depletion -0.064617 deg;
         combined -0.045827 deg; interaction +0.015207 deg

1 GHz:   contact -0.003951 deg; depletion -0.107715 deg;
         combined -0.095513 deg; interaction +0.016152 deg
```

### 50% contact

```text
100 MHz: contact +0.003292 deg; depletion -0.013656 deg;
         combined +0.019067 deg; interaction +0.029431 deg

500 MHz: contact -0.002259 deg; depletion -0.064617 deg;
         combined +0.024753 deg; interaction +0.091630 deg

1 GHz:   contact -0.087215 deg; depletion -0.107715 deg;
         combined -0.161244 deg; interaction +0.033686 deg
```

Thus finite-electrode geometry and depletion are not additive perturbations. Their interaction can reverse signs and substantially change the apparent spectral-depth signal.

However, the existence of the hidden confound is established before this interaction is introduced.

---

## 6. Tangent-confound structure

The six-channel nuisance vectors were projected onto the local rank-one tangent space.

The raw tangent-energy fraction is near unity for many scenarios because a common amplitude perturbation is itself a tangent direction, so that scalar by itself is not a sufficient danger metric.

More informative is the combination of:

- fitted spatial-root shift;
- one-mode residual;
- rank singular-value ratio.

The 75% + depletion case illustrates the mechanism sharply.

At 500 MHz, adding depletion changes the mimic ratio from approximately

```text
0.061 -> 0.780
```

while `sigma2/sigma1` changes from approximately

```text
6.21e-4 -> 5.64e-4.
```

At 1 GHz, mimic changes from

```text
0.0358 -> 0.865
```

while `sigma2/sigma1` remains approximately

```text
8.81e-4 -> 8.58e-4.
```

Thus nuisance amplitude and model-order warning are not monotone with one another.

This behavior is explained by `PAPER02_TANGENT_CONFOUND_THEOREM_2026-08-15.md`.

---

## 7. Dense frequency test using simple geometric root

GitHub Actions run:

```text
run id       31917263235
artifact     paper02-depletion-frequency-law
artifact id  9255275424
sha256       d66b9af730bc2475aba2e706fb2cdbd2eea62efdc301113b9e9b16fd5f55612f
```

The deterministic planar-depletion response was evaluated at

```text
0, 25, 50, 100, 200, 300, 500, 750 MHz,
1, 1.5, 2, 3 GHz.
```

A homogeneous no-recombination drift-diffusion law identified from the 100 MHz spatial root returns

```math
D_{\rm eff}=2.371213\times10^{-3}\ {\rm m^2/s},
```

```math
w_{\rm eff}=2.592141\times10^4\ {\rm m/s}.
```

Both are physically admissible under the inversion even though the simulation truth is

```text
microscopic D = 0.
```

The wrong homogeneous law remains below 1% relative residual through 1 GHz.

This first calculation used the approximate geometric source-coordinate reduction, so it was not by itself sufficient to challenge the stronger calibrated-kernel Rev. 9 procedure.

---

## 8. Kernel-aware dense frequency test

The test was therefore repeated using the exact six calibrated optical kernels.

GitHub Actions run:

```text
run id       31917357402
artifact     paper02-kernel-aware-depletion-frequency-law
artifact id  9255304855
sha256       a9d90b20449d7eba1edc4dc5328dc4fd4a5a6e2d51ae03d9f6b7118b1e62d27e
```

At every frequency the six currents were fit to the finite-kernel one-mode form

```math
J_m=C+K\int g_m(z)\frac{e^{r(z-z_{\rm ref})}-1}{r}\,dz,
```

with continuous affine limit at `r=0`.

The coordinate convention gives `gamma=-r`.

### Validation against uniform planar truth

The same fitter applied to the uniform planar device has maximum relative residual

```text
7.23e-9
```

over the entire 0--3 GHz sweep.

This verifies that calibrated wavelength-dependent kernel shape is not creating the result.

### Depleted deterministic device

The depleted device remains one-mode to relative fit residual

```text
<= 1.74e-4 through 1 GHz
<= 8.04e-4 through 3 GHz.
```

The 100 MHz one-RF homogeneous inversion returns

```math
\boxed{
D_{\rm eff}=2.609795\times10^{-3}\ {\rm m^2/s}
}
```

and

```math
\boxed{
w_{\rm eff}=2.570098\times10^4\ {\rm m/s}.
}
```

The trajectory truth still contains no diffusion.

Physical-law residual:

```text
25 MHz     0.0090 %
50 MHz     0.0071 %
100 MHz    0       %
200 MHz    0.0280 %
300 MHz    0.0745 %
500 MHz    0.2219 %
750 MHz    0.5044 %
1 GHz      0.8885 %
1.5 GHz    1.9201 %
2 GHz      3.2276 %
3 GHz      6.3461 %
```

A joint fit over the nonzero points through 200 MHz gives

```math
D_{\rm eff}=2.606303\times10^{-3}\ {\rm m^2/s},
```

```math
w_{\rm eff}=2.570629\times10^4\ {\rm m/s},
```

and also remains below 1% law residual through 1 GHz.

This is the strongest result of the Paper-02 branch to date.

---

## 9. Analytical explanation now established

Two new analytical notes explain the result.

### `PAPER02_LOW_FREQUENCY_EFFECTIVE_DIFFUSION_THEOREM_2026-08-15.md`

Any recovered exponent

```math
\delta\gamma
=-i a_1\omega+a_2\omega^2+O(\omega^3)
```

with `a_1,a_2>0` can be matched through quadratic order by a homogeneous drift-diffusion model with

```math
V_{*,\rm eff}=1/a_1,
\qquad
D_{\rm eff}=a_2/a_1^3.
```

The first locally non-adjustable dispersion coefficient is cubic.

### `PAPER02_DETERMINISTIC_FIELD_GRADIENT_THEOREM_2026-08-15.md`

For planar Ramo readout with deterministic variable velocity, the local quadratic coefficient is

```math
\boxed{
a_2(z)=
\frac{v'(z)}{v(z)^2}
\left[
\frac{(L-z)^2}{v(z)}
-\int_z^L\frac{L-u}{v(u)}du
\right].
}
```

Monotonic downstream acceleration implies `a_2>0` even though microscopic `D=0`.

In the weak-gradient limit,

```math
\boxed{
D_{\rm eff}(z)\simeq\frac12(L-z)^2v'(z).
}
```

Thus the sign and existence of the false diffusion are no longer merely numerical observations.

---

## 10. Impact on the original Rev. 9 logic

This result does **not** invalidate the exact Rev. 9 mathematics.

The Rev. 9 statement that DC + one RF structurally identifies the assumed homogeneous drift-diffusion-recombination model and that later RF points are overdetermined remains correct **within that model class**.

The new result changes the practical interpretation:

- an omitted deterministic electrostatic nuisance can remain close to the same one-mode spectral manifold;
- its low-frequency root can lie close to the homogeneous drift-diffusion dispersion manifold through quadratic order;
- therefore the first additional RF point may require much higher precision or frequency than the phrase "tries to kill the model" could be read to imply.

In the current example, a wrong zero-diffusion deterministic device remains within 0.89% of the inferred homogeneous diffusion law at 1 GHz.

This should be treated as a **model-attribution and conditioning issue**, not as a contradiction of structural identifiability.

No Rev. 9 manuscript edit has been made in this branch.

---

## 11. Prior-art status

Initial primary-source audit confirms that the broad ingredients are established:

- nonuniform semiconductor electric fields can distort TOF transport inference;
- space-charge assumptions can cause large errors in diffusion-length extraction;
- measured planar terminal-current transients contain space-charge/electrode contributions that complicate interpretation;
- conventional nondispersive TOF transient fitting can recover drift and diffusion from transient shape.

The possible distinct contribution is narrower:

1. the spectral-depth Shockley-Ramo source-coordinate formulation;
2. the deterministic field-gradient positive-`D_eff` theorem;
3. the two-stage tangent confound across spectral-channel and RF-dispersion manifolds;
4. explicit quantification of the RF bandwidth/precision required to distinguish electrostatic heterogeneity from microscopic diffusion.

Priority remains **OPEN** until a dedicated full-text audit of that exact combination is complete.

---

## 12. Active next questions

The strongest next calculations are now:

1. quantitatively verify the analytic field-gradient formula against the exact numerical velocity profile;
2. sweep depletion width and voltage drop to test the predicted scaling of `D_eff`;
3. derive/predict the cubic mismatch coefficient and compare it to the 1--3 GHz residual growth;
4. repeat with at least one independent field-profile family;
5. translate law residual into required complex-response precision and experimental SNR;
6. only then decide whether this becomes a standalone Paper 02 or a major adversarial addition to Paper 01.
