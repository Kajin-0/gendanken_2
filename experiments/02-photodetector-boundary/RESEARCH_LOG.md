# Research Log — Experiment 02: The Photodetector Boundary

Chronological reasoning log. This file records **why the direction changed**, especially failed universal boundaries and the missing resource that killed them. Detailed algebra is preserved in dedicated derivation files.

---

## 2026-08-12 — Experiment opened

Starting question:

> At what point does a simple collection of atoms become a photodetector? If light is absorbed and re-emitted versus absorbed and a charge pair is generated, when does that happen and what is the boundary?

Initial intuition:

```text
few atoms
-> bands
-> electron-hole generation
-> photodetector.
```

The project explicitly refused to assume this chain.

---

## Re-emission versus electron-hole generation — corrected

Interband absorption can create an electron-hole excitation which later recombines radiatively.

**Conclusion:** re-emission and pair generation can be stages of one event.

**Direction:** separate absorption physics from detector-record physics.

---

## Universal atom-count threshold — killed

A single microscopic system can encode photon arrival; a macroscopic absorber can fail to retain an accessible record.

**Conclusion:** no universal `N_c` without interaction/readout/persistence/noise constraints.

**Missing coordinate:** operational distinguishability.

---

## Detector defined as hypothesis discrimination

For accessible material states

```math
\rho_D^{(0)},\qquad\rho_D^{(1)},
```

use

```math
\mathcal D_D
=\frac12\|\rho_D^{(1)}-\rho_D^{(0)}\|_1,
```

with equal-prior optimum error

```math
P_{e,\min}=\frac12(1-\mathcal D_D).
```

**Conclusion:** detection is a functional information relation, not a phase-of-matter label.

---

## Absorption as detector boundary — killed twice

A perfect absorber can leave identical accessible detector states.

A dispersive interaction can leave the photon intact while changing a material pointer.

**Conclusion:** absorption is neither sufficient nor universally necessary.

---

## Band formation separated

Increasing atom count can produce a dense, band-like electronic spectrum.

**Conclusion:** atomic-to-band crossover is condensed-matter structure, not detector definition.

---

## Electron-hole generation separated

A semiconductor photon can create an excitation that remains bound, recombines, traps, or fails extraction.

Minimal collection benchmark:

```math
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
```

**Conclusion:** electron-hole generation is transduction, not a complete detector event.

---

## Gain reinterpreted

Gain enlarges/stabilizes an upstream distinction against later readout limitations.

**Conclusion:** gain does not create photon-arrival information that was absent before the gain stage.

---

## Irreversibility reframed

Closed-system evolution may remain unitary while local coherence becomes inaccessible and a metastable record forms.

**Conclusion:** practical irreversibility must be tied to subsystem choice, information dispersal, and record persistence.

---

## Momentary encoding versus retention

A transient `D_D(t)>0` can disappear before allowed readout.

**Conclusion:** acquisition and retention are distinct resources.

---

## Universal deposited-energy lower bound — killed

A degenerate two-state pointer can become orthogonal with zero final bare-energy change.

Finite-time pure-state separation still requires interaction action:

```math
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon).
```

Perfect discrimination requires `pi hbar/2`.

**Conclusion:** final deposited energy fails; interaction action survives conditionally.

Detailed derivation: `INTERACTION_ACTION_LOWER_BOUND.md`.

---

## Constrained atom count recovered

If each constituent supplies at most action `a_max`, then

```math
N
\ge
\left\lceil
\hbar\arcsin(1-2\epsilon)/a_{\max}
\right\rceil.
```

**Conclusion:** `N_min` can emerge only after a microscopic resource cap is stated.

---

## Exact one-photon + N-dipole benchmark

For identical resonant dipoles,

```math
G=g\sqrt N,
```

and

```math
\mathcal D_D(t)=\sin^2(g\sqrt Nt).
```

Perfect transient first-lobe transfer requires

```math
N_{\min}=\left\lceil(\pi/(2g\tau))^2\right\rceil.
```

**Conclusion:** a many-atom threshold can arise from collective coupling and finite interaction time without band formation.

Detailed derivation: `N_DIPOLE_SINGLE_MODE_MODEL.md`.

---

## Coherent transfer as persistent detection — killed

The excitation Rabi-oscillates back into the optical mode.

**Conclusion:** acquisition is not yet persistent record.

---

## Record trapping introduced

For collective coupling `G`, optical loss `kappa`, unwanted matter loss `gamma`, and desired trapping `Gamma`,

```math
P_R
=\frac{4G^2\Gamma}
{(\kappa+\gamma+\Gamma)[4G^2+\kappa(\gamma+\Gamma)]}.
```

The formula was cross-checked numerically at about `1e-11` absolute agreement in tested cases.

Detailed derivation: `COHERENT_CAPTURE_TO_RECORD.md`.

---

## More irreversibility is always better — killed

The trapping rate has a finite optimum; for `gamma=0`,

```math
\Gamma_{\rm opt}=2G.
```

Too little trapping fails to freeze the event; too much overdamps acquisition.

**Conclusion:** record formation is a rate-matching problem.

---

## Traveling-wave capture introduced

The photon was no longer placed inside the mode by assumption.

Clean one-port matching gives

```math
\Gamma_{\rm match}=4G^2/\kappa
```

and unit resonant record conversion.

Detailed derivation: `TRAVELING_WAVE_CAPTURE.md`.

---

## Peak-efficiency atom threshold — killed

The critical-coupling condition works for any nonzero `G` if arbitrarily slow/narrowband operation is allowed.

**Conclusion:** peak monochromatic efficiency does not impose positive `N_min`.

**Missing resource:** bandwidth / interaction time.

---

## Optical escape and cooperativity separated

Optimized external efficiency becomes

```math
\eta_{R,\max}
=\eta_{\rm esc}\frac{C_N}{1+C_N}.
```

**Conclusion:** more atoms cannot repair inaccessible optical escape.

---

## Finite bandwidth restored a constrained matter threshold

In a clean matched Lorentzian benchmark,

```math
P_R=\Gamma/(\Gamma+B),
\qquad
\Gamma=4Ng^2/\kappa.
```

**Conclusion:** weak coupling trades against bandwidth.

---

## Literal total atom count — killed

For unequal microscopic couplings,

```math
G^2=\sum_j|g_j|^2.
```

Only the bright mode-weighted combination participates.

**Conclusion:** the relevant microscopic resource is mode-weighted oscillator strength, not total physical `N`.

Detailed derivation: `MODE_WEIGHTED_OPTICAL_DEPTH.md`.

---

## Continuum limit -> optical depth

For dilute single-pass matter,

```math
\mathrm{OD}=n\sigma L,
\qquad
P_{\rm abs}=1-e^{-\mathrm{OD}}.
```

**Conclusion:** column density / optical depth replaces total atom count in extended matter.

Resonant critical coupling showed that architecture can trade absorber strength against dwell time/bandwidth.

---

## Semiconductor chain reconstructed

Minimal signal-record probability:

```math
\eta_s
=\eta_{\rm mode}(1-e^{-\alpha L})\eta_{eh}P_{\rm col}P_{\rm read}.
```

**Conclusion:** electron-hole generation occupies the microscopic transduction stage inside a longer optical-to-record chain.

Detailed derivation: `SEMICONDUCTOR_DECISION_BRIDGE.md`.

---

## Dark-event ceiling derived

For Poisson dark clicks,

```math
\mathcal D_{\rm click}=\eta_s e^{-R_d\tau}.
```

Target error requires

```math
R_d\tau\le-\ln(1-2\epsilon).
```

**Conclusion:** more absorber/gain cannot overcome a dark-event budget that already destroys the evidential contrast.

---

## Continuous Gaussian electrical output introduced

For

```math
H_0:y=n,
\qquad
H_1:y=s+n,
```

with common Gaussian covariance,

```math
d^2
=\langle s,C^{-1}s\rangle
=\int |\tilde s(f)|^2/S_n^{(2)}(f)\,df,
```

and

```math
P_e=Q(d/2).
```

Input referring gives the NEP-weighted waveform integral.

**Conclusion:** the practical detector coordinate is the full noise-weighted waveform distance.

Detailed derivation: `CONTINUOUS_GAUSSIAN_DECISION.md`.

---

## Same D* -> same event performance — killed

For a one-pole white-noise short-pulse benchmark,

```math
d^2
=\frac{E^2D^{*2}}{A\tau}.
```

**Conclusion:** equal scalar low-frequency `D*` can coexist with different event-detection performance because temporal response differs.

**Missing coordinate:** task spectrum / response time.

---

## Equal-covariance noise model generalized

For Gaussian hypotheses with `C_0 != C_1`, the optimum statistic becomes quadratic. Covariance change alone can carry information.

**Conclusion:** the detector output is the complete conditional distribution, not just a mean signal plus nuisance noise.

Detailed derivation: `SIGNAL_DEPENDENT_NOISE.md`.

---

## Poisson count geometry exposed the local nature of SNR

For Poisson means `mu_0,mu_1`,

```math
BC
=\exp[-(\sqrt{\mu_1}-\sqrt{\mu_0})^2/2].
```

Weak-signal finite-background expansion recovers familiar shot-noise scaling.

Zero background instead gives

```math
P_e=\frac12e^{-\lambda_sT}.
```

**Conclusion:** one fixed-noise SNR law cannot cover all count regimes.

---

## Unknown arrival time introduced

For `M` independent candidate temporal modes,

```math
\Lambda(z)=\frac1M\sum_m e^{dz_m-d^2/2}.
```

A max-threshold benchmark gives

```math
P_{\rm FA}=1-\Phi(\eta)^M,
```

```math
P_{\rm miss}=\Phi(\eta-d)\Phi(\eta)^{M-1}.
```

The threshold grows roughly as `sqrt(2 ln M)` at large `M` for fixed small false-alarm probability.

**Conclusion:** timing uncertainty / search complexity is a separate detector resource.

Detailed derivation: `UNKNOWN_ARRIVAL_TIME.md`.

---

## Faster is always better — narrowed

Higher bandwidth can increase known-time waveform information but also increase the number of distinguishable candidate arrival cells in a fixed search window.

**Conclusion:** speed must be interpreted relative to timing uncertainty and false-alarm constraints.

---

## Task-specific scalar constructed

For `p(t)=E q(t)`,

```math
\mathcal K_D[q]
=\int |\tilde q(f)|^2/\mathrm{NEP}_{2,D}^2(f)\,df,
```

with

```math
E_{\min}
=2Q^{-1}(\epsilon)/\sqrt{\mathcal K_D[q]}
```

for known-time equal-prior Gaussian readout.

**Conclusion:** an operational scalar exists after the task and decision target are fixed, but it is not detector-only.

Detailed derivation: `TASK_SPECIFIC_DETECTIVITY.md`.

---

## Universal scalar detector ranking — killed when kernels cross

Define

```math
W_D(f)=1/\mathrm{NEP}_{2,D}^2(f).
```

Pointwise dominance `W_A>=W_B` guarantees A is never worse for any waveform in the task class.

If `W_A-W_B` changes sign, appropriately chosen waveforms reverse the ranking.

**Conclusion:** detector comparison is generally a partial order, not a universal one-dimensional leaderboard.

---

## Returned to thermodynamic lower bounds

The original per-click Landauer claim had already failed at acquisition.

The new question became:

> Does thermodynamics re-enter when the detector must be reused cyclically?

Detailed derivation: `RESET_AND_CYCLE_CLOSURE.md`.

---

## Fixed `k_B T ln2` reset cost — narrowed to the actual record entropy

For a binary event record with event prior `p`, logical entropy is

```math
h(p)=-p\ln p-(1-p)\ln(1-p).
```

Under ideal degenerate-memory quasistatic isothermal erasure with no retained side information,

```math
W_{\rm erase,min}\ge k_BT h(p).
```

`k_BT ln2` is only the unbiased `p=1/2` case.

**Conclusion:** even cyclic erasure does not carry a universal fixed `ln2` cost independent of record statistics.

---

## Local reusable detector -> local Landauer cost — killed by record export

Copy/export the detector record into an external register `R`, then reset the local detector conditionally using `R`.

The local uncertainty becomes `H(M|R)`; for a perfect external copy it can vanish.

**Conclusion:** a detector can be locally reusable without a mandatory local `k_BT ln2` heat packet per click.

**Missing resource:** external record memory / entropy capacity.

---

## Global detector-memory closure appeared to restore erasure

The requirement was strengthened to

```text
detector + controller + all record memories
must return to standard states,
and no event copy may remain outside the accounting boundary.
```

At that stage it appeared that a `k_BT h(p)`-scale erasure problem returned.

**Provisional conclusion at this point:** a Landauer-like bound might live at global cycle closure rather than at photon absorption.

This provisional statement is retained here because the next attack killed it in this form.

---

## Stability versus reset speed derived conditionally

Activated retention gives

```math
E_b
\ge
k_BT\ln[\nu_0\tau_{\rm rec}/(-\ln(1-p_d))].
```

If reset lowers the barrier by `Delta E`, rapid reliable reset gives

```math
\Delta E
\ge
k_BT\ln\left[
\frac{\tau_{\rm rec}\ln(1/\epsilon_r)}
{\tau_r[-\ln(1-p_d)]}
\right]
```

when positive in the common activated-rate model.

**Conclusion:** long retention + tiny false switching + fast reset requires large control of the energy landscape.

**Important correction:** this is a control-range requirement, not a proof that the barrier modulation energy must be dissipated.

---

## Detector-memory global closure — killed by surviving source side information

The previous closure still omitted the original optical/source variable.

For a nondestructive measurement,

```math
|x\rangle_S|0\rangle_M
\xrightarrow{U_{\rm meas}}
|x\rangle_S|x\rangle_M
\xrightarrow{U_{\rm meas}^{\dagger}}
|x\rangle_S|0\rangle_M.
```

The detector memory is exactly reset and no detector record remains, but no logical erasure occurred because `S` still carries `x` and enables reversible uncomputation.

**Conclusion:**

```text
detector/controller/record-memory closure
!=
source-inclusive informational closure.
```

**Missing resource:** surviving source/reference side information.

Detailed correction: `SOURCE_INCLUSIVE_THERMODYNAMIC_CLOSURE.md`.

---

## Closure boundary strengthened to include the information source itself

A true erasure statement now requires that every usable degree of freedom correlated with `X` either

```text
be included in the closure boundary;
be explicitly retained as side information;
or be identified as an environment/resource that changes.
```

If two orthogonal global histories are both required to end in one identical complete state, closed unitary dynamics alone cannot do it. Distinguishability must be exported or discarded somewhere.

**Conclusion:** logical irreversibility begins only when distinguishability is actually destroyed from the controlled description, not merely when a detector pointer is reset.

---

## Positive external work under source-inclusive closure — killed by optical free energy

Even if information is genuinely discarded, the detected optical field can carry usable nonequilibrium free energy.

Schematic resource balance:

```math
W_{\rm ext}
\gtrsim
W_{\rm info}
-\Delta F_{\rm opt}^{\rm avail}
-\Delta F_{\rm other}^{\rm avail}.
```

The exact inequality depends on regime and allowed operations; the robust point is the resource trade.

**Conclusion:** source-inclusive erasure does not imply positive externally supplied detector work.

**Missing resource:** optical free energy.

Do not replace `Delta F_opt^avail` by raw `h nu` automatically; usable nonequilibrium free energy is the disciplined resource.

---

## Active pump / bias reservoir kills detector-only energetic bounds

A photon can trigger release of much larger energy from a bias or pump reservoir.

The same reservoir can also pay record-processing/reset work.

**Conclusion:** if arbitrary nonequilibrium reservoirs are allowed but not charged, no positive architecture-independent detector work bound can survive.

**Missing resource:** pump/bias free-energy consumption.

---

## Binary-memory assumption — killed by continuous reversible transduction

A detector can correlate the optical state with a continuous pointer or output coordinate without a latched bit.

If later uncomputed, no logical erasure is required.

If retained, the output is the record.

If later discarded, thermodynamic cost attaches at the discard stage.

**Conclusion:** thermodynamic cost is tied to discarded information in the full process, not to a mandatory binary detector memory.

---

## Quantum side information makes the closure lesson stronger

Established quantum information thermodynamics allows conditional entropy to become negative for entangled side information. Erasure can then yield work while consuming correlations.

Restoring those correlations closes the resource cycle and restores second-law accounting.

**Conclusion:** even the sign of an erasure-work contribution is conditional on what side information/resources are available.

---

## Current strongest thermodynamic conclusion

The attempt to find a universal heat/work quantum for photodetection has failed repeatedly.

The strongest surviving statement is now:

> **No architecture-independent positive heat or external-work cost per photon event survives when arbitrary side information, optical free energy, nonequilibrium pumps, reversible transduction, or exported records are allowed. A nontrivial thermodynamic constraint appears only after every information-bearing and free-energy-bearing resource is included in the accounting boundary. The surviving law is a generalized resource/second-law balance, not a fixed detector Landauer cost.**

This is not a novelty claim; the information-thermodynamic ingredients are established. The value of the Gedanken path is the detector-specific resource accounting and the sequence of failed boundaries.

---

## Reference-frame access exposed another hidden resource

Unrestricted trace distance assumes the detector can perform the optimal measurement.

Take

```math
|\psi_\pm\rangle
=(|0\rangle\pm|1\rangle)/\sqrt2.
```

These are orthogonal globally.

Without an optical phase reference, `U(1)` phase twirling maps both to

```math
\frac12(|0\rangle\langle0|+|1\rangle\langle1|),
```

so a symmetry-restricted reference-free detector cannot distinguish them.

**Conclusion:** globally available optical information and operationally accessible detector information are not the same when measurement operations are reference constrained.

**Missing resource:** phase/reference-frame asymmetry; clock/synchronization is the temporal analogue.

Detailed derivation: `REFERENCE_FRAME_ACCESS.md`.

---

## Arbitrarily weak critical matching — narrowed by control precision

The clean one-port critical-coupling counterexample used

```math
\Gamma_{\rm match}=4G^2/\kappa.
```

Define

```math
x=\Gamma/\Gamma_{\rm match}.
```

The exact resonant efficiency is

```math
\eta_R=\frac{4x}{(1+x)^2},
```

so

```math
1-\eta_R
=\left(\frac{x-1}{x+1}\right)^2.
```

If a nonzero minimum realizable trapping rate `Gamma_floor` exists, target efficiency `1-epsilon` requires

```math
G^2
\ge
\frac{\kappa\Gamma_{\rm floor}}{4}
\frac{1-\sqrt\epsilon}{1+\sqrt\epsilon}.
```

For identical dipoles this restores a positive conditional `N_min`.

**Conclusion:** the earlier `G->0` perfect-efficiency result used arbitrarily slow and arbitrarily precise rate control as a hidden free resource.

**Missing coordinate:** achievable control range / resolution.

Detailed derivation: `CRITICAL_MATCHING_CONTROL_PRECISION.md`.

---

## Parallel channels exposed a spatial/multiplicity resource

For independent Gaussian channels,

```math
d_{\rm tot}^2=\sum_jd_j^2.
```

For independent Poisson channels, the square-root-count separation exponents likewise add.

Thus many weak known channels can compensate weak per-channel evidence.

If the active channel is unknown, however, a spatial trials penalty appears analogous to unknown arrival time.

**Conclusion:** a per-channel lower bound is not automatically a system-level detector bound.

**Missing coordinate:** total accessible channel count/capacity and knowledge of active-channel identity.

Detailed derivation: `PARALLEL_CHANNEL_RESOURCE.md`.

---

## Search for a universal scalar detector ranking was superseded by channel ordering

The earlier crossing-kernel result already showed that scalar rankings can reverse across tasks.

The stronger question became:

> Is there a mathematically exact sense in which detector A is never worse than detector B for every decision problem?

Represent the detector as a complete statistical channel

```math
K_D(y|x)=P_D(Y=y|X=x).
```

If

```math
K_B=T\circ K_A
```

for a hypothesis-independent post-processing channel `T`, every decision strategy available with B can be simulated from A.

This is the established classical Blackwell/garbling order applied to detector outputs.

If neither detector can be obtained from the other by allowed post-processing, they are incomparable and different tasks can legitimately prefer different detectors.

**Conclusion:** the strongest universal detector comparison is a **partial order on complete detector channels**, not a scalar leaderboard.

At the microscopic level the analogous object is a quantum channel

```math
\Phi_D:\rho_{\rm opt}\mapsto\rho_{\rm out},
```

with proper quantum post-processing/comparison conditions.

Detailed derivation: `DETECTOR_CHANNEL_ORDERING.md`.

---

## Performance hierarchy reorganized

The experiment now has a cleaner hierarchy:

```text
scalar conventional metric
-> task-specific decision metric
-> detector-channel partial order
-> resource-constrained set of physically achievable detector channels.
```

This reframes the research program.

Rather than inventing a generalized scalar `D*`, the next question is:

> What resource constraints define the physically achievable set of detector channels?

---

## Current strongest organizing picture

```text
optical input family / task
-> allowed operations + reference frames
-> optical access / mode overlap
-> mode-weighted interaction resource
-> microscopic transduction
-> acquisition/extraction versus loss
-> persistent record
-> complete conditional output process
-> timing / parallel-channel nuisance structure
-> optimum decision
-> detector-channel partial order
-> record export / local reset
-> source-inclusive information accounting
-> nonequilibrium free-energy accounting if full cyclic thermodynamics is imposed.
```

Every attempted universal scalar/bound has exposed a missing coordinate:

```text
atom count             -> interaction strength/time + mode overlap
peak efficiency        -> bandwidth
weak-coupling matching -> control range / precision
more atoms             -> optical escape
more absorber          -> downstream loss + dark events
fixed-noise SNR        -> hypothesis-dependent statistics
D*                     -> task spectrum / temporal response
known-time score       -> timing-search complexity
per-channel bound      -> parallel channel count
unrestricted D         -> reference-frame / operation access
local reset heat       -> external record capacity
memory-global erasure  -> surviving source/side information
positive cycle work    -> optical/pump nonequilibrium free energy.
```

---

## Current frontier

Do not propose another scalar metric or simple Landauer bound.

Attack whether the present resource ledger is actually closed under

```text
correlating catalysts;
finite-size / single-shot fluctuations;
causal latency / maximum power;
spatially distributed adaptive measurements;
resource states that return locally unchanged but accumulate correlations.
```

Only after those attacks should a detector-channel resource-conversion theorem be attempted.

A focused primary-source prior-art audit remains mandatory before novelty language.
