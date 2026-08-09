# HgCdTe Spectral Timing Two-Moment Inverse — Reconstructing Mean Transport and Timing Broadening

**Date:** 2026-08-09  
**Status:** exact law-of-total-variance inverse under additive conditional timing cumulants; local drift-diffusion interpretation is conditional; no novelty claim

## 1. Purpose

The current spectral timing inverse reconstructs the spatial mean-delay density

```math
q_1(x)=1/v_{\rm eff}(x)
```

from wavelength-dependent mean timing.

The full complex frequency response contains more information than mean delay.

At low modulation frequency,

```math
\arg H_\lambda(\Omega)
=-\Omega\kappa_1(\lambda)+O(\Omega^3),
```

while

```math
\ln|H_\lambda(\Omega)|
=-\frac{\Omega^2}{2}\kappa_2(\lambda)+O(\Omega^4).
```

Thus phase provides the first timing cumulant and magnitude curvature provides the second.

Question:

> After reconstructing the mean transport profile, can the wavelength-dependent timing variance be inverted into a spatial broadening profile?

Under an additive conditional-cumulant model, yes.

---

## 2. Conditional timing model

For a carrier generated at position `x`, let its conditional collection-time mean be

```math
\boxed{
m(x)
=\int_x^L q_1(s)ds.
}
```

Let its conditional transport variance be additive along the remaining path:

```math
\boxed{
V(x)
=\int_x^L q_2(s)ds.
}
```

Here `q_2(s)>=0` is a local timing-broadening density.

This model does not require `q_2` to be identified with diffusion until a specific transport closure is chosen.

---

## 3. Wavelength-dependent generation kernel

For wavelength index `i`, let

```math
p_i(x)
=p(x|E_{\gamma,i},{\rm abs})
```

be the known normalized generation-position density.

Define its cumulative kernel

```math
\boxed{
K_i(s)
=\int_0^s p_i(x)dx.
}
```

The same kernel appears in both moment inversions.

---

## 4. First moment

The measured intrinsic mean delay is

```math
\mu_i
=\mathbb E_i[m(X)].
```

As derived previously,

```math
\boxed{
\mu_i
=\int_0^L K_i(s)q_1(s)ds.
}
```

Discretely,

```math
\boxed{
\boldsymbol\mu
=\mathbf A\mathbf q_1+c_1\mathbf1,
}
```

where `c_1` can absorb a wavelength-independent common group delay.

---

## 5. Total variance

The law of total variance gives

```math
\boxed{
\sigma_i^2
=\mathbb E_i[V(X)]
+\operatorname{Var}_i[m(X)].
}
```

The two terms have different meanings.

### Transport broadening

```math
\mathbb E_i[V(X)]
=\int_0^L p_i(x)
\left[
\int_x^L q_2(s)ds
\right]dx.
```

Swap integrals:

```math
\boxed{
\mathbb E_i[V(X)]
=\int_0^L K_i(s)q_2(s)ds.
}
```

### Generation-position broadening

```math
\boxed{
\operatorname{Var}_i[m(X)]
=\int p_i(x)m^2(x)dx
-\left[
\int p_i(x)m(x)dx
\right]^2.
}
```

Once `q_1` is reconstructed, `m(x)` is known and this term is calculable entirely from the optical generation kernel.

---

## 6. Second inverse

Define the corrected variance datum

```math
\boxed{
y_{2,i}
\equiv
\sigma_i^2
-\operatorname{Var}_i[m(X)].
}
```

Then

```math
\boxed{
y_{2,i}
=\int_0^L K_i(s)q_2(s)ds.
}
```

Discretely,

```math
\boxed{
\mathbf y_2
=\mathbf A\mathbf q_2+c_2\mathbf1.
}
```

The **same spatial forward matrix** `A` is used for the first and second moments.

A wavelength-independent common broadening contribution from the readout can be represented by nuisance constant `c_2` to the extent that its low-frequency logarithmic transfer cumulant is additive and wavelength independent.

---

## 7. Local drift-diffusion interpretation

For a constant-coefficient drift-diffusion first-passage segment of length `dx`,

```math
\mathbb E[dT]
=\frac{dx}{v},
```

and

```math
\operatorname{Var}(dT)
=\frac{2D}{v^3}dx.
```

Thus in the local advection-dominated additive-segment approximation,

```math
\boxed{
q_1(x)=\frac1{v(x)},
}
```

```math
\boxed{
q_2(x)\simeq\frac{2D(x)}{v^3(x)}.
}
```

Therefore after reconstructing both profiles,

```math
\boxed{
v(x)=1/q_1(x),
}
```

and

```math
\boxed{
D(x)
\simeq
\frac{q_2(x)}{2q_1^3(x)}.
}
```

This identification is **conditional**, not a general theorem for arbitrary position-dependent stochastic transport.

For a full drift-diffusion operator with strongly varying coefficients, mean and variance satisfy backward differential equations rather than exactly independent local increments.

---

## 8. Frequency-domain extraction of the two cumulants

For a normalized timing transfer factor,

```math
\boxed{
\ln H_i(\Omega)
=-i\Omega\mu_i
-\frac{\Omega^2}{2}\sigma_i^2
+\frac{i\Omega^3}{6}\kappa_{3,i}
+O(\Omega^4).
}
```

Therefore

```math
\boxed{
\mu_i
=-\left.
\frac{d}{d\Omega}
\arg H_i(\Omega)
\right|_{0},
}
```

and

```math
\boxed{
\sigma_i^2
=-\left.
\frac{d^2}{d\Omega^2}
\ln|H_i(\Omega)|
\right|_{0}.
}
```

At finite low frequency,

```math
\boxed{
\arg H_i\approx-\Omega\mu_i,
}
```

```math
\boxed{
\ln|H_i|
\approx-\frac{\Omega^2}{2}\sigma_i^2.
}
```

Using several modulation frequencies is preferable to estimating the second cumulant from one amplitude point.

---

## 9. Common instrument response

If

```math
H_{\rm meas}(\Omega,\lambda)
=H_{\rm det}(\Omega,\lambda)
H_{\rm common}(\Omega),
```

then

```math
\ln H_{\rm meas}
=\ln H_{\rm det}+\ln H_{\rm common}.
```

Hence the low-frequency cumulant-like coefficients of the common transfer add equally at every wavelength.

The inverse may therefore fit

```text
one common first-order delay nuisance
+
one common second-order magnitude-curvature nuisance
```

provided the common chain is stable and wavelength independent.

This does not remove wavelength-dependent source or optical-system transfer effects.

---

## 10. Why the second moment adds real information

A wavelength-dependent mean delay can identify a slow region but does not distinguish whether that region is

```text
slow but deterministic
```

or

```text
slow and strongly diffusive / stochastic.
```

The second-moment inverse separates

```text
mean transport density q1
```

from

```text
transport timing-broadening density q2.
```

The generation-position contribution to timing spread is not confused with carrier-scattering broadening because it is explicitly calculable once the optical kernel and mean-delay profile are known.

---

## 11. Connection to HgCdTe transport physics

Primary HgCdTe Monte Carlo work calculates both

- drift velocity;
- diffusion / velocity fluctuations;
- velocity relaxation;
- energy relaxation;
- impact ionization.

Therefore a two-profile reconstruction has a natural comparison target in microscopic transport modeling.

The method should not be advertised as a direct measurement of the microscopic diffusion coefficient until its local additive approximation has been validated against such a model.

---

## 12. Synthetic falsification target

A meaningful numerical test should generate

```text
known q1(x)
known q2(x)
known wavelength-dependent p_i(x)
common mean-delay offset
common broadening offset
measurement noise in phase and magnitude.
```

Then reconstruct

```text
q1 from first cumulants
q2 from variance after subtracting generation-position variance.
```

The decisive test is whether a region with enhanced transport broadening can be localized independently of a region with reduced mean velocity.

---

## 13. Claim boundary

### Derived exactly under the additive conditional-cumulant assumptions

```math
\boxed{
\mu_i=\int K_i q_1,
}
```

```math
\boxed{
\sigma_i^2
=\int K_i q_2
+\operatorname{Var}_{p_i}[m(X)].
}
```

and therefore the corrected second linear inverse.

### Conditional transport identification

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3
```

requires a local advection-dominated drift-diffusion interpretation.

### Not established

- experimental second-moment precision in graded HgCdTe;
- local `D(x)` recoverability in real nonlocal HgCdTe transport;
- a real two-profile reconstruction;
- novelty.

---

## 14. Next decisive work

1. build a synthetic two-moment inversion where slow velocity and large diffusion occur at different positions;
2. establish conditioning/noise sensitivity of `q_2`, which will be worse than `q_1` because magnitude curvature is harder to measure than phase;
3. compare the reconstructed profiles to a microscopic HgCdTe transport simulation before assigning `q_2` a diffusion interpretation;
4. if successful, include phase **and magnitude** in the proposed wavelength-resolved experiment rather than measuring only group delay.
