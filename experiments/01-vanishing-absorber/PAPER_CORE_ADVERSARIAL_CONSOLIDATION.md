# Adversarial Paper-Core Consolidation — What Survives a Hostile Review

**Date:** 2026-08-10  
**Status:** active manuscript-planning boundary after explicit counterexample attacks; theory-first; no novelty or priority claim

## 1. Purpose

The project accumulated many exact identities.  A paper should not contain all of them merely because they are correct.

This document asks the narrower hostile-review question:

> **After correcting the observable, boundaries, ordinary electron-hole signal formation, optical-source width, and prior-art collisions, what is the smallest coherent set of predictions that still looks scientifically strong?**

The answer is substantially narrower than the full `THEORY_FALSIFICATION_LADDER.md`.

The strongest surviving paper is about **spectrally sampling a spatial propagation law and falsifying increasingly specific transport models**, with the measured terminal-current observable treated correctly through Shockley-Ramo signal formation.

---

# 2. Major adversarial correction — terminal current is not arrival flux

The earlier theory repeatedly used

```math
U(d,\omega)=E[e^{-i\omega T_d}]
```

as a timing response.

That is an exact **arrival/collection-flux** observable.

It is not the generic terminal photocurrent of a semiconductor detector.

Shockley-Ramo signal formation makes moving charge induce current continuously along its trajectory.

Even perfect deterministic uniform transit gives

```math
U(d,i\omega)=e^{-i\omega d/w}
```

but planar terminal current

```math
J(d,i\omega)
\propto
1-e^{-i\omega d/w}.
```

Therefore the old three-color law applied directly to measured current is false in the simplest conventional counterexample.

**Disposition:**

```text
arrival-flux three-color theorem -> retain as ideal first-passage theorem

generic measured-current three-color theorem -> reject

planar terminal-current four-color first-difference theorem -> active replacement
```

Canonical correction:

`SHOCKLEY_RAMO_OBSERVABLE_CORRECTION.md`

---

# 3. Headline Gedanken experiment I — four colors isolate one spatial propagator

Consider the deliberately simple detector:

```text
one dominant carrier species
planar geometry
uniform weighting field
homogeneous drift and diffusion over the sampled segment
negligible carrier-loss complications in the minimal theorem
one calibrated generated-carrier amplitude per optical channel
wavelength translates one fixed generation kernel shape.
```

For a point source a distance `d` from the collector, homogeneous drift-diffusion gives

```math
D\gamma^2+w\gamma=i\omega.
```

The raw de-embedded Shockley-Ramo current is

```math
\boxed{
J(d,\omega)
=C(\omega)
\left[1-e^{-\gamma(\omega)d}\right].
}
```

For four equally spaced internal source coordinates

```math
d_m=d_0+m\Delta d,
\qquad m=0,1,2,3,
```

first differences satisfy

```math
\Delta J_m
=J_{m+1}-J_m
=Bq^m,
\qquad
q=e^{-\gamma\Delta d}.
```

Therefore

```math
\boxed{
(J_2-J_1)^2
=(J_1-J_0)(J_3-J_2).
}
\tag{P1}
```

This is the simplest terminal-current spatial closure that survives the Ramo correction.

Three positions estimate

```math
q
=\frac{J_2-J_1}{J_1-J_0},
```

while the fourth is a parameter-free falsification point.

Then

```math
\boxed{
\gamma
=-\frac{1}{\Delta d}\log q.
}
\tag{P2}
```

The branch must be spatially unwrapped; a sufficient single-frequency no-alias condition is approximately

```math
|\operatorname{Im}\gamma|\Delta d<\pi.
```

In practice continuity across RF provides additional branch information.

---

# 4. Why P1 is experimentally attractive as a gedanken null

At fixed RF, let the entire external chain multiply every optical channel by an arbitrary common complex factor `G(omega)` and add a common complex offset `C0`:

```math
J_m^{meas}=GJ_m+C_0.
```

First differences remove `C0` and carry the same `G`.

Equation (P1) is unchanged.

Thus the ideal closure is insensitive to

```text
common RF gain,
common RF phase,
and wavelength-independent additive offset.
```

What still matters is

```text
relative spectral generation coordinate,
relative generated-carrier amplitude,
wavelength-dependent optics,
and wavelength-dependent external transfer.
```

This is a favorable asymmetry for a null experiment.

---

# 5. Broad optical generation is not automatically fatal

If each wavelength translates the same finite source shape `g`, then averaging the affine exponential over that source changes only the coefficient of the exponential:

```math
J_m=A+\tilde Bq^m.
```

Therefore P1 remains exact for arbitrary source width, asymmetry, or multimodality if the shape is translated rigidly and remains within the homogeneous region.

The dangerous optical correction is **shape evolution with wavelength**, not width by itself.

This is the same structural lesson found earlier for the ideal arrival-flux theorem.

A real material example must therefore calculate the wavelength-dependent generation kernels rather than assume rigid translation.

---

# 6. Headline Gedanken experiment II — one RF identifies, the second RF falsifies

Once `gamma=a+ib` is isolated from the four-color current data, uniform real drift-diffusion predicts

```math
D\gamma^2+w\gamma=i\omega.
```

At one RF frequency,

```math
\boxed{
D
=\frac{\omega a}
{b(a^2+b^2)},
}
\tag{P3}
```

and

```math
\boxed{
w
=\frac{\omega(b^2-a^2)}
{b(a^2+b^2)}.
}
\tag{P4}
```

For positive downstream transport,

```math
\boxed{0<a<b.}
\tag{P5}
```

A second RF frequency introduces **no new `D,w` parameter**.

Therefore ordinary local homogeneous drift-diffusion predicts

```math
\boxed{
D(\omega_2)=D(\omega_1),
\qquad
w(\omega_2)=w(\omega_1).
}
\tag{P6}
```

This is the cleanest transport falsification statement in the paper.

The paper should emphasize the logic:

```text
first RF -> identify
second RF -> try to kill the model.
```

Not

```text
many RF points -> fit a flexible transport curve.
```

---

# 7. Ordinary counterexample — electron and hole both contribute

A real photodiode can have two conventional Ramo contributions.

For deterministic planar electron-hole motion,

```math
J(z,\omega)
=C_0
+C_e e^{+i\omega z/v_e}
+C_h e^{-i\omega z/v_h}.
```

This **generically fails** the one-carrier four-color closure P1.

That failure is not anomalous transport.

However first differences contain only two exponentials, so six colors provide five differences and obey the exact rank-two Hankel closure

```math
\boxed{
\det
\begin{pmatrix}
\Delta J_0&\Delta J_1&\Delta J_2\\
\Delta J_1&\Delta J_2&\Delta J_3\\
\Delta J_2&\Delta J_3&\Delta J_4
\end{pmatrix}=0.
}
\tag{P7}
```

Thus a failed four-color test should be followed by **mode counting**, not immediate exotic-physics interpretation.

Numerical counterexample:

`numerics/ramo_two_carrier_rank_counterexample.py`

---

# 8. A finite boundary produces the same rank but a different RF root geometry

Uniform scalar second-order transport near a finite boundary also produces two homogeneous spatial roots.

After removal of the constant Ramo particular solution, first differences again have rank at most two.

So electron-hole transport and a finite boundary can both pass P7.

Their recovered spatial exponents are nevertheless strongly constrained in different ways.

For one scalar finite-boundary drift-diffusion equation,

```math
D r^2+w r-i\omega=0.
```

The two roots obey

```math
\boxed{
r_++r_-=-w/D
\quad\text{real and RF-independent},
}
\tag{P8}
```

```math
\boxed{
r_+r_-=-i\omega/D
\quad\text{purely imaginary and linear in RF}.
}
\tag{P9}
```

For a conventional deterministic electron-hole pair instead,

```math
\boxed{
r_e+r_h
=i\omega(1/v_e-1/v_h),
}
\tag{P10}
```

```math
\boxed{
r_er_h
=\omega^2/(v_ev_h).
}
\tag{P11}
```

So the same spatial rank has qualitatively different RF geometry:

```text
simple boundary:
root sum real constant
root product imaginary ~ omega

electron-hole pair:
root sum imaginary ~ omega
root product real ~ omega^2.
```

This is a strong example of the paper's central philosophy:

> **count modes first; then use their RF algebra to falsify mechanisms.**

Canonical boundary file:

`FIVE_COLOR_BOUNDARY_ROOT_PAIR_CLOSURE.md`

Terminal-current counterexample/regression:

`numerics/ramo_two_carrier_root_signature.py`

---

# 9. Boundary depth law remains an independent cross-check

The earlier HgCdTe worked-example error produced a useful exact theorem.

For homogeneous drift-diffusion with a reflecting upstream boundary, the mean first-passage curvature for a symmetric three-depth triplet obeys

```math
\boxed{
C_1^{boundary}
=\frac{2D}{w^2}
 e^{-z_0w/D}
\left[
\cosh(hw/D)-1
\right].
}
```

Hence translating the same triplet deeper gives

```math
\boxed{
\frac{C_1(z_0+\Delta z)}{C_1(z_0)}
=e^{-\Delta z/\ell_D},
\qquad
\ell_D=D/w.
}
\tag{P12}
```

A finite-boundary explanation is therefore overdetermined:

```text
rank-two spatial response
+ root-pair Vieta closure
+ exponential depth decay with the same D/w scale.
```

This is far stronger than fitting an arbitrary boundary correction.

---

# 10. What happens to the timing-distribution / inverse-Gaussian results?

They remain mathematically correct for the **arrival first-passage process**.

They must not be applied blindly to normalized terminal-current waveforms.

For example, deterministic uniform transit has

```text
arrival time -> delta distribution
planar Ramo current -> rectangular pulse
```

so the corresponding normalized signal-time statistics are completely different.

The useful way to retain the first-passage results is through the recovered spatial propagation exponent `gamma(s)`.

For a homogeneous regenerative first-passage process,

```math
U(d,s)=e^{-d\Phi(s)}.
```

Thus the propagation exponent itself is the Laplace exponent

```math
\gamma(s)=\Phi(s)
```

(up to the coordinate sign convention).

Ordinary uniform drift-diffusion gives one special form

```math
\Phi(s)
=\frac{\sqrt{w^2+4Ds}-w}{2D}.
```

The inverse-Gaussian cumulant ratios and regenerative Lévy/Hankel inequalities should therefore be interpreted as **constraints on the recovered propagation law**, not generic raw-current waveform identities.

This is a cleaner and more defensible use of that mathematics.

---

# 11. What is demoted from the headline paper

The following results may remain appendices, follow-up work, or repository provenance, but they should not compete with the central argument.

### Arbitrary-profile local derivative inversion

Exact but requires first and second spatial derivatives of noisy response fields.  Statistically expensive and obscures the simple gedanken logic.

### Occupation-time / local-clock spectroscopy

Mathematically strong, but the ideal clock perturbation is not a direct physical composition/electric-field perturbation.  Better as a future extension.

### Full Lévy-spectrum reconstruction

Interesting but broadens the paper from a sharp falsification argument into general stochastic-process spectroscopy.

### Purpose-built translated-gradient fabrication optimization

Useful evidence that a future validation structure is not absurd, but not part of the theory contribution.

### Published sample-A/B rescue calculations

Important provenance showing why uncontrolled near-contact comparisons are inadequate, not active paper claims.

---

# 12. What is invalidated or superseded

## Generic terminal current equals first-passage characteristic function

**INVALIDATED as a general photodiode statement.**

Shockley-Ramo current is induced continuously along the path.

## Generic terminal-current three-color geometric-mean law

**INVALIDATED.**

A deterministic rectangular Ramo pulse is already a counterexample.

## Direct inverse-Gaussian skewness/kurtosis test on arbitrary measured photocurrent impulse

**INVALIDATED as a generic observable statement.**

It applies to the first-passage distribution, not automatically the induced-current timing distribution.

## Earlier large HgCdTe three-color phase attributed mainly to the bulk drift gradient

**INVALIDATED / SUPERSEDED.**

A matched finite-boundary control showed that most of the original `~0.1-1 deg` phase curvature came from the reflecting boundary.

The gradient-only excess in that explicit model was much smaller.

---

# 13. The minimal manuscript spine

A coherent paper can now be told with only three gedanken experiments.

## Gedanken A — four colors at one RF

```text
four equally spaced internal generation coordinates
-> first-difference geometric closure
-> recover one spatial propagation exponent
```

Question:

> **Is one homogeneous single-carrier propagation mode sufficient?**

## Gedanken B — repeat at a second RF

```text
same four colors
second RF frequency
-> infer D,w again
```

Question:

> **Does one real frequency-independent drift-diffusion generator survive?**

## Gedanken C — if A fails, use six colors

```text
six internal coordinates
-> first-difference Hankel rank
-> recover two spatial roots
-> examine RF root sum/product
```

Question:

> **Is the extra mode a conventional second carrier, a finite boundary, or something requiring a richer model?**

This is simple enough to explain without a device schematic full of fitted parameters.

---

# 14. Candidate contribution after hostile reduction

The candidate is no longer

```text
wavelength-dependent timing,
spectral tomography,
Ramo signal theory,
Prony/Hankel rank,
or convection-diffusion inversion
```

individually.

All of those have substantial established context.

The surviving candidate is the integrated detector protocol:

```text
wavelength -> calibrated internal source coordinate

Shockley-Ramo-aware spatial differencing
-> isolate propagation modes

minimal color-count closure
-> falsify spatial model order

RF root algebra
-> falsify physical transport law

only then
-> introduce a richer mechanism.
```

**Status:** CANDIDATE DISTINCT APPLICATION / PRIORITY UNPROVEN.

A focused primary-source search must still determine whether this exact spectral-depth closure protocol has already appeared in photodiode transport characterization, optical receiver calibration, time-of-flight spectroscopy, or semiconductor system-identification literature.

---

# 15. Remaining decisive work before manuscript drafting

1. derive and numerically check the four-color theorem directly from the Shockley-Ramo / backward-resolvent formulation, including a transparent statement of stochastic assumptions;
2. quantify source-shape-evolution error for the four-color current closure using a mean-depth spectral coordinate;
3. work one HgCdTe example using **raw per-generated-carrier RF current**, not the previously conflated DC-normalized first-passage observable;
4. derive measurement-noise propagation for the difference ratio `q` and the four-color closure residual;
5. complete a focused literature audit for the exact 4-color / 6-color spectral-depth closure construction;
6. only then outline a manuscript.

The project should resist adding another general theorem until these six points are closed.
