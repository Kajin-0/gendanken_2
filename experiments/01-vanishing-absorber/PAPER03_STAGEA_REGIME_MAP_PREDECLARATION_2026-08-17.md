# Paper 03 Stage-A Regime-Map Screening — Predeclaration

**Date:** 2026-08-17  
**Status:** **PREDECLARED BEFORE SCREENING OUTPUT / NON-CLAIM**

## 1. Purpose

The nominal finite75 + depletion Stage-A coordinate supports candidate Outcome A: an order-one geometry-induced transport-like signature survives the correct calibrated optical kernels, rejects the one-mode model, is compactly represented by a two-mode diagnostic, then fails the homogeneous physical root law; the predeclared bootstrap detects the one-mode failure before the frozen transport-claim SNR at all three RFs.

That single coordinate is insufficient for a standalone Paper 03. The next question is whether the behavior occupies a broad ordinary region or is a narrow hand-picked point.

This file fixes the first broad **screening** lattice and the expensive-point selection rules before reading any screening result.

The screen is not itself the final regime map. It is designed to locate boundaries, strongest confounds, and possible hidden-risk candidates for refined calculation.

---

## 2. Forward formulation

Use the checked deterministic Stage-A backward resolvent

```math
(\kappa+i\omega-L_h)H=L_h\phi_w
```

with the existing finite-contact / controlled-depletion geometry solver.

Use the correct calibrated six-channel optical kernels and the kernel-aware one-mode null

```math
J_m=A+B M_m(r).
```

The screen may use the local regular noncentral-chi-square SNR approximation as a **ranking coordinate** because the nominal point has already been bootstrap-calibrated. The screen must not relabel that analytic estimate as a bootstrap result.

No kernel-aware two-mode global fit and no parametric bootstrap is performed at every screening point. Those are reserved for predeclared selected points.

---

## 3. Screening numerical level

Use

```text
spatial grid = 81 x 61
lateral quadrature = 9 points
full calibrated optical depth support
frequencies = DC, 100 MHz, 500 MHz, 1 GHz
```

This is deliberately lower resolution than the accepted nominal 201x151 result. The 81x61 values are **selection coordinates only**.

Every selected scientific point is subsequently recomputed on at least

```text
161 x 121
201 x 151
17-point lateral quadrature
```

before scientific interpretation.

No point is declared hidden or self-announcing solely from the 81x61 screen.

---

## 4. Block A — geometry / transport lattice

Use a centered Gaussian beam

```text
sigma_x = 2.0 um
x0 = 0.0 um
```

and the Cartesian product

```text
contact fraction fc = {0.50, 0.75, 0.875, 1.00}

electrostatic/depletion coordinate =
  E0: Wd=0.0 um, Vsc=0.000 V
  E1: Wd=3.0 um, Vsc=0.050 V

D = {1.0e-3, 2.5e-3, 5.0e-3} m^2/s

tau = {infinity, 5 ns}
```

Total Block-A points:

```text
4 x 2 x 3 x 2 = 48.
```

`fc=1` points are included as full-contact controls. They are not assumed a priori to equal the simple planar reference when the controlled depletion coordinate is nonzero.

---

## 5. Block B — optical-position lattice

Lock transport/electrostatic coordinates to

```text
D = 2.5e-3 m^2/s
tau = infinity
Wd = 3.0 um
Vsc = 0.050 V
```

and use

```text
contact fraction fc = {0.50, 0.75, 0.875}
beam sigma_x = {1.0, 2.0} um
beam center x0 = {0.0, 1.5} um
```

Total Block-B points:

```text
3 x 2 x 2 = 12.
```

The Gaussian is renormalized over the inherited finite lateral optical integration support.

The normalized optical coordinates recorded are

```math
\beta=\sigma_x/(W_{contact}/2),
```

```math
\xi=x_0/(W_{contact}/2).
```

---

## 6. Same-physics reference

For every unique `(D,tau,beam_sigma,beam_center)` combination, calculate a same-physics full-contact/no-depletion reference

```text
fc = 1
Wd = 0
Vsc = 0
```

on the same numerical grid and optical quadrature.

The historical phase comparison coordinate is

```text
mimic fraction = |phase_case - phase_reference| / |frozen transport target|.
```

It is retained because it measures the scale of the confound relative to the existing transport target, but the actual one-mode falsification statistic is the calibrated-kernel nonlinear residual.

---

## 7. Screened quantities

For each point and nonzero RF record at minimum

```text
same-physics mimic fraction;
calibrated all-six one-mode contrast-normalized residual rho1;
best-fit one-mode root as a mathematical diagnostic only;
profile condition number;
mean adjacent current-step amplitude s_J;
deterministic one-mode residual norm;
local regular analytic SNR for alpha=0.002699796063260207 and 90% power;
frozen transport-claim SNR;
analytic warning margin = claim SNR - analytic rejection SNR;
selected-contact / resolvent numerical diagnostics.
```

The analytic rejection SNR uses the same per-quadrature noise convention as the nominal predeclared bootstrap.

No physical microscopic parameter is inferred from the one-mode root.

---

## 8. Screening classifications

At an RF define

```text
order-one mimic row:
  mimic fraction >= 0.50

analytic early-warning row:
  analytic warning margin > 0 dB

analytic hidden-risk row:
  mimic fraction >= 0.50
  and analytic warning margin <= 0 dB
```

These are **screening labels only**. A hidden-risk screening row is not Outcome B until refined and bootstrap-calibrated.

For a detector point, aggregate over the three nonzero RFs and retain

```text
max mimic fraction;
min analytic warning margin;
max analytic warning margin;
max rho1;
RF at each extremum.
```

---

## 9. Predeclared expensive-point selection rules

After the complete 60-point screen is generated, select the following detector points using only the declared screen metrics. Deduplicate identical points while preserving the first-listed selection reason.

### S0 — nominal anchor

Always select

```text
fc=0.75, Wd=3 um, Vsc=0.05 V,
D=2.5e-3 m^2/s, tau=infinity,
sigma_x=2 um, x0=0.
```

### S1 — maximum confound

Select the point with the largest `max mimic fraction` over the three RFs.

### S2 — worst early-warning margin among order-one points

Among detector points having at least one RF with `mimic >=0.50`, select the point with the minimum analytic warning margin over those order-one rows.

If that margin is nonpositive, this is the primary hidden-risk candidate.

### S3 — closest analytic warning boundary

Among order-one rows, select the detector point whose analytic warning margin has the smallest absolute value.

### S4 — strongest early warning among order-one points

Among order-one rows, select the detector point with the largest analytic warning margin.

### S5 — largest calibrated one-mode mismatch

Select the detector point with the largest all-six `rho1` over nonzero RF.

### S6 — optical-offset stress

Within Block B only, select the point with the minimum analytic warning margin over order-one rows. If Block B has no order-one row, select its largest-mimic point.

### S7 — weakest still-order-one confound

Among rows with `mimic >=0.50`, select the detector point whose maximum mimic fraction is closest to `0.50` from above.

Maximum unique refined points:

```text
8.
```

No additional point may be called predeclared after the screen is examined. Additional scientifically motivated points must be labeled post-screen/adversarial.

---

## 10. Tie breaking

For exact or machine-level ties, use this deterministic lexicographic order:

```text
block label;
contact fraction ascending;
depletion width ascending;
space-charge drop ascending;
D ascending;
lifetime with finite before infinity;
beam sigma ascending;
beam center ascending.
```

This prevents manual preference among numerically tied candidates.

---

## 11. Refined selected-point gate

Each selected point is recomputed at 161x121 and 201x151 with 17-point lateral quadrature.

Before interpreting that point, require

```text
all sparse linear residuals < 1e-8;
committor residual < 1e-8 where applicable;
DC committor/Ramo identity < 1e-8 for tau=infinity;
201-vs-161 change of the historical raw phase <= 2% of the frozen target at every nonzero RF.
```

The retained 2% criterion is the same Stage-A spatial readiness coordinate already passed by the nominal point. It is not relaxed for selected extremes.

If a selected point fails refinement, it is reported as numerically unresolved and is not used to decide Outcome A/B until further explicitly post-screen refinement.

---

## 12. Bootstrap selection after refinement

Do not bootstrap every screening point.

After refined selected-point calculations:

- bootstrap **S2** if it has any refined order-one row;
- bootstrap **S3** if it is distinct from S2 and has any refined order-one row;
- bootstrap **S1** if distinct from S2/S3 and its refined maximum mimic exceeds `1.0`;
- the already completed nominal S0 bootstrap is reused rather than rerun if the forward coordinate is unchanged.

For each new bootstrap point, use the same `alpha`, 90% power target, per-quadrature noise convention, null/alternative sample counts, and five-point SNR offset grid as the nominal bootstrap unless a new predeclaration explicitly changes them **before** that selected-point bootstrap is run.

---

## 13. Screening decision categories

After refined/bootstrapped selected points:

### Broad Outcome-A evidence

Requires all of:

```text
no refined hidden-risk selected point survives bootstrap calibration;
order-one mimic occurs in more than one contact fraction or transport coordinate;
selected boundary/worst points preserve positive tested warning margin;
and the nominal Outcome-A hierarchy remains qualitatively intact.
```

### Outcome-B evidence

Requires at least one numerically refined, order-one point for which the predeclared bootstrap fails to reject the calibrated one-mode model before the frozen transport-claim SNR, **and** that point is not a numerical/conditioning pathology.

A single coarse-screen analytic hidden-risk row is not Outcome B.

### Narrow-corner result

If order-one mimic and early warning survive only around the nominal coordinate and collapse elsewhere, the result remains useful Paper-01 validation but weakens the case for standalone Paper 03.

---

## 14. Remaining standalone requirements unaffected by this screen

Even broad Stage-A Outcome-A evidence does not complete Paper 03. Still required:

```text
a materially different second geometry family;
Stage-B self-consistent semiconductor validation;
focused prior-art audit.
```

`science_interpretation_ready` remains false throughout this screen.