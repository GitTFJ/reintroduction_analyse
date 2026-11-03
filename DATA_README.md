# Reintroduction simulation data and source archive

This release preserves the analysis-ready data and additional simulation files supplied by the authors for *Reintroductions can backfire by destabilising food webs and triggering further extinction cascades* (Johnson, Danet, Hänfling and Beckerman).

## Reproduce the analysis

The root-level `sim.Rdata` is the sole data input loaded by `reintrov_0.3.Rmd`. It is byte-identical to the previously deposited input. It contains the R data frame `sim_tom_ok`: 69,895 rows and 32 columns, with one simulation record per row. Load it with `load("sim.Rdata")`. The analysis first excludes non-finite `delta_bmp_31` (66,959 rows remain), then retains `is.na(nb_link)` (10,969 rows and unique simulation IDs remain). Individual model sample sizes can differ due to missing response/predictor values. Install the packages listed in the R Markdown setup before rendering. The v0.4 statistical models are rerun from this input; the historical Julia food-web simulations are not rerun.

## Additional files

- `fw_C_S.arrow`, `fw_Z.arrow`, `fw_B.arrow`, `fw_G.arrow`: network inputs for the historical connectance/richness, body-mass-ratio, release-biomass and diet-breadth experiments respectively.
- `simCS.arrow`, `simZ.arrow`, `simB.arrow`, `simG.arrow`: corresponding historical simulation outputs. These are supplied for preservation; the current R analysis loads `sim.Rdata`, not these Arrow files directly. Their presence is not evidence that sensitivity analyses were included in the manuscript.
- `simulation-source-1258885.zip`: unmodified source snapshot from https://github.com/BecksLab/rewilding2023 at commit `125888592b61cc0b8c5329d8dc756646d6c30680`. Its own project, documentation and licensing information are preserved within the archive.
- `DATA_DICTIONARY.csv`: column definitions for `sim_tom_ok`.
- `SHA256SUMS.txt`: checksums for data and the simulation-source snapshot.

## Interpretation and provenance

Phase suffixes 1, 2 and 3 denote intact, extirpated and reintroduced communities. Ratio suffixes 21, 32 and 31 denote phase 2 / phase 1, phase 3 / phase 2 and phase 3 / phase 1 respectively. The data are theoretical simulation outputs, not field observations. Model time is not calibrated to years or generations.

The supplied main Julia script currently specifies a 2,000-unit burn-in and 500-unit measurement window, with an extinction threshold of 1e-5; its equilibrium-termination callback is commented out. This release preserves the source as found, but does not independently establish the exact source revision that generated every historical data file. The historical v0.3 script defines nine statistical models. Version 0.4 adds two newly reconstructed evenness models and provides an executed analysis report and rebuilt figures. It preserves the nine original formulas, makes predator-response eligibility explicit, corrects reversed scenario labels, and propagates uncertainty through sequential community comparisons. These are fresh estimates, not recovered historical evenness outputs; review the report and CHANGELOG_v0.4.md before updating manuscript figures. No new Julia simulations were generated.

Code in the analysis repository retains its existing MIT licence. Upstream source retains its own notices. The supplied simulation files contain no human-subject or field-observation data.
