# HgCdTe Spectral Timing by Differential Phase — A Practical Frequency-Domain Route to the Inverse

**Date:** 2026-08-09  
**Status:** exact low-frequency cumulant relation plus experimental-resolution estimates for wavelength-resolved timing; no novelty claim

## 1. Purpose

The spectral timing inverse reconstructs a spatial delay density from wavelength-dependent intrinsic mean carrier delay.

Directly resolving picosecond changes in a nanosecond-scale impulse response can be experimentally awkward.

The 2022 high-speed graded-HgCdTe study already used a vector-network-analyzer / Lightwave Component Analyzer frequency-response setup over approximately `50 MHz` to `1 GHz`, but with a fixed `1550 nm` optical source that caused strong surface absorption.

This note asks:

> Can the proposed wavelength scan use **differential phase** rather than raw pulse-width differences to access the carrier-delay information?

Yes, provided the modulation frequency remains in the low-order cumulant regime for the wavelength-dependent carrier timing distribution.

---

## 2. Timing distribution transfer function

Let the carrier collection time for a detected photon at wavelength `lambda` be the random variable

```math
T_\lambda.
```

The intrinsic timing transfer factor is the characteristic function

```math
\boxed{
H_\lambda(\Omega)
=\left\langle
 e^{-i\Omega T_\lambda}
\right\rangle.
}
```

Its cumulant expansion is

```math
\boxed{
\ln H_\lambda(\Omega)
=
\sum_{n=1}^{\infty}
\frac{(-i\Omega)^n}{n!}
\kappa_n(\lambda),
}
```

where

```text
kappa_1 = mean delay
kappa_2 = timing variance
kappa_3 = third cumulant
...
```

---

## 3. Phase expansion

Taking the imaginary part,

```math
\boxed{
\arg H_\lambda(\Omega)
=-\Omega\kappa_1(\lambda)
+\frac{\Omega^3}{6}\kappa_3(\lambda)
-\frac{\Omega^5}{120}\kappa_5(\lambda)
+\cdots.
}
```

Therefore at sufficiently low modulation frequency,

```math
\boxed{
\arg H_\lambda(\Omega)
\simeq
-\Omega\langle T_\lambda\rangle.
}
```

The low-frequency group delay is exactly

```math
\boxed{
\tau_g(\lambda)
=-\left.
\frac{d}{d\Omega}
\arg H_\lambda(\Omega)
\right|_{\Omega=0}
=\langle T_\lambda\rangle.
}
```

Thus the mean carrier delay required by the inverse is a natural low-frequency phase observable.

---

## 4. Differential wavelength measurement cancels common electronics

Suppose the measured transfer function factorizes approximately as

```math
\boxed{
H_{\rm meas}(\Omega,\lambda)
=H_{\rm carrier}(\Omega,\lambda)
H_{\rm common}(\Omega),
}
```

where `H_common` is wavelength independent.

For two wavelengths,

```math
\boxed{
\frac{H_{\rm meas}(\Omega,\lambda_1)}
{H_{\rm meas}(\Omega,\lambda_2)}
=
\frac{H_{\rm carrier}(\Omega,\lambda_1)}
{H_{\rm carrier}(\Omega,\lambda_2)}.
}
```

Therefore the differential phase is

```math
\boxed{
\Delta\phi_{12}(\Omega)
=\arg H_{\rm meas}(\Omega,\lambda_1)
-\arg H_{\rm meas}(\Omega,\lambda_2).
}
```

In the low-frequency timing regime,

```math
\boxed{
\Delta\phi_{12}(\Omega)
\simeq
-\Omega
\left[
\bar T(\lambda_1)-\bar T(\lambda_2)
\right].
}
```

Hence

```math
\boxed{
\Delta T_{12}
\simeq
-\frac{\Delta\phi_{12}}{\Omega}.
}
```

This is the direct frequency-domain timing observable.

---

## 5. Finite-frequency validity criterion

The first phase correction is controlled by the third cumulant:

```math
\delta\phi_3
=\frac{\Omega^3}{6}\kappa_3.
```

Relative to the leading mean-delay phase,

```math
\left|
\frac{\delta\phi_3}
{\Omega\bar T}
\right|
\sim
\frac{\Omega^2|\kappa_3|}
{6\bar T}.
```

A simpler conservative diagnostic is

```math
\boxed{
\Omega\sigma_T\ll1,
}
```

which keeps the timing distribution spectrally unresolved enough that the phase is dominated by its first moment.

If this condition fails, do not discard the data.

Instead fit the **full complex transfer function** using the calculated timing-distribution forward model.

Thus

```text
low Omega
-> mean-delay phase inversion

higher Omega
-> richer timing-distribution spectroscopy / full forward fit.
```

---

## 6. Phase precision maps directly into transit-distance precision

For a local effective velocity `v_eff`, a small transport-distance change produces

```math
\Delta T\simeq\frac{\Delta x}{v_{\rm eff}}.
```

Using

```math
\Delta\phi\simeq-\Omega\Delta T,
```

```math
\boxed{
|\Delta\phi|
\simeq
\Omega\frac{|\Delta x|}{v_{\rm eff}}.
}
```

Therefore phase uncertainty `sigma_phi` corresponds approximately to

```math
\boxed{
\sigma_{x,\phi}
\sim
\frac{v_{\rm eff}\sigma_\phi}{\Omega}.
}
```

This is the frequency-domain analogue of

```math
\sigma_{x,T}\sim v_{\rm eff}\sigma_T.
```

---

## 7. Illustrative phase scales

Take only as a transparent scale

```math
v_{\rm eff}=10^5\ {\rm m/s}.
```

At

```math
f=1\ {\rm GHz},
```

one degree of phase is

```math
\sigma_\phi
=\frac{\pi}{180}.
```

Then

```math
\boxed{
\sigma_{x,\phi}
\approx0.28\ {\rm um}.
}
```

At

```math
f=500\ {\rm MHz},
```

the same one-degree phase precision corresponds to approximately

```math
\boxed{
\sigma_{x,\phi}
\approx0.56\ {\rm um}.
}
```

These are **not** performance claims for any specific instrument or HgCdTe velocity.

They show why frequency-domain phase can access micron/submicron transport contrasts without measuring an isolated `1 ps` pulse-width change directly.

---

## 8. Existing 2022 graded-HgCdTe timing hardware is adjacent but not sufficient by itself

The 2022 graded-HgCdTe work reports

```text
100 fs pulses at 1.55 um
80 MHz repetition rate
20-GHz sampling module
```

for impulse response, and an LCA / network-analyzer measurement over approximately

```text
50 MHz to 1 GHz
```

with a `1550 nm`, `5 mW` modulated optical source.

The authors explicitly state that `1550 nm` undergoes strong surface absorption.

Therefore their RF timing chain is conceptually well matched to differential-phase timing, but the **optical source is not the required spectral scanner**.

The proposed experiment needs a tunable/modulated MWIR source that scans the graded absorption interval while preserving stable phase referencing.

---

## 9. Candidate optical implementations

The repository should not prematurely choose one hardware solution.

Possible routes include

- tunable pulsed OPO plus time-domain centroid extraction;
- directly modulated / externally modulated QCL or ICL sources over selected wavelengths;
- two-source optical heterodyne / photomixing methods where a controlled RF beat is available;
- frequency-comb / dual-comb approaches if spectral timing phase can be referenced robustly.

The high-speed MWIR/LWIR literature emphasizes that ordinary telecom-style broadband modulators are not generally available across these infrared bands.

Therefore source architecture is a genuine experimental design constraint.

---

## 10. Full inverse in phase form

The linear timing inverse is

```math
\boxed{
\mathbf T
=\mathbf A\mathbf q+c\mathbf1.
}
```

At a modulation frequency within the linear phase regime,

```math
\boldsymbol\phi
\simeq
-\Omega
(\mathbf A\mathbf q+c\mathbf1)
+\phi_0\mathbf1,
```

where `phi_0` collects wavelength-independent instrument phase.

Equivalently,

```math
\boxed{
-\frac{\boldsymbol\phi}{\Omega}
=\mathbf A\mathbf q+c'\mathbf1
}
```

for a fitted nuisance constant `c'`.

Thus the same regularized inverse machinery applies directly to phase data.

No numerical phase derivative with respect to frequency is required if a low enough fixed modulation frequency is used and the first-moment approximation is validated.

Using several modulation frequencies provides a consistency check and access to higher timing cumulants.

---

## 11. Multiple-frequency extension

Measure complex response at frequencies `Omega_k` and wavelengths `lambda_i`.

In the low-order regime,

```math
\phi_{ik}
=-\Omega_k\bar T_i
+\frac{\Omega_k^3}{6}\kappa_{3,i}
+\phi_{\rm common}(\Omega_k)
+\cdots.
```

A joint fit can separate

```text
mean delay
third timing cumulant / asymmetry
common electrical phase.
```

Similarly, the logarithmic magnitude contains even cumulants:

```math
\boxed{
\ln|H_\lambda(\Omega)|
=-\frac{\Omega^2}{2}\sigma_T^2
+\frac{\Omega^4}{24}\kappa_4
+\cdots.
}
```

Thus the same frequency sweep can, in principle, constrain both

```text
mean transit profile
+
timing spread / diffusion profile.
```

This is a possible later extension, not yet a validated HgCdTe inversion.

---

## 12. Experimental systematics

Differential phase cancels only wavelength-independent common response.

Potential wavelength-dependent contaminants include

- optical-path phase / group delay through tunable-source optics;
- wavelength-dependent cable/photonic reference path if the setup changes between wavelengths;
- wavelength-dependent penetration into non-active/passivation/contact layers;
- wavelength-dependent device capacitance or impedance through changing carrier populations;
- source modulation phase changing with wavelength.

A reference arm or calibration detector may be required.

The inverse should never interpret uncalibrated source phase as carrier transit.

---

## 13. Claim boundary

### Derived

- low-frequency phase equals minus modulation frequency times mean arrival delay to leading order;
- differential wavelength phase cancels a wavelength-independent common transfer function;
- spatial phase-resolution scale
  ```math
  sigma_x ~ v_eff sigma_phi / Omega;
  ```
- direct phase-domain form of the linear transport inverse.

### Established prior physics

- photodiode bandwidth characterization using VNA/LCA phase and amplitude;
- the 2022 graded-HgCdTe VNA/LCA setup;
- timing cumulants / characteristic-function expansion.

### Not established

- achievable phase precision with a tunable MWIR implementation;
- wavelength-independent instrument phase at the required precision;
- a real reconstructed HgCdTe transport profile;
- novelty.

---

## 14. Next decisive work

The inverse method now has a plausible measurement observable.

The next high-value step is to take an actual published `x(z)` / `alpha(z,lambda)` profile and calculate

```text
A matrix
singular values
predicted differential phase per wavelength
required phase precision
```

for a realistic set of modulation frequencies.

If the resulting phase contrasts are comfortably measurable with plausible instrumentation, the method graduates from mathematical possibility to a credible experimental proposal.
