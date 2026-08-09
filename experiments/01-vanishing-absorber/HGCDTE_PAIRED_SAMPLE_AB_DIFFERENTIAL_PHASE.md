# Paired Sample A/B Differential Phase — Cancelling Tunable-Source Phase to Isolate Transport Contrast

**Date:** 2026-08-09  
**Status:** differential measurement protocol derived from the published 2023 A/B geometry; no sample-A numerical inversion yet; no novelty claim

## 1. Motivation

A tunable-MWIR phase measurement has a dangerous systematic:

```text
source modulation phase can itself change with wavelength.
```

That wavelength-dependent source phase cannot be removed by subtracting only one constant group delay.

The 2023 Xu et al. experiment naturally supplies two related devices:

```text
sample B
-> nonlinear interdiffusion region removed
-> smooth linear-gradient calibration case

sample A
-> part of nonlinear interdiffusion region retained
-> local built-in field approaches ~2e3 V/cm
-> strong published carrier-collection contrast.
```

This suggests a paired differential experiment in which the two devices are driven by the **same tunable modulated source at the same time**.

Primary structure source:

G.-Q. Xu et al., *Journal of Infrared and Millimeter Waves* 42 (2023) 285-291, DOI `10.11972/j.issn.1001-9014.2023.03.001`.

---

## 2. Single-device measured phase

At wavelength index `i` and RF frequency `Omega`, write the measured phase of device `d` as

```math
\boxed{
\phi_{d,i}
=\phi_{\rm src,i}
+\phi_{\rm path,d,i}
+\phi_{\rm elec,d}
-\Omega\,\mathbf A_{d,i}\mathbf q_d.
}
```

Here

```text
phi_src,i
= wavelength-dependent optical-source/modulation phase

phi_path,d,i
= wavelength-dependent phase of that optical arm/window/path

phi_elec,d
= device-channel electronics phase at the chosen RF frequency

A_d q_d
= device carrier mean-delay contribution.
```

For a full multi-frequency experiment, each term can also depend on `Omega`.

---

## 3. Simultaneous A-B subtraction removes arbitrary source phase

Illuminate both devices from the same split modulated MWIR beam and measure their electrical responses against the same RF reference.

Subtract:

```math
\Delta\phi_{AB,i}
\equiv
\phi_{A,i}-\phi_{B,i}.
```

Then

```math
\boxed{
\Delta\phi_{AB,i}
=
-\Omega
\left(
\mathbf A_{A,i}\mathbf q_A
-
\mathbf A_{B,i}\mathbf q_B
\right)
+\Delta\phi_{\rm path,i}
+\Delta\phi_{\rm elec}.
}
```

The arbitrary common source phase

```math
\phi_{\rm src,i}
```

cancels **at every wavelength**.

This is stronger than ordinary wavelength differencing on one detector, which cancels only a wavelength-independent common transfer.

---

## 4. Reciprocal detector swap cancels static arm asymmetry

A two-arm experiment still has

```text
optical-arm phase difference
+
electrical-channel phase difference.
```

Use two configurations.

### Configuration 1

```text
sample A in arm/channel 1
sample B in arm/channel 2.
```

Measure

```math
D_1
=\phi_{A,1}-\phi_{B,2}.
```

### Configuration 2

Swap the devices together with their device-specific connection reference so that the static arm/channel contribution reverses sign:

```text
sample A in arm/channel 2
sample B in arm/channel 1.
```

Measure

```math
D_2
=\phi_{A,2}-\phi_{B,1}.
```

Under a reciprocal, stable arm model,

```math
D_1
=\Phi_{AB}+\Psi_{12},
```

```math
D_2
=\Phi_{AB}-\Psi_{12},
```

where `Phi_AB` is the device transport contrast and `Psi_12` the static arm/channel difference.

Therefore

```math
\boxed{
\frac{D_1+D_2}{2}
=\Phi_{AB}.
}
```

This reciprocal swap is a **systematic-cancellation protocol**, not an assumption that the two optical paths are identical.

If physical swapping changes coupling/alignment substantially, use an equivalent calibrated RF/optical cross-over measurement rather than assuming exact reciprocity.

---

## 5. What is actually reconstructed

After source/arm cancellation, the paired phase gives

```math
\boxed{
\Phi_{AB,i}
=-\Omega
\left(
\mathbf A_{A,i}\mathbf q_A
-
\mathbf A_{B,i}\mathbf q_B
\right)
+\Delta c,
}
```

where `Delta c` is any remaining wavelength-independent device-specific timing offset.

Thus the paired experiment directly measures a **transport contrast**, not either absolute profile independently.

This is scientifically appropriate because the published 2023 experiment itself is a contrast experiment between the nonlinear-gradient and linear-gradient structures.

---

## 6. Joint reduced-mode inverse

Parameterize each device with a few smooth modes:

```math
\mathbf q_A
=\mathbf V_A\mathbf a,
```

```math
\mathbf q_B
=\mathbf V_B\mathbf b.
```

Then

```math
\boxed{
\boldsymbol\Phi_{AB}
=-\Omega
\begin{bmatrix}
\mathbf A_A\mathbf V_A &
-\mathbf A_B\mathbf V_B &
\mathbf1
\end{bmatrix}
\begin{bmatrix}
\mathbf a\\
\mathbf b\\
\Delta c/(-\Omega)
\end{bmatrix}.
}
```

The difference data can therefore fit transport modes in both devices jointly, provided their wavelength kernels are sufficiently independent and the model rank remains below the information content of the data.

No assumption that `q_A=q_B` is required.

---

## 7. Stronger constrained comparison

The most useful physical model may be

```math
\mathbf q_A
=\mathbf q_{A,\rm smooth}
+\delta\mathbf q_A,
```

where `delta q_A` is supported mainly in the retained nonlinear/high-field region, while sample B is represented by a smooth low-rank baseline.

Then the paired experiment asks directly:

> **Does sample A contain an additional spatial transport component beyond the smooth transport needed to explain sample B?**

That question is more robust than claiming an absolute microscopic velocity profile from either detector.

---

## 8. Why sample B is valuable even if its gradient barely changes transport

The 2023 authors conclude that sample B's remaining `100-200 V/cm` linear-gradient field does not strongly affect carrier motion.

That is an advantage for calibration.

Sample B can test whether the inversion / phase chain falsely invents internal structure when the physical transport should be relatively smooth.

If the method reconstructs strong localized structure in B, that is evidence for

```text
optical-kernel error
source/path systematic
regularization artifact
or an unmodeled transport mechanism.
```

Only after B behaves sensibly should sample A be used as the high-field contrast test.

---

## 9. Source-phase cancellation is a major practical advantage

A single-detector scan requires an independent model or calibration of

```math
\phi_{\rm src}(\lambda,\Omega).
```

The paired simultaneous measurement removes this entire arbitrary function from the device difference.

This changes the systematic requirement from

```text
know the absolute wavelength-dependent source phase
```

to

```text
maintain stable differential paths between two simultaneous detector channels.
```

The latter is still difficult, but it can be attacked experimentally with reciprocal swaps and reference calibration.

---

## 10. Remaining non-common systematics

The A-B subtraction does **not** automatically cancel

- different cryostat-window thickness / dispersion;
- different optical spot size or incidence angle;
- different detector impedance and RF packaging;
- different absorbed optical power;
- different contact/passivation transfer functions;
- different temperature;
- sample-to-sample material variation unrelated to the nonlinear gradient.

These must be controlled or modeled.

The paired experiment is therefore strongest when A and B are fabricated and packaged as comparably as possible.

---

## 11. Relation to the 2024 close-collision paper

The existence of the 2024 paper

`Potential application of HgCdTe detector with composition gradient in laser measurement`

is confirmed, but its technical text is not presently available in the accessible sources.

Do **not** claim that the paired differential method is absent from that paper until it is inspected.

Priority remains unresolved.

---

## 12. Claim boundary

### DERIVED

For two simultaneously driven devices, common arbitrary source phase cancels in their electrical phase difference.

Under a reciprocal two-arm swap, stable arm/channel phase asymmetry cancels in the average of the two swapped differential measurements.

### CONDITIONAL

- common source truly drives both arms coherently;
- arm/channel phase is stable over the reciprocal measurement;
- device coupling can be swapped/calibrated without introducing uncontrolled changes;
- low-frequency phase is dominated by mean carrier delay or the full transfer model is used.

### NOT ESTABLISHED

- actual sample-A optical matrix;
- actual A-B phase contrast;
- sufficient similarity of packages/cryostats;
- novelty / priority.

---

## 13. Next decisive work

The paired protocol makes the next data need sharper:

1. recover/digitize the **sample-A and sample-B** composition profiles, not only B;
2. build both optical kernel matrices;
3. determine a realistic dual-arm differential-phase covariance;
4. compute the joint A-B mode identifiability;
5. if feasible, use sample B as the smooth calibration structure and sample A as the nonlinear-gradient contrast structure.

This is currently a more promising route than attempting an absolute single-device phase inversion with a poorly known tunable-source phase.
