from pathlib import Path

DATA_DIR = Path("data")
RESULTS_DIR = Path("results")
NONE_DIR = Path(".")
ALTERNATE_DIR = None
FEW_DIR = None
SOME_DIR = Path(".")
MANY_DIR = Path(".")

script_paths = {
    "none": NONE_DIR,
    "few": FEW_DIR,
    "some": SOME_DIR,
    "many": MANY_DIR,
}