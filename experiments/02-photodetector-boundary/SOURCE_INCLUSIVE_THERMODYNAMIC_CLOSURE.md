# Source-Inclusive Thermodynamic Closure — Experiment 02

**Date:** 2026-08-12  
**Status:** active adversarial correction / thermodynamic lower-bound attack  
**Priority:** unassessed; no novelty claim

This file attacks the strongest thermodynamic statement retained in `RESET_AND_CYCLE_CLOSURE.md`.

The previous candidate was roughly:

> if detector + controller + record memories all return to standard states and no output record remains, the event-record entropy must eventually be erased at a scale `k_B T h(p)`.

That statement is still too strong unless the **information source and all usable side information are included in the closure boundary**.

The correction is important enough to preserve as a dedicated derivation.

---

## 1. Reversible-uncomputation counterexample

Let the optical/source variable be

```math
X\in\{0,1\},
```

encoded in orthogonal source states

```math
|0\rangle_S,
\qquad
|1\rangle_S.
```

Let the detector memory start in

```math
|0\rangle_M.
```

A nondestructive measurement can be represented ideally as

```math
U_{\rm meas}:
|x\rangle_S|0\rangle_M
\longrightarrow
|x\rangle_S|x\rangle_M.
```

The detector has acquired a perfectly distinguishable record.

Now apply the inverse interaction:

```math
U_{\rm meas}^{\dagger}:
|x\rangle_S|x\rangle_M
\longrightarrow
|x\rangle_S|0\rangle_M.
```

Afterward:

```text
memory M is exactly reset;
no detector output record remains;
the source state still carries X;
no many-to-one logical erasure of X was performed.
```

Therefore

```math
\boxed{
\text{all detector-side memories reset}
+\text{ no retained detector output}
\not\Rightarrow
\text{Landauer erasure of }X.
}
```

The source itself is side information.

This counterexample is sufficient because Experiment 02 explicitly allows nonabsorptive / nondestructive detection when testing universal statements.

---

## 2. What the previous global-cycle statement omitted

The missing question was not merely

```text
where is the detector record stored?
```

but

```text
where does the original hypothesis variable X still exist?
```

If any accessible degree of freedom remains correlated with `X`, it can in principle act as side information for reversible reset/uncomputation.

Candidates include

```text
surviving incident/output photon;
source preparation register;
outgoing radiation;
material/environmental correlations;
controller state;
external classical record;
quantum reference system.
```

Thus `no output record` is not enough.

A true erasure statement requires closing the accounting boundary around **all systems that retain usable information about X**.

---

## 3. Source-inclusive closure

Define a stronger requirement:

```text
SOURCE-INCLUSIVE INFORMATIONAL CLOSURE

After the complete cycle,
all apparatus, memories, source/reference degrees of freedom,
and all other systems correlated with X inside the declared boundary
must be restored to specified X-independent standard states,
and no usable copy/correlation carrying X may remain outside the boundary.
```

Only then is the logical information associated with `X` genuinely discarded rather than moved or uncomputed.

This is much stronger than detector reset.

It can include the photon source itself.

---

## 4. Why source-inclusive closure is logically irreversible

Suppose two distinguishable initial histories

```math
|0\rangle_S|A_0\rangle,
\qquad
|1\rangle_S|A_0\rangle
```

must both end in the same complete standard state

```math
|S_{\rm std}\rangle|A_{\rm std}\rangle.
```

A closed unitary transformation cannot map two orthogonal states to one identical state.

Therefore the distinguishability must either

```text
remain in some degree of freedom;
be exported to an environment;
consume a correlated resource that itself changes;
or be discarded into an uncontrolled bath/reservoir.
```

This is the precise point at which logical irreversibility enters.

The conclusion is not detector-specific; it is ordinary reversibility/information conservation applied to the complete cycle.

---

## 5. Side information determines erasure cost

For a memory `M` and retained side information `R`, the relevant information-thermodynamic quantity is conditional entropy.

In the classical degenerate-memory asymptotic idealization,

```math
W_{\rm erase}
\sim
k_BT\,H(M|R).
```

If `R` perfectly specifies `M`, then

```math
H(M|R)=0,
```

and local erasure can be reversible.

In the quantum setting, conditional entropy can even be negative for entangled side information, so erasure can yield work while consuming that correlation resource.

This does not violate the second law because restoring the consumed side-information/entanglement resource closes the accounting loop.

Therefore:

```math
\boxed{
\text{erasure cost attaches to discarded information conditional on what remains accessible,}
}
```

not to `a detector click` as such.

Established information-thermodynamic results underlie this statement; no novelty is claimed.

---

## 6. Work extraction from the detected optical field

A detected photon is not only an information carrier. It can also carry nonequilibrium free energy.

Let

```math
\Delta F_{\rm opt}^{\rm avail}
=
F(\rho_{\rm opt,in})-F(\rho_{\rm opt,out})
```

be the optical free energy consumed by the full cycle relative to the chosen thermal reference.

If record erasure would otherwise require an idealized work scale

```math
W_{\rm info},
```

then optical free-energy consumption can subsidize that work.

A schematic isothermal resource balance is

```math
\boxed{
W_{\rm ext}
\gtrsim
W_{\rm info}
-
\Delta F_{\rm opt}^{\rm avail}
-
\Delta F_{\rm other}^{\rm avail},
}
```

where `W_ext` is externally supplied work and `Delta F_other^avail` includes any other nonequilibrium resource that is consumed.

This equation is an organizing balance, not a universal single-shot theorem; the exact free-energy functional depends on regime and allowed operations.

The crucial counterexample is qualitative and robust:

```text
if the optical input supplies enough usable free energy,
there need be no positive external-work cost for closing the detector cycle.
```

Indeed net work extraction is not excluded in principle.

Thus

```math
\boxed{
\text{source-inclusive logical erasure}
\not\Rightarrow
\text{positive detector-supplied work per event}.
}
```

---

## 7. Why photon energy `h nu` is not automatically the correct subsidy

Do not simply subtract `h nu` from a Landauer term.

The relevant resource is **available nonequilibrium free energy**, not raw energy alone.

For a state `rho` with Hamiltonian `H` at bath temperature `T`, the standard nonequilibrium free-energy form is schematically

```math
F(\rho)
=\operatorname{Tr}(\rho H)
-k_BT S(\rho)
```

up to the chosen reference convention.

Only the decrease in usable free energy under the allowed operations can subsidize work.

Photon frequency, state purity/mixing, coherence, coupling accessibility, output state, and reservoir temperature all matter.

Therefore the physically disciplined statement is

```text
optical free energy can pay for information processing,
```

not

```text
every photon contributes exactly h nu of reset work.
```

---

## 8. Active pumps and nonequilibrium reservoirs kill a detector-only work bound

Suppose an avalanche detector, superconducting detector, or other active architecture is supplied by an external bias/pump reservoir.

That reservoir can provide free energy

```math
\Delta F_{\rm pump}^{\rm avail}>0.
```

The photon can act mainly as a trigger selecting which metastable/bias-driven trajectory occurs.

Then macroscopic output energy can be much larger than photon energy while the ultimate energetic resource comes from the pump.

Conversely, the pump can also pay any reset/record-processing cost.

Therefore if arbitrary nonequilibrium resources are allowed but not charged in the ledger,

```math
\boxed{
\text{no positive architecture-independent external-work lower bound can survive.}
}
```

The omitted resource simply supplies the work.

---

## 9. Continuous reversible transduction attacks the binary-memory assumption

Consider an idealized detector that never forms a latched binary memory.

Instead it implements a reversible correlation such as

```text
optical state
<-> continuous pointer displacement
<-> reversible output field/work coordinate.
```

If the output is later coherently uncomputed and no information is discarded, no logical erasure step is required.

If the output is retained, that output itself is the record.

If the output is eventually erased, the thermodynamic accounting attaches there.

Therefore

```math
\boxed{
\text{binary memory is not a necessary stage of photodetection.}
}
```

The correct thermodynamic object is discarded information in the complete transformation, not a presumed detector bit.

---

## 10. Indefinitely retained external records remain an escape resource

If a detector exports `h(p)` nats per independent cycle into an ever-growing memory and never resets that memory, it can indefinitely postpone erasure work in the idealized model.

After `N_cyc` cycles the stored information grows as approximately

```math
N_{\rm cyc}h(p).
```

Thus one can trade

```text
thermodynamic reset cost now
against
unbounded memory/resource consumption later.
```

A finite-memory cyclic theorem must therefore explicitly bound or close exported record capacity.

---

## 11. Quantum side information makes the lesson stronger

For quantum-correlated side information `R`, conditional von Neumann entropy

```math
S(M|R)=S(MR)-S(R)
```

can be negative.

In established quantum information thermodynamics, negative conditional entropy can correspond to work extraction during erasure while consuming entanglement/correlation resources.

Hence even

```text
positive conditional entropy cost
```

is not universal unless the allowed side-information class is specified.

When the consumed correlation resource must itself be restored to complete a true cycle, its preparation/restoration cost re-enters.

This is exactly the pattern that Experiment 02 has repeatedly found:

```text
an apparent bound disappears when an omitted resource is admitted;
the bound returns only after that resource is included in the accounting boundary.
```

---

## 12. The strongest thermodynamic statement that survives this attack

The previous statement

```text
global detector/controller/memory reset
-> k_B T h(p) must be paid somewhere
```

is **SUPERSEDED**.

A stronger and more accurate statement is:

> **Photodetection has no architecture-independent positive heat or external-work cost per event when arbitrary side information, optical free energy, nonequilibrium pumps, reversible transduction, or unbounded exported records are allowed. A nontrivial thermodynamic requirement appears only after the accounting boundary includes every resource that stores information or supplies free energy. Under such source-inclusive resource closure, the surviving constraint is a generalized second-law / discarded-information free-energy balance, not a universal `k_B T ln 2` detector cost.**

This is currently the strongest thermodynamic conclusion of Experiment 02.

---

## 13. What remains genuinely fundamental

Three layers now have to be separated:

```text
INFORMATION CONSERVATION
reversible dynamics cannot map distinguishable global histories to one identical global history;

LOGICAL IRREVERSIBILITY
if distinguishing information is actually discarded, it must leave the controlled degrees of freedom;

THERMODYNAMIC RESOURCE BALANCE
the work/heat consequence depends on bath temperature, Hamiltonians,
side information, free-energy resources, allowed operations, and cycle closure.
```

The first is kinematic/informational.

The second states when erasure occurs.

The third determines energetic cost.

None alone says that one photon detection must dissipate one fixed quantum of heat.

---

## 14. Relation back to the original atom-to-detector question

The original question asked when a collection of atoms `becomes a detector`.

The thermodynamic attack now shows that even at the deepest cycle level, the answer is not a material phase boundary.

A physical system can

```text
acquire photon information reversibly;
export it;
retain it;
uncompute it using side information;
consume optical or pump free energy;
or erase it later elsewhere.
```

Thus the detector boundary is operational, while thermodynamic irreversibility is a separate property of the **complete information-processing cycle**.

---

## 15. Current next attack

The strongest remaining question is no longer `what is the heat cost of detection?`

It is:

> **Can the full detector problem be expressed as a resource-conversion theorem whose primitive inputs are optical-state distinguishability, available nonequilibrium free energy, allowed interaction time/bandwidth, side information, exported-record capacity, and target decision error?**

Before attempting such a theorem, attack whether these coordinates are complete.

Candidate missing resources include

```text
coherence/reference-frame resources;
spatial mode volume and channel count;
finite control precision;
clock/timing resources;
catalysts that return locally unchanged but become correlated;
finite-size / single-shot fluctuations;
causal latency and maximum power.
```

The next iteration should try to generate counterexamples using these resources before proposing any universal resource ledger.
