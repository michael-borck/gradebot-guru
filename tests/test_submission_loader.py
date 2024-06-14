import os
import pytest
from pytest_mock import MockerFixture
from typing import List
from gradebotguru.submission_loader import load_submissions

def test_load_submissions(mocker: MockerFixture) -> None:
    """
    Test loading and parsing submissions from a directory.

    Mocks the presence of files in a directory and checks if `load_submissions`
    correctly reads and parses the files.
    """
    mock_files = {
        'submission1.txt': 'This is the content of submission 1.',
        'submission2.txt': 'This is the content of submission 2.'
    }

    def mock_listdir(directory: str) -> List[str]:
        return list(mock_files.keys())

    def mock_isfile(path: str) -> bool:
        return path.split(os.sep)[-1] in mock_files

    def mock_open_func(filepath: str, mode: str = 'r', encoding: str = None):
        filename = filepath.split(os.sep)[-1]
        if filename in mock_files:
            return mocker.mock_open(read_data=mock_files[filename]).return_value
        raise FileNotFoundError

    mocker.patch('os.listdir', mock_listdir)
    mocker.patch('os.path.isfile', mock_isfile)
    mocker.patch('builtins.open', mock_open_func)

    submissions = load_submissions('path/to/submissions')
    assert submissions == mock_files
