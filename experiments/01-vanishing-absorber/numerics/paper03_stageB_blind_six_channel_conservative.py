"""Conservative classification wrapper for the locked Stage-B blind gate.

No forward, fit, threshold, or SNR calculation changes.  This implements the
pre-execution clarification that an uncalibrated deterministic root-law result
cannot substitute for a missing precision-calibrated one-mode early warning.
"""
from __future__ import annotations

import paper03_stageB_blind_six_channel as core


def conservative_classify(comp, blind, roots):
    order_one=comp['max_historical_mimic_fraction']>=core.ORDER_ONE_MIMIC
    early=all(r['early_warning_analytic'] for r in blind['analytic_warning_before_claim'])
    stable=all(r['stable_under_5pct_rule'] for r in roots['per_frequency'])
    if not order_one:
        return 'B2-C: small self-consistent confound; generic blind machinery validated if all numerical gates pass'
    if not early:
        return 'B2-B: hidden-risk Stage-B point under the precision-ordering rule'
    if not stable:
        return 'B2-D: one-mode rejection before false-claim precision; higher-order mechanism unresolved'
    return 'B2-A: order-one self-consistent confound self-announces before false-claim precision'


core.classify=conservative_classify

if __name__=='__main__':
    core.main()
