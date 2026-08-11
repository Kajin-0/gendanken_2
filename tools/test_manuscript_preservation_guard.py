#!/usr/bin/env python3
"""Self-test the manuscript preservation guard against safe and destructive edits."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
CHECKER = ROOT / "tools" / "check_manuscript_preservation.py"
EXTRACTOR = ROOT / "tools" / "extract_manuscript_baseline.py"
MANIFEST = EXP / "MANUSCRIPT_BASELINE.json"
CURRENT = EXP / "MANUSCRIPT_CURRENT.tex"


def run_checker(candidate: Path, base: Path | None = None) -> subprocess.CompletedProcess[str]:
    cmd = [
        sys.executable,
        str(CHECKER),
        "--candidate",
        str(candidate),
        "--manifest",
        str(MANIFEST),
    ]
    if base is not None:
        cmd += ["--base", str(base)]
    return subprocess.run(cmd, text=True, capture_output=True, check=False)


def report(proc: subprocess.CompletedProcess[str]) -> dict:
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(
            f"checker did not return JSON\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
        ) from exc


def main() -> int:
    subprocess.run([sys.executable, str(EXTRACTOR)], check=True)
    baseline = CURRENT.read_text(encoding="utf-8")

    # The exact extracted baseline must pass its own manifest.
    exact = run_checker(CURRENT)
    exact_report = report(exact)
    if exact.returncode != 0 or exact_report.get("result") != "PASS":
        raise SystemExit(f"exact baseline unexpectedly failed: {exact_report}")

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        # A surgical additive edit must pass.
        safe = td / "safe.tex"
        safe.write_text(
            baseline.replace(
                "\\end{document}",
                "% harmless additive manuscript note for guard self-test\n\\end{document}",
            ),
            encoding="utf-8",
        )
        safe_proc = run_checker(safe, CURRENT)
        safe_report = report(safe_proc)
        if safe_proc.returncode != 0 or safe_report.get("result") != "PASS":
            raise SystemExit(f"safe additive edit unexpectedly failed: {safe_report}")

        # Reproduce the key accidental-rewrite failure class: author replacement,
        # missing established subsection, and severe truncation.
        bad = td / "bad.tex"
        destructive = baseline.replace(
            "\\author{Terence Fisher}", "\\author{[Author]}"
        ).replace(
            "\\subsection{Two conventional carrier species}",
            "\\subsection{REMOVED BY ACCIDENT}",
        )
        lines = destructive.splitlines()
        destructive = "\n".join(lines[: int(len(lines) * 0.63)]) + "\n\\end{document}\n"
        bad.write_text(destructive, encoding="utf-8")

        bad_proc = run_checker(bad, CURRENT)
        bad_report = report(bad_proc)
        if bad_proc.returncode == 0 or bad_report.get("result") != "FAIL":
            raise SystemExit(f"destructive edit was not rejected: {bad_report}")

        errors = "\n".join(bad_report.get("errors", []))
        expected_signals = ("author changed", "missing", "line count")
        if not all(signal in errors for signal in expected_signals):
            raise SystemExit(
                "destructive edit failed, but not for all expected guard reasons: "
                + errors
            )

    print("manuscript preservation guard self-test: PASS")
    print("  exact canonical baseline: accepted")
    print("  harmless additive edit: accepted")
    print("  destructive rewrite: rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
