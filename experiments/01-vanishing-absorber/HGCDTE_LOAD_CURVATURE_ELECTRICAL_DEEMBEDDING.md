# Optical-Load Curvature — Electrical De-Embedding Requirement

**Date:** 2026-08-09  
**Status:** derived first-order electrical-pole error budget; conditional one-pole diagnostic; no calibrated readout model; no novelty claim

## 1. Why this systematic is now first-order

The short-wave optical-load curvature observable was introduced to avoid the nearly singular **static** sample-A baseline inversion.

However, strong illumination does not only alter carrier transport.

Published room-temperature MWIR HgCdTe saturation modeling reports that increasing irradiation lowers the detector's zero-bias impedance and that heating materially affects saturation behavior.

Therefore the measured RF phase can change because the **electrical detector/readout transfer function** changes with optical load even if carrier transit timing were unchanged.

This must be de-embedded before assigning load-dependent phase curvature to internal transport.

---

## 2. Minimal first-order electrical model

Use an effective first-order electrical pole

```math
\boxed{
H_e(\Omega)
=\frac{1}{1+i\Omega\tau_e},
}
```

with

```math
\tau_e=RC
```

representing the relevant load-dependent detector/readout time constant.

Its phase is

```math
\boxed{
\phi_e
=-\tan^{-1}(\Omega\tau_e).
}
```

Define

```math
x=\Omega\tau_e
=\frac{f}{f_{\rm pole}}.
```

For a small residual fractional de-embedding error

```math
\eta
=\frac{\delta\tau_e}{\tau_e},
```

```math
\boxed{
\delta\phi_e
\simeq
-\frac{x}{1+x^2}\eta.
}
```

The sensitivity

```math
\left|
\frac{\partial\phi_e}{\partial\ln\tau_e}
\right|
=
\frac{x}{1+x^2}
```

is largest at the electrical pole `x=1`.

The requirement should therefore be stated in terms of the **effective RF time constant or full complex transfer**, not resistance alone. Capacitance, package parasitics, detector impedance, cables, and frontend loading can all contribute.

---

## 3. Apply the result to the six-state curvature observable

The proposed causal observable uses

```text
three optical-load states at lambda_1
three optical-load states at lambda_2
```

with coefficients

```text
+1, -2, +1,
-1, +2, -1.
```

Hence

```math
\sum_i a_i^2=12.
```

If the residual fractional time-constant errors at the six states are independent, have equal RMS `sigma_tau/tau`, and operate at approximately the same normalized electrical frequency `x`, then

```math
\boxed{
\sigma_{\mathcal C,e}
\simeq
\sqrt{12}
\frac{x}{1+x^2}
\frac{\sigma_{\tau_e}}{\tau_e}
}
```

in radians.

Therefore the per-state fractional de-embedding requirement for an electrical-curvature phase budget `sigma_C,e` is

```math
\boxed{
\frac{\sigma_{\tau_e}}{\tau_e}
\lesssim
\frac{\sigma_{\mathcal C,e}}
{\sqrt{12}}
\frac{1+x^2}{x}.
}
```

This is a conservative independent-error budget. Common calibration errors can cancel strongly in the second difference, while correlated load-dependent errors require the full covariance rather than the `sqrt(12)` rule.

---

## 4. Representative requirements

### Allocate `0.04 degree RMS` to electrical curvature

For

```math
\sigma_{\mathcal C,e}=0.04^\circ,
```

the equal independent per-state effective time-constant requirement is approximately:

| `x = Omega tau_e` | `f_pole/f` | required `sigma_tau/tau` |
|---:|---:|---:|
| 0.01 | 100 | 2.02% |
| 0.03 | 33.3 | 0.672% |
| 0.10 | 10 | 0.204% |
| 0.30 | 3.33 | 0.0732% |
| 1.00 | 1 | **0.0403%** |
| 3.00 | 0.333 | 0.0672% |
| 10.0 | 0.10 | 0.204% |

The high-`x` branch also reduces phase sensitivity mathematically, but operating well above a dominant electrical pole is generally unattractive for a precision detector-timing measurement because the signal transfer is already strongly attenuated. The useful practical route is normally `x << 1` or explicit de-embedding.

### Tighter `0.01 degree RMS` electrical budget

```text
x=0.10 -> sigma_tau/tau <= ~0.0509%
x=0.30 -> <= ~0.0183%
x=1.00 -> <= ~0.0101%.
```

Thus sub-`0.01 degree` electrical systematics near the RF pole require extremely accurate state-by-state knowledge of the complex detector/readout transfer.

---

## 5. A 1% uncorrected time-constant change is already large on the target phase scale

For one load state, a small `1%` change in `tau_e` produces approximately

```text
x=0.03 -> 0.017 degree phase
x=0.10 -> 0.057 degree
x=0.30 -> 0.158 degree
x=1.00 -> 0.286 degree.
```

These are **single-state** phase changes, not curvature values.

A perfectly linear change with load would cancel in the second finite difference. But any nonlinear illumination dependence of detector impedance or parasitic transfer can leave curvature on exactly the `0.01-0.1 degree` scale being sought for transport.

This is why electrical de-embedding is not a secondary correction.

---

## 6. Measurement-frequency interpretation

For a first-order pole,

```math
x=f/f_{\rm pole}.
```

At a `1 GHz` timing measurement:

```text
x=0.10 -> f_pole = 10 GHz
x=0.03 -> f_pole ~33 GHz
x=0.01 -> f_pole = 100 GHz.
```

So simply demanding `x << 1` can imply a very high electrical bandwidth.

The realistic design choice is therefore a trade:

```text
lower RF frequency
-> smaller electrical phase sensitivity
-> smaller transport phase leverage

higher RF frequency
-> larger transport phase leverage
-> larger electrical de-embedding burden as the pole is approached.
```

This reinforces the repository's existing conclusion that RF frequency should be **adaptive**, not fixed at `1 GHz` by assumption.

---

## 7. What should actually be measured

A real calibration should not infer `tau_e` from resistance alone.

At every wavelength and optical-load state, measure or otherwise constrain the detector/readout complex electrical transfer sufficiently to remove its contribution to phase.

The minimal useful objects are

```text
complex detector impedance or small-signal electrical transfer vs load
frontend / cable transfer vs load and frequency
load-dependent amplitude-to-phase conversion
state-to-state covariance of the de-embedded phase
repeatability of the load cycle.
```

If a one-pole model is empirically adequate, report the inferred `tau_e(P,lambda)` and its covariance.

If it is not, directly de-embed the measured complex transfer rather than forcing an RC interpretation.

---

## 8. Relation to known HgCdTe behavior

The need for this correction is independently motivated by published HgCdTe work:

- room-temperature MWIR saturation simulations report that zero-bias impedance decreases as irradiation is increased and that heating affects saturation;
- HgCdTe timing literature shows that series resistance / RC effects can become an important or dominant contribution to measured response time in relevant detector structures.

These are known device effects, not candidate novelty.

The inverse-metrology question is whether, **after** those electrical effects are measured and removed, a wavelength-dependent nonlinear transport curvature remains that is spatially consistent with sample A's retained graded region.

---

## 9. Current go/no-go interpretation

For the load-curvature route to be credible, at least one of the following must hold:

```text
1. the measurement operates sufficiently below the relevant electrical pole;
2. the load-dependent complex electrical transfer is de-embedded to the required phase accuracy;
3. the electrical curvature is independently shown to be much smaller than the transport-curvature target.
```

For example, if a `0.04 degree RMS` electrical-curvature budget is used, the conservative independent-state requirement is about

```text
0.20% RMS effective-time-constant knowledge at x=0.1
0.040% RMS near x=1.
```

Failure to meet or validate this requirement would make an observed load-phase curvature ambiguous.

---

## 10. Next decisive step

Do not yet build a detailed nonlinear HgCdTe transport model around an unverified phase observable.

The next useful step is to audit **prior timing/frequency-response measurements versus optical intensity/load** in HgCdTe and closely related graded detectors.

Two questions matter:

1. has optical-load-dependent RF phase / impulse timing already been measured in HgCdTe, especially under saturation or space-charge conditions?
2. if so, did those studies separate electrical impedance/RC effects from carrier transit dynamics?

That literature boundary determines whether the load-curvature direction is genuinely underexplored or simply a reformulation of established transient saturation measurements.

Numerical implementation:

`numerics/hgcdte_load_curvature_electrical_deembedding.py`
