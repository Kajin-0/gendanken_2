# HgCdTe Ballistic Grading Span Rule — A Simple Cutoff-Ratio Corollary of the Nonlocal II Boundary

**Date:** 2026-08-09  
**Status:** exact ballistic-limit corollary of `HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`; conditional mean-energy result; no novelty claim

## 1. Starting point

For a linear quasi-neutral p-type graded absorber, the repository mean-energy phase boundary is

```math
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r},
```

with

```math
\zeta=\frac{E_{g,\rm in}-E_{g,\rm out}}
{E_{g,\rm in}},
```

and

```math
r=L/\ell_E.
```

In the ballistic limit

```math
r\to0,
```

```math
\boxed{
\zeta_{\rm II}^{(\rm bal)}
=\frac{\chi}{1+\chi}.
}
```

## 2. Gap-ratio form

Mean-threshold-safe ballistic grading requires

```math
\zeta
\le
\frac{\chi}{1+\chi}.
```

Since

```math
1-\zeta
=\frac{E_{g,\rm out}}{E_{g,\rm in}},
```

this becomes

```math
\boxed{
\frac{E_{g,\rm out}}{E_{g,\rm in}}
\ge
\frac{1}{1+\chi}.
}
```

Equivalently,

```math
\boxed{
\frac{E_{g,\rm in}}{E_{g,\rm out}}
\le
1+\chi.
}
```

For the common simplified threshold choice `chi=1`,

```math
\boxed{
E_{g,\rm in}
\le
2E_{g,\rm out}.
}
```

## 3. Cutoff-wavelength form

Using the approximate detector relation

```math
E_g\simeq hc/\lambda_c,
```

the same condition becomes

```math
\boxed{
\frac{\lambda_{c,\rm out}}
{\lambda_{c,\rm in}}
\le
1+\chi.
}
```

or

```math
\boxed{
\lambda_{c,\rm in}
\ge
\frac{\lambda_{c,\rm out}}
{1+\chi}.
}
```

For `chi=1`,

```math
\boxed{
\lambda_{c,\rm in}
\ge
\lambda_{c,\rm out}/2.
}
```

Thus the ideal ballistic `chi=1` model allows about a factor-of-two cutoff span before the deterministic mean carrier energy reaches the local II threshold.

## 4. Examples

For an endpoint cutoff near `10 um`, the ballistic boundary corresponds to an entrance cutoff near `5 um`.

For an endpoint cutoff near `17 um`, the corresponding entrance cutoff is near `8.5 um`.

A larger span is not forbidden. It requires sufficient energy relaxation, quantified by `HGCDTE_II_SAFE_TRANSIT_CEILING.md`.

## 5. Physical interpretation

In the quasi-neutral ballistic limit,

```math
\varepsilon
=E_{g,\rm in}-E_g(x).
```

The local II threshold is modeled as

```math
E_{\rm th}=\chi E_g(x).
```

So the carrier catches the threshold when

```math
E_{g,\rm in}-E_g
=\chi E_g.
```

The cutoff-ratio rule is simply this energy bookkeeping written in detector language.

## 6. Design implication

The same composition engineering can be assigned two different roles:

```text
decreasing-gap absorber gradient
-> carrier acceleration
-> should respect the nonlocal hot-electron span constraint

increasing-gap collection boundary
-> dark-current / contact protection
-> can be electrostatically compensated so Ec is flat
-> need not add the same carrier-heating burden.
```

This suggests avoiding unnecessarily large downhill gap spans in the accelerator itself. Use the wide-gap boundary for leakage protection rather than using the entire wide-to-narrow gap change as electron acceleration.

## 7. Caveats

This is not a calibrated HgCdTe avalanche threshold or a universal factor-of-two law.

It depends on

- the deterministic mean-energy surrogate;
- cold injection;
- ballistic energy retention;
- `E_th=chi E_g`;
- quasi-neutral majority-band pinning;
- approximate `E_g=hc/lambda_c` conversion.

Stochastic high-energy tails can ionize before the mean reaches threshold, while real energy relaxation can permit larger grading spans.

## 8. Next use

Use this corollary only as a fast design sanity check. Quantitative work should use the finite-relaxation `r_min(zeta,chi)` relation and ultimately a calibrated energy-dependent Monte Carlo model.
