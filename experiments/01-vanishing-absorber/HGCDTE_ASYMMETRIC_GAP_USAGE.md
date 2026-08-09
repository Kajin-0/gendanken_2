# HgCdTe Asymmetric Gap Usage — Why the Widest-Gap Material Belongs More Naturally in the Collection Boundary

**Date:** 2026-08-09  
**Status:** exact corollary of the graded mean-energy phase boundary plus the minimum-compensation boundary result; conditional design principle; no novelty claim

## 1. Correct the resource question

A tempting next optimization is to imagine a conserved bandgap/composition budget

```text
accelerator gap drop + boundary gap rise = fixed resource.
```

That is not implied by a finite available composition range.

If the material system permits

```math
E_{g,\min}\le E_g(x)\le E_{g,\max},
```

the same wide-gap composition may appear in more than one spatial region. There is no fundamental sum rule requiring the total downward and upward gap excursions to add to a fixed value.

Therefore the relevant question is instead:

> **How much of the available wide-gap range can safely be used as downhill accelerator drive, and how much can be used in a compensated collection boundary?**

The two uses are physically asymmetric.

---

## 2. Mean-II-safe accelerator gap ratio

For the linear quasi-neutral graded absorber, the repository phase boundary is

```math
\zeta
\le
\frac{\chi}
{\chi+A(r)},
```

where

```math
\zeta
=1-\frac{E_{g,\rm out}}
{E_{g,\rm in}},
```

```math
r=L/\ell_E,
```

and

```math
A(r)=\frac{1-e^{-r}}{r}.
```

Then

```math
1-\zeta
\ge
\frac{A(r)}{\chi+A(r)}.
```

Therefore

```math
\boxed{
\frac{E_{g,\rm in}}
{E_{g,\rm out}}
\le
1+\frac{\chi}{A(r)}
}
```

or explicitly

```math
\boxed{
R_g^{\max}(r,\chi)
=1+\chi\frac{r}{1-e^{-r}}.
}
```

This is the maximum entrance-to-exit gap ratio permitted by the deterministic mean-energy threshold condition in the stated model.

---

## 3. Limits

### Ballistic limit

For

```math
r\to0,
```

```math
r/(1-e^{-r})\to1,
```

so

```math
\boxed{
R_g^{\max}\to1+\chi.
}
```

For `chi=1`,

```math
\boxed{R_g^{\max}=2.}
```

### Stronger relaxation

As `r` increases,

```math
R_g^{\max}
```

increases because the electron loses more of the energy gained from the downhill conduction band.

For `r >> 1`,

```math
\boxed{
R_g^{\max}\simeq1+\chi r.
}
```

Thus a larger available gap span can be used safely only by spending more energy-relaxation distance/time.

---

## 4. Cutoff-wavelength form

Using approximately

```math
E_g\simeq hc/\lambda_c,
```

the accelerator condition becomes

```math
\boxed{
\frac{\lambda_{c,\rm out}}
{\lambda_{c,\rm in}}
\le
1+\chi\frac{r}{1-e^{-r}}.
}
```

Equivalently,

```math
\boxed{
\lambda_{c,\rm in}
\ge
\frac{\lambda_{c,\rm out}}
{1+\chi r/(1-e^{-r})}.
}
```

For `chi=1`:

| `r=L/ell_E` | max gap ratio `Eg,in/Eg,out` | minimum `lambda_in/lambda_out` |
|---:|---:|---:|
| 0 | 2.000 | 0.500 |
| 0.5 | 2.271 | 0.440 |
| 1 | 2.582 | 0.387 |
| 2 | 3.313 | 0.302 |
| 3 | 4.157 | 0.241 |

These are conditional mean-energy design ratios, not measured HgCdTe limits.

---

## 5. Available material gap versus usable accelerator gap

Let

```math
E_{g,H}
```

be the maximum wide gap available from the chosen HgCdTe composition/process range, and let

```math
E_{g,L}
```

be the target narrow-gap endpoint of the accelerator.

The maximum entrance gap that may be used by the graded **accelerator** in the current mean-II model is

```math
\boxed{
E_{g,A}^{\max}
=
\min\left[
E_{g,H},
E_{g,L}R_g^{\max}(r,\chi)
\right].
}
```

If

```math
E_{g,H}
>
E_{g,L}R_g^{\max},
```

the material system offers more wide-gap range than the accelerator can use without additional relaxation.

That excess wide-gap capability is not wasted. It can still be valuable in the collection boundary.

---

## 6. Why the collection boundary is different

A wider-gap collection boundary has material conduction offset

```math
\alpha\Delta E_g^{(b)}.
```

At minimum barrier-free compensation,

```math
qV_b=\alpha\Delta E_g^{(b)},
```

so the **total** conduction edge is flat:

```math
\boxed{\Delta E_c^{(b)}=0.}
```

Therefore increasing the material boundary gap does not automatically add the same downhill carrier work that an accelerator gap drop does.

Instead, a wider boundary gap can

- raise the local direct-BTBT characteristic field;
- improve TAT tolerance if the defect spectrum also remains favorable;
- raise the local approximate II threshold;
- provide a region in which incoming hot carriers relax at minimum compensation.

Its costs appear elsewhere:

- larger barrier-canceling electrostatic voltage;
- finite boundary width needed to carry that voltage within local tunneling margins;
- interface/growth complexity;
- possible new defect states;
- boundary transit/cooling time.

This is why the same wide-gap composition is not equivalent when used as accelerator material versus boundary material.

---

## 7. Example in cutoff language

Take `chi=1` only as the current threshold surrogate.

### 10 um narrow-gap endpoint

Ballistic mean-II safety gives

```text
accelerator entrance cutoff >= 5 um.
```

With `L/ell_E=1`, the lower allowed entrance cutoff becomes approximately

```text
10 um / 2.582 = 3.87 um.
```

### 17 um narrow-gap endpoint

Ballistic mean-II safety gives

```text
accelerator entrance cutoff >= 8.5 um.
```

With `L/ell_E=2`,

```text
17 um / 3.313 = 5.13 um.
```

Thus a roughly `5 um`-equivalent wide-gap composition could be quite natural as a protective collection boundary for a `17 um` endpoint while being too aggressive as a ballistic downhill accelerator; it would require roughly `L/ell_E > 2` to use the full gap span as accelerator drive in the present mean-energy model.

---

## 8. Design principle

The current model therefore suggests

```text
Do not automatically use the full available composition gap range as downhill carrier acceleration.
```

Instead:

```text
accelerator gap span
-> limited by nonlocal carrier heating and available relaxation

boundary gap span
-> limited by compensation voltage, local TAT/BTBT capacity, defects, and transit/cooling length.
```

This is an **asymmetric use of the same material bandgap range**, not a split of one conserved gap budget.

---

## 9. Claim boundary

### Derived / conditional

```math
\boxed{
R_g^{\max}(r,\chi)
=1+\chi\frac{r}{1-e^{-r}}
}
```

and

```math
\boxed{
E_{g,A}^{\max}
=
\min[E_{g,H},E_{g,L}R_g^{\max}].
}
```

follow exactly from the repository mean-energy threshold model.

### Invalidated abstraction

A finite composition range alone does **not** imply a conserved additive relation between accelerator gap drop and boundary gap rise.

### Not established

- an optimum real HgCdTe composition profile;
- actual `ell_E` for the target device;
- stochastic II probability;
- optical-absorption cost of wide-gap portions;
- growth/defect cost of repeated composition excursions;
- novelty of the design interpretation.

---

## 10. Next question

The remaining important coupling is now optical:

> **If the downhill accelerator is not allowed to use the full wide-gap-to-narrow-gap span, how much narrow-gap optical absorbing length must be retained to achieve the desired quantum efficiency, and does that optical length conflict with the transport/relaxation lengths derived here?**

This reconnects the material transport branch to the original photodetector problem without returning to the invalid active-volume theorem.
