# Continuous Gaussian Readout and Conventional Detector Metrics — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional derivation  
**Priority:** unassessed; no novelty claim

This file replaces the binary click/no-click readout in `SEMICONDUCTOR_DECISION_BRIDGE.md` with a continuous current or voltage waveform corrupted by stationary Gaussian noise.

The goal is to identify the decision-theoretic quantity underlying responsivity, NEP, `D*`, bandwidth, and integration time.

---

## 1. Binary waveform hypotheses

Let the measured electrical output be

```math
H_0:\quad y(t)=n(t),
```

```math
H_1:\quad y(t)=s(t)+n(t),
```

where

```text
s(t) = deterministic mean electrical signal caused by the optical event
n(t) = zero-mean Gaussian detector/readout noise.
```

Assume initially that the noise covariance is the same under both hypotheses.

This is the standard Gaussian shift-detection problem.

---

## 2. The exact decision coordinate is Mahalanobis distance

Discretize the observation or treat the continuum formally. If the noise covariance operator is `C`, define

```math
\boxed{
d^2
=\langle s,C^{-1}s\rangle.
}
```

For stationary noise with a **two-sided** output-noise PSD `S_n^{(2)}(f)` and Fourier transform `s_tilde(f)`, this becomes

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}
{S_n^{(2)}(f)}\,df.
}
```

This is the matched-filter / noise-whitened signal energy.

It is dimensionless.

---

## 3. Exact equal-prior error

The log-likelihood ratio is Gaussian.

Under `H0` it has mean `-d^2/2`; under `H1` it has mean `+d^2/2`; under either hypothesis its variance is `d^2`.

With equal priors and the optimum threshold,

```math
\boxed{
P_e
=Q\left(\frac{d}{2}\right),
}
```

where `Q` is the standard normal upper-tail function.

The classical total-variation distance between the complete waveform distributions is

```math
\boxed{
\mathcal D_{\rm TV}
=1-2P_e
=\operatorname{erf}\left(
\frac{d}{2\sqrt2}
\right).
}
```

Thus the continuous-output analogue of the earlier detector-state distinguishability is controlled entirely by `d` in this Gaussian equal-covariance model.

---

## 4. Matched filter interpretation

The optimum linear statistic is proportional to

```math
\tilde w(f)
\propto
\frac{\tilde s^*(f)}{S_n^{(2)}(f)}.
```

Therefore the detector does not merely need a large peak signal.

It needs signal energy in frequencies where the noise is small.

This produces a strong generalization of the earlier rate/bandwidth results:

> **useful detector information is the signal waveform measured in the inverse-noise metric.**

---

## 5. Refer the noise back to optical input

Suppose an incident optical-power waveform `p(t)` produces electrical signal

```math
\tilde s(f)
=\mathcal R(f)\tilde p(f),
```

where `mathcal R(f)` is the complex electrical responsivity including detector temporal transfer.

Define the two-sided input-referred optical noise PSD

```math
\boxed{
S_P^{(2)}(f)
=\frac{S_n^{(2)}(f)}
{|\mathcal R(f)|^2}.
}
```

Then

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde p(f)|^2}
{S_P^{(2)}(f)}\,df.
}
```

Equivalently, define a frequency-dependent two-sided NEP by

```math
\mathrm{NEP}_2^2(f)=S_P^{(2)}(f).
```

Then

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_2^2(f)}\,df.
}
```

This is the natural decision-theoretic replacement for treating a single quoted NEP as the whole detector.

---

## 6. What a scalar D* does and does not contain

A conventional specific detectivity is schematically

```math
D^*(f)
=\frac{\sqrt A}{\mathrm{NEP}(f)},
```

under the measurement convention being used.

Therefore a full frequency-dependent `D*(f)` can be inserted into the decision integral.

But one scalar quoted at one frequency cannot generally determine

```math
\int
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}^2(f)}df.
```

Two detectors can have identical quoted `D*` at the reference frequency while having different

```text
response time,
frequency rolloff,
colored noise,
resonances,
1/f corners,
integration-window response,
```

and therefore different waveform-discrimination error.

This is a direct decision-theoretic reason why conventional `D*` is not a complete detector boundary.

---

## 7. White-noise one-pole impulse benchmark

Now take a simple detector with DC responsivity `R_0` and one-pole impulse response

```math
h(t)
=\frac{1}{\tau}e^{-t/\tau}u(t),
```

so

```math
\int_0^\infty h(t)dt=1.
```

Let a short optical pulse deposit/arrive with energy `E`, so

```math
p(t)=E\delta(t).
```

The mean electrical signal is

```math
\boxed{
s(t)
=\frac{R_0E}{\tau}e^{-t/\tau}u(t).
}
```

Its squared time-domain signal energy is

```math
\boxed{
\int_0^\infty s^2(t)dt
=\frac{(R_0E)^2}{2\tau}.
}
```

---

## 8. White one-sided output-noise PSD

Let the output current/voltage noise have flat **one-sided** PSD `S_n^{(1)}`.

The corresponding two-sided PSD is

```math
S_n^{(2)}=S_n^{(1)}/2.
```

Therefore

```math
\boxed{
d^2
=\frac{(R_0E)^2}
{\tau S_n^{(1)}}.
}
```

Define the usual white input-referred one-sided NEP

```math
\mathrm{NEP}
=\frac{\sqrt{S_n^{(1)}}}{R_0}.
```

Then

```math
\boxed{
d^2
=\frac{E^2}
{\tau\,\mathrm{NEP}^2}.
}
```

and

```math
\boxed{
P_e
=Q\left(
\frac{E}{2\,\mathrm{NEP}\sqrt\tau}
\right).
}
```

This is a compact pulse-detection law for the stated idealized model.

---

## 9. Equal D* does not imply equal pulse detectability

If

```math
\mathrm{NEP}=\frac{\sqrt A}{D^*},
```

then

```math
\boxed{
d^2
=\frac{E^2D^{*2}}
{A\tau}.
}
```

Thus for two detectors with the same area and the same low-frequency white-noise `D*`, but different response times,

```math
\boxed{
d\propto\tau^{-1/2}.}
```

The faster detector has better discrimination of a short fixed-energy optical event in this model.

This is a precise counterexample to

```text
same D* -> same event-detection performance.
```

The result is conditional on

```text
same active area,
same quoted low-frequency D*,
white output noise,
single-pole response,
short optical pulse,
matched-filter readout,
no saturation/gain complications.
```

It must not be generalized beyond those assumptions without using the full spectral decision integral.

---

## 10. Finite observation time

If the electrical waveform is observed only over `0<t<T`, then

```math
\int_0^T s^2(t)dt
=
\frac{(R_0E)^2}{2\tau}
\left(1-e^{-2T/\tau}\right).
```

Hence

```math
\boxed{
d^2(T)
=
\frac{E^2}
{\tau\,\mathrm{NEP}^2}
\left(1-e^{-2T/\tau}\right).
}
```

For

```math
T\ll\tau,
```

```math
d^2(T)
\simeq
\frac{2E^2T}
{\tau^2\mathrm{NEP}^2}.
```

For

```math
T\gg\tau,
```

```math
d^2(T)
\rightarrow
\frac{E^2}
{\tau\mathrm{NEP}^2}.
```

Therefore a slow detector pays twice under a strict short decision deadline: its signal is smaller initially and much of the available matched-filter energy has not yet appeared.

---

## 11. The physically invariant object is the whole signal/noise spectrum

The one-pole result is not fundamental.

The general quantity remains

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\mathcal R(f)\tilde p(f)|^2}
{S_n^{(2)}(f)}df.
}
```

or equivalently

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_2^2(f)}df.
}
```

This formula automatically handles

```text
multiple poles,
colored noise,
1/f noise,
GR-like noise peaks,
resonant detector response,
finite pulse duration,
modulated signals,
matched filtering,
```

provided the Gaussian equal-covariance approximation is valid.

---

## 12. A new interpretation of detector figures of merit

The hierarchy is now

```text
microscopic detector physics
-> responsivity transfer R(f)
   and output-noise PSD S_n(f)
-> input-referred NEP(f)
-> noise-weighted waveform distance d
-> decision error P_e.
```

Thus

```text
responsivity
NEP
D*
bandwidth
time constant
```

are not independent definitions of detection.

They are lower-level descriptors that enter the hypothesis-distance functional.

A detector figure of merit is complete for a task only if it preserves enough information to compute the relevant decision distance.

---

## 13. Connection back to the photodetector-boundary question

The original question asked when matter becomes a detector.

At the electrical-output level, the answer becomes especially concrete:

> **matter functions as a detector for a specified optical task when the photon-conditioned output waveform is sufficiently separated from the no-photon output distribution in the inverse-noise metric over the allowed observation interval.**

This makes the detector boundary explicitly task dependent.

The same physical device can be

```text
excellent for slow narrowband power sensing
but
poor for fast single-event discrimination,
```

without contradiction.

---

## 14. Strong conceptual consequence

A single scalar `D*` is not the fundamental detector coordinate because it discards the spectral/temporal structure needed for a decision problem.

The more complete object is something like

```math
\boxed{
\mathcal J[p]
=\int
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}^2(f)}df,
}
```

with exact factors determined by one-sided/two-sided conventions.

`mathcal J` is task dependent through the incident waveform `p(t)`.

Thus there may be no architecture-independent scalar detector quality at all unless the class of optical tasks is first specified.

---

## 15. Current next attacks

1. Extend from equal-covariance Gaussian noise to signal-dependent noise, especially generation-recombination and shot noise.
2. Include random photon arrival time / timing jitter and derive the penalty for unknown temporal alignment.
3. Ask whether an optimal scalar task-specific detectivity can be defined from the matched-filter distance.
4. Compare this decision formulation directly with conventional `D*`, NEP, bandwidth, and the separate equal-`D*` fast-versus-slow Gedanken experiment without silently merging the two projects.
5. Perform a primary-source audit of classical detection theory / matched filtering and detector-metric conventions before novelty language.
