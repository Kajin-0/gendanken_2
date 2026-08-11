# Paper Claim Ledger Addendum — Hot-State / Thermalization Revision

**Date:** 2026-08-11  
**Purpose:** records only the claims produced by the initial-state / thermalization adversarial stress. `PAPER_CLAIM_LEDGER.md` and the earlier review addendum remain the base ledgers.

## HS1 — finite hot->cold thermalization adds one spatial mode

**Status:** DERIVED / CHECKED / CONDITIONAL

For a deterministic hot state with velocity `v_h` relaxing irreversibly to a cold state with velocity `v_c` at rate `rho`, the exact raw-current response is

```math
J_h(d,s)
=A+B_c e^{-s d/v_c}
+B_h e^{-(s+\rho)d/v_h}.
```

Thus finite thermalization introduces a second spatial exponential rather than destroying finite spatial rank.

## HS2 — thermalization length

**Status:** DERIVED

The hot-state memory decays over

```math
\boxed{\ell_h=v_h/\rho=v_h\tau_h.}
```

This is the natural spatial control parameter for the spectral-depth experiment.

## HS3 — wavelength-independent initialization is exact rank two

**Status:** DERIVED / CHECKED

If the same hot fraction `f` is generated in every spectral channel,

```math
J_f=(1-f)J_c+fJ_h
```

is a depth-independent particular term plus two spatial exponentials.

Therefore the first-difference sequence satisfies the six-color rank-two closure exactly.

Finite thermalization by itself is a model-order increase, not an uncontrolled failure of the hierarchy.

## HS4 — wavelength-dependent initialization is a separate source-state systematic

**Status:** DERIVED

If

```math
f_m=f_0+\delta f_m,
```

then

```math
J_m=J_{f_0}(d_m)+\delta f_m[J_h(d_m)-J_c(d_m)].
```

The channel-dependent coefficient generically breaks fixed-coefficient rank-two closure.

The relevant assumption is therefore sufficiently invariant initial-state distribution across wavelength, or an explicit source-state model.

## HS5 — excess-energy invariance protects fixed model order

**Status:** DERIVED / CONDITIONAL

In the ideal linear graded-gap limit where absorption depends only on local total photon excess energy, the generated excess-energy distribution is wavelength-independent.

Any initial-state probability depending only on that excess-energy variable is then wavelength-independent as well, preserving the rank-two thermalization model.

This is a sufficient protection, not a fundamental requirement of the spectral-depth method.

## HS6 — current HgCdTe quartet has small excess-energy mismatch

**Status:** CHECKED / CONDITIONAL OPTICAL MODEL

For the current Hansen/Moazzami quartet, the generation-weighted mean total excess energies are approximately

```text
52.3532, 52.4276, 52.4782, 52.4726 meV
```

with peak-to-peak variation

```math
\boxed{\Delta \bar E_{ex}\simeq0.125\ \mathrm{meV}.}
```

The corresponding standard deviation changes from approximately `33.235` to `32.694 meV`.

This does not prove microscopic hot-state invariance.

## HS7 — long thermalization can create a one-mode failure comparable to the current target

**Status:** CHECKED / CONDITIONAL GENERIC STRESS

For

```text
v_c = 3.45e4 m/s
v_h = 6.90e4 m/s
f_hot = 0.5
RF = 100 MHz
```

and the current four source depths, wavelength-independent thermalization gives approximately

```text
ell_h = 1 um -> C4 phase ~ +0.00087 deg
ell_h = 2 um -> ~ +0.00373 deg
ell_h = 5 um -> ~ +0.00547 deg
```

while remaining an exact rank-two process.

## HS8 — small wavelength-dependent hot-fraction changes can matter for the present tiny target

**Status:** CHECKED / CONDITIONAL SENSITIVITY

Using the actual quartet excess-energy means and the same generic two-state stress, requiring initialization-induced 100-MHz phase error to remain below 10% of the current `0.01198 deg` gradient-sensitive target gives allowed peak-to-peak hot-fraction variation of order

```text
~0.25-0.8 percentage points
```

across thermalization lengths `0.25-10 um`.

These are sensitivity coordinates, not HgCdTe thermalization measurements.

## HS9 — one-mode failure can precede resolvable second-mode identification

**Status:** CHECKED / IMPORTANT INTERPRETATION LIMIT

A second mode can produce a detectable four-color closure failure while the six-color Hankel minor is not yet significant enough for reliable root recovery at the same noise level.

Therefore

```text
four-color failure + unresolved second-mode witness
-> mechanism unresolved at present SNR
```

and not

```text
four-color failure -> velocity gradient.
```

This conservative interpretation rule is mandatory for the manuscript.

---

## Paper consequence

The revised discussion should distinguish

```text
finite wavelength-independent thermalization
-> ordinary extra spatial mode handled by the six-color branch

wavelength-dependent initialization
-> source-state systematic requiring optical/material bounding or explicit modeling.
```

The current HgCdTe excess-energy invariance check materially reduces, but does not eliminate, the second concern.
