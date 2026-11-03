# Reintroduction analysis

Code and simulation data for Thomas F. Johnson, Alain Danet, Toby Hänfling and Andrew P. Beckerman, *Reintroductions can backfire by destabilising food webs and triggering further extinction cascades*. Related preprint: [10.1101/2025.08.28.672799](https://doi.org/10.1101/2025.08.28.672799).

## Current analysis: v0.4

- [Annotated R Markdown source](reintrov_0.4.Rmd)
- [Executed PDF report](reintrov_0.4.pdf)
- [Executed Markdown report](reintrov_0.4.md)
- [Change log and interpretation notes](CHANGELOG_v0.4.md)

Version 0.4 fits eleven models: the nine formulas from v0.3 plus two newly reconstructed evenness models. It rebuilds the three manuscript figure layouts, corrects reversed scenario labels, handles zero predator biomass explicitly, reports model sample sizes, and propagates uncertainty through sequential community comparisons using a paired bootstrap. These changes can alter numerical predictions; the reconstructed evenness panels should be reviewed before replacing historical manuscript images.

## Reproduce

Place `sim.Rdata` beside `reintrov_0.4.Rmd`. Install R packages `rmarkdown`, `knitr`, `mgcv`, `ggplot2` and `patchwork`. Rendering uses Pandoc; PDF additionally needs LaTeX, for example TinyTeX.

```r
rmarkdown::render("reintrov_0.4.Rmd", output_format = "pdf_document",
                  output_options = list(keep_md = TRUE))
```

For a matching rerender, optionally extract `results_v0.4.zip` beside the Rmd first; it contains the completed, provenance-checked bootstrap cache.

The default runs 200 paired resamples using four workers on macOS/Linux (one on Windows). Results and provenance-checked checkpoints are written to `results_v0.4`. Matching subsequent renders reuse completed bootstrap replicates. Set `params = list(reuse_bootstrap = FALSE)` to recompute, or change `bootstrap_replicates`, `bootstrap_workers` and `seed` explicitly. The source does not install packages or download data.

The root-level figure PDFs/PNGs and CSV tables are published copies of the corresponding `results_v0.4` outputs. The Markdown report uses those root-level PNGs for GitHub display. Fitted-model RDS files are generated locally rather than committed; all fits are reproducible from the source and archived input.

## Data and provenance

The input `sim.Rdata` contains `sim_tom_ok`, 69,895 rows and 32 columns. The inherited v0.3 filters retain 10,969 unique baseline trajectories. See [data documentation](DATA_README.md), [column definitions](DATA_DICTIONARY.csv), and the executed report for exclusions and model-specific sample sizes.

Additional Arrow files preserve historical scenario experiments. A source snapshot of the Julia simulation repository is included at commit `125888592b61cc0b8c5329d8dc756646d6c30680`; upstream development is at [BecksLab/rewilding2023](https://github.com/BecksLab/rewilding2023). No new Julia simulations were generated for v0.4, and the precise historical source revision that generated each data file remains unverified.

The original v0.3 source and PDF remain available for comparison. Version 1.0.0 of the archive is preserved at [10.5281/zenodo.23913924](https://doi.org/10.5281/zenodo.23913924); later releases are separately versioned by Zenodo.

## Publish the executed Markdown

After rendering, run `python3 prepare_github_report.py`. This copies compact outputs to `publish_v0.4`, converts PDF-specific figure markup into Markdown images, checks every image link, and creates `results_v0.4.zip`. It does not refit models or upload anything.
