# Mode-Weighted Atom Count and Optical Depth — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional derivation  
**Priority:** unassessed; no novelty claim

The traveling-wave calculation shows that external photon capture is controlled by optical access and collective coupling. This file asks what `N` actually means when the atoms do not all couple equally to the optical field.

---

## 1. Unequal microscopic couplings

For `N` two-level constituents coupled to one optical mode,

```math
H_I
=\hbar\sum_{j=1}^N
\left(g_j a\sigma_j^+ + g_j^* a^\dagger\sigma_j^-\right).
```

In the one-excitation sector define

```math
\boxed{
G
=\left(\sum_{j=1}^N|g_j|^2\right)^{1/2}.
}
```

The only matter superposition directly coupled to the photon is the normalized bright state

```math
\boxed{
|B\rangle
=\frac{1}{G}
\sum_j g_j|e_j\rangle.
}
```

All orthogonal combinations are dark to this ideal optical mode.

Thus the identical-coupling result

```math
G=g\sqrt N
```

is only a special case.

The real microscopic resource is

```math
\boxed{
G^2=\sum_j|g_j|^2,
}
```

not total atom number.

---

## 2. Effective coupled atom number

If `g_ref` is a chosen reference single-particle coupling, define

```math
\boxed{
N_{\rm eff}
=\frac{1}{|g_{\rm ref}|^2}
\sum_j|g_j|^2.
}
```

Then

```math
G=|g_{\rm ref}|\sqrt{N_{\rm eff}}.
```

`N_eff` need not equal the literal number of atoms in the object.

Examples:

```text
atom outside the optical mode       -> g_j ~ 0 -> negligible contribution
atom at a field node                 -> g_j ~ 0 -> negligible contribution
misaligned transition dipole        -> reduced contribution
strongly coupled antinode atom      -> large contribution
```

Therefore adding material outside the optically sampled region does not move the detector toward the useful boundary.

This kills total atom count as even the natural constrained coordinate in spatially extended detectors.

---

## 3. Continuum limit

For number density `n(r)`, transition dipole `d(r)`, and normalized mode field, schematically

```math
G^2
\propto
\int d^3r\,
n(\mathbf r)
|\mathbf d(\mathbf r)\cdot\mathbf E_{\rm mode}(\mathbf r)|^2.
```

The exact normalization depends on the optical-mode convention.

The important invariant structure is

```text
matter density
x
oscillator-strength density
x
optical-mode intensity/participation
integrated over the active region.
```

This is much closer to how a real semiconductor absorber should enter the detector boundary than literal total atom number.

---

## 4. Single-pass dilute-absorber limit

Now consider a traveling beam crossing a slab with independent absorbers of number density `n`, absorption cross section `sigma`, and thickness `L`.

Beer-Lambert attenuation gives optical depth

```math
\boxed{
\mathrm{OD}=n\sigma L.
}
```

For illuminated area `A`, the number of absorbers inside the sampled column is

```math
N_{\rm col}=nAL,
```

so

```math
\boxed{
\mathrm{OD}
=\frac{N_{\rm col}\sigma}{A}.
}
```

Single-pass absorption probability is

```math
\boxed{
P_{\rm abs}=1-e^{-\mathrm{OD}}.
}
```

This immediately shows that the relevant geometric combination is not `N` alone but approximately

```math
\frac{N\sigma}{A}.
```

Lateral atoms outside the illuminated area are irrelevant.

---

## 5. Add record branching

Let `eta_rec` be the conditional probability that an absorbed excitation becomes the desired persistent record, and `eta_mode` collect input mode-overlap/interface factors not included in Beer-Lambert absorption.

A minimal single-pass record probability is then

```math
\boxed{
P_R
=\eta_{\rm mode}\eta_{\rm rec}
\left(1-e^{-\mathrm{OD}}\right).
}
```

This factorization is conditional and deliberately simple; real semiconductor optics can include reflection, interference, re-emission, carrier diffusion, multiple passes, etc.

For target

```math
P_R\ge\eta_{\rm req},
```

one requires

```math
\boxed{
\mathrm{OD}
\ge
-\ln\left[
1-\frac{\eta_{\rm req}}
{\eta_{\rm mode}\eta_{\rm rec}}
\right]
}
```

provided

```math
\eta_{\rm req}<\eta_{\rm mode}\eta_{\rm rec}.
```

Equivalently,

```math
\boxed{
N_{\rm col}
\ge
\frac{A}{\sigma}
\left\{
-\ln\left[
1-\frac{\eta_{\rm req}}
{\eta_{\rm mode}\eta_{\rm rec}}
\right]
\right\}.
}
```

This is a concrete single-pass atom-column threshold.

---

## 6. High-efficiency asymptotic

In the idealized case

```text
eta_mode = 1,
eta_rec  = 1,
eta_req  = 1 - 2 epsilon,
```

we get

```math
\boxed{
\mathrm{OD}_{\min}
=-\ln(2\epsilon).
}
```

and

```math
\boxed{
N_{\rm col,min}
=\frac{A}{\sigma}\ln\left(\frac{1}{2\epsilon}\right).
}
```

Thus a simple single-pass absorber approaches unit detection only logarithmically with increasing optical depth.

This differs qualitatively from the ideal one-port resonant critical-coupling architecture in `TRAVELING_WAVE_CAPTURE.md`, where unit *monochromatic* efficiency can occur for arbitrarily weak nonzero absorber coupling by increasing interaction dwell time / narrowing bandwidth.

---

## 7. Why the cavity result does not contradict Beer-Lambert

Single-pass Beer-Lambert absorption gives the photon one traversal of the absorber.

The one-port resonant architecture allows coherent field buildup and repeated interaction before the photon can escape. At critical coupling, prompt reflection destructively interferes with the field leaking back from the resonator, allowing all incident monochromatic power to enter the internal loss/record channel.

Therefore

```text
single pass:
weak optical depth -> weak absorption;

matched resonant structure:
weak absorption per pass can still -> unity narrowband capture after many effective interactions.
```

The cost is stored-energy lifetime / bandwidth / sensitivity to detuning.

This is exactly the kind of hidden resource that invalidates a universal atom-count boundary.

---

## 8. Architecture changes the N scaling

The same microscopic absorbers can therefore obey very different apparent detector thresholds:

### Single-pass slab

```math
N_{\rm col,min}
\sim
\frac{A}{\sigma}\ln(1/\epsilon).
```

for high idealized efficiency.

### Resonant one-port matched detector

At one exact frequency and zero intrinsic loss,

```text
no finite N_min follows from peak efficiency alone;
```

finite bandwidth `B` restores a constraint through roughly

```math
N_{\rm eff,min}\propto\frac{\kappa B}{g^2\epsilon}
```

in the conditional bad-cavity Lorentzian benchmark.

Therefore there is no architecture-independent map

```text
atom count -> detector/not-detector.
```

The apparent `N_min` is a property of the whole optical + material + temporal architecture.

---

## 9. Extended semiconductor interpretation

For a bulk semiconductor with absorption coefficient `alpha`,

```math
\mathrm{OD}=\alpha L,
```

and

```math
P_{\rm abs}=1-e^{-\alpha L}
```

in the simplest noninterfering single-pass approximation.

Increasing detector area at fixed illumination, `alpha`, and `L` can add enormous numbers of atoms without changing the sampled optical depth or photon-record probability.

That is a decisive conceptual reason total atom count is the wrong variable for a macroscopic photodetector.

The more natural quantities are

```text
absorption coefficient x active thickness,
mode overlap,
oscillator-strength density,
carrier-record branching,
loss rates,
bandwidth / dwell time.
```

For spatially varying material, the optical resource is an intensity-weighted integral rather than a raw volume count.

---

## 10. New organizing statement

The original question

> At what point does a collection of atoms become a photodetector?

has now been sharpened again.

A more physically invariant version is:

> **How much mode-weighted optical oscillator strength is available, over what interaction time/bandwidth, and what fraction of the resulting excitation is converted into a persistent accessible record before it is lost?**

In the ideal collective model the microscopic optical resource is

```math
G^2=\sum_j|g_j|^2.
```

In the dilute traveling-wave limit it becomes optical depth

```math
\mathrm{OD}=n\sigma L.
```

In a bulk semiconductor it becomes approximately

```math
\alpha L
```

for simple single-pass absorption.

These are different representations of the same general lesson:

```text
only matter that actually participates in the optical interaction counts.
```

---

## 11. Current frontier

The next useful step is to bridge the ideal discrete-emitter picture to a continuum semiconductor more carefully.

Candidate route:

```text
sum_j |g_j|^2
-> oscillator-strength density / susceptibility
-> Im chi(omega)
-> absorption coefficient alpha(omega)
-> electron-hole generation rate
-> competition among recombination, trapping, extraction
-> persistent electrical record.
```

That would finally return to the user's original electron-hole-pair intuition while preserving all of the detector-boundary distinctions uncovered so far.

The central question becomes whether a useful dimensionless detector map can be constructed from quantities resembling

```math
\alpha L,
\qquad
\frac{\Gamma_{\rm ext}}{\Gamma_{\rm rec}},
\qquad
B\tau,
\qquad
\text{dark-event probability},
```

rather than atom count.
