# Paper 03 Stage-B mesh / weighting / reciprocity validation lock

**Date:** 2026-08-17  
**Status:** **PREDECLARED GENERIC NUMERICAL VALIDATION / NON-CLAIM**

This is the next mandatory generic Stage-B layer after the checked coupled operating-state validation. It does not alter the synthetic semiconductor parameters, does not instantiate HgCdTe, and does not make a detector-performance claim.

## 1. Fixed operating-state model

Reuse `paper03_stageB_operating_state.py` without changing its physics:

```text
W = 16 um; L = 7.6 um
T = 100 K; eps_r = 12
mu_n = 0.50 m^2/(V s); N_D = 1e19 m^-3
built-in selected-top offset = -10 mV
external finite bias = +30 mV
selected top contact fraction = 0.75
bottom full reservoir contact
uncontacted top and sidewalls insulating
D_n = mu_n kT/q
```

All values remain explicit synthetic validation coordinates.

## 2. Three-mesh operating-state gate

Run the same finite-bias coupled solve on

```text
21 x 15
31 x 23
41 x 31
```

Before inspecting the result, require the 31x23 -> 41x31 pair to satisfy all of:

```text
absolute relative change of mean terminal/cut current <= 0.03
centerline potential RMS change / max(V_T, |V_top|) <= 0.02
centerline density RMS change / N_D <= 0.03
relative change of min(n/N_D) <= 0.05
```

The internal profiles are compared on a common normalized-z interpolation grid. If a threshold fails, refine the mesh; do not relax the threshold.

Every mesh must separately retain positive finite carrier density, Poisson residual <1e-8, continuity residual <1e-8, horizontal-cut current nonconservation <1e-5, and terminal imbalance <1e-5.

## 3. Independent weighting-potential problem

On each mesh solve a separate Laplace finite-volume problem for the selected top electrode:

```text
selected finite top contact -> phi_w = 1
full bottom contact          -> phi_w = 0
uncontacted top              -> zero normal flux
sidewalls                    -> zero normal flux
```

The semiconductor charge density, applied electrostatic bias, and carrier density do not enter this solve.

Require:

```text
linear residual <1e-10
all cell-center phi_w in [0,1] to 1e-10 tolerance
31x23 -> 41x31 centerline phi_w RMS change <= 0.02
```

## 4. Frozen-field dilute signal operator

At the accepted finest self-consistent operating state, freeze the electrostatic potential and the synthetic material coefficients. Construct the linear dilute photocarrier operator directly from the same Scharfetter-Gummel edge coefficients used by the continuity discretization, with contact perturbations fixed to zero.

This is a small-signal perturbation around the converged state; it is not a second nonlinear Poisson solve.

Use the explicit low-injection normalization

```text
max |delta n| / N_D = 1e-4
```

for the reciprocity demonstration. Because the signal problem is linear, this normalization sets amplitude only and cannot change the transfer-function shape.

## 5. DC Shockley-Ramo invariant

Let `Q` be the backward Markov generator of the frozen-field dilute carrier, `b_sel` the selected-contact absorption-rate vector, and `phi_w` the independently solved weighting potential. Use the discrete Ramo source

```text
q_R = Q phi_w + b_sel.
```

Solve the selected-contact committor

```text
(-Q) p_sel = b_sel
```

and the zero-frequency Ramo response

```text
(-Q) H_0 = q_R.
```

Require

```text
max |H_0 - (p_sel - phi_w)| < 1e-8
committor linear residual <1e-8
Ramo linear residual <1e-8.
```

This is a discrete algebraic invariant of the accepted operator construction, not a material claim.

## 6. Independent forward/backward reciprocity

Use one nontrivial frequency fixed before execution:

```text
f = 500 MHz.
```

The backward response is

```text
(i omega I - Q) H = q_R.
```

Independently assemble the forward perturbation operator from the frozen continuity matrix with zero contact perturbation. Require operator transpose consistency as an implementation diagnostic but perform the response solve independently:

```text
(i omega I - F) u = s.
```

Use a fixed positive Gaussian cell source centered at `(x,z)=(0,0.55L)` with widths `(0.20W,0.18L)`, normalized after solving so `max|delta n|/N_D=1e-4`.

Test the bilinear reciprocity identity

```text
s^T H = q_R^T u
```

with no complex conjugation, as appropriate for the transpose Green-function identity. Require:

```text
backward linear residual <1e-8
forward linear residual <1e-8
relative reciprocity mismatch <1e-9
relative ||F-Q^T|| diagnostic <1e-12.
```

## 7. Claim boundary

Passing this layer establishes only:

```text
three-mesh convergence for the generic coupled operating state;
independent selected-electrode weighting solve;
discrete DC Ramo/committor consistency;
and forward/backward small-signal reciprocity for one nontrivial generic point.
```

It does **not** establish:

```text
HgCdTe material realism;
bipolar HgCdTe operation;
six-channel Stage-B spectral/RF behavior;
blind-analysis success on Stage B;
Paper-03 standalone GO;
science_interpretation_ready = true.
```

The preliminary HgCdTe ledger independently indicates that the preferred low-doped x~0.30, 230-300 K material route is bipolar by default; this generic electron-only validation must not be relabeled as that material case.
