# HgCdTe TAT–BTBT Crossover — Converting Trap-Assisted Exponential Advantage into a Trap-Density Requirement

**Date:** 2026-08-09  
**Status:** exact algebra within a standard one-dimensional HgCdTe TAT current model and the repository BTBT model; defect matrix element/trap density/electrostatics remain device-specific; no novelty claim

## 1. Purpose

`HGCDTE_TAT_FIELD_SCALE.md` showed that a near-band-edge trap can reduce the tunneling exponent field far below the direct-BTBT scale.

That does not yet say whether the **current** is important, because TAT has a defect-dependent prefactor.

The next question is:

> **At a specified field, what trap density makes TAT equal to direct BTBT?**

This turns the exponential comparison into a material-quality threshold.

---

## 2. Direct-BTBT current

Use the standard uniform-field parabolic-barrier HgCdTe form

```math
J_{\rm BTBT}
=
\frac{q^3\sqrt{2m^*}\,F V}
{4\pi^3\hbar^2E_g^{1/2}}
\exp(-F_K/F),
```

where

```math
\boxed{
F_K
=
\frac{\pi\sqrt{m^*}E_g^{3/2}}
{2\sqrt2 q\hbar}.
}
```

---

## 3. Trap-assisted current

A standard HgCdTe TAT expression can be written

```math
J_{\rm TAT}
=
\frac{q^2m^*V\,\kappa_d^2N_T}
{8\pi\hbar^3\Delta_t}
\exp(-F_T/F),
```

where

```math
\Delta_t=E_g-E_T,
```

`N_T` is trap density and `kappa_d^2` is the defect-potential matrix-element factor.

The exact exponent field `F_T` depends on the adopted trap/barrier geometry.

For the simple one-dimensional trap-to-conduction-band barrier used in `HGCDTE_TAT_FIELD_SCALE.md`,

```math
\boxed{
F_T
=
\frac{4\sqrt{2m^*}\Delta_t^{3/2}}
{3q\hbar}.
}
```

More general HgCdTe TAT models replace this by a geometrical factor; the crossover algebra below does not require the special form until numerical evaluation.

---

## 4. Exact current ratio

Divide the two currents. The bias factor `V` cancels:

```math
\boxed{
\frac{J_{\rm TAT}}{J_{\rm BTBT}}
=
\frac{\pi^2\kappa_d^2N_T\sqrt{m^*E_g}}
{2\sqrt2 q\hbar\Delta_t F}
\exp\!\left[
\frac{F_K-F_T}{F}
\right].
}
```

This equation isolates the two reasons TAT can dominate:

```text
prefactor
-> trap density and defect matrix element

exponent
-> TAT traverses only a partial-gap barrier.
```

If

```math
F_T<F_K,
```

the exponential factor favors TAT by

```math
\exp[(F_K-F_T)/F].
```

At fields far below `F_K`, this factor can be enormous.

---

## 5. Crossover trap density

Define

```math
J_{\rm TAT}=J_{\rm BTBT}
```

at a specified field `F`.

Solving for trap density gives

```math
\boxed{
N_{T,\times}(F)
=
\frac{2\sqrt2 q\hbar\Delta_t F}
{\pi^2\kappa_d^2\sqrt{m^*E_g}}
\exp\!\left[-
\frac{F_K-F_T}{F}
\right].
}
```

Therefore

```text
N_T > N_T,x
-> TAT exceeds direct BTBT

N_T < N_T,x
-> direct BTBT exceeds TAT
```

inside the shared simplified model.

The exponential term can drive `N_T,x` to extremely small values when `F_T << F_K`.

This is the precise mathematical statement behind the qualitative observation that

> **an exponentially tiny direct-BTBT current is not evidence that tunneling leakage is negligible in a defect-containing device.**

---

## 6. Normalize the exponent advantage by trap depth

For the simple one-dimensional TAT exponent,

```math
\frac{F_T}{F_K}
=
\frac{16}{3\pi}
\left(\frac{\Delta_t}{E_g}\right)^{3/2}.
```

Define

```math
\delta_t=\Delta_t/E_g,
\qquad
x=F/F_K.
```

Then

```math
\boxed{
\frac{F_K-F_T}{F}
=
\frac{1-
\frac{16}{3\pi}\delta_t^{3/2}}
{x}.
}
```

Hence the TAT exponential advantage is

```math
\boxed{
\mathcal A_{\rm exp}
=
\exp\!\left[
\frac{1-
\frac{16}{3\pi}\delta_t^{3/2}}
{x}
\right].
}
```

For a near-conduction-band trap and `x << 1`, this factor is extraordinarily large.

---

## 7. Example of the exponent only

Take

```math
\delta_t=0.06,
```

corresponding to a trap about `6 meV` below the conduction band in a `100 meV` gap.

Then

```math
F_T/F_K\simeq0.02495.
```

At

```math
F/F_K=0.01,
```

the exponent advantage is

```math
\exp[(1-0.02495)/0.01]
\sim e^{97.5},
```

an astronomically large ratio before any prefactor is included.

At

```math
F/F_K=0.05,
```

it is still

```math
\sim e^{19.5}.
```

This does **not** establish a large absolute TAT current. If `N_T` or the matrix element is vanishingly small, the current can still be negligible.

It shows only that once a viable trap channel exists, direct BTBT is a poor reference for deciding whether tunneling leakage is absent.

---

## 8. Direct material-quality requirement for a TAT current budget

The TAT expression itself is linear in `N_T`.

For an allowed TAT current density

```math
J_{T,*},
```

the maximum permitted trap density is

```math
\boxed{
N_{T,\max}
=
\frac{8\pi\hbar^3\Delta_t}
{q^2m^*V\kappa_d^2}
J_{T,*}
\exp(F_T/F).
}
```

If the field is approximately uniform over width `L`,

```math
V=FL,
```

so

```math
\boxed{
N_{T,\max}
=
\frac{8\pi\hbar^3\Delta_t}
{q^2m^*FL\kappa_d^2}
J_{T,*}
\exp(F_T/F).
}
```

This is the cleanest way to turn a speed-driven field requirement into a **trap-density specification**, once the trap matrix element and trap energy are identified experimentally.

---

## 9. Why this is more useful than a universal TAT field

There is no unique intrinsic TAT onset field because TAT depends on defect population.

The useful design statement is instead

```text
target transit requirement
-> required local field

required field + trap energy/matrix element
-> allowed N_T for a specified TAT current budget.
```

That is fundamentally different from direct BTBT, where the exponent is set by intrinsic band structure in the simplified model.

---

## 10. Claim boundary

### DERIVED within the shared simplified TAT/BTBT model

```math
\boxed{
\frac{J_{\rm TAT}}{J_{\rm BTBT}}
=
\frac{\pi^2\kappa_d^2N_T\sqrt{m^*E_g}}
{2\sqrt2q\hbar\Delta_tF}
\exp[(F_K-F_T)/F],
}
```

```math
\boxed{
N_{T,\times}
=
\frac{2\sqrt2q\hbar\Delta_tF}
{\pi^2\kappa_d^2\sqrt{m^*E_g}}
\exp[-(F_K-F_T)/F],
}
```

and

```math
\boxed{
N_{T,\max}
=
\frac{8\pi\hbar^3\Delta_t}
{q^2m^*FL\kappa_d^2}
J_{T,*}e^{F_T/F}
}
```

for the uniform-field version.

### KNOWN

HgCdTe diode literature reports TAT-limited leakage and fitted near-band-edge trap states in multiple technologies.

### OPEN

- target trap energy distribution;
- target `N_T`;
- defect-potential matrix element;
- trap occupation and capture cross sections;
- realistic nonuniform field profile;
- quantitative TAT current in the user's target geometry.

### NON-CLAIM

This file does not establish

- a universal maximum trap density;
- a universal TAT onset field;
- that TAT dominates every HgCdTe detector;
- a complete speed–dark-current frontier;
- novelty of the algebraic crossover.

---

## 11. Next step

The material problem is now experimentally well posed.

For any candidate fast HgCdTe detector geometry, specify

1. cutoff / `E_g`;
2. collection length and field profile;
3. acceptable tunneling current density;
4. plausible trap energies.

Then the model outputs the required trap-density scale.

The remaining question is whether those trap-density / trap-energy requirements are realistic for detector-grade HgCdTe.

That should be answered from measured TAT fits and defect studies—not by assigning an arbitrary `N_T`.