# Rev. 8 adversarial-review correction record

## Governing rule

The Rev. 7 referee report was treated as an adversarial attack list, not as authority. Each objection was independently checked against the canonical Rev. 7 algebra, the numerical implementation, and primary literature where material physics or priority was involved. The manuscript was changed only where the criticism survived that check.

## 1. Six-color rank-two closure — ACCEPTED; genuine algebraic defect

Rev. 7 used

```math
W_m=d_m d_{m+2}-d_{m+1}^2,
\qquad
W_1^2=W_0W_2
```

as an unconditional six-color rank-two null. Direct expansion gives instead

```math
W_1^2-W_0W_2=-d_2\det H,
```

where

```math
H=\begin{pmatrix}
d_0&d_1&d_2\\
d_1&d_2&d_3\\
d_2&d_3&d_4
\end{pmatrix}.
```

Therefore the Rev. 7 residual also vanishes on the spurious branch `d2=0`. The explicit sequence `(0,1,0,1,100)` has `W=(-1,1,-1)`, passes the old minor closure exactly, but has `det(H)=-100`.

Rev. 8 replaces the unconditional rank-at-most-two null by

```math
\det H=0.
```

The adjacent-minor identity

```math
W_m=ab(q_1q_2)^m(q_1-q_2)^2
```

is retained for mode separation, conditioning, and recurrence-parameter recovery when nondegenerate. It is no longer advertised as the unconditional model-order null.

## 2. Noisy rank-two-vs-higher test — ACCEPTED

A nonzero adjacent minor rejects rank one; it does not prove rank at most two. Rev. 8 inserts the missing operational rung:

```text
rank one rejected
-> rank-at-most-two determinant null tested
-> two-mode parameters resolved
-> physical root law tested.
```

For `F_H=det(H)`, the manuscript gives the exact first derivative with respect to the five complex first differences and the leading proper-complex covariance

```math
sigma_F^2 ~= g_H^T Sigma_d g_H^*.
```

A stacked real/imaginary statistic is then used for the complex determinant residual. The manuscript also notes that the smallest Hankel singular value is a useful diagnostic, but does not assume a universal noisy singular-value distribution; covariance calibration or simulation is required when linearization is inadequate.

## 3. Weighting-field numbers — ACCEPTED; stale prose replaced, referee's simple rescaling not adopted

The Rev. 7 prose retained old 1%-weighting false phases while its nuisance table had already been recomputed with the new transport scale. A fresh finite-kernel calculation from the Rev. 7/8 model gives for 1% linear weighting variation across the quartet:

```text
100 MHz   0.00294725 deg
500 MHz   0.01214001 deg
1 GHz     0.01000744 deg
```

The corresponding exact variations that place the false phase at 10% of the worked gradient signal are:

```text
100 MHz   0.75683%
500 MHz   0.88129%
1 GHz     1.96060%
```

The low-RF analytic estimate gives about `0.00270 deg` at 100 MHz and is now explicitly distinguished from the finite-kernel result. The referee's `1.15--1.44%` rescaling follows only if the stale Rev. 7 phase values are taken as correct, so it is not adopted.

## 4. Graded-recombination numerical floor — CONCERN ACCEPTED; conclusion retained after a dedicated differential cross-check

The referee correctly noted that a generic `1e-5 deg` absolute agreement between two solvers cannot by itself validate a `1e-8 deg` subtraction.

A dedicated differential test was therefore added. Both the no-recombination case and the graded-recombination/matched-homogeneous case were solved independently with the finite-difference BVP and adaptive DOP853 shooting implementations before the recombination difference was formed. The recombination-induced phase changes are:

```text
RF        finite difference       shooting              |difference|
100 MHz   3.77751e-8 deg          3.77891e-8 deg        1.40e-11 deg
500 MHz   1.84770e-7 deg          1.85360e-7 deg        5.89e-10 deg
1 GHz     3.45631e-7 deg          3.43691e-7 deg        1.94e-9 deg
```

Thus the rounded tiny corrections are retained. The dedicated implementations agree within about `3e-9 deg` across the tested environments, and the manuscript no longer pretends that the coarser absolute `1e-5 deg` comparison is their validation. The stale `1e-6 deg` wording is also corrected to `1e-5 deg` for the absolute cross-check.

## 5. Electron-affinity anchor versus total drift — ACCEPTED

The electron-affinity relation anchors the composition-induced conduction-band/electron-affinity force term. It does not determine the total self-consistent device drift. The full electron current also depends on electrostatic field, carrier-density diffusion, and effective-mass/DOS terms. Rev. 8 now states explicitly that no Poisson solution is imposed and that an electrostatic field comparable to the composition-induced field could reinforce or oppose the worked drift.

Accordingly, the HgCdTe calculation is described as an electron-affinity-anchored **composition-band-edge stress**, not an electron-affinity-anchored total transport prediction.

## 6. Density-of-states/effective-mass sensitivity — ACCEPTED

Under the retained reduced prescription `m* proportional to Eg`, the DOS velocity is not negligible:

```text
|v_DOS| / v_field ~= 8.8% at x=0.55
|v_DOS| / v_field ~= 18.3% at x=0.32
```

Rev. 8 adds the explicit sensitivity `v = v_field + alpha_DOS v_DOS`:

```text
alpha_DOS    100 MHz       500 MHz       1 GHz
0            -0.01861 deg  -0.09026 deg  -0.16513 deg
0.5          -0.02035 deg  -0.09852 deg  -0.17964 deg
1.0          -0.02202 deg  -0.10644 deg  -0.19423 deg
1.5          -0.02349 deg  -0.11360 deg  -0.20885 deg
```

Removing the DOS term changes the worked closure by roughly 15%, so the approximation is now exposed as a substantive model uncertainty rather than a minor correction.

## 7. Continuous free-xi curve — NOT ADOPTED AS A MAIN-TEXT REQUIREMENT

Rev. 8 does not recentre the paper around the historical free `xi` parameter. The headline force is now spatially varying and fixed by the electron-affinity relation, so a dense constant-`xi` curve would primarily characterize an obsolete normalization coordinate. The sparse constant-`xi` table remains as a bracket. The more relevant remaining uncertainty is the DOS/effective-mass term, which is now given an explicit sensitivity table.

A dense free-`xi` scan can remain a supplementary diagnostic if desired, but it is not needed to repair the theorem or to state the current physical boundary accurately.

## 8. Nearly lossless two-carrier DC degeneracy — ACCEPTED

Rev. 7 correctly limited its signed-root statement to the generic recombining case, but the important limiting degeneracy was not explicit. In the nearly lossless electron-hole limit, the integrated Shockley-Ramo path dependence of the two carriers can cancel in the total DC terminal charge, making `J(z,0)` nearly constant and the DC first differences nearly zero.

Rev. 8 therefore states that DC signed roots can label collection directions when appreciable recombination supplies contrast, whereas long-lifetime two-carrier transport may require two or more nonzero RF frequencies for species-specific root tracking.

## 9. Combined-physics detector challenge — IMPORTANT FUTURE WORK, NOT REQUIRED FOR THIS ALGEBRAIC REPAIR

The review is correct that a blind, self-consistent combined-physics synthetic detector would be the strongest next device-physics validation. It remains explicit future work. It is not made a prerequisite for correcting a localized rank-two algebra defect, nor is another large simulation section added to this revision.

## 10. 2024 composition-gradient HgCdTe priority audit — STILL OPEN

The bibliographic metadata and a public landing page for the directly relevant 2024 paper were located, but the exact full text was not successfully retrievable through the available access path during this revision. Related 2022/2023 work from the same research line concerns composition-gradient built-in fields, responsivity, and high-speed response, but it does not substitute for reading the exact 2024 source.

Priority therefore remains **OPEN / UNPROVEN**. Rev. 8 does not convert metadata, a title, or related-paper inspection into a novelty claim.

## 11. Figure suggestion — NOT REQUIRED FOR THE SCIENTIFIC CORRECTION

The existing manuscript is already dense, but a new figure is editorially optional rather than scientifically necessary. Rev. 8 adds one compact DOS-sensitivity table because that directly exposes a newly quantified material uncertainty. No decorative figure is added solely because the referee suggested one.

## Regression

The numerical and algebraic anchors above are checked in:

```text
numerics/rev8_review_regression.py
```

The script verifies the spurious minor branch, the exact factorization numerically on generic complex sequences, the revised weighting-field false phases and thresholds, the DOS sensitivity, the unchanged finite-width HgCdTe targets, and the dedicated differential recombination cross-check.

## Scientific status after this pass

The central four-color terminal-current closure, spatial-log branch qualification, DC/RF inversion, conditioning result, singular weighting-field treatment, and optical/calibration framework were not altered because this review did not break them. The six-color rung is materially stronger: its model-order null is now the proper Hankel determinant, with a separate noise-aware test before parameter recovery.
