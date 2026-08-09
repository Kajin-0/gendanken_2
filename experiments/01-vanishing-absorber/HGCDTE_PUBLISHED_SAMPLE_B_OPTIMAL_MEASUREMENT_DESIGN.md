# Published Sample B — Optimal Wavelength/Time Design for the Few-Mode Inverse

**Date:** 2026-08-09  
**Status:** reduced-rank D-optimal experimental-design calculation using the literature-constrained sample-B matrix and simple phase-noise scalings; no novelty claim

## 1. Why uniform wavelength sampling is not the right target

The published sample-B matrix contains strong redundancy between neighboring wavelengths.

At the same time, phase precision degrades as absorbed signal falls near cutoff.

Therefore an evenly spaced `110`-wavelength scan spends substantial time on measurements that are either

```text
nearly redundant
```

or

```text
spatially sharp but too noisy per unit measurement time.
```

The correct question is:

> **Given a fixed total measurement-time budget, which wavelengths should receive that time if the first goal is to estimate a few smooth internal transport modes?**

---

## 2. Reduced parameterization

The current experimentally realistic target is approximately three smooth differential transport modes rather than a pointwise `q(z)` profile.

Take the first three right-singular transport modes of the common-mode-centered sample-B optical matrix:

```math
\mathbf q(z)
\approx
\sum_{m=1}^{3}a_m\mathbf v_m(z).
```

Retain one additional wavelength-independent phase nuisance `c`.

The reduced parameter vector therefore has dimension

```math
\boxed{p=4.}
```

This is an **experimental-design basis**, not a claim that the physical transport truly has exactly three degrees of freedom.

---

## 3. Fisher information with wavelength-dependent measurement time

For wavelength `i`, let the reduced phase-sensitivity row be

```math
\mathbf h_i.
```

If phase variance after measurement time `t_i` is

```math
\boxed{
\operatorname{Var}(\phi_i)
=\frac{c_i}{t_i},
}
```

then the Fisher contribution is

```math
\boxed{
\mathbf J_i
=\frac{t_i}{c_i}
\mathbf h_i\mathbf h_i^T.
}
```

For fixed total normalized time

```math
\sum_i t_i=1,
```

```math
\boxed{
\mathbf J
=\sum_i
\frac{t_i}{c_i}
\mathbf h_i\mathbf h_i^T.
}
```

The present calculation maximizes

```math
\boxed{\log\det\mathbf J,}
```

the standard D-optimal criterion.

This maximizes the generalized information volume for the four reduced parameters.

---

## 4. Noise models tested

Three per-unit-time variance scalings are compared.

### Equal-noise idealization

```math
c_i=1.
```

### Statistics-like fixed-power scaling

```math
\boxed{c_i\propto1/P_{\rm abs}(\lambda_i).}
```

This corresponds to

```math
\sigma_\phi\propto P_{\rm abs}^{-1/2}
```

at fixed integration time.

### Additive-noise-like fixed-power scaling

```math
\boxed{c_i\propto1/P_{\rm abs}^2(\lambda_i).}
```

corresponding to

```math
\sigma_\phi\propto P_{\rm abs}^{-1}.
```

These are limiting scaling laws, not complete instrument models.

---

## 5. D-optimal result

The multiplicative optimal-design calculation on the `0.01 um` wavelength grid collapses the dense scan into essentially **four spectral support bands**.

Because one continuous optimum lies between two neighboring grid points, the numerical solver divides one support weight between adjacent wavelengths. Combining each adjacent pair gives:

### Equal-noise idealization

```text
~2.800 um
~3.430 um
~3.681 um
~3.890 um
```

### Statistics-like phase noise

```text
~2.800 um
~3.410 um
~3.632 um
~3.840 um
```

### Additive-noise-like phase noise

```text
~2.800 um
~3.400 um
~3.596 um
~3.780 um
```

Each support band receives approximately

```math
\boxed{25\%}
```

of the total time in this saturated four-parameter D-optimal design.

---

## 6. Physical interpretation

The four supports have clear roles.

### Short-wave anchor

Near

```text
2.8 um
```

absorption is almost complete and generation is weighted near the junction side.

### First interior kernel

Near

```text
3.4 um
```

one intermediate combination of transport modes becomes distinguishable.

### Second interior kernel

Near

```text
3.6-3.68 um
```

another complementary spatial weighting is obtained.

### Long-wave localized kernel

The last support exploits the spatial localization of long-wave generation.

But as its phase-noise cost rises, the optimizer moves it away from the extreme cutoff:

```text
equal-noise -> ~3.89 um
statistics-like -> ~3.84 um
additive-like -> ~3.78 um.
```

This is exactly the expected physical compromise between

```text
spatial localization
```

and

```text
measurement SNR per unit time.
```

---

## 7. Information gain relative to a uniform 110-wavelength scan

For the same total measurement time, compare the D-optimal design against assigning equal time to every retained wavelength.

Define the generalized information scale

```math
\boxed{
\mathcal I_D
=(\det\mathbf J)^{1/p}.
}
```

Because `p=4`, the optimized-to-uniform gain is

```text
equal-noise:        ~1.53
statistics-like:    ~1.34
additive-like:      ~1.34.
```

For the two fixed-power noise scalings, the optimized four-band design therefore has about

```math
\boxed{34\%}
```

higher generalized information scale per unit total time than uniform sampling.

Equivalently, because `I_D` scales linearly with total measurement time in this model, the optimized design needs only approximately

```math
\boxed{0.75}
```

of the total measurement time required by the uniform scan to reach the same D-optimal information volume.

This is a property of the stated reduced model and covariance scaling, not a universal 25% experiment-time saving.

---

## 8. Important consequence

The experiment should not be specified as

```text
sweep every 10 nm with equal averaging time.
```

The current physics instead recommends

```text
few strategically separated wavelength bands
+
measurement time allocated according to information and SNR.
```

A dense wavelength scan remains useful during an initial exploratory experiment to test the forward model and detect unexpected structure.

But once the kernel/covariance model is validated, an optimized sparse design should be much more efficient for repeated measurements or temperature/bias sweeps.

---

## 9. Why four bands appear

The reduced model contains

```text
3 differential transport-mode amplitudes
+
1 common phase nuisance.
```

A saturated D-optimal linear design often concentrates on approximately the minimum number of complementary support points needed to span the parameter space.

The present four-band result should therefore **not** be interpreted as a universal property of graded HgCdTe.

If the experiment fits

```text
more transport modes
more common/source nuisance parameters
second timing moments
multiple optical-profile uncertainties
```

then more spectral support points will generally be required.

---

## 10. Multi-frequency extension

At low RF frequency, phase sensitivity to mean delay scales as

```math
\partial\phi/\partial a_m
\propto\Omega.
```

So increasing RF frequency initially increases Fisher information as approximately

```math
\Omega^2,
```

provided phase variance is unchanged and the first-cumulant approximation remains valid.

But higher frequency also introduces

```text
higher timing cumulants
frequency-dependent readout noise
possible RC/electrical poles
source/reference phase structure.
```

The real experimental design should therefore eventually optimize **wavelength, RF frequency, and averaging time jointly** using the full complex-response Jacobian and measured covariance.

---

## 11. Stronger experimental strategy

The current evidence suggests a two-stage program.

### Stage A — validation scan

Use a denser wavelength × RF grid on sample B to validate

```text
x(z)/alpha model
common-mode cancellation
phase covariance
low-frequency cumulant approximation.
```

### Stage B — optimized transport measurement

Once validated, reduce to a small set of information-rich wavelength/RF bands and allocate measurement time optimally.

Then repeat efficiently versus

```text
temperature
bias
optical loading
sample A vs B
etc.
```

The sparse design is therefore an outcome of a validated model, not a substitute for initial model validation.

---

## 12. Claim boundary

### CHECKED NUMERICALLY / CONDITIONAL

For the literature-constrained sample-B matrix, first-three-mode parameterization, one common-phase nuisance, and the stated variance scalings:

- the D-optimal wavelength-time design has four effective support bands;
- increasing long-wave noise moves the final band away from cutoff;
- statistics-like and additive-like designs improve generalized information scale by about `34%` versus uniform-time use of the 110-point grid;
- the corresponding D-criterion time fraction is approximately `0.75`.

### NOT ESTABLISHED

- actual instrument covariance;
- exact optimal wavelengths for a real device;
- exact number of physical transport modes;
- optimal design once profile uncertainty and second-moment data are included;
- novelty / priority.

---

## 13. Next decisive work

Do not further optimize an idealized covariance indefinitely.

The next valuable input is empirical:

1. measure or obtain realistic phase/magnitude covariance versus wavelength and RF frequency;
2. incorporate actual sample-B `x(z)` uncertainty;
3. compute the full complex-response Fisher matrix;
4. optimize wavelength × RF-frequency × averaging-time allocation subject to detector-linearity constraints;
5. validate the optimized design experimentally before using it to compare sample A and B.

Reproducibility:

`numerics/hgcdte_published_sample_b_optimal_design.py`
