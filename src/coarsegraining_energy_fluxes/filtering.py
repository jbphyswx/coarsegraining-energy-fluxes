"""Filtering engine.

Two methods:

* ``"direct"`` — real-space footprint convolution. Supports land masks, regional/non-periodic
  domains, arbitrary scales. Mask strategies: ``"deformable"`` (renormalize over wet points) or
  ``"zerofill"`` (treat land as 0).
* ``"spectral"`` — transform → multiply by ``spectral_transfer`` → inverse transform. Assumes a
  homogeneous (periodic/global) domain, no mask. Backend chosen by grid type:
  FFT (uniform Cartesian), NUFFT (scattered Cartesian), spherical-harmonic (uniform/scattered sphere).

NumPy is the reference backend; Dask provides chunked/out-of-core execution over batch dimensions.
"""

from __future__ import annotations

import numpy as np


def filter_field(field, grid, kernel, scale, *, method="direct", mask_strategy="deformable"):  # noqa: ANN001
    """Filter a single field at one scale; returns the coarse-grained field (same shape)."""
    raise NotImplementedError


def filter_fields(fields, grid, kernel, scale, **kwargs):  # noqa: ANN001
    """Filter several fields sharing a grid/kernel/scale, building the footprint/plan once."""
    raise NotImplementedError


def plan_filter(grid, kernel, scale, *, method="direct", mask_strategy="deformable"):  # noqa: ANN001
    """Build a reusable filter plan (precomputed footprint, or cached transform) for one scale."""
    raise NotImplementedError


def filter_apply(out, field, plan):  # noqa: ANN001
    """Apply a prebuilt plan to a field."""
    raise NotImplementedError
