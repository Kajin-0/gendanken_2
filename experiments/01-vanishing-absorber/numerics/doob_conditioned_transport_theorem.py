"""Doob-conditioned transport theorem for DC-normalized first-passage RF.

Original killed backward generator:

    D u'' + v u' - (kappa+s) u = 0.

Let h=u(z,0) and F=u(z,i omega)/h. Then exactly

    D F'' + w F' - i omega F = 0,
    w = v + 2D h'/h.

Thus normalized RF is the first-passage dynamics of the diffusion conditioned
on successful collection (Doob h-transform). It identifies D and conditioned
drift w; the DC field h is needed to reconstruct original v and kappa.

This regression solves a strongly varying killed diffusion and verifies the
transformed PDE and exact local coefficient reconstruction.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_bvp


L = 1.0
OMEGA = 5.0


def velocity(z):
    return 1.5 * (
        1.0
        + 0.25 * np.sin(2.0 * np.pi * z)
        + 0.08 * np.sin(6.0 * np.pi * z)
    )


def diffusion(z):
    return 0.06 * (1.0 + 0.20 * np.cos(3.0 * np.pi * z))


def kappa(z):
    return 0.50 * (1.0 + 0.30 * np.sin(4.0 * np.pi * z))


def solve_dc():
    grid = np.linspace(0.0, L, 1001)

    def ode(z, y):
        v = velocity(z)
        D = diffusion(z)
        k = kappa(z)
        return np.vstack((y[1], (k * y[0] - v * y[1]) / D))

    def bc(ya, yb):
        return np.array((ya[1], yb[0] - 1.0))

    initial = np.vstack((np.ones_like(grid), np.zeros_like(grid)))
    result = solve_bvp(ode, bc, grid, initial, tol=1e-9, max_nodes=20000)
    if result.status != 0:
        raise RuntimeError(result.message)
    return result


def solve_rf():
    grid = np.linspace(0.0, L, 1001)

    def ode(z, y):
        v = velocity(z)
        D = diffusion(z)
        k = kappa(z)
        ur, upr, ui, upi = y
        return np.vstack(
            (
                upr,
                (k * ur - OMEGA * ui - v * upr) / D,
                upi,
                (k * ui + OMEGA * ur - v * upi) / D,
            )
        )

    def bc(ya, yb):
        return np.array((ya[1], ya[3], yb[0] - 1.0, yb[2]))

    initial = np.vstack(
        (
            np.ones_like(grid),
            np.zeros_like(grid),
            np.zeros_like(grid),
            np.zeros_like(grid),
        )
    )
    result = solve_bvp(ode, bc, grid, initial, tol=1e-9, max_nodes=30000)
    if result.status != 0:
        raise RuntimeError(result.message)
    return result


def main() -> None:
    sol0 = solve_dc()
    solw = solve_rf()
    z = np.linspace(0.05, 0.95, 1801)

    y0 = sol0.sol(z)
    y0d = sol0.sol(z, 1)
    h = y0[0]
    hp = y0[1]
    hpp = y0d[1]
    c = hp / h
    cp = hpp / h - c * c

    yw = solw.sol(z)
    ywd = solw.sol(z, 1)
    u = yw[0] + 1j * yw[2]
    up = yw[1] + 1j * yw[3]
    upp = ywd[1] + 1j * ywd[3]

    # F=u/h. Work through logarithmic slopes for numerical stability.
    gamma_u = up / u
    gamma_up = upp / u - gamma_u * gamma_u
    r = gamma_u - c
    rp = gamma_up - cp
    A = rp + r * r

    D_true = diffusion(z)
    v_true = velocity(z)
    k_true = kappa(z)
    w_true = v_true + 2.0 * D_true * c

    # The transformed Riccati equation must be D A + w r = i omega.
    closure = D_true * A + w_true * r - 1j * OMEGA
    closure_error = float(np.max(np.abs(closure)))

    determinant = np.real(A) * np.imag(r) - np.imag(A) * np.real(r)
    D_rec = -OMEGA * np.real(r) / determinant
    w_rec = OMEGA * np.real(A) / determinant

    # Undo the conditioning with the independently observed DC field.
    v_rec = w_rec - 2.0 * D_rec * c
    k_rec = D_rec * (cp - c * c) + w_rec * c

    def rel_stats(rec, truth):
        err = np.abs(rec / truth - 1.0)
        return float(np.median(err)), float(np.max(err))

    D_stats = rel_stats(D_rec, D_true)
    w_stats = rel_stats(w_rec, w_true)
    v_stats = rel_stats(v_rec, v_true)
    k_stats = rel_stats(k_rec, k_true)

    print("Doob-conditioned DC-normalized transport theorem")
    print(f"max transformed-PDE Riccati closure error = {closure_error:.3e}")
    print(f"D relative error median/max = {D_stats[0]:.3e}/{D_stats[1]:.3e}")
    print(f"w relative error median/max = {w_stats[0]:.3e}/{w_stats[1]:.3e}")
    print(f"v relative error median/max = {v_stats[0]:.3e}/{v_stats[1]:.3e}")
    print(f"kappa relative error median/max = {k_stats[0]:.3e}/{k_stats[1]:.3e}")

    assert closure_error < 2.0e-12
    assert D_stats[1] < 2.0e-13
    assert w_stats[1] < 2.0e-13
    assert v_stats[1] < 2.0e-13
    assert k_stats[1] < 2.0e-13

    print()
    print(
        "PASS: DC-normalized RF exactly obeys a no-killing drift-diffusion "
        "equation with conditioned drift w=v+2D d_z ln h. Normalized RF "
        "recovers D,w; the DC collection field then uniquely unconditions the "
        "process to recover the original v and kappa."
    )


if __name__ == "__main__":
    main()
