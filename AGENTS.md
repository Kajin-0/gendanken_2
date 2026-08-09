# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is wavelength × frequency inverse metrology of internal transport in compositionally graded HgCdTe; no novelty claim**

Read this file first.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, corrections, counterexamples, and prior-art collisions are part of the result.

**There is still no manuscript.**

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches;
6. make narrow edits where practical.

**Live `main` overrides snapshots and recovery notes.**

---

## 2. Epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and `CLAIM_LEDGER.md` update.

---

## 3. Current research path

```text
active-volume thought experiment
-> universal volume bound killed by field concentration

microscopic / passive / active optical limits
-> successive resource loopholes

semiconductor extraction and filtering
-> detailed balance, delay, tunneling

HgCdTe field-driven collection
-> BTBT normalization
-> TAT and nonlocal hot-electron physics

homogeneous field shaping
-> no local benefit under stated model

HgCdTe bandgap grading
-> direct-Zener geometry can be suppressed at fixed conduction drive
-> quasi-neutral p-type grading can pin the majority-hole band

wavelength-resolved generation
-> photon energy changes first allowed generation position in a monotonic gap profile

ballistic timing model
-> predicted entrance-gap timing maximum

momentum-scattering attack
-> maximum not universal
-> entrance-gap initial-condition switch survives

prior-art collision
-> wavelength-dependent generation + graded transport + response-time forward modeling is already established
-> localized-position HgCdTe transit-time measurement is already established

CURRENT FRONTIER
-> use a known graded gap as an internal spectral position encoder
-> measure complex frequency response versus wavelength
-> invert timing data for spatial mean-delay density q1(x)
-> optionally invert timing variance for broadening density q2(x)
-> validate against localized excitation or independent transport modeling.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
6. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md`
7. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
8. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`
9. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_RESOLUTION.md`
10. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
11. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`
12. `experiments/01-vanishing-absorber/HGCDTE_ENTRANCE_GAP_INITIAL_CONDITION_SWITCH.md`
13. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
14. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

Earlier ballistic peak, optical-resource, and active-volume branches are provenance, not the active claim.

---

## 5. What is already prior art

Do **not** claim novelty for

- wavelength-dependent absorption / generation depth in photodiodes;
- wavelength-dependent transit time or bandwidth;
- graded-bandgap carrier acceleration;
- wavelength- and depth-dependent photogeneration in graded HgCdTe forward models;
- graded HgCdTe response-time modeling;
- localized-position transit-time measurements in HgCdTe.

The 2022 graded-HgCdTe work already writes a depth- and wavelength-dependent generation rate and couples it to transport / response modeling.

Perrais et al. already measured HgCdTe APD impulse response using localized excitation at different positions.

A 2024 paper from the same group titled `Potential application of HgCdTe detector with composition gradient in laser measurement` is especially close application prior art; its full technical content has not yet been recovered. Treat priority as unresolved until it is read.

---

## 6. Narrow active candidate: inverse metrology

For wavelength `i`, let

```math
p_i(x)=p(x|E_{\gamma,i},{\rm abs})
```

be the known normalized generation-position density.

Define the cumulative timing kernel

```math
\boxed{
K_i(s)=P(X_g\le s|E_{\gamma,i},{\rm abs}).
}
```

If the conditional mean collection delay is path additive,

```math
m(x)=\int_x^L q_1(s)ds,
```

then

```math
\boxed{
\mu_i
=\int_0^L K_i(s)q_1(s)ds.
}
```

Discretely,

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q_1+c_1\mathbf1.
}
```

Here

```math
q_1(x)
```

is the spatial mean-delay density; under a local path-additive velocity interpretation,

```math
\boxed{q_1(x)=1/v_{\rm eff}(x).}
```

The additive nuisance `c_1` absorbs wavelength-independent common delay.

This inverse reconstruction—not the forward wavelength/timing physics—is the only active candidate contribution.

---

## 7. Sharp-generation limit

For a monotonic linear gap

```math
E_g(x)=E_{g,\rm in}-Gx,
```

inside the graded-gap interval,

```math
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G}.
```

If generation is sharply localized and mean delay is path additive,

```math
\boxed{
\frac{dT}{dE_\gamma}
=\frac1{Gv_{\rm eff}[x_g(E_\gamma)]},
}
```

so

```math
\boxed{
v_{\rm eff}[x_g(E_\gamma)]
=\frac1{G\,dT/dE_\gamma}.
}
```

This is the singular-kernel limit of the full linear inverse.

Do not differentiate noisy experimental data by default; use the full forward matrix when finite optical depth matters.

---

## 8. Finite optical depth

For the analytic edge law

```math
\alpha=C(E_\gamma-E_g)^\beta
```

in a linear gap, the generation offset `z=x-x_g` has a stationary Weibull kernel away from downstream truncation.

The spectral derivative then measures a kernel-averaged inverse velocity:

```math
\boxed{
G\frac{d\bar T}{dE_\gamma}
=\int p(z)\frac{dz}{v_{\rm eff}(x_g+z)}.
}
```

Near the long-wave cutoff the eligible region truncates the kernel; use the full conditional generation kernel instead of the stationary approximation.

---

## 9. Second timing moment

If conditional timing variance is also path additive,

```math
V(x)=\int_x^Lq_2(s)ds,
```

then the law of total variance gives

```math
\boxed{
\sigma_i^2
=\int_0^L K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].
}
```

After reconstructing `q_1`, the generation-position variance is calculable and can be subtracted.

The same matrix `A` can then reconstruct `q_2`.

In a local high-Peclet drift-diffusion approximation only,

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

Do not call `q_2` a microscopic diffusion coefficient without validating that approximation.

---

## 10. Frequency-domain measurement

For timing distribution `T_lambda`,

```math
H_\lambda(\Omega)=\langle e^{-i\Omega T_\lambda}\rangle.
```

Low-frequency cumulants give

```math
\arg H_\lambda
=-\Omega\mu_\lambda+O(\Omega^3),
```

```math
\ln|H_\lambda|
=-\frac{\Omega^2}{2}\sigma_\lambda^2+O(\Omega^4).
```

Thus phase probes mean delay and magnitude curvature probes timing variance.

For differential phase,

```math
\boxed{
\Delta T
\simeq-\Delta\phi/\Omega.
}
```

A useful local spatial scale is

```math
\boxed{
\sigma_{x,\phi}
\sim
v_{\rm eff}\sigma_\phi/\Omega.
}
```

At illustrative `v_eff=1e5 m/s`, one degree at `1 GHz` corresponds to about `0.28 um`. This is a scale estimate, not an instrument performance claim.

---

## 11. Synthetic falsification status

Current deterministic synthetic regressions show:

- a nonuniform `q_1` profile can be reconstructed with finite optical depth, common delay, and small timing noise;
- a separate `q_2` broadening region can be recovered independently in a controlled two-moment case;
- broader optical kernels reduce the number of recoverable spatial modes substantially;
- near cutoff, kernel truncation can strongly bias a naive point inversion.

These are conditioning checks only. They are not experimental validation.

---

## 12. Experimental resolution constraints

Spatial resolution is limited independently by

```text
optical generation-kernel width
source spectral width / wavelength calibration
gap-profile uncertainty
timing or phase precision
conditioning / regularization
nonlocal transport.
```

For a linear gap,

```math
\sigma_{x,\lambda}
\simeq
\frac{hc}{G\lambda^2}\sigma_\lambda.
```

A local timing scale is

```math
\sigma_{x,T}\sim v_{\rm eff}\sigma_T.
```

Do not equate wavelength sample count with spatial degrees of freedom; use the singular-value spectrum of the forward matrix.

---

## 13. Published-device validation target

The 2022 VPE graded HgCdTe detector reports a composition span approximately `x=0.57 -> 0.31`, uses FTIR-based composition-depth profiling, and already has high-speed impulse / LCA characterization.

Its timing measurement used `1.55 um`, which produces strong surface absorption and therefore does not scan the generation kernel through the MWIR gradient.

The 2023 follow-on graded HgCdTe study reports processed thicknesses around `7.6 um` and `3.7 um` and spectral evidence of different spatial collection behavior.

A strong validation would compare

```text
spectral inverse reconstruction
versus
localized-position excitation timing
```

on the same or a closely matched graded structure.

---

## 14. Current numerical regressions

Relevant files:

```text
numerics/hgcdte_spectral_timing_linear_inverse.py
numerics/hgcdte_spectral_timing_kernel_tomography.py
numerics/hgcdte_spectral_timing_svd_resolution.py
numerics/hgcdte_spectral_timing_two_moment_inverse.py
numerics/hgcdte_spectral_momentum_scattering_surrogate.py
```

Earlier ballistic peak regressions are historical/supporting only.

---

## 15. Current next step

Do **not** add another generic analytic theorem.

Next priorities:

1. recover a dimensional published `x(z)` / `E_g(z)` profile and calibrated `alpha(z,lambda)`;
2. construct its actual forward matrix `A`;
3. predict wavelength × RF phase/magnitude contrasts and required measurement precision;
4. determine the recoverable spatial modes from the real kernel matrix;
5. collision-test the full 2024 laser-measurement paper before any novelty language;
6. if possible, validate the spectral inverse against localized-position HgCdTe timing or a calibrated transport simulation.

Only after a real-device forward/inverse model or experimental validation should manuscript readiness be reassessed.
