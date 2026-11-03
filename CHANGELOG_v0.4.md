# Analysis v0.4 changes

- Preserve `reintrov_0.3.Rmd` and its nine original model formulas.
- Add m10/m11 for log evenness ratios at the extirpation and reintroduction transitions, using the community-model predictors specified in the manuscript.
- Explicitly restrict predator biomass and stability models to established predators with valid positive responses. This prevents log(0) and reports exclusions.
- Rebuild Figures 1-3 in the manuscript layout, including the fourth (evenness) community row, shared scenario colours, illustrative intact references and the post-extirpation/post-reintroduction circle/square comparison.
- Correct inverted Short/Tall trophic-height and High/Low survival labels. Use caption scenario values explicitly rather than changing quantiles.
- Propagate uncertainty in sequential community comparisons by paired case bootstrap, with deterministic seeds, saved checkpoints and a provenance-checked cache.
- Report model sample sizes, coefficients, convergence diagnostics, predictor profiles and predictions; explain geometric back-transforms, boundary proportions and inherited cohort filtering.
- Newly reconstructed evenness estimates and corrected labels can differ from old manuscript images. No historical values were reverse-engineered or forced to match.
- No new Julia simulations are generated. The exact historical simulation-code revision remains unverified.

The source is fully annotated. The PDF/Markdown reports are executed results, not handwritten summaries. The original data files are unchanged.
