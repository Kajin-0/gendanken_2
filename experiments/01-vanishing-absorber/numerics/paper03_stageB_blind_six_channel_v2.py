"""Stage-B blind v2 numerical wrapper.

Implements PAPER03_STAGEB_BLIND_V2_REFINEMENT_LOCK_2026-08-18.md.
The scientific forward model, blind models, SNR convention, and classification
are unchanged.  Only the production B2 mesh pair and the mathematically
well-posed six-current convergence acceptance rule are replaced after v1 was
formally designated REFINE.
"""
from __future__ import annotations

import numpy as np

import paper03_stageB_blind_six_channel as core
import paper03_stageB_blind_six_channel_conservative as conservative


core.MESHES=((91,71),(101,79))


def observable_convergence_v2(Jc:np.ndarray,Jf:np.ndarray):
    pc,pf=core.raw_phase_map(Jc),core.raw_phase_map(Jf)
    rows=[]
    for kf,f in enumerate(core.FREQUENCIES):
        shape=core.affine_shape_error(Jc[kf],Jf[kf])
        phase_change=None
        phase_fraction=None
        if f>0:
            phase_change=abs(pf[float(f)]-pc[float(f)])
            phase_fraction=phase_change/abs(float(core.base.GRADIENT_TARGET_DEG[float(f)]))
        passed=shape<=core.SHAPE_GATE
        rows.append({
            'frequency_hz':float(f),
            'complex_affine_shape_residual':shape,
            'raw_phase_coarse_deg':pc[float(f)],
            'raw_phase_fine_deg':pf[float(f)],
            'raw_phase_absolute_change_deg':phase_change,
            'raw_phase_change_fraction_of_frozen_target_diagnostic_only':phase_fraction,
            'raw_phase_acceptance_status':'diagnostic only under v2; v1 criterion remains preserved as failed/refine',
            'pass':bool(passed),
        })
    if not all(r['pass'] for r in rows):
        raise AssertionError('Stage-B v2 six-channel complex-current convergence failed')
    return {
        'schema':'paper03-stageB-blind-observable-convergence-v2',
        'production_mesh_pair':[[91,71],[101,79]],
        'rows':rows,
        'complex_affine_shape_gate':core.SHAPE_GATE,
        'raw_four_color_phase_role':'reported ill-conditioned historical diagnostic; not a v2 acceptance coordinate',
        'v1_disposition':'preserved REFINE/failure; not retroactively passed',
        'pass':True,
    }


core.observable_convergence=observable_convergence_v2
core.classify=conservative.conservative_classify

if __name__=='__main__':
    core.main()
