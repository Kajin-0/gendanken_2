# HgCdTe Spectral Momentum-Scattering Surrogate — What Survives Between Ballistic and Diffusive Limits?

**Date:** 2026-08-09  
**Status:** dimensionless underdamped stochastic stress test; not a calibrated HgCdTe Monte Carlo model; narrows the candidate spectral prediction; no novelty claim

## 1. Purpose

`HGCDTE_SPECTRAL_DRIFT_DIFFUSION_ROBUSTNESS.md` showed that the earlier ballistic entrance-gap timing **maximum** is not universal.

In the strong momentum-randomizing limit, the high-optical-depth delay rises through the graded-gap interval and then approaches a full-length drift plateau.

This note asks the intermediate question:

> With finite momentum memory, what aspects of the spectral timing curve survive when the photoelectron can retain some initial velocity information before scattering?

The answer is useful because it separates the robust optical geometry from transport-model-dependent short-wave behavior.

---

## 2. Dimensionless transport surrogate

Use a one-dimensional underdamped Langevin / Ornstein-Uhlenbeck velocity model

```math
\boxed{
dv
=\frac{v_d-v}{\tau_m}dt
+\sqrt{\frac{2\sigma_v^2}{\tau_m}}\,dW_t,
}
```

with

```math
\boxed{dx=v\,dt.}
```

Here

- `v_d` is the asymptotic drift velocity;
- `tau_m` is the momentum-relaxation time;
- `sigma_v` sets stochastic velocity fluctuations;
- `W_t` is a Wiener process.

This is not intended to reproduce the microscopic scattering rates of HgCdTe.

It is the minimal stochastic bridge between

```text
persistent directed velocity memory
```

and

```text
strong momentum randomization / drift transport.
```

---

## 3. Preserve the same graded optical geometry

Normalize

```text
Eg_out = 1
Eg_in  = 2
G      = 1
L      = 1.
```

Define

```math
s=E_\gamma-E_{g,\rm out}.
```

In the high-optical-depth geometry,

```math
\boxed{
d(s)=\min(s,1).}
```

Thus

```text
s < 1
-> first allowed generation point moves upstream
-> remaining distance grows with photon energy

s >= 1
-> first allowed generation point has reached the physical entrance
-> remaining distance is fixed at L.
```

The geometric transition is fixed at

```math
\boxed{s=1}
```

or

```math
\boxed{E_\gamma=E_{g,\rm in}.}
```

---

## 4. Three initial momentum models

Above the entrance gap, the local photon excess at the entrance is

```math
u=E_\gamma-E_{g,\rm in}.
```

Represent the corresponding hot-carrier velocity scale schematically as

```math
v_h\propto\sqrt\nu.
```

Three deliberately different longitudinal initial conditions are tested.

### A. Strong-randomization reference

```math
\boxed{v_0=0.}
```

Photon excess is not converted into a retained directed longitudinal velocity.

### B. Persistent forward memory

```math
\boxed{v_0=+v_h.}
```

This is the favorable one-dimensional ballistic-like case used to test the strongest possible short-wave speedup.

### C. Symmetric/isotropic-projection stress test

```math
\boxed{v_0\sim\mathrm{Uniform}(-v_h,+v_h).}
```

This keeps zero mean longitudinal velocity while increasing the width of the hot initial velocity distribution.

It is only a toy projection of an isotropic hot distribution, not a full optical-selection-rule calculation.

---

## 5. Numerical stress-test result

The deterministic regression

```text
numerics/hgcdte_spectral_momentum_scattering_surrogate.py
```

uses

```text
tau_m = 0.40
sigma_v = 0.10
v_d = 1
hot-scale coefficient = 1.50
```

in normalized units.

The sampled photon coordinate is

```text
s = 0.25, 0.50, 0.75, 1.00, 1.50, 2.00.
```

All three cases are identical below the entrance-gap point because the high-optical-depth generation event occurs at the local band edge and no upstream hot excess is assigned.

The mean delay rises monotonically as the generation position moves upstream.

Above the entrance gap the three cases separate.

### Strong-randomization reference

The mean delay is approximately constant because the path length is fixed and the retained transport coefficients are photon-energy independent.

This is the drift-like plateau.

### Persistent forward memory

The mean delay decreases as photon energy increases.

This reproduces the qualitative ballistic post-knee decline.

### Symmetric hot initial distribution

The mean delay does **not** show the same decline in the chosen stress test.

The negative-velocity part of the distribution delays some trajectories, while the timing variance grows strongly.

Thus an isotropic/symmetric hot distribution is an explicit counterexample to treating `more photon excess -> shorter mean longitudinal transit` as automatic.

---

## 6. Corrected hierarchy of spectral claims

The results now support three different levels of statement.

### Robust geometry

```math
\boxed{
E_\gamma=E_{g,\rm in}
}
```

is the energy at which the first allowed generation position stops moving upstream and becomes pinned at the physical entrance.

This is independent of the carrier transport model.

### Strong-scattering timing prediction

For wavelength-independent drift coefficients, the geometry produces a rise into a plateau.

### Persistent directed hot-carrier prediction

If significant forward velocity memory survives optical generation and subsequent scattering, the plateau can turn into a true local maximum followed by a short-wave decline.

Therefore

```text
entrance-gap maximum
```

is **not** the transport-independent prediction.

The safer candidate signature is

> **an entrance-gap spectral feature / knee / change in timing slope whose post-knee shape diagnoses momentum and energy relaxation.**

---

## 7. Why this is better experimentally

The previous falsification proposal was unnecessarily binary:

```text
find peak
or reject model.
```

The improved interpretation is richer.

A wavelength sweep through the entrance-gap energy can distinguish transport regimes:

```text
rise -> plateau
= strong momentum randomization with nearly wavelength-independent drift

rise -> maximum -> decline
= retained forward hot-carrier velocity memory / energy-dependent transport

rise -> continued rise with broadened timing
= possible symmetric hot initial momentum effects or energy-dependent scattering

no reproducible feature
= optical localization assumption fails, another device pole dominates, or the graded model is incomplete.
```

Thus the experiment becomes a probe of **carrier transport regime**, not only a test of one curve shape.

---

## 8. Connection to primary HgCdTe transport work

Primary Monte Carlo work on `Hg_0.8Cd_0.2Te` at 77 K explicitly calculates microscopic scattering, drift velocity, mean energy, diffusion, velocity relaxation, energy relaxation and impact-ionization behavior.

Modern HgCdTe APD Monte Carlo work likewise emphasizes that carrier momentum is changed by optical/acoustic phonons, alloy scattering, ionized impurities and other interactions, and compares reduced models against full-band Monte Carlo calculations.

Therefore a full HgCdTe treatment should not infer longitudinal transport directly from photon excess energy.

The present OU model is only an adversarial bridge until those microscopic scattering rates are inserted.

---

## 9. Claim boundary

### Derived / checked inside the surrogate

- the generation-distance rule changes at `E_gamma=Eg_in`;
- cold/strong-randomization transport gives an approximately flat post-knee branch;
- retained positive directed initial velocity can produce the ballistic decline;
- a symmetric hot initial longitudinal distribution provides a counterexample to universal short-wave decline;
- post-knee timing variance can be highly sensitive to momentum-memory assumptions.

### Not established

- the quantitative post-knee shape of real graded HgCdTe;
- a calibrated `tau_m(E,x)` or velocity-noise process for the target composition;
- that real optical excitation is exactly isotropic in the relevant multilayer structure;
- that the entrance-gap feature remains sharp after finite optical depth, scattering, contacts, recombination and readout;
- novelty.

---

## 10. Next decisive work

The target has changed.

Do **not** spend effort defending the ballistic maximum.

The next high-value model is a wavelength-resolved hydrodynamic or Monte Carlo calculation with

```text
measured / published HgCdTe scattering physics
+
realistic Eg(x)
+
optical generation position
+
carrier momentum/energy history
+
first-passage/current-response timing.
```

The experimental observable should be framed as the existence and shape of an **entrance-gap timing feature**, with the post-knee slope used to diagnose the scattering regime.
