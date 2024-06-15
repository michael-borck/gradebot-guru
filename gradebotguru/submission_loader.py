import os
from typing import Dict


def load_submissions(directory: str) -> Dict[str, str]:
    """
    Load and parse student submissions from a directory.

    Args:
        directory (str): Path to the directory containing submissions.

    Returns:
        Dict[str, str]: A dictionary where keys are filenames and values are the content of the submissions.

    Examples:
        >>> import tempfile
        >>> import os
        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     file1_path = os.path.join(tmpdir, 'submission1.txt')
        ...     file2_path = os.path.join(tmpdir, 'submission2.txt')
        ...     with open(file1_path, 'w', encoding='utf-8') as f1:
        ...         _ = f1.write('Content of submission 1')
        ...     with open(file2_path, 'w', encoding='utf-8') as f2:
        ...         _ = f2.write('Content of submission 2')
        ...     submissions = load_submissions(tmpdir)
        >>> submissions == {
        ...     'submission1.txt': 'Content of submission 1',
        ...     'submission2.txt': 'Content of submission 2'
        ... }
        True
    """
    submissions = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                submissions[filename] = file.read()
    return submissions
