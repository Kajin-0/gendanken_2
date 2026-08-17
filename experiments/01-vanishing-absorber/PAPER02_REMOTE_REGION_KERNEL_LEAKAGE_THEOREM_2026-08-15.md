# Remote-region finite-kernel leakage theorem

**Date:** 2026-08-15  
**Status:** **DERIVED / PRIORITY UNPROVEN**  
**Purpose:** formalize how a transport/electrostatic perturbation spatially outside the nominal source centers can enter a calibrated spectral-depth measurement through finite optical generation support while producing little one-mode residual.

## 1. Setup

At a fixed RF frequency let the true point-source terminal-current response be

```math
H(z)=H_0(z)+\delta H(z),
```

where the reference one-mode response is

```math
H_0(z)=A+B e^{rz}.
```

Let the nuisance region be `R` and suppose

```math
\delta H(z)=0\qquad z\notin R.
```

For normalized calibrated generation kernel `g_m(z)`, the measured spectral channel is

```math
J_m=\int g_m(z)H(z)\,dz.
```

Define

```math
M_m(r)=\int g_m(z)e^{rz}\,dz.
```

Then exactly

```math
\boxed{
J_m=A+B M_m(r)+E_m,
}
```

with nuisance leakage

```math
\boxed{
E_m=\int_R g_m(z)\delta H(z)\,dz.
}
```

This identity is elementary but operationally important: **a nuisance region need not contain the mean or nominal center of any optical channel to influence the spectral-depth inversion. Nonzero kernel support in that region is sufficient.**

---

## 2. Zero-overlap invariance

Let

```math
p_m=\int_R g_m(z)\,dz
```

be the generation probability overlapping the nuisance region.

If

```math
p_m=0
```

for every channel, then

```math
E_m=0
```

for every channel and the exact calibrated one-mode sequence is recovered regardless of how complicated `\delta H` is inside `R`.

Hence:

```math
\boxed{
\operatorname{supp}(g_m)\cap R=\varnothing\ \forall m
\quad\Longrightarrow\quad
\text{remote nuisance is invisible to the spectral channels.}
}
```

This is stronger than saying that the kernel means lie outside `R`.

---

## 3. Leakage bound

For nonnegative normalized generation kernels,

```math
|E_m|
\le
p_m\,\|\delta H\|_{\infty,R}.
```

Therefore

```math
\boxed{
|E_m|\le p_m H_R,
\qquad
H_R\equiv\sup_{z\in R}|\delta H(z)|.
}
```

The overlap probability sets a strict channel-by-channel upper envelope on the remote nuisance contribution.

Small overlap does not by itself guarantee small inferred-parameter bias, because inversion conditioning can amplify a small `E_m`.

---

## 4. First-order bias versus residual

Collect the channels into a complex vector

```math
\mathbf J=\mathbf f(\theta)+\mathbf E,
```

where a local parameterization of the calibrated one-mode model is

```math
\theta=(A,B,r).
```

Linearize about the reference point:

```math
\mathbf f(\theta+\delta\theta)
\simeq
\mathbf f(\theta)+\mathcal J\,\delta\theta.
```

For an appropriate real-stacked or complex weighted least-squares representation, let `P_T` be the projection onto the model tangent space `col(J)`.

Then to first order

```math
\boxed{
\mathbf E_T=P_T\mathbf E
}
```

drives fitted parameter bias, while

```math
\boxed{
\mathbf E_N=(I-P_T)\mathbf E
}
```

drives the one-mode goodness-of-fit residual.

In particular, the root bias is the `r` component of the pseudoinverse solution

```math
\delta\theta=\mathcal J^+\mathbf E
```

under the chosen noise metric.

Thus a remote nuisance can strongly bias the recovered spatial exponent while producing a very small rank/model residual if its finite-kernel leakage vector is nearly tangent to the calibrated one-mode manifold.

This is the arbitrary-kernel version of the earlier discrete tangent-confound theorem.

---

## 5. Why variation across channels matters

If all channels had identical kernel overlap and sampled exactly the same nuisance contribution, the resulting common-mode term could often be absorbed mainly into the fitted offset/amplitude parameters.

Transport-like root bias requires a channel-dependent component of

```math
E_m=\int_R g_m(z)\delta H(z)dz.
```

Such dependence can arise through

- different overlap probabilities `p_m`;
- different shapes within `R` even at equal `p_m`;
- frequency-dependent phase of `\delta H(z,\omega)` across the nuisance region.

Therefore the natural optical nuisance coordinates are not only mean generation depth and width, but the set of **restricted kernel moments inside the electrostatic region**.

At minimum:

```math
p_m=\int_R g_m(z)dz,
```

```math
\mu_{R,m}=\frac{1}{p_m}\int_R z g_m(z)dz,
```

and higher restricted moments when required.

---

## 6. Spatially remote electrostatic region

The current conditional example has

```text
absorber thickness      L = 7.6 um
depletion width         Wd = 3.0 um
nuisance boundary       zd = 4.6 um
nominal source means        2.0--4.5 um
```

Ideal point sources at all six nominal depths give

```math
D_{\rm eff}\simeq1.7\times10^{-12}\ {\rm m^2/s}\approx0.
```

Actual finite calibrated kernels with the same nominal mean-depth range give

```math
D_{\rm eff}\simeq2.61\times10^{-3}\ {\rm m^2/s}.
```

Point sources placed inside the depletion region give

```math
D_{\rm eff}\simeq4.87\times10^{-3}\ {\rm m^2/s}.
```

This is precisely the ordering predicted by the support-based leakage picture.

The pending kernel-tail ablation is the direct causal test: set the kernel mass inside `R` to zero while using the exact modified kernels in both forward and inverse models.

---

## 7. Distinction from ordinary optical-kernel calibration

Calibrating the full kernel `g_m(z)` is necessary but not sufficient to remove this confound.

Kernel calibration prevents a false residual caused merely by pretending that finite, shape-evolving kernels are delta functions or rigid translations.

It does **not** make the underlying point-source transport response homogeneous.

If the true `H(z)` changes functional form inside the support of a calibrated kernel, the measured integral still contains that physics:

```math
J_m=\int g_m H\,dz.
```

The calibrated one-mode model can reject the data only to the extent that the resulting leakage vector has a component normal to its model manifold.

Therefore:

> **Exact knowledge of the optical generation kernels solves the optical forward-model error, but it cannot by itself identify whether the spatial response being averaged belongs to the assumed material-transport model.**

---

## 8. Design implication

A spectral-depth experiment intended to attribute a recovered parameter to bulk material transport should avoid relying only on the nominal source means.

A more relevant design criterion is to bound the entire calibrated kernel overlap with known nuisance regions:

```math
p_{m,R}=\int_R g_m(z)dz.
```

If the nuisance response can be bounded by `H_R`, then the channel-level systematic is bounded by `p_{m,R}H_R` before inversion conditioning.

A complete attribution bound would combine

1. restricted kernel overlap;
2. a physical bound on `\delta H` in the nuisance region;
3. the noise-weighted inverse Jacobian mapping channel systematic error into transport-parameter bias.

This suggests a possible practical theorem/design rule for the eventual Paper 02.

---

## 9. What remains open

The present theorem establishes the exact leakage decomposition and the zero-overlap invariance, but not a publication-level novelty claim.

Next requirements:

1. complete the direct depletion-tail ablation;
2. determine the physical `p_m` values for the six HgCdTe kernels;
3. measure how `D_eff` scales as overlap is continuously varied;
4. derive a quantitative first-order `D_eff` bias formula from the restricted kernel moments and the one-mode inverse Jacobian;
5. audit partially depleted absorber / wavelength-dependent impulse-response literature for an equivalent inverse-identifiability result.
