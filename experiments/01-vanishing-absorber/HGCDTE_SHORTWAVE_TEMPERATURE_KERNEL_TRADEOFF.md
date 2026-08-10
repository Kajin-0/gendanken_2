# Short-Wave Temperature-Kernel Tradeoff — Why Temperature Is a Mid/Deep Control, Not the Preferred Near-Junction Perturbation

**Date:** 2026-08-09  
**Status:** conditional full-kernel temperature-matching calculation over the 72-member sample-A profile family; Hansen/Moazzami Beer-Lambert optics; no transport-temperature model; no novelty claim

## 1. Why revisit temperature after the short-wave pivot?

The mid/deep branch found a useful common A/B temperature schedule near

```text
300 K -> 3.632 um
215 K -> ~3.7935 um
115 K -> ~4.0045 um
```

with small full-kernel mismatch.

The short-wave branch independently found that wavelengths down to `~2.0 um` are needed to move generation through sample A's retained near-junction nonlinear/high-field region.

A natural proposal is therefore:

```text
use the short-wave pair
+
change temperature
+
retune wavelength to preserve generation position
+
form a temperature difference-in-differences.
```

That proposal is only valid if the **full timing kernel**, not just the local bandgap coordinate, can actually be held fixed.

This note tests that condition.

---

## 2. Full joint A/B matching objective

For each 300 K reference wavelength `lambda_0`, each lower temperature `T`, and each sample-A profile-family member, define

```math
\epsilon_A(T,\lambda)
=
\frac{
\|\mathbf A_A(T,\lambda)-\mathbf A_A(300,\lambda_0)\|_2
}{
\|\mathbf A_A(300,\lambda_0)\|_2
},
```

```math
\epsilon_B(T,\lambda)
=
\frac{
\|\mathbf A_B(T,\lambda)-\mathbf A_B(300,\lambda_0)\|_2
}{
\|\mathbf A_B(300,\lambda_0)\|_2
}.
```

At each profile solve

```math
\boxed{
\lambda_*(T)
=
\arg\min_{\lambda\ge2\ \mu{\rm m}}
\left[
\epsilon_A^2+\epsilon_B^2
\right].
}
```

The lower bound

```text
lambda >= 2.0 um
```

is imposed because `2 um` is already the short-wave edge of the optical model being used in the repository.

---

## 3. Local-gap matching is not enough in the short-wave regime

For orientation, the 300 K local-gap composition coordinate is approximately

```text
2.00 um -> x_edge ~0.5385
2.69 um -> x_edge ~0.4257
3.42 um -> x_edge ~0.3528
3.55 um -> x_edge ~0.3435
3.632 um -> x_edge ~0.3376.
```

A simple band-edge argument might suggest retuning wavelength with temperature so the same `x_edge` is selected.

But the conditional generation/timing kernel depends on the **entire depth-dependent absorption coefficient**, not just the first location satisfying

```math
E_g(x,T)=hc/\lambda.
```

In the strongly absorbing short-wave regime, temperature changes the absorption weighting enough that preserving `x_edge` does not preserve the full survival kernel.

---

## 4. The `2.00 um` lower anchor fails badly

For a 300 K reference

```math
\lambda_0=2.00\ \mu{\rm m},
```

the 215 K optimum is already driven against the `2.0 um` lower model boundary.

Worst profile-family mismatches are approximately

```text
215 K:
A ~32%
B ~41%

115 K:
A ~58%
B ~72%.
```

Thus the lower anchor that gives the strongest near-junction leverage cannot be treated as an iso-kernel temperature probe inside the present validated wavelength range.

---

## 5. The `2.69 um` upper short-wave anchor also fails as a temperature control

For

```math
\lambda_0=2.69\ \mu{\rm m},
```

the optimized common wavelengths are approximately

```text
215 K -> ~2.20-2.25 um
115 K -> ~2.00 um boundary.
```

Worst A/B full-kernel mismatches remain large:

```text
215 K:
A up to ~9.3%
B ~18.7%

115 K:
A up to ~24.5%
B ~43.1%.
```

So even the less aggressive member of the optimized short-wave pair is not a clean temperature-invariant optical coordinate.

---

## 6. The temperature-control crossover lies in the mid/deep band

Sweep the 300 K reference wavelength upward.

At 115 K the worst A/B mismatch decreases rapidly:

```text
300 K reference 3.30 um:
A worst ~6.9%
B ~9.8%

3.40 um:
A ~2.8%
B ~5.4%

3.42 um:
A ~2.3%
B ~4.9%

3.50 um:
A ~1.4%
B ~2.7%

3.55 um:
A <1%
B ~1.9%

3.60 um:
A ~0.6%
B ~1.2%.
```

Therefore, across the current 72-profile A family:

```math
\boxed{
\text{worst A and B mismatch}<5\%
}
```

first occurs near a 300 K reference of approximately

```math
\boxed{3.42\ \mu{\rm m},}
```

while

```math
\boxed{
\text{worst A and B mismatch}<2\%
}
```

requires roughly

```math
\boxed{3.55\ \mu{\rm m}.}
```

These are conditional thresholds for the present optical model/profile family, not universal wavelengths.

---

## 7. This creates a real experimental tradeoff

The wavelength directions needed for the two goals are opposite.

### Near-junction nonlinear-region leverage

Short wavelength moves the first allowed generation coordinate to higher Cd composition:

```text
~2.0-2.8 um
-> strong leverage on sample A's retained nonlinear region.
```

### Temperature-invariant full-kernel control

Longer wavelength is required before the entire temperature-dependent absorption kernel can be reproduced accurately:

```text
~3.4 um and above
-> increasingly good A/B temperature iso-kernel control.
```

Thus

```math
\boxed{
\text{short-wave localization}
\not\equiv
\text{temperature iso-kernel compatibility}.
}
```

This is not an optimization inconvenience. It follows from the wavelength/temperature dependence of the full absorption profile.

---

## 8. Why this matters for difference-in-differences

A temperature comparison has

```math
\mathbf A_T\mathbf q_T
-
\mathbf A_0\mathbf q_0.
```

Writing

```math
\mathbf A_T=\mathbf A_0+\delta\mathbf A,
\qquad
\mathbf q_T=\mathbf q_0+\delta\mathbf q,
```

gives

```math
\boxed{
\mathbf A_T\mathbf q_T
-
\mathbf A_0\mathbf q_0
=
\mathbf A_0\delta\mathbf q
+
\delta\mathbf A\,\mathbf q_0
+
\delta\mathbf A\,\delta\mathbf q.
}
```

The desired transport-change term is

```math
\mathbf A_0\delta\mathbf q.
```

But when short-wave temperature kernel mismatch is tens of percent, the optical term

```math
\delta\mathbf A\,\mathbf q_0
```

reintroduces exactly the unknown static sample-A baseline that the causal subtraction was intended to remove.

Therefore a naïve short-wave temperature difference-in-differences does **not** solve the A-baseline problem.

---

## 9. Correct role of temperature in the current architecture

Temperature remains valuable, but for the **mid/deep branch**.

Use it to test transport changes where common A/B full-kernel schedules such as

```text
3.632 -> ~3.7935 -> ~4.0045 um
```

are already conditionally robust.

Do not force temperature to also serve as the near-junction short-wave perturbation.

This strengthens the two-branch architecture:

```text
mid/deep wavelengths
-> sample-B calibration
-> temperature-controlled transport perturbation

short-wave wavelengths
-> sample-A near-junction localization
-> require a different causal knob whose optical kernel is much more stable.
```

---

## 10. Candidate alternative perturbations

Two obvious alternatives are applied bias and optical loading.

Applied bias is known to modify HgCdTe response time, but HgCdTe also exhibits field-dependent Franz-Keldysh absorption/cutoff shift, so bias cannot be assumed optically invisible without a separate electroabsorption audit.

Optical loading at fixed temperature and wavelength is especially relevant because the published sample-A/B work interprets composition-gradient effects in terms of space-charge suppression under strong injection.

In the linear-absorption regime, changing photon flux changes the **amplitude** of generation without changing its normalized Beer-Lambert depth kernel. Heating, nonlinear absorption, impedance changes, and readout amplitude-to-phase conversion remain explicit systematics that must be measured.

---

## 11. Next collision

The strongest next route is therefore not another temperature wavelength search.

Test a fixed-temperature, fixed-wavelength **load-differential complex-response observable**:

```text
low optical load
vs
higher optical load
```

using simultaneous A/B differential phase.

A particularly useful construction is the curvature or second finite difference versus load, because it cancels both

```text
static A/B baseline
and
approximately linear load-dependent phase response,
```

leaving the nonlinear saturation/space-charge timing response that the graded structure is physically expected to modify.

Numerical implementation for the present temperature tradeoff:

`numerics/hgcdte_shortwave_temperature_kernel_tradeoff.py`
