# Structured-Reservoir Access Audit — When Non-Markovian Spectral Structure Does and Does Not Escape the Harmonic Bound

**Date:** 2026-08-08  
**Status:** conditional extension by passive Markov embedding / `H2` limit; no universal continuum theorem; no novelty claim  

## 1. Question

The harmonic external-access theorem was derived for a finite-dimensional Markov/LTI network terminated by memoryless optical and detector reservoirs.

A realistic detector may instead see

- colored optical coupling;
- structured phonon/electronic reservoirs;
- narrow or broad continua;
- strong memory/non-Markovian response.

Can reservoir structure alone evade the access-resource picture?

The answer is conditional:

> **If the structured passive reservoir can be represented or approximated by an enlarged passive internal network with finite terminal access budgets and convergent `H2` transfer, spectral structure does not evade the harmonic bound.**

A genuine escape requires one of those resource/convergence assumptions to fail.

---

## 2. Augmented-system viewpoint

A standard way to treat a structured reservoir is to pull one or more collective environmental coordinates into an enlarged explicit system.

Schematically,

```text
small detector system
+
structured reservoir
```

is rewritten as

```text
augmented internal system
+
simpler residual reservoir.
```

Reaction-coordinate and pseudomode constructions are established versions of this idea. The structured spectral response becomes additional internal modes/couplings, while the residual bath can often be treated as approximately Markovian.

This observation is important here because `PASSIVE_MULTIMODE_TRANSFER_AREA_BOUND.md` is already independent of the finite internal mode count and coherent topology.

Thus adding finite reaction coordinates does not by itself create an escape.

---

## 3. Finite passive embedding

Let the `n`th passive augmented realization have transfer matrix

```math
G_n(i\omega)
```

from the useful optical terminal reservoir to the irreversible detector terminal reservoir.

Let

```math
L_n=\operatorname{Tr}\Gamma_{L,n},
\qquad
R_n=\operatorname{Tr}\Gamma_{R,n}.
```

For every finite strictly proper stable passive realization,

```math
\boxed{
\|G_n\|_{H2}^2
\le
\frac{2L_nR_n}{L_n+R_n}.
}
```

Here

```math
\|G_n\|_{H2}^2
=
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Tr}
[G_n^\dagger(i\omega)G_n(i\omega)].
```

This statement is exact for each finite embedding.

---

## 4. Conditional continuum-limit theorem

Suppose a sequence of such passive realizations satisfies

```math
G_n\to G
```

in `H2`, meaning

```math
\|G_n-G\|_{H2}\to0.
```

Also suppose

```math
L_n\to L<\infty,
\qquad
R_n\to R<\infty.
```

Then `H2` norm continuity gives

```math
\|G_n\|_{H2}^2\to\|G\|_{H2}^2.
```

The harmonic right-hand side is continuous for positive finite `L,R`, so taking the limit yields

```math
\boxed{
\|G\|_{H2}^2
\le
\frac{2LR}{L+R}.
}
```

Thus a passive structured continuum does **not** evade the harmonic access bound merely by containing infinitely many internal spectral degrees of freedom, provided the continuum is reached through a finite-access `H2`-convergent passive embedding sequence.

This is a mathematical conditional extension, not a claim that every physical continuum satisfies the assumptions.

---

## 5. Exactly how a structured reservoir can escape

The limit argument identifies the possible escape routes precisely.

### Escape A — direct/high-frequency feedthrough

If the limiting transfer has a nonzero frequency-independent prompt component, it is not strictly proper and its all-frequency `H2` area diverges.

This is the case treated in `DIRECT_FEEDTHROUGH_AND_BAND_LIMIT.md`.

### Escape B — divergent terminal access budget

If

```math
L_n\to\infty
```

or

```math
R_n\to\infty,
```

then no finite harmonic resource ceiling survives.

The continuum has been made broadband by increasing the terminal coupling resource itself.

### Escape C — failure of `H2` convergence

A continuum transfer can have a sufficiently slow high-frequency tail or singular spectral structure that the integrated transfer is not finite or the approximants do not converge in `H2`.

Again, this is not an escape at fixed finite integrated access; it means the resource measure must be changed.

### Escape D — nonpassive / time-varying / nonlinear dynamics

Gain, pumping, time modulation, nonlinear conversion, measurement feedback, etc. lie outside this theorem.

### Escape E — terminal bath cannot be reduced to a bounded passive residual access

Some strongly coupled continua may not admit the required passive Markov embedding with finite limiting boundary rates. Such cases remain open rather than being forced into the theorem.

---

## 6. Physical interpretation

The mathematical point is simple:

```text
spectral complexity != free external access.
```

A structured reservoir can store energy, create memory, generate Fano interference, split resonances, broaden or narrow local features, etc.

But if all of that structure can be moved inside the system boundary while the two terminal access budgets remain finite, then the integrated useful transfer remains bounded by their harmonic mean.

The relevant resource is therefore attached to the **boundary between the detector and its asymptotic reservoirs**, not to the number of internal modes used to model memory.

---

## 7. Connection to established non-Markovian methods

Reaction-coordinate methods explicitly enlarge the system by incorporating collective environmental modes and leave a simpler residual bath. They are widely used precisely to handle structured spectral densities and strong/non-Markovian system-bath effects.

This repository does not claim that construction as new.

The present use is only logical:

> whenever a passive structured bath is successfully converted into a finite passive augmented network with bounded Markov terminal couplings, it falls inside the already-derived multimode theorem.

---

## 8. Connection to physical broadband optical limits

A separate line of established photonic theory constrains how much external coupling or absorption bandwidth a real Maxwell structure can have.

Important examples include:

1. Yu, Raman & Fan (2012), who used thermodynamic/Kirchhoff arguments to upper-bound the sum of external coupling rates of optical modes to free-space channels;
2. modern multiresonant absorption theory, which treats mode density and radiative/nonradiative decay rates as explicit resources;
3. Bode-Fano-type optical bounds, which cast broadband absorption as a passive causal impedance-matching problem.

These results suggest a physical bridge:

```text
Maxwell / thermodynamic / matching bound
-> bound on optical access resource
-> harmonic two-access transfer theorem
-> detector transfer bound.
```

No such combined detector theorem is yet claimed here.

---

## 9. Claim boundary

### Established conditionally

If a passive structured-reservoir detector admits finite passive strictly proper approximants satisfying

```math
G_n -> G in H2,
L_n -> L < infinity,
R_n -> R < infinity,
```

then

```math
\boxed{
\|G\|_{H2}^2
\le
\frac{2LR}{L+R}.
}
```

### Not established

- that every Maxwell/material continuum admits such an embedding;
- that `L` and `R` are universally finite without additional material/geometry assumptions;
- that strong non-Markovian detector reservoirs obey a Markov terminal description;
- a universal bound for nonlinear, active, or time-dependent detectors;
- novelty of this limit argument.

---

## 10. Direction change

The structured-reservoir loophole does not kill the access-resource picture under finite passive embedding assumptions.

The remaining physical bottleneck is now sharper:

> **What bounds the terminal optical and irreversible detector access resources themselves in an actual causal material detector?**

The optical side already has relevant thermodynamic, modal-density, material-response, and Bode-Fano prior theory.

The detector-reservoir side is less obvious and likely requires explicit microscopic dissipation / detailed-balance / reset-resource accounting.

That is the next natural layer.