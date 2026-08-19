# Semiconductor Thickness Branch — Current Disposition

**Date:** 2026-08-12  
**Status:** branch closed as primary novelty route; retain as conceptual/modeling result  
**Priority:** no novelty claim

This file records the current disposition of the semiconductor thickness / dark-exposure branch after derivation, stronger-observer tests, physical refinements, device-architecture stress, and prior-art audit.

## 1. What survived

A useful reduced scaling framework survived:

```math
\eta_s(L)\sim S L^s,
\qquad
\mu_d(L)\sim K L^p,
```

with leading objective

```math
\mathcal D(L)\sim S L^s e^{-K L^p}.
```

In the first Poisson-mode regime,

```math
L_*
\sim
\left(\frac{s}{pK}\right)^{1/p},
```

```math
\mu_*=s/p,
```

```math
\mathcal D_{\max}
\sim
S\left(\frac{s}{epK}\right)^{s/p}.
```

This provides a compact way to classify how useful-signal growth competes with geometry/timing-dependent dark exposure.

The bulk-dark + transit-gate case is the conditional specialization

```math
s=1,
\qquad
p=2,
\qquad
K=r_dA/v,
```

which gives

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

## 2. Robustness tests it passed

The leading `p=2` class survived:

```text
full timestamp/count processing rather than binary click/no-click;
collection-weighting of bulk dark-generated carriers;
explicit point-process likelihood treatment;
finite collection survival in the thin asymptotic limit.
```

Thus the scaling was not merely an artifact of the first coarse readout model.

## 3. What did not survive

The numerical statement

```math
\mu_*=1/2
```

is not universal.

It is only the `s=1,p=2` member of the general class

```math
\mu_*=s/p.
```

Changing the dark mechanism or timing architecture changes `p`.

A realistic separate-absorption/multiplication detector stress also showed that

```text
collection can be field engineered rather than exponential far-contact survival;
dominant dark counts need not scale with absorber volume;
observation time need not scale as L/v;
multiple thickness-independent, linear, and quadratic dark/time terms can coexist.
```

Therefore the pure square-root law is **not a generic SPAD/APD law**.

## 4. More realistic mixed reduced model

For thin useful signal

```math
\eta_s\sim SL,
```

with

```math
\lambda_d(L)=\lambda_0+\lambda_1L,
```

and

```math
T(L)=T_0+L/v,
```

the dark mean becomes

```math
\mu_d(L)
=\mu_0+K_1L+K_2L^2,
```

where

```math
\mu_0=\lambda_0T_0,
```

```math
K_1=\lambda_0/v+\lambda_1T_0,
```

```math
K_2=\lambda_1/v.
```

The thin-model optimum is

```math
\boxed{
L_*
=\frac{2}
{K_1+\sqrt{K_1^2+8K_2}}.
}
```

This interpolates continuously between linear-penalty and quadratic-penalty regimes.

The dimensionless crossover

```math
\chi=K_2/K_1^2
```

is a more honest architecture descriptor than assuming one exponent in advance.

## 5. Prior-art boundary

Direct audits found strong prior-art overlap for the underlying ingredients:

```text
absorption-depth versus carrier-collection tradeoffs;
finite optimum semiconductor absorber thickness;
SPAD/photodiode PDE-dark-count-area tradeoffs;
Poisson point-process signal detection;
matched filtering and event-energy resolution;
device-geometry optimization.
```

The reduced scaling formulas are mathematically elementary enough that absence of an identical closed form would not establish novelty.

## 6. Scientific value retained

The branch gives a rigorous answer to one version of the original atom-count intuition:

> **Adding more detector matter need not improve detection. Additional thickness can simultaneously increase optical capture, carrier path length, dark-active material, observation time, and search/noise exposure. Which effect wins is architecture dependent.**

The useful abstraction is therefore

```text
how the complete detector channel scales when matter is added,
```

not

```text
how many atoms are present.
```

This remains a strong conceptual result even though it is not presently a novel device theorem.

## 7. Branch disposition

**CLOSE as the primary novelty route.**

Retain all derivations and audits because they document:

```text
why the initial thickness law looked promising;
which stronger observers/refinements it survived;
which architecture assumptions ultimately limited its generality;
why prior art blocks a broad novelty claim.
```

Do not add arbitrary real-device parameter values merely to make the branch look more concrete.

Reopen only if a specific physical device mechanism produces a genuinely nontrivial constraint not reducible to standard device optimization.

## 8. Return to the central Gedanken question

With the semiconductor route closed as a novelty path, return to:

> **After absorption, atom count, bands, carrier generation, amplification, scalar detectivity, thermodynamic cost, and geometry have all failed as universal detector boundaries, what property is left that is actually necessary for matter to function as a detector?**

The strongest surviving candidate remains **accessible correlation between the optical input and a persistent output process under a declared set of allowed operations/resources**.

The next step should attack whether even `persistent material record` is necessary, or whether a system can function operationally as a detector by transiently routing information directly into an external output without retaining any local memory at all.
