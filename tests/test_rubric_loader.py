import pytest
from pytest_mock import MockerFixture
from gradebotguru.rubric_loader import load_rubric


def test_load_rubric(mocker: MockerFixture) -> None:
    """
    Test loading and parsing a rubric from a CSV file.

    Mocks the presence of a CSV file and checks if `load_rubric`
    correctly reads and parses the file.
    """
    mock_csv_content = "criterion,weight\ncontent,0.4\nstructure,0.3\ngrammar,0.3\n"
    mocker.patch('builtins.open', mocker.mock_open(read_data=mock_csv_content))

    rubric = load_rubric('path/to/rubric.csv')
    expected_rubric = {
        'content': 0.4,
        'structure': 0.3,
        'grammar': 0.3
    }
    assert rubric == expected_rubric
