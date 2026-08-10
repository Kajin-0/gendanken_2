# Paired A/B Joint Identifiability — Why the Contrast Experiment Should Not Fit Two Arbitrary Smooth Profiles Symmetrically

**Date:** 2026-08-09  
**Status:** conditional optical-geometry identifiability calculation over the 72-member sample-A profile family; no calibrated transport and no novelty claim

## 1. The hidden question in the paired experiment

The paired same-source observable is

```math
\Delta\phi_{AB}
=-\Omega
\left(
\mathbf A_A\mathbf q_A
-
\mathbf A_B\mathbf q_B
\right)
+\Delta c.
```

This is excellent for removing arbitrary common tunable-source phase.

But it creates an inverse question that had not yet been quantified:

> **Can the paired spectrum separate several independent smooth transport modes in A and B simultaneously, or are the two devices' spectral response spaces too similar?**

If the response spaces overlap strongly, the correct use of the paired measurement is not

```text
recover q_A and q_B independently from A-B
```

but rather

```text
calibrate/constrain B first
-> use A-B to recover transport contrast / extra A structure.
```

This calculation tests that distinction directly.

---

## 2. Optical matrices

Use

```text
sample B:
current central 150 V/cm Hansen/Moazzami Beer-Lambert envelope

sample A:
all 72 text-constrained profile-family members

300 K
front-collection survival timing kernels
80 cells per device
lambda = 2.80-3.95 um in 0.01 um steps
retain only wavelengths with Pabs >= 0.05 in both devices.
```

Depending on the sample-A profile, the common retained scan has

```text
102-104 wavelengths
```

and terminates near

```text
3.81-3.83 um.
```

The calculation deliberately uses the simpler Beer-Lambert optical matrices because the question is the **relative spectral-response geometry** of A and B. Interference/reflection uncertainty is treated separately in the temperature-control branch.

---

## 3. Separate smooth-mode bases

For each device, first remove the wavelength-independent row component and perform an SVD of its own optical timing operator.

For sample A:

```math
\mathbf A_{A,\Delta}
=\mathbf A_A-\mathbf 1\overline{\mathbf A_A},
```

```math
\mathbf A_{A,\Delta}
=\mathbf U_A\mathbf\Sigma_A\mathbf V_A^T.
```

Similarly for B.

Take the first `m` right-singular transport modes in each device:

```math
\mathbf q_A\approx\mathbf V_{A,m}\mathbf a,
```

```math
\mathbf q_B\approx\mathbf V_{B,m}\mathbf b.
```

Their paired spectral response is

```math
\boxed{
\mathbf G_m
=\mathbf P_\perp
\begin{bmatrix}
\mathbf A_A\mathbf V_{A,m}
&
-\mathbf A_B\mathbf V_{B,m}
\end{bmatrix},
}
```

where `P_perp` removes the wavelength-independent phase mode.

---

## 4. Geometry-only conditioning diagnostic

The A and B modal amplitudes have arbitrary basis normalization.

To ask only whether their **spectral shapes** can be distinguished, normalize every response column of `G_m` to unit Euclidean norm and calculate its singular values.

Thus the resulting ratios are not absolute Fisher information.

They answer the narrower question:

> **If every candidate parameter direction produced the same total response norm, how linearly independent would their wavelength signatures be?**

A very small singular value therefore indicates a true response-shape degeneracy rather than merely weak absolute signal.

---

## 5. One independent smooth mode per device already overlaps strongly

For

```text
1 A mode + 1 B mode,
```

the weakest normalized singular ratio across the 72 A-profile family is

```math
\boxed{
0.0590\text{-}0.1937
}
```

with median

```math
\boxed{0.1438.}
```

Even the dominant smooth A and B transport signatures are therefore far from orthogonal.

A symmetric two-parameter decomposition already carries a geometry-only condition ratio of approximately

```text
5-17.
```

---

## 6. Two modes per device becomes poorly conditioned

For

```text
2 A modes + 2 B modes,
```

the weakest normalized singular ratio falls to

```math
\boxed{
0.00853\text{-}0.04042
}
```

with median

```math
\boxed{0.02567.}
```

That corresponds to a geometry-only amplification scale of roughly

```text
25-117
```

for the weakest independent combination before any actual heteroscedastic noise or optical uncertainty is included.

---

## 7. Three modes per device is effectively singular for independent reconstruction

For

```text
3 A modes + 3 B modes,
```

the six normalized singular ratios across the A-profile family are

| mode | range of `s_k/s_1` | median |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 0.9907-0.9995 | 0.9960 |
| 3 | 0.8417-0.9575 | 0.8894 |
| 4 | 0.2886-0.5399 | 0.4572 |
| 5 | 0.03075-0.13654 | 0.08992 |
| 6 | **0.001831-0.007633** | **0.002934** |

Thus the weakest direction has a geometry-only condition ratio of roughly

```math
\boxed{
1/(s_6/s_1)\approx131\text{-}546.
}
```

This is before

```text
phase noise
wavelength-dependent SNR
sample-A optical uncertainty
instrument covariance
regularization
or transport-model error.
```

A symmetric six-parameter A+B reconstruction is therefore not a credible first interpretation of paired data.

---

## 8. Principal-angle view makes the reason transparent

Compute the principal angles between the first-three **spectral response subspaces** of A and B after removing common phase.

Across the 72 sample-A profiles:

```text
first principal angle:
0.210-0.875 deg
median 0.336 deg

second principal angle:
3.524-15.695 deg
median 10.318 deg

third principal angle:
33.546-65.356 deg
median 54.407 deg.
```

The first A/B smooth response direction is therefore almost the **same spectral function** in the two devices.

The second also overlaps substantially.

Only the third three-mode direction is consistently well separated.

This is exactly why the paired operator develops one or two nearly null combinations when both devices are allowed arbitrary smooth coefficients.

---

## 9. What the paired measurement actually supports

For the six-column `3+3` normalized transport operator, the number of singular directions above simple relative thresholds is approximately

```text
s/s1 > 0.10 -> 4-5 directions, median 4
s/s1 > 0.05 -> 4-5 directions, median 5.
```

These thresholds are only geometric diagnostics, not experimental rank claims.

But they show something important:

> **The paired wavelength scan contains multiple useful transport-contrast directions, even though it cannot stably assign all of them independently to arbitrary A and B profiles.**

The experiment is therefore not information poor.

Its natural coordinates are **contrast modes**, not two separate unconstrained mode sets.

---

## 10. Correct experimental architecture

The result elevates the previously proposed sample-B calibration from a useful control to an identifiability requirement.

### Stage 1 — independently constrain sample B

Use sample B alone to determine its few smooth differential transport modes as well as the instrument permits.

This can use

```text
single-device wavelength × RF data
common-chain calibration
smoothness/physical priors
bias/temperature repetitions
etc.
```

The goal is not perfect absolute `q_B(z)`.

It is a posterior/covariance for the few B modes that matter to the paired observable.

### Stage 2 — paired A-B measurement

Then use

```math
\Delta\phi_{AB}
+\text{calibrated/constrained }\mathbf q_B
```

to infer

```text
additional A transport structure
or directly parameterized A-B contrast modes.
```

This prevents the shared smooth A/B spectral directions from being incorrectly interpreted as independently measured quantities.

---

## 11. Strongest physical parameterization

The most defensible paired model is now

```math
\boxed{
\mathbf q_A
=\mathbf q_{A,\rm smooth}
+\delta\mathbf q_A,
}
```

with sample B supplying the calibrated smooth-control behavior and

```math
\delta\mathbf q_A
```

representing transport associated with A's retained nonlinear/high-field region.

The scientific question becomes

> **Is an additional A-only transport component required after the smooth response calibrated on B is accounted for?**

That is much better conditioned conceptually and statistically than asking paired data to produce two independent absolute profiles.

---

## 12. Why this is a useful negative result

The same-source A/B architecture was introduced primarily to cancel tunable-source phase.

It would have been easy to assume that the resulting high-quality difference data could then fit several modes in each device independently.

The present calculation shows that assumption is false for the current optical structures.

The systematic advantage survives, but the inverse must respect the shared A/B spectral subspace.

This is an experimentally consequential correction rather than a cosmetic reparameterization.

---

## 13. Claim boundary

### CHECKED NUMERICALLY / CONDITIONAL

For the current central sample-B optical model, all 72 sample-A sensitivity profiles, common `Pabs>=0.05` wavelength support, and separately defined first-three smooth transport bases:

- the first A/B response-subspace principal angle is only `~0.21-0.87 deg`;
- a symmetric `1+1` fit has weakest normalized singular ratio `~0.059-0.194`;
- `2+2` falls to `~0.0085-0.0404`;
- `3+3` falls to `~0.00183-0.00763`;
- the first four paired contrast directions remain substantially stronger than the final one or two.

### INTERPRETATION

Paired data are naturally suited to **transport contrast** and A-only excess structure, not to independent recovery of several arbitrary smooth modes in both devices.

### NOT ESTABLISHED

- actual sample-A transport modes;
- actual sample-B posterior uncertainty;
- covariance-weighted paired experimental rank;
- interference-aware full A/B joint singular spectrum;
- ability to localize the real nonlinear-gradient transport effect;
- novelty / priority.

---

## 14. Next decisive work

The next inverse calculation should therefore **not** increase the number of symmetric A/B parameters.

Instead:

1. formulate a calibration-first Bayesian/Fisher problem in which B modes enter the paired inversion with finite prior covariance;
2. determine how accurately B must be known before an A-only nonlinear transport mode becomes measurable at `~0.1 deg` differential phase precision;
3. use the measured two-arm covariance once available;
4. test an A-localized anomaly family tied to the retained nonlinear-gradient region rather than arbitrary A modes.

This directly connects sample-B calibration quality to the detectability of the scientifically interesting A-specific transport contrast.

---

## 15. Reproducibility

Deterministic regression:

`numerics/hgcdte_paired_ab_joint_identifiability.py`
