# Thermal Irreversibility Cost — Forward Detector Access Versus Reverse Thermal Activation

**Date:** 2026-08-08  
**Status:** restricted local-detailed-balance detector model; derived resource relation; no universal dark-count theorem; no novelty claim  

## 1. Purpose

`THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md` converted a broadband optical requirement into a necessary irreversible detector-access rate.

That note still treated the detector reservoir as an ideal one-way sink.

This note removes that idealization in the smallest possible model.

Consider an optically active state `|e>` and a lower-energy dark/localized detection state `|d>` separated by

```math
\Delta=E_e-E_d>0.
```

A thermal reservoir at temperature `T` drives both

```text
|e> -> |d>    forward localization/detection
```

and

```text
|d> -> |e>    reverse thermal activation.
```

The question is:

> If broadband optical performance requires the forward detector coupling to become large, what must happen to the energy bias or temperature if reverse thermal activation is to remain controlled?

---

## 2. Local detailed balance

For a weak thermal reservoir satisfying KMS/local detailed balance, the population transition rates obey

```math
\boxed{
\frac{k_\uparrow}{k_\downarrow}
=e^{-\beta\Delta},
\qquad
\beta=\frac{1}{k_BT}.
}
```

For a bosonic bath one may write the familiar form

```math
k_\downarrow
=\kappa\,[n_B(\Delta)+1],
```

```math
k_\uparrow
=\kappa\,n_B(\Delta),
```

with

```math
n_B(\Delta)
=\frac{1}{e^{\beta\Delta}-1}.
```

Their ratio is exactly the detailed-balance factor above.

This is established thermal open-system physics, not a repository novelty claim.

---

## 3. Rate convention relative to the access theorem

The passive-network theorem uses **amplitude-decay** rates.

Let

```math
R_B
```

be the aggregate detector amplitude-access rate appearing in the transfer theorem.

For a simple irreversible quantum jump with population rate `k_down`, the no-jump amplitude decays at half the population rate. Thus the minimal identification is

```math
\boxed{
k_\downarrow=2R_B.}
```

This identification is model-specific but fixes the factor of two consistently with the preceding optical calculations.

---

## 4. Import the broadband detector-access requirement

For the restricted one-free-space-channel model in `THERMODYNAMIC_OPTICAL_ACCESS_BRIDGE.md`, achieving band-averaged transfer

```math
\overline T_B\ge\eta
```

over angular-frequency width `W` requires

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

Therefore the forward population-localization rate must obey

```math
\boxed{
k_\downarrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}.
}
```

This converts desired optical bandwidth and efficiency into a minimum forward irreversible transition rate.

---

## 5. Reverse activation cannot stay fixed at fixed energy bias

Detailed balance gives

```math
k_\uparrow
=k_\downarrow e^{-\beta\Delta}.
```

Therefore the previous lower bound immediately implies

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
\exp\left(-\frac{\Delta}{k_BT}\right).
}
```

Within this restricted model, increasing optical bandwidth while holding `eta`, `Delta`, and `T` fixed necessarily increases the minimum reverse thermal-activation rate linearly with `W`.

So an arbitrarily fast thermal sink is not arbitrarily one-way at fixed energy bias.

---

## 6. Required energy bias for a fixed reverse-activation budget

Suppose the device requires

```math
k_\uparrow\le D_{\rm rev},
```

where `D_rev` is an allowed **reverse thermal-activation rate**.

Do not automatically call `D_rev` a dark-count rate: whether a reverse activation becomes a recorded false count depends on the rest of the detector cycle.

Combining the forward-rate requirement with detailed balance gives the necessary condition

```math
D_{\rm rev}
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
\exp\left(-\frac{\Delta}{k_BT}\right).
```

Solving for the energy bias,

```math
\boxed{
\Delta
\ge
k_BT
\ln\!\left[
\frac{\eta W}
{2\pi(1-\eta)D_{\rm rev}}
\right]
}
```

whenever the logarithm's argument exceeds unity.

This is the central restricted result of this note.

---

## 7. Equivalent temperature requirement

For fixed `Delta`, `eta`, `W`, and `D_rev`, the same condition may be written

```math
\boxed{
T
\le
\frac{\Delta}
{k_B\ln\!\left[
\eta W/
\left(2\pi(1-\eta)D_{\rm rev}\right)
\right]}.
}
```

Thus cooling and energy bias appear as interchangeable resources for suppressing reverse thermal activation in this minimal equilibrium reservoir model.

---

## 8. Important scaling

At fixed efficiency and reverse-activation budget,

```math
\Delta_{\min}
\sim
k_BT\ln W.
```

So the thermodynamic energy bias need only grow logarithmically with bandwidth in this idealized chain, while the required forward detector rate grows linearly with bandwidth.

Likewise, as

```math
\eta\to1,
```

the required forward access scales as

```math
\frac{\eta}{1-\eta},
```

and the minimum energy bias acquires the logarithmic penalty

```math
\Delta_{\min}
\sim
k_BT\ln\frac{1}{1-\eta}.
```

This is a restricted resource scaling, not a universal photodetector limit.

---

## 9. Fractional reversibility versus absolute reverse rate

If one only requires a fixed **ratio**

```math
\frac{k_\uparrow}{k_\downarrow}
\le\epsilon,
```

then detailed balance gives simply

```math
\boxed{
\Delta
\ge
k_BT\ln\frac{1}{\epsilon}.
}
```

This condition is independent of bandwidth.

The bandwidth dependence arises only when the absolute reverse-activation rate must remain bounded while the forward detection rate is forced upward.

That distinction must be preserved.

---

## 10. What this does and does not mean for dark counts

A reverse transition

```text
|d> -> |e>
```

is not automatically a detector output event.

Whether it becomes a false count depends on

- how `|d>` is monitored;
- whether `|e>` can re-enter the detection pathway without a photon;
- reset timing;
- amplification dynamics;
- additional states/reservoirs.

Therefore the repository currently claims only a **reverse thermal-activation constraint**.

A dark-count theorem requires an explicit cyclic detector model.

---

## 11. Nonequilibrium escape

The detailed-balance relation applies to a thermal equilibrium reservoir under the stated weak-coupling assumptions.

An actively driven or chemically biased reservoir can suppress the reverse process beyond the equilibrium Boltzmann factor.

But that introduces an additional nonequilibrium/free-energy resource.

Thus violating the thermal relation is not necessarily impossible; it changes the accounting problem to

```text
what work / chemical potential / reset resource maintains the one-way detector cycle?
```

This is consistent with prior quantum-detector architectures that assume rapid transfer to an optically dark state with negligible thermally activated return.

---

## 12. Claim boundary

### Derived within the restricted chain

Using

1. the one-free-space-channel thermodynamic optical-access bound;
2. the passive harmonic two-access theorem;
3. the identification `k_down = 2 R_B`;
4. local detailed balance for one thermal detector transition;

one obtains

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
e^{-\Delta/(k_BT)}
}
```

and, for `k_up <= D_rev`,

```math
\boxed{
\Delta
\ge
k_BT
\ln\!\left[
\frac{\eta W}
{2\pi(1-\eta)D_{\rm rev}}
\right].
}
```

### Not established

- that `D_rev` equals the observable detector dark-count rate;
- a minimum reset work;
- a nonequilibrium detector bound;
- validity under strong non-Markovian detector-bath coupling;
- universality beyond the free-space optical-channel model;
- novelty of this combined scaling.

---

## 13. Next decisive model

The natural next step is now a **complete minimal cycle**:

```text
|g> --photon--> |e>
|e> --detector bath--> |d>
|d> --readout/reset--> |g>.
```

That model should include

1. forward and reverse thermal rates between `e` and `d`;
2. an explicit readout or monitored transition;
3. a reset process with its reservoir/work source;
4. a precise definition of what constitutes a false count;
5. steady-state count statistics.

Only then can the current reverse-activation inequality be promoted—or rejected—as a true speed/efficiency/dark-count thermodynamic statement.