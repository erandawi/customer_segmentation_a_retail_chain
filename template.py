from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "customer_segmentation_a_retail_chain"

list_of_files = [
    ".github/workflows/main.yaml",
    "config/params.yaml",
    "config/mlflow_config.yaml",
    "data_schema/schema.yaml",
    "final_models/.gitkeep",
    "data/.gitkeep",
    "reports/eda/.gitkeep",
    "dvc.yaml",
    ".dvc/config",

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/clustering_metrics.py",

    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/constant/training_pipeline/__init__.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/exception/exception.py",

    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/logger.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/segment_customers.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/main_utils/__init__.py",
    f"src/{project_name}/utils/utils.py",
    f"src/{project_name}/utils/ml_utils/__init__.py",
    f"src/{project_name}/utils/ml_utils/metric/__init__.py",
    f"src/{project_name}/utils/ml_utils/metric/clustering_metric.py",
    f"src/{project_name}/utils/ml_utils/mlflow_utils.py",

    f"src/{project_name}/utils/model/__init__.py",
    f"src/{project_name}/utils/model/estimator.py",

    f"src/{project_name}/notebooks/experiments.ipynb",
    f"src/{project_name}/prediction_output/.gitkeep",
    f"src/{project_name}/valid_data/.gitkeep",

    "app/serve.py",
    "Dockerfile",
    "main.py",
    "push_data.py",
    "README.md",
    "requirements.txt",
    "test_mongodb.py",
    "test.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
