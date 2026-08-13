# D* / Temporal-Response Prior-Art and Normalization Audit — Experiment 02

**Date:** 2026-08-12  
**Status:** normalization checked; broad novelty rejected; conceptual counterexample retained  
**Priority:** unresolved; no novelty claim

This file audits the Experiment-02 result that equal conventional specific detectivity `D*` does not guarantee equal event-detection performance when detector temporal responses differ.

The audit has two purposes:

1. eliminate one-sided/two-sided PSD normalization ambiguity;
2. determine whether the result is new physics or a transparent consequence of established signal-detection theory plus the conventional definition of `D*`.

---

## 1. General Gaussian decision result

For a known deterministic signal `s(t)` in zero-mean stationary Gaussian noise with two-sided PSD `S_n^(2)(f)`, define Fourier transform by

```math
\tilde s(f)=\int_{-\infty}^{\infty}s(t)e^{-i2\pi ft}dt.
```

The optimum equal-covariance decision distance is

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}
{S_n^{(2)}(f)}df.
}
```

If the optical input is `p(t)` and detector frequency response is absorbed into the input-referred noise-equivalent-power ASD, define

```math
\mathrm{NEP}_2^2(f)
=\frac{S_n^{(2)}(f)}{|R(f)|^2}.
```

Then

```math
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_2^2(f)}df.
}
```

This is the clean task-specific object. A scalar `D*` retains only a conventional low-frequency/band-limited normalization of this richer spectral object.

---

## 2. One-pole impulse benchmark

Take a detector whose normalized impulse response is

```math
h(t)
=\frac1\tau e^{-t/\tau}u(t).
```

Then

```math
H(f)
=\frac{1}{1+i2\pi f\tau}.
```

For an optical impulse of energy `E`,

```math
p(t)=E\delta(t),
```

the output signal is proportional to

```math
E h(t).
```

Parseval gives

```math
\int_{-\infty}^{\infty}|h(t)|^2dt
=\frac{1}{2\tau},
```

and equivalently

```math
\int_{-\infty}^{\infty}|H(f)|^2df
=\frac{1}{2\tau}.
```

---

## 3. Two-sided NEP convention

Let `NEP_2` denote a constant **two-sided** input-referred amplitude spectral density, so its squared value has units `W^2/Hz`.

Then

```math
\boxed{
d^2
=\frac{E^2}{2\tau\,\mathrm{NEP}_2^2}.
}
```

This is the correct two-sided normalization.

---

## 4. One-sided NEP convention

For a real stationary process,

```math
S_n^{(1)}(f)=2S_n^{(2)}(f),
\qquad f>0.
```

Therefore

```math
\mathrm{NEP}_1^2=2\mathrm{NEP}_2^2.
```

The matched-filter distance can be written in one-sided form as

```math
\boxed{
d^2
=4\int_0^\infty
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_1^2(f)}df.
}
```

For the one-pole impulse,

```math
\int_0^\infty|H(f)|^2df
=\frac{1}{4\tau},
```

so

```math
\boxed{
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}_1^2}.
}
```

Thus the two formulas

```math
d^2=E^2/(2\tau\mathrm{NEP}_2^2)
```

and

```math
d^2=E^2/(\tau\mathrm{NEP}_1^2)
```

are exactly equivalent.

---

## 5. Conventional D* form

Using the usual amplitude-spectral-density form

```math
\boxed{
D^*
=\frac{\sqrt A}{\mathrm{NEP}_1}
}
```

for the stated one-sided convention, the benchmark becomes

```math
\boxed{
d^2
=\frac{E^2D^{*2}}{A\tau}.
}
```

Therefore the existing Experiment-02 `D*` formula is correct **provided the one-sided NEP convention is stated explicitly**.

### Documentation lock

Do not combine

```math
\int_{-\infty}^{\infty}|p|^2/\mathrm{NEP}_2^2 df
```

with

```math
d^2=E^2/(\tau\mathrm{NEP}_2^2)
```

for the same two-sided `NEP_2`; that would be a factor-of-two error.

---

## 6. What equal D* actually fixes in this benchmark

For equal area and equal conventional low-frequency `D*`, two detectors have the same one-sided low-frequency NEP ASD.

That does **not** fix

```text
impulse-response shape;
response time;
full NEP(f);
noise color;
timing jitter;
signal-dependent noise;
search-window burden.
```

For one-pole detectors with equal `A` and `D*`,

```math
\frac{d_A^2}{d_B^2}
=\frac{\tau_B}{\tau_A}
```

for the stated short-impulse/white-input-referred-noise benchmark.

Hence a faster detector has a larger optimum known-time impulse decision distance in this particular model.

This is **conditional**, not a universal theorem that faster is always better.

---

## 7. Why the result is not new signal-detection theory

The general result

```math
d^2=\int |s(f)|^2/S_n(f)df
```

is standard matched-filter / Gaussian hypothesis-testing theory.

Specific detectivity `D*` is a conventional radiation-detector figure of merit designed to normalize noise-equivalent sensitivity by detector area and bandwidth convention; it is not a complete arbitrary-waveform decision functional.

Therefore the statement

> equal scalar `D*` does not imply equal SNR for arbitrary time-dependent signals

is a direct consequence of established detection theory once two detectors have different transfer functions / noise spectra.

### Current disposition

**DERIVED PHOTODETECTOR COUNTEREXAMPLE / PRIOR ART IN UNDERLYING THEORY / NO NOVELTY CLAIM.**

---

## 8. R. Clark Jones lineage

Specific detectivity traces to the radiation-detector figure-of-merit work of R. Clark Jones, including the classic paper

```text
R. Clark Jones,
Phenomenological Description of the Response and Detecting Ability of Radiation Detectors,
Proceedings of the IRE 47 (1959).
```

The exact bibliographic metadata and convention definitions should be verified from the primary source before manuscript citation.

The historical purpose of `D*` was normalization/comparison of detector sensitivity under a declared measurement bandwidth/area convention, not representation of every possible optical waveform decision problem.

---

## 9. Direct photodetector FOM prior-art collision

S. J. van Enk's

```text
Photodetector figures of merit in terms of POVMs
(arXiv:1705.09640, 2017)
```

already emphasizes that photodetectors possess multiple figures of merit—response time, bandwidth, dark counts, efficiency, spectral/photon-number resolution, etc.—and derives detector figures of merit from a fuller quantum measurement description.

This reinforces the claim boundary:

```text
one scalar detector FOM is not a complete platform-independent detector description
```

is not an Experiment-02 novelty.

---

## 10. What remains scientifically useful

The branch is still valuable because the one-pole benchmark gives a very transparent counterexample:

```text
same conventional D*
same area
but different tau
-> different optimum impulse decision distance.
```

For readers accustomed to interpreting `D*` as a global detector ranking, the equation

```math
\boxed{
d^2=E^2D^{*2}/(A\tau)
}
```

makes the missing temporal coordinate explicit with minimal machinery.

Its value is explanatory and diagnostic, not foundational novelty.

---

## 11. Stronger general statement

The real task-level quantity is

```math
\boxed{
d_D^2[p]
=\int_{-\infty}^{\infty}
\frac{|\tilde p(f)|^2}
{\mathrm{NEP}_{2,D}^2(f)}df.
}
```

or its one-sided equivalent.

Two detectors are ordered for every waveform in an allowed linear-Gaussian task class only under stronger spectral dominance conditions such as

```math
\frac{1}{\mathrm{NEP}_{A}^2(f)}
\ge
\frac{1}{\mathrm{NEP}_{B}^2(f)}
```

throughout the relevant band.

If their spectral decision kernels cross, tasks can reverse the ranking.

That is an application of the broader statistical-experiment/channel-order logic already identified in `MATHEMATICAL_PRIOR_ART_AUDIT.md`.

---

## 12. Audit disposition

| Statement | Disposition |
|---|---|
| Gaussian matched-filter waveform distance | **ESTABLISHED DETECTION THEORY** |
| conventional `D*` as bandwidth/area-normalized detector FOM | **ESTABLISHED RADIATION-DETECTOR METROLOGY** |
| one-sided one-pole formula `d^2=E^2D*^2/(A tau)` | **DERIVED SPECIAL CASE / CORRECT WITH EXPLICIT CONVENTION** |
| equal `D*` does not imply equal arbitrary-waveform performance | **DIRECT CONSEQUENCE / NO NOVELTY CLAIM** |
| full `NEP(f)` decision kernel as task-relevant object | **STANDARD SIGNAL-DETECTION CONSEQUENCE** |
| task ranking reversal when kernels cross | **DECISION-THEORY CONSEQUENCE / NO NOVELTY CLAIM** |

---

## 13. Direction after this audit

The `D*` branch should remain as a clear motivating example, not as the novelty center.

The next quantitative audits should focus on the more detector-specific equations where ordinary textbook reduction is less obvious:

```text
retention/reset control-range relation;
source-inclusive thermodynamic accounting;
critical-coupling control-floor threshold in a real detector architecture;
possible physical constraints on achievable detector-process regions.
```

Any eventual paper-worthy result must survive direct source-level comparison and must add more than a repackaging of established matched-filter / detector-FOM theory.
