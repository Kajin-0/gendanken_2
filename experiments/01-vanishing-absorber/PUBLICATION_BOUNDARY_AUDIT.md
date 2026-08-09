# Publication-Boundary Audit — What Is Known, What Is Derived, and What Is Still Missing

**Date:** 2026-08-08  
**Status:** focused publication-level boundary assessment; **no novelty or priority claim**  

## 1. Purpose

The project has accumulated a coherent chain from propagating optical capture to detector-side access and then to nonequilibrium readiness / thermal irreversibility.

Before opening another branch, this note asks the question a skeptical theoretical-physics reviewer would ask:

> **Is there already a paper here, or are the current results primarily a useful synthesis of known theories plus supporting corollaries?**

Current verdict:

> **The research is scientifically coherent and worth continuing, but the present chain is not yet strong enough to freeze into a manuscript.**

The reason is not that nothing interesting was found. The reason is that the strongest potentially distinct statements still have either uncertain mathematical priority or can plausibly be characterized as compositions of established results.

---

## 2. Closest prior framework A — incoming quantum field, absorption, amplification

Steve M. Young, Mohan Sarovar, and François Léonard,

**“General Modeling Framework for Quantum Photodetectors,”**
*Physical Review A* **98**, 063835 (2018), DOI `10.1103/PhysRevA.98.063835`.

This work already treats

```text
quantized incoming photon field
+
absorption
+
internal detector dynamics
+
amplification / monitored detector states
```

as one coupled quantum system.

It handles single- and multiphoton field states, multiple detector architectures, and performance metrics.

### Consequence for this repository

The repository cannot claim novelty for

- placing a propagating quantum field and detector matter in one model;
- dynamically coupling photon absorption to amplification;
- defining efficiency, dark counts, latency/jitter, etc. in a quantum photodetector framework.

A future paper must add a physically distinct resource constraint, not merely rebuild this formalism.

---

## 3. Closest prior framework B — autonomous detector thermodynamics

Emanuel Schwarzhans et al.,

**“Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition,”**
*PRX Quantum* **7**, 033001 (2026), DOI `10.1103/wm5p-tjtg`.

This work already constructs a detector as an autonomous nonequilibrium thermal machine and analyzes

- detection efficiency;
- gain;
- jitter;
- dead time;
- internal dark counts;
- entropy production / dissipation.

The detector is maintained in a nonequilibrium steady state by a work-producing thermal machine.

Their transient detection model couples the detector gain medium to a target excitation that is already represented inside a target system rather than deriving a propagating optical capture spectrum from an asymptotic incident field.

### Consequence for this repository

The repository cannot claim novelty for

- autonomous detector thermodynamics;
- reset / metastable-state preparation as a thermodynamic resource;
- entropy-production versus detector-performance tradeoffs;
- generic dark-count / jitter / dead-time tradeoffs.

The useful gap, if one exists, lies at the **capture interface**, not in rebuilding the detector back end.

---

## 4. Closest prior framework C — broadband optical access

Zongfu Yu, Aaswath Raman, and Shanhui Fan,

**“Thermodynamic Upper Bound on Broadband Light Coupling with Photonic Structures,”**
*Physical Review Letters* **109**, 173901 (2012), DOI `10.1103/PhysRevLett.109.173901`.

They show that the sum of external coupling rates from optical modes into a specified free-space radiation channel is thermodynamically bounded.

This directly constrains broadband coupling and was already used to derive broadband absorption limits.

More recent work further reduces the novelty space:

- Stéphane Collin and Maxime Giteau, *PRX Energy* **5**, 023006 (2026), derive upper bounds for broadband absorption with multiple overlapping resonances;
- Emanuele Corsaro, Andrea Alù, and Carlo Forestiere, arXiv:2606.24658 (2026), derive Bode–Fano limits for broadband absorption of passive subwavelength objects by mapping optical scattering to impedance matching.

### Consequence for this repository

Do not claim novelty for

- external/internal rate matching as the origin of optimal absorption;
- the fact that many resonances do not provide unlimited broadband absorption for free;
- passive causality / matching constraints on absorption bandwidth;
- external-coupling rate-sum limits.

Any detector result must use these as inputs or comparisons, not rediscover them under detector terminology.

---

## 5. Current result A — harmonic two-access transfer-area theorem

The internally derived finite passive-network result is

```math
\boxed{
\mathcal I_{L\to R}
\le
\frac{2LR}{L+R},
}
```

with

```math
L=\operatorname{Tr}\Gamma_L,
\qquad
R=\operatorname{Tr}\Gamma_R.
```

The exact Gramian decomposition is

```math
\boxed{
\frac{\mathcal I_{L\to R}}2
=
\sum_i
\frac{\ell_i r_i}
{\ell_i+r_i+\iota_i}.
}
```

The theorem is tight and survives arbitrary finite coherent modal overlap / interference inside the stated passive network class.

### What is genuinely useful about it

It packages the detector as a **two-access problem**:

```text
propagating optical access
+
irreversible receiving / detector access.
```

It gives an interference-tolerant integrated-transfer statement without resolving the internal system into isolated Lorentzians.

### Reviewer-level weakness

Its proof is based entirely on standard linear-systems machinery:

- `H2` norm;
- controllability Gramian;
- Lyapunov equation;
- passivity;
- Cauchy–Schwarz.

A targeted search has not found the exact formula in this detector/passive-port form, but that is not strong evidence of novelty. Closely related Gramian and transmission-sum structures occur throughout control, scattering, transport, and network theory.

A mathematically sophisticated reviewer could reasonably say:

> “This is a clean corollary of standard passive-system identities unless the authors establish that the exact trace-harmonic inequality is previously unstated and physically consequential.”

### Current status

**Keep as a load-bearing supporting theorem. Do not make it the paper's sole novelty claim yet.**

---

## 6. Current result B — free-space optical access to detector access

Combining the prior Yu–Raman–Fan optical coupling ceiling with the harmonic theorem gives, in the stated one-free-space-channel setting,

```math
\boxed{
\overline T_B
\le
\frac{R_B}{R_B+W/(4\pi)}
}
```

and therefore

```math
\boxed{
R_B
\ge
\frac{\eta}{1-\eta}
\frac{W}{4\pi}.
}
```

### Reviewer-level strength

This expresses a broadband photodetector requirement in a clean language:

> once optical access is pushed to its thermodynamic ceiling, broadband capture requires irreversible detector-side access that grows with bandwidth.

### Reviewer-level weakness

The algebra is a composition of

1. an established optical coupling-rate sum bound;
2. the repository harmonic passivity corollary.

A reviewer could call it a useful reformulation rather than a new physical law.

### Current status

**Useful bridge, not yet an independent publication claim.**

---

## 7. Current result C — thermal irreversibility chain

Under local detailed balance,

```math
\frac{k_\uparrow}{k_\downarrow}
=e^{-\Delta/(k_BT)}.
```

Combining this with the restricted detector-access requirement gives

```math
\boxed{
k_\uparrow
\ge
\frac{\eta}{1-\eta}
\frac{W}{2\pi}
 e^{-\Delta/(k_BT)}
}
```

and, for an allowed reverse-activation budget `D_rev`,

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

### Reviewer-level strength

This is the first place in the thought experiment where optical bandwidth is chained explicitly to a detector thermal bias.

### Reviewer-level weakness

`D_rev` is not automatically an observable dark-count rate. The relation combines established detailed balance with a restricted optical-access requirement.

A reviewer could correctly reject any presentation of this formula as a universal efficiency-bandwidth-dark-count theorem.

### Current status

**Conceptually useful; insufficient as a stand-alone novelty claim.**

---

## 8. Current result D — capture-to-click and readiness relations

The serial reference model gives

```math
\overline\eta_{\rm ext}
\le
\eta_D
\frac{R_C}{R_C+W/(4\pi)}.
```

Including stationary ready-state probability

```math
p_r
=\frac1{1+e^{-\mathcal A_r}}
```

gives

```math
\boxed{
\overline\eta_{\rm ext}
\le
\frac{\eta_D}{1+e^{-\mathcal A_r}}
\frac{R_C}{R_C+W/(4\pi)}.
}
```

### Reviewer-level strength

The relation cleanly separates

- optical access;
- accepted bandwidth;
- conditional back-end quality;
- thermodynamic detector readiness.

### Reviewer-level weakness

The composition is elementary once the ingredients are stated. The effective affinity `A_r = ln(u/d)` is not yet connected to a universal minimum work or entropy-production cost.

### Current status

**Reference architecture / intuition, not a paper-level theorem.**

---

## 9. Unified three-level testbed

The unified model established several useful distinctions:

1. stored ready-state free energy can amplify the energy of the registered output quantum while conditional photon capture retains the rate-matching form;
2. gross forward click events and net thermodynamic detector current are not the same observable when reverse jumps exist;
3. a nonequilibrium pump that merely restores the lower optical state cannot make the non-inverted weak-probe absorptive population factor exceed the fully ready value `p_1-p_2=1`.

### Reviewer-level weakness

All three mechanisms have close antecedents:

- three-level maser / thermal-machine physics;
- full counting statistics and distinction between gross jumps and net currents;
- standard optical Bloch population-difference susceptibility.

### Current status

**Excellent analytic testbed, but not itself a novelty candidate.**

---

## 10. What the focused searches did *not* find

Targeted searches were made for combinations of

```text
photodetector
propagating photon / input-output
capture bandwidth
entropy production
thermodynamics
autonomous detector
dark counts
Bode-Fano / passive matching
```

and direct searches combining the Young–Sarovar–Léonard and Schwarzhans frameworks.

No inspected primary source was found that simultaneously treats

```text
externally normalized propagating optical capture spectrum
+
a passive/causal broadband access constraint
+
an autonomous nonequilibrium detector machine
+
internal dark counts and reset / entropy production
```

as one resource-accounting problem.

This is the strongest current indication that the **junction** may be underexplored.

It remains only a negative search result. Priority is unproven.

---

## 11. A skeptical-reviewer assessment

If submitted **now**, the likely strongest criticism would be:

> “The paper elegantly connects known broadband optical bounds, passive linear-system theory, and recent autonomous detector thermodynamics, but the principal equations are mostly corollaries or compositions of existing frameworks. What genuinely new physical obstruction is derived that could not have been inferred from those ingredients separately?”

That criticism would be difficult to answer decisively at the current stage.

The harmonic theorem might ultimately provide part of that answer if its exact form proves genuinely distinct, but relying on uncertain mathematical priority is too fragile.

---

## 12. Go / no-go decision

### Do not write a manuscript yet

The project has enough structure for a serious research note, but not yet a sufficiently isolated new physical result for a strong theoretical photodetector paper.

### Continue the thought experiment

The next branch should attack the most important assumption still protecting the passive capture theorem:

```text
passive / non-inverted optical front end.
```

The decisive question is:

> **Can coherent pumping, parametric frequency conversion, or active/non-Foster matching broaden propagating-photon capture beyond the passive access envelope while preserving high irreversible click probability, and what pump-work / entropy / added-noise resource must scale with the gained bandwidth?**

This is a natural next step because

- active matching is a known way to evade passive Bode–Fano bounds;
- optical frequency conversion can use pump work to connect spectral modes that a passive resonance cannot;
- the repository now has a clear passive baseline against which such an escape can be quantified;
- a genuine **work–bandwidth–capture-efficiency** relation would be qualitatively stronger than another passive composition formula.

---

## 13. Candidate publication shape *if* the active branch succeeds

A future paper could then have a genuinely causal progression:

```text
1. passive capture baseline
2. exact two-access integrated-transfer resource law
3. autonomous thermodynamic detector back end
4. active pump as an explicit escape resource
5. bound/tradeoff connecting pump work, bandwidth, capture, false counts/noise
```

The publication claim would then be about what resource is required to **beat** the passive detector envelope, not about rediscovering the envelope itself.

That is currently the strongest route toward a distinct theoretical result.

---

## 14. Current claim boundary

### Worth preserving

- harmonic two-access transfer theorem;
- fixed-target Hopfield supporting lemma;
- direct-feedthrough and structured-reservoir scope audits;
- optical-to-detector-access bridge;
- distinction between external background photons and internal dark events;
- unified three-level analytic testbed;
- readiness and NESS optical-response audits.

### Not currently sufficient for a headline novelty claim

- the passive harmonic inequality by itself;
- serial capture × back-end efficiency;
- readiness factorization;
- detailed-balance reverse-rate scaling;
- three-level thermodynamic cycle;
- gross-versus-net counting distinction.

### Current next scientific target

**Active/coherently pumped capture as a resource-explicit escape from the passive bandwidth envelope.**