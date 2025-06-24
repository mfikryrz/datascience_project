import os
from tabnanny import verbose
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty or not in the correct format.")
    except yaml.YAMLError as e:
        raise e


@ensure_annotations
def create_directories(paths: list, verbose=True):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        data = json.load(f)
    
    logger.info(f"JSON file loaded from {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(path: Path, data: Any):
    joblib.dump(data, path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data


"""
Import Analysis:
pythonimport os                           # Operasi sistem operasi
import yaml                         # Parse YAML files
from src.datascience import logger  # Logger yang sudah kita bahas sebelumnya
import json                         # Handle JSON files
import joblib                       # Serialize/deserialize Python objects (terutama ML models)
from ensure import ensure_annotations  # Type checking decorator
from box import ConfigBox           # Advanced dictionary dengan dot notation
from pathlib import Path            # Modern path handling
from typing import Any              # Type hints
from box.exceptions import BoxValueError  # Exception handling untuk ConfigBox
Penjelasan Function read_yaml:
1. Decorator @ensure_annotations
python@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

@ensure_annotations: Memastikan tipe data input/output sesuai dengan type hints
path_to_yaml: Path: Parameter input harus bertipe pathlib.Path
-> ConfigBox: Function mengembalikan object bertipe ConfigBox

2. Function Body
pythontry:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f"YAML file {path_to_yaml} read successfully.")
        return ConfigBox(content)
Step by step:

with open(path_to_yaml): Context manager untuk membuka file YAML
yaml.safe_load(yaml_file): Parse YAML content ke Python dictionary

safe_load lebih aman dari load karena tidak execute arbitrary code


logger.info(...): Log success message
ConfigBox(content): Convert dictionary ke ConfigBox object

3. Exception Handling
pythonexcept BoxValueError:
    raise ValueError("yaml file is empty or not in the correct format.")
except yaml.YAMLError as e:
    raise e

BoxValueError: Error saat ConfigBox tidak bisa dibuat (file kosong/format salah)
yaml.YAMLError: Error saat parsing YAML (syntax error, dll)
"""