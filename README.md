# Astro Planner - MVP

This is an initial skeleton for *Astro Planner* — a Streamlit-based web dashboard that helps pick astrophotography targets
based on your equipment, local horizon, catalogs (Messier/NGC/IC), and moon conditions.

This repository contains:
TBD

## Quick Start (end user)
1. Install latest release
pip install astro-planner

2. Run (opens browser at http://localhost:8501)
astro-planner

## Developer Setup (From Git Repo)

### Clone and Run

git clone <your-repo> astro-planner
cd astro-planner

### Install dependencies + editable developer install
uv sync --dev

### Run app (opens browser)
uv run astro-planner

### Project Structure

.
├── pyproject.toml
├── README.md
├── src
    ├── astro_planner
      ├── altaz.py
      ├── catalog.py
      ├── config
      │   └── config.toml
      ├── config_loader.py
      ├── data
      │   └── NGC.csv
      ├── ephemeris.py
      ├── equipment.py
      ├── horizon
      │   ├── GSpring_horizon.txt
      │   └── horizon_sample.txt
      ├── horizon.py
      ├── __init__.py
      ├── main.py
      ├── moon.py
      ├── optics.py
      ├── paths.py
      ├── planner.py
      ├── plotting.py
      └── skyfield_data
          └── de421.bsp

### Daily Development
from repo root
uv sync --dev                    # Install deps + editable package
uv run astro-planner             # Run app

### Add Dependencies
uv add streamlit                 # Production dep (example)
uv add --dev pytest black        # Dev-only deps (example)
uv sync --dev                    # Update lockfile

### Test Changes Live
-Edit files in src/astro_planner/
-uv run astro-planner auto-reloads
-Warnings about "bare mode" are normal/harmless

### Building & Testing Distribution

#### Build Wheel
uv build                         # Creates dist/astro_planner-*.whl

### Test Global Install

#### Clean test (simulates end user)
pip uninstall astro-planner -y
pip install dist/astro_planner-*.whl
cd ~                             # Leave project dir
astro-planner                    # Should work perfectly!

#### Verify Data Bundled
unzip -l dist/astro_planner-*.whl | grep -E "(NGC.csv|de421.bsp)"
Should list your data files

#### Testing
# Run tests (add pytest to dev deps first)
uv run pytest

#### Lint
uv run black .
uv run ruff check .

#### Publishing (Optional)
Build + upload to PyPI
uv build
uv publish  # Requires twine credentials





