import os

BASE_PATH = r"E:\Personal\GitHub\Python Code Repo\nvidia-ml-risk-modelling"

FOLDERS = [
    "config",
    "data/raw",
    "data/processed",
    "data/external",
    "src/data",
    "src/risk",
    "src/ml",
    "src/utils",
    "src/pipelines",
    "tests"
]

FILES = [
    "README.md",
    "requirements.txt",
    "setup.py",
    "config/paths.py",
    "config/model_config.py",
    "config/risk_config.py",
    "src/data/load_data.py",
    "src/data/preprocess.py",
    "src/data/feature_engineering.py",
    "src/risk/volatility_models.py",
    "src/risk/var_cvar.py",
    "src/risk/tail_risk.py",
    "src/risk/drawdowns.py",
    "src/risk/scenario_generation.py",
    "src/ml/model_training.py",
    "src/ml/model_selection.py",
    "src/ml/risk_prediction.py",
    "src/utils/logging_utils.py",
    "src/utils/plotting.py",
    "src/utils/metrics.py",
    "src/pipelines/risk_pipeline.py",
    "src/pipelines/forecasting_pipeline.py",
    "tests/test_volatility.py",
    "tests/test_var_cvar.py",
    "tests/test_tail_risk.py",
    "tests/test_drawdowns.py",
    "tests/test_pipelines.py"
]

def create_structure():
    for folder in FOLDERS:
        folder_path = os.path.join(BASE_PATH, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

    for file in FILES:
        file_path = os.path.join(BASE_PATH, file)
        with open(file_path, "w") as f:
            f.write("")
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_structure()
