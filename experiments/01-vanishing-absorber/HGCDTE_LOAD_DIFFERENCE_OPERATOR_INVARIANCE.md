# Optical-Load Differencing Does Not Create New Spatial Rank

**Date:** 2026-08-09  
**Status:** exact operator result under load-independent optical kernels; clarifies the role of load curvature; no novelty claim

## 1. The question

The optical-load curvature observable is attractive because it cancels the static A/B baseline and load-linear phase terms.

But cancellation of nuisance terms is not the same thing as gaining new spatial information.

The key question is:

> **If changing optical load leaves the normalized wavelength-dependent generation kernel unchanged, does measuring several load states create a new depth operator?**

The answer is **no**.

---

## 2. One device at one load

For wavelength index `i` and load coordinate `P`, write the orientation-correct mean-delay observable as

```math
\boxed{
T_i(P)
=\int_0^L K_i(s)q(s,P)ds,
}
```

or discretely

```math
\boxed{
\mathbf T(P)
=\mathbf A\mathbf q(P).
}
```

Assume the normalized optical kernel is independent of load over the chosen range:

```math
\boxed{
\mathbf A(P)=\mathbf A.
}
```

This is the same conditional assumption required for clean optical-load subtraction.

---

## 3. Any linear load difference commutes with the spatial operator

Let a load-difference operator use coefficients `c_k` on measurements at load states `P_k`:

```math
\Delta_P\mathbf T
=\sum_k c_k\mathbf T(P_k).
```

Then

```math
\Delta_P\mathbf T
=\sum_k c_k\mathbf A\mathbf q(P_k)
```

and therefore exactly

```math
\boxed{
\Delta_P\mathbf T
=
\mathbf A
\left[
\sum_k c_k\mathbf q(P_k)
\right].
}
```

Define

```math
\Delta_P\mathbf q
=\sum_k c_k\mathbf q(P_k).
```

Then

```math
\boxed{
\Delta_P\mathbf T
=\mathbf A\Delta_P\mathbf q.
}
```

Thus the load-differenced transport profile is measured by **the same wavelength-to-depth matrix `A`** as the static profile.

---

## 4. The second load difference has exactly the same spatial operator

For equally spaced load states,

```math
C_P\mathbf T
=
\mathbf T(P_+)-2\mathbf T(P_0)+\mathbf T(P_-).
```

Therefore

```math
\boxed{
C_P\mathbf T
=\mathbf A
\left[
\mathbf q(P_+)-2\mathbf q(P_0)+\mathbf q(P_-)
\right].
}
```

Or

```math
\boxed{
C_P\mathbf T
=\mathbf A\,C_P\mathbf q.
}
```

The curvature observable changes **what transport state is being estimated**, not the optical spatial operator that estimates it.

Consequences:

```text
same singular vectors
same singular values up to measurement weighting
same wavelength-limited spatial bandwidth
same near-boundary gauge
same point-spread limitations.
```

Load curvature does not turn a few-mode spectral encoder into high-resolution tomography.

---

## 5. General load-basis formulation

Suppose the transport profile is expanded in load basis functions

```math
\mathbf q(P)
=
\sum_{m=0}^{M-1}
b_m(P)\mathbf q_m.
```

At load states `P_k`, stack all measurements.

Let

```math
B_{km}=b_m(P_k).
```

Then the full load × wavelength forward operator is the Kronecker product

```math
\boxed{
\mathbf G
=\mathbf B\otimes\mathbf A.
}
```

Therefore

```math
\boxed{
\operatorname{rank}(\mathbf G)
=
\operatorname{rank}(\mathbf B)
\operatorname{rank}(\mathbf A).
}
```

Load diversity can identify **several different load-response profiles** `q_m`, but every one of those profiles is observed through the same spatial bandwidth of `A`.

It multiplies the number of transport states; it does not improve the intrinsic depth resolution of each state.

---

## 6. Singular-value consequence

For a Kronecker product, the singular values satisfy

```math
\boxed{
\sigma(\mathbf B\otimes\mathbf A)
=
\{\sigma_j(\mathbf B)\sigma_k(\mathbf A)\}_{j,k}.
}
```

So any weak spatial singular direction of `A` remains weak in every load-order block.

A well-conditioned load basis cannot repair a poorly conditioned spatial mode.

This is the exact linear-algebra reason why

```text
more load states
```

cannot by themselves cure the near-junction gauge or create new depth resolution.

---

## 7. Paired A/B load curvature retains the A/B overlap problem

For simultaneous paired data,

```math
D(P)
=
\mathbf A_A\mathbf q_A(P)
-
\mathbf A_B\mathbf q_B(P).
```

Applying any load-difference operator gives

```math
\boxed{
\Delta_P D
=
\mathbf A_A\Delta_P\mathbf q_A
-
\mathbf A_B\Delta_P\mathbf q_B.
}
```

Therefore the response-geometry overlap previously found between smooth A and B spectral modes does not disappear merely because the data are load differentiated.

If both A and B are allowed arbitrary smooth nonlinear load-response profiles, their separation remains poorly conditioned.

The load experiment needs a physical/control assumption such as

```text
sample B load curvature is small or independently constrained
```

or an additional observable that distinguishes the two mechanisms.

---

## 8. What load curvature actually buys

The value of the curvature construction is **nuisance rejection**, not spatial-rank creation.

It can cancel

```text
static A/B transport baselines
load-independent phase offsets
terms linear in load
and, after wavelength differencing, wavelength-independent nonlinear chain curvature.
```

That can make a *change profile*

```math
C_P\mathbf q
```

far easier to estimate than the absolute static profile.

But once that change profile is defined, its spatial reconstruction is still subject to the same wavelength kernel physics.

---

## 9. Important implication for the project

The load-curvature branch should not be described as adding a new tomographic dimension in the low-frequency linear inverse.

The correct description is:

> **optical load provides a causal state perturbation that can cancel static nuisance transport, while wavelength remains the spatial-encoding coordinate.**

This distinction matters for novelty and experimental design.

The contribution cannot be

```text
load dimension increases tomography rank.
```

That statement is false under load-independent kernels.

---

## 10. How a genuinely new spatial operator can arise

Additional independent depth information requires at least one ingredient that changes the spatial kernel itself, for example

```text
a different optical illumination geometry
a physically different absorption kernel
or
finite-RF complex timing weights that depend on accumulated baseline transit phase.
```

The last option is already compatible with the project's original wavelength × RF direction.

At finite RF frequency, for deterministic conditional transit time `T(x)`,

```math
H_i(\Omega)
=
\int p_i(x)e^{-i\Omega T(x)}dx.
```

A small local transport perturbation then carries a complex frequency-dependent sensitivity kernel rather than the zero-frequency survival kernel.

Therefore **RF-frequency diversity**, unlike simple load differencing, can in principle alter the effective spatial Jacobian.

Whether it adds enough independent information to matter experimentally must be checked numerically.

---

## 11. Next decisive calculation

Use the current sample-A/B optical models and an explicit baseline transport scale to construct the finite-frequency complex Jacobian

```math
\frac{\partial\ln H_i(\Omega)}{\partial q_j}
```

for wavelength × RF data.

Then compare

```text
low-frequency phase-only response geometry
vs
multi-RF complex response geometry
```

for the A-localized nonlinear-region change and smooth A/B nuisance modes.

The useful question is not whether RF gives more data points.

It is:

> **Does finite-frequency complex weighting rotate the spectral/spatial response enough to break the degeneracy that survives wavelength-only phase measurements?**
