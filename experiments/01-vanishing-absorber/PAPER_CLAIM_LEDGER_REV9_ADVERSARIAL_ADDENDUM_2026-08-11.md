# Paper Claim Ledger — Rev. 9 Adversarial Addendum

**Status:** additive correction to `PAPER_CLAIM_LEDGER.md`; canonical predecessor claims remain unless explicitly superseded below.

## RANK9-1 — six-color rank-at-most-two determinant

**Status:** **DERIVED / CHECKED / KNOWN HANKEL MATHEMATICS**

For five first differences, `det(H)=0` is the unconditional rank-at-most-two recurrence null under the finite-rank sequence model. It does not by itself imply two distinct exponential roots.

## RANK9-2 — distinct versus confluent rank two

**Status:** **DERIVED / CHECKED**

After rank two is accepted and recurrence parameters `S,P` are resolved, define
```math
Delta_q=S^2-4P.
```

- `Delta_q != 0`: two distinct recurrence roots.
- `Delta_q = 0` with nonzero rank-two contrast: confluent/repeated-root sequence
  ```math
  d_m=(A+Bm)q^m.
  ```

For the confluent sequence,
```math
W_m=-B^2q^{2m+2},
```
so the distinct-root formula `ab(q1 q2)^m(q1-q2)^2` must not be evaluated by simply setting `q1=q2`.

A physical second-order model can itself become confluent; repeated roots require multiplicity-aware physical testing rather than automatic rejection.

## STAT9-1 — determinant statistic is nonregular at rank one

**Status:** **DERIVED**

At exact rank one all `2x2` cofactors of the `3x3` Hankel matrix vanish, so the first derivative of `det(H)` vanishes. First-order delta-method calibration is therefore singular at that boundary. Null-constrained simulation / parametric bootstrap is the preferred calibration near rank one.

## CAL9-1 — common spatial-scale bias

**Status:** **DERIVED / CHECKED**

If the calibrated spatial scale is `c` times the true scale,
```math
D_cal=c^2D,
w_cal=cw,
kappa_cal=kappa.
```
Thus closure/model-order calibration and dimensional transport-coefficient calibration are separate budgets.

## OPT9-1 — known arbitrary generation-kernel null

**Status:** **DERIVED / CHECKED / CONDITIONAL**

For independently calibrated normalized kernels `g_m(z)`, define
```math
M_m(r)=int g_m(z)e^{rz}dz.
```
The homogeneous one-mode model has
```math
J_m=A+B M_m(r).
```
Four channels overdetermine this relation through kernel-aware nonlinear consistency residuals. The simple geometric four-color identity is the rigid-translation special case.

Therefore a raw simple-closure failure with evolving optical kernels rejects the combined transport+optical idealization unless the optical kernel correction is independently constrained.

## OPT9-2 — composition profile is a shared nuisance

**Status:** **CONDITIONAL / EXPERIMENTAL REQUIREMENT**

In the worked graded-HgCdTe construction, the same `x(z)` affects both spectral generation kernels and the composition-induced band-edge force. Experimental inference should propagate `x(z)` jointly or constrain it independently; optical and transport uncertainties are not generically independent.

## PHY9-1 — free DC admissibility

**Status:** **DERIVED / CHECKED**

For the stated homogeneous downstream one-carrier model,
```math
q(0) in (0,1],
D>0,
kappa>=0,
```
with the assumed drift-direction sign. Violation is an immediate physical null failure before cross-RF overdetermination.

## HGC9-1 — high-Peclet formula is asymptotic intuition for the worked scale

**Status:** **CHECKED / CONDITIONAL**

The worked local Peclet numbers are only about `0.48` per 0.5-um source step and `0.75` over the 0.79-um kernel width. The local high-Peclet expression is not a quantitative approximation to the headline HgCdTe result; the full finite-diffusion boundary-value calculation remains the numerical result.

## HGC9-2 — electron-affinity partition validation interval

**Status:** **PRIMARY-SOURCE QUALIFICATION**

The explicit 300 K affinity formula is evaluated over the worked profile, but the cited source's quoted `67.1%` average conduction-band partition and approximately `+-1%` accuracy of the two-thirds rule are tied to its stated averaging interval `0.15<x<0.45`. The worked front composition `x=0.55` lies outside that interval.

## PRIOR9-1 — spectral-depth carrier probing predates this work

**Status:** **KNOWN / HARD PRIOR-ART BOUNDARY**

Classical surface-photovoltage/diffusion-length and photodiode spectral-response literature already uses wavelength-dependent absorption/generation depth to infer or model carrier transport. This manuscript does not claim that spectral-depth probing itself is new.

The candidate distinction remains the combined:
```text
spectral/internal-depth calibration
-> Shockley-Ramo terminal-current observable
-> spatial differencing / finite-rank model-order closure
-> RF root constraints
-> physical-law falsification.
```

## PRIOR9-2 — exact 2024 graded-HgCdTe comparison

**Status:** **OPEN / SUBMISSION BLOCKER**

The exact 2024 graded-HgCdTe paper remains directly relevant. Bibliographic metadata and adjacent literature are not sufficient to establish priority. A direct technical full-text comparison remains required before submission-level novelty/priority language.

## FUTURE9-1 — combined-physics blind detector challenge

**Status:** **OPEN / NEXT MAJOR VALIDATION**

A self-consistent synthetic detector containing several ordinary departures simultaneously should generate currents independently of the closure model and then be analyzed blindly through the hierarchy. Safe output `rank>2, mechanism unresolved` is a valid success mode.
