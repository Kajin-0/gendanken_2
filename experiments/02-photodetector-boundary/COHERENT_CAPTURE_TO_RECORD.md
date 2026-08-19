# Coherent Capture -> Persistent Record — Experiment 02

**Date:** 2026-08-12  
**Status:** exact minimal lossy capture/trapping model; analytic result cross-checked numerically  
**Priority:** no novelty claim; closest prior-art boundary not yet audited

## 1. Why this step is necessary

The lossless `N`-dipole model produced a matter excitation with collective coupling

```math
G=g\sqrt N.
```

But the excitation Rabi-oscillates back into the optical mode. That is **acquisition without retention**.

To become detector-like, add the smallest possible process that turns the coherent matter excitation into a long-lived record.

Use four ingredients:

```text
|P> : one photon in the optical mode, matter in ground state
|M> : no photon, one collective bright matter excitation
|R> : long-lived accessible record state
loss : inaccessible failure channels
```

Rates:

```text
G      = g sqrt(N)  coherent photon <-> matter coupling
kappa  = optical-mode population-loss rate
 gamma  = unwanted matter-excitation population-loss rate
Gamma  = desired irreversible record-trapping population rate M -> R
```

No dark record generation is included yet.

---

## 2. No-jump acquisition dynamics

In the one-excitation manifold, the effective amplitudes satisfy

```math
\dot c_P
=-\frac{\kappa}{2}c_P-iGc_M,
```

```math
\dot c_M
=-\frac{\gamma+\Gamma}{2}c_M-iGc_P,
```

with

```math
c_P(0)=1,
\qquad
c_M(0)=0.
```

Define

```math
\lambda=\gamma+\Gamma.
```

The desired record probability is the integrated flux into `|R>`:

```math
P_R
=
\Gamma
\int_0^\infty |c_M(t)|^2dt.
```

This is the probability that the initial in-mode photon eventually becomes a persistent record rather than being lost optically or through the unwanted matter channel.

---

## 3. Exact integrated matter occupancy

Let

```math
Y
=\int_0^\infty|c_M(t)|^2dt.
```

Solving the two-state Lyapunov/integrated-population problem gives

```math
\boxed{
Y
=
\frac{4G^2}
{(\kappa+\lambda)(4G^2+\kappa\lambda)}.
}
```

Therefore

```math
\boxed{
P_R
=
\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)
\left[4G^2+\kappa(\gamma+\Gamma)\right]}.
}
```

This closed form was independently checked by direct numerical integration of the amplitude equations for multiple parameter sets; agreement was at approximately `1e-11` absolute level in the tested cases.

This is the central result of the present step.

---

## 4. Immediate limiting checks

### No record channel

```math
\Gamma\rightarrow0
\quad\Rightarrow\quad
P_R\rightarrow0.
```

Acquisition that is never trapped does not become a persistent record.

### No coherent coupling

```math
G\rightarrow0
\quad\Rightarrow\quad
P_R\rightarrow0.
```

An irreversible record channel cannot create photon information that never entered the matter degree of freedom.

### Infinite optical loss

```math
\kappa\rightarrow\infty
\quad\Rightarrow\quad
P_R\rightarrow0.
```

The photon escapes before a record is formed.

### Unwanted matter loss dominates

Large `gamma` suppresses `P_R` because population reaching `|M>` is diverted into inaccessible decay instead of the desired record.

All four limits behave physically.

---

## 5. There is an optimal record-trapping rate

For fixed `G`, `kappa`, and `gamma`, maximize `P_R` with respect to `Gamma`.

Writing

```math
A=\kappa+\gamma,
```

```math
B=4G^2+\kappa\gamma,
```

the exact optimum is

```math
\boxed{
\Gamma_{\rm opt}
=
\sqrt{\frac{AB}{\kappa}}
=
\sqrt{
\frac{(\kappa+\gamma)(4G^2+\kappa\gamma)}{\kappa}
}.
}
```

This result is meaningful only for `kappa>0`; the `kappa=0` limit has different behavior because there is no competing optical escape channel.

For negligible unwanted matter loss,

```math
\gamma=0,
```

the optimum collapses to the especially simple result

```math
\boxed{\Gamma_{\rm opt}=2G=2g\sqrt N.}
```

Thus the best trapping rate is of the same order as the coherent photon--matter transfer rate.

---

## 6. Why too much irreversibility can hurt

This model gives a useful correction to the intuitive narrative

```text
more irreversible trapping -> better detector.
```

When `kappa>0`:

### If `Gamma` is too small

The matter excitation is not frozen quickly enough. It can coherently return to the optical mode, after which the photon can escape through `kappa`, or it can be lost through `gamma`.

### If `Gamma` is too large

The matter state is broadened/overdamped so strongly that coherent transfer from `|P>` into `|M>` is inhibited. While transfer is suppressed, the photon can leak through `kappa`.

Therefore

```text
Gamma too small -> insufficient retention
Gamma too large -> suppressed acquisition
```

and a finite rate-matching optimum appears.

This is closely related in spirit to overdamping / quantum-Zeno / impedance-matching phenomena, but the exact prior-art mapping has not yet been audited and no novelty claim is made.

---

## 7. Maximum record probability

At the optimum trapping rate,

```math
\boxed{
P_{R,\max}
=
\frac{4G^2}
{\left[
\sqrt{\kappa(\kappa+\gamma)}
+
\sqrt{4G^2+\kappa\gamma}
\right]^2}.
}
```

For `gamma=0`, this becomes

```math
\boxed{
P_{R,\max}
=
\left(
\frac{2G}{\kappa+2G}
\right)^2.
}
```

The high-efficiency condition is therefore not merely `Gamma` large. It requires the coherent collective coupling itself to outrun optical loss:

```math
G=g\sqrt N\gg\kappa
```

in this particular initial-in-mode model.

When this is satisfied and `Gamma` is matched near `2G`, `P_R` approaches unity.

---

## 8. A new atom-count law when loss is present

For the clean case

```math
\gamma=0
```

with `Gamma` optimized, suppose a persistent record is perfectly distinguishable from the no-photon state and failures leave no false record.

Then the matter-record trace distance at long times is simply

```math
\mathcal D_R=P_{R,\max}.
```

An equal-prior error target `epsilon` therefore requires

```math
P_{R,\max}\ge1-2\epsilon.
```

Let

```math
\eta=1-2\epsilon.
```

Using

```math
\sqrt\eta
\le
\frac{2G}{\kappa+2G},
```

gives

```math
G
\ge
\frac{\kappa}{2}
\frac{\sqrt\eta}{1-\sqrt\eta}.
```

Since

```math
G=g\sqrt N,
```

we obtain

```math
\boxed{
N
\ge
\left[
\frac{\kappa}{2g}
\frac{\sqrt{1-2\epsilon}}
{1-\sqrt{1-2\epsilon}}
\right]^2.
}
```

This is a **loss-and-record constrained atom-count bound** for the stated model.

As `epsilon -> 0`,

```math
1-\sqrt{1-2\epsilon}\approx\epsilon,
```

so

```math
\boxed{
N_{\min}
\sim
\left(\frac{\kappa}{2g\epsilon}\right)^2
\qquad
(\epsilon\ll1,\ \gamma=0,\ \Gamma=\Gamma_{\rm opt}).
}
```

Near-perfect persistent detection is therefore much more demanding than merely producing a transient coherent matter excitation.

---

## 9. Three detector boundaries now appear in one equation chain

The current sequence is

```text
COHERENT ACQUISITION
G = g sqrt(N)

LOSS COMPETITION
G versus kappa and gamma

RECORD FORMATION
Gamma chosen near a finite optimum
```

This gives a more precise answer to the original conceptual question:

> A microscopic optical excitation becomes detector-like not when it simply exists, but when information transfer into matter is fast enough relative to competing loss and is then converted into a sufficiently persistent record at a compatible rate.

The word **compatible** matters. Record formation that is arbitrarily fast is not automatically optimal.

---

## 10. Why this is distinct from ordinary absorption probability

In the lossless Tavis--Cummings step,

```math
\mathcal D_D(t)
=
P_{\rm matter\ excitation}(t)
```

because the model has only one bright matter state and one optical state.

The present model adds a separate record state. Now the quantity that matters at long times is

```math
P_R,
```

not merely whether the photon ever occupied `|M>`.

A photon can enter the matter excitation and still fail to create a record because it

```text
returns to the optical mode,
is lost from the optical mode,
or decays through an unwanted matter channel.
```

Thus even inside one simple Hamiltonian family,

```text
absorption / excitation transfer
!= persistent detection probability.
```

This reinforces, rather than replaces, the experiment's original absorption counterexample.

---

## 11. Rate matching is a candidate organizing principle

The strongest structural insight from this step is not the exact algebraic form of `P_R`.

It is the appearance of a **rate-matching problem**:

```text
coherent acquisition rate
<-> optical escape
<-> unwanted matter decay
<-> desired record trapping.
```

The detector boundary may therefore be better organized by ratios of dynamical rates than by atom number or absorbed energy alone.

In the simplest clean limit,

```math
\Gamma_{\rm opt}=2g\sqrt N.
```

This suggests a hierarchy:

```text
N controls collective coupling,
collective coupling controls acquisition speed,
acquisition speed sets the useful trapping rate,
loss rates determine achievable record fidelity.
```

That is a physically interpretable route from microscopic constitution to macroscopic detector function.

---

## 12. Important scope limitations

This model assumes

```text
photon already occupies the relevant optical mode at t=0
single excitation
exact resonance
identical coherent dipoles
one collective bright state
Markovian exponential loss channels
no pure dephasing term beyond the lumped unwanted rate
a perfectly distinguishable long-lived record state
no dark record generation
no input-output wavepacket matching problem
no detector reset/dead time.
```

Because the incident photon is placed inside the mode initially, `kappa` here represents competing escape **after loading**, not the full external coupling problem of capturing a traveling photon.

A true photodetector must solve the additional input-coupling / impedance-matching problem.

---

## 13. Adversarial checks

### Check A — can `Gamma -> infinity` make detection perfect?

No when `kappa>0`. The exact formula gives `P_R -> 0` as `Gamma -> infinity` for finite `kappa`, because coherent transfer is overdamped while optical escape remains available.

### Check B — does this contradict the idea that irreversible amplification helps?

No. It shows that the irreversible stage must be coupled appropriately to the information-acquisition stage. Once the record is actually populated, downstream gain may still strongly improve practical readout.

### Check C — is `Gamma_opt=2G` universal?

No. It holds only for `gamma=0` in the stated two-state Markovian model with a photon initially in the mode.

### Check D — is the resulting `N_min` universal?

No. It depends on `g`, `kappa`, the error target, symmetry, resonance, and optimized trapping.

### Check E — is the finite optimum likely entirely new?

Almost certainly not in broad physical form. Closely related rate matching, critical coupling, impedance matching, and quantum-Zeno/overdamping effects are established in quantum optics and open-system dynamics. A direct prior-art audit is mandatory before any distinct claim.

---

## 14. Current strongest conclusion

The thought experiment has progressed through three successive corrections:

```text
NAIVE
many atoms -> band -> pair generation -> detector

OPERATIONAL
photon hypothesis -> distinguishable matter state -> record

DYNAMICAL
coherent information transfer must beat loss
AND
record trapping must be rate-matched to acquisition.
```

A detector boundary is beginning to look less like a static material threshold and more like a **dynamical phase diagram in dimensionless rate ratios**.

Candidate coordinates now include

```math
\frac{g\sqrt N}{\kappa},
\qquad
\frac{g\sqrt N}{\gamma},
\qquad
\frac{\Gamma}{g\sqrt N}.
```

This is the strongest next organizing picture.

---

## 15. Next attack

The current model begins with the photon already inside the optical mode. That sidesteps the most important optical question.

The next step should therefore introduce a traveling single-photon wavepacket coupled through an input port:

```text
traveling photon
-> cavity / resonant absorber loading rate kappa_in
-> parasitic optical loss kappa_loss
-> collective matter coupling g sqrt(N)
-> record trapping Gamma
```

Then determine whether a true **impedance-matching condition** exists for near-unity conversion of an incoming photon into the persistent record state.

That is the point where the Gedanken experiment should begin connecting directly to absorptance, optical cross section, critical coupling, and detector quantum efficiency.
