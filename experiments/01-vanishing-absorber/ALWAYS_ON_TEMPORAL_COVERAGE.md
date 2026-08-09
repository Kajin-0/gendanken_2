# Always-On Temporal Coverage — Accepted Modes, Thermal Background, and Dead-Time Blocking

**Date:** 2026-08-08  
**Status:** restricted mode-counting / renewal-model composition; no novelty claim  

## 1. Purpose

Dynamic impedance matching can capture one known temporal mode very efficiently.

`TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md` shows that unknown arrival time changes the problem: an always-on detector must accept many possible temporal modes rather than one scheduled waveform.

This note connects that temporal-mode coverage to

- real external thermal/background photon counts;
- detector dead time.

The result is intentionally simple and model-specific. It is not a universal dark-count theorem.

---

## 2. Accepted temporal modes and external background photons

Let

```math
|\psi_j\rangle,
\qquad j=1,\ldots,M,
```

be orthogonal accepted input spatiotemporal modes.

Let the detector click probability for one photon in mode `j` be

```math
\eta_j.
```

Assume the same input modes carry independent thermal/background occupation

```math
\bar n_j.
```

In the dilute mean-counting limit, the expected number of registered background photons from these modes is

```math
\boxed{
N_{\rm bg}
=\sum_{j=1}^{M}
\bar n_j\eta_j.
}
```

These are real external photons, not internal detector dark events.

---

## 3. Uniform acceptance requirement

If every possible signal mode must be accepted with

```math
\eta_j\ge\eta
```

and the background occupation is bounded below by

```math
\bar n_j\ge\bar n,
```

then

```math
\boxed{
N_{\rm bg}
\ge
\bar n M\eta.
}
```

Thus accepting more orthogonal possible arrival modes at fixed efficiency necessarily admits more background photon opportunities when the signal and background share those modes.

---

## 4. Continuous one-channel limit

For one spatial/polarization channel, an observation duration

```math
\mathcal T
```

and angular-frequency span

```math
W
```

contain an effective number of orthogonal time-frequency degrees of freedom of order

```math
M_{\rm eff}
\simeq
\frac{W\mathcal T}{2\pi}
```

for a long observation window.

This is the usual asymptotic time-bandwidth mode count and should not be interpreted as an exact finite-window identity.

For approximately flat thermal occupation and efficiency,

```math
\bar n_j\simeq\bar n,
\qquad
\eta_j\simeq\eta,
```

the mode-counting expression gives

```math
N_{\rm bg}
\simeq
\bar n\eta
\frac{W\mathcal T}{2\pi}.
```

Hence

```math
\boxed{
R_{\rm bg}
\equiv
\frac{N_{\rm bg}}{\mathcal T}
\simeq
\bar n\eta
\frac{W}{2\pi}.
}
```

This reproduces the continuum mean background-count relation already derived independently in `CAPTURE_TO_CLICK_COMPOSITION.md`.

The mode picture explains *why*: always-on temporal coverage over larger `W` means accepting proportionally more thermal input modes per unit time.

---

## 5. Scheduled versus unknown arrival

### Scheduled / heralded photon

If the photon is known to arrive inside one narrow temporal window, the detector can restrict its acceptance to that window.

The integrated admitted background can then be reduced because fewer temporal modes are opened.

### Unknown stationary arrival

If the photon arrival is uniformly distributed over a long observation time and every time bin must be accepted equally, closing most temporal windows lowers signal efficiency in the same proportion.

Thus gating is not a free background-rejection resource for a completely unknown stationary arrival process.

Arrival-time prior information or a herald is itself a resource.

This is consistent with the weighted-prior mode-capacity result in `TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md`.

---

## 6. Minimal nonparalyzable dead-time model

Now add a detector dead time

```math
\tau_d.
```

Assume

- when ready, an individual photon in the accepted channel produces a click with raw probability `eta_0`;
- thermal/background photons arrive with mean flux

```math
\Phi_{\rm bg}
=\bar n\frac{W}{2\pi};
```

- registered events make the detector completely unavailable for a fixed time `tau_d`;
- events arriving during dead time are ignored and do not extend it;
- background events are dilute enough that the nonparalyzable renewal model is valid;
- no internal dark events yet.

When ready, the attempted background-click rate is

```math
\lambda_{\rm bg}
=\eta_0\Phi_{\rm bg}.
```

A renewal cycle consists of mean ready waiting time

```math
1/\lambda_{\rm bg}
```

followed by dead time `tau_d`.

Therefore the steady ready fraction is

```math
\boxed{
p_{\rm ready}
=\frac{1}
{1+\eta_0\Phi_{\rm bg}\tau_d}.
}
```

---

## 7. External signal-efficiency ceiling from background blocking

An independently arriving weak signal photon sees the detector ready with probability `p_ready`.

Its observed efficiency is therefore

```math
\boxed{
\eta_{\rm ext}
=\eta_0p_{\rm ready}
=\frac{\eta_0}
{1+\eta_0\Phi_{\rm bg}\tau_d}.
}
```

For fixed background flux and dead time, this increases monotonically with `eta_0`.

Since

```math
\eta_0\le1,
```

the maximum possible external efficiency in this minimal model is

```math
\boxed{
\eta_{\rm ext}
\le
\frac{1}
{1+\Phi_{\rm bg}\tau_d}
=
\frac{1}
{1+\bar n W\tau_d/(2\pi)}.
}
```

This ceiling is caused entirely by real admitted thermal photons occupying the detector's dead time.

It survives even if the detector has zero internal dark-count hazard.

---

## 8. Required dead time for target efficiency

Demand

```math
\eta_{\rm ext}\ge\eta_*.
```

A necessary condition is

```math
\frac{1}
{1+\bar n W\tau_d/(2\pi)}
\ge\eta_*.
```

Therefore

```math
\boxed{
\tau_d
\le
\frac{2\pi}{\bar n W}
\left(
\frac{1}{\eta_*}-1
\right).
}
```

Equivalently,

```math
\boxed{
\bar n W\tau_d
\le
2\pi\frac{1-\eta_*}{\eta_*}.
}
```

This is a simple bandwidth x thermal-occupation x dead-time requirement for the stated single-channel renewal model.

---

## 9. Include an internal false-event hazard

Let

```math
D_{\rm int}
```

be an internal false-click hazard per unit **ready time**, independent of the external thermal photon flux.

Then the total false-event hazard while ready is

```math
\lambda_f
=D_{\rm int}
+\eta_0\Phi_{\rm bg}.
```

The ready fraction becomes

```math
p_{\rm ready}
=
\frac{1}
{1+\tau_d(D_{\rm int}+\eta_0\Phi_{\rm bg})}.
```

Thus

```math
\boxed{
\eta_{\rm ext}
=
\frac{\eta_0}
{1+\tau_d(D_{\rm int}+\eta_0\Phi_{\rm bg})}.
}
```

If `D_int` is independent of `eta_0`, the expression is again monotonic in `eta_0`, giving

```math
\boxed{
\eta_{\rm ext}
\le
\frac{1}
{1+\tau_d(D_{\rm int}+\Phi_{\rm bg})}.
}
```

This is not universal because real internal dark-count rates can depend strongly on the same bias/coupling parameters that determine `eta_0` and `tau_d`.

---

## 10. Relation to autonomous detector thermodynamics

Schwarzhans et al. already study internal dark-count rate and dead time in an autonomous nonequilibrium detector model and find model-specific tradeoffs between them.

The present calculation adds a separate effect:

```text
external thermal/background photons
-> real clicks
-> detector dead-time occupancy.
```

Therefore a complete optical detector should distinguish at least

```text
internal dark current / false events
+
external background photons admitted by optical bandwidth
+
dead-time blocking from both.
```

This is precisely the interface missing from a purely post-capture thermodynamic detector model.

---

## 11. Connection to dynamic known-time capture

The active time-modulation thought experiment now has a clear resolution.

### Known arrival mode

A dynamically matched single mode can be loaded with efficiency approaching one if coupling strength x loading time is sufficient.

### Unknown arrival over many modes

A finite coherent storage space has limited temporal-mode capacity.

### Always-on irreversible detector

The output continuum can cover many arrival modes, but accepting all of those modes also admits thermal photons and creates dead-time occupancy.

So the apparent active escape migrates from

```text
spectral matching
```

to

```text
temporal-mode coverage
+
external background mode count
+
reset/dead-time capacity.
```

---

## 12. Claim boundary

### Derived within the stated mode-count / renewal model

Mean external background count rate for flat one-channel occupation:

```math
\boxed{
R_{\rm bg}
\simeq
\bar n\eta\frac{W}{2\pi}.
}
```

Nonparalyzable dead-time external-efficiency ceiling:

```math
\boxed{
\eta_{\rm ext}
\le
\frac{1}
{1+\bar n W\tau_d/(2\pi)}.
}
```

### Not established

- novelty of these counting/dead-time compositions;
- a universal dead-time model;
- a universal time-bandwidth definition of accepted modes;
- effects of thermal bunching on dead-time statistics;
- afterpulsing / paralyzable behavior;
- a general adaptive time-modulated detector theorem;
- a complete active work-bandwidth-dark-count bound.

---

## 13. Next direction

The time-dependent escape has now been reduced to a physically sharper choice:

```text
scheduled detector
-> exploits arrival-time information

always-on detector
-> must accept many temporal modes
-> pays in storage/output capacity and admitted background / dead time.
```

The next research step should compare this **temporal-coverage resource** with the active pump singular-value resource derived in `ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md`.

The central question becomes:

> Can one formulate a common space-time mode-count resource law for an actively controlled detector, in which pump/control norm, number of accepted modes, irreversible output capacity, and background occupation all appear explicitly?