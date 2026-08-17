"""Predeclared coplanar second-geometry numerical gate for Paper 03.

This implements only the fixed-field Stage-A geometry and numerical acceptance
contract frozen in:

  PAPER03_SECOND_GEOMETRY_PREDECLARATION_2026-08-17.md
  PAPER03_SECOND_GEOMETRY_NUMERICAL_LOCK_2026-08-17.md

No vertical-planar subtraction is constructed. Scientific model-order
interpretation is downstream of this numerical gate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.linalg import spsolve

import paper03_stageA_kernel_blind_gate as blind
import paper03_stageA_resolvent as resolvent
import realistic_geometry_closure_stress as base


WIDTH_UM = 16.0
L_UM = float(base.L_UM)
CONTACT_EDGE_UM = 2.0
V_BIAS = 0.30
D_M2_S = 2.5e-3
LIFETIME_S = float("inf")
BEAM_CENTER_UM = 0.0
BEAM_SIGMA_UM = 1.0
SOURCE_EXTENT_UM = 3.5
GRID_LADDER = ((81, 61), (121, 91), (161, 121))

DIRECT_FINE_GATE = 0.005
FIRST_DIFF_FINE_GATE = 0.020
RHO_FINE_ABS_FLOOR = 2e-5
RHO_FINE_REL_GATE = 0.10
DIRECT_QUAD_GATE = 0.0025
FIRST_DIFF_QUAD_GATE = 0.010
RHO_QUAD_ABS_FLOOR = 1e-5
RHO_QUAD_REL_GATE = 0.05


def _k(j: int, i: int, nx: int) -> int:
    return j * nx + i


def _backward_error(A: csr_matrix, x: np.ndarray, b: np.ndarray) -> float:
    r = A @ x - b
    Aa = A.copy()
    Aa.data = np.abs(Aa.data)
    denom = np.asarray(Aa @ np.abs(x)).ravel() + np.abs(b)
    scale = np.maximum(denom, np.finfo(float).tiny)
    return float(np.max(np.abs(r) / scale))


def solve_coplanar_potential(
    right_value: float, nx: int, nz: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Mixed-BC Laplace solve for the frozen coplanar topology."""
    W = WIDTH_UM * 1e-6
    L = L_UM * 1e-6
    edge = CONTACT_EDGE_UM * 1e-6
    xs = np.linspace(-W / 2.0, W / 2.0, nx)
    zs = np.linspace(0.0, L, nz)
    dx = float(xs[1] - xs[0])
    dz = float(zs[1] - zs[0])
    tol = 1e-14

    A = lil_matrix((nx * nz, nx * nz), dtype=float)
    b = np.zeros(nx * nz, dtype=float)

    for j, _z in enumerate(zs):
        for i, x in enumerate(xs):
            r = _k(j, i, nx)
            # Top electrical contacts take precedence at the top corners.
            if j == nz - 1 and x <= -edge + tol:
                A[r, r] = 1.0
                b[r] = 0.0
            elif j == nz - 1 and x >= edge - tol:
                A[r, r] = 1.0
                b[r] = right_value
            elif j == nz - 1:
                # Insulating central top gap: zero normal derivative.
                A[r, r] = 1.0
                A[r, _k(j - 1, i, nx)] = -1.0
            elif j == 0:
                # Insulating bottom.
                A[r, r] = 1.0
                A[r, _k(j + 1, i, nx)] = -1.0
            elif i == 0:
                # Insulating left sidewall.
                A[r, r] = 1.0
                A[r, _k(j, i + 1, nx)] = -1.0
            elif i == nx - 1:
                # Insulating right sidewall.
                A[r, r] = 1.0
                A[r, _k(j, i - 1, nx)] = -1.0
            else:
                A[r, r] = -2.0 / dx**2 - 2.0 / dz**2
                A[r, _k(j, i - 1, nx)] = 1.0 / dx**2
                A[r, _k(j, i + 1, nx)] = 1.0 / dx**2
                A[r, _k(j - 1, i, nx)] = 1.0 / dz**2
                A[r, _k(j + 1, i, nx)] = 1.0 / dz**2

    A = A.tocsr()
    sol = np.asarray(spsolve(A, b), float)
    err = _backward_error(A, sol, b)
    return xs, zs, sol.reshape(nz, nx), err


def geometry(nx: int, nz: int) -> dict[str, Any]:
    xs, zs, V, physical_err = solve_coplanar_potential(V_BIAS, nx, nz)
    xw, zw, pw, weighting_err = solve_coplanar_potential(1.0, nx, nz)
    if not (np.array_equal(xs, xw) and np.array_equal(zs, zw)):
        raise AssertionError("physical/weighting grids differ")
    dVdz, dVdx = np.gradient(V, zs, xs, edge_order=2)
    dwdz, dwdx = np.gradient(pw, zs, xs, edge_order=2)
    return {
        "xs": xs,
        "zs": zs,
        "V": V,
        "pw": pw,
        "dVdx": dVdx,
        "dVdz": dVdz,
        "dwdx": dwdx,
        "dwdz": dwdz,
        "physical_potential_backward_error": physical_err,
        "weighting_potential_backward_error": weighting_err,
    }


def build_generator(nx: int, nz: int) -> tuple[resolvent.DiscreteGenerator, dict[str, Any]]:
    g = geometry(nx, nz)
    xs = np.asarray(g["xs"], float)
    zs = np.asarray(g["zs"], float)
    dx = float(xs[1] - xs[0])
    dz = float(zs[1] - zs[0])
    edge = CONTACT_EDGE_UM * 1e-6
    tol = 1e-14

    right = np.zeros((nz, nx), dtype=bool)
    left = np.zeros((nz, nx), dtype=bool)
    right[-1, xs >= edge - tol] = True
    left[-1, xs <= -edge + tol] = True
    absorbing = right | left

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
        Q[row, row] -= rate
        q[row] += rate * (phi_grid[jn, inn] - phi_grid[j, i])
        if right[jn, inn]:
            b_selected[row] += rate
        elif left[jn, inn]:
            pass
        else:
            flat_n = jn * nx + inn
            col = int(flat_to_transient[flat_n])
            if col < 0:
                raise AssertionError("transient-neighbour map failure")
            Q[row, col] += rate

    for flat in transient_flat:
        j, i = divmod(int(flat), nx)
        row = int(flat_to_transient[flat])
        vx, vz, _ = base.velocity(float(g["dVdx"][j, i]), float(g["dVdz"][j, i]))
        rxp, rxm, pex = resolvent.directional_rates(vx, dx, D_M2_S)
        rzp, rzm, pez = resolvent.directional_rates(vz, dz, D_M2_S)
        max_pe = max(max_pe, pex, pez)

        # Missing neighbours represent the declared reflecting boundaries.
        if i + 1 < nx:
            add_jump(row, j, i, j, i + 1, rxp)
        if i - 1 >= 0:
            add_jump(row, j, i, j, i - 1, rxm)
        if j + 1 < nz:
            add_jump(row, j, i, j + 1, i, rzp)
        if j - 1 >= 0:
            add_jump(row, j, i, j - 1, i, rzm)

    Q = Q.tocsr()
    q_from_matrix = Q @ phi + b_selected
    source_identity = float(np.max(np.abs(q - q_from_matrix)))
    source_scale = max(1.0, float(np.max(np.abs(q))))
    source_rel = source_identity / source_scale
    if source_rel >= 1e-8:
        raise AssertionError(f"discrete Ramo source identity failed: {source_rel}")

    gen = resolvent.DiscreteGenerator(
        Q=Q,
        q_ramo=q,
        b_selected=b_selected,
        phi=phi,
        transient_flat=transient_flat,
        flat_to_transient=flat_to_transient,
        selected_mask=right,
        bottom_mask=left,
        max_cell_peclet=float(max_pe),
        xs=xs,
        zs=zs,
        geometry=g,
    )
    return gen, {
        "physical_potential_backward_error": float(g["physical_potential_backward_error"]),
        "weighting_potential_backward_error": float(g["weighting_potential_backward_error"]),
        "discrete_ramo_source_relative_error": source_rel,
        "left_contact_nodes": int(np.sum(left)),
        "right_contact_nodes": int(np.sum(right)),
    }


def integrate_currents(gen: resolvent.DiscreteGenerator, U: np.ndarray, nx_src: int) -> np.ndarray:
    xq_um, wx = base.gauss(-SOURCE_EXTENT_UM, SOURCE_EXTENT_UM, nx_src)
    beam = np.exp(-0.5 * ((xq_um - BEAM_CENTER_UM) / BEAM_SIGMA_UM) ** 2)
    beam /= np.sum(wx * beam)

    z_um = np.asarray(base.OPT_Z_UM, float)
    points = np.column_stack(
        (
            np.repeat(z_um * 1e-6, len(xq_um)),
            np.tile(xq_um * 1e-6, len(z_um)),
        )
    )

    J = np.zeros((len(base.FREQUENCIES), len(base.DEPTHS)), dtype=complex)
    for kf in range(len(base.FREQUENCIES)):
        grid = resolvent.full_grid(gen, U[kf])
        interp = RegularGridInterpolator(
            (gen.zs, gen.xs), grid, method="linear", bounds_error=True
        )
        vals = interp(points).reshape(len(z_um), len(xq_um))
        for ix in range(len(xq_um)):
            Hz = vals[:, ix]
            for m, optical in enumerate(base.OPTICS):
                J[kf, m] += (
                    wx[ix]
                    * beam[ix]
                    * np.trapezoid(np.asarray(optical[3], float) * Hz, z_um)
                )
    return J


def fit_rho(J: np.ndarray) -> list[dict[str, Any]]:
    rows = []
    for kf, f in enumerate(base.FREQUENCIES):
        if float(f) <= 0.0:
            continue
        fit = blind.kernel_one_mode_fit(J[kf], blind.ALL6)
        rows.append(
            {
                "frequency_hz": float(f),
                "rho_all6": float(fit["contrast_normalized_residual"]),
                "r_per_um": fit["r_per_um"],
                "profile_design_condition_number": float(fit["profile_design_condition_number"]),
            }
        )
    return rows


def solve_grid(nx: int, nz: int, nx_src: int = 17) -> tuple[np.ndarray, dict[str, Any], resolvent.DiscreteGenerator, np.ndarray]:
    gen, electro = build_generator(nx, nz)
    cfg = resolvent.ResolventConfig(
        diffusion_m2_s=D_M2_S,
        lifetime_s=LIFETIME_S,
        nx=nx,
        nz=nz,
        nx_src=nx_src,
    )
    U, transport = resolvent.solve_resolvent(gen, cfg)
    J = integrate_currents(gen, U, nx_src)

    if not np.all(np.isfinite(J.real)) or not np.all(np.isfinite(J.imag)):
        raise AssertionError("non-finite coplanar current")
    for key in ("physical_potential_backward_error", "weighting_potential_backward_error", "discrete_ramo_source_relative_error"):
        if electro[key] >= 1e-8:
            raise AssertionError(f"{key} failed: {electro[key]}")
    if transport["max_linear_relative_residual"] >= 1e-8:
        raise AssertionError("RF resolvent residual gate failed")
    if transport["committor_relative_residual"] >= 1e-8:
        raise AssertionError("committor residual gate failed")
    if transport["dc_committor_ramo_max_abs_error"] is None or transport["dc_committor_ramo_max_abs_error"] >= 1e-8:
        raise AssertionError("DC committor/Ramo identity gate failed")

    return J, {
        "grid": [nx, nz],
        "source_quadrature": nx_src,
        "electrostatics": electro,
        "transport": transport,
        "one_mode": fit_rho(J),
    }, gen, U


def _rho_map(diag: dict[str, Any]) -> dict[float, float]:
    return {float(r["frequency_hz"]): float(r["rho_all6"]) for r in diag["one_mode"]}


def compare(
    Ja: np.ndarray,
    da: dict[str, Any],
    Jb: np.ndarray,
    db: dict[str, Any],
    *,
    direct_gate: float,
    diff_gate: float,
    rho_abs_floor: float,
    rho_rel_gate: float,
) -> dict[str, Any]:
    ra, rb = _rho_map(da), _rho_map(db)
    rows = []
    for kf, f0 in enumerate(base.FREQUENCIES):
        f = float(f0)
        if f <= 0.0:
            continue
        a = np.asarray(Ja[kf], complex)
        b = np.asarray(Jb[kf], complex)
        daj = np.diff(a)
        dbj = np.diff(b)
        eJ = float(np.linalg.norm(b - a) / max(np.linalg.norm(b), np.finfo(float).tiny))
        edJ = float(np.linalg.norm(dbj - daj) / max(np.linalg.norm(dbj), np.finfo(float).tiny))
        drho = abs(rb[f] - ra[f])
        rho_limit = max(rho_abs_floor, rho_rel_gate * rb[f])
        passed = eJ <= direct_gate and edJ <= diff_gate and drho <= rho_limit
        rows.append(
            {
                "frequency_hz": f,
                "direct_current_relative_change": eJ,
                "first_difference_relative_change": edJ,
                "rho_a": ra[f],
                "rho_b": rb[f],
                "rho_absolute_change": float(drho),
                "rho_allowed_change": float(rho_limit),
                "passed": bool(passed),
            }
        )
    return {"rows": rows, "passed": bool(all(r["passed"] for r in rows))}


def json_complex_matrix(J: np.ndarray) -> dict[str, Any]:
    return {"real": J.real.tolist(), "imag": J.imag.tolist()}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_second_geometry_gate.json"),
    )
    args = p.parse_args()

    grid_cases: list[tuple[np.ndarray, dict[str, Any], resolvent.DiscreteGenerator, np.ndarray]] = []
    for nx, nz in GRID_LADDER:
        grid_cases.append(solve_grid(nx, nz, 17))

    J81, d81, _, _ = grid_cases[0]
    J121, d121, _, _ = grid_cases[1]
    J161, d161, gen161, U161 = grid_cases[2]

    # 13->17 source quadrature check reuses the identical finest-grid field and resolvent.
    J161_13 = integrate_currents(gen161, U161, 13)
    d161_13 = {
        "one_mode": fit_rho(J161_13),
    }

    coarse_progress = compare(
        J81, d81, J121, d121,
        direct_gate=DIRECT_FINE_GATE,
        diff_gate=FIRST_DIFF_FINE_GATE,
        rho_abs_floor=RHO_FINE_ABS_FLOOR,
        rho_rel_gate=RHO_FINE_REL_GATE,
    )
    finest_pair = compare(
        J121, d121, J161, d161,
        direct_gate=DIRECT_FINE_GATE,
        diff_gate=FIRST_DIFF_FINE_GATE,
        rho_abs_floor=RHO_FINE_ABS_FLOOR,
        rho_rel_gate=RHO_FINE_REL_GATE,
    )
    source_quadrature = compare(
        J161_13, d161_13, J161, d161,
        direct_gate=DIRECT_QUAD_GATE,
        diff_gate=FIRST_DIFF_QUAD_GATE,
        rho_abs_floor=RHO_QUAD_ABS_FLOOR,
        rho_rel_gate=RHO_QUAD_REL_GATE,
    )

    numerical_gate_passed = bool(finest_pair["passed"] and source_quadrature["passed"])
    result = {
        "schema": "paper03-second-geometry-numerical-gate-v1",
        "status": "PREDECLARED COPLANAR NUMERICAL GATE / NON-CLAIM",
        "predeclaration": "PAPER03_SECOND_GEOMETRY_PREDECLARATION_2026-08-17.md",
        "numerical_lock": "PAPER03_SECOND_GEOMETRY_NUMERICAL_LOCK_2026-08-17.md",
        "geometry": {
            "width_um": WIDTH_UM,
            "thickness_um": L_UM,
            "left_contact_um": [-8.0, -2.0],
            "gap_um": [-2.0, 2.0],
            "right_contact_um": [2.0, 8.0],
            "bias_v": V_BIAS,
            "selected_terminal": "right_top",
            "bottom": "insulating",
            "sidewalls": "insulating",
            "top_gap": "insulating",
        },
        "physics": {
            "stage_B_self_consistent_semiconductor": False,
            "laplace_only": True,
            "diffusion_m2_s": D_M2_S,
            "lifetime_s": "inf",
            "beam_center_um": BEAM_CENTER_UM,
            "beam_sigma_um": BEAM_SIGMA_UM,
            "source_extent_um": SOURCE_EXTENT_UM,
        },
        "grids": [d81, d121, d161],
        "currents_finest": json_complex_matrix(J161),
        "coarse_progress_81_to_121": coarse_progress,
        "finest_pair_121_to_161": finest_pair,
        "source_quadrature_13_to_17": source_quadrature,
        "numerical_gate_passed": numerical_gate_passed,
        "science_interpretation_ready": False,
    }

    args.output.write_text(
        json.dumps(resolvent.json_safe(result), indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print("numerical_gate_passed =", numerical_gate_passed)
    for label, block in (
        ("121->161", finest_pair),
        ("13->17", source_quadrature),
    ):
        print(label)
        for row in block["rows"]:
            print(row)
    print("science_interpretation_ready = false")

    if not numerical_gate_passed:
        raise SystemExit("second-geometry numerical convergence gate failed; refine without moving thresholds")


if __name__ == "__main__":
    main()
