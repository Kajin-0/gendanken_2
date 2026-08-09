# Research Log — Experiment 01: The Vanishing Absorber

This file is chronological. It records why the research direction changed, not just the final equations.

---

## 2026-08-08 — Experiment opened

### Starting motivation

Use a simple photodetector thought experiment to probe whether familiar engineering tradeoffs hide a more general physical constraint.

The guiding question was chosen because it is easy to state without committing to a particular detector material or architecture:

> Can an ideal photodetector be made arbitrarily small, arbitrarily fast, arbitrarily sensitive, and still absorb essentially every incident photon?

### Initial physical tension

Shrinking the active semiconductor volume appears to help at least two desirable directions in an idealized detector:

- bulk thermally generated event count decreases with active volume for fixed generation-rate density;
- carrier transit distances can decrease.

But ordinary optical absorption also falls as absorbing material is removed.

The thought experiment therefore grants ideal passive optical confinement and asks where any unavoidable cost reappears.

### First candidate mechanism

A one-port critically coupled resonance suggests that weak absorber loss can be compensated by weak external leakage, preserving unity on-resonance absorption while increasing photon dwell time.

This raises the possibility that a thickness/volume penalty can migrate from absorption efficiency into temporal bandwidth.

### Important restraint

No general theorem was accepted from this intuition.

In particular, the provisional relation

```text
eta^2 B <= C V
```

was explicitly demoted from an apparent target formula to an unproved example of what a later bound might resemble.

### Current decision

Do not begin with general electromagnetic bounds or HgCdTe-specific physics.

First derive the complete one-port resonator response from the dynamical equation and determine exactly which bandwidth and lifetime relations are true.

Only then attempt to generalize or find counterexamples.
