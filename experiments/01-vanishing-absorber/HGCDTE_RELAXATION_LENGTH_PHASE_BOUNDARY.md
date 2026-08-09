# HgCdTe Relaxation-Length Phase Boundary — How Much Energy Relaxation Is Enough to Change Which High-Field Mechanism Appears First?

**Date:** 2026-08-09  
**Status:** exact Lambert-W boundary inside the repository mean-energy + simplified direct-BTBT models; sensitivity tool, not a calibrated HgCdTe limit; no novelty claim

## 1. Purpose

`HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md` identified the missing target-composition input

```text
energy-relaxation length ell_E(F)
```

before a finite-length impact-ionization probability can be compared quantitatively with direct BTBT.

A full interpolation is not always necessary.

This note asks a sharper question:

> **For a chosen cutoff, collection length, and direct-BTBT current budget, what critical energy-relaxation length makes the mean impact-ionization threshold occur at exactly the same field as the BTBT budget?**

If the real `ell_E` lies clearly on one side of this threshold, the mechanism ordering can be decided without knowing the complete relaxation curve.

---

## 2. Inputs

### Mean-energy ionization threshold

For cold injection and

```math
E_{\rm th}=\chi E_g,
```

the one-relaxation-time surrogate gives

```math
\boxed{
F_{\rm th}^{(\rm mean)}
=
\frac{\chi E_g}
{q\ell_E(1-e^{-L/\ell_E})}.
}
```

Define the ballistic field-work threshold

```math
\boxed{
F_{\rm dead}
=\frac{\chi E_g}{qL}.
}
```

### Direct-BTBT budget field

From the normalized HgCdTe BTBT model,

```math
\boxed{
F_J
=
\frac{F_K}
{2W_0[\tfrac12\sqrt{J_K/J_*}]}.
}
```

`F_J` is the field where the isolated direct-BTBT current reaches the stated current-density budget `J_*`.

---

## 3. Set the two fields equal

The mechanism boundary is defined by

```math
F_{\rm th}^{(\rm mean)}=F_J.
```

Using

```math
F_{\rm dead}=\chi E_g/(qL),
```

define

```math
\boxed{
r
\equiv
\frac{F_{\rm dead}}{F_J}.
}
```

Then the equality becomes

```math
\ell_E(1-e^{-L/\ell_E})
=rL.
```

Define

```math
\boxed{y=L/\ell_E.}
```

The boundary equation is

```math
\boxed{
\frac{1-e^{-y}}{y}=r.
}
```

The left side decreases monotonically from `1` at `y -> 0` to `0` at `y -> infinity`.

Therefore a finite positive critical relaxation length exists iff

```math
\boxed{0<r<1.}
```

---

## 4. Exact Lambert-W solution

Starting from

```math
1-r y=e^{-y},
```

let

```math
u=1-r y.
```

Then

```math
u
=e^{-(1-\nu)/r}
=e^{-1/r}e^{\nu/r}.
```

Hence

```math
\left(-\frac{\nu}{r}\right)
\exp\left(-\frac{\nu}{r}\right)
=
-\frac1r e^{-1/r}.
```

Therefore

```math
-\frac{\nu}{r}
=W\!\left[-\frac1r e^{-1/r}\right].
```

The nonzero physical solution uses the principal real branch `W_0`:

```math
\boxed{
y_*
=
\frac1r
+
W_0\!\left[-\frac1r e^{-1/r}\right].
}
```

The `W_{-1}` branch returns the limiting trivial root `y=0`, corresponding to `ell_E -> infinity`.

Thus the critical energy-relaxation length is

```math
\boxed{
\ell_{E,*}
=
\frac{L}
{\frac1r
+W_0[-r^{-1}e^{-1/r}]}
}
```

for `0<r<1`.

---

## 5. Which side means what?

The effective acceleration length

```math
L_{\rm eff}
=\ell_E(1-e^{-L/\ell_E})
```

increases monotonically with `ell_E`.

Therefore:

### Weak energy relaxation / long `ell_E`

If

```math
\boxed{\ell_E>\ell_{E,*},}
```

then

```math
F_{\rm th}^{(\rm mean)}<F_J.
```

The **mean-energy impact-ionization threshold becomes accessible before the chosen direct-BTBT budget is exhausted**.

### Strong energy relaxation / short `ell_E`

If

```math
\boxed{\ell_E<\ell_{E,*},}
```

then

```math
F_{\rm th}^{(\rm mean)}>F_J.
```

The chosen direct-BTBT budget is reached before the mean electron trajectory reaches the ionization threshold.

Important:

> This is a boundary for the **mean-energy surrogate**, not for the true stochastic impact-ionization probability.

A high-energy tail may ionize even when the mean remains below threshold.

---

## 6. Special case `r >= 1`

If

```math
F_{\rm dead}\ge F_J,
```

then

```math
r\ge1.
```

Even the ideal ballistic / infinite-`ell_E` threshold does not occur below the BTBT budget field.

Therefore, inside the mean-energy model,

```math
\boxed{
r\ge1
\quad\Rightarrow\quad
\text{BTBT budget occurs first for every finite }\ell_E.
}
```

Again, this does not exclude stochastic II from the high-energy tail.

---

## 7. Representative critical lengths for `L = 1 um`, `chi = 1`

Using the repository simplified HgCdTe BTBT model:

### Direct-BTBT budget `J_* = 1e-12 A/cm2`

| cutoff | `F_J` | `F_dead` | `ell_E,*` |
|---:|---:|---:|---:|
| 8 um | 6.80 kV/cm | 1.55 kV/cm | 0.231 um |
| 10 um | 4.45 kV/cm | 1.24 kV/cm | 0.288 um |
| 12 um | 3.14 kV/cm | 1.03 kV/cm | 0.348 um |
| 17 um | 1.62 kV/cm | 729 V/cm | 0.529 um |
| 24 um | 845 V/cm | 517 V/cm | 0.926 um |

### Direct-BTBT budget `J_* = 1e-8 A/cm2`

| cutoff | `ell_E,*` |
|---:|---:|
| 8 um | 0.178 um |
| 10 um | 0.218 um |
| 12 um | 0.259 um |
| 17 um | 0.367 um |
| 24 um | 0.551 um |

### Direct-BTBT budget `J_* = 1e-6 A/cm2`

| cutoff | `ell_E,*` |
|---:|---:|
| 8 um | 0.153 um |
| 10 um | 0.186 um |
| 12 um | 0.218 um |
| 17 um | 0.301 um |
| 24 um | 0.429 um |

These are **model phase boundaries**, not measured relaxation lengths.

---

## 8. Convert the critical length into a critical relaxation time

Because

```math
\ell_E=v\tau_E,
```

```math
\boxed{
\tau_{E,*}
=\frac{\ell_{E,*}}{v}.
}
```

The currently recovered `x=0.20`, 77 K transport literature supports high-field velocity scales of roughly

```text
2.5e5 to 5e5 m/s
```

depending on density/model/field regime.

For `J_*=1e-12 A/cm2`, `L=1 um`:

### 10 um cutoff

```math
\ell_{E,*}=0.288\ {\rm um}.
```

Thus

```text
v = 2.5e5 m/s -> tau_E,* ~ 1.15 ps
v = 5.0e5 m/s -> tau_E,* ~ 0.576 ps.
```

### 17 um cutoff

```math
\ell_{E,*}=0.529\ {\rm um}.
```

Thus

```text
v = 2.5e5 m/s -> tau_E,* ~ 2.12 ps
v = 5.0e5 m/s -> tau_E,* ~ 1.06 ps.
```

This is useful because the required external data have become a **sub-picosecond / few-picosecond classification problem**, not an arbitrary full-function reconstruction.

---

## 9. Sensitivity interpretation

The critical length grows strongly toward longer cutoff wavelength because

```text
F_J falls toward F_dead.
```

Thus long-wavelength HgCdTe does not merely have a smaller BTBT field scale.

It also requires less efficient carrier energy accumulation for the mean ionization threshold to become competitive with a stated direct-BTBT current budget.

The ordering is controlled jointly by

```math
\boxed{
F_{\rm dead}/F_J
}
```

and

```math
\boxed{
\ell_E/L.
}
```

This is more informative than quoting a single bulk "impact-ionization onset field."

---

## 10. Relation to the stochastic ionization rate

The phase boundary above uses only the mean trajectory.

The true finite-device event probability is

```math
P_{\rm II}
=1-
\exp\left[-
\int \Gamma_{\rm II}(E(t))dt
\right]
```

for a given trajectory, and a true Monte Carlo calculation averages over stochastic trajectories.

Therefore:

### If `ell_E >> ell_E,*`

The mean itself reaches threshold before the BTBT budget.

Impact ionization is clearly a mechanism that cannot be ignored before the BTBT ceiling.

### If `ell_E << ell_E,*`

The mean remains below threshold at `F_J`.

This does **not** prove II is negligible because the high-energy tail can still contribute.

So the phase boundary is one-sided as evidence:

```text
mean threshold first
-> II definitely requires attention

mean threshold after BTBT
-> stochastic II still needs checking.
```

---

## 11. Reproducibility

A companion deterministic regression should compute

- `F_J(lambda,L,J_*)`;
- `F_dead(lambda,L,chi)`;
- `r=F_dead/F_J`;
- the exact Lambert-W critical `ell_E,*`;
- `tau_E,*` for stated velocity ranges.

The numeric boundary should also be checked by substituting `ell_E,*` back into

```math
\ell_E(1-e^{-L/\ell_E})=rL.
```

---

## 12. Claim boundary

### DERIVED within the mean-energy + simplified BTBT models

```math
\boxed{
\frac{1-e^{-y_*}}{y_*}=r,
\qquad
r=F_{\rm dead}/F_J,
}
```

```math
\boxed{
y_*
=\frac1r
+W_0[-r^{-1}e^{-1/r}],
}
```

```math
\boxed{
ell_{E,*}=L/y_*.
}
```

### CHECKED

Representative critical lengths were independently evaluated numerically.

### NOT ESTABLISHED

- the actual `ell_E(F)` of the target material;
- stochastic `P_II(F,L)` from the high-energy tail;
- a complete II-vs-BTBT mechanism boundary;
- TAT constraints;
- a universal HgCdTe speed-dark-current law;
- novelty of the Lambert-W reduction.

---

## 13. Next decisive step

This result narrows the data request dramatically.

For a stated cutoff, geometry and `J_*`, ask only:

> **Is the real energy-relaxation length at the relevant field above or below `ell_E,*`?**

If the answer is robustly above, mean-energy II becomes accessible before the BTBT budget.

If robustly below, the stochastic high-energy tail—not the mean energy—becomes the only remaining II route before BTBT.

Next, search or infer physically defensible bounds on `ell_E` / `tau_E` from primary `Hg_0.8Cd_0.2Te`, 77 K transport data. Do not invent an exact interpolation if only a bound is justified.
