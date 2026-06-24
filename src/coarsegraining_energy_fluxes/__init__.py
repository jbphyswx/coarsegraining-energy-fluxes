"""coarsegraining_energy_fluxes — spatial coarse-graining of cross-scale energy fluxes.

A NumPy / Dask / xarray toolkit for Aluie/FlowSieve-style coarse-graining diagnostics. Current
module layout:

    geometry     coordinate systems (Cartesian, spherical) + planetary-Cartesian transforms
    grids        structured / curvilinear / unstructured grids with land masks
    kernels      filter kernels (top-hat, Gaussian, sharp-spectral) + spectral transfer Ĝ(k)
    filtering    real-space footprint convolution + spectral (FFT / NUFFT / SHT) filtering
    derivatives  finite-difference stencils (2D/3D Cartesian, spherical with curvature)
    diagnostics  energy flux Π, filtering spectrum, stress / Helmholtz / tracer decompositions
    pipeline     high-level `coarse_grain` orchestration across scales

A Julia sibling (`CoarseGrainingEnergyFluxes.jl`) exists as prior art and a useful reference; this
package is free to diverge where the Python ecosystem (Dask, xarray, existing libraries) suggests a
better design.

STATUS: scaffolding only — APIs are declared but not yet implemented (see TODO.md).
"""

from __future__ import annotations

__version__ = "0.0.1"

__all__ = [
    "__version__",
]
