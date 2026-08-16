"""Execution adapter for paper02_inference_convergence_gate.py.

The first full CI execution on 2026-08-16 completed all seven numerical
configurations, then failed in the reporting layer because `_metric_value`
matched `D_low` / `w_low` as if they were probe-frequency labels.  No numerical
convergence verdict was produced by that run.

This adapter fixes only that dispatch defect and then executes the unchanged
scientific calculation/gating logic from paper02_inference_convergence_gate.py.
Keeping the repair additive preserves the failed first-run provenance while
avoiding a large in-place rewrite before the corrected result is independently
checked.
"""

from __future__ import annotations

import paper02_inference_convergence_gate as gate


def fixed_metric_value(result, name):
    fk = result["finite_kernel"]
    cp = result["causal_point_controls"]

    table = {
        "D_low": fk["low_band"]["D_eff_m2_per_s"],
        "w_low": fk["low_band"]["w_eff_m_per_s"],
        "law_residual_1ghz": fk["frequency_law"]["relative_residual_1ghz"],
        "max_kernel_fit_1ghz": fk["frequency_law"]["max_kernel_fit_rel_through_1ghz"],
        "D_out": cp["outside_depletion"]["D_eff_m2_per_s"],
        "D_in": cp["inside_depletion"]["D_eff_m2_per_s"],
    }
    if name in table:
        return float(table[name])

    if name in ("D_100", "D_500", "D_1000"):
        f = int(name.split("_")[1]) * 1e6
        return float(fk["probe"][str(int(f))]["D_eff_m2_per_s"])

    if name in ("w_100", "w_500", "w_1000"):
        f = int(name.split("_")[1]) * 1e6
        return float(fk["probe"][str(int(f))]["w_eff_m_per_s"])

    raise KeyError(name)


gate._metric_value = fixed_metric_value


if __name__ == "__main__":
    gate.main()
