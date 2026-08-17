"""First-order validation of the Paper-02 parameter-bias law.

This test keeps the six calibrated optical kernels fixed and perturbs only the
true deterministic velocity field away from the uniform zero-diffusion point.
It therefore matches the assumptions of PAPER02_PARAMETER_BIAS_BOUND_2026-08-15.md.

At 100 MHz:

  y0 = exact uniform-velocity six-channel response,
  y(eps) = response for a weak prescribed downstream velocity gradient,
  E = y(eps)-y0.

The baseline calibrated one-mode model is exact.  We compute its root
sensitivity h = K dF/dr, remove the offset/amplitude tangent directions, and
predict

    delta r = (h_perp^H E)/(h_perp^H h_perp).

The actual fitted root is then obtained independently with the nonlinear
kernel-aware inverse.  We also propagate the predicted root shift through the
local homogeneous D(gamma) Jacobian and compare with the actual apparent D.

Both linear and exponential velocity families, with positive and negative small
endpoint perturbations, are tested.  Microscopic diffusion and recombination are
zero for every case.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import realistic_geometry_closure_stress as base
from paper02_kernel_aware_depletion_frequency_law import kernel_aware_root, kernel_basis


FREQUENCY_HZ = 100e6
OMEGA = 2.0 * np.pi * FREQUENCY_HZ
V0_M_PER_S = 2.65565e4
ZD_UM = 4.6
EPSILONS = (-0.05, -0.02, -0.01, -0.005, -0.002, -0.001,
             0.001, 0.002, 0.005, 0.01, 0.02, 0.05)
FAMILIES = ("linear", "exponential")


@dataclass(frozen=True)
class VelocityCase:
    family: str
    epsilon: float

    @property
    def endpoint_ratio(self):
        return 1.0 + self.epsilon


def velocity(case: VelocityCase | None, z_m: float) -> float:
    if case is None:
        return V0_M_PER_S
    z_um = z_m * 1e6
    if z_um <= ZD_UM:
        return V0_M_PER_S
    xi = (z_um - ZD_UM) / (float(base.L_UM) - ZD_UM)
    xi = float(np.clip(xi, 0.0, 1.0))
    R = case.endpoint_ratio
    if case.family == "linear":
        return V0_M_PER_S * (1.0 + (R - 1.0) * xi)
    if case.family == "exponential":
        return V0_M_PER_S * np.exp(np.log(R) * xi)
    raise ValueError(case.family)


def point_response(case: VelocityCase | None) -> np.ndarray:
    L_m = float(base.L_UM) * 1e-6

    def rhs(z, y):
        H = y[0]
        return np.asarray(
            (-1.0 / L_m + 1j * OMEGA * H / velocity(case, z),),
            dtype=complex,
        )

    sol = solve_ivp(
        rhs,
        (L_m, 0.0),
        np.asarray((0.0 + 0.0j,), dtype=complex),
        dense_output=True,
        rtol=2e-12,
        atol=2e-14,
        max_step=0.005e-6,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return np.asarray(sol.sol(np.asarray(base.OPT_Z_UM) * 1e-6)[0], dtype=complex)


def channels(case: VelocityCase | None) -> np.ndarray:
    H = point_response(case)
    return np.asarray(
        [np.trapezoid(np.asarray(row[3]) * H, base.OPT_Z_UM) for row in base.OPTICS],
        dtype=complex,
    )


def kernel_basis_derivative(r_per_m: complex) -> np.ndarray:
    z_um = np.asarray(base.OPT_Z_UM, dtype=float)
    z_m = z_um * 1e-6
    z_ref_m = float(np.mean(base.DEPTHS)) * 1e-6
    dz = z_m - z_ref_m
    r = complex(r_per_m)

    if abs(r) < 1e-8:
        point = 0.5 * dz**2
    else:
        erd = np.exp(r * dz)
        point = (r * dz * erd - np.expm1(r * dz)) / (r * r)

    return np.asarray(
        [np.trapezoid(np.asarray(row[3]) * point, z_um) for row in base.OPTICS],
        dtype=complex,
    )


def root_projection_setup(J0: np.ndarray):
    r0, coeff0, model0, fit0 = kernel_aware_root(J0)
    C0, K0 = coeff0
    F0 = kernel_basis(r0)
    Fr0 = kernel_basis_derivative(r0)
    X = np.column_stack((np.ones(len(F0), dtype=complex), F0))
    h = K0 * Fr0

    gram = X.conj().T @ X
    PX = X @ np.linalg.solve(gram, X.conj().T)
    h_perp = (np.eye(len(F0), dtype=complex) - PX) @ h
    denom = np.vdot(h_perp, h_perp).real
    if denom <= 0:
        raise RuntimeError("nonpositive root-sensitivity norm")
    return r0, C0, K0, fit0, h_perp, denom


def solve_dw(gamma: complex):
    a = float(gamma.real)
    b = float(gamma.imag)
    s = a * a + b * b
    D = -OMEGA * a / (b * s)
    w = OMEGA * (a * a - b * b) / (b * s)
    return float(D), float(w)


def diffusion_gradient(gamma: complex):
    a = float(gamma.real)
    b = float(gamma.imag)
    s = a * a + b * b
    dD_da = OMEGA * (a * a - b * b) / (b * s * s)
    dD_db = OMEGA * a * (a * a + 3.0 * b * b) / (b * b * s * s)
    return float(dD_da), float(dD_db)


def complex_relative_error(pred: complex, actual: complex):
    return float(abs(pred - actual) / max(abs(actual), 1e-30))


def run(args):
    old_freq = base.FREQUENCIES
    base.FREQUENCIES = np.asarray((0.0, FREQUENCY_HZ), dtype=float)
    try:
        J0 = channels(None)
        r0, C0, K0, fit0, h_perp, denom = root_projection_setup(J0)
        gamma0 = -r0
        D0, w0 = solve_dw(gamma0)
        dD_da, dD_db = diffusion_gradient(gamma0)

        rows = []
        for family in FAMILIES:
            for eps in EPSILONS:
                case = VelocityCase(family, float(eps))
                J = channels(case)
                E = J - J0

                dr_pred = np.vdot(h_perp, E) / denom
                r, _, _, fit_rel = kernel_aware_root(J)
                dr_actual = r - r0

                dgamma_pred = -dr_pred
                dgamma_actual = -dr_actual
                dD_pred = dD_da * dgamma_pred.real + dD_db * dgamma_pred.imag

                gamma = -r
                D, w = solve_dw(gamma)
                dD_actual = D - D0

                post_linear = E - np.column_stack(
                    (
                        np.ones(len(J0), dtype=complex),
                        kernel_basis(r0),
                        K0 * kernel_basis_derivative(r0),
                    )
                ) @ np.linalg.lstsq(
                    np.column_stack(
                        (
                            np.ones(len(J0), dtype=complex),
                            kernel_basis(r0),
                            K0 * kernel_basis_derivative(r0),
                        )
                    ),
                    E,
                    rcond=None,
                )[0]

                rows.append(
                    {
                        "family": family,
                        "epsilon": float(eps),
                        "endpoint_ratio": float(1.0 + eps),
                        "E_norm": float(np.linalg.norm(E)),
                        "pred_dr_real_per_m": float(dr_pred.real),
                        "pred_dr_imag_per_m": float(dr_pred.imag),
                        "actual_dr_real_per_m": float(dr_actual.real),
                        "actual_dr_imag_per_m": float(dr_actual.imag),
                        "root_shift_relative_error": complex_relative_error(dr_pred, dr_actual),
                        "pred_dD_m2_per_s": float(dD_pred),
                        "actual_dD_m2_per_s": float(dD_actual),
                        "D_linearization_relative_error": float(abs(dD_pred - dD_actual) / max(abs(dD_actual), 1e-30)),
                        "actual_D_m2_per_s": float(D),
                        "actual_w_m_per_s": float(w),
                        "kernel_fit_rel": float(fit_rel),
                        "linear_postfit_residual_over_E": float(np.linalg.norm(post_linear) / max(np.linalg.norm(E), 1e-30)),
                    }
                )
    finally:
        base.FREQUENCIES = old_freq

    small = [r for r in rows if abs(r["epsilon"]) <= 0.01]
    tiny = [r for r in rows if abs(r["epsilon"]) <= 0.002]

    payload = {
        "status": "CHECKED first-order bias-law validation",
        "frequency_hz": FREQUENCY_HZ,
        "model_truth": {
            "microscopic_diffusion": 0.0,
            "recombination": 0.0,
            "uniform_baseline_velocity_m_per_s": V0_M_PER_S,
            "nonuniform_region_start_um": ZD_UM,
        },
        "baseline": {
            "kernel_fit_rel": float(fit0),
            "r_real_per_m": float(r0.real),
            "r_imag_per_m": float(r0.imag),
            "gamma_real_per_m": float(gamma0.real),
            "gamma_imag_per_m": float(gamma0.imag),
            "D_m2_per_s": float(D0),
            "w_m_per_s": float(w0),
            "root_sensitivity_norm": float(np.sqrt(denom)),
            "dD_dgamma_real_m3_per_s": float(dD_da),
            "dD_dgamma_imag_m3_per_s": float(dD_db),
        },
        "validation": {
            "max_root_shift_relative_error_abs_eps_le_0p002": max(r["root_shift_relative_error"] for r in tiny),
            "max_D_linearization_relative_error_abs_eps_le_0p002": max(r["D_linearization_relative_error"] for r in tiny),
            "max_root_shift_relative_error_abs_eps_le_0p01": max(r["root_shift_relative_error"] for r in small),
            "max_D_linearization_relative_error_abs_eps_le_0p01": max(r["D_linearization_relative_error"] for r in small),
            "all_positive_eps_give_positive_D": all(r["actual_D_m2_per_s"] > 0 for r in rows if r["epsilon"] > 0),
            "all_negative_eps_give_negative_D": all(r["actual_D_m2_per_s"] < 0 for r in rows if r["epsilon"] < 0),
        },
        "rows": rows,
    }

    out_csv = Path(args.output_csv)
    out_json = Path(args.output_summary)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--output-csv", default="paper02_bias_bound_linearization.csv")
    p.add_argument("--output-summary", default="paper02_bias_bound_linearization_summary.json")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
