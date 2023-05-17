import os
from typing import Iterator


def get_all_files(directory: str) -> Iterator[str]:
    if not os.path.isdir(directory):
        raise ValueError(f"Error: {directory} is not a valid directory.")
    for root, _, files in os.walk(directory):
        for name in files:
            yield(os.path.join(root, name))