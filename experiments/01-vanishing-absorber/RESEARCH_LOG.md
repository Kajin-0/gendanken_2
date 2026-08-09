# Research Log — Experiment 01: The Vanishing Absorber

Chronological recovery log. Dedicated files preserve detailed algebra; this file records **why the direction changed**.

---

## 2026-08-08 — Experiment opened

Starting question:

> Can an ideal photodetector be made arbitrarily small, fast, sensitive, and still absorb essentially every incident photon?

The project explicitly refused to assume a theorem or optimize for a paper-shaped result.

---

## One-port absorber

A one-port resonator showed that unity monochromatic absorption can survive arbitrarily weak absorber loss through critical coupling.

The useful temporal response narrows as the internal loss rate decreases, and a factor-of-two distinction was established between absorption spectral FWHM and small-signal absorbed-power bandwidth.

Direction: ask whether absorber loss must scale with active material volume.

---

## Active-volume route killed

A field-concentration counterexample retained finite optical participation while active material volume tended to zero.

Conclusion:

> active semiconductor volume alone is not a universal detector resource.

Direction: descend to microscopic coupling and access resources.

---

## Microscopic / passive-network / active-control branches

Finite absorber count did not impose a one-photon speed limit.

A finite passive multimode network produced the harmonic integrated-transfer bound

```math
\mathcal I_{L\to R}
\le\frac{2LR}{L+R}.
```

But direct feedthrough, continuum reservoirs, pumped conversion, temporal-mode capture, adaptive branching, and output-record capacity exposed genuine extra resources.

An unrestricted output continuum killed the attempted universal finite detector-only space-time capacity theorem.

Direction:

> stop adding abstract resource coordinates and return to a real semiconductor detector.

---

## Semiconductor extraction and HgCdTe high-field transport

Fermi-reservoir detailed balance tied rapid extraction to reverse loading.

Multipole filters showed that spectral width is not a universal carrier-speed variable.

A simplified HgCdTe direct-BTBT model collapsed to

```math
j=x^2e^{-1/x},
```

but primary high-field transport work killed low-field `v=mu F` extrapolation.

TAT and nonlocal impact-ionization/hot-carrier history could become important before direct BTBT.

A path-dependent mean-energy state was introduced:

```math
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
```

Direction: use material grading to alter tunneling geometry without throwing away useful carrier drive.

---

## Homogeneous field shaping no-go

Within the stated homogeneous local transport/WKB model, redistributing electric field did not improve the fixed-transit leakage optimum; uniform field won.

Conclusion:

> a true escape requires material heterogeneity.

---

## Graded-band HgCdTe

For linear band edges,

```math
S_v=S_c-G,
\qquad
G=-dE_g/dx.
```

At fixed conduction-band drive, direct-Zener action increases strongly as the valence-band slope approaches zero.

For quasi-neutral p-type material,

```math
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v),
```

so nearly constant `N_A/N_v` gives

```math
E_v\approx\text{constant},
\qquad
S_c\approx G.
```

Thus quasi-neutral grading can naturally separate useful minority-electron drive from the ordinary same-direction direct-Zener geometry.

---

## Boundary and nonlocal hot-electron cost

Barrier-free entry into a wider-gap collection region requires

```math
qV_b\ge\alpha\Delta E_g^{(b)},
```

and any nonnegative field over width `w` obeys

```math
F_{\max}\ge V_b/w.
```

For local inverse-field leakage mechanisms the boundary has finite voltage capacity.

The graded absorber's mean-energy dynamics produced the conditional phase boundary

```math
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
```

This revealed a penalty migration:

> grading can suppress one direct-Zener geometry while preserving the conduction-band work that heats the useful electron.

Direction: reconnect transport to where photons are actually absorbed.

---

## Spectral generation geometry

Inside a monotonic graded gap, wavelength determines which part of the absorber is energetically available.

For a linear gap,

```math
x_g(E_\gamma)
=\frac{E_{g,\rm in}-E_\gamma}{G}
```

inside the graded interval.

The exact conditional generation distribution in optical-depth coordinates is

```math
p(y|{\rm abs})
=\frac{e^{-y}}{1-e^{-\tau_\gamma}}.
```

This created a natural map

```text
wavelength
-> generation-position distribution
-> carrier path length / timing.
```

---

## Photoexcitation correction

The first timing pass incorrectly treated every downstream photoelectron as cold.

For local photon excess,

```math
\varepsilon_{\rm gen}
=\xi_e(E_\gamma-E_g).
```

A symmetric two-band model gives `xi_e=1/2`; a simplified flat-heavy-hole HgCdTe Kane channel motivates `xi_e approximately 1` as a limiting case.

Important correction:

> excess photon energy is not automatically persistent **forward longitudinal velocity**. Momentum-space scattering must be modeled separately.

---

## 2026-08-09 — Ballistic entrance-gap timing maximum

A directed-ballistic high-optical-depth model predicted

```text
inside graded gap:
higher photon energy -> generation moves upstream -> delay rises

above entrance gap:
generation pinned at entrance -> extra photon energy raises initial carrier speed -> delay falls.
```

Hence that model gave a maximum at

```math
E_\gamma=E_{g,\rm in}.
```

A deterministic mean-energy-relaxation calculation preserved the peak over the tested parameter range.

At that stage the peak looked like the leading detector-specific prediction.

---

## Momentum-scattering attack kills universal peak

A strong-scattering drift-diffusion model gives

```math
\langle T|d\rangle=d/v_d,
```

and therefore a **rise into a plateau**, not a decline, after the entrance becomes optically allowed.

An underdamped stochastic surrogate showed that the short-wave shape can vary with the initial longitudinal momentum distribution:

```text
persistent forward memory -> decline
rapid randomization -> plateau
symmetric hot longitudinal spread -> decline not guaranteed.
```

Conclusion:

> the entrance-gap timing maximum is model specific, not transport independent.

The more robust object is the switch in how photon energy enters the initial-value problem.

---

## Entrance-gap initial-condition switch

In the sharp-generation limit,

```math
x_g(E_\gamma)
=\max\left[0,\frac{E_{g,\rm in}-E_\gamma}{G}\right],
```

while the excess energy available at the earliest point is

```math
u_g(E_\gamma)
=\max(0,E_\gamma-E_{g,\rm in}).
```

Below the entrance gap, wavelength primarily moves generation position. Above it, generation is pinned and photon energy changes the injected carrier state.

This suggested using the wavelength scan as an **inverse transport measurement** rather than merely looking for a peak/cusp.

---

## Spectral timing velocity inversion

For path-additive delay and downstream collection,

```math
T(x_g)=\int_{x_g}^L\frac{dx}{v_{\rm eff}(x)}.
```

In the sharp linear-gap limit,

```math
\frac{dT}{dE_\gamma}
=\frac1{Gv_{\rm eff}[x_g(E_\gamma)]}.
```

This exposed the core idea:

> a monotonic gap can act as an internal spectral position encoder.

Finite optical depth then turned the point formula into a known spatial convolution.

---

## Full linear inverse replaces differentiation

Let

```math
q(x)=1/v_{\rm eff}(x)
```

inside a local path-additive interpretation.

For known wavelength-dependent generation density `p_i(x)`, mean timing can be written as a linear operator on `q`.

Synthetic tests showed smooth nonuniform profiles could be reconstructed under controlled finite-depth/noise conditions, but singular-value analysis immediately exposed a hard limitation:

> wavelength count is not spatial degree-of-freedom count.

Broader optical kernels destroy fine spatial modes.

Direction: collide with primary detector literature before promoting the inverse.

---

## Prior-art collisions narrow the candidate severely

Primary literature already establishes

- wavelength-dependent photodiode generation depth and bandwidth;
- graded-bandgap acceleration;
- graded HgCdTe response-time modeling;
- position-resolved HgCdTe impulse response using localized excitation.

Perrais et al. already measured HgCdTe timing versus localized generation position.

Sang et al. 2022 already write a wavelength- and depth-dependent generation rate

```math
G_L(z,\lambda)
=\alpha(z,\lambda)\phi_0
\exp\left[-\int_0^z\alpha(u,\lambda)du\right]
```

and combine it with graded-HgCdTe transport/response-time forward modeling.

Therefore the candidate is **not** new spectral-generation/timing physics.

It narrowed to:

> use the known forward optical kernels **in reverse** against measured timing data to reconstruct internal transport.

A 2024 same-group paper titled `Potential application of HgCdTe detector with composition gradient in laser measurement` remains an unresolved close collision because full technical text has not been recovered.

---

## Differential phase makes the inverse experimentally plausible

For the timing distribution,

```math
H_\lambda(\Omega)
=\langle e^{-i\Omega T_\lambda}\rangle.
```

Low-frequency cumulants give

```math
\arg H_\lambda
=-\Omega\langle T_\lambda\rangle+O(\Omega^3),
```

```math
\ln|H_\lambda|
=-\frac{\Omega^2}{2}\operatorname{Var}(T_\lambda)+O(\Omega^4).
```

Thus differential phase measures differential mean delay without requiring direct picosecond pulse-width resolution.

This also suggested a second inverse for timing broadening.

---

## Two-moment inverse

Under additive conditional timing cumulants,

```math
\mu_i=\int K_i(s)q_1(s)ds,
```

and

```math
\sigma_i^2
=\int K_i(s)q_2(s)ds
+\operatorname{Var}_{p_i}[m(X)].
```

The optical generation-position broadening is calculable after the mean-delay profile is estimated.

In a local high-Peclet drift-diffusion approximation only,

```math
q_1=1/v,
\qquad
q_2\simeq2D/v^3.
```

Synthetic tests showed separate slow-transport and high-broadening regions can be numerically distinguished in a controlled normalized problem.

---

## Real-device orientation correction

The 2023 Xu et al. sample geometry forced an important correction.

Its PN junction is at the **high-Cd end**. Long-wave carriers generated deeper toward the low-Cd side return toward that junction.

Therefore for front collection

```math
T_0(x)=\int_0^xq(s)ds,
```

and the correct kernel is the generation **survival function**

```math
\boxed{
S_i(s)=P(X_g\ge s|\lambda_i,{\rm abs}).
}
```

For downstream collection the kernel is instead the CDF

```math
F_i(s)=P(X_g\le s).
```

This orientation correction is now canonical.

---

## Common-delay / broadening identifiability correction

The earlier synthetic inverse appended a wavelength-independent timing offset and recovered it numerically.

That was not proof of structural identifiability.

At the collection boundary the timing kernel tends to unity for every wavelength, so sufficiently boundary-localized internal delay is spectrally degenerate with a common electronics/optical delay.

The same issue applies to second-cumulant broadening.

Conclusion:

> spectral timing robustly identifies **differential spatial transport modes**. Absolute common/boundary timing components require calibration, a gauge constraint, or a physical prior.

Differential phase naturally removes the common wavelength mode.

---

## Published 2023 sample B selected as calibration structure

Xu et al. report sample B with

```text
processed thickness ~3.7 um
nominal FTIR x ~0.316
nonlinear interdiffusion region completely removed
junction at high-Cd end
linear-gradient field ~100-200 V/cm over the measured temperature range.
```

The paper gives the fitted composition model

```math
x(z)
=x_s+s(d-z)
+(1-x_s-sd)
\left\{
1-\left[
\operatorname{erf}\left(2z/\Delta z\right)
\right]^3
\right\},
```

but the actual sample-B fit parameters are only available graphically in the accessible article.

The authors infer that the `100-200 V/cm` linear-gradient field does not strongly affect carrier motion in sample B.

Therefore sample B is best treated as a **smooth calibration case**.

Sample A retains part of the nonlinear region with local field near `2e3 V/cm` and is the better future transport-contrast case.

---

## Real HgCdTe absorption replaces toy power law

Moazzami et al. 2005 provide

```math
\alpha(E,x,T)
=K(x,T)
\left(\frac{E-E_g}{E}\right)^{n(x,T)},
\qquad E>E_g,
```

with empirical composition- and temperature-dependent `K,n` over the relevant HgCdTe range.

The correct Hansen-Schmit-Casselman gap relation with `+0.832x^3` is used.

A machine-readable `0.132x^3` transcription seen in one 2022 article is treated as a typo and is not used.

---

## Dimensional sample-B forward matrix

Because the exact fitted sample-B `x(z)` is unavailable, the present envelope takes `x=0.316` conditionally as the low-Cd endpoint and brackets the linear field by `100, 150, 200 V/cm`.

At 300 K,

```math
E_{g,\rm low}=0.312314\ {\rm eV},
\qquad
\lambda_{g,\rm low}=3.9699\ {\rm um}.
```

The field bracket implies high-Cd local-gap wavelengths of approximately

```text
100 V/cm -> 3.5494 um
150 V/cm -> 3.3708 um
200 V/cm -> 3.2094 um.
```

For the central 150 V/cm envelope, the Moazzami optical model gives approximately

```text
2.80 um: Pabs=0.998, mean depth=0.677 um
3.88 um: Pabs=0.070, mean depth=3.523 um.
```

Thus the conditional mean generation depth moves by

```math
\boxed{\approx2.85\ {\rm um}.}
```

At illustrative `v_eff=1e5 m/s`, that is about `28.5 ps` or `10.25 degrees` at `1 GHz`.

This is a measurement scale, not a sample-B transport prediction.

---

## Real optical matrix reveals few-mode limit

Using

```text
80 spatial cells
0.01 um wavelength steps
Pabs >= 0.05
cell-integrated front-collection survival kernels,
```

the relative singular-mode counts above `[1e-1,1e-2,1e-3,1e-4]` are

```text
100 V/cm -> [2,5,10,20]
150 V/cm -> [2,5,10,21]
200 V/cm -> [2,5,11,23].
```

The earlier pre-cell-integration central `22` at `1e-4` is superseded by `21`.

Conclusion:

> the real few-micron structure supports a **few-mode band-limited transport tomography**, not a pointwise velocity image.

---

## Phase-noise stress test

A synthetic anomaly was imposed on the real central sample-B optical matrix:

```text
baseline v = 1e5 m/s
25% slowdown
center = 2.30 um
Gaussian sigma = 0.35 um
f = 1 GHz.
```

After removing the smooth/common wavelength mode, the anomaly produces only about

```math
\boxed{0.935^\circ}
```

peak-to-peak spectral phase.

A rank-3 reconstruction at `0.10 degree` independent per-wavelength phase noise gives roughly

```text
17.5% median error relative to the recoverable rank-3 target
0.13 um 90%-quantile peak-location error.
```

At `0.25 degree`, localization degrades strongly.

Five-mode recovery is already noise dominated near `0.10 degree` for this anomaly.

Therefore the realistic first target is about **3-4 smooth differential transport modes**, not a finely sampled velocity curve.

---

## Current frontier

The surviving candidate is now very narrow:

> **Use a known graded-HgCdTe optical profile and wavelength-resolved complex RF response to reconstruct a finite set of differential internal mean-delay and timing-broadening modes without physically scanning generation position.**

Priority remains unproven.

Do not write a manuscript yet.

The next decisive work is experimental/data-facing:

1. obtain or digitize the actual 2023 sample-B `x(z)` fit;
2. build a realistic wavelength × RF-frequency covariance model for a tunable-MWIR complex-response measurement;
3. fit multiple RF frequencies rather than one phase point;
4. validate the recovered modes against localized-position timing or calibrated microscopic transport;
5. read the unresolved 2024 laser-measurement paper before any novelty language.

Further generic inverse algebra has lower value than these collisions.
