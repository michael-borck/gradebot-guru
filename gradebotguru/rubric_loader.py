import csv
from typing import Dict
from io import StringIO


def load_rubric(file_path: str | StringIO) -> Dict[str, float]:
    """
    Load and parse a grading rubric from a CSV file or StringIO object.

    Args:
        file_path (str | StringIO): Path to the CSV file or StringIO object containing the rubric.

    Returns:
        Dict[str, float]: A dictionary where keys are criteria and values are weights.

    Examples:
        >>> csv_content = '''criterion,weight
        ... Clarity,0.3
        ... Organization,0.4
        ... Evidence,0.3
        ... '''
        >>> with StringIO(csv_content) as f:
        ...     rubric = load_rubric(f)
        >>> rubric
        {'Clarity': 0.3, 'Organization': 0.4, 'Evidence': 0.3}
    """
    rubric = {}
    with file_path as file:  # Use the passed object directly
        reader = csv.DictReader(file)
        for row in reader:
            criterion = row['criterion']
            weight = float(row['weight'])
            rubric[criterion] = weight
    return rubric
