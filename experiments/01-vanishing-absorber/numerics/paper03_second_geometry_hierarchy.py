"""Post-numerical model-order/root-law diagnostic for the Paper-03 coplanar family."""
from __future__ import annotations

import argparse, itertools, json
from pathlib import Path
import numpy as np

import paper03_second_geometry_gate as cop
import paper03_stageA_kernel_two_mode as two
import paper03_stageA_resolvent as resolvent
import realistic_geometry_closure_stress as base


def zval(d):
    return complex(float(d["real"]), float(d["imag"]))


def fit_table(J, seed0):
    rows=[]
    for kf in (1,2,3):
        f=float(base.FREQUENCIES[kf])
        fit=two.fit_two_mode(J[kf], seed=seed0+kf)
        rows.append({"frequency_hz":f,"fit":fit})
    return rows


def byf(rows):
    return {float(r["frequency_hz"]):r["fit"] for r in rows}


def main():
    p=argparse.ArgumentParser(); p.add_argument("--output",type=Path,required=True); a=p.parse_args()
    regression=two.validate_exact_two_mode()
    J121,d121,_,_=cop.solve_grid(121,91,17)
    J161,d161,_,_=cop.solve_grid(161,121,17)
    t121=fit_table(J121,4100); t161=fit_table(J161,4200)
    A=byf(t121); B=byf(t161)
    rows=[]
    for f in (1e8,5e8,1e9):
        fa,fb=A[f],B[f]
        stab=two.root_set_distance(fa,fb)
        roots=(zval(fb["r1_per_um"]),zval(fb["r2_per_um"]))
        largest=max(abs(roots[0]),abs(roots[1]),1e-12)
        stable=stab["max_abs_root_change_per_um"] <= max(0.05,0.10*largest)
        compact=(fb["two_mode_contrast_normalized_residual"] <= 0.20*fb["one_mode_contrast_normalized_residual"] and fb["profile_design_condition_number"] <= 1e6 and fb["smaller_over_larger_profiled_mode_amplitude"] >= 1e-3)
        s=roots[0]+roots[1]
        us=float(stab["sum_abs_root_change_per_um"])
        imag_tol=0.005+5.0*us
        rows.append({"frequency_hz":f,"one_mode_rho":fb["one_mode_contrast_normalized_residual"],"two_mode_rho":fb["two_mode_contrast_normalized_residual"],"reduction_factor":fb["residual_reduction_factor_one_over_two"],"profile_condition":fb["profile_design_condition_number"],"modal_amplitude_ratio":fb["smaller_over_larger_profiled_mode_amplitude"],"r1_per_um":fb["r1_per_um"],"r2_per_um":fb["r2_per_um"],"root_sum_per_um":{"real":s.real,"imag":s.imag},"root_stability":stab,"root_stable":bool(stable),"compact_non_negligible":bool(compact),"imaginary_sum_tolerance_per_um":imag_tol,"imaginary_sum_violation":bool(stable and compact and abs(s.imag)>imag_tol)})
    usable=[r for r in rows if r["root_stable"] and r["compact_non_negligible"]]
    pair=[]
    for x,y in itertools.combinations(usable,2):
        sx=zval(x["root_sum_per_um"]); sy=zval(y["root_sum_per_um"])
        ux=x["root_stability"]["sum_abs_root_change_per_um"]; uy=y["root_stability"]["sum_abs_root_change_per_um"]
        tol=0.010+5.0*(ux+uy); delta=abs(sx-sy)
        pair.append({"frequency_pair_hz":[x["frequency_hz"],y["frequency_hz"]],"root_sum_change_per_um":delta,"allowed_numerical_separation_per_um":tol,"rf_independence_violation":bool(delta>tol)})
    law_rejected=any(r["imaginary_sum_violation"] for r in rows) or any(r["rf_independence_violation"] for r in pair)
    if law_rejected:
        classification="stable compact higher-order description; homogeneous scalar root law rejected"
    elif len(usable)<2:
        classification="one mode rejected; higher-order representation not sufficiently identifiable for homogeneous root-law claim"
    else:
        classification="higher-order representation did not reject homogeneous root law under frozen numerical separation criteria"
    out={"schema":"paper03-second-geometry-hierarchy-v1","status":"POST-NUMERICAL MODEL-ORDER/ROOT-LAW DIAGNOSTIC / NON-CLAIM","lock":"PAPER03_SECOND_GEOMETRY_ANALYSIS_LOCK_2026-08-17.md","exact_two_mode_regression":regression,"grid_121":d121,"grid_161":d161,"fits_121":t121,"fits_161":t161,"rows":rows,"root_sum_pair_tests":pair,"homogeneous_scalar_root_law_rejected":bool(law_rejected),"classification":classification,"science_interpretation_ready":False}
    a.output.write_text(json.dumps(resolvent.json_safe(out),indent=2,allow_nan=False)+"\n")
    print(classification)
    for r in rows: print(r["frequency_hz"],r["one_mode_rho"],r["two_mode_rho"],r["root_stable"],r["compact_non_negligible"],r["root_sum_per_um"],r["imaginary_sum_violation"])
    print("homogeneous_scalar_root_law_rejected =",law_rejected)
    print("science_interpretation_ready = false")

if __name__=="__main__": main()
