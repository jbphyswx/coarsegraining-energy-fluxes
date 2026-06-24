"""Grid types with land masks.

Structured (rectilinear, 1D/2D/3D), curvilinear, and unstructured (scattered) grids. Each carries a
geometry, coordinate axes, an N-D cell measure (length/area/volume), a boolean wet/dry mask, and
per-axis periodicity flags.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class StructuredGrid:
    """Rectilinear grid: one coordinate vector per axis + N-D measure + mask + periodicity."""

    geometry: object
    axes: tuple[np.ndarray, ...]
    measure: np.ndarray
    mask: np.ndarray
    periodic: tuple[bool, ...]


@dataclass
class CurvilinearGrid:
    """Model-native curvilinear grid (2D coordinate arrays)."""

    geometry: object
    lon: np.ndarray
    lat: np.ndarray
    areas: np.ndarray
    mask: np.ndarray


@dataclass
class UnstructuredGrid:
    """Scattered points (1D arrays of coordinates / areas / mask)."""

    geometry: object
    lon: np.ndarray
    lat: np.ndarray
    areas: np.ndarray
    mask: np.ndarray


def structured_grid(geometry, *axes, mask=None, periodic=None):  # noqa: ANN001
    """Convenience constructor: build a `StructuredGrid`, precomputing the cell measure."""
    raise NotImplementedError
