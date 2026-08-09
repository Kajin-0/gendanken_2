# Finite-Transition LDOS Power–Bandwidth Constraint

**Date:** 2026-08-08  
**Status:** conditional derivation by combining established LDOS power–bandwidth theory with the repository's matched-rate single-transition detector model; no novelty claim  

## 1. Purpose

The previous microscopic test showed that one two-level transition plus an irreversible detection channel does not itself impose a one-photon speed ceiling if its optical coupling rate is treated as a freely adjustable Markov parameter.

This note asks the next question:

> If the transition strength is finite and the surrounding electromagnetic environment is passive and constrained, can the optical coupling rate remain arbitrarily large over a nonzero signal bandwidth?

The answer is **no under explicit environmental constraints**, but the resulting bound is not universal: it depends strongly on the minimum emitter–environment separation and the allowed material response.

This note uses the bandwidth-averaged LDOS bounds of Shim, Fan, Johnson & Miller, *Physical Review X* 9, 011043 (2019), DOI `10.1103/PhysRevX.9.011043`.

---

## 2. Microscopic detector requirement

From `MICROSCOPIC_SINGLE_TRANSITION.md`, use the one-excitation detector with

- optical amplitude-decay rate `gamma_o`;
- irreversible detection amplitude-decay rate `gamma_d`.

The irreversible detection probability for a monochromatic photon is

```math
A_d(\omega)
=
\frac{4\gamma_o\gamma_d}
{(\omega-\omega_0)^2+(\gamma_o+\gamma_d)^2}.
```

At matched rates,

```math
\gamma_o=\gamma_d=\Lambda,
```

so

```math
\boxed{
A_d(\Delta)
=
\frac{4\Lambda^2}
{\Delta^2+4\Lambda^2}.
}
```

The detection-probability HWHM is therefore

```math
\boxed{
\Delta\omega_{d,\rm HWHM}=2\Lambda.
}
```

If the desired signal has a Lorentzian spectral HWHM `Delta_omega_s`, a minimal matched-bandwidth requirement is

```math
\boxed{
\Lambda\ge\frac{\Delta\omega_s}{2}.
}
```

This criterion only requires that the detector's half-power spectral width be at least as wide as the signal's Lorentzian HWHM. More demanding flat-efficiency criteria would require a larger `Lambda`.

---

## 3. Finite transition strength and LDOS

For a fixed electric-dipole transition in the weak-coupling / Markov regime, spontaneous-emission rate is proportional to the projected electromagnetic LDOS.

Write the bare free-space population-decay rate as

```math
\Gamma_0.
```

The total radiative population-decay rate in an environment can be written schematically as

```math
\Gamma_{\rm tot}(\omega)
=
\Gamma_0 F_{\rm LDOS}(\omega),
```

where `F_LDOS` is the appropriate projected-LDOS enhancement including the free-space contribution.

The population-decay rate into one **useful** optical input/output channel cannot exceed the total radiative population-decay rate:

```math
\Gamma_o\le\Gamma_{\rm tot}.
```

In the amplitude-decay convention used throughout this repository,

```math
\Gamma_o=2\gamma_o.
```

Therefore

```math
\boxed{
\gamma_o
\le
\frac{\Gamma_0}{2}F_{\rm LDOS}.
}
```

This is deliberately optimistic: it allows unit branching of all radiative decay into the useful channel.

---

## 4. Shim et al. bandwidth-averaged LDOS bound

Shim et al. define a normalized Lorentzian frequency window

```math
H_{\omega_0,\Delta\omega}(\omega)
=
\frac{\Delta\omega/\pi}
{(\omega-\omega_0)^2+(\Delta\omega)^2},
```

where `Delta_omega` is the HWHM, and

```math
\langle\rho\rangle
=
\int_{-\infty}^{\infty}
\rho(\omega)
H_{\omega_0,\Delta\omega}(\omega)
\,d\omega.
```

For an emitter outside an arbitrary passive bulk nonmagnetic scatterer that can be enclosed by a halfspace no closer than distance `d`, their near-field electric/total LDOS bound can be written

```math
\boxed{
\frac{\langle\rho_E\rangle}
{\rho_0(|\widetilde\omega|)}
\le
\frac{1}
{8|\widetilde k|^3d^3}
\left[
 f(\widetilde\omega)
 e^{-2d\Delta\omega/c}
 +2\frac{\Delta\omega}{|\widetilde\omega|}
\right],
}
```

with

```math
\widetilde\omega
=\omega_0+i\Delta\omega,
\qquad
\widetilde k=\widetilde\omega/c,
```

and the bulk-material figure of merit

```math
\boxed{
f(\widetilde\omega)
=
\frac{
|\widetilde\omega\chi|^2
+|\widetilde\omega\chi|\Delta\omega
}
{|\widetilde\omega|\,
\operatorname{Im}(\widetilde\omega\epsilon)}.
}
```

The exact coefficient above follows the orientation-averaged electric/total LDOS convention of Shim et al. A specially oriented fixed dipole can change orientation factors; this note does not claim the same coefficient for every fixed orientation.

Define the right-hand side as

```math
F_B(\omega_0,\Delta\omega,d,\epsilon).
```

The scattered LDOS enhancement is bounded by `F_B`; including the free-space contribution gives the optimistic total enhancement bound

```math
\boxed{
\langle F_{\rm LDOS}\rangle
\le
1+F_B.
}
```

The critical conceptual property is that `F_B` is finite for any nonzero bandwidth when `d`, material response, and the admissible passive region are fixed.

---

## 5. Self-consistency bound for the Markov detector rate

The single-transition detector model assumed an approximately frequency-independent optical rate `gamma_o` over the signal bandwidth.

If the signal itself uses the same Lorentzian HWHM `Delta_omega_s`, then the constant-rate Markov model implies that its useful-channel enhancement over that window cannot exceed the bandwidth-averaged total LDOS enhancement.

Optimistically taking unit useful-channel branching,

```math
\boxed{
\gamma_o
\le
\frac{\Gamma_0}{2}
\left[1+F_B(\Delta\omega_s)\right].
}
```

Matched high-efficiency detection over the signal width requires

```math
\gamma_o=\Lambda
\ge
\frac{\Delta\omega_s}{2}.
```

Combining the two inequalities gives the implicit condition

```math
\boxed{
\Delta\omega_s
\le
\Gamma_0
\left[1+F_B(\Delta\omega_s)
\right].
}
```

This is the first version of the vanishing-absorber problem in which an arbitrarily large Markov optical rate is explicitly forbidden **once the entire passive environment and emitter separation are constrained**.

It is not a universal detector theorem. It is a self-consistency condition for the ideal matched-rate microscopic detector under the stated LDOS-bound geometry/material assumptions.

---

## 6. Narrowband low-loss scaling

The exact complex-frequency material figure of merit should be used for quantitative work.

For intuition only, consider a locally weakly dispersive, low-loss dielectric over a narrow band such that `chi` and `epsilon = 1 + chi` can be treated approximately real and slowly varying while

```math
\Delta\omega_s\ll\omega_0,
\qquad
k_0d\ll1.
```

At

```math
\widetilde\omega=\omega_0+i\Delta\omega_s,
```

the material FOM has the leading scaling

```math
f(\widetilde\omega)
\sim
\frac{\omega_0}{\Delta\omega_s}
\frac{\chi^2}{\epsilon}
```

up to terms that remain finite as `Delta_omega_s -> 0`.

The leading LDOS enhancement therefore scales approximately as

```math
F_B
\sim
\frac{1}{8(k_0d)^3}
\frac{\omega_0}{\Delta\omega_s}
\frac{\chi^2}{\epsilon}.
```

In the strongly enhanced regime `F_B >> 1`, the implicit condition becomes

```math
\Delta\omega_s
\lesssim
\Gamma_0
\frac{1}{8(k_0d)^3}
\frac{\omega_0}{\Delta\omega_s}
\frac{\chi^2}{\epsilon}.
```

Hence

```math
\boxed{
(\Delta\omega_s)^2
\lesssim
\frac{\Gamma_0\omega_0}
{8(k_0d)^3}
\frac{\chi^2}{\epsilon}.
}
```

Equivalently, defining the bare fractional linewidth

```math
r\equiv\frac{\Gamma_0}{\omega_0}
```

and normalized separation

```math
q\equiv k_0d,
```

the fractional signal HWHM obeys the approximate scaling

```math
\boxed{
\frac{\Delta\omega_s}{\omega_0}
\lesssim
\sqrt{
\frac{r}{8q^3}
\frac{\chi^2}{\epsilon}
}.
}
```

This scaling is the main physical insight of the present note. The precise numerical coefficient is conditional on the orientation-averaged halfspace LDOS bound and on the narrowband approximation used above.

---

## 7. Illustrative dimensionless scaling

To show only the strength of the distance dependence, take

```text
Gamma_0 / omega_0 = 1e-8
chi^2 / epsilon = 1
```

without assigning these numbers to a particular detector material.

The approximate fractional HWHM ceiling is then:

| `k0 d` | approximate `Delta_omega_s / omega_0` |
|---:|---:|
| `0.1` | `1.12e-3` |
| `0.03` | `6.80e-3` |
| `0.01` | `3.54e-2` |
| `0.003` | `2.15e-1` |

The final row is already large enough that the narrowband approximation is becoming questionable; it is retained only to show the `d^(-3/2)` trend.

---

## 8. The new loophole is explicit

The conditional ceiling scales as

```math
\Delta\omega_{s,\max}
\propto
\frac{1}{d^{3/2}}.
```

Therefore

```math
d\to0
```

again sends the local-response bound upward without limit.

This is not an algebraic nuisance. It identifies the next missing physical resource.

The earlier continuum capacitor counterexample concentrated the field by shrinking a geometric gap. The LDOS power–bandwidth theorem now says that if the emitter is kept a **fixed finite distance** from the passive concentrating material, arbitrary broadband enhancement is impossible; but if that distance is itself allowed to vanish, the local electromagnetic theory again permits divergence.

Thus a truly microscopic bound cannot avoid specifying what prevents

```math
d\to0.
```

Candidates include

- atomic dimensions;
- electron-wavefunction extent;
- spatially nonlocal dielectric response;
- tunneling / charge transfer across subnanometer gaps;
- chemical hybridization;
- finite-size structure of the optical transition.

---

## 9. What has actually changed

The candidate resource chain has now evolved as follows:

```text
active geometric volume
    -> insufficient

active energy participation
    -> can remain finite as volume vanishes

finite absorber number / two-level saturation
    -> insufficient for one photon

finite transition strength alone
    -> insufficient if arbitrary LDOS engineering is allowed

finite transition strength
+ finite bandwidth
+ constrained passive material
+ finite emitter-environment separation d
    -> finite optical-coupling ceiling
```

The remaining spatial loophole is the limit `d -> 0`.

---

## 10. Important limitations

This note does not establish a universal detector bound because:

1. the LDOS theorem constrains a specified passive material region and emitter separation, not arbitrary active/time-varying environments;
2. the coefficient quoted is for the orientation-averaged LDOS convention of the cited work;
3. useful-channel branching can be less than one, which would only tighten practical coupling;
4. the Markov detector model itself becomes questionable in strong/ultrastrong coupling;
5. the low-loss closed-form scaling is an approximation to the exact complex-frequency material FOM;
6. local continuum electrodynamics is precisely what becomes questionable as `d -> 0`;
7. no thermodynamic cost for the irreversible dark-state transfer or reset is included.

---

## 11. Prior-art interpretation

Shim et al. already establish the relevant arbitrary-bandwidth LDOS theorem: single-frequency LDOS may diverge in ideal lossless systems, while the average response over any nonzero bandwidth is finite once material and separation constraints are fixed.

Therefore this repository must not claim novelty for the LDOS power–bandwidth bound itself.

The repository-specific step is only to use that known bound as an adversarial constraint on the freely adjustable optical rate in the preceding ideal microscopic photodetector model.

Whether that combination yields a publishable detector-specific statement after a complete prior-art search is currently unknown.

---

## 12. Next decisive question

The optical branch now points to a sharply defined microscopic issue:

> **What physically justified minimum length replaces `d` when a photodetector transition is embedded in, bonded to, or formed from the concentrating material itself?**

A useful next calculation should test a nonlocal electronic/material model rather than imposing an arbitrary fabrication cutoff.

Possible first routes:

1. hydrodynamic/nonlocal dielectric response as a controlled continuum regularization;
2. a finite-size bound from the transition wavefunction and oscillator-strength sum rule;
3. a minimal dipole–surface separation derived from tunneling/hybridization rather than assigned by hand.

The thermodynamic irreversibility/reset problem remains an independent branch and should not be mixed into this spatial regularization until necessary.