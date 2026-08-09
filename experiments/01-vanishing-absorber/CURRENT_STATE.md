# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is self-consistent graded HgCdTe plus collection-boundary TAT/BTBT/defect allocation; no novelty claim

## 1. Current question

The original active-volume idea has been falsified. The project has progressively moved through optical confinement, microscopic transitions, passive/active network resources, and semiconductor transport.

The current question is now concrete:

> **Can a realistic graded HgCdTe detector use band-structure drive for fast minority-carrier collection while placing the unavoidable junction electrostatic field in sufficiently wide-gap, low-defect material that TAT, direct BTBT, and nonlocal impact ionization remain controlled?**

There is still **no manuscript**.

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md`
2. `HGCDTE_GRADED_POISSON_ROBUSTNESS.md`
3. `HGCDTE_LINEAR_GRADED_KANE_WKB.md`
4. `HGCDTE_BOUNDARY_LAYER_TAT_TRADEOFF.md`
5. `HGCDTE_ELECTROSTATIC_COMPENSATION_PEAK_FIELD_BOUND.md`
6. `HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`
7. `HGCDTE_TAT_FIELD_SCALE.md`
8. `HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
9. `HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md`
10. `HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md`
11. `CLAIM_LEDGER.md`
12. `RESEARCH_LOG.md`

Older optical/control branches remain important provenance but are no longer the active frontier.

## 3. Graded-Kane direct-Zener result

For a one-dimensional two-band/Kane dispersion

```math
(E-U)^2=\Delta^2+(\hbar v_K k)^2,
\qquad E_g=2\Delta,
```

and linear band edges

```math
E_c=E_{c0}-S_cx,
\qquad
E_v=E_{v0}-S_vx,
```

the direct interband WKB action is

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

The constant-gap common-field limit recovers

```math
\boxed{
\mathcal S_0
=\frac{\pi E_g^2}
{4q\hbar v_KF}.
}
```

This is a checked model-level result.

## 4. Band-offset partition cancels from the decisive geometry

Define the local gap slope

```math
G=-\frac{dE_g}{dx}>0
```

and positive downhill edge slopes

```math
S_c=-\frac{dE_c}{dx},
\qquad
S_v=-\frac{dE_v}{dx}.
```

Because `E_g=E_c-E_v`, identically

```math
\boxed{S_v=S_c-G.}
```

Thus the relative conduction/valence geometry does not depend on how the bare composition shift is partitioned between the bands.

At fixed useful conduction slope `S_c=S`, define

```math
\boxed{\delta=G/S.}
```

For the linear two-turning-point model,

```math
\boxed{
\frac{\mathcal S_Z(\delta)}
{\mathcal S_Z(0)}
=
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}},
\qquad
0\le\delta<1.
}
```

This ratio increases strictly and diverges as `delta -> 1-`.

For a finite linear region,

```math
\boxed{
\delta=\Delta E_g/\Delta E_c.
}
```

So the ideal same-direction direct-Zener geometry closes when

```math
\boxed{\Delta E_g\ge\Delta E_c.}
```

This statement does not eliminate TAT, interface tunneling, or other nonlocal processes.

## 5. Self-consistent quasi-neutral p-type interior is favorable

At equilibrium, for nondegenerate holes,

```math
p=N_v\exp[(E_v-E_F)/(k_BT)].
```

In a quasi-neutral p-type region, `p approximately N_A`, giving

```math
\boxed{
S_v
\simeq
-k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

Since

```math
S_c=S_v+G,
```

nearly constant `N_A/N_v` yields

```math
\boxed{
S_v\approx0,
\qquad
S_c\approx G,
\qquad
\delta\approx1.
}
```

Interpretation:

> **A quasi-neutral p-type graded HgCdTe interior can naturally pin the majority-hole band while leaving the composition-induced gap slope available as minority-electron conduction-band drive.**

Self-consistent electrostatics therefore does not necessarily destroy the graded escape; in the quasi-neutral interior it can reinforce the desired band geometry.

For n-type quasi-neutral material, the analogous pinning acts mainly on the conduction band and naturally favors minority-hole drive.

## 6. Uniform-depletion picture fails quickly with length

For an illustrative uniform net space charge `N_eff` over length `L`, a sufficient condition to keep the valence edge from tilting downhill anywhere is

```math
\boxed{
\Delta E_g-\Delta E_c
\ge
\frac{q^2|N_{\rm eff}|L^2}{2\epsilon}.
}
```

The `N_eff L^2` scaling becomes severe for multi-micron HgCdTe at ordinary doping.

The active physical picture is therefore

```text
quasi-neutral graded interior
+
short screening/depletion collection boundary.
```

## 7. Collection boundary: barrier-free extraction costs electrostatic voltage

Let the boundary increase the gap by

```math
\Delta E_g>0
```

and let `alpha` be the fraction of the material gap increase appearing in the conduction band.

Barrier-free minority-electron extraction requires

```math
\boxed{qV_b\ge\alpha\Delta E_g.}
```

At minimum compensation,

```math
\boxed{
\Delta E_c=0,
\qquad
\Delta E_v=-\Delta E_g.
}
```

Thus a wide-gap boundary can keep electrons barrier free while increasing valence-band separation.

Composition/doping modulation and delta-doped HgCdTe barrier structures already exploit related band-engineering ideas; the architecture itself is prior art.

## 8. Electrostatic shaping cannot make the compensation field disappear

For any one-sign compensating field over physical width `w`,

```math
V_b=\int_0^wF(x)dx.
```

Therefore

```math
\boxed{F_{\max}\ge V_b/w.}
```

At minimum barrier-free compensation,

```math
\boxed{
F_{\max}
\ge
\frac{\alpha\Delta E_g}{qw}.
}
```

Uniform field saturates this peak-field lower bound.

Delta doping or depletion shaping can redistribute the required field into better material, but cannot supply the same electrostatic voltage across width `w` with a smaller peak field than `V_b/w`.

## 9. Boundary TAT width and delay floor

Use the established local TAT exponent scale

```math
\exp(-F_{\rm TAT}/F),
```

with

```math
\boxed{
F_{\rm TAT}
=\frac{4\sqrt{2m^*}\Delta_t^{3/2}}
{3q\hbar}.
}
```

Demand a minimum exponent margin `Sigma_t` everywhere.

Then the peak-field bound gives the necessary boundary-width condition

```math
\boxed{
w
\ge
\frac{\alpha\Delta E_g}
{qF_{\rm TAT}}
\Sigma_t.
}
```

For characteristic crossing speed `v_b`,

```math
\boxed{
t_b
\ge
\frac{\alpha\Delta E_g}
{qF_{\rm TAT}v_b}
\Sigma_t.
}
```

This is not a complete TAT-current theorem because trap density, occupancy, cross section, and prefactors remain essential.

A representative 50 nm, 0.124 eV -> 0.25 eV compensated boundary gives a compensation field of order `1.7e4 V/cm`. For a trap `0.3 E_g` below the local conduction band, the simplified Kane-scaled TAT exponent is of order 10. This only demonstrates plausibility; it is not a device current prediction.

## 10. Measured defect spectra make the boundary a materials problem

HgCdTe studies report

- TAT-sensitive LWIR trap populations around `10^14 cm^-3` in some modeled devices;
- dominant damaging levels around `E_v + 0.7 E_g` in one 77 K LWIR analysis;
- DLTS-resolved electron and hole traps with capture cross sections spanning orders of magnitude in multilayer HgCdTe heterostructures;
- distinct defect signatures in wide-gap layers.

Therefore the high-field boundary cannot be characterized by one universal `Delta_t`.

The likely resource is now the **spatial defect spectrum** together with the available wide-gap band structure.

## 11. Exact exponent-level field allocation rule

Let `F_T(x)` be the local TAT characteristic field and require fixed compensation voltage

```math
V_b=\int Fdx.
```

Choose `F(x)` to maximize the worst local TAT exponent.

The exact maximin allocation is

```math
\boxed{
F_{\rm opt}(x)
=\frac{V_bF_T(x)}
{\int F_T(x')dx'}.
}
```

The optimized minimum exponent is

```math
\boxed{
\Sigma_{\rm TAT}^{\rm maximin}
=\frac{\int F_T(x)dx}{V_b}.
}
```

Thus the optimal exponent-level rule is:

> **put more of the unavoidable electric field where the local material/trap spectrum tolerates more field, equalizing normalized tunneling stress.**

A conservative generalized tolerance profile can include several mechanisms,

```math
F_{\rm tol}(x)
=\min[
F_{\rm TAT}/\Sigma_t,
F_K/\Sigma_Z,
F_{\rm II},
...].
```

Then a necessary one-dimensional feasibility condition is

```math
\boxed{V_b\le\int F_{\rm tol}(x)dx.}
```

If this fails, no electrostatic field profile can provide the required band alignment without violating at least one chosen local field ceiling.

## 12. What remains from the older field-shaping theorem

For a homogeneous material with local velocity `v(F)` and WKB leakage `g(F)`, nonuniform field alone does not beat the fixed-transit-time leakage trade in the repository model.

Heterogeneity is the real resource.

At a general transit-constrained interior optimum,

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda.
}
```

The new maximin boundary rule is the robust exponent-only limit when the full leakage prefactors are not trustworthy enough for that variational optimization.

## 13. Competing mechanisms remain active

### TAT

```math
\boxed{
F_{\rm TAT}/F_K
=\frac{16}{3\pi}(\Delta_t/E_g)^{3/2}.
}
```

### Nonlocal impact ionization

Finite-device II must be treated from carrier energy history and dead space, not a bulk onset field.

### Direct BTBT

Wide-gap material raises the direct Kane scale strongly, but local field maxima must still be checked.

### Interfaces

Abrupt composition changes can introduce reflection, interface states, dipoles, and localized high fields not captured by the smooth one-dimensional model.

## 14. Prior-art boundary

Established prior physics includes

- compositionally graded HgCdTe detectors;
- graded heterojunction no-barrier optimization;
- HgCdTe nBn/xBx barrier engineering;
- composition and doping modulation;
- delta doping for band-discontinuity control;
- graded-gap WKB/Kane analysis;
- TAT/BTBT modeling;
- DLTS defect spectroscopy;
- APD field engineering.

The internally derived formulas are currently treated as detector-facing corollaries/design inequalities with **unassessed priority and no novelty claim**.

## 15. Stopped shortcuts

Do not revive without a new explicit counterexample/assumption:

- active-volume-only universal bounds;
- direct BTBT assumed first high-field limiter;
- low-field mobility extrapolated to high-field HgCdTe;
- bulk impact-ionization onset treated as finite-device threshold;
- nonuniform field alone assumed beneficial in homogeneous material;
- pure grading assumed to eliminate all leakage;
- uniformly depleted multi-micron graded absorber assumed without Poisson check;
- delta doping treated as removing the electrostatic compensation requirement.

## 16. Current next step

Build one explicit boundary rather than adding another abstract theorem.

Use a realistic p-type graded absorber plus a wider-gap collection region:

1. choose `x_Cd(x)` / `E_g(x)`;
2. use a modern HgCdTe electron-affinity/band-offset model;
3. choose `N_A(x)` and any delta-doped sheet;
4. solve Fermi-Dirac Poisson through the boundary;
5. calculate the continuous `E_c(x), E_v(x)` profile;
6. calculate minority-electron transit;
7. calculate direct Kane WKB action;
8. calculate TAT with experimentally anchored trap energies, densities, and capture cross sections;
9. calculate nonlocal II;
10. compare the resulting field allocation with the maximin tolerance profile.

The decisive question is:

> **Does a realistic boundary retain the graded interior's transport advantage, or does the required high-field junction region recover the dark-current penalty?**

Only after this calculation should publication significance be reassessed.