#!/usr/bin/env python3
"""Small dependency-free validator for local GitHub profile assets and README."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = (ROOT / "assets/hero-dark.svg", ROOT / "assets/hero-light.svg")

def check() -> list[str]:
    errors = []
    if not README.is_file():
        return ["Missing README.md"]
    text = README.read_text(encoding="utf-8")
    if not text.startswith("<!--") or "Krishna" not in text:
        errors.append("Profile identity missing or README header changed")
    for asset in ASSETS:
        if not asset.is_file():
            errors.append(f"Missing {asset.relative_to(ROOT)}")
            continue
        try:
            svg = ET.parse(asset).getroot()
            if not svg.tag.endswith("svg"):
                errors.append(f"{asset.name}: root is not SVG")
            title = svg.find("{http://www.w3.org/2000/svg}title")
            if title is None or not (title.text or "").strip():
                errors.append(f"{asset.name}: missing accessible title")
        except ET.ParseError as exc:
            errors.append(f"{asset.name}: malformed XML ({exc})")
    for target in re.findall(r"(?:src|srcset)=[\"'](\./[^\"']+)[\"']", text):
        target_path = ROOT / target.removeprefix("./")
        if not target_path.is_file():
            errors.append(f"Broken local image path: {target}")
    for target in re.findall(r"!\[[^]]*\]\((\./[^)]+)\)", text):
        if not (ROOT / target.removeprefix("./")).is_file():
            errors.append(f"Broken local Markdown image path: {target}")
    if "<script" in text.lower() or "<iframe" in text.lower():
        errors.append("README contains unsupported script or iframe element")
    return errors

if __name__ == "__main__":
    problems = check()
    for problem in problems:
        print("ERROR:", problem)
    if problems:
        sys.exit(1)
    print("Profile validation passed: README image references and SVG XML")
