# Experiment 02 Manuscript — Adversarial Referee Review, Round 3

**Date:** 2026-08-13  
**Target:** `MANUSCRIPT_REV2.md`  
**Disposition:** scientifically coherent; major conceptual blocker reduced to one issue — avoid tautology by proving architecture dependence rather than merely defining it

---

## Executive assessment

Revision 2 fixes the main technical and citation problems of the first draft. The manuscript is now substantially cleaner:

- the data-processing issue is corrected;
- the one-atom claim is properly architectural;
- the risky interaction-action bound is removed from the main text;
- the cavity-matching formula is no longer over-attributed;
- the `D*`/NEP convention is explicit;
- the semiconductor example is reduced;
- the thermodynamics section is restrained;
- the measurement endpoint is explicitly an operational level of description rather than a fundamental microscopic classicalization event;
- the Jenčová citation is corrected.

The remaining serious objection is **standalone scientific value**. A hostile referee can still summarize the paper as:

> `A detector is defined by a measurement architecture, therefore detector status depends on the measurement architecture.`

If that is all the paper says, the central result is tautological.

The manuscript needs one formal argument demonstrating that **no classification based only on intrinsic properties of the light-sensitive material subsystem can reproduce operational detector status across all embeddings**. That turns the central conclusion from a naming convention into an explicit counterexample theorem.

---

## Major comment 1 — add an architecture-dependence proposition

Let `M` be a fixed light-sensitive material subsystem implementing an information-bearing channel

```math
\Phi_M:\rho_S\mapsto\rho_Q.
```

Assume there exist optical hypotheses `H0,H1` for which

```math
\Phi_M(\rho_S^{(0)})\neq\Phi_M(\rho_S^{(1)}).
```

Now construct two larger architectures using **the same M** and **the same channel Phi_M**.

### Architecture A — readout

Append a measurement channel `Mcal` chosen so that its outcome statistics differ for the two output states:

```math
\rho_S^{(i)}
\xrightarrow{\Phi_M}
\rho_Q^{(i)}
\xrightarrow{\mathcal M}
p_A(y|H_i).
```

For nonidentical states, some measurement gives nonzero statistical distinguishability; the Helstrom measurement is optimal for binary unrestricted discrimination.

### Architecture B — discard

Append a hypothesis-independent replacement/discard channel

```math
\mathcal T(\rho_Q)=\sigma_0
```

for every input state, followed by the same nominal output interface. Then

```math
p_B(y|H_0)=p_B(y|H_1),
```

so the declared output carries zero information about the optical hypothesis.

The intrinsic material subsystem `M`, its atom count, Hamiltonian, band structure, absorption coefficient, carrier-generation mechanism, and internal transduction dynamics are unchanged between A and B. Operational detection performance changes because the **embedding/readout architecture** changes.

Therefore no architecture-independent Boolean classifier

```math
C=C(\text{intrinsic properties of }M)
```

can in general be both necessary and sufficient for completed detection across arbitrary embeddings.

This is the strongest general statement the paper can make without claiming new measurement theory.

### Suggested proposition

> **Architecture-dependence proposition.** For any fixed light-sensitive subsystem whose output channel preserves nonzero information about the optical hypothesis, there exist downstream embeddings of that same subsystem that respectively preserve and erase that information at the declared measurement output. Hence completed photodetection cannot, in general, be classified solely from intrinsic properties of the light-sensitive material subsystem.

This proposition is elementary and likely not novel as abstract information theory, but it is exactly the missing logical step in the photodetector argument.

---

## Major comment 2 — distinguish `active element`, `detector subsystem`, and `complete detector architecture`

The manuscript is much better on this point, but the terminology should be locked throughout:

```text
active light-sensitive element
    microscopic subsystem directly coupled to the optical field;

transducer
    subsystem/channel mapping optical information into another degree of freedom;

declared detector subsystem
    chosen physical boundary whose accessible outputs are included in the detector model;

complete measurement architecture
    detector subsystem + readout/measurement interface + declared outcome variable.
```

The paper's strongest negative result applies to attempts to classify the **active material element** intrinsically as `detector matter`.

---

## Major comment 3 — connect the Tavis-Cummings threshold directly to decision error

The current `P_req` formulation is correct but slightly detached from the operational language introduced earlier.

After tracing out the optical mode in the ideal single-excitation model,

```math
rho_M^(1)
=
cos^2(Gt)|G><G|
+
sin^2(Gt)|W_N><W_N|,
```

while under no photon

```math
rho_M^(0)=|G><G|.
```

Therefore

```math
D_M(t)=sin^2(Gt).
```

For equal priors,

```math
P_e(t)=1/2 cos^2(Gt).
```

A target `P_e <= epsilon` on the first lobe gives directly

```math
N_min
=
ceil{ [asin sqrt(1-2epsilon)/(g tau)]^2 }.
```

This is more internally consistent than introducing a separate `P_req`.

**Required revision:** use the direct decision-error form in the main text.

---

## Major comment 4 — the semiconductor scaling should move to an appendix or explicit optional box

Even compressed, the `L^s` versus `L^p` model risks being read as a second paper competing for attention with the central argument. It is not necessary to prove architecture dependence and its device realism is deliberately limited.

**Recommendation:** move it to `Appendix A: A reduced semiconductor geometry example` or remove it from the main narrative. The `D*` example already provides the engineering bridge.

---

## Major comment 5 — the Landauer section is now acceptable but can be integrated into the irreversibility section

The current section is scientifically cautious. However, the conceptual argument only needs one paragraph:

```text
measurement correlation != erasure;
Landauer requires a specified logically irreversible reset/erasure process;
therefore kBT ln 2 per click is not a universal detection criterion.
```

Keeping a standalone thermodynamics section makes the manuscript appear broader than it is.

**Recommendation:** fold the argument into the persistent-memory/irreversibility section unless the target venue favors tutorial breadth.

---

## Major comment 6 — the conclusion should explicitly separate three levels of claim

The final paper should distinguish:

### Established formalism

```text
POVMs/instruments;
Helstrom discrimination;
Blackwell/quantum channel comparison;
Tavis-Cummings collective coupling;
matched filtering / NEP;
Landauer / one-shot information thermodynamics.
```

### Derived conditional examples in this manuscript

```text
Tavis-Cummings N_min expressed directly at a target binary decision error;
one-pole D* + tau short-event counterexample;
optional L^s/L^p geometry optimum.
```

### Paper-level synthesis claim

```text
no intrinsic material criterion among atom count, band formation, absorption,
e-h generation, persistent local memory, or microscopic irreversibility
can serve as a universal completed-photodetection boundary;
architecture dependence is demonstrated explicitly by embedding the same
light-sensitive subsystem in readout-preserving and information-erasing downstream architectures.
```

This three-level separation is the manuscript's best defense against both novelty inflation and the accusation that nothing was derived.

---

## Minor comments

1. The abstract is now focused enough; if the architecture-dependence proposition is added, replace the semiconductor sentence with the proposition.
2. `functional role` is good language, but pair it with the explicit embedding construction so it does not sound philosophical.
3. Avoid `completed measurement` where a continuous measurement is intended; `declared measurement output` is more general.
4. The mirror example should be phrased as a transducer/optical transformer example, not as proof by ordinary-language convention alone.
5. A schematic figure would materially help: same material block `M`, two downstream branches `measure` and `discard`, with different output distinguishability. This is optional for the theory draft but strongly recommended for submission.

---

## Publication assessment

### As conventional original-theory Article

**Current:** weak-to-moderate. The formal ingredients are established and the central synthesis may be judged obvious unless the embedding proposition is made explicit and the venue values conceptual clarification.

### As foundations/conceptual article

**Current:** moderate-to-strong after one more revision. The question is intuitive, the failed-boundary sequence is useful, and the same-subsystem/different-embedding construction gives the paper a crisp logical core.

### As Perspective / advanced pedagogical paper

**Current:** strong, provided the journal accepts unsolicited papers of that type.

---

## Recommended action

Create `MANUSCRIPT_REV3.md` with:

1. the architecture-dependence proposition as the central formal result;
2. Tavis-Cummings threshold expressed directly in decision-error language;
3. semiconductor scaling moved to an appendix;
4. Landauer compressed into the irreversibility discussion;
5. a three-level claim taxonomy in the scope/conclusion.

After that revision, perform a final novelty/usefulness review rather than adding new physics to Experiment 02.
