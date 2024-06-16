import pytest
from pytest_mock import MockerFixture
from gradebotguru.rubric_loader import load_rubric

def test_load_rubric_with_description(mocker: MockerFixture) -> None:
    """
    Test loading and parsing a rubric from a CSV file with descriptions.

    Mocks the presence of a CSV file and checks if `load_rubric`
    correctly reads and parses the file.
    """
    mock_csv_content = "criterion,description,max_points\nContent,Quality and relevance of content.,10\nClarity,Clarity of expression and organization.,5\nGrammar,Proper use of grammar and syntax.,5\n"
    mocker.patch('builtins.open', mocker.mock_open(read_data=mock_csv_content))

    rubric = load_rubric('path/to/rubric.csv')
    expected_rubric = {
        'Content': {"description": "Quality and relevance of content.", "max_points": 10},
        'Clarity': {"description": "Clarity of expression and organization.", "max_points": 5},
        'Grammar': {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }
    assert rubric == expected_rubric

def test_load_rubric_without_description(mocker: MockerFixture) -> None:
    """
    Test loading and parsing a rubric from a CSV file without descriptions.

    Mocks the presence of a CSV file and checks if `load_rubric`
    correctly reads and parses the file.
    """
    mock_csv_content = "criterion,max_points\nContent,10\nClarity,5\nGrammar,5\n"
    mocker.patch('builtins.open', mocker.mock_open(read_data=mock_csv_content))

    rubric = load_rubric('path/to/rubric.csv')
    expected_rubric = {
        'Content': {"description": "", "max_points": 10},
        'Clarity': {"description": "", "max_points": 5},
        'Grammar': {"description": "", "max_points": 5}
    }
    assert rubric == expected_rubric
