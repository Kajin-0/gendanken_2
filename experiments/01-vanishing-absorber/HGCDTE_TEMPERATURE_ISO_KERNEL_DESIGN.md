# Temperature Iso-Kernel Design — Separating Transport Changes from Optical Reweighting

**Date:** 2026-08-09  
**Status:** numerical experimental-design result using the literature-constrained sample-B composition envelope and temperature-dependent HgCdTe absorption; no transport calibration and no novelty claim

## 1. The confound in an ordinary temperature sweep

A graded-HgCdTe timing experiment cannot interpret

```text
phase changes with temperature
```

as pure carrier-transport changes if the optical excitation wavelength is held fixed.

Changing temperature changes

```text
HgCdTe band gap
+
absorption coefficient
+
generation-position distribution
```

at the same wavelength.

Therefore the timing kernel itself changes with temperature:

```math
\mathbf A=\mathbf A(T,\lambda).
```

A fixed-wavelength comparison mixes

```text
transport change
+
optical spatial reweighting.
```

The correct experiment should instead try to hold the **optical timing kernel** fixed while temperature changes.

---

## 2. Iso-kernel definition

Choose a reference temperature and wavelength

```math
(T_0,\lambda_0),
```

with cell-integrated front-collection timing row

```math
\mathbf a_0
=\mathbf A(T_0,\lambda_0).
```

At another temperature `T`, choose wavelength

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\frac{\|\mathbf A(T,\lambda)-\mathbf a_0\|_2}
{\|\mathbf a_0\|_2}.
}
```

Call this an **iso-kernel wavelength**.

If the mismatch is small, the two measurements weight nearly the same spatial transport region despite the temperature change.

Then a phase difference is much closer to

```text
same spatial probe
-> changed carrier transport
```

rather than

```text
different spatial probe
-> changed carrier transport.
```

---

## 3. Current sample-B model

Use the same fixed composition envelope as the dimensional sample-B calculation:

```text
W = 3.7 um
x_low = 0.316
x_high = 0.357207
```

where `x_high` is chosen so the 300 K gap slope corresponds to the central `150 V/cm` field bracket.

The **composition profile is held fixed with temperature**. Only material optical quantities change through the temperature dependence of

```text
Eg(x,T)
+
alpha(E,x,T).
```

This is the correct physical separation for a fixed fabricated sample.

The optical model remains the current Hansen gap law plus Moazzami above-gap absorption model.

---

## 4. Reference bands

Use the four 300 K wavelength supports selected by the statistics-like D-optimal design:

```text
2.800 um
3.410 um
3.632 um
3.840 um.
```

They approximately represent

```text
shallow strong-absorption anchor
first interior kernel
second interior/deep kernel
near-cutoff localized kernel.
```

The comparison temperatures are

```text
300 K reference
215 K
115 K.
```

---

## 5. Full-kernel matching result

### 300 K reference: `3.410 um`

Reference:

```text
Pabs ~0.886
mean generation depth ~1.927 um.
```

Matched wavelengths:

```text
215 K -> 3.52095 um
kernel mismatch ~2.45%
Pabs ~0.822
mean depth ~1.938 um

115 K -> 3.65954 um
kernel mismatch ~5.08%
Pabs ~0.705
mean depth ~1.951 um.
```

This mode remains usable, though the 115 K optical equality is only approximate.

### 300 K reference: `3.632 um`

Reference:

```text
Pabs ~0.560
mean depth ~2.878 um.
```

Matched wavelengths:

```text
215 K -> 3.79272 um
kernel mismatch ~0.44%
Pabs ~0.475
mean depth ~2.880 um

115 K -> 4.00268 um
kernel mismatch ~0.84%
Pabs ~0.360
mean depth ~2.881 um.
```

This is a strong iso-kernel mode.

### 300 K reference: `3.840 um`

Reference:

```text
Pabs ~0.131
mean depth ~3.437 um.
```

Matched wavelengths:

```text
215 K -> 4.04232 um
kernel mismatch ~0.043%
Pabs ~0.105
mean depth ~3.437 um

115 K -> 4.31011 um
kernel mismatch ~0.112%
Pabs ~0.075
mean depth ~3.437 um.
```

This deep localized kernel can be held almost invariant with temperature.

The penalty is weak absorbed signal.

---

## 6. The shallow anchor fails at low temperature

For the `2.800 um`, 300 K shallow reference kernel:

```text
Pabs ~0.998
mean depth ~0.677 um.
```

At `215 K`, the full-kernel match is still practical:

```text
lambda ~2.43533 um
kernel mismatch ~1.08%
Pabs ~0.996
mean depth ~0.680 um.
```

At `115 K`, however, the mathematical optimum is approximately

```text
lambda ~1.14883 um
kernel mismatch ~2.12%.
```

That wavelength lies outside the approximate `600-5000 cm^-1` spectral region used to establish the current Moazzami above-gap fit.

If the search is constrained to

```math
\lambda\ge2.0\ {\rm um},
```

the best solution sits at the boundary and still has approximately

```math
\boxed{17.5\%}
```

kernel mismatch.

Therefore the 300 K shallow anchor should **not** be forced into the 115 K comparison under the current optical model.

A lower-temperature experiment should either

- drop that mode;
- define a different shallow reference kernel that remains inside a validated spectral range;
- or obtain a validated short-wave absorption model before using the mathematical `~1.15 um` solution.

---

## 7. Why matching the full kernel is stronger than matching mean depth

Two optical generation distributions can have the same mean depth but different widths or tails.

Timing depends on the full cumulative/survival weighting:

```math
\bar T
=\int S(s)q(s)ds.
```

Therefore matching only

```math
\langle z\rangle
```

is insufficient for a transport comparison.

The current optimization minimizes the difference between the entire **cell-integrated survival timing rows**.

This is the correct object for the linear inverse.

---

## 8. Temperature-difference observable

For one device, compare matched kernels:

```math
\phi(T,\lambda_*(T))
\simeq
-\Omega\mathbf a_0\mathbf q(T)
+\phi_{\rm common}(T),
```

up to the residual kernel mismatch and higher timing moments.

Then

```math
\Delta_T\phi
\approx
-\Omega\mathbf a_0
[\mathbf q(T_2)-\mathbf q(T_1)]
+\Delta_T\phi_{\rm common}.
```

The optical spatial weighting is now approximately fixed.

A stable common/reference calibration is still required for a single device.

---

## 9. Combine with paired A/B differential phase

The stronger experiment uses samples A and B simultaneously.

At each temperature,

```math
\Delta_{AB}\phi(T)
=\phi_A(T)-\phi_B(T),
```

which cancels arbitrary common tunable-source phase when both devices are driven coherently by the same source.

Now form a temperature difference:

```math
\boxed{
\Delta_T\Delta_{AB}\phi
=
[\phi_A(T_2)-\phi_B(T_2)]
-
[\phi_A(T_1)-\phi_B(T_1)].
}
```

But the wavelengths at each temperature should be chosen so the **A and B optical kernels are matched to their reference kernels as closely as possible**.

Then the experiment becomes a difference-in-differences test:

```text
sample B
-> smooth graded control

sample A
-> retained nonlinear/high-field region

change with temperature
-> controlled perturbation of transport physics

iso-kernel wavelength retuning
-> suppress optical spatial reweighting

simultaneous A-B phase subtraction
-> cancel common source phase.
```

This is currently the strongest proposed validation architecture in the repository.

---

## 10. Important residuals

Iso-kernel matching does not remove every temperature-dependent systematic.

Still required:

- actual sample A and B composition profiles;
- temperature-dependent refractive index / reflection / interference where material;
- device impedance and RF-chain temperature dependence;
- optical power and phase covariance at the retuned wavelengths;
- thermal stabilization;
- transport nonlinearity with optical loading.

Sample A is especially likely to require interference-aware optics because the 2023 paper reports interference near its cutoff.

---

## 11. Falsification logic

A useful hierarchy is:

### Sample B

At iso-kernel wavelengths, reconstructed transport should remain comparatively smooth if the published interpretation of its weak linear gradient is correct.

Strong unexplained localized structure in B would challenge the optical model, the inverse, or the assumption of smooth transport.

### Sample A

If its retained nonlinear region produces the extra transport effect inferred in the 2023 study, the A-B contrast should contain additional structure beyond B.

### Temperature

The 2023 primary study attributes the A/B photoelectric difference to composition-gradient fields and reports strong temperature dependence. A temperature-dependent A-B timing contrast, measured at iso-kernel wavelengths, would therefore be a much sharper transport test than a static spectrum alone.

Failure to see such a contrast would narrow the proposed timing interpretation even if the DC/spectral responsivity contrast remains.

---

## 12. Claim boundary

### DERIVED / CHECKED NUMERICALLY / CONDITIONAL

For the current literature-constrained sample-B optical model:

- three mid/deep 300 K reference kernels can be reproduced at 215 K and 115 K with approximately `0.04-5%` relative full-kernel mismatch;
- the `3.632` and `3.840 um` reference kernels remain particularly stable after wavelength retuning;
- the `2.800 um` shallow kernel cannot be reproduced at 115 K inside the current validated spectral range of the absorption fit.

### EXPERIMENTAL DESIGN CONSEQUENCE

Temperature comparisons should use **iso-kernel wavelengths**, not fixed wavelengths, when the objective is to isolate transport changes.

### NOT ESTABLISHED

- actual sample-A iso-kernel schedule;
- exact sample-B schedule using the real fitted `x(z)`;
- temperature-dependent complex-response data;
- transport causality from temperature alone;
- novelty / priority.

---

## 13. Next decisive work

The next genuinely useful input is the actual sample-A/sample-B profile data.

Once available:

1. build `A_A(T,lambda)` and `A_B(T,lambda)` with the real profiles;
2. compute paired iso-kernel schedules;
3. optimize wavelength × RF frequency × averaging time jointly;
4. measure the paired difference-in-differences phase;
5. compare against a transport model with the composition-gradient field explicitly included.

Do not replace the missing profile data with additional abstract theory.

Reproducibility:

`numerics/hgcdte_sample_b_iso_kernel_temperature.py`
