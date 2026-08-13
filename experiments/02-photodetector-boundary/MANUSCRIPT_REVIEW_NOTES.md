# Experiment 02 Manuscript — First Adversarial Review Notes

**Date:** 2026-08-13  
**Applies to:** `MANUSCRIPT_DRAFT.md`  
**Disposition:** viable as a conceptual/foundations/pedagogical theory manuscript; not viable as a claim of a new general photodetection formalism without a new narrow theorem

## Immediate corrections required

1. Replace philosophically broad wording such as `observer-independent boundary` with the more precise `architecture-independent intrinsic material boundary` or `boundary independent of the declared system partition`.
2. Correct the Jenčová citation. The directly verified 2016 publication is:

   Anna Jenčová, `Comparison of quantum channels and quantum statistical experiments`, 2016 IEEE International Symposium on Information Theory (ISIT), 2249–2253 (2016), DOI `10.1109/ISIT.2016.7541699`; extended treatment: arXiv:1512.07016.

   Do not cite this as an IEEE Transactions on Information Theory article without a separately verified journal source.
3. Explicitly state that the phrase `detector endpoint` means the level of description at which the measurement is declared complete and a classical outcome is exposed. This prevents the text from sounding as though every physical photodetector must contain a unique microscopic classicalization event.
4. The interaction-action benchmark is not central to the manuscript and has the highest avoidable referee risk because its exact norm/interaction-strength convention must be stated carefully. Either move it to an appendix or make the conditional norm convention explicit before submission.
5. Keep the `D*`/response-time counterexample. It is concrete, directly relevant to detector engineering, and its one-sided/two-sided PSD convention has already been audited.
6. Keep the semiconductor scaling only as an illustrative reduced model. Do not imply that `L_* ~ sqrt(v/(2 r_d A))` is a generic SPAD/APD design law. The generalized `eta_s ~ S L^s`, `mu_d ~ K L^p` form is the safer main-text statement.
7. Add the terminology clarification that absorption followed by photon re-emission is fluorescence/spontaneous emission, not the photoelectric effect; semiconductor electron-hole generation is one possible absorption/transduction pathway.

## Positioning

The manuscript should be presented as one of:

- a foundations-oriented conceptual analysis;
- an advanced pedagogical photodetector paper;
- a Perspective/Tutorial-style article if the target venue supports that format.

It should **not** claim:

- a new POVM formalism;
- a new general quantum photodetector theory;
- a new statistical-experiment ordering;
- a new matched-filter sensitivity theorem;
- a universal atom-number, energy, entropy, or thickness bound.

## Strongest paper-level contribution

The strongest defensible contribution is the organized Gedanken chain itself:

```text
candidate intrinsic boundary
-> explicit counterexample
-> why the criterion fails
-> what additional architecture/task/resource specification repairs it
-> final transducer-versus-measurement-endpoint distinction.
```

That chain makes the conceptual boundary between

```text
absorption,
electron-hole generation,
transduction,
record formation,
and completed photodetection
```

unusually explicit while remaining consistent with established measurement theory.

## Recommendation

Revise once for precision and compression, then perform a second adversarial review focused on whether the manuscript is sufficiently useful/novel **as a synthesis** to justify journal publication. Do not try to manufacture novelty by adding more abstract formalism.