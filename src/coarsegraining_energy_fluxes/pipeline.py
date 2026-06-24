"""High-level orchestration.

`coarse_grain` sweeps a set of filter scales, reusing the filter plan, and returns the flux maps and
spectrum in a single result object.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class CoarseGrainResult:
    """Container for a multi-scale coarse-graining run."""

    scales: np.ndarray
    pi: list[np.ndarray]            # flux map per scale
    cumulative_energy: np.ndarray   # ½ρ₀⟨|ū_ℓ|²⟩ per scale (Eq. 15)
    wavenumber: np.ndarray          # k_ℓ = L/ℓ
    filtering_spectrum: np.ndarray  # Ẽ(k_ℓ) density (Eq. 14)


def coarse_grain(u, v, grid, *, scales, kernel=None, w=None, rho0=1025.0, length=1.0,
                 mask_strategy="deformable"):  # noqa: ANN001
    """Full coarse-graining analysis across ``scales`` → :class:`CoarseGrainResult`."""
    raise NotImplementedError
