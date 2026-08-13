# When Does Matter Become a Photodetector?
## An Operational Gedanken Analysis from Absorption to Measurement

**Anonymous manuscript — Revision 2 — 2026-08-13**  
**Status:** conceptual/foundations manuscript; no claim of a new general measurement formalism

---

## Abstract

At what point does a collection of atoms become a photodetector? The wording suggests an intrinsic microscopic boundary: perhaps a critical atom number, the emergence of bands, photon absorption, electron-hole generation, irreversibility, or a persistent material record. We test these candidates sequentially with minimal thought experiments. None is a universal boundary. A single atom can be the active microscopic element of a detector architecture; perfect absorption can fail to produce an accessible outcome; nondemolition measurement shows that photon destruction is not universally required; electron-hole generation can be followed by recombination rather than collection; and a light-sensitive material can return to the same local state while an external output degree of freedom retains the information. The surviving distinction is operational. Once an input/output partition is declared, a coherent transducer maps optical information into another physical degree of freedom, whereas a completed measurement exposes an outcome variable described by a POVM or quantum instrument. This is not a claim of a unique microscopic quantum-to-classical transition: the placement of the system cut is part of the measurement model. Two quantitative examples show how real thresholds reappear only after resources and tasks are fixed. In a resonant Tavis-Cummings benchmark, a finite interaction time produces a conditional minimum participating atom number through the collective coupling \(g\sqrt N\). In a one-pole Gaussian readout benchmark with a stated one-sided noise convention, \(d^2=E^2D^{*2}/(A\tau)\), so equal low-frequency \(D^*\) does not imply equal detectability of a short fixed-energy event. A reduced semiconductor example further illustrates how a finite thickness optimum depends on architecture-specific useful-signal and dark-event scalings. The result is not a new formal theory of photodetection. It is a first-principles elimination argument: photodetector status is a functional role within a specified measurement architecture, not an intrinsic phase of matter.

---

## I. Introduction and scope

Photodetectors are usually introduced through mechanisms. A photon is absorbed, a microscopic excitation is produced, the excitation is transported or amplified, and an electrical or optical signal is read out. In a semiconductor, interband absorption and electron-hole creation are natural starting points. In avalanche devices, gain and metastability become important. Superconducting, atomic, and cavity-based detectors use different microscopic degrees of freedom and can separate photon inference from the destructive absorption picture familiar from a photodiode.

This diversity motivates a simple question:

> **At what point does a collection of atoms become a photodetector?**

The question is easy to misstate. Absorption followed by later photon emission is fluorescence or spontaneous emission; in a semiconductor, radiative recombination is one possible later fate of an electron-hole excitation. These processes are not the external photoelectric effect, and electron-hole generation is not the conceptual opposite of re-emission. Rather, they are different branches of light-matter interaction and relaxation.

The wording of the question nevertheless tempts one to search for an intrinsic material threshold: a critical atom number \(N_c\), band formation, the first possibility of electron-hole generation, an irreversibility threshold, or a sufficiently persistent material record. The aim here is to test those candidate boundaries directly instead of assuming one in advance.

The analysis is deliberately operational. For optical hypotheses

\[
H_0:\text{no target optical event},
\qquad
H_1:\text{target optical event},
\]

we ask which physical output is declared accessible and whether its conditional statistics permit the alternatives to be distinguished. This perspective is established in quantum measurement and statistical decision theory. Photodetectors can be represented by POVMs, instruments, or more detailed microscopic input-output models, and platform-independent figures of merit have already been formulated from the POVM of the incoming field [1]. General quantum photodetector models that couple field, absorption, and amplification are also established [2,3].

Accordingly, this paper does **not** propose a new POVM formalism, a new detector-ordering theory, or a new general theory of quantum measurement. Its contribution is narrower: it uses a common Gedanken chain to eliminate the most natural intrinsic-material answers to the boundary question and to show exactly which missing architectural assumptions repair each failed criterion.

The argument is therefore an elimination argument:

\[
\boxed{
\text{candidate intrinsic boundary}
\rightarrow
\text{counterexample}
\rightarrow
\text{missing architecture/task constraint}.
}
\]

---

## II. The operational test: distinguishable accessible outcomes

Let \(S\) denote the optical input and let \(O\) denote the physical output subsystem that the measurement architecture declares accessible before the final decision rule. Under the two hypotheses, suppose the output states are

\[
\rho_O^{(0)},\qquad \rho_O^{(1)}.
\]

If arbitrary measurements on \(O\) are allowed, the trace distance

\[
\mathcal D_O
=\frac12\left\|\rho_O^{(1)}-\rho_O^{(0)}\right\|_1
\]

sets the optimum equal-prior binary discrimination error through the Helstrom relation [4],

\[
P_{e,\min}
=\frac12(1-\mathcal D_O).
\]

Thus \(\mathcal D_O=0\) means that the selected output contains no usable information for this binary task, while \(\mathcal D_O=1\) permits perfect discrimination in the unrestricted setting.

This separates **physical interaction** from **usable detection information**. A system can interact strongly with a photon while leaving the declared output identical under the two hypotheses. Conversely, a small but nonzero output distinction can in principle be exploited by a suitable measurement.

A crucial qualification is the data-processing principle: downstream amplification or signal processing cannot create hypothesis information that is absent from the physical output. A hypothesis-independent physical channel applied after \(O\) cannot increase trace distance. Additional interaction time, repeated probing, collective coupling, a reference field, or another physical resource can increase distinguishability before the final output is fixed, but readout processing cannot manufacture it afterward.

For an actual detector endpoint, the output is usually represented by an outcome variable \(y\) with conditional probabilities

\[
p(y|H_0),\qquad p(y|H_1).
\]

The point of the Gedanken experiment is not to insist that every internal detector degree of freedom itself hold a record. It is to identify which proposed *intrinsic material property* can guarantee that some declared output contains discriminating information. The following sections show that none of the obvious candidates does so universally.

---

## III. Candidate intrinsic boundaries and why they fail

### A. Atom count and band formation

A universal atom-count criterion fails immediately once the architecture is specified carefully.

Consider one atom as the active light-sensitive element. If it is excited and later returns to its ground state while the emitted field is ignored,

\[
|g\rangle|1_\gamma\rangle
\rightarrow
|e\rangle|0_\gamma\rangle
\rightarrow
|g\rangle|1_{\gamma'}\rangle,
\]

then the atom itself need not retain a useful late-time record. But one atom can nevertheless be the active microscopic element of a detector architecture. Ionization followed by collection of the emitted electron is the simplest limiting example,

\[
A+h\nu\rightarrow A^++e^-.
\]

Fluorescence can likewise participate in detection if the emitted field is subsequently measured.

The correct conclusion is not that an isolated atom is intrinsically a complete photodetector. It is that **no positive universal atom number can be necessary for participation in a detector architecture**.

Increasing \(N\) certainly changes the available physics. Atomic levels hybridize; extended materials support band descriptions; oscillator strength, transport pathways, thermalization, and collective coupling can change. But band formation is a microscopic modeling crossover, not a measurement criterion. A macroscopic absorber can return no useful declared output, while a few-level system can participate in a high-fidelity measurement chain.

Therefore

\[
\boxed{
\text{atom count and band formation are not universal detector boundaries.}
}
\]

### B. Absorption

Absorption is the next natural candidate because many practical photodetectors begin with

\[
\text{photon absorption}
\rightarrow
\text{material excitation}.
\]

It fails in both logical directions.

First, perfect absorptance is not sufficient. Imagine a system that absorbs the photon with unit probability but later leaves the declared accessible output in the same state under \(H_0\) and \(H_1\). Whatever happened microscopically, the selected output has

\[
\mathcal D_O=0,
\]

and the event cannot be inferred from that output.

Second, photon destruction is not universally necessary. Quantum-nondemolition measurement is specifically designed to extract information about an observable while preserving that observable under repeated measurement [5]. An idealized photon-number measurement can correlate a pointer with the number state without requiring the measured photon to be absorbed:

\[
|0\rangle|D_0\rangle\rightarrow |0\rangle|D_0'\rangle,
\]

\[
|1\rangle|D_0\rangle\rightarrow |1\rangle|D_1'\rangle.
\]

If the pointer alternatives are distinguishable, photon number has been measured even though the photon survives in the idealized model.

Hence

\[
\boxed{
\text{absorption is neither universally sufficient nor universally necessary for photodetection.}
}
\]

This does not make absorptance unimportant. In a semiconductor detector it can dominate quantum efficiency. The claim is only that absorptance is an implementation coordinate rather than a universal definition.

### C. Electron-hole generation

The original motivation for the thought experiment included a contrast between atomic excitation/re-emission and semiconductor electron-hole generation. The comparison becomes clearer once the sequence is written correctly.

Interband absorption may produce

\[
h\nu + e^-_{\rm VB}
\rightarrow
 e^-_{\rm CB}+h^+,
\]

while radiative recombination can later give

\[
e^-+h^+\rightarrow h\nu'.
\]

Nonradiative recombination, trapping, diffusion away from the collecting region, or other relaxation can instead remove the excitation before readout.

A minimal semiconductor chain is therefore

\[
\boxed{
\text{optical access}
\rightarrow
\text{absorption}
\rightarrow
 e^-h^+\text{ excitation}
\rightarrow
\text{survival/collection}
\rightarrow
\text{readout}.
}
\]

A schematic useful-event probability is

\[
\eta_s
=\eta_{\rm mode}
(1-e^{-\alpha L})
\eta_{eh}
P_{\rm col}
P_{\rm read},
\]

where \(\alpha\) and \(L\) are an absorption coefficient and absorber thickness. A minimal competing-rate illustration gives

\[
P_{\rm col}
=\frac{\Gamma_{\rm ext}}
{\Gamma_{\rm ext}+\Gamma_{\rm rec}}.
\]

Electron-hole creation can therefore be an essential microscopic transduction step while remaining insufficient for a readable event.

### D. Persistent local memory and microscopic irreversibility

A stronger candidate is that detector matter must retain a persistent state change. This also fails.

Let \(D\) denote the material element and \(R\) an external output register. Consider a physically allowed mapping

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

The material element finishes in the same local state,

\[
\boxed{
\rho_D^{(0)}=\rho_D^{(1)}=|D_0\rangle\langle D_0|,
}
\]

while the external output satisfies

\[
\rho_R^{(0)}\neq\rho_R^{(1)}.
\]

The material can therefore act as a transient mediator, export the information, and locally return to its ready state. Persistent **local** material memory is not necessary. What is required is only that the declared measurement architecture retain enough accessible correlation for the allowed readout to use.

The same observation blocks microscopic irreversibility as a universal boundary. The larger source-device-environment dynamics can be modeled unitarily even when a robust effective record is produced in a restricted description. Irreversibility is important for many practical detectors because it stabilizes macroscopic records, but it is not an intrinsic phase transition into `detector matter`.

---

## IV. Transducer versus declared measurement endpoint

The previous section appears to create a paradox. A mirror transforms an incident optical mode into a reflected mode,

\[
|1\rangle_{\rm in}
\rightarrow
|1\rangle_{\rm refl},
\]

and the reflected field contains information about the incident field. If `information is present somewhere downstream` were the definition, a mirror would become a photodetector whenever somebody later measures the reflected beam.

The required distinction is operational.

### A. Coherent transducer

A coherent transducer can be represented schematically as a quantum channel

\[
\Phi:\rho_{\rm opt}\mapsto\rho_Q,
\]

where \(Q\) is another physical degree of freedom. The output can retain coherence and can itself require a later measurement. A mirror, coherent frequency converter, reversible optical-microwave interface, or matter-light state transfer can occupy this role.

### B. Measurement endpoint

A measurement with outcomes \(y\) is described by POVM elements \(E_y\),

\[
p(y|\rho)=\operatorname{Tr}(E_y\rho),
\qquad
\sum_y E_y=I.
\]

If one writes an explicit outcome register, the corresponding quantum-to-classical representation is

\[
\mathcal M(\rho)
=
\sum_y
\operatorname{Tr}(E_y\rho)
|y\rangle\langle y|.
\]

More generally, a quantum instrument \(\{\mathcal I_y\}\) supplies both an outcome and a conditional post-measurement state [6]:

\[
p(y|\rho)=\operatorname{Tr}[\mathcal I_y(\rho)],
\]

\[
\rho_y
=\frac{\mathcal I_y(\rho)}{p(y|\rho)}.
\]

Here `measurement endpoint` means **the level of description at which the measurement is declared complete and an outcome variable is exposed to the user or subsequent decision rule**. It is not a claim that every physical photodetector contains a unique fundamental instant at which quantum mechanics becomes classical. The outcome can be encoded in physical degrees of freedom that are themselves treated quantum mechanically in a larger description.

This qualification is essential because the system cut is movable. A photodiode alone can be modeled as a transducer feeding an amplifier; the photodiode plus front end can be modeled as an analog measurement device; the full receiver plus discriminator and digitizer can be treated as one instrument with a discrete outcome. Different partitions retain different degrees of freedom and therefore support different predictions about coherence, backaction, and accessible information.

The surviving conclusion is therefore

\[
\boxed{
\text{photodetector status is a functional role in a specified measurement architecture, not an intrinsic material phase.}
}
\]

Once the architecture and output are declared, detector performance is objective. What is not fixed by atom count is the placement of the word `detector` inside an arbitrarily decomposed measurement chain.

---

## V. Why conditional thresholds still arise

Rejecting an intrinsic material boundary does not imply that detector design has no sharp thresholds. It implies that those thresholds are conditional on a task and resource model.

### A. Finite-time atom-number threshold in a collective-coupling model

Take \(N\) identical resonant two-level dipoles coupled with equal single-particle strength \(g\) to one optical mode. In the single-excitation symmetric subspace, the Tavis-Cummings interaction [7] couples

\[
|1_\gamma,G\rangle
\leftrightarrow
|0_\gamma,W_N\rangle
\]

with collective rate

\[
\boxed{G=g\sqrt N.}
\]

Starting with one photon and all dipoles in the ground state, the ideal resonant evolution is

\[
|\Psi(t)\rangle
=
\cos(g\sqrt N\,t)|1_\gamma,G\rangle
-i\sin(g\sqrt N\,t)|0_\gamma,W_N\rangle.
\]

The matter-excitation probability is therefore

\[
P_M(t)=\sin^2(g\sqrt N\,t).
\]

If the task requires, on the first transfer lobe, a matter-transfer probability of at least \(P_{\rm req}\) by time \(\tau\), then

\[
\boxed{
N
\ge
\left[
\frac{\arcsin\sqrt{P_{\rm req}}}{g\tau}
\right]^2,
}
\]

with the integer ceiling understood. Perfect transient transfer gives

\[
\boxed{
N
\ge
\left(\frac{\pi}{2g\tau}\right)^2.
}
\]

This is a real atom-number threshold, but it exists only because the microscopic coupling and allowed interaction time have been specified. It is not a transition at which matter acquires an intrinsic detector property. The coherent transfer is also reversible; additional physics is required if the architecture demands a long-lived record.

The complementary lesson is familiar from impedance-matched cavity capture and quantum memory: suitable control and sufficiently long/narrowband interaction can trade time and bandwidth against instantaneous coupling [8]. Thus a threshold that appears under a fixed time budget need not survive when that budget is relaxed.

### B. Equal low-frequency \(D^*\) does not imply equal short-event performance

At the electrical-output level, consider

\[
H_0:y(t)=n(t),
\qquad
H_1:y(t)=s(t)+n(t),
\]

with zero-mean Gaussian noise having the same covariance under both hypotheses. The optimum noise-weighted waveform distance is

\[
\boxed{
d^2=\langle s,C^{-1}s\rangle.
}
\]

For stationary noise with a two-sided PSD,

\[
d^2
=
\int_{-\infty}^{\infty}
\frac{|\tilde s(f)|^2}{S_n^{(2)}(f)}\,df,
\]

and the equal-prior optimum error is

\[
P_e=Q(d/2).
\]

This is standard matched-filter detection theory. Its value here is to expose what a scalar detector figure of merit omits.

Take a normalized one-pole signal response

\[
h(t)=\frac{1}{\tau}e^{-t/\tau}u(t).
\]

A short optical event of energy \(E\) and DC responsivity \(R_0\) produces

\[
s(t)=\frac{R_0E}{\tau}e^{-t/\tau}u(t),
\]

so

\[
\int_0^\infty s^2(t)dt
=\frac{(R_0E)^2}{2\tau}.
\]

Let \(S_n^{(1)}\) be a flat **one-sided output-noise PSD**. Define the one-sided input-referred **power-noise amplitude spectral density**

\[
\mathrm{NEP}_{\rm ASD}
=\frac{\sqrt{S_n^{(1)}}}{R_0},
\]

with units of \(\mathrm{W}/\sqrt{\mathrm{Hz}}\). Under this convention,

\[
\boxed{
d^2
=\frac{E^2}{\tau\,\mathrm{NEP}_{\rm ASD}^2}.
}
\]

If specific detectivity is quoted with the same one-sided 1-Hz normalization,

\[
D^*=rac{\sqrt A}{\mathrm{NEP}_{\rm ASD}},
\]

then

\[
\boxed{
d^2
=\frac{E^2D^{*2}}{A\tau}.
}
\]

Thus two equal-area detectors with the same low-frequency \(D^*\) but different \(\tau\) need not have the same ability to detect a short fixed-energy event in this model:

\[
d\propto\tau^{-1/2}.
\]

The assumptions are part of the result: a short event, one-pole signal response, flat one-sided output-noise PSD, common Gaussian covariance, matched-filter readout, and consistent \(D^*\)/NEP convention. If the noise is colored, signal dependent, or filtered differently, the full spectrum must be used. Frequency-integrated NEP and optimum filtering are established detector concepts, including in calorimetric event-energy detection [9]. The point is not a new matched-filter theorem; it is a concrete counterexample to interpreting one quoted low-frequency \(D^*\) as a complete arbitrary-event metric.

### C. Brief semiconductor geometry illustration

A reduced semiconductor model provides one more illustration of conditionality without pretending to be a device design law.

Suppose that over a thin-device regime the useful-event probability scales as

\[
\eta_s(L)\sim S L^s,
\]

while mean dark-event exposure in the relevant decision interval scales as

\[
\mu_d(L)\sim K L^p,
\]

with positive \(S,K,s,p\). In the simplest leading benchmark where useful distinguishability is proportional to useful-event probability times the probability of avoiding a dark event,

\[
\mathcal D(L)
\sim
S L^s e^{-K L^p}.
\]

Then

\[
\frac{d}{dL}\ln\mathcal D
=\frac{s}{L}-pK L^{p-1}=0
\]

gives

\[
\boxed{
L_*
\sim
\left(\frac{s}{pK}\right)^{1/p},
\qquad
\mu_d(L_*)=\frac{s}{p}.
}
\]

The exponent \(p\) is not universal. Bulk dark generation with a transit-linked decision time can produce a different scaling class from surface dark counts, tunneling, a fixed electronic gate, or a separated absorption/multiplication architecture. The example therefore does exactly what is needed here: it shows how a real finite geometry optimum can emerge inside a declared model without becoming an intrinsic boundary of detector matter.

---

## VI. Detection, reset, and Landauer's principle

Thermodynamics supplies another tempting universal criterion: the claim that every detector click must dissipate at least

\[
k_BT\ln2.
\]

That statement is too strong.

Landauer's principle concerns logically irreversible information processing and erasure under specified thermodynamic assumptions [10]. Creating a measurement correlation is not identical to erasing a memory. A detector can also export a record into another subsystem while its local light-sensitive element returns to a ready state.

More general finite-process treatments make the dependence on the logical map and discarded information explicit; Faist *et al.* relate the work requirement to information discarded conditional on the output and treat fluctuating one-shot work requirements [11].

For the present argument, no stronger thermodynamic claim is required. The conclusion is simply

\[
\boxed{
\text{Landauer erasure is not the definition of photodetection, and }k_BT\ln2\text{ is not a universal heat cost per detected photon.}
}
\]

A thermodynamic lower bound can be meaningful only after the complete reset protocol, reservoirs, retained side information, work-storage systems, and accuracy requirements have been specified.

---

## VII. Relation to established theory and contribution boundary

The formal ingredients of this paper are established.

Van Enk explicitly formulated photodetector figures of merit from the POVM of the incoming optical field and emphasized the POVM as a platform-independent detector description [1]. Young, Sarovar, and Léonard developed a general microscopic quantum framework coupling the photon field, absorption, and amplification [2], and separately analyzed limits associated with quantum coherence and backaction [3]. Quantum instruments provide the standard language for outcomes together with conditional post-measurement states [6].

At the decision-theory level, Blackwell's comparison of statistical experiments formalizes all-decision-problem informativeness through stochastic post-processing [12]. Quantum extensions of statistical-model comparison are established [13], as are comparison/deficiency results for quantum channels [14] and multi-round memory-assisted quantum networks [15].

The quantitative examples are likewise not presented as foundational novelty. Collective \(\sqrt N\) coupling is Tavis-Cummings physics [7]. Controlled impedance matching for complete photon-to-matter state mapping is established in cavity-memory models [8]. Optimum filtering and frequency-dependent NEP are standard event-detection tools [9].

The contribution is therefore specifically the **photodetector boundary argument**:

1. pose the microscopic boundary question explicitly;
2. test the most natural intrinsic-material answers within one common operational criterion;
3. exhibit simple counterexamples showing why atom count, band formation, absorption, electron-hole generation, persistent local memory, and microscopic irreversibility each fail as universal definitions;
4. distinguish coherent transduction from the level at which a measurement outcome is declared;
5. show with compact detector examples why sharp thresholds reappear once coupling, time, noise, geometry, and decision requirements are fixed.

This positioning is closer to a foundations-oriented conceptual analysis or advanced pedagogical article than to a new general detector formalism.

---

## VIII. Discussion

The original intuition can be summarized as

\[
\text{atoms}
\rightarrow
\text{bands}
\rightarrow
 e^-h^+\text{ pairs}
\rightarrow
\text{detector}.
\]

The Gedanken analysis replaces it with

\[
\boxed{
\text{microscopic interaction}
\rightarrow
\text{transduction}
\rightarrow
\text{accessible output}
\rightarrow
\text{measurement outcome}
\rightarrow
\text{decision task}.
}
\]

The left side is material physics. Atom number changes the available spectrum, oscillator strength, collective coupling, transport, thermalization, dark-active volume, and geometry. Those changes determine which detector architectures are feasible and how well they perform. But they do not by themselves specify the operational completion of a measurement.

This resolves several statements that can otherwise appear contradictory.

Absorption can dominate semiconductor quantum efficiency, yet absorption is not the universal definition because nondestructive measurement exists. Electron-hole generation is central to many semiconductor detectors, yet it is not the completed event because collection and readout can fail. Persistent memory is valuable for latching and slow readout, yet it is not universally necessary because the record can be exported. Irreversibility can stabilize a macroscopic record, yet microscopic reversibility of a larger description does not prevent a declared measurement outcome. \(D^*\) is useful under its convention, yet a single low-frequency value does not determine arbitrary transient-event performance.

### A. What makes a crystal a detector?

A bare crystal does not acquire detector status merely from a direct gap, high absorption coefficient, long lifetime, or high mobility. Those properties determine the transduction channels available when the crystal is embedded in an architecture.

Once optical coupling, contacts or other output ports, fields, amplification, timing, and readout are specified, objective questions can be asked:

\[
P(y|H_0),\qquad P(y|H_1),
\]

what decision error is achievable, how long the decision takes, what false-event rate is tolerated, what reset behavior is required, and what physical resources are consumed.

At that point `detector` is a functional description of how the subsystem participates in producing those outcome statistics.

### B. What is the boundary between a transducer and a detector?

For a fixed model partition, the distinction is operationally sharp: a coherent transducer supplies another physical state that still requires measurement, while the declared measurement endpoint exposes an outcome variable used by a decision rule. The placement of that partition within a composite receiver is conventional, but the channel, instrument, and outcome statistics after the partition is chosen are not.

Thus the paper does not argue that detector terminology is arbitrary. It argues that the terminology is **relational to a declared measurement architecture rather than intrinsic to a collection of atoms**.

---

## IX. Conclusion

The question `At what point does a collection of atoms become a photodetector?` does not have an architecture-independent microscopic-threshold answer.

A universal critical atom number fails because one atom can serve as the active microscopic element of a detector architecture, while a macroscopic absorber can fail to produce a useful declared output. Band formation changes the material description but does not complete a measurement. Absorption is neither sufficient nor universally necessary. Electron-hole creation is a semiconductor transduction step, not a guarantee of collection or readout. Persistent local material memory and microscopic irreversibility are likewise not required if information is exported to another accessible output.

Once the measurement architecture is declared, the problem becomes precise. The light-sensitive subsystem participates in an input-output process; a coherent transducer may map the optical information into another degree of freedom; and the measurement is declared complete at the level where an outcome variable is exposed and used for inference. POVMs and quantum instruments provide the standard formal language for that endpoint.

Quantitative thresholds then emerge naturally when resources are fixed. Finite interaction time produces a conditional \(N_{\min}\) in a collective-coupling model. Equal low-frequency \(D^*\) does not imply equal detectability of a short event when temporal responses differ. Finite absorber-thickness optima can arise from architecture-specific useful-signal and dark-event scalings. These are genuine engineering boundaries, but they are task and architecture dependent.

The first-principles resolution is therefore

\[
\boxed{
\text{photodetector status is a functional role in a specified measurement architecture, not an intrinsic phase of matter.}
}
\]

What has **not** been established is equally important. This work does not introduce a new POVM or instrument formalism, a universal detector ordering, a universal atom-number bound, a universal thermodynamic cost per click, or a replacement scalar for conventional detector figures of merit. Its value is the elimination chain itself: it separates absorption, excitation, transduction, record formation, and completed measurement without conflating any one implementation stage with the universal definition of photodetection.

---

# References

1. S. J. van Enk, “Photodetector figures of merit in terms of POVMs,” *Journal of Physics Communications* **1**, 045001 (2017). doi:10.1088/2399-6528/aa90ce.
2. S. M. Young, M. Sarovar, and F. Léonard, “General modeling framework for quantum photodetectors,” *Physical Review A* **98**, 063835 (2018). doi:10.1103/PhysRevA.98.063835.
3. S. M. Young, M. Sarovar, and F. Léonard, “Fundamental limits to single-photon detection determined by quantum coherence and backaction,” *Physical Review A* **97**, 033836 (2018). doi:10.1103/PhysRevA.97.033836.
4. C. W. Helstrom, *Quantum Detection and Estimation Theory* (Academic Press, New York, 1976).
5. V. B. Braginsky, Y. I. Vorontsov, and K. S. Thorne, “Quantum nondemolition measurements,” *Science* **209**, 547–557 (1980). doi:10.1126/science.209.4456.547.
6. E. B. Davies and J. T. Lewis, “An operational approach to quantum probability,” *Communications in Mathematical Physics* **17**, 239–260 (1970). doi:10.1007/BF01647093.
7. M. Tavis and F. W. Cummings, “Exact solution for an N-molecule—radiation-field Hamiltonian,” *Physical Review* **170**, 379–384 (1968). doi:10.1103/PhysRev.170.379.
8. J. Dilley, P. Nisbet-Jones, B. W. Shore, and A. Kuhn, “Single-photon absorption in coupled atom-cavity systems,” *Physical Review A* **85**, 023834 (2012). doi:10.1103/PhysRevA.85.023834.
9. S. H. Moseley, J. C. Mather, and D. McCammon, “Thermal detectors as X-ray spectrometers,” *Journal of Applied Physics* **56**, 1257–1262 (1984). doi:10.1063/1.334129.
10. R. Landauer, “Irreversibility and heat generation in the computing process,” *IBM Journal of Research and Development* **5**, 183–191 (1961). doi:10.1147/rd.53.0183.
11. P. Faist, F. Dupuis, J. Oppenheim, and R. Renner, “The minimal work cost of information processing,” *Nature Communications* **6**, 7669 (2015). doi:10.1038/ncomms8669.
12. D. Blackwell, “Equivalent comparisons of experiments,” *Annals of Mathematical Statistics* **24**, 265–272 (1953). doi:10.1214/aoms/1177729032.
13. F. Buscemi, “Comparison of quantum statistical models: equivalent conditions for sufficiency,” *Communications in Mathematical Physics* **310**, 625–647 (2012). doi:10.1007/s00220-012-1421-3.
14. A. Jenčová, “Comparison of quantum channels and statistical experiments,” in *2016 IEEE International Symposium on Information Theory (ISIT)*, pp. 2249–2253 (2016). doi:10.1109/ISIT.2016.7541699. Extended version: arXiv:1512.07016.
15. G. Chiribella, G. M. D’Ariano, and P. Perinotti, “Theoretical framework for quantum networks,” *Physical Review A* **80**, 022339 (2009). doi:10.1103/PhysRevA.80.022339.

---

## Internal status note

Revision 2 implements the major scientific changes from `MANUSCRIPT_REVIEW_ROUND2.md`:

- contribution reframed as an elimination/synthesis argument;
- no fundamental microscopic `classicalization` claim;
- explicit data-processing correction;
- one-atom claim narrowed to active microscopic element of an architecture;
- interaction-action bound removed from the main manuscript;
- exact Experiment-02 constant-rate impedance-matching formula removed from the main manuscript;
- Tavis-Cummings finite-time threshold made the clean conditional-`N` example;
- `D*`/NEP convention tightened to an explicit one-sided power-noise ASD;
- semiconductor model compressed and generalized;
- Landauer discussion compressed;
- fluorescence/photoelectric terminology corrected;
- Jenčová citation corrected;
- QND reference added.

The next required step is a third adversarial review of **Revision 2 itself**, focused on whether the manuscript has enough standalone scientific value as a conceptual synthesis to justify journal submission and whether any remaining statement can be attacked as circular, tautological, or already obvious from standard measurement theory.
