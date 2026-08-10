# Short-Wave Finite-RF Complex Jacobian — RF Diversity Rotates the Spatial Kernel but Does Not Remove the A/B Degeneracy

**Date:** 2026-08-09  
**Status:** conditional deterministic-baseline finite-frequency Jacobian over the 72-member sample-A profile family; illustrative A-localized change; no calibrated transport or covariance; no novelty claim

## 1. Why RF frequency is different from simple load differencing

For load-independent optical kernels, any linear load difference commutes with the wavelength-to-depth matrix:

```math
\Delta_P\mathbf T
=\mathbf A\Delta_P\mathbf q.
```

So load diversity does not create a new low-frequency spatial operator.

Finite RF frequency is different.

For deterministic front-directed transit time `T_0(z)`, the complex response is

```math
\boxed{
H_i(\Omega)
=
\int p_i(z)e^{-i\Omega T_0(z)}dz.
}
```

A small local delay-density perturbation `delta q(s)` changes the conditional transit time of every carrier generated downstream of `s`.

Therefore the first-order complex response is

```math
\delta\ln H_i(\Omega)
=
\int J_i(s,\Omega)\delta q(s)ds,
```

with

```math
\boxed{
J_i(s,\Omega)
=
-\frac{i\Omega}{H_i(\Omega)}
\int_{z\ge s}
 p_i(z)
 e^{-i\Omega T_0(z)}dz.
}
```

More precisely, after cell integration the inner integral contains the path length through each spatial cell.

In the low-frequency limit,

```math
J_i(s,\Omega)
\to
-i\Omega S_i(s),
```

recovering the survival-kernel mean-delay inverse.

At finite frequency, however, the factor

```math
e^{-i\Omega T_0(z)}
```

rotates different generation depths differently.

Thus RF frequency can genuinely change the effective spatial Jacobian.

---

## 2. Conditional baseline used for the test

Use an explicitly illustrative deterministic baseline

```math
v_0=10^5\ {\rm m/s},
```

so

```math
q_0=10\ {\rm ps/um}
```

and

```math
T_0(z)=q_0 z.
```

Use

```text
300 K
2.00-2.80 um
0.01 um wavelength spacing
80 spatial cells
Hansen gap
Moazzami Beer-Lambert absorption
all 72 sample-A sensitivity profiles
central sample-B envelope.
```

The illustrative A-localized change is the same support-shaped `25%` transport perturbation used in the preceding short-wave visibility work.

This remains a scale test, not a prediction of sample A.

---

## 3. Smooth nuisance coordinates

For each sample-A profile:

1. construct the low-frequency short-wave timing matrix;
2. take its first three smooth spatial right-singular modes;
3. do the same for the central sample-B matrix;
4. propagate those six physical spatial modes through the finite-RF complex Jacobian.

The candidate A-localized change is also propagated through the same Jacobian.

At every RF frequency, remove an arbitrary wavelength-independent response separately before comparing shapes.

This is conservative with respect to residual common electrical/path terms.

---

## 4. Compare 1 GHz phase-only to multi-RF complex data

Two measurement designs are compared.

### Single-frequency phase-only

```text
1 GHz
phase versus wavelength only.
```

### Multi-frequency complex

```text
0.25, 0.50, 1.0, 2.0, 3.0 GHz
phase + log-magnitude versus wavelength.
```

The multi-RF set is still inside a relatively mild optical-only response envelope for the short-wave A family:

```math
\boxed{
\min |H_A|\approx0.9815
}
```

through `3 GHz` for the stated deterministic baseline.

That does not include stochastic carrier or electrical bandwidth loss.

---

## 5. Finite RF does rotate the target away from the nuisance subspace

Use the principal angle from the A-localized response vector to the six-dimensional smooth A/B nuisance span.

### `1 GHz` phase-only

Across the 72 A profiles:

```math
\boxed{
\theta
=0.028^\circ
\text{ to }
0.571^\circ
}
```

with median

```math
\boxed{0.052^\circ.}
```

This reproduces the severe near-degeneracy seen in the wavelength-only calculations.

### `0.25-3 GHz` phase-only

The median angle increases to approximately

```math
0.21^\circ.
```

### `0.25-3 GHz` full complex response

Using both phase and log-magnitude:

```math
\boxed{
\theta
=0.050^\circ
\text{ to }
1.36^\circ
}
```

with median

```math
\boxed{0.64^\circ.}
```

Thus the median geometric separation is roughly

```math
\boxed{12\times}
```

larger than for `1 GHz` phase-only data.

This is a real gain in response geometry.

---

## 6. But the absolute separation remains very small

A principal angle of

```math
0.64^\circ
```

corresponds to only about

```math
\sin(0.64^\circ)\approx1.1\%
```

of the target norm lying outside the arbitrary smooth A/B nuisance span.

For the least favorable A profiles the multi-RF complex angle remains only about

```math
0.05^\circ,
```

or a residual fraction below

```math
10^{-3}.
```

Therefore the RF-induced rotation is not remotely large enough to make a fully unconstrained smooth A/B decomposition stable.

---

## 7. Fixed-time no-prior detection remains poor

For an illustrative comparison, assume

```text
0.10 degree numerical RMS noise for phase
and the same numerical RMS in log-magnitude
```

for the one-frequency reference.

When the same total coherent-time resource is split equally across the five RF frequencies, per-point noise is increased by `sqrt(5)`.

After projecting out all six smooth A/B nuisance modes:

### `1 GHz` phase-only

Illustrative no-prior SNR is approximately

```text
0.002-0.10
median ~0.004.
```

### `0.25-3 GHz` complex

```math
\boxed{
\mathrm{SNR}
\approx0.013-0.41
}
```

with median

```math
\boxed{0.090.}
```

The exact numerical values should not be treated as an instrument prediction because real phase/magnitude covariance has not been measured.

The important result is qualitative and robust:

> **finite-RF complex data improve the geometry materially, but a no-prior fit remains deeply noise dominated.**

---

## 8. Why the result matters

The project had two possible interpretations of RF diversity.

### Overoptimistic interpretation

```text
full complex wavelength x RF data
-> enough independent information to remove smooth A/B ambiguity automatically.
```

The present calculation rejects that interpretation for the current deterministic baseline and RF range.

### Corrected interpretation

```text
RF diversity rotates the spatial Jacobian
-> improves conditioning
-> helps test transport models
but
-> does not substitute for physical constraints / calibration.
```

This is more defensible.

---

## 9. Why simply pushing to still higher RF is not an obvious solution

Higher RF increases accumulated transit phase and can rotate the Jacobian further.

But it simultaneously increases sensitivity to

```text
electrical poles
package parasitics
carrier stochastic broadening
amplitude loss
and full-transfer-model error.
```

The separate load-curvature electrical analysis already shows that phase de-embedding becomes stringent as the measurement approaches the detector/readout pole.

Therefore arbitrarily high RF cannot be invoked as a free conditioning resource.

The useful frequency range must be selected from measured complex transfer and covariance.

---

## 10. Important conceptual consequence

The strongest candidate is no longer a completely model-free reconstruction of arbitrary A and B transport profiles.

The data geometry supports a narrower goal:

> **estimate a few physically constrained differential transport modes and test whether an additional A-specific component is required.**

This is consistent with the existing calibration-first and control/contrast architecture.

RF frequency is valuable because it can help falsify a proposed physical mode through its complex frequency signature.

It does not make the inverse pointwise or absolute.

---

## 11. What remains conditional

This calculation assumes

- deterministic baseline transit at `v_0=1e5 m/s`;
- a local additive delay perturbation;
- current Hansen/Moazzami optical kernels;
- the current 72-member A profile family;
- three smooth A and three smooth B nuisance modes;
- linearized `delta ln H` response;
- equal numerical phase/log-magnitude noise for the illustrative SNR comparison;
- no electrical transfer function.

A real high-field/nonlocal HgCdTe transport model can produce additional frequency structure.

That structure would be **physical-model information**, not generic inverse rank.

---

## 12. Next research consequence

Do not keep adding generic measurement dimensions hoping the degeneracy disappears.

The project should now distinguish two things explicitly:

```text
nonparametric spatial inversion
-> intrinsically few-mode and strongly degenerate near the boundary

physical hypothesis testing
-> can use wavelength + RF + A/B + perturbations to test a small number of specific transport mechanisms.
```

The next useful numerical branch is therefore to compare a **localized nonlinear-region transport hypothesis** against a small set of physically motivated alternative nuisance mechanisms rather than against arbitrary smooth A/B functions.

That is the level at which the experimental controls may become decisive.

Numerical implementation:

`numerics/hgcdte_shortwave_finite_rf_jacobian.py`
