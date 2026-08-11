"""Minimal exactly solvable and falsifiable transport gedanken experiment.

Ideal uniform downstream conditioned drift-diffusion on a semi-infinite/local
segment:

    F(z,omega) proportional exp[gamma(omega) z]

with

    gamma = (sqrt(w^2 + 4 i D omega)-w)/(2D).

Two generation depths determine gamma from one complex response ratio. One RF
frequency then determines D and conditioned drift w exactly. A second RF
frequency has no new transport coefficient and is therefore a pure closure /
falsification measurement.

If a local Markov killing/recombination rate kappa is present before DC
conditioning, then

    w = sqrt(v^2 + 4 D kappa)
    c = d_z ln h = (w-v)/(2D)

for the simple one-exponential semi-infinite geometry. Hence one DC collection
slope c recovers

    v = w - 2 D c
    kappa = D c^2 + v c.

The numerical values below are illustrative detector-scale values, not a
calibrated HgCdTe prediction.
"""

from __future__ import annotations

import numpy as np


D_TRUE = 0.20          # m^2/s
V_TRUE = 1.00e5        # m/s
KAPPA_TRUE = 1.00e6    # 1/s
DZ = 1.00e-6           # m
FREQUENCIES_HZ = (0.50e9, 2.00e9)


def conditioned_drift(D: float, v: float, kappa: float) -> float:
    return float(np.sqrt(v * v + 4.0 * D * kappa))


def gamma(D: float, w: float, omega: float) -> complex:
    return (np.sqrt(w * w + 4j * D * omega) - w) / (2.0 * D)


def invert_gamma(g: complex, omega: float):
    a = float(g.real)
    b = float(g.imag)
    modulus2 = a * a + b * b
    D = omega * a / (b * modulus2)
    w = omega * (b * b - a * a) / (b * modulus2)
    return D, w


def main() -> None:
    w_true = conditioned_drift(D_TRUE, V_TRUE, KAPPA_TRUE)
    c_dc = (w_true - V_TRUE) / (2.0 * D_TRUE)

    inferred = []
    print("Minimal two-depth / two-frequency transport gedanken")
    print(f"true D={D_TRUE:.9f} m^2/s")
    print(f"true physical v={V_TRUE:.6f} m/s")
    print(f"true kappa={KAPPA_TRUE:.6f} 1/s")
    print(f"conditioned drift w={w_true:.9f} m/s")
    print(f"DC collection log-slope c={c_dc:.9f} 1/m")
    print()

    for f_hz in FREQUENCIES_HZ:
        omega = 2.0 * np.pi * f_hz
        g = gamma(D_TRUE, w_true, omega)

        # Response ratio for two localized generation points separated by DZ.
        ratio = np.exp(g * DZ)
        g_measured = np.log(ratio) / DZ
        D_inf, w_inf = invert_gamma(g_measured, omega)
        inferred.append((D_inf, w_inf))

        print(f"f={f_hz/1e9:.3f} GHz")
        print(
            f"  gamma = {g_measured.real:.6f} + i {g_measured.imag:.6f} 1/m"
        )
        print(
            f"  ratio amplitude={abs(ratio):.9f}, "
            f"phase={np.degrees(np.angle(ratio)):.6f} deg"
        )
        print(f"  inferred D={D_inf:.12f}, w={w_inf:.9f}")
        print(
            "  downstream sign cone 0<Re(gamma)<Im(gamma): "
            f"{0.0 < g.real < g.imag}"
        )
        print()

    inferred = np.asarray(inferred)
    D_from_rf = float(np.mean(inferred[:, 0]))
    w_from_rf = float(np.mean(inferred[:, 1]))

    # Undo the DC conditioning in the simple uniform/semi-infinite geometry.
    v_rec = w_from_rf - 2.0 * D_from_rf * c_dc
    kappa_rec = D_from_rf * c_dc**2 + v_rec * c_dc

    print("second-frequency closure")
    print(f"  Delta D = {inferred[1,0]-inferred[0,0]:.3e} m^2/s")
    print(f"  Delta w = {inferred[1,1]-inferred[0,1]:.3e} m/s")
    print()
    print("DC unconditioning")
    print(f"  recovered physical v={v_rec:.9f} m/s")
    print(f"  recovered kappa={kappa_rec:.9f} 1/s")
    print(f"  recovered lifetime={1.0/kappa_rec:.12e} s")

    assert np.max(np.abs(inferred[:, 0] - D_TRUE)) < 3.0e-13
    assert np.max(np.abs(inferred[:, 1] - w_true)) < 2.0e-8
    assert abs(v_rec / V_TRUE - 1.0) < 2.0e-13
    assert abs(kappa_rec / KAPPA_TRUE - 1.0) < 2.0e-12

    print()
    print(
        "PASS: one complex two-depth RF ratio identifies D and conditioned "
        "drift exactly in the ideal uniform model; the second RF frequency is "
        "an exact parameter-free closure test; one DC depth slope then recovers "
        "physical drift and recombination in the simple one-exponential geometry."
    )


if __name__ == "__main__":
    main()
