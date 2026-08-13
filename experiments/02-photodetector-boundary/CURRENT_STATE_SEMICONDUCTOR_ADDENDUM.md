# Current State Addendum — Semiconductor Dark-Exposure Branch

**Date:** 2026-08-12  
**Status:** live narrow branch; robust conditional scaling, no novelty claim  
**Priority:** unproven; broad framework and obvious device-optimization novelty routes already narrowed by prior art

This addendum updates only the semiconductor thickness/dark-event branch. Read it together with `CURRENT_STATE_LIVE.md`, `CLAIM_LEDGER_SEMICONDUCTOR_ADDENDUM.md`, and the prior-art audit files. It does not supersede unrelated Experiment-02 results.

## 1. Strongest current narrow result

For a thin detector whose useful signal probability scales as

```math
\eta_s(L)\sim S L^s
```

and whose mean dark exposure over the permitted observation interval scales as

```math
\mu_d(L)\sim K L^p,
```

the leading binary/uniform-point-process distinguishability has the form

```math
\mathcal D(L)\sim S L^s e^{-K L^p}.
```

In the first Poisson-mode interval the optimum is

```math
\boxed{
L_*
\sim
\left(\frac{s}{pK}\right)^{1/p},
}
```

```math
\boxed{\mu_*=s/p,}
```

and

```math
\boxed{
\mathcal D_{\max}
\sim
S\left(\frac{s}{epK}\right)^{s/p}.
}
```

Thus the previously observed `mu_*=1/2` is **not universal**; it is the `s=1,p=2` member of a scaling family.

## 2. Bulk-dark + transit-gate class

For ordinary thin single-pass absorption,

```math
s=1,
\qquad
S=\eta_0\alpha.
```

If detected bulk dark-event rate is locally proportional to thickness and the observation time is transit linked,

```math
T(L)\sim L/v,
```

then

```math
p=2,
\qquad
K=r_dA/v.
```

Hence

```math
\boxed{
L_*
\sim
\sqrt{\frac{v}{2r_dA}},
}
```

```math
\boxed{\mu_*=1/2,}
```

and

```math
\boxed{
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{\frac{v}{2e\,r_dA}}.
}
```

For required equal-prior distinguishability `D_req=1-2epsilon`, the asymptotic feasibility condition is

```math
\boxed{
\frac{r_dA}{v}
\lesssim
\frac{\eta_0^2\alpha^2}
{2eD_{\rm req}^2}.
}
```

This is conditional on the stated asymptotic model.

## 3. Robustness tests already passed

### Full timestamp/count readout

The complete point-process likelihood is

```math
\Lambda(Y)
=1-\eta_s(L)
+
\sum_{t_i\in Y}
\frac{q_L(t_i)}{\lambda_0(t_i)}.
```

In the strong-dark thin limit, the signal and dark time shapes become equal to leading order and the problem reduces to a shifted-Poisson count test. The `p=2` optimum lies at `mu=1/2<1`, where binary any-click/no-click coarse graining is already sufficient for total-variation discrimination. Therefore the leading square-root scaling survives access to the full timestamp/count record.

### Collection-weighted dark carriers

If thermally generated dark carriers obey the same exponential collection survival as photo-carriers,

```math
\lambda_d^{\rm col}(L)
=\frac{r_dA}{\beta}(1-e^{-\beta L}),
```

then

```math
\mu_d^{\rm col}(L)
=\frac{r_dA}{v}L^2+O(L^3)
```

under transit-linked gating. Thus the same leading `p=2` class survives.

## 4. Mechanism dependence is mandatory

The scaling class changes if the dark mechanism or timing architecture changes.

Examples for thin absorption `s=1`:

```text
bulk dark rate ~ L + transit gate ~ L  -> p=2 -> mu*=1/2
surface dark rate ~ constant + transit gate ~ L -> p=1 -> mu*=1
bulk dark rate ~ L + fixed gate -> p=1 -> mu*=1
```

Therefore no universal `half-dark-count` detector constant is claimed.

## 5. Prior-art disposition

The following are already established physical/statistical lineages:

```text
Beer-Lambert absorption;
generation-depth-dependent carrier collection;
finite optimum absorber thickness;
SPAD/photodiode efficiency-dark-count-area tradeoffs;
Poisson point-process likelihood detection;
matched filtering / event-energy sensitivity;
statistical experiment/channel comparison.
```

The present scaling laws are therefore classified as

```text
DERIVED / CONDITIONAL / ROBUST WITHIN THE STATED ASYMPTOTIC CLASS / PRIORITY UNPROVEN.
```

Their value at present is explanatory and as a candidate reduced design law, not as a fundamental novelty claim.

## 6. Current scientific frontier

Do not further elaborate the abstract scaling without a real device model.

The next test is one physically defensible detector architecture with measured/literature-grounded values and mechanisms for

```text
absorption coefficient / optical mode;
carrier transport / collection time;
dominant dark-event mechanism and geometry scaling;
active area;
timing/readout decision process.
```

A SPAD/APD-like architecture is the cleanest validation target for the discrete-event model. HgCdTe should only be used if its actual operating architecture supports the same event/count assumptions; otherwise its continuous-readout case should be treated separately.

If the scaling collapses to ordinary device optimization under a realistic model, close this branch as conceptual synthesis rather than force a publication result.
