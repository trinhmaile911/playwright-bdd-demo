import json
from pathlib import Path


def load_test_data(file_name: str):
    path = Path("test_data") / file_name

    with open(path, encoding="utf-8") as f:
        return json.load(f)