"""Execution-only shard wrapper for predeclared regime refinement."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import paper03_stageA_regime_refine as refine
import paper03_stageA_resolvent as resolvent

def main():
    p=argparse.ArgumentParser(); p.add_argument('--manifest',type=Path,required=True); p.add_argument('--index',type=int,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    m=json.loads(a.manifest.read_text()); pts=m['selected_unique_points']
    if not (0<=a.index<len(pts)): raise IndexError(a.index)
    point=pts[a.index]
    result={
      'schema':'paper03-stageA-regime-refinement-shard-v1',
      'status':'EXECUTION-ONLY SHARD OF PREDECLARED SELECTED-POINT REFINEMENT / NON-CLAIM',
      'predeclaration':'PAPER03_STAGEA_REGIME_MAP_PREDECLARATION_2026-08-17.md',
      'manifest_id':point['manifest_id'],
      'manifest_index':a.index,
      'result':refine.refine_point(point),
      'science_interpretation_ready':False,
    }
    a.output.write_text(json.dumps(resolvent.json_safe(result),indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result['result'],indent=2)); print('science_interpretation_ready = false')
if __name__=='__main__': main()
