# Gedanken 2

First-principles thought experiments in photodetector physics.

The repository follows the physics rather than a predetermined theorem. Failed conjectures, counterexamples, and prior-art collisions are preserved because they define the actual result.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, fast, sensitive, and perfectly absorbing?

The original active-volume route failed. The research moved through optical access, microscopic transitions, passive/active network resources, adaptive control, semiconductor contacts, high-field transport, tunneling, and finally **HgCdTe band-structure engineering**.

## Current frontier

The active question is now:

> **Can a graded HgCdTe absorber use band-structure drive for fast minority-electron collection without entering the nonlocal hot-electron / impact-ionization regime, while a separate wide-gap boundary carries the unavoidable electrostatic voltage without excessive TAT or direct BTBT?**

There is still **no manuscript**.

## Current physical picture

For a quasi-neutral p-type graded absorber, the majority-hole band can be nearly pinned while a decreasing band gap makes the conduction band slope downhill for minority electrons:

```math
E_v\approx\text{constant},
\qquad
S_c\approx -dE_g/dx.
```

This strongly suppresses the ordinary same-direction direct-Zener geometry in the repository two-band/Kane model.

But the same conduction-band slope still supplies energy to the useful electron.

The mean nonlocal energy state is

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

For a linear graded absorber,

```math
E_g(x)=E_{g0}-Gx,
```

constant `ell_E`, and local II threshold

```math
E_{\rm th}=\chi E_g,
```

define

```math
\zeta=\Delta E_g/E_{g0},
\qquad
r=L/\ell_E.
```

The exact deterministic mean-energy phase boundary is

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r}.
}
```

Mean threshold access occurs when

```math
\zeta\ge\zeta_{\rm II}.
```

### Ballistic interpretation

For `r -> 0`,

```math
\boxed{
\zeta_{\rm II}\to\frac{\chi}{1+\chi}.
}
```

For the common simplified choice `chi=1`, this means the graded accelerator reaches the mean II threshold after roughly one half of the entrance gap has been removed.

Equivalently,

```math
\boxed{
E_{g,\rm in}\lesssim2E_{g,\rm out}
}
```

or approximately

```math
\boxed{
\lambda_{c,\rm in}\gtrsim\lambda_{c,\rm out}/2
}
```

for the ballistic mean-threshold-safe regime.

This is a conditional design rule, not a universal HgCdTe factor-of-two law.

## Relaxation converts the phase boundary into a time scale

When the grading span exceeds the ballistic-safe value, define

```math
\boxed{
a=\chi(1-\zeta)/\zeta.}
```

Then the minimum relaxation ratio satisfying the mean-energy condition is

```math
\boxed{
r_{\min}
=\frac1a
+W_0\!\left[-\frac1a e^{-1/a}\right].
}
```

Thus

```math
\boxed{L\ge\ell_Er_{\min}.}
```

Within the simplified two-band/Kane dispersion, `|v_g|<v_K`, giving the kinematic lower bound

```math
\boxed{
T_{\rm tr}\ge\frac{\ell_E}{v_K}r_{\min}.
}
```

This exposes the current missing material parameter directly: the target-composition energy-relaxation length.

## Collection boundary

A wider-gap boundary with gap increase `Delta Eg_b` and conduction-band share `alpha` requires

```math
\boxed{qV_b\ge\alpha\Delta E_g^{(b)}}
```

for barrier-free minority-electron extraction.

No one-dimensional electrostatic profile can avoid the integral field requirement

```math
\boxed{F_{\max}\ge V_b/w.}
```

For local TAT/BTBT constraints, define a local allowable field `F_allow(x)`. The boundary is feasible only if

```math
\boxed{
V_b\le\int_0^wF_{\rm allow}(x)dx.
}
```

At minimum compensation,

```math
qV_b=\alpha\Delta E_g^{(b)},
```

the net conduction-band step is flat. The boundary then adds no downhill carrier work; the electron can relax while the local gap rises.

So the emerging architecture is

```text
quasi-neutral graded absorber
-> fast band-structure drive
-> direct-Zener suppression
-> nonlocal hot-electron constraint

wide-gap collection boundary
-> unavoidable electrostatic voltage
-> field placed in high-gap / low-defect material
-> local TAT/BTBT constraint
-> hot-electron relaxation at minimum compensation.
```

## Major prior-art boundary

The ingredients are not individually new. Existing HgCdTe literature already covers graded-gap carrier drive, heterojunction/barrier engineering, TAT/BTBT, dead-space/impact-ionization physics, and energy-dependent Monte Carlo APD transport.

The repository currently treats its closed-form reductions as **derived conditional results with unassessed priority**, not novelty claims.

## Publication status

> **Continue the research. Do not write a manuscript yet.**

The next useful output is a finite-device phase map comparing

```text
transit time
+
local TAT/BTBT margin
+
nonlocal carrier-energy / II margin.
```

The main missing quantitative input is a trustworthy energy-relaxation and energy-dependent II model for the target narrow-gap HgCdTe composition near 77 K.

## Canonical files

Start with:

- [`AGENTS.md`](AGENTS.md)
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)
- [`HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`](experiments/01-vanishing-absorber/HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md)
- [`HGCDTE_II_SAFE_TRANSIT_CEILING.md`](experiments/01-vanishing-absorber/HGCDTE_II_SAFE_TRANSIT_CEILING.md)
- [`HGCDTE_BALLISTIC_GRADING_SPAN_RULE.md`](experiments/01-vanishing-absorber/HGCDTE_BALLISTIC_GRADING_SPAN_RULE.md)
- [`HGCDTE_GRADED_ABSORBER_BOUNDARY_RELAXATION.md`](experiments/01-vanishing-absorber/HGCDTE_GRADED_ABSORBER_BOUNDARY_RELAXATION.md)
- [`HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md`](experiments/01-vanishing-absorber/HGCDTE_QUASINEUTRAL_GRADING_SELF_CONSISTENCY.md)
- [`HGCDTE_LINEAR_GRADED_KANE_WKB.md`](experiments/01-vanishing-absorber/HGCDTE_LINEAR_GRADED_KANE_WKB.md)
- [`HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`](experiments/01-vanishing-absorber/HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md)
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)

New agents should read `AGENTS.md` first.
