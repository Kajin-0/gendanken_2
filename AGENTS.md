# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; passive/autonomous baseline mapped; active and time-dependent capture under adversarial audit; no novelty claim**  

Read this file first.

The project starts from thought experiments and follows the physics. Counterexamples are progress. Do not force the work toward the original active-volume idea or toward a paper.

---

## 1. Mandatory repository protocol

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes if needed;
3. fetch the exact current blob SHA immediately before replacing a file;
4. never overwrite a stale SHA;
5. preserve concurrent work and failed branches.

**Live `main` overrides all snapshots.**

---

## 2. Mandatory epistemic labels

Use explicitly:

- **known result**;
- **derived result**;
- **checked result**;
- **candidate distinct lemma — priority unproven**;
- **conjecture**;
- **model assumption**;
- **invalidated result**;
- **superseded result**;
- **open question**.

Never convert a negative literature search into a novelty claim.

No `new`, `first`, `fundamental`, or `universal` language without a focused primary-source audit and `CLAIM_LEDGER.md` update.

---

## 3. Current path

```text
weak passive resonance
-> bandwidth penalty in loss rate

active volume
-> killed by field concentration

finite absorber number
-> killed as one-photon speed resource

finite transition / LDOS / emitter extent
-> conditional bounds, then perturbative theory fails

nonperturbative Hopfield
-> dressed external access can collapse

multimode passive network
-> exact harmonic integrated-transfer access law

direct feedthrough / structured continuum
-> scope/resource audits

passive optical access + autonomous detector thermodynamics
-> coherent junction mapped, but publication audit says not manuscript-ready

active frequency conversion
-> pump coupling buys bandwidth; architecture-level resource laws

known-time dynamic loading
-> arbitrary temporal-mode matching possible with controlled coupling
-> bounded coupling x loading-time resource

unknown arrival
-> finite storage has temporal-mode rank limit
-> always-on detector requires many output modes / irreversible continuum
-> accepted thermal modes create background and dead-time occupancy

CURRENT FRONTIER
-> common space-time mode resource law for actively controlled always-on detection.
```

---

## 4. Canonical finite passive theorem

Read `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md`.

For a finite stable passive strictly proper network,

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R,
```

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R}.
}
```

In the controllability-Gramian eigenbasis,

```math
\boxed{
\frac{\mathcal I}{2}
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

For band width `W`,

```math
\boxed{
\overline T_B
\le
\frac{4\pi LR}{W(L+R)}.
}
```

Interpret as an external-access resource law, not an absolute bandwidth theorem.

The math uses standard `H2`/Lyapunov/passivity machinery. Novelty is not claimed.

---

## 5. Important passive scope limits

### Direct feedthrough

A frequency-independent prompt path makes the all-frequency `H2` area divergent; it inserts infinite Markov bandwidth.

For finite band `W`,

```math
\sqrt{\mathcal I_B}
\le
\sqrt{W/(2\pi)}\|D_{RL}\|_F
+
\sqrt{2LR/(L+R)}.
```

### Structured reservoirs

The harmonic theorem survives passive finite-budget `H2`-convergent augmentations. A continuum escape must violate those assumptions or use active/nonlinear/time-dependent physics.

---

## 6. Current prior-art boundary

### Young, Sarovar & Leonard (2018)

Already unify incoming quantized photon fields, absorption, amplification/monitored states, efficiency, dark counts, and timing.

### Schwarzhans et al. (2026)

Already treat autonomous nonequilibrium detector work source, amplification/reset, entropy production, internal dark counts, jitter and dead time.

Do not reinvent either as novelty.

The narrowed candidate gap is spectral/passive capture-resource constraints **plus** autonomous thermodynamic detector accounting. A targeted search has not found the exact intersection; priority remains unproven.

`PUBLICATION_BOUNDARY_AUDIT.md` currently says **continue research; do not write a manuscript yet**.

---

## 7. Active frequency-conversion branch

Read:

- `ACTIVE_FREQUENCY_CONVERTER_BASELINE.md`
- `MULTIMODE_ACTIVE_PUMP_RESOURCE.md`
- `TRAVELING_WAVE_ACTIVE_CONVERTER.md`
- `ACTIVE_CONVERSION_SINGULAR_VALUE_BOUND.md`

Two-mode critical converter:

```math
G_{\min}=W/(2\sqrt2).
```

For `G=g_0 sqrt(N_p)`,

```math
N_p\ge W^2/(8g_0^2).
```

This `W^2` scaling is architecture specific, not universal.

Finite-mode singular-value resource:

```math
H_{\rm conv}/\hbar
=\mathbf b^\dagger K\mathbf a+h.c.
```

If `M_c` orthogonal conversion channels each achieve efficiency `eta` in time `tau`,

```math
\boxed{
\|K\|_F^2
\ge
\frac{M_c}{\tau^2}
\arcsin^2\sqrt\eta.
}
```

For pump amplitudes `alpha_p`,

```math
K=\sum_p\alpha_pK_p,
\qquad
N_p=\sum_p|\alpha_p|^2,
```

```math
C_{pq}=\operatorname{Tr}(K_p^\dagger K_q),
\qquad
\Lambda=\lambda_{\max}(C),
```

```math
\boxed{
N_p
\ge
\frac{M_c\arcsin^2\sqrt\eta}
{\Lambda\tau^2}.
}
```

Schmidt-mode conversion is established prior theory. `Lambda` remains an unbounded device/material resource in the current analysis.

---

## 8. Time-dependent known-mode capture

Read `TIME_DEPENDENT_CAPTURE_AUDIT.md`.

For one controlled lossless storage mode,

```math
\dot a=-\kappa(t)a+\sqrt{2\kappa(t)}s_{\rm in}.
```

Perfect zero-reflection loading requires

```math
\boxed{
\kappa(t)
=
\frac{P_{\rm in}(t)}
{2\int_{-\infty}^{t}P_{\rm in}(t')dt'}.
}
```

Finite-support pulses with ordinary hard leading edges generically require singular ideal coupling.

With `kappa <= kappa_max` during duration `tau`,

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

Dynamic single-photon capture is established prior research. Do not claim novelty.

---

## 9. Unknown arrival / temporal-mode capacity

Read `TEMPORAL_UNCERTAINTY_MODE_CAPACITY.md`.

For a fixed linear capture map into `r` coherent storage modes and `M` orthogonal possible temporal input modes,

```math
\boxed{
\sum_j\eta_j\le r.
}
```

Hence uniform efficiency requires

```math
\boxed{r\ge M\eta,}
```

and equal-prior average efficiency obeys

```math
\boxed{\overline\eta\le r/M.}
```

This is why known-time dynamic loading is not an always-on detector counterexample.

To cover many possible arrival modes, add storage dimension, adaptation, repeated reset/reuse, or an irreversible output continuum.

---

## 10. Always-on thermal-mode / dead-time result

Read `ALWAYS_ON_TEMPORAL_COVERAGE.md`.

For `M` accepted modes with thermal occupation at least `nbar` and efficiency `eta`,

```math
N_{\rm bg}\ge\bar nM\eta.
```

In a long-time one-channel band of angular width `W`,

```math
R_{\rm bg}\simeq\bar n\eta W/(2\pi).
```

In the stated minimal nonparalyzable model with dead time `tau_d`, an otherwise perfect raw detector obeys

```math
\boxed{
\eta_{\rm ext}
\le
\frac1{1+\bar nW\tau_d/(2\pi)}.
}
```

This is model-level background blocking, not a universal dead-time theorem.

---

## 11. Invalidated routes — do not restart casually

- active-volume-only theorem;
- finite absorber number as missing one-photon speed limit;
- largest internal coupling as universal multimode parameter;
- `2 min(L,R)` bound (superseded by harmonic bound);
- all-frequency harmonic theorem with ideal feedthrough;
- generic capture+amplification novelty;
- generic autonomous thermodynamic detector novelty;
- universal active `pump ~ W^2` law;
- treating known-time dynamic matching as an always-on broadband detector solution.

---

## 12. Current next step

Do **not** jump to a manuscript.

Try to formulate—and then break—a common **space-time mode resource law** for an actively controlled always-on detector.

The candidate resource accounting should include

1. accepted spatiotemporal mode count;
2. pump/control norm;
3. irreversible detector-output capacity;
4. background occupation of accepted modes;
5. reset/dead-time resource.

Before promoting any theorem, attack it with

- noncommuting time-dependent controls;
- adaptive/measurement-based coupling;
- active feedforward;
- time-switched energy trapping;
- output continua with large mode rank.

Do not add HgCdTe-specific transport until this abstract detector-resource question has either survived or failed.