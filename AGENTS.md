# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical/experimental-method exploration; active frontier is few-mode wavelength × frequency inverse metrology of internal transport in a real graded-HgCdTe geometry; no novelty claim**

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
-> universal volume bound killed

optical / network / active-control branches
-> successive loopholes and resource dependence

HgCdTe tunneling / transport / grading
-> material-specific design constraints

wavelength-resolved generation
-> photon wavelength encodes generation depth in a monotonic gap

ballistic spectral timing
-> entrance-gap timing maximum proposed

momentum-scattering attack
-> maximum not universal

prior-art collision
-> wavelength-dependent generation + graded transport + response-time forward modeling already exists
-> localized-position HgCdTe timing already exists

inverse formulation
-> known optical kernels + timing data -> spatial delay density

orientation correction
-> downstream collection uses CDF kernel
-> front collection uses survival kernel

identifiability correction
-> wavelength-independent boundary/common delay is gauge-like
-> same issue applies to timing broadening

published 2023 sample-B instantiation
-> W ~3.7 um
-> nominal x ~0.316
-> nonlinear region removed
-> 100-200 V/cm linear-gradient bracket
-> Moazzami above-gap alpha

real matrix
-> conditional mean generation depth shifts by ~2.85 um over useful MWIR sweep
-> only a few spatial modes are strongly conditioned

phase-noise test
-> subtle internal anomaly produces sub-degree residual phase
-> ~3 coarse modes survive ~0.1 degree phase noise in the stated synthetic test

CURRENT FRONTIER
-> recover a finite set of differential internal transport modes
-> obtain real x(z) / instrument covariance / complex-response data
-> validate against localized excitation or microscopic transport.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`
6. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`
7. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_PHASE_PRECISION.md`
8. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`
9. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`
10. `experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`
11. `experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`
12. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
13. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

Older ballistic-peak, normalized-kernel, optical-resource, and active-volume branches are provenance/supporting work, not the active claim.

---

## 5. What is already prior art

Do **not** claim novelty for

- wavelength-dependent absorption / generation depth;
- wavelength-dependent photodiode transit time or bandwidth;
- graded-bandgap carrier transport;
- wavelength- and depth-dependent generation in graded HgCdTe;
- graded-HgCdTe response-time forward models;
- localized-position HgCdTe transit measurements.

Sang et al. 2022 already combine wavelength/depth generation with graded-HgCdTe forward transport/response modeling.

Perrais et al. already use localized excitation to study HgCdTe transit behavior.

A 2024 same-group paper titled `Potential application of HgCdTe detector with composition gradient in laser measurement` remains an unresolved close collision. Treat priority as unresolved until the paper is read.

---

## 6. Active operator — collection orientation matters

Let

```math
p_i(x)=p(x|\lambda_i,{\rm abs})
```

and local mean-delay density

```math
q_1(x).
```

### Collection at `L`

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

### Collection at `0`

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

Discretize with **cell-integrated kernels**:

```math
\boxed{
A_{ij}=\int_{\text{cell }j}K_i(s)ds,
}
```

so

```math
\boxed{
\mathbf T=\mathbf A\mathbf q_1.
}
```

The 2023 sample-B device is a front-collection / survival-kernel case.

Under a local path-additive interpretation only,

```math
q_1=1/v_{\rm eff}.
```

---

## 7. Common-delay / common-broadening gauge

Do **not** state that a wavelength-independent common delay can always be fitted uniquely with arbitrary `q_1`.

At the collecting boundary the timing kernel tends to unity for every wavelength. Boundary-localized internal delay can therefore be indistinguishable from common electronics/optics.

The same issue applies to wavelength-independent second-cumulant broadening and arbitrary boundary-localized `q_2`.

Robust options:

```text
differential phase/timing
independent common-chain calibration
boundary transport prior
lower-dimensional physical model.
```

Regularization may choose a decomposition; it does not prove identifiability.

---

## 8. Two timing moments

For the orientation-correct kernel `K_i`, additive conditional cumulants give

```math
\boxed{
\mu_i=\int K_iq_1,
}
```

```math
\boxed{
\sigma_i^2
=\int K_iq_2
+\operatorname{Var}_{p_i}[m(X)].
}
```

Only under a local high-Peclet drift-diffusion approximation may one identify

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

Do not call `q_2` microscopic diffusion without validation.

---

## 9. Frequency-domain observable

For the carrier timing distribution,

```math
H_i(\Omega)=\langle e^{-i\Omega T_i}\rangle.
```

Low-frequency cumulants give

```math
\arg H_i=-\Omega\mu_i+O(\Omega^3),
```

```math
\ln|H_i|=-\frac{\Omega^2}{2}\sigma_i^2+O(\Omega^4).
```

Hence

```text
differential phase -> differential mean-delay modes
magnitude curvature -> differential broadening modes.
```

At higher RF frequency, stop using the truncated cumulant approximation and fit the full complex transfer function.

---

## 10. Published sample-B dimensional baseline

Current literature-constrained 300 K envelope:

```text
W = 3.7 um
nominal x_low = 0.316
field bracket = 100-200 V/cm
nonlinear interdiffusion region removed
junction at high-Cd end.
```

Correct Hansen relation gives

```math
E_{g,\rm low}=0.312314\ {\rm eV},
\qquad
\lambda_{g,\rm low}=3.9699\ {\rm um}.
```

Field bracket implies approximately

```text
100 V/cm -> x_high=0.34348 -> 3.5494 um
150 V/cm -> x_high=0.35721 -> 3.3708 um
200 V/cm -> x_high=0.37091 -> 3.2094 um.
```

Use Moazzami et al. 2005 above-gap absorption for the current forward kernels.

The exact sample-B fitted `x(z)` is still OPEN.

---

## 11. Real-matrix result

For the central 150 V/cm envelope, current calculation gives approximately

```text
lambda 2.80 um -> Pabs 0.998, mean z 0.677 um
lambda 3.88 um -> Pabs 0.070, mean z 3.523 um.
```

Thus

```math
\boxed{\Delta\langle z\rangle\approx2.85\ {\rm um}.}
```

At illustrative `v_eff=1e5 m/s`, this is about

```text
28.5 ps
10.25 degrees at 1 GHz.
```

That is a scale, not a sample-B transport prediction.

Using 80 spatial cells, `0.01 um` wavelength sampling, and `Pabs>=0.05`, singular-mode counts are approximately

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23]
```

above relative thresholds `[1e-1,1e-2,1e-3,1e-4]`.

The defensible interpretation is **few-mode band-limited tomography**, not pointwise imaging.

---

## 12. Phase-noise result

Current synthetic stress test on the real optical matrix:

```text
baseline v = 1e5 m/s
25% slowdown
center = 2.30 um
sigma = 0.35 um
f = 1 GHz.
```

Residual anomaly phase:

```math
\boxed{\Delta\phi_{pp}\approx0.935^\circ.}
```

Three-mode reconstruction at `0.10 degree` independent per-wavelength phase noise gives approximately

```text
17.5% median error relative to the recoverable rank-3 target
0.13 um 90% peak-location error.
```

At `0.25 degree`, localization degrades strongly.

Five modes require substantially better phase precision for this anomaly.

This is an illustrative conditioning result, not an instrument or sample-defect claim.

---

## 13. Important nonclaims

Do not claim

- pointwise high-resolution `v(z)` reconstruction;
- absolute common delay from wavelength data alone;
- absolute common broadening from wavelength data alone;
- calibrated sample-B velocity/diffusion;
- actual sample-B transport defects;
- novelty/priority;
- manuscript readiness.

---

## 14. Current numerical regressions

```text
numerics/hgcdte_published_sample_b_forward_matrix.py
numerics/hgcdte_published_sample_b_phase_noise.py
numerics/hgcdte_spectral_timing_linear_inverse.py
numerics/hgcdte_spectral_timing_kernel_tomography.py
numerics/hgcdte_spectral_timing_svd_resolution.py
numerics/hgcdte_spectral_timing_two_moment_inverse.py
```

Older ballistic timing regressions remain provenance.

---

## 15. Next decisive work

Do **not** add another abstract inverse theorem.

Next priority:

1. obtain/digitize the actual 2023 sample-B `x(z)` fit;
2. build a realistic wavelength × RF-frequency covariance model for tunable-MWIR complex response;
3. include reflection/Urbach/interference only where they materially change the kernels;
4. fit multiple RF frequencies simultaneously;
5. validate recovered modes against localized-position timing or calibrated microscopic transport;
6. read the unresolved 2024 laser-measurement paper before any novelty language.

Only after a real-data or independently validated inversion should manuscript readiness be reassessed.
