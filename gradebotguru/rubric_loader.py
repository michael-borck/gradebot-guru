import csv
from typing import Dict


def load_rubric(file_path: str) -> Dict[str, float]:
    """
    Load and parse a grading rubric from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing the rubric.

    Returns:
        Dict[str, float]: A dictionary where keys are criteria and values are weights.
    """
    rubric = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            criterion = row['criterion']
            weight = float(row['weight'])
            rubric[criterion] = weight
    return rubric
