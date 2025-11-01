# Google Code Golf 2025 — ARC Auto Solver & DSL Pipeline

> For **Kaggle: Google Code Golf 2025** with an extensible ARC mini-DSL, auto-solver, one-click pipeline, and reporting.

[![CI](https://img.shields.io/github/actions/workflow/status/USER/REPO/ci.yml?branch=main)](https://github.com/USER/REPO/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Python-3.11-blue.svg)](#)

## ✨ Features
- **Mini-DSL for ARC**: rotations, flips, diagonals, shifts, rolls, padding, recolor.
- **Auto Solver**: search shortest op-sequence for each task.
- **One-Click Pipeline**: `python -m code_golf.tools.pipeline_run` to solve + chart.
- **Kaggle-Ready**: drop-in zip; tested in Kaggle Notebook.
- **GitHub-Ready**: CI, issue/PR templates, Code of Conduct, CONTRIBUTING, MIT license.

## 🚀 Quickstart
```bash
# 1) Create & activate env
uv venv && source .venv/bin/activate  # or: python -m venv .venv && source .venv/bin/activate
pip install -U -r requirements.txt

# 2) Run the pipeline (local)
python -m code_golf.tools.pipeline_run
or 
python tools/pipeline_run.py

# 3) Results
# - reports/auto_summary.csv
# - reports/charts/success.png, length.png, example_*.png
```

## 🧪 Kaggle Notebook
Upload the release zip (see below) and run:
```bash
!unzip code_golf_release.zip -d /kaggle/working/
!python /kaggle/working/code_golf/tools/pipeline_run.py
```

## 🧩 Repo Layout
```
src/code_golf/
  dsl/               # mini-DSL operators
  tools/             # auto solver & pipeline
tasks/               # ARC-like tasks (json)
reports/             # outputs (csv, charts)
solutions_auto/      # generated solutions
notebooks/           # viz & experiments
```

## 🔧 Customize
- Add tasks under `tasks/*.json` (ARC format).
- Add new primitives in `src/code_golf/dsl/core.py` and include in `PRIMITIVES`.
- Tune search depth in `auto_arc_solver.py`.

## 🧰 Developer Guide
```bash
# lint & format
ruff check .
black src tests

# run tests
pytest -q
```

## 📦 Release (Kaggle-ready ZIP)
```bash
# Produces code_golf_release.zip
python scripts/make_release_zip.py
```

## 🗺️ Roadmap
- [ ] Param search for (shift dx/dy, recolor a→b)
- [ ] Symmetry detection (axes, anti-diagonal, repetition)
- [ ] Genetic code-golfing
- [ ] Streamlit dashboard
- [ ] LLM+DSL hybrid

## 📜 Citation
If you use this template, please cite:
```text
Li, Y. (2025). Google Code Golf 2025 — ARC DSL Auto Solver. GitHub repository.
```

## 🪪 License
MIT © Yuan Li
