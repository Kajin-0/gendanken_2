# Gedanken 2

First-principles thought experiments in photodetector physics.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, corrections, counterexamples, and prior-art collisions are retained because they define the actual result.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, fast, sensitive, and perfectly absorbing?

The original active-volume route failed. The research subsequently moved through optical access, microscopic coupling, active control, semiconductor extraction, HgCdTe tunneling/transport, bandgap grading, and wavelength-resolved carrier timing.

The current frontier is now a **measurement/inverse problem**, not another proposed fundamental limit.

## Current question

> **Can the known composition / band-gap gradient of an HgCdTe detector act as an internal spectral position encoder, allowing wavelength-resolved complex timing measurements to reconstruct the device's spatial carrier-transport profile?**

## Central inverse

For wavelength `i`, let

```math
p_i(x)=p(x|E_{\gamma,i},{\rm abs})
```

be the known normalized carrier-generation profile and define

```math
\boxed{
K_i(s)=P(X_g\le s|E_{\gamma,i},{\rm abs}).
}
```

If mean collection delay is represented by the spatial delay density `q_1(x)`,

```math
m(x)=\int_x^Lq_1(s)ds,
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

Under a local path-additive interpretation,

```math
\boxed{q_1(x)=1/v_{\rm eff}(x).}
```

Thus the wavelength sweep becomes an inverse reconstruction of **internal carrier delay density**, not merely another wavelength-dependent bandwidth measurement.

## Sharp-generation limit

For a linear graded gap

```math
E_g(x)=E_{g,\rm in}-Gx,
```

inside the graded-gap interval,

```math
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G}.
```

If absorption is sharply localized and mean transit is path additive,

```math
\boxed{
v_{\rm eff}[x_g(E_\gamma)]
=\frac1{G\,dT/dE_\gamma}.
}
```

This simple derivative formula is only the narrow-kernel limit of the full finite-depth linear inverse above.

## Second timing moment

If conditional timing variance also has an additive spatial density `q_2(x)`,

```math
V(x)=\int_x^Lq_2(s)ds,
```

then

```math
\boxed{
\sigma_i^2
=\int_0^L K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].
}
```

After reconstructing `q_1`, the generation-position contribution can be calculated and subtracted, leaving a second linear inverse for `q_2`.

In a local high-Peclet drift-diffusion interpretation only,

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

So a wavelength × frequency dataset may carry separate information about **mean transport** and **timing broadening**.

## Frequency-domain implementation

For the carrier timing distribution,

```math
H_\lambda(\Omega)
=\langle e^{-i\Omega T_\lambda}\rangle.
```

At low modulation frequency,

```math
\arg H_\lambda
=-\Omega\mu_\lambda+O(\Omega^3),
```

```math
\ln|H_\lambda|
=-\frac{\Omega^2}{2}\sigma_\lambda^2+O(\Omega^4).
```

Therefore

```text
phase
-> mean delay / q1

magnitude curvature
-> timing variance / q2.
```

A wavelength-independent common electronics delay can be fitted as a nuisance constant.

## Important correction to the earlier timing-peak branch

The earlier forward-ballistic model predicted a timing maximum at the entrance-gap wavelength.

That maximum is **not universal**.

A strong-scattering drift-diffusion model gives a rise into a plateau, and a finite momentum-memory stochastic model allows several short-wave behaviors depending on the initial longitudinal momentum distribution.

The transport-independent statement that survives is an **entrance-gap initial-condition switch**:

```text
below Eg,in
-> changing photon energy moves the first allowed generation position

above Eg,in
-> generation position is pinned at the entrance
-> changing photon energy changes the injected carrier state instead.
```

The old ballistic timing maximum is retained only as a special-case/provenance result.

## Prior-art boundary

The forward ingredients are already strong prior art.

Existing work covers

- wavelength-dependent generation depth and photodiode bandwidth;
- position-resolved HgCdTe transit-time measurement;
- graded-HgCdTe carrier acceleration and impulse response;
- wavelength- and depth-dependent generation combined with graded-HgCdTe response modeling;
- spectral inference of spatial carrier collection in graded HgCdTe.

A particularly close 2024 paper from the same research group is titled `Potential application of HgCdTe detector with composition gradient in laser measurement`; its full technical content has not yet been recovered.

Therefore the repository makes **no novelty claim** for spectral-generation/timing coupling.

The only active candidate is narrower:

> **use the known graded optical-generation kernels in reverse to reconstruct an internal spatial transport profile from measured wavelength-resolved timing.**

Status:

> **candidate underexplored inverse-metrology method; priority unproven.**

## Synthetic status

Current deterministic regressions show that, in controlled synthetic cases,

- a nonuniform mean-delay / velocity profile can be reconstructed with finite optical depth, common delay, and small timing noise;
- a separate timing-broadening profile can also be recovered;
- broader optical kernels sharply reduce the number of recoverable spatial modes;
- extreme-cutoff data require the full truncated optical kernel.

These are **conditioning checks**, not experimental validation.

## Published-device validation target

The 2022 VPE graded HgCdTe work reports a composition span around `x=0.57 -> 0.31`, FTIR-derived depth profiling, and high-speed impulse / LCA characterization. Its timing measurement used `1.55 um`, where absorption is strongly surface localized, so it did not scan through the MWIR gradient.

The 2023 follow-on reports processed graded structures around `7.6 um` and `3.7 um` thick and shows that different portions of the composition profile affect spectral carrier collection.

The strongest proposed validation is therefore

```text
known dimensional Eg(x)
+
known/calibrated p(x|lambda)
+
wavelength x frequency complex-response data
->
reconstruct q1(x), optionally q2(x)
```

and compare against

```text
localized-position excitation timing
or
validated transport simulation.
```

## Publication status

> **Continue research. Do not write a manuscript yet.**

The method becomes scientifically interesting only if the inverse reconstruction provides internal transport information that existing forward models or ordinary wavelength-dependent bandwidth measurements do not.

## Canonical files

Start with:

- [`AGENTS.md`](AGENTS.md)
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)
- [`HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_LINEAR_INVERSE.md)
- [`HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_KERNEL_TOMOGRAPHY.md)
- [`HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TWO_MOMENT_INVERSE.md)
- [`HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_DIFFERENTIAL_PHASE.md)
- [`HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TIMING_TOMOGRAPHY_PRIOR_ART_AUDIT.md)
- [`HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md`](experiments/01-vanishing-absorber/HGCDTE_PUBLISHED_GRADED_DEVICE_TOMOGRAPHY_CASE.md)

New agents should read `AGENTS.md` first.
