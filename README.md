# Predator reintroduction analysis — v0.4

This code fits the statistical models and reports the results in R for *Reintroductions can backfire by destabilising food webs and triggering further extinction cascades*. For the Julia simulation code and data, see [julia/](julia/).

To read the results, download [reintrov_0.4.html](reintrov_0.4.html) and open it in your browser.

To run the analysis, download the repository, open [reintrov_0.4.Rmd](reintrov_0.4.Rmd) in RStudio and click **Knit to HTML**. The R input is [data/sim.Rdata](data/sim.Rdata); column definitions are in [data/DATA_DICTIONARY.csv](data/DATA_DICTIONARY.csv).

Install the required packages once:

```r
install.packages(c("rmarkdown", "knitr", "mgcv", "ggplot2", "patchwork", "ggeffects", "ggpubr"))
```

Then run:

```r
rmarkdown::render("reintrov_0.4.Rmd")
```
