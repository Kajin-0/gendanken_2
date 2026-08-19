# Strong-Dark Semiconductor Scaling Prior-Art Audit — Experiment 02

**Date:** 2026-08-12  
**Status:** focused audit; exact asymptotic law retained as conditional synthesis, not a novelty claim  
**Priority:** unproven; low-to-moderate novelty expectation

This file audits the strongest narrow semiconductor result currently produced by Experiment 02:

```math
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{\frac{v}{2e\,r_dA}}
```

for the bulk-dark + transit-gate strong-dark asymptote, together with its general scaling-class form.

---

## 1. Exact result being audited

Under the minimal assumptions

```text
thin Beer-Lambert absorber;
useful signal probability ~ eta_0 alpha L;
bulk dark-event rate ~ r_d A L;
transport-linked observation time ~ L/v;
independent Poisson dark events;
full timestamp/count readout;
```

the mean dark count is

```math
\mu
\sim
\frac{r_dA}{v}L^2.
```

The full time-tagged point-process analysis shows that, at leading order, signal and dark timestamps have the same shape and the statistical problem reduces to

```text
Poisson(mu)
versus
one-extra-event + Poisson(mu).
```

The optimum occurs at

```math
\mu_*=1/2,
```

so

```math
L_*
\sim
\sqrt{\frac{v}{2r_dA}},
```

and

```math
\mathcal D_{\max}
\sim
\eta_0\alpha
\sqrt{\frac{v}{2e\,r_dA}}.
```

The corresponding target-error condition is

```math
\frac{r_dA}{v}
\lesssim
\frac{\eta_0^2\alpha^2}
{2e(1-2\epsilon)^2}.
```

---

## 2. Point-process likelihood is established detection theory

The likelihood-ratio structure for detecting an added event/signal process in Poisson point-process background is established statistical signal-detection theory.

Therefore the Experiment-02 formula

```math
\Lambda(Y)
=1-\eta_s+
\sum_{t_i\in Y}q_L(t_i)/\lambda_0(t_i)
```

must not be claimed as a new point-process detection theorem.

Likewise, retaining event timestamps/counts rather than coarse-graining to a binary click is standard information-preserving detection logic.

### Claim boundary

```text
PRIOR ART / STANDARD:
Poisson point-process likelihood ratios;
matched filtering / weighting by signal-to-background intensity;
count/timestamp data outperforming coarse binary output when the output distributions differ.
```

---

## 3. Semiconductor absorption-versus-collection thickness trade is established

Classical photodiode/solar-cell/radiation-detector models already combine

```text
optical absorption depth
with
carrier diffusion/drift/collection survival.
```

Therefore finite optimum thickness from absorption plus carrier loss is not new physical territory.

The current exponential survival kernel is deliberately simpler than standard drift-diffusion/device models.

---

## 4. SPAD / single-photon detector design already trades efficiency and dark counts

Single-photon avalanche photodiode design literature, including InGaAs/InP device work, explicitly treats tradeoffs among

```text
absorption-region/device structure;
photon-detection efficiency;
active area;
dark-count rate;
timing / avalanche behavior.
```

A representative primary device paper is

```text
S. Pellegrini et al.,
Design and performance of an InGaAs-InP single-photon avalanche diode detector,
IEEE Journal of Quantum Electronics 42 (2006).
```

Before manuscript citation, exact pagination/DOI and the precise design claims should be verified from the primary full text.

### Consequence

The broad statement

> `geometry, transport, area, and dark counts jointly determine single-photon performance`

is direct detector-engineering prior art.

---

## 5. The exact square-root law is a model reduction, not automatically new physics

The scaling

```math
L_*\propto\sqrt{v/(r_dA)}
```

arises because

```text
thin signal ~ L;
bulk dark rate ~ L;
transport gate ~ L;
therefore mean dark count ~ L^2.
```

Optimizing

```math
L e^{-KL^2}
```

is elementary.

Thus even if an identical closed form is absent from the literature search, that absence would **not** by itself justify novelty.

Current interpretation:

```text
useful cross-layer asymptotic reduction
rather than
new fundamental detection law.
```

---

## 6. The scaling-class generalization further weakens any universal-constant claim

`DARK_SCALING_UNIVERSALITY_CLASSES.md` shows that if

```math
\eta_s\sim SL^s,
```

and

```math
\mu\sim KL^p,
```

then, in the first Poisson-mode interval,

```math
L_*
\sim
\left(\frac{s}{pK}\right)^{1/p},
```

```math
\mu_*=s/p,
```

and

```math
\mathcal D_{\max}
\sim
S\left(\frac{s}{epK}\right)^{s/p}.
```

For ordinary thin absorption `s=1`,

```math
\mu_*=1/p.
```

Therefore the earlier `1/2` is only the `p=2` member of a family.

### Consequence

No universal numerical `half-dark-count` detector constant should be claimed.

The physically interesting quantity is the **scaling exponent produced by the dark mechanism and timing architecture**.

---

## 7. Collection-weighting the bulk dark carriers does not kill the p=2 class

`COLLECTION_WEIGHTED_DARK_TRANSPORT.md` replaces raw dark generation

```math
r_dAL
```

with collection-weighted rate

```math
\lambda_d^{\rm col}(L)
=
\frac{r_dA}{\beta}(1-e^{-\beta L}).
```

For thin devices,

```math
\lambda_d^{\rm col}
=r_dAL+O(L^2).
```

With gate `L/v`,

```math
\mu_d^{\rm col}
=\frac{r_dA}{v}L^2+O(L^3).
```

Hence the same `p=2` leading class survives.

This increases physical robustness but does not make the scaling mathematically novel.

---

## 8. Full time-tag readout also does not kill the leading p=2 scaling

`TIMETAGGED_POINT_PROCESS_DECISION.md` shows that full timestamp/count processing generally improves over binary click/no-click.

However, in the strong-dark/thin limit, the optimum is driven into

```math
\mu_*=1/2<1,
```

where the leading signal and dark time shapes are uniform and the binary coarse graining is already sufficient for total-variation discrimination.

Therefore the leading square-root law survives the stronger observer.

This is a meaningful **robustness result inside the model**, but still not evidence of priority.

---

## 9. Current novelty disposition

| Component | Disposition |
|---|---|
| Poisson point-process likelihood | **ESTABLISHED DETECTION THEORY** |
| absorption/collection thickness trade | **CLASSICAL DEVICE PRIOR ART** |
| area/dark-count/PDE tradeoffs in SPAD design | **DIRECT DEVICE PRIOR ART** |
| `L e^{-K L^2}` optimization | **ELEMENTARY** |
| `mu_*=1/2` for bulk+transit model | **MODEL-SPECIFIC DERIVED COROLLARY** |
| general `mu_*=s/p` scaling class | **ELEMENTARY ASYMPTOTIC GENERALIZATION** |
| survival of leading law under full time tags | **USEFUL MODEL ROBUSTNESS RESULT** |
| survival under collection-weighted bulk dark transport | **USEFUL MODEL ROBUSTNESS RESULT** |
| broad novelty claim | **NOT JUSTIFIED** |

---

## 10. Strongest safe scientific statement

> **In a thin, back-collected semiconductor model where useful single-photon probability grows linearly with thickness, the dominant asymptotic decision scaling is controlled by how mean dark exposure grows with thickness. Bulk dark generation combined with a transit-linked observation time gives a `p=2` class with `L_*~sqrt(v/(2r_dA))`; other dark/timing mechanisms produce different exponents. This scaling survives, to leading order, full timestamp/count readout and collection-weighting of the same bulk dark carriers.**

Status:

**DERIVED / CONDITIONAL / ROBUST WITHIN THE STATED ASYMPTOTIC CLASS / PRIORITY UNPROVEN / NO NOVELTY CLAIM.**

---

## 11. What would be required to elevate this branch scientifically

At least one of the following:

```text
1. derive the scaling from a realistic drift-diffusion/depletion model rather than imposed exponential survival;
2. use a real material dark-current mechanism rather than generic Poisson volume generation;
3. show the scaling survives field-dependent collection, timing jitter, and realistic threshold/readout noise;
4. identify an experimentally measurable dimensionless collapse across devices;
5. show that an existing device-design practice misses the decision-feasibility boundary in a consequential way.
```

Without such a step, this branch is best regarded as a rigorous Gedanken-model insight rather than a publishable new law.

---

## 12. Recommended next move

Do **not** keep making the abstract scaling more elaborate.

The best next test is one realistic semiconductor specialization—preferably a material/architecture where Experiment 02 can use physically defensible `alpha`, transport speed/lifetime, dark mechanism, area, and timing.

HgCdTe is a natural candidate given the repository's detector context, but it should only be introduced if the model can be tied to real HgCdTe dark-current/transport physics rather than generic parameters.

If the scaling collapses or becomes ordinary device optimization, the branch should be closed as conceptual synthesis.
