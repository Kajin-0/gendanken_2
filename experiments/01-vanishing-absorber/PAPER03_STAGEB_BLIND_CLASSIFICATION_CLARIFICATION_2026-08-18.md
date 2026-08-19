# Paper 03 Stage-B blind classification clarification

**Date:** 2026-08-18  
**Status:** **PRE-EXECUTION CONSERVATIVE CLARIFICATION / NON-CLAIM**

This clarification is committed before the Stage-B blind six-channel workflow produces a result.

The B2 gate computes a precision-calibrated analytic one-mode rejection SNR, but it does **not** separately calibrate a measurement-noise SNR threshold for the two-root physical-root-law statistic. Therefore a deterministic fine-grid root-law violation may strengthen or qualify a result **only after** the calibrated one-mode model inadequacy is already detectable below the frozen false-claim SNR.

For an order-one Stage-B finite-minus-planar confound:

```text
if any nonzero-RF calibrated one-mode analytic rejection threshold
is not below its frozen false-transport claim SNR,
classify the point as B2-B for the warning-ordering question,
regardless of a deterministic two-root root-law violation.
```

If all three one-mode analytic early-warning conditions pass:

```text
stable two-root fits -> B2-A;
unstable two-root fits -> B2-D (mechanism unresolved).
```

If the maximum historical finite-minus-planar mimic fraction is below 0.5, retain B2-C.

This clarification does not change any forward model, source kernel, noise convention, SNR threshold, numerical tolerance, root-fit bound, or false-claim comparison coordinate. It only prevents an uncalibrated deterministic root-law diagnostic from substituting for the predeclared precision-ordering test.
