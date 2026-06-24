"""Filter kernels and spectral transfer functions.

The filter scale ``ell`` is the FULL filter width (Pope convention). Real-space weights are
unnormalized; the filtering routines divide by the running measure-weighted sum.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TopHatKernel:
    """Box filter: unit weight for ``d <= ell/2``. Not supported for spectral filtering (rings)."""


@dataclass(frozen=True)
class GaussianKernel:
    """``G(d) ∝ exp(-alpha (d/ell)^2)``. alpha=6 (Pope, default), alpha=4 (FlowSieve)."""

    alpha: float = 6.0


@dataclass(frozen=True)
class SharpSpectralKernel:
    """Ideal low-pass: ``Ĝ(k) = 1`` for ``k <= pi/ell`` else 0."""


def kernel_weight(kernel, d, ell):  # noqa: ANN001
    """Unnormalized real-space kernel weight at distance ``d`` for width ``ell``."""
    raise NotImplementedError


def kernel_radius(kernel, ell):  # noqa: ANN001
    """Distance beyond which the kernel weight is negligible (footprint truncation radius)."""
    raise NotImplementedError


def spectral_transfer(kernel, kmag, ell):  # noqa: ANN001
    """Isotropic spectral transfer Ĝ(|k|, ell), normalized to 1 at k=0. Shared by all backends.

    For spherical harmonics pass the degree-``l`` wavenumber ``kmag = sqrt(l(l+1)) / R``.
    """
    raise NotImplementedError
