# Interaction-Action Lower Bound — Experiment 02

**Date:** 2026-08-12  
**Status:** first constrained lower-bound result; pure conditional-unitary model  
**Priority:** no novelty claim; built from established quantum-state geometry / speed-limit physics

## 1. Why this branch exists

The previous stage killed several tempting universal detector resources:

```text
atom count alone         -> not universal
photon absorption        -> neither necessary nor sufficient
electron-hole generation -> not sufficient
macroscopic gain         -> downstream stabilization, not initial information creation
per-click k_B T ln 2     -> cannot be attached to detection without reset logic
```

The next question is therefore sharper:

> If a detector must create a specified photon/no-photon distinction in a finite time, is there any resource that cannot be made arbitrarily small?

A useful surviving candidate is **interaction action**: the time integral of the photon-conditioned Hamiltonian scale that actually drives the two detector branches apart in state space.

This is not an energy-dissipation bound. It is a finite-time distinguishability bound.

---

## 2. Minimal conditional-unitary detector

Let the detector start in the same pure state

```math
|D_0\rangle.
```

Under the no-photon hypothesis, let its Hamiltonian be

```math
H_0(t)=H_D(t).
```

Under the one-photon hypothesis, let

```math
H_1(t)=H_D(t)+V(t),
```

where `V(t)` is the photon-conditioned interaction term.

The two detector branch states after time `tau` are

```math
|D^{(0)}(\tau)\rangle=U_0(\tau)|D_0\rangle,
```

```math
|D^{(1)}(\tau)\rangle=U_1(\tau)|D_0\rangle.
```

Define the branch angle

```math
\theta(\tau)
=
\arccos
\left|
\langle D^{(0)}(\tau)|D^{(1)}(\tau)\rangle
\right|,
\qquad
0\le\theta\le\frac{\pi}{2}.
```

For two pure states their trace distance is

```math
\mathcal D_D=\sin\theta.
```

Thus an equal-prior binary error target

```math
P_e\le\epsilon
```

requires

```math
\mathcal D_D\ge1-2\epsilon,
```

or

```math
\boxed{
\theta\ge\theta_\epsilon
\equiv
\arcsin(1-2\epsilon).
}
```

Examples:

```text
epsilon = 0.10  -> theta_epsilon = 0.9273 rad
epsilon = 0.01  -> theta_epsilon = 1.3705 rad
epsilon = 0.001 -> theta_epsilon = 1.5075 rad
epsilon = 0     -> theta_epsilon = pi/2
```

The target approaches an orthogonal-state rotation as the allowed decision error approaches zero.

---

## 3. Remove common detector evolution

Define the relative propagator

```math
W(t)=U_0^\dagger(t)U_1(t).
```

Then

```math
|\chi(t)\rangle=W(t)|D_0\rangle
```

contains exactly the state-space separation caused by the photon-conditioned interaction after the common detector evolution is removed.

In the interaction picture,

```math
i\hbar\frac{d}{dt}|\chi(t)\rangle
=V_I(t)|\chi(t)\rangle,
```

where

```math
V_I(t)=U_0^\dagger(t)V(t)U_0(t).
```

The branch overlap is

```math
\left|
\langle D^{(0)}(t)|D^{(1)}(t)\rangle
\right|
=
|\langle D_0|\chi(t)\rangle|.
```

So the detector problem has become a state-rotation problem generated only by the differential photon-conditioned interaction.

---

## 4. Geometric speed bound

For pure-state unitary evolution, the Fubini--Study angle cannot increase faster than the Hamiltonian uncertainty divided by `hbar`:

```math
\frac{d\theta}{dt}
\le
\frac{\Delta_\chi V_I(t)}{\hbar},
```

with

```math
(\Delta_\chi V_I)^2
=
\langle\chi|V_I^2|\chi\rangle
-
\langle\chi|V_I|\chi\rangle^2.
```

Integrating gives

```math
\theta(\tau)
\le
\frac{1}{\hbar}
\int_0^\tau
\Delta_\chi V_I(t)\,dt.
```

Define the **interaction-uncertainty action**

```math
\mathcal A_\Delta
\equiv
\int_0^\tau
\Delta_\chi V_I(t)\,dt.
```

Then any detector in this model meeting error target `epsilon` must obey

```math
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
}
```

For perfect photon/no-photon discrimination,

```math
\boxed{
\mathcal A_\Delta
\ge
\frac{\pi\hbar}{2}.
}
```

This is the first nontrivial surviving lower bound in Experiment 02.

It is deliberately narrow:

```text
pure initial detector state
conditional unitary branch model
binary vacuum / one-photon hypotheses
finite interaction interval tau
unrestricted optimal final detector measurement
```

Open-system and mixed-state generalizations require a Bures-angle / generator treatment and are not silently assumed here.

---

## 5. Counterexample that kills a universal deposited-energy bound

Take a detector pointer with two degenerate bare states,

```math
H_D=0,
```

and a photon-conditioned interaction

```math
V
=
\frac{\hbar\Omega}{2}\sigma_y.
```

Let the detector begin in `|0>`. The no-photon branch remains

```math
|D^{(0)}(t)\rangle=|0\rangle,
```

while the photon branch is

```math
|D^{(1)}(t)\rangle
=
\exp\left(-i\frac{\Omega t}{2}\sigma_y\right)|0\rangle.
```

At

```math
\Omega\tau=\pi,
```

the detector state becomes orthogonal:

```math
|D^{(1)}(\tau)\rangle=|1\rangle
```

up to phase.

Because the bare pointer states are degenerate,

```math
\Delta\langle H_D\rangle=0.
```

So the detector can acquire a perfectly distinguishable record with zero change in bare detector energy in this idealized model.

But the interaction action is nonzero:

```math
\Delta V=\frac{\hbar\Omega}{2},
```

therefore

```math
\mathcal A_\Delta
=
\frac{\hbar\Omega\tau}{2}
=
\frac{\pi\hbar}{2}.
```

The model exactly saturates the perfect-discrimination action bound.

Conclusion:

```text
net deposited detector energy -> not a universal acquisition resource;
interaction action            -> survives this counterexample.
```

This does **not** show that a real detector can operate without energetic overhead. It isolates the logical point that distinguishability itself does not require a nonzero final energy separation.

---

## 6. Conditional atom-count bound recovered

Now return to the original atom-count intuition, but add an explicit microscopic constraint.

Suppose the photon-conditioned interaction decomposes as

```math
V_I(t)=\sum_{j=1}^{N}v_j(t).
```

For each atomic/local contribution define the half spectral range

```math
g_j(t)
\equiv
\frac{\lambda_{\max}[v_j(t)]-\lambda_{\min}[v_j(t)]}{2}.
```

For any state,

```math
\Delta v_j\le g_j.
```

The spectral range is subadditive, so

```math
\Delta V_I(t)
\le
\sum_{j=1}^{N}g_j(t).
```

Define each atom's maximum available interaction action

```math
a_j
\equiv
\int_0^\tau g_j(t)dt.
```

Combining this upper bound with the required geometric action gives

```math
\boxed{
\sum_{j=1}^{N}a_j
\ge
\hbar\arcsin(1-2\epsilon).
}
```

If every atom is constrained by

```math
a_j\le a_{\max},
```

then

```math
\boxed{
N
\ge
\frac{\hbar\arcsin(1-2\epsilon)}{a_{\max}}.
}
```

Since `N` is integral, the engineering lower bound is the ceiling of the right-hand side.

For perfect discrimination,

```math
\boxed{
N
\ge
\frac{\pi\hbar}{2a_{\max}}.
}
```

This is the first clean answer to the experiment's original question:

> There is no universal critical atom count, but a minimum atom count appears immediately once the maximum photon-conditioned action available from each atom is specified.

The atom count is therefore a **derived resource count**, not the fundamental detector boundary.

---

## 7. What the atom-count bound does and does not say

The bound is robust to whether the optical interaction is called absorptive, dispersive, charge-generating, etc. Those mechanisms merely determine the accessible `v_j(t)` and therefore the action budget.

It does **not** yet include

```text
mixed initial detector states
thermal occupation
open-system decoherence during acquisition
photon loss into inaccessible modes
finite measurement efficiency
restricted measurement bases
record retention after acquisition
reset / dead time
many-photon backgrounds
continuous-wave fields
```

Nor does it assume independent atoms. Correlations can alter how close a real architecture comes to the additive spectral-range ceiling. The stated `N` bound uses only the per-local-term action cap and is therefore intentionally conservative within its model.

---

## 8. Retention is a different bound

The action result governs **record creation**. It says nothing by itself about how long the record survives.

For an activated bistable pointer with dark escape rate

```math
\Gamma_d
=\nu_0\exp\left(-\frac{E_b}{k_BT}\right),
```

the probability of a spontaneous false switch during retention interval `tau_rec` is

```math
p_d
=1-e^{-\Gamma_d\tau_{\rm rec}}.
```

Demanding

```math
p_d\le p_{d,\max}
```

gives the conditional barrier requirement

```math
\boxed{
E_b
\ge
k_BT
\ln\left[
\frac{\nu_0\tau_{\rm rec}}
{-\ln(1-p_{d,\max})}
\right].
}
```

For small `p_d`,

```math
E_b
\gtrsim
k_BT
\ln\left(
\frac{\nu_0\tau_{\rm rec}}{p_d}
\right).
```

This is useful engineering physics but **not universal detector thermodynamics**. It assumes activated escape with an Arrhenius rate and a well-defined attempt frequency.

Counterexamples to universality include architectures whose stability is controlled primarily by symmetry, selection rules, isolation, active correction, topology, or nonthermal dynamics.

---

## 9. Acquisition, retention, reset separate naturally

The first lower-bound attack suggests a three-stage resource decomposition:

```text
ACQUISITION
photon-conditioned interaction action
A_Delta >= hbar theta_epsilon

RETENTION
architecture-specific stability against false evolution
for activated pointer: E_b/k_B T >= logarithmic reliability requirement

RESET
thermodynamic / logical cost depends on how the stored record is erased or recycled
```

This is stronger than treating `energy per detected photon` as one indivisible number.

A detector can in principle have

```text
small or zero net acquisition-energy change,
large interaction action,
large retention barrier,
and a separate reset cost.
```

These resources answer different physical questions.

---

## 10. Why this matters for real photodetectors

The framework creates a common language for apparently different detector mechanisms.

### Photoconductor / photodiode

The optical interaction moves population into carrier states. Collection and bias convert the microscopic distinction into an electrical record. Per-absorbed-photon energy deposition is natural, but the abstract acquisition bound concerns the state-space separation generated by the interaction, not the later electrical energy delivered by the bias supply.

### APD / SPAD

Avalanche multiplication mainly belongs to amplification / record stabilization. The original photon must first perturb a degree of freedom enough to seed a branch distinguishable from the dark trajectory.

### Bolometer

The pointer is thermal; acquisition and retention are tied more directly to energy and heat capacity. This is an architecture in which an energy-like resource may become the natural constrained bound, even though it is not universal across all detectors.

### Dispersive / nondestructive detector

The photon can survive. The interaction action can still rotate a matter pointer state while absorption tends toward zero.

Thus the action formulation unifies absorptive and nonabsorptive detection more naturally than an absorbed-energy criterion.

---

## 11. Adversarial status

### Killed

```text
K1: nonzero final detector energy separation is necessary for detection.
K2: a universal minimum deposited/dissipated energy follows from target discrimination alone.
K3: atom count by itself is the fundamental lower-bound coordinate.
```

### Survives conditionally

```text
S1: finite-time pure-state branch separation requires finite integrated Hamiltonian uncertainty.
S2: a per-atom cap on differential interaction action induces an explicit minimum N.
S3: activated thermal retention induces a logarithmic barrier-height requirement.
```

### Still open

```text
O1: mixed-state / finite-temperature acquisition bound.
O2: open-system bound when the environment participates in record creation.
O3: whether a useful bound can be stated directly in experimentally measurable optical quantities such as cross section, oscillator strength, photon dwell time, or cooperativity.
O4: whether many-body entanglement changes practical N scaling under physically realistic local-coupling constraints.
O5: information-disturbance bound when absorption is explicitly forbidden.
O6: mapping acquisition action to semiconductor matrix elements and detector bandwidth.
```

---

## 12. Closest established foundations

The geometric speed statement is established quantum mechanics, not a new theorem of this experiment.

- J. Anandan and Y. Aharonov, **"Geometry of quantum evolution,"** *Physical Review Letters* **65**, 1697 (1990), DOI `10.1103/PhysRevLett.65.1697`.
- M. M. Taddei, B. M. Escher, L. Davidovich, and R. L. de Matos Filho, **"Quantum Speed Limit for Physical Processes,"** *Physical Review Letters* **110**, 050402 (2013), DOI `10.1103/PhysRevLett.110.050402` — relevant for later nonunitary generalization.
- R. Landauer, **"Irreversibility and Heat Generation in the Computing Process,"** *IBM Journal of Research and Development* **5**, 183--191 (1961), DOI `10.1147/rd.53.0183` — relevant to reset/logical irreversibility, not automatically a per-detection acquisition bound.

No novelty claim is attached to the speed-limit mathematics or Landauer principle. The potentially useful research direction is their disciplined application to the **detector-boundary decomposition** and the resulting constrained atom-count question.

---

## 13. Next attack

The next step should not be another abstract resource guess.

Take the action bound and ask whether a real photon--matter interaction supplies enough action under measurable microscopic constraints.

The most natural next specialization is a one-photon interaction with `N` identical two-level absorbers or dipoles:

```text
single-photon wavepacket
-> per-dipole coupling g
-> finite interaction/dwell time
-> collective coupling scaling
-> achievable detector-state trace distance
-> minimum N for specified epsilon and tau
```

This will test whether the new bound can be expressed in optical quantities such as oscillator strength, mode volume, cross section, optical depth, or cooperativity rather than an abstract Hamiltonian norm.
