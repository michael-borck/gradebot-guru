import csv
from typing import Any


def load_rubric(file_path: str) -> dict[str, dict[str, Any]]:
    """
    Load and parse a grading rubric from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing the rubric.

    Returns:
        Dict[str, Dict[str, Any]]: A dictionary where keys are criteria and values are dictionaries with descriptions and max points.

    Examples:
        >>> csv_content = '''criterion,description,max_points
        ... Clarity,Clarity of expression and organization.,5
        ... Organization,Quality and structure of content.,10
        ... Evidence,Support and relevance of arguments.,5
        ... '''
        >>> with open('temp_rubric.csv', 'w') as f:
        ...     _ = f.write(csv_content)
        >>> rubric = load_rubric('temp_rubric.csv')
        >>> rubric
        {'Clarity': {'description': 'Clarity of expression and organization.', 'max_points': 5},\
 'Organization': {'description': 'Quality and structure of content.', 'max_points': 10},\
 'Evidence': {'description': 'Support and relevance of arguments.', 'max_points': 5}}
        >>> import os; os.remove('temp_rubric.csv')

        >>> csv_content = '''criterion,max_points
        ... Clarity,5
        ... Organization,10
        ... Evidence,5
        ... '''
        >>> with open('temp_rubric.csv', 'w') as f:
        ...     _ = f.write(csv_content)
        >>> rubric = load_rubric('temp_rubric.csv')
        >>> rubric
        {'Clarity': {'description': '', 'max_points': 5},\
 'Organization': {'description': '', 'max_points': 10},\
 'Evidence': {'description': '', 'max_points': 5}}
        >>> import os; os.remove('temp_rubric.csv')
    """
    rubric = {}
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            criterion = row["criterion"].strip()
            description = (
                row.get("description") or ""
            ).strip()  # Handle missing description
            max_points = row["max_points"].strip() if row["max_points"] else None
            rubric[criterion] = {
                "description": description,
                "max_points": int(max_points) if max_points else 0,
            }
    return rubric
