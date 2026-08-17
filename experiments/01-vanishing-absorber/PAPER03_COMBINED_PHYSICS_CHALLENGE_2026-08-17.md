# Paper 03 Combined-Physics Blind Challenge

**Date:** 2026-08-17  
**Status:** **PREDECLARED / NON-CLAIM / DEVELOPMENT GATE**  
**Purpose:** test whether the spectral-depth Shockley--Ramo falsification hierarchy remains conservative when several ordinary detector-physics departures coexist in one forward model that is not the inverse model.

## 1. Scientific question

The next decisive question is not whether another isolated mechanism can break a four-color closure. That is already known. The question is:

> When finite geometry, nonuniform electrostatics, diffusion, recombination, realistic optical generation kernels, and eventually contact / multicarrier effects coexist in one physically plausible synthetic detector, does the existing hierarchy reject an inadequate low-dimensional transport interpretation before a false microscopic parameter claim becomes statistically defensible?

The benchmark is deliberately allowed to return

```text
rank > 2
mechanism unresolved
```

That is a correct conservative outcome. The benchmark fails if the hierarchy permits a mechanism-specific homogeneous transport interpretation at a precision where the independent forward generator is known not to satisfy that model.

This record predeclares the test before the combined-physics results are used for a manuscript claim.

---

## 2. Independence boundary

### Forward generator

The synthetic detector generator may use

```text
2-D electrostatic potential;
2-D Shockley--Ramo weighting potential;
field-dependent drift;
diffusion;
finite optical generation kernels;
recombination / survival dynamics;
contact and boundary rules;
and, in later stages, self-consistent charge and more than one carrier/state.
```

It must generate terminal-current observables directly from the forward physics.

### Blind analysis

The analysis layer may receive only quantities that would be legitimate calibrated experimental inputs:

```text
complex spectral/RF currents J(lambda, omega);
known channel ordering / calibrated generation kernels when that test requires them;
RF frequencies;
measurement-noise model or injected noise level;
and predeclared geometric/source calibration information explicitly granted to the inverse.
```

The analysis layer must **not** receive generating mechanism labels, true diffusion coefficient, true recombination lifetime, the forward electrostatic field, trajectory histories, or a flag identifying which departure was switched on.

Forward-model diagnostics and blind-analysis outputs must therefore be stored separately in the result object.

No inverse is allowed to call a forward-generator internal routine to infer the hidden mechanism.

---

## 3. Observable lock

The observable remains the selected-electrode Shockley--Ramo terminal response.

For a trajectory with weighting potential `phi_w`, the discrete RF contribution is accumulated from actual weighting-potential increments,

```math
H(\omega)=\sum_k
\exp[-i\omega(t_k+\Delta t_k/2)]
\left[\phi_w({\bf r}_{k+1})-\phi_w({\bf r}_k)\right].
```

At DC this telescopes exactly, apart from interpolation / numerical error, to

```math
H(0)=\phi_w({\bf r}_{\rm end})-\phi_w({\bf r}_0).
```

For collection at the selected electrode this becomes `1-phi_w(r0)`. For recombination or collection at another boundary the correct endpoint weighting potential is retained. The code must not silently force every trajectory to unit selected-electrode collection.

This distinction is mandatory once diffusion and finite lifetime are introduced.

---

## 4. Staged forward model

The project is intentionally staged so that every added physical layer has a recovery limit.

### Stage A — checked geometry plus stochastic transport

Reuse the already checked 2-D finite-electrode/depletion electrostatic and weighting-potential solver in

```text
numerics/realistic_geometry_closure_stress.py
```

and add a separate stochastic forward layer

```math
d{\bf r}
={\bf v}({\bf r})dt+\sqrt{2D}\,d{\bf W},
```

with an exponential recombination hazard when `tau < infinity`.

Required recovery gates:

1. `D=0`, `tau=infinity` delegates to or reproduces the existing deterministic geometry result rather than defining a new baseline.
2. Every stochastic path satisfies the DC endpoint Ramo telescope to numerical interpolation tolerance.
3. Fixed seeds make the smoke/regression calculation reproducible.
4. Particle-count / step-size convergence is reported before any small closure phase is interpreted scientifically.

Stage A is a **combined-physics seed**, not yet a self-consistent semiconductor solution.

### Stage B — self-consistent semiconductor electrostatics / drift-diffusion

Replace the controlled depletion-like Poisson source with a charge-coupled semiconductor forward problem for at least one explicitly declared detector structure. At minimum the model must document

```text
permittivity;
fixed ionized charge / doping prescription;
carrier statistics used;
contact boundary conditions;
Poisson coupling;
drift mobility / velocity saturation;
diffusion closure;
recombination law;
and convergence tolerances.
```

The weighting potential remains a separate Laplace problem, as required by Shockley--Ramo signal formation.

The Stage B forward model must be validated against analytically soluble limits or an independent numerical formulation before its output is used as evidence.

### Stage C — broad blind regime map

Only after Stages A and B pass their internal gates should a broad regime map be interpreted.

At least one materially different geometry family is required before standalone-paper status is considered. Changing only contact fraction inside the same rectangular pixel does not satisfy that requirement.

---

## 5. Predeclared coordinates

The geometry coordinates inherited from the checked roadmap remain useful:

```math
f_c=W_{contact}/W_{device},
```

```math
\delta_d=W_d/L,
```

```math
\chi_{sc}=V_{sc}/V_{bias},
```

```math
\beta=\sigma_x/(W_{contact}/2),
```

and

```math
\xi=x_0/(W_{contact}/2).
```

The combined-physics map adds transport coordinates such as

```math
Pe_L=\frac{v_*L}{D},
```

```math
Da_L=\frac{L}{v_*\tau},
```

and, where a finite surface/contact transfer time is introduced,

```math
\Theta_c=\frac{v_*\tau_c}{L}.
```

`v_*` must be defined from the forward model for each plotted map; it may not be changed post hoc to improve collapse.

For a two-carrier or two-state extension, use an explicit speed/mobility/lifetime ratio rather than a hidden categorical label whenever possible.

---

## 6. Required outputs at each accepted point

### Forward-only diagnostics

```text
collection fraction by terminal fate;
recombination fraction;
transit-time summary;
maximum DC endpoint-Ramo consistency error;
Poisson / drift-diffusion residual norms where applicable;
mesh, trajectory-step, particle-count, and seed metadata;
forward-model convergence diagnostics.
```

These fields are not exposed to the blind classifier.

### Blind hierarchy outputs

At minimum:

```text
four-color complex closure and phase excess over the declared same-optics reference;
geometry/combined-physics mimic fraction relative to the frozen reference transport signal;
sigma2/sigma1 and sigma3/sigma2 of the six-color first-difference Hankel matrix;
3-sigma second-mode current-step SNR threshold;
warning margin relative to the SNR required for the transport claim;
two-root recurrence residual;
root multiplicity / discriminant diagnostic;
physical root-law admissibility across RF;
final conservative classification.
```

Where the arbitrary-kernel consistency test rather than translated-kernel closure is appropriate, the calibrated kernels must be passed explicitly and the raw geometric identity must not be misrepresented as the physical null.

---

## 7. Statistical discipline

Numerical Monte Carlo noise and measurement noise are different quantities.

The forward solver must first demonstrate that numerical/particle uncertainty is below the scale being interpreted. Only then may synthetic measurement noise be added.

For rank testing near a rank-one boundary, do not rely on a first-order determinant covariance if the derivative vanishes. Use the same null-constrained Monte Carlo / parametric-bootstrap discipline retained by Paper 01.

All headline SNR comparisons must state whether the SNR is

```text
raw-current amplitude SNR,
first-difference SNR,
or another explicitly defined statistic.
```

No threshold may be selected after examining the answer and then described as predeclared.

---

## 8. Frozen comparison signal

Until deliberately superseded by a separately versioned reference, the geometry-mimic comparison uses the existing one-dimensional gradient targets

```text
100 MHz -> -0.011978 deg
500 MHz -> -0.058727 deg
1 GHz   -> -0.110405 deg
```

and the associated current-step amplitude SNR requirements already used by the checked geometry stress.

These are comparison coordinates, not claims that the combined detector should physically reproduce the one-dimensional model.

---

## 9. Predeclared scientific outcomes

### Outcome A — combined physics self-announces

An order-one false transport signature is accompanied by resolvable higher spatial order and/or cross-RF physical-root failure at lower required measurement precision than the mechanism-specific transport claim.

This supports the hierarchy as a conservative falsification protocol under a broader ordinary-physics class.

### Outcome B — combined physics can hide

A broad, numerically converged, physically ordinary region produces an order-one transport-like signal while remaining effectively low-rank and satisfying the tested physical root laws through the precision required for the transport claim.

This is the scientifically strongest warning result. It would require narrowing the Paper 01 interpretation protocol and would be a strong standalone Paper 03 result if it survives an independent geometry family.

### Outcome C — combined effects are small in the tested domain

The added physics does not materially alter the checked geometry warning hierarchy over a broad declared domain.

This is useful validation but is not automatically a standalone paper.

### Outcome D — hierarchy rejects but does not diagnose

The synthetic data robustly produce

```text
rank > 2
mechanism unresolved
```

or another conservative rejection without correct mechanism assignment.

This counts as a successful safety outcome for the hierarchy. The hierarchy is a falsification structure, not a guaranteed mechanism classifier.

---

## 10. GO / NO-GO for a standalone Paper 03

**GO** only if all of the following hold:

1. the forward calculation passes numerical recovery and convergence gates;
2. the blind-analysis contract is respected;
3. Outcome A or B survives a broad physically ordinary parameter domain, not a single hand-picked point;
4. the organizing behavior persists in at least one materially different geometry family;
5. the result has an experimentally actionable consequence stated in observable/SNR terms;
6. a focused primary-source audit does not collapse the contribution into an already standard multidimensional detector-modeling result.

**NO-GO as standalone** if the result is only a narrow sensitivity study of one rectangular finite-contact model, if the apparent effect disappears under numerical refinement, or if the interpretation requires revealing the generating mechanism to the inverse.

---

## 11. Immediate execution order

```text
A1. lock this predeclaration;
A2. add stochastic diffusion/recombination to the checked 2-D geometry as a separate forward layer;
A3. gate D=0 / infinite-lifetime recovery and DC endpoint-Ramo consistency;
A4. expose a mechanism-blind analysis interface;
A5. establish particle/step convergence before interpreting closure-scale effects;
B1. implement and validate one self-consistent Poisson/drift-diffusion detector forward model;
B2. analyze its synthetic spectral/RF currents blindly;
C1. map the declared dimensionless coordinates;
C2. repeat the decisive regime in a materially different geometry family;
C3. only then perform the standalone-manuscript novelty gate and drafting decision.
```

---

## 12. Claim boundary

At creation of this record:

- the earlier deterministic 2-D geometry stress is checked under its stated assumptions;
- the combined stochastic forward model is development work;
- the self-consistent semiconductor Stage B has **not** yet been demonstrated;
- no Paper 03 novelty claim is made;
- no real detector calibration or experimental validation is implied.

Any later result used as evidence must identify the exact source commit, numerical configuration, seed/convergence record, and blind-analysis version.