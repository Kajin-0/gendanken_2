"""Execution-only shard wrapper for the predeclared Stage-A regime screen.

Calls the exact same point generation, forward solve, reference construction,
and metric_row implementation as paper03_stageA_regime_screen.py.  Sharding
changes wall-clock scheduling only; it does not change the declared 60-point
lattice, numerical level, analytic statistic, or downstream selection rules.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import paper03_stageA_regime_screen as screen
import paper03_stageA_resolvent as resolvent


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--start',type=int,required=True)
    p.add_argument('--stop',type=int,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()

    points=screen.make_points()
    if not (0 <= args.start < args.stop <= len(points)):
        raise ValueError((args.start,args.stop,len(points)))
    subset=points[args.start:args.stop]
    reference_cache={}
    rows=[]
    records=[]
    for global_index, point in enumerate(subset,start=args.start+1):
        print(f'shard point {global_index:02d}/60 {point.block}:{point.point_id}',flush=True)
        J,diag=screen.solve_point(point)
        rk=screen.reference_key(point)
        if rk not in reference_cache:
            reference_cache[rk]=screen.solve_point(screen.reference_point(point))
        Jref,_=reference_cache[rk]
        local=[screen.metric_row(point,J,Jref,diag,kf) for kf in (1,2,3)]
        rows.extend(local)
        records.append({
            'global_index_zero_based':global_index-1,
            'block':point.block,
            'point_id':point.point_id,
            'contact_fraction':point.contact_fraction,
            'depletion_width_um':point.depletion_width_um,
            'space_charge_drop_v':point.space_charge_drop_v,
            'diffusion_m2_s':point.diffusion_m2_s,
            'lifetime_s':'inf' if np.isinf(point.lifetime_s) else point.lifetime_s,
            'beam_sigma_um':point.beam_sigma_um,
            'beam_center_um':point.beam_center_um,
            'solver_diagnostics':diag,
        })
    result={
        'schema':'paper03-stageA-regime-screen-shard-v1',
        'status':'EXECUTION-ONLY SHARD OF PREDECLARED SCREEN / NON-CLAIM',
        'scientific_code_path':'paper03_stageA_regime_screen',
        'predeclaration':'PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md',
        'start_zero_based':args.start,
        'stop_exclusive':args.stop,
        'expected_point_count':args.stop-args.start,
        'numerical':{'grid':[screen.NX,screen.NZ],'lateral_quadrature':screen.NX_SRC},
        'screen_points':records,
        'frequency_rows':rows,
        'science_interpretation_ready':False,
    }
    args.output.write_text(json.dumps(resolvent.json_safe(result),indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(f'wrote {args.output} rows={len(rows)}')

if __name__=='__main__':
    main()
