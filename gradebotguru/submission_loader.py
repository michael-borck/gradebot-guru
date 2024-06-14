import os
from typing import Dict, List


def load_submissions(directory: str) -> Dict[str, str]:
    """
    Load and parse student submissions from a directory.

    Args:
        directory (str): Path to the directory containing submissions.

    Returns:
        Dict[str, str]: A dictionary where keys are filenames and values are the content of the submissions.
    """
    submissions = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                submissions[filename] = file.read()
    return submissions
