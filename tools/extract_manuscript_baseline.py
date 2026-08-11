#!/usr/bin/env python3
"""Extract and verify the immutable anonymous Rev. 6 manuscript baseline."""
from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
HISTORY = EXP / "manuscript_history"
PART_GLOB = "MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part*"
OUTPUT = EXP / "MANUSCRIPT_CURRENT.tex"
EXPECTED_SOURCE_SHA256 = "2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4"
EXPECTED_GZIP_SHA256 = "aa7ab9e3271599bf9cdaa5ef37618cb2b9757ee0e08c867303a83e06e61adb8e"
EXPECTED_PARTS = 6
EXPECTED_LINES = 924


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parts = sorted(HISTORY.glob(PART_GLOB))
    if len(parts) != EXPECTED_PARTS:
        raise SystemExit(
            f"Refusing extraction: expected {EXPECTED_PARTS} snapshot parts, found {len(parts)}"
        )

    encoded = "".join(part.read_text(encoding="ascii").strip() for part in parts)
    packed = base64.b64decode(encoded, validate=True)
    packed_hash = sha256(packed)
    if packed_hash != EXPECTED_GZIP_SHA256:
        raise SystemExit(
            f"Refusing extraction: gzip hash mismatch {packed_hash} != {EXPECTED_GZIP_SHA256}"
        )

    source = gzip.decompress(packed)
    source_hash = sha256(source)
    if source_hash != EXPECTED_SOURCE_SHA256:
        raise SystemExit(
            f"Refusing extraction: source hash mismatch {source_hash} != {EXPECTED_SOURCE_SHA256}"
        )

    text = source.decode("utf-8")
    lines = len(text.splitlines())
    if lines != EXPECTED_LINES:
        raise SystemExit(
            f"Refusing extraction: expected {EXPECTED_LINES} lines, recovered {lines}"
        )
    if r"\author{Anonymous}" not in text or "pdfauthor={Anonymous}" not in text:
        raise SystemExit("Refusing extraction: canonical author metadata is not anonymous")

    OUTPUT.write_bytes(source)
    print(f"Wrote verified anonymous manuscript baseline: {OUTPUT}")
    print(f"source SHA-256: {source_hash}")
    print(f"lines: {lines}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
