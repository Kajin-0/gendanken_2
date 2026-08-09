# HgCdTe Spectral Timing Linear Inverse — Reconstructing Delay Density Without Differentiating Noisy Data

**Date:** 2026-08-09  
**Status:** exact linear-operator formulation under a path-additive mean-delay model with known optical generation kernels; collection-boundary orientation and common-delay identifiability corrected; no novelty claim

## 1. Purpose

The pointwise relation

```math
v_{\rm eff}=1/[G(dT/dE_\gamma)]
```

is useful in a sharp-generation limit, but numerical differentiation amplifies noise and finite optical depth spatially averages the measurement.

A more general formulation is linear in the local **delay density**

```math
\boxed{q(x)=1/v_{\rm eff}(x).}
```

The wavelength-resolved mean-delay data then form a linear inverse problem for `q(x)`.

The timing kernel depends on **which boundary collects the carrier**.

---

## 2. Generation distribution

For wavelength / photon-energy index `i`, let

```math
\boxed{
p_i(x)=p(x|E_{\gamma,i},{\rm abs})
}
```

be the normalized conditional generation-position density:

```math
\int_0^L p_i(x)dx=1.
```

It may come from Beer-Lambert absorption, transfer-matrix/FDTD optics, or a measured calibrated optical model.

Define the conditional CDF

```math
\boxed{
F_i(s)=P(X_g\le s)=\int_0^s p_i(x)dx.
}
```

and survival function

```math
\boxed{
S_i(s)=P(X_g\ge s)=1-F_i(s).
}
```

---

## 3. Collection at the downstream boundary `L`

If every generated carrier moves toward `x=L`, then

```math
\boxed{
T_L(x)=\int_x^L q(s)ds.
}
```

The wavelength-dependent mean delay is

```math
\bar T_{L,i}
=\int_0^L p_i(x)
\left[
\int_x^L q(s)ds
\right]dx.
```

Swap the integration order:

```math
\boxed{
\bar T_{L,i}
=\int_0^L F_i(s)q(s)ds.
}
```

Thus the downstream-collection timing kernel is

```math
\boxed{K_{L,i}(s)=F_i(s).}
```

A delay element at `s` contributes only when the carrier was generated upstream of it.

---

## 4. Collection at the entrance boundary `0`

For a front-side junction, as in the 2023 published graded-HgCdTe sample-B geometry, the carrier instead returns toward `x=0`.

Then

```math
\boxed{
T_0(x)=\int_0^x q(s)ds.
}
```

and

```math
\bar T_{0,i}
=\int_0^L p_i(x)
\left[
\int_0^x q(s)ds
\right]dx.
```

Swapping integrals gives

```math
\boxed{
\bar T_{0,i}
=\int_0^L S_i(s)q(s)ds.
}
```

Therefore the front-collection kernel is

```math
\boxed{K_{0,i}(s)=S_i(s)=1-F_i(s).}
```

A delay element at depth `s` contributes only when the photon was generated at or beyond that depth.

This correction is essential when instantiating the inverse on a real device.

---

## 5. Unified linear operator

For either one-boundary geometry, write the appropriate timing kernel as

```math
K_i(s).
```

Then

```math
\boxed{
\bar T_i
=\int_0^L K_i(s)q(s)ds.
}
```

Discretize the device into cells `j` and integrate the kernel over each cell:

```math
\boxed{
A_{ij}
=\int_{x_{j-1}}^{x_j}K_i(s)ds.
}
```

This cell-integrated form is preferable to simply evaluating `K_i` at a cell edge.

The discrete forward model is

```math
\boxed{
\mathbf T=\mathbf A\mathbf q.
}
```

If `q_j>0`, a local effective velocity may be reported as

```math
\boxed{v_{\rm eff}(x_j)=1/q_j.}
```

subject to the path-additive interpretation.

---

## 6. Important correction — a common timing offset is not generically identifiable

Suppose the measured timing data contain a wavelength-independent common delay `c`:

```math
\boxed{
\mathbf T^{\rm meas}
=\mathbf A\mathbf q+c\mathbf1.
}
```

It is algebraically possible to append a constant column,

```math
[\mathbf A\ \mathbf1],
```

but this does **not** guarantee that `c` and all components of `q` are uniquely separable.

For front collection,

```math
S_i(0)=1
```

for every wavelength.

For downstream collection,

```math
F_i(L)=1
```

for every wavelength.

Therefore transport concentrated arbitrarily close to the collecting boundary produces an approximately wavelength-independent delay and becomes degenerate with `c`.

In a finite discretization, the boundary-cell column can be strongly correlated with the constant column.

Hence the earlier statement

```text
"the common delay can simply be estimated simultaneously"
```

was too strong.

The safe statement is

> **spectral timing determines wavelength-dependent / differential transport modes. A wavelength-independent boundary/common component requires calibration, a gauge constraint, or a physical prior.**

---

## 7. Practical ways to fix the delay gauge

A real inversion should use at least one of the following:

### Differential timing

Choose a reference wavelength and use

```math
\Delta T_i=T_i-T_{\rm ref}.
```

The common delay cancels exactly, but the absolute spectrally invariant transport component is also removed.

### Independent common-delay calibration

Measure or model the electronics/optical common group delay separately.

### Boundary condition / transport prior

Constrain the delay density near the collection boundary using independent transport information.

### Parametric transport model

Fit a lower-dimensional physical model whose constant-delay component is separately defined.

Regularization by itself may select one decomposition of `q` and `c`, but that choice is not evidence that the decomposition is physically unique.

---

## 8. Regularized inversion

The kernel matrix is generally ill conditioned because neighboring wavelength kernels overlap strongly.

A smoothness-regularized estimate may use

```math
\boxed{
\hat{\mathbf q}
=\arg\min_{\mathbf q}
\left\|
\mathbf A_\Delta\mathbf q-\mathbf T_\Delta
\right\|_2^2
+
\lambda
\left\|
\mathbf D_2\mathbf q
\right\|_2^2,
}
```

where the subscript `Delta` indicates either differential data or a system projected orthogonal to the common-delay mode.

Physical constraints may impose

```math
q_j>0.
```

Other defensible choices include Bayesian smoothness priors, total variation for sharp interfaces, or a lower-dimensional transport parameterization.

No regularizer is universally optimal.

---

## 9. Sharp-generation limit

For downstream collection, if

```math
p_i(x)\to\delta(x-x_g),
```

then

```math
F_i(s)\to H(s-x_g),
```

and

```math
\bar T_L(E_\gamma)
=\int_{x_g(E_\gamma)}^Lq(s)ds.
```

For a linear gap with

```math
x_g=(E_{g,\rm in}-E_\gamma)/G,
```

```math
\boxed{
G\frac{d\bar T_L}{dE_\gamma}
=q[x_g(E_\gamma)].
}
```

For front collection, the sign/orientation changes consistently because

```math
\bar T_0(E_\gamma)
=\int_0^{x_g(E_\gamma)}q(s)ds.
```

The pointwise derivative formula is therefore only a special limit of the correct orientation-dependent integral operator.

---

## 10. Identifiability and spatial rank

The inverse requires sufficiently diverse wavelength kernels.

If all wavelengths generate the same spatial distribution, the rows of `A` are nearly identical and no internal profile can be reconstructed.

Even with strongly wavelength-dependent generation, the optical kernels are smooth, so only a finite number of spatial modes are well conditioned.

The relevant questions are therefore

```text
How many singular modes survive the experimental noise floor?
Which spatial combinations do those modes represent?
Which modes are lost to the common-delay gauge?
```

The number of wavelength samples is **not** the number of recoverable spatial degrees of freedom.

---

## 11. Spatial resolution

Resolution is controlled jointly by

- optical generation-kernel width;
- wavelength grid and source linewidth;
- uncertainty in `E_g(x)` / composition profile;
- timing or RF-phase precision;
- common-delay calibration;
- regularization;
- nonlocal carrier transport.

Thus the method is a **band-limited transport tomography**, not arbitrary microscopic imaging.

---

## 12. Relation to the synthetic regressions

Earlier synthetic regressions appended a common constant and recovered it numerically under smoothness regularization.

Those tests remain useful demonstrations that a regularized solver can reproduce the imposed synthetic profile.

However, the apparent recovery of the common constant should **not** be interpreted as proof of structural identifiability.

The regularizer and discretization choose one solution from a nearly degenerate family.

Future regressions should report differential-profile recovery separately from absolute common-delay recovery.

---

## 13. Experimental observable

Low-frequency differential phase is particularly natural:

```math
\Delta T
\simeq
-\frac{\Delta\phi}{\Omega}.
```

A wavelength-independent electronic or optical delay cancels in the phase difference.

This aligns the observable with what the inverse can identify most robustly: **spectrally varying internal transport**.

A wavelength-dependent optical-path or electronic phase must still be calibrated because it can masquerade as transport structure.

---

## 14. Reviewer-level significance test

Wavelength-dependent carrier generation and response time are established photodiode physics.

The scientific value of this method, if any, must come from demonstrating useful inverse metrology beyond ordinary bandwidth comparison:

- reconstructing a nonuniform transport profile;
- detecting a buried slow or broadening region;
- validating against localized excitation or microscopic transport;
- extracting several internal transport modes from real wavelength-resolved complex response data.

The calculus identity itself is not the contribution.

---

## 15. Claim boundary

### DERIVED

For collection at `L`,

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q(s)ds.
}
```

For collection at `0`,

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q(s)ds.
}
```

### DERIVED IDENTIFIABILITY LIMIT

A wavelength-independent delay component is not generically separable from arbitrary delay density near the collection boundary without extra information.

### CONDITIONAL

- path-additive mean delay;
- known/calibrated optical generation kernels;
- one-boundary transport geometry;
- local interpretation `q=1/v_eff`;
- sufficient kernel diversity.

### NOT ESTABLISHED

- absolute boundary delay without calibration/prior;
- experimental stability in HgCdTe;
- unique high-resolution reconstruction for arbitrary profiles;
- novelty / priority.

---

## 16. Next decisive work

Use the **published 2023 sample-B dimensional matrix** rather than another normalized toy problem.

Quantify reconstruction versus

```text
0.1-1 degree RF phase noise
+
unknown common phase
+
real Moazzami optical kernels
+
several smooth transport modes.
```

Judge success on recovery of differential transport structure, not on artificial recovery of an uncalibrated absolute common delay.
