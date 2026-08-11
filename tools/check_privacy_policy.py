#!/usr/bin/env python3
"""Enforce pseudonymity-first canonical manuscript metadata."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
MANIFEST = EXP / "MANUSCRIPT_BASELINE.json"
CURRENT = EXP / "MANUSCRIPT_CURRENT.tex"
RELEASE = EXP / "IDENTITY_RELEASE.md"


def parse_release() -> tuple[str, str] | None:
    if not RELEASE.exists():
        return None
    text = RELEASE.read_text(encoding="utf-8")
    required = {
        "USER_EXPLICITLY_APPROVED_IDENTITY_DISCLOSURE": "true",
        "USER_REQUEST_QUOTE": None,
        "APPROVED_IDENTIFIER": None,
        "APPROVED_SCOPE": None,
    }
    values: dict[str, str] = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    if values.get("USER_EXPLICITLY_APPROVED_IDENTITY_DISCLOSURE", "").lower() != "true":
        raise SystemExit("IDENTITY_RELEASE.md missing explicit disclosure approval flag")
    for key in ("USER_REQUEST_QUOTE", "APPROVED_IDENTIFIER", "APPROVED_SCOPE"):
        if not values.get(key):
            raise SystemExit(f"IDENTITY_RELEASE.md missing {key}")
    return values["APPROVED_IDENTIFIER"], values["APPROVED_SCOPE"]


def extract_author(tex: str) -> tuple[str, str]:
    author = re.search(r"\\author\{([^}]*)\}", tex)
    pdfauthor = re.search(r"pdfauthor=\{([^}]*)\}", tex)
    if not author or not pdfauthor:
        raise SystemExit("Canonical manuscript is missing author/PDF-author metadata")
    return author.group(1).strip(), pdfauthor.group(1).strip()


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    release = parse_release()

    subprocess.run([sys.executable, str(ROOT / "tools" / "extract_manuscript_baseline.py")], cwd=ROOT, check=True)
    tex = CURRENT.read_text(encoding="utf-8")
    author, pdfauthor = extract_author(tex)

    if release is None:
        expected = "Anonymous"
        if manifest.get("privacy_default") != "anonymous":
            raise SystemExit("Manifest privacy_default must remain anonymous")
        if manifest.get("identity_release_required") is not True:
            raise SystemExit("Manifest must require identity release")
        if manifest.get("author") != expected:
            raise SystemExit("Canonical manifest author must remain Anonymous without an identity release")
        if author != expected or pdfauthor != expected:
            raise SystemExit("Canonical manuscript author metadata must remain Anonymous without an identity release")
    else:
        approved_identifier, _scope = release
        if manifest.get("author") != approved_identifier:
            raise SystemExit("Manifest author does not match the explicitly approved identifier")
        if author != approved_identifier or pdfauthor != approved_identifier:
            raise SystemExit("Manuscript author metadata does not match the explicitly approved identifier")

    # Canonical live snapshot filenames themselves must remain identity-neutral.
    history = EXP / "manuscript_history"
    expected_parts = sorted(history.glob("MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part*"))
    if release is None and len(expected_parts) != 2:
        raise SystemExit("Expected exactly two anonymous canonical snapshot parts")

    print("privacy policy check: PASS")
    print(f"canonical author metadata: {author}")
    print("identity release: present" if release else "identity release: absent; anonymous default enforced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
