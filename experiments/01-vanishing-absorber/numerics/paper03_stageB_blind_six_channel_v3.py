"""Stage-B blind v3 geometry-aligned production wrapper.

Implements PAPER03_STAGEB_BLIND_V3_ALIGNED_MESH_LOCK_2026-08-18.md.
The finite selected-contact edges at +/-6 um lie exactly on cell faces for both
nx=96 and nx=112.  Scientific forward equations, blind models, statistical
rules, and the v2 direct six-current convergence criterion are unchanged.
"""
from __future__ import annotations

import paper03_stageB_blind_six_channel as core
import paper03_stageB_blind_six_channel_conservative as conservative
import paper03_stageB_blind_six_channel_v2 as v2

core.MESHES=((96,75),(112,87))


def aligned_observable_convergence(Jc,Jf):
    out=v2.observable_convergence_v2(Jc,Jf)
    out['schema']='paper03-stageB-blind-observable-convergence-v3-aligned'
    out['production_mesh_pair']=[[96,75],[112,87]]
    out['geometry_alignment']='finite contact edges x=+/-6 um coincide with lateral cell faces at both nx values'
    out['v2_disposition']='preserved failed numerical confirmation; not retroactively passed'
    return out

core.observable_convergence=aligned_observable_convergence
core.classify=conservative.conservative_classify

if __name__=='__main__':
    core.main()
