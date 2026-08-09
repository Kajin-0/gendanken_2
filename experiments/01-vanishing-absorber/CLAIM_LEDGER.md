# Claim Ledger — Experiment 01

**Updated:** 2026-08-09  
**Status:** exploratory; current frontier is graded-band HgCdTe transport versus Zener/TAT/nonlocal II; no novelty claim

This file defines the epistemic boundary. `RESEARCH_LOG.md` preserves chronology and superseded branches.

## Status vocabulary

- **KNOWN** — established external result used as input.
- **DERIVED** — exact consequence of stated repository assumptions.
- **CHECKED** — independently/numerically verified.
- **CONDITIONAL** — exact only inside a deliberately simplified model.
- **INVALIDATED** — explicit counterexample or correction found.
- **OPEN** — unresolved.
- **NON-CLAIM** — explicitly not asserted.

## 1. Permanent invalidations / stopped universal routes

### H1 — active-volume-only universal detector limit — INVALIDATED

Ideal field concentration permits finite optical participation while `V_a -> 0`.

### H2 — finite absorber count as one-photon speed limit — INVALIDATED

The one-photon / one-excitation sector remains linear.

### H3 — finite internal storage rank as universal always-on detector capacity — INVALIDATED

Adaptive branching and unrestricted output continua export the missing distinguishability.

### H4 — local Landauer erasure as universal detector cost — INVALIDATED

Useful output can carry the record information.

### H5 — one-Lorentzian leakage law or spectral FWHM as universal electronic speed — INVALIDATED

Higher-order filters trade spectral rejection against delay/state count.

### H6 — low-field `v=mu F` extrapolation as high-field HgCdTe speed law — INVALIDATED

Primary HgCdTe transport is strongly non-ohmic at high field.

### H7 — direct BTBT automatically first high-field limiter in ordinary LWIR — INVALIDATED AS WORKING HYPOTHESIS

TAT, nonlocal II, and transport nonlinearity intervene on distinct and often earlier scales.

### H8 — bulk `~100 V/cm` II onset equals finite-device II threshold — INVALIDATED INTERPRETATION

Finite-device II depends on dead space and carrier energy history.

### H9 — nonuniform field alone improves homogeneous speed–tunneling tradeoff — INVALIDATED WITHIN LOCAL MODEL

For the stated homogeneous transport/leakage family, uniform field is the unique minimizer at fixed transit time.

## 2. Retained passive-network theorem

For a finite stable passive strictly proper network,

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

**Status:** DERIVED / CHECKED; standard `H_2`/Lyapunov ingredients; exact priority unassessed; not the active material frontier.

## 3. HgCdTe direct-BTBT normalization

Using the published uniform-field HgCdTe form plus the simplified Kane mass relation:

```math
\boxed{
J_{\rm BTBT}
=\frac{q^3L}{4\pi^3\hbar^2v_K}
F^2e^{-F_K/F},
}
```

```math
\boxed{
F_K
=\frac{\pi E_g^2}{4q\hbar v_K}
=\frac{\pi^3\hbar c^2}{qv_K\lambda_c^2},
}
```

```math
\boxed{
J_K
=\frac{q\pi^3c^4L}{4v_K^3\lambda_c^4}.
}
```

With `x=F/F_K`, `j=J/J_K`:

```math
\boxed{j=x^2e^{-1/x}.}
```

**Status:** DERIVED / CHECKED / CONDITIONAL. Scaling model only.

## 4. Finite impact-ionization scales

For `E_th=chi E_g`, cold field-work threshold:

```math
\boxed{F_{\rm dead}\simeq\chi E_g/(qL).}
```

Kane relation:

```math
\boxed{
F_{\rm dead}/F_K
=(4\chi/\pi)(\ell_K/L),
\qquad
\ell_K=\hbar v_K/E_g.
}
```

With one energy-relaxation time,

```math
\boxed{
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E}),
}
```

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=\Delta E_{\rm th}/(qL_{\rm eff}).
}
```

**Status:** DERIVED / CONDITIONAL. Mean trajectory is not the stochastic high-energy tail.

For the analytic `alpha=1,beta=0` II-rate test case, the repository has a closed nonlocal hazard and

```math
\boxed{P_{\rm II}=1-e^{-\Xi_{\rm II}}.}
```

**Status:** DERIVED / CHECKED / CONDITIONAL.

Target `x=0.20`, 77 K `ell_E(F)` and `Gamma_II(E)` calibration remain OPEN.

## 5. Relaxation-length phase boundary

Let `F_J` be the direct-BTBT field for a chosen current budget and

```math
r=F_{\rm dead}/F_J.
```

The mean-II/BTBT boundary obeys

```math
\boxed{
\frac{1-e^{-y_*}}{y_*}=r,
\qquad
y_*=L/\ell_{E,*}.
}
```

For `0<r<1`,

```math
\boxed{
y_*
=\frac1r+W_0[-r^{-1}e^{-1/r}],}
```

```math
\boxed{\ell_{E,*}=L/y_*.}
```

**Status:** DERIVED / CHECKED / CONDITIONAL. One-sided evidence only because stochastic II can occur below mean threshold.

## 6. Trap-assisted tunneling scale

For trap depth

```math
\Delta_t=E_g-E_T,
```

simple TAT exponent field:

```math
\boxed{
F_{\rm TAT}
=\frac{4\sqrt{2m^*}\Delta_t^{3/2}}
{3q\hbar}.
}
```

Relative to direct BTBT:

```math
\boxed{
\frac{F_{\rm TAT}}{F_K}
=\frac{16}{3\pi}
(\Delta_t/E_g)^{3/2}.
}
```

**Status:** DERIVED from standard simplified TAT/BTBT exponents; no universal trap depth/prefactor.

Within the shared simplified current models,

```math
\boxed{
N_{T,\times}
=\frac{2\sqrt2q\hbar\Delta_tF}
{\pi^2\kappa_d^2\sqrt{m^*E_g}}
\exp[-(F_K-F_T)/F].
}
```

**Status:** DERIVED / CONDITIONAL.

Real HgCdTe studies report technologically relevant TAT with trap densities around `10^13–10^14 cm^-3` in some LWIR devices. Those are external device-specific benchmarks, not universal values.

## 7. Homogeneous field-profile theorem

For

```math
v(F)=\mu F/[1+(F/d)^r],
\qquad r>1,
```

and

```math
g(F)=AF^pe^{-K/F},
\qquad p>0,
```

local leakage is strictly convex as a function of reciprocal velocity over the entire rising-velocity branch; the falling branch is dominated.

Hence, at fixed transit time,

```math
\boxed{
G[F]\ge Lg(F_0),
}
```

where `F_0` is uniform and satisfies `v(F_0)=L/T`.

**Status:** DERIVED / CHECKED. Standard convexity/Jensen mathematics; local homogeneous model only.

## 8. Heterogeneous marginal field allocation

For spatially varying local laws,

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda
}
```

at an interior transit-constrained optimum.

For ohmic WKB regions,

```math
\boxed{
\mathcal M_i
=\mu_iA_iF_i^{p+1}e^{-K_i/F_i}
(p+K_i/F_i).
}
```

**Status:** DERIVED. Standard constrained optimization.

The repository two-region example reduces modeled leakage by about `20.6%` at fixed transit time while requiring about `2.2%` extra voltage.

## 9. Voltage–transit inequality

For ohmic spatial transport,

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
\boxed{F(x)\propto\mu(x)^{-1/2}.}
```

For two equal-length/equal-mobility regions at bias ratio `beta=V/V_min`,

```math
\boxed{s=\sqrt{1-1/\beta},}
```

```math
\boxed{F_{\rm low,high}=F_{\rm bar}/(1\pm s).}
```

**Status:** DERIVED. Standard Cauchy mathematics.

## 10. Linear graded-gap Kane WKB result — current strongest new model-level corollary

Use

```math
(E-U)^2=\Delta^2+(\hbar v_Kk)^2,
```

with linear edges

```math
E_c=E_{c0}-S_cx,
\qquad
E_v=E_{v0}-S_vx.
```

For `S_c,S_v>0`, the exact WKB action is

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

Constant gap/common slope recovers

```math
\boxed{
\mathcal S_0
=\frac{\pi E_g^2}{4q\hbar v_KF}.
}
```

Decompose

```math
S_c=S_U+S_\Delta,
\qquad
S_v=S_U-S_\Delta.
```

Hold useful conduction slope `S_c=S` fixed and define

```math
\eta=S_\Delta/S.
```

For `0<=eta<1/2`,

```math
\boxed{
\frac{\mathcal S_Z(\eta)}
{\mathcal S_Z(0)}
=
\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}.
}
```

It is strictly increasing:

```math
\boxed{
\frac{d\ln R}{d\eta}
=\frac{1+\eta}
{(1-\eta)(1-2\eta)}>0.
}
```

As `eta -> 1/2-`, the valence turning point recedes and the action diverges.

For `eta>=1/2`, if the finite graded region remains positive-gap and ends before gap closure, the conventional same-energy two-turning-point direct-Zener path is absent inside this ideal model.

**Status:** DERIVED / CHECKED / CONDITIONAL.

**Priority:** graded-gap HgCdTe, WKB and Kane/Zener are established. The exact fixed-conduction-slope ratio was not found in the inspected focused search. That negative search is not proof of novelty. Current label: **exact internally derived linear-profile WKB corollary; priority unassessed.**

## 11. Grading resource requirement

In the symmetric two-band picture,

```math
S_\Delta L=\Delta E_g/2.
```

Therefore

```math
\boxed{\Delta E_g=2\eta SL.}
```

Composition grading exchanges electrostatic/common-mode drive for finite bandgap/band-offset range; it is not free acceleration.

## 12. OPEN questions now

### O1

Real HgCdTe conduction/valence band-offset partition versus composition in the target grading range.

### O2

Self-consistent `U(x)` generated by doping, fixed charge and carrier redistribution in a graded structure.

### O3

Full finite-profile direct WKB current after integrating over tunneling energy and transverse states.

### O4

TAT in the graded profile with spatially varying trap energy/density.

### O5

Nonlocal impact-ionization probability in the same profile.

### O6

Whether the exact graded-action corollary has prior mathematical/device literature under another notation.

## 13. Explicit non-claims

Do **not** claim

- a universal photodetector limit;
- a universal HgCdTe speed-dark-current theorem;
- zero tunneling in a real graded detector;
- that real grading has `U'=0`;
- that TAT or II are eliminated by grading;
- that the exact WKB ratio is novel;
- readiness for a manuscript.

## 14. Promotion criterion

The graded-action result becomes publication-relevant only if it survives

1. realistic HgCdTe band-offset partition;
2. finite positive-gap endpoints;
3. self-consistent Poisson electrostatics;
4. TAT/interface-state attack;
5. nonlocal impact-ionization attack;
6. deeper prior-art collision.
