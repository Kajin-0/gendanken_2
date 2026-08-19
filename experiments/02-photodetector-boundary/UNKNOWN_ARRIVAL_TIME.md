# Unknown Arrival Time and Timing Search — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional derivation  
**Priority:** unassessed; no novelty claim

The previous continuous Gaussian calculation assumed the photon-conditioned waveform was aligned in time. This file removes that assumption.

The purpose is to ask whether uncertainty in *when* the optical event occurs creates another unavoidable detector resource coordinate.

---

## 1. Known arrival time benchmark

For common Gaussian covariance `C`, suppose the event waveform is `s_tau(t)=s(t-tau)`.

If `tau` is known, the log-likelihood ratio is linear in the matched-filter statistic

```math
z_\tau
=\frac{\langle y,C^{-1}s_\tau\rangle}{d},
```

where

```math
\boxed{
d^2=\langle s_\tau,C^{-1}s_\tau\rangle.
}
```

For a stationary observation away from boundaries, `d` is independent of the shift.

Under normalized conventions,

```text
H0: z_tau ~ N(0,1)
H1 at the known tau: z_tau ~ N(d,1).
```

The known-time equal-prior error is

```math
P_e=Q(d/2).
```

---

## 2. Unknown arrival time makes H1 a mixture

Let the arrival time have prior density `p(tau)`.

Then

```math
p(y|H_1)
=\int d\tau\,p(\tau)\,p(y|s_\tau).
```

For common Gaussian covariance, the exact likelihood ratio is

```math
\boxed{
\Lambda(y)
=\int d\tau\,p(\tau)
\exp\left[
\langle y,C^{-1}s_\tau\rangle
-\frac12\langle s_\tau,C^{-1}s_\tau\rangle
\right].
}
```

Thus the optimum detector is no longer one aligned matched filter.

It is a weighted integration over a **bank of time-shifted matched filters**.

This is the continuous-time analogue of marginalizing over an unknown nuisance parameter.

---

## 3. M independent candidate arrival bins

To expose the timing penalty cleanly, take an idealized benchmark with `M` mutually orthogonal / statistically independent candidate templates of equal norm.

Let the normalized matched-filter outputs be

```math
z_1,\ldots,z_M.
```

Under `H0`,

```math
z_m\overset{\rm iid}{\sim}\mathcal N(0,1).
```

Under `H1`, assume one unknown bin `J` contains the event and `J` is uniform on `1,...,M`:

```text
z_J ~ N(d,1)
all other z_m ~ N(0,1).
```

The exact likelihood ratio is

```math
\boxed{
\Lambda(z)
=\frac1M
\sum_{m=1}^M
\exp\left(dz_m-\frac{d^2}{2}\right).
}
```

This is a log-sum-exp detector.

For `M=1`, it reduces to the ordinary matched filter.

---

## 4. Strong-signal limit becomes a max search

When one candidate filter dominates the sum,

```math
\ln\Lambda
\approx
dz_{\max}-\frac{d^2}{2}-\ln M,
```

where

```math
z_{\max}=\max_m z_m.
```

The equal-prior decision boundary is approximately

```math
\boxed{
z_{\max}
\gtrsim
\frac d2+\frac{\ln M}{d}.
}
```

The extra term

```math
\frac{\ln M}{d}
```

is the explicit price of not knowing which temporal mode contains the event.

This already shows that arrival-time uncertainty is a resource coordinate independent of the known-time waveform SNR.

---

## 5. Exact false-alarm probability for the max benchmark

For a threshold `eta`, under `H0`

```math
P(z_{\max}<\eta|H_0)
=\Phi(\eta)^M.
```

Therefore

```math
\boxed{
P_{\rm FA}
=1-\Phi(\eta)^M.
}
```

To impose target false-alarm probability `alpha`, choose

```math
\boxed{
\eta_\alpha
=\Phi^{-1}\left[(1-\alpha)^{1/M}\right].
}
```

For large `M` and small `alpha`, the leading scaling is

```math
\boxed{
\eta_\alpha
\sim
\sqrt{2\ln(M/\alpha)}
}
```

up to the usual logarithmic extreme-value corrections.

Thus the required normalized matched-filter amplitude grows only logarithmically with the number of searched temporal cells, but it does grow.

---

## 6. Detection probability when one bin contains the signal

For the same max-threshold benchmark, under `H1` with one signal bin,

```math
P_{\rm miss}
=
P(z_J<\eta)
\prod_{m\ne J}P(z_m<\eta).
```

Hence

```math
\boxed{
P_{\rm miss}
=
\Phi(\eta-d)\Phi(\eta)^{M-1}.
}
```

and

```math
\boxed{
P_D
=1-\Phi(\eta-d)\Phi(\eta)^{M-1}.
}
```

For fixed false-alarm target `alpha` and miss target `beta`, a sufficient/benchmark requirement is

```math
\boxed{
d
\ge
\eta_\alpha
-
\Phi^{-1}\left[
\frac{\beta}{\Phi(\eta_\alpha)^{M-1}}
\right].
}
```

For small `alpha` this is approximately

```math
d
\gtrsim
\eta_\alpha+z_{1-\beta},
```

where `z_{1-beta}` is the corresponding normal quantile.

The known-time requirement is recovered when `M=1`.

---

## 7. Timing uncertainty creates a trials factor, not an N-like linear cost

The independent-bin benchmark gives

```text
search-window enlargement
-> more statistically independent candidate event times
-> larger false-alarm threshold
-> higher required waveform distance d.
```

The penalty scales roughly as

```math
\sqrt{2\ln M}
```

rather than as `sqrt(M)` or `M`.

This is important: uncertainty about arrival time is costly, but the optimum search uses the structure of the problem rather than paying for every candidate independently.

---

## 8. Effective number of temporal trials is a time-bandwidth resource

Real shifted templates are correlated, so literal sample count is not the correct `M`.

A rough independent-cell estimate is

```math
\boxed{
M_{\rm eff}
\sim
T_{\rm search}\,B_{\rm eff},
}
```

up to convention-dependent order-unity factors and the actual template/noise correlation function.

Here

```text
T_search = allowed event-arrival search window
B_eff    = effective noise-whitened signal bandwidth.
```

This estimate is **heuristic**, not a universal theorem.

The robust statement is that the temporal search penalty is set by the number of effectively distinguishable shifted signal modes, not the digitizer sample count.

Thus another detector coordinate appears:

```math
\boxed{
\text{temporal search complexity}
\sim T_{\rm search}B_{\rm eff}.
}
```

---

## 9. Bandwidth has two opposing roles

Earlier results showed that insufficient detector bandwidth suppresses the waveform distance for a fast event.

The timing-search calculation adds the opposite effect:

```text
more bandwidth
-> sharper temporal localization / larger known-time signal space
but also
-> more distinguishable candidate arrival-time cells inside a fixed search window.
```

So bandwidth is not monotonically equivalent to detection performance once arrival time is unknown.

The optimum depends on the complete task:

```text
known versus unknown arrival time
search-window duration
false-alarm budget
signal spectrum
noise spectrum
allowed processing.
```

This is another failure of a one-scalar detector-quality picture.

---

## 10. Random timing jitter is a mixture, not simply a broader deterministic pulse

Suppose the detector latency or arrival time has random shift `tau` with density `p(tau)`.

The exact `H1` distribution is the mixture

```math
p(y|H_1)
=\int p(\tau)p(y|s_\tau)d\tau.
```

Replacing this mixture by its mean waveform generally loses information and is not the optimum detector.

Nevertheless, if one deliberately uses only the mean template, then

```math
\bar s(t)
=\int p(\tau)s(t-\tau)d\tau.
```

In frequency space,

```math
\boxed{
\tilde{\bar s}(f)
=\tilde s(f)\,\Phi_\tau(f),
}
```

where

```math
\Phi_\tau(f)
=E[e^{-i2\pi f\tau}]
```

is the characteristic function of the timing jitter.

For Gaussian jitter with standard deviation `sigma_t`,

```math
\boxed{
|\Phi_\tau(f)|^2
=e^{-4\pi^2f^2\sigma_t^2}.
}
```

A mean-template Gaussian matched-filter benchmark therefore gives

```math
\boxed{
\bar d^2
=\int
\frac{|\tilde s(f)|^2
|\Phi_\tau(f)|^2}
{S_n^{(2)}(f)}df.
}
```

High-frequency timing information is preferentially destroyed by jitter if the timing itself is not estimated.

---

## 11. Timing information can be recovered if it is estimated jointly

The mean-template penalty above is not fundamental.

An optimum likelihood method can jointly infer

```text
event present / absent
and
arrival time.
```

The price then appears through the nuisance-parameter search / mixture likelihood rather than simply through waveform smearing.

This distinction parallels several earlier lessons:

```text
tracing out outgoing light can make information appear lost;
using only mean response can make covariance information appear lost;
using only an averaged waveform can make timing information appear lost.
```

What counts as detector information depends on what the observer is allowed to measure and infer.

---

## 12. New detector-boundary coordinate

The detector decision problem now needs at least three temporal quantities that must not be conflated:

```text
intrinsic detector response time / bandwidth
record-retention time
arrival-time uncertainty / search window.
```

A fast intrinsic detector can still perform poorly if the false-alarm threshold is inflated by a huge unconstrained search window.

A slow detector may naturally reduce the number of temporal trials but can lose waveform distance and timing localization.

Therefore the temporal detector boundary is a trade space, not simply

```text
faster = always better.
```

---

## 13. Strongest current temporal statement

For known timing and equal-covariance Gaussian noise, event detectability is controlled by the matched-filter distance `d`.

For unknown timing, the relevant problem becomes

```text
matched-filter distance
+
number/correlation of candidate temporal modes
+
false-alarm and miss targets.
```

In the independent-bin benchmark,

```math
P_{\rm FA}=1-\Phi(\eta)^M,
```

```math
P_{\rm miss}=\Phi(\eta-d)\Phi(\eta)^{M-1}.
```

This makes temporal uncertainty an explicit resource coordinate.

---

## 14. Current frontier

The experiment now has enough structure to ask whether a **task-specific detectivity** can be defined without repeating the failure of scalar `D*`.

A candidate should:

```text
be defined only after specifying a class of optical waveforms/tasks;
reduce to the matched-filter distance for Gaussian readout;
include timing uncertainty when relevant;
allow non-Gaussian likelihoods rather than assuming one PSD;
remain explicit about area and observation time conventions.
```

The next step is to construct such a candidate and immediately try to break it with counterexamples.
