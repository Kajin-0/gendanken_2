# HgCdTe Spectral Delay Peak with Energy Relaxation — First Robustness Test Beyond Ballistic Transport

**Date:** 2026-08-09  
**Status:** deterministic mean-energy transport model with Kane group velocity; numerical robustness result, not calibrated HgCdTe timing; no novelty claim

## 1. Purpose

`HGCDTE_SPECTRAL_DELAY_PEAK.md` predicts a high-optical-depth ballistic transit-time maximum at

```math
E_\gamma=E_{g,\rm in}.
```

The next question is whether that maximum disappears as soon as carriers lose energy while traversing the gradient.

This note adds the simplest available energy-relaxation dynamics while retaining the Kane velocity law.

---

## 2. Mean-energy transport equations

Use a linear gap

```math
E_g(x)=E_{g,\rm in}-Gx.
```

Let the electron mean excess energy above the local conduction edge be `epsilon`.

Use

```math
\boxed{
\frac{d\varepsilon}{dx}
=G-\frac{\varepsilon}{\ell_E}.
}
```

For local gap `E_g`, the two-band/Kane group velocity corresponding to mean excess energy `epsilon` is

```math
\boxed{
\frac{v}{v_K}
=
\frac{2\sqrt{\varepsilon(\varepsilon+E_g)}}
{2\varepsilon+E_g}.
}
```

This velocity tends to `v_K` at high excess energy and to zero at the band edge.

The transit time is

```math
\boxed{
T
=\int\frac{dx}{v[\varepsilon(x),E_g(x)]}.
}
```

This is a mean-energy surrogate, not a momentum-scattering Monte Carlo model.

---

## 3. Dimensionless form

Normalize energy by

```math
E_0=E_{g,\rm out}.
```

Define

```math
R=E_{g,\rm in}/E_0,
```

```math
h=E_\gamma/E_0,
```

and

```math
\boxed{
\kappa
=\frac{G\ell_E}{E_0}.
}
```

Since

```math
GL=E_0(R-1),
```

```math
\boxed{
\kappa
=\frac{R-1}{L/\ell_E}.
}
```

The dimensionless transit is

```math
\boxed{
\Theta
=\frac{Gv_K}{E_0}T.
}
```

---

## 4. High-optical-depth initial conditions

### Inside the graded gap range

For

```math
1<h\le R,
```

high optical depth places absorption close to the first allowed point where

```math
E_g=E_\gamma.
```

Thus

```math
\boxed{
\varepsilon(0)=0,
}
```

and the remaining gap span is

```math
\boxed{E_0(h-1).}
```

### Above the entrance gap

For

```math
h>R,
```

high optical depth places absorption close to the physical entrance.

The remaining geometric path is fixed at the full graded length.

Let `xi_e` be the electron share of photon excess above the entrance gap:

```math
\boxed{
\varepsilon(0)
=\xi_eE_0(h-R).
}
```

The HgCdTe flat-heavy-hole baseline corresponds approximately to

```math
\xi_e\approx1.
```

---

## 5. Analytic energy trajectory

Let `z` be the normalized downstream conduction-band drop measured from the generation point:

```math
z=G(x-x_s)/E_0.
```

The normalized excess energy

```math
e=\varepsilon/E_0
```

obeys

```math
\frac{de}{dz}
=1-\frac{e}{\kappa}.
```

Hence

```math
\boxed{
e(z)
=\kappa+(e_s-\kappa)e^{-z/\kappa}.}
```

The local normalized gap is

```math
g(z)=g_s-z.
```

Therefore

```math
\boxed{
\Theta
=\int_0^{g_s-1}
\frac{dz}
{2\sqrt{e(z)[e(z)+g(z)]}/[2e(z)+g(z)]}.
}
```

The integral is evaluated numerically.

---

## 6. Short-wave side is analytically monotonic

For

```math
h>R,
```

the physical path and gap profile are fixed.

Increasing photon energy increases the initial electron excess `e_s` when `xi_e>0`.

The relaxation solution preserves that ordering:

```math
\boxed{
\partial e(z)/\partial e_s
=e^{-z/\kappa}>0.
}
```

At fixed local gap, the Kane group velocity increases monotonically with electron excess energy.

Therefore

```math
\boxed{
\frac{dT}{dE_\gamma}<0
\qquad
(E_\gamma>E_{g,\rm in},\;\xi_e>0)
}
```

within this mean-energy model.

So the decreasing short-wave side of the timing peak is not a ballistic accident.

---

## 7. Long-wave side — numerical robustness result

For

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

raising photon energy moves the generation point upstream, increasing path length, but also lets the carrier enter the downstream part of the trajectory with more accumulated energy.

The sign is therefore not obvious from local reasoning alone.

Numerical integration was performed for

```text
R = 1.5, 2, 3
L/ell_E = 0 (ballistic), 0.2, 0.5, 1, 2, 5, 10
xi_e = 1 for the above-entrance branch.
```

Across this sweep,

```math
\boxed{
T(E_\gamma)
\text{ increased throughout }
E_{g,\rm out}<E_\gamma<E_{g,\rm in}.
}
```

The maximum remained at

```math
\boxed{E_\gamma=E_{g,\rm in}.}
```

No shift of the peak was observed in the tested mean-energy parameter range.

This is a numerical robustness result, not a proof for arbitrary scattering models.

---

## 8. Relaxation strengthens the peak delay

For fixed gap ratio `R`, stronger energy relaxation removes kinetic energy while the electron traverses the graded region.

Therefore the entrance-gap carrier, which starts cold at the physical entrance, becomes slower than in the ballistic model.

For example at

```math
R=2,
```

the dimensionless peak delay was

| `L/ell_E` | `Theta_peak` |
|---:|---:|
| 0 | 1.650 |
| 0.5 | 1.681 |
| 1 | 1.714 |
| 2 | 1.786 |
| 5 | 2.025 |
| 10 | 2.414 |

The peak position did not move in this sweep.

---

## 9. Physical interpretation

The spectral timing extremum is produced by two different mechanisms on its two sides.

### Long-wave side

```text
higher photon energy
-> first allowed generation point moves upstream
-> longer carrier path
-> delay increases.
```

### Short-wave side

```text
photon already exceeds entrance gap
-> generation point cannot move farther upstream
-> path is fixed
-> additional photon energy increases initial electron energy
-> delay decreases.
```

Energy relaxation modifies the quantitative time but does not remove this geometric change of regime in the tested model.

---

## 10. Prior-art posture

No novelty claim is made for

- energy relaxation;
- Kane group velocity;
- graded HgCdTe carrier transport;
- wavelength-dependent absorption position.

The focused search has not yet located the specific entrance-gap timing maximum in primary HgCdTe literature.

The result remains

**CANDIDATE TESTABLE PREDICTION — PRIORITY UNPROVEN.**

---

## 11. What this test does not establish

The calculation does not include

- momentum relaxation independent of energy relaxation;
- diffusion;
- stochastic phonon emission;
- multiband velocity corrections;
- nonuniform grading;
- recombination;
- space charge;
- avalanche multiplication;
- optical-depth broadening of generation position;
- electronics/RC response.

The next physically stronger test would use a drift-diffusion or Monte Carlo transport kernel rather than a single mean-energy trajectory.

---

## 12. Current conclusion

Within both

```text
ballistic Kane transport
```

and

```text
Kane velocity + finite mean energy-relaxation length,
```

the predicted high-optical-depth intrinsic timing maximum remains at

```math
\boxed{
E_\gamma=E_{g,\rm in}.
}
```

That makes the peak robust enough to justify an explicit tunable-wavelength experimental proposal before adding more theoretical complexity.
