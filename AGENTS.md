# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gendanken_2`  
**Active experiment:** `experiments/01-vanishing-absorber/`  
**Current mode:** **open theoretical exploration; active frontier is graded-band HgCdTe transport versus Zener/TAT/nonlocal II; no novelty claim**

Read this file first.

## 1. Repository discipline

Before every write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch exact current blob SHA before replacing a file;
4. never overwrite stale state;
5. preserve failed/corrected branches;
6. make narrow edits.

**Live `main` overrides all snapshots.**

## 2. Epistemic labels

Use explicitly:

- **KNOWN**
- **DERIVED**
- **CHECKED**
- **CONDITIONAL**
- **INVALIDATED**
- **OPEN**
- **NON-CLAIM**

A negative literature search is not novelty evidence.

Do not use `first`, `new fundamental`, `universal`, etc. without a focused primary-source audit and `CLAIM_LEDGER.md` update.

## 3. Current path

```text
active-volume thought experiment
-> volume bound killed by field concentration

finite absorber / LDOS / ultrastrong coupling
-> successive microscopic loopholes

finite passive network
-> harmonic two-access transfer-area theorem

active/adaptive/time-dependent control
-> pump, timing, storage and output-record resources

semiconductor contact / filters
-> detailed balance, lifetime broadening, delay

HgCdTe field-driven collection
-> normalized direct BTBT

bulk II onset
-> corrected by finite dead space / energy history

TAT
-> defect-mediated partial-gap tunneling can precede direct BTBT

homogeneous field shaping
-> cannot beat local speed–WKB leakage trade at fixed transit time

heterostructure allocation
-> field belongs where marginal leakage cost is smallest

bandgap grading
-> CURRENT FRONTIER: exact linear graded-gap Kane WKB action at fixed conduction-band drive.
```

## 4. Canonical reading order

1. `AGENTS.md`
2. `README.md`
3. `experiments/01-vanishing-absorber/CURRENT_STATE.md`
4. `experiments/01-vanishing-absorber/CLAIM_LEDGER.md`
5. `experiments/01-vanishing-absorber/HGCDTE_LINEAR_GRADED_KANE_WKB.md`
6. `experiments/01-vanishing-absorber/HGCDTE_BANDGAP_GRADIENT_ESCAPE_AUDIT.md`
7. `experiments/01-vanishing-absorber/HGCDTE_FIELD_PROFILE_VARIATIONAL_BOUND.md`
8. `experiments/01-vanishing-absorber/HGCDTE_TWO_REGION_FIELD_ALLOCATION.md`
9. `experiments/01-vanishing-absorber/HGCDTE_VOLTAGE_TRANSIT_FIELD_ALLOCATION.md`
10. `experiments/01-vanishing-absorber/HGCDTE_TAT_FIELD_SCALE.md`
11. `experiments/01-vanishing-absorber/HGCDTE_NONLOCAL_IONIZATION_SURROGATE.md`
12. `experiments/01-vanishing-absorber/RESEARCH_LOG.md`
13. `experiments/01-vanishing-absorber/ARCHIVE_STATUS.md`

There is still **no manuscript**.

## 5. Strongest current model-level result

Use the two-band/Kane dispersion

```math
(E-U)^2
=\Delta^2+(\hbar v_Kk)^2,
\qquad E_g=2\Delta.
```

For linear edges

```math
E_c=E_{c0}-S_cx,
\qquad
E_v=E_{v0}-S_vx,
```

with `S_c,S_v>0`, the exact WKB action is

```math
\boxed{
\mathcal S(E)
=\frac{\pi\sqrt{S_cS_v}}
{4\hbar v_K}(x_c-x_v)^2.
}
```

The uniform-gap/common-field limit recovers

```math
\boxed{
\mathcal S_0
=\frac{\pi E_g^2}
{4q\hbar v_KF}.
}
```

Decompose

```math
S_c=S_U+S_\Delta,
\qquad
S_v=S_U-S_\Delta.
```

Hold useful conduction slope `S_c=S` fixed and define

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
=\frac{(1-\eta)^2}
{(1-2\eta)^{3/2}}.
}
```

It is strictly increasing:

```math
\boxed{
\frac{d\ln R}{d\eta}
=\frac{1+\eta}
{(1-\eta)(1-2\eta)}>0.
}
```

As `eta -> 1/2-`, the valence turning point recedes and the direct linear-profile action diverges.

For `eta >= 1/2`, if a finite graded region remains positive-gap and ends before gap closure, the ordinary same-energy two-turning-point direct-Zener path is absent inside this ideal model.

**Status:** DERIVED / CHECKED / CONDITIONAL. Graded-gap/WKB/Kane ingredients are prior physics; exact fixed-conduction-slope ratio has unassessed priority.

## 6. Physical interpretation

At fixed useful conduction-band downhill slope:

```text
common-mode tilt U'
-> drives conduction edge
-> also tilts valence edge toward spatial overlap
-> direct Zener path

gap gradient Delta'
-> drives conduction edge
-> tilts valence edge in opposite direction
-> increases turning-point separation
-> suppresses that direct Zener path.
```

This is why composition grading is a genuine escape from the homogeneous field theorem.

It exchanges electrostatic/common-mode drive for finite band-structure resource.

## 7. Grading is not free

In the symmetric two-band model,

```math
S_\Delta L=\Delta E_g/2,
```

so

```math
\boxed{\Delta E_g=2\eta SL.}
```

The amount of useful grading is limited by

- available Cd-composition range;
- band offsets;
- required absorption cutoff;
- barrier avoidance;
- positive-gap endpoint condition.

## 8. Homogeneous field-profile theorem retained

For

```math
v(F)=\mu F/[1+(F/d)^r],
\qquad r>1,
```

and local

```math
g(F)=AF^pe^{-K/F},
\qquad p>0,
```

uniform field is the unique leakage-minimizing profile for a fixed transit time.

Do not claim that field nonuniformity alone is beneficial.

The escape requires spatially varying material/defect/transport parameters.

## 9. Heterostructure marginal-cost rule

At a transit-constrained interior optimum,

```math
\boxed{
-\frac{\partial g/\partial F}
{\partial(1/v)/\partial F}
=\lambda.
}
```

Interpretation:

> allocate field until every region has the same marginal leakage cost per marginal transit-time improvement.

## 10. Voltage constraint

For ohmic spatial transport,

```math
\boxed{
VT
\ge
\left[\int_0^L\frac{dx}{\sqrt{\mu(x)}}\right]^2.
}
```

Leakage-protecting redistribution generally requires extra bias beyond this kinematic minimum.

## 11. Competing mechanisms remain active

### TAT

```math
\boxed{
F_{\rm TAT}/F_K
=\frac{16}{3\pi}
(\Delta_t/E_g)^{3/2}.
}
```

Near-band-edge traps can open tunneling far below the direct-BTBT exponent scale.

### Nonlocal II

```math
\boxed{
F_{\rm dead}/F_K
=(4\chi/\pi)(\ell_K/L).
}
```

With energy relaxation,

```math
L_{\rm eff}=\ell_E(1-e^{-L/\ell_E}).
```

Finite-device II must be treated from carrier energy history, not a bulk onset field.

## 12. Current numerical regressions

```text
numerics/hgcdte_graded_kane_wkb.py
numerics/hgcdte_field_profile_variational.py
numerics/hgcdte_relaxation_length_phase_boundary.py
numerics/hgcdte_nonlocal_ii_surrogate.py
numerics/hgcdte_impact_dead_space.py
numerics/hgcdte_field_regime_map.py
numerics/hgcdte_btbt_normalized_sweep.py
```

No CI is justified yet.

## 13. Important stopped shortcuts

Do not restart casually:

- active-volume-only bound;
- finite absorber count as one-photon limit;
- finite internal rank as always-on capacity;
- spectral FWHM as architecture-independent transport speed;
- low-field mobility extrapolated into high-field HgCdTe;
- direct BTBT assumed first high-field limiter;
- bulk `100 V/cm` II onset treated as finite-device threshold;
- nonuniform field alone assumed to reduce homogeneous WKB leakage;
- pure grading assumed to eliminate all tunneling in a real device.

## 14. Prior-art posture

Known prior work already covers

- graded HgCdTe devices;
- WKB graded-gap HgCdTe analysis;
- analytical graded heterojunction band profiles;
- classic Kane/Zener tunneling;
- nonuniform-field tunneling methods;
- HgCdTe APD field engineering.

The exact fixed-conduction-slope ratio was not found in the focused search. That is not novelty evidence.

## 15. Next decisive work

Build a finite self-consistent graded HgCdTe energy landscape:

1. choose `x_Cd(x)` / `E_g(x)`;
2. use realistic conduction/valence band-offset partition;
3. solve Poisson for `U(x)` under doping and bias;
4. compute transit from `E_c(x)`;
5. compute WKB action from the full `E_c/E_v` profile;
6. add TAT/interface states;
7. add nonlocal II.

Only after those attacks should publication significance be reassessed.