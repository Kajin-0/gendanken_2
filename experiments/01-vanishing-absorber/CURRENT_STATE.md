# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is graded-band HgCdTe transport versus direct Zener/TAT/nonlocal II; no novelty claim

## 1. Current question

The original active-volume idea has been falsified. After optical, quantum, control, and semiconductor counterexamples, the project has reached a concrete materials question:

> **Can HgCdTe band-structure engineering supply fast carrier collection without paying the same tunneling penalty as a homogeneous electrostatic field?**

The answer is now partly yes in an idealized two-band model, but the real device must still survive TAT, nonlocal impact ionization, band offsets, and self-consistent electrostatics.

There is still **no manuscript**.

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_LINEAR_GRADED_KANE_WKB.md`
2. `HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md`
3. `HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md`
4. `HGCDTE_TWO_REGION_FIELD_ALLOCATION.md`
5. `HGCDTE_VOLTAGE_TRANSIT_FIELD_ALLOCATION.md`
6. `HGCDTE_TAT_FIELD_SCALE.md`
7. `HGCDTE_TAT_BTBT_CROSSOVER.md`
8. `HGCDTE_RELAXATION_LENGTH_PHASE_BOUNDARY.md`
9. `HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
10. `HGCDTE_IMPACT_IONIZATION_DEAD_SPACE.md`
11. `HGCDTE_NORMALIZED_BTBT_FRONTIER.md`
12. `CLAIM_LEDGER.md`
13. `RESEARCH_LOG.md`

## 3. Homogeneous field shaping is closed in the local model

For homogeneous transport

```math
v(F)=\frac{\mu F}{1+(F/d)^r},
\qquad r>1,
```

and local WKB leakage

```math
g(F)=A F^p e^{-K/F},
\qquad p>0,
```

the leakage is strictly convex as a function of reciprocal velocity on the entire rising-velocity branch.

Fields above the velocity maximum are dominated because they give lower/equal speed and higher leakage.

Therefore, for fixed transit time

```math
T=\int_0^L\frac{dx}{v[F(x)]},
```

```math
\boxed{
G[F]\equiv\int_0^L g[F(x)]dx
\ge Lg(F_0),
}
```

where `F_0` is the unique uniform rising-branch field satisfying

```math
v(F_0)=L/T.
```

Thus **field shaping alone cannot beat the speed–local-tunneling tradeoff in one homogeneous material under the stated local model.**

## 4. Heterogeneity is the real escape

For spatially varying material parameters, the interior optimum obeys

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda.
}
```

The field should be allocated until each region has the same marginal leakage cost per marginal reduction in transit time.

For two ohmic WKB regions,

```math
\boxed{
\mathcal M_i(F)
=\mu_iA_iF^{p+1}
 e^{-K_i/F}
(p+K_i/F).
}
```

A larger tunneling barrier or lower leakage prefactor can rationally receive more field.

The dimensionless two-region example in the repo lowers modeled tunneling exposure by about `20.6%` while using only about `2.2%` additional voltage at fixed transit time.

## 5. Voltage is an independent resource

For ohmic spatial transport,

```math
V=\int Fdx,
\qquad
T=\int\frac{dx}{\mu(x)F(x)},
```

Cauchy-Schwarz gives

```math
\boxed{
VT
\ge
\left[
\int_0^L\frac{dx}{\sqrt{\mu(x)}}
\right]^2.
}
```

Equality requires

```math
\boxed{
F(x)\propto\mu(x)^{-1/2}.
}
```

Therefore leakage-protecting field redistribution generally consumes extra bias above the kinematic minimum.

For two equal-length/equal-mobility regions, if

```math
\beta=V/V_{\min}\ge1,
```

then the exact allowed field contrast at fixed transit time is

```math
\boxed{
s=\sqrt{1-1/\beta},}
```

```math
\boxed{
F_{\rm low,high}
=F_{\rm bar}/(1\pm s).
}
```

## 6. Composition grading changes the Hamiltonian, not just `F(x)`

Use the idealized two-band/Kane landscape

```math
H=U(x)I+v_Kp\sigma_x+\Delta(x)\sigma_z,
```

with

```math
E_c=U+\Delta,
\qquad
E_v=U-\Delta,
\qquad
E_g=2\Delta.
```

A common-mode slope `U'` and a gap slope `Delta'` both affect the conduction-band force, but they move the valence edge differently.

This is the core reason grading can escape the homogeneous-field theorem.

## 7. Exact linear graded-gap WKB result

For linear edges

```math
E_c(x)=E_{c0}-S_cx,
```

```math
E_v(x)=E_{v0}-S_vx,
```

with `S_c,S_v>0`, the forbidden wavevector is

```math
\kappa(x)
=\frac{\sqrt{[E_c-E][E-E_v]}}
{\hbar v_K}.
```

The WKB action integrates exactly:

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}
(x_c-x_v)^2.
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

Thus the normalized direct-BTBT Kane exponent used earlier is recovered exactly.

## 8. Fixed transport slope: grading strictly suppresses the direct linear Zener path

Decompose

```math
S_c=S_U+S_\Delta,
```

```math
S_v=S_U-S_\Delta.
```

Hold the useful conduction slope fixed at

```math
S_c=S
```

and define

```math
\eta=S_\Delta/S.
```

Then

```math
S_U=(1-\eta)S,
```

```math
S_v=(1-2\eta)S.
```

For

```math
0\le\eta<1/2,
```

the exact action ratio is

```math
\boxed{
\frac{\mathcal S_Z(\eta)}
{\mathcal S_Z(0)}
=
\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}.
}
```

Its derivative is strictly positive:

```math
\boxed{
\frac{d\ln R}{d\eta}
=\frac{1+\eta}
{(1-\eta)(1-2\eta)}>0.
}
```

Therefore any positive grading contribution increases the direct-Zener WKB action at the same conduction-band downhill slope.

As

```math
\eta\to1/2^{-},
```

the valence turning point recedes and the action diverges.

For

```math
\eta\ge1/2,
```

the valence edge is flat or tilts in the opposite direction; if the finite graded region remains positive-gap and terminates before gap closure, the conventional same-energy two-turning-point direct-Zener path is absent inside this ideal model.

This does **not** eliminate TAT, interface tunneling, phonon-assisted processes, or electrostatic tilt generated self-consistently by charge.

## 9. Grading consumes finite band-structure resource

In the symmetric two-band picture,

```math
S_\Delta L=\Delta E_g/2.
```

Thus supplying fraction `eta` of conduction slope `S` by grading requires

```math
\boxed{
\Delta E_g
=2\eta SL.
}
```

The `eta=1/2` point therefore requires a total gap change equal to the conduction-band driving energy drop `SL`.

Composition grading trades electrical-field resource for finite band-edge/gap-profile resource; it is not free acceleration.

## 10. HgCdTe experiments make the escape physically relevant

Established HgCdTe work reports composition-gradient built-in/quasi-electric fields that materially affect minority-carrier transport. Primary studies report fields of order `100–200 V/cm` for linear gradients in measured structures and much larger local values for nonlinear grading.

A graded-band uncooled MWIR HgCdTe detector has been reported with roughly `1.33 ns` total response time (`750 MHz`) at zero bias, and newer graded-composition APD structures explicitly use wide-gap gradients and built-in fields to guide carriers while controlling dark current.

These are not tests of the exact WKB slope-ratio formula.

## 11. Competing leakage mechanisms remain active

### TAT

For a trap a depth

```math
\Delta_t=E_g-E_T
```

below the conduction band,

```math
\boxed{
\frac{F_{\rm TAT}}{F_K}
=\frac{16}{3\pi}
(\Delta_t/E_g)^{3/2}.
}
```

Near-band-edge traps can therefore open a tunneling path at a much smaller exponent scale than direct BTBT.

Real LWIR HgCdTe studies report technologically relevant trap densities around `10^13–10^14 cm^-3` in some devices.

### Nonlocal II

For cold injection,

```math
\boxed{
F_{\rm dead}\simeq\chi E_g/(qL),
}
```

and

```math
\boxed{
F_{\rm dead}/F_K
=(4\chi/\pi)(\ell_K/L).
}
```

With energy relaxation,

```math
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}),
```

and

```math
F_{\rm th}^{(\rm mean)}
=\Delta E_{\rm th}/(qL_{\rm eff}).
```

The target `x=0.20`, 77 K calibration of `ell_E(F)` and `Gamma_II(E)` remains incomplete.

## 12. Prior-art / novelty boundary

Known prior physics includes

- graded-band HgCdTe detectors;
- WKB analysis of graded HgCdTe;
- classic Kane/Zener tunneling;
- analytical graded heterojunction band profiles;
- field engineering in HgCdTe APDs.

A focused search did not locate the exact fixed-conduction-slope ratio

```math
(1-\eta)^2/(1-2\eta)^{3/2}.
```

That is only a negative search result.

Current status:

> **exact internally derived linear-profile WKB corollary; priority unassessed; no novelty claim.**

## 13. Numerical checks

Current relevant regressions:

```text
numerics/hgcdte_field_profile_variational.py
numerics/hgcdte_graded_kane_wkb.py
numerics/hgcdte_btbt_normalized_sweep.py
numerics/hgcdte_field_regime_map.py
numerics/hgcdte_impact_dead_space.py
numerics/hgcdte_nonlocal_ii_surrogate.py
numerics/hgcdte_relaxation_length_phase_boundary.py
```

The graded-WKB regression integrates the forbidden wavevector directly and reproduces the closed action.

## 14. Current next step

Do **not** return to uniform-field device estimates.

The next decisive model is a finite, self-consistent graded HgCdTe energy landscape:

1. specify `E_g(x)` / composition;
2. specify realistic conduction/valence band-offset partition;
3. solve Poisson for `U(x)` under doping and bias;
4. calculate carrier transit from the resulting `E_c(x)`;
5. evaluate direct interband WKB action from the full `E_c/E_v` profile;
6. evaluate TAT and nonlocal II as competing escape channels.

Only after this attack should the graded-action corollary be reassessed for publication significance.