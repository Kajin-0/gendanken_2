# Capture-to-Click Composition — External Bandwidth, Conditional Detection Efficiency, and Background Counts

**Date:** 2026-08-08  
**Status:** restricted serial-composition results joining repository capture theory to established autonomous-detector back-end theory; no novelty claim  

## 1. Motivation

The July 2026 autonomous-detector work of Schwarzhans et al. analyzes amplification/readout thermodynamics once the target excitation is present and explicitly notes that capture may carry additional costs and inefficiencies.

The repository's harmonic access theorem instead constrains transfer from a propagating optical channel into an irreversible receiving channel.

This note joins those two stages in the simplest possible serial architecture.

---

## 2. Serial detector architecture

Assume

```text
incident propagating optical mode
        -> capture front end
        -> stored/available target excitation
        -> autonomous detector back end
        -> registered click.
```

Let

```math
\eta_{\rm cap}(\omega)
```

be the probability that an incident photon at angular frequency `omega` is successfully captured into the state that triggers the back end.

Let

```math
\eta_D
```

be the conditional probability that a successfully captured excitation produces the registered detector click.

Assume for this first composition that

- the two stages are serial with no bypass;
- the back-end conditional efficiency is approximately constant over the optical capture band;
- events are sufficiently separated that back-end dead time does not modify the single-event probability.

Then

```math
\boxed{
\eta_{\rm ext}(\omega)
=\eta_{\rm cap}(\omega)\eta_D.
}
```

This factorization is elementary and is not a novelty claim.

---

## 3. Band-averaged external efficiency

For an angular-frequency band `B` of width

```math
W=|B|,
```

define

```math
\overline\eta_{\rm cap}
=\frac1W\int_B\eta_{\rm cap}(\omega)\,d\omega,
```

and

```math
\overline\eta_{\rm ext}
=\frac1W\int_B\eta_{\rm ext}(\omega)\,d\omega.
```

Under the constant-`eta_D` assumption,

```math
\boxed{
\overline\eta_{\rm ext}
=\eta_D\overline\eta_{\rm cap}.
}
```

---

## 4. Import the restricted one-channel capture bound

For the passive one-free-space-channel setting of `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`, let

```math
R_C
```

be the aggregate **amplitude-decay** access from the optical capture network into the receiving/capture side.

The restricted capture result is

```math
\boxed{
\overline\eta_{\rm cap}
\le
\frac{R_C}
{R_C+W/(4\pi)}.
}
```

Therefore the complete serial detector obeys

```math
\boxed{
\overline\eta_{\rm ext}
\le
\eta_D
\frac{R_C}
{R_C+W/(4\pi)}.
}
```

This is the first explicit repository relation containing both a propagating optical capture bandwidth and a separate conditional detector-back-end efficiency.

It is a restricted composition corollary, not a universal photodetector bound.

---

## 5. Capture-resource requirement for target external efficiency

Demand

```math
\overline\eta_{\rm ext}\ge\eta_*,
```

where

```math
0<\eta_*<1.
```

A necessary condition is first

```math
\boxed{
\eta_D>\eta_*.
}
```

If the back end is less efficient than the desired total detector, no optical front end can compensate for it in a serial architecture.

For `eta_D > eta_*`, solve the preceding inequality for `R_C`:

```math
\boxed{
R_C
\ge
\frac{\eta_*}
{\eta_D-\eta_*}
\frac{W}{4\pi}.
}
```

Thus

- required capture-side access grows linearly with optical bandwidth;
- it grows as the total efficiency target increases;
- it diverges as `eta_* -> eta_D` from below.

The divergence simply says that making the capture stage arbitrarily close to unity requires increasing the capture-access resource without bound within this idealized thermodynamic-coupling envelope.

---

## 6. Do not identify `eta_D` with a universal constant

In Schwarzhans et al., the conditional autonomous-detector efficiency depends on the detector's internal couplings and thermodynamic operating point. They provide a model-specific conjecture for its maximum in terms of detector/gain-medium dissipation rates.

This repository does **not** promote that conjecture into a general detector law.

The capture-to-click relation above is therefore kept in terms of the abstract conditional efficiency

```math
\eta_D.
```

Any particular back-end model may be inserted later only with its own assumptions and claim status.

---

## 7. External thermal/background counts are distinct from internal dark counts

Schwarzhans et al. define dark count rate from the detector's nonequilibrium steady-state detection current when no external target excitations are injected.

Call that internal rate

```math
R_{\rm dc,int}.
```

Now consider real thermal/background photons entering through the accepted propagating optical channel.

For one bosonic spatial/polarization channel with mean occupation

```math
\bar n(\omega),
```

the mean incoming photon flux per angular-frequency interval is

```math
\frac{\bar n(\omega)}{2\pi}.
```

The mean background click rate from the serial detector is therefore

```math
\boxed{
R_{\rm bg}
=
\int_B
\frac{d\omega}{2\pi}
\bar n(\omega)
\eta_{\rm ext}(\omega).
}
```

This is a count of **real input photons**, not an internal dark count.

---

## 8. Flat-background band result

If the thermal occupation is approximately constant across the accepted band,

```math
\bar n(\omega)\simeq\bar n_B,
```

then

```math
R_{\rm bg}
=
\frac{\bar n_B}{2\pi}
\int_B\eta_{\rm ext}(\omega)\,d\omega.
```

Using the definition of band-averaged external efficiency,

```math
\boxed{
R_{\rm bg}
=
\bar n_B
\frac{W}{2\pi}
\overline\eta_{\rm ext}.
}
```

Therefore a target

```math
\overline\eta_{\rm ext}\ge\eta_*
```

implies the unavoidable accepted-background mean-count floor

```math
\boxed{
R_{\rm bg}
\ge
\bar n_B
\frac{W}{2\pi}
\eta_*.
}
```

This statement is conditional on the signal and thermal background occupying the same accepted channel and band and on the detector being unable to distinguish them by another degree of freedom.

It is a mean-rate statement; thermal bunching affects fluctuations/noise beyond the mean and was treated separately in `THERMAL_INPUT_CHANNEL.md`.

---

## 9. System false-count bookkeeping in the dilute-event limit

If internal detector dark events and admitted external-background events are statistically independent and sufficiently dilute that dead-time blocking can be neglected, the observed false-click rate is

```math
\boxed{
R_{\rm false}
=R_{\rm dc,int}+R_{\rm bg}.
}
```

Hence, under the flat one-channel background approximation,

```math
\boxed{
R_{\rm false}
\ge
R_{\rm dc,int}
+
\bar n_B
\frac{W}{2\pi}
\eta_*.
}
```

This is not valid once detector dead time, afterpulsing, saturation, or correlated background events appreciably modify the counting process.

---

## 10. Why this distinction matters

The autonomous back-end detector can in principle reduce its internal thermal dark current by changing its nonequilibrium resources, energy gaps, temperatures, etc.

But it cannot distinguish a background photon from a desired photon if both arrive in the same accepted optical mode with the same energy/polarization/time statistics.

Therefore broadening the accepted optical band introduces a separate false-count pressure even if

```math
R_{\rm dc,int}\to0.
```

At infrared wavelengths this external thermal contribution can be much more important than at visible/near-visible frequencies because the Bose occupation of room-temperature modes rises rapidly toward longer wavelengths.

No material-specific claim is made yet.

---

## 11. Relation to the July 2026 autonomous-detector paper

The two theories now occupy complementary parts of the chain:

```text
THIS REPOSITORY FRONT END
propagating optical channel
-> capture probability / bandwidth / external background admission

SCHWARZHANS ET AL. BACK END
captured target excitation
-> amplification / entropy production / jitter / dead time / internal dark current.
```

Their conclusion explicitly identifies capture as an omitted source of possible cost/inefficiency.

This makes the capture-to-click interface a legitimate research question, but not automatically a novel one.

---

## 12. Claim boundary

### Derived within the restricted serial model

```math
\boxed{
\overline\eta_{\rm ext}
\le
\eta_D
\frac{R_C}{R_C+W/(4\pi)}
}
```

and therefore

```math
\boxed{
R_C
\ge
\frac{\eta_*}{\eta_D-\eta_*}
\frac{W}{4\pi}
}
```

for `eta_D > eta_*`.

For a flat one-channel thermal occupation,

```math
\boxed{
R_{\rm bg}
=
\bar n_B
\frac{W}{2\pi}
\overline\eta_{\rm ext}.
}
```

### Not established

- novelty of this composition;
- a universal external efficiency-bandwidth theorem beyond the one-free-space-channel optical bound;
- a universal relation between `eta_D` and internal dark count/dead time/entropy production;
- validity when capture and back-end dynamics are coherent and inseparable;
- validity in the high-flux/dead-time-limited counting regime;
- a material-specific infrared limit.

---

## 13. Next decisive search

Search specifically for prior work that already combines

```text
propagating optical capture bandwidth
+
autonomous/thermodynamic detector amplification
+
internal dark counts / dead time.
```

If that junction is absent, the next calculation should replace the serial factorization by a unified scattering-plus-autonomous-detector model and determine whether the harmonic capture bound survives when the back end is dynamically coupled rather than treated as a conditional black box.