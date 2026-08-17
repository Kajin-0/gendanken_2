"""Paper-02 parameter sweep for multidimensional Shockley-Ramo geometry.

This script extends realistic_geometry_closure_stress.py without changing its
physics.  It sweeps finite-contact/depletion geometry plus lateral illumination
coordinates and records whether a geometry-generated four-color phase signature
is accompanied by a resolvable higher spatial mode before the reference
transport-gradient claim reaches its required SNR.

This is a conditional geometry stress study, not a calibrated detector model
and not a novelty claim.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline

import realistic_geometry_closure_stress as base


def currents_with_beam(
    scenario: base.Scenario,
    beam_sigma_um: float,
    beam_center_um: float,
    *,
    nx: int,
    nz: int,
    nx_src: int,
    nz_src: int,
    ds_um: float,
):
    """Evaluate the six-channel current for a laterally shifted Gaussian beam.

    The integration support remains the same finite interval used by the
    baseline calculation; the Gaussian is renormalized on that support.
    """
    g = base.geometry(scenario, nx=nx, nz=nz)

    x, wx = base.gauss(-base.X_EXTENT_UM, base.X_EXTENT_UM, nx_src)
    beam = np.exp(-0.5 * ((x - beam_center_um) / beam_sigma_um) ** 2)
    beam /= np.sum(wx * beam)

    zsrc = np.linspace(0.01, base.L_UM - 0.01, nz_src)
    transfer = np.zeros(
        (nx_src, nz_src, len(base.FREQUENCIES)),
        dtype=complex,
    )

    collected = 0
    dc_error = 0.0
    tmax = 0.0

    for ix, x0 in enumerate(x):
        for iz, z0 in enumerate(zsrc):
            H, t, ok, phi0 = base.trajectory(g, x0, z0, ds_um=ds_um)
            transfer[ix, iz] = H
            collected += int(ok)
            dc_error = max(dc_error, abs(H[0].real - (1.0 - phi0)))
            tmax = max(tmax, t)

    mask = (base.OPT_Z_UM >= zsrc[0]) & (base.OPT_Z_UM <= zsrc[-1])
    zd = base.OPT_Z_UM[mask]

    J = np.zeros(
        (len(base.FREQUENCIES), len(base.DEPTHS)),
        dtype=complex,
    )

    for ix in range(nx_src):
        for jf in range(len(base.FREQUENCIES)):
            Hz = CubicSpline(zsrc, transfer[ix, :, jf])(zd)
            for m, row in enumerate(base.OPTICS):
                J[jf, m] += (
                    wx[ix]
                    * beam[ix]
                    * np.trapezoid(row[3][mask] * Hz, zd)
                )

    diagnostics = {
        "collected": collected / (nx_src * nz_src),
        "dc_error": dc_error,
        "tmax_s": tmax,
    }
    return J, diagnostics


def grid_for_tier(tier: str):
    """Return a deliberately bounded first sweep.

    The quick tier is suitable for regression/iteration.  The broad tier is
    intended for the paper-development run after the quick tier is stable.
    """
    if tier == "quick":
        return {
            "contact_fraction": [0.75, 0.50],
            "depletion_width_um": [0.0, 3.0],
            "space_charge_drop_v": [0.05],
            "beam_sigma_um": [2.0],
            "beam_center_um": [0.0, 1.0],
        }

    if tier == "broad":
        return {
            "contact_fraction": [0.875, 0.75, 0.625, 0.50],
            "depletion_width_um": [0.0, 1.5, 3.0, 4.5],
            "space_charge_drop_v": [0.025, 0.05, 0.075],
            "beam_sigma_um": [1.0, 2.0, 3.0],
            "beam_center_um": [0.0, 0.75, 1.50],
        }

    raise ValueError(f"unknown tier {tier!r}")


def geometry_cases(grid):
    for fc in grid["contact_fraction"]:
        for wd in grid["depletion_width_um"]:
            drops = [0.0] if wd == 0.0 else grid["space_charge_drop_v"]
            for vsc in drops:
                yield base.Scenario(
                    name=f"fc{fc:.3f}_wd{wd:.3f}_vsc{vsc:.3f}",
                    contact_fraction=float(fc),
                    depletion_width_um=float(wd),
                    space_charge_drop_v=float(vsc),
                )


def metric_rows(
    scenario,
    diag,
    metrics,
    planar_metrics,
    beam_sigma_um,
    beam_center_um,
):
    rows = []
    contact_half_width_um = scenario.contact_fraction * base.WIDTH_UM / 2.0

    for m, p in zip(metrics, planar_metrics):
        f = float(m["f"])
        if f <= 0:
            continue

        phase_deg = float(np.degrees(m["c4"].imag))
        planar_phase_deg = float(np.degrees(p["c4"].imag))
        excess_deg = phase_deg - planar_phase_deg

        target_deg = float(base.GRADIENT_TARGET_DEG[f])
        claim_snr_db = float(base.GRADIENT_SNR_DB[f])
        rank2_snr_db = float(m["snr3"])
        warning_margin_db = claim_snr_db - rank2_snr_db

        rows.append(
            {
                "scenario": scenario.name,
                "frequency_hz": f,
                "contact_fraction": scenario.contact_fraction,
                "depletion_width_um": scenario.depletion_width_um,
                "depletion_fraction": scenario.depletion_width_um / base.L_UM,
                "space_charge_drop_v": scenario.space_charge_drop_v,
                "space_charge_ratio": (
                    scenario.space_charge_drop_v / base.V_BIAS
                    if base.V_BIAS != 0
                    else np.nan
                ),
                "beam_sigma_um": beam_sigma_um,
                "beam_center_um": beam_center_um,
                "beam_width_ratio": beam_sigma_um / contact_half_width_um,
                "beam_offset_ratio": beam_center_um / contact_half_width_um,
                "four_color_phase_deg": phase_deg,
                "planar_phase_deg": planar_phase_deg,
                "geometry_excess_deg": excess_deg,
                "transport_target_deg": target_deg,
                "mimic_ratio": abs(excess_deg / target_deg),
                "sigma2_over_sigma1": float(m["s21"]),
                "sigma3_over_sigma2": float(m["s32"]),
                "rank2_3sigma_snr_db": rank2_snr_db,
                "transport_claim_snr_db": claim_snr_db,
                "warning_margin_db": warning_margin_db,
                "root_sum_imag_per_um": float(m["rsum"].imag / 1e6),
                "rank2_recurrence_relative_error": float(m["recurrence"]),
                "collected_fraction": float(diag["collected"]),
                "dc_ramo_error": float(diag["dc_error"]),
                "max_trajectory_ps": float(1e12 * diag["tmax_s"]),
            }
        )

    return rows


def summarize(rows):
    if not rows:
        return {}

    mimic = np.asarray([r["mimic_ratio"] for r in rows], dtype=float)
    margin = np.asarray([r["warning_margin_db"] for r in rows], dtype=float)

    order_one = mimic >= 0.5
    hidden = order_one & (margin <= 0.0)

    summary = {
        "n_frequency_rows": int(len(rows)),
        "n_order_one_rows_mimic_ge_0p5": int(np.sum(order_one)),
        "n_hidden_risk_rows_order_one_and_no_early_rank2_warning": int(
            np.sum(hidden)
        ),
        "max_mimic_ratio": float(np.nanmax(mimic)),
        "median_mimic_ratio": float(np.nanmedian(mimic)),
        "min_warning_margin_db": float(np.nanmin(margin)),
        "max_warning_margin_db": float(np.nanmax(margin)),
    }

    if np.any(order_one):
        om = margin[order_one]
        summary.update(
            {
                "order_one_fraction_with_positive_warning_margin": float(
                    np.mean(om > 0.0)
                ),
                "order_one_min_warning_margin_db": float(np.nanmin(om)),
                "order_one_median_warning_margin_db": float(np.nanmedian(om)),
                "order_one_max_warning_margin_db": float(np.nanmax(om)),
            }
        )

    return summary


def run(args):
    grid = grid_for_tier(args.tier)
    base.V_BIAS = float(args.bias_v)
    base.X_EXTENT_UM = float(args.x_extent_um)

    numerical = {
        "nx": args.nx,
        "nz": args.nz,
        "nx_src": args.nx_src,
        "nz_src": args.nz_src,
        "ds_um": args.ds_um,
    }

    rows = []
    planar_cache = {}

    for sigma in grid["beam_sigma_um"]:
        for center in grid["beam_center_um"]:
            beam_key = (float(sigma), float(center))
            planar = base.Scenario(
                name="planar",
                contact_fraction=1.0,
                depletion_width_um=0.0,
                space_charge_drop_v=0.0,
            )
            Jp, dp = currents_with_beam(
                planar,
                sigma,
                center,
                **numerical,
            )
            planar_cache[beam_key] = (dp, base.metrics(Jp))

    cases = list(geometry_cases(grid))
    total = len(cases) * len(grid["beam_sigma_um"]) * len(
        grid["beam_center_um"]
    )
    done = 0

    for scenario in cases:
        for sigma in grid["beam_sigma_um"]:
            for center in grid["beam_center_um"]:
                done += 1
                print(
                    f"[{done:4d}/{total:4d}] {scenario.name} "
                    f"sigma={sigma:.3f} um center={center:.3f} um",
                    flush=True,
                )
                J, diag = currents_with_beam(
                    scenario,
                    sigma,
                    center,
                    **numerical,
                )
                M = base.metrics(J)
                _, Mp = planar_cache[(float(sigma), float(center))]
                rows.extend(
                    metric_rows(
                        scenario,
                        diag,
                        M,
                        Mp,
                        float(sigma),
                        float(center),
                    )
                )

    out_csv = Path(args.output_csv)
    out_json = Path(args.output_summary)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = list(rows[0].keys()) if rows else []
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    payload = {
        "status": "CONDITIONAL geometry stress / not calibrated device prediction",
        "tier": args.tier,
        "grid": grid,
        "numerical": numerical,
        "fixed": {
            "device_width_um": base.WIDTH_UM,
            "absorber_thickness_um": base.L_UM,
            "bias_v": base.V_BIAS,
            "x_extent_um": base.X_EXTENT_UM,
            "mu_m2_per_vs": base.MU,
            "v_sat_m_per_s": base.V_SAT,
            "frequencies_hz": [float(v) for v in base.FREQUENCIES],
        },
        "summary": summarize(rows),
    }

    with out_json.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)

    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    print(f"wrote {out_csv}")
    print(f"wrote {out_json}")


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--tier", choices=("quick", "broad"), default="quick")
    p.add_argument("--bias-v", type=float, default=0.30)
    p.add_argument("--x-extent-um", type=float, default=3.5)

    p.add_argument("--nx", type=int, default=81)
    p.add_argument("--nz", type=int, default=61)
    p.add_argument("--nx-src", type=int, default=9)
    p.add_argument("--nz-src", type=int, default=31)
    p.add_argument("--ds-um", type=float, default=0.035)

    p.add_argument(
        "--output-csv",
        default="paper02_geometry_parameter_sweep.csv",
    )
    p.add_argument(
        "--output-summary",
        default="paper02_geometry_parameter_sweep_summary.json",
    )
    return p


if __name__ == "__main__":
    run(parser().parse_args())
