# coarsegraining-energy-fluxes

Spatial coarse-graining (Aluie / FlowSieve-style) analysis of cross-scale energy fluxes in
geophysical fluid dynamics — a **NumPy / Dask / xarray** toolkit.

> **Status: pre-alpha scaffolding.** The package layout and public API are sketched, but the numerics
> are not yet implemented. See [TODO.md](TODO.md) for the plan.

A Julia sibling, [`CoarseGrainingEnergyFluxes.jl`](https://github.com/jbphyswx/CoarseGrainingEnergyFluxes.jl),
exists as prior art and a handy cross-reference for the physics, but this package stands on its own and
is free to diverge where the Python ecosystem suggests a better design (Dask, xarray, existing libraries).

## What it will do

Coarse-graining (spatial filtering) decomposes a turbulent flow into scale-dependent contributions
and measures the energy transferred between them. Given the filtered velocity ū_ℓ and the sub-scale
stress τ_ℓ = (u⊗u)̄_ℓ − ū_ℓ⊗ū_ℓ, the cross-scale kinetic-energy flux is

```
Π(x, ℓ) = −ρ₀ τ_ℓ : S̄_ℓ
```

(Π > 0 forward cascade, Π < 0 inverse cascade). Planned capabilities mirror the Julia package:

- cross-scale energy flux Π(x, ℓ) on Cartesian and spherical grids, with land masks;
- the **filtering spectrum** (Sadek & Aluie 2018): cumulative coarse KE E(ℓ) and density Ẽ(k_ℓ);
- decompositions: Leonard/Cross/Reynolds stress, rotational/divergent (Helmholtz) flux, and the
  tracer/buoyancy-variance flux;
- top-hat / Gaussian / sharp-spectral kernels;
- real-space (direct-sum) filtering with deformable or zero-fill masking, and spectral filtering
  (FFT for uniform Cartesian; NUFFT and spherical-harmonic transforms as optional extras);
- **NumPy** reference backend, **Dask** for chunked / out-of-core batches, **xarray** for a
  labelled-array convenience API.

## Architecture

```
src/coarsegraining_energy_fluxes/
├── geometry.py      coordinate systems (Cartesian, spherical) + planetary-Cartesian transforms
├── grids.py         structured / curvilinear / unstructured grids with land masks
├── kernels.py       filter kernels + spectral transfer Ĝ(k)
├── filtering.py     real-space footprint convolution + spectral filtering
├── derivatives.py   finite-difference stencils
├── diagnostics.py   energy flux Π, filtering spectrum, stress / Helmholtz / tracer decompositions
└── pipeline.py      high-level coarse_grain across scales
```

## Install (development)

```bash
pip install -e ".[all,dev]"     # NumPy core + Dask/xarray/scipy/matplotlib extras + dev tools
pytest
```

NumPy is the only required dependency; `dask`, `xarray`, `scipy` (spectral), and `matplotlib` (viz)
are optional extras.

## Relationship to the Julia sibling

[`CoarseGrainingEnergyFluxes.jl`](https://github.com/jbphyswx/CoarseGrainingEnergyFluxes.jl) is a
related implementation of the same physics and a useful reference (theory, conventions, and a handy
source of cross-check cases). This package does not aim to be a line-for-line port — it targets a
Pythonic design and can leverage the surrounding ecosystem (Dask, xarray, …) as it sees fit.
