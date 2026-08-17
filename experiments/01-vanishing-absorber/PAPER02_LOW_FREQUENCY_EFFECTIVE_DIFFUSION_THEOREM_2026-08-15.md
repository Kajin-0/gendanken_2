# Low-frequency effective-diffusion equivalence

**Date:** 2026-08-15  
**Status:** **DERIVED / CANDIDATE DISTINCT APPLICATION — PRIORITY UNPROVEN**  
**Scope:** local identifiability of the recovered one-mode spatial exponent. The algebra below is general; no novelty claim is made until a focused prior-art audit is completed.

## 1. Why this note exists

A fine-resolution 2-D Shockley-Ramo calculation produced a surprising but reproducible result.

The simulated planar device contains a 3.0 um space-charge/depletion region with a 0.05 V electrostatic drop. Carrier trajectories are deterministic: the trajectory model contains **no diffusion and no recombination**. Nevertheless, when the wavelength-resolved terminal-current responses are reduced to a one-mode spatial exponent and that exponent is fit to the homogeneous drift-diffusion law, the inversion returns a positive apparent diffusion coefficient.

The effect survives the calibrated finite-optical-kernel one-mode fit used by the Rev. 9 logic.

At 100 MHz the kernel-aware one-RF inversion returns approximately

```math
D_{\rm eff}=2.610\times10^{-3}\ {\rm m^2/s},
\qquad
w_{\rm eff}=2.570\times10^4\ {\rm m/s},
```

even though the simulation truth is `D=0`.

Using those parameters, the homogeneous physical-law residual remains below 1% through 1 GHz.

This note explains why that is possible without any numerical coincidence.

---

## 2. Local expansion of an arbitrary recovered exponent

Let `gamma(omega)` denote the spatial exponent recovered from the spectral channels after whatever exact optical-kernel calibration is required.

Assume only that, near DC,

1. `gamma(omega)` is analytic in `omega`;
2. the real time-domain response gives the usual conjugate symmetry;
3. the downstream DC exponent `gamma_0=gamma(0)` is finite.

Write

```math
\delta\gamma(\omega)=\gamma(\omega)-\gamma_0.
```

Under the Fourier-sign convention used in the Paper-02 numerical tests,

```math
\delta\gamma(\omega)
=-i a_1\omega+a_2\omega^2+i a_3\omega^3+O(\omega^4),
```

with real coefficients `a_j` when the local symmetry assumptions hold.

The coefficients need not originate from microscopic diffusion. They are simply the local frequency derivatives of the experimentally recovered spatial exponent.

---

## 3. Homogeneous drift-diffusion-recombination expansion

The homogeneous model obeys

```math
D\gamma^2+w\gamma=\kappa-i\omega,
```

for the present Fourier convention. At DC,

```math
D\gamma_0^2+w\gamma_0=\kappa.
```

Define

```math
V_*=w+2D\gamma_0
=\sqrt{w^2+4D\kappa}.
```

Subtracting the DC equation gives

```math
D(\delta\gamma)^2+V_*\delta\gamma=-i\omega.
```

Expanding the physical root about `omega=0` yields

```math
\boxed{
\delta\gamma_{\rm DD}(\omega)
=-\frac{i\omega}{V_*}
+\frac{D\omega^2}{V_*^3}
+\frac{2iD^2\omega^3}{V_*^5}
+O(\omega^4).
}
```

Therefore

```math
\boxed{a_1=\frac{1}{V_*}},
```

```math
\boxed{a_2=\frac{D}{V_*^3}},
```

and the first coefficient that is not independently adjustable once `a_1` and `a_2` are matched is

```math
\boxed{
a_3^{\rm DD}=\frac{2a_2^2}{a_1}.
}
```

---

## 4. Theorem: any admissible first two coefficients define an effective drift-diffusion model

Suppose an arbitrary physical or nuisance mechanism produces

```math
\delta\gamma(\omega)
=-i a_1\omega+a_2\omega^2+O(\omega^3),
```

with

```math
a_1>0,
\qquad
a_2>0.
```

Then define

```math
\boxed{V_{*,\rm eff}=\frac{1}{a_1}},
```

```math
\boxed{D_{\rm eff}=\frac{a_2}{a_1^3}}.
```

The homogeneous drift-diffusion model with these parameters satisfies

```math
\boxed{
\gamma_{\rm DD}(\omega)-\gamma(\omega)=O(\omega^3).
}
```

If `gamma_0` is also known from DC, then the usual relations

```math
w_{\rm eff}=V_{*,\rm eff}-2D_{\rm eff}\gamma_0,
```

```math
\kappa_{\rm eff}=V_{*,\rm eff}\gamma_0-D_{\rm eff}\gamma_0^2
```

complete the local effective homogeneous model whenever the resulting parameters satisfy the adopted physical-admissibility constraints.

Thus **DC plus low-frequency information through quadratic order cannot, by itself, distinguish true homogeneous diffusion from any different mechanism that produces the same first two frequency coefficients of the recovered spatial exponent.**

The distinction begins in the cubic coefficient and higher.

---

## 5. Equivalent multiplier/cumulant form

For a source-coordinate spacing `h`, let

```math
q(\omega)=e^{-h\gamma(\omega)}.
```

In the no-recombination case `gamma_0=0`, write

```math
\log q(\omega)
=i\tau\omega-\beta\omega^2-i\zeta\omega^3+O(\omega^4).
```

Then

```math
\tau=h a_1,
\qquad
\beta=h a_2,
```

and the effective homogeneous parameters are

```math
\boxed{w_{\rm eff}=\frac{h}{\tau}},
```

```math
\boxed{
D_{\rm eff}=\frac{\beta w_{\rm eff}^3}{h}
=\frac{\beta h^2}{\tau^3}.
}
```

If the multiplier is locally the characteristic function of an incremental delay distribution,

```math
\log q(\omega)
=i\mu\omega-\frac{\sigma_T^2}{2}\omega^2
-\frac{i\kappa_3}{6}\omega^3+\cdots,
```

then

```math
\boxed{
D_{\rm eff}=\frac{\sigma_T^2 h^2}{2\mu^3}.
}
```

This equation exposes the confound directly: **any source of incremental delay variance can look like diffusion at sufficiently low RF**, even if the microscopic trajectories themselves are deterministic.

Spatially varying electric field, unresolved lateral path variation, deterministic velocity heterogeneity, or other path-to-path timing dispersion can therefore contribute to an apparent diffusion coefficient unless independently constrained.

The characteristic-function interpretation is conditional; the analytic two-coefficient equivalence above does not require it.

---

## 6. Where the falsification information first appears

After matching `a_1` and `a_2`, the leading physical-law discrepancy is

```math
\delta\gamma_{\rm true}-\delta\gamma_{\rm DD}
=i\left(a_3-\frac{2a_2^2}{a_1}\right)\omega^3
+O(\omega^4).
```

Therefore the next-RF falsification principle remains mathematically valid, but its practical power depends on whether the experiment reaches frequencies and precision large enough to resolve the cubic-and-higher mismatch.

The statement

> `DC + one RF identifies; the next RF tries to kill the model`

is a **structural-identifiability statement**, not a guarantee that the next RF has useful discriminatory power.

Near DC, a wrong heterogeneous model can be tangent to the homogeneous drift-diffusion family through second order.

---

## 7. Connection to the tangent-confound theorem

The earlier Paper-02 tangent theorem addresses the spectral-channel direction:

- nuisance components tangent to the rank-one channel manifold bias the recovered spatial exponent;
- normal components create same-frequency rank/model-order residuals.

The present theorem addresses the frequency direction:

- the first two low-frequency coefficients of that biased exponent can always be represented by effective `V_*` and `D` when `a_1,a_2>0`;
- only cubic and higher frequency structure distinguishes the mechanism.

Together they define a two-stage hidden-confound geometry:

```text
spectral-channel tangent alignment
    -> nuisance survives same-frequency rank test

low-frequency dispersion tangent alignment
    -> nuisance survives DC+RF homogeneous-law fit
```

A robust attribution of microscopic material diffusion therefore requires both spatial-channel and frequency-domain separation from device-level nuisance mechanisms.

---

## 8. Current numerical demonstration

The strongest current conditional example is a full-width planar contact with a 3.0 um depletion region and 0.05 V space-charge drop at 0.30 V total bias.

The carrier solver contains deterministic saturated drift only.

### Kernel-aware one-mode fit

The exact calibrated optical kernels are retained and each frequency is fit to

```math
J_m=C+K\int g_m(z)\frac{e^{r(z-z_{\rm ref})}-1}{r}\,dz,
```

with the continuous affine limit at `r=0` and `gamma=-r` for the increasing-z coordinate used by the numerical model.

The uniform planar reference is recovered to better than

```math
7.3\times10^{-9}
```

relative error over the entire 0--3 GHz sweep, validating the kernel-aware fit implementation against the known homogeneous geometry.

For the depleted deterministic device, the one-mode kernel-aware fit residual remains below

```math
1.74\times10^{-4}
```

through 1 GHz.

The 100 MHz one-RF inversion gives

```math
D_{\rm eff}=2.609795\times10^{-3}\ {\rm m^2/s},
```

```math
w_{\rm eff}=2.570098\times10^4\ {\rm m/s}.
```

The resulting homogeneous physical-law residual is approximately

```text
25 MHz    0.0090 %
50 MHz    0.0071 %
100 MHz   0       %   [identification point]
200 MHz   0.0280 %
300 MHz   0.0745 %
500 MHz   0.2219 %
750 MHz   0.5044 %
1 GHz     0.8885 %
1.5 GHz   1.9201 %
2 GHz     3.2276 %
3 GHz     6.3461 %
```

A simultaneous low-band fit through 200 MHz gives nearly the same effective parameters,

```math
D_{\rm eff}=2.606303\times10^{-3}\ {\rm m^2/s},
```

```math
w_{\rm eff}=2.570629\times10^4\ {\rm m/s},
```

and remains below 1% physical-law residual through 1 GHz.

These are **effective parameters of a wrong homogeneous model**. They are not microscopic diffusion and drift coefficients of the simulated device.

---

## 9. What this does and does not establish

### DERIVED

1. Any analytic recovered spatial exponent with positive first- and second-order coefficients admits a homogeneous drift-diffusion model matching it through `O(omega^2)`.
2. The effective parameters are fixed by those first two coefficients.
3. Cubic and higher frequency structure is the first local discriminator after the two coefficients are matched.
4. If an effective multiplier is a delay characteristic function, delay variance maps directly onto a positive apparent diffusion coefficient.

### CHECKED in the present conditional numerical model

1. A deterministic planar depletion field produces a positive false `D_eff`.
2. The effect survives exact calibrated finite-optical-kernel fitting.
3. The wrong homogeneous law remains below 1% relative residual through 1 GHz for the current parameter point.
4. The underlying trajectory model contains no diffusion or recombination.

### NOT established

1. That the specific 3 um / 0.05 V example corresponds to any calibrated real detector.
2. That the effect is large enough to matter at a given laboratory noise floor.
3. That the theorem or detector application is novel.
4. That no independent electrostatic measurement can break the degeneracy.
5. That Rev. 9 is mathematically wrong. Its structural overdetermination remains correct; the new result concerns practical attribution and conditioning against an omitted nuisance model.

---

## 10. Next scientific gate

Before manuscript integration or a separate Paper-02 draft:

1. perform a focused primary-source prior-art audit for effective diffusion / apparent diffusion generated by deterministic field or velocity inhomogeneity;
2. derive the exact deterministic variable-velocity low-frequency coefficients directly from the Ramo path functional, rather than only from the fitted `gamma(omega)`;
3. sweep depletion width and voltage drop to determine scaling of `D_eff` and the cubic mismatch frequency;
4. test an independent electrostatic profile family, not only the present quadratic-space-charge surrogate;
5. quantify the RF precision and bandwidth required to reject the wrong homogeneous model.

Until those gates are passed, the result remains a **candidate distinct detector-identifiability application**, not a novelty claim.
