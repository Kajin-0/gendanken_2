# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-08  
**Status:** exploratory; no novelty claim  

## 1. Question

Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The point of the experiment is not to prove that the answer is no. The point is to identify which physical assumptions determine the answer.

---

## 2. Minimal starting model

Consider an active semiconductor region of volume `V` with a dark carrier-generation event-rate density `g_d`.

At the simplest counting level,

```math
\Gamma_d = g_d V.
```

If the relevant events are independent and each produces one collected elementary charge, the one-sided shot-noise-like current spectral density would scale as

```math
S_I \propto q^2 g_d V,
```

with the exact factor depending on the event and spectral-density convention.

The only robust point currently needed is the volume scaling:

```math
\Gamma_d \propto V.
```

Therefore shrinking the active volume appears favorable for intrinsic generation noise.

This is a deliberately idealized starting point. Surface generation, contacts, tunneling, background photons, gain, recombination correlations, and readout noise are not yet included.

---

## 3. The optical obstruction

For an ordinary weakly absorbing slab, reducing active thickness also reduces absorption.

So the thought experiment grants the detector ideal passive optical structures capable of increasing optical dwell time or field concentration: a cavity, antenna, photon-trapping structure, slow-light region, or another passive coupler.

The question then becomes:

> If the absorbing volume tends toward zero while the desired absorption remains near unity, where does the physical cost reappear?

A plausible place is optical temporal response.

---

## 4. First concrete subproblem

Analyze a single passive one-port resonance with external coupling rate `gamma_e` and absorber loss rate `gamma_a`.

The standard coupled-mode model suggests a resonant absorptance of the form

```math
A(\omega)
=
\frac{4\gamma_e\gamma_a}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_a)^2},
```

subject to normalization conventions that must be checked explicitly before this expression is treated as canonical.

At resonance this model gives unity absorption when

```math
\gamma_e = \gamma_a.
```

If shrinking the absorber forces `gamma_a -> 0`, maintaining critical coupling would also require `gamma_e -> 0`, suggesting a longer optical dwell time and narrower optical response.

This is the first mechanism to test, not yet a general theorem.

---

## 5. What has actually been established

At this stage only the following are treated as secure qualitative statements:

1. For a fixed volumetric dark-event rate density, total bulk dark-event rate scales with active volume.
2. Weak bare absorption generally decreases when absorbing material is removed.
3. Passive resonant confinement can trade spectral/temporal extent for stronger interaction with a weak absorber.

No general detector sensitivity-bandwidth limit has been derived.

---

## 6. Active conjectures

### C1 — Resonant shrinking penalty

Within a one-port passive resonant model, maintaining near-unity absorptance while absorber loss tends to zero forces the resonance lifetime to increase.

This should be derivable exactly within temporal coupled-mode theory.

### C2 — More general passive bound

There may exist a geometry-independent relation connecting integrated absorption or absorption-weighted bandwidth to active material volume and susceptibility.

No specific formula is currently claimed.

### C3 — Detector-level consequence

Combining an electromagnetic absorption-bandwidth bound with intrinsic carrier-generation statistics may yield a volume-independent upper bound on a properly defined sensitivity-speed metric.

This is currently speculative.

---

## 7. Important non-claims

We have **not** established that:

- `NEP -> 0` as `V -> 0` in a complete detector;
- all passive optical architectures obey a simple `eta^2 B <= C V` law;
- cavity photon lifetime is always the dominant detector response time;
- active, nonreciprocal, time-varying, or gain-assisted systems obey the same restriction;
- any current conjecture is novel.

---

## 8. Next decisive calculation

Do the one-port resonator cleanly from the dynamical amplitude equation rather than importing the absorptance formula.

Derive, with one normalization convention throughout:

1. steady-state absorptance `A(omega)`;
2. the critical-coupling condition;
3. stored optical energy and energy-decay time;
4. the response to a small modulation of incident optical power;
5. the exact `-3 dB` detection-response bandwidth;
6. the relationship, if any, between this modulation bandwidth and the spectral absorption linewidth;
7. how `gamma_a` scales with active material participation in the weak-loss limit.

The key question after that derivation is whether the intuitive statement

```text
less absorbing material -> longer dwell time -> lower usable bandwidth
```

is actually correct under the stated model, including all factors of two.
