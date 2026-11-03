# Predator reintroduction analysis — v0.4

Analysis and results for *Reintroductions can backfire by destabilising food webs and triggering further extinction cascades*.

- **Read the results:** download [reintrov_0.4.html](reintrov_0.4.html) and open it in your browser. It includes instructions, all three manuscript figures, marginal-effect plots for all eleven models, model summaries and diagnostics. GitHub displays HTML source rather than the rendered page.
- **Run the analysis:** download this repository, open [reintrov_0.4.Rmd](reintrov_0.4.Rmd) in RStudio, and click **Knit to HTML**. Installation and rerun instructions are at the start of the report.
- **Input data:** [data/sim.Rdata](data/sim.Rdata), with [column definitions](data/DATA_DICTIONARY.csv).
- **Julia simulation source:** [julia/](julia/), with the original simulation scripts, bundled model source and project files. [Source provenance and the Julia–R workflow](julia/PROVENANCE.md) explain how these relate to the supplied analysis data.

```text
reintrov_0.4.Rmd     annotated analysis and instructions
reintrov_0.4.html    complete results, with embedded figures
data/               simulation input and column definitions
results/            bootstrap checkpoint; generated outputs go here
julia/              preserved Julia simulation source and provenance
```

Install `rmarkdown`, `knitr`, `mgcv`, `ggplot2`, `patchwork`, `ggeffects` and `ggpubr` once. From the repository folder:

```r
rmarkdown::render("reintrov_0.4.Rmd")
```

The supplied checkpoint saves recomputing 200 bootstrap fits when its provenance checks match. A full recomputation can take tens of minutes.
