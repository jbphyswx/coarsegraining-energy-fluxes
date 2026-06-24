"""Smoke tests — the package imports and exposes its module layout.

Numerical correctness tests (analytic/known cases, with optional cross-checks against the Julia
sibling) land alongside each module as it is implemented; see TODO.md.
"""

from __future__ import annotations

import importlib

import coarsegraining_energy_fluxes as cgef


def test_version() -> None:
    assert isinstance(cgef.__version__, str)


def test_modules_importable() -> None:
    for name in (
        "geometry",
        "grids",
        "kernels",
        "filtering",
        "derivatives",
        "diagnostics",
        "pipeline",
    ):
        importlib.import_module(f"coarsegraining_energy_fluxes.{name}")
