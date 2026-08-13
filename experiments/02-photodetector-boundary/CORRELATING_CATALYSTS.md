# Correlating Catalysts as a Hidden Detector Resource — Experiment 02

**Date:** 2026-08-12  
**Status:** active resource-ledger correction  
**Priority:** unassessed; no novelty claim

The current detector program asks whether a closed resource ledger can characterize the physically achievable detector channels.

A dangerous loophole is an auxiliary system that appears to be returned unchanged after each operation but becomes correlated with the detector, source, or earlier outputs.

This file distinguishes

```text
local state restoration
```

from

```text
global resource restoration.
```

The distinction is established in correlated-catalytic quantum thermodynamics and general resource theories. No novelty is claimed for catalytic/correlating-catalyst mathematics.

---

## 1. Ordinary catalyst versus correlated catalyst

Let `S` be the detector/source system being transformed and `C` an auxiliary catalyst.

A strict uncorrelated catalytic transformation has

```math
\rho_S\otimes\tau_C
\longrightarrow
\rho'_S\otimes\tau_C.
```

The catalyst is returned locally and globally decoupled.

A correlated catalytic transformation relaxes this to

```math
\rho_S\otimes\tau_C
\longrightarrow
\rho'_{SC}
```

with only

```math
\boxed{
\operatorname{Tr}_S\rho'_{SC}=\tau_C.
}
```

The catalyst marginal is exactly unchanged, but generally

```math
\rho'_{SC}
\ne
\rho'_S\otimes\tau_C.
```

Thus the catalyst can look unchanged to every local measurement on `C` while the global state has changed.

---

## 2. The missing quantity is correlation

Define the final mutual information

```math
\boxed{
I(S:C)_{\rho'}
=S(\rho'_S)+S(\tau_C)-S(\rho'_{SC}).
}
```

Initially, for the product state,

```math
I(S:C)=0.
```

After correlated catalysis one may have

```math
I(S:C)>0
```

while still satisfying

```math
\rho'_C=\tau_C.
```

Therefore

```math
\boxed{
\text{same catalyst marginal}
\not\Rightarrow
\text{same global resource state}.
}
```

This is the exact analogue of the earlier detector-memory lesson:

```text
same local detector state
!=
same global information state.
```

---

## 3. Why marginal-only accounting can falsely label a resource as free

Suppose a detector theorem says that an auxiliary resource may be used repeatedly provided

```math
\rho'_C=\rho_C.
```

If correlations with outputs/source are not charged, the auxiliary may assist transformations that are impossible under strict product-return catalysis.

The resource has not necessarily been consumed in its local marginal; instead the global correlation structure has changed.

Thus a marginal-only resource ledger can declare

```text
catalyst returned unchanged
```

while silently allowing

```text
new correlations / memory across cycles.
```

This can enlarge the achievable detector-channel set.

---

## 4. Established thermodynamic warning

Correlated-catalytic thermodynamics shows that allowing small residual correlations can radically enlarge microscopic state convertibility.

Shiraishi and Sagawa showed that correlated-catalytic state conversion in a quantum/single-shot thermodynamic setting can be characterized by the standard nonequilibrium free energy under their stated framework.

Takagi and Shiraishi showed that allowing correlations among catalysts while preserving their local marginals can give extremely strong coherence-manipulation power.

These are prior-art structures, not Experiment-02 novelty.

Their role here is adversarial:

> **a detector resource theorem that checks only catalyst marginals is vulnerable to correlation-assisted counterexamples.**

Primary references for later full audit:

```text
N. Shiraishi and T. Sagawa,
Quantum Thermodynamics of Correlated-Catalytic State Conversion at Small Scale,
Phys. Rev. Lett. 126, 150502 (2021).

R. Takagi and N. Shiraishi,
Correlation in Catalysts Enables Arbitrary Manipulation of Quantum Coherence,
Phys. Rev. Lett. 128, 240501 (2022),
DOI 10.1103/PhysRevLett.128.240501.
```

---

## 5. Repeated detector cycles make the distinction operational

Let a catalyst `C` interact sequentially with detector/source cycles

```text
S_1, S_2, ..., S_n.
```

A marginal-only condition might demand after every cycle

```math
\rho_C^{(k)}=\tau_C.
```

But the joint state may contain

```math
I(C:S_1\cdots S_k)>0,
```

or correlations among the outputs themselves that were mediated by `C`.

Then later cycles do not begin from the same **global** state even though the catalyst's local density matrix is unchanged.

This can produce

```text
cross-cycle memory;
non-Markovian effective behavior;
correlated false events;
correlated gain/noise;
additional state-conversion power.
```

So `locally cyclic` and `independently repeatable` are different requirements.

---

## 6. Strict detector-cycle closure condition

If the purpose is to model a genuinely reusable resource that does not accumulate hidden correlations, the stronger condition is

```math
\boxed{
\rho'_{C R}
=\tau_C\otimes\rho'_R,
}
```

where `R` denotes all source, detector, output, controller, and environmental degrees of freedom inside the declared accounting boundary.

Equivalently, require

```math
\boxed{I(C:R)_{\rm final}=0}
```

in addition to

```math
\rho'_C=\tau_C.
```

This is **strict uncorrelated return**.

If correlated return is allowed instead, the correlation budget must be treated explicitly as part of the resource ledger.

---

## 7. A finite catalyst has a finite instantaneous correlation capacity

For a catalyst of finite Hilbert-space dimension `d_C`, quantum mutual information obeys

```math
\boxed{
I(C:R)\le 2\ln d_C.
}
```

Thus a finite catalyst cannot hold arbitrarily large mutual information with the rest at one instant.

But this does **not** by itself close the loophole:

```text
correlations may be transferred among outputs;
multiple catalysts may correlate with each other;
large catalyst dimension may be used;
small correlations can still alter convertibility strongly;
approximate/correlating catalysis can have singular limits.
```

Therefore catalyst dimension and correlation tolerance may both matter.

---

## 8. Correlation tolerance becomes a resource parameter

A practical theorem may allow a small residual correlation

```math
I(C:R)\le\delta_I.
```

or a state-distance decoupling criterion such as

```math
\|\rho'_{CR}-\tau_C\otimes\rho'_R\|_1\le\delta_C.
```

The achievable detector-channel region can depend discontinuously or strongly on how these tolerances scale with system size, number of cycles, or catalyst dimension.

Therefore statements like

```text
correlations are negligible
```

must not be made without specifying the norm/measure and scaling limit.

---

## 9. Connection to detector noise and history dependence

Correlating catalysts are not only an abstract thermodynamic loophole.

A detector element that returns to the same local macroscopic state while retaining microscopic correlations with prior events can produce history-dependent statistics.

Operationally this resembles

```text
trap memory;
afterpulsing;
slow environmental modes;
correlated gain fluctuations;
colored/non-Markovian noise.
```

The specific physical mechanisms differ, but the information-theoretic warning is the same:

```math
\boxed{
\text{same one-cycle marginal behavior}
\not\Rightarrow
\text{independent identical cycles}.
}
```

A detector channel for repeated operation must therefore specify whether it is memoryless or a channel with memory.

---

## 10. This extends the detector-channel framework

For one isolated event, the classical detector object was

```math
K_D(y|x).
```

For repeated events with hidden internal/catalytic memory, the correct object is generally

```math
\boxed{
P(y_1,\ldots,y_n|x_1,\ldots,x_n),
}
```

not a product

```math
\prod_kK_D(y_k|x_k).
```

Thus the resource-ledger attack has exposed a new structural transition:

```text
memoryless detector channel
-> detector process / channel with memory.
```

The Blackwell/post-processing idea must then be applied at the process level rather than to one-use marginals alone.

---

## 11. Strongest surviving conclusion

The current detector resource ledger must distinguish at least three notions of resource reuse:

```text
LOCAL RETURN
catalyst marginal restored;

UNCORRELATED RETURN
catalyst restored and decoupled from everything else;

APPROXIMATE / CORRELATED RETURN
local state restored within tolerance while correlations are allowed/charged.
```

Only the second corresponds to a strict cycle with no hidden correlation memory.

Therefore:

> **A resource is not operationally `free and reusable` merely because its local state is returned. Correlation with the detector/source/output is itself a resource/state variable and must either be forbidden, bounded, or explicitly included in the achievable-channel ledger.**

---

## 12. Consequence for the current frontier

The proposed resource-constrained detector-channel theorem must not be based only on a list of marginal resource states.

It must specify

```text
resource dimensions;
local resource states;
allowed correlations;
correlation/decoupling tolerance;
number of repeated uses;
whether resource states must return uncorrelated;
whether output histories may accumulate correlations.
```

The next natural attack is **finite-size / single-shot closure**:

> even after correlations are properly charged, can average entropy/free-energy/action constraints predict a guaranteed one-event detector performance, or do fluctuation-sensitive one-shot quantities introduce another independent resource axis?
