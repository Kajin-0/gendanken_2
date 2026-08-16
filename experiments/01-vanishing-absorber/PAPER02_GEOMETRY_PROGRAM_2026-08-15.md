# Paper 02 Development Program — Multidimensional Shockley-Ramo Geometry

**Date:** 2026-08-15  
**Status:** **CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN**  
**Manuscript status:** no manuscript yet  
**Relation to Rev. 9:** independent development branch; do not modify or compress the canonical Rev. 9 manuscript while this program is being tested.

## 1. Scientific question

The existing one-dimensional spectral-depth closure hierarchy can be confounded by finite-electrode geometry, curved weighting potential, and nonuniform electrostatic transport fields.

The standalone question is narrower and experimentally actionable:

> **When can multidimensional Shockley-Ramo/electrostatic geometry imitate a one-dimensional spectral transport signature, and when does the geometry reveal itself through increased spatial rank or cross-frequency physical-law failure before a microscopic transport claim becomes statistically significant?**

The paper is only justified if a systematic organizing result survives beyond the existing 75%- and 50%-contact examples.

---

## 2. Existing checked anchor

The present 2-D model solves separate physical and weighting potentials, propagates deterministic saturated-drift trajectories, and accumulates the exact discrete Shockley-Ramo weighting-potential increment

```math
H(\omega|\mathbf r_0)=\int e^{-i\omega t}\,d\phi_w.
```

For collected trajectories the DC response telescopes to

```math
H(0|\mathbf r_0)=1-\phi_w(\mathbf r_0).
```

The refined calculation reported a maximum DC consistency error of approximately

```text
5.4e-15
```

with all sampled trajectories collected.

For the 75%-contact + 3-um depletion stress, the four-color geometry/depletion excess over the planar same-optics baseline was approximately

| RF | excess phase | fraction of reference transport target |
|---:|---:|---:|
| 100 MHz | -0.008841 deg | 0.738 |
| 500 MHz | -0.045827 deg | 0.780 |
| 1 GHz | -0.095513 deg | 0.865 |

The corresponding six-color second-mode threshold at 100 MHz was approximately

```text
84.6 dB current-step amplitude SNR
```

versus approximately

```text
96.1 dB
```

for the current reference transport-gradient claim, giving an approximately

```text
11.5 dB
```

warning margin.

For the 50%-contact stress the warning margin was approximately `24.6 dB`.

These numbers are the regression anchors, not universal claims.

---

## 3. What must be established for a standalone paper

A paper-quality result must answer at least three questions.

### 3.1 How large can the false one-dimensional transport signature become?

Define the four-color phase excess relative to a planar same-optics baseline

```math
\Delta\phi_{\rm geom}(f)
=\phi_{4,\rm geom}(f)-\phi_{4,\rm planar}(f).
```

Normalize it to a declared reference transport signal

```math
M(f)=
\left|
\frac{\Delta\phi_{\rm geom}(f)}
{\phi_{\rm target}(f)}
\right|.
```

`M~1` means geometry can imitate an order-one fraction of the target signal.

### 3.2 Does the same geometry create resolvable extra model order?

For six colors form the `3 x 3` Hankel matrix of first differences and record

```math
R_{21}=\sigma_2/\sigma_1,
\qquad
R_{32}=\sigma_3/\sigma_2.
```

The existing family suggests finite geometry often introduces an additional spatial mode rather than silently preserving strict rank one.

This must be tested over a substantially larger parameter region.

### 3.3 Is the extra mode visible before the microscopic claim?

Let

```math
S_{2,3\sigma}(f)
```

be the raw current-step amplitude SNR required for a 3-sigma second-mode witness and let

```math
S_{\rm claim}(f)
```

be the SNR needed for the reference transport claim.

Define the warning margin

```math
\boxed{
\Delta S(f)=S_{\rm claim}(f)-S_{2,3\sigma}(f).
}
```

Interpretation:

```text
Delta S > 0
-> extra mode is detectable before the transport claim reaches its target precision;

Delta S <= 0
-> geometry may remain unresolved at the precision where the transport claim would otherwise be made.
```

This is the central practical metric for Paper 02.

---

## 4. First sweep coordinates

The first parameterized sweep uses the existing physics and varies the finite-contact/depletion and lateral illumination coordinates.

Dimensionless coordinates to record are

```math
f_c=W_c/W,
```

```math
\delta_d=W_d/L,
```

```math
\chi_{sc}=V_{sc}/V_{bias},
```

```math
\beta=\sigma_x/(W_c/2),
```

```math
\xi=x_0/(W_c/2).
```

The new executable is

```text
numerics/paper02_geometry_parameter_sweep.py
```

It has two tiers.

### Quick tier

```text
contact fraction: 0.75, 0.50
depletion width: 0, 3 um
space-charge drop: 0.05 V when depletion is present
beam sigma: 2 um
beam center: 0, +1 um
```

This is a regression/diagnostic tier.

### Broad tier

```text
contact fraction: 0.875, 0.75, 0.625, 0.50
depletion width: 0, 1.5, 3.0, 4.5 um
space-charge drop: 0.025, 0.05, 0.075 V
beam sigma: 1, 2, 3 um
beam center: 0, 0.75, 1.5 um
```

For zero depletion, the space-charge drop is fixed to zero.

The broad grid is intentionally still bounded. It is a first regime map, not a claim that all realistic detector geometry is represented.

---

## 5. Recorded outputs

Every nonzero RF point records

```text
four-color phase;
planar same-optics phase;
geometry phase excess;
reference transport target;
mimic ratio M;
sigma2/sigma1;
sigma3/sigma2;
3-sigma second-mode SNR threshold;
reference transport-claim SNR;
warning margin Delta S;
imaginary part of the fitted two-root sum;
rank-two recurrence residual;
collection fraction;
exact DC Ramo consistency error;
maximum sampled trajectory time.
```

The script emits both row-level CSV and machine-readable JSON summary.

---

## 6. Predeclared classifications

The classifications below are diagnostic labels, not significance claims.

### Order-one geometry mimic

Use

```math
M\ge0.5
```

as a flag for a geometry contribution at least half as large as the reference transport signal.

This threshold is deliberately simple and can be changed in a later statistical model; it is not a universal physical boundary.

### Early warning

Use

```math
\Delta S>0
```

to indicate that the second-mode witness is predicted to become visible before the transport claim reaches its required SNR.

### Hidden-risk row

Flag

```math
M\ge0.5
\quad\text{and}\quad
\Delta S\le0.
```

Such a row would be scientifically important because it would show a regime where geometry can imitate an order-one transport signature without the present second-mode witness necessarily appearing first.

---

## 7. Required numerical hardening

No manuscript drafting should begin from the coarse sweep alone.

For every extremal or hidden-risk region:

1. rerun at the refined baseline spatial/electrostatic resolution;
2. decrease trajectory step size;
3. increase lateral and depth source quadrature;
4. verify collection fraction;
5. verify DC Shockley-Ramo telescoping to numerical precision;
6. check phase continuity and branch handling;
7. compare against at least one independent numerical formulation if practical.

A useful convergence target is that the geometry excess phase and rank ratios change by less than a few percent under the final refinement, with the exact tolerance reported rather than silently chosen.

---

## 8. Second geometry family required

A standalone paper should not rest on only a centered rectangular finite top electrode.

At least one materially different family must be added, for example

```text
split / neighboring top electrodes;
finite sidewall collection electrode;
non-centered selected electrode;
curved or tapered contact footprint;
explicit laterally varying space-charge region;
finite pixel with neighboring grounded/biased electrodes.
```

The second family is not required to reproduce identical numerical values. It is required to test whether the organizing conclusion is structural or an artifact of one boundary-value problem.

---

## 9. Potential strongest results

### Result A — self-announcing geometry

If essentially all order-one mimic cases satisfy

```math
\Delta S>0
```

with a useful positive margin and fail the next physical root-law rung, the strongest statement would be operational:

> Representative multidimensional geometry can strongly contaminate one-dimensional spectral transport signatures, but the same geometry tends to increase observable spatial model order before the precision required for the microscopic interpretation is reached.

Any word such as `representative` must match the actually tested domain.

### Result B — hidden geometry

If a broad hidden-risk region appears, the stronger result becomes a warning:

> A one-dimensional spectral closure hierarchy can be silently confounded by multidimensional geometry over a quantifiable device/illumination regime, so explicit electrostatic/weighting calibration is required before microscopic transport assignment.

This outcome would require revisiting interpretation language in Paper 01, but it would not invalidate the closure mathematics itself.

### Result C — weak geometry

If order-one mimic cases disappear under broader/refined study, retain the result as validation/support for Paper 01 rather than forcing a second manuscript.

---

## 10. Prior-art gate

Before any novelty statement, audit primary literature for

```text
Shockley-Ramo weighting-field induced timing distortion;
finite-pixel weighting-potential effects in photodiodes/APDs;
geometry-induced apparent carrier transit-time dispersion;
position-dependent photodiode frequency response;
weighting-field corrections to transient-current technique;
model-order / modal diagnostics of detector geometry;
spectral-depth or wavelength-resolved timing under finite electrode geometry.
```

The candidate claim is not that weighting fields matter. That is established.

The possible distinct contribution is the **quantitative relationship between a false spectral-transport signature, spectral model order, and the SNR at which the geometry confound becomes detectable**.

Priority remains open until that narrower statement is audited.

---

## 11. Manuscript go/no-go

A Paper-02 manuscript is recommended only after all of the following are true:

```text
[ ] broad parameter sweep completed;
[ ] extremal regions numerically refined;
[ ] at least one second geometry family tested;
[ ] hidden-risk/self-announcing classification stabilized;
[ ] closest prior art read directly;
[ ] claim ledger written;
[ ] no conflict with or duplicate extraction from Rev. 9;
[ ] reproducible scripts and machine-readable sweep outputs preserved.
```

Until then the status remains

> **CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN.**