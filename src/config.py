from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Пути
DATA_DIR = PROJECT_ROOT / "data"
AUDIO_FILES_DIR = PROJECT_ROOT / "data" / "raw" / "morse_dataset"
# NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
MODELS_DIR = PROJECT_ROOT / "models"

# Прочее
SEED = 777
