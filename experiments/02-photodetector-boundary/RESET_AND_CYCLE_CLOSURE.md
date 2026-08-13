# Reset, Record Export, and Global Cycle Closure — Experiment 02

**Date:** 2026-08-12  
**Status:** active conditional lower-bound attack  
**Priority:** unassessed; no novelty claim

This file returns to the thermodynamic question after the detector resource ledger has been expanded through optical coupling, record formation, noise, timing, and decision theory.

The target is the repeatedly tempting statement

> every detected photon must dissipate at least `k_B T ln 2`.

That statement already failed as a universal **acquisition** bound. The remaining question is whether something Landauer-like reappears when a detector must be reused cyclically.

---

## 1. Separate three different operations

Do not call all of the following `detection`:

```text
ACQUISITION
photon history becomes correlated with a detector degree of freedom;

LOCAL RESET
the detector's internal memory/pointer is returned to its ready state;

GLOBAL CYCLE CLOSURE
detector + controller + exported record + auxiliary memories are all returned to their initial standard macrostates.
```

Thermodynamic statements can differ sharply among these stages.

---

## 2. Binary event record with arbitrary prior

Let the record bit be

```math
X\in\{0,1\},
```

with event probability

```math
P(X=1)=p.
```

Its Shannon entropy in nats is

```math
\boxed{
h(p)
=-p\ln p-(1-p)\ln(1-p).
}
```

The maximum

```math
h(p)=\ln2
```

occurs only at

```math
p=1/2.
```

Therefore even before discussing side information, `k_B T ln 2` is not the generic entropy scale of a biased detector record.

---

## 3. Conditional Landauer result for a degenerate binary memory

Consider an idealized memory with energetically degenerate logical states, coupled quasistatically to a bath at temperature `T`.

If exact reset maps the random memory state to one standard logical state and no useful side information is retained, the minimum isothermal work / exported heat associated with the entropy decrease is

```math
\boxed{
W_{\rm erase,min}
\ge
k_BT\,h(p)
}
```

under the stated equilibrium/degenerate-memory assumptions.

For an unbiased bit,

```math
p=1/2
```

this reduces to

```math
W_{\rm erase,min}\ge k_BT\ln2.
```

For a rare-event record,

```math
p\ll1,
```

```math
h(p)
\simeq
p\ln(1/p)+p.
```

Thus the average reset cost per cycle can become much smaller than `k_BT ln2` when the record is strongly biased and its statistics are exploited.

This is a standard information-thermodynamic structure, not a novelty claim.

---

## 4. Imperfect reset changes the entropy reduction

Suppose the final nominal ready state has reset error probability `delta`, giving final logical entropy

```math
h(\delta).
```

For the same degenerate-memory idealization, the entropy-reduction contribution becomes

```math
\boxed{
W_{\rm reset,min}
\ge
k_BT[\,h(p)-h(\delta)\,]
}
```

when the bracket is positive and other free-energy terms vanish.

Therefore reset accuracy is itself a resource coordinate.

There is no universal constant cost independent of

```text
record prior p
and
allowed reset error delta.
```

---

## 5. Local reset can use exported side information

Now let the detector memory be `M` and suppose the measurement result has already been copied/exported into another accessible register `R`.

The relevant uncertainty of `M` given `R` is the conditional entropy

```math
H(M|R).
```

Under the corresponding ideal information-thermodynamic assumptions, the logical erasure cost of `M` can be reduced to a scale set by

```math
\boxed{
k_BT\,H(M|R).
}
```

If `R` perfectly determines `M`, then

```math
H(M|R)=0.
```

So the detector's **local** memory can in principle be reset conditionally without an unavoidable `k_BT ln2` entropy cost at that location.

The information has not vanished.

It has moved into `R`.

This is the thermodynamic analogue of earlier subsystem-boundary corrections:

```text
information absent from detector memory
!=
information absent globally.
```

---

## 6. Exported record kills a universal local per-click heat bound

Construct the cycle

```text
photon event
-> detector pointer M
-> reversible copy/correlation into external record R
-> conditionally restore M using R
-> leave R unchanged.
```

The detector itself can return to its ready state while the event record persists externally.

Therefore

```math
\boxed{
\text{reusable local detector}
\not\Rightarrow
k_BT\ln2\text{ dissipated locally per click}.
}
```

This is another counterexample to a detector-local Landauer bound.

The missing resource is the accumulating external memory / exported entropy.

---

## 7. Global cycle closure changes the question

Now impose a stronger requirement:

```text
after each complete cycle,
all detector, controller, and record memories
must return to their original standard states,
and no copy of the event record may remain outside the accounted system.
```

Then the event information cannot simply be exported indefinitely.

If the full logical record has entropy `h(p)` and must be erased from the globally accounted memory, the usual reversible isothermal limit reappears at the **system level**:

```math
\boxed{
W_{\rm global,min}
\gtrsim
k_BT\,h(p)
}
```

for the ideal degenerate-memory assumptions and exact reset.

The key correction is location and scope:

```text
not necessarily at photon absorption;
not necessarily inside the detector;
not necessarily at readout;
but somewhere in the closed reusable information cycle
if all record entropy must truly be erased.
```

---

## 8. Per-cycle and per-event costs are not the same

For rare events `p<<1`, exact global reset gives average ideal cost per cycle

```math
W_{\rm cycle,min}
\simeq
k_BT[p\ln(1/p)+p].
```

If one divides this average cycle cost by event probability `p`, the amortized scale per actual event becomes

```math
\boxed{
\frac{W_{\rm cycle,min}}{p}
\simeq
k_BT[\ln(1/p)+1].
}
```

This can exceed `k_BT ln2` for rare records.

But that does **not** imply each physical click must dissipate this amount at the click time.

It is an amortized global information-reset accounting under a particular cycle protocol.

Thus even the phrase

```text
energy per detected photon
```

is ambiguous unless the reset cadence and accounting boundary are specified.

---

## 9. Compression can move the cost across cycles

If many detector outcomes are stored before erasure, a reversible compressor can in principle pack a long biased record toward its Shannon entropy before the memory is erased.

For independent events with probability `p`, the asymptotic information per cycle is `h(p)` nats.

Thus batching/compression changes *where and when* erasure work occurs but not the asymptotic entropy that must disappear if the entire record store is eventually reset.

This further kills any claim that one specific detector event must carry one indivisible `k_BT ln2` packet of heat.

---

## 10. Record stability is a separate physical constraint

Suppose a persistent binary record is protected by an activation barrier `E_b` and has spontaneous false-switch rate

```math
\Gamma_d
=\nu_0e^{-E_b/(k_BT)}.
```

Requiring false-switch probability no larger than `p_d` during retention time `tau_rec` gives

```math
\boxed{
E_b
\ge
k_BT
\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_d)}
\right].
}
```

This is a **retention barrier** requirement, not automatically a dissipated-work requirement.

A large energy barrier can exist without being dissipated on every cycle.

---

## 11. Passive stability conflicts with fast reset unless the landscape is actively changed

Take the same activated model and suppose reset is performed by lowering the relevant barrier by an amount `Delta E`.

The reset transition rate is modeled as

```math
\Gamma_r
=\nu_0
\exp[-(E_b-\Delta E)/(k_BT)].
```

To reset successfully with failure probability at most `epsilon_r` in time `tau_r`, require

```math
1-e^{-\Gamma_r\tau_r}
\ge
1-\epsilon_r.
```

Hence

```math
\Gamma_r\tau_r
\ge
\ln(1/\epsilon_r).
```

Therefore

```math
\boxed{
\Delta E
\ge
E_b
-
k_BT\ln\left[
\frac{\nu_0\tau_r}
{\ln(1/\epsilon_r)}
\right].
}
```

Combining with the retention requirement gives the conditional landscape-modulation requirement

```math
\boxed{
\Delta E
\ge
k_BT
\ln\left[
\frac{
\tau_{\rm rec}\ln(1/\epsilon_r)
}{
\tau_r[-\ln(1-p_d)]
}
\right]
}
```

when the right-hand side is positive and the same activated-rate model applies.

For small `p_d`,

```math
\Delta E
\gtrsim
k_BT
\ln\left[
\frac{
\tau_{\rm rec}\ln(1/\epsilon_r)
}{\tau_r p_d}
\right].
```

---

## 12. Important interpretation — this is a control-range bound, not a heat bound

The combined relation says:

```text
long-lived passive record
+
very small spontaneous error
+
rapid reliable reset
```

requires the control protocol to change the effective energy landscape by a large amount in this simple activated model.

It does **not** prove that `Delta E` must be dissipated irreversibly.

An ideal quasistatic/control protocol could in principle recover some of that energy.

Thus the robust conclusion is a **stability/reset-speed control-range tradeoff**, not a universal per-cycle heat theorem.

This distinction must be preserved.

---

## 13. Another hidden resource appears: external memory capacity

The local-reset counterexample works by exporting the record.

If the detector runs for `N_cyc` cycles without erasing the external memory, the typical stored information grows approximately as

```math
N_{\rm cyc}h(p)
```

nats for independent records.

Therefore one can trade

```text
local dissipation
against
external memory capacity / eventual reset work.
```

This is structurally analogous to earlier trades:

```text
weak absorber strength <-> optical dwell time;
weak coupling <-> bandwidth;
local reset heat <-> exported record capacity.
```

Again, a proposed universal bound fails because an omitted resource can carry the burden.

---

## 14. Strongest thermodynamic statement that currently survives

The naive statement

```text
every detection event dissipates at least k_BT ln2
```

is rejected.

The stronger surviving conditional statement is:

> **If a complete reusable detector/controller/record system must return to a fixed standard logical state, no copy of the event record may remain outside the accounting boundary, and reset occurs isothermally under the standard information-thermodynamic assumptions, then the entropy of the stored event record must eventually be removed somewhere. For a binary event with prior `p`, the ideal scale is `k_BT h(p)` per cycle, not universally `k_BT ln2`.**

This is fundamentally a **global cycle-closure** statement.

---

## 15. Relation to the original detector-boundary question

The detector boundary itself still does not require thermodynamic erasure.

A one-shot detector can create a record and never reset.

A local reusable detector can export the record.

Thermodynamic erasure becomes unavoidable only after stronger cyclic closure requirements are imposed.

Therefore:

```text
photodetection
!=
logical erasure.
```

But:

```text
fully cyclic reusable detection
+
finite memory
+
no retained external record
```

can force an eventual erasure problem.

---

## 16. Current frontier

The next lower-bound attack should ask whether a detector can evade even the global cycle-closure cost by using

```text
correlations with the optical/environmental input as side information;
work extraction from the detected field;
nonequilibrium reservoirs;
active pumps;
measurement protocols that never store a binary logical record;
continuous reversible transduction;
```

or whether the full thermodynamic accounting simply moves the entropy/free-energy cost elsewhere.

The goal is not to defend Landauer but to find the weakest closure assumptions under which a nontrivial detector-cycle bound actually survives.
