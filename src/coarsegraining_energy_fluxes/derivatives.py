"""Finite-difference stencils.

Second-order centered differences with one-sided fallback at domain edges and land cells, for 2D and
3D Cartesian grids and spherical grids (with curvature terms).
"""

from __future__ import annotations

import numpy as np


def ddx(field, grid):  # noqa: ANN001
    """∂/∂x (eastward / λ)."""
    raise NotImplementedError


def ddy(field, grid):  # noqa: ANN001
    """∂/∂y (northward / φ)."""
    raise NotImplementedError


def ddz(field, grid):  # noqa: ANN001
    """∂/∂z (vertical)."""
    raise NotImplementedError
