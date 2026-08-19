# Claim Ledger Addendum — Semiconductor Thickness / Dark-Exposure Branch

**Date:** 2026-08-12  
**Status:** active addendum; narrow cross-layer branch retained as conditional model insight  
**Priority:** unproven; low-to-moderate novelty expectation; no novelty claim

Read together with

```text
CLAIM_LEDGER.md
CLAIM_LEDGER_PROCESS_ADDENDUM.md
CLAIM_LEDGER_PRIOR_ART_ADDENDUM.md
```

This addendum records the post-audit status of the semiconductor thickness / time-tagged dark-event branch.

---

## SD1 — useful back-collected signal probability in the minimal slab
**Status:** DERIVED / CONDITIONAL

For front illumination, opposite-side collection, Beer-Lambert absorption `alpha`, exponential survival inverse length `beta`, and prefactor `eta_0`,

```math
\eta_s(L)
=\eta_0\frac{\alpha}{\alpha-\beta}
(e^{-\beta L}-e^{-\alpha L})
```

for `alpha != beta`, with continuous limit

```math
\eta_s(L)=\eta_0\alpha L e^{-\alpha L}
```

at `alpha=beta`.

The physical absorption-versus-collection structure is classical semiconductor prior art; the formula is a minimal model, not a novelty claim.

## SD2 — fixed-gate click/no-click distinguishability
**Status:** DERIVED / CONDITIONAL

For independent bulk Poisson dark events with fixed gate `tau_g`, define

```math
\delta=r_dA\tau_g.
```

Then

```math
\mathcal D(L)=\eta_s(L)e^{-\delta L}.
```

For `alpha != beta`, the exact optimum is

```math
L_*
=\frac{\ln[(\alpha+\delta)/(\beta+\delta)]}{\alpha-\beta}.
```

This is a useful closed-form cross-layer corollary, but its ingredients are standard and novelty expectation is low.

## SD3 — fixed-gate decision-feasibility ceiling
**Status:** DERIVED / CONDITIONAL

Target equal-prior error `epsilon` is achievable by some thickness if and only if

```math
\mathcal D_{\max}\ge1-2\epsilon
```

inside the model.

This is elementary decision theory applied to the optimized device model, not a new statistical theorem.

## SD4 — transit-linked dark exposure
**Status:** DERIVED / CONDITIONAL

For gate

```math
\tau_g(L)=\tau_0+L/v,
```

the dark mean contains

```math
\mu_d(L)=\delta_1L+\zeta L^2,
```

with

```math
\delta_1=r_dA\tau_0,
\qquad
\zeta=r_dA/v.
```

The unique optimum for `alpha != beta` satisfies

```math
\frac{\alpha-\beta}
{e^{(\alpha-\beta)L_*}-1}
=\beta+\delta_1+2\zeta L_*.
```

Within this model, adding the transit-linked dark term shifts the optimum thinner than the otherwise identical fixed-gate case.

## SD5 — strong bulk-dark/transit asymptote
**Status:** DERIVED / CONDITIONAL

In the thin strong-dark regime,

```math
L_*
\sim
\sqrt{\frac{v}{2r_dA}},
```

and

```math
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{\frac{v}{2e\,r_dA}}.
```

Thus a target `D_req=1-2epsilon` approximately requires

```math
\frac{r_dA}{v}
\lesssim
\frac{\eta_0^2\alpha^2}
{2eD_{\rm req}^2}.
```

This is the strongest narrow cross-layer scaling in the branch, but it is not classified as novel.

## SD6 — full time-tagged point-process likelihood
**Status:** DERIVED / STANDARD POINT-PROCESS STRUCTURE

With detected signal time density `q_L(t)` and dark intensity `lambda_0(t)`,

```math
\Lambda(Y)
=1-\eta_s(L)
+
\sum_{t_i\in Y}
\frac{q_L(t_i)}{\lambda_0(t_i)}.
```

Poisson point-process likelihood theory is established; no novelty claim is permitted for the statistical form.

## SD7 — full-output total-variation factorization
**Status:** DERIVED / CONDITIONAL

For

```math
P_1=(1-\eta_s)P_0+\eta_sQ,
```

```math
\mathcal D_{\rm full}(L)
=\eta_s(L)\operatorname{TV}(Q,P_0).
```

This separates physical useful-event probability from the statistical distinguishability of an added event against dark background.

## SD8 — shifted-Poisson special case
**Status:** DERIVED / CONDITIONAL

When signal and dark timestamp shapes coincide, the count problem reduces to

```text
Poisson(mu)
versus
1 + Poisson(mu),
```

with

```math
\operatorname{TV}
=p_{\max}(\mu),
```

where `p_max` is the maximum Poisson pmf.

For `mu<1`,

```math
p_{\max}=e^{-\mu},
```

so binary any-click/no-click readout is already sufficient for the total-variation decision in that special regime.

## SD9 — strong-dark scaling survives full timestamp/count readout
**Status:** DERIVED ROBUSTNESS RESULT / CONDITIONAL

In the strong-dark thin limit, the optimum lies at

```math
\mu_*=1/2<1,
```

so full timestamp/count processing gives the same leading optimum and

```math
\mathcal D_{\max}^{\rm full}
\sim
\eta_0\alpha
\sqrt{\frac{v}{2e\,r_dA}}.
```

Thus the leading bulk-transit asymptote is not an artifact of binary click/no-click coarse graining.

## SD10 — `mu_*=1/2` is not universal
**Status:** INVALIDATED AS A UNIVERSAL CONSTANT / SUPERSEDED BY SCALING CLASS

If thin useful signal scales as

```math
\eta_s\sim SL^s
```

and mean dark exposure as

```math
\mu\sim KL^p,
```

then in the first Poisson-mode interval

```math
L_*
\sim
\left(\frac{s}{pK}\right)^{1/p},
```

```math
\mu_*=s/p,
```

and

```math
\mathcal D_{\max}
\sim
S\left(\frac{s}{epK}\right)^{s/p}.
```

For ordinary thin absorption `s=1`,

```math
\mu_*=1/p.
```

The bulk + transit model has `p=2`; surface + transit or bulk + fixed gate can have `p=1`.

## SD11 — dark mechanism and timing architecture define scaling class
**Status:** DERIVED ORGANIZING STATEMENT

The exponent `p` is the sum of the thickness scaling of dark-event rate and observation time in the asymptotic model.

Therefore the strong-dark geometry law is mechanism/architecture dependent rather than universal.

## SD12 — collection-weighting the bulk dark carriers preserves the p=2 thin class
**Status:** DERIVED PHYSICAL ROBUSTNESS RESULT / CONDITIONAL

If dark-generated carriers obey the same survival law as signal carriers,

```math
\lambda_d^{\rm col}(L)
=\frac{r_dA}{\beta}(1-e^{-\beta L}),
```

so

```math
\mu_d^{\rm col}(L)
=\frac{r_dA}{v}L^2+O(L^3)
```

with transit gate `L/v`.

Thus the leading `p=2` strong-dark class survives a more physically consistent dark-collection model.

## SD13 — broad novelty disposition
**Status:** NO NOVELTY CLAIM

Established lineages already cover:

```text
absorption-depth / collection-length tradeoffs;
finite optimum semiconductor thickness;
Poisson point-process signal detection;
SPAD/photodiode efficiency-dark-count-area optimization;
optimum filtering / event-energy decision theory.
```

The current semiconductor branch is therefore treated as

```text
rigorous Gedanken-model synthesis + robust asymptotic scaling
```

rather than a new fundamental photodetector law.

## SD14 — possible path to stronger scientific value
**Status:** OPEN

The branch would become materially stronger only if a realistic detector specialization shows that the scaling or feasibility boundary survives:

```text
real drift-diffusion/depletion transport;
real dark-current mechanism;
field-dependent carrier velocity/lifetime;
timing jitter;
real readout threshold/noise;
and actual device geometry.
```

A natural next test is one physically defensible real architecture rather than further abstract algebra.
