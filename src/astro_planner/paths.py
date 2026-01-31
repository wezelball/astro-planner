# src/astro_planner/paths.py

from pathlib import Path
import os
import astro_planner

def get_project_root():
    """Heuristic to find project root: src/astro_planner → astro_planner/"""
    current_dir = Path(__file__).parent
    src_dir = current_dir.parent
    project_root = src_dir.parent
    return project_root

#ROOT_DIR = get_project_root()
ROOT_DIR = os.path.dirname(astro_planner.__file__)

# User data / config: live in your workdir
DATA_DIR = Path(os.path.dirname(astro_planner.__file__)) / "data"  # Path object
# should be DATA_DIR = ROOT_DIR / "DATA"
CONFIG_DIR = Path(os.path.dirname(astro_planner.__file__)) / "config"  # Path object
HORIZON_DIR = Path(os.path.dirname(astro_planner.__file__)) / "horizon"  # Path object
SKYFIELD_DIR = Path(os.path.dirname(astro_planner.__file__)) / "skyfield_data"  # Path object

if __name__ == "__main__":
    print("Package directory:", Path(__file__).parent)
    print("Project root     :", ROOT_DIR)
    print("Data dir         :", DATA_DIR)
    print("Config dir       :", CONFIG_DIR)
    print("SKYFIELD dir     :", SKYFIELD_DIR)
    print("Data files:", list(DATA_DIR.glob("*.csv")))
