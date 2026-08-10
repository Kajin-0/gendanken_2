"""Exact local inverse for variable-coefficient 1-D first-passage transport.

Model
-----
    D(z) u'' + v(z) u' - [kappa(z)+s] u = 0.

Define the DC logarithmic spatial slope
    c = d_z ln u(z,0)
and the DC-normalized RF logarithmic spatial slope
    r = d_z ln[u(z,i omega)/u(z,0)].

Then gamma_w=c+r. Subtracting the DC Riccati equation from the real
part of the RF equation gives, with

    Z = r' + 2 c r + r^2,

    D Re Z + v Re r = 0,
    D Im Z + v Im r = omega.

If det = Re(Z) Im(r) - Im(Z) Re(r) != 0,

    D = -omega Re(r)/det,
    v =  omega Re(Z)/det,
    kappa = D(c' + c^2) + v c.

The identities are exact for the stated local backward generator; no WKB or
slow-variation assumption is used. This regression solves a strongly varying
boundary-value problem and checks the inverse.
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
        # Reflecting upstream boundary and unit collection value at z=L.
        return np.array((ya[1], yb[0] - 1.0))

    initial = np.vstack((np.ones_like(grid), np.zeros_like(grid)))
    result = solve_bvp(
        ode,
        bc,
        grid,
        initial,
        tol=1.0e-9,
        max_nodes=20000,
    )
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
    result = solve_bvp(
        ode,
        bc,
        grid,
        initial,
        tol=1.0e-9,
        max_nodes=30000,
    )
    if result.status != 0:
        raise RuntimeError(result.message)
    return result


def main() -> None:
    sol0 = solve_dc()
    solw = solve_rf()

    # Stay away from the boundary layers only to make the regression summary
    # representative. The pointwise algebra itself is local and exact wherever
    # the determinant is nonzero.
    z = np.linspace(0.05, 0.95, 1801)

    y0 = sol0.sol(z)
    y0_deriv = sol0.sol(z, 1)
    u0 = y0[0]
    u0p = y0[1]
    u0pp = y0_deriv[1]
    c = u0p / u0
    cp = u0pp / u0 - c * c

    yw = solw.sol(z)
    yw_deriv = solw.sol(z, 1)
    uw = yw[0] + 1j * yw[2]
    uwp = yw[1] + 1j * yw[3]
    uwpp = yw_deriv[1] + 1j * yw_deriv[3]
    gamma_w = uwp / uw
    gamma_wp = uwpp / uw - gamma_w * gamma_w

    r = gamma_w - c
    rp = gamma_wp - cp
    Z = rp + 2.0 * c * r + r * r

    determinant = np.real(Z) * np.imag(r) - np.imag(Z) * np.real(r)
    D_rec = -OMEGA * np.real(r) / determinant
    v_rec = OMEGA * np.real(Z) / determinant
    k_rec = D_rec * (cp + c * c) + v_rec * c

    D_true = diffusion(z)
    v_true = velocity(z)
    k_true = kappa(z)

    def error_stats(recovered, truth):
        err = np.abs(recovered / truth - 1.0)
        return float(np.median(err)), float(np.max(err))

    D_stats = error_stats(D_rec, D_true)
    v_stats = error_stats(v_rec, v_true)
    k_stats = error_stats(k_rec, k_true)

    print("Exact local variable-coefficient drift-diffusion inverse")
    print(
        f"D relative error median/max = {D_stats[0]:.3e}/{D_stats[1]:.3e}"
    )
    print(
        f"v relative error median/max = {v_stats[0]:.3e}/{v_stats[1]:.3e}"
    )
    print(
        f"kappa relative error median/max = {k_stats[0]:.3e}/{k_stats[1]:.3e}"
    )
    print(
        "determinant min/max = "
        f"{np.min(determinant):.6f}/{np.max(determinant):.6f}"
    )

    assert D_stats[1] < 2.0e-13
    assert v_stats[1] < 2.0e-13
    assert k_stats[1] < 2.0e-13
    assert np.min(np.abs(determinant)) > 1.0e-3

    print()
    print(
        "PASS: strongly varying D(z), v(z), and kappa(z) are recovered to "
        "numerical precision from the DC slope, normalized complex RF slope, "
        "and their spatial derivatives. No local-uniform or WKB approximation "
        "is required in the stated 1-D backward-generator model."
    )


if __name__ == "__main__":
    main()
