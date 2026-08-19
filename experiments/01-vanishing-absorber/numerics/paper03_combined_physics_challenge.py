"""Paper 03 combined-physics blind-challenge seed.

Stage A only: reuse the checked 2-D electrostatic / Shockley-Ramo geometry from
``realistic_geometry_closure_stress.py`` and add stochastic diffusion plus an
optional exponential recombination hazard.  This file is deliberately *not* a
self-consistent semiconductor Poisson/drift-diffusion solver.  Stage B of the
predeclared challenge will add that separately after this recovery layer is
numerically locked.

The forward generator and blind analysis are kept as separate functions.  The
blind analysis receives only complex spectral/RF currents; it never receives
D, tau, trajectory fates, fields, or mechanism labels.

The smoke mode is a reproducibility/invariant gate, not a precision science
run.  Monte-Carlo disagreement is reported explicitly and the output remains
``science_interpretation_ready = false`` until a separately documented
particle/step convergence study is passed.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.interpolate import CubicSpline

import realistic_geometry_closure_stress as base


@dataclass(frozen=True)
class StochasticConfig:
    diffusion_m2_s: float
    lifetime_s: float
    particles_per_source: int
    seed: int
    ds_um: float
    nx: int
    nz: int
    nx_src: int
    nz_src: int
    rms_diffusion_step_um: float = 0.070
    max_time_s: float = 5.0e-9
    max_steps: int = 20000


@dataclass
class PathResult:
    H: np.ndarray
    time_s: float
    fate: str
    endpoint_ramo_error: float


def _reflect(value: float, lo: float, hi: float) -> float:
    """Reflect a coordinate into [lo, hi] without an artificial absorbing wall."""
    if hi <= lo:
        raise ValueError("invalid reflection interval")
    width = hi - lo
    y = (value - lo) % (2.0 * width)
    if y > width:
        y = 2.0 * width - y
    return lo + y


def _safe_metric_dict(m: dict[str, Any]) -> dict[str, Any]:
    """Convert the checked hierarchy metric record to JSON-safe scalars."""
    return {
        "frequency_hz": float(m["f"]),
        "closure4_real": float(m["c4"].real),
        "closure4_imag": float(m["c4"].imag),
        "closure4_phase_deg": float(np.degrees(m["c4"].imag)),
        "closure5_real": float(m["c5"].real),
        "closure5_imag": float(m["c5"].imag),
        "sigma2_over_sigma1": float(m["s21"]),
        "sigma3_over_sigma2": float(m["s32"]),
        "rank2_3sigma_current_step_snr_db": float(m["snr3"]),
        "root_sum_real_per_m": float(m["rsum"].real),
        "root_sum_imag_per_m": float(m["rsum"].imag),
        "recurrence_relative_residual": float(m["recurrence"]),
    }


def blind_analysis(currents: np.ndarray) -> dict[str, Any]:
    """Analyze currents without access to the generating physics.

    This is intentionally thin: it delegates to the already checked hierarchy
    diagnostics and serializes their outputs.  No mechanism label, field,
    diffusion coefficient, lifetime, or trajectory history is accepted.
    """
    J = np.asarray(currents, dtype=complex)
    if J.shape != (len(base.FREQUENCIES), len(base.DEPTHS)):
        raise ValueError(
            f"expected {(len(base.FREQUENCIES), len(base.DEPTHS))}, got {J.shape}"
        )
    if not np.all(np.isfinite(J.real)) or not np.all(np.isfinite(J.imag)):
        raise ValueError("non-finite synthetic current supplied to blind analysis")
    return {"metrics": [_safe_metric_dict(m) for m in base.metrics(J)]}


def stochastic_path(
    g: dict[str, Any],
    x0_um: float,
    z0_um: float,
    cfg: StochasticConfig,
    rng: np.random.Generator,
) -> PathResult:
    """Euler-Maruyama path with exact discrete weighting-potential increments.

    Transport boundary rules for this Stage-A stress are explicit:

    * selected top contact: absorbing / collected;
    * bottom contact: absorbing / opposite-contact loss;
    * uncontacted top surface: reflecting;
    * lateral sidewalls: reflecting.

    Recombination terminates the path at its actual weighting potential.  The
    DC Ramo invariant is therefore phi_end - phi_start, not automatically
    1 - phi_start.
    """
    D = float(cfg.diffusion_m2_s)
    tau = float(cfg.lifetime_s)
    if D < 0:
        raise ValueError("diffusion coefficient must be nonnegative")
    if not (np.isinf(tau) or tau > 0):
        raise ValueError("lifetime must be positive or infinity")

    xs, zs = g["xs"], g["zs"]
    x = float(x0_um * 1e-6)
    z = float(z0_um * 1e-6)
    L = float(zs[-1])
    half = float(g["s"].contact_fraction * (xs[-1] - xs[0]) / 2.0)
    omega = 2.0 * np.pi * base.FREQUENCIES

    phi0 = phi = base.interp(g, "pw", x, z)
    H = np.zeros(len(base.FREQUENCIES), dtype=complex)
    t = 0.0
    fate = "stalled"
    ds = float(cfg.ds_um * 1e-6)
    rms_target = float(cfg.rms_diffusion_step_um * 1e-6)

    for _ in range(cfg.max_steps):
        if t >= cfg.max_time_s:
            fate = "time_limit"
            break

        gx = base.interp(g, "dVdx", x, z)
        gz = base.interp(g, "dVdz", x, z)
        vx, vz, speed = base.velocity(gx, gz)
        if speed < 1.0 and D == 0.0:
            fate = "stalled"
            break

        # Drift-controlled step, with a diffusion RMS cap when D > 0.
        dt_drift = ds / max(speed, 1.0)
        dt = min(dt_drift, cfg.max_time_s - t)
        if D > 0.0:
            dt_diff = rms_target**2 / (2.0 * D)
            dt = min(dt, dt_diff)
        if dt <= 0.0:
            fate = "time_limit"
            break

        # Sample an exponential recombination clock inside the present step.
        recombines = False
        if np.isfinite(tau):
            t_recomb = -tau * np.log(max(rng.random(), np.finfo(float).tiny))
            if t_recomb < dt:
                dt = t_recomb
                recombines = True

        sigma = np.sqrt(2.0 * D * dt) if D > 0.0 else 0.0
        dx_b, dz_b = (rng.normal(0.0, sigma, 2) if sigma > 0.0 else (0.0, 0.0))
        xn = x + vx * dt + dx_b
        zn = z + vz * dt + dz_b

        # Reflect lateral walls before deciding the top-contact fate.
        xn = _reflect(float(xn), float(xs[0]), float(xs[-1]))

        terminal = None
        if zn <= 0.0:
            zn = 0.0
            terminal = "bottom_contact"
        elif zn >= L:
            if abs(xn) <= half + 1e-15:
                zn = L
                terminal = "selected_contact"
            else:
                zn = _reflect(float(zn), 0.0, L)

        phin = base.interp(g, "pw", xn, zn)
        if terminal == "selected_contact":
            # Enforce the exact selected-electrode Dirichlet endpoint.
            phin = 1.0
        elif terminal == "bottom_contact":
            phin = 0.0

        H += (phin - phi) * np.exp(-1j * omega * (t + 0.5 * dt))
        x, z, phi, t = float(xn), float(zn), float(phin), t + dt

        if terminal is not None:
            fate = terminal
            break
        if recombines:
            fate = "recombined"
            break
    else:
        fate = "step_limit"

    ramo_error = float(abs(H[0] - (phi - phi0)))
    return PathResult(H=H, time_s=t, fate=fate, endpoint_ramo_error=ramo_error)


def _ensemble_transfer(
    g: dict[str, Any],
    x0_um: float,
    z0_um: float,
    cfg: StochasticConfig,
    rng: np.random.Generator,
) -> tuple[np.ndarray, dict[str, Any]]:
    H = np.zeros(len(base.FREQUENCIES), dtype=complex)
    fates: dict[str, int] = {}
    t_sum = 0.0
    max_ramo_error = 0.0

    for _ in range(cfg.particles_per_source):
        p = stochastic_path(g, x0_um, z0_um, cfg, rng)
        H += p.H
        fates[p.fate] = fates.get(p.fate, 0) + 1
        t_sum += p.time_s
        max_ramo_error = max(max_ramo_error, p.endpoint_ramo_error)

    n = cfg.particles_per_source
    return H / n, {
        "fates": fates,
        "mean_time_s": t_sum / n,
        "max_endpoint_ramo_error": max_ramo_error,
    }


def stochastic_currents(
    scenario: base.Scenario,
    cfg: StochasticConfig,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Generate spectral/RF currents from hidden stochastic forward physics."""
    if cfg.diffusion_m2_s == 0.0 and np.isinf(cfg.lifetime_s):
        # The recovery limit is the already checked deterministic implementation,
        # not a second approximately equivalent trajectory integrator.
        J, d = base.currents(
            scenario,
            nx=cfg.nx,
            nz=cfg.nz,
            nx_src=cfg.nx_src,
            nz_src=cfg.nz_src,
            ds_um=cfg.ds_um,
        )
        return J, {
            "mode": "checked_deterministic_recovery",
            "sampled_path_fates": {"selected_contact": int(cfg.nx_src * cfg.nz_src)},
            "max_endpoint_ramo_error": float(d["dc_error"]),
            "mean_time_s": None,
            "deterministic_diagnostics": {
                "collected": float(d["collected"]),
                "dc_error": float(d["dc_error"]),
                "tmax_s": float(d["tmax"]),
            },
        }

    g = base.geometry(scenario, cfg.nx, cfg.nz)
    x, wx = base.gauss(-base.X_EXTENT_UM, base.X_EXTENT_UM, cfg.nx_src)
    beam = np.exp(-0.5 * (x / base.X_SIGMA_UM) ** 2)
    beam /= np.sum(wx * beam)
    zsrc = np.linspace(0.01, base.L_UM - 0.01, cfg.nz_src)
    transfer = np.zeros(
        (cfg.nx_src, cfg.nz_src, len(base.FREQUENCIES)), dtype=complex
    )

    rng = np.random.default_rng(cfg.seed)
    fate_counts: dict[str, int] = {}
    max_ramo_error = 0.0
    time_sum = 0.0
    ensembles = 0

    for ix, x0 in enumerate(x):
        for iz, z0 in enumerate(zsrc):
            H, diag = _ensemble_transfer(g, float(x0), float(z0), cfg, rng)
            transfer[ix, iz] = H
            for name, count in diag["fates"].items():
                fate_counts[name] = fate_counts.get(name, 0) + int(count)
            max_ramo_error = max(max_ramo_error, diag["max_endpoint_ramo_error"])
            time_sum += diag["mean_time_s"]
            ensembles += 1

    mask = (base.OPT_Z_UM >= zsrc[0]) & (base.OPT_Z_UM <= zsrc[-1])
    zd = base.OPT_Z_UM[mask]
    J = np.zeros((len(base.FREQUENCIES), len(base.DEPTHS)), dtype=complex)
    for ix in range(cfg.nx_src):
        for jf in range(len(base.FREQUENCIES)):
            Hz = CubicSpline(zsrc, transfer[ix, :, jf])(zd)
            for m, row in enumerate(base.OPTICS):
                J[jf, m] += (
                    wx[ix]
                    * beam[ix]
                    * np.trapezoid(row[3][mask] * Hz, zd)
                )

    total_paths = cfg.nx_src * cfg.nz_src * cfg.particles_per_source
    return J, {
        "mode": "stochastic_stage_A",
        "sampled_path_fates": fate_counts,
        "sampled_path_fractions": {
            k: float(v / total_paths) for k, v in sorted(fate_counts.items())
        },
        "max_endpoint_ramo_error": float(max_ramo_error),
        "mean_source_ensemble_time_s": float(time_sum / max(ensembles, 1)),
        "total_sampled_paths": int(total_paths),
    }


def _complex_array_json(a: np.ndarray) -> dict[str, Any]:
    a = np.asarray(a, dtype=complex)
    return {"real": a.real.tolist(), "imag": a.imag.tolist()}


def _step_disagreement(a: np.ndarray, b: np.ndarray) -> float:
    """Replica disagreement normalized to the spectral first-difference scale."""
    da = np.diff(a, axis=1)
    db = np.diff(b, axis=1)
    mean_d = 0.5 * (da + db)
    denom = np.linalg.norm(mean_d)
    return float(np.linalg.norm(da - db) / max(denom, np.finfo(float).tiny))


def run(mode: str) -> dict[str, Any]:
    scenario = next(s for s in base.SCENARIOS if s.name == "finite75_depletion")

    if mode == "smoke":
        common = dict(
            particles_per_source=24,
            ds_um=0.050,
            nx=81,
            nz=61,
            nx_src=5,
            nz_src=17,
            rms_diffusion_step_um=0.080,
            max_time_s=5.0e-9,
            max_steps=12000,
        )
    elif mode == "production":
        common = dict(
            particles_per_source=128,
            ds_um=0.030,
            nx=121,
            nz=91,
            nx_src=7,
            nz_src=25,
            rms_diffusion_step_um=0.050,
            max_time_s=5.0e-9,
            max_steps=20000,
        )
    else:
        raise ValueError(mode)

    deterministic = StochasticConfig(
        diffusion_m2_s=0.0,
        lifetime_s=float("inf"),
        seed=1001,
        **common,
    )
    diffusion_a = StochasticConfig(
        diffusion_m2_s=2.5e-3,
        lifetime_s=float("inf"),
        seed=2001,
        **common,
    )
    diffusion_b = StochasticConfig(
        diffusion_m2_s=2.5e-3,
        lifetime_s=float("inf"),
        seed=2002,
        **common,
    )
    combined = StochasticConfig(
        diffusion_m2_s=2.5e-3,
        lifetime_s=5.0e-9,
        seed=3001,
        **common,
    )

    J0, d0 = stochastic_currents(scenario, deterministic)
    Ja, da = stochastic_currents(scenario, diffusion_a)
    Jb, db = stochastic_currents(scenario, diffusion_b)
    Jc, dc = stochastic_currents(scenario, combined)
    Jdiff = 0.5 * (Ja + Jb)

    replica_disagreement = _step_disagreement(Ja, Jb)

    # Invariant gates only.  The smoke calculation is intentionally not a
    # precision closure result, so no small-phase scientific threshold is
    # asserted here.
    assert d0["deterministic_diagnostics"]["collected"] == 1.0
    assert d0["max_endpoint_ramo_error"] < 1e-12
    assert da["max_endpoint_ramo_error"] < 1e-12
    assert db["max_endpoint_ramo_error"] < 1e-12
    assert dc["max_endpoint_ramo_error"] < 1e-12
    assert np.all(np.isfinite(Ja.real)) and np.all(np.isfinite(Ja.imag))
    assert np.all(np.isfinite(Jc.real)) and np.all(np.isfinite(Jc.imag))
    assert np.isfinite(replica_disagreement)

    # Keep numerical diagnostics and blind outputs physically separated.
    result = {
        "schema": "paper03-combined-physics-stageA-v1",
        "mode": mode,
        "scenario": {
            "name": scenario.name,
            "contact_fraction": scenario.contact_fraction,
            "depletion_width_um": scenario.depletion_width_um,
            "space_charge_drop_v": scenario.space_charge_drop_v,
        },
        "frequencies_hz": base.FREQUENCIES.tolist(),
        "generation_depth_means_um": base.DEPTHS.tolist(),
        "wavelengths_um": base.WAVELENGTHS.tolist(),
        "forward_hidden": {
            "deterministic": {
                "config": asdict(deterministic),
                "diagnostics": d0,
            },
            "diffusion_replica_a": {
                "config": asdict(diffusion_a),
                "diagnostics": da,
            },
            "diffusion_replica_b": {
                "config": asdict(diffusion_b),
                "diagnostics": db,
            },
            "diffusion_plus_recombination": {
                "config": asdict(combined),
                "diagnostics": dc,
            },
            "diffusion_replica_first_difference_disagreement": replica_disagreement,
        },
        "synthetic_currents": {
            "deterministic": _complex_array_json(J0),
            "diffusion_replica_mean": _complex_array_json(Jdiff),
            "diffusion_plus_recombination": _complex_array_json(Jc),
        },
        "blind_outputs": {
            "deterministic": blind_analysis(J0),
            "diffusion_replica_mean": blind_analysis(Jdiff),
            "diffusion_plus_recombination": blind_analysis(Jc),
        },
        "gate": {
            "deterministic_recovery_delegates_to_checked_solver": True,
            "dc_endpoint_ramo_invariant_passed": True,
            "fixed_seed_reproducibility_enabled": True,
            "particle_replica_disagreement_reported": True,
            "science_interpretation_ready": False,
            "reason": (
                "Stage-A smoke/seed run only; particle-count and step-size "
                "convergence must be demonstrated before closure-scale effects "
                "are interpreted, and Stage B self-consistent semiconductor "
                "Poisson/drift-diffusion is not yet implemented."
            ),
        },
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("smoke", "production"),
        default="smoke",
        help="smoke is an invariant gate; production only increases sampling",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("paper03_combined_physics_stageA.json"),
    )
    args = parser.parse_args()

    result = run(args.mode)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=True) + "\n")

    fwd = result["forward_hidden"]
    print("Paper 03 Stage-A combined-physics seed")
    print(f"mode={args.mode}")
    print(
        "diffusion replica first-difference disagreement = "
        f"{fwd['diffusion_replica_first_difference_disagreement']:.6g}"
    )
    for key in ("diffusion_replica_a", "diffusion_replica_b", "diffusion_plus_recombination"):
        d = fwd[key]["diagnostics"]
        print(
            f"{key}: paths={d['total_sampled_paths']}, "
            f"fates={d['sampled_path_fractions']}, "
            f"max DC endpoint-Ramo error={d['max_endpoint_ramo_error']:.3e}"
        )
    print("science_interpretation_ready = false")
    print(f"wrote {args.output}")
    print("PASS: Stage-A invariants passed; no scientific convergence claim made.")


if __name__ == "__main__":
    main()
