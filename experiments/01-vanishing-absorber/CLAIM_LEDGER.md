# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory; passive/autonomous baseline mapped; active/time-dependent escapes under audit; no novelty claim  
**Purpose:** separate known ingredients, internally derived results, invalidated routes, model-level compositions, and open claims.

---

## 1. Current organizing variables

The original active-volume target has been replaced by

```text
optical access
+
detector-side irreversible access
+
active pump/control resource
+
number of accepted spatiotemporal modes
+
ready/reset capacity
+
external background occupation.
```

---

## 2. Established prior ingredients — not novelty targets

Do not claim novelty for

- temporal coupled-mode theory / critical coupling;
- propagating few-photon detector models with absorption and amplification (Young, Sarovar & Leonard 2018);
- autonomous detector thermodynamics, internal dark counts, jitter/dead time and entropy production (Schwarzhans et al. 2026);
- `H2`/Lyapunov/passive-system theory;
- LDOS/material power-bandwidth bounds;
- broadband thermodynamic optical-coupling bounds;
- Bode-Fano passive matching limits and active/time-modulated violations;
- deep-strong light-matter decoupling;
- quantum frequency conversion, Schmidt/temporal conversion modes and pump-shaped converters;
- dynamically impedance-matched single-photon absorption;
- multimode quantum-memory / time-bandwidth capacity;
- local detailed balance, optical Bloch response and stochastic thermodynamics.

---

## 3. Invalidated / stopped general routes

### H1 — active-volume-only theorem — STOPPED

An explicit field-concentrating continuum family has

```math
V_a\to0,
\qquad
\gamma_a/V_a\to\infty.
```

Do not revive universal `eta^2 B <= C V_a` without new explicit constraints.

### H2 — finite absorber count as one-photon speed limit — STOPPED

The one-photon one-excitation sector remains linear.

### H3 — largest multimode internal coupling as universal control parameter — STOPPED

Spectator strong-coupling sectors are counterexamples.

### H4 — all-frequency passive harmonic theorem with arbitrary ideal feedthrough — INVALID EXTENSION

A constant prompt transfer block carries infinite Markov bandwidth.

### H5 — generic propagating-field capture + amplification as novelty — STOPPED

Young et al. 2018 already cover it.

### H6 — generic autonomous thermodynamic detector cycle as novelty — STOPPED

Schwarzhans et al. 2026 already cover it.

### H7 — universal `pump resource ~ W^2` active theorem — NOT SUPPORTED

`W^2` appears in particular cavity and first-order traveling-wave architectures but the exponent depends on mode allocation, interaction time, dispersion, and control architecture.

---

## 4. Canonical passive finite-network result

For a finite stable passive strictly proper network,

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

and

```math
\mathcal I_{L\to R}
=\int\frac{d\omega}{2\pi}
\operatorname{Tr}[G_{RL}^\dagger G_{RL}],
```

### D1 — exact Gramian decomposition

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

### D2 — harmonic access bound

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

A single passive resonance saturates it.

### D3 — fixed-band access requirement

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Thus target `Tbar_B >= T_*` requires

```math
\boxed{
\frac{LR}{L+R}
\ge
\frac{T_*W}{4\pi}.
}
```

**Status:** exact internally derived detector-facing passivity corollary; mathematical ingredients prior; exact formula priority unassessed; no novelty claim.

---

## 5. Passive scope results

### D4 — finite-band direct feedthrough accounting

For

```math
G_{RL}=D_{RL}+G_{\rm res},
```

```math
\boxed{
\sqrt{\mathcal I_B}
\le
\sqrt{\frac{W}{2\pi}}\|D_{RL}\|_F
+
\sqrt{\frac{2LR}{L+R}}.
}
```

### D5 — conditional structured-reservoir extension

If finite passive augmented models converge in `H2` with finite limiting terminal budgets,

```math
\boxed{
\|G\|_{H2}^2
\le
\frac{2LR}{L+R}.
}
```

---

## 6. Restricted passive optical-to-thermal compositions

Prior one-free-space-channel coupling theory gives, in amplitude-rate convention,

```math
L_B\le W/(4\pi).
```

### D6 — detector-side access requirement

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

### D7 — thermal reverse-activation requirement

For energy release `Delta`,

```math
k_\uparrow/k_\downarrow=e^{-\Delta/(k_BT)},
```

and with `k_down=2R_B`,

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}e^{-\Delta/(k_BT)}.
}
```

Reverse activation is not automatically an observable dark count.

---

## 7. Unified passive/autonomous detector testbed

For the three-level machine

```text
|0> reset/ground
|1> ready
|2> optical activation
```

### D8 — ready-state frequency-converting capture

```math
\boxed{
T_{L\to R}(\omega)
=
\frac{4\Gamma_L\Gamma_R}
{(\omega-\omega_L)^2
+(\Gamma_L+\Gamma_R+\Gamma_I)^2}.
}
```

### D9 — gross forward click versus net current

For reversible rates `u,d,a,b,c,e` and

```math
Z=ac+ae+au+bd+be+bu+cd+cu+de,
```

```math
\boxed{
R_+
=\frac{c(ae+au+de)}{Z},
}
```

```math
\boxed{
J_D
=\frac{uac-dbe}{Z}.
}
```

These are distinct observables when reverse jumps matter.

### D10 — readiness factor

```math
p_r
=\frac1{1+e^{-\mathcal A_r}},
\qquad
\mathcal A_r=\ln(u/d).
```

In the dilute serial reference limit,

```math
\boxed{
\overline\eta_{\rm ext}
\le
\frac{\eta_D}{1+e^{-\mathcal A_r}}
\frac{R_C}{R_C+W/(4\pi)}.
}
```

### D11 — non-inverted NESS optical response

```math
\boxed{
\rho_{21}^{(1)}
=
\frac{i\Omega}{2}
\frac{p_1-p_2}{\gamma_\perp+i\Delta}.
}
```

In the absorbing regime,

```math
0\le p_1-p_2\le1.
```

Incoherent readiness pumping cannot exceed the fully ready absorptive population factor. True optical inversion/gain is a distinct active resource.

---

## 8. Supporting Hopfield results

### D12 — fixed-target retuning no-go

For fixed lower dressed target `omega_t`, fixed local bath resources and `g -> infinity`,

```math
\boxed{
\min(\Gamma_L,\Gamma_R)\to0.
}
```

**Status:** candidate distinct supporting lemma; priority unproven.

### D13 — reservoir compensation

For target peak/linewidth, at least one bare bath resource grows as

```math
\boxed{
\max(\gamma_L,\gamma_R)
\ge
\Gamma_*\sqrt{1+2g/\omega_t}.
}
```

---

## 9. Active frequency-conversion results

### D14 — two-mode pumped converter

```math
\boxed{
T(\delta)
=
\frac{4G^2\Gamma_a\Gamma_b}
{|(\Gamma_a-i\delta)(\Gamma_b-i\delta)+G^2|^2}.
}
```

Unit peak requires

```math
G^2=\Gamma_a\Gamma_b.
```

For target unit-peak FWHM `W`, the minimum `G` is

```math
\boxed{
G_{\min}=W/(2\sqrt2)
}
```

at `Gamma_a=Gamma_b=G`.

If `G=g_0 sqrt(N_p)`,

```math
\boxed{
N_p\ge W^2/(8g_0^2).
}
```

**Status:** architecture baseline with direct quantum-frequency-conversion prior art; not a novelty target.

### D15 — discrete multimode pump allocation

If independent subchannels satisfy `N_i >= W_i^2/(8g_i^2)` and

```math
\sum_i g_i^2\le G_0^2,
```

then

```math
\boxed{
N_{p,\rm tot}
\ge
W^2/(8G_0^2).
}
```

Conditional on finite aggregate nonlinear coupling resource.

### D16 — traveling-wave local-dispersion scaling

If

```math
\Delta k(\delta)\simeq D_m\delta^m/m!,
```

then shortest-branch unit conversion with FWHM `W` requires

```math
\boxed{
q
=
\frac{\pi|D_m|}
{2^{m+2}m!x_{1/2}}
W^m,
\qquad
x_{1/2}\approx1.25457202234609.
}
```

Pump flux scales as `W^(2m)` within this architecture. Not universal.

---

## 10. Active singular-value pump resource

For finite number-conserving pumped conversion,

```math
H_{\rm conv}/\hbar
=\mathbf b^\dagger K\mathbf a+h.c.
```

If `M_c` orthogonal singular channels each need efficiency at least `eta` in time `tau`,

```math
\boxed{
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
}
```

If

```math
K=\sum_p\alpha_pK_p,
\qquad
N_p=\sum_p|\alpha_p|^2,
```

with

```math
C_{pq}=\operatorname{Tr}(K_p^\dagger K_q),
\qquad
\Lambda=\lambda_{\max}(C),
```

then

```math
\boxed{
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\Lambda\tau^2}.
}
```

Schmidt-mode conversion is established prior theory. The finite-pump bookkeeping has unassessed priority.

`Lambda` remains an unbounded device/material resource in the current analysis.

---

## 11. Time-dependent known-mode capture

For one lossless time-controlled storage mode,

```math
\dot a=-\kappa(t)a+\sqrt{2\kappa(t)}s_{\rm in},
```

### D17 — exact zero-reflection schedule

```math
\boxed{
\kappa_{\rm perfect}(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
}
```

Hard finite pulse onsets generically make this coupling singular.

### D18 — bounded-coupling loading limit

If `0 <= kappa(t) <= kappa_max` for loading duration `tau`,

```math
\boxed{
\eta_{\rm cap}
\le
1-e^{-2\kappa_{\max}\tau}.
}
```

Thus

```math
\boxed{
\kappa_{\max}\tau
\ge
\frac12\ln\frac1{1-\eta}.
}
```

Dynamic perfect capture is established prior theory; these identities are supporting time-domain resource statements, not novelty claims.

---

## 12. Temporal uncertainty / storage-mode capacity

For a fixed linear capture map into `r` coherent storage dimensions and `M` orthogonal possible temporal input modes,

### D19 — exact mode-sum bound

```math
\boxed{
\sum_{j=1}^{M}\eta_j\le r.
}
```

Hence uniform target efficiency requires

```math
\boxed{r\ge M\eta,}
```

and equal-prior average efficiency obeys

```math
\boxed{\overline\eta\le r/M.}
```

Arrival-time prior information is therefore a resource. This is a linear-algebra/multimode-capacity statement, not a novelty claim.

---

## 13. Always-on temporal coverage and background/dead time

If `M` accepted temporal modes have thermal occupation at least `nbar` and signal efficiency at least `eta`,

```math
\boxed{
N_{\rm bg}\ge\bar n M\eta.
}
```

In the long-time one-channel continuum limit,

```math
R_{\rm bg}\simeq\bar n\eta W/(2\pi).
```

For the stated minimal nonparalyzable dead-time model with otherwise perfect raw efficiency,

```math
\boxed{
\eta_{\rm ext}
\le
\frac1{1+\bar n W\tau_d/(2\pi)}.
}
```

**Status:** model-level composition of accepted thermal modes and dead-time blocking; not universal.

---

## 14. Publication status

`PUBLICATION_BOUNDARY_AUDIT.md` verdict:

> **continue research; do not write a manuscript yet.**

Current passive/autonomous results are coherent but vulnerable to the criticism that they are corollaries/compositions of established theories. A stronger new result should quantify the resource required to beat the passive envelope.

---

## 15. Explicit non-claims

Do not claim

- a universal sensitivity-speed-dark-count-entropy theorem;
- novelty of the harmonic passive bound;
- novelty of dynamic single-photon capture;
- a universal active `W^2` pump law;
- a universal bound on nonlinear coupling resource `Lambda`;
- a universal dead-time formula;
- that known-time dynamic loading solves unknown-arrival photodetection;
- a material-specific infrared limit;
- publication priority of the passive/autonomous or active-mode-resource junctions.

---

## 16. Current frontier

The next candidate generalization is a **space-time mode resource law** for an actively controlled always-on detector.

A useful theorem would have to place, in one inequality,

```text
accepted spatiotemporal mode count
+
pump/control norm
+
irreversible output capacity
+
background occupation
```

without assuming a particular cavity, waveguide, gating schedule, or known arrival time.

Before promoting such a statement, actively search for counterexamples using noncommuting time-dependent control, adaptive feedback, and continuously monitored output reservoirs.