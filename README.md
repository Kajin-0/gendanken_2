# Gedanken 2

First-principles thought experiments in photodetector physics.

This repository follows the physics rather than a predetermined theorem. Failed conjectures, counterexamples, and prior-art collisions are retained because they define the real result.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

The answer has not been assumed.

The path has evolved:

```text
weak resonant absorber
-> high peak absorption can cost temporal bandwidth

active volume
-> not fundamental; field concentration defeats simple V scaling

finite absorber number
-> not the missing one-photon resource

microscopic transition / LDOS / finite emitter
-> weak-coupling closure eventually fails

nonperturbative coupling
-> external optical/detector access can collapse

arbitrary finite passive multimode network
-> exact harmonic two-access transfer-area bound

autonomous detector thermodynamics
-> prior literature already covers post-capture reset/dark-count/entropy tradeoffs

active frequency conversion
-> pump/control resource explicitly buys conversion bandwidth

time-dependent known-mode capture
-> dynamic impedance matching can absorb a scheduled temporal mode

unknown arrival
-> finite coherent storage has a temporal-mode capacity limit

always-on detection
-> many accepted temporal modes imply external background admission and dead-time occupancy
```

## Strongest passive finite-network result

For a finite stable passive strictly proper optical-to-detector network, define

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

The frequency-integrated useful transfer obeys

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

For angular-frequency band width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

This is an **external-access resource law**, not an absolute bandwidth limit. Its mathematical ingredients are standard `H2`/Lyapunov/passivity theory; no novelty claim is made.

## Active control changes the resource, not necessarily the problem

A pumped two-mode frequency converter with unit peak conversion and FWHM `W` requires

```math
G\ge\frac{W}{2\sqrt2}.
```

For `G=g_0 sqrt(N_p)`,

```math
N_p\ge\frac{W^2}{8g_0^2}.
```

That quadratic scaling is architecture specific.

A more abstract finite-mode converter obeys

```math
\boxed{
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\Lambda\tau^2},
}
```

where `M_c` is the number of efficiently converted orthogonal modes and `Lambda` is the pump-to-conversion operator strength of the device.

The material/device bound on `Lambda` is unresolved.

## Known-time capture versus always-on detection

For a time-controlled one-port storage mode,

```math
\dot a=-\kappa(t)a+\sqrt{2\kappa(t)}s_{\rm in}.
```

Perfect zero-reflection loading of a known temporal wavepacket requires

```math
\boxed{
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
}
```

With finite maximum coupling during loading time `tau`,

```math
\boxed{
\eta_{\rm cap}
\le
1-e^{-2\kappa_{\max}\tau}.
}
```

So scheduled dynamic capture can evade a stationary spectral match, but it spends temporal control/coupling resource.

If the photon may instead occupy one of `M` orthogonal possible temporal modes and the detector has only `r` coherent storage modes before irreversible readout,

```math
\boxed{
\sum_j\eta_j\le r.
}
```

Hence uniform efficiency requires

```math
\boxed{r\ge M\eta.}
```

This is the key distinction:

> **perfectly matching one known temporal mode is not the same problem as building an always-on photodetector.**

## Always-on thermal coverage

Accepting more temporal modes also accepts more background modes.

For one flat thermal spatial/polarization channel,

```math
R_{\rm bg}\simeq\bar n\eta\frac{W}{2\pi}.
```

In a minimal nonparalyzable dead-time model, an otherwise perfect detector obeys

```math
\boxed{
\eta_{\rm ext}
\le
\frac1{1+\bar n W\tau_d/(2\pi)}.
}
```

This is a model-level background-blocking relation, not a universal detector theorem.

## Major prior-art boundary

Two primary frameworks sharply narrow what can be claimed:

- **Young, Sarovar & Leonard (2018)** already model incoming quantum fields, absorption, amplification, efficiency, dark counts, and timing in one photodetector framework.
- **Schwarzhans et al. (2026)** already model an autonomous detector work source, amplification/reset, entropy production, internal dark counts, jitter, and dead time.

A targeted search has not found a primary source combining externally normalized spectral capture/access constraints with autonomous detector thermodynamic accounting in one resource theory. This is only a negative search result; priority is unproven.

## Publication status

`PUBLICATION_BOUNDARY_AUDIT.md` currently concludes:

> **Continue the research. Do not write a manuscript yet.**

The passive/autonomous results are coherent but still vulnerable to being characterized as corollaries or compositions of established theories.

The active branch is now testing whether a more general space-time resource law survives.

## Canonical files

Start with:

- [`AGENTS.md`](AGENTS.md)
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)
- [`PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`](experiments/01-vanishing-absorber/PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md)
- [`PUBLICATION_BOUNDARY_AUDIT.md`](experiments/01-vanishing-absorber/PUBLICATION_BOUNDARY_AUDIT.md)
- [`ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md`](experiments/01-vanishing-absorber/ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md)
- [`TIME_DEPENDENT_CAPTURE_AUDIT.md`](experiments/01-vanishing-absorber/TIME_DEPENDENT_CAPTURE_AUDIT.md)
- [`TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md`](experiments/01-vanishing-absorber/TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md)
- [`ALWAYS_ON_TEMPORAL_COVERAGE.md`](experiments/01-vanishing-absorber/ALWAYS_ON_TEMPORAL_COVERAGE.md)
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)
- [`ARCHIVE_STATUS.md`](experiments/01-vanishing-absorber/ARCHIVE_STATUS.md)

Earlier derivations remain in the experiment directory as provenance.

## Current frontier

The next adversarial target is a common **space-time mode resource law** for actively controlled always-on photodetection, with explicit accounting of

```text
accepted spatiotemporal modes
+
pump/control norm
+
irreversible output capacity
+
thermal/background occupation
+
reset/dead-time capacity.
```

New agents should read [`AGENTS.md`](AGENTS.md) first.