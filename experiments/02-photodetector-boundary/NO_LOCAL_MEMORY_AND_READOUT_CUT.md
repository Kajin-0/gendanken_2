# No Local Memory and the Readout Cut — Experiment 02

**Date:** 2026-08-12  
**Status:** central conceptual correction  
**Priority:** organizing result; no novelty claim

The early Experiment-02 formulation moved from

```text
photon absorption
```

to

```text
persistent material record.
```

The semiconductor branch and detector-process audit now motivate a stronger question:

> **Must the detector material itself retain a persistent record after the photon interaction?**

The answer is no.

This correction pushes the detector boundary away from `memory inside matter` and toward the declared **measurement/readout boundary**.

---

## 1. Minimal no-local-memory detector model

Let

```text
S = optical input system
D = material detector/transducer degree of freedom
R = accessible output/register
```

with initial state

```math
|D_0\rangle|R_0\rangle.
```

Consider binary optical hypotheses

```math
H_0:|0\rangle_S,
\qquad
H_1:|1\rangle_S.
```

A physically allowed joint interaction can in principle implement

```math
|0\rangle_S|D_0\rangle|R_0\rangle
\longrightarrow
|\psi_0\rangle_S|D_0\rangle|R_0'\rangle,
```

```math
|1\rangle_S|D_0\rangle|R_0\rangle
\longrightarrow
|\psi_1\rangle_S|D_0\rangle|R_1'\rangle,
```

where the material subsystem has returned to exactly the same local state

```math
\boxed{
\rho_D^{(0)}=\rho_D^{(1)}=|D_0\rangle\langle D_0|.
}
```

Yet the output states may satisfy

```math
\boxed{
\rho_R^{(0)}\ne\rho_R^{(1)}.
}
```

If they are orthogonal,

```math
\mathcal D_R=1,
```

so the optical hypotheses are perfectly distinguishable from the output even though the material retains **zero local memory** of which event occurred.

---

## 2. Persistent local material memory is therefore not necessary

The earlier possible criterion

```text
photon interaction
-> persistent state change in detector matter
```

is too strong as a universal definition.

The material can serve as a transient mediator that transfers information into an output degree of freedom and then locally resets/uncomputes.

Thus

```math
\boxed{
\text{persistent local detector state}
\not\text{ necessary for operational photodetection.}
}
```

What must persist is only enough accessible correlation somewhere in the declared measurement chain for the decision to be made.

---

## 3. This also clarifies detector reset

If `D` returns automatically to `D_0` while the record is exported into `R`, then the detector material can be locally ready for the next event without erasing the record.

This is the same information-accounting structure that previously killed a universal local Landauer reset cost.

The record entropy resides in `R`, not `D`.

Hence

```text
local detector recovery time
```

and

```text
record lifetime
```

can belong to different physical subsystems.

---

## 4. The mirror paradox

Now make the criterion too broad.

Suppose a mirror maps an incoming photon into a reflected output mode:

```math
|1\rangle_{\rm in}
\longrightarrow
|1\rangle_{\rm refl}.
```

An observer who later measures the reflected mode can learn that a photon was present.

If the rule is merely

```text
matter interacts with light
and
some outgoing degree of freedom contains information,
```

then a passive mirror, beamsplitter, waveguide, filter, or lens begins to qualify as a `photodetector` whenever a downstream observer measures the output.

That is too broad for ordinary detector language.

Therefore another boundary must be declared.

---

## 5. The missing ingredient is the readout cut

A measurement architecture has a chain

```text
optical field
-> interaction / transduction
-> intermediate degrees of freedom
-> amplification / routing
-> accessible output
-> decision.
```

Where we choose to call one subsystem `the detector` is partly a **system-boundary/readout convention**.

A material element is not intrinsically a detector merely because its scattering matrix depends on the optical input.

It functions as a detector when the declared device boundary includes an output variable whose statistics are intentionally used as evidence about the optical input.

Thus a more defensible operational statement is

> **A detector is a physical measurement architecture—or a declared subsystem of one—that maps an optical input family into an accessible output process used for inference under a specified readout boundary.**

This is relational, not an intrinsic phase of matter.

---

## 6. Three roles that should not be conflated

### Optical transformer

```text
input optical state
-> output optical state
```

with no declared measurement/readout role.

Examples can include passive propagation, reflection, filtering, or phase shifting.

### Transducer

```text
optical state
-> another physical degree of freedom
```

with the optical information transferred or copied into another modality.

### Detector

```text
optical input family
-> accessible output process
-> inference/decision
```

under a declared device/readout boundary.

The same physical component can occupy different roles depending on how it is embedded and what outputs are accessible.

---

## 7. Consequence for the original atom-count question

The question

> `At what N does matter become a photodetector?`

presupposes that `photodetector` is an intrinsic material category.

The accumulated counterexamples now indicate otherwise.

A single atom can participate in a detector architecture if its optical interaction controls an accessible output.

A macroscopic semiconductor can fail as a detector for a given task if its accessible output distributions are indistinguishable or too noisy.

A passive optical component can carry optical information without ordinarily being called a detector because no readout cut terminates there.

Therefore

```math
\boxed{
\text{photodetector-ness is relational / architectural, not a material phase transition.}
}
```

---

## 8. The local-state trace distance was never the fully general detector criterion

Early Experiment 02 used

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1
```

for the material subsystem.

The no-local-memory counterexample has

```math
\mathcal D_D=0
```

but

```math
\mathcal D_R>0.
```

Thus the correct subsystem for decision theory is the **declared accessible output**, not necessarily the material degree of freedom after the interaction.

This is exactly why the later detector-process formulation superseded the early material-state-only formulation.

---

## 9. Persistence also becomes task relative

Suppose the output pulse exists only for duration `tau_out`.

It can still serve as a detector record if the allowed readout accesses it during that interval.

Therefore a universal requirement

```math
\tau_{\rm record}>\text{some intrinsic threshold}
```

cannot be imposed without specifying the readout latency and task.

The necessary relation is only schematic:

```math
\boxed{
\text{output information must remain accessible long enough for the allowed readout strategy to exploit it.}
}
```

A permanently latched state is one implementation, not the definition.

---

## 10. Classicality is also not a sharp material boundary

One might try to repair the definition by requiring a `classical` output.

But classicality itself depends on decoherence, coarse graining, observer access, and the scale at which interference is neglected.

Quantum-nondemolition and other quantum measurement architectures can produce useful measurement records without a unique microscopic point at which matter becomes classically different.

Thus

```text
becomes classical
```

is not a clean atom-count detector boundary either.

---

## 11. Strongest conceptual answer so far

After attacking

```text
absorption;
band formation;
electron-hole generation;
atom count;
persistent local memory;
irreversibility;
gain;
energy dissipation;
scalar D*;
geometry;
```

none survives as the universal detector boundary.

The strongest surviving statement is now:

> **Matter does not become a photodetector at a special microscopic boundary. A physical subsystem functions as a photodetector when, within a declared measurement architecture and allowed resource/readout model, optical alternatives induce distinguishable accessible output processes that can support the specified inference task.**

This is an organizing conclusion, not a novelty claim.

---

## 12. What this says about `simple collection of atoms`

For `N=1`, `N=10`, `N=10^23`, the right question is not

```text
Does N exceed the detector threshold?
```

but

```text
What optical interaction is available?
What output degree of freedom is coupled to it?
What information reaches that output?
How long is it accessible?
What noise/resources constrain readout?
What decision must be made?
```

Atom count changes the available physical mechanisms—bands, oscillator strength, transport, thermalization, collective coupling, etc.—but does not itself define detector status.

---

## 13. Current next question

This correction leaves one remaining conceptual boundary worth attacking:

> **If detector-ness depends on the declared readout cut, is there any observer-independent physical distinction between a `transducer` and a `detector`, or is the distinction necessarily functional/semantic once the full measurement chain is considered?**

If no observer-independent distinction survives, the original Gedanken question may be considered conceptually closed: `photodetector` is a role in a measurement process, not an emergent phase of matter.
