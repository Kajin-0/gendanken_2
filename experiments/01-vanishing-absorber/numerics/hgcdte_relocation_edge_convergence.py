"""Spatial-convergence test for programmed-gradient relocation edge sharpness.

The first feature-shape sweep appeared to prefer a ~50-nm edge ramp, but the
canonical inverse used only 80 transport cells over 7.6 um (~95 nm/cell). This
script removes that numerical ambiguity by rebuilding the finite-RF Jacobian at
80, 160, and 320 spatial cells and comparing programmed edge ramps from 25 to
200 nm.

Fixed physical design for the convergence test:
- absorber L=7.6 um, x_front=0.55, x_back=0.32;
- 1.0-um programmed feature, slope modulation a=4;
- translated centers 4.1 and 5.6 um;
- lambda = 2.00-2.40 um in 0.025-um steps;
- f = 0.25, 0.50, 1, 2, 3 GHz;
- front and back interface nuisance exponentials plus cubic smooth bulk;
- additive-like sigma_phi proportional to Pabs^-1;
- fixed-total-wavelength-time score ||r_white||/sqrt(N_lambda).

The illustrative 25% feature-supported transport perturbation remains a design
probe, not a device prediction.

No novelty claim.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

from hgcdte_sample_a_constraint_family_joint_iso_kernel import (
    HC_EV_UM,
    alpha_moazzami,
)
from hgcdte_matched_contact_translated_gradient_design import (
    FREQUENCIES_GHZ,
    L_UM,
    X_BACK,
    X_FRONT,
)
from hgcdte_shortwave_finite_rf_jacobian import (
    PERTURBATION_FRACTION,
    Q0_PS_PER_UM,
    project_residual,
)

WAVELENGTHS_UM = np.arange(2.00, 2.4001, 0.025)
Z1_UM = 4.1
Z2_UM = 5.6
FEATURE_WIDTH_UM = 1.0
MODULATION = 4.0
RAMP_VALUES_UM = (0.025, 0.050, 0.075, 0.100, 0.150, 0.200)
N_CELL_VALUES = (80, 160, 320)


def eg_hansen(x: np.ndarray | float, T: float = 300.0):
    return (
        -0.302
        + 1.93 * x
        + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2
        + 0.832 * x**3
    )


def programmed_feature(z: np.ndarray, z0: float, ramp: float):
    half = 0.5 * FEATURE_WIDTH_UM
    flat_half = half - ramp
    d = np.abs(z - z0)
    h = np.zeros_like(z)
    h[d <= flat_half] = 1.0
    transition = (d > flat_half) & (d < half)
    h[transition] = (half - d[transition]) / ramp
    return h


def profile(z0: float, ramp: float):
    z = np.linspace(0.0, L_UM, 4001)
    h = programmed_feature(z, z0, ramp)
    h_mean = float(np.trapezoid(h, z) / L_UM)
    s0 = (X_FRONT - X_BACK) / L_UM
    slope = s0 * (1.0 + MODULATION * (h - h_mean))
    if np.min(slope) <= 0.0:
        raise RuntimeError("nonmonotonic programmed profile")
    x = X_FRONT - np.concatenate(([0.0], cumulative_trapezoid(slope, z)))
    return z, x, h


def generation_probabilities(z, x, wavelength, n_cell):
    edges = np.linspace(0.0, L_UM, n_cell + 1)
    alpha = alpha_moazzami(HC_EV_UM / wavelength, x, 300.0)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, z * 1.0e-4)))
    tau_edges = np.interp(edges, z, tau)
    pabs = float(1.0 - np.exp(-tau_edges[-1]))
    probability = (
        np.exp(-tau_edges[:-1]) - np.exp(-tau_edges[1:])
    ) / pabs
    probability /= np.sum(probability)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return probability, centers, edges, pabs


def finite_rf(z, x, n_cell):
    edges = np.linspace(0.0, L_UM, n_cell + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    starts = edges[:-1]
    widths = np.diff(edges)
    overlap = np.clip(
        centers[:, None] - starts[None, :],
        0.0,
        widths[None, :],
    )
    t0_ps = Q0_PS_PER_UM * centers

    probability = []
    pabs = []
    for wavelength in WAVELENGTHS_UM:
        p, _, _, pa = generation_probabilities(
            z, x, float(wavelength), n_cell
        )
        probability.append(p)
        pabs.append(pa)
    probability = np.asarray(probability)

    jacobian = []
    transfer = []
    for f_ghz in FREQUENCIES_GHZ:
        omega = 2.0 * np.pi * f_ghz * 1.0e9
        phase = np.exp(-1j * omega * t0_ps * 1.0e-12)
        H = probability @ phase
        weighted = (probability * phase[None, :]) @ overlap
        J = -1j * omega * 1.0e-12 * weighted / H[:, None]
        jacobian.append(J)
        transfer.append(H)
    return np.asarray(jacobian), np.asarray(transfer), np.asarray(pabs), centers


def delta_q(z, support, centers):
    h = np.interp(centers, z, support)
    h /= np.max(h)
    return Q0_PS_PER_UM * (
        1.0 / (1.0 - PERTURBATION_FRACTION * h) - 1.0
    )


def nuisance_spatial(centers):
    u = centers / L_UM
    columns = [np.ones_like(centers), u, u**2, u**3]
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-centers / ell))
    for ell in (0.30, 0.50, 0.75, 1.00):
        columns.append(np.exp(-(L_UM - centers) / ell))
    return np.column_stack(columns)


def raw_vector(response):
    return np.concatenate((response.imag.reshape(-1), response.real.reshape(-1)))


def raw_matrix(response):
    return np.concatenate(
        (
            response.imag.reshape(-1, response.shape[-1]),
            response.real.reshape(-1, response.shape[-1]),
        ),
        axis=0,
    )


def intercepts(n_lambda):
    n_f = len(FREQUENCIES_GHZ)
    n = n_f * n_lambda
    matrix = np.zeros((2 * n, 2 * n_f))
    for fi in range(n_f):
        rows = np.arange(fi * n_lambda, (fi + 1) * n_lambda)
        matrix[rows, fi] = 1.0
        matrix[n + rows, n_f + fi] = 1.0
    return matrix


def design_score(ramp: float, n_cell: int):
    z1, x1, h1 = profile(Z1_UM, ramp)
    z2, x2, h2 = profile(Z2_UM, ramp)
    J1, _, p1, centers = finite_rf(z1, x1, n_cell)
    J2, _, p2, _ = finite_rf(z2, x2, n_cell)

    dq1 = delta_q(z1, h1, centers)
    dq2 = delta_q(z2, h2, centers)
    target = (
        np.einsum("flj,j->fl", J2, dq2)
        - np.einsum("flj,j->fl", J1, dq1)
    )
    spatial = nuisance_spatial(centers)
    common = np.einsum("flj,jk->flk", J2 - J1, spatial)

    data = raw_vector(target)
    nuisance = np.column_stack((raw_matrix(common), intercepts(len(WAVELENGTHS_UM))))

    relative_sigma = np.sqrt(p1 ** (-2.0) + p2 ** (-2.0))
    sigma_rows = np.tile(relative_sigma, len(FREQUENCIES_GHZ))
    sigma_rows = np.concatenate((sigma_rows, sigma_rows))

    angle_deg, residual = project_residual(
        data / sigma_rows,
        nuisance / sigma_rows[:, None],
    )
    score = float(residual / np.sqrt(len(WAVELENGTHS_UM)))
    phase_pp = float(
        np.ptp(np.degrees(target[FREQUENCIES_GHZ.index(1.0)].imag))
    )
    return score, float(angle_deg), phase_pp


def main() -> None:
    stored = {}
    print("Programmed relocation edge-ramp spatial convergence")
    for n_cell in N_CELL_VALUES:
        print(f"N_cell={n_cell}, dz={L_UM/n_cell:.6f} um")
        for ramp in RAMP_VALUES_UM:
            result = design_score(ramp, n_cell)
            stored[(n_cell, ramp)] = result
            print(
                f"  ramp={ramp:.3f} um -> score={result[0]:.9f}, "
                f"angle={result[1]:.3f} deg, phase_pp={result[2]:.6f} deg"
            )

    score320 = {r: stored[(320, r)][0] for r in RAMP_VALUES_UM}
    plateau = [score320[r] for r in (0.025, 0.050, 0.075, 0.100)]
    spread = (max(plateau) - min(plateau)) / np.mean(plateau)
    loss_020 = 1.0 - score320[0.200] / score320[0.100]

    print()
    print(f"320-cell 25-100 nm plateau fractional spread = {spread:.4f}")
    print(f"320-cell 200 nm vs 100 nm score loss = {loss_020:.4f}")

    assert spread < 0.011
    assert 0.29 < loss_020 < 0.31
    assert 0.00272 < score320[0.100] < 0.00275

    # 100-nm ramp is already converged at the sub-percent scale from 160->320.
    conv100 = abs(stored[(320, 0.100)][0] - stored[(160, 0.100)][0]) / stored[(320, 0.100)][0]
    assert conv100 < 0.001

    print()
    print(
        "PASS: the apparent 50-nm optimum at 80 cells was not a reliable exact "
        "feature-size result. At 320 cells, 25-100 nm transitions form an "
        "essentially flat information plateau (~1% spread), while a 200-nm "
        "transition loses about 30%. A ~0.1-um graded edge is therefore already "
        "near the resolved optimum in this model; there is no numerical evidence "
        "that an ultrasharp interface is required."
    )


if __name__ == "__main__":
    main()
