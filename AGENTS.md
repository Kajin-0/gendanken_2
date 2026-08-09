# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is a dimensionless graded-HgCdTe device phase map combining nonlocal hot-electron safety, boundary TAT/BTBT voltage capacity, and best-case transit time; no novelty claim**

Read this file first.

The project follows the physics rather than a predetermined theorem. Counterexamples and prior-art collisions are progress. Do not force the work back toward the original active-volume idea or prematurely toward a manuscript.

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA immediately before replacing a file;
4. never overwrite a stale SHA;
5. preserve failed/corrected branches;
6. make narrow edits where practical.

**Live `main` overrides all snapshots and recovery notes.**

---

## 2. Mandatory epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **CANDIDATE DISTINCT — PRIORITY UNPROVEN**
- **INVALIDATED**
- **SUPERSEDED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and `CLAIM_LEDGER.md` update.

---

## 3. Current research path

```text
active volume
-> universal volume bound killed by field concentration

microscopic absorber / LDOS / ultrastrong coupling
-> successive loopholes and nonperturbative access physics

finite passive network
-> harmonic optical-to-detector transfer-area law

active / adaptive / time-dependent control
-> pump, timing, storage, and output-record resources
-> unrestricted output continuum kills universal finite detector-only capacity

semiconductor extraction / energy filters
-> detailed balance, lifetime broadening, multipole delay

HgCdTe field-driven collection
-> normalized BTBT
-> low-field mobility shortcut killed

TAT / nonlocal impact ionization
-> leakage depends on defect spectrum and carrier energy history

homogeneous field shaping
-> no local speed/leakage benefit under stated model

heterostructure allocation
-> field should be placed where leakage cost is lower

composition grading
-> direct-Zener geometry can be suppressed at fixed conduction drive

quasi-neutral p-type grading
-> majority-hole band can be nearly pinned
-> gap slope becomes minority-electron drive

collection boundary
-> unavoidable barrier-canceling voltage
-> local TAT/BTBT voltage capacity

nonlocal hot-electron branch
-> grading does not remove conduction-band work
-> exact mean-II phase boundary
-> relaxation converts it into a transit-time floor

CURRENT FRONTIER
-> dimensionless finite-device phase map:
   absorber II margin
   + boundary local-tunneling margin
   + cooling/transit cost.
```

---

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_DIMENSIONLESS_DEVICE_PHASE_MAP.md`
6. `experiments/01-vanishing-absorber/HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`
7. `experiments/01-vanishing-absorber/HGCDTE_II_SAFE_TRANSIT_CEILING.md`
8. `experiments/01-vanishing-absorber/HGCDTE_BALLISTIC_GRADING_SPAN_RULE.md`
9. `experiments/01-vanishing-absorber/HGCDTE_BOUNDARY_COOLING_TRANSIT_FLOOR.md`
10. `experiments/01-vanishing-absorber/HGCDTE_GRADED_ABSORBER_BOUNDARY_RELAXATION.md`
11. `experiments/01-vanishing-absorber/HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md`
12. `experiments/01-vanishing-absorber/HGCDTE_LINEAR_GRADED_KANE_WKB.md`
13. `experiments/01-vanishing-absorber/HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`
14. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
15. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

There is still **no manuscript**.

---

## 5. Direct-Zener grading result

Define

```math
S_c=-dE_c/dx,
\qquad
S_v=-dE_v/dx,
\qquad
G=-dE_g/dx.
```

Because `E_g=E_c-E_v`,

```math
\boxed{S_v=S_c-G.}
```

At fixed useful conduction slope `S_c=S`, define

```math
\delta=G/S.
```

For the linear two-band/Kane two-turning-point model,

```math
\boxed{
\frac{\mathcal S_Z(\delta)}
{\mathcal S_Z(0)}
=
\frac{(2-\delta)^2}
{4(1-\delta)^{3/2}},
\qquad 0\le\delta<1.
}
```

The action increases monotonically and diverges as `delta -> 1-`.

**Interpretation:** a decreasing gap can provide useful `E_c` slope while removing the relative `E_c/E_v` geometry that enables the ordinary direct-Zener path.

This does not eliminate TAT, interface tunneling, or hot-carrier processes.

---

## 6. Quasi-neutral p-type self-consistency

For nondegenerate holes with `p approximately N_A`,

```math
\boxed{
\frac{dE_v}{dx}
\simeq
k_BT\frac{d}{dx}\ln(N_A/N_v).
}
```

For nearly constant `N_A/N_v`,

```math
\boxed{E_v\approx\text{constant},}
```

so for a decreasing gap

```math
\boxed{S_c\approx G.}
```

Thus the favorable direct-Zener geometry can emerge naturally from quasi-neutral equilibrium.

Do not default to a uniformly depleted multi-micron graded absorber; its `N_eff L^2` Poisson burden becomes severe rapidly.

---

## 7. Nonlocal carrier-energy state

Hot-electron energy depends on the **total conduction-band slope**, not on whether that slope came from electric potential or composition grading.

Use

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

For cold injection,

```math
\boxed{
\varepsilon(x)
=
\int_0^xS_c(s)
\exp\!\left[-\int_s^x\frac{du}{\ell_E(u)}\right]ds.
}
```

This is path dependent.

**Do not replace it with a local `F_II(x)` ceiling** unless a local-equilibrium reduction has been justified.

---

## 8. Linear graded mean-II phase boundary

For

```math
E_g=E_{g0}-Gx,
\qquad
S_c=G,
```

constant `ell_E`, and threshold surrogate

```math
E_{\rm th}=\chi E_g,
```

define

```math
\zeta=\Delta E_g/E_{g0},
\qquad
r=L/\ell_E.
```

Then

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

Mean threshold access occurs for

```math
\boxed{\zeta\ge\zeta_{\rm II}.}
```

Ballistic limit:

```math
\boxed{
\zeta_{\rm II}\to\frac{\chi}{1+\chi}.
}
```

For `chi=1`, this is `1/2`.

This is a deterministic mean-energy boundary, not a zero-probability stochastic II theorem.

---

## 9. Relaxation-required grading and transit floor

If

```math
\zeta>\chi/(1+\chi),
```

define

```math
\boxed{
a=\chi(1-\zeta)/\zeta.}
```

Then the minimum safe relaxation ratio is

```math
\boxed{
r_{\min}
=\frac1a
+W_0\!\left[-\frac1a e^{-1/a}\right].
}
```

Hence

```math
\boxed{L\ge\ell_Er_{\min}.}
```

Using the simplified Kane group-velocity ceiling `|v_g|<v_K`,

```math
\boxed{
T_{\rm tr}\ge\frac{\ell_E}{v_K}r_{\min}.
}
```

For `chi=1`, representative `r_min` values are

```text
zeta=0.55 -> 0.416
zeta=0.60 -> 0.874
zeta=0.70 -> 2.026
zeta=0.80 -> 3.921
zeta=0.90 -> 8.999
```

---

## 10. Ballistic cutoff-span sanity rule

The ballistic phase boundary may be written

```math
\boxed{
E_{g,\rm in}/E_{g,\rm out}
\le1+\chi.
}
```

Using `E_g approximately hc/lambda_c`,

```math
\boxed{
\lambda_{c,\rm in}
\ge
\lambda_{c,\rm out}/(1+\chi).
}
```

For `chi=1`, the conditional ballistic span is approximately a factor of two in cutoff wavelength.

This is a sanity rule inside the mean-energy model, not a universal HgCdTe factor-of-two law.

---

## 11. Collection-boundary local tunneling resource

For a wider-gap boundary with gap increase `Delta Eg_b` and conduction-band share `alpha`, barrier-free extraction requires

```math
\boxed{qV_b\ge\alpha\Delta E_g^{(b)}.}
```

Any nonnegative field over width `w` obeys

```math
\boxed{F_{\max}\ge V_b/w.}
```

For local inverse-field mechanisms `m` with characteristic fields `F_m(x)` and required margins `Sigma_m`, define

```math
\boxed{
F_{\rm allow}(x)
=\min_m\frac{F_m(x)}{\Sigma_m}.
}
```

The required voltage is locally feasible iff

```math
\boxed{
V_b\le\int_0^wF_{\rm allow}(x)dx.
}
```

Use this for TAT and direct BTBT where their local WKB forms are valid.

---

## 12. Minimum-compensation boundary and cooling

At

```math
\boxed{qV_b=\alpha\Delta E_g^{(b)},}
```

the net conduction-edge step is zero.

The boundary therefore adds no downhill carrier work and

```math
\boxed{
\varepsilon_b(s)
=\varepsilon_a e^{-s/\ell_{E,b}}.
}
```

while the local gap and approximate II threshold increase.

If the carrier enters below mean threshold, a monotonic minimally compensated wider-gap boundary cannot create a new mean-threshold crossing in the current model.

To cool the carrier to fraction `c`, however,

```math
\boxed{
w_{\rm cool}
=\ell_{E,b}\ln(1/c).}
```

Cooling is therefore not zero-length.

---

## 13. Combined conditional device transit floor

For a uniform boundary with required TAT and direct-Zener exponent margins,

```math
w_{\rm TAT}
=\frac{\alpha\Delta E_g^{(b)}\Sigma_t}{qF_{\rm TAT}},
```

```math
w_Z
=\frac{\alpha\Delta E_g^{(b)}\Sigma_Z}{qF_K}.
```

The minimum boundary width is

```math
\boxed{
w_b\ge
\max\left[
\ell_{E,b}\ln(1/c),
 w_{\rm TAT},
 w_Z
\right].
}
```

Therefore, in the constant-`v_K` kinematic model,

```math
\boxed{
T_{\rm total}
\ge
\frac1{v_K}
\left[
\ell_{E,a}r_{\min}
+
\max\left(
\ell_{E,b}\ln(1/c),
 w_{\rm TAT},
 w_Z
\right)
\right].
}
```

This is conditional and generally optimistic; real scattering and diffusion can increase the time.

---

## 14. Current dimensionless phase map

Define absorber mean-II margin

```math
\boxed{
\mathcal M_{\rm II}
=
\frac{\chi(1-\zeta)}
{\zeta(1-e^{-r})/r}.
}
```

Define boundary local-tunneling voltage margin

```math
\boxed{
\mathcal M_b
=
\frac{q\int_0^wF_{\rm allow}(x)dx}
{\alpha\Delta E_g^{(b)}}.
}
```

The idealized minimum-compensation device is conditionally feasible only when

```math
\boxed{
\mathcal M_{\rm II}\ge1,
\qquad
\mathcal M_b\ge1.
}
```

Normalize latency by absorber relaxation length:

```math
\Theta
=T_{\rm total}v_K/\ell_{E,a}.
```

Then

```math
\boxed{
\Theta_{\min}
=
r_{\min}
+
\max\left[
\rho_E\ln(1/c),
\nu_{\rm TAT},
\nu_Z
\right],
}
```

where `rho_E=ell_E,b/ell_E,a` and the `nu` terms are boundary width requirements normalized by `ell_E,a`.

This three-coordinate representation

```math
\boxed{
(\mathcal M_{\rm II},\mathcal M_b,\Theta_{\min})
}
```

is the current organizing device model.

---

## 15. Important stopped shortcuts

Do not restart casually:

- active-volume-only theorem;
- finite absorber count as a one-photon speed limit;
- largest internal coupling as a universal parameter;
- finite internal rank as always-on detector capacity;
- universal active `pump ~ W^2` law;
- spectral FWHM as arbitrary transport speed;
- low-field mobility extrapolated into high-field HgCdTe;
- direct BTBT assumed first high-field limiter;
- bulk II onset treated as a finite-device threshold;
- nonuniform field alone assumed beneficial in homogeneous material;
- pure grading assumed to eliminate all leakage;
- delta doping assumed to eliminate compensation field;
- local `F_II(x)` used without local-equilibrium justification;
- minimum-compensation boundary treated as a zero-time cooling sink.

---

## 16. Current missing inputs

Need target-composition data for

```text
ell_E(E,x) / energy-loss rate
+
Gamma_II(E,x)
+
boundary trap energies, densities, occupations, capture cross sections
+
finite self-consistent band profile under doping and bias
+
high-field velocity / transport law for actual transit time.
```

Do not invent interpolation coefficients from narrative literature statements.

---

## 17. Current numerical regressions

Relevant checks include

```text
numerics/hgcdte_dimensionless_device_phase_map.py
numerics/hgcdte_ii_safe_transit_ceiling.py
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
numerics/hgcdte_graded_kane_wkb.py
numerics/hgcdte_field_profile_variational.py
numerics/hgcdte_nonlocal_ii_surrogate.py
numerics/hgcdte_btbt_normalized_sweep.py
```

No CI is justified yet.

---

## 18. Next decisive work

Do **not** jump to a manuscript.

Use the phase map to attack the next design degree of freedom:

> **How should a finite available composition / bandgap excursion be split between downhill absorber grading (which accelerates electrons but consumes hot-electron margin) and the wider-gap collection boundary (which improves local tunneling tolerance but requires compensation voltage and cooling length)?**

That optimization should remain dimensionless first.

Then test it against

- nonlinear composition profiles;
- realistic `N_A(x)` / density-of-states variation;
- overcompensated boundaries;
- measured trap spectra;
- stochastic II tails;
- self-consistent bias-dependent electrostatics.

Only after those attacks should publication significance be reassessed.
