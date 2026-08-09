# Gedanken 2

First-principles thought experiments in photodetector physics.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.

## Experiment 01 — The vanishing absorber

The project began with

> Can an ideal photodetector be made arbitrarily small, fast, sensitive, and perfectly absorbing?

That universal-bound route failed. After several optical, network, and semiconductor-transport branches, the research converged on a much narrower detector-metrology question.

## Current question

> **Can a known graded-HgCdTe optical profile act as an internal spectral encoder, allowing wavelength × RF complex-response data to recover a small number of differential internal carrier-transport modes without physically scanning the generation position?**

There is **no manuscript** and **no novelty claim**.

## Core inverse

Let

```math
p_i(x)=p(x|\lambda_i,{\rm abs})
```

be the known wavelength-dependent generation density and let `q_1(x)` be a path-additive mean-delay density.

For collection at the downstream boundary `L`,

```math
\boxed{
\bar T_i
=\int_0^L F_i(s)q_1(s)ds,
\qquad
F_i(s)=P(X_g\le s).
}
```

For collection at the entrance boundary `0`,

```math
\boxed{
\bar T_i
=\int_0^L S_i(s)q_1(s)ds,
\qquad
S_i(s)=P(X_g\ge s).
}
```

Use cell-integrated kernels

```math
\boxed{
A_{ij}=\int_{\text{cell }j}K_i(s)ds,
}
```

so

```math
\boxed{\mathbf T=\mathbf A\mathbf q_1.}
```

Only under a local path-additive interpretation may one identify

```math
q_1=1/v_{\rm eff}.
```

The published 2023 graded-HgCdTe samples are **front-collection** geometries, so their timing kernels are survival functions.

## Important identifiability limit

A wavelength-independent delay is not generically separable from arbitrary transport concentrated near the collecting boundary. The same issue applies to wavelength-independent timing broadening.

Therefore the robust observables are **differential spatial transport modes**.

Use differential phase/timing, independent common-chain calibration, boundary priors, or a lower-dimensional physical model. A regularizer choosing one decomposition is not proof of uniqueness.

## Complex-response implementation

For carrier timing distribution `T_i`,

```math
H_i(\Omega)=\langle e^{-i\Omega T_i}\rangle.
```

At low RF frequency,

```math
\arg H_i=-\Omega\mu_i+O(\Omega^3),
```

```math
\ln|H_i|=-\frac{\Omega^2}{2}\sigma_i^2+O(\Omega^4).
```

Thus

```text
differential phase
-> differential mean-delay modes

magnitude curvature
-> differential timing-broadening modes.
```

At higher normalized frequency, fit the full complex transfer rather than forcing a first-moment interpretation.

## Published 2023 validation pair

Xu et al. 2023 provide a useful control/contrast pair.

### Sample B — calibration/control

```text
processed thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region removed
junction at high-Cd end
remaining linear-gradient field ~100-200 V/cm.
```

The authors infer that the remaining linear gradient does not strongly alter carrier motion.

### Sample A — nonlinear/high-field contrast

```text
processed thickness ~7.6 um
part of nonlinear interdiffusion region retained
junction at high-Cd end
local nonlinear-gradient field approaches ~2e3 V/cm.
```

The authors attribute the A/B photoelectric difference primarily to composition-gradient effects on minority-carrier motion.

The strongest present strategy is therefore

```text
sample B
-> validate the optical/instrument/inverse chain

sample A
-> test for additional internal transport structure.
```

## Sample-B dimensional result

Because the exact fitted `x(z)` parameters are graphical rather than machine-readable, the current model uses a literature-constrained envelope rather than claiming the true sample profile.

At 300 K, with the central `150 V/cm` envelope and the Moazzami above-gap absorption law:

```text
2.80 um -> Pabs ~0.998, mean generation depth ~0.677 um
3.88 um -> Pabs ~0.070, mean generation depth ~3.523 um.
```

Hence

```math
\boxed{\Delta\langle z\rangle\approx2.85\ {\rm um}.}
```

At an illustrative `v_eff=1e5 m/s`, this corresponds to about `28.5 ps` or `10.25 degrees` at `1 GHz`. This is a measurement scale, **not** a sample-B velocity prediction.

## Few-mode limit

With 80 spatial cells, `0.01 um` wavelength steps, `Pabs>=0.05`, and cell-integrated front-collection kernels, the current sample-B envelope gives relative singular-mode counts

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23]
```

above thresholds `[1e-1,1e-2,1e-3,1e-4]`.

The defensible interpretation is

> **few-mode, band-limited transport tomography — not pointwise velocity imaging.**

The first realistic target is roughly `3-4` smooth differential transport modes.

## Wavelength-dependent measurement noise

The optical matrix alone does not determine experimental rank.

Across the retained sample-B scan, the absorbed-signal ratio between the strongly absorbed short-wave end and near-cutoff end is about `17.6`.

At fixed incident power, simple limits give

```text
statistics-like phase noise: sigma_phi proportional to Pabs^(-1/2)
additive-like phase noise:   sigma_phi proportional to Pabs^(-1).
```

Thus the correct inverse uses a **noise-whitened, common-mode-projected information matrix**.

## Sparse optimal wavelength design

For a reduced target of

```text
3 smooth transport modes
+
1 common-phase nuisance,
```

a D-optimal design concentrates measurement time into about four information-rich spectral bands.

Statistics-like example:

```text
~2.800, 3.410, 3.632, 3.840 um.
```

Additive-like example:

```text
~2.800, 3.400, 3.596, 3.780 um.
```

These are conditional design results, not universal recommended wavelengths.

## RF-frequency rule

For the current sample-B optical distributions and deterministic `T=z/v`, an illustrative optical-only criterion gives

```math
\boxed{f_{\max}\approx0.13\,v/W}
```

for keeping the timing-transfer magnitude above `0.98`.

RF frequency should therefore be adaptive to the observed transport scale. At higher normalized frequency, use the full complex response.

## Temperature comparisons require iso-kernel wavelengths

Holding wavelength fixed while changing temperature is optically confounded because

```math
\mathbf A=\mathbf A(T,\lambda).
```

Define a one-device iso-kernel wavelength by

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\frac{\|\mathbf A(T,\lambda)-\mathbf A(T_0,\lambda_0)\|_2}
{\|\mathbf A(T_0,\lambda_0)\|_2}.
}
```

For the current sample-B model, several mid/deep kernels can be reproduced at `215 K` and `115 K` with sub-percent to few-percent full-kernel mismatch by retuning wavelength.

The shallow `2.80 um` 300 K reference cannot be cleanly reproduced at `115 K` inside the spectral region used to establish the current absorption fit, so it should be dropped/redefined rather than forced.

## Paired A/B phase cancellation

If A and B are driven simultaneously by the same coherent modulated source at the same wavelength/frequency,

```math
\boxed{
\Delta\phi_{AB}
=-\Omega
(\mathbf A_A\mathbf q_A-
 \mathbf A_B\mathbf q_B)
+\Delta\phi_{\rm path}
+\Delta\phi_{\rm elec}.
}
```

Arbitrary common wavelength-dependent source phase cancels.

A reciprocal device/arm swap can cancel stable arm asymmetry under its stated assumptions.

This measures a **transport contrast**, not either absolute profile.

## Important paired-temperature correction

The two strongest controls do **not** combine automatically.

Simultaneous A/B source-phase cancellation requires the **same wavelength** at both devices. Exact iso-kernel matching generally gives a different wavelength for A and B because their composition profiles differ.

The correct common-wavelength temperature design is therefore a **joint iso-kernel optimization**:

```math
\boxed{
\lambda_*(T)
=\arg\min_\lambda
\left[
w_A\epsilon_A^2(T,\lambda)
+w_B\epsilon_B^2(T,\lambda)
\right].
}
```

Whether a useful joint schedule exists is currently **OPEN** because the numerical sample-A profile has not been recovered.

## Prior-art boundary

The forward ingredients are already prior art: wavelength-dependent generation depth, graded-HgCdTe transport, response-time modeling, and localized-position HgCdTe timing.

A close 2024 paper from the same group — `Potential application of HgCdTe detector with composition gradient in laser measurement`, DOI `10.5768/JAO202445.0310009`, pp. 549-556 — remains technically unresolved because accessible indexes expose metadata but not its abstract/full text.

Therefore:

> **no novelty or priority claim is made.**

## Publication status

> **Continue research. Do not write a manuscript yet.**

The next decisive step is to recover/digitize the real sample-A composition profile, build `A_A(T,lambda)`, and determine whether a common A/B joint iso-kernel temperature schedule exists.

If sample-A profile recovery remains blocked, the next best step is an instrument-level covariance model followed by a real sample-B calibration experiment.

## Canonical files

Start with:

- [`AGENTS.md`](AGENTS.md)
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)
- [`HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md)
- [`HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md`](experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_DIMENSIONAL_FORWARD_MATRIX.md)
- [`HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md`](experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_HETEROSCEDASTIC_PHASE_NOISE.md)
- [`HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md`](experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_SAMPLE_B_OPTIMAL_MEASUREMENT_DESIGN.md)
- [`HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md`](experiments/01-vanishing-absorber/HGCDTE_SAMPLE_B_RF_FREQUENCY_VALIDITY.md)
- [`HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md`](experiments/01-vanishing-absorber/HGCDTE_TEMPERATURE_ISO_KERNEL_DESIGN.md)
- [`HGCDTE_PAIRED_SAMPLE_AB_DIFFERENTIAL_PHASE.md`](experiments/01-vanishing-absorber/HGCDTE_PAIRED_SAMPLE_AB_DIFFERENTIAL_PHASE.md)
- [`HGCDTE_PAIRED_AB_TEMPERATURE_DESIGN.md`](experiments/01-vanishing-absorber/HGCDTE_PAIRED_AB_TEMPERATURE_DESIGN.md)
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)
- [`ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md)

New agents should read `AGENTS.md` first.
