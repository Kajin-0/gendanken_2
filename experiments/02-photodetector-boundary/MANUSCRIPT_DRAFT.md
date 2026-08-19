# When Does Matter Become a Photodetector?
## An Operational Gedanken Analysis from Absorption to Measurement

**Anonymous draft — 2026-08-13**  
**Experiment 02 manuscript draft**  
**Status:** conceptual/theory manuscript; no claim of a new general measurement formalism

---

## Abstract

At what point does a collection of atoms become a photodetector? The question sounds as though it should have a microscopic answer: perhaps when discrete atomic states become bands, when a photon creates an electron-hole pair, when the absorbed energy becomes irreversible, or when a persistent electrical record appears. We test these possibilities one at a time using deliberately minimal thought experiments. None survives as a universal boundary. A single atom can participate in a detector architecture; a perfect absorber need not leave an accessible record; electron-hole generation can fail to produce a readable event; nondestructive measurements can detect without absorbing the photon; and the material element that mediates the interaction need not retain any persistent local memory if the information is exported to another output degree of freedom. The surviving distinction is operational rather than material. Once an input/output partition is declared, a coherent transducer maps optical information into another quantum system, whereas a detector endpoint supplies a measurement outcome, described in general by a POVM or quantum instrument. We use several quantitative examples to show why apparent microscopic thresholds reappear only after compensating resources are constrained: finite interaction time, collective coupling, optical escape, temporal bandwidth, readout noise, transport, dark events, or decision latency. In particular, a one-pole Gaussian benchmark gives \(d^2=E^2D^{*2}/(A\tau)\) under an explicit one-sided-noise convention, demonstrating that equal conventional \(D^*\) does not imply equal detectability of a short optical event. A semiconductor asymptotic model similarly gives \(L_*\sim[s/(pK)]^{1/p}\) when useful-event probability scales as \(L^s\) while dark exposure scales as \(L^p\), emphasizing that any thickness or atom-count optimum is architecture dependent. The analysis does not propose a new general theory of photodetection; POVM descriptions, quantum-detector modeling, statistical-experiment comparison, and optimum filtering are established. Its purpose is instead to give a compact first-principles answer to the boundary question: photodetector status is a role within a specified measurement architecture, not a phase of matter.

---

## I. Introduction

Photodetectors are normally introduced through their physical mechanisms. A photon is absorbed; a microscopic excitation is produced; that excitation is transported or amplified; and an electrical or optical signal is read out. In a semiconductor, the microscopic description naturally emphasizes interband excitation and electron-hole creation. In an avalanche device, gain and metastability become central. In a superconducting detector, the important degrees of freedom and the route to a macroscopic record are different again. In atomic and cavity systems, photons may be inferred without the kind of irreversible absorption usually associated with a photodiode.

This diversity motivates a deceptively simple question:

> **At what point does a collection of atoms become a photodetector?**

The wording tempts one to search for an intrinsic material threshold. One might imagine a critical atom number \(N_c\), the formation of a band structure, the first possibility of electron-hole generation, an irreversibility threshold, or the emergence of a sufficiently long-lived material record. The aim of this paper is to test those candidate boundaries directly rather than assume one of them in advance.

The exercise is intentionally operational. For two optical alternatives,

\[
H_0:\text{no target optical event},
\qquad
H_1:\text{target optical event},
\]

we ask what physical output is actually accessible and whether its statistics permit discrimination of the alternatives. This perspective is standard in quantum measurement and statistical decision theory. A detector can be represented by a POVM, an instrument, or a more general input-output process; platform-independent photodetector figures of merit can be defined from the POVM [1], and microscopic quantum models can treat field, absorption, and amplification as one coupled system [2,3]. The purpose here is therefore not to introduce another general formalism. It is to use those established ideas as a consistency test on the microscopic intuition that matter must cross a special boundary before it can be called a detector.

The result is negative but useful. No universal atom-count, absorption, carrier-generation, irreversibility, or local-memory criterion survives. Once a physical architecture and readout boundary are fixed, objective detector performance can be calculated. But the location at which one chooses to call a subsystem “the detector” is not fixed by an intrinsic phase transition in the material.

The paper proceeds in the order in which the thought experiment eliminates possible boundaries. Section II defines the minimum operational problem. Sections III–VI test atom count, absorption, electron-hole creation, irreversibility, and persistent memory. Section VII gives the resulting transducer-versus-detector distinction in the language of measurement channels and instruments. Sections VIII–X give quantitative examples showing how real thresholds reappear only after resources and tasks are constrained. Section XI discusses thermodynamic reset. Section XII places the analysis against prior art and states what is and is not being claimed.

---

## II. The minimum operational problem

Consider a physical system \(D\) interacting with an optical input \(S\). The input is prepared under one of two hypotheses, \(H_0\) or \(H_1\). A first attempt at defining detector performance is to compare two conditional states of some accessible detector degree of freedom,

\[
\rho_D^{(0)},\qquad \rho_D^{(1)}.
\]

If arbitrary measurements on that degree of freedom are allowed, the trace distance

\[
\mathcal D_D
=\frac12\left\|\rho_D^{(1)}-\rho_D^{(0)}\right\|_1
\]

sets the optimum equal-prior binary discrimination error through the Helstrom relation [4],

\[
P_{e,\min}=\frac{1-\mathcal D_D}{2}.
\]

Thus 

\[
\mathcal D_D=0
\]

means that the selected output contains no usable information about the optical alternative, while

\[
\mathcal D_D=1
\]

permits perfect discrimination in the unrestricted binary setting.

This already separates **interaction** from **detection**. A photon can interact strongly with matter while leaving the selected output states identical. Conversely, a weak interaction can in principle produce a measurable conditional change if the downstream readout is sufficiently sensitive and sufficiently long observation is allowed.

However, even this first definition is not yet general enough. The state labeled \(D\) need not be the degree of freedom that ultimately carries the record. Later we will replace the material-state criterion by a criterion on the declared accessible output of the full measurement architecture. The temporary use of \(ho_D^{(i)}\) is useful precisely because it lets us see why the material-state boundary eventually fails.

---

## III. No universal critical atom number

### A. One atom already defeats an atom-count definition

Take a single atom \(A\). If the optical transition merely excites it and it later radiates back into an uncontrolled optical mode,

\[
|g\rangle|1_\gamma\rangle
\rightarrow
|e\rangle|0_\gamma\rangle
\rightarrow
|g\rangle|1_{\gamma'}\rangle,
\]

then at late time the atom itself may contain no persistent record of whether the incident photon arrived.

But the same single atom can participate in a detector architecture if its optical interaction controls an accessible output. Ionization is the obvious limiting example,

\[
A+h\nu\rightarrow A^++e^- ,
\]

where collection of the emitted electron can supply the record. Atomic fluorescence can also be used in a measurement architecture when the emitted light is itself measured. Therefore no universal statement of the form

\[
N<N_c:\text{not a detector},
\qquad
N\ge N_c:\text{detector}
\]

can be correct without additional architectural assumptions.

### B. Band formation is a crossover, not the detector boundary

Increasing \(N\) certainly changes the available physics. Discrete atomic levels hybridize into molecular states and, in extended ordered matter, into bands. A useful finite-size criterion for when a continuum or band description becomes adequate is not a special integer \(N\) but the comparison of level spacing with relevant broadening. Schematically,

\[
\delta E\sim \frac{1}{g(E)V},
\]

and a band-like description is useful when

\[
\delta E\ll \Gamma_{\rm eff},
\]

where \(\Gamma_{\rm eff}\) can include thermal, lifetime, disorder, and measurement broadening.

That crossover matters for modeling the microscopic excitation. It does not decide whether the excitation is measured. A macroscopic crystal can absorb light and thermalize without furnishing the output required for a particular detection task. Conversely, a few-level artificial atom can be embedded in a high-fidelity measurement chain.

The first candidate boundary therefore fails:

\[
\boxed{\text{band formation is neither necessary nor sufficient for detector status.}}
\]

---

## IV. Absorption is not the boundary

The next natural candidate is absorption. Ordinary photodetectors often begin with

\[
\text{photon absorbed}\rightarrow\text{material excitation}.
\]

This makes absorption appear almost synonymous with detection. Two counterexamples separate them.

### A. Perfect absorption can fail to produce a record

Imagine a system that absorbs an incident photon with unit probability but later returns all accessible detector degrees of freedom to the same state they would have occupied under \(H_0\). In the selected detector subsystem,

\[
\rho_D^{(1)}(t\rightarrow\infty)=\rho_D^{(0)}.
\]

The photon interacted and may even have been temporarily stored, yet the final accessible material record has zero distinguishability. Perfect absorptance by itself therefore does not imply perfect detection.

### B. Detection need not destroy the photon

A nondestructive measurement provides the converse. An idealized interaction may correlate photon number with a pointer while leaving the photon in the measured number state,

\[
|0\rangle|D_0\rangle\rightarrow |0\rangle|D_0'\rangle,
\]

\[
|1\rangle|D_0\rangle\rightarrow |1\rangle|D_1'\rangle.
\]

If \(D_0'\) and \(D_1'\) are distinguishable, the photon number has been measured even though the photon was not absorbed. Quantum-nondemolition measurement fits naturally into the instrument description discussed below.

Thus

\[
\boxed{\text{absorption is neither universally sufficient nor universally necessary for photodetection.}}
\]

This statement does not diminish the engineering importance of absorptance. In most semiconductor detectors, optical absorption is the first transduction step and strongly limits quantum efficiency. The point is only that absorptance is an implementation coordinate, not the definition of detection.

---

## V. Electron-hole generation is a transduction step, not the completed measurement

The original motivation for the thought experiment came partly from the contrast between atomic excitation/re-emission and semiconductor electron-hole generation. The comparison contains a terminology trap. In a semiconductor, creation of an electron-hole pair is not an alternative to absorption; it is one possible consequence of absorption:

\[
h\nu + e^-_{\rm VB}\rightarrow e^-_{\rm CB},
\]

leaving a hole in the valence band. Symbolically,

\[
h\nu\rightarrow e^-+h^+.
\]

Radiative recombination is a later branch,

\[
e^-+h^+\rightarrow h\nu'.
\]

Nonradiative recombination, trapping, diffusion away from the collecting region, or return to equilibrium can erase the useful excitation before it reaches the readout.

A minimal semiconductor chain is therefore

\[
\text{optical access}
\rightarrow
\text{absorption}
\rightarrow
\text{electron-hole excitation}
\rightarrow
\text{survival/collection}
\rightarrow
\text{readout}.
\]

The useful-event probability may be written schematically as

\[
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read},
\]

where \(\alpha\) is an absorption coefficient and \(L\) an absorber thickness. A simple competing-rate model gives

\[
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}},
\]

with extraction and recombination rates \(\Gamma_{\rm ext}\) and \(\Gamma_{\rm rec}\).

This is enough to defeat another proposed boundary. Electron-hole generation is a microscopic transduction event. It can be essential to a semiconductor detector while still being insufficient to guarantee a readable measurement outcome.

---

## VI. Persistent local memory and microscopic irreversibility also fail

A stronger candidate is that detection occurs only when the material retains a persistent state change. This seems attractive because it distinguishes a transient excitation from a “record.” It also fails as a universal requirement.

Let \(S\) be the optical input, \(D\) a material transducer, and \(R\) an accessible output register. Consider

\[
|0\rangle_S|D_0\rangle|R_0\rangle
\rightarrow
|\psi_0\rangle_S|D_0\rangle|R_0'\rangle,
\]

\[
|1\rangle_S|D_0\rangle|R_0\rangle
\rightarrow
|\psi_1\rangle_S|D_0\rangle|R_1'\rangle.
\]

The material subsystem finishes in exactly the same local state for both hypotheses,

\[
\boxed{
\rho_D^{(0)}=\rho_D^{(1)}=|D_0\rangle\langle D_0|,
}
\]

while the output states satisfy

\[
\rho_R^{(0)}\ne \rho_R^{(1)}.
\]

If the output states are orthogonal, the optical alternatives can be distinguished perfectly from \(R\), despite zero persistent local memory in \(D\).

The material has acted as a transient mediator. It has transferred information into the accessible output and locally returned to its ready state. Persistent memory is therefore not a universal property of the material element. What must persist is only enough correlation **somewhere in the declared measurement chain** for the allowed readout to exploit it.

This also weakens attempts to define detection through microscopic irreversibility. The combined source-detector-environment evolution may remain unitary. Operational irreversibility appears when information disperses into degrees of freedom that are not controlled or reversed. That can be crucial for robust macroscopic records, but it is not a universal microscopic phase boundary separating “detector matter” from “non-detector matter.”

---

## VII. The surviving distinction: transduction versus a declared measurement outcome

The no-local-memory example risks making the definition too broad. A mirror maps an incoming optical mode into a reflected mode,

\[
|1\rangle_{\rm in}\rightarrow |1\rangle_{\rm refl}.
\]

The reflected field certainly contains information about the incident field. Yet a mirror is not ordinarily called a photodetector.

The missing distinction is supplied by quantum measurement theory.

### A. Coherent transducer

A coherent transducer may be represented as a quantum channel

\[
\boxed{
\Phi:\rho_{\rm opt}\mapsto\rho_Q,
}
\]

where \(Q\) is another quantum degree of freedom. The output can carry optical information while preserving coherence or entanglement. A frequency converter, coherent microwave-optical interface, or reversible matter-light mapping can belong to this category.

### B. Detector endpoint

A measurement endpoint with classical outcomes \(y\) is represented by a quantum-to-classical measurement channel,

\[
\boxed{
\mathcal M(\rho)
=\sum_y
\operatorname{Tr}(E_y\rho)
|y\rangle\langle y|,
}
\]

where the positive operators \(E_y\) form a POVM and

\[
p(y|\rho)=\operatorname{Tr}(E_y\rho).
\]

More generally, a quantum instrument \(\{\mathcal I_y\}\) gives both an outcome and a conditional post-measurement quantum state [5]:

\[
p(y|\rho)=\operatorname{Tr}[\mathcal I_y(\rho)],
\]

\[
\rho_y=
\frac{\mathcal I_y(\rho)}{p(y|\rho)}.
\]

This includes nondestructive measurement. The photon or another residual quantum state may survive; what identifies the endpoint is the declared measurement outcome.

The classical-output marginal of the measurement is entanglement breaking, even though the full instrument may retain conditional quantum degrees of freedom. That gives a mathematically objective distinction from a generic coherent transducer once the input/output partition has been fixed.

### C. The cut is physical but not uniquely located by atom count

A practical detector chain can be partitioned at several levels:

\[
\text{absorber}
\rightarrow
\text{carrier system}
\rightarrow
\text{preamplifier}
\rightarrow
\text{discriminator}
\rightarrow
\text{digitizer}.
\]

If microscopic degrees of freedom are modeled explicitly, the effective quantum-to-classical boundary moves. The semiconductor alone may be treated as a transducer feeding a classical electronic readout, or the entire photoreceiver may be treated as one instrument with a digitized outcome.

Thus the strongest answer to the original question is relational:

\[
\boxed{
\text{photodetector status is a role in a declared measurement architecture, not a material phase.}
}
\]

Once the architecture is declared, performance is objective. Before that declaration, no atom number tells us where nature has labeled “detector starts here.”

---

## VIII. Why constrained atom-number thresholds still appear

Rejecting a universal \(N_c\) does not make atom number irrelevant. It changes the question from

> “How many atoms are required to become a detector?”

into

> “Given specified coupling, time, geometry, loss, and readout constraints, how much participating matter is required to reach a target decision error?”

That constrained question can have a precise answer.

### A. Finite-time interaction benchmark

For a pure conditional-unitary benchmark, suppose the two optical hypotheses drive the material pointer along different trajectories. Let the accumulated hypothesis-dependent interaction action be denoted

\[
\mathcal A_\Delta
=\int_0^\tau \Delta V_I(t)\,dt,
\]

with \(\Delta V_I\) chosen consistently as the interaction-strength quantity bounding the rate of state separation. Using the projective-state geometry underlying quantum speed limits [6], the Experiment-02 benchmark gives

\[
\boxed{
\mathcal A_\Delta
\ge
\hbar\arcsin(1-2\epsilon)
}
\]

for equal-prior error no larger than \(\epsilon\) in the stated pure-pointer model. Perfect discrimination requires the corresponding orthogonalization action \(\pi\hbar/2\).

This is not a universal deposited-energy bound. A degenerate pointer can rotate between orthogonal states with zero final bare-energy difference. The resource is finite-time state separation under a bounded interaction, not a fixed heat packet deposited by the photon.

### B. Collective dipoles

For \(N\) identical resonant two-level dipoles coupled to one mode, the symmetric bright state has collective coupling

\[
\boxed{G=g\sqrt N,}
\]

as in the Tavis-Cummings model [7]. The first coherent transfer maximum occurs at a time of order

\[
\tau\sim\frac{\pi}{2g\sqrt N}.
\]

Thus, if the interaction time is capped, a conditional atom-number threshold scales as

\[
N_{\min}\propto (g\tau)^{-2}.
\]

The physical message is not that \(N\) crosses a detector phase transition. It is that many weakly coupled constituents can collectively supply the interaction strength that a finite-time task demands.

### C. External capture and the disappearance of a peak-efficiency atom threshold

Once a traveling photon and an input port are included, another compensation appears. In a clean one-port model, a record-trapping rate can be impedance matched to the light-matter coupling. The Experiment-02 benchmark has

\[
\Gamma_{\rm match}=\frac{4G^2}{\kappa},
\]

where \(\kappa\) characterizes optical escape. Under ideal narrowband conditions, arbitrarily small nonzero \(G\) can in principle approach unit resonant conversion if the matching rate is correspondingly slow. This is the same physical family as impedance-matched cavity capture and quantum-memory state mapping [8].

The apparent atom threshold therefore disappears if arbitrarily long time and arbitrarily narrow bandwidth are allowed. It reappears only when bandwidth, lifetime, control-rate floor, or interaction time is bounded.

This is the recurring structure of the thought experiment:

\[
\boxed{\text{a threshold appears only after the compensating resource is fixed.}}
\]

---

## IX. Conventional \(D^*\) is a task projection, not a complete event metric

The same lesson appears at the opposite end of the detector chain, where microscopic dynamics have already been reduced to electrical responsivity and noise.

Consider binary waveform hypotheses

\[
H_0:y(t)=n(t),
\qquad
H_1:y(t)=s(t)+n(t),
\]

with zero-mean Gaussian noise of common covariance. The optimum decision coordinate is the noise-weighted waveform distance

\[
\boxed{
d^2=\langle s,C^{-1}s\rangle.
}
\]

For stationary noise with a two-sided PSD,

\[
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}\,df,
\]

and the equal-prior optimum error is

\[
P_e=Q(d/2).
\]

If the electrical signal is produced from incident optical power through responsivity \(\mathcal R(f)\), one may refer the noise to the optical input and write

\[
\boxed{
d^2
=\int_{-\infty}^{\infty}
\frac{|\tilde p(f)|^2}{\mathrm{NEP}_2^2(f)}\,df.
}
\]

This is standard matched-filter geometry, and frequency-integrated NEP has direct precedent in event-energy detector theory [9]. Its relevance here is conceptual: a scalar detector metric cannot generally preserve all the temporal information needed for arbitrary tasks.

### A. Explicit one-pole counterexample

Let

\[
h(t)=\frac{1}{\tau}e^{-t/\tau}u(t)
\]

be a normalized one-pole impulse response. A short optical event of energy \(E\) produces

\[
s(t)=\frac{R_0E}{\tau}e^{-t/\tau}u(t).
\]

The signal-energy integral is

\[
\int_0^\infty s^2(t)dt
=\frac{(R_0E)^2}{2\tau}.
\]

Let \(S_n^{(1)}\) be the flat **one-sided** output-noise PSD. Since the two-sided value is \(S_n^{(2)}=S_n^{(1)}/2\), the matched-filter distance becomes

\[
d^2
=\frac{(R_0E)^2}{\tau S_n^{(1)}}.
\]

With the conventional one-sided input-referred NEP,

\[
\mathrm{NEP}_1
=\frac{\sqrt{S_n^{(1)}}}{R_0},
\]

we obtain

\[
\boxed{
d^2=\frac{E^2}{\tau\,\mathrm{NEP}_1^2}.
}
\]

Using

\[
D^*=\frac{\sqrt A}{\mathrm{NEP}_1},
\]

this becomes

\[
\boxed{
d^2=\frac{E^2D^{*2}}{A\tau}.}
\]

Therefore two equal-area detectors with the same quoted low-frequency \(D^*\) but different response times do **not** have equal ability to detect a short fixed-energy event in this model:

\[
d\propto \tau^{-1/2}.
\]

This is not a new theorem about matched filtering. It is a direct counterexample to interpreting one conventional scalar \(D^*\) as a complete detector-performance coordinate.

The conclusion generalizes in form but not in this simple scaling: the complete task requires the whole responsivity/noise spectrum, the signal waveform, the observation interval, and the relevant conditional noise statistics.

---

## X. A semiconductor thickness example: why geometry thresholds are conditional

The same logic can be made explicit in a reduced semiconductor model. The point of the model is not to predict a specific SPAD, HgCdTe photodiode, or photoconductor. It is to show mathematically how a finite optimum thickness emerges from competing architecture-dependent scalings.

Suppose that, in a thin-device regime,

\[
\eta_s(L)\sim S L^s
\]

for the useful event probability, while the mean number of dark events in the relevant decision gate scales as

\[
\mu_d(L)\sim K L^p,
\]

with positive \(S,K,s,p\).

In a leading first-Poisson-mode benchmark, the useful distinguishability scales as

\[
\mathcal D(L)
\sim
S L^s e^{-K L^p}.
\]

Maximizing its logarithm gives

\[
\frac{d}{dL}\ln\mathcal D
=\frac{s}{L}-pK L^{p-1}=0,
\]

hence

\[
\boxed{
L_*
\sim
\left(\frac{s}{pK}\right)^{1/p},
}
\]

and the optimum mean dark exposure is

\[
\boxed{
\mu_*=K L_*^p=\frac{s}{p}.
}
\]

The maximum leading-order distinguishability is

\[
\boxed{
\mathcal D_{\max}
\sim
S
\left(\frac{s}{e pK}\right)^{s/p}.
}
\]

These expressions make an important correction to any attempt to universalize a particular optimum. For linear thin absorption, \(s=1\). If a bulk dark-generation rate scales with thickness and the decision gate itself scales with carrier transit time, then \(p=2\), yielding

\[
L_*\propto K^{-1/2}.
\]

In one simple drift picture with dark-generation density \(r_d\), device area \(A\), and carrier speed \(v\),

\[
K\sim \frac{r_dA}{v},
\]

so

\[
L_*\sim \sqrt{\frac{v}{2r_dA}}.
\]

But if a thickness-independent dark mechanism or fixed gate dominates, the leading exponent changes. Real SPAD and photodiode architectures can mix surface dark counts, depletion-region generation, tunneling, afterpulsing, field-dependent collection, fixed electronics windows, and transit-linked timing. The coefficients and even the exponent \(p\) therefore depend on the architecture.

This subproblem reinforces rather than contradicts the main thesis. A geometry threshold can be very real **inside a specified detector model**, while remaining unsuitable as a universal definition of detector matter.

---

## XI. Detection, reset, and Landauer’s principle

Irreversibility and thermodynamics provide another tempting universal boundary. A common shortcut is to assert that each detector click must dissipate at least

\[
k_BT\ln2.
\]

That is too strong.

Landauer’s principle concerns logically irreversible information processing and erasure under stated thermodynamic assumptions [10]. Measurement correlation and erasure are different operations. A detector can export its record into another register and return its local material state to the ready state without locally erasing the information. If side information remains available, reversible uncomputation may also reset a subsystem without applying the usual one-bit erasure argument.

Modern one-shot treatments make the resource accounting more precise: the work cost of a logical process depends on the information discarded conditional on the output, and fluctuating single-shot costs need not be characterized by average Shannon or von Neumann entropy alone [11].

The correct lesson for the present boundary question is limited but firm:

\[
\boxed{
\text{Landauer erasure is not the definition of photodetection, and no fixed per-click heat quantum is universal.}
}
\]

Thermodynamic costs can become unavoidable after the full information-bearing cycle and all retained side information are specified. They are properties of that cycle, not evidence for a microscopic atom-count transition into detector matter.

---

## XII. Relation to established theory and scope of the contribution

The central ingredients used above are established.

A photodetector can be characterized at the measurement level by a POVM, and van Enk has explicitly shown how conventional detector figures of merit can be derived from a POVM and used for platform-independent comparison [1]. Young, Sarovar, and Léonard developed a general quantum framework in which the photon field, absorption, and amplification are treated as one coupled system [2], and analyzed fundamental performance tradeoffs arising from coherence and backaction [3]. Quantum instruments provide the general language for measurement outcomes and post-measurement states [5].

At the decision-theory level, the idea that one statistical experiment can be universally more informative than another through hypothesis-independent post-processing is classical Blackwell theory [12]. Quantum extensions and channel-comparison results are established [13,14], and multi-round memory-assisted transformations are contained in the quantum-comb/network framework [15]. Consequently, this paper does **not** claim a new detector-ordering formalism or a new general theory of quantum measurement.

Likewise, the quantitative examples are intentionally used as illustrations rather than novelty claims. Collective \(\sqrt N\) coupling is standard Tavis-Cummings physics [7]. Impedance-matched single-photon capture and quantum-memory state mapping are established [8]. Noise-weighted optimum filtering and event-energy resolution are established detector theory [9].

The contribution is narrower:

1. to pose the microscopic boundary question explicitly;
2. to eliminate, through a common sequence of counterexamples, the most natural proposed material boundaries;
3. to show how the surviving operational distinction resolves the apparent tension between atomic excitation, semiconductor electron-hole generation, coherent transduction, and ordinary detector readout;
4. to demonstrate with simple calculations why atom number, thickness, \(D^*\), or dissipation can become meaningful thresholds only after the task and compensating resources are constrained.

This makes the paper closer to a foundations-oriented or advanced pedagogical analysis than to a claim of a new universal detector formalism.

---

## XIII. Discussion

The thought experiment changes the original question in a useful way.

The naive hierarchy is

\[
\text{atoms}
\rightarrow
\text{bands}
\rightarrow
\text{electron-hole pairs}
\rightarrow
\text{detector}.
\]

The operational hierarchy is instead

\[
\boxed{
\text{available microscopic interaction}
\rightarrow
\text{transduction}
\rightarrow
\text{accessible output process}
\rightarrow
\text{measurement outcome}
\rightarrow
\text{decision task}.
}
\]

Atom number influences the left side. It determines which microscopic descriptions are useful, how much oscillator strength lies in the optical mode, whether collective coupling occurs, how carriers thermalize, what transport channels exist, and how much dark-active material is present. But none of those changes by itself defines the rightmost transition into a measurement outcome.

This distinction also explains why seemingly incompatible statements about detectors can all be true in their proper domains.

- **Absorption matters:** it can dominate quantum efficiency in a semiconductor.
- **Absorption does not define detection:** nondestructive measurement is possible.
- **Electron-hole generation matters:** it is the key transduction event in many semiconductor devices.
- **Electron-hole generation is not enough:** collection and readout can fail.
- **Persistent memory matters:** it is useful for robust latching and slow readout.
- **Persistent memory is not universally required:** the information can be exported while the material resets.
- **Irreversibility matters:** it can stabilize macroscopic records.
- **Microscopic irreversibility does not define detector matter:** the full dynamics may remain reversible while a declared measurement outcome is produced elsewhere in the chain.
- **\(D^*\) matters:** it is an effective sensitivity metric under its convention.
- **\(D^*\) is not a complete task metric:** transient performance depends on the complete temporal and noise structure.

The outcome is therefore not that conventional detector concepts are wrong. It is that each belongs to a particular layer of the measurement architecture.

### A. What, then, makes a crystal a detector?

A bare crystal does not become a detector merely because it has a direct gap, large absorption coefficient, long carrier lifetime, or favorable mobility. Those properties determine what the crystal can do when embedded in an architecture.

Once contacts, fields, optical coupling, amplification, and readout are specified, objective questions can be asked:

\[
P(y|H_0),\qquad P(y|H_1),
\]

what error is achievable, how fast the decision can be made, how often the system can reset, what dark-event probability is tolerated, and what energy or control resources are consumed.

At that point “detector” is no longer a mysterious material label. It is shorthand for the role that the physical subsystem plays in producing those outcome statistics.

### B. What is the boundary between transducer and detector?

For a fixed model boundary, the distinction is formal. A coherent transducer produces a quantum output channel. A measurement endpoint produces a classical outcome marginal, described by a POVM or instrument. But the **placement** of that boundary inside a composite apparatus is not fixed by an invariant atom count.

This is not merely semantic. Different cuts retain different physical degrees of freedom and therefore support different predictions about coherence, backaction, and accessible information. What is conventional is where the apparatus is partitioned; what is objective is the channel or instrument implemented after the partition is specified.

---

## XIV. Conclusion

The question “At what point does a collection of atoms become a photodetector?” does not have the expected microscopic-threshold answer.

A universal critical atom number fails because a single atom can participate in a detector architecture while a macroscopic absorber can fail to produce a usable record. Band formation is a modeling crossover, not a measurement boundary. Absorption is neither sufficient nor universally necessary. Electron-hole creation is a semiconductor transduction step rather than a completed detection event. Persistent local material memory and microscopic irreversibility can both be bypassed by exporting the information to another output degree of freedom.

The surviving distinction appears only after the measurement architecture is declared. A coherent transducer maps optical information into another quantum system. A detector endpoint supplies a measurement outcome, represented generally by a POVM or quantum instrument. Once that boundary is fixed, detector performance is objective and may be quantified through the complete conditional output statistics. But no universal atom count or condensed-matter phase transition specifies where the boundary must lie.

Quantitative thresholds nevertheless emerge whenever resources are constrained. Finite interaction time produces coupling requirements; collective coupling can turn those into \(N_{\min}\) laws; bandwidth and impedance matching trade against coupling; transient-event detectability depends on the complete noise-weighted waveform rather than a scalar \(D^*\); and semiconductor thickness optima depend on the scaling of useful absorption, transport, dark events, and timing. These are real detector-design boundaries, but they are architecture- and task-specific.

The first-principles answer is therefore:

\[
\boxed{
\text{photodetector-ness is a functional role in a measurement architecture, not a phase of matter.}
}
\]

That conclusion does not replace conventional detector physics. It organizes it: absorption, electron-hole generation, gain, transport, noise, bandwidth, memory, and reset specify **how** a detector realizes a measurement, not **whether matter has crossed an intrinsic detector boundary**.

---

# References

1. S. J. van Enk, “Photodetector figures of merit in terms of POVMs,” *Journal of Physics Communications* **1**, 045001 (2017). doi:10.1088/2399-6528/aa90ce.
2. S. M. Young, M. Sarovar, and F. Léonard, “General modeling framework for quantum photodetectors,” *Physical Review A* **98**, 063835 (2018). doi:10.1103/PhysRevA.98.063835.
3. S. M. Young, M. Sarovar, and F. Léonard, “Fundamental limits to single-photon detection determined by quantum coherence and backaction,” *Physical Review A* **97**, 033836 (2018). doi:10.1103/PhysRevA.97.033836.
4. C. W. Helstrom, *Quantum Detection and Estimation Theory* (Academic Press, New York, 1976).
5. E. B. Davies and J. T. Lewis, “An operational approach to quantum probability,” *Communications in Mathematical Physics* **17**, 239–260 (1970). doi:10.1007/BF01647093.
6. J. Anandan and Y. Aharonov, “Geometry of quantum evolution,” *Physical Review Letters* **65**, 1697–1700 (1990). doi:10.1103/PhysRevLett.65.1697.
7. M. Tavis and F. W. Cummings, “Exact solution for an N-molecule—radiation-field Hamiltonian,” *Physical Review* **170**, 379–384 (1968). doi:10.1103/PhysRev.170.379.
8. J. Dilley, P. Nisbet-Jones, B. W. Shore, and A. Kuhn, “Single-photon absorption in coupled atom-cavity systems,” *Physical Review A* **85**, 023834 (2012). doi:10.1103/PhysRevA.85.023834.
9. S. H. Moseley, J. C. Mather, and D. McCammon, “Thermal detectors as X-ray spectrometers,” *Journal of Applied Physics* **56**, 1257–1262 (1984). doi:10.1063/1.334129.
10. R. Landauer, “Irreversibility and heat generation in the computing process,” *IBM Journal of Research and Development* **5**, 183–191 (1961). doi:10.1147/rd.53.0183.
11. P. Faist, F. Dupuis, J. Oppenheim, and R. Renner, “The minimal work cost of information processing,” *Nature Communications* **6**, 7669 (2015). doi:10.1038/ncomms8669.
12. D. Blackwell, “Equivalent comparisons of experiments,” *Annals of Mathematical Statistics* **24**, 265–272 (1953). doi:10.1214/aoms/1177729032.
13. F. Buscemi, “Comparison of quantum statistical models: equivalent conditions for sufficiency,” *Communications in Mathematical Physics* **310**, 625–647 (2012). doi:10.1007/s00220-012-1421-3.
14. A. Jenčová, “Comparison of quantum channels and statistical experiments,” *IEEE Transactions on Information Theory* **62** (2016), arXiv:1512.07016.
15. G. Chiribella, G. M. D’Ariano, and P. Perinotti, “Theoretical framework for quantum networks,” *Physical Review A* **80**, 022339 (2009). doi:10.1103/PhysRevA.80.022339.

---

## Author note for internal review

This draft deliberately avoids claiming novelty for POVM-based photodetector descriptions, general quantum detector modeling, Blackwell/channel ordering, matched filtering, critical coupling, or quantum instruments. Before any submission, the manuscript should undergo a separate adversarial review focused on: (i) whether the interaction-action benchmark is stated with a sufficiently rigorous norm convention; (ii) whether the semiconductor asymptotic example earns its space or distracts from the conceptual argument; (iii) whether the phrase “detector endpoint” is compatible with the terminology of the target journal; and (iv) whether the manuscript is better positioned as a Perspective, Tutorial, Foundations article, or advanced pedagogical paper rather than as an original-research Article.