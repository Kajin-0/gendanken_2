# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** exploratory  
**Purpose:** keep known inputs, derivations, conjectures, and invalidated ideas from being conflated.

---

## 1. Active question

Can an ideal photodetector simultaneously approach:

```math
V \to 0,
\qquad
\eta_{\rm abs} \to 1,
\qquad
B \to \infty,
\qquad
\mathrm{intrinsic\ noise} \to 0?
```

The project does not assume that these limits are mutually incompatible. Their compatibility is the object of study.

---

## 2. Known or model-defining ingredients

### K1 — Bulk event-rate scaling

For a uniform volumetric dark-generation rate density `g_d`, defining an active volume `V` gives

```math
\Gamma_d = g_d V.
```

This is a model definition plus extensivity assumption, not a new result.

### K2 — Passive resonant absorption

A one-port lossy resonance can exhibit unity on-resonance absorption at critical coupling when its external leakage rate matches its internal absorptive loss rate.

This is established resonator physics, not a novelty claim. The exact normalization will be rederived in this repository before it is used quantitatively.

### K3 — Optical confinement can separate physical absorber volume from optical collection area

Resonators, antennas, gratings, photon trapping, and related structures can increase interaction with a small absorbing region.

This is established detector/photonic engineering, not a novelty claim.

---

## 3. Derived results

None yet at publication standard.

The next calculation is intended to derive the complete one-port dynamic response from a single amplitude equation and fix all linewidth/lifetime conventions.

---

## 4. Active conjectures

### C1 — Resonant shrinking penalty

For the specified one-port passive resonant model, if active-material participation tends to zero and therefore absorptive decay `gamma_a` tends to zero, maintaining critical coupling forces total optical decay toward zero and increases the optical response time.

**Status:** plausible; derivation pending.

### C2 — General passive absorption-bandwidth bound

A more general passive electromagnetic bound may constrain absorption strength integrated over frequency in terms of material response and absorber amount/volume.

**Status:** plausible from known classes of optical bounds; exact statement not selected and no novelty claim made.

### C3 — Volume elimination

If a valid optical bound links absorption-weighted bandwidth to active absorber volume, and intrinsic dark-event fluctuations scale extensively with that same volume, eliminating `V` may produce a detector-level sensitivity-speed bound that depends on material/statistical parameters rather than device geometry alone.

**Status:** speculative; no formula currently endorsed.

---

## 5. Explicitly unestablished statements

Do not present any of the following as results:

- `eta^2 B <= C V` as a universal law;
- `sqrt(B)/NEP <= constant` as a universal detector bound;
- the claim that passive nanophotonics cannot improve every sensible detector figure of merit simultaneously;
- the claim that optical dwell time always sets detector bandwidth;
- the claim that active volume alone determines dark current or NEP in real detectors;
- any claim of novelty or priority.

---

## 6. Criteria for promoting a conjecture

A conjecture can move to **derived result** only after:

1. its assumptions are explicit;
2. normalization and bandwidth conventions are explicit;
3. units and limiting cases pass;
4. the derivation is internally checked;
5. obvious counterexamples have been tested.

A result can move to **publication claim candidate** only after, additionally:

6. an independent derivation or numerical falsification test where feasible;
7. focused primary-source prior-art comparison;
8. explicit statement of architectures/regimes outside the claim.

---

## 7. Correction history

No substantive correction has yet been recorded.

When a claim fails, preserve it here with the reason it failed rather than deleting it from the research record.
