"""Energy-flux diagnostics.

Cross-scale kinetic-energy flux Π, the filtering spectrum (Sadek & Aluie 2018), and the stress /
Helmholtz / tracer decompositions.
"""

from __future__ import annotations

import numpy as np


def compute_pi(u, v, w, grid, kernel, scale, *, rho0=1025.0, mask_strategy="deformable"):  # noqa: ANN001
    """Cross-scale KE flux Π = -ρ₀ S̄_ij τ_ij at scale ``scale`` (2D, or 3D Cartesian when ``w`` given)."""
    raise NotImplementedError


def cumulative_energy(u, v, w, grid, kernel, scales, *, rho0=1025.0):  # noqa: ANN001
    """Cumulative coarse KE E(ℓ) = ½ρ₀⟨|ū_ℓ|²⟩ per scale (Sadek & Aluie Eq. 15)."""
    raise NotImplementedError


def filtering_spectrum(u, v, w, grid, kernel, scales, *, rho0=1025.0, length=1.0):  # noqa: ANN001
    """Filtering spectral density Ẽ(k_ℓ) = dE/dk_ℓ, k_ℓ = L/ℓ (Eq. 14). Returns (k_ℓ, Ẽ)."""
    raise NotImplementedError


def tau_decomposition(u, v, grid, kernel, scale):  # noqa: ANN001
    """Germano Leonard/Cross/Reynolds split of the subfilter stress (L + C + R = τ)."""
    raise NotImplementedError


def compute_pi_decomposed(u, v, u_rot, v_rot, grid, kernel, scale, *, rho0=1025.0):  # noqa: ANN001
    """Rotational/divergent (Helmholtz) split: Π = Π_rotational + Π_cross + Π_divergent."""
    raise NotImplementedError


def tracer_variance_flux(u, v, theta, grid, kernel, scale):  # noqa: ANN001
    """Cross-scale tracer-variance flux Πθ = -∂_jθ̄ · τ_j(u, θ) (buoyancy ⇒ APE transfer)."""
    raise NotImplementedError
