# Astro Planner - MVP

This is an initial skeleton for *Astro Planner* — a Streamlit-based web dashboard that helps pick astrophotography targets
based on your equipment, local horizon, catalogs (Messier/NGC/IC), and moon conditions.

This repository contains:
TBD

## Quick Start (end user)
1. Install latest release <br>
pip install astro-planner <br>

2. Run (opens browser at http://localhost:8501) <br>
astro-planner

## Developer Setup (From Git Repo)

### Clone and Run

git clone <your-repo> astro-planner <br>
cd astro-planner

### Install dependencies + editable developer install
uv sync --dev

### Run app (opens browser)
uv run astro-planner

### Daily Development
from repo root <br>
uv sync --dev                    # Install deps + editable package <br>
uv run astro-planner             # Run app <br>

### Add Dependencies
uv add streamlit                 # Production dep (example) <br>
uv add --dev pytest black        # Dev-only deps (example) <br>
uv sync --dev                    # Update lockfile <br>

### Test Changes Live
-Edit files in src/astro_planner/ <br>
-uv run astro-planner auto-reloads <br>
-Warnings about "bare mode" are normal/harmless <br>

### Building & Testing Distribution

#### Build Wheel
uv build                         # Creates dist/astro_planner-*.whl

### Test Global Install

#### Clean test (simulates end user)
pip uninstall astro-planner -y <br>
pip install dist/astro_planner-*.whl <br>
cd ~                             # Leave project dir <br>
astro-planner                    # Should work perfectly! <br>

#### Verify Data Bundled
unzip -l dist/astro_planner-*.whl | grep -E "(NGC.csv|de421.bsp)" <br>
Should list your data files <br>

#### Testing
Run tests (add pytest to dev deps first) <br>
uv run pytest <br>

#### Lint
uv run black . <br>
uv run ruff check . <br>

#### Publishing (Optional)
Build + upload to PyPI <br>
uv build <br>
uv publish  # Requires twine credentials <br>





