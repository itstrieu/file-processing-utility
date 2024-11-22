import pandas as pd
import os


def load_file(file_path):
    """Load a file and return its contents."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")

    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.csv':
        return pd.read_csv(file_path)
    elif file_extension == '.json':
        return pd.read_json(file_path)
    elif file_extension == '.txt':
        with open(file_path, 'r') as file:
            return file.readlines()
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")
