# Gedanken 2

First-principles thought experiments in photodetector physics.

The repository follows the physics rather than a predetermined theorem. Failed conjectures and prior-art collisions are preserved because they define the actual result.

## Experiment 01 — The vanishing absorber

> Can an ideal photodetector be made arbitrarily small, fast, sensitive, and perfectly absorbing?

The original active-volume route failed. The research has moved through optical access, quantum limits, active control, semiconductor contacts, high-field transport, tunneling, and finally **HgCdTe band-structure engineering**.

## Current frontier

The active question is now:

> **Can a graded HgCdTe energy landscape provide the carrier-driving slope needed for fast collection while suppressing the direct Zener path that accompanies a homogeneous electrostatic field?**

### Homogeneous field shaping cannot help by itself

For homogeneous

```math
v(F)=\mu F/[1+(F/d)^r],
```

and local WKB leakage

```math
g(F)=AF^pe^{-K/F},
```

uniform field is the unique leakage-minimizing profile at fixed transit time.

So useful field engineering requires spatially varying material/defect/transport physics—not merely a nonuniform `F(x)`.

### Heterostructure field allocation

At a transit-constrained optimum,

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda.
}
```

Field belongs where the marginal leakage cost of improving transit is smallest.

For ohmic spatial transport,

```math
\boxed{
VT
\ge
\left[\int_0^L\frac{dx}{\sqrt{\mu(x)}}\right]^2.
}
```

Thus protecting a fragile region by field redistribution generally consumes extra bias.

## Strongest current model-level result

Use the two-band/Kane landscape

```math
(E-U)^2
=\Delta^2+(\hbar v_Kk)^2,
\qquad
E_g=2\Delta.
```

For linear band edges

```math
E_c=E_{c0}-S_cx,
\qquad
E_v=E_{v0}-S_vx,
```

the direct WKB action is exactly

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

Decompose the useful conduction slope into common tilt plus gap grading:

```math
S_c=S_U+S_\Delta.
```

Hold `S_c=S` fixed and define

```math
\eta=S_\Delta/S.
```

For

```math
0\le\eta<1/2,
```

```math
\boxed{
\frac{\mathcal S_Z(\eta)}
{\mathcal S_Z(0)}
=
\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}.
}
```

This ratio is strictly increasing.

So, in the ideal linear two-band model:

> **At the same conduction-band downhill slope, replacing common electrostatic tilt with a decreasing gap strictly suppresses the conventional direct Zener path.**

As `eta -> 1/2-`, the valence turning point recedes and the action diverges. For stronger grading, if the finite region remains positive-gap, that specific two-turning-point direct-Zener path is absent inside the model.

This does **not** eliminate TAT, interface tunneling, or impact ionization.

## Why HgCdTe is relevant

Compositionally graded HgCdTe is established technology. Primary work reports gradient-induced built-in/quasi-electric fields affecting carrier transport, graded-band devices designed for faster carrier evacuation, and recent graded-composition HgCdTe APDs that use band-structure engineering to guide carriers while controlling dark-current mechanisms.

The exact fixed-conduction-slope WKB ratio above has **unassessed priority**. Graded-gap HgCdTe, WKB analysis and Kane/Zener tunneling are established prior physics. No novelty claim is made.

## Competing material mechanisms

The project retains separate models for

```text
trap-assisted tunneling
nonlocal impact ionization / dead space
direct BTBT
high-field velocity saturation
```

because no one mechanism is universally dominant.

## Publication status

There is still **no manuscript**.

The graded-action result must first survive

1. realistic HgCdTe band-offset partition;
2. finite endpoint gaps;
3. self-consistent Poisson electrostatics;
4. TAT/interface-state attack;
5. nonlocal impact-ionization attack;
6. deeper prior-art collision.

## Start here

- [`AGENTS.md`](AGENTS.md)
- [`CURRENT_STATE.md`](experiments/01-vanishing-absorber/CURRENT_STATE.md)
- [`CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/CLAIM_LEDGER.md)
- [`HGCDTE_LINEAR_GRADED_KANE_WKB.md`](experiments/01-vanishing-absorber/HGCDTE_LINEAR_GRADED_KANE_WKB.md)
- [`HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md`](experiments/01-vanishing-absorber/HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md)
- [`HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md`](experiments/01-vanishing-absorber/HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md)
- [`HGCDTE_TAT_FIELD_SCALE.md`](experiments/01-vanishing-absorber/HGCDTE_TAT_FIELD_SCALE.md)
- [`HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`](experiments/01-vanishing-absorber/HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md)
- [`RESEARCH_LOG.md`](experiments/01-vanishing-absorber/RESEARCH_LOG.md)
