# Rev. 9 adversarial-review correction record

## Governing rule

The post-Rev. 8 referee report was treated as an adversarial attack list, not authority. Each objection was checked independently against the canonical Rev. 8 source, algebra, numerical implementation, and primary literature where appropriate. Only objections that survived that check were integrated.

## 1. Confluent rank-two branch — ACCEPTED; genuine mathematical qualification

The full Hankel determinant remains the correct rank-at-most-two null. However, rank two does not imply two distinct exponentials.

For the exact confluent sequence
```math
d_m=(A+Bm)q^m,
```
one has
```math
det(H)=0,
\qquad
W_m=-B^2 q^{2m+2},
```
while recurrence recovery gives
```math
P=W_1/W_0=q^2,
\qquad
S=2q,
\qquad
Delta_q=S^2-4P=0.
```

Therefore Rev. 9 explicitly classifies a resolved rank-two sequence into:
```text
distinct-root rank two: Delta_q != 0
confluent/repeated-root rank two: Delta_q = 0 with nonzero rank-two contrast
```

The distinct-root adjacent-minor identity
```math
W_m=ab(q_1q_2)^m(q_1-q_2)^2
```
is not applied by naively setting `q1=q2` in the confluent case. The confluent basis is `(A+Bm)q^m`.

A repeated root is not automatically nonphysical: a second-order physical model can itself reach a repeated characteristic root. Physical testing must therefore be multiplicity-aware rather than simply discarding the confluent branch.

## 2. Rank-two statistics near rank one — ACCEPTED QUALIFICATION

At exact rank one all `2x2` cofactors of the `3x3` Hankel matrix vanish, so
```math
grad det(H)=0.
```
The first-order delta-method covariance therefore degenerates at the rank-one boundary. Rev. 9 retains the covariance statistic away from that boundary and explicitly recommends null-constrained Monte Carlo / parametric-bootstrap calibration when the determinant linearization is nonregular.

## 3. Common spatial-scale calibration — ACCEPTED

The closure/model-order null is insensitive to a common affine depth rescaling, but dimensional transport coefficients are not.

If
```math
h_cal=c h,
```
then
```math
gamma_cal=gamma/c,
D_cal=c^2 D,
w_cal=c w,
kappa_cal=kappa.
```
Thus for `c=1+epsilon`,
```math
delta D / D ~= 2 epsilon,
delta w / w ~= epsilon.
```

Rev. 9 separates:
```text
model-order/closure calibration
from
absolute dimensional transport-coefficient calibration.
```

## 4. Known arbitrary generation kernels — ACCEPTED; generalized null added

For independently calibrated normalized channel kernels `g_m(z)`, define
```math
M_m(r)=int g_m(z) exp(r z) dz.
```
A homogeneous one-mode terminal-current response has
```math
J_m=A+B M_m(r).
```
Eliminating the two nuisance amplitudes gives, for example,
```math
R_012=(J_1-J_0)(M_2-M_0)-(J_2-J_0)(M_1-M_0),
R_013=(J_1-J_0)(M_3-M_0)-(J_3-J_0)(M_1-M_0).
```
The homogeneous one-mode hypothesis requires a common `r` satisfying both residuals.

For rigid translated kernels, `M_m(r)` becomes a geometric sequence and the original four-color identity is recovered exactly. For independently varying kernels, the experiment becomes a calibrated kernel-aware nonlinear consistency test rather than the parameter-free geometric null.

This makes explicit that an uncorrected `C4 != 0` in a realistic wavelength-dependent optical system rejects the combined homogeneous-transport + assumed-optical-kernel idealization, not homogeneous transport alone.

The Rev. 9 regression includes a deliberately nontranslated Gaussian-kernel example in which the kernel-aware residuals vanish while the simple geometric closure does not.

## 5. Shared composition nuisance — ACCEPTED

In the worked graded-HgCdTe stress, the composition profile `x(z)` enters both:
1. the wavelength-to-generation-depth/kernels, and
2. the composition-induced transport-driving term.

Those uncertainties are therefore correlated. Rev. 9 states that experimental inference should either obtain the depth/composition map independently or propagate the composition profile as a shared nuisance parameter rather than treating optical and transport uncertainties as independent.

## 6. Electron-affinity validation interval — ACCEPTED QUALIFICATION

The explicit 300 K electron-affinity relation remains evaluated over the full worked profile. However, the cited paper's quoted average conduction-band partition of about `67.1%` and the associated statement that the `2/3` rule is accurate to about `+-1%` are tied to its stated averaging interval `0.15 < x < 0.45`.

The worked profile reaches `x=0.55`. Rev. 9 therefore no longer implies that the quantified `67.1% / +-1%` validation interval extends unchanged to `x=0.55`.

## 7. DOS/effective-mass sensitivity — RETAINED

Rev. 8 already exposed this as a substantive model uncertainty. Rev. 9 preserves the `alpha_DOS` sensitivity and continues to describe the HgCdTe calculation as a conditional composition-band-edge stress rather than a calibrated material prediction.

## 8. High-Peclet interpretation — ACCEPTED QUALIFICATION

Using the current worked scale,
```text
v ~= 2.22e4 m/s
D = 0.02327 m^2/s
h = 0.5 um
```
gives
```text
Pe_h ~= 0.477
Pe over 0.79-um kernel width ~= 0.754.
```
Thus the local high-Peclet formula is retained only as asymptotic intuition. The quantitative HgCdTe headline continues to come from the full finite-diffusion boundary-value calculation.

## 9. Hot-state benchmark normalization — ACCEPTED AS LABELING CLEANUP

The inherited hot-to-cold benchmark uses a deliberately strong two-state speed normalization different from the current HgCdTe path-harmonic drift. Rev. 9 labels it explicitly as an independent deliberately strong two-state benchmark, not as the same HgCdTe transport realization.

## 10. Older spectral-depth transport prior art — ACCEPTED

The prior-art discussion now explicitly acknowledges that wavelength-dependent absorption/generation depth has long been used to infer or model carrier transport, including classical surface-photovoltage/diffusion-length and photodiode spectral-response work.

Rev. 9 therefore does not imply that spectral-depth carrier probing began with optical-emission-detection or with this manuscript. The candidate distinction is narrowed to the specific chain:
```text
calibrated spectral/internal-depth channels
-> Shockley-Ramo terminal-current observable
-> spatial differencing / finite-rank model-order test
-> branch-controlled or branch-free RF root constraints
-> cross-RF physical-law falsification.
```
The finite-exponential/Hankel mathematics and spectral-depth probing are both prior art.

## 11. Exact 2024 graded-HgCdTe paper — PRIORITY AUDIT STILL OPEN

A public landing/full-text route was reported, but a complete inspectable technical text was not recovered through the available access path during this pass. Bibliographic metadata and related papers do not substitute for the exact comparison.

Rev. 9 therefore retains the submission boundary in a cleaner form: a direct technical comparison with the exact 2024 paper remains required before submission-level priority language.

## 12. DC physical-admissibility nulls — ACCEPTED

For the homogeneous downstream one-carrier model,
```math
gamma(0)=[sqrt(w^2+4D kappa)-w]/(2D) >= 0,
```
hence
```math
q(0)=exp[-gamma(0)h] in (0,1].
```
Rev. 9 states this branch-independent DC admissibility test together with `D>0`, `kappa>=0`, and the assumed drift-direction constraint. These are free physical nulls before later RF overdetermination.

## 13. Combined-physics blind synthetic challenge — IMPORTANT NEXT VALIDATION, NOT INTEGRATED INTO THIS REPAIR

The referee is right that the strongest remaining device-physics test is a self-consistent synthetic detector containing several ordinary departures simultaneously and analyzed blindly through the hierarchy.

That remains the next major validation project. It is not made a prerequisite for correcting the localized Rev. 8 mathematical/calibration/prior-art issues, and no large simulation section is inserted into Rev. 9.

## Regression

`numerics/rev9_review_regression.py` checks:
- confluent rank-two determinant, minors, recurrence, and repeated-root discriminant;
- vanishing determinant gradient at exact rank one;
- exact common-scale coefficient transformation;
- an arbitrary-kernel one-mode null that succeeds while the simple geometric closure fails;
- local Peclet scales;
- branch-independent DC multiplier admissibility.

Local regression result: PASS.

## Scientific status after this pass

The central four-color translated-kernel Shockley-Ramo closure, branch-qualified DC/RF inversion, conditioning result, corrected Hankel model-order null, weighting-field treatment, and Rev. 8 numerical fixes remain intact. Rev. 9 adds the missing confluent branch and more sharply separates exact ideal nulls, calibrated kernel-aware experimental nulls, and dimensional coefficient recovery.
