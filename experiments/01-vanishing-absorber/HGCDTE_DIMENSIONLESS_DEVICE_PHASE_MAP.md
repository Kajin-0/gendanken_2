# HgCdTe Dimensionless Device Phase Map — Separate Hot-Electron and Boundary-Tunneling Feasibility

**Date:** 2026-08-09  
**Status:** exact organization of previously derived conditional inequalities; design map, not a calibrated device model; no novelty claim

## 1. Purpose

The graded-HgCdTe branch now has two qualitatively different constraints:

```text
absorber
-> nonlocal carrier-energy history
-> impact-ionization threshold access

collection boundary
-> local electrostatic field
-> TAT / direct-BTBT exponent margins.
```

They should not be represented by one scalar `maximum field`.

This note defines a dimensionless phase map in which the two constraints remain separate.

---

## 2. Absorber nonlocal-II margin

For a linear quasi-neutral p-type graded absorber,

```math
E_g(x)=E_{g0}-Gx,
```

with

```math
\zeta=\frac{\Delta E_g}{E_{g0}},
\qquad
r=\frac{L}{\ell_E},
```

define

```math
A(r)=\frac{1-e^{-r}}{r}.
```

The exit mean excess energy is

```math
\varepsilon_L
=\zeta E_{g0}A(r),
```

while the threshold surrogate is

```math
E_{\rm th,L}
=\chi E_{g0}(1-\zeta).
```

Define the mean-II margin

```math
\boxed{
\mathcal M_{\rm II}
\equiv
\frac{E_{\rm th,L}}
{\varepsilon_L}
=
\frac{\chi(1-\zeta)}
{\zeta A(r)}.
}
```

Then

```math
\boxed{
\mathcal M_{\rm II}>1
}
```

is below the deterministic mean threshold,

```math
\boxed{
\mathcal M_{\rm II}=1
}
```

is the phase boundary, and

```math
\boxed{
\mathcal M_{\rm II}<1
}
```

is mean-threshold accessible.

This is not a true stochastic ionization probability.

---

## 3. Collection-boundary local tunneling margin

At minimum barrier-free compensation,

```math
V_b
=\frac{\alpha\Delta E_g^{(b)}}{q}.
```

For local inverse-field constraints define

```math
F_{\rm allow}(x)
=\min_m\frac{F_m(x)}{\Sigma_m},
```

where current mechanisms `m` may include TAT and direct BTBT when their local WKB descriptions are valid.

The maximum compensation voltage supportable without violating those local margins is

```math
\boxed{
V_{\rm cap}
=\int_0^wF_{\rm allow}(x)dx.
}
```

Define the dimensionless boundary voltage margin

```math
\boxed{
\mathcal M_b
\equiv
\frac{V_{\rm cap}}{V_b}
=
\frac{q\int_0^wF_{\rm allow}(x)dx}
{\alpha\Delta E_g^{(b)}}.
}
```

Then

```math
\boxed{
\mathcal M_b\ge1
}
```

is locally feasible, while

```math
\boxed{
\mathcal M_b<1
}
```

means no nonnegative one-dimensional field profile can supply the required barrier-canceling voltage without violating at least one adopted local field margin.

---

## 4. Two-axis feasibility map

The simplest minimum-compensation device classification is therefore

```math
\boxed{
(\mathcal M_{\rm II},\mathcal M_b).
}
```

### Region I — jointly feasible

```math
\boxed{
\mathcal M_{\rm II}\ge1,
\qquad
\mathcal M_b\ge1.
}
```

The absorber remains below the deterministic mean-II threshold and the boundary can carry the required voltage within the chosen local TAT/BTBT margins.

### Region II — hot-electron limited

```math
\mathcal M_{\rm II}<1,
\qquad
\mathcal M_b\ge1.
```

The boundary is locally acceptable, but the downhill absorber grading is too aggressive for the available energy relaxation in the mean-energy model.

### Region III — boundary-tunneling limited

```math
\mathcal M_{\rm II}\ge1,
\qquad
\mathcal M_b<1.
```

The absorber is mean-II safe, but the collection boundary cannot carry the required compensation voltage at the adopted local tunneling margins.

### Region IV — jointly infeasible

```math
\mathcal M_{\rm II}<1,
\qquad
\mathcal M_b<1.
```

Both constraints fail.

This two-axis description is preferred to a single combined margin because the underlying remedies differ physically.

---

## 5. Why the constraints approximately factor at minimum compensation

At the minimum barrier-free voltage,

```math
\Delta E_c^{(b)}=0.
```

Therefore the boundary adds no further downhill conduction-band work.

If the carrier enters below mean II threshold, the boundary mean energy relaxes while the local gap rises.

Thus in the present idealized architecture the absorber's nonlocal-II constraint can be evaluated first, and the boundary's local tunneling-voltage constraint can then be evaluated separately.

This approximate factorization fails once the boundary is overcompensated enough to produce a net downhill conduction-band slope.

---

## 6. Add a normalized latency coordinate

Feasibility alone does not determine speed.

Let

```math
r_{\min}(\zeta,\chi)
```

be the minimum absorber `L/ell_E,a` required by the mean-II condition, with `r_min=0` in the ballistic-safe regime.

Let the boundary require cooling to energy fraction `c`, and define

```math
\rho_E=\ell_{E,b}/\ell_{E,a}.
```

Let

```math
u_t=w_{\rm TAT}/\ell_{E,a},
```

```math
nu_Z=w_Z/\ell_{E,a}.
```

Then the conditional kinematic transit floor from `HGCDTE_BOUNDARY_COOLING_TRANSIT_FLOOR.md` is

```math
\boxed{
\Theta_{\min}
\equiv
\frac{T_{\rm total,min}v_K}
{\ell_{E,a}}
=
r_{\min}
+
\max\left[
\rho_E\ln\frac1c,
\nu_t,
\nu_Z
\right].
}
```

Thus the full dimensionless design point can be written as

```math
\boxed{
(\mathcal M_{\rm II},\mathcal M_b,\Theta_{\min}).
}
```

The first two coordinates determine conditional feasibility; the third gives a best-case time cost within the current model.

---

## 7. Useful design motions in the phase map

### Increase absorber grading span `zeta`

At fixed `r`,

```text
more downhill band-structure drive
-> smaller M_II
-> eventually enters hot-electron-limited region.
```

### Increase absorber relaxation ratio `r=L/ell_E`

At fixed `zeta`,

```text
more relaxation distance
-> larger M_II
-> larger minimum transit distance/time.
```

### Improve boundary gap/trap quality

Increasing local `F_allow` increases

```math
\mathcal M_b.
```

This moves the design away from boundary-tunneling limitation without directly changing absorber hot-electron history at minimum compensation.

### Increase boundary width

For roughly fixed local material quality,

```math
V_{\rm cap}\propto w,
```

so `M_b` increases, but the boundary transit/cooling distance also increases.

### Overcompensate the boundary

Extra compensation can accelerate carriers through the boundary, but the factorization above breaks because it adds both local field stress and nonlocal carrier work.

Treat overcompensation as a separate active speed resource, not as a free improvement.

---

## 8. What the phase map does not include

The present axes do not yet contain

- stochastic impact-ionization probability below the mean threshold;
- full TAT prefactors and trap occupations;
- SRH/Auger generation;
- interface recombination;
- space-charge modification under illumination;
- high-field velocity beyond the Kane kinematic ceiling;
- capacitance/readout bandwidth;
- optical absorption efficiency.

Those should be added only when they change the active device decision.

---

## 9. Current use

Until calibrated `ell_E(E,x)` and `Gamma_II(E,x)` data are available for the target HgCdTe composition and temperature, use this phase map parametrically.

The purpose is to answer questions such as

```text
How aggressive can the downhill gap gradient be?
How much relaxation distance is then required?
Can the collection boundary carry its alignment voltage at the chosen TAT/BTBT margins?
Which mechanism fails first as the design is made faster?
```

That is the current device-level frontier.
