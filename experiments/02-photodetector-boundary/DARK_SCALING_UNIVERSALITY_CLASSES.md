# Dark-Exposure Scaling Classes for Thin Photodetectors — Experiment 02

**Date:** 2026-08-12  
**Status:** adversarial generalization of the strong-dark semiconductor branch  
**Priority:** unassessed; no novelty claim

`TIMETAGGED_POINT_PROCESS_DECISION.md` found, for one specific bulk-dark + transit-gate model,

```math
L_*\sim\sqrt{\frac{v}{2r_dA}},
\qquad
\mu_*\to\frac12.
```

The number `1/2` looked suggestive, but it is not fundamental. It follows from the assumed thickness scaling of the dark process.

This file generalizes that result and identifies the actual scaling structure.

---

## 1. Thin-device signal scaling

In the optically thin regime, Beer-Lambert absorption gives

```math
\eta_s(L)
\sim S L,
```

with

```math
\boxed{S=\eta_0\alpha}
```

for the current minimal semiconductor model.

More generally, retain

```math
\boxed{\eta_s(L)\sim S L^s}
```

with positive signal exponent `s`.

For ordinary thin single-pass absorption,

```math
s=1.
```

---

## 2. General dark-exposure scaling

Let the dark-event rate during the observation window scale as

```math
\lambda_d(L)\sim C_d L^m,
```

and let the required observation/gate time scale as

```math
T(L)\sim C_t L^n.
```

Then the mean number of dark events scales as

```math
\boxed{
\mu(L)
=\lambda_d(L)T(L)
\sim K L^p,
}
```

where

```math
\boxed{
K=C_dC_t,
\qquad
p=m+n.
}
```

Examples:

```text
bulk dark generation:        m=1
surface/area dark rate:      m=0
transit-linked gate:         n=1
fixed gate:                  n=0
```

Thus

```text
bulk dark + transit gate -> p=2
surface dark + transit gate -> p=1
bulk dark + fixed gate -> p=1.
```

The exponent `p`, not a universal `1/2`, controls the strong-dark optimum.

---

## 3. Binary coarse-grained strong-dark model

When the device is forced thin enough that the signal probability is small,

```math
\mathcal D_{\rm bin}(L)
\sim
S L^s e^{-KL^p}.
```

Take the logarithmic derivative:

```math
\frac{d}{dL}\ln\mathcal D
=\frac{s}{L}-pK L^{p-1}.
```

The optimum satisfies

```math
pK L_*^p=s.
```

Therefore

```math
\boxed{
L_*
\sim
\left(\frac{s}{pK}\right)^{1/p}.
}
```

The mean dark count at the optimum is

```math
\boxed{
\mu_*
=K L_*^p
=\frac{s}{p}.
}
```

This is the general origin of the earlier `1/2`:

```text
s=1,
p=2
-> mu_*=1/2.
```

---

## 4. Maximum distinguishability scaling

At the optimum,

```math
\mathcal D_{\max}
\sim
S
\left(\frac{s}{pK}\right)^{s/p}
\exp\left(-\frac{s}{p}\right).
```

Thus

```math
\boxed{
\mathcal D_{\max}
\sim
S
\left(\frac{s}{epK}\right)^{s/p}.
}
```

For ordinary thin absorption `s=1`,

```math
\boxed{
\mathcal D_{\max}
\sim
S
\left(\frac{1}{epK}\right)^{1/p}.
}
```

This identifies a family of strong-dark scaling classes indexed by `p`.

---

## 5. Recovery of the bulk-transit result

For uniform bulk dark-event density `r_d`, area `A`, and transit gate `T=L/v`,

```math
\lambda_d=r_dAL,
```

so

```math
m=1,
\qquad
n=1,
\qquad
p=2,
```

and

```math
K=\frac{r_dA}{v}.
```

With `s=1`,

```math
\boxed{
L_*
\sim
\frac1{\sqrt{2K}}
=
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
\frac{S}{\sqrt{2eK}}
=
\eta_0\alpha
\sqrt{\frac{v}{2er_dA}}.
}
```

So the previous result is exactly the `p=2`, `s=1` member of the general family.

---

## 6. Surface-dominated dark process gives a different law

Suppose the dominant dark count rate is set by an area/surface mechanism whose total rate is approximately thickness independent:

```math
\lambda_d\sim R_sA.
```

With transit gate

```math
T=L/v,
```

we have

```math
m=0,
\qquad
n=1,
\qquad
p=1,
```

and

```math
K=\frac{R_sA}{v}.
```

For thin absorption `s=1`,

```math
\boxed{
L_*
\sim
\frac1K
=\frac{v}{R_sA},
}
```

```math
\boxed{\mu_*=1,}
```

and

```math
\boxed{
\mathcal D_{\max}
\sim
\frac{S}{eK}
=
\frac{\eta_0\alpha v}{eR_sA}.
}
```

Thus the square-root bulk scaling is **not universal across dark mechanisms**.

The dark mechanism changes the exponent of the geometry-performance law.

---

## 7. Fixed gate + bulk dark has the same p=1 scaling class

For bulk rate

```math
\lambda_d=r_dAL
```

but thickness-independent gate `T=tau_0`,

```math
p=1,
\qquad
K=r_dA\tau_0.
```

Then

```math
L_*\sim1/K,
\qquad
\mu_*=1,
\qquad
\mathcal D_{\max}\sim S/(eK).
```

This shows that **the same dark mechanism can move between scaling classes when the timing architecture changes**.

---

## 8. Full point-process observer

`TIMETAGGED_POINT_PROCESS_DECISION.md` showed that in the thin-device limit, when signal timestamps become approximately indistinguishable in shape from homogeneous dark timestamps, the full output distinguishability has the form

```math
\mathcal D_{\rm full}(L)
\sim
S L^s p_{\max}[\mu(L)],
```

where

```math
p_{\max}(\mu)
=\max_n e^{-\mu}\mu^n/n!.
```

For

```math
0\le\mu\le1,
```

```math
p_{\max}(\mu)=e^{-\mu}.
```

Therefore, whenever

```math
\boxed{\frac{s}{p}\le1,}
```

the binary optimum

```math
\mu_*=s/p
```

lies in the first Poisson-mode interval and the **full timestamp/count observer has the same leading optimum and scaling**.

For ordinary thin absorption `s=1` and any `p>=1`, this condition is satisfied.

Hence:

```math
\boxed{
\mu_*=1/p
}
```

and the corresponding leading scaling survive full point-process readout for the physically common `p>=1` classes under the uniform-time thin limit.

---

## 9. If s/p > 1, count resolution changes the optimum

When

```math
s/p>1,
```

the binary candidate optimum lies at `mu>1`, where

```math
p_{\max}(\mu)\ne e^{-\mu}.
```

Then the full count-resolved optimum must be found piecewise from

```math
\mu^{s/p}p_{\max}(\mu).
```

Thus the simple `mu_*=s/p` result is not universally valid beyond the first Poisson-mode interval.

This is another reason not to promote `mu=1/2` into a fundamental detector constant.

---

## 10. Decision-feasibility scaling by universality class

For `s=1` and `p>=1`, define required distinguishability

```math
D_{\rm req}=1-2\epsilon.
```

The strong-dark asymptotic condition is

```math
D_{\rm req}
\lesssim
S(epK)^{-1/p}.
```

Equivalently,

```math
\boxed{
K
\lesssim
\frac{S^p}{epD_{\rm req}^p}.
}
```

The physical meaning of `K` depends on the dark/timing architecture.

### Bulk + transit, p=2

```math
K=r_dA/v
```

gives

```math
\frac{r_dA}{v}
\lesssim
\frac{S^2}{2eD_{\rm req}^2}.
```

### Surface + transit, p=1

```math
K=R_sA/v
```

gives

```math
\frac{R_sA}{v}
\lesssim
\frac{S}{eD_{\rm req}}.
```

These are different physical feasibility laws.

---

## 11. Strongest conceptual correction

The earlier result

```math
\mu_*=1/2
```

is **not fundamental**.

The stronger statement is

```math
\boxed{
\mu_*=\frac{s}{p}
}
```

for the leading binary/uniform-point-process regime, where

```text
s = thin-device signal-growth exponent;
p = dark-exposure growth exponent.
```

For ordinary thin absorption `s=1`,

```math
\boxed{\mu_*=1/p.}
```

Thus the optimum expected dark count is set by the **relative scaling exponents of useful signal and dark exposure**, not by one universal numerical constant.

---

## 12. Why this matters for the original Gedanken experiment

This generalization reinforces the central pattern:

```text
an apparent detector constant
-> hidden architecture/mechanism assumption
-> resource scaling exponent exposed.
```

The detector boundary is not controlled merely by how much matter is present.

It depends on how additional material changes

```text
signal-generation probability;
dark-event generation;
observation time;
collection geometry;
readout information.
```

---

## 13. Prior-art expectation

The optimization

```math
L^s e^{-KL^p}
```

is elementary.

Therefore the scaling-class mathematics itself should have **low novelty expectation**.

Potential scientific value would have to come from identifying physically justified exponents/coefficients for a real detector mechanism and showing that the resulting feasibility law is experimentally useful or not already standard in that detector literature.

No novelty claim is made.

---

## 14. Next physical attack

The most important next correction is to make the dark process physically consistent with carrier collection.

A thermally generated bulk carrier pair should not necessarily count as a dark event merely because it was generated; it may also need to survive transport to the collecting boundary.

Replace the raw bulk dark rate

```math
r_dAL
```

with a collection-weighted dark rate

```math
\lambda_d^{\rm col}(L)
\propto
r_dA\int_0^L P_{\rm dark,col}(z,L)dz.
```

Then ask whether the `p=2` thin-limit class and its feasibility scaling survive.

If they do, the result is robust to a more consistent signal/dark transport model. If not, the current scaling should be downgraded accordingly.
