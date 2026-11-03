# Julia simulation source

This folder preserves the complete source snapshot from [BecksLab/rewilding2023](https://github.com/BecksLab/rewilding2023/tree/125888592b61cc0b8c5329d8dc756646d6c30680), commit `125888592b61cc0b8c5329d8dc756646d6c30680`. It is the same snapshot included in the original v1.0.0 archive. All 113 upstream files are retained unchanged, including the bundled EcologicalNetworksDynamics source, documentation and tests. This provenance note is the only added file within this folder.

## How the Julia and R components connect

The Julia scripts generate food webs and simulate the intact, predator-extirpated and predator-reintroduced phases. They write Arrow outputs containing species biomass, richness, stability and food-web measurements. The current R analysis uses the supplied analysis-ready `../data/sim.Rdata` and reproduces the statistical results and figures in `../reintrov_0.4.html`.

| Location | Purpose |
| --- | --- |
| `script/00_generate_foodweb.jl` | Generate food webs and simulation parameters |
| `script/01_sim.jl` | Run the sequential intact–extirpated–reintroduced simulation |
| `script/01_connectance_richness.jl` | Connectance and richness experiment |
| `script/02_Z_predator.jl` | Predator–prey mass-ratio experiment |
| `script/03_propagule_size.jl` | Reintroduction propagule-size experiment |
| `script/04_generality.jl` | Predator diet-breadth experiment |
| `src/` | Food-web construction, simulation and measurement functions, and bundled model package |
| `Project.toml` | Julia dependencies |
| `00_prep_analysis.Rmd`, `_targets.Rmd`, `report/` | Original R preparation and reporting code |
| `job/` | Original cluster job script |

## Working with the simulation source

Start with the original [README](README.md) and the experiment scripts listed above. The scripts use paths such as `~/rewilding2023/`, relative `../src/` includes and experiment-specific Arrow inputs. Set these paths and worker counts for your machine, and run the scripts from the `script/` directory with the Julia project in this folder. `01_sim.jl` also takes the first and last simulation indices as command-line arguments. The original Arrow inputs and additional outputs are available in the [v1.0.0 archive](https://doi.org/10.5281/zenodo.23913924).

The snapshot has a `Project.toml` but no Julia `Manifest.toml`. It contains a development copy of EcologicalNetworksDynamics under `src/EcologicalNetworksDynamics.jl-dev/`; dependency resolution and the package path should be checked before a new simulation run.

## Provenance limits

This is a preserved source snapshot, not a newly executed Julia simulation run. The exact source revision and dependency environment that generated every historical simulation file have not been independently established. The original preparation scripts are included, but a complete automated conversion from the historical Arrow outputs to the supplied `sim.Rdata` has not been verified. The supplied R input remains the starting point for reproducing the manuscript's current statistical analysis.

Upstream files, notices and attribution are preserved verbatim.
