# Paper 03 Stage-B Self-Consistent Forward-Model Specification

**Date:** 2026-08-17  
**Status:** **PREIMPLEMENTATION MODEL CONTRACT / NON-CLAIM**

## 1. Purpose

Stage A deliberately uses a controlled Poisson curvature as a sensitivity coordinate. Stage B must replace that construction with a semiconductor operating state whose electrostatic potential and mobile-carrier distribution satisfy a coupled Poisson / carrier-transport problem.

The word **self-consistent** is reserved for that coupled operating-state solve. It must not be applied retroactively to Stage A.

The first Stage-B target is deliberately narrower than a full high-injection transient TCAD calculation. It is:

```text
self-consistent dark / bias operating state
+
dilute small-signal photocarrier transport through that converged state
+
separate Shockley--Ramo weighting-potential calculation
+
blind spectral/RF analysis.
```

If photoinduced space charge is neglected in the signal calculation, that approximation must be stated explicitly and supported by a low-injection coordinate. A later high-injection extension would be a different model level.

---

## 2. Semiconductor operating-state equations

The initial implementation should use the simplest carrier content that is physically adequate for the declared structure. For a unipolar electron operating-state model the unknowns are electrostatic potential `psi(x,z)` and electron density `n(x,z)`.

The governing system is

```math
-\nabla\cdot(\epsilon\nabla\psi)
=\rho_{fixed}+\rho_{mobile},
```

with the sign convention for charge density written explicitly in code and documentation, together with a steady carrier-continuity equation

```math
\nabla\cdot J_n = q R_{dark}
```

and a drift-diffusion / Scharfetter--Gummel-consistent flux law.

The implementation must not mix electrostatic-potential and electron-potential sign conventions implicitly. A one-dimensional analytic polarity test is mandatory before two-dimensional results are used.

If the operating structure requires both electrons and holes, Stage B must be promoted to the corresponding coupled `psi,n,p` system rather than hiding the second carrier in an effective source term.

---

## 3. Contacts and insulating boundaries

Every electrical boundary must be physically typed rather than inferred from the finite-difference stencil.

At minimum distinguish

```text
ohmic / reservoir contact;
selected collecting contact;
opposite electrical contact;
passivated or insulating surface;
lateral symmetry / insulating boundary.
```

For an ohmic contact, the electrostatic and carrier-density / quasi-Fermi boundary condition must be documented consistently with the declared doping and applied bias.

At insulating/passivated boundaries, use zero normal carrier flux unless an explicit surface-recombination velocity is later introduced.

A finite selected top contact with an insulating remainder is retained so the multidimensional geometry remains nontrivial.

---

## 4. Weighting potential remains a separate problem

The selected-electrode weighting potential is not the semiconductor electrostatic potential.

After geometry is defined, solve separately

```math
\nabla\cdot(\epsilon_w\nabla\phi_w)=0
```

with

```text
selected electrode -> phi_w = 1
all other electrical electrodes -> phi_w = 0
insulating external boundaries -> appropriate homogeneous boundary condition
```

under the weighting-field construction.

Changing doping, carrier density, or applied bias must not directly change `phi_w` unless the physical electrode/dielectric geometry itself changes.

---

## 5. Signal-transport level

The first accepted Stage-B signal model is the **dilute small-signal limit**.

The converged dark/bias state supplies the physical field and local transport coefficients. A photocarrier then obeys a linear drift-diffusion/recombination operator about that state. The terminal response can be computed by either

```text
A. backward resolvent / adjoint first-moment formulation, or
B. a directly solved forward frequency-domain carrier-continuity equation,
```

provided the two are shown to agree in at least one nontrivial test case.

The backward form is the natural continuation of Stage A, schematically

```math
(\kappa+i\omega-L_{DD})H=L_{DD}\phi_w,
```

with contact/surface boundary conditions inherited from the physical signal-carrier problem.

If transport coefficients depend on the self-consistent carrier density or field, that dependence is frozen at the dark operating point for the first small-signal implementation and explicitly recorded.

---

## 6. Low-injection qualification

Calling the signal calculation a dilute perturbation requires an explicit coordinate.

At minimum record an assumed or normalized injected photocarrier density `delta n` and compare it with the relevant background/mobile/fixed charge scale. A Stage-B result used as evidence must state a bound such as

```math
max|q\,\delta n| / max|rho_{operating}| \ll 1
```

or an equivalent potential-perturbation estimate.

If this cannot be made small for the intended observable, photogenerated charge must be coupled back into Poisson and the first Stage-B model is insufficient.

---

## 7. Numerical formulation

The preferred first implementation is a conservative finite-volume or equivalent flux-conservative discretization with exponentially fitted Scharfetter--Gummel carrier fluxes.

The implementation must retain

```text
nonnegative carrier density;
local flux conservation;
explicit residual norms;
mesh metadata;
nonlinear iteration history;
and deterministic reproducibility.
```

A Gummel-type iteration is acceptable for the first solve if convergence is demonstrated. Newton coupling may be added if needed; changing nonlinear solver does not change the physical model contract.

---

## 8. Mandatory solver validation before detector interpretation

### 8.1 Poisson-only analytic limit

With mobile charge disabled and a full parallel-plate contact geometry, recover the appropriate one-dimensional Poisson solution for a declared constant fixed charge, including field polarity and curvature.

### 8.2 Charge-neutral / zero-space-charge limit

For a neutral uniform semiconductor with compatible contacts, recover the expected near-linear applied-bias potential rather than generating spurious curvature.

### 8.3 Equilibrium or zero-bias current test

For an equilibrium-compatible boundary condition, the net carrier current must vanish to the discretization/nonlinear-solver tolerance.

### 8.4 Steady current conservation

At finite bias with no bulk generation/recombination source, integrated normal current through transverse cuts must be spatially constant within the declared tolerance.

### 8.5 Mesh convergence

At least three meshes are required. A detector-relevant observable and the internal operating-state quantities must both be checked; a small terminal-current change cannot excuse an unconverged internal field.

### 8.6 Weighting-potential invariants

The independent weighting solve must satisfy its boundary values and discrete Laplace residual, and the selected-electrode dc Shockley--Ramo endpoint identity must remain satisfied by the signal solver.

### 8.7 Backward-versus-forward signal check

At one nontrivial Stage-B operating point, compare the backward resolvent with an independently assembled forward linearized carrier-continuity calculation for the same spectral/RF response or an equivalent source-response reciprocity identity.

No Paper-03 scientific use is permitted before these gates pass.

---

## 9. Material parameter discipline

Do not choose semiconductor parameters merely to reproduce the Stage-A geometry signal.

Before the first material-specific Stage-B run, create a parameter ledger giving for every dimensional input

```text
symbol;
value/range;
temperature;
composition/doping regime;
primary source or explicit synthetic status;
model relation used;
and uncertainty/sensitivity coordinate.
```

For HgCdTe-specific instantiation, parameters requiring direct source support include at minimum

```text
permittivity;
carrier statistics / intrinsic density model;
electron and, if used, hole mobility;
velocity-field law;
diffusion closure;
recombination law/lifetime coordinate;
contact carrier-density prescription;
doping/fixed-charge scale.
```

No literature value outside its stated temperature/composition/doping regime should be silently transplanted.

A dimensionless generic-semiconductor validation case may precede the HgCdTe instantiation, but it must be labeled as such.

---

## 10. Blind-analysis boundary remains unchanged

The Stage-B forward solver may know

```text
doping/fixed charge;
carrier densities;
self-consistent field;
transport coefficients;
contact physics;
recombination;
trajectory/Green-function information.
```

The Paper-01/Paper-03 blind analyzer may not receive those hidden fields or generating labels. It receives only the calibrated observable inputs allowed by the predeclared hierarchy.

The forward and blind result objects remain physically separate.

---

## 11. Stage-B minimum accepted milestone

Stage B is considered **numerically established**, but still not a Paper-03 result, only when all of the following are true:

```text
one coupled Poisson/carrier operating state converges reproducibly;
analytic/limiting validation tests pass;
current and charge residuals pass declared tolerances;
three-mesh convergence passes;
weighting-potential and dc Ramo invariants pass;
backward/forward small-signal cross-check passes;
material/synthetic parameter provenance is explicit;
and a blind six-channel spectral/RF analysis can be executed without hidden-field leakage.
```

Only after this milestone should the self-consistent forward model be added to the geometry/diffusion/lifetime regime map.

---

## 12. Claim boundary

At creation of this specification:

```text
Stage A deterministic backward resolvent is numerically validated under its stated fixed-field model;
Stage B equations and validation requirements are specified;
Stage B has not yet been implemented or demonstrated;
no material-specific self-consistent detector result is claimed.
```

This file prevents later code from being described as self-consistent unless it satisfies the model and validation boundary above.