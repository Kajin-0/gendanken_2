# Traveling-Wave Capture — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional derivation  
**Priority:** unassessed; no novelty claim

This file removes the most artificial assumption in `COHERENT_CAPTURE_TO_RECORD.md`: the photon no longer begins inside the optical mode. It arrives as an external traveling one-photon wavepacket.

The purpose is to determine what actually limits conversion of an *incident* photon into a persistent material record.

---

## 1. Minimal one-port model

Use one optical mode `a`, one collective matter excitation `b`, and one irreversible record channel.

Parameters:

```text
kappa_in   = coupling rate between the external input/output channel and optical mode
kappa_loss = parasitic optical loss rate
kappa      = kappa_in + kappa_loss
G          = g sqrt(N) collective optical-matter coupling
gamma      = unwanted matter-excitation loss rate
Gamma      = desired matter -> persistent-record trapping rate
q          = gamma + Gamma
```

For a weak one-photon excitation, the one-excitation dynamics are linear. In a rotating frame,

```math
\dot a
= -\left(\frac{\kappa}{2}+i\Delta_c\right)a
-iGb
+\sqrt{\kappa_{\rm in}}\,\xi_{\rm in}(t),
```

```math
\dot b
= -\left(\frac{q}{2}+i\Delta_m\right)b
-iGa.
```

The one-port input-output relation is

```math
\xi_{\rm out}(t)
=\xi_{\rm in}(t)-\sqrt{\kappa_{\rm in}}\,a(t).
```

The persistent-record probability is

```math
P_R
=\Gamma\int_{-\infty}^{\infty}|b(t)|^2dt.
```

No dark-record process is included yet.

---

## 2. Exact spectral conversion kernel

For Fourier detuning `delta`, solve the linear equations frequency by frequency. With cavity and matter detunings written relative to the same incident frequency,

```math
b(\delta)
=
\frac{-iG\sqrt{\kappa_{\rm in}}}
{\left(\frac{\kappa}{2}-i\delta_c\right)
 \left(\frac{q}{2}-i\delta_m\right)+G^2}
\,\xi_{\rm in}(\delta).
```

Therefore the record-conversion probability density per incident spectral component is

```math
\boxed{
\eta_R(\delta)
=
\frac{\kappa_{\rm in}\Gamma G^2}
{\left|
\left(\frac{\kappa}{2}-i\delta_c\right)
\left(\frac{q}{2}-i\delta_m\right)
+G^2
\right|^2}.
}
```

For a normalized one-photon spectrum `|xi(delta)|^2`, the total record probability is the spectral average

```math
P_R
=\int d\delta\,|\xi(\delta)|^2\eta_R(\delta),
```

up to the chosen Fourier-normalization convention.

This already shows that external detection is a *mode-matching and bandwidth* problem, not just an internal transfer problem.

---

## 3. Resonant narrowband efficiency

At exact resonance,

```math
\boxed{
\eta_R(0)
=
\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}.
}
```

Define an effective matter-induced optical damping rate

```math
\boxed{
\kappa_m
=\frac{4G^2}{\gamma+\Gamma}.
}
```

Also define the fraction of matter decay that actually produces the desired record,

```math
\beta_R
=\frac{\Gamma}{\gamma+\Gamma}.
```

Then

```math
\boxed{
\eta_R(0)
=
\beta_R
\frac{4\kappa_{\rm in}\kappa_m}
{(\kappa+\kappa_m)^2}.
}
```

This factorization is physically transparent:

```text
external optical matching
x
matter-to-record branching.
```

The optical factor has exactly the familiar critical-coupling form.

---

## 4. Reflection amplitude and perfect capture condition

At resonance the one-port reflection amplitude is

```math
\boxed{
r(0)
=1-\frac{2\kappa_{\rm in}}
{\kappa+\kappa_m}.
}
```

In the clean one-port limit

```text
kappa_loss = 0,
gamma = 0,
```

we have `kappa = kappa_in` and `beta_R=1`.

Then zero reflection requires

```math
\boxed{\kappa_m=\kappa_{\rm in}.}
```

Since `kappa_m=4G^2/Gamma` when `gamma=0`, this gives

```math
\boxed{
\Gamma_{\rm match}
=\frac{4G^2}{\kappa_{\rm in}}
=\frac{4Ng^2}{\kappa_{\rm in}}.
}
```

At this point

```math
r(0)=0,
\qquad
\eta_R(0)=1.
```

Thus an incident resonant photon can be converted with unit monochromatic efficiency into the persistent record in this ideal one-port model.

---

## 5. Major counterexample — peak efficiency does not impose a minimum N

This result kills a tempting inference from the previous internal-mode calculation.

For any

```math
G>0,
```

however small, one can in principle choose

```math
\Gamma=4G^2/\kappa
```

and satisfy the critical-coupling condition in the clean one-port narrowband limit.

Therefore

```text
arbitrarily weak nonzero collective coupling
+
correspondingly slow matched record formation
-> unit monochromatic external efficiency.
```

So **peak narrowband detection efficiency by itself does not imply a nonzero minimum atom count.**

What weak coupling costs is bandwidth / speed.

This is an important correction to any attempt to infer a universal `N_min` from efficiency alone.

---

## 6. Optimization with parasitic optical and matter loss

For fixed `G`, `kappa`, and `gamma`, maximize

```math
\eta_R(0)
=
\frac{16\kappa_{\rm in}\Gamma G^2}
{[\kappa(\gamma+\Gamma)+4G^2]^2}
```

with respect to `Gamma`.

The optimum is

```math
\boxed{
\Gamma_{\rm opt}
=\gamma+\frac{4G^2}{\kappa}.
}
```

Substitution gives

```math
\boxed{
\eta_{R,\max}(0)
=
\frac{\kappa_{\rm in}}{\kappa}
\frac{4G^2}{4G^2+\kappa\gamma}.
}
```

Define

```math
\eta_{\rm esc}
=\frac{\kappa_{\rm in}}{\kappa},
```

and collective cooperativity

```math
\boxed{
C_N
=\frac{4G^2}{\kappa\gamma}
=\frac{4Ng^2}{\kappa\gamma}.
}
```

Then

```math
\boxed{
\eta_{R,\max}(0)
=\eta_{\rm esc}\frac{C_N}{1+C_N}.
}
```

The cooperativity language is established cavity-QED physics; no novelty claim attaches to that structure.

For `gamma -> 0`, interpret `C_N -> infinity`, giving

```math
\eta_{R,\max}(0)\to\eta_{\rm esc}.
```

---

## 7. Two independent ceilings

The optimized expression separates two failure mechanisms:

```text
eta_esc = kappa_in/kappa
```

sets the optical-access / parasitic-loss ceiling, while

```text
C_N/(1+C_N)
```

sets the coherent-coupling versus matter-loss ceiling.

This gives a strong design statement:

> increasing atom number cannot compensate indefinitely for photons that leave through inaccessible optical channels.

If the target record probability is `eta_req`, then a necessary condition is

```math
\eta_{\rm req}<\eta_{\rm esc}
```

for finite cooperativity.

No increase in `N` can beat the optical escape ceiling without changing the architecture.

For a symmetric two-sided cavity driven from only one side, `kappa_in/kappa=1/2` if the opposite port is otherwise equivalent. The single-sided maximum is therefore 50% in this simple accounting, unless the second port is coherently driven, suppressed, or otherwise incorporated into the design.

Thus optical boundary topology is itself part of the detector resource.

---

## 8. Cooperativity-based constrained atom count

Let the required persistent-record probability be

```math
\eta_{\rm req}=1-2\epsilon
```

for the idealized no-dark-record equal-prior discrimination mapping.

From

```math
\eta_{\rm req}
\le
\eta_{\rm esc}\frac{C_N}{1+C_N},
```

we obtain

```math
\boxed{
C_N
\ge
\frac{\eta_{\rm req}}
{\eta_{\rm esc}-\eta_{\rm req}}
}
```

provided `eta_req < eta_esc`.

Since

```math
C_N=\frac{4Ng^2}{\kappa\gamma},
```

this gives

```math
\boxed{
N
\ge
\frac{\kappa\gamma}{4g^2}
\frac{\eta_{\rm req}}
{\eta_{\rm esc}-\eta_{\rm req}}.
}
```

For an ideal one-port optical interface, `eta_esc=1`,

```math
\boxed{
N
\ge
\frac{\kappa\gamma}{4g^2}
\frac{1-2\epsilon}{2\epsilon}.
}
```

For small `epsilon`,

```math
N_{\min}
\sim
\frac{\kappa\gamma}{8g^2\epsilon}.
```

This is a different atom-count law from the closed transient Rabi-transfer result because it belongs to a different architecture and performance constraint.

---

## 9. Where the minimum N went when gamma = 0

If

```text
gamma = 0,
kappa_loss = 0,
```

then monochromatic resonant efficiency can reach unity for any nonzero `G` by reducing the matched record rate in proportion to `G^2`.

Therefore a finite `N_min` reappears only after imposing another resource constraint such as

```text
finite photon bandwidth,
finite observation time,
minimum count rate,
maximum dead time,
minimum reset rate,
nonzero matter loss,
finite parasitic optical loss,
etc.
```

This sharpens the central thesis:

> **an atom-count threshold is not intrinsic to detection; it is the projection of a higher-dimensional resource boundary onto a constrained architecture.**

---

## 10. Finite-bandwidth benchmark

Take the clean one-port critical-coupling condition

```math
\Gamma=\frac{4G^2}{\kappa}
```

and the bad-cavity / narrow-feature regime

```math
\kappa\gg G,
\qquad
|\delta|\ll\kappa.
```

Then the exact spectral kernel reduces to the Lorentzian form

```math
\boxed{
\eta_R(\delta)
\simeq
\frac{\Gamma^2}{\delta^2+\Gamma^2}.
}
```

Thus weak coupling preserves unit on-resonance efficiency but narrows the detector bandwidth to the scale

```math
\boxed{
\Gamma
=\frac{4Ng^2}{\kappa}.
}
```

This is the missing price of the weak-coupling perfect-efficiency construction.

---

## 11. Lorentzian one-photon wavepacket benchmark

Use a normalized incident spectral density

```math
S_B(\delta)
=
\frac{1}{\pi}
\frac{B}{\delta^2+B^2},
```

where `B` is the incident photon HWHM in angular-frequency units.

Averaging the matched detector response gives

```math
P_R
=\int d\delta\,
S_B(\delta)
\frac{\Gamma^2}{\delta^2+\Gamma^2}.
```

The integral is exact:

```math
\boxed{
P_R
=\frac{\Gamma}{\Gamma+B}.
}
```

Requiring

```math
P_R\ge 1-2\epsilon
```

gives

```math
\boxed{
\Gamma
\ge
B\frac{1-2\epsilon}{2\epsilon}.
}
```

Using `Gamma=4Ng^2/kappa`,

```math
\boxed{
N
\ge
\frac{\kappa B}{8g^2}
\frac{1-2\epsilon}{\epsilon}.
}
```

For small `epsilon`,

```math
\boxed{
N_{\min}
\sim
\frac{\kappa B}{8g^2\epsilon}.
}
```

This is a **conditional bandwidth-limited atom-count law**.

The exact numerical prefactor depends on wavepacket shape and operating regime, but the important physics is robust:

```text
weak coupling can preserve peak efficiency only by sacrificing bandwidth;
finite bandwidth restores a finite resource threshold.
```

---

## 12. Relation to the previous internal-mode result

The previous model started with the photon already inside the cavity and found a clean-limit optimum

```math
\Gamma_{\rm opt}=2G.
```

The external narrowband scattering problem instead gives, in the clean one-port limit,

```math
\Gamma_{\rm match}=\frac{4G^2}{\kappa}.
```

These are not contradictory.

They optimize different tasks:

```text
internal initial excitation:
convert a stored cavity excitation into a record before cavity loss;

external scattering:
impedance-match a traveling incident field into the matter/record channel.
```

The distinction must be retained.

---

## 13. Strongest conceptual update

The photodetector boundary now separates into at least four independent resources:

```text
1. optical access / mode matching
2. coherent light-matter coupling
3. competition with intrinsic matter loss
4. conversion bandwidth / record rate
```

Atom number enters mainly through

```math
G=g\sqrt N
```

or equivalently collective cooperativity

```math
C_N=\frac{4Ng^2}{\kappa\gamma}.
```

This suggests a more precise answer to the original question:

> **A collection of atoms does not become a photodetector at a universal N. It enters a useful detector regime when the optical access, collective coupling, loss, record-conversion, and bandwidth ratios jointly cross the performance surface demanded by the measurement.**

A useful set of coordinates is now

```math
\eta_{\rm esc}=\frac{\kappa_{\rm in}}{\kappa},
\qquad
C_N=\frac{4Ng^2}{\kappa\gamma},
\qquad
\frac{\Gamma}{4G^2/\kappa},
\qquad
\frac{B}{4G^2/\kappa}.
```

The first controls optical accessibility, the second loss-limited conversion, the third critical matching, and the fourth bandwidth mismatch.

---

## 14. Current next attack

The natural next step is to remove the cavity-specific language as far as possible and connect these rate ratios to free-space / semiconductor quantities:

```text
single-particle absorption cross section
oscillator strength
number density
optical depth
active thickness
mode area / confinement
carrier-extraction or trapping rate
recombination rate
incident bandwidth.
```

Questions to test:

1. Does collective cooperativity reduce to an optical-depth-like resource in the appropriate traveling-wave limit?
2. Can the matched-record condition be written directly as an absorptance / extraction-rate condition for a semiconductor slab?
3. Does the atom-count question become a density x interaction-length question rather than total N in extended matter?
4. Which parts survive once band formation, disorder, dephasing, and many-mode continua replace the ideal bright state?

A focused primary-source audit is required before any claim that the exact detector-boundary formulation is new.
