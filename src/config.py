from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Пути
DATA_DIR = PROJECT_ROOT / "data"
AUDIO_FILES_DIR = PROJECT_ROOT / "data" / "raw" / "morse_dataset"
MODELS_DIR = PROJECT_ROOT / "models"

EXPERIMENT_NAME = "Morse_Decoding"
MODELS_INFO_PATH = PROJECT_ROOT / "mlflow_server" / "mlartifacts" / "models_info.json"
OPTUNA_DB_PATH = PROJECT_ROOT / "mlflow_server" / "optuna" / "optuna_study.db"
STUDY_DB_URI = f"sqlite:///{OPTUNA_DB_PATH.as_posix()}"
# Прочее
SEED = 777
