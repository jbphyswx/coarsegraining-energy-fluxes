"""Coordinate systems and metric helpers.

Cartesian and spherical geometries, great-circle distance, cell-area elements, and the
local↔planetary-Cartesian velocity transforms used for commuting filtering with ∇ on the sphere
(Aluie 2019).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class CartesianGeometry:
    """Uniform Cartesian geometry with cell spacings (m)."""

    dx: float
    dy: float
    dz: float = 0.0


@dataclass(frozen=True)
class SphericalGeometry:
    """Spherical geometry on a sphere of radius ``R`` (m)."""

    R: float = 6.371e6


def distance(geometry, p1, p2):  # noqa: ANN001
    """Distance between two points (Euclidean for Cartesian, great-circle for spherical)."""
    raise NotImplementedError


def area_element(geometry, lat: float | None = None, dlon: float = 0.0, dphi: float = 0.0) -> float:
    """Cell area (Cartesian) / latitude-dependent area (spherical)."""
    raise NotImplementedError


def to_planetary_cartesian(geometry, u, v, w, lon, lat):  # noqa: ANN001
    """Local (east, north, up) velocity → global planetary-Cartesian (X, Y, Z)."""
    raise NotImplementedError


def from_planetary_cartesian(geometry, ux, uy, uz, lon, lat):  # noqa: ANN001
    """Global planetary-Cartesian (X, Y, Z) velocity → local (east, north, up)."""
    raise NotImplementedError
