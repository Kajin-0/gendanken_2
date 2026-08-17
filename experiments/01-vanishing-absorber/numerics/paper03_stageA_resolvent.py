"""Deterministic backward-resolvent solver for Paper 03 Stage A.

This is an independent numerical formulation of the same fixed-field
single-carrier diffusion/recombination problem sampled by
``paper03_combined_physics_challenge.py``.  It is NOT the Stage-B
self-consistent semiconductor Poisson/drift-diffusion model.

For the stopped diffusion

    dX = v(X) dt + sqrt(2D) dW,

with independent bulk killing rate kappa=1/tau, define the selected-electrode
Shockley--Ramo response

    H(x; omega) = E_x[ integral exp(-i omega t) d phi_w(X_t) ].

The backward generator L gives the resolvent problem

    (kappa + i omega - L) H = L phi_w,

with H=0 on absorbing electrical contacts and reflecting conditions on the
sidewalls / uncontacted top surface.  A positive nearest-neighbour,
Scharfetter--Gummel-like Markov generator discretizes L.  The discrete source
is defined as L_h phi_w itself, rather than a separately differentiated field,
so the dc Ramo/committor identity

    H(0) = p_selected - phi_w

is an exact algebraic invariant of the discrete model up to the sparse-solver
residual.  This is a strong implementation check and avoids Monte-Carlo noise
in small closure observables.

The existing stochastic calculation remains valuable as an independent
cross-formulation validation.  No output from this script is a physics claim
until grid convergence, Monte-Carlo cross-check, and the kernel-aware blind
inverse gates are passed.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.linalg import spsolve

import paper03_combined_physics_challenge as stage
import realistic_geometry_closure_stress as base


@dataclass(frozen=True)
class ResolventConfig:
    diffusion_m2_s: float
    lifetime_s: float
    nx: int
    nz: int
    nx_src: int = 11


@dataclass
class DiscreteGenerator:
    Q: csr_matrix
    q_ramo: np.ndarray
    b_selected: np.ndarray
    phi: np.ndarray
    transient_flat: np.ndarray
    flat_to_transient: np.ndarray
    selected_mask: np.ndarray
    bottom_mask: np.ndarray
    max_cell_peclet: float
    xs: np.ndarray
    zs: np.ndarray
    geometry: dict[str, Any]


def bernoulli(x: float) -> float:
    """Stable B(x)=x/(exp(x)-1), positive for real x."""
    ax = abs(x)
    if ax < 1e-6:
        # 1 - x/2 + x^2/12 - x^4/720
        x2 = x * x
        return 1.0 - 0.5 * x + x2 / 12.0 - x2 * x2 / 720.0
    if x > 50.0:
        return x * np.exp(-x)
    if x < -50.0:
        return -x
    return x / np.expm1(x)


def directional_rates(v: float, h: float, D: float) -> tuple[float, float, float]:
    """Return positive (+,-) jump rates and |cell Peclet|.

    For D>0 the exponentially fitted rates satisfy

        (r_plus-r_minus) h -> v

    and recover centered diffusion as Pe->0.  For D=0 the Markov upwind limit
    is returned, although scientific D=0 recovery is delegated to the checked
    deterministic trajectory solver elsewhere.
    """
    if h <= 0:
        raise ValueError("grid spacing must be positive")
    if D < 0:
        raise ValueError("diffusion coefficient must be nonnegative")
    if D == 0.0:
        return max(v, 0.0) / h, max(-v, 0.0) / h, float("inf") if v else 0.0
    pe = v * h / D
    rp = D / h**2 * bernoulli(-pe)
    rm = D / h**2 * bernoulli(pe)
    if rp < 0.0 or rm < 0.0:
        raise AssertionError("negative jump rate")
    return float(rp), float(rm), float(abs(pe))


def build_generator(scenario: base.Scenario, cfg: ResolventConfig) -> DiscreteGenerator:
    """Build the transient-state backward Markov generator."""
    g = base.geometry(scenario, cfg.nx, cfg.nz)
    xs = np.asarray(g["xs"], float)
    zs = np.asarray(g["zs"], float)
    nx, nz = len(xs), len(zs)
    dx, dz = float(xs[1] - xs[0]), float(zs[1] - zs[0])
    D = float(cfg.diffusion_m2_s)

    W = float(xs[-1] - xs[0])
    half = scenario.contact_fraction * W / 2.0
    selected = np.zeros((nz, nx), dtype=bool)
    bottom = np.zeros((nz, nx), dtype=bool)
    bottom[0, :] = True
    selected[-1, np.abs(xs) <= half + 1e-15] = True
    absorbing = selected | bottom

    transient_flat = np.flatnonzero(~absorbing.ravel())
    flat_to_transient = np.full(nx * nz, -1, dtype=int)
    flat_to_transient[transient_flat] = np.arange(len(transient_flat))

    Q = lil_matrix((len(transient_flat), len(transient_flat)), dtype=float)
    q = np.zeros(len(transient_flat), dtype=float)
    b_selected = np.zeros(len(transient_flat), dtype=float)
    phi_grid = np.asarray(g["pw"], float)
    phi = phi_grid.ravel()[transient_flat]
    max_pe = 0.0

    def add_jump(row: int, j: int, i: int, jn: int, inn: int, rate: float) -> None:
        if rate <= 0.0:
            return
        flat_n = jn * nx + inn
        phi_i = phi_grid[j, i]
        phi_n = phi_grid[jn, inn]
        Q[row, row] -= rate
        q[row] += rate * (phi_n - phi_i)
        if selected[jn, inn]:
            b_selected[row] += rate
        elif bottom[jn, inn]:
            pass
        else:
            col = flat_to_transient[flat_n]
            if col < 0:
                raise AssertionError("transient-neighbour map failure")
            Q[row, col] += rate

    for flat in transient_flat:
        j, i = divmod(int(flat), nx)
        row = int(flat_to_transient[flat])
        vx, vz, _ = base.velocity(float(g["dVdx"][j, i]), float(g["dVdz"][j, i]))
        rxp, rxm, pex = directional_rates(vx, dx, D)
        rzp, rzm, pez = directional_rates(vz, dz, D)
        max_pe = max(max_pe, pex, pez)

        # Missing neighbours are reflecting boundaries: no jump crosses them.
        if i + 1 < nx:
            add_jump(row, j, i, j, i + 1, rxp)
        if i - 1 >= 0:
            add_jump(row, j, i, j, i - 1, rxm)
        if j + 1 < nz:
            add_jump(row, j, i, j + 1, i, rzp)
        if j - 1 >= 0:
            add_jump(row, j, i, j - 1, i, rzm)

    Q = Q.tocsr()
    # q was assembled from the exact same jump rates.  Verify against Q phi+b.
    q_matrix = Q @ phi + b_selected
    q_identity = float(np.max(np.abs(q - q_matrix))) if len(q) else 0.0
    if q_identity > 1e-8 * max(1.0, float(np.max(np.abs(q)))):
        raise AssertionError(f"discrete Ramo source identity failed: {q_identity}")

    return DiscreteGenerator(
        Q=Q,
        q_ramo=q,
        b_selected=b_selected,
        phi=phi,
        transient_flat=transient_flat,
        flat_to_transient=flat_to_transient,
        selected_mask=selected,
        bottom_mask=bottom,
        max_cell_peclet=float(max_pe),
        xs=xs,
        zs=zs,
        geometry=g,
    )


def solve_resolvent(gen: DiscreteGenerator, cfg: ResolventConfig) -> tuple[np.ndarray, dict[str, Any]]:
    """Solve all RF resolvents and the independent dc committor check."""
    n = gen.Q.shape[0]
    if n == 0:
        raise ValueError("no transient grid nodes")
    if not (np.isinf(cfg.lifetime_s) or cfg.lifetime_s > 0.0):
        raise ValueError("lifetime must be positive or infinity")
    kappa = 0.0 if np.isinf(cfg.lifetime_s) else 1.0 / cfg.lifetime_s
    I = csr_matrix(np.eye(n))

    # Selected-contact hitting probability for the no-recombination dc identity.
    p = spsolve((-gen.Q).tocsc(), gen.b_selected)
    committor_res = -gen.Q @ p - gen.b_selected
    committor_rel = float(
        np.linalg.norm(committor_res)
        / max(np.linalg.norm(gen.b_selected), np.finfo(float).tiny)
    )

    U = np.zeros((len(base.FREQUENCIES), n), dtype=complex)
    residuals = []
    for kf, f in enumerate(base.FREQUENCIES):
        s = kappa + 1j * 2.0 * np.pi * float(f)
        A = (s * I - gen.Q).tocsc()
        u = spsolve(A, gen.q_ramo.astype(complex))
        U[kf] = u
        r = A @ u - gen.q_ramo
        residuals.append(
            float(
                np.linalg.norm(r)
                / max(np.linalg.norm(gen.q_ramo), np.finfo(float).tiny)
            )
        )

    if kappa == 0.0:
        dc_identity_error = float(np.max(np.abs(U[0].real - (p - gen.phi))))
        dc_imag_max = float(np.max(np.abs(U[0].imag)))
    else:
        # The simple committor identity is specifically the infinite-lifetime
        # check.  The killed resolvent still uses the same discrete Ramo source.
        dc_identity_error = None
        dc_imag_max = float(np.max(np.abs(U[0].imag)))

    return U, {
        "max_linear_relative_residual": float(max(residuals)),
        "linear_relative_residual_by_frequency": residuals,
        "committor_relative_residual": committor_rel,
        "dc_committor_ramo_max_abs_error": dc_identity_error,
        "dc_max_imaginary_part": dc_imag_max,
        "max_cell_peclet": gen.max_cell_peclet,
        "transient_nodes": int(n),
    }


def full_grid(gen: DiscreteGenerator, u: np.ndarray) -> np.ndarray:
    """Embed a transient-state solution in the physical grid with zero future response on contacts."""
    out = np.zeros(len(gen.xs) * len(gen.zs), dtype=complex)
    out[gen.transient_flat] = np.asarray(u, complex)
    return out.reshape(len(gen.zs), len(gen.xs))


def integrate_currents(gen: DiscreteGenerator, U: np.ndarray, cfg: ResolventConfig) -> np.ndarray:
    """Integrate the resolvent over the inherited lateral and spectral kernels."""
    xq_um, wx = base.gauss(-base.X_EXTENT_UM, base.X_EXTENT_UM, cfg.nx_src)
    beam = np.exp(-0.5 * (xq_um / base.X_SIGMA_UM) ** 2)
    beam /= np.sum(wx * beam)

    # Match the checked trajectory integration support: avoid evaluating source
    # exactly on absorbing contacts.
    mask = (base.OPT_Z_UM >= 0.01) & (base.OPT_Z_UM <= base.L_UM - 0.01)
    zd_um = np.asarray(base.OPT_Z_UM[mask], float)
    points = np.column_stack(
        [
            np.repeat(zd_um * 1e-6, len(xq_um)),
            np.tile(xq_um * 1e-6, len(zd_um)),
        ]
    )

    J = np.zeros((len(base.FREQUENCIES), len(base.DEPTHS)), dtype=complex)
    for kf in range(len(base.FREQUENCIES)):
        grid = full_grid(gen, U[kf])
        interp = RegularGridInterpolator(
            (gen.zs, gen.xs), grid, method="linear", bounds_error=True
        )
        vals = interp(points).reshape(len(zd_um), len(xq_um))
        for ix in range(len(xq_um)):
            Hz = vals[:, ix]
            for m, optical in enumerate(base.OPTICS):
                J[kf, m] += (
                    wx[ix]
                    * beam[ix]
                    * np.trapezoid(optical[3][mask] * Hz, zd_um)
                )
    return J


def run_case(scenario: base.Scenario, cfg: ResolventConfig) -> dict[str, Any]:
    if cfg.diffusion_m2_s == 0.0 and np.isinf(cfg.lifetime_s):
        J, d = base.currents(
            scenario,
            nx=cfg.nx,
            nz=cfg.nz,
            nx_src=cfg.nx_src,
            nz_src=41,
            ds_um=0.020,
        )
        return {
            "mode": "checked_deterministic_recovery",
            "config": cfg.__dict__,
            "currents": {"real": J.real.tolist(), "imag": J.imag.tolist()},
            "solver_diagnostics": d,
            "blind_diagnostics": stage.blind_analysis(J),
        }

    gen = build_generator(scenario, cfg)
    U, diag = solve_resolvent(gen, cfg)
    J = integrate_currents(gen, U, cfg)
    assert np.all(np.isfinite(J.real)) and np.all(np.isfinite(J.imag))
    assert diag["max_linear_relative_residual"] < 1e-8
    assert diag["committor_relative_residual"] < 1e-8
    if np.isinf(cfg.lifetime_s):
        assert diag["dc_committor_ramo_max_abs_error"] < 1e-8
    return {
        "mode": "deterministic_backward_resolvent_stage_A",
        "config": cfg.__dict__,
        "currents": {"real": J.real.tolist(), "imag": J.imag.tolist()},
        "solver_diagnostics": diag,
        "blind_diagnostics": stage.blind_analysis(J),
    }


def complex_currents(case: dict[str, Any]) -> np.ndarray:
    c = case["currents"]
    return np.asarray(c["real"], float) + 1j * np.asarray(c["imag"], float)


def metric_by_frequency(case: dict[str, Any]) -> dict[float, dict[str, Any]]:
    return {
        float(m["frequency_hz"]): m
        for m in case["blind_diagnostics"]["metrics"]
    }


def convergence_pair(coarse: dict[str, Any], fine: dict[str, Any]) -> dict[str, Any]:
    Jc, Jf = complex_currents(coarse), complex_currents(fine)
    dc, df = np.diff(Jc, axis=1), np.diff(Jf, axis=1)
    scale = np.linalg.norm(df)
    step_rel = float(np.linalg.norm(df - dc) / max(scale, np.finfo(float).tiny))

    mc, mf = metric_by_frequency(coarse), metric_by_frequency(fine)
    phase_rows = []
    for f in base.FREQUENCIES:
        f = float(f)
        if f <= 0.0:
            continue
        pc = float(mc[f]["closure4_phase_deg"])
        pf = float(mf[f]["closure4_phase_deg"])
        target = abs(float(base.GRADIENT_TARGET_DEG[f]))
        phase_rows.append(
            {
                "frequency_hz": f,
                "coarse_phase_deg": pc,
                "fine_phase_deg": pf,
                "absolute_phase_change_deg": abs(pf - pc),
                "phase_change_fraction_of_frozen_target": abs(pf - pc) / target,
            }
        )
    return {
        "first_difference_relative_change": step_rel,
        "rf_phase_rows": phase_rows,
        "worst_phase_change_fraction_of_frozen_target": float(
            max(r["phase_change_fraction_of_frozen_target"] for r in phase_rows)
        ),
    }


def json_safe(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [json_safe(v) for v in obj]
    if isinstance(obj, np.generic):
        return json_safe(obj.item())
    if isinstance(obj, float):
        if np.isnan(obj):
            return "nan"
        if np.isposinf(obj):
            return "inf"
        if np.isneginf(obj):
            return "-inf"
    return obj


def run_grid_gate(tier: str) -> dict[str, Any]:
    scenario = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")
    if tier == "quick":
        grids = ((61, 47), (81, 61), (121, 91))
        nx_src = 9
    elif tier == "refined":
        grids = ((81, 61), (121, 91), (161, 121))
        nx_src = 13
    else:
        raise ValueError(tier)

    cases = []
    for nx, nz in grids:
        print(f"resolvent grid {nx}x{nz}", flush=True)
        cfg = ResolventConfig(
            diffusion_m2_s=2.5e-3,
            lifetime_s=float("inf"),
            nx=nx,
            nz=nz,
            nx_src=nx_src,
        )
        cases.append(run_case(scenario, cfg))

    pairs = []
    for a, b in zip(cases[:-1], cases[1:]):
        pairs.append(
            {
                "from_grid": [a["config"]["nx"], a["config"]["nz"]],
                "to_grid": [b["config"]["nx"], b["config"]["nz"]],
                **convergence_pair(a, b),
            }
        )

    # Predeclared numerical-readiness coordinate for this deterministic solver.
    # The finest available pair must change the raw four-color phase by <=2%
    # of the frozen transport target at every nonzero RF.  This is stricter
    # than the initial Monte-Carlo 5% readiness coordinate and is not a physics
    # significance threshold.
    threshold = 0.02
    finest_pass = pairs[-1]["worst_phase_change_fraction_of_frozen_target"] <= threshold

    return {
        "schema": "paper03-stageA-resolvent-grid-gate-v1",
        "status": "DETERMINISTIC NUMERICAL GATE / NON-CLAIM",
        "tier": tier,
        "scenario": scenario.__dict__,
        "formulation": {
            "process": "fixed-field single-carrier drift-diffusion with optional exponential killing",
            "backward_equation": "(kappa+i*omega-L_h)H=L_h(phi_w)",
            "spatial_discretization": "positive exponentially fitted nearest-neighbour Markov generator",
            "absorbing_boundaries": "selected top contact and bottom contact",
            "reflecting_boundaries": "sidewalls and uncontacted top surface",
            "stage_B_self_consistent_semiconductor": False,
        },
        "cases": cases,
        "grid_pairs": pairs,
        "initial_grid_precision_gate": {
            "definition": "finest-pair raw four-color phase change <=2% of frozen reference transport phase at every nonzero RF",
            "threshold_fraction": threshold,
            "finest_pair_passed": bool(finest_pass),
        },
        "blind_analysis_scope": (
            "The stored closure/Hankel/root quantities are inherited raw geometry "
            "diagnostics only.  The full calibrated arbitrary-kernel one-mode "
            "consistency inverse and branch-controlled physical root test remain "
            "a separate required gate."
        ),
        "science_interpretation_ready": False,
        "remaining_before_interpretation": [
            "cross-check the deterministic resolvent against independent stochastic sampling",
            "pass/refine the deterministic grid precision gate",
            "implement the kernel-aware blind consistency inverse",
            "implement and independently validate Stage-B self-consistent semiconductor physics",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--tier", choices=("quick", "refined"), default="quick")
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_stageA_resolvent_grid_gate.json"),
    )
    args = p.parse_args()

    result = run_grid_gate(args.tier)
    safe = json_safe(result)
    args.output.write_text(json.dumps(safe, indent=2, allow_nan=False) + "\n", encoding="utf-8")

    for case in result["cases"]:
        d = case["solver_diagnostics"]
        print(
            f"{case['config']['nx']}x{case['config']['nz']}: "
            f"Pe_max={d['max_cell_peclet']:.4g}, "
            f"linear_res={d['max_linear_relative_residual']:.3e}, "
            f"dc_identity={d['dc_committor_ramo_max_abs_error']:.3e}"
        )
    print(json.dumps(result["grid_pairs"], indent=2))
    print(json.dumps(result["initial_grid_precision_gate"], indent=2))
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")
    print("PASS: deterministic Stage-A resolvent gate completed; no physics claim made.")


if __name__ == "__main__":
    main()
