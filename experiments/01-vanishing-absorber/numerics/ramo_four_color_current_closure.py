"""Shockley-Ramo observable audit for the spectral-depth closure program.

This regression distinguishes two different observables that must not be
conflated:

1. arrival / collection-flux transfer
       U(d,s) = E[exp(-s T_d)]
   which is exponential in propagation distance for homogeneous scalar
   first-passage transport;

2. planar Shockley-Ramo induced current for one conserved carrier in a uniform
   weighting field.  For constant drift w>0 and diffusion D>0 on a half-line
   with an absorbing collector a distance d away,

       D gamma^2 + w gamma = s,
       U(d,s) = exp(-gamma d),

   while the expected de-embedded induced-current transform is

       J(d,s) = C(s) [1 - exp(-gamma d)].

The additive constant means the old three-color geometric-mean law is NOT a
terminal-current identity.  However first spatial differences remove that
constant.  Four equally spaced source depths obey

       (J2-J1)^2 = (J1-J0)(J3-J2).

The difference ratio recovers exp(-gamma Delta d), so one RF frequency still
recovers D,w and a second RF frequency is a pure model test.

The script also demonstrates that DC-normalizing the terminal current generally
destroys the finite-rank affine-exponential structure.  Thus arrival-flux,
raw induced-current, and DC-normalized current must remain distinct throughout
the theory.
"""

from __future__ import annotations

import numpy as np


D = 0.12
W = 1.70
OMEGAS = (0.8, 2.3, 5.1)
D0 = 0.55
DELTA = 0.31
DEPTHS = D0 + DELTA * np.arange(4)


def gamma(omega: float) -> complex:
    return (np.sqrt(W * W + 4j * D * omega) - W) / (2.0 * D)


def arrival(depth: np.ndarray, omega: float) -> np.ndarray:
    return np.exp(-gamma(omega) * depth)


def raw_ramo(depth: np.ndarray, omega: float, gain: complex = 1.0) -> np.ndarray:
    # The overall factor is irrelevant to all closure identities below.
    return gain * (1.0 - np.exp(-gamma(omega) * depth))


def dc_ramo(depth: np.ndarray) -> np.ndarray:
    # Conserved-carrier s->0 limit: mean induced charge-time integral is
    # proportional to mean first-passage time d/W.
    return depth / W


def normalized_ramo(depth: np.ndarray, omega: float) -> np.ndarray:
    return raw_ramo(depth, omega) / dc_ramo(depth)


def invert_gamma(g: complex, omega: float) -> tuple[float, float]:
    a = float(np.real(g))
    b = float(np.imag(g))
    modulus2 = a * a + b * b
    D_rec = omega * a / (b * modulus2)
    W_rec = omega * (b * b - a * a) / (b * modulus2)
    return D_rec, W_rec


def four_color_residual(values: np.ndarray) -> complex:
    d01 = values[1] - values[0]
    d12 = values[2] - values[1]
    d23 = values[3] - values[2]
    return d12 * d12 - d01 * d23


def three_color_log_closure(values: np.ndarray) -> complex:
    return 2.0 * np.log(values[1]) - np.log(values[0]) - np.log(values[2])


def main() -> None:
    print("Shockley-Ramo four-color current closure")

    max_four = 0.0
    max_D = 0.0
    max_W = 0.0
    for omega in OMEGAS:
        # Allow an arbitrary common electronics/source complex gain.  The
        # closure and difference ratio must be invariant to it.
        common_gain = (1.2 - 0.35j) * np.exp(0.13j * omega)
        offset = 0.17 + 0.09j
        J = raw_ramo(DEPTHS, omega, gain=common_gain) + offset

        residual = four_color_residual(J)
        max_four = max(max_four, abs(residual))

        delta0 = J[1] - J[0]
        delta1 = J[2] - J[1]
        q = delta1 / delta0
        g_rec = -np.log(q) / DELTA
        D_rec, W_rec = invert_gamma(g_rec, omega)
        max_D = max(max_D, abs(D_rec / D - 1.0))
        max_W = max(max_W, abs(W_rec / W - 1.0))

        print(
            f"omega={omega:.2f}: |four-color residual|={abs(residual):.3e}, "
            f"D={D_rec:.12f}, w={W_rec:.12f}"
        )

    # The arrival observable obeys the old three-color law exactly.
    A = arrival(DEPTHS[:3], OMEGAS[1])
    arrival_closure = three_color_log_closure(A)

    # The raw Ramo current does not obey that same law.
    J3 = raw_ramo(DEPTHS[:3], OMEGAS[1])
    ramo_old_closure = three_color_log_closure(J3)

    # Nor does the DC-normalized terminal current.  This is the crucial
    # counterexample to treating generic photodiode RF current as a
    # first-passage characteristic function.
    Hn = normalized_ramo(DEPTHS[:3], OMEGAS[1])
    normalized_old_closure = three_color_log_closure(Hn)

    print()
    print(f"arrival 3-color closure magnitude = {abs(arrival_closure):.3e}")
    print(f"raw Ramo old 3-color closure magnitude = {abs(ramo_old_closure):.3e}")
    print(
        "DC-normalized Ramo old 3-color closure magnitude = "
        f"{abs(normalized_old_closure):.3e}"
    )

    assert max_four < 5.0e-14
    assert max_D < 2.0e-13
    assert max_W < 2.0e-13
    assert abs(arrival_closure) < 2.0e-14
    assert abs(ramo_old_closure) > 1.0e-3
    assert abs(normalized_old_closure) > 1.0e-3

    print()
    print(
        "PASS: arrival flux, raw induced current, and DC-normalized terminal "
        "current are distinct observables.  The arrival field obeys the "
        "three-color exponential law; planar raw Shockley-Ramo current instead "
        "obeys an exact four-color first-difference closure."
    )


if __name__ == "__main__":
    main()
