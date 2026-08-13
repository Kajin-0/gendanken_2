# Task-Specific Detectivity and the Failure of Universal Scalar Ranking — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional derivation  
**Priority:** unassessed; no novelty claim

The experiment has repeatedly found that a scalar detector threshold fails when a hidden task/resource coordinate is restored.

This file asks whether the full Gaussian decision functional can be compressed into a task-specific scalar without repeating the same mistake.

---

## 1. Normalize the optical task by event energy

Let a known-time incident optical waveform be

```math
p(t)=E q(t),
```

where

```math
\int q(t)dt=1.
```

Thus `E` is total incident optical energy and `q(t)` specifies the normalized temporal shape.

For a linear detector with frequency-dependent input-referred two-sided noise `NEP_2(f)`, the Gaussian decision distance is

```math
\boxed{
d^2
=E^2\mathcal K[q],
}
```

where

```math
\boxed{
\mathcal K[q]
=\int_{-\infty}^{\infty}
\frac{|\tilde q(f)|^2}
{\mathrm{NEP}_2^2(f)}df.
}
```

`mathcal K[q]` is a task-specific detector sensitivity functional.

It has units of inverse energy squared under the stated Fourier/NEP convention.

---

## 2. Decision-equivalent minimum event energy

For known timing and equal priors,

```math
P_e=Q(d/2).
```

Target

```math
P_e\le\epsilon
```

therefore requires

```math
\boxed{
E
\ge
E_{\min}(q,\epsilon)
=
\frac{2Q^{-1}(\epsilon)}
{\sqrt{\mathcal K[q]}}.
}
```

This is a physically direct scalar for a **specified task**:

```text
minimum event energy needed to achieve the chosen decision error.
```

Unlike a universal detector-quality number, it explicitly carries

```text
waveform shape q
decision target epsilon
noise spectrum
temporal response.
```

---

## 3. One-pole white-noise benchmark

For the one-pole impulse detector already analyzed,

```math
\mathcal K
=\frac{1}{\tau\,\mathrm{NEP}^2}.
```

Hence

```math
\boxed{
E_{\min}
=2Q^{-1}(\epsilon)
\,\mathrm{NEP}\sqrt\tau.
}
```

Using

```math
\mathrm{NEP}=\sqrt A/D^*,
```

```math
\boxed{
E_{\min}
=2Q^{-1}(\epsilon)
\frac{\sqrt{A\tau}}{D^*}.
}
```

This makes the temporal resource missing from scalar `D*` explicit.

For a short-energy event, the combination

```math
\mathrm{NEP}\sqrt\tau
```

rather than NEP alone controls this conditional energy threshold.

---

## 4. Unknown arrival time changes the scalar again

If the event can occur in one of `M` independent candidate temporal cells, the required normalized distance is no longer simply `2Q^-1(epsilon)`.

For max-threshold false-alarm target `alpha` and miss target `beta`, define

```math
\eta_\alpha
=\Phi^{-1}[(1-\alpha)^{1/M}].
```

The benchmark requirement from `UNKNOWN_ARRIVAL_TIME.md` is

```math
\boxed{
d_{\rm req}
=
\eta_\alpha
-
\Phi^{-1}\left[
\frac{\beta}{\Phi(\eta_\alpha)^{M-1}}
\right].
}
```

Therefore

```math
\boxed{
E_{\min}
=\frac{d_{\rm req}}
{\sqrt{\mathcal K[q]}}.
}
```

The same physical detector and waveform acquire a different task-specific threshold once arrival-time uncertainty and false-alarm accounting are changed.

Thus even the useful scalar `E_min` is not detector-only.

It is a **detector + task + decision-rule** quantity.

---

## 5. Detector-specific spectral decision kernel

For known-time equal-covariance Gaussian tasks, define

```math
\boxed{
W_D(f)
=\frac{1}{\mathrm{NEP}_{2,D}^2(f)}
=\frac{|\mathcal R_D(f)|^2}
{S_{n,D}^{(2)}(f)}.
}
```

Then

```math
\boxed{
\mathcal K_D[q]
=\int |\tilde q(f)|^2W_D(f)df.
}
```

All task dependence enters through the nonnegative spectral weight

```math
|\tilde q(f)|^2.
```

This makes detector comparison a functional-ordering problem.

---

## 6. Pointwise dominance gives universal ordering inside this task class

Consider detectors `A` and `B`.

If

```math
\boxed{
W_A(f)\ge W_B(f)
\quad\text{for every allowed }f,
}
```

then for every allowed waveform `q`,

```math
\boxed{
\mathcal K_A[q]\ge\mathcal K_B[q].
}
```

Therefore

```math
E_{\min,A}(q,\epsilon)
\le
E_{\min,B}(q,\epsilon)
```

for all known-time Gaussian tasks in the class.

This is a genuine task-independent dominance relation **within the stated model class**.

A scalar ranking is safe only when it respects this stronger spectral dominance.

---

## 7. Crossing spectral kernels destroy universal scalar ranking

Suppose instead there are frequency regions where

```math
W_A(f)>W_B(f)
```

and other regions where

```math
W_B(f)>W_A(f).
```

Then choose a normalized optical task whose spectrum is concentrated in a region where `A` is better. This gives

```math
\mathcal K_A[q_A]>\mathcal K_B[q_A].
```

Choose another task concentrated where `B` is better. Then

```math
\mathcal K_B[q_B]>\mathcal K_A[q_B].
```

Therefore the detector ranking reverses with task.

So:

```math
\boxed{
W_A-W_B\text{ changes sign}
\Rightarrow
\text{no universal scalar ranking can represent all waveform tasks.}
}
```

This is one of the strongest structural results of the experiment so far.

It is elementary as a functional-analysis consequence, not claimed as a new theorem.

---

## 8. Equal scalar D* is only one special case of crossing/incomplete kernels

Two detectors can share the same quoted `D*` at one reference frequency while their spectral kernels differ elsewhere.

Then the scalar equality says only

```text
one point or one conventionally weighted measurement agrees.
```

It does not imply

```math
W_A(f)=W_B(f)
```

over the frequencies used by a particular event waveform.

Thus equal scalar `D*` naturally permits task-dependent ranking reversal.

The earlier one-pole equal-`D*` fast/slow example is a special case: the temporal transfer functions differ, so the full kernels differ even though the quoted low-frequency value is equal.

---

## 9. No detector-only scalar can preserve all tasks unless the task family is restricted

Suppose one wants a scalar

```math
F(D)
```

that ranks detectors correctly for every waveform in an unrestricted task family.

If the kernels cross, no total scalar ordering can reproduce both task rankings.

Therefore one must do at least one of the following:

```text
restrict the optical task family;
retain the full frequency-dependent detector kernel;
accept only a partial dominance ordering;
or report multiple task-specific scalars.
```

This is the same conceptual pattern seen earlier:

```text
universal N failed -> missing interaction architecture;
universal efficiency failed -> missing bandwidth;
universal D* ranking fails -> missing task spectrum.
```

---

## 10. A partial order is more natural than one universal score

Within the Gaussian linear class, define

```text
A dominates B
```

if

```math
W_A(f)\ge W_B(f)
```

throughout the allowed frequency domain.

Some detector pairs will be comparable under this relation.

Many will not.

For incomparable pairs, the physically correct answer is not

```text
A is better
```

or

```text
B is better,
```

but

```text
which detector is better depends on the optical task and decision constraints.
```

This suggests detector comparison may be intrinsically a **partial-order problem**, not a one-dimensional ranking problem.

---

## 11. Task-specific scalar candidate that does survive

For a *fixed* task `q`, fixed timing model, and fixed decision target, the minimum event energy

```math
\boxed{
E_{\min}
=\frac{d_{\rm req}}{\sqrt{\mathcal K_D[q]}}
}
```

is well defined in the Gaussian model.

It is operationally meaningful and directly answers

> how much optical event energy is required for the specified decision performance?

This may be a better endpoint than trying to invent another detector-only universal scalar.

---

## 12. Why forcing D*-like units is not unique

`D*` contains area and bandwidth normalization by convention.

The task functional `sqrt(K)` has units of inverse energy.

To manufacture `D*`-like units one could multiply by a square root of area and a chosen task time scale, but the choice of time-scale definition is not unique for arbitrary waveforms:

```text
RMS duration
equivalent-noise duration
FWHM
integration window
inverse effective bandwidth
etc.
```

Therefore a generalized `D*_task` with the same units as conventional `D*` requires an additional convention.

The operational energy threshold `E_min` avoids that ambiguity.

---

## 13. Extension beyond Gaussian noise

The kernel `W_D(f)` exists because equal-covariance Gaussian likelihoods reduce to a quadratic norm.

For signal-dependent Gaussian noise or Poisson/counting statistics, the correct task score is instead derived from the full likelihood overlap.

Therefore even `mathcal K[q]` is not universal across noise classes.

The truly general object remains

```text
statistical distinguishability of the complete conditional output processes.
```

Task-specific energy threshold can still be defined operationally by solving

```math
P_e(E)=\epsilon,
```

but the functional form of `P_e(E)` is architecture/noise dependent.

---

## 14. Strongest current conclusion

The experiment began by asking for a boundary in **matter**.

It has arrived at a boundary in **measurement performance**.

Even after restricting to linear Gaussian readout, there is generally no one-dimensional task-independent detector ranking unless one detector's full inverse-noise spectral kernel dominates the other's pointwise over the allowed task band.

Thus:

> **“Which detector is better?” is not a complete physical question until the optical task and decision constraints are specified.**

And:

> **“When does matter become a detector?” has no universal scalar boundary because detection is a relation among matter, optical mode, temporal task, noise process, observer access, and decision criterion.**

---

## 15. Current next attack

The strongest remaining conceptual question is whether any **architecture-independent lower bound** survives this increasingly complete resource ledger.

Candidate possibilities to attack next:

```text
finite information acquisition rate per interaction action;
energy-time / bandwidth-resource bounds after task specification;
minimum entropy export for reusable cyclic detection;
minimum reset cost at fixed error and cycle time;
fundamental trade between persistent record stability and reset speed.
```

The project should return to counterexample-first lower-bound testing rather than adding more conventional detector metrics indefinitely.

A focused prior-art audit should precede any novelty claim.
