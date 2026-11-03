#!/usr/bin/env python3
"""Prepare a GitHub-friendly copy of an executed v0.4 PDF/Markdown report.

Run after rmarkdown::render("reintrov_0.4.Rmd") from the repository directory.
This only copies artifacts and normalises image markup/paths; it never fits
models, changes results, uploads files, or edits the original knitted report.
Usage: python3 prepare_github_report.py [analysis_directory] [staging_directory]
"""
from pathlib import Path
import re
import shutil
import sys
import zipfile

base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
stage = Path(sys.argv[2]) if len(sys.argv) > 2 else base / "publish_v0.4"
stage.mkdir(parents=True, exist_ok=True)
results = base / "results_v0.4"

# PDF-targeted knitr Markdown uses LaTeX figure wrappers. GitHub needs normal
# Markdown image links instead. Captions here are plain text, not equations.
report = (base / "reintrov_0.4.md").read_text()
image_map = {"figure-1-1": "figure_1_extirpation.png",
             "figure-2-1": "figure_2_predator.png",
             "figure-3-1": "figure_3_reintroduction.png",
             "residual-plots-1": "residual_diagnostics_v0.4.png"}
converted = []

def figure(match):
    source, caption = match.group(1), match.group(2)
    stem = Path(source).stem
    if stem not in image_map:
        raise ValueError(f"Unrecognised report figure: {source}")
    converted.append(stem)
    caption = caption.replace(r"\%", "%")
    return f"![{caption}]({image_map[stem]})\n\n{caption}"

report = re.sub(
    r"\\begin\{figure\}(?:\[[^\]]*\])?\s*\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}\s*"
    r"\\caption\{(.*?)\}\\label\{[^}]*\}\s*\\end\{figure\}",
    figure, report, flags=re.S)
residual_pattern = r"\\includegraphics(?:\[[^\]]*\])?\{[^}]*residual-plots-1\}"
report, residual_count = re.subn(residual_pattern,
    "![Pearson residual diagnostics](residual_diagnostics_v0.4.png)", report)
if set(converted) != {"figure-1-1", "figure-2-1", "figure-3-1"} or residual_count != 1:
    raise ValueError("Expected three manuscript figures and one diagnostics figure")
if r"\includegraphics" in report:
    raise ValueError("Unconverted figure markup remains")
report = report.replace(r"\clearpage", "")
(stage / "reintrov_0.4.md").write_text(report)

# Copy compact, directly viewable outputs; the large fitted-model RDS can be
# regenerated and is deliberately not uploaded through GitHub's web interface.
for name in ("reintrov_0.4.Rmd", "reintrov_0.4.pdf", "CHANGELOG_v0.4.md",
             "README.md", "DATA_README.md", ".zenodo.json"):
    shutil.copy2(base / name, stage / name)
shutil.copy2(Path(__file__), stage / Path(__file__).name)
for source in results.iterdir():
    if source.suffix in (".csv", ".pdf", ".png") or source.name == "sessionInfo.txt":
        shutil.copy2(source, stage / source.name)
diagnostic = base / "reintrov_0.4_files/figure-latex/residual-plots-1.png"
shutil.copy2(diagnostic, stage / image_map["residual-plots-1"])

# Preserve a correctly structured, compact results directory, including the
# provenance-keyed bootstrap cache. Extracting this ZIP beside the Rmd permits
# a matching rerender to reuse the completed resampling calculation.
with zipfile.ZipFile(stage / "results_v0.4.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for source in sorted(results.iterdir()):
        if source.is_file() and source.name not in ("models_v0.4.rds", "bootstrap_progress.txt"):
            archive.write(source, Path("results_v0.4") / source.name)

# Verify every published Markdown image points to a staged file.
links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", report)
if not links or not all((stage / link).is_file() for link in links):
    raise ValueError("A report image is missing from the staging directory")
print(f"Prepared {len(list(stage.iterdir()))} files in {stage.resolve()}")
