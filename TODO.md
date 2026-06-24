# TODO — coarsegraining-energy-fluxes (Python)

A NumPy / Dask / xarray toolkit for coarse-graining energy-flux diagnostics. The Julia sibling
[`CoarseGrainingEnergyFluxes.jl`](https://github.com/jbphyswx/CoarseGrainingEnergyFluxes.jl) is a
useful reference for theory/conventions and a source of cross-check cases — but this package is
designed Pythonically and free to diverge (Dask, xarray, existing libraries).

Legend: `[ ]` todo · `[~]` in progress · `[x]` done.

## P0 — Repo & tooling
- [x] Repo split out of the polyglot tree; standalone git repo.
- [x] `pyproject.toml` (hatchling, src layout, optional extras: dask / xarray / scipy / viz / dev).
- [x] Package skeleton mirroring the Julia module layout; smoke test; `.gitignore`.
- [ ] Choose + add a `LICENSE` (match the Julia sibling) and re-declare it in `pyproject.toml`.
- [ ] CI (GitHub Actions): ruff + mypy + pytest on 3.10–3.13.
- [ ] Pre-commit config (ruff format/lint).

## P1 — Test harness (do this early)
- [ ] Self-contained correctness tests: analytic/known cases (e.g. rigid rotation ⇒ Π≈0, constant
      field preserved, single Fourier/SH mode scaled by Ĝ, power-law slope recovery).
- [ ] Optional cross-check fixtures against the Julia sibling for extra confidence — a `tests/fixtures/`
      loader + parametrized `assert_allclose` helper; fixtures are git-ignored and regenerated locally.

## P2 — Core domain types (`geometry`, `grids`, `kernels`)
- [ ] `CartesianGeometry` / `SphericalGeometry`: `distance`, `area_element`, planetary-Cartesian
      transforms. Match Julia conventions (full-circle-lon periodicity auto-detect, etc.).
- [ ] `StructuredGrid` 1D/2D/3D constructors (cell measure from geometry); curvilinear / unstructured.
- [ ] Kernels: `TopHat`, `Gaussian(alpha=6|4)`, `SharpSpectral`; `kernel_weight`, `kernel_radius`,
      and the shared `spectral_transfer` (Gaussian `exp(-k²ℓ²/4α)`, sharp `1[k≤π/ℓ]`, top-hat errors).

## P3 — Real-space filtering (`filtering`, `derivatives`)
- [ ] Footprint precompute (per-latitude bands for 2D; n-D offsets for 1D/3D) + apply.
- [ ] Mask strategies: `deformable` (renormalize over wet) vs `zerofill`; periodic wrap.
- [ ] `filter_field` / `filter_fields` / `plan_filter` / `filter_apply`; plan reuse across scales.
- [ ] 2D/3D Cartesian + spherical (curvature) derivatives `ddx/ddy/ddz`.
- [ ] Validate filtered fields + derivatives against Julia fixtures.

## P4 — Diagnostics (`diagnostics`, `pipeline`)
- [ ] `compute_pi` (2D; 3D Cartesian six-term contraction); spherical planetary-Cartesian path.
- [ ] `cumulative_energy` (Eq. 15) + `filtering_spectrum` (Eq. 14, `k_ℓ = L/ℓ`).
- [ ] `tau_decomposition` (Leonard/Cross/Reynolds); `compute_pi_decomposed` (Helmholtz);
      `tracer_variance_flux`.
- [ ] `coarse_grain` + `CoarseGrainResult`.
- [ ] Test every diagnostic (Π, spectra, decompositions, rigid-rotation≈0), per the P1 harness.

## P5 — Spectral backends (optional extras)
- [ ] FFT (uniform periodic Cartesian) via `numpy.fft` / `scipy.fft`.
- [ ] NUFFT (scattered Cartesian) via a finufft binding — optional extra.
- [ ] Spherical-harmonic (uniform sphere) and scattered-spherical transforms — optional extras.
- [ ] Confirm the sharp-spectral kernel recovers the Fourier slope (Gaussian biases it).

## P6 — Backends & scaling
- [ ] Dask-array path for chunked / out-of-core batches over extra (time/depth/ensemble) dims.
- [ ] Keep the NumPy core backend-agnostic (duck-typed array ops) so Dask drops in.

## P7 — xarray convenience API
- [ ] Thin wrappers taking/returning `xarray.DataArray`/`Dataset` with labelled dims + coords;
      infer grid from coords; preserve metadata/attrs.

## P8 — Docs & examples
- [ ] README usage examples once the API works; runnable example scripts (Cartesian + spherical).
- [ ] API docs (mkdocs or sphinx); link to the Julia docs for theory.

## Notes / conventions
- Filter scale `ℓ` is the FULL filter width (Pope). Gaussian `α=6` default (Pope), `α=4` = FlowSieve.
- Sign: `Π>0` forward cascade, `Π<0` inverse. Density `ρ₀=1025` default.
- Spectral filtering assumes a homogeneous/periodic domain (no mask); use direct-sum for masked/regional.
- Pythonic snake_case naming (`compute_pi`, `coarse_grain`, …).
