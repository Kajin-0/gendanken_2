# Gedanken 2

First-principles thought experiments in photodetector physics.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, counterexamples, corrections, and prior-art collisions are preserved because they define the actual result.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, fast, sensitive, and perfectly absorbing?

The original active-volume route failed. The research moved through optical access, quantum and network constraints, active control, semiconductor extraction, HgCdTe tunneling/transport, heterostructure grading, and finally back to a detector-specific optical question:

> **Does photon wavelength determine intrinsic carrier timing in a compositionally graded HgCdTe absorber because the local band gap determines where that photon can first be absorbed?**

## Current candidate prediction

For a monotonic linear gap

```math
E_g(x)=E_{g,\rm in}-Gx,
```

photons satisfying

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in}
```

cannot be absorbed until

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G}.
}
```

Their maximum remaining graded transport distance is

```math
\boxed{
d_\gamma
=\frac{E_\gamma-E_{g,\rm out}}{G}.
}
```

At high optical depth, absorption occurs close to that first allowed point.

Inside the graded gap range, the intrinsic transit delay therefore increases as photon energy rises because the generation point moves farther upstream.

Once

```math
E_\gamma>E_{g,\rm in},
```

the whole absorber is optically allowed. The generation point can no longer move upstream; additional photon energy instead increases the electron's initial kinetic energy and reduces transit time.

Hence the current ballistic model predicts

```math
\boxed{
T(E_\gamma)
\text{ reaches a maximum at }
E_\gamma=E_{g,\rm in}.
}
```

Equivalently,

```math
\boxed{
\lambda_{\rm peak}
\simeq hc/E_{g,\rm in}.
}
```

The predicted timing fingerprint is

```text
near long-wave endpoint:
short intrinsic delay

through graded absorption range:
delay rises

entrance-gap wavelength:
delay maximum

shorter wavelengths:
delay falls toward a full-length high-energy floor.
```

## HgCdTe-specific photoexcitation correction

A downstream absorbed photon does not generally create a cold electron.

Write

```math
\varepsilon_{\rm gen}
=\xi_e(E_\gamma-E_g).
```

The symmetric two-band optical model gives `xi_e=1/2`, but the experimentally validated simplified HgCdTe Kane spectrum contains a nearly flat heavy-hole band and heavy-hole-to-electron optical transitions.

In that ideal heavy-hole limit,

```math
\boxed{\xi_e\approx1.}
```

so nearly all local photon excess can enter the electron.

This correction changes the hot-electron interpretation but **does not remove the timing peak**.

## First relaxation robustness test

The timing calculation was repeated with mean carrier energy obeying

```math
\frac{d\varepsilon}{dx}
=G-\frac{\varepsilon}{\ell_E}
```

and local Kane group velocity

```math
\boxed{
\frac{v}{v_K}
=
\frac{2\sqrt{\varepsilon(\varepsilon+E_g)}}
{2\varepsilon+E_g}.
}
```

Across tested gap ratios

```text
Eg,in/Eg,out = 1.5, 2, 3
```

and relaxation strengths

```text
L/ell_E = 0 through 10,
```

the delay maximum remained at

```math
\boxed{E_\gamma=E_{g,\rm in}.}
```

Energy relaxation increased the peak delay but did not move it in this deterministic mean-energy model.

This is not yet a full scattering/Monte Carlo result.

## Exact generation statistics

In optical-depth coordinates, conditioned on absorption,

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}
{1-e^{-\tau_\gamma}}.
}
```

This gives an exact analytic route from spectral absorption to a distribution of carrier generation positions and then to transit-time statistics.

At finite optical depth, the generation-position timing spread is not necessarily monotonic with QE; the full distribution should be used rather than a slogan such as `higher QE -> lower jitter`.

## Prior-art status

Existing primary HgCdTe work already covers

- compositionally graded detectors;
- grading-induced faster carrier transport;
- graded spectral response/QE;
- ultrafast/tunable optical timing instrumentation;
- heavy-hole-to-electron Kane transitions.

The focused search has **not** found an inspected primary source explicitly deriving or measuring

```text
wavelength
-> generation-position distribution
-> corrected graded transit-time distribution
```

or the specific **timing maximum at the entrance-gap wavelength**.

That negative search is not novelty evidence.

Current status:

> **candidate underexplored, directly testable analytic prediction; priority unproven.**

## Proposed decisive experiment

Use a graded HgCdTe detector with a measured composition profile and sweep an ultrafast source across

```text
near output cutoff
-> graded-gap interval
-> entrance-gap wavelength
-> shorter wavelengths.
```

Keep bias, temperature, spot, pulse energy, and readout fixed.

The preferred observable is differential low-frequency group delay or normalized impulse centroid because a wavelength-independent common electronics transfer cancels in differences.

A strong validation would be a reproducible timing extremum near the independently predicted entrance-gap wavelength, ideally shifting with the temperature dependence of that entrance gap.

See:

`experiments/01-vanishing-absorber/HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`

## Publication status

> **Continue research. Do not write a manuscript yet.**

The next decisive tests are

1. a stronger scattering/drift-diffusion/Monte Carlo robustness calculation; or
2. wavelength-resolved timing data on a graded HgCdTe device.

If the timing peak survives stronger transport physics and remains absent from prior literature, reassess publication significance then.

## Canonical files

Start with:

- [`AGENTS.md`](AGENTS.md)
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)
- [`HGCDTE_SPECTRAL_DELAY_PEAK.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_DELAY_PEAK.md)
- [`HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_DELAY_RELAXATION_ROBUSTNESS.md)
- [`HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md`](experiments/01-vanishing-absorber/HGCDTE_PROPOSED_SPECTRAL_TIMING_EXPERIMENT.md)
- [`HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md)
- [`HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md`](experiments/01-vanishing-absorber/HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md)
- [`HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md`](experiments/01-vanishing-absorber/HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md)
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)

New agents should read `AGENTS.md` first.
